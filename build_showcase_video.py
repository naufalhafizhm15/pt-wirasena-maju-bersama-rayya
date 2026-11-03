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
OUT_VIDEO_PATH = os.path.join(BASE_DIR, 'assets/video/wirasena-responsive-showcase.mp4')
os.makedirs(os.path.dirname(OUT_VIDEO_PATH), exist_ok=True)

# Smooth easing helpers
def ease_in_out(t):
    t = max(0.0, min(1.0, t))
    return 0.5 * (1.0 - math.cos(math.pi * t))

def ease_out(t):
    t = max(0.0, min(1.0, t))
    return math.sin((t * math.pi) / 2.0)

def lerp(a, b, t):
    return a + (b - a) * t

print("1. Loading Real High-Resolution Website Captures...")
desk_raw = Image.open('/tmp/full_desktop_web.png').convert('RGB')
mob_raw = Image.open('/tmp/full_mobile_web.png').convert('RGB')

# Mobile Screen Setup (Inside iPhone 15 Pro: 560 x 1180)
SCREEN_W = 560
SCREEN_H = 1180
mob_scale = SCREEN_W / mob_raw.width
mob_strip = mob_raw.resize((SCREEN_W, int(mob_raw.height * mob_scale)), Image.Resampling.LANCZOS)

# Desktop Window Setup (960 x 620)
DESK_W = 960
DESK_H = 620
TITLE_H = 46
VIEW_DESK_H = DESK_H - TITLE_H
desk_scale = DESK_W / desk_raw.width
desk_strip = desk_raw.resize((DESK_W, int(desk_raw.height * desk_scale)), Image.Resampling.LANCZOS)

# Vector macOS Cursor Generator
def make_cursor(size=44):
    cursor = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    pts = [
        (0, 0),
        (0, int(size * 0.8)),
        (int(size * 0.22), int(size * 0.62)),
        (int(size * 0.44), int(size * 0.95)),
        (int(size * 0.58), int(size * 0.88)),
        (int(size * 0.36), int(size * 0.55)),
        (int(size * 0.65), int(size * 0.55))
    ]
    pad = 12
    final = Image.new('RGBA', (size + pad*2, size + pad*2), (0, 0, 0, 0))
    sh = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sh)
    sdraw.polygon(pts, fill=(0, 0, 0, 150))
    sh_blur = sh.filter(ImageFilter.GaussianBlur(4))
    final.paste(sh_blur, (pad + 2, pad + 4), mask=sh_blur)
    
    cdraw = ImageDraw.Draw(final)
    pts_offset = [(x + pad, y + pad) for (x, y) in pts]
    cdraw.polygon(pts_offset, fill=(255, 255, 255), outline=(24, 24, 27), width=2)
    return final

cursor_img = make_cursor(44)

# Touch Pointer Generator
def make_touch_pointer(size=52, pulse=0.0):
    im = Image.new('RGBA', (size + 30, size + 30), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = (size + 30) // 2, (size + 30) // 2
    r_outer = (size // 2) + int(pulse * 12)
    alpha_outer = max(0, int((1.0 - pulse) * 110))
    if pulse > 0.05:
        draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], fill=(52, 211, 153, alpha_outer))
    
    r_ring = size // 2
    draw.ellipse([cx - r_ring, cy - r_ring, cx + r_ring, cy + r_ring], fill=(255, 255, 255, 90), outline=(255, 255, 255, 220), width=2)
    draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(255, 255, 255, 240))
    return im

# Desktop Window Renderer
def render_desktop_window(scroll_y=0):
    win = Image.new('RGBA', (DESK_W, DESK_H), (0, 0, 0, 0))
    
    # Titlebar
    titlebar = Image.new('RGBA', (DESK_W, TITLE_H), (20, 24, 32, 255))
    tdraw = ImageDraw.Draw(titlebar)
    tdraw.ellipse([18, 17, 30, 29], fill='#FF5F56')
    tdraw.ellipse([38, 17, 50, 29], fill='#FFBD2E')
    tdraw.ellipse([58, 17, 70, 29], fill='#27C93F')
    
    ub_w = 420
    ub_x = (DESK_W - ub_w) // 2
    tdraw.rounded_rectangle([ub_x, 10, ub_x + ub_w, 36], radius=13, fill=(12, 15, 22), outline=(45, 55, 75), width=1)
    
    font_addr = ImageFont.truetype('/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/fonts/Inter-Regular.ttf', 13)
    tdraw.text((ub_x + 18, 14), "🔒 https://wirasenaraya.com", fill='#94A3B8', font=font_addr)
    
    # Viewport crop
    max_scroll = desk_strip.height - VIEW_DESK_H
    sy = max(0, min(int(scroll_y), max_scroll))
    viewport = desk_strip.crop((0, sy, DESK_W, sy + VIEW_DESK_H))
    
    win.paste(titlebar, (0, 0))
    win.paste(viewport, (0, TITLE_H))
    
    # Rounded corners mask
    mask = Image.new('L', (DESK_W, DESK_H), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle([0, 0, DESK_W, DESK_H], radius=16, fill=255)
    
    rounded_win = Image.new('RGBA', (DESK_W, DESK_H), (0, 0, 0, 0))
    rounded_win.paste(win, (0, 0), mask=mask)
    rdraw = ImageDraw.Draw(rounded_win)
    rdraw.rounded_rectangle([0, 0, DESK_W-1, DESK_H-1], radius=16, outline=(60, 75, 100), width=1)
    
    pad = 40
    res = Image.new('RGBA', (DESK_W + pad*2, DESK_H + pad*2), (0, 0, 0, 0))
    sh = Image.new('RGBA', (DESK_W, DESK_H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sh)
    sdraw.rounded_rectangle([0, 0, DESK_W, DESK_H], radius=16, fill=(0, 0, 0, 150))
    sh_blur = sh.filter(ImageFilter.GaussianBlur(25))
    res.paste(sh_blur, (pad, pad + 16), mask=sh_blur)
    res.paste(rounded_win, (pad, pad), mask=rounded_win)
    return res

# Phone Chassis Renderer
PHONE_W = 600
PHONE_H = 1240
BEZEL = 20
def render_phone_mockup(scroll_y=0):
    phone = Image.new('RGBA', (PHONE_W, PHONE_H), (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(phone)
    radius = 54
    
    pdraw.rounded_rectangle([0, 0, PHONE_W-1, PHONE_H-1], radius=radius, fill=(35, 38, 46), outline=(90, 100, 120), width=2)
    pdraw.rounded_rectangle([2, 2, PHONE_W-3, PHONE_H-3], radius=radius-2, fill=(12, 14, 18))
    
    max_scroll = mob_strip.height - SCREEN_H
    sy = max(0, min(int(scroll_y), max_scroll))
    viewport = mob_strip.crop((0, sy, SCREEN_W, sy + SCREEN_H))
    
    smask = Image.new('L', (SCREEN_W, SCREEN_H), 0)
    smdraw = ImageDraw.Draw(smask)
    smdraw.rounded_rectangle([0, 0, SCREEN_W, SCREEN_H], radius=42, fill=255)
    phone.paste(viewport, (BEZEL, BEZEL), mask=smask)
    
    # Dynamic Island
    di_w, di_h = 130, 34
    di_x = (PHONE_W - di_w) // 2
    di_y = BEZEL + 11
    pdraw.rounded_rectangle([di_x, di_y, di_x + di_w, di_y + di_h], radius=17, fill=(0, 0, 0))
    pdraw.ellipse([di_x + 100, di_y + 10, di_x + 114, di_y + 24], fill=(15, 23, 42))
    
    # Home bar
    bar_w, bar_h = 160, 5
    bar_x = (PHONE_W - bar_w) // 2
    bar_y = PHONE_H - BEZEL - 14
    pdraw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=3, fill=(220, 220, 220, 160))
    
    pad = 50
    res = Image.new('RGBA', (PHONE_W + pad*2, PHONE_H + pad*2), (0, 0, 0, 0))
    sh = Image.new('RGBA', (PHONE_W, PHONE_H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sh)
    sdraw.rounded_rectangle([0, 0, PHONE_W, PHONE_H], radius=radius, fill=(0, 0, 0, 160))
    sh_blur = sh.filter(ImageFilter.GaussianBlur(30))
    res.paste(sh_blur, (pad, pad + 20), mask=sh_blur)
    res.paste(phone, (pad, pad), mask=phone)
    return res

# Base Canvas (Luxury Dark Studio)
canvas_base = Image.new('RGB', (WIDTH, HEIGHT), (10, 13, 20))
glow = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
gdraw = ImageDraw.Draw(glow)
gdraw.ellipse([160, 420, 920, 1380], fill=(22, 42, 80, 140))
glow_blur = glow.filter(ImageFilter.GaussianBlur(130))
canvas_base.paste(glow_blur, (0, 0), mask=glow_blur)

print("2. Spawning FFmpeg encoder...")
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

# Mobile scroll timeline keyframes: (frame, scroll_y)
# Max scroll_y ~ 8550
mob_keyframes = [
    (240, 0),     # Arrive at Hero
    (310, 0),     # Calm hold at Hero
    (390, 1550),  # Scroll to Solusi 01: Sparepart & MRO
    (460, 1550),  # Calm hold
    (530, 3100),  # Scroll to Solusi 02: Lakban & K3
    (590, 3100),  # Calm hold
    (660, 4900),  # Scroll to Solusi 03 & 04: Fabrikasi & Karton
    (720, 4900),  # Calm hold
    (780, 7100),  # Scroll to Fasilitas 5 Mesin Pabrik
    (820, 7100),  # Calm hold
    (860, 8550),  # Scroll to Footer & Direct Contact
    (900, 8550)   # Final hold
]

def get_mob_scroll(f):
    if f <= mob_keyframes[0][0]:
        return mob_keyframes[0][1]
    for i in range(len(mob_keyframes) - 1):
        f1, s1 = mob_keyframes[i]
        f2, s2 = mob_keyframes[i+1]
        if f1 <= f <= f2:
            prog = (f - f1) / (f2 - f1)
            eased = ease_in_out(prog)
            return lerp(s1, s2, eased)
    return mob_keyframes[-1][1]

print(f"3. Rendering {TOTAL_FRAMES} frames (30.0s @ 30 FPS)...")

# Main Render Loop
for f in range(TOTAL_FRAMES):
    frame = canvas_base.copy()
    
    # ----------------------------------------------------
    # PHASE 1: Desktop Experience (Frames 0 - 180, 0.0s - 6.0s)
    # ----------------------------------------------------
    if f < 180:
        # Smooth window entry
        t_enter = min(1.0, f / 35.0)
        e_enter = ease_out(t_enter)
        desk_y = int(lerp(650, 610, e_enter))
        
        # Scroll in desktop
        if f < 80:
            desk_scroll = 0
        else:
            p_scroll = min(1.0, (f - 80) / 70.0)
            desk_scroll = lerp(0, 450, ease_in_out(p_scroll))
            
        desk_win = render_desktop_window(desk_scroll)
        desk_x = (WIDTH - desk_win.width) // 2
        frame.paste(desk_win, (desk_x, desk_y), desk_win)
        
        # Cursor Motion
        if f < 20:
            cx, cy = 920, 1200
        elif f < 80:
            p = (f - 20) / 60.0
            cx = lerp(920, 560, ease_out(p))
            cy = lerp(1200, 690, ease_out(p))
        elif f < 140:
            p = (f - 80) / 60.0
            cx = lerp(560, 360, ease_in_out(p))
            cy = lerp(690, 890, ease_in_out(p))
        else:
            # gentle subtle hover float
            cx = 360 + int(math.sin(f * 0.1) * 3)
            cy = 890 + int(math.cos(f * 0.1) * 2)
            
        frame.paste(cursor_img, (int(cx), int(cy)), cursor_img)
        
    # ----------------------------------------------------
    # PHASE 2: Seamless Device Morph (Frames 180 - 240, 6.0s - 8.0s)
    # ----------------------------------------------------
    elif 180 <= f < 240:
        p_morph = (f - 180) / 60.0
        e_morph = ease_in_out(p_morph)
        
        # Desktop scales down and fades
        desk_scale_val = lerp(1.0, 0.45, e_morph)
        desk_win = render_desktop_window(450)
        dw = int(desk_win.width * desk_scale_val)
        dh = int(desk_win.height * desk_scale_val)
        desk_scaled = desk_win.resize((dw, dh), Image.Resampling.BILINEAR)
        
        # Apply alpha fade
        alpha_desk = int((1.0 - e_morph) * 255)
        d_mask = Image.new('L', (dw, dh), alpha_desk)
        dx = (WIDTH - dw) // 2
        dy = int(lerp(610, 520, e_morph))
        frame.paste(desk_scaled, (dx, dy), d_mask)
        
        # Phone scales in from center
        phone_scale_val = lerp(0.55, 1.0, e_morph)
        phone = render_phone_mockup(0)
        pw = int(phone.width * phone_scale_val)
        ph = int(phone.height * phone_scale_val)
        phone_scaled = phone.resize((pw, ph), Image.Resampling.BILINEAR)
        
        alpha_phone = int(e_morph * 255)
        p_mask = Image.new('L', (pw, ph), alpha_phone)
        px = (WIDTH - pw) // 2
        py = int(lerp(420, 290, e_morph))
        frame.paste(phone_scaled, (px, py), p_mask)
        
        # Cursor transitions to touch pointer
        cx = lerp(360, 540, e_morph)
        cy = lerp(890, 850, e_morph)
        tp = make_touch_pointer(52, pulse=0.0)
        frame.paste(tp, (int(cx - 26), int(cy - 26)), tp)

    # ----------------------------------------------------
    # PHASE 3 & 4: Mobile Kinetic Tour & Outro (Frames 240 - 900, 8.0s - 30.0s)
    # ----------------------------------------------------
    else:
        mob_scroll_y = get_mob_scroll(f)
        phone = render_phone_mockup(mob_scroll_y)
        px = (WIDTH - phone.width) // 2
        py = (HEIGHT - phone.height) // 2 # 290
        
        # Final subtle camera settle in the last 2 seconds
        if f > 820:
            settle_p = min(1.0, (f - 820) / 40.0)
            settle_scale = lerp(1.0, 0.98, ease_out(settle_p))
            pw = int(phone.width * settle_scale)
            ph = int(phone.height * settle_scale)
            phone = phone.resize((pw, ph), Image.Resampling.LANCZOS)
            px = (WIDTH - pw) // 2
            py = (HEIGHT - ph) // 2
            
        frame.paste(phone, (px, py), phone)
        
        # Touch pointer animation
        pulse = 0.0
        # Check if clicking at the end
        if 840 <= f <= 870:
            click_p = (f - 840) / 30.0
            pulse = math.sin(click_p * math.pi)
            pointer_x = 540
            pointer_y = 1120
        elif f < 310:
            pointer_x = 540 + math.sin(f * 0.08) * 8
            pointer_y = 850 + math.cos(f * 0.08) * 5
        elif 310 <= f < 840:
            # Subtle natural sway during scrolls
            pointer_x = 540 + math.sin(f * 0.12) * 12
            pointer_y = 860 + math.cos(f * 0.12) * 8
        else:
            pointer_x = 540
            pointer_y = 1120
            
        tp = make_touch_pointer(52, pulse=pulse)
        frame.paste(tp, (int(pointer_x - 26), int(pointer_y - 26)), tp)

    # Pipe raw frame to ffmpeg
    proc.stdin.write(frame.tobytes())
    
    if (f + 1) % 90 == 0 or f == TOTAL_FRAMES - 1:
        elapsed_s = (f + 1) / FPS
        print(f"Rendered frame {f + 1}/{TOTAL_FRAMES} ({elapsed_s:.1f}s / 30.0s)...")

proc.stdin.close()
proc.wait()

print("\n==========================================")
print(f"🎬 VIDEO SUKSES DI-RENDER 100%!")
print(f"Output: {OUT_VIDEO_PATH}")
print(f"Size: {os.path.getsize(OUT_VIDEO_PATH) / (1024*1024):.2f} MB")
print("==========================================")
