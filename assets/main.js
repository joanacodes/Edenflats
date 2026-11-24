// Menu mobile, en-tête au défilement, rail des quartiers, apparition des blocs, bouton de contact,
// bandeau cookies et proposition de changer de langue.
document.documentElement.classList.remove('no-js');

// Le stockage local peut être refusé (navigation privée, réglages) : le site doit marcher sans lui.
const store = {
  get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* choix non mémorisé, sans conséquence */ } },
};

const burger = document.querySelector('.burger');
const nav = document.getElementById('menu');
if (burger && nav) {
  burger.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', String(open));
  });
  // Échap referme le menu : sans cela, il reste ouvert par-dessus la page au clavier.
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      nav.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
      burger.focus();
    }
  });
}

// « top » est déjà un nom réservé du navigateur (window.top) : l'en-tête s'appelle donc « entete ».
const entete = document.querySelector('.top');
const bulle = document.querySelector('.bubble');
const hautDePage = document.querySelector('.hero-panel, .phead-panel');
const finDePage = document.querySelector('.final') || document.querySelector('.foot');
let attente = false;
function auDefilement() {
  attente = false;
  if (entete) entete.classList.toggle('scrolled', window.scrollY > 8);
  if (bulle) {
    // Le bouton arrive une fois le haut de page passé et repart quand l'appel final ou le pied de page entre à
    // l'écran : ils ont déjà leurs boutons de contact, et le bouton masquerait leur dernière ligne.
    const passe = hautDePage ? hautDePage.getBoundingClientRect().bottom < 80 : window.scrollY > 400;
    const fin = finDePage ? finDePage.getBoundingClientRect().top < window.innerHeight : false;
    bulle.classList.toggle('in', passe && !fin);
  }
}
const surDefilement = () => { if (!attente) { attente = true; requestAnimationFrame(auDefilement); } };
window.addEventListener('scroll', surDefilement, { passive: true });
window.addEventListener('resize', surDefilement);
auDefilement();

// Les flèches font défiler le rail d'une carte et demie ; sans JavaScript, le rail défile au doigt.
document.querySelectorAll('[data-rail]').forEach((box) => {
  const rail = box.querySelector('.rail');
  const step = () => (rail.firstElementChild?.offsetWidth || 260) * 1.5;
  box.querySelector('.prev')?.addEventListener('click', () => rail.scrollBy({ left: -step() }));
  box.querySelector('.next')?.addEventListener('click', () => rail.scrollBy({ left: step() }));
});

const items = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }
  }, { rootMargin: '0px 0px -8% 0px' });
  items.forEach((el) => io.observe(el));
} else {
  items.forEach((el) => el.classList.add('in'));
}

// Les fenêtres (bandeau, proposition de langue) viennent d'un <template> : leur texte n'est pas lu comme
// contenu de la page par les moteurs de recherche. On les place juste après le lien d'évitement, pour
// qu'au clavier on les atteigne tout de suite.
function poser(id) {
  const tpl = document.getElementById(id);
  if (!tpl) return null;
  const el = tpl.content.firstElementChild.cloneNode(true);
  const skip = document.querySelector('.skip');
  if (skip) skip.after(el); else document.body.prepend(el);
  requestAnimationFrame(() => requestAnimationFrame(() => el.classList.add('in')));
  return el;
}
function retirer(el, apres) {
  el.classList.remove('in');
  setTimeout(() => { el.remove(); if (apres) apres(); }, 450);
}

// ── Cookies ──────────────────────────────────────────────────────────────────
// Rien n'est déposé avant « Accepter ». Le choix est gardé six mois (durée conseillée par la CNIL) avec
// l'identifiant de mesure en vigueur : si l'outil change, la question est reposée.
const CLE_COOKIES = 'ef-cookies';
const SIX_MOIS = 182 * 24 * 3600 * 1000;
const ga4 = document.body.dataset.ga4 || '';

function choixCookies() {
  try {
    const c = JSON.parse(store.get(CLE_COOKIES) || 'null');
    if (c && c.outil === ga4 && Date.now() - c.date < SIX_MOIS) return c.choix;
  } catch (e) { /* valeur illisible : on redemande */ }
  return null;
}

function chargerMesure() {
  if (!ga4 || window.gtag) return;
  window.dataLayer = window.dataLayer || [];
  window.gtag = function gtag() { window.dataLayer.push(arguments); };
  // L'accord porte sur la mesure d'audience seulement : la publicité reste refusée.
  window.gtag('consent', 'default', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'granted' });
  window.gtag('js', new Date());
  // Treize mois au plus pour les cookies de mesure, au lieu de deux ans par défaut (recommandation de la CNIL).
  window.gtag('config', ga4, { cookie_expires: 34128000 });
  const s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(ga4);
  document.head.appendChild(s);
}

// Après un refus, on efface les cookies de mesure déjà déposés (sur ce domaine et ses domaines parents).
function effacerMesure() {
  const parties = location.hostname.split('.');
  document.cookie.split(';').forEach((c) => {
    const nom = c.split('=')[0].trim();
    if (!/^_ga/.test(nom)) return;
    document.cookie = nom + '=; Max-Age=0; path=/';
    for (let i = 0; i < parties.length - 1; i++) {
      document.cookie = nom + '=; Max-Age=0; path=/; domain=.' + parties.slice(i).join('.');
    }
  });
}

let bandeau = null;
function ouvrirBandeau() {
  if (bandeau || !document.getElementById('tpl-cookies')) return;
  bandeau = poser('tpl-cookies');
  document.body.classList.add('consent-open');
  bandeau.addEventListener('click', (e) => {
    const b = e.target.closest('[data-consent]');
    if (!b) return;
    const choix = b.dataset.consent;
    store.set(CLE_COOKIES, JSON.stringify({ choix, outil: ga4, date: Date.now() }));
    const avant = window.gtag;
    if (choix === 'oui') chargerMesure();
    else { effacerMesure(); if (avant) { location.reload(); return; } }
    const el = bandeau;
    bandeau = null;
    retirer(el, () => document.body.classList.remove('consent-open'));
  });
}

// ── Langue ───────────────────────────────────────────────────────────────────
// Une page française lue par un navigateur qui n'est pas en français propose la version anglaise, et
// inversement. Jamais de redirection automatique : le visiteur choisit, et son choix n'est plus redemandé.
const CLE_LANGUE = 'ef-langue';
const langueDeLaPage = document.documentElement.lang;
const langues = (navigator.languages && navigator.languages.length) ? navigator.languages : [navigator.language || ''];
const francais = langues.some((l) => (l || '').toLowerCase().startsWith('fr'));
const proposerLangue = !!document.getElementById('tpl-langue') && !store.get(CLE_LANGUE)
  && ((langueDeLaPage === 'fr' && !francais) || (langueDeLaPage === 'en' && francais));
document.querySelectorAll('a.lang').forEach((a) => a.addEventListener('click', () => store.set(CLE_LANGUE, a.getAttribute('hreflang'))));

// Une seule question à la fois : si la langue est proposée, le bandeau cookies attend la réponse. Il s'affiche
// alors dans la langue choisie (« View in English » ouvre la page anglaise, qui le présente en anglais).
if (document.getElementById('tpl-cookies')) {
  const choix = choixCookies();
  if (choix === 'oui') chargerMesure();
  else if (choix === null && !proposerLangue) setTimeout(ouvrirBandeau, 600);
}
if (proposerLangue) {
  setTimeout(() => {
    const fenetre = poser('tpl-langue');
    if (!fenetre) return;
    fenetre.addEventListener('click', (e) => {
      const b = e.target.closest('[data-lang]');
      if (!b) return;
      store.set(CLE_LANGUE, b.dataset.lang);
      if (b.tagName === 'BUTTON') retirer(fenetre, () => { if (choixCookies() === null) ouvrirBandeau(); });
    });
  }, 1200);
}

// « Gérer les cookies » rouvre le bandeau ; le focus y va, pour qu'au clavier on n'ait pas à le chercher.
document.addEventListener('click', (e) => {
  if (!e.target.closest('[data-consent-open]')) return;
  ouvrirBandeau();
  if (bandeau) bandeau.querySelector('button').focus({ preventScroll: true });
});

