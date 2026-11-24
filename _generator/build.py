# Génère tout le site à la racine du dépôt : pages françaises et anglaises, plan du site, redirections
# des anciennes adresses Squarespace, llms.txt, icônes. Usage : py build.py (depuis _generator/).
#
# Chaque page est un fichier .html servi sans extension (/faq sert faq.html) : les adresses françaises
# sont ainsi exactement celles de l'ancien site, sans barre finale.
import re
from datetime import date
from html import unescape
from pathlib import Path

from PIL import Image, ImageDraw

import faq
import illus
import kit
import pages as P
import quartiers as Q

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = Path(__file__).resolve().parent / ".fichiers-generes"
TODAY = date.today().isoformat()

PAGES = [  # (identifiant, fonction)
    ("home", P.home), ("voyageurs", P.voyageurs), ("logement", P.logement), ("formules", P.formules),
    ("faq", P.faq_page), ("paris", Q.hub), ("contact", P.contact), ("mentions", P.mentions), ("cgv", P.cgv),
    ("confidentialite", P.confidentialite), ("credits", P.credits), ("plan", P.plan_du_site),
]

# Anciennes adresses Squarespace sans équivalent : une page qui redirige aussitôt vers la plus proche.
# Les autres anciennes adresses (gestion des voyageurs, de propriété, FAQ, contact, Créteil, Saint-Maur,
# mentions légales, conditions générales de vente, politique de cookies) sont servies telles quelles.
REDIRECTS = {
    "/accueil": "/",
    "/boutique": "/",
    "/erreur-404": "/",
}

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#24485C"/>'
           '<path d="M10.5 25V15a5.5 5.5 0 0 1 11 0v10" fill="none" stroke="#FBF2E8" stroke-width="2.4" stroke-linecap="round"/>'
           '<path d="M8 25h16" stroke="#FBF2E8" stroke-width="2.4" stroke-linecap="round"/>'
           '<circle cx="18.6" cy="19.6" r="1.6" fill="#FC585C"/></svg>')

# Jekyll (GitHub Pages) publie le dossier tel quel, sauf ces fichiers de travail.
JEKYLL = "exclude:\n  - README.md\n  - IMAGES-MIDJOURNEY.md\n  - _generator\n"

written = []


def file_for(path):
    if path == "/":
        return ROOT / "index.html"
    if path.endswith("/"):
        return ROOT / path.strip("/") / "index.html"
    return ROOT / (path.lstrip("/") + ".html")


def write(path, html):
    out = file_for(path) if path.startswith("/") else ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    written.append(str(out.relative_to(ROOT)))


def redirect_page(target):
    full = kit.SITE["url"] + target
    return (f'<!doctype html>\n<html lang="fr"><head><meta charset="utf-8"><title>EdenFlats</title>'
            f'<meta name="robots" content="noindex"><link rel="canonical" href="{full}">'
            f'<meta http-equiv="refresh" content="0; url={target}"></head>'
            f'<body><p><a href="{target}">EdenFlats</a></p></body></html>\n')


def icons():
    """Icône d'écran d'accueil (180 px) et, faute d'image Midjourney dédiée, image de partage (1200 × 630)."""
    img = ROOT / "assets" / "img"
    s = 4  # dessin en grand puis réduction, pour des bords lisses
    im = Image.new("RGBA", (180 * s, 180 * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, 180 * s - 1, 180 * s - 1], radius=40 * s, fill="#24485C")
    cream, w = "#FBF2E8", 13 * s
    d.arc([59 * s, 55 * s, 121 * s, 117 * s], 180, 360, fill=cream, width=w)
    d.line([65 * s, 86 * s, 65 * s, 141 * s], fill=cream, width=w)
    d.line([115 * s, 86 * s, 115 * s, 141 * s], fill=cream, width=w)
    d.line([45 * s, 141 * s, 135 * s, 141 * s], fill=cream, width=w)
    d.ellipse([96 * s, 102 * s, 114 * s, 120 * s], fill="#FC585C")
    im.resize((180, 180), Image.LANCZOS).save(img / "apple-touch-icon.png")
    og = img / "og-image.jpg"
    if not og.exists():
        src = Image.open(img / "accueil-faq.jpg").convert("RGB")
        h = round(src.width / (1200 / 630))
        top = (src.height - h) // 2
        src.crop((0, top, src.width, top + h)).resize((1200, 630), Image.LANCZOS).save(og, "JPEG", quality=82)


def plain(html):
    text = re.sub(r"<li>", "\n- ", html)
    text = re.sub(r"</p>|<br\s*/?>", "\n", text)
    return re.sub(r"[ \t]+", " ", unescape(re.sub(r"<[^>]+>", "", text))).strip()


def llms(entries):
    """llms.txt : résumé du site et liste des pages pour les assistants IA ; llms-full.txt : le contenu utile en texte."""
    base = kit.SITE["url"]
    c = kit.SITE["company"]
    head = ("# EdenFlats\n\n"
            "> Conciergerie Airbnb à Paris et en Île-de-France : gestion locative saisonnière de résidences secondaires et de "
            "biens locatifs (annonce, sélection des voyageurs, remise des clés, ménage, linge, entretien, assistance 24h/24). "
            "Deux formules : revenu garanti (marge moyenne de 15 %) ou revenu réel (commission de 18 à 25 % selon la durée de location). "
            "Site en français et en anglais.\n\n"
            f"EdenFlats est exploitée par {c['name']} ({c['acronym']}), SAS, {c['address']}, SIRET {c['siret']}. "
            f"Contact : {kit.SITE['phone']} (téléphone et WhatsApp), {kit.SITE['email']}.\n")
    groups = {"fr": [], "en": [], "areas_fr": [], "areas_en": []}
    for e in entries:
        line = f"- [{e['name']}]({base}{e['path']}): {e['desc']}"
        groups[e["group"]].append(line)
    out = (head + "\n## Pages principales\n\n" + "\n".join(groups["fr"])
           + "\n\n## Quartiers de Paris et communes d'Île-de-France\n\n" + "\n".join(groups["areas_fr"])
           + "\n\n## English\n\n" + "\n".join(groups["en"])
           + "\n\n## English: Paris neighbourhoods\n\n" + "\n".join(groups["areas_en"])
           + f"\n\n## Optional\n\n- [Texte complet du site (FAQ, formules, quartiers)]({base}/llms-full.txt)\n- [Plan du site XML]({base}/sitemap.xml)\n")
    (ROOT / "llms.txt").write_text(out, encoding="utf-8")
    written.append("llms.txt")
    full = [head]
    for L, title in (("fr", "Questions fréquentes"), ("en", "Frequently asked questions")):
        full.append(f"\n## {title}\n")
        for fr_t, en_t, ids in faq.GROUPS:
            full.append(f"\n### {fr_t if L == 'fr' else en_t}\n")
            for q, a in faq.pick(L, ids):
                full.append(f"\n**{q}**\n\n{plain(a)}\n")
    for L, title in (("fr", "Quartiers et communes"), ("en", "Neighbourhoods and towns")):
        full.append(f"\n## {title}\n")
        for a in Q.AREAS + Q.TOWNS:
            d = a[L]
            full.append(f"\n### {d['name']} ({d['arr']}) — {base}{Q.area_url(a, L)}\n\n{d['lead']}\n\n{d['p1']}\n\n{d['p2']}\n\n{d['ours']}\n")
    (ROOT / "llms-full.txt").write_text("".join(full), encoding="utf-8")
    written.append("llms-full.txt")


def check(title, desc, where):
    """Signale les titres et descriptions trop longs ou trop courts pour Google."""
    t, d = unescape(title), unescape(desc)
    if len(t) > 65:
        print(f"  ! titre long ({len(t)}) : {where} — {t}")
    if not 110 <= len(d) <= 170:
        print(f"  ! description ({len(d)}) : {where} — {d[:70]}…")


def main():
    old = MANIFEST.read_text(encoding="utf-8").split("\n") if MANIFEST.exists() else []
    illus.write(ROOT)
    areas_footer = {L: [(a[L]["name"], Q.area_url(a, L)) for a in Q.AREAS] for L in ("fr", "en")}
    towns_footer = {L: [(a[L]["name"], Q.area_url(a, L)) for a in Q.TOWNS] for L in ("fr", "en")}
    sitemap, entries = [], []
    for L in ("fr", "en"):
        for pid, fn in PAGES:
            p = fn(L)
            check(p["title"], p["desc"], kit.url(pid, L))
            html = kit.layout(L, pid, p["title"], p["desc"], p["body"], areas_footer[L], towns_footer[L],
                              ld=p.get("ld"), cta=p.get("cta", True), cta_title=p.get("cta_title"), cta_text=p.get("cta_text"),
                              og_image=p.get("og_image", "/assets/img/og-image.jpg"), og_alt=p.get("og_alt"), section=p.get("section"))
            write(kit.url(pid, L), html)
            if L == "fr":
                sitemap.append((kit.url(pid, "fr"), kit.url(pid, "en"), p.get("image")))
            entries.append({"group": L, "name": re.sub(r"\s*\|\s*EdenFlats$", "", unescape(p["title"])), "path": kit.url(pid, L), "desc": unescape(p["desc"])})
        for a in Q.AREAS + Q.TOWNS:
            p = Q.area_page(a, L)
            check(p["title"], p["desc"], p["path"])
            html = kit.layout(L, "area", p["title"], p["desc"], p["body"], areas_footer[L], towns_footer[L],
                              path=p["path"], alt_path=p["alt_path"], ld=p.get("ld"), cta_title=p.get("cta_title"),
                              og_image=p["og_image"], og_alt=p["og_alt"], section=p.get("section"))
            write(p["path"], html)
            if L == "fr":
                sitemap.append((p["path"], p["alt_path"], p.get("image")))
            entries.append({"group": "areas_" + L, "name": a[L]["name"], "path": p["path"], "desc": a[L]["teaser"]})
    nf = P.not_found("fr")
    write("404.html", kit.layout("fr", "404", nf["title"], nf["desc"], nf["body"], areas_footer["fr"], towns_footer["fr"],
                                 path="/404", noindex=True, cta=False))
    for src, target in REDIRECTS.items():
        write(src, redirect_page(target))
    # Pour Cloudflare Pages ou Netlify : vraies redirections 301 (GitHub Pages utilise les pages ci-dessus).
    write("_redirects", "".join(f"{src} {target} 301\n" for src, target in REDIRECTS.items()))
    base = kit.SITE["url"]
    urls = []
    for fr, en, image in sitemap:
        alts = (f'<xhtml:link rel="alternate" hreflang="fr" href="{base}{fr}"/>'
                f'<xhtml:link rel="alternate" hreflang="en" href="{base}{en}"/>'
                f'<xhtml:link rel="alternate" hreflang="x-default" href="{base}{fr}"/>')
        img = f"<image:image><image:loc>{base}{image}</image:loc></image:image>" if image else ""
        for u in (fr, en):
            urls.append(f"  <url><loc>{base}{u}</loc><lastmod>{TODAY}</lastmod>{alts}{img}</url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" '
          'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(urls) + "\n</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n")
    write("favicon.svg", FAVICON)
    write("_config.yml", JEKYLL)
    llms(entries)
    icons()
    # Supprime les pages générées par une version précédente qui n'existent plus (et seulement celles-là).
    for rel in set(old) - set(written):
        f = ROOT / rel
        if rel and f.is_file() and (f.suffix in (".html", ".txt", ".xml") or f.name == "_redirects"):
            f.unlink()
            print("  supprimé :", rel)
    MANIFEST.write_text("\n".join(sorted(written)), encoding="utf-8")
    print(f"{len(written)} fichiers, {len(REDIRECTS)} redirections, {len(urls)} adresses dans le plan du site")


if __name__ == "__main__":
    main()
