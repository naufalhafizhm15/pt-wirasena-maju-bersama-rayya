from PIL import Image, ImageDraw

f = Image.open('/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/business-card/master-cetak/MASTER-CETAK-KARTU-DEPAN-300DPI.png')
b = Image.open('/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/business-card/master-cetak/MASTER-CETAK-KARTU-BELAKANG-300DPI.png')

# Create showcase
w, h = f.size
show = Image.new('RGB', (w * 2 + 100, h + 100), '#081410')
show.paste(f, (40, 50))
show.paste(b, (w + 60, 50))

out_p = '/home/naufalhzh/.gemini/antigravity/scratch/pt-wirasena-maju-bersama-rayya/assets/business-card/showcase-sisyphus-style.png'
show.save(out_p, quality=95)
print('Saved showcase to', out_p)
