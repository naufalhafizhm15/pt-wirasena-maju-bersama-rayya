from PIL import Image

# Open original uploaded WB logo
img = Image.open('/home/naufalhzh/.gemini/antigravity/brain/eed21edb-60e5-4e2f-86a8-177dc2bedcaf/.user_uploaded/media_1793329914531_30ffa296.jpg').convert('RGBA')

# The user wants ONLY the upper 3D emerald WB ribbon emblem + outer oval ring (without the micro text underneath)
# Dimensions of original: 1024 x 571
# Text "PT. WIRASENA MAJU BERSAMA RAYYA" starts at y ~ 370
# Let's crop just the emblem symbol + ring (y from 0 to 365, x from 50 to 974)
w, h = img.size

# Make white/off-white background pure transparent
datas = img.getdata()
new_data = []
for item in datas:
    r, g, b, a = item
    # If pixel is near white/light grey (background)
    if r > 235 and g > 235 and b > 235:
        # Fully transparent
        new_data.append((0, 0, 0, 0))
    elif r > 210 and g > 210 and b > 210:
        # Soft antialiased blend
        alpha = int(255 - ((r - 210) / 25.0 * 255))
        new_data.append((r, g, b, max(0, min(255, alpha))))
    else:
        new_data.append(item)

img_trans = Image.new('RGBA', img.size)
img_trans.putdata(new_data)

# Let's crop the emblem (WB + Ring), masking out the text at bottom
# Crop box around symbol:
crop_symbol = img_trans.crop((50, 10, 974, 370))

# Trim any transparent borders
bbox = crop_symbol.getbbox()
if bbox:
    crop_symbol = crop_symbol.crop(bbox)

out_symbol = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/logo-wb-clean-transparent.png'
crop_symbol.save(out_symbol)
print('Saved clean transparent WB symbol at', out_symbol, 'Size:', crop_symbol.size)

# Also let's save full version (with text) clean transparent
crop_full = img_trans.crop((50, 10, 974, 520))
bbox_full = crop_full.getbbox()
if bbox_full:
    crop_full = crop_full.crop(bbox_full)
out_full = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/logo-wb-full-transparent.png'
crop_full.save(out_full)
print('Saved full transparent WB logo at', out_full, 'Size:', crop_full.size)

