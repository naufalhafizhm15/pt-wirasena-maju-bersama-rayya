import math
from PIL import Image, ImageDraw

def render_flat_vector_wb(size=600):
    # Pure flat vector monogram WB matching Sisyphus flat aesthetic
    # Transparent background, clean solid flat emerald/mint geometric planes
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Palette matching Sisyphus flat cards (NO metallic shine, pure solid modern colors)
    C_BASE = (0, 154, 76, 255)      # Emerald Base #009A4C
    C_MID = (0, 185, 96, 255)       # Mid Emerald #00B960
    C_MINT = (104, 219, 154, 255)   # Mint Highlight #68DB9A
    C_DARK = (0, 110, 55, 255)      # Deep Emerald Shade #006E37

    s = size / 600.0

    # Draw continuous vector geometric ribbon forming W and B
    # Letter 'W' (Left Stroke, Center V, Right Connection)
    # Stroke 1: Left diagonal upward
    p1 = [(110*s, 380*s), (170*s, 190*s), (230*s, 220*s), (170*s, 410*s)]
    draw.polygon(p1, fill=C_BASE)

    # Stroke 2: Left top cap / fold
    p2 = [(170*s, 190*s), (230*s, 220*s), (200*s, 260*s), (140*s, 230*s)]
    draw.polygon(p2, fill=C_MINT)

    # Stroke 3: Center downward V
    p3 = [(170*s, 410*s), (230*s, 220*s), (280*s, 290*s), (220*s, 440*s)]
    draw.polygon(p3, fill=C_MID)

    # Stroke 4: Center upward V to apex
    p4 = [(220*s, 440*s), (280*s, 290*s), (340*s, 340*s), (280*s, 460*s)]
    draw.polygon(p4, fill=C_DARK)

    # Stroke 5: Rising to B connection
    p5 = [(280*s, 290*s), (340*s, 200*s), (390*s, 230*s), (340*s, 340*s)]
    draw.polygon(p5, fill=C_MINT)

    # Letter 'B' (Top Loop & Bottom Loop)
    # Top Loop of B
    p_b_top = [(340*s, 200*s), (440*s, 200*s), (480*s, 260*s), (420*s, 310*s), (340*s, 310*s), (390*s, 230*s)]
    draw.polygon(p_b_top, fill=C_MID)

    p_b_top_inner = [(380*s, 240*s), (430*s, 240*s), (440*s, 270*s), (400*s, 280*s)]
    draw.polygon(p_b_top_inner, fill=C_MINT)

    # Bottom Loop of B (Sweeping out slightly wider)
    p_b_bot = [(340*s, 310*s), (440*s, 310*s), (490*s, 380*s), (430*s, 440*s), (330*s, 440*s), (310*s, 390*s)]
    draw.polygon(p_b_bot, fill=C_BASE)

    p_b_bot_inner = [(370*s, 350*s), (430*s, 350*s), (450*s, 390*s), (390*s, 400*s)]
    draw.polygon(p_b_bot_inner, fill=C_MINT)

    # Final crop to content bbox
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    return img

flat_wb = render_flat_vector_wb(600)
out_p = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/logo-wb-flat-vector.png'
flat_wb.save(out_p)
print('Flat vector WB generated at', out_p, 'Size:', flat_wb.size)

