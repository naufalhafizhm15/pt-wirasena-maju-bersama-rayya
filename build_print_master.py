import os
from PIL import Image, ImageDraw, ImageFont

# 1. SETUP SPECIFICATIONS (Percetakan Digital / Offset Indonesia)
# Standard Size: 90 x 55 mm
# Bleed: 2 mm on each side -> 94 x 59 mm
# 300 DPI:
# Canvas with Bleed = 1110 x 697 px
# Trim Box = 1063 x 650 px (centered)
# Offset Bleed: dx = 23 px, dy = 23 px

CANVAS_W = 1110
CANVAS_H = 697
TRIM_W = 1063
TRIM_H = 650
BLEED_X = (CANVAS_W - TRIM_W) // 2
BLEED_Y = (CANVAS_H - TRIM_H) // 2

out_dir = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/business-card/master-cetak'
os.makedirs(out_dir, exist_ok=True)

# Fonts
font_sans_bold = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
font_sans_reg = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

f_corp_name = ImageFont.truetype(font_sans_bold, 34)
f_tagline = ImageFont.truetype(font_sans_reg, 16)
f_meta = ImageFont.truetype(font_sans_reg, 13)

f_person_name = ImageFont.truetype(font_sans_bold, 38)
f_person_title = ImageFont.truetype(font_sans_bold, 17)
f_person_corp = ImageFont.truetype(font_sans_reg, 15)

f_label = ImageFont.truetype(font_sans_bold, 13)
f_val = ImageFont.truetype(font_sans_bold, 17)
f_val_sub = ImageFont.truetype(font_sans_reg, 15)
f_qr_helper = ImageFont.truetype(font_sans_bold, 13)
f_qr_sub = ImageFont.truetype(font_sans_reg, 12)

# Colors matching Option 1 (Deep Forest Emerald + Crisp Swiss Layout)
COLOR_EMERALD_DARK = '#0F2622'
COLOR_EMERALD_ACCENT = '#2E7D32'
COLOR_EMERALD_MINT = '#34D399'
COLOR_TEXT_DARK = '#0F172A'
COLOR_TEXT_MUTED = '#64748B'
COLOR_HAIRLINE = '#E2E8F0'

# Image paths
logo_path = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/logo-avatar-full.png'
qr_path = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/qr-code-wa-yongki.png'

# Helper: Draw Printer Crop Marks
def draw_crop_marks(img):
    draw = ImageDraw.Draw(img)
    mark_len = 16
    mark_col = (120, 120, 120)
    
    x1, y1 = BLEED_X, BLEED_Y
    x2, y2 = BLEED_X + TRIM_W, BLEED_Y + TRIM_H
    
    # Top-Left
    draw.line([(x1, 0), (x1, mark_len)], fill=mark_col, width=1)
    draw.line([(0, y1), (mark_len, y1)], fill=mark_col, width=1)
    
    # Top-Right
    draw.line([(x2, 0), (x2, mark_len)], fill=mark_col, width=1)
    draw.line([(CANVAS_W - mark_len, y1), (CANVAS_W, y1)], fill=mark_col, width=1)
    
    # Bottom-Left
    draw.line([(x1, CANVAS_H - mark_len), (x1, CANVAS_H)], fill=mark_col, width=1)
    draw.line([(0, y2), (mark_len, y2)], fill=mark_col, width=1)
    
    # Bottom-Right
    draw.line([(x2, CANVAS_H - mark_len), (x2, CANVAS_H)], fill=mark_col, width=1)
    draw.line([(CANVAS_W - mark_len, y2), (CANVAS_W, y2)], fill=mark_col, width=1)

# =========================================================
# 1. GENERATE MASTER FRONT (SISI DEPAN) - DEEP EMERALD MATTE
# =========================================================
front = Image.new('RGB', (CANVAS_W, CANVAS_H), COLOR_EMERALD_DARK)
draw_f = ImageDraw.Draw(front)

# Center Logo
logo = Image.open(logo_path).convert('RGBA')
logo.thumbnail((260, 260), Image.Resampling.LANCZOS)
logo_x = (CANVAS_W - logo.size[0]) // 2
logo_y = BLEED_Y + 95
front.paste(logo, (logo_x, logo_y), logo)

# Text: PT. WIRASENA MAJU BERSAMA RAYYA
t_name = "PT. WIRASENA MAJU BERSAMA RAYYA"
w_name = draw_f.textlength(t_name, font=f_corp_name)
draw_f.text(((CANVAS_W - w_name) // 2, BLEED_Y + 390), t_name, fill='#FFFFFF', font=f_corp_name)

# Text: 3 Pillars
t_tag = "SUPPLIER KEBUTUHAN PABRIK   •   CARTON BOX   •   FABRIKASI"
w_tag = draw_f.textlength(t_tag, font=f_tagline)
draw_f.text(((CANVAS_W - w_tag) // 2, BLEED_Y + 448), t_tag, fill='#8BB0A4', font=f_tagline)

# Text: Location & URL
t_loc = "SUKADAMI, CIKARANG SELATAN   •   WWW.WIRASENARAYA.COM"
w_loc = draw_f.textlength(t_loc, font=f_meta)
draw_f.text(((CANVAS_W - w_loc) // 2, BLEED_Y + 540), t_loc, fill='#4E7266', font=f_meta)

draw_crop_marks(front)
front_path = os.path.join(out_dir, 'MASTER-CETAK-KARTU-DEPAN-300DPI.png')
front.save(front_path, dpi=(300, 300), quality=100)
print("Front print master saved at:", front_path)

# =========================================================
# 2. GENERATE MASTER BACK (SISI BELAKANG) - SWISS EDITORIAL
# =========================================================
back = Image.new('RGB', (CANVAS_W, CANVAS_H), '#FFFFFF')
draw_b = ImageDraw.Draw(back)

# Left accent color block (Inside trim box)
draw_b.rectangle([BLEED_X, BLEED_Y, BLEED_X + 10, BLEED_Y + TRIM_H], fill=COLOR_EMERALD_DARK)

# Left Column: Executive Identity
x_text = BLEED_X + 70
draw_b.text((x_text, BLEED_Y + 75), "Yongki Kav", fill=COLOR_TEXT_DARK, font=f_person_name)
draw_b.text((x_text, BLEED_Y + 128), "Sales & Business Development Director", fill=COLOR_EMERALD_ACCENT, font=f_person_title)
draw_b.text((x_text, BLEED_Y + 155), "PT. Wirasena Maju Bersama Rayya", fill=COLOR_TEXT_MUTED, font=f_person_corp)

# Thin dividing rule
draw_b.line([(x_text, BLEED_Y + 195), (BLEED_X + 680, BLEED_Y + 195)], fill=COLOR_HAIRLINE, width=1)

# Contact rows (Clean Swiss tabular layout)
contacts = [
    ("WHATSAPP / TELP", "0852-2106-0766 (Official B2B Line)", True),
    ("EMAIL RESMI", "marketing@wirasenaraya.com", False),
    ("WEBSITE RESMI", "www.wirasenaraya.com", False),
    ("ALAMAT PABRIK", "Jl. Bah Kilong Kp. Kandang, RT.004/RW.002", False),
    ("", "Sukadami, Cikarang Selatan, Bekasi 17530", False)
]

y_row = BLEED_Y + 225
for lbl, val, is_bold in contacts:
    if lbl:
        draw_b.text((x_text, y_row), lbl, fill='#94A3B8', font=f_label)
    
    val_font = f_val if is_bold else f_val_sub
    val_col = COLOR_TEXT_DARK if is_bold else '#334155'
    draw_b.text((x_text + 175, y_row - 1), val, fill=val_col, font=val_font)
    y_row += 39

# NPWP PKP verification in footer
draw_b.text((x_text, BLEED_Y + 545), "NPWP : 96.434.539.2-447.000  (PENGUSAHA KENA PAJAK / PKP)", fill='#94A3B8', font=f_meta)

# Right Column: Smart QR Code Module
qr_box_x = BLEED_X + 760
qr_box_y = BLEED_Y + 105
qr_w = 210

qr = Image.open(qr_path).convert('RGBA')
qr.thumbnail((qr_w, qr_w), Image.Resampling.LANCZOS)

# Crisp fine outline around QR code
draw_b.rectangle([qr_box_x - 12, qr_box_y - 12, qr_box_x + qr_w + 12, qr_box_y + qr_w + 12], outline='#CBD5E1', width=1)
back.paste(qr, (qr_box_x, qr_box_y), qr)

# Text below QR
t_qr1 = "SCAN KAMERA HP"
w_qr1 = draw_b.textlength(t_qr1, font=f_qr_helper)
draw_b.text((qr_box_x + (qr_w - w_qr1) // 2, qr_box_y + qr_w + 22), t_qr1, fill=COLOR_TEXT_DARK, font=f_qr_helper)

t_qr2 = "Chat WhatsApp Om Yongki"
w_qr2 = draw_b.textlength(t_qr2, font=f_qr_sub)
draw_b.text((qr_box_x + (qr_w - w_qr2) // 2, qr_box_y + qr_w + 44), t_qr2, fill=COLOR_EMERALD_ACCENT, font=f_qr_sub)

draw_crop_marks(back)
back_path = os.path.join(out_dir, 'MASTER-CETAK-KARTU-BELAKANG-300DPI.png')
back.save(back_path, dpi=(300, 300), quality=100)
print("Back print master saved at:", back_path)

# =========================================================
# 3. GENERATE READY-TO-PRINT PDF (2 PAGES @ 300 DPI)
# =========================================================
# Convert RGB PIL images to PDF directly
pdf_path = os.path.join(out_dir, 'MASTER-CETAK-KARTU-NAMA-YONGKI-KAV-300DPI.pdf')

# Save multi-page PDF (Page 1 = Front, Page 2 = Back)
front.save(pdf_path, "PDF", resolution=300.0, save_all=True, append_images=[back])
print("Print PDF generated at:", pdf_path)

