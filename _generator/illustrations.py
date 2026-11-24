# Illustrations provisoires aux couleurs de la marque, écrites dans assets/img/.
# À remplacer par de vraies photos : voir README (« Images »).
from pathlib import Path

N, S, S2, L, L2, C, W = "#1B1B4B", "#A9C2FF", "#C9D8FF", "#E4FBC0", "#CDEE9A", "#EEEDE8", "#FFFFFF"
OUT = Path(__file__).resolve().parent.parent / "assets" / "img"


def svg(body, bg=C, w=800, h=600):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'preserveAspectRatio="xMidYMid slice"><rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')


def window(x, y, w, h, sky=S):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{sky}"/>'
            f'<path d="M{x + w / 2} {y}v{h}M{x} {y + h / 2}h{w}" stroke="{W}" stroke-width="8"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{W}" stroke-width="10"/>')


def plant(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0C-50-60-40-130-10-170C0-110 5-60 0 0Z" fill="{L2}"/>'
            f'<path d="M0 0C40-50 80-70 110-120C60-110 20-70 0 0Z" fill="{L2}"/>'
            f'<path d="M0 0C-40-30-90-40-120-80C-70-80-30-50 0 0Z" fill="{L2}"/>'
            f'<path d="M-34 0h68l-10 70h-48z" fill="{N}"/></g>')


salon = svg(
    f'<rect y="430" width="800" height="170" fill="{S2}"/>'
    + window(90, 70, 250, 290)
    + f'<rect x="470" y="110" width="150" height="190" fill="{L}"/><circle cx="545" cy="190" r="42" fill="{S}"/>'
    f'<path d="M700 60v150" stroke="{N}" stroke-width="5"/><path d="M650 210h100l-22 70h-56z" fill="{N}"/>'
    f'<rect x="230" y="330" width="420" height="150" rx="34" fill="{N}"/>'
    f'<rect x="200" y="380" width="80" height="120" rx="30" fill="{N}"/><rect x="600" y="380" width="80" height="120" rx="30" fill="{N}"/>'
    f'<rect x="290" y="350" width="130" height="80" rx="18" fill="{S}"/><rect x="450" y="350" width="130" height="80" rx="18" fill="{L}"/>'
    f'<rect x="250" y="500" width="14" height="40" fill="{N}"/><rect x="620" y="500" width="14" height="40" fill="{N}"/>'
    f'<ellipse cx="440" cy="560" rx="250" ry="26" fill="{L}"/>'
    + plant(110, 500, 0.9))

facade_windows = "".join(
    f'<rect x="{x}" y="{y}" width="70" height="{110 if y < 400 else 130}" rx="{35 if y < 150 else 0}" fill="{S if (x + y) % 3 else L}"/>'
    f'<rect x="{x - 12}" y="{y + (96 if y < 400 else 116)}" width="94" height="14" fill="{N}"/>'
    for y in (110, 260, 410) for x in (130, 265, 400, 535, 670))
facade = svg(
    f'<rect x="80" y="70" width="700" height="560" fill="{W}"/>'
    f'<path d="M60 70h740l-40-60H100z" fill="{N}"/>' + facade_windows
    + f'<rect x="0" y="560" width="800" height="40" fill="{N}"/>', bg=S)

cles = svg(
    f'<rect x="120" y="40" width="330" height="560" fill="{N}"/><rect x="150" y="70" width="270" height="230" fill="none" stroke="{S}" stroke-width="6"/>'
    f'<rect x="150" y="330" width="270" height="240" fill="none" stroke="{S}" stroke-width="6"/>'
    f'<rect x="360" y="290" width="64" height="110" rx="14" fill="{L}"/><circle cx="392" cy="325" r="16" fill="{N}"/>'
    f'<rect x="386" y="350" width="12" height="34" rx="6" fill="{N}"/>'
    f'<rect x="530" y="210" width="170" height="300" rx="26" fill="{W}" stroke="{N}" stroke-width="10"/>'
    f'<circle cx="615" cy="330" r="46" fill="{L}"/><path d="M594 330l14 16 30-34" fill="none" stroke="{N}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<rect x="570" y="410" width="90" height="12" rx="6" fill="{S}"/><rect x="585" y="436" width="60" height="12" rx="6" fill="{S}"/>'
    f'<path d="M450 310c30-30 50-40 80-30M455 345c30-10 45-10 70 0" fill="none" stroke="{N}" stroke-width="5" stroke-dasharray="4 12" stroke-linecap="round"/>',
    bg=L)

linge = svg(
    window(470, 50, 240, 230, S2)
    + f'<rect x="60" y="150" width="60" height="330" rx="20" fill="{N}"/><rect x="60" y="330" width="700" height="150" rx="24" fill="{W}"/>'
    f'<rect x="60" y="400" width="700" height="100" fill="{S}"/><rect x="140" y="270" width="190" height="90" rx="30" fill="{L}"/>'
    f'<rect x="350" y="280" width="170" height="80" rx="30" fill="{W}"/>'
    f'<rect x="540" y="330" width="150" height="26" rx="8" fill="{N}"/><rect x="548" y="304" width="134" height="26" rx="8" fill="{L2}"/>'
    f'<rect x="556" y="278" width="118" height="26" rx="8" fill="{W}"/>'
    f'<rect x="80" y="500" width="20" height="50" fill="{N}"/><rect x="720" y="500" width="20" height="50" fill="{N}"/>'
    + plant(730, 250, 0.45), bg=C)

marne = svg(
    f'<circle cx="640" cy="130" r="60" fill="{L}"/>'
    f'<path d="M0 330h800v80H0z" fill="{L2}"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{N}"/><rect x="{x - 5}" y="{y}" width="10" height="{330 - y + 10}" fill="{N}"/>'
              for x, y, r in ((70, 250, 56), (300, 270, 44), (520, 240, 60), (740, 265, 50)))
    + f'<path d="M150 330v-90l55-45 55 45v90z" fill="{W}"/><path d="M140 244l65-54 65 54" fill="none" stroke="{N}" stroke-width="10"/>'
    f'<rect x="190" y="270" width="30" height="60" fill="{S}"/>'
    f'<path d="M380 330v-110h110v110z" fill="{W}"/><path d="M370 222h130l-20-40H390z" fill="{N}"/>'
    f'<rect x="400" y="250" width="26" height="36" fill="{S}"/><rect x="444" y="250" width="26" height="36" fill="{S}"/>'
    f'<path d="M0 410h800v190H0z" fill="{S}"/>'
    f'<path d="M40 470h120M260 500h160M520 460h140M120 550h200M480 540h220" stroke="{W}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M560 420h150l-26 30H586z" fill="{N}"/><path d="M630 420v-70l50 60z" fill="{W}"/>', bg=S2)

accueil = svg(
    f'<rect y="470" width="800" height="130" fill="{L}"/>'
    + window(60, 80, 200, 260, S)
    + f'<circle cx="470" cy="210" r="62" fill="{N}"/><path d="M350 600c0-150 50-230 120-230s120 80 120 230z" fill="{N}"/>'
    f'<path d="M430 372c10 40 70 40 80 0l-40 60z" fill="{L}"/>'
    f'<rect x="590" y="400" width="130" height="170" rx="14" fill="{W}" stroke="{N}" stroke-width="8"/>'
    f'<path d="M620 400v-30a35 35 0 0 1 70 0v30" fill="none" stroke="{N}" stroke-width="8"/><rect x="590" y="455" width="130" height="14" fill="{S}"/>'
    + plant(690, 330, 0.5), bg=S2)

FILES = {"salon.svg": salon, "facade.svg": facade, "cles.svg": cles, "linge.svg": linge, "marne.svg": marne, "accueil.svg": accueil}


def write():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, data in FILES.items():
        (OUT / name).write_text(data, encoding="utf-8")


if __name__ == "__main__":
    write()
