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

print("1. Đọc tệp GT_IoT_Manual.md và IoTmain.md...")
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    manual = f.read()

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md', 'r', encoding='utf-8') as f:
    iotmain = f.read()

# -------------------------------------------------------------
# TRÍCH XUẤT CÁC PHẦN TỪ GT_IOT_MANUAL.MD
# -------------------------------------------------------------

# A. Phần Mở Đầu
p_md_start = manual.find('PHẦN MỞ ĐẦU')
p_md_end = manual.find('# MỤC LỤC')
mo_dau_raw = manual[p_md_start:p_md_end]
mo_dau_clean = clean_manual_snippet(mo_dau_raw).replace("PHẦN MỞ ĐẦU", "").strip()

mo_dau_section = f"""# Phần mở đầu: Lời giới thiệu giáo trình

{mo_dau_clean}
"""

# B. Chương 1 từ GT_IoT_Manual.md
p_ch1_start = manual.find('### 1.1. Tổng quan về công nghệ Internet vạn vật')
p_ch1_end = manual.find('# CHƯƠNG 2. CÁC LĨNH VỰC ỨNG DỤNG IOT')
ch1_manual_clean = clean_manual_snippet(manual[p_ch1_start:p_ch1_end])

p_oic = ch1_manual_clean.find('**Open InterConnect Consortium (OIC)**')
ch1_stats_research = ch1_manual_clean[:p_oic].replace("### 1.1. Tổng quan về công nghệ Internet vạn vật", "").strip()

p_challenges = ch1_manual_clean.find('**Phần mềm:** Trong quy trình phức tạp')
ch1_standards = ch1_manual_clean[p_oic:p_challenges].strip()

p_sec12 = ch1_manual_clean.find('### 1.2. Xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam')
ch1_challenges = ch1_manual_clean[p_challenges:p_sec12].strip()

p_bt1 = ch1_manual_clean.find('## BÀI TẬP CHƯƠNG 1')
ch1_vietnam = ch1_manual_clean[p_sec12:p_bt1].replace("### 1.2. Xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam", "").strip()
ch1_exercises = ch1_manual_clean[p_bt1:].replace("## BÀI TẬP CHƯƠNG 1", "").strip()

# C. Chương 4 phần cứng từ GT_IoT_Manual.md
p_ch4_intro = manual.find('Công nghệ IoT được phát triển để phục vụ cho nhiều lĩnh vực khác nhau')
p_ch4_411 = manual.find('#### 4.1.1. Những đặc trưng và phân loại các nền tảng phần cứng dùng cho IoT')
ch4_intro = clean_manual_snippet(manual[p_ch4_intro:p_ch4_411])

p_ch4_412 = manual.find('#### 4.1.2. Thiết bị cảm biến không dây TelosB')
ch4_411 = clean_manual_snippet(manual[p_ch4_411:p_ch4_412]).replace("#### 4.1.1. Những đặc trưng và phân loại các nền tảng phần cứng dùng cho IoT", "").strip()

p_ch4_413 = manual.find('#### 4.1.3. Thiết bị nhúng Arduino')
ch4_412 = clean_manual_snippet(manual[p_ch4_412:p_ch4_413]).replace("#### 4.1.2. Thiết bị cảm biến không dây TelosB", "").strip()

p_ch4_414 = manual.find('#### 4.1.4. Thiết bị máy tính nhúng Raspberry Pi')
ch4_413 = clean_manual_snippet(manual[p_ch4_413:p_ch4_414]).replace("#### 4.1.3. Thiết bị nhúng Arduino", "").strip()

p_ch4_415 = manual.find('#### 4.1.5. Tổng hợp một số nền tảng phần cứng IoT phổ biến')
ch4_414 = clean_manual_snippet(manual[p_ch4_414:p_ch4_415]).replace("#### 4.1.4. Thiết bị máy tính nhúng Raspberry Pi", "").strip()

p_ch4_sw = manual.find('### 4.2. Các nền tảng phần mềm dùng trong IoT')
ch4_415 = clean_manual_snippet(manual[p_ch4_415:p_ch4_sw])

p_ch4_tiny = manual.find('#### 4.2.2. Hệ điều hành TinyOS')
ch4_421 = clean_manual_snippet(manual[p_ch4_sw:p_ch4_tiny]).replace("### 4.2. Các nền tảng phần mềm dùng trong IoT", "").replace("#### 4.2.1. Những đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT", "").strip()

# -------------------------------------------------------------
# GHÉP VÀO IOTMAIN.MD
# -------------------------------------------------------------
print("2. Tích hợp Phần Mở Đầu vào đầu sách...")
# Chèn Phần mở đầu vào ngay trước '# Chương 1: Giới thiệu'
ch1_marker = "# Chương 1: Giới thiệu"
pos_ch1 = iotmain.find(ch1_marker)
if pos_ch1 != -1:
    before_ch1 = iotmain[:pos_ch1].strip()
    after_ch1 = iotmain[pos_ch1:]
    iotmain_step1 = before_ch1 + "\n\n" + mo_dau_section + "\n" + after_ch1
else:
    iotmain_step1 = iotmain

print("3. Tích hợp đầy đủ các phần của Chương 1...")
# Trong Chương 1, thay thế phần tóm tắt ngắn từ '## 1.2. Trends of applying IoT' tới '## Bài tập Chương 1'
ch1_rep_start = iotmain_step1.find('## 1.2. Trends of applying IoT')
ch1_rep_end = iotmain_step1.find('# Chương 2: Các lĩnh vực ứng dụng IoT')

if ch1_rep_start != -1 and ch1_rep_end != -1:
    ch1_rich_integration = f"""## 1.2. Thống kê quy mô toàn cầu và các chương trình nghiên cứu IoT quốc tế

{ch1_stats_research}

## 1.3. Các tổ chức tiêu chuẩn hóa và liên minh IoT quốc tế

{ch1_standards}

## 1.4. Các thách thức kỹ thuật cốt lõi trong phát triển hệ thống IoT

{ch1_challenges}

## 1.5. Xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam

{ch1_vietnam}

## Bài tập Chương 1

{ch1_exercises}
"""
    iotmain_step2 = iotmain_step1[:ch1_rep_start] + ch1_rich_integration + "\n" + iotmain_step1[ch1_rep_end:]
else:
    print("Warning: Không tìm thấy vị trí thay thế Chương 1, giữ nguyên.")
    iotmain_step2 = iotmain_step1

print("4. Tích hợp đầy đủ phần cứng & hệ điều hành của Chương 4...")
# Tìm vị trí '## 4.4. Các nền tảng phần cứng'
p_hw_start = iotmain_step2.find('## 4.4. Các nền tảng phần cứng')
p_sw_start = iotmain_step2.find('## 4.5. Các nền tảng phần mềm')

if p_hw_start != -1 and p_sw_start != -1:
    # Lấy các phần cứng phụ hiện có trong IoTmain (GizmoSphere, Tinkerforge, BeagleBoard, Jetson Nano, Zerynth...)
    existing_hw_text = iotmain_step2[p_hw_start:p_sw_start]
    
    # Trích xuất các bo mạch mở rộng từ existing_hw_text
    p_gizmo = existing_hw_text.find('### GizmoSphere')
    if p_gizmo != -1:
        extra_hw_text = existing_hw_text[p_gizmo:].strip()
    else:
        extra_hw_text = ""
        
    rich_ch4_hw = f"""## 4.4. Các nền tảng phần cứng dùng trong IoT (IoT Hardware Platforms)

{ch4_intro}

### 4.4.1. Những đặc trưng và phân loại các nền tảng phần cứng dùng cho IoT

{ch4_411}

### 4.4.2. Mote cảm biến không dây TelosB

{ch4_412}

### 4.4.3. Thiết bị nhúng Arduino (Kiến trúc phần cứng & Hệ sinh thái)

{ch4_413}

### 4.4.4. Thiết bị máy tính nhúng Raspberry Pi

{ch4_414}

### 4.4.5. Các nền tảng phần cứng và thiết bị biên bổ sung

{extra_hw_text}

### 4.4.6. Bảng tổng hợp so sánh các nền tảng phần cứng IoT đặc trưng

**Bảng 4.1.** Tổng hợp 3 nền tảng phần cứng IoT đặc trưng

| Đặc điểm | TelosB Mote | Arduino-based boards | Raspberry Pi |
|:---|:---|:---|:---|
| **Bộ xử lý** | TI MSP430 16-bit @ 8MHz | ATmega328P 8-bit @ 16MHz (hoặc ESP8266/ESP32 32-bit) | Broadcom BCM2837/2711 Quad-core ARM 64-bit @ 1.4 - 1.5GHz |
| **Bộ nhớ** | 10kB RAM, 48kB Flash | 2kB SRAM, 32kB Flash (ESP32: 520kB RAM, 4MB Flash) | 1GB - 8GB LPDDR4 RAM, thẻ nhớ MicroSD ngoài |
| **Kết nối mạng** | IEEE 802.15.4 / Zigbee (2.4GHz, 250kbps) | Cần shield gắn thêm (hoặc tích hợp Wi-Fi/BLE trên ESP) | Gigabit Ethernet, Wi-Fi Dual-band 802.11ac, Bluetooth 5.0 |
| **Cảm biến** | Tích hợp sẵn nhiệt độ, độ ẩm, ánh sáng | Kết nối cảm biến ngoài qua chân GPIO, ADC, I2C, SPI | Kết nối cảm biến ngoài qua GPIO, USB, Camera CSI |
| **Phần mềm** | TinyOS, Contiki OS | Arduino IDE, FreeRTOS, MicroPython | Linux (Raspbian OS), Python, Node.js, C/C++, Java |
| **Nguồn điện** | Nguồn pin 2xAA công suất cực thấp | Cổng USB (5V) hoặc DC 7-12V, tiêu thụ thấp | Cổng USB-C (5V - 3A), tiêu thụ công suất 2W - 5W |
| **Vai trò** | Nút cảm biến không dây (Sensor Node) | Thiết bị đo đạc, cơ cấu chấp hành (End Device / Node) | Cổng kết nối (IoT Gateway), máy chủ biên (Edge Server) |
"""
    iotmain_step3 = iotmain_step2[:p_hw_start] + rich_ch4_hw + "\n\n" + iotmain_step2[p_sw_start:]
else:
    print("Warning: Không tìm thấy Section 4.4, giữ nguyên.")
    iotmain_step3 = iotmain_step2

# Xóa Section 4.8 trùng lặp ở cuối Chương 4 (vì đã đưa lên 4.4.2 và 4.4.6)
# Thay vào đó, mục Hệ điều hành sẽ là Section 4.8
p_old_48 = iotmain_step3.find('## 4.8. Thiết bị cảm biến không dây TelosB và So sánh các nền tảng phần cứng IoT')
p_old_49 = iotmain_step3.find('## 4.9. Đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT')

if p_old_48 != -1 and p_old_49 != -1:
    # Bỏ đoạn cũ từ p_old_48 đến p_old_49
    after_47 = iotmain_step3[:p_old_48]
    after_old_49 = iotmain_step3[p_old_49:]
    
    # Đưa ch4_421 vào Section 4.8 Hệ điều hành
    rich_os_section = f"""## 4.8. Đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT

{ch4_421}
"""
    # Thay thế '## 4.9. Đặc trưng và phân loại...' bằng rich_os_section
    # và đánh số lại các mục OS sau đó:
    after_old_49_renumbered = after_old_49.replace(
        "## 4.9. Đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT",
        rich_os_section.strip()
    )
    after_old_49_renumbered = after_old_49_renumbered.replace("## 4.10. Hệ điều hành TinyOS", "## 4.9. Hệ điều hành TinyOS")
    after_old_49_renumbered = after_old_49_renumbered.replace("### 4.10.1.", "### 4.9.1.")
    after_old_49_renumbered = after_old_49_renumbered.replace("### 4.10.2.", "### 4.9.2.")
    after_old_49_renumbered = after_old_49_renumbered.replace("## 4.11. Hệ điều hành Contiki", "## 4.10. Hệ điều hành Contiki")
    after_old_49_renumbered = after_old_49_renumbered.replace("### 4.11.1.", "### 4.10.1.")
    after_old_49_renumbered = after_old_49_renumbered.replace("### 4.11.2.", "### 4.10.2.")
    after_old_49_renumbered = after_old_49_renumbered.replace("## 4.12. Hệ điều hành Raspbian OS", "## 4.11. Hệ điều hành Raspbian OS")
    after_old_49_renumbered = after_old_49_renumbered.replace("## 4.13. Bảng tổng hợp so sánh các hệ điều hành IoT phổ biến", "## 4.12. Bảng tổng hợp so sánh các hệ điều hành IoT phổ biến")
    
    iotmain_step4 = after_47 + after_old_49_renumbered
else:
    iotmain_step4 = iotmain_step3

# 5. Ghi tệp hoàn chỉnh ra IoTmain.md
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md', 'w', encoding='utf-8') as f:
    f.write(iotmain_step4)

print(f"Hoàn thành hợp nhất! Kích thước IoTmain.md mới: {len(iotmain_step4):,} ký tự, {len(iotmain_step4.splitlines()):,} dòng.")
