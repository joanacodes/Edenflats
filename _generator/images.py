# Prépare les images générées avec Midjourney (voir IMAGES-MIDJOURNEY.md à la racine du dépôt).
# 1. Enregistrez chaque image dans _generator/sources/ sous le nom indiqué (ex. accueil-hero.png).
# 2. Lancez : py images.py
# Chaque image est recadrée au centre au bon format, puis enregistrée en deux tailles dans assets/img/
# (grande et 800 px), sous le nom attendu par les pages. Relancez ensuite py build.py.
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
SOURCES = HERE / "sources"
OUT = HERE.parent / "assets" / "img"

# nom : (largeur, hauteur) du format, largeur de la grande version
SLOTS = {
    "accueil-hero": ((4, 5), 1600), "accueil-voyageurs": ((6, 5), 1600), "accueil-logement": ((6, 5), 1600),
    "accueil-faq": ((6, 5), 1600), "voyageurs-hero": ((4, 5), 1600), "voyageurs-annonce": ((6, 5), 1600),
    "voyageurs-selection": ((6, 5), 1600), "logement-hero": ((4, 5), 1600), "logement-menage": ((6, 5), 1600),
    "logement-reassort": ((6, 5), 1600), "formules-hero": ((4, 5), 1600),
    # Page Paris, quartiers et communes.
    "paris": ((5, 4), 1280),
    **{f"paris-{k}": ((5, 4), 1280) for k in (
        "marais", "montmartre", "saint-germain-des-pres", "quartier-latin", "tour-eiffel", "champs-elysees", "opera",
        "louvre", "canal-saint-martin", "bastille", "montparnasse", "trocadero")},
    "ville-creteil": ((5, 4), 1280), "ville-saint-maur": ((5, 4), 1280),
}


def crop(im, ratio):
    w, h = im.size
    rw, rh = ratio
    if w / h > rw / rh:
        nw = round(h * rw / rh)
        return im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    nh = round(w * rh / rw)
    return im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))


def main():
    if not SOURCES.exists():
        SOURCES.mkdir()
        print(f"Dossier créé : {SOURCES}. Déposez-y les images, puis relancez.")
        return
    done = 0
    for f in sorted(SOURCES.iterdir()):
        if f.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
            continue
        name = f.stem.lower()
        im = Image.open(f).convert("RGB")
        if name == "og-image":
            crop(im, (1200, 630)).resize((1200, 630), Image.LANCZOS).save(OUT / "og-image.jpg", "JPEG", quality=84, optimize=True)
            print("og-image.jpg")
            done += 1
            continue
        if name not in SLOTS:
            print(f"  ? nom inconnu, ignoré : {f.name} (voir la liste dans IMAGES-MIDJOURNEY.md)")
            continue
        ratio, big = SLOTS[name]
        im = crop(im, ratio)
        for width, suffix, q in ((big, "", 80), (800, "-800", 78)):
            out = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS) if im.width > width else im
            out.save(OUT / f"{name}{suffix}.jpg", "JPEG", quality=q, optimize=True, progressive=True)
        print(f"{name}.jpg")
        done += 1
    print(f"{done} image(s) prête(s). Lancez maintenant : py build.py")


if __name__ == "__main__":
    sys.exit(main())
