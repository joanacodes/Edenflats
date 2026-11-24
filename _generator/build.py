# Génère tout le site à la racine du dépôt : pages françaises et anglaises, plan du site, redirections
# des anciennes adresses Squarespace, icônes. Usage : py build.py (depuis _generator/).
from pathlib import Path

from PIL import Image, ImageDraw

import kit
import pages as P
import quartiers as Q

ROOT = Path(__file__).resolve().parent.parent

PAGES = [  # (identifiant, fonction)
    ("home", P.home), ("voyageurs", P.voyageurs), ("logement", P.logement), ("formules", P.formules),
    ("faq", P.faq_page), ("paris", Q.hub), ("contact", P.contact), ("mentions", P.mentions),
    ("confidentialite", P.confidentialite), ("credits", P.credits),
]

# Anciennes adresses Squarespace sans équivalent direct : une page qui redirige aussitôt.
# Les autres anciennes adresses (gestion des voyageurs, de propriété, FAQ, contact, Créteil, Saint-Maur,
# mentions légales) sont gardées telles quelles.
REDIRECTS = {
    "/accueil/": "/",
    "/conditions-generales-de-vente/": "/mentions-legales/",
    "/politique-de-cookies/": "/confidentialite/",
    "/boutique/": "/",
    "/erreur-404/": "/",
}

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#21190D"/>'
           '<path d="M10.5 25V15a5.5 5.5 0 0 1 11 0v10" fill="none" stroke="#DDF47E" stroke-width="2.4" stroke-linecap="round"/>'
           '<path d="M8 25h16" stroke="#DDF47E" stroke-width="2.4" stroke-linecap="round"/>'
           '<circle cx="18.6" cy="19.6" r="1.4" fill="#DDF47E"/></svg>')


def write(rel, html):
    out = ROOT / rel.lstrip("/")
    if rel.endswith("/"):
        out = out / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def redirect_page(target):
    full = kit.SITE["url"] + target
    return (f'<!doctype html>\n<html lang="fr"><head><meta charset="utf-8"><title>EdenFlats</title>'
            f'<meta name="robots" content="noindex"><link rel="canonical" href="{full}">'
            f'<meta http-equiv="refresh" content="0; url={target}"></head>'
            f'<body><p><a href="{target}">EdenFlats</a></p></body></html>\n')


def icons():
    """Icône pour l'écran d'accueil des téléphones (180 px) et image de partage (1200 × 630)."""
    img = ROOT / "assets" / "img"
    s = 4  # dessin en grand puis réduction, pour des bords lisses
    im = Image.new("RGBA", (180 * s, 180 * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, 180 * s - 1, 180 * s - 1], radius=40 * s, fill="#21190D")
    lime, w = "#DDF47E", 13 * s
    d.arc([59 * s, 55 * s, 121 * s, 117 * s], 180, 360, fill=lime, width=w)
    d.line([65 * s, 86 * s, 65 * s, 141 * s], fill=lime, width=w)
    d.line([115 * s, 86 * s, 115 * s, 141 * s], fill=lime, width=w)
    d.line([45 * s, 141 * s, 135 * s, 141 * s], fill=lime, width=w)
    d.ellipse([97 * s, 103 * s, 113 * s, 119 * s], fill=lime)
    im.resize((180, 180), Image.LANCZOS).save(img / "apple-touch-icon.png")
    src = Image.open(img / "photo-salon-plantes.jpg").convert("RGB")
    ratio = 1200 / 630
    h = round(src.width / ratio)
    top = (src.height - h) // 2
    src.crop((0, top, src.width, top + h)).resize((1200, 630), Image.LANCZOS).save(img / "og-image.jpg", "JPEG", quality=82)


def main():
    areas_footer = {L: [(a[L]["name"], Q.area_url(a, L)) for a in Q.AREAS] for L in ("fr", "en")}
    towns_footer = {L: [(a[L]["name"], Q.area_url(a, L)) for a in Q.TOWNS] for L in ("fr", "en")}
    sitemap = []  # (adresse fr, adresse en)
    count = 0
    for L in ("fr", "en"):
        for pid, fn in PAGES:
            p = fn(L)
            html = kit.layout(L, pid, p["title"], p["desc"], p["body"], areas_footer[L], towns_footer[L],
                              ld=p.get("ld"), cta=p.get("cta", True), cta_title=p.get("cta_title"), cta_text=p.get("cta_text"))
            write(kit.url(pid, L), html)
            count += 1
            if L == "fr":
                sitemap.append((kit.url(pid, "fr"), kit.url(pid, "en")))
        for a in Q.AREAS + Q.TOWNS:
            p = Q.area_page(a, L)
            html = kit.layout(L, "area", p["title"], p["desc"], p["body"], areas_footer[L], towns_footer[L],
                              path=p["path"], alt_path=p["alt_path"], ld=p.get("ld"), cta_title=p.get("cta_title"))
            write(p["path"], html)
            count += 1
            if L == "fr":
                sitemap.append((p["path"], p["alt_path"]))
    nf = P.not_found("fr")
    (ROOT / "404.html").write_text(kit.layout("fr", "404", nf["title"], nf["desc"], nf["body"], areas_footer["fr"], towns_footer["fr"],
                                              path="/404.html", noindex=True, cta=False), encoding="utf-8")
    for old, new in REDIRECTS.items():
        write(old, redirect_page(new))
    base = kit.SITE["url"]
    urls = []
    for fr, en in sitemap:
        alts = (f'<xhtml:link rel="alternate" hreflang="fr" href="{base}{fr}"/>'
                f'<xhtml:link rel="alternate" hreflang="en" href="{base}{en}"/>'
                f'<xhtml:link rel="alternate" hreflang="x-default" href="{base}{fr}"/>')
        for u in (fr, en):
            urls.append(f"  <url><loc>{base}{u}</loc>{alts}</url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n", encoding="utf-8")
    (ROOT / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    icons()
    print(f"{count} pages, {len(REDIRECTS)} redirections, {len(urls)} adresses dans le plan du site")


if __name__ == "__main__":
    main()
