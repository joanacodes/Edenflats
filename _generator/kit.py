# Briques communes à toutes les pages : coordonnées, adresses des pages, gabarit, composants, icônes.
# Les textes des pages sont dans pages.py, quartiers.py et faq.py.
import json
import re
from datetime import date
from html import escape

from illus import illu  # noqa: F401  (réexporté pour les pages)

# Une valeur vide s'affiche « à compléter » (cadre pointillé) : on ne publie pas d'information inventée.
SITE = {
    "name": "EdenFlats",
    "url": "https://www.edenflats.com",
    "phone": "+33 7 84 54 48 61",
    "phone_href": "+33784544861",
    "whatsapp": "33784544861",
    "email": "edenflats.paris@gmail.com",
    "booking": "https://directbooky.com/vacationrentals",
    # Réseaux sociaux : (icône, nom, adresse de la page). Tant que l'adresse est vide, l'icône s'affiche sans lien.
    # Supprimez une ligne pour retirer un réseau ; l'icône de chaque réseau est dans ICONS (TikTok y est déjà).
    "social": [
        ("instagram", "Instagram", ""),
        ("facebook", "Facebook", ""),
        ("linkedin", "LinkedIn", ""),
        ("youtube", "YouTube", ""),
        # ("tiktok", "TikTok", ""),
    ],
    # Bandeau cookies (accepter / refuser, choix gardé six mois, rouvrable en bas de page). Il demande l'accord
    # pour la mesure d'audience Google Analytics, qui ne se charge qu'après « Accepter » et seulement si
    # l'identifiant GA4 est renseigné (ex. "G-ABC123XYZ9"). Sans mesure d'audience, aucun bandeau n'est
    # nécessaire : mettez alors "cookie_banner" à False, la politique de confidentialité s'adapte.
    "cookie_banner": True,
    "analytics": {"ga4": ""},
    "company": {
        "name": "EDENEL PATRIMOINE GESTION RESEAUX & SERVICES",
        "acronym": "EPGRS",
        "form": {"fr": "Société par actions simplifiée (SAS)", "en": "French simplified joint-stock company (SAS)"},
        "capital": "",  # ex. "1 000 €"
        "address": "14 rue de Champigny, 94370 Sucy-en-Brie, France",
        "siren": "104 632 591",
        "siret": "104 632 591 00012",
        "rcs": "",  # ex. "RCS Créteil 104 632 591" (à vérifier sur l'extrait Kbis)
        "vat": "",  # ex. "FR62104632591" (à confirmer : numéro calculé, non publié par le registre)
        "naf": "68.31Z",
        "director": "Flore Hountondji",
        "director_role": {"fr": "présidente", "en": "President"},
    },
    "host": {"name": "GitHub, Inc.", "address": "88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA",
             "url": "https://github.com"},
    "maker": ("MLK Web Studio", "https://mlkwebstudio.fr"),
}

OTHER = {"fr": "en", "en": "fr"}

# Adresses des pages. Les pages françaises reprennent exactement les adresses de l'ancien site
# Squarespace (sans barre finale) pour garder leur référencement : chaque page est un fichier .html
# que GitHub Pages sert sans l'extension (/faq sert faq.html).
ROUTES = {
    "home": {"fr": "/", "en": "/en/"},
    "voyageurs": {"fr": "/gestion-des-voyageurs-conciergerie-airbnb-ile-de-france", "en": "/en/guest-management"},
    "logement": {"fr": "/gestion-de-propriete-conciergerie-airbnb-ile-de-france", "en": "/en/property-management"},
    "formules": {"fr": "/nos-formules", "en": "/en/plans"},
    "faq": {"fr": "/faq", "en": "/en/faq"},
    "paris": {"fr": "/conciergerie-airbnb-paris", "en": "/en/airbnb-management-paris"},
    "contact": {"fr": "/contact", "en": "/en/contact"},
    "mentions": {"fr": "/mentions-legales", "en": "/en/legal-notice"},
    "cgv": {"fr": "/conditions-generales-de-vente", "en": "/en/terms-and-conditions"},
    "confidentialite": {"fr": "/politique-de-cookies", "en": "/en/privacy"},
    "plan": {"fr": "/plan-du-site", "en": "/en/sitemap"},
}


def url(pid, L):
    return ROUTES[pid][L]


def tr(L):
    """Renvoie t(fr, en) qui choisit le texte de la langue de la page."""
    return lambda fr, en: fr if L == "fr" else en


# ── Icônes (trait, 24 × 24) ─────────────────────────────────────────────────
ICONS = {
    "calendar": '<rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="M8.5 14.5l2 2 4-4"/>',
    "door": '<path d="M6 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16"/><path d="M3.5 21h17"/><circle cx="14.5" cy="12.5" r="1"/>',
    "sparkle": '<path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M18.5 15.5l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/>',
    "linen": '<path d="M4 7.5h16v3.5H4zM5 11h14v3.5H5zM6 14.5h12V18H6z"/><path d="M8 7.5V5.5h8v2"/>',
    "wrench": '<path d="M14.5 6.5a4 4 0 0 0 5 5L12 19a2.1 2.1 0 0 1-3-3z"/><path d="M14.5 6.5L17 4l3 3-2.5 2.5"/>',
    "headset": '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/><path d="M19 19c0 1.5-1.5 2.5-4 2.5h-2"/>',
    "scales": '<path d="M12 4v16M7 20h10M5 7h14"/><path d="M5 7l-3 6a3 3 0 0 0 6 0zM19 7l-3 6a3 3 0 0 0 6 0z"/>',
    "sliders": '<path d="M4 7h10M18 7h2M4 17h4M12 17h8"/><circle cx="16" cy="7" r="2"/><circle cx="10" cy="17" r="2"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l8.5-8.5M16 7l3 3M14 9l2 2"/>',
    "camera": '<path d="M4 8h3l2-2.5h6L17 8h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.6 3.5 5.4 3.5 8.5s-1 5.9-3.5 8.5c-2.5-2.6-3.5-5.4-3.5-8.5s1-5.9 3.5-8.5z"/>',
    "shield": '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 8-7.5 9.5-4.3-1.5-7.5-5-7.5-9.5V6z"/><path d="M8.5 12l2.5 2.5 4.5-4.5"/>',
    "chart": '<path d="M4 19.5h16"/><path d="M6.5 16l4-5 3 2.5 4.5-6.5"/><path d="M15 7h3v3"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/><circle cx="12" cy="15.5" r="1.3"/>',
    "phone": '<path d="M6.5 3.5h3l1.5 4.5-2.3 1.4a11 11 0 0 0 5.9 5.9l1.4-2.3 4.5 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.5 5.7a2 2 0 0 1 2-2.2z"/>',
    "chat": '<path d="M12 3.5a8.5 8.5 0 0 0-7.4 12.7L3.5 20.5l4.4-1.1A8.5 8.5 0 1 0 12 3.5z"/><path d="M9.2 8.6c.3-.4.8-.4 1 0l.8 1.6c.1.3 0 .6-.2.8l-.5.5a5.6 5.6 0 0 0 2.7 2.7l.5-.5c.2-.2.5-.3.8-.2l1.6.8c.4.2.4.7 0 1-.7.7-1.7 1-2.6.6a8.4 8.4 0 0 1-4.7-4.7c-.4-.9-.1-1.9.6-2.6z"/>',
    "mail": '<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="M3.5 7l8.5 6.5L20.5 7"/>',
    "pin": '<path d="M12 21s-6.5-6.1-6.5-11a6.5 6.5 0 0 1 13 0c0 4.9-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    "train": '<rect x="5.5" y="3.5" width="13" height="13" rx="3"/><path d="M5.5 10.5h13M9 20.5l1.5-4M15 20.5l-1.5-4"/><circle cx="9" cy="13.5" r=".8"/><circle cx="15" cy="13.5" r=".8"/>',
    "eye": '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
    "users": '<circle cx="9" cy="8.5" r="3.5"/><path d="M2.5 20c.6-3.6 3.2-5.5 6.5-5.5s5.9 1.9 6.5 5.5"/><path d="M15.5 5.2a3.5 3.5 0 0 1 0 6.6M18 14.8c2 .6 3.2 2.4 3.5 5.2"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "star": '<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z"/>',
    "id": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="11" r="2.2"/><path d="M5.5 16c.5-1.6 1.6-2.4 3-2.4s2.5.8 3 2.4M14 10h4.5M14 13.5h3"/>',
    "family": '<circle cx="7" cy="6.5" r="2.5"/><circle cx="17" cy="6.5" r="2.5"/><circle cx="12" cy="12.5" r="2"/><path d="M3 20v-4.5a4 4 0 0 1 8 0M13 15.5a4 4 0 0 1 8 0V20M9.5 20v-1.5a2.5 2.5 0 0 1 5 0V20"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "out": '<path d="M7 17L17 7M9 7h8v8"/>',
    "home": '<path d="M3.5 11l8.5-7 8.5 7v9.5h-17z"/><path d="M9.5 20.5v-6h5v6"/>',
    "coffee": '<path d="M4 9h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5zM17 10.5h1.5a2.5 2.5 0 0 1 0 5H17"/><path d="M8 3.5c-.8 1 .8 2 0 3M12 3.5c-.8 1 .8 2 0 3"/>',
    "brush": '<path d="M14 4l6 6-7.5 7.5-6-6z"/><path d="M6.5 11.5L3.5 20.5l9-3"/>',
    "instagram": '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".9"/>',
    "facebook": '<path d="M14 8.5h2.5V5h-2.5A3.5 3.5 0 0 0 10.5 8.5V11H8v3.5h2.5V21H14v-6.5h2.5L17 11h-3V9a.5.5 0 0 1 .5-.5z"/>',
    "linkedin": '<rect x="3.5" y="3.5" width="17" height="17" rx="3.5"/><path d="M8 10.5V16.5M11.5 16.5v-6M11.5 13.2c0-1.7 1-2.7 2.4-2.7s2.1 1 2.1 2.7v3.3"/><circle cx="8" cy="7.6" r=".4"/>',
    "youtube": '<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10.2 9.2v5.6l4.8-2.8z"/>',
    "tiktok": '<path d="M13.5 3.5v11.3a3.3 3.3 0 1 1-3.3-3.3"/><path d="M13.5 3.5c.4 2.5 2.1 4.2 4.8 4.5"/>',
    "bubble": '<path d="M20.5 11.5a8 8 0 0 1-11.9 7L4 19.8l1.3-4.4A8 8 0 1 1 20.5 11.5z"/><path d="M8.6 11.6h.01M12.5 11.6h.01M16.4 11.6h.01" stroke-width="2.6"/>',
    "cookie": '<path d="M20.5 12.6A8.5 8.5 0 1 1 11.4 3.5a2.8 2.8 0 0 0 3.4 3.4 2.8 2.8 0 0 0 3.3 3.3 2.8 2.8 0 0 0 2.4 2.4z"/><path d="M8.3 10.2h.01M11.8 15.6h.01M15.6 14.2h.01M8.4 15h.01" stroke-width="2.4"/>',
    "close": '<path d="M6.5 6.5l11 11M17.5 6.5l-11 11"/>',
    "help": '<circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.5a2.5 2.5 0 0 1 4.9.7c0 1.7-2.5 2.1-2.5 3.6"/><path d="M12 16.8h.01" stroke-width="2.6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
}


def icon(name, cls="ico", label=None):
    aria = f'role="img" aria-label="{escape(label)}"' if label else 'aria-hidden="true"'
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" {aria}>{ICONS[name]}</svg>')


# Le logo : une porte en arc, comme l'entrée d'un immeuble parisien.
# Les couleurs du trait suivent la place du logo (--mark-fg) : vert anis sur bleu nuit, bleu nuit sur pervenche.
MARK = ('<svg class="mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="currentColor"/>'
        '<path d="M10.5 25V15a5.5 5.5 0 0 1 11 0v10" fill="none" style="stroke:var(--mark-fg,#FBF2E8)" stroke-width="2.4" stroke-linecap="round"/>'
        '<path d="M8 25h16" style="stroke:var(--mark-fg,#FBF2E8)" stroke-width="2.4" stroke-linecap="round"/>'
        '<circle cx="18.6" cy="19.6" r="1.6" fill="#FC585C"/></svg>')


def logo(L, cls="logo"):
    t = tr(L)
    return (f'<a class="{cls}" href="{url("home", L)}" aria-label="{t("EdenFlats, accueil", "EdenFlats, home")}">'
            f'{MARK}<span>Eden<b>Flats</b></span></a>')


# ── Petits composants ───────────────────────────────────────────────────────
def chip(text, tone=""):
    return f'<span class="chip {tone}">{text}</span>'


def btn(href, text, kind="", ext=False, ico="arrow"):
    attrs = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="btn {kind}" href="{href}"{attrs}><span>{text}</span><i>{icon(ico)}</i></a>'


def more(href, text, ext=False):
    attrs = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="more" href="{href}"{attrs}>{text} {icon("out" if ext else "arrow")}</a>'


def todo(label):
    return f'<b class="todo">{label}</b>'


def fcard(tag, tone, text, cls="", ico="check"):
    """Carte blanche posée sur une photo, avec une étiquette de couleur (motif repris de Bridge)."""
    return (f'<div class="fc {cls}"><span class="tag {tone}">{icon(ico)}{tag}</span>'
            f'<p>{text}</p></div>')


def photo(name, alt, sizes="(max-width: 900px) 100vw, 50vw", lazy=True, cls="", big=1600):
    """Photo en deux tailles (800 px et grande) : le navigateur prend la plus légère qui suffit."""
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="/assets/img/{name}.jpg" srcset="/assets/img/{name}-800.jpg 800w, '
            f'/assets/img/{name}.jpg {big}w" sizes="{sizes}" alt="{escape(alt)}"{load}>')


def sticker(name, tone="", cls=""):
    """Pastille ronde illustrée posée sur le bord d'une photo."""
    bg = tone or "light"
    style = "" if tone else ' style="background:#fff;color:var(--ink)"'
    return f'<div class="sticker {bg} {cls}"{style} aria-hidden="true">{illu(name)}</div>'


def ticks(items, cls="ticks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in items) + "</ul>"


def head(label, h2, intro="", center=False, hid=""):
    c = " center" if center else ""
    hid_attr = f' id="{hid}"' if hid else ""
    intro_html = f'<p class="intro">{intro}</p>' if intro else ""
    return f'<div class="shead{c}">{chip(label)}<h2{hid_attr}>{h2}</h2>{intro_html}</div>'


def faq_list(items):
    return '<div class="faq">' + "".join(
        f'<details><summary><span>{q}</span><i aria-hidden="true"></i></summary><div class="ans">{a}</div></details>'
        for q, a in items) + "</div>"


def crumbs(L, trail):
    """trail : liste de (texte, adresse) ; le dernier élément est la page courante."""
    t = tr(L)
    items = [(t("Accueil", "Home"), url("home", L))] + trail
    parts = []
    for i, (txt, href) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<span aria-current="page">{txt}</span>')
        else:
            parts.append(f'<a href="{href}">{txt}</a>')
    return f'<nav class="crumbs" aria-label="{t("Fil d’Ariane", "Breadcrumb")}">' + '<span aria-hidden="true">/</span>'.join(parts) + "</nav>"


def crumbs_ld(L, trail):
    t = tr(L)
    items = [(t("Accueil", "Home"), url("home", L))] + trail
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": re.sub("<[^>]+>", "", n), "item": SITE["url"] + h}
        for i, (n, h) in enumerate(items)]}


ORG_ID = SITE["url"] + "/#entreprise"
SITE_ID = SITE["url"] + "/#site"


def org_ld(L):
    c = SITE["company"]
    t = tr(L)
    d = {
        "@context": "https://schema.org", "@type": "ProfessionalService", "@id": ORG_ID,
        "name": "EdenFlats", "legalName": c["name"], "url": SITE["url"] + "/",
        "logo": SITE["url"] + "/assets/img/apple-touch-icon.png", "image": SITE["url"] + "/assets/img/og-image.jpg",
        "description": t("Conciergerie Airbnb à Paris et en Île-de-France : gestion locative saisonnière de résidences secondaires et de biens locatifs.",
                         "Airbnb management in Paris and Île-de-France: short-term rental management for second homes and buy-to-let properties."),
        "telephone": SITE["phone_href"], "email": SITE["email"],
        "address": {"@type": "PostalAddress", "streetAddress": "14 rue de Champigny", "postalCode": "94370",
                    "addressLocality": "Sucy-en-Brie", "addressRegion": "Île-de-France", "addressCountry": "FR"},
        "areaServed": [{"@type": "City", "name": "Paris"}, {"@type": "AdministrativeArea", "name": "Île-de-France"}],
        "knowsLanguage": ["fr", "en"],
        "identifier": {"@type": "PropertyValue", "propertyID": "SIRET", "value": c["siret"].replace(" ", "")},
    }
    # Seules les pages renseignées dans SITE["social"] sont déclarées aux moteurs de recherche.
    same = [href for _, _, href in SITE["social"] if href]
    if same:
        d["sameAs"] = same
    return d


def website_ld(L):
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE_ID, "url": SITE["url"] + url("home", L),
            "name": "EdenFlats", "inLanguage": "fr-FR" if L == "fr" else "en-GB", "publisher": {"@id": ORG_ID}}


def service_ld(L, name, desc, path, area=None, service_type=None):
    d = {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc,
         "url": SITE["url"] + path, "provider": {"@id": ORG_ID}, "inLanguage": "fr-FR" if L == "fr" else "en-GB",
         "serviceType": service_type or ("Conciergerie Airbnb" if L == "fr" else "Airbnb management")}
    d["areaServed"] = {"@type": "Place", "name": area} if area else [{"@type": "City", "name": "Paris"},
                                                                    {"@type": "AdministrativeArea", "name": "Île-de-France"}]
    return d


def contact_buttons(L, on_dark=False):
    t = tr(L)
    s = SITE
    ghost = "ghost-light" if on_dark else "ghost"
    return (f'<div class="cta-row">'
            f'{btn("https://wa.me/" + s["whatsapp"], t("Écrire sur WhatsApp", "Message us on WhatsApp"), "green", ext=True, ico="chat")}'
            f'{btn("tel:" + s["phone_href"], s["phone"], "light" if on_dark else "", ico="phone")}'
            f'{btn("mailto:" + s["email"], t("Envoyer un e-mail", "Send an email"), ghost, ico="mail")}'
            f'</div>')


def social_links(L, cls="social"):
    """Icônes des réseaux sociaux. Sans adresse, l'icône reste visible mais n'est pas un lien."""
    t = tr(L)
    out = []
    for key, name, href in SITE["social"]:
        if href:
            out.append(f'<a href="{href}" target="_blank" rel="noopener" aria-label="{name}">{icon(key)}</a>')
        else:
            label = f'{name} ({t("bientôt", "coming soon")})'
            out.append(f'<span class="soon" role="img" aria-label="{label}" title="{label}">{icon(key)}</span>')
    return f'<div class="{cls}">{"".join(out)}</div>' if out else ""


# ── Typographie ─────────────────────────────────────────────────────────────
def typo(html, L):
    """Apostrophes typographiques partout ; en français, espaces insécables avant : ; ! ? % et dans « »."""
    out = []
    for part in re.split(r"(<script.*?</script>|<style.*?</style>|<[^>]+>)", html, flags=re.S):
        if part.startswith("<"):
            out.append(part)
            continue
        part = re.sub(r"(?<=\w)'(?=\w)", "’", part)
        part = re.sub(r"(?<=s)'(?=[\s.,;:!?)<]|$)", "’", part)
        if L == "fr":
            part = re.sub(r" ([;!?%»])", "\u00a0\\1", part)
            part = re.sub(r" :(?=\s|$)", "\u00a0:", part)
            part = part.replace("« ", "«\u00a0")
        out.append(part)
    return "".join(out)


# ── Gabarit ─────────────────────────────────────────────────────────────────
def nav_items(L):
    t = tr(L)
    return [("voyageurs", t("Gestion des voyageurs", "Guest management")),
            ("logement", t("Gestion du logement", "Property management")),
            ("formules", t("Nos formules", "Plans")),
            ("paris", "Paris"),
            ("faq", "FAQ")]


def final_cta(L, title=None, text=None):
    t = tr(L)
    title = title or t('<span class="o">Vous souhaitez nous rejoindre ?</span> Notre équipe est prête à mettre votre bien en valeur.',
                       '<span class="o">Ready to join us?</span> Our team is ready to show your property at its best.')
    text = text or t("Dites-nous où se trouve votre logement et ce que vous souhaitez nous confier. Nous vous répondons par téléphone, sur WhatsApp ou par e-mail.",
                     "Tell us where your property is and what you would like us to handle. We will get back to you by phone, WhatsApp or email.")
    badges = "".join(f'<span class="badge">{icon("check")}{b}</span>' for b in (
        t("Revenu garanti ou réel", "Guaranteed or actual income"),
        t("Assistance 24h/24", "24/7 guest support"),
        t("Annonce en français et en anglais", "Listing in French and English")))
    return f"""<section class="final" aria-labelledby="final-t">
  <div class="wrap final-grid">
    <div><h2 id="final-t">{title}</h2><p>{text}</p><div class="badges">{badges}</div></div>
    <div class="final-actions">{contact_buttons(L, on_dark=True)}</div>
  </div>
</section>"""


def footer(L, areas, towns):
    """Pied de page pervenche de la maquette : logo, colonnes en petites capitales, réseaux, retour en haut."""
    t = tr(L)
    s = SITE
    area_links = "".join(f'<li><a href="{h}">{n}</a></li>' for n, h in areas)
    town_links = "".join(f'<li><a href="{h}">{n}</a></li>' for n, h in towns)
    year = date.today().year
    # Retirer son accord doit être aussi simple que le donner : ce bouton rouvre le bandeau cookies.
    manage = (f'<li><button class="linkish" type="button" data-consent-open>{t("Gérer les cookies", "Cookie settings")}</button></li>'
              if s["cookie_banner"] else "")
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-mark"><a href="{url('home', L)}" aria-label="{t("EdenFlats, accueil", "EdenFlats, home")}">{MARK}</a></div>
      <div><h3>{t("Informations", "Information")}</h3><ul>
        <li><a href="{url('mentions', L)}">{t("Mentions légales", "Legal notice")}</a></li>
        <li><a href="{url('cgv', L)}">{t("Conditions générales de vente", "Terms and conditions")}</a></li>
        <li><a href="{url('confidentialite', L)}">{t("Confidentialité et cookies", "Privacy and cookies")}</a></li>
        {manage}
        <li><a href="{url('plan', L)}">{t("Plan du site", "Sitemap")}</a></li></ul></div>
      <div><h3>{t("Services", "Services")}</h3><ul>
        <li><a href="{url('voyageurs', L)}">{t("Gestion des voyageurs", "Guest management")}</a></li>
        <li><a href="{url('logement', L)}">{t("Gestion du logement", "Property management")}</a></li>
        <li><a href="{url('formules', L)}">{t("Nos formules", "Our plans")}</a></li>
        <li><a href="{url('faq', L)}">{t("Questions fréquentes", "FAQ")}</a></li>
        <li><a href="{s['booking']}" target="_blank" rel="noopener">{t("Réserver un séjour", "Book a stay")} ↗</a></li></ul></div>
      <div><h3><a href="{url('paris', L)}">Paris</a></h3><ul class="cols2">{area_links}</ul>
        <h3 class="mt">{t("Île-de-France", "Île-de-France")}</h3><ul>{town_links}</ul></div>
      <div><h3>{t("Contactez-nous", "Contact us")}</h3>
        <ul class="foot-contact">
          <li><a href="tel:{s['phone_href']}">{icon("phone")}{s['phone']}</a></li>
          <li><a href="https://wa.me/{s['whatsapp']}" target="_blank" rel="noopener">{icon("chat")}WhatsApp</a></li>
          <li><a href="mailto:{s['email']}">{icon("mail")}{s['email']}</a></li>
          <li><a href="{url('contact', L)}">{icon("arrow")}{t("Page contact", "Contact page")}</a></li>
        </ul>
        {social_links(L)}
      </div>
    </div>
    <div class="foot-bottom">
      <span>Copyright © {year} EdenFlats · {t("Site conçu par", "Website by")} <a href="{s['maker'][1]}" target="_blank" rel="noopener">{s['maker'][0]}</a></span>
    </div>
  </div>
  <a class="to-top" href="#top" aria-label="{t("Revenir en haut de la page", "Back to top")}">{icon("arrow")}</a>
</footer>"""


def bubble(L, pid):
    """Petit bouton de contact fixé en bas de l'écran ; il apparaît une fois passé le haut de page."""
    if pid == "contact":
        return ""
    t = tr(L)
    return (f'<a class="bubble" href="{url("contact", L)}"><i>{icon("bubble")}</i>'
            f'<span>{t("Nous contacter", "Contact us")}</span></a>\n')


def consent_template(L):
    """Bandeau cookies, inséré par main.js tant que le visiteur n'a pas choisi (choix gardé six mois)."""
    if not SITE["cookie_banner"]:
        return ""
    t = tr(L)
    return f"""<template id="tpl-cookies">
<div class="consent" role="region" aria-label="Cookies">
  <p class="consent-t">{icon("cookie")}<b>{t("Cookies", "Cookies")}</b></p>
  <p>{t("Nous aimerions mesurer la fréquentation du site pour l'améliorer. Ces cookies ne sont déposés qu'avec votre accord ; vous pouvez changer d'avis à tout moment en bas de page.",
        "We would like to measure visits to the site to improve it. These cookies are only set with your consent, and you can change your mind at any time from the footer.")}</p>
  <div class="consent-actions"><button type="button" data-consent="non">{t("Refuser", "Decline")}</button><button type="button" data-consent="oui">{t("Accepter", "Accept")}</button></div>
  <a class="consent-more" href="{url('confidentialite', L)}#cookies">{t("En savoir plus", "Learn more")}</a>
</div>
</template>
"""


def language_template(L, target):
    """Proposition de changer de langue quand celle du navigateur ne correspond pas à la page.
    Elle est écrite dans l'autre langue : c'est celle que lit le visiteur à qui elle s'adresse."""
    if L == "fr":
        lang, text, go, stay, close = ("en", "<b>It looks like you don't speak French.</b> Would you like to see the website in English?",
                                       "View in English", "Stay in French", "Close")
    else:
        lang, text, go, stay, close = ("fr", "<b>Vous parlez français ?</b> Ce site existe aussi en français.",
                                       "Voir en français", "Rester en anglais", "Fermer")
    return f"""<template id="tpl-langue">
<div class="langprompt" lang="{lang}" role="dialog" aria-labelledby="lp-t">
  {illu("langues")}
  <div><p id="lp-t">{text}</p>
    <div class="lp-actions"><a class="btn small" href="{target}" hreflang="{lang}" data-lang="{lang}"><span>{go}</span><i>{icon("arrow")}</i></a><button class="linkish" type="button" data-lang="{L}">{stay}</button></div></div>
  <button class="lp-close" type="button" aria-label="{close}" data-lang="{L}">{icon("close")}</button>
</div>
</template>
"""


# Lancé dans <head>, avant le premier affichage : pose html.m-on pour que les éléments animés partent cachés
# (sinon ils apparaîtraient, puis disparaîtraient le temps que motion.js démarre). Rien de caché si le visiteur
# demande moins d'animations ; et si motion.js ne s'est pas lancé au bout de 4 s, tout est réaffiché.
HEAD_JS = ("<script>(function(d){d.classList.remove('no-js');"
           "if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver' in window){"
           "d.classList.add('m-on');try{if(document.referrer.indexOf(location.origin)===0)d.classList.add('m-nav')}catch(e){}"
           "setTimeout(function(){if(!window.efMotion)d.classList.remove('m-on')},4000)}})(document.documentElement)</script>")


def layout(L, pid, title, desc, body, areas, towns, *, alt_path=None, path=None, ld=None, cta=True,
           cta_title=None, cta_text=None, og_image="/assets/img/og-image.jpg", og_alt=None, noindex=False, section=None):
    t = tr(L)
    path = path or url(pid, L)
    alt_path = alt_path or (url(pid, OTHER[L]) if pid in ROUTES else None)
    fr_path, en_path = (path, alt_path) if L == "fr" else (alt_path, path)
    hreflang = ""
    if alt_path:
        hreflang = (f'<link rel="alternate" hreflang="fr" href="{SITE["url"]}{fr_path}">\n'
                    f'<link rel="alternate" hreflang="en" href="{SITE["url"]}{en_path}">\n'
                    f'<link rel="alternate" hreflang="x-default" href="{SITE["url"]}{fr_path}">\n')
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (ld or []))
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{url(k, L)}"{cur if url(k, L) == path or k == section else ""}>{n}</a>'
                  for k, n in nav_items(L))
    other = OTHER[L]
    switch = (f'<a class="lang" href="{alt_path}" hreflang="{other}" lang="{other}" '
              f'aria-label="{t("English version", "Version française")}">{other.upper()}</a>') if alt_path else ""
    robots = ('<meta name="robots" content="noindex">' if noindex
              else '<meta name="robots" content="index, follow, max-image-preview:large">') + "\n"
    og_alt = og_alt or title
    ga4 = SITE["analytics"]["ga4"] if SITE["cookie_banner"] else ""
    body_attrs = f' data-ga4="{escape(ga4)}"' if ga4 else ""
    html = f"""<!doctype html>
<html lang="{L}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{HEAD_JS}
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
{robots}<link rel="canonical" href="{SITE['url']}{path}">
{hreflang}<meta property="og:type" content="website">
<meta property="og:site_name" content="EdenFlats">
<meta property="og:locale" content="{t('fr_FR', 'en_GB')}">
<meta property="og:locale:alternate" content="{t('en_GB', 'fr_FR')}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{SITE['url']}{path}">
<meta property="og:image" content="{SITE['url']}{og_image}">
<meta property="og:image:alt" content="{escape(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{SITE['url']}{og_image}">
<meta name="theme-color" content="#1B1B4B">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/instrument-serif-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/public-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
<link rel="stylesheet" href="/assets/motion.css">
{lds}</head>
<body id="top"{body_attrs}>
<a class="skip" href="#contenu">{t("Aller au contenu", "Skip to content")}</a>
<header class="top">
  <div class="wrap top-in">
    {logo(L)}
    <nav class="nav" id="menu" aria-label="{t("Menu principal", "Main menu")}">{nav}
      <a class="nav-contact" href="{url('contact', L)}">{t("Contact", "Contact")}</a></nav>
    <div class="top-actions">
      {switch}
      {btn(url('contact', L), t("Nous contacter", "Contact us"), "small hide-sm")}
      <button class="burger" type="button" aria-label="{t("Ouvrir le menu", "Open menu")}" aria-expanded="false" aria-controls="menu">{icon("menu")}</button>
    </div>
  </div>
</header>
<main id="contenu">
{body}
</main>
{final_cta(L, cta_title, cta_text) if cta else ""}
{footer(L, areas, towns)}
{bubble(L, pid)}{consent_template(L)}{language_template(L, alt_path or url("home", OTHER[L]))}<script src="/assets/main.js" defer></script><script src="/assets/motion.js" defer></script>
</body>
</html>
"""
    return typo(html, L)
