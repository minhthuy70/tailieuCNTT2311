# -*- coding: utf-8 -*-
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(^## Trang \d+\s*$)', text, flags=re.MULTILINE)

page_markers = []
pages_dict = {}

for i in range(1, len(parts), 2):
    marker = parts[i].strip()
    p_num = int(re.search(r'\d+', marker).group(0))
    page_markers.append(p_num)
    pages_dict[p_num] = parts[i+1].strip()

print(f"Total page markers found: {len(page_markers)}")
print(f"Min page: {min(page_markers)}, Max page: {max(page_markers)}")

missing_pages = [p for p in range(1, 215) if p not in pages_dict]
if missing_pages:
    print(f"ERROR: Missing pages: {missing_pages}")
else:
    print("SUCCESS: All 214 pages (1 to 214) are present and in order!")

# Check for empty pages
empty_pages = [p for p in range(1, 215) if len(pages_dict.get(p, '')) == 0]
print(f"Empty pages: {empty_pages}")

# Check Chapter titles
chapters = [
    (21, "CHƯƠNG 1"),
    (32, "CHƯƠNG 2"),
    (52, "CHƯƠNG 3"),
    (83, "CHƯƠNG 4"),
    (116, "CHƯƠNG 5"),
    (143, "CHƯƠNG 6"),
    (179, "CHƯƠNG 7"),
    (205, "KẾT LUẬN"),
    (209, "TÀI LIỆU THAM KHẢO"),
]

print("\nVerifying Chapter Titles:")
for p, title in chapters:
    page_text = pages_dict.get(p, "")
    has_title = title in page_text
    print(f"  Page {p:03d}: {'[OK]' if has_title else '[FAIL]'} contains '{title}' (first line: {page_text.splitlines()[0] if page_text else 'EMPTY'})")

# Check Exercises
exercises = [
    (31, "BÀI TẬP CHƯƠNG 1"),
    (51, "BÀI TẬP CHƯƠNG 2"),
    (82, "BÀI TẬP CHƯƠNG 3"),
    (114, "BÀI TẬP CHƯƠNG 4"),
    (142, "BÀI TẬP CHƯƠNG 5"),
    (178, "BÀI TẬP CHƯƠNG 6"),
    (204, "BÀI TẬP CHƯƠNG 7"),
]

print("\nVerifying Exercise Sections:")
for p, title in exercises:
    page_text = pages_dict.get(p, "")
    has_ex = title in page_text
    print(f"  Page {p:03d}: {'[OK]' if has_ex else '[FAIL]'} contains '{title}'")

print(f"\nTotal file size: {len(text.encode('utf-8')):,} bytes")
print(f"Total lines: {len(text.splitlines()):,}")
