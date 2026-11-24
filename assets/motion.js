// Animations du site. Le script de <head> pose html.m-on, sauf si le visiteur a demandé moins d'animations dans les
// réglages de son appareil : dans ce cas, rien ici ne s'exécute et tout reste affiché tel quel.
// Les listes de sélecteurs sont les mêmes que dans motion.css, qui définit les états de départ et d'arrivée.
(() => {
  const html = document.documentElement;
  if (!html.classList.contains('m-on')) return;
  window.efMotion = true; // sans ce signal, le script de <head> retire m-on au bout de 4 s pour ne rien laisser caché

  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const SPLIT = 'main h1,main .shead h2,main .split-text h2,main .prose h2,main .rtitle h2,main .hj-text h2,main .mp-text h2,main .banner h2,main .jobs-head h2,main .nl-text h2,main .where h2,main .travel h2,.final h2';
  const UP = 'main .phead .crumbs,main .phead .chip,main .phead .lead,main .phead .cta-row,main .hero-text .chip,main .hero-text .lead,main .hero-text .cta-row,main .hb-text p,main .hb-text .pill,main .shead .chip,main .shead .intro,main .split-text>.chip,main .split-text>p,main .split-text>.btn,main .sub,main .hj-text p,main .hj-text .pill,main .mp-text p,main .help-left p,main .help-right .pill,main .jobs-head p,main .navy-sec .wrap>.pill,main .nl-text p,main .nl-text .pill,main .nl-lines,main .feat,main .rail-foot,main .prose>p,main .prose>ul,main .facts,main .where p,main .travel p,main .travel .btn,main .label-rule,.final p,.final .badges,.final-actions';
  const IMG = 'main .hero-photo,main .split-visual .ph,main .feat figure,main .more-panel figure,main .help-left figure,main .nl-ph';
  const POP = 'main .fc,main .sticker,main .nl-mark';
  const STAG = 'main .cards,main .steps,main .plans,main .rules,main .minis,main .contact-cards,main .areas,main .stats,main .ticks,main .faq,main .events,main .act-cards,main .mp-tiles,main .pop,main .acc,main .sitemap,.foot-grid';
  const RAIL = 'main .rail';
  const WIPE = 'main .mosaic,main .bento';
  const LINE = 'main .rtitle';
  const DRAW = 'main .illu';
  const COUNT = 'main .stat b,main .kpi b,main .ev-num b,main .plan .big';

  // Délai propre à un élément (variable --d de motion.css), en millisecondes.
  const delayOf = (el) => {
    const v = getComputedStyle(el).getPropertyValue('--d').trim();
    if (!v) return 0;
    return v.endsWith('ms') ? parseFloat(v) : parseFloat(v) * 1000;
  };

  // ── Titres découpés en mots, chacun dans un masque ─────────────────────────
  // Seules les espaces ordinaires séparent les mots : l'espace insécable de « Paris ? » garde la ponctuation collée.
  function split(el) {
    let n = 0;
    const walk = (node) => {
      for (const child of Array.from(node.childNodes)) {
        if (child.nodeType === 3) {
          const frag = document.createDocumentFragment();
          for (const part of child.textContent.split(/([ \t\n\r]+)/)) {
            if (!part) continue;
            if (/^[ \t\n\r]+$/.test(part)) { frag.appendChild(document.createTextNode(part)); continue; }
            const w = document.createElement('span');
            const inner = document.createElement('span');
            w.className = 'w';
            inner.textContent = part;
            inner.style.setProperty('--wi', n++);
            w.appendChild(inner);
            frag.appendChild(w);
          }
          child.replaceWith(frag);
        } else if (child.nodeType === 1 && child.tagName !== 'BR') {
          walk(child);
        }
      }
    };
    walk(el);
    el.classList.add('m-split');
  }
  $$(SPLIT).forEach(split);

  // ── Groupes : chaque enfant reçoit son rang, pour arriver l'un après l'autre ─
  const groups = $$(`${STAG},${RAIL},${WIPE}`);
  groups.forEach((g) => Array.from(g.children).forEach((c, i) => c.style.setProperty('--i', Math.min(i, 8))));

  // ── Chiffres qui défilent (« 15 % », « 18 à 25 % ») ; « 24h/24 » reste tel quel ─
  const FIGURE = /^\s*[≈~]?\s*\d+(\s*(à|–|-)\s*\d+)?\s*%?\s*$/;
  const counters = new Map();
  $$(COUNT).forEach((el) => {
    const nodes = [];
    const tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, {
      acceptNode: (t) => (t.parentElement.closest('small') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT),
    });
    while (tw.nextNode()) nodes.push(tw.currentNode);
    const items = nodes.filter((t) => /\d/.test(t.textContent)).map((t) => ({ t, src: t.textContent }));
    if (!items.length || !items.every((x) => FIGURE.test(x.src))) return;
    items.forEach((x) => { x.t.textContent = x.src.replace(/\d+/g, '0'); });
    counters.set(el, items);
  });
  function count(el) {
    const items = counters.get(el);
    if (!items) return;
    const start = performance.now() + delayOf(el) + 350;
    const dur = 1500;
    const ease = (t) => 1 - Math.pow(1 - t, 4);
    const frame = (now) => {
      const t = Math.min(1, Math.max(0, (now - start) / dur));
      const k = ease(t);
      items.forEach((x) => { x.t.textContent = x.src.replace(/\d+/g, (d) => String(Math.round(Number(d) * k))); });
      if (t < 1) requestAnimationFrame(frame);
    };
    requestAnimationFrame(frame);
  }

  // ── Apparition au défilement ───────────────────────────────────────────────
  const groupSel = `${STAG},${RAIL},${WIPE}`;
  function reveal(el) {
    el.classList.add('in');
    const d = delayOf(el);
    if (el.matches(groupSel)) {
      // Une fois tout arrivé : plus de délai au survol, et plus de découpe (ombres et débords réapparaissent).
      const n = Math.min(el.children.length, 9);
      setTimeout(() => el.classList.add('m-done'), d + n * 120 + 1400);
    } else if (el.matches(IMG)) {
      setTimeout(() => el.classList.add('m-free'), d + 1450);
    }
    if (counters.has(el)) count(el);
  }
  // Une photo découpée (rideau baissé) compte pour invisible aux yeux du navigateur : on surveille donc son parent,
  // qui, lui, n'est pas découpé. Un même élément surveillé peut ainsi déclencher plusieurs apparitions.
  const watched = new Map();
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      (watched.get(e.target) || []).forEach(reveal);
      watched.set(e.target, []);
      io.unobserve(e.target);
    }
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  const watch = (el, by = el) => {
    if (!watched.has(by)) { watched.set(by, []); io.observe(by); }
    watched.get(by).push(el);
  };
  $$(`${SPLIT},${UP},${POP},${STAG},${RAIL},${WIPE},${LINE},${DRAW},${COUNT}`).forEach((el) => watch(el));
  $$(IMG).forEach((el) => watch(el, el.parentElement));

  // ── Parallaxe ──────────────────────────────────────────────────────────────
  // Les cartes flottantes bougent un peu plus ou un peu moins vite que la page (mesurées sur leur parent, qui ne
  // bouge pas) ; dans les grandes photos, l'image glisse dans son cadre, agrandie juste ce qu'il faut pour ne
  // jamais montrer de bord.
  const OUTER = [
    ['main .hero-visual .fc-1', -0.07], ['main .hero-visual .fc-2', 0.06], ['main .hero-visual .fc-3', -0.05], ['main .hero-visual .sticker', 0.1],
    ['main .split-visual .fc.a', -0.05], ['main .split-visual .fc.b', 0.05], ['main .split-visual .fc.c', -0.04], ['main .split-visual .sticker', 0.08],
  ];
  const INNER = 'main .hero-photo,main .split-visual .ph,main .feat figure,main .more-panel figure,main .help-left figure,main .mosaic figure,main .b-portrait,main .b-ph';
  const BACK = 'main .banner,main .nl';
  const OVERSCAN = 1.12;
  const layers = [];
  OUTER.forEach(([sel, speed]) => $$(sel).forEach((el) => { el.classList.add('m-par'); layers.push({ el, ref: el.parentElement, speed, max: 70 }); }));
  $$(INNER).forEach((el) => { el.classList.add('m-pin'); el.style.setProperty('--ps', OVERSCAN); layers.push({ el, ref: el, speed: 0.06, inner: true }); });
  $$(BACK).forEach((el) => layers.push({ el, ref: el, speed: 0.12, inner: true, scale: 1.18 }));
  const visible = new Set();
  const pio = new IntersectionObserver((entries) => entries.forEach((e) => (e.isIntersecting ? visible.add(e.target) : visible.delete(e.target))), { rootMargin: '25% 0px' });
  layers.forEach((l) => pio.observe(l.ref));
  function parallax() {
    const vh = window.innerHeight;
    for (const l of layers) {
      if (!visible.has(l.ref)) continue;
      const r = l.ref.getBoundingClientRect();
      const c = (r.top + r.height / 2 - vh / 2) / vh;
      const max = l.inner ? ((l.scale || OVERSCAN) - 1) / 2 * r.height : l.max;
      const y = Math.max(-max, Math.min(max, -c * l.speed * vh));
      l.el.style.setProperty('--py', `${y.toFixed(1)}px`);
    }
  }

  // ── En-tête : s'efface en descendant, revient en remontant ; fine barre de progression ─
  const top = document.querySelector('.top');
  const menu = document.getElementById('menu');
  if (top) {
    const bar = document.createElement('span');
    bar.className = 'm-progress';
    bar.setAttribute('aria-hidden', 'true');
    top.appendChild(bar);
    top.addEventListener('focusin', () => top.classList.remove('m-hide'));
  }
  function header(y, dy) {
    if (!top) return;
    if (menu && menu.classList.contains('open')) top.classList.remove('m-hide');
    else if (y > 420 && dy > 3) top.classList.add('m-hide');
    else if (dy < -3 || y < 200) top.classList.remove('m-hide');
    const max = document.documentElement.scrollHeight - window.innerHeight;
    top.style.setProperty('--p', max > 0 ? Math.min(1, y / max).toFixed(4) : '0');
  }

  // ── Bandeau des quartiers : il accélère avec le défilement, puis reprend son rythme ─
  const marquee = document.querySelector('.marquee');
  const anim = marquee && marquee.getAnimations ? marquee.getAnimations()[0] : null;
  let rate = 1;
  let boost = 1;
  let spinning = false;
  function spin() {
    rate += (boost - rate) * 0.12;
    boost += (1 - boost) * 0.06;
    anim.playbackRate = rate;
    if (Math.abs(rate - 1) > 0.01 || Math.abs(boost - 1) > 0.01) requestAnimationFrame(spin);
    else { anim.playbackRate = 1; spinning = false; }
  }
  function speedUp(dy) {
    if (!anim) return;
    boost = Math.max(boost, 1 + Math.min(6, Math.abs(dy) * 0.3));
    if (!spinning) { spinning = true; requestAnimationFrame(spin); }
  }

  let lastY = window.scrollY;
  let ticking = false;
  function frame() {
    ticking = false;
    const y = window.scrollY;
    const dy = y - lastY;
    lastY = y;
    header(y, dy);
    parallax();
    if (dy) speedUp(dy);
  }
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  frame();

  // ── Boutons aimantés (souris seulement) ────────────────────────────────────
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    $$('.btn,.pill').forEach((b) => {
      b.addEventListener('pointermove', (e) => {
        const r = b.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        b.style.transform = `translate(${(x * 12).toFixed(1)}px, ${(y * 10).toFixed(1)}px)`;
      });
      b.addEventListener('pointerleave', () => { b.style.transform = ''; });
    });
  }

  // ── Questions qui s'ouvrent et se referment en douceur ────────────────────
  $$('main details').forEach((d) => {
    const s = d.querySelector('summary');
    if (!s) return;
    s.addEventListener('click', (e) => {
      e.preventDefault();
      // Un second clic pendant l'animation la renverse, depuis la hauteur où elle en est.
      const start = d.offsetHeight;
      const wasClosing = Boolean(d.m && d.m.closing);
      if (d.m) d.m.cancel();
      const opening = wasClosing || !d.open;
      if (opening) d.open = true;
      const end = opening ? d.offsetHeight : s.offsetHeight + (d.offsetHeight - d.clientHeight);
      d.style.overflow = 'hidden';
      d.m = d.animate({ height: [`${start}px`, `${end}px`] }, { duration: 480, easing: 'cubic-bezier(.16,1,.3,1)' });
      d.m.closing = !opening;
      const body = s.nextElementSibling;
      if (opening && body) body.animate({ opacity: [0, 1], transform: ['translateY(-8px)', 'none'] }, { duration: 480, easing: 'ease-out' });
      d.m.onfinish = () => { d.m = null; d.style.overflow = ''; if (!opening) d.open = false; };
      d.m.oncancel = () => { d.m = null; d.style.overflow = ''; };
    });
  });
})();
