"""
Generates the SVG files used by README.md.
Edit the DATA section below, run `python generate_assets.py`, commit the assets folder.
"""
from html import escape
import os

# ---------- Design tokens (dark only) ----------
BG       = "#0F1114"   # page / window
SURFACE  = "#14171B"   # cards
HAIRLINE = "#262B31"
TEXT     = "#E6E8EB"   # primary
TEXT_2   = "#9AA1AA"   # secondary
TEXT_3   = "#6B727B"   # muted
ACCENT   = "#E5A94B"   # amber, the only accent
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"

W = 888  # GitHub's readme content width

# ---------- DATA: edit these ----------
WHOAMI = [
    ("name",      "Soumen Sen"),
    ("studies",   "CSE, International Islamic University Chittagong"),
    ("based in",  "Chittagong, Bangladesh"),
    ("builds",    "machine learning, full-stack web, embedded systems"),
    ("site",      "soumen.me"),
]

PROJECTS = [
    # (file name, title, one-line description, category)
    ("movie-recommendation", "Movie recommendation model",
     "Machine learning model that recommends movies", "Machine learning"),
    ("food-delivery", "Food delivery time prediction",
     "Predicts how long a food delivery will take", "Machine learning"),
    ("dsa", "Data structures and algorithms",
     "A collection of data structure and algorithm work", "Algorithms"),
    ("deep-learning", "Deep learning model",
     "Deep learning model implementation", "Deep learning"),
    ("bank-management", "Bank management system",
     "Software for managing bank accounts", "Software"),
    ("mental-health", "Student mental health score prediction",
     "Predicts a mental health score for students", "Machine learning"),
]

STACK = [
    ("Data science", ["NumPy", "Pandas", "Matplotlib", "Seaborn", "SciPy", "scikit-learn"]),
    ("Web",          ["HTML5", "CSS3", "JavaScript", "Tailwind", "DaisyUI", "React", "Django", "Flask", "Vite", "GSAP"]),
    ("Languages",    ["Python", "C++", "C"]),
    ("Tools",        ["Git", "VS Code", "Postman", "Arduino", "MongoDB", "Firebase"]),
]

# ---------- Builders ----------
def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">\n{body}\n</svg>\n')

def header():
    H = 300
    out = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="{BG}" stroke="{HAIRLINE}"/>',
           f'<line x1="0.5" y1="44.5" x2="{W-0.5}" y2="44.5" stroke="{HAIRLINE}"/>',
           f'<text x="24" y="28" font-family="{MONO}" font-size="12" fill="{TEXT_3}">soumen / whoami.py</text>',
           f'<text x="28" y="84" font-family="{MONO}" font-size="15" fill="{ACCENT}">$</text>',
           f'<text x="48" y="84" font-family="{MONO}" font-size="15" fill="{TEXT}">python whoami.py</text>']
    y = 124
    for i, (label, value) in enumerate(WHOAMI):
        size, weight, color = (20, 500, "#F4F5F7") if i == 0 else (15, 400, TEXT)
        out.append(f'<text x="48" y="{y}" font-family="{MONO}" font-size="14" fill="{TEXT_3}">{escape(label)}</text>')
        out.append(f'<text x="176" y="{y}" font-family="{MONO}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>')
        y += 30 if i == 0 else 28
    out.append(f'<text x="28" y="{y+12}" font-family="{MONO}" font-size="15" fill="{ACCENT}">$</text>')
    out.append(f'<rect x="48" y="{y-1}" width="9" height="18" fill="{ACCENT}"/>')
    return svg(W, H, "\n".join(out), "Terminal output of whoami.py: Soumen Sen, CSE student")

def project_row(index, title, desc, category):
    H = 72
    out = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="{SURFACE}" stroke="{HAIRLINE}"/>',
           f'<text x="24" y="42" font-family="{MONO}" font-size="13" fill="{TEXT_3}">{index:02d}</text>',
           f'<text x="64" y="32" font-family="{SANS}" font-size="16" font-weight="500" fill="{TEXT}">{escape(title)}</text>',
           f'<text x="64" y="53" font-family="{SANS}" font-size="13" fill="{TEXT_2}">{escape(desc)}</text>',
           f'<text x="{W-24}" y="42" text-anchor="end" font-family="{MONO}" font-size="12" fill="{TEXT_3}">{escape(category)}</text>']
    return svg(W, H, "\n".join(out), f"{title}: {desc}")

def stack():
    row_h = 40
    pad = 8
    H = pad*2 + row_h*len(STACK)
    out = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="{SURFACE}" stroke="{HAIRLINE}"/>']
    for i, (label, items) in enumerate(STACK):
        y = pad + row_h*i + 25
        if i:
            out.append(f'<line x1="24" y1="{pad+row_h*i+0.5}" x2="{W-24}" y2="{pad+row_h*i+0.5}" stroke="{HAIRLINE}"/>')
        out.append(f'<text x="24" y="{y}" font-family="{MONO}" font-size="13" fill="{TEXT_3}">{escape(label)}</text>')
        text = "  ·  ".join(escape(t) for t in items)
        out.append(f'<text x="176" y="{y}" font-family="{SANS}" font-size="14" fill="{TEXT}" xml:space="preserve">{text}</text>')
    flat = "; ".join(f"{l}: {', '.join(i)}" for l, i in STACK)
    return svg(W, H, "\n".join(out), "Languages and tools. " + flat)

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    open("assets/header.svg", "w").write(header())
    for n, (slug, title, desc, cat) in enumerate(PROJECTS, 1):
        open(f"assets/project-{slug}.svg", "w").write(project_row(n, title, desc, cat))
    open("assets/stack.svg", "w").write(stack())
    print("done")
