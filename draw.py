"""Draw the 20 November 2026 news image with Pillow (local build tool only).

The submitted program is main.ts, which only copies entry.png.
This script is how entry.png was made, so the picture is reproducible
from the same six verified stories. Run: python3 draw.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 20, 20)
RED = (178, 34, 34)
BLUE = (24, 68, 128)
GREEN = (34, 120, 70)
GOLD = (176, 128, 20)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 10], fill=INK)

# Header
d.text((32, 28), "THE WORLD IN ONE DAY", font=font(BOLD, 26), fill=RED)
d.text((32, 62), "FRIDAY 20 NOVEMBER 2026", font=font(SERIF, 58), fill=INK)
d.rectangle([32, 138, 992, 144], fill=RED)
d.text(
    (32, 156),
    "Genocide ruling  •  Three-power summit  •  Markets fall",
    font=font(BOLD, 24),
    fill=INK,
)
d.text(
    (32, 188),
    "Kyiv struck  •  Riyadh hit  •  Ebola ends in Kenya",
    font=font(BOLD, 24),
    fill=INK,
)

stories = [
    ("WORLD COURT  •  THE HAGUE", "ICJ rules Myanmar committed genocide against Rohingya",
     "First such ruling against a state by the world court.", RED),
    ("SHENZHEN SUMMIT  •  CHINA", "Trump, Xi and Putin meet, issue joint peace declaration",
     "First three-way summit of the three leaders.", BLUE),
    ("MARKETS FALL  •  NEW YORK", "Anthropic falls to about $87; Bitcoin below $60,000",
     "Closed its debut at $97, then fell ~10% on Friday.", RED),
    ("KYIV ATTACKED  •  UKRAINE", "Russian overnight strikes hit Kyiv bridges; 8 killed",
     "28 injured across nine regions, officials say.", INK),
    ("RIYADH HIT  •  SAUDI ARABIA", "Houthi missile damages Saudi wealth-fund tower",
     "Strike hits Riyadh's financial district.", BLUE),
    ("EBOLA ENDS  •  KENYA", "Kenya discharges its last Ebola patient",
     "37 days after its first case. The day's good news.", GREEN),
]

# Six panels: 2 columns x 3 rows
x0, y0, pw, ph, gap = 32, 232, 474, 240, 12
for i, (kicker, head, body, colour) in enumerate(stories):
    x = x0 + (i % 2) * (pw + gap)
    y = y0 + (i // 2) * (ph + gap)
    d.rectangle([x, y, x + pw, y + ph], fill=(255, 255, 255),
                outline=(200, 190, 170), width=2)
    d.rectangle([x, y, x + 10, y + ph], fill=colour)
    d.text((x + 26, y + 16), kicker, font=font(BOLD, 19), fill=colour)
    lines = wrap(d, head, font(BOLD, 27), pw - 52)
    yy = y + 48
    for line in lines[:3]:
        d.text((x + 26, yy), line, font=font(BOLD, 27), fill=INK)
        yy += 34
    blines = wrap(d, body, font(REG, 20), pw - 52)
    for line in blines[:2]:
        d.text((x + 26, yy + 6), line, font=font(REG, 20), fill=(70, 70, 70))
        yy += 26

# Footer
d.rectangle([32, 976, 992, 980], fill=INK)
d.text((32, 988), "20 NOVEMBER 2026  —  SIX STORIES, ONE DAY",
       font=font(BOLD, 20), fill=INK)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
