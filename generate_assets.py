#!/usr/bin/env python3
"""Generate Zelda ALTTP-themed SVG assets for GitHub profile."""
import os

OUT = r"e:\study\Projects\github\red1-for-hek-main\assets"
os.makedirs(OUT, exist_ok=True)

# Palette
BG = "#0B1A13"
BG2 = "#0f1f14"
GOLD = "#D4AF37"
GREEN = "#78C27A"
TXT = "#E2DFD2"

def save(name, svg):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"  OK: {name}")

# ── TECH CATEGORY SVGs ──
CATS = [
    ("Programming Languages", [
        ("C","#A8B9CC"), ("C++","#00599C"), ("Java","#ED8B00"),
        ("Python","#3776AB"), ("JavaScript","#F7DF1E"), ("TypeScript","#3178C6"),
    ]),
    ("Frontend Technologies", [
        ("HTML5","#E34F26"), ("CSS3","#1572B6"), ("React","#61DAFB"),
    ]),
    ("Backend / Frameworks", [
        ("Node.js","#339933"), ("Express.js","#888888"), ("Django","#092E20"),
    ]),
    ("Databases", [
        ("MySQL","#4479A1"), ("MongoDB","#47A248"), ("SQLite","#003B57"),
    ]),
    ("Machine Learning / Data Science", [
        ("PyTorch","#EE4C2C"), ("TensorFlow","#FF6F00"),
        ("scikit-learn","#F7931E"), ("Google Colab","#F9AB00"),
    ]),
    ("Dev Tools & Platforms", [
        ("Git","#F05032"), ("Linux","#FCC624"),
    ]),
    ("Documentation & Design", [
        ("LaTeX","#008080"), ("Markdown","#555555"), ("Figma","#F24E1E"),
        ("Onshape","#53B13B"), ("AutoCAD","#E51937"),
    ]),
]

def make_abbrev(name):
    abbrevs = {"C++":"C+","JavaScript":"JS","TypeScript":"TS","HTML5":"H5",
               "CSS3":"C3","Node.js":"Nj","Express.js":"Ex","Django":"Dj",
               "MySQL":"My","MongoDB":"Mg","SQLite":"Sq","PyTorch":"Pt",
               "TensorFlow":"TF","scikit-learn":"Sk","Google Colab":"Gc",
               "Git":"Gt","Linux":"Lx","LaTeX":"Lx","Markdown":"Md",
               "Figma":"Fg","Onshape":"On","AutoCAD":"Ac","React":"Re",
               "Python":"Py","Java":"Jv","C":"C"}
    return abbrevs.get(name, name[:2])

def tech_cat_svg(cat_name, items, fname):
    cw, ch, gap = 108, 30, 6
    per_row = min(len(items), 5)
    rows = (len(items) + per_row - 1) // per_row
    pad = 12
    hdr_h = 30
    w = pad*2 + per_row*cw + (per_row-1)*gap
    h = pad + hdr_h + rows*(ch+gap) + pad

    # Use dark text color for light-background abbreviations
    def abbr_color(brand_color):
        # For very light colors like yellow, use dark text
        if brand_color in ("#F7DF1E", "#FCC624", "#F9AB00"):
            return "#1a1a1a"
        return "#fff"

    cat_safe = cat_name.replace('&', '&amp;')
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<text x="{pad}" y="{pad+14}" font-family="'Courier New',monospace" font-size="12" font-weight="700" fill="{GOLD}" letter-spacing="1">◆ {cat_safe}</text>
<line x1="{pad}" y1="{pad+20}" x2="{w-pad}" y2="{pad+20}" stroke="{GOLD}" stroke-width="0.5" opacity="0.3"/>
'''
    for i,(name,color) in enumerate(items):
        r,c = divmod(i, per_row)
        x = pad + c*(cw+gap)
        y = pad + hdr_h + r*(ch+gap)
        ab = make_abbrev(name)
        ac = abbr_color(color)
        svg += f'''<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="4" fill="{BG2}" stroke="{GOLD}" stroke-width="0.5" stroke-opacity="0.4"/>
<rect x="{x+5}" y="{y+4}" width="{ch-8}" height="{ch-8}" rx="3" fill="{color}" opacity="0.85"/>
<text x="{x+5+(ch-8)//2}" y="{y+4+(ch-8)//2+4}" text-anchor="middle" font-family="'Courier New',monospace" font-size="9" font-weight="700" fill="{ac}">{ab}</text>
<text x="{x+30}" y="{y+19}" font-family="'Courier New',monospace" font-size="11" fill="{TXT}">{name}</text>
'''
    svg += '</svg>\n'
    save(fname, svg)

for i,(cat,items) in enumerate(CATS):
    tech_cat_svg(cat, items, f"tech_{i}.svg")

# ── TECH STACK HEADER ──
save("tech_header.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="500" height="40" viewBox="0 0 500 40">
<line x1="20" y1="20" x2="140" y2="20" stroke="{GOLD}" stroke-width="0.5" opacity="0.5"/>
<polygon points="148,14 154,20 148,26 142,20" fill="{GREEN}" opacity="0.7"/>
<text x="250" y="24" text-anchor="middle" font-family="'Courier New',monospace" font-size="14" font-weight="700" fill="{GOLD}" letter-spacing="3">TECH STACK</text>
<polygon points="352,14 358,20 352,26 346,20" fill="{GREEN}" opacity="0.7"/>
<line x1="364" y1="20" x2="480" y2="20" stroke="{GOLD}" stroke-width="0.5" opacity="0.5"/>
</svg>
''')

# ── SIDEBAR: ABOUT ME ──
save("sidebar_about.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="220" height="175" viewBox="0 0 220 175">
<rect width="220" height="175" rx="6" fill="{BG}" stroke="{GOLD}" stroke-width="0.5" stroke-opacity="0.3"/>
<rect x="8" y="8" width="204" height="24" rx="3" fill="{BG2}"/>
<text x="110" y="24" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" font-weight="700" fill="{GOLD}" letter-spacing="2">ABOUT ME</text>
<line x1="30" y1="36" x2="190" y2="36" stroke="{GOLD}" stroke-width="0.5" opacity="0.3"/>
<text x="16" y="58" font-family="'Courier New',monospace" font-size="10" fill="{TXT}">Senior CS Undergrad</text>
<text x="16" y="74" font-family="'Courier New',monospace" font-size="10" fill="{TXT}">from Bangladesh.</text>
<text x="16" y="96" font-family="'Courier New',monospace" font-size="10" fill="{TXT}">Passionate about building</text>
<text x="16" y="112" font-family="'Courier New',monospace" font-size="10" fill="{TXT}">systems, exploring AI, and</text>
<text x="16" y="128" font-family="'Courier New',monospace" font-size="10" fill="{TXT}">creating tools that make</text>
<text x="16" y="144" font-family="'Courier New',monospace" font-size="10" fill="{TXT}">a difference.</text>
<line x1="30" y1="158" x2="190" y2="158" stroke="{GOLD}" stroke-width="0.5" opacity="0.2"/>
</svg>
''')

# ── SIDEBAR: FOCUS AREAS ──
focuses = [
    ("Gen AI, LLM & DL Research", GREEN),
    ("Data Science & ML", "#61DAFB"),
    ("Full Stack Development", "#F7DF1E"),
    ("Meaningful Research", "#EE4C2C"),
]
fy = 58
focus_lines = ""
for text, color in focuses:
    text_safe = text.replace('&', '&amp;')
    focus_lines += f'<rect x="16" y="{fy-8}" width="8" height="8" rx="2" fill="{color}" opacity="0.7"/>\n'
    focus_lines += f'<text x="30" y="{fy}" font-family="\'Courier New\',monospace" font-size="10" fill="{TXT}">{text_safe}</text>\n'
    fy += 22

save("sidebar_focus.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="220" height="{fy+10}" viewBox="0 0 220 {fy+10}">
<rect width="220" height="{fy+10}" rx="6" fill="{BG}" stroke="{GOLD}" stroke-width="0.5" stroke-opacity="0.3"/>
<rect x="8" y="8" width="204" height="24" rx="3" fill="{BG2}"/>
<text x="110" y="24" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" font-weight="700" fill="{GOLD}" letter-spacing="2">FOCUS AREAS</text>
<line x1="30" y1="36" x2="190" y2="36" stroke="{GOLD}" stroke-width="0.5" opacity="0.3"/>
{focus_lines}
</svg>
''')

# ── SOCIAL ICON SVGs ──
socials = [
    ("icon_github.svg", "GH", "#E2DFD2"),
    ("icon_linkedin.svg", "in", "#0A66C2"),
    ("icon_facebook.svg", "fb", "#1877F2"),
]
for fname, label, color in socials:
    save(fname, f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 36 36">
<rect width="36" height="36" rx="6" fill="{BG2}" stroke="{GOLD}" stroke-width="0.5" stroke-opacity="0.4"/>
<text x="18" y="23" text-anchor="middle" font-family="'Courier New',monospace" font-size="13" font-weight="700" fill="{color}">{label}</text>
</svg>
''')

# ── QUEST LOG ──
save("quest_log.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="620" height="130" viewBox="0 0 620 130">
<text x="310" y="20" text-anchor="middle" font-family="'Courier New',monospace" font-size="14" font-weight="700" fill="{GOLD}" letter-spacing="3">QUEST LOG</text>
<line x1="60" y1="28" x2="250" y2="28" stroke="{GOLD}" stroke-width="0.5" opacity="0.4"/>
<polygon points="305,24 310,30 305,36 300,30" fill="{GREEN}" opacity="0.6"/>
<line x1="370" y1="28" x2="560" y2="28" stroke="{GOLD}" stroke-width="0.5" opacity="0.4"/>
<rect x="20" y="42" width="280" height="70" rx="5" fill="{BG2}" stroke="{GOLD}" stroke-width="0.5" stroke-opacity="0.3"/>
<text x="35" y="64" font-family="'Courier New',monospace" font-size="11" font-weight="700" fill="{GOLD}">??? - Ancient AI Relic</text>
<text x="35" y="82" font-family="'Courier New',monospace" font-size="10" fill="#7a8a6a">Status: Being prepared...</text>
<text x="35" y="100" font-family="'Courier New',monospace" font-size="9" fill="#5a6a4a" font-style="italic">Quest details coming soon.</text>
<rect x="320" y="42" width="280" height="70" rx="5" fill="{BG2}" stroke="{GOLD}" stroke-width="0.5" stroke-opacity="0.3"/>
<text x="335" y="64" font-family="'Courier New',monospace" font-size="11" font-weight="700" fill="{GOLD}">??? - Sacred DL Manuscript</text>
<text x="335" y="82" font-family="'Courier New',monospace" font-size="10" fill="#7a8a6a">Status: Being prepared...</text>
<text x="335" y="100" font-family="'Courier New',monospace" font-size="9" fill="#5a6a4a" font-style="italic">Quest details coming soon.</text>
</svg>
''')

# ── FOOTER ──
save("footer.svg", f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="500" height="50" viewBox="0 0 500 50">
<polygon points="214,18 220,28 214,38 208,28" fill="{GREEN}" opacity="0.5"/>
<text x="250" y="32" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="{GOLD}" opacity="0.7" letter-spacing="1">Thanks for visiting! May the Triforce guide you.</text>
<polygon points="440,12 448,22 440,32 448,22 456,12 448,22 456,32" fill="{GOLD}" opacity="0.4"/>
<polygon points="440,12 448,22 456,12" fill="{GOLD}" opacity="0.35"/>
<polygon points="432,22 440,32 448,22" fill="{GOLD}" opacity="0.35"/>
<polygon points="448,22 456,32 464,22" fill="{GOLD}" opacity="0.35"/>
</svg>
''')

print("\nAll assets generated!")
