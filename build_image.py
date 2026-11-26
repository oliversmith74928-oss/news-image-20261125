#!/usr/bin/env python3
"""Draw the 25 November 2026 world-news front page, 1024x1024 PNG.

Original illustration drawn with Pillow only. No network, no photos,
no copied artwork. Text is the verified news of Wednesday 25 November
2026, cross-checked in Reuters / Straits Times / SCMP / Daily Mirror
summaries dated 25 November 2026.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (251, 247, 237)
INK = (20, 20, 20)
NAVY = (18, 40, 75)
RED = (180, 35, 24)
TEAL = (14, 107, 107)
ORANGE = (194, 87, 26)
GOLD = (150, 110, 20)
GREY = (90, 90, 86)
LIGHT = (238, 232, 214)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=6):
    lines = wrap(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def hline(draw, x0, x1, y, fill=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def icon_chip(draw, cx, cy, r, c1=NAVY):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c1)
    draw.rectangle([cx - r * 0.45, cy - r * 0.45, cx + r * 0.45, cy + r * 0.45],
                   fill=(255, 255, 255))
    draw.rectangle([cx - r * 0.18, cy - r * 0.18, cx + r * 0.18, cy + r * 0.18],
                   fill=c1)
    for dx in (-0.3, 0, 0.3):
        draw.rectangle([cx + dx * r - 3, cy - r * 0.75, cx + dx * r + 3,
                        cy - r * 0.45], fill=(255, 255, 255))
        draw.rectangle([cx + dx * r - 3, cy + r * 0.45, cx + dx * r + 3,
                        cy + r * 0.75], fill=(255, 255, 255))


def icon_scale(draw, cx, cy, r, c1=RED):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c1)
    draw.rectangle([cx - 2, cy - r * 0.55, cx + 2, cy + r * 0.45],
                   fill=(255, 255, 255))
    draw.rectangle([cx - r * 0.55, cy + r * 0.45, cx + r * 0.55, cy + r * 0.55],
                   fill=(255, 255, 255))
    draw.line([(cx, cy - r * 0.55), (cx - r * 0.5, cy - r * 0.2)],
              fill=(255, 255, 255), width=3)
    draw.line([(cx, cy - r * 0.55), (cx + r * 0.5, cy - r * 0.2)],
              fill=(255, 255, 255), width=3)
    draw.ellipse([cx - r * 0.62, cy - r * 0.2, cx - r * 0.38, cy + r * 0.05],
                 fill=(255, 255, 255))
    draw.ellipse([cx + r * 0.38, cy - r * 0.2, cx + r * 0.62, cy + r * 0.05],
                 fill=(255, 255, 255))


def icon_rocket(draw, cx, cy, r, c1=TEAL):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c1)
    draw.rectangle([cx - r * 0.22, cy - r * 0.55, cx + r * 0.22,
                    cy + r * 0.25], fill=(255, 255, 255))
    draw.polygon([(cx - r * 0.22, cy - r * 0.55), (cx + r * 0.22, cy - r * 0.55),
                  (cx, cy - r * 0.85)], fill=(255, 255, 255))
    draw.polygon([(cx - r * 0.22, cy + r * 0.10), (cx - r * 0.45, cy + r * 0.45),
                  (cx - r * 0.22, cy + r * 0.30)], fill=(255, 255, 255))
    draw.polygon([(cx + r * 0.22, cy + r * 0.10), (cx + r * 0.45, cy + r * 0.45),
                  (cx + r * 0.22, cy + r * 0.30)], fill=(255, 255, 255))
    draw.polygon([(cx - r * 0.12, cy + r * 0.25), (cx + r * 0.12, cy + r * 0.25),
                  (cx, cy + r * 0.62)], fill=(255, 200, 60))


def icon_tower(draw, cx, cy, r, c1=ORANGE):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c1)
    x0, y0 = cx - r * 0.45, cy + r * 0.5
    draw.rectangle([x0, y0 - r * 0.9, x0 + r * 0.18, y0], fill=(255, 255, 255))
    draw.rectangle([cx - r * 0.09, y0 - r * 1.1, cx + r * 0.09, y0],
                   fill=(255, 255, 255))
    draw.rectangle([cx + r * 0.27, y0 - r * 0.7, cx + r * 0.45, y0],
                   fill=(255, 255, 255))
    draw.polygon([(cx - r * 0.09, y0 - r * 1.1), (cx + r * 0.09, y0 - r * 1.1),
                  (cx, y0 - r * 1.35)], fill=(255, 255, 255))


def icon_shield(draw, cx, cy, r, c1=NAVY):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c1)
    pts = [(cx, cy - r * 0.6), (cx + r * 0.45, cy - r * 0.35),
           (cx + r * 0.45, cy + r * 0.1), (cx, cy + r * 0.6),
           (cx - r * 0.45, cy + r * 0.1), (cx - r * 0.45, cy - r * 0.35)]
    draw.polygon(pts, fill=(255, 255, 255))
    draw.line([(cx - r * 0.2, cy), (cx - r * 0.02, cy + r * 0.2),
               (cx + r * 0.25, cy - r * 0.25)], fill=c1, width=4)


def icon_globe(draw, cx, cy, r, c1=GOLD):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c1)
    draw.ellipse([cx - r * 0.55, cy - r * 0.55, cx + r * 0.55, cy + r * 0.55],
                 outline=(255, 255, 255), width=3)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=(255, 255, 255), width=3)
    draw.line([(cx, cy - r), (cx, cy + r)], fill=(255, 255, 255), width=3)


def draw_card(draw, x, y, w, h, tag, tag_color, headline, deck, icon_fn):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           outline=(200, 192, 170), width=2, fill=(255, 255, 255))
    draw.rounded_rectangle([x, y, x + w, y + 32], radius=10, fill=tag_color)
    draw.rectangle([x, y + 18, x + w, y + 32], fill=tag_color)
    draw.text((x + 12, y + 7), tag, font=font(SANS_B, 13), fill=(255, 255, 255))
    icon_fn(draw, x + 38, y + 72, 26)
    yy = para(draw, x + 74, y + 42, headline, font(SERIF_B, 21), w - 86,
              leading=2)
    deck_y = max(yy + 4, y + 108)
    para(draw, x + 12, deck_y, deck, font(SANS, 14), w - 24, fill=(60, 60, 58),
         leading=3)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([4, 4, W - 5, H - 5], outline=NAVY, width=5)

    # Masthead
    d.text((W // 2, 28), "THE WORLD  •  IN ONE IMAGE",
           font=font(SANS_B, 20), fill=GREY, anchor="ma")
    d.text((W // 2, 56), "THE WORLD TODAY",
           font=font(SERIF_B, 76), fill=INK, anchor="ma")
    hline(d, 28, W - 28, 146, fill=INK, width=3)
    d.rectangle([28, 154, W - 28, 198], fill=NAVY)
    d.text((W // 2, 164), "WEDNESDAY  25  NOVEMBER  2026",
           font=font(SANS_B, 30), fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 204), "Tariffs, a chip rout, a verdict, a launch — and a region on edge",
           font=font(SANS, 17), fill=GREY, anchor="ma")

    # Lead story
    lx, ly, lw = 28, 232, 600
    d.text((lx, ly), "TRADE  •  WASHINGTON", font=font(SANS_B, 17), fill=RED)
    y = para(d, lx, ly + 28, "US plans tariffs of up to 20% on China, the EU and 12 others",
             font(SERIF_B, 38), lw, leading=3)
    y = para(d, lx, y + 8,
             "A USTR probe into excess industrial capacity paves the way for "
             "new duties next year — and rattles the chip markets.",
             font(SANS, 18), lw, fill=(60, 60, 58), leading=4)

    # Lead illustration: bar chart of market falls (closing moves, 25 Nov)
    px, py, pw, ph = 652, 232, 344, 200
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=10, fill=NAVY)
    d.text((px + pw // 2, py + 12), "THE CHIP ROUT — 25 NOV",
           font=font(SANS_B, 15), fill=(255, 255, 255), anchor="ma")
    bars = [("TAIWAN", "-4.8%", 0.78), ("KOREA", "-6.2%", 1.0),
            ("JAPAN", "-2.8%", 0.45), ("NVIDIA", "-5.9%", 0.95)]
    bw, gap = 52, 22
    bx = px + 28
    for name, label, frac in bars:
        bh = int(92 * frac)
        d.rectangle([bx, py + 148 - bh, bx + bw, py + 148],
                    fill=(255, 255, 255))
        d.rectangle([bx, py + 148 - bh, bx + bw, py + 148 - bh + 8],
                    fill=(255, 200, 60))
        d.text((bx + bw // 2, py + 126 - bh), label, font=font(SANS_B, 12),
               fill=(255, 200, 60), anchor="ma")
        d.text((bx + bw // 2, py + 154), name, font=font(SANS_B, 12),
               fill=(255, 255, 255), anchor="ma")
        bx += bw + gap
    d.text((px + pw // 2, py + 176), "Samsung -9.9%  •  SK Hynix -10.3%  •  TSMC -3.6%",
           font=font(SANS, 12), fill=(255, 255, 255), anchor="ma")
    hline(d, 28, W - 28, 450, fill=INK, width=2)

    # Story cards: 3 across, 2 rows
    cw, ch, gx = 312, 196, 16
    x0, y0 = 28, 466
    draw_card(d, x0, y0, cw, ch, "TECH  •  VERDICT", RED,
              "Huawei convicted by a US jury",
              "Fraud, trade-secret theft and Iran sanctions breaches. "
              "Beijing accuses Washington of suppressing Chinese firms.",
              icon_scale)
    draw_card(d, x0 + cw + gx, y0, cw, ch, "SPACE  •  TIANGONG", TEAL,
              "First Pakistani astronaut in orbit",
              "Muhammad Zeeshan Ali flies aboard Shenzhou-24 to China's "
              "Tiangong station — a first for Pakistan.",
              icon_rocket)
    draw_card(d, x0 + 2 * (cw + gx), y0, cw, ch, "MIDDLE EAST", ORANGE,
              "Houthi strike hits Riyadh's tallest tower",
              "Eleven hurt in a second attack in under a week, as shipping "
              "in the Strait of Hormuz comes under fire.",
              icon_tower)
    y1 = y0 + ch + 16
    draw_card(d, x0, y1, cw, ch, "WAR  •  UKRAINE", NAVY,
              "Ukraine hits Russian energy sites",
              "Strikes on energy infrastructure as peace talks continue. "
              "Moscow's own figures put war deaths near 500,000.",
              icon_shield)
    draw_card(d, x0 + cw + gx, y1, cw, ch, "CYBER  •  WASHINGTON", GOLD,
              "Unclassified CIA system breached",
              "The latest US cybersecurity incident, amid wider concern "
              "over digital security after recent tech outages.",
              icon_chip)
    draw_card(d, x0 + 2 * (cw + gx), y1, cw, ch, "PACIFIC  •  TREATY", TEAL,
              "Solomon Islands signs Australia pact",
              "A sweeping security treaty: no foreign military bases on "
              "its territory, in a win for Canberra.",
              icon_globe)

    # Bottom strip
    hline(d, 28, W - 28, 890, fill=INK, width=2)
    d.text((28, 904), "ALSO TODAY", font=font(SANS_B, 16), fill=RED)
    para(d, 28, 928,
         "GAZA  Israeli strike kills a Hamas security chief  •  BANGLADESH  "
         "Garment wage rises 36% after protests  •  IOWA  Army blows up "
         "unstable explosives  •  NEW YORK  Macy's parade postponed by a "
         "storm  •  CAIRO  Dozens dead in a fire  •  MISSISSIPPI  Six killed "
         "in a plane crash",
         font(SANS, 15), W - 56, fill=(60, 60, 58), leading=4)
    d.text((W // 2, 990), "25 NOVEMBER 2026  •  An original illustration of the day's news",
           font=font(SANS, 14), fill=GREY, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
