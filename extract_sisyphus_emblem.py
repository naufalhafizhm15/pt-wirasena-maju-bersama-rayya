from PIL import Image

ref_front = Image.open('/home/naufalhzh/.gemini/antigravity/brain/eed21edb-60e5-4e2f-86a8-177dc2bedcaf/.user_uploaded/media_1793339746215_05d7a7ba.png').convert('RGBA')

# In ref_front (502 x 288), the isometric lightning/S-monogram is in the center
# Let's crop it precisely:
# x: 200 to 300, y: 55 to 175
crop_box = (210, 58, 290, 178)
emblem = ref_front.crop(crop_box)

# Now remove the dark background (0, 33, 19) to make it pure transparent RGBA
datas = emblem.getdata()
new_data = []
for item in datas:
    # If pixel is close to background dark emerald (0, 33, 19)
    r, g, b, a = item
    if r < 10 and g < 45 and b < 30:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(item)

emblem.putdata(new_data)
out_p = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/images/sisyphus-emblem-exact.png'
emblem.save(out_p)
print('Exact emblem extracted to', out_p)
