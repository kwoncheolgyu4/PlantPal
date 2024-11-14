# pip install opencv-python-headless ultralytics cryptography
from googleapiclient.mimeparse import quality
from keras.src.testing_infra.test_utils import for_all_test_methods
from ultralytics import YOLO
import cv2
import base64
import numpy as np

img_path = "./image_re/곰취_전초_1991469.jpg"
img = cv2.imread(img_path)
frame = cv2.resize(img, (224,224))

cv2.imwrite('./image_re/resize_image2.jpg', frame)


from PIL import Image
from pathlib import Path

path_dir = ""

for fname in Path(path_dir).iterdir():
    try:
        img = Image.open(fname)
        re_img = img.resize((1000, 1000), Image.LANCZOS) # Image.ANTIALIAS
        re_img.save(fname, quality=100)
        print("success : " + str(fname))
    except Exception as e:
        print(e)
        pass