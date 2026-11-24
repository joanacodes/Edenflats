// Menu mobile, ombre de l'en-tête au défilement, rail des quartiers et apparition des blocs.
document.documentElement.classList.remove('no-js');

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
const onScroll = () => entete && entete.classList.toggle('scrolled', window.scrollY > 8);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Les flèches font défiler le rail d'une carte et demie ; sans JavaScript, le rail défile au doigt.
document.querySelectorAll('[data-rail]').forEach((box) => {
  const rail = box.querySelector('.rail');
  const step = () => (rail.querySelector('.area-card')?.offsetWidth || 260) * 1.5;
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
