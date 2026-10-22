# -*- coding: utf-8 -*-
"""
Script to build a single unified textbook (1 quyển giáo trình thống nhất hoàn chỉnh)
Merging IoTmain.md and GT_IoT_Manual.md seamlessly without page markers.
"""
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

def remove_page_markers_and_clean(text):
    # Remove page markers ## Trang \d+
    text = re.sub(r'(?m)^## Trang \d+\s*\n+', '', text)
    # Fix repeated words across page breaks
    text = text.replace(
        "Trong các đô thị thông minh, mạng cảm biến không dây thường\n\nthường được triển khai",
        "Trong các đô thị thông minh, mạng cảm biến không dây thường được triển khai"
    )
    text = text.replace(
        "Trong các đô thị thông minh, mạng cảm biến không dây thường\n\n thường được triển khai",
        "Trong các đô thị thông minh, mạng cảm biến không dây thường được triển khai"
    )
    text = text.replace(
        "kết nối mạng.\n\nmạng kết nối.",
        "kết nối mạng."
    )
    # Clean redundant blank lines (more than 2 consecutive)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

print("Reading input files...")
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md', 'r', encoding='utf-8') as f:
    iotmain_raw = f.read()

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    manual_raw = f.read()

# Locate main chapter slices in GT_IoT_Manual.md
pattern = r'(?m)^#\s+(CHƯƠNG\s+\d+\..*?|KẾT LUẬN|TÀI LIỆU THAM KHẢO|THÔNG TIN XUẤT BẢN)$'
matches = list(re.finditer(pattern, manual_raw))
slices = {}
for i in range(len(matches)):
    start = matches[i].start()
    end = matches[i+1].start() if i+1 < len(matches) else len(manual_raw)
    name = matches[i].group(1)
    slices[name] = manual_raw[start:end]

print("Found slices in manual:")
for k in slices:
    print(f"  - {k} ({len(slices[k])} chars)")

