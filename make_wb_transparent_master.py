from PIL import Image

img = Image.open('/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/logo-wb-master-3d.jpg').convert('RGBA')

# The background is solid dark obsidian #002113 (r < 10, g ~ 33, b ~ 19)
# Let's cleanly isolate the emerald ribbon logo
datas = img.getdata()
new_data = []

for item in datas:
    r, g, b, a = item
    # If pixel is dark background (low brightness or close to #002113)
    if r < 15 and g < 45 and b < 30:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(item)

img.putdata(new_data)
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

out_p = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/logo-wb-master-transparent.png'
img.save(out_p)
print('Master transparent logo saved at', out_p, 'Size:', img.size)
