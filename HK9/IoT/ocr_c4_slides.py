# -*- coding: utf-8 -*-
"""
Render all pages from 48 to 160 of IoT_Application Development_C4_updated.pdf
and run Tesseract OCR on each page to inspect the content thoroughly.
"""
import os, sys, json
import pymupdf
from PIL import Image
import pytesseract

sys.stdout.reconfigure(encoding='utf-8')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\tessdata'

pdf_path = r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Baigiang\IoT_Application Development_C4_updated.pdf'
out_dir = r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Baigiang\c4_pages'
os.makedirs(out_dir, exist_ok=True)

doc = pymupdf.open(pdf_path)
print(f"Total pages in doc: {len(doc)}")

ocr_data = {}

for pno in range(47, len(doc)): # 0-indexed: 47 is page 48, up to 159 (page 160)
    page_num = pno + 1
    page = doc[pno]
    img_path = os.path.join(out_dir, f'page_{page_num:03d}.png')
    
    # Render if not exists
    if not os.path.exists(img_path):
        pix = page.get_pixmap(dpi=150)
        pix.save(img_path)
    
    img = Image.open(img_path)
    # OCR with eng+vie
    text = pytesseract.image_to_string(img, lang='eng+vie')
    ocr_data[page_num] = text.strip()
    
    # Print high level summary
    first_few_lines = [l.strip() for l in text.splitlines() if l.strip()][:3]
    summary = " | ".join(first_few_lines)
    print(f"P.{page_num:03d}: {summary[:90]}")

# Save all OCR text to json for fast access
json_path = os.path.join(out_dir, 'ocr_pages_48_160.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(ocr_data, f, ensure_ascii=False, indent=2)

print(f"\nAll pages 48 to 160 processed and saved to {json_path}")
