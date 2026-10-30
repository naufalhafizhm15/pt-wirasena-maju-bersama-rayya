from PIL import Image

# Load original uploaded image (1024 x 571)
img = Image.open('/home/naufalhzh/.gemini/antigravity/brain/eed21edb-60e5-4e2f-86a8-177dc2bedcaf/.user_uploaded/media_1793329914531_30ffa296.jpg').convert('RGBA')

# In original image:
# The WB letters are around: x: 340 to 680, y: 120 to 320
# Let's crop ONLY the pure 3D WB letters (without the ring, and without any text!)
wb_pure = img.crop((345, 125, 675, 315))

# Make white/off-white background pure transparent
datas = wb_pure.getdata()
new_data = []
for item in datas:
    r, g, b, a = item
    # Check if pixel is white / light grey
    if r > 230 and g > 230 and b > 230:
        new_data.append((0, 0, 0, 0))
    elif r > 200 and g > 200 and b > 200:
        alpha = int(255 - ((r - 200) / 30.0 * 255))
        new_data.append((r, g, b, max(0, min(255, alpha))))
    else:
        new_data.append(item)

wb_pure.putdata(new_data)
bbox = wb_pure.getbbox()
if bbox:
    wb_pure = wb_pure.crop(bbox)

out_pure = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/logo-wb-standalone-pure.png'
wb_pure.save(out_pure)
print('Pure 3D WB letters isolated successfully at', out_pure, 'Size:', wb_pure.size)
