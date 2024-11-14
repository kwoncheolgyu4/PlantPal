from PIL import Image
from pathlib import Path

path_dir = "plant_image\\test\\VS_제비쑥"

for fname in Path(path_dir).iterdir():
    try:
        img = Image.open(fname)
        re_img = img.resize((224, 224), Image.Resampling.LANCZOS)
        re_img.save(fname, quality=100)
        print("success : " + str(fname))
    except Exception as e:
        print(e)
        pass