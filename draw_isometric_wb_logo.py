from PIL import Image, ImageDraw

def create_isometric_w_logo(size=300):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Palette matching Sisyphus reference
    C1 = (0, 154, 76, 255)    # Emerald base #009A4C
    C2 = (0, 185, 96, 255)    # Mid emerald #00B960
    C3 = (104, 219, 154, 255) # Mint highlight #68DB9A
    C4 = (0, 120, 60, 255)    # Deep emerald shadow #00783C
    
    # Scaler
    s = size / 300.0
    
    # Geometric Isometric Monogram "W" (Modern Tech-Fold Ribbon style)
    # Left Fold
    p_left_front = [(40*s, 190*s), (90*s, 140*s), (90*s, 240*s), (40*s, 290*s)]
    p_left_top = [(40*s, 190*s), (90*s, 140*s), (140*s, 190*s), (90*s, 240*s)]
    p_left_side = [(90*s, 240*s), (140*s, 190*s), (140*s, 290*s), (90*s, 340*s)]
    
    # Center Peak Fold (Forming the sharp "W" geometric lightning/ribbon)
    # Poly 1: Left upper ribbon
    draw.polygon([(60*s, 170*s), (110*s, 120*s), (160*s, 170*s), (110*s, 220*s)], fill=C3)
    draw.polygon([(60*s, 170*s), (110*s, 220*s), (110*s, 260*s), (60*s, 210*s)], fill=C1)
    draw.polygon([(110*s, 220*s), (160*s, 170*s), (160*s, 210*s), (110*s, 260*s)], fill=C2)

    # Poly 2: Center-Right rising ribbon
    draw.polygon([(140*s, 190*s), (190*s, 140*s), (240*s, 190*s), (190*s, 240*s)], fill=C3)
    draw.polygon([(140*s, 190*s), (190*s, 240*s), (190*s, 280*s), (140*s, 230*s)], fill=C1)
    draw.polygon([(190*s, 240*s), (240*s, 190*s), (240*s, 230*s), (190*s, 280*s)], fill=C2)

    # Center connector forming the seamless "W"
    draw.polygon([(110*s, 120*s), (150*s, 80*s), (190*s, 120*s), (150*s, 160*s)], fill=C3)
    draw.polygon([(150*s, 80*s), (190*s, 120*s), (190*s, 140*s), (150*s, 100*s)], fill=C2)
    draw.polygon([(110*s, 120*s), (150*s, 80*s), (150*s, 100*s), (110*s, 140*s)], fill=C4)

    return img

img = create_isometric_w_logo(400)
out_p = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/logo-wirasena-isometric.png'
img.save(out_p)
print('Generated isometric logo at', out_p)
