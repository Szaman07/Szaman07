#!/usr/bin/env python3
"""Generate clean Zelda ALTTP-inspired SVG assets. Minimal, atmospheric, readable."""
import os

OUT = r"e:\study\Projects\github\red1-for-hek-main\assets"
os.makedirs(OUT, exist_ok=True)

GOLD = "#D4AF37"
GREEN = "#78C27A"
BG_CARD = "#1a2e1a"
TXT = "#E2DFD2"

def save(name, svg):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"  OK: {name}")

# ── TECH CATEGORY SVGs ──
# Fixed card size: 120x32, 4 per row max, readable text
CATS = [
    ("Programming Languages", [
        ("C","#A8B9CC"), ("C++","#00599C"), ("Java","#ED8B00"),
        ("Python","#3776AB"), ("JavaScript","#F7DF1E"), ("TypeScript","#3178C6"),
    ]),
    ("Frontend", [
        ("HTML5","#E34F26"), ("CSS3","#1572B6"), ("React","#61DAFB"),
    ]),
    ("Backend / Frameworks", [
        ("Node.js","#339933"), ("Express.js","#888888"), ("Django","#092E20"),
    ]),
    ("ML / Data Science", [
        ("PyTorch","#EE4C2C"), ("TensorFlow","#FF6F00"),
        ("scikit-learn","#F7931E"), ("Google Colab","#F9AB00"),
    ]),
    ("Databases", [
        ("MySQL","#4479A1"), ("MongoDB","#47A248"), ("SQLite","#003B57"),
    ]),
    ("Dev Tools", [
        ("Git","#F05032"), ("Linux","#FCC624"),
    ]),
    ("Documentation &amp; Design", [
        ("LaTeX","#008080"), ("Markdown","#555555"), ("Figma","#F24E1E"),
        ("Onshape","#53B13B"), ("AutoCAD","#E51937"),
    ]),
]

ABBR = {"C++":"C+","JavaScript":"JS","TypeScript":"TS","HTML5":"H5",
        "CSS3":"C3","Node.js":"Nj","Express.js":"Ex","Django":"Dj",
        "MySQL":"My","MongoDB":"Mg","SQLite":"Sq","PyTorch":"Pt",
        "TensorFlow":"TF","scikit-learn":"Sk","Google Colab":"Gc",
        "Git":"Gt","Linux":"Lx","LaTeX":"Lx","Markdown":"Md",
        "Figma":"Fg","Onshape":"On","AutoCAD":"Ac","React":"Re",
        "Python":"Py","Java":"Jv","C":"C"}

def dark_text(c):
    return "#1a1a1a" if c in ("#F7DF1E","#FCC624","#F9AB00","#61DAFB") else "#fff"

def tech_svg(cat_name, items, fname):
    cw, ch, gap = 120, 34, 8
    per_row = min(len(items), 4)
    rows = (len(items) + per_row - 1) // per_row
    pad = 14
    hdr_h = 32
    w = pad*2 + per_row*cw + (per_row-1)*gap
    h = pad + hdr_h + rows*(ch+gap) + 4

    cards = ""
    for i,(name,color) in enumerate(items):
        r,c = divmod(i, per_row)
        x = pad + c*(cw+gap)
        y = pad + hdr_h + r*(ch+gap)
        ab = ABBR.get(name, name[:2])
        tc = dark_text(color)
        cards += f'''  <rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="5" fill="{BG_CARD}" stroke="{GOLD}" stroke-width="0.6" stroke-opacity="0.5"/>
  <rect x="{x+6}" y="{y+5}" width="24" height="24" rx="4" fill="{color}" opacity="0.85"/>
  <text x="{x+18}" y="{y+22}" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" font-weight="700" fill="{tc}">{ab}</text>
  <text x="{x+36}" y="{y+22}" font-family="'Courier New',monospace" font-size="12" fill="{TXT}">{name}</text>
'''

    save(fname, f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <text x="{w//2}" y="{pad+12}" text-anchor="middle" font-family="'Courier New',monospace" font-size="13" font-weight="700" fill="{GOLD}" letter-spacing="1">◆ {cat_name} ◆</text>
  <line x1="{pad+20}" y1="{pad+20}" x2="{w-pad-20}" y2="{pad+20}" stroke="{GOLD}" stroke-width="0.5" opacity="0.25"/>
{cards}</svg>
''')

for i,(cat,items) in enumerate(CATS):
    tech_svg(cat, items, f"tech_{i}.svg")

# ── GOLD DIVIDER (refined) ──
save("gold-divider.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="20" viewBox="0 0 800 20">
  <line x1="100" y1="10" x2="360" y2="10" stroke="{GOLD}" stroke-width="0.8" opacity="0.3"/>
  <polygon points="400,4 406,10 400,16 394,10" fill="{GREEN}" opacity="0.6"/>
  <line x1="440" y1="10" x2="700" y2="10" stroke="{GOLD}" stroke-width="0.8" opacity="0.3"/>
</svg>
''')

# ── FOOTER ──
save("footer.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="460" height="40" viewBox="0 0 460 40">
  <text x="230" y="24" text-anchor="middle" font-family="'Courier New',monospace" font-size="12" fill="{GOLD}" opacity="0.6" letter-spacing="1">Thanks for visiting! May the Triforce guide you. ▲</text>
</svg>
''')

print("\nAll assets generated!")
