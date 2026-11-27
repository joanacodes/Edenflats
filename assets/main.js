// Thème clair ou sombre, menu des téléphones (tiroir), fenêtre de contact et son formulaire, en-tête au
// défilement, rail des quartiers, bouton de contact, bandeau cookies et proposition de changer de langue.
// Les animations sont dans motion.js.
document.documentElement.classList.remove('no-js');

// Le stockage local peut être refusé (navigation privée, réglages) : le site doit marcher sans lui.
const store = {
  get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* choix non mémorisé, sans conséquence */ } },
};
const racine = document.documentElement;
const moinsAnimer = () => matchMedia('(prefers-reduced-motion: reduce)').matches;

// ── Thème clair ou sombre ────────────────────────────────────────────────────
// Le script de <head> a posé data-theme avant le premier affichage. Le bouton garde le choix ; sans choix, le site
// suit le réglage de l'appareil, même s'il change pendant la visite (passage automatique en sombre le soir).
const CLE_THEME = 'ef-theme';
const sombreAppareil = matchMedia('(prefers-color-scheme: dark)');
const couleurBarre = document.querySelector('meta[name="theme-color"]');
function poserTheme(t) {
  racine.setAttribute('data-theme', t);
  document.querySelectorAll('[data-theme-toggle]').forEach((b) => b.setAttribute('aria-pressed', String(t === 'dark')));
  if (couleurBarre) couleurBarre.content = t === 'dark' ? '#10181D' : '#24485C';
}
poserTheme(racine.getAttribute('data-theme') === 'dark' ? 'dark' : 'light');
if (sombreAppareil.addEventListener) {
  sombreAppareil.addEventListener('change', (e) => { if (!store.get(CLE_THEME)) poserTheme(e.matches ? 'dark' : 'light'); });
}

// Le nouveau thème se répand en cercle depuis le bouton (View Transitions). Sans cette possibilité, ou quand le
// visiteur demande moins d'animations, il s'applique d'un coup.
function basculerTheme(bouton) {
  const t = racine.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  store.set(CLE_THEME, t);
  if (!document.startViewTransition || moinsAnimer()) { poserTheme(t); return; }
  const r = bouton.getBoundingClientRect();
  const x = r.left + r.width / 2;
  const y = r.top + r.height / 2;
  const rayon = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
  racine.classList.add('vt-theme');
  const vt = document.startViewTransition(() => poserTheme(t));
  vt.ready.then(() => {
    racine.animate({ clipPath: [`circle(0px at ${x}px ${y}px)`, `circle(${rayon}px at ${x}px ${y}px)`] },
      { duration: 700, easing: 'cubic-bezier(.65,0,.35,1)', pseudoElement: '::view-transition-new(root)' });
  }).catch(() => {});
  vt.finished.finally(() => racine.classList.remove('vt-theme'));
}
document.addEventListener('click', (e) => {
  const b = e.target.closest('[data-theme-toggle]');
  if (b) basculerTheme(b);
});

// ── Fenêtres : menu des téléphones et fenêtre de contact ─────────────────────
// Des <dialog> ouverts par showModal() : le navigateur garde le focus à l'intérieur, Échap les referme et le reste
// de la page devient inerte. Elles viennent d'un <template> et ne sont créées qu'à leur première ouverture.
// La fermeture est animée : on joue la sortie (classe « closing »), puis on ferme vraiment.
function creerFenetre(id) {
  const tpl = document.getElementById(id);
  if (!tpl) return null;
  const dlg = tpl.content.firstElementChild.cloneNode(true);
  document.body.appendChild(dlg);
  poserTheme(racine.getAttribute('data-theme')); // état des bascules de thème qu'elle contient
  dlg.addEventListener('cancel', (e) => { e.preventDefault(); fermer(dlg); });
  // Le panneau remplit tout le <dialog> : seul un clic sur le voile, autour, a le <dialog> lui-même pour cible.
  dlg.addEventListener('click', (e) => { if (e.target === dlg || e.target.closest('[data-close]')) fermer(dlg); });
  return dlg;
}
function ouvrir(dlg, origine) {
  if (!dlg || dlg.open) return;
  dlg.classList.remove('closing');
  dlg.retour = origine || document.activeElement;
  dlg.showModal();
  racine.classList.add('modal-open');
}
function fermer(dlg, ensuite) {
  if (!dlg || !dlg.open) { if (ensuite) ensuite(); return; }
  if (dlg.classList.contains('closing')) return;
  let fini = false;
  const fin = () => {
    if (fini) return;
    fini = true;
    dlg.classList.remove('closing');
    dlg.style.removeProperty('--drag');
    dlg.close();
    if (!document.querySelector('dialog[open]')) racine.classList.remove('modal-open');
    dlg.dispatchEvent(new Event('fermee'));
    if (ensuite) ensuite();
    else if (dlg.retour && dlg.retour.isConnected) dlg.retour.focus({ preventScroll: true });
  };
  if (moinsAnimer()) { fin(); return; }
  dlg.classList.add('closing');
  // Seule compte la fin de l'animation du <dialog> lui-même : celles de son voile et de ses liens arrivent aussi ici.
  dlg.addEventListener('animationend', function surFin(e) {
    if (e.target !== dlg || e.pseudoElement) return;
    dlg.removeEventListener('animationend', surFin);
    fin();
  });
  setTimeout(fin, 700); // filet : si l'animation ne se termine pas (onglet passé en arrière-plan), on ferme quand même
}

// ── Menu des téléphones : un tiroir qui glisse depuis la droite ──────────────
const burger = document.querySelector('.burger');
let tiroir = null;

// Sur écran tactile, le tiroir suit le doigt vers la droite et se referme s'il a été tiré assez loin.
function glisserPourFermer(dlg) {
  const panneau = dlg.querySelector('.drawer-in');
  let x0 = null;
  let y0 = 0;
  let dx = 0;
  let horizontal = null;
  panneau.addEventListener('touchstart', (e) => {
    x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; dx = 0; horizontal = null;
  }, { passive: true });
  panneau.addEventListener('touchmove', (e) => {
    if (x0 === null) return;
    const mx = e.touches[0].clientX - x0;
    const my = e.touches[0].clientY - y0;
    if (horizontal === null && (Math.abs(mx) > 8 || Math.abs(my) > 8)) horizontal = Math.abs(mx) > Math.abs(my);
    if (!horizontal) return;
    dx = Math.max(0, mx);
    dlg.classList.add('dragging');
    dlg.style.setProperty('--drag', dx + 'px');
  }, { passive: true });
  const relacher = () => {
    if (x0 === null) return;
    x0 = null;
    dlg.classList.remove('dragging');
    if (horizontal && dx > Math.min(110, panneau.offsetWidth * 0.3)) fermer(dlg);
    else dlg.style.setProperty('--drag', '0px');
  };
  panneau.addEventListener('touchend', relacher);
  panneau.addEventListener('touchcancel', relacher);
}

if (burger) {
  burger.addEventListener('click', () => {
    if (!tiroir) {
      tiroir = creerFenetre('tpl-tiroir');
      if (!tiroir) return;
      tiroir.addEventListener('fermee', () => burger.setAttribute('aria-expanded', 'false'));
      glisserPourFermer(tiroir);
    }
    ouvrir(tiroir, burger);
    burger.setAttribute('aria-expanded', 'true');
  });
  // Au-delà de 1080 px, le menu est dans l'en-tête : un tiroir resté ouvert (fenêtre agrandie) se referme.
  const large = matchMedia('(min-width: 1081px)');
  if (large.addEventListener) large.addEventListener('change', (e) => { if (e.matches && tiroir && tiroir.open) fermer(tiroir); });
}

// ── Fenêtre de contact : appel, WhatsApp et formulaire ───────────────────────
let contact = null;
function ouvrirContact(origine) {
  if (!contact) {
    contact = creerFenetre('tpl-contact');
    if (!contact) return false;
    brancherFormulaire(contact);
    // Rouverte après un envoi, la fenêtre montre de nouveau le formulaire, vide, et non le remerciement.
    contact.addEventListener('fermee', () => {
      const merci = contact.querySelector('.cdlg-done');
      if (merci && !merci.hidden) { merci.hidden = true; contact.querySelector('.cdlg-main').hidden = false; }
    });
  }
  // Depuis le tiroir : il se referme d'abord ; à la fermeture de la fenêtre, le focus revient au bouton ☰.
  if (tiroir && tiroir.open) fermer(tiroir, () => ouvrir(contact, burger));
  else ouvrir(contact, origine);
  return true;
}
document.addEventListener('click', (e) => {
  const lien = e.target.closest('[data-contact]');
  if (!lien || e.defaultPrevented) return;
  // Ctrl/Cmd-clic ou clic du milieu : le bouton reste un lien vers la page Contact, ouverte dans un nouvel onglet.
  if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
  if (ouvrirContact(lien)) e.preventDefault();
});

// Le message part en arrière-plan vers FormSubmit, qui le transmet par e-mail ; le visiteur reste sur la page. Le
// navigateur vérifie d'abord les champs obligatoires et l'adresse e-mail (l'envoi n'a lieu que s'ils sont bons).
// En cas d'échec, rien n'est effacé : le visiteur peut réessayer, ou passer par WhatsApp juste au-dessus.
function brancherFormulaire(dlg) {
  const form = dlg.querySelector('.cform');
  if (!form) return;
  const etat = form.querySelector('.cform-status');
  const bouton = form.querySelector('.cform-send');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (form.classList.contains('busy')) return;
    const donnees = Object.fromEntries(new FormData(form));
    donnees.Page = location.href;
    form.classList.add('busy');
    bouton.disabled = true;
    etat.classList.remove('err');
    etat.textContent = form.dataset.sending;
    try {
      const r = await fetch(form.dataset.ajax, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(donnees),
      });
      const j = await r.json().catch(() => ({}));
      // FormSubmit répond {"success": "true"} ; avant l'activation de l'adresse, "false" et un message qui l'explique.
      if (!r.ok || String(j.success) !== 'true') throw new Error(j.message || 'HTTP ' + r.status);
      form.reset();
      etat.textContent = '';
      dlg.querySelector('.cdlg-main').hidden = true;
      const merci = dlg.querySelector('.cdlg-done');
      merci.hidden = false;
      merci.querySelector('button').focus();
    } catch (err) {
      console.warn('Formulaire de contact :', err && err.message);
      etat.textContent = form.dataset.error;
      etat.classList.add('err');
    } finally {
      form.classList.remove('busy');
      bouton.disabled = false;
    }
  });
}

// ── En-tête et bouton de contact au défilement ───────────────────────────────
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

// Le bandeau cookies et la proposition de langue viennent d'un <template> : leur texte n'est pas lu comme contenu
// de la page par les moteurs de recherche. On les place juste après le lien d'évitement, pour qu'au clavier on les
// atteigne tout de suite.
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
const langueDeLaPage = racine.lang;
const langues = (navigator.languages && navigator.languages.length) ? navigator.languages : [navigator.language || ''];
const francais = langues.some((l) => (l || '').toLowerCase().startsWith('fr'));
const proposerLangue = !!document.getElementById('tpl-langue') && !store.get(CLE_LANGUE)
  && ((langueDeLaPage === 'fr' && !francais) || (langueDeLaPage === 'en' && francais));
// Changer de langue par l'en-tête ou par le tiroir compte comme une réponse : la question n'est plus posée.
document.addEventListener('click', (e) => {
  const a = e.target.closest('a.lang, a[data-lang-switch]');
  if (a) store.set(CLE_LANGUE, a.getAttribute('hreflang'));
});

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
