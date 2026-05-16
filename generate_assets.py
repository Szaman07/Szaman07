#!/usr/bin/env python3
"""Generate larger, cleaner Zelda ALTTP-inspired SVG assets."""
import os

OUT = r"e:\study\Projects\github\red1-for-hek-main\assets"
os.makedirs(OUT, exist_ok=True)

GOLD = "#D4AF37"
GREEN = "#78C27A"
BG_CARD = "#13261a" # Slightly lighter dark green for contrast
TXT = "#E2DFD2"

def save(name, svg):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"  OK: {name}")

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
    ("Documentation & Design", [
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
    cw, ch, gap = 170, 46, 12  # Increased card sizes
    per_row = min(len(items), 4)
    rows = (len(items) + per_row - 1) // per_row
    pad = 20
    hdr_h = 44  # Increased header height
    w = pad*2 + per_row*cw + (per_row-1)*gap
    h = pad + hdr_h + rows*(ch+gap) + 10

    cards = ""
    for i,(name,color) in enumerate(items):
        r,c = divmod(i, per_row)
        x = pad + c*(cw+gap)
        y = pad + hdr_h + r*(ch+gap)
        ab = ABBR.get(name, name[:2])
        tc = dark_text(color)
        cards += f'''  <rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="6" fill="{BG_CARD}" stroke="{GOLD}" stroke-width="0.8" stroke-opacity="0.6"/>
  <rect x="{x+8}" y="{y+7}" width="32" height="32" rx="4" fill="{color}" opacity="0.9"/>
  <text x="{x+24}" y="{y+29}" text-anchor="middle" font-family="'Courier New',monospace" font-size="13" font-weight="700" fill="{tc}">{ab}</text>
  <text x="{x+48}" y="{y+29}" font-family="'Courier New',monospace" font-size="14" fill="{TXT}">{name}</text>
'''

    cat_safe = cat_name.replace('&', '&amp;')
    save(fname, f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <text x="{w//2}" y="{pad+18}" text-anchor="middle" font-family="'Courier New',monospace" font-size="18" font-weight="700" fill="{GOLD}" letter-spacing="2">◆ {cat_safe} ◆</text>
  <line x1="{pad+40}" y1="{pad+30}" x2="{w-pad-40}" y2="{pad+30}" stroke="{GOLD}" stroke-width="0.8" opacity="0.4"/>
{cards}</svg>
''')

for i,(cat,items) in enumerate(CATS):
    tech_svg(cat, items, f"tech_{i}.svg")

# ── GOLD DIVIDER (larger) ──
save("gold-divider.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="24" viewBox="0 0 900 24">
  <line x1="120" y1="12" x2="410" y2="12" stroke="{GOLD}" stroke-width="1.2" opacity="0.4"/>
  <polygon points="450,4 458,12 450,20 442,12" fill="{GREEN}" opacity="0.7"/>
  <line x1="490" y1="12" x2="780" y2="12" stroke="{GOLD}" stroke-width="1.2" opacity="0.4"/>
</svg>
''')

# ── QUEST LOG (fixed spacing) ──
save("quest_log.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200" viewBox="0 0 800 200">
<text x="400" y="30" text-anchor="middle" font-family="'Courier New',monospace" font-size="18" font-weight="700" fill="{GOLD}" letter-spacing="4">QUEST LOG</text>
<line x1="80" y1="50" x2="330" y2="50" stroke="{GOLD}" stroke-width="0.8" opacity="0.4"/>
<polygon points="395,44 400,50 395,56 390,50" fill="{GREEN}" opacity="0.7"/>
<line x1="470" y1="50" x2="720" y2="50" stroke="{GOLD}" stroke-width="0.8" opacity="0.4"/>

<rect x="40" y="75" width="340" height="90" rx="6" fill="{BG_CARD}" stroke="{GOLD}" stroke-width="0.8" stroke-opacity="0.4"/>
<text x="60" y="105" font-family="'Courier New',monospace" font-size="14" font-weight="700" fill="{GOLD}">??? - Ancient AI Relic</text>
<text x="60" y="130" font-family="'Courier New',monospace" font-size="13" fill="#8ca893">Status: Being prepared...</text>
<text x="60" y="150" font-family="'Courier New',monospace" font-size="11" fill="#6c8272" font-style="italic">Quest details coming soon.</text>

<rect x="420" y="75" width="340" height="90" rx="6" fill="{BG_CARD}" stroke="{GOLD}" stroke-width="0.8" stroke-opacity="0.4"/>
<text x="440" y="105" font-family="'Courier New',monospace" font-size="14" font-weight="700" fill="{GOLD}">??? - Sacred DL Manuscript</text>
<text x="440" y="130" font-family="'Courier New',monospace" font-size="13" fill="#8ca893">Status: Being prepared...</text>
<text x="440" y="150" font-family="'Courier New',monospace" font-size="11" fill="#6c8272" font-style="italic">Quest details coming soon.</text>
</svg>
''')

# ── SOCIAL BUTTONS ──
def social_btn(name, color, fname):
    save(fname, f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="160" height="42" viewBox="0 0 160 42">
  <rect x="2" y="2" width="156" height="38" rx="6" fill="{BG_CARD}" stroke="{GOLD}" stroke-width="1.2" stroke-opacity="0.5"/>
  <rect x="12" y="9" width="24" height="24" rx="4" fill="{color}" opacity="0.9"/>
  <text x="24" y="26" text-anchor="middle" font-family="'Courier New',monospace" font-size="12" font-weight="700" fill="#fff">{name[:2]}</text>
  <text x="48" y="26" font-family="'Courier New',monospace" font-size="14" font-weight="700" fill="{TXT}">{name}</text>
</svg>
''')

social_btn("LinkedIn", "#0077B5", "btn_linkedin.svg")
social_btn("Facebook", "#1877F2", "btn_facebook.svg")

# ── FOOTER (larger) ──
save("footer.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="50" viewBox="0 0 600 50">
  <text x="300" y="30" text-anchor="middle" font-family="'Courier New',monospace" font-size="15" fill="{GOLD}" opacity="0.8" letter-spacing="1">Thanks for visiting! May the Triforce guide you. ▲</text>
</svg>
''')

print("\nAll assets generated with updated typography!")
