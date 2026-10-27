import sys
import os
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def clean_manual_snippet(text):
    t = re.sub(r'(?m)^## Trang \d+\s*\n+', '', text)
    t = re.sub(r'(?m)^\[\d+\].*?\n+', '', t)
    t = re.sub(r'(?m)^---\s*\n+', '', t)
    t = t.replace("nối các thiết bị thông minh", "kết nối các thiết bị thông minh")
    t = t.replace("mạng kết nối.\n\nNhững đối tượng này", "Những đối tượng này")
    t = t.replace("chương trình chứng nhận (certification program) cho\n\ncác thiết bị kết nối không dây.",
                  "chương trình chứng nhận (certification program) cho các thiết bị kết nối không dây.")
    t = t.replace("Trong các đô thị thông minh, mạng cảm biến không dây thường\n\nthường được triển khai",
                  "Trong các đô thị thông minh, mạng cảm biến không dây thường được triển khai")
    
    dup_str = "Một thế giới kết nối, hay “Internet của vạn vật” (Internet of Things - IoTs), sẽ mang lại giá trị kinh tế lớn. Tuy nhiên, hiện mới chỉ có khoảng 1% thiết bị được kết nối trên toàn cầu. Báo cáo của Cisco trình bày “Internet của vạn vật” đã mang lại 613 tỷ USD lợi nhuận trong năm 2013 và những công ty tối ưu hóa\n\n"
    t = t.replace(dup_str, "")
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()

print("Loading GT_IoT_Manual.md and IoTmain.md...")
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    manual = f.read()

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md', 'r', encoding='utf-8') as f:
    iotmain = f.read()

# 1. Trích xuất Phần Mở Đầu
p_md_start = manual.find('PHẦN MỞ ĐẦU')
p_md_end = manual.find('# MỤC LỤC')
mo_dau_raw = manual[p_md_start:p_md_end]
mo_dau_clean = clean_manual_snippet(mo_dau_raw)

# Xóa tiêu đề chữ hoa 'PHẦN MỞ ĐẦU' ở đầu để tạo tiêu đề markdown chuẩn
mo_dau_body = mo_dau_clean.replace("PHẦN MỞ ĐẦU", "").strip()
mo_dau_section = f"""# Phần mở đầu: Lời giới thiệu giáo trình

{mo_dau_body}
"""

# 2. Trích xuất Chương 1 từ GT_IoT_Manual.md
# Từ '### 1.1. Tổng quan về công nghệ Internet vạn vật' đến '## BÀI TẬP CHƯƠNG 1'
p_ch1_start = manual.find('### 1.1. Tổng quan về công nghệ Internet vạn vật')
p_ch1_end = manual.find('# CHƯƠNG 2. CÁC LĨNH VỰC ỨNG DỤNG IOT')
ch1_manual_raw = manual[p_ch1_start:p_ch1_end]
ch1_manual_clean = clean_manual_snippet(ch1_manual_raw)

# Tách thành các phần con rõ ràng
# Phần A: Thống kê toàn cầu và các chương trình nghiên cứu
p_oic = ch1_manual_clean.find('**Open InterConnect Consortium (OIC)**')
ch1_part_stats_research = ch1_manual_clean[:p_oic].replace("### 1.1. Tổng quan về công nghệ Internet vạn vật", "").strip()

# Phần B: Các tổ chức tiêu chuẩn hóa và liên minh quốc tế
p_challenges = ch1_manual_clean.find('**Phần mềm:** Trong quy trình phức tạp')
ch1_part_standards = ch1_manual_clean[p_oic:p_challenges].strip()

# Phần C: Các thách thức kỹ thuật cốt lõi
p_sec12 = ch1_manual_clean.find('### 1.2. Xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam')
ch1_part_challenges = ch1_manual_clean[p_challenges:p_sec12].strip()

# Phần D: Xu thế ứng dụng tại Việt Nam và Bài tập Chương 1
ch1_part_vietnam_and_exercises = ch1_manual_clean[p_sec12:].strip()

# 3. Trích xuất Chương 4 phần cứng từ GT_IoT_Manual.md
# 4.1.1 đến 4.1.5
p_ch4_intro = manual.find('Công nghệ IoT được phát triển để phục vụ cho nhiều lĩnh vực khác nhau')
p_ch4_411 = manual.find('#### 4.1.1. Những đặc trưng và phân loại các nền tảng phần cứng dùng cho IoT')
ch4_intro = clean_manual_snippet(manual[p_ch4_intro:p_ch4_411])

p_ch4_412 = manual.find('#### 4.1.2. Thiết bị cảm biến không dây TelosB')
ch4_411 = clean_manual_snippet(manual[p_ch4_411:p_ch4_412])

p_ch4_413 = manual.find('#### 4.1.3. Thiết bị nhúng Arduino')
ch4_412 = clean_manual_snippet(manual[p_ch4_412:p_ch4_413])

p_ch4_414 = manual.find('#### 4.1.4. Thiết bị máy tính nhúng Raspberry Pi')
ch4_413 = clean_manual_snippet(manual[p_ch4_413:p_ch4_414])

p_ch4_415 = manual.find('#### 4.1.5. Tổng hợp một số nền tảng phần cứng IoT phổ biến')
ch4_414 = clean_manual_snippet(manual[p_ch4_414:p_ch4_415])

p_ch4_sw = manual.find('### 4.2. Các nền tảng phần mềm dùng trong IoT')
ch4_415 = clean_manual_snippet(manual[p_ch4_415:p_ch4_sw])

p_ch4_tiny = manual.find('#### 4.2.2. Hệ điều hành TinyOS')
ch4_421 = clean_manual_snippet(manual[p_ch4_sw:p_ch4_tiny])

print("Extraction completed successfully!")
print(f"- Mở đầu: {len(mo_dau_section)} chars")
print(f"- Ch1 Stats & Research: {len(ch1_part_stats_research)} chars")
print(f"- Ch1 Standards: {len(ch1_part_standards)} chars")
print(f"- Ch1 Challenges: {len(ch1_part_challenges)} chars")
print(f"- Ch1 Vietnam & Exercises: {len(ch1_part_vietnam_and_exercises)} chars")
print(f"- Ch4 Hardware taxonomy (4.1.1): {len(ch4_411)} chars")
print(f"- Ch4 Arduino (4.1.3): {len(ch4_413)} chars")
print(f"- Ch4 Raspberry Pi (4.1.4): {len(ch4_414)} chars")
print(f"- Ch4 OS taxonomy (4.2.1): {len(ch4_421)} chars")
