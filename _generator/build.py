# Génère toutes les pages HTML à la racine du dépôt. Usage : py build.py (depuis _generator/).
# Les textes communs (menu, pied de page, coordonnées) sont ici : on les change une fois, pour toutes les pages.
import json
from html import escape
from pathlib import Path

import illustrations

ROOT = Path(__file__).resolve().parent.parent

# Coordonnées : une valeur vide s'affiche « à compléter », entourée de pointillés, pour ne pas publier de faux numéro.
SITE = {
    "name": "EdenFlats",
    "group": "EF Group",
    "url": "https://www.edenflats.com",
    "phone": "",        # ex. "01 23 45 67 89"
    "phone_intl": "",   # ex. "+33123456789"
    "whatsapp": "",     # ex. "33612345678" (sans +)
    "email": "",        # ex. "contact@edenflats.com"
}

NAV = [
    ("Gestion des voyageurs", "/gestion-des-voyageurs/"),
    ("Gestion du logement", "/gestion-du-logement/"),
    ("Secteurs", "/#secteurs"),
    ("FAQ", "/faq/"),
]
TOWNS = [
    ("Créteil", "/conciergerie-airbnb-creteil/"),
    ("Saint-Maur-des-Fossés", "/conciergerie-airbnb-saint-maur-des-fosses/"),
]

ICONS = {
    "annonce": '<path d="M5 4h14v16H5zM9 9h6M9 13h6M9 17h3"/>',
    "prix": '<path d="M4 19h16M6 15l4-5 4 3 5-7"/><path d="M15 6h4v4"/>',
    "voyageur": '<circle cx="12" cy="8" r="3.5"/><path d="M5 20c1-4 4-6 7-6s6 2 7 6"/>',
    "cle": '<circle cx="8" cy="15" r="4"/><path d="M11 12l8-8M16 7l3 3M14 9l2 2"/>',
    "menage": '<path d="M12 3v9M8 12h8l2 9H6z"/><path d="M10 16v5M14 16v5"/>',
    "linge": '<path d="M4 8h16v4H4zM5 12h14v4H5zM6 16h12v4H6z"/>',
    "entretien": '<path d="M14 6a4 4 0 0 0 5 5l-8 8a2.1 2.1 0 0 1-3-3l8-8z"/><path d="M14 6l3-2 3 3-2 3"/>',
    "tel": '<path d="M6 3h4l2 5-3 2a12 12 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 4 5a2 2 0 0 1 2-2z"/>',
    "mail": '<path d="M3 6h18v12H3z"/><path d="M3 7l9 7 9-7"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
    "maison": '<path d="M4 11l8-7 8 7v9H4z"/><path d="M10 20v-6h4v6"/>',
}


def ico(name, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


LOGO = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
        '<path d="M12 2v20M4 6l16 12M20 6L4 18"/></svg>')


def todo(label):
    return f'<b class="todo">{label} à compléter</b>'


def contact_items():
    s = SITE
    tel = (f'<a href="tel:{s["phone_intl"]}">{ico("tel", "")}<span><small>Téléphone</small><b>{s["phone"]}</b></span></a>'
           if s["phone"] else f'<div>{ico("tel", "")}<span><small>Téléphone</small>{todo("Numéro")}</span></div>')
    wa = (f'<a href="https://wa.me/{s["whatsapp"]}">{ico("chat", "")}<span><small>WhatsApp</small><b>Écrire sur WhatsApp</b></span></a>'
          if s["whatsapp"] else f'<div>{ico("chat", "")}<span><small>WhatsApp</small>{todo("Numéro WhatsApp")}</span></div>')
    mail = (f'<a href="mailto:{s["email"]}">{ico("mail", "")}<span><small>E-mail</small><b>{s["email"]}</b></span></a>'
            if s["email"] else f'<div>{ico("mail", "")}<span><small>E-mail</small>{todo("Adresse e-mail")}</span></div>')
    return f'<div class="contact-list">{tel}{wa}{mail}</div>'


def layout(path, title, desc, body, extra_head=""):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{h}"{cur if h == path else ""}>{t}</a>' for t, h in NAV)
    towns = "".join(f'<li><a href="{h}">Conciergerie à {t}</a></li>' for t, h in TOWNS)
    return f"""<!doctype html>
<html lang="fr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{SITE['url']}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{SITE['url']}{path}">
<meta name="theme-color" content="#1B1B4B">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/instrument-sans-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
{extra_head}</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="top on-dark">
  <div class="wrap">
    <a class="logo" href="/" aria-label="EdenFlats, accueil">{LOGO}<span>Eden<em>Flats</em></span></a>
    <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu"><span></span></button>
    <nav class="nav" id="menu" aria-label="Menu principal">{nav}<a href="/contact/"{' aria-current="page"' if path == '/contact/' else ''}>Contact</a></nav>
    <a class="btn lime" href="/contact/">Confier mon logement</a>
  </div>
</header>
<main id="contenu">
{body}
</main>
<footer>
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="logo" href="/">{LOGO}<span>Eden<em>Flats</em></span></a>
        <p style="margin-top:14px;max-width:32ch">Conciergerie Airbnb pour les propriétaires, à Paris et en Île-de-France.</p>
      </div>
      <div><h3>Services</h3><ul>
        <li><a href="/gestion-des-voyageurs/">Gestion des voyageurs</a></li>
        <li><a href="/gestion-du-logement/">Gestion du logement</a></li>
        <li><a href="/faq/">Questions fréquentes</a></li></ul></div>
      <div><h3>Secteurs</h3><ul>{towns}<li><a href="/#secteurs">Paris et Île-de-France</a></li></ul></div>
      <div><h3>Nous joindre</h3><ul><li><a href="/contact/">Téléphone, WhatsApp, e-mail</a></li></ul></div>
    </div>
    <div class="legal"><span>© {SITE['name']}, une marque d’{SITE['group']}</span><span>Paris et Île-de-France</span></div>
  </div>
</footer>
<script src="/assets/main.js" defer></script>
</body>
</html>
"""


def cta_band(title="Parlons de <em>votre logement</em>",
             text="Dites-nous où se trouve votre bien et ce que vous souhaitez nous confier. Nous vous répondons sur ce que nous pouvons prendre en charge."):
    return f"""<section class="cta-band" aria-labelledby="cta-t">
  <img src="/assets/img/facade.svg" alt="" loading="lazy">
  <div class="wrap"><div class="cta-card reveal">
    <div><h2 id="cta-t">{title}</h2><p>{text}</p>
      <div class="cta"><a class="btn" href="/contact/">Nous contacter</a><a class="btn ghost" href="/faq/">Lire la FAQ</a></div></div>
    <figure><img src="/assets/img/accueil.svg" alt="" loading="lazy"></figure>
  </div></div>
</section>"""


def page_head(crumb, h1, lead, img, alt=""):
    return f"""<section class="page-head">
  <div class="wrap">
    <div class="txt"><p class="crumbs"><a href="/">Accueil</a> / {crumb}</p><h1>{h1}</h1><p class="lead">{lead}</p></div>
    <figure><img src="/assets/img/{img}" alt="{alt}"></figure>
  </div>
</section>"""


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# ── Questions fréquentes ─────────────────────────────────────────────────────
# Les réponses sur le contrat, les tarifs et l'accès au compte Airbnb restent générales :
# elles sont à reprendre mot pour mot du site actuel (voir README, « À compléter »).
FAQ = [
    ("Sur quelles plateformes mon logement est-il publié ?",
     "Votre logement est publié sur Airbnb, sur Booking.com et sur d’autres plateformes de location. Nous rédigeons les annonces et nous les tenons à jour."),
    ("Puis-je choisir seulement certains services ?",
     "Oui. Les services se choisissent à la carte : vous nous confiez ce que vous ne voulez plus faire et vous gardez le reste."),
    ("Comment les prix des nuits sont-ils fixés ?",
     "Les prix suivent la demande : ils sont ajustés selon la période, pour que votre logement reste loué au bon tarif."),
    ("Comment se passe l’arrivée des voyageurs ?",
     "Nous accueillons les voyageurs sur place, ou ils entrent seuls grâce à une clé connectée ou à une boîte à clés. Dans les deux cas, vous n’avez pas à vous déplacer."),
    ("Qui s’occupe du ménage et du linge ?",
     "Nous. Le logement est nettoyé après chaque départ, le linge est changé et les consommables sont remis en place avant l’arrivée suivante."),
    ("Louez-vous en courte ou en moyenne durée ?",
     "Les deux. Nous gérons des séjours de quelques nuits comme des locations de plusieurs semaines ou de plusieurs mois."),
    ("Comment fonctionnent le contrat et la tarification ?",
     "Ils dépendent des services que vous choisissez et de votre logement. Nous vous les détaillons par écrit avant tout engagement : contactez-nous pour recevoir une proposition."),
    ("Qui garde l’accès au compte Airbnb ?",
     "C’est un point que nous réglons avec vous dès le départ, avant la mise en ligne. Posez-nous la question lors de notre premier échange."),
    ("Quels secteurs couvrez-vous ?",
     "Paris et l’Île-de-France, notamment Créteil et Saint-Maur-des-Fossés. Si votre commune n’apparaît pas sur le site, demandez-nous : nous vous dirons si nous pouvons intervenir."),
]


def faq_html(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)


# ── Accueil ──────────────────────────────────────────────────────────────────
def home():
    places = "".join(f'<a href="{h}">{t}</a>' for t, h in TOWNS)
    body = f"""<section class="hero">
  <div class="wrap">
    <div>
      <h1>Votre logement loué sur Airbnb, <em>sans vous en occuper</em></h1>
      <p class="lead">EdenFlats est une conciergerie pour les propriétaires de résidences secondaires et de biens locatifs, à Paris et en Île-de-France. Nous gérons votre meublé en location courte et moyenne durée, de l’annonce au ménage.</p>
      <div class="cta"><a class="btn" href="/contact/">Confier mon logement</a><a class="btn ghost" href="#services">Voir ce que nous gérons</a></div>
    </div>
    <div class="mosaic">
      <div class="tile a">{ico("annonce", "")}<b>Airbnb, Booking.com</b><span>et d’autres plateformes</span></div>
      <div class="b"><img src="/assets/img/salon.svg" alt="Salon d’un appartement meublé"></div>
      <div class="c"><img src="/assets/img/cles.svg" alt="Porte équipée d’une serrure connectée"></div>
      <div class="tile d">{ico("cle", "")}<b>Arrivée autonome</b><span>clé connectée ou boîte à clés</span></div>
    </div>
  </div>
</section>

<section id="services" aria-labelledby="s-t">
  <div class="wrap">
    <div class="rule"><h2 id="s-t">Tout ce que vous n’aurez <em>plus à faire</em></h2></div>
    <p class="intro">Louer un meublé en courte durée, c’est une longue liste de tâches qui reviennent à chaque séjour. Voici celles que nous prenons en charge.</p>
    <div class="bento">
      <a class="card lime s4 reveal" href="/gestion-des-voyageurs/">{ico("voyageur")}<h3>Gestion des voyageurs</h3><p>Annonces, prix, sélection des voyageurs, accueil ou arrivée à distance.</p></a>
      <div class="card pic s4 reveal"><img src="/assets/img/facade.svg" alt="" loading="lazy"><span>Paris et Île-de-France</span></div>
      <div class="card pic s4 r2 round-tr reveal"><img src="/assets/img/accueil.svg" alt="" loading="lazy"><span>Un accueil sur place ou à distance</span></div>
      <div class="card pic s4 round-bl reveal"><img src="/assets/img/linge.svg" alt="" loading="lazy"><span>Ménage et linge après chaque départ</span></div>
      <a class="card navy s4 reveal" href="/gestion-du-logement/">{ico("maison")}<h3>Gestion du logement</h3><p>Ménage, linge, consommables et entretien courant de votre bien.</p></a>
      <div class="card cream s3 reveal">{ico("annonce")}<h3>Annonces</h3><p>Rédigées et publiées sur Airbnb, Booking.com et d’autres plateformes.</p></div>
      <div class="card sky s3 reveal">{ico("prix")}<h3>Prix ajustés</h3><p>Des tarifs qui suivent la demande, période par période.</p></div>
      <div class="card cream s3 reveal">{ico("cle")}<h3>Clés connectées</h3><p>Serrures connectées et boîtes à clés pour les arrivées à distance.</p></div>
      <div class="card lime s3 reveal">{ico("entretien")}<h3>Entretien</h3><p>Le suivi courant du logement, pour qu’il reste prêt à louer.</p></div>
    </div>
  </div>
</section>

<section class="cream" aria-labelledby="v-t">
  <div class="wrap overlap">
    <figure><img src="/assets/img/accueil.svg" alt="Une personne accueille des voyageurs à l’entrée d’un logement" loading="lazy"></figure>
    <div class="panel reveal">
      <p class="kicker">Gestion des voyageurs</p>
      <h2 id="v-t">Des voyageurs choisis, <em>accueillis</em> et suivis</h2>
      {ticks(["Sélection des voyageurs avant chaque réservation", "Accueil sur place, ou arrivée à distance avec une clé connectée ou une boîte à clés", "Des prix ajustés selon la demande", "Séjours de courte et de moyenne durée"])}
      <a class="btn" href="/gestion-des-voyageurs/">Gestion des voyageurs</a>
    </div>
  </div>
</section>

<section aria-labelledby="l-t">
  <div class="wrap overlap flip">
    <figure><img src="/assets/img/linge.svg" alt="Lit fait avec du linge propre plié" loading="lazy"></figure>
    <div class="panel lime reveal">
      <p class="kicker">Gestion du logement</p>
      <h2 id="l-t">Un logement <em>prêt</em> pour chaque arrivée</h2>
      {ticks(["Ménage après chaque départ", "Linge de lit et de toilette", "Réassort des consommables", "Entretien courant du logement"])}
      <a class="btn" href="/gestion-du-logement/">Gestion du logement</a>
    </div>
  </div>
</section>

<section class="sky" id="secteurs" aria-labelledby="z-t">
  <div class="wrap two">
    <div><div class="rule left"><h2 id="z-t">Près de <em>votre bien</em></h2></div>
      <p class="lead" style="color:var(--navy)">Une conciergerie se choisit près de son logement. Nous intervenons à Paris et en Île-de-France.</p></div>
    <div><div class="places"><span>Paris</span><span>Île-de-France</span>{places}</div>
      <p style="margin-top:20px">Votre commune n’est pas dans la liste ? <a href="/contact/">Demandez-nous</a> si nous la couvrons.</p></div>
  </div>
</section>

<section class="navy on-dark" aria-labelledby="f-t">
  <div class="wrap faq-grid">
    <div><div class="rule left"><h2 id="f-t">Avant de nous <em>confier vos clés</em></h2></div>
      <p>Les questions que les propriétaires nous posent avant d’appeler.</p>
      <figure><img src="/assets/img/salon.svg" alt="" loading="lazy"></figure></div>
    <div>{faq_html(FAQ[:5])}<p style="margin-top:28px"><a class="btn ghost" href="/faq/">Toutes les questions</a></p></div>
  </div>
</section>

{cta_band()}"""
    return layout("/", "EdenFlats : conciergerie Airbnb à Paris et en Île-de-France",
                  "EdenFlats gère la location courte et moyenne durée de votre logement meublé à Paris et en Île-de-France : annonces, voyageurs, clés, ménage, linge et entretien.",
                  body)


# ── Pages de service ─────────────────────────────────────────────────────────
def voyageurs():
    body = page_head("Gestion des voyageurs", "La gestion des voyageurs, <em>de la réservation au départ</em>",
                     "Nous publions votre logement, nous choisissons les voyageurs et nous les accueillons, sur place ou à distance.",
                     "accueil.svg", "Une personne accueille des voyageurs") + f"""
<section><div class="wrap two">
  <div class="prose">
    <h2 style="margin-top:0">Des annonces sur les bonnes plateformes</h2>
    <p>Nous rédigeons l’annonce de votre logement et nous la publions sur Airbnb, sur Booking.com et sur d’autres plateformes. Le calendrier et les informations restent à jour d’une plateforme à l’autre.</p>
    <h2>Des prix qui suivent la demande</h2>
    <p>Le tarif d’une nuit n’est pas le même toute l’année. Nous l’ajustons selon la demande, pour que votre logement soit loué au bon prix à chaque période.</p>
    <h2>Des voyageurs sélectionnés</h2>
    <p>Chaque demande est examinée avant d’être acceptée. Vous savez que votre logement n’est pas ouvert au premier venu.</p>
    <h2>L’accueil, sur place ou à distance</h2>
    <p>Nous accueillons les voyageurs dans le logement. Quand ils arrivent tard ou préfèrent entrer seuls, une clé connectée ou une boîte à clés leur ouvre la porte, sans que vous ayez à vous déplacer.</p>
    <h2>Courte et moyenne durée</h2>
    <p>Un week-end, une semaine ou plusieurs mois : nous gérons les deux types de séjours et nous adaptons la mise en location à votre bien.</p>
  </div>
  <div class="panel navy on-dark" style="background:var(--navy);color:#fff;padding:32px;border-radius:0 var(--r-lg) 0 0">
    <p class="kicker" style="color:var(--lime)">Ce que nous prenons en charge</p>
    {ticks(["Annonces sur Airbnb, Booking.com et d’autres plateformes", "Prix ajustés selon la demande", "Sélection des voyageurs", "Accueil sur place", "Clés connectées et boîtes à clés", "Séjours courts et moyens"])}
    <p style="margin-top:24px"><a class="btn lime" href="/contact/">Confier mon logement</a></p>
  </div>
</div></section>
{cta_band("Et le logement <em>lui-même</em> ?", "Ménage, linge, consommables, entretien : nous nous occupons aussi du bien entre deux séjours.").replace('href="/faq/">Lire la FAQ', 'href="/gestion-du-logement/">Gestion du logement')}"""
    return layout("/gestion-des-voyageurs/", "Gestion des voyageurs Airbnb | EdenFlats",
                  "Annonces sur Airbnb et Booking.com, prix ajustés, sélection et accueil des voyageurs, arrivée à distance : la gestion des voyageurs par EdenFlats, en Île-de-France.",
                  body)


def logement():
    body = page_head("Gestion du logement", "Un logement <em>prêt à louer</em>, séjour après séjour",
                     "Ménage, linge, consommables et entretien : nous remettons votre bien en état après chaque départ.",
                     "linge.svg", "Lit fait avec du linge propre") + f"""
<section><div class="wrap">
  <div class="rule"><h2>Entre deux <em>séjours</em></h2></div>
  <div class="bento">
    <div class="card lime s6 reveal">{ico("menage")}<h3>Ménage après chaque départ</h3><p>Le logement est nettoyé dès que les voyageurs sont partis, avant l’arrivée des suivants.</p></div>
    <div class="card navy s6 round-tr reveal">{ico("linge")}<h3>Linge</h3><p>Draps et serviettes propres à chaque séjour : vous n’avez ni lessive ni stock à gérer.</p></div>
    <div class="card sky s6 round-bl reveal">{ico("annonce")}<h3>Réassort des consommables</h3><p>Ce qui s’use d’un séjour à l’autre est remis en place avant l’arrivée suivante.</p></div>
    <div class="card cream s6 reveal">{ico("entretien")}<h3>Entretien du logement</h3><p>Nous suivons l’état de votre bien au fil des séjours, pour qu’il reste en bon état et prêt à louer.</p></div>
  </div>
</div></section>
<section class="cream"><div class="wrap overlap">
  <figure><img src="/assets/img/salon.svg" alt="Salon d’un appartement meublé" loading="lazy"></figure>
  <div class="panel reveal"><p class="kicker">À la carte</p><h2>Vous choisissez ce que vous <em>nous confiez</em></h2>
    <p>Vous pouvez nous laisser toute la gestion, ou seulement une partie. Les services se choisissent à la carte, selon ce que vous voulez garder en main.</p>
    <a class="btn" href="/contact/">En parler avec nous</a></div>
</div></section>
{cta_band("Et les <em>voyageurs</em> ?", "Annonces, prix, sélection, accueil : nous gérons aussi tout ce qui se passe avant et pendant le séjour.").replace('href="/faq/">Lire la FAQ', 'href="/gestion-des-voyageurs/">Gestion des voyageurs')}"""
    return layout("/gestion-du-logement/", "Gestion du logement en location courte durée | EdenFlats",
                  "Ménage après chaque départ, linge, réassort des consommables et entretien de votre meublé : la gestion du logement par EdenFlats, à Paris et en Île-de-France.",
                  body)


def faq():
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    head = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
    body = page_head("FAQ", "Les questions des <em>propriétaires</em>",
                     "Plateformes, services à la carte, contrat, tarifs : ce qu’on nous demande avant de nous confier un logement.",
                     "cles.svg", "Porte équipée d’une serrure connectée") + f"""
<section class="faq-page"><div class="wrap"><div class="prose" style="max-width:820px">{faq_html(FAQ)}
  <p style="margin-top:32px">Vous ne trouvez pas votre réponse ? <a href="/contact/">Écrivez-nous ou appelez-nous</a>.</p></div></div></section>
{cta_band()}"""
    return layout("/faq/", "Questions fréquentes des propriétaires | EdenFlats",
                  "Sur quelles plateformes votre logement est publié, quels services choisir à la carte, comment fonctionnent contrat et tarifs : les réponses d’EdenFlats.",
                  body, head)


# ── Pages par commune ────────────────────────────────────────────────────────
def town(slug, name, a_name, lead, local, places_txt):
    body = page_head(f"Conciergerie à {name}", f"Conciergerie Airbnb <em>{a_name}</em>", lead, "marne.svg", "") + f"""
<section><div class="wrap two">
  <div class="prose">{local}
    <h2>Ce que nous gérons {a_name}</h2>
    <p>Les mêmes services que partout en Île-de-France : <a href="/gestion-des-voyageurs/">la gestion des voyageurs</a>, des annonces à l’accueil, et <a href="/gestion-du-logement/">la gestion du logement</a>, du ménage à l’entretien. Vous pouvez tout nous confier ou choisir à la carte.</p>
  </div>
  <div style="background:var(--lime);padding:32px;border-radius:0 var(--r-lg) 0 0">
    <p class="kicker">{name}</p>
    {ticks(places_txt)}
    <p style="margin-top:24px"><a class="btn" href="/contact/">Confier mon logement {a_name}</a></p>
  </div>
</div></section>
{cta_band(f"Un logement <em>{a_name}</em> ?", "Dites-nous où il se trouve et ce que vous souhaitez nous confier.")}"""
    return layout(f"/{slug}/", f"Conciergerie Airbnb {a_name} | EdenFlats",
                  f"EdenFlats gère votre location courte et moyenne durée {a_name} : annonces, voyageurs, clés, ménage, linge et entretien.", body)


CRETEIL = town(
    "conciergerie-airbnb-creteil", "Créteil", "à Créteil",
    "Vous avez un meublé à Créteil ? Nous le gérons en location courte et moyenne durée, de l’annonce au ménage.",
    """<h2 style="margin-top:0">Louer un meublé à Créteil</h2>
    <p>Préfecture du Val-de-Marne, Créteil est reliée à Paris par la ligne 8 du métro. La ville accueille l’université Paris-Est Créteil et l’hôpital Henri-Mondor : on y vient pour étudier, pour travailler ou pour accompagner un proche, souvent pour plus que quelques nuits.</p>
    <p>C’est un secteur où la moyenne durée a autant de sens que le court séjour. Nous adaptons la mise en location à votre bien et à son quartier, du centre ancien aux abords du lac.</p>""",
    ["Métro ligne 8 vers Paris", "Université Paris-Est Créteil", "Hôpital Henri-Mondor", "Lac de Créteil"])

SAINT_MAUR = town(
    "conciergerie-airbnb-saint-maur-des-fosses", "Saint-Maur-des-Fossés", "à Saint-Maur-des-Fossés",
    "Vous avez un meublé à Saint-Maur-des-Fossés ? Nous le gérons en location courte et moyenne durée, de l’annonce au ménage.",
    """<h2 style="margin-top:0">Louer un meublé à Saint-Maur-des-Fossés</h2>
    <p>Saint-Maur-des-Fossés occupe une boucle de la Marne, dans le Val-de-Marne. Le RER A y compte quatre gares et rejoint le centre de Paris sans changement. Les voyageurs y cherchent le calme des bords de Marne à proximité de la capitale.</p>
    <p>De La Varenne au Vieux Saint-Maur, les quartiers n’attirent pas les mêmes séjours. Nous présentons votre logement pour ce qu’il offre : la gare à pied, la rivière, un jardin.</p>""",
    ["RER A, quatre gares dans la commune", "Les bords de Marne", "La Varenne, Le Parc, Champignol", "Le Vieux Saint-Maur"])


def contact():
    body = f"""<section class="page-head" style="padding-bottom:clamp(40px,6vw,72px)">
  <div class="wrap" style="display:block"><p class="crumbs"><a href="/">Accueil</a> / Contact</p>
    <h1>Parlons de <em>votre logement</em></h1>
    <p class="lead">Appelez-nous, écrivez-nous sur WhatsApp ou par e-mail. Dites-nous où se trouve votre bien et ce que vous souhaitez nous confier.</p></div>
</section>
<section class="cream"><div class="wrap two">
  {contact_items()}
  <div><h2 style="font-size:1.5rem;margin-bottom:16px">Pour préparer notre échange</h2>
    {ticks(["La commune et le type de logement", "S’il est déjà en location, et sur quelles plateformes", "Ce que vous voulez nous confier : tout, ou certains services", "La durée des séjours que vous visez"])}
    <p style="margin-top:20px">Avant d’appeler, la <a href="/faq/">FAQ</a> répond aux questions les plus courantes.</p></div>
</div></section>"""
    return layout("/contact/", "Contact | EdenFlats, conciergerie Airbnb en Île-de-France",
                  "Contactez EdenFlats par téléphone, WhatsApp ou e-mail pour confier la gestion de votre logement meublé à Paris et en Île-de-France.", body)


def not_found():
    body = """<section class="page-head" style="padding-bottom:clamp(56px,8vw,112px)"><div class="wrap" style="display:block">
  <h1>Cette page <em>n’existe pas</em></h1><p class="lead">Le lien est peut-être ancien.</p>
  <p style="margin-top:28px"><a class="btn" href="/">Retour à l’accueil</a></p></div></section>"""
    return layout("/404.html", "Page introuvable | EdenFlats", "Page introuvable.", body)


PAGES = {
    "index.html": home(),
    "gestion-des-voyageurs/index.html": voyageurs(),
    "gestion-du-logement/index.html": logement(),
    "faq/index.html": faq(),
    "conciergerie-airbnb-creteil/index.html": CRETEIL,
    "conciergerie-airbnb-saint-maur-des-fosses/index.html": SAINT_MAUR,
    "contact/index.html": contact(),
    "404.html": not_found(),
}

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#1B1B4B"/>'
           '<path d="M16 6v20M7 10l18 12M25 10L7 22" stroke="#E4FBC0" stroke-width="2.6"/></svg>')

if __name__ == "__main__":
    illustrations.write()
    for rel, html in PAGES.items():
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
    (ROOT / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    urls = [("/" + rel.removesuffix("index.html")) for rel in PAGES if rel != "404.html"]
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{SITE['url']}{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("pages :", len(PAGES))
