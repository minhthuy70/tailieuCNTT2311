# -*- coding: utf-8 -*-
import os, sys
from PIL import Image
import pytesseract

sys.stdout.reconfigure(encoding='utf-8')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\tessdata'

for p in [111, 112, 113]:
    img_path = rf'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\pages\page_{p:03d}.png'
    img = Image.open(img_path)
    # Page 111 text is readable at rot 270
    # Page 112: top part rot 90, bottom part rot 270
    # Let's see which rotation is upright for each:
    for rot in [270, 90]:
        img_rot = img.rotate(rot, expand=True)
        txt = pytesseract.image_to_string(img_rot, lang='vie')
        print(f'=== PAGE {p} ROT {rot} ===')
        print(txt)
