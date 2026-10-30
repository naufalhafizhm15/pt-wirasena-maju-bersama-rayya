import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

CANVAS_W = 1110
CANVAS_H = 697
TRIM_W = 1063
TRIM_H = 650
BLEED_X = (CANVAS_W - TRIM_W) // 2
BLEED_Y = (CANVAS_H - TRIM_H) // 2

out_dir = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/business-card/master-cetak'

BG_DARK = (0, 33, 19)          # Deep obsidian emerald green #002113
C_LIGHT_GREEN = (0, 154, 76)    # Emerald base #009A4C
C_PALE_GREEN = (104, 219, 154)  # Mint highlight #68DB9A
C_MID_GREEN = (0, 185, 96)     # Mid green #00B960
C_WHITE = (255, 255, 255)
C_MUTED = (160, 195, 180)

font_bold = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
font_reg = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

f_brand = ImageFont.truetype(font_bold, 56)
f_sub = ImageFont.truetype(font_reg, 16)
f_name = ImageFont.truetype(font_bold, 44)
f_title = ImageFont.truetype(font_reg, 20)
f_contact = ImageFont.truetype(font_reg, 18)

# Load the exact extracted emblem from reference
emblem_path = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/sisyphus-emblem-exact.png'
emblem = Image.open(emblem_path).convert('RGBA')

# 1. FRONT
front = Image.new('RGB', (CANVAS_W, CANVAS_H), BG_DARK)
draw_f = ImageDraw.Draw(front)

# Diagonal isometric pillars
poly1_dark = [(BLEED_X, BLEED_Y + 450), (BLEED_X + 280, BLEED_Y + 170), (BLEED_X + 280, BLEED_Y + 380), (BLEED_X + 60, BLEED_Y + 600), (BLEED_X, BLEED_Y + 600)]
draw_f.polygon(poly1_dark, fill=C_MID_GREEN)

poly1_light = [(BLEED_X, BLEED_Y + 600), (BLEED_X + 60, BLEED_Y + 600), (BLEED_X + 280, BLEED_Y + 380), (BLEED_X + 280, BLEED_Y + 590), (BLEED_X + 60, BLEED_Y + TRIM_H), (BLEED_X, BLEED_Y + TRIM_H)]
draw_f.polygon(poly1_light, fill=C_PALE_GREEN)

poly_b1 = [(BLEED_X, BLEED_Y + 600), (BLEED_X + 60, BLEED_Y + 600), (BLEED_X + 60, BLEED_Y + TRIM_H), (BLEED_X, BLEED_Y + TRIM_H)]
draw_f.polygon(poly_b1, fill=C_LIGHT_GREEN)

draw_f.rectangle([BLEED_X + 280, BLEED_Y + 600, BLEED_X + 500, BLEED_Y + TRIM_H], fill=C_LIGHT_GREEN)
draw_f.rectangle([BLEED_X + 620, BLEED_Y, BLEED_X + 840, BLEED_Y + 95], fill=C_LIGHT_GREEN)

poly2_face1 = [(BLEED_X + 840, BLEED_Y), (BLEED_X + 840, BLEED_Y + 95), (BLEED_X + TRIM_W, BLEED_Y + 95), (BLEED_X + TRIM_W, BLEED_Y)]
draw_f.polygon(poly2_face1, fill=C_LIGHT_GREEN)

poly2_diag_light = [(BLEED_X + 840, BLEED_Y), (BLEED_X + 840, BLEED_Y + 480), (BLEED_X + 970, BLEED_Y + 350), (BLEED_X + 970, BLEED_Y + 95), (BLEED_X + TRIM_W, BLEED_Y + 95), (BLEED_X + TRIM_W, BLEED_Y)]
draw_f.polygon(poly2_diag_light, fill=C_PALE_GREEN)

poly2_diag_mid = [(BLEED_X + 840, BLEED_Y + 480), (BLEED_X + TRIM_W, BLEED_Y + 320), (BLEED_X + TRIM_W, BLEED_Y + TRIM_H), (BLEED_X + 840, BLEED_Y + TRIM_H)]
draw_f.polygon(poly2_diag_mid, fill=C_MID_GREEN)

poly2_diag_dark = [(BLEED_X + 970, BLEED_Y + 95), (BLEED_X + TRIM_W, BLEED_Y + 95), (BLEED_X + TRIM_W, BLEED_Y + 230), (BLEED_X + 970, BLEED_Y + 350)]
draw_f.polygon(poly2_diag_dark, fill=C_LIGHT_GREEN)

# Resize exact Sisyphus emblem
emb_front = emblem.resize((180, 270), Image.Resampling.LANCZOS)
front.paste(emb_front, ((CANVAS_W - emb_front.size[0]) // 2, BLEED_Y + 140), emb_front)

# Title: Wirasena
brand_text = "Wirasena"
w_bt = draw_f.textlength(brand_text, font=f_brand)
draw_f.text(((CANVAS_W - w_bt) // 2, BLEED_Y + 430), brand_text, fill=C_WHITE, font=f_brand)

p_front = os.path.join(out_dir, 'MASTER-CETAK-KARTU-DEPAN-300DPI.png')
front.save(p_front, dpi=(300, 300), quality=100)

# 2. BACK
back = Image.new('RGB', (CANVAS_W, CANVAS_H), BG_DARK)
draw_b = ImageDraw.Draw(back)

qr = qrcode.QRCode(version=1, box_size=5, border=1)
qr.add_data('https://wa.me/6285221060766')
qr.make(fit=True)
qr_img = qr.make_image(fill_color='black', back_color='white').convert('RGBA')
qr_img = qr_img.resize((150, 150), Image.Resampling.NEAREST)

qr_x = BLEED_X + 80
qr_y = BLEED_Y + 70
back.paste(qr_img, (qr_x, qr_y))

web_text = "www.wirasenaraya.com"
draw_b.text((BLEED_X + 380, BLEED_Y + 120), web_text, fill=C_WHITE, font=f_title)

# Paste exact emblem on top right
emb_back = emblem.resize((140, 210), Image.Resampling.LANCZOS)
back.paste(emb_back, (BLEED_X + TRIM_W - 220, BLEED_Y + 45), emb_back)

name_text = "Yongki Kav"
draw_b.text((BLEED_X + 80, BLEED_Y + 280), name_text, fill=C_WHITE, font=f_name)

role_text = "Sales & Business Development Director"
draw_b.text((BLEED_X + 80, BLEED_Y + 345), role_text, fill=C_MUTED, font=f_title)

email_text = "marketing@wirasenaraya.com"
draw_b.text((BLEED_X + 80, BLEED_Y + 520), email_text, fill=C_WHITE, font=f_contact)

phone_text = "+62 852 2106 0766"
w_ph = draw_b.textlength(phone_text, font=f_contact)
draw_b.text((BLEED_X + TRIM_W - 80 - w_ph, BLEED_Y + 520), phone_text, fill=C_WHITE, font=f_contact)

p_back = os.path.join(out_dir, 'MASTER-CETAK-KARTU-BELAKANG-300DPI.png')
back.save(p_back, dpi=(300, 300), quality=100)

# Save PDF (2 pages)
pdf_path = os.path.join(out_dir, 'MASTER-CETAK-KARTU-NAMA-YONGKI-KAV-300DPI.pdf')
front.save(pdf_path, "PDF", resolution=300.0, save_all=True, append_images=[back])

# Re-render showcase with a timestamped name to bypass browser cache
w, h = front.size
show = Image.new('RGB', (w * 2 + 100, h + 100), '#081410')
show.paste(front, (40, 50))
show.paste(back, (w + 60, 50))
out_show = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/business-card/showcase-sisyphus-v3.png'
show.save(out_show, quality=95)
# Also overwrite main showcase
show.save('/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/business-card/showcase-sisyphus-style.png', quality=95)

print("Master v3 with EXACT Sisyphus isometric emblem generated!")
