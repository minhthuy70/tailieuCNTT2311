# -*- coding: utf-8 -*-
"""
Verification Script for IoTmain.md (The Unified Textbook)
"""
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print(f"Total lines: {len(lines)}")
print(f"Total characters: {len(text)}")

# 1. Check for any remaining page markers
page_markers = re.findall(r'## Trang \d+', text)
print(f"1. Remaining page markers: {len(page_markers)}")
assert len(page_markers) == 0, f"Found {len(page_markers)} page markers!"

# 2. Check all Chapters
print("\n2. Checking Chapter headings:")
expected_chapters = [
    "# Chương 1: Giới thiệu",
    "# Chương 2: Các lĩnh vực ứng dụng IoT",
    "# Chương 3: Các kiến trúc mạng và bộ giao thức mạng IoT",
    "# Chương 4: Các nền tảng phần cứng và phần mềm IoT thông dụng",
    "# Chương 5: Điện toán đám mây, điện toán cận biên và IoT",
    "# Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT",
    "# Chương 7: Tái cấu hình trong IoT",
    "# Kết luận",
    "# Tài liệu tham khảo",
    "# Thông tin xuất bản"
]

for ch in expected_chapters:
    if ch in text:
        print(f"   [OK] Found: {ch}")
    else:
        print(f"   [MISSING] Not found: {ch}")

# 3. Check all Exercise sections
print("\n3. Checking Exercise sections:")
expected_exercises = [
    "## Bài tập Chương 1",
    "## Bài tập Chương 2",
    "## Bài tập Chương 3",
    "## Bài tập Chương 4",
    "## Bài tập Chương 5",
    "## Bài tập Chương 6",
    "## Bài tập Chương 7"
]

for ex in expected_exercises:
    if ex in text:
        print(f"   [OK] Found: {ex}")
    else:
        print(f"   [MISSING] Not found: {ex}")

# 4. Check all Tables
print("\n4. Checking Tables:")
expected_tables = [
    "Các ký hiệu viết tắt",
    "Bảng 3.3",
    "Bảng 3.4",
    "Bảng 3.5",
    "Bảng 3.6",
    "Bảng 3.7",
    "Bảng 4.1",
    "Bảng 4.2",
    "Bảng 4.3",
    "Bảng 5.1",
    "Bảng 6.2",
    "Bảng 6.5",
    "Bảng 6.6"
]

for tb in expected_tables:
    if tb in text:
        print(f"   [OK] Found table marker: {tb}")
    else:
        print(f"   [MISSING] Table marker not found: {tb}")

# 5. Check original IoTmain key sections preservation
print("\n5. Checking original IoTmain key passages:")
key_passages = [
    "TS. Nguyễn Đình Tứ",
    "1.1.1. Khái niệm và bối cảnh",
    "1.1.2 Định nghĩa IoT",
    "1.1.3. Background and More Complete IoT Definition",
    "1.1.8. Level IoT",
    "1.1.10.Convergence of IT and OT",
    "1.1.13. The Nonstop Moore’s Law",
    "ORing, NCU (National Central University), and Chunghwa Telecom",
    "3.1. The Open System Interconnection Model",
    "3.2. Transmission Control Protocol/Internet Protocol (TCP/IP)",
    "3.3. IoT Network Level: Key Performance Characteristics",
    "Wide Area Networks (WAN) (*Mạng diện rộng*)",
    "3.9. Cảm biến trong IoT (IoT Sensors)",
    "4.1. Wireless Sensor Networks (WSN)",
    "4.3. The Role of Open Source in IoT",
    "NVIDIA Jetson Nano",
    "Giao thức MQTT",
    "Nền tảng Blynk",
    "Triết lý Arduino (The Arduino Way)",
    "Anatomy of an Interactive Device",
    "delay(100);"
]

for kp in key_passages:
    if kp in text:
        print(f"   [OK] Preserved: {kp[:50]}")
    else:
        print(f"   [MISSING]: {kp[:50]}")

# 6. Check code block fences balance
print("\n6. Checking code block fences:")
code_fences = len(re.findall(r'(?m)^```', text))
print(f"   Total code fences: {code_fences} ({'BALANCED' if code_fences % 2 == 0 else 'UNBALANCED!'})")

# 7. Check references count
print("\n7. Checking References in Tài liệu tham khảo:")
ref_matches = re.findall(r'(?m)^\d+\.\s+', text[text.find("# Tài liệu tham khảo"):])
print(f"   Total references found: {len(ref_matches)}")

print("\n--- ALL VERIFICATIONS FINISHED ---")
