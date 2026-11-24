# Illustrations au trait dans l'esprit de Bridge : traits dans la couleur foncée de la carte,
# surfaces blanches, petits traits d'accent et ombre portée. Toutes tiennent dans 160 × 120.
# Elles sont regroupées dans assets/illus.svg et appelées par <use> : une seule requête, et
# la couleur suit la carte (currentColor), le blanc se règle avec --illu-fill.
import re
from pathlib import Path

S = 'stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
L = 'fill="var(--illu-fill,#fff)"'
D = 'fill="currentColor"'
N = 'fill="none"'
LT = 'stroke="var(--illu-fill,#fff)"'
FONT = 'font-family="Public Sans, Arial, sans-serif" font-weight="800" text-anchor="middle"'


def shadow(cx, cy, rx):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="4.5" fill="currentColor" opacity=".16"/>'


def sparks(x, y, mirror=False):
    """Trois petits traits qui rayonnent, comme sur les illustrations de Bridge."""
    k = -1 if mirror else 1
    return (f'<path d="M{x} {y}l{-7 * k} -5M{x + 6 * k} {y - 5}l{-2 * k} -8M{x + 13 * k} {y - 4}l{3 * k} -8" '
            f'{N} {S} stroke-width="2.6"/>')


def star(cx, cy, r):
    i = r * 0.28
    return (f'<path d="M{cx} {cy - r}L{cx + i} {cy - i}L{cx + r} {cy}L{cx + i} {cy + i}L{cx} {cy + r}'
            f'L{cx - i} {cy + i}L{cx - r} {cy}L{cx - i} {cy - i}z" {D}/>')


ILLUS = {
    "calendrier": (
        shadow(80, 108, 44)
        + f'<rect x="36" y="28" width="80" height="72" rx="9" {L} {S}/>'
        + f'<path d="M45 28h62a9 9 0 0 1 9 9v9H36v-9a9 9 0 0 1 9-9z" {D} {S}/>'
        + f'<rect x="53" y="17" width="8" height="19" rx="4" {L} {S}/><rect x="91" y="17" width="8" height="19" rx="4" {L} {S}/>'
        + "".join(f'<rect x="{x - 4}" y="{y - 3}" width="8" height="6" rx="1.6" fill="currentColor" opacity=".3"/>'
                  for y in (58, 72, 86) for x in (49, 63, 77, 91, 105) if (x, y) != (91, 72))
        + f'<circle cx="91" cy="72" r="9" {D}/><path d="M86.5 72.5l3 3 6-6.5" {N} {LT} stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        + f'<g transform="rotate(32 132 66)"><rect x="126" y="34" width="12" height="50" rx="2" {L} {S}/>'
        + f'<rect x="126" y="34" width="12" height="9" {D} {S}/><path d="M126 84l6 12 6-12z" {L} {S}/>'
        + f'<path d="M130.6 93.2 132 96l1.4-2.8z" {D}/></g>'
        + sparks(24, 30)
    ),
    "porte": (
        f'<path d="M30 104h100" {S}/>'
        + f'<path d="M40 104V48a40 40 0 0 1 80 0v56" {N} {S}/>'
        + f'<path d="M50 104V50a30 30 0 0 1 60 0v54z" {L} {S}/>'
        + f'<path d="M60 62a20 20 0 0 1 40 0v6H60z" {N} {S} stroke-width="2.4"/>'
        + f'<rect x="60" y="76" width="40" height="20" rx="3" {N} {S} stroke-width="2.4"/>'
        + f'<circle cx="101" cy="72" r="3.4" {D}/>'
        + f'<path d="M44 104h72l-6 9H50z" {D}/>'
        + f'<path d="M12 88h20l-3 16H15z" {D}/>'
        + f'<path d="M22 88c-11-6-13-19-7-28 5 8 9 17 7 28z" {L} {S} stroke-width="2.4"/>'
        + f'<path d="M22 88c3-11 12-16 21-16-2 9-11 15-21 16z" {L} {S} stroke-width="2.4"/>'
        + sparks(128, 26)
    ),
    "menage": (
        shadow(86, 108, 48)
        + f'<path d="M44 56c0-6 4-10 10-10h18c6 0 10 4 10 10v40a8 8 0 0 1-8 8H52a8 8 0 0 1-8-8z" {L} {S}/>'
        + f'<rect x="50" y="64" width="26" height="24" rx="4" {D}/><path d="M56 76h14" {LT} stroke-width="3" stroke-linecap="round"/>'
        + f'<rect x="54" y="36" width="20" height="11" rx="2" {L} {S}/>'
        + f'<path d="M50 37V26a4 4 0 0 1 4-4h22l12 6v9z" {D} {S}/><rect x="86" y="24" width="9" height="7" rx="1.5" {D}/>'
        + f'<path d="M78 37c3 6 1 11-4 15" {N} {S}/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="1.9" {D}/>' for x, y in ((101, 22), (105, 30), (109, 23), (112, 33), (117, 27), (115, 17)))
        + f'<rect x="90" y="84" width="44" height="19" rx="6" {L} {S}/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="1.7" fill="currentColor" opacity=".45"/>' for x, y in ((100, 91), (110, 96), (119, 90), (127, 96), (104, 98)))
        + star(126, 56, 10) + star(142, 70, 5)
    ),
    "linge": (
        shadow(80, 108, 54)
        + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="8" {L}/><rect x="{x + w - 22}" y="{y}" width="9" height="22" {D}/>'
                  f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="8" {N} {S}/>'
                  f'<path d="M{x + 8} {y + 11}h{w - 40}" stroke="currentColor" stroke-width="2" stroke-linecap="round" opacity=".35"/>'
                  for x, y, w in ((28, 80, 104), (36, 58, 90), (46, 36, 72)))
        + f'<path d="M58 34c8-7 18-10 32-11" {N} {S} stroke-width="2.4"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="2.5" {D}/>' for x, y in ((68, 28), (74, 26), (80, 24.5), (86, 23.5)))
        + sparks(22, 34)
    ),
    "outils": (
        shadow(80, 108, 54)
        + f'<path d="M104 58L128 30" stroke="currentColor" stroke-width="9" stroke-linecap="round"/>'
        + f'<circle cx="131" cy="26" r="10" {L} {S}/><path d="M131 15v10" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>'
        + f'<path d="M52 58L40 34" {S} stroke-width="3"/><g transform="rotate(-26 38 28)"><rect x="33" y="12" width="10" height="22" rx="4" {D}/></g>'
        + f'<path d="M64 56V46a6 6 0 0 1 6-6h20a6 6 0 0 1 6 6v10" {N} {S} stroke-width="4"/>'
        + f'<rect x="30" y="56" width="100" height="46" rx="7" {L} {S}/>'
        + f'<path d="M37 56h86a7 7 0 0 1 7 7v8H30v-8a7 7 0 0 1 7-7z" {D} {S}/>'
        + f'<rect x="72" y="64" width="16" height="13" rx="3" {L} {S}/>'
        + f'<path d="M44 88h20M96 88h20" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" opacity=".4"/>'
        + sparks(140, 60)
    ),
    "casque": (
        f'<path d="M46 72v-10a34 34 0 0 1 68 0v10" {N} {S} stroke-width="5"/>'
        + f'<rect x="36" y="62" width="18" height="28" rx="8" {D}/><rect x="106" y="62" width="18" height="28" rx="8" {D}/>'
        + f'<path d="M115 90c0 12-8 18-22 18h-4" {N} {S}/><rect x="74" y="102" width="17" height="10" rx="5" {D}/>'
        + f'<path d="M112 10h26a12 12 0 0 1 12 12v4a12 12 0 0 1-12 12h-16l-10 10 2-10h-2a12 12 0 0 1-12-12v-4a12 12 0 0 1 12-12z" {L} {S}/>'
        + f'<text x="125" y="29.5" {FONT} font-size="13" {D}>24/7</text>'
        + sparks(22, 44)
    ),
    "balance": (
        shadow(80, 110, 30)
        + f'<path d="M80 34v62" {S} stroke-width="4"/><path d="M62 104h36l-4-7H66z" {D}/>'
        + f'<path d="M42 40h76" {S} stroke-width="4"/><circle cx="80" cy="28" r="5.5" {L} {S}/>'
        + f'<path d="M42 40l-12 30M42 40l12 30M118 40l-12 30M118 40l12 30" {N} {S} stroke-width="2"/>'
        + f'<rect x="35" y="58" width="14" height="11" rx="2" {D}/><rect x="111" y="58" width="14" height="11" rx="2" {D}/>'
        + f'<path d="M26 70h32a16 9 0 0 1-32 0z" {L} {S}/><path d="M102 70h32a16 9 0 0 1-32 0z" {L} {S}/>'
        + sparks(130, 22)
    ),
    "carte": (
        shadow(80, 109, 44)
        + f'<rect x="34" y="22" width="92" height="80" rx="12" {L} {S}/>'
        + f'<path d="M48 44h64M48 62h64M48 82h64" {N} stroke="currentColor" stroke-width="3" stroke-linecap="round" opacity=".3"/>'
        + f'<circle cx="66" cy="44" r="7.5" {D}/><circle cx="98" cy="62" r="7.5" {L} {S}/><circle cx="78" cy="82" r="7.5" {D}/>'
        + f'<circle cx="126" cy="24" r="13" {D}/><path d="M120 24.5l4 4 8-8.5" {N} {LT} stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>'
        + sparks(22, 20)
    ),
    "cles": (
        shadow(86, 112, 40)
        + f'<circle cx="56" cy="40" r="16" {N} {S} stroke-width="3.6"/>'
        + f'<path d="M42 58c-2-5 0-9 5-12" {N} {S} stroke-width="2.4"/>'
        + f'<g transform="rotate(-14 40 76)"><rect x="28" y="58" width="24" height="34" rx="6" {L} {S}/>'
        + f'<circle cx="40" cy="66" r="3" {D}/><path d="M34 78h12M34 85h8" {N} {S} stroke-width="2.4"/></g>'
        + f'<circle cx="64" cy="64" r="11" {D}/><path d="M60.5 74h7v32h-7z" {D}/><path d="M67.5 90h5v5h-5zM67.5 99h4v4h-4z" {D}/>'
        + f'<circle cx="82" cy="56" r="14" {L} {S}/><circle cx="78" cy="52" r="4" {D}/>'
        + f'<path d="M95 52h36v8h-6v7h-6v-7h-5v6h-6v-6H95z" {L} {S}/>'
        + sparks(124, 34)
    ),
    "serrure": (
        f'<rect x="24" y="10" width="60" height="100" rx="4" fill="currentColor" fill-opacity=".1" {S}/>'
        + f'<rect x="40" y="30" width="34" height="56" rx="12" {L} {S}/>'
        + f'<circle cx="57" cy="50" r="11" {D}/><circle cx="57" cy="50" r="5.5" {N} {LT} stroke-width="2.6"/><circle cx="57" cy="74" r="2.6" {D}/>'
        + f'<path d="M93 50a10 10 0 0 0 0 16M87 45a17 17 0 0 0 0 26" {N} {S} stroke-width="2.6"/>'
        + shadow(116, 108, 22)
        + f'<rect x="99" y="40" width="34" height="62" rx="7" {L} {S}/><path d="M110 47h12" {N} {S} stroke-width="2.4"/>'
        + f'<circle cx="116" cy="72" r="10" {D}/><path d="M111 72.5l3.5 3.5 7-7.5" {N} {LT} stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        + sparks(128, 28)
    ),
    "appareil": (
        shadow(80, 109, 46)
        + f'<path d="M56 42l6-10h24l6 10" {L} {S}/><rect x="104" y="34" width="14" height="9" rx="2.5" {D}/>'
        + f'<rect x="32" y="42" width="96" height="60" rx="11" {L} {S}/>'
        + f'<circle cx="80" cy="72" r="21" {D}/><circle cx="80" cy="72" r="13" {L}/><circle cx="80" cy="72" r="7" {D}/><circle cx="76" cy="68" r="2.4" {L}/>'
        + f'<rect x="40" y="50" width="12" height="8" rx="2" {D}/>'
        + sparks(30, 32)
    ),
    "langues": (
        f'<path d="M38 20h40a14 14 0 0 1 14 14v14a14 14 0 0 1-14 14H52l-16 12 4-12h-2a14 14 0 0 1-14-14V34a14 14 0 0 1 14-14z" {L} {S}/>'
        + f'<text x="58" y="48" {FONT} font-size="18" {D}>FR</text>'
        + f'<path d="M82 52h40a14 14 0 0 1 14 14v14a14 14 0 0 1-14 14h-2l4 12-16-12H82a14 14 0 0 1-14-14V66a14 14 0 0 1 14-14z" {D} {S}/>'
        + f'<text x="102" y="80" {FONT} font-size="18" fill="var(--illu-fill,#fff)">EN</text>'
        + sparks(138, 30)
    ),
    "identite": (
        shadow(76, 110, 48)
        + f'<rect x="24" y="34" width="100" height="66" rx="10" {L} {S}/>'
        + f'<path d="M34 34h80a10 10 0 0 1 10 10v3H24v-3a10 10 0 0 1 10-10z" {D} {S}/>'
        + f'<circle cx="50" cy="66" r="9" {D}/><path d="M36 92a14 12 0 0 1 28 0z" {D}/>'
        + "".join(f'<rect x="74" y="{y}" width="{w}" height="5" rx="2.5" fill="currentColor" opacity=".4"/>' for y, w in ((60, 38), (72, 30), (84, 34)))
        + f'<circle cx="124" cy="36" r="15" {D} {S}/><path d="M117 36.5l5 5 9-10" {N} {LT} stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>'
        + sparks(18, 30)
    ),
    "valise": (
        shadow(80, 112, 40)
        + f'<path d="M66 40V30a6 6 0 0 1 6-6h16a6 6 0 0 1 6 6v10" {N} {S} stroke-width="4"/>'
        + f'<rect x="44" y="40" width="72" height="62" rx="11" {L} {S}/><path d="M62 40v62M98 40v62" {N} {S}/>'
        + f'<circle cx="80" cy="60" r="8" {D}/><rect x="70" y="77" width="20" height="12" rx="3" {N} {S} stroke-width="2.4" transform="rotate(-8 80 83)"/>'
        + f'<circle cx="56" cy="106" r="4.5" {D}/><circle cx="104" cy="106" r="4.5" {D}/>'
        + sparks(124, 30)
    ),
    "maison": (
        shadow(84, 108, 56)
        + f'<path d="M88 44V33h9v18" {L} {S}/>'
        + f'<path d="M38 62v38h64V62L70 36z" {L} {S}/><path d="M30 67l40-34 40 34" {N} {S} stroke-width="4"/>'
        + f'<rect x="62" y="76" width="16" height="24" rx="3" {D}/>'
        + f'<rect x="44" y="70" width="12" height="12" rx="2" {N} {S} stroke-width="2.4"/><path d="M50 70v12M44 76h12" {N} {S} stroke-width="1.8"/>'
        + "".join(f'<ellipse cx="126" cy="{y}" rx="15" ry="5.5" {L} {S}/>' for y in (100, 92, 84))
        + f'<circle cx="126" cy="56" r="13" {D}/><text x="126" y="61.5" {FONT} font-size="16" fill="var(--illu-fill,#fff)">€</text>'
        + sparks(140, 34)
    ),
    "graphique": (
        shadow(80, 109, 48)
        + f'<rect x="30" y="24" width="100" height="76" rx="10" {L} {S}/>'
        + "".join(f'<rect x="{x}" y="{y}" width="13" height="{90 - y}" rx="2" fill="currentColor" opacity="{o}"/>'
                  for x, y, o in ((44, 72, ".3"), (63, 62, ".5"), (82, 52, ".75"), (101, 42, "1")))
        + f'<path d="M44 62l20-12 16 6 30-22" {N} {S}/><path d="M99 33h12v12" {N} {S}/>'
        + sparks(132, 20)
    ),
    "cafe": (
        f'<ellipse cx="60" cy="100" rx="32" ry="7" {L} {S}/>'
        + f'<path d="M86 66h6a9 9 0 0 1 0 18h-7" {N} {S}/>'
        + f'<path d="M36 60h48v16a20 20 0 0 1-20 20h-8a20 20 0 0 1-20-20z" {L} {S}/>'
        + f'<ellipse cx="60" cy="60" rx="24" ry="5" {D}/>'
        + f'<path d="M52 50c-5-5 5-9 0-15M66 50c-5-5 5-9 0-15" {N} {S} stroke-width="2.6"/>'
        + shadow(124, 104, 28)
        + f'<path d="M98 96C94 82 108 70 124 70S154 82 150 96C146 92 140 91 136 94C132 88 128 86 124 86S116 88 112 94C108 91 102 92 98 96z" {L} {S}/>'
        + f'<path d="M111 75c-2 6-2 12 1 19M124 71v15M137 75c2 6 2 12-1 19" {N} {S} stroke-width="2.2"/>'
        + f'<circle cx="20" cy="92" r="5.5" {D}/><path d="M25 90h13v4h-3v4h-3v-4h-7z" {D}/>'
        + sparks(96, 40)
    ),
    "lampe": (
        shadow(88, 109, 50)
        + f'<rect x="98" y="18" width="36" height="28" rx="3" {L} {S}/><path d="M102 42l9-11 7 7 5-5 7 9" {N} {S} stroke-width="2.2"/>'
        + f'<path d="M44 22h36l8 24H36z" {L} {S}/><path d="M62 46v52" {S} stroke-width="3.2"/><ellipse cx="62" cy="101" rx="16" ry="4" {D}/>'
        + f'<path d="M45 54l-6 8M62 56v9M79 54l6 8" {N} {S} stroke-width="2.4"/>'
        + f'<path d="M113 80c-12-6-16-20-8-30 6 8 10 18 8 30z" {L} {S} stroke-width="2.4"/>'
        + f'<path d="M113 80c2-12 12-20 24-20-2 10-12 18-24 20z" {L} {S} stroke-width="2.4"/>'
        + f'<path d="M113 80c-4-8-14-10-22-6 4 6 12 8 22 6z" {L} {S} stroke-width="2.4"/>'
        + f'<path d="M98 80h30l-4 22h-22z" {D}/>'
    ),
    "rouleau": (
        shadow(76, 112, 30)
        + f'<rect x="26" y="56" width="84" height="16" rx="8" fill="currentColor" opacity=".22"/>'
        + f'<path d="M98 41h12v22H74v14" {N} {S} stroke-width="3.6"/>'
        + f'<rect x="34" y="30" width="64" height="22" rx="9" {L} {S}/>'
        + f'<path d="M48 35v12M60 35v12M72 35v12M84 35v12" {N} stroke="currentColor" stroke-width="2" stroke-linecap="round" opacity=".4"/>'
        + f'<rect x="67" y="76" width="14" height="30" rx="6" {D}/>'
        + f'<path d="M50 52v9M62 52v5" {N} {S}/>'
        + sparks(120, 26)
    ),
    "telephone": (
        shadow(80, 114, 34)
        + f'<rect x="52" y="12" width="56" height="98" rx="11" {L} {S}/><path d="M72 21h16" {N} {S} stroke-width="2.6"/>'
        + f'<rect x="60" y="34" width="36" height="14" rx="7" {D}/>'
        + f'<rect x="66" y="55" width="34" height="14" rx="7" {N} {S} stroke-width="2.4"/>'
        + f'<rect x="60" y="76" width="28" height="14" rx="7" {D}/>'
        + f'<path d="M120 26h20a8 8 0 0 1 8 8v8a8 8 0 0 1-8 8h-10l-8 7 1-7h-3a8 8 0 0 1-8-8v-8a8 8 0 0 1 8-8z" {L} {S}/>'
        + f'<path d="M124 40l6-5 6 5v6h-12z" {D}/>'
        + sparks(30, 30)
    ),
    "tour-eiffel": (
        shadow(80, 109, 38)
        + f'<path d="M28 40a8 8 0 0 1 14-6 10 10 0 0 1 18 4 7 7 0 0 1-2 14H32a7 7 0 0 1-4-12z" {L} {S} stroke-width="2.4"/>'
        + f'<path d="M54 104c10-6 16-22 20-44h12c4 22 10 38 20 44" {N} {S}/>'
        + f'<path d="M66 104c4-10 24-10 28 0" {N} {S}/><path d="M60 82h40M69 60h22" {N} {S} stroke-width="3.6"/>'
        + f'<path d="M74 60l4-30h4l4 30" {N} {S}/><path d="M80 30V15" {N} {S} stroke-width="2.6"/><circle cx="80" cy="13" r="2.4" {D}/>'
        + f'<path d="M66 82l8-22M94 82l-8-22M76 60l4-13 4 13" {N} stroke="currentColor" stroke-width="1.8" opacity=".6"/>'
        + f'<circle cx="124" cy="30" r="10" {N} {S} stroke-width="2.6"/>'
        + f'<path d="M124 12v4M124 44v4M106 30h4M138 30h4" {N} {S} stroke-width="2.4"/>'
    ),
}


def dedupe(svg):
    """Un même attribut répété dans une balise rend le SVG invalide : on garde la dernière valeur."""
    def fix(m):
        tag = m.group(0)
        for attr in ("stroke-width", "fill", "stroke"):
            found = re.findall(rf'\s{attr}="[^"]*"', tag)
            for extra in found[:-1]:
                tag = tag.replace(extra, "", 1)
        return tag
    return re.sub(r"<[^>]+>", fix, svg)


def sprite():
    symbols = "".join(f'<symbol id="i-{k}" viewBox="0 0 160 120">{dedupe(v)}</symbol>' for k, v in ILLUS.items())
    return f'<svg xmlns="http://www.w3.org/2000/svg">{symbols}</svg>\n'


def write(root):
    (Path(root) / "assets" / "illus.svg").write_text(sprite(), encoding="utf-8")


def illu(name, cls="illu", label=None):
    if name not in ILLUS:
        raise KeyError(name)
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg class="{cls}" viewBox="0 0 160 120" {aria}><use href="/assets/illus.svg#i-{name}"/></svg>'
