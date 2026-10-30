import os
from PIL import Image, ImageDraw, ImageFont

# Dimensions for 90x55 mm at 300 DPI: 1063 x 650 px
WIDTH = 1063
HEIGHT = 650

assets_dir = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets'
img_dir = os.path.join(assets_dir, 'images')
out_dir = os.path.join(assets_dir, 'business-card')
os.makedirs(out_dir, exist_ok=True)

# 1. GENERATE FRONT CARD (Dark Luxe Emerald with 3D Logo)
front = Image.new('RGB', (WIDTH, HEIGHT), '#0F2622')
draw_front = ImageDraw.Draw(front)

# Decorative background accent curves / lines
for i in range(12):
    draw_front.ellipse([-200 + i*15, -150 + i*10, 600 + i*20, 750 + i*15], outline=(25, 65, 58, 40), width=2)
    draw_front.ellipse([WIDTH - 500 + i*10, -200 + i*15, WIDTH + 300 + i*15, 600 + i*10], outline=(46, 125, 75, 30), width=2)

# Paste Logo Avatar or Logo Trans
logo_path = os.path.join(img_dir, 'logo-avatar-full.png')
if not os.path.exists(logo_path):
    logo_path = os.path.join(img_dir, 'logo-trans.png')

logo = Image.open(logo_path).convert('RGBA')
# Resize logo to fit nicely on the front card
logo_size = 280
logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)

# Paste centered vertically on left or center
front.paste(logo, ((WIDTH - logo.size[0]) // 2, 90), logo)

# Text on front
try:
    font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 19)
    font_tag = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf", 16)
except:
    font_bold = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_tag = ImageFont.load_default()

# Title
company_name = "PT. WIRASENA MAJU BERSAMA RAYYA"
w_title = draw_front.textlength(company_name, font=font_bold)
draw_front.text(((WIDTH - w_title) // 2, 400), company_name, fill="#FFFFFF", font=font_bold)

# Subtitle
sub_text = "General Supplier Pabrik • Manufaktur Kemasan • Jasa Fabrikasi"
w_sub = draw_front.textlength(sub_text, font=font_sub)
draw_front.text(((WIDTH - w_sub) // 2, 455), sub_text, fill="#78B89E", font=font_sub)

# Tagline / Accent Bar
tagline = "Mitra Pengadaan & Otomasi Presisi Kawasan Industri Cikarang & Karawang"
w_tag = draw_front.textlength(tagline, font=font_tag)
draw_front.text(((WIDTH - w_tag) // 2, 510), tagline, fill="#A3C7BD", font=font_tag)

# Bottom gold / emerald accent line
draw_front.rectangle([180, 560, WIDTH - 180, 563], fill="#34D399")

front_path = os.path.join(out_dir, 'kartu-nama-depan.png')
front.save(front_path, quality=95)
print("Front card generated at:", front_path)


# 2. GENERATE BACK CARD (Modern Executive Profile + Smart QR Code)
back = Image.new('RGB', (WIDTH, HEIGHT), '#FFFFFF')
draw_back = ImageDraw.Draw(back)

# Top accent bar (Dark Emerald)
draw_back.rectangle([0, 0, WIDTH, 16], fill="#102A25")
draw_back.rectangle([0, 16, WIDTH, 22], fill="#34D399")

# Left side decorative vertical pillar
draw_back.rectangle([0, 22, 14, HEIGHT], fill="#102A25")

# Left Column: Identity & Contact Info
# Name: Yongki Kav
try:
    font_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    font_role = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    font_pt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
    font_contact = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    font_bold_contact = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    font_qr_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
except:
    font_name = ImageFont.load_default()
    font_role = ImageFont.load_default()
    font_pt = ImageFont.load_default()
    font_contact = ImageFont.load_default()
    font_bold_contact = ImageFont.load_default()
    font_qr_label = ImageFont.load_default()

# Name & Title
draw_back.text((60, 60), "Yongki Kav", fill="#0F2622", font=font_name)
draw_back.text((60, 115), "Sales & Business Development Director", fill="#237B35", font=font_role)
draw_back.text((60, 145), "PT. WIRASENA MAJU BERSAMA RAYYA", fill="#64748B", font=font_pt)

# Separator line
draw_back.line([(60, 185), (680, 185)], fill="#E2E8F0", width=2)

# Contact rows
y = 215
contacts = [
    ("WhatsApp / Telp :", " 0852-2106-0766 (Official B2B Line)"),
    ("Email Resmi        :", " marketing@wirasenaraya.com"),
    ("Website Resmi     :", " www.wirasenaraya.com"),
    ("Lokasi Workshop :", " Jl. Bah Kilong Kp. Kandang, Sukadami,"),
    ("                               ", " Cikarang Selatan, Bekasi 17530")
]

for label, val in contacts:
    draw_back.text((60, y), label, fill="#64748B", font=font_contact)
    draw_back.text((250, y), val, fill="#0F2622", font=font_bold_contact)
    y += 42

# Right Column: Smart QR Code Box
qr_box_x = 740
qr_box_y = 80
qr_box_w = 265
qr_box_h = 490

# Rounded-like background for QR box
draw_back.rectangle([qr_box_x, qr_box_y, qr_box_x + qr_box_w, qr_box_y + qr_box_h], fill="#F8FAFC", outline="#E2E8F0", width=2)
draw_back.rectangle([qr_box_x, qr_box_y, qr_box_x + qr_box_w, qr_box_y + 40], fill="#102A25")
draw_back.text((qr_box_x + 28, qr_box_y + 12), "SMART CONTACT", fill="#34D399", font=font_qr_label)

# Paste QR Code
qr_path = os.path.join(img_dir, 'qr-code-wa-yongki.png')
if os.path.exists(qr_path):
    qr_img = Image.open(qr_path).convert('RGBA')
    qr_img.thumbnail((220, 220), Image.Resampling.LANCZOS)
    back.paste(qr_img, (qr_box_x + (qr_box_w - qr_img.size[0]) // 2, qr_box_y + 65), qr_img)

# QR helper labels
draw_back.text((qr_box_x + 18, qr_box_y + 315), "Scan Kamera HP untuk:", fill="#0F2622", font=font_qr_label)
draw_back.text((qr_box_x + 18, qr_box_y + 345), "✓ Chat Langsung WhatsApp", fill="#237B35", font=font_pt)
draw_back.text((qr_box_x + 18, qr_box_y + 375), "✓ Simpan Kontak Otomatis", fill="#237B35", font=font_pt)
draw_back.text((qr_box_x + 18, qr_box_y + 405), "✓ Buka Katalog & Web PT", fill="#237B35", font=font_pt)

# Small bottom accent on right box
draw_back.rectangle([qr_box_x, qr_box_y + qr_box_h - 10, qr_box_x + qr_box_w, qr_box_y + qr_box_h], fill="#34D399")

# Bottom card accent line
draw_back.rectangle([0, HEIGHT - 12, WIDTH, HEIGHT], fill="#102A25")

back_path = os.path.join(out_dir, 'kartu-nama-belakang.png')
back.save(back_path, quality=95)
print("Back card generated at:", back_path)

