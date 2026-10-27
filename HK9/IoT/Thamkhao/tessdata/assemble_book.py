# -*- coding: utf-8 -*-
"""
Full Assembly Script: Tạo 1 quyển giáo trình IoT thống nhất hoàn chỉnh
Giữ nguyên văn nội dung IoTmain.md và tích hợp đầy đủ nội dung từ GT_IoT_Manual.md.
"""
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

def clean_page_markers(text):
    """Xóa tất cả các đánh dấu trang ## Trang X và làm sạch chuyển đoạn."""
    # Xóa ## Trang \d+
    text = re.sub(r'(?m)^## Trang \d+\s*\n+', '', text)
    # Khắc phục từ bị lặp qua chỗ ngắt trang
    text = text.replace(
        "Trong các đô thị thông minh, mạng cảm biến không dây thường\n\nthường được triển khai",
        "Trong các đô thị thông minh, mạng cảm biến không dây thường được triển khai"
    )
    text = text.replace(
        "kết nối mạng.\n\nmạng kết nối.",
        "kết nối mạng."
    )
    # Khắc phục các đoạn bị đứt dòng giữa câu
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def promote_headings_manual(text):
    """
    Chuyển đổi cấp độ tiêu đề từ GT_IoT_Manual.md sang chuẩn của quyển sách:
    # CHƯƠNG X -> # Chương X: ...
    ### X.Y. -> ## X.Y.
    #### X.Y.Z. -> ### X.Y.Z.
    ##### X.Y.Z.W. -> #### X.Y.Z.W.
    ## BÀI TẬP CHƯƠNG X -> ## Bài tập Chương X
    """
    lines = text.splitlines()
    out = []
    for line in lines:
        # Check BÀI TẬP
        m_bt = re.match(r'^##\s+BÀI TẬP CHƯƠNG\s+(\d+)', line, re.IGNORECASE)
        if m_bt:
            out.append(f"## Bài tập Chương {m_bt.group(1)}")
            continue
        # Check #####
        if line.startswith('##### '):
            out.append('#### ' + line[6:])
            continue
        # Check ####
        if line.startswith('#### '):
            out.append('### ' + line[5:])
            continue
        # Check ###
        if line.startswith('### '):
            out.append('## ' + line[4:])
            continue
        out.append(line)
    return '\n'.join(out)

# 1. Đọc nội dung 2 file gốc
print("Đang đọc IoTmain.md và GT_IoT_Manual.md...")
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md', 'r', encoding='utf-8') as f:
    iotmain_content = f.read()

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    manual_content = f.read()

# 2. Tách các lát cắt (slices) từ GT_IoT_Manual.md
pattern = r'(?m)^#\s+(CHƯƠNG\s+\d+\..*?|KẾT LUẬN|TÀI LIỆU THAM KHẢO|THÔNG TIN XUẤT BẢN)$'
matches = list(re.finditer(pattern, manual_content))
slices = {}
for i in range(len(matches)):
    start = matches[i].start()
    end = matches[i+1].start() if i+1 < len(matches) else len(manual_content)
    name = matches[i].group(1)
    slices[name] = manual_content[start:end]

# --- CHƯƠNG 1 BỔ SUNG ---
ch1_raw = slices['CHƯƠNG 1. GIỚI THIỆU']
ch1_cleaned = clean_page_markers(ch1_raw)

ch1_standards_and_challenges = """
### 1.1.17. Các tổ chức tiêu chuẩn hóa và liên minh IoT quốc tế

Nhằm giải quyết bài toán phân mảnh và đảm bảo khả năng tương thích liên thông giữa hàng tỷ thiết bị thông minh từ các nhà sản xuất khác nhau, nhiều liên minh công nghệ và tổ chức tiêu chuẩn quốc tế đã ra đời:

- **Open Interconnect Consortium (OIC)** [12]: Được thành lập bởi các tập đoàn công nghệ hàng đầu (Intel, Samsung, Broadcom, Dell...) nhằm xác định đặc tả kỹ thuật và tiêu chuẩn truyền thông mở, cho phép các thiết bị kết nối không dây giao tiếp liền mạch mà không phụ thuộc vào hệ điều hành hay giao thức mạng vật lý bên dưới.
- **AllSeen Alliance** [13]: Liên minh gồm các tập đoàn công nghệ lớn như Haier, LG Electronics, Panasonic, Qualcomm, Sharp, Technicolor, Silicon Image, TP-LINK và Microsoft, phối hợp phát triển khung hạ tầng phần mềm nguồn mở AllJoyn (khởi xướng bởi Qualcomm).
- **IEEE 802.15.4** [14]: Chuẩn truyền thông vật lý (PHY) và điều khiển truy cập môi trường (MAC) cho mạng cảm biến không dây công suất thấp (LR-WPAN).
- **IETF CoAP (Constrained Application Protocol)** [15]: Giao thức tầng ứng dụng tối ưu theo mô hình REST cho các thiết bị tài nguyên hạn chế hoạt động trên UDP.
- **Zigbee Alliance** [16]: Liên minh xây dựng bộ giao thức mạng lưới (mesh) công suất thấp ứng dụng trong nhà thông minh và tự động hóa tòa nhà.
- **Bluetooth Special Interest Group (SIG) & Bluetooth Smart (BLE)** [17]: Chuẩn giao tiếp tầm ngắn năng lượng thấp cho thiết bị đeo và di động.
- **W3C Semantic Sensor Networks (SSN)** [18]: Chuẩn hóa ngữ nghĩa dữ liệu cảm biến dựa trên mô hình bản thể học Ontology (OWL/RDF).
- **Open Geospatial Consortium (OGC) Sensor Web Enablement (SWE)** [19] và **CityGML** [20]: Chuẩn hóa dịch vụ web cảm biến không gian địa lý và mô hình hóa dữ liệu không gian 3D cho đô thị thông minh.
- **European Sensor Network Architecture (ESNA)** [21]: Khung kiến trúc mạng cảm biến châu Âu.
- **IETF 6LoWPAN** [22]: Tiêu chuẩn đưa giao thức IPv6 trực tiếp xuống các mạng cảm biến không dây năng lượng thấp thông qua kỹ thuật nén tiêu đề và phân mảnh gói tin.

### 1.1.18. Các thách thức kỹ thuật cốt lõi trong phát triển hệ thống IoT

Tốc độ tăng trưởng nhanh chóng của Internet of Things đặt ra nhiều thách thức kỹ thuật phức tạp cần giải quyết đồng thời:

1. **Phần mềm (Software):** Đóng vai trò sống còn trong toàn bộ vòng đời phát triển của thiết bị và hệ thống IoT, bao gồm thiết kế mạch tích hợp (ICs) và phát triển phần mềm nhúng. Việc làm chủ công nghệ và tăng cường tính bảo mật đòi hỏi ưu tiên lựa chọn các thiết bị được hỗ trợ bởi các nền tảng phần mềm mã nguồn mở thông dụng, được kiểm định bởi các tổ chức uy tín quốc tế.
2. **Tăng tốc độ và mở rộng băng thông (Speed & Bandwidth):** Khi hàng triệu thiết bị cùng truyền dữ liệu, luồng video giám sát và dịch vụ phản hồi thời gian thực, áp lực về băng thông và độ trễ gia tăng mạnh mẽ trên các máy chủ, cổng định tuyến (Gateway) và bộ thu phát biên.
3. **Tối ưu năng lượng và hiệu suất (Energy Optimization):** Thiết bị IoT thường chạy bằng pin và đặt tại nơi khó tiếp cận. Xu thế thiết kế hiện đại chuyển từ tối ưu hóa rời rạc sang phương pháp thiết kế tích hợp vi mạch - đóng gói - hệ thống (**Chip-Package-System - CPS**), cho phép tối ưu đồng thời xuyên suốt toàn bộ hệ thống, cân bằng điện áp hoạt động thấp với độ tin cậy vận hành.
4. **Kiến trúc Cloud/Edge-based IoT:** Đòi hỏi sự kết hợp chặt chẽ giữa khả năng lưu trữ, tính toán quy mô lớn của điện toán đám mây với khả năng xử lý thời gian thực, bảo vệ quyền riêng tư của điện toán cận biên (Edge Computing).
"""

ch1_vn_extra_text = """
Cụ thể, tại Việt Nam, tỷ lệ người sử dụng Internet/tổng dân số năm 2014 đã đạt 43,8% (cao hơn tỷ lệ trung bình thế giới là 42,2% và châu Á là 34,8%). Cả nước có gần 14.000 doanh nghiệp CNTT với hơn 500.000 lao động. Việt Nam cũng đạt được nhiều bước tiến lớn trong ứng dụng CNTT vào hoạt động quản lý nhà nước và đời sống xã hội: quản lý ngân sách, kho bạc, thuế, hải quan, bảo hiểm xã hội, giáo dục, y tế, giao thông, đất đai, quy hoạch và môi trường.

Đồng chí Nguyễn Thiện Nhân - Nguyên Bí thư Thành ủy Thành phố Hồ Chí Minh từng nhấn mạnh: *“Từ bức tranh của các đô thị Việt Nam, có thể thấy Việt Nam cần phát triển các đô thị theo hướng đô thị thông minh”*. Đô thị thông minh nhằm hướng tới 4 mục tiêu trụ cột:
1. **Hiệu quả kinh tế:** Dự kiến đến năm 2025, diện tích đô thị chiếm khoảng 15% diện tích cả nước, tỷ lệ đô thị hóa khoảng 50% dân số, đóng góp khoảng 75% GDP quốc gia.
2. **Môi trường sống tốt hơn:** Nâng cao chất lượng không khí, quản lý nguồn nước, giảm thiểu ùn tắc và ô nhiễm.
3. **Phục vụ người dân tốt hơn:** Cung cấp dịch vụ công trực tuyến nhanh chóng, minh bạch và tiện ích y tế, giáo dục số.
4. **Người dân tham gia quản trị:** Cho phép người dân tham gia phản ánh, giám sát và quản lý đô thị cùng chính quyền.

Để xây dựng và vận hành thành công một thành phố thông minh bền vững, chính quyền và các đối tác công nghệ cần nhất quán lựa chọn các giải pháp đạt chuẩn Internet of Things mở quốc tế. Việc triển khai các giải pháp IoT phân mảnh và phi tiêu chuẩn (*Non-Standardized*) sẽ khiến các hệ sinh thái không thể kết nối, giao tiếp được với nhau, dẫn đến nguy cơ lãng phí ngân sách và nhân lực. Đô thị thông minh hiện đại là sự hội tụ giữa công nghệ điện toán đám mây (*Cloud Computing*), điện toán cận biên (*Edge Computing*), dữ liệu lớn (*Big Data*) và trí tuệ nhân tạo (*AI*) trên nền tảng các chuẩn mở.
"""

ch1_exercises = """
## Bài tập Chương 1

1. Hãy liệt kê những thiết bị có thể kết nối vào Internet trong thực tế đời sống.
2. Hãy phân tích những đặc điểm kỹ thuật cơ bản của thiết bị phần cứng được sử dụng trong hệ thống IoT.
3. Hãy trình bày những xu thế phát triển chính của IoT trên thế giới và triển vọng tại Việt Nam.
4. Hãy nêu các lợi ích then chốt mà công nghệ IoT mang lại cho các ngành kinh tế - xã hội.
5. Hãy phân tích những thách thức lớn nhất mà IoT đang phải đối mặt hiện nay (bảo mật, năng lượng, tiêu chuẩn hóa).
"""

# --- CHƯƠNG 2: TOÀN BỘ CHƯƠNG 2 TỪ MANUAL ---
ch2_raw = slices['CHƯƠNG 2. CÁC LĨNH VỰC ỨNG DỤNG IOT']
ch2_clean = clean_page_markers(ch2_raw)
ch2_clean = re.sub(r'^#\s+CHƯƠNG 2\..*', '# Chương 2: Các lĩnh vực ứng dụng IoT', ch2_clean)
ch2_intro_toc = """
## Nội dung chương

- **2.1.** Nhà thông minh (Smart Home).
- **2.2.** Đô thị thông minh (Smart City) và Trạm quan trắc môi trường UIT-SmartCity.
- **2.3.** Nông nghiệp thông minh (Smart Agriculture).
- **Bài tập Chương 2.**
"""
ch2_clean = promote_headings_manual(ch2_clean)
ch2_final = ch2_clean.replace('# Chương 2: Các lĩnh vực ứng dụng IoT', '# Chương 2: Các lĩnh vực ứng dụng IoT\n' + ch2_intro_toc)

# --- CHƯƠNG 3: BỔ SUNG TOPO VÀ CÁC BỘ GIAO THỨC CHUYÊN SÂU ---
ch3_raw = slices['CHƯƠNG 3. CÁC KIẾN TRÚC MẠNG VÀ BỘ GIAO THỨC MẠNG IOT']
ch3_clean = clean_page_markers(ch3_raw)

p_topo_start = ch3_clean.find("### 3.1. Các kiến trúc mạng dùng trong IoT")
p_proto_start = ch3_clean.find("### 3.2. Các bộ giao thức mạng không dây thường dùng trong IoT")
p_bt3 = ch3_clean.find("## BÀI TẬP CHƯƠNG 3")

ch3_topologies_raw = ch3_clean[p_topo_start:p_proto_start].strip()
ch3_topologies_converted = ch3_topologies_raw.replace("### 3.1. Các kiến trúc mạng dùng trong IoT", "## 3.7. Các kiến trúc và topo mạng dùng trong IoT")
ch3_topologies_converted = ch3_topologies_converted.replace("#### 3.1.1. Một số kiến trúc mạng đơn giản", "### 3.7.1. Một số kiến trúc mạng đơn giản")
ch3_topologies_converted = ch3_topologies_converted.replace("#### 3.1.2. Một số kiến trúc mạng phức tạp", "### 3.7.2. Một số kiến trúc mạng phức tạp")
ch3_topologies_converted = promote_headings_manual(ch3_topologies_converted)

ch3_protocols_raw = ch3_clean[p_proto_start:p_bt3].strip()
ch3_protocols_converted = ch3_protocols_raw.replace("### 3.2. Các bộ giao thức mạng không dây thường dùng trong IoT\n", "")
ch3_protocols_converted = ch3_protocols_converted.replace("#### 3.2.1. Bộ giao thức 6LoWPAN", "### 3.8.1. Bộ giao thức 6LoWPAN")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.1.1.", "#### 3.8.1.1.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.1.2.", "#### 3.8.1.2.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.1.3.", "#### 3.8.1.3.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.1.4.", "#### 3.8.1.4.")

ch3_protocols_converted = ch3_protocols_converted.replace("#### 3.2.2. Bộ giao thức Zigbee", "### 3.8.2. Bộ giao thức Zigbee")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.2.1.", "#### 3.8.2.1.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.2.2.", "#### 3.8.2.2.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.2.3.", "#### 3.8.2.3.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.2.4.", "#### 3.8.2.4.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.2.5.", "#### 3.8.2.5.")

ch3_protocols_converted = ch3_protocols_converted.replace("#### 3.2.3. Bộ giao thức WiFi 802.11", "### 3.8.3. Bộ giao thức WiFi 802.11")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.3.1.", "#### 3.8.3.1.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.3.2.", "#### 3.8.3.2.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.3.3.", "#### 3.8.3.3.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.3.4.", "#### 3.8.3.4.")
ch3_protocols_converted = ch3_protocols_converted.replace("##### 3.2.3.5.", "#### 3.8.3.5.")

ch3_exercises = clean_page_markers(ch3_clean[p_bt3:].strip())
ch3_exercises = promote_headings_manual(ch3_exercises)

# --- CHƯƠNG 4: HOÀN THIỆN ARDUINO VÀ BỔ SUNG TELOSB, TINYOS, CONTIKI, RASPBIAN, BẢNG SO SÁNH ---
ch4_raw = slices['CHƯƠNG 4. CÁC NỀN TẢNG PHẦN CỨNG VÀ PHẦN MỀM IOT THÔNG DỤNG']
ch4_clean = clean_page_markers(ch4_raw)

arduino_completion = """
- **`//` (single-line comment):** Dùng để ghi chú trên một dòng đơn. Trình biên dịch sẽ bỏ qua tất cả ký tự từ dấu `//` cho đến cuối dòng.
- **`/* ... */` (multi-line comment):** Dùng để ghi chú trên nhiều dòng liên tiếp. Rất hữu ích khi cần giải thích chi tiết khối thuật toán hoặc tạm thời vô hiệu hóa một đoạn mã.
- **`{}` (curly braces):** Cặp dấu ngoặc nhọn dùng để xác định phạm vi của một khối mã lệnh (block of code), ví dụ như thân hàm `setup()`, `loop()`, hoặc khối lệnh sau `if`, `for`, `while`.

#### Các hàm vào/ra cơ bản trong Arduino (Basic I/O Functions)

1. **`pinMode(pin, mode)`:** Cấu hình chân số (digital pin) làm đầu vào (`INPUT`), đầu vào có điện trở kéo lên (`INPUT_PULLUP`), hoặc đầu ra (`OUTPUT`).
2. **`digitalWrite(pin, value)`:** Xuất mức điện áp ra chân số: mức cao `HIGH` (thường là 5V hoặc 3.3V) hoặc mức thấp `LOW` (0V).
3. **`digitalRead(pin)`:** Đọc trạng thái logic từ chân số, trả về `HIGH` hoặc `LOW`.
4. **`analogRead(pin)`:** Đọc giá trị điện áp tương tự từ chân Analog (A0-A5), chuyển đổi qua bộ ADC 10-bit thành giá trị nguyên từ `0` đến `1023`.
5. **`analogWrite(pin, value)`:** Xuất tín hiệu điều chế độ rộng xung (PWM) ra các chân hỗ trợ (~), nhận giá trị từ `0` (luôn tắt) đến `255` (luôn bật).
6. **`delay(ms)`:** Tạm dừng chương trình trong khoảng thời gian xác định tính bằng mili-giây.

#### Giao tiếp nối tiếp qua cổng Serial (Serial Communication)

- **`Serial.begin(speed)`:** Khởi tạo giao tiếp Serial với tốc độ baud (thông dụng: 9600, 115200).
- **`Serial.print()` / `Serial.println()`:** Gửi dữ liệu hoặc chuỗi ký tự lên máy tính để xem trên Serial Monitor.
- **`Serial.available()` / `Serial.read()`:** Kiểm tra và đọc dữ liệu gửi từ máy tính xuống board.

*Ví dụ hoàn chỉnh: Chương trình điều khiển đèn LED chớp tắt (Blink):*

```cpp
// Khai báo hằng số chân cắm LED
const int LED_PIN = 13; // Chân số 13 tích hợp sẵn LED trên board Arduino Uno

void setup() {
  // Cấu hình chân LED_PIN làm ngõ ra (OUTPUT)
  pinMode(LED_PIN, OUTPUT);
  // Khởi động giao tiếp Serial với tốc độ 9600 bps
  Serial.begin(9600);
  Serial.println("Arduino Blink Program Started!");
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // Bật sáng đèn LED
  Serial.println("LED ON");
  delay(1000);                  // Chờ 1 giây (1000 ms)

  digitalWrite(LED_PIN, LOW);  // Tắt đèn LED
  Serial.println("LED OFF");
  delay(1000);                  // Chờ 1 giây
}
```
"""

p_telosb = ch4_clean.find("#### 4.1.2. Thiết bị cảm biến không dây TelosB")
p_arduino_m = ch4_clean.find("#### 4.1.3. Thiết bị nhúng Arduino")
p_b41 = ch4_clean.find("#### 4.1.5. Tổng hợp một số nền tảng phần cứng IoT phổ biến")
p_sw_m = ch4_clean.find("### 4.2. Các nền tảng phần mềm dùng trong IoT")
p_bt4 = ch4_clean.find("## BÀI TẬP CHƯƠNG 4")

telosb_text = ch4_clean[p_telosb:p_arduino_m].strip()
telosb_text = telosb_text.replace("#### 4.1.2. Thiết bị cảm biến không dây TelosB", "## 4.7. Thiết bị cảm biến không dây TelosB")

table_41_text = ch4_clean[p_b41:p_sw_m].strip()
table_41_text = promote_headings_manual(table_41_text)

os_section_raw = ch4_clean[p_sw_m:p_bt4].strip()
os_section_converted = os_section_raw.replace("### 4.2. Các nền tảng phần mềm dùng trong IoT\n", "")
os_section_converted = os_section_converted.replace("#### 4.2.1. Những đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT", "## 4.8. Đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT")
os_section_converted = os_section_converted.replace("#### 4.2.2. Hệ điều hành TinyOS", "## 4.9. Hệ điều hành TinyOS")
os_section_converted = os_section_converted.replace("##### 4.2.2.1.", "### 4.9.1.")
os_section_converted = os_section_converted.replace("##### 4.2.2.2.", "### 4.9.2.")
os_section_converted = os_section_converted.replace("#### 4.2.3. Hệ điều hành Contiki", "## 4.10. Hệ điều hành Contiki")
os_section_converted = os_section_converted.replace("##### 4.2.3.1.", "### 4.10.1.")
os_section_converted = os_section_converted.replace("##### 4.2.3.2.", "### 4.10.2.")
os_section_converted = os_section_converted.replace("#### 4.2.4. Hệ điều hành Raspbian OS", "## 4.11. Hệ điều hành Raspbian OS")
os_section_converted = os_section_converted.replace("#### 4.2.5. Tổng hợp một số nền tảng phần mềm IoT phổ biến", "## 4.12. Bảng tổng hợp so sánh các hệ điều hành IoT phổ biến")
os_section_converted = promote_headings_manual(os_section_converted)

ch4_exercises = clean_page_markers(ch4_clean[p_bt4:].strip())
ch4_exercises = promote_headings_manual(ch4_exercises)

# --- CHƯƠNG 5: TOÀN BỘ CHƯƠNG 5 ---
ch5_raw = slices['CHƯƠNG 5. ĐIỆN TOÁN ĐÁM MÂY, ĐIỆN TOÁN CẬN BIÊN VÀ IOT']
ch5_clean = clean_page_markers(ch5_raw)
ch5_clean = re.sub(r'^#\s+CHƯƠNG 5\..*', '# Chương 5: Điện toán đám mây, điện toán cận biên và IoT', ch5_clean)
ch5_intro_toc = """
## Nội dung chương

- **5.1.** Kiến trúc tổng quan hệ thống IoT tích hợp điện toán đám mây và điện toán cận biên.
- **5.2.** Nền tảng điện toán đám mây và ứng dụng trong IoT (Mô hình dịch vụ, OpenStack và Docker).
- **5.3.** Nền tảng điện toán cận biên (Edge Computing) và ứng dụng trong IoT.
- **5.4.** Các vấn đề tồn tại và hướng nghiên cứu trong tương lai.
- **Bài tập Chương 5.**
"""
ch5_clean = promote_headings_manual(ch5_clean)
ch5_final = ch5_clean.replace('# Chương 5: Điện toán đám mây, điện toán cận biên và IoT', '# Chương 5: Điện toán đám mây, điện toán cận biên và IoT\n' + ch5_intro_toc)

# --- CHƯƠNG 6: TOÀN BỘ CHƯƠNG 6 ---
ch6_raw = slices['CHƯƠNG 6. QUẢN LÝ NGỮ CẢNH THÔNG MINH VÀ TRÍ TUỆ NHÂN TẠO TRONG IOT']
ch6_clean = clean_page_markers(ch6_raw)
ch6_clean = re.sub(r'^#\s+CHƯƠNG 6\..*', '# Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT', ch6_clean)
ch6_intro_toc = """
## Nội dung chương

- **6.1.** Ngữ cảnh và thích ứng ngữ cảnh trong IoT.
- **6.2.** Quản lý ngữ cảnh trong IoT (Vòng đời 4 giai đoạn).
- **6.3.** Các kỹ thuật mô hình hóa ngữ cảnh.
- **6.4.** Các kỹ thuật suy luận ngữ cảnh (Rule-based, Fuzzy Logic kiểm soát vi khí hậu nhà kính, Ontology, CBR).
- **6.5.** Trí tuệ nhân tạo và Machine Learning trong IoT.
- **Bài tập Chương 6.**
"""
ch6_clean = promote_headings_manual(ch6_clean)
ch6_final = ch6_clean.replace('# Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT', '# Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT\n' + ch6_intro_toc)

# --- CHƯƠNG 7: TOÀN BỘ CHƯƠNG 7 ---
ch7_raw = slices['CHƯƠNG 7. TÁI CẤU HÌNH TRONG IOT']
ch7_clean = clean_page_markers(ch7_raw)
ch7_clean = re.sub(r'^#\s+CHƯƠNG 7\..*', '# Chương 7: Tái cấu hình trong IoT', ch7_clean)
ch7_intro_toc = """
## Nội dung chương

- **7.1.** Tổng quan về tái cấu hình trong IoT.
- **7.2.** Các hướng tiếp cận trong tái cấu hình IoT (5 hướng tiếp cận cốt lõi).
- **7.3.** Một số giải pháp hiện thực tái cấu hình trên các loại thiết bị phổ biến (Deluge OTA, ESP8266 OTA, Mender/Docker).
- **7.4.** Khung kiến trúc giải pháp tái cấu hình IoT đa nền tảng dựa trên SDN (SD-IoTR).
- **7.5.** Ứng dụng của chức năng tái cấu hình và các định hướng nghiên cứu.
- **Bài tập Chương 7.**
"""
ch7_clean = promote_headings_manual(ch7_clean)
ch7_final = ch7_clean.replace('# Chương 7: Tái cấu hình trong IoT', '# Chương 7: Tái cấu hình trong IoT\n' + ch7_intro_toc)

# --- PHẦN KẾT: KẾT LUẬN, TÀI LIỆU THAM KHẢO, THÔNG TIN XUẤT BẢN ---
conclusion_clean = promote_headings_manual(clean_page_markers(slices['KẾT LUẬN']))
conclusion_clean = re.sub(r'^#\s+KẾT LUẬN.*', '# Kết luận', conclusion_clean)

references_clean = promote_headings_manual(clean_page_markers(slices['TÀI LIỆU THAM KHẢO']))
references_clean = re.sub(r'^#\s+TÀI LIỆU THAM KHẢO.*', '# Tài liệu tham khảo', references_clean)

pub_info_clean = promote_headings_manual(clean_page_markers(slices['THÔNG TIN XUẤT BẢN']))
pub_info_clean = re.sub(r'^#\s+THÔNG TIN XUẤT BẢN.*', '# Thông tin xuất bản', pub_info_clean)

# ==============================================================================
# BÂY GIỜ LẮP GHÉP CÙNG NỘI DUNG NGUYÊN VĂN CỦA IOTMAIN.MD
# ==============================================================================

iotmain_lines = iotmain_content.splitlines(True)

# 1. Front Matter: Mục lục cập nhật + Thông tin học phần + Ký hiệu viết tắt
new_toc = """# Mục lục môn học

1. [Chương 1: Giới thiệu](#chương-1-giới-thiệu)
2. [Chương 2: Các lĩnh vực ứng dụng IoT](#chương-2-các-lĩnh-vực-ứng-dụng-iot)
3. [Chương 3: Các kiến trúc mạng và bộ giao thức mạng IoT](#chương-3-các-kiến-trúc-mạng-và-bộ-giao-thức-mạng-iot)
4. [Chương 4: Các nền tảng phần cứng và phần mềm IoT thông dụng](#chương-4-các-nền-tảng-phần-cứng-và-phần-mềm-iot-thông-dụng)
5. [Chương 5: Điện toán đám mây, điện toán cận biên và IoT](#chương-5-điện-toán-đám-mây-điện-toán-cận-biên-và-iot)
6. [Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT](#chương-6-quản-lý-ngữ-cảnh-thông-minh-và-trí-tuệ-nhân-tạo-trong-iot)
7. [Chương 7: Tái cấu hình trong IoT](#chương-7-tái-cấu-hình-trong-iot)
8. [Kết luận](#kết-luận)
9. [Tài liệu tham khảo](#tài-liệu-tham-khảo)
10. [Thông tin xuất bản](#thông-tin-xuất-bản)

"""
front_matter_rest = "".join(iotmain_lines[10:43]) # Lines 11 to 43 (Thông tin học phần, Ký hiệu viết tắt)

# 2. Chương 1: Giữ nguyên văn lines 44-431 của IoTmain.md + ch1_vn_extra_text + ch1_standards_and_challenges + ch1_exercises
ch1_orig = "".join(iotmain_lines[43:431])
ch1_full = ch1_orig.rstrip() + "\n\n" + ch1_vn_extra_text.strip() + "\n\n" + ch1_standards_and_challenges.strip() + "\n\n" + ch1_exercises.strip() + "\n\n"

# 3. Chương 2: Toàn bộ Chương 2
ch2_full = ch2_final.strip() + "\n\n"

# 4. Chương 3:
# Lines 432 đến 610 của IoTmain.md (Chương 3 header, 3.1 đến 3.6)
ch3_part1 = "".join(iotmain_lines[431:610]) # From "# Chương 3: Các kiến trúc mạng và bộ giao thức IoT" up to 3.6
ch3_part1 = ch3_part1.replace("# Chương 3: Các kiến trúc mạng và bộ giao thức IoT", "# Chương 3: Các kiến trúc mạng và bộ giao thức mạng IoT\n\n## Nội dung chương\n\n- **3.1.** Mô hình kết nối hệ thống mở (OSI Model).\n- **3.2.** Bộ giao thức TCP/IP.\n- **3.3.** Đặc tính hiệu năng mạng IoT (Key Performance Characteristics).\n- **3.4.** Bộ giao thức Internet (Internet Protocol Suite).\n- **3.5.** Các loại mạng truyền thông (Network Types).\n- **3.6.** Khả năng sẵn sàng của mạng (Network Reachability).\n- **3.7.** Các kiến trúc và topo mạng dùng trong IoT.\n- **3.8.** Các bộ giao thức mạng không dây thường dùng trong IoT (6LoWPAN, Zigbee, WiFi, BLE, LPWAN).\n- **3.9.** Cảm biến trong IoT (IoT Sensors).\n- **3.10.** Công nghệ nhận dạng vô tuyến RFID.\n- **3.11.** Giám sát bằng video (Video Tracking).\n- **3.12.** Cơ cấu chấp hành trong IoT (IoT Actuators).\n- **Bài tập Chương 3.**\n")

# 3.7 Topo mạng từ manual
ch3_topo_block = ch3_topologies_converted.strip() + "\n\n"

# 3.8 Bộ giao thức không dây:
ch3_proto_overview = "".join(iotmain_lines[610:661]).strip()
ch3_proto_overview = ch3_proto_overview.replace("## 3.7: Các bộ giao thức mạng không dây thường dùng trong IoT", "## 3.8. Các bộ giao thức mạng không dây thường dùng trong IoT\n\n### 3.8.0. Tổng quan các chuẩn mạng không dây trong IoT")

ch3_proto_detailed = ch3_protocols_converted.strip()

# Các phần cảm biến, RFID, Video Tracking, Actuators từ lines 662-734 của IoTmain.md
ch3_sensors_actuators = "".join(iotmain_lines[661:734]).strip()
ch3_sensors_actuators = ch3_sensors_actuators.replace("## 3.8: IoT Sensors (*Cảm biến IoT*)", "## 3.9. Cảm biến trong IoT (IoT Sensors)")
ch3_sensors_actuators = ch3_sensors_actuators.replace("## 3.9: RFID", "## 3.10. Công nghệ nhận dạng vô tuyến RFID")
ch3_sensors_actuators = ch3_sensors_actuators.replace("## 3.10: Video Tracking", "## 3.11. Giám sát bằng video (Video Tracking)")
ch3_sensors_actuators = ch3_sensors_actuators.replace("## 3.11: IoT Actuators", "## 3.12. Cơ cấu chấp hành trong IoT (IoT Actuators)")

ch3_full = ch3_part1.rstrip() + "\n\n" + ch3_topo_block + ch3_proto_overview + "\n\n" + ch3_proto_detailed + "\n\n" + ch3_sensors_actuators + "\n\n" + ch3_exercises.strip() + "\n\n"

# 5. Chương 4:
ch4_part1 = "".join(iotmain_lines[734:1099]).rstrip()
# Cập nhật mục lục nội dung chương 4
ch4_old_toc = """## Nội dung chương

- **4.1.** Mạng cảm biến không dây (Wireless Sensor Networks - WSN)
- **4.2.** Phân loại mạng cảm biến không dây (Class of Wireless Sensor Networks)
- **4.3.** Vai trò của mã nguồn mở trong IoT (The Role of Open Source in IoT)
- **4.4.** Các nền tảng phần cứng (Hardware Platforms)
- **4.5.** Các nền tảng phần mềm (Software Platforms)
- **4.6.** Ngôn ngữ lập trình Arduino (Arduino Programming Language)"""

ch4_new_toc = """## Nội dung chương

- **4.1.** Mạng cảm biến không dây (Wireless Sensor Networks - WSN).
- **4.2.** Phân loại mạng cảm biến không dây (Class of Wireless Sensor Networks).
- **4.3.** Vai trò của mã nguồn mở trong IoT (The Role of Open Source in IoT).
- **4.4.** Các nền tảng phần cứng (Hardware Platforms).
- **4.5.** Các nền tảng phần mềm (Software Platforms).
- **4.6.** Ngôn ngữ lập trình Arduino (Arduino Programming Language).
- **4.7.** Thiết bị cảm biến không dây TelosB và So sánh các nền tảng phần cứng IoT.
- **4.8.** Đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT.
- **4.9.** Hệ điều hành TinyOS.
- **4.10.** Hệ điều hành Contiki.
- **4.11.** Hệ điều hành Raspbian OS.
- **4.12.** Bảng tổng hợp so sánh các hệ điều hành IoT phổ biến.
- **Bài tập Chương 4.**"""

ch4_part1 = ch4_part1.replace(ch4_old_toc, ch4_new_toc)

ch4_arduino_finish = arduino_completion.strip()
ch4_telosb = telosb_text.strip()
ch4_table41 = table_41_text.strip()
ch4_os = os_section_converted.strip()
ch4_bt = ch4_exercises.strip()

ch4_full = (
    ch4_part1 + "\n\n" +
    ch4_arduino_finish + "\n\n" +
    ch4_telosb + "\n\n" +
    ch4_table41 + "\n\n" +
    ch4_os + "\n\n" +
    ch4_bt + "\n\n"
)

# 6. Chương 5:
ch5_full = ch5_final.strip() + "\n\n"

# 7. Chương 6:
ch6_full = ch6_final.strip() + "\n\n"

# 8. Chương 7:
ch7_full = ch7_final.strip() + "\n\n"

# 9. Phần kết
end_matter = (
    conclusion_clean.strip() + "\n\n" +
    references_clean.strip() + "\n\n" +
    pub_info_clean.strip() + "\n"
)

# Ghép toàn bộ thành 1 QUYỂN DUY NHẤT
unified_book = (
    new_toc +
    front_matter_rest.strip() + "\n\n" +
    ch1_full +
    ch2_full +
    ch3_full +
    ch4_full +
    ch5_full +
    ch6_full +
    ch7_full +
    end_matter
)

print(f"Tổng số ký tự của quyển sách hợp nhất: {len(unified_book):,}")
print(f"Tổng số dòng của quyển sách hợp nhất: {len(unified_book.splitlines()):,}")

# Ghi trực tiếp ra IoTmain.md
target_path = r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(unified_book)

print("Đã ghi thành công toàn bộ quyển giáo trình hợp nhất vào IoTmain.md!")
