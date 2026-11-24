# Cadres « Photo à venir » pour les emplacements dont l'image Midjourney n'est pas encore livrée.
# Usage : py placeholders.py paris paris-marais …  (sans argument : la page Paris, les quartiers et les communes).
# Chaque cadre porte le nom du fichier à fournir (voir IMAGES-MIDJOURNEY.md) ; images.py l'écrase ensuite
# avec la vraie image.
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import photos
import quartiers as Q

OUT = Path(__file__).resolve().parent.parent / "assets" / "img"
FONTS = ["/usr/share/fonts/truetype/dejavu/DejaVuSans{}.ttf", "C:/Windows/Fonts/arial{}.ttf"]


def font(size, bold=False):
    for f in FONTS:
        path = f.format(("-Bold" if "dejavu" in f else "bd") if bold else "")
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def frame(name, label, w=1280, h=1024):
    s = 2  # dessin en double taille puis réduction, pour des bords lisses
    im = Image.new("RGB", (w * s, h * s), "#FBF2E8")
    d = ImageDraw.Draw(im)
    ink, soft = "#24485C", "#B9A994"
    m = 44 * s
    for x in range(m, w * s - m, 28 * s):  # cadre pointillé
        d.line([(x, m), (x + 14 * s, m)], fill=soft, width=3 * s)
        d.line([(x, h * s - m), (x + 14 * s, h * s - m)], fill=soft, width=3 * s)
    for y in range(m, h * s - m, 28 * s):
        d.line([(m, y), (m, y + 14 * s)], fill=soft, width=3 * s)
        d.line([(w * s - m, y), (w * s - m, y + 14 * s)], fill=soft, width=3 * s)
    cx, cy = w * s // 2, h * s // 2 - 120 * s  # petite icône d'image : cadre, soleil, montagnes
    d.rounded_rectangle([cx - 90 * s, cy - 66 * s, cx + 90 * s, cy + 66 * s], radius=18 * s, outline=ink, width=6 * s)
    d.ellipse([cx + 22 * s, cy - 40 * s, cx + 52 * s, cy - 10 * s], outline="#FC585C", width=6 * s)
    d.line([(cx - 70 * s, cy + 46 * s), (cx - 22 * s, cy - 6 * s), (cx + 8 * s, cy + 22 * s), (cx + 28 * s, cy + 6 * s),
            (cx + 70 * s, cy + 46 * s)], fill=ink, width=6 * s, joint="curve")
    for text, size, bold, color, y in (("PHOTO À VENIR", 30, True, "#617079", cy + 120 * s),
                                       (name, 58, True, ink, cy + 190 * s),
                                       (label, 32, False, "#4E5F68", cy + 268 * s)):
        # Les pages de quartier recadrent la photo en hauteur : le texte doit tenir dans 60 % de la largeur.
        while True:
            f = font(size * s, bold)
            tw = d.textlength(text, font=f)
            if tw <= 0.6 * w * s or size <= 14:
                break
            size -= 2
        d.text((cx - tw / 2, y), text, font=f, fill=color)
    return im.resize((w, h), Image.LANCZOS)


def main(names):
    labels = {"paris": "Page Paris"}
    for a in Q.AREAS + Q.TOWNS:
        labels[photos.AREA[a["id"]]["file"]] = a["fr"]["name"]
    for name in names or list(labels):
        im = frame(name, f'{labels.get(name, "")} · format 5:4'.lstrip(" ·"))
        im.save(OUT / f"{name}.jpg", "JPEG", quality=82, optimize=True)
        im.resize((800, 640), Image.LANCZOS).save(OUT / f"{name}-800.jpg", "JPEG", quality=80, optimize=True)
        print(name)


if __name__ == "__main__":
    main(sys.argv[1:])
