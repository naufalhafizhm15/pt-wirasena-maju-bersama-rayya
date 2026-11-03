import os
import sys
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1080
HEIGHT = 1920
FPS = 30
TOTAL_FRAMES = 900  # Exactly 30.0 seconds

BASE_DIR = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya'
OUT_VIDEO_PATH = os.path.join(BASE_DIR, 'assets/video/wirasena-meta-tiktok-ad-30s.mp4')
os.makedirs(os.path.dirname(OUT_VIDEO_PATH), exist_ok=True)

# Smooth easing
def ease_in_out(t):
    t = max(0.0, min(1.0, t))
    return 0.5 * (1.0 - math.cos(math.pi * t))

def ease_out(t):
    t = max(0.0, min(1.0, t))
    return math.sin((t * math.pi) / 2.0)

def lerp(a, b, t):
    return a + (b - a) * t

print("1. Loading Assets for Ad...")
# Background
bg_factory_raw = Image.open(os.path.join(BASE_DIR, 'assets/images/wirasena-factory-hero-bg.jpg')).convert('RGB')
# Crop & resize to fit vertical 1080x1920
ratio = max(WIDTH / bg_factory_raw.width, HEIGHT / bg_factory_raw.height)
bg_factory = bg_factory_raw.resize((int(bg_factory_raw.width * ratio), int(bg_factory_raw.height * ratio)), Image.Resampling.LANCZOS)
bg_factory = bg_factory.crop(((bg_factory.width - WIDTH) // 2, (bg_factory.height - HEIGHT) // 2, (bg_factory.width - WIDTH) // 2 + WIDTH, (bg_factory.height - HEIGHT) // 2 + HEIGHT))

# Product transparent cutouts
gearpump = Image.open('/tmp/gearpump_crop.png').convert('RGBA')
yuema = Image.open('/tmp/yuema_crop.png').convert('RGBA')
tape = Image.open('/tmp/tape_crop.png').convert('RGBA')
trolley = Image.open('/tmp/trolley_crop.png').convert('RGBA')
carton = Image.open('/tmp/impra_crop.png').convert('RGBA')
logo_white = Image.open(os.path.join(BASE_DIR, 'assets/images/logo-footer-white.png')).convert('RGBA')
logo_white.thumbnail((260, 65), Image.Resampling.LANCZOS)

# Mobile website screenshot
mob_raw = Image.open('/tmp/mobile_site.png').convert('RGBA')

# Fonts
F_MONT_BOLD = os.path.join(BASE_DIR, 'assets/fonts/Montserrat-Bold.ttf')
F_INTER_REG = os.path.join(BASE_DIR, 'assets/fonts/Inter-Regular.ttf')
F_HELV_B = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

font_hook_super = ImageFont.truetype(F_MONT_BOLD, 52)
font_hook_accent = ImageFont.truetype(F_MONT_BOLD, 56)
font_hook_sub = ImageFont.truetype(F_INTER_REG, 23)

font_scene_title = ImageFont.truetype(F_MONT_BOLD, 44)
font_scene_sub = ImageFont.truetype(F_INTER_REG, 21)

font_badge = ImageFont.truetype(F_HELV_B, 17)
font_card_head = ImageFont.truetype(F_MONT_BOLD, 22)
font_card_desc = ImageFont.truetype(F_INTER_REG, 17)

font_cta_big = ImageFont.truetype(F_MONT_BOLD, 36)
font_cta_btn = ImageFont.truetype(F_MONT_BOLD, 26)

# Phone Mockup Renderer for Act 6
def render_phone_card(target_h=860):
    screen = mob_raw.copy()
    sw, sh = screen.size
    bezel = 12
    pw, ph = sw + bezel * 2, sh + bezel * 2
    phone = Image.new('RGBA', (pw, ph), (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(phone)
    pdraw.rounded_rectangle([0, 0, pw-1, ph-1], radius=48, fill=(35, 38, 46), outline=(90, 100, 120), width=2)
    pdraw.rounded_rectangle([2, 2, pw-3, ph-3], radius=46, fill=(12, 14, 18))
    
    smask = Image.new('L', (sw, sh), 0)
    sdraw = ImageDraw.Draw(smask)
    sdraw.rounded_rectangle([0, 0, sw, sh], radius=38, fill=255)
    phone.paste(screen, (bezel, bezel), mask=smask)
    
    # Dynamic Island
    di_w, di_h = 110, 30
    di_x, di_y = (pw - di_w) // 2, bezel + 10
    pdraw.rounded_rectangle([di_x, di_y, di_x + di_w, di_y + di_h], radius=15, fill=(0, 0, 0))
    
    # Scale
    scale = target_h / ph
    nw, nh = int(pw * scale), target_h
    phone_resized = phone.resize((nw, nh), Image.Resampling.LANCZOS)
    
    pad = 40
    res = Image.new('RGBA', (nw + pad*2, nh + pad*2), (0, 0, 0, 0))
    sh_box = Image.new('RGBA', (nw, nh), (0, 0, 0, 0))
    s_dr = ImageDraw.Draw(sh_box)
    s_dr.rounded_rectangle([0, 0, nw, nh], radius=int(48*scale), fill=(0, 0, 0, 160))
    sh_blur = sh_box.filter(ImageFilter.GaussianBlur(24))
    res.paste(sh_blur, (pad, pad + 16), mask=sh_blur)
    res.paste(phone_resized, (pad, pad), mask=phone_resized)
    return res

phone_ad = render_phone_card(target_h=880)

# Product shadow helper
def paste_product_with_shadow(canvas, img, x, y, max_w=400, max_h=340):
    im = img.copy()
    im.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    
    # Shadow
    sw, sh = int(im.width * 0.75), 24
    shadow = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.ellipse([0, 0, sw, sh], fill=(0, 0, 0, 70))
    sh_blur = shadow.filter(ImageFilter.GaussianBlur(8))
    
    canvas.paste(sh_blur, (x + (im.width - sw) // 2, y + im.height - 14), mask=sh_blur)
    canvas.paste(im, (x, y), mask=im)

print("2. Spawning FFmpeg encoder for 30s Ad...")
proc = subprocess.Popen([
    'ffmpeg', '-y',
    '-f', 'rawvideo',
    '-vcodec', 'rawvideo',
    '-s', f'{WIDTH}x{HEIGHT}',
    '-pix_fmt', 'rgb24',
    '-r', str(FPS),
    '-i', '-',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '18',
    '-pix_fmt', 'yuv420p',
    OUT_VIDEO_PATH
], stdin=subprocess.PIPE)

print(f"3. Rendering 900 Ad frames (30.0s @ 30 FPS)...")

for f in range(TOTAL_FRAMES):
    # ----------------------------------------------------
    # ACT 1: THE HIGH-STAKES HOOK (0.0s - 3.5s, Frames 0 - 105)
    # Relatable pain point that stops the scroll
    # ----------------------------------------------------
    if f < 105:
        p_zoom = f / 105.0
        # Slow cinematic push-in on factory bg
        scale_bg = 1.0 + p_zoom * 0.08
        bg_w, bg_h = int(WIDTH * scale_bg), int(HEIGHT * scale_bg)
        bg_frame = bg_factory.resize((bg_w, bg_h), Image.Resampling.BILINEAR)
        crop_x = (bg_w - WIDTH) // 2
        crop_y = (bg_h - HEIGHT) // 2
        frame = bg_frame.crop((crop_x, crop_y, crop_x + WIDTH, crop_y + HEIGHT))
        
        # Heavy dark tint with red alert vignette
        tint = Image.new('RGBA', (WIDTH, HEIGHT), (10, 12, 18, 225))
        frame.paste(tint, (0, 0), tint)
        draw = ImageDraw.Draw(frame)
        
        # Alert badge in first 3s
        draw.rounded_rectangle([(WIDTH - 420) // 2, 380, (WIDTH + 420) // 2, 435], radius=16, fill=(185, 28, 28, 220), outline=(239, 68, 68))
        draw.text(((WIDTH - 380) // 2, 394), "⚠️ MASALAH KRUSIAL OPERASIONAL PABRIK", font=font_badge, fill=(255, 255, 255))
        
        # Big Kinetic Typography Hook
        draw.text(((WIDTH - draw.textlength("DOWNTIME MESIN 1 JAM...", font=font_hook_super)) // 2, 480), "DOWNTIME MESIN 1 JAM...", font=font_hook_super, fill=(255, 255, 255))
        
        # Flashing highlight on second line
        pulse_color = (239, 68, 68) if (f // 8) % 2 == 0 else (245, 158, 11)
        draw.text(((WIDTH - draw.textlength("BISA BIKIN SATU SHIFT GAGAL.", font=font_hook_accent)) // 2, 550), "BISA BIKIN SATU SHIFT GAGAL.", font=font_hook_accent, fill=pulse_color)
        
        # Divider line
        draw.line([(WIDTH - 300) // 2, 650, (WIDTH + 300) // 2, 650], fill=(75, 85, 99), width=2)
        
        sub_lines = [
            "Lini produksi butuh kepastian vendor suku cadang,",
            "perlengkapan packaging, dan safety yang sat-set",
            "langsung di kawasan industri Cikarang & Karawang."
        ]
        sy = 680
        for sl in sub_lines:
            draw.text(((WIDTH - draw.textlength(sl, font=font_hook_sub)) // 2, sy), sl, font=font_hook_sub, fill=(209, 213, 219))
            sy += 36
            
        # Warning countdown pill at bottom
        draw.rounded_rectangle([(WIDTH - 440) // 2, 920, (WIDTH + 440) // 2, 980], radius=14, fill=(20, 24, 34), outline=(55, 65, 81))
        draw.text(((WIDTH - 400) // 2, 938), "STOP TUNGGU LAMA. INI SOLUSINYA ↓", font=font_badge, fill=(147, 197, 253))

    # ----------------------------------------------------
    # ACT 2: THE INTRODUCTION & CREDIBILITY (3.5s - 8.0s, Frames 105 - 240)
    # Present PT. Wirasena Maju Bersama Rayya
    # ----------------------------------------------------
    elif 105 <= f < 240:
        p_act2 = (f - 105) / 135.0
        frame = Image.new('RGB', (WIDTH, HEIGHT), (10, 13, 20))
        glow = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.ellipse([200, 300, 880, 1200], fill=(24, 45, 85, 130))
        glow_blur = glow.filter(ImageFilter.GaussianBlur(120))
        frame.paste(glow_blur, (0, 0), mask=glow_blur)
        draw = ImageDraw.Draw(frame)
        
        # Logo Entry
        frame.paste(logo_white, ((WIDTH - logo_white.width) // 2, 280), logo_white)
        
        # Official Badge
        draw.rounded_rectangle([(WIDTH - 360) // 2, 380, (WIDTH + 360) // 2, 425], radius=14, fill=(16, 40, 32), outline=(52, 211, 153))
        draw.text(((WIDTH - 320) // 2, 392), "⭐ MITRA GENERAL SUPPLIER RESMI", font=font_badge, fill=(167, 243, 208))
        
        # Headlines
        draw.text(((WIDTH - draw.textlength("PT. WIRASENA MAJU", font=font_scene_title)) // 2, 460), "PT. WIRASENA MAJU", font=font_scene_title, fill=(255, 255, 255))
        draw.text(((WIDTH - draw.textlength("BERSAMA RAYYA", font=font_scene_title)) // 2, 515), "BERSAMA RAYYA", font=font_scene_title, fill=(59, 130, 246))
        
        draw.text(((WIDTH - draw.textlength("Solusi Pengadaan Pabrik & Manufaktur Kemasan", font=font_scene_sub)) // 2, 585), "Solusi Pengadaan Pabrik & Manufaktur Kemasan", font=font_scene_sub, fill=(156, 163, 175))
        
        # 3 Pillar Pillars
        pillars = [
            ("⚡ LEGALITAS RESMI & FAKTUR PAJAK (PKP)", "Badan hukum PT resmi, transparansi audit vendor"),
            ("📍 GUDANG & WORKSHOP LOKAL CIKARANG", "Sukadami, Cikarang Selatan • Armada distribusi sendiri"),
            ("🚀 RESPON CEPAT PENAWARAN HARGA (RFQ)", "Dokumen penawaran harga & BOM diproses cepat")
        ]
        
        py = 660
        for title, desc in pillars:
            draw.rounded_rectangle([100, py, WIDTH - 100, py + 105], radius=16, fill=(18, 24, 38), outline=(40, 50, 75))
            draw.text((130, py + 22), title, font=font_card_head, fill=(219, 234, 254))
            draw.text((130, py + 56), desc, font=font_card_desc, fill=(148, 163, 184))
            py += 125

    # ----------------------------------------------------
    # ACT 3: PILAR 1 — SUKU CADANG MESIN & MRO (8.0s - 14.0s, Frames 240 - 420)
    # Real Gear Pump & Yuema Motor hardware focus
    # ----------------------------------------------------
    elif 240 <= f < 420:
        p_act3 = (f - 240) / 180.0
        frame = Image.new('RGB', (WIDTH, HEIGHT), (10, 13, 20))
        glow = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.ellipse([180, 500, 900, 1300], fill=(22, 50, 90, 130))
        glow_blur = glow.filter(ImageFilter.GaussianBlur(110))
        frame.paste(glow_blur, (0, 0), mask=glow_blur)
        draw = ImageDraw.Draw(frame)
        
        # Tag
        draw.rounded_rectangle([(WIDTH - 380) // 2, 180, (WIDTH + 380) // 2, 225], radius=14, fill=(20, 32, 50), outline=(59, 130, 246))
        draw.text(((WIDTH - 340) // 2, 192), "PILAR 01: ELECTRICAL & MECHANICAL", font=font_badge, fill=(147, 197, 253))
        
        # Title
        draw.text(((WIDTH - draw.textlength("SUKU CADANG MESIN & MRO", font=font_scene_title)) // 2, 250), "SUKU CADANG MESIN & MRO", font=font_scene_title, fill=(255, 255, 255))
        draw.text(((WIDTH - draw.textlength("Siap suplai untuk preventive & emergency breakdown", font=font_scene_sub)) // 2, 310), "Siap suplai untuk preventive & emergency breakdown", font=font_scene_sub, fill=(156, 163, 175))
        
        # 2 Product Cards
        # Float effect
        float_y = int(math.sin(f * 0.1) * 8)
        
        # Card 1: Gear Pump
        c1_x, c1_y = 100, 390 + float_y
        draw.rounded_rectangle([c1_x, c1_y, WIDTH - 100, c1_y + 360], radius=20, fill=(18, 24, 38), outline=(40, 50, 75))
        paste_product_with_shadow(frame, gearpump, c1_x + 30, c1_y + 25, max_w=380, max_h=240)
        draw.text((c1_x + 440, c1_y + 70), "GEAR PUMP GC-20 / GC-25", font=font_card_head, fill=(255, 255, 255))
        draw.text((c1_x + 440, c1_y + 110), "• Material Cast Iron Heavy Duty", font=font_card_desc, fill=(148, 163, 184))
        draw.text((c1_x + 440, c1_y + 145), "• Suplai Oli & Cairan Kental Mesin", font=font_card_desc, fill=(148, 163, 184))
        draw.text((c1_x + 440, c1_y + 180), "• Presisi Tinggi Tanpa Kebocoran", font=font_card_desc, fill=(52, 211, 153))
        
        # Card 2: Yuema Motor
        c2_x, c2_y = 100, 780 - float_y
        draw.rounded_rectangle([c2_x, c2_y, WIDTH - 100, c2_y + 360], radius=20, fill=(18, 24, 38), outline=(40, 50, 75))
        paste_product_with_shadow(frame, yuema, c2_x + 30, c2_y + 25, max_w=380, max_h=240)
        draw.text((c2_x + 440, c2_y + 70), "ELEKTRO MOTOR YUEMA SA", font=font_card_head, fill=(255, 255, 255))
        draw.text((c2_x + 440, c2_y + 110), "• 3-Phase Induction Motor", font=font_card_desc, fill=(148, 163, 184))
        draw.text((c2_x + 440, c2_y + 145), "• Standar Flange B3 / B5 Pabrik", font=font_card_desc, fill=(148, 163, 184))
        draw.text((c2_x + 440, c2_y + 180), "• Daya Tahan Beban Kontinu 24 Jam", font=font_card_desc, fill=(52, 211, 153))
        
        # Tagline bottom
        draw.text(((WIDTH - draw.textlength("Pengiriman Cepat: MM2100 • Jababeka • EJIP • GIIC • KIIC", font=font_badge)) // 2, 1180), "Pengiriman Cepat: MM2100 • Jababeka • EJIP • GIIC • KIIC", font=font_badge, fill=(147, 197, 253))

    # ----------------------------------------------------
    # ACT 4: PILAR 2 & 3 — LAKBAN, APD K3 & TROLLEY (14.0s - 20.0s, Frames 420 - 600)
    # ----------------------------------------------------
    elif 420 <= f < 600:
        p_act4 = (f - 420) / 180.0
        frame = Image.new('RGB', (WIDTH, HEIGHT), (10, 13, 20))
        glow = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.ellipse([180, 500, 900, 1300], fill=(20, 45, 75, 130))
        glow_blur = glow.filter(ImageFilter.GaussianBlur(110))
        frame.paste(glow_blur, (0, 0), mask=glow_blur)
        draw = ImageDraw.Draw(frame)
        
        # Tag
        draw.rounded_rectangle([(WIDTH - 420) // 2, 180, (WIDTH + 420) // 2, 225], radius=14, fill=(18, 38, 30), outline=(52, 211, 153))
        draw.text(((WIDTH - 380) // 2, 192), "PILAR 02 & 03: CONSUMABLES & FABRIKASI", font=font_badge, fill=(167, 243, 208))
        
        draw.text(((WIDTH - draw.textlength("LAKBAN, APD K3 & PARTS TROLLEY", font=font_scene_title)) // 2, 250), "LAKBAN, APD K3 & PARTS TROLLEY", font=font_scene_title, fill=(255, 255, 255))
        draw.text(((WIDTH - draw.textlength("Suplai rutin berkala dan fabrikasi kustom presisi", font=font_scene_sub)) // 2, 310), "Suplai rutin berkala dan fabrikasi kustom presisi", font=font_scene_sub, fill=(156, 163, 175))
        
        float_y = int(math.sin(f * 0.1) * 8)
        
        # Card 1: Lakban & K3
        c1_x, c1_y = 100, 390 + float_y
        draw.rounded_rectangle([c1_x, c1_y, WIDTH - 100, c1_y + 360], radius=20, fill=(18, 24, 38), outline=(40, 50, 75))
        paste_product_with_shadow(frame, tape, c1_x + 30, c1_y + 35, max_w=380, max_h=230)
        draw.text((c1_x + 440, c1_y + 70), "LAKBAN INDUSTRI & APD K3", font=font_card_head, fill=(255, 255, 255))
        draw.text((c1_x + 440, c1_y + 110), "• OPP Tape Bening & Masking Tape", font=font_card_desc, fill=(148, 163, 184))
        draw.text((c1_x + 440, c1_y + 145), "• Helm Proyek SNI, Sarung Tangan, Sepatu", font=font_card_desc, fill=(148, 163, 184))
        draw.text((c1_x + 440, c1_y + 180), "• Kontrak Suplai Mingguan / Bulanan", font=font_card_desc, fill=(52, 211, 153))
        
        # Card 2: Parts Trolley
        c2_x, c2_y = 100, 780 - float_y
        draw.rounded_rectangle([c2_x, c2_y, WIDTH - 100, c2_y + 360], radius=20, fill=(18, 24, 38), outline=(40, 50, 75))
        paste_product_with_shadow(frame, trolley, c2_x + 40, c2_y + 20, max_w=360, max_h=260)
        draw.text((c2_x + 440, c2_y + 70), "STORAGE PARTS TROLLEY", font=font_card_head, fill=(255, 255, 255))
        draw.text((c2_x + 440, c2_y + 110), "• Rangka SUS 304 / Mild Steel Coating", font=font_card_desc, fill=(148, 163, 184))
        draw.text((c2_x + 440, c2_y + 145), "• 4 Susun Ergonomis dengan Roda PU Kunci", font=font_card_desc, fill=(148, 163, 184))
        draw.text((c2_x + 440, c2_y + 180), "• Custom Ukuran Sesuai Jalur Produksi", font=font_card_desc, fill=(52, 211, 153))
        
        draw.text(((WIDTH - draw.textlength("Terima Pesanan Kustom & Sampling Langsung!", font=font_badge)) // 2, 1180), "Terima Pesanan Kustom & Sampling Langsung!", font=font_badge, fill=(167, 243, 208))

    # ----------------------------------------------------
    # ACT 5: PABRIK KARTON SENDIRI — 5 MESIN IN-HOUSE (20.0s - 25.0s, Frames 600 - 750)
    # The ultimate proof of manufacturing power
    # ----------------------------------------------------
    elif 600 <= f < 750:
        p_act5 = (f - 600) / 150.0
        frame = Image.new('RGB', (WIDTH, HEIGHT), (10, 13, 20))
        glow = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.ellipse([180, 480, 900, 1300], fill=(22, 50, 85, 140))
        glow_blur = glow.filter(ImageFilter.GaussianBlur(120))
        frame.paste(glow_blur, (0, 0), mask=glow_blur)
        draw = ImageDraw.Draw(frame)
        
        # Tag
        draw.rounded_rectangle([(WIDTH - 380) // 2, 180, (WIDTH + 380) // 2, 225], radius=14, fill=(20, 32, 50), outline=(59, 130, 246))
        draw.text(((WIDTH - 340) // 2, 192), "PABRIK SENDIRI DI CIKARANG SELATAN", font=font_badge, fill=(147, 197, 253))
        
        draw.text(((WIDTH - draw.textlength("MANUFAKTUR KEMASAN KARTON", font=font_scene_title)) // 2, 250), "MANUFAKTUR KEMASAN KARTON", font=font_scene_title, fill=(255, 255, 255))
        draw.text(((WIDTH - draw.textlength("Bukan perantara — Diproduksi langsung dengan 5 lini mesin!", font=font_scene_sub)) // 2, 310), "Bukan perantara — Diproduksi langsung dengan 5 lini mesin!", font=font_scene_sub, fill=(52, 211, 153))
        
        # Visual carton / impraboard
        float_y = int(math.sin(f * 0.1) * 8)
        paste_product_with_shadow(frame, carton, (WIDTH - 500) // 2, 360 + float_y, max_w=500, max_h=300)
        
        # 5 Mesin Grid Box
        draw.rounded_rectangle([100, 680, WIDTH - 100, 1140], radius=20, fill=(18, 24, 38), outline=(40, 50, 75))
        draw.text((140, 715), "5 UNIT MESIN MANUFAKTUR IN-HOUSE:", font=font_card_head, fill=(219, 234, 254))
        
        machines = [
            "1. Mesin Cutting & Creasing (Potong Presisi)",
            "2. Mesin Auto Folder Glue (Lem Lipat Otomatis)",
            "3. Mesin Semi Folder Glue (Karton Ukuran Jumbo)",
            "4. Mesin Rotary Slotter (Pembentukan Celah Box)",
            "5. Mesin Rotary Die-Cut (Box Partisi Kustom)"
        ]
        my = 770
        for m in machines:
            draw.text((140, my), f"✓ {m}", font=font_card_desc, fill=(241, 245, 249))
            my += 45
            
        draw.text((140, 1030), "• Kapasitas Puluhan Ribu Pcs / Bulan", font=font_badge, fill=(52, 211, 153))
        draw.text((140, 1070), "• Bebas Custom Ukuran & Desain Sesuai Komponen Anda", font=font_badge, fill=(147, 197, 253))

    # ----------------------------------------------------
    # ACT 6: HIGH-CONVERTING CALL TO ACTION (25.0s - 30.0s, Frames 750 - 900)
    # The clear next step for TikTok & Meta ads
    # ----------------------------------------------------
    else:
        p_cta = (f - 750) / 150.0
        frame = Image.new('RGB', (WIDTH, HEIGHT), (10, 13, 20))
        glow = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.ellipse([140, 300, 940, 1400], fill=(22, 60, 45, 140))
        glow_blur = glow.filter(ImageFilter.GaussianBlur(130))
        frame.paste(glow_blur, (0, 0), mask=glow_blur)
        draw = ImageDraw.Draw(frame)
        
        # Phone Mockup displaying live website
        frame.paste(phone_ad, (60, 260), phone_ad)
        
        # Right Side CTA Action Card
        rx = 540
        draw.text((rx, 340), "BUTUH PENAWARAN", font=font_cta_big, fill=(255, 255, 255))
        draw.text((rx, 390), "HARGA CEPAT (RFQ)?", font=font_cta_big, fill=(52, 211, 153))
        
        draw.text((rx, 465), "Konsultasikan kebutuhan pabrik Anda", font=font_card_desc, fill=(156, 163, 175))
        draw.text((rx, 495), "bersama tim sales B2B kami sekarang.", font=font_card_desc, fill=(156, 163, 175))
        
        # Pulsating Green CTA Button
        pulse = math.sin((f - 750) * 0.15) * 4
        btn_y = int(570 + pulse)
        draw.rounded_rectangle([rx, btn_y, WIDTH - 60, btn_y + 80], radius=16, fill=(22, 101, 52), outline=(52, 211, 153), width=2)
        draw.text((rx + 35, btn_y + 24), "💬 CHAT WHATSAPP SEKARANG", font=font_cta_btn, fill=(255, 255, 255))
        
        # Direct Contacts & URL
        draw.text((rx, 690), "DIRECT WHATSAPP SALES:", font=font_badge, fill=(148, 163, 184))
        draw.text((rx, 725), "0852-2106-0766", font=font_cta_big, fill=(255, 255, 255))
        
        draw.text((rx, 800), "PORTAL RESMI & KATALOG:", font=font_badge, fill=(148, 163, 184))
        draw.text((rx, 835), "wirasenaraya.com", font=font_cta_big, fill=(96, 165, 250))
        
        # Regional Coverage
        draw.line([(rx, 910), (WIDTH - 60, 910)], fill=(40, 50, 70), width=1)
        draw.text((rx, 935), "JANGKAUAN PENGIRIMAN CEPAT:", font=font_badge, fill=(148, 163, 184))
        draw.text((rx, 968), "MM2100 • Jababeka • EJIP", font=font_card_desc, fill=(219, 234, 254))
        draw.text((rx, 998), "Delta Silicon • GIIC • KIIC", font=font_card_desc, fill=(219, 234, 254))
        
        # Bottom legal note
        draw.text(((WIDTH - draw.textlength("PT. WIRASENA MAJU BERSAMA RAYYA • CIKARANG SELATAN, BEKASI", font=font_badge)) // 2, 1220), "PT. WIRASENA MAJU BERSAMA RAYYA • CIKARANG SELATAN, BEKASI", font=font_badge, fill=(100, 116, 139))

    # Pipe frame
    proc.stdin.write(frame.tobytes())
    
    if (f + 1) % 90 == 0 or f == TOTAL_FRAMES - 1:
        elapsed = (f + 1) / FPS
        print(f"Rendered ad frame {f + 1}/{TOTAL_FRAMES} ({elapsed:.1f}s / 30.0s)...")

proc.stdin.close()
proc.wait()

print("\n==========================================")
print(f"🚀 VIDEO IKLAN META & TIKTOK SUKSES 100%!")
print(f"Output: {OUT_VIDEO_PATH}")
print(f"Size: {os.path.getsize(OUT_VIDEO_PATH) / (1024*1024):.2f} MB")
print("==========================================")
