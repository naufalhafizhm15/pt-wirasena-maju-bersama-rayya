from PIL import Image

# Original uploaded logo
orig = Image.open('/home/naufalhzh/.gemini/antigravity/brain/eed21edb-60e5-4e2f-86a8-177dc2bedcaf/.user_uploaded/media_1793329914531_30ffa296.jpg').convert('RGBA')

# In original 1024x571:
# The letters 'WB' strictly sit between:
# x: 350 to 670
# y: 145 to 300 (top ring ends around y=140, letters start at y=145!)
crop_pure = orig.crop((355, 142, 665, 305))

# Convert white/light grey background to pure transparent
datas = crop_pure.getdata()
new_data = []
for item in datas:
    r, g, b, a = item
    if r > 225 and g > 225 and b > 225:
        new_data.append((0, 0, 0, 0))
    elif r > 195 and g > 195 and b > 195:
        # smooth antialiased edge
        alpha = int(255 - ((r - 195) / 30.0 * 255))
        new_data.append((r, g, b, max(0, min(255, alpha))))
    else:
        new_data.append(item)

crop_pure.putdata(new_data)
bbox = crop_pure.getbbox()
if bbox:
    crop_pure = crop_pure.crop(bbox)

# Clean any stray pixel in the upper margin
# Let's verify size
out_p = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/logo-wb-pure-surgical.png'
crop_pure.save(out_p)
print('Surgically cleaned WB saved at', out_p, 'Size:', crop_pure.size)
