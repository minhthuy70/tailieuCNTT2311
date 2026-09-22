# Kế hoạch thực hành môn Phát triển ứng dụng IoT (TT188)

## 1. Thông tin chung

- **Môn học:** Phát triển ứng dụng IoT (IoT Application Development)
- **Mã học phần:** TT188
- **Thời lượng:** 03 tín chỉ
- **Lý thuyết:** 30 tiết
- **Thực hành:** 30 tiết
- **Mục tiêu thực hành:** Từ việc làm quen phần cứng, cảm biến và giao tiếp mạng đến xây dựng một hệ thống IoT hoàn chỉnh có thu thập dữ liệu, truyền dữ liệu, xử lý và điều khiển.

---

# 2. Lộ trình thực hành tổng thể

| Buổi | Chủ đề | Nội dung chính | Kết quả cần đạt |
|---|---|---|---|
| 1 | Làm quen hệ thống IoT | Kiến trúc IoT, phần cứng, GPIO, môi trường lập trình | Hiểu và chạy được chương trình IoT đầu tiên |
| 2 | GPIO và thiết bị đầu ra | LED, Button, Buzzer | Điều khiển thiết bị bằng GPIO |
| 3 | Cảm biến cơ bản | DHT11/DHT22, đọc nhiệt độ và độ ẩm | Thu thập dữ liệu cảm biến |
| 4 | Cảm biến ánh sáng/chuyển động | LDR, PIR | Phát hiện trạng thái môi trường |
| 5 | Arduino và giao tiếp cảm biến | Serial, I2C, SPI | Kết nối nhiều thiết bị/cảm biến |
| 6 | Raspberry Pi | GPIO, Python, Linux/Raspbian | Điều khiển phần cứng bằng Raspberry Pi |
| 7 | Kết nối Wi-Fi | ESP32/Raspberry Pi, TCP/IP cơ bản | Thiết bị kết nối Internet |
| 8 | MQTT | Broker, Publisher, Subscriber, Topic | Gửi/nhận dữ liệu IoT qua MQTT |
| 9 | HTTP/REST API | GET, POST, JSON | Gửi dữ liệu cảm biến lên server |
| 10 | Lưu trữ và trực quan hóa | Database, dashboard | Lưu và theo dõi dữ liệu |
| 11 | Edge Computing | Xử lý dữ liệu tại thiết bị | Giảm dữ liệu truyền lên server |
| 12 | IoT + AI/ML cơ bản | Phân loại/dự đoán dữ liệu cảm biến | Hiểu quy trình AI trong IoT |
| 13 | Điều khiển và tự động hóa | Rule, threshold, actuator | Hệ thống tự động phản ứng |
| 14 | OTA và bảo mật cơ bản | Firmware update, authentication | Hiểu quản lý thiết bị từ xa |
| 15 | Đồ án IoT | Tích hợp toàn bộ hệ thống | Hoàn thành prototype và báo cáo |

> Có thể điều chỉnh số lượng buổi tùy thời khóa biểu thực tế. Tổng thời lượng thực hành mục tiêu là **30 tiết**, tương đương khoảng **15 buổi × 2 tiết**.

---

# 3. Giai đoạn 1 – Làm quen IoT và phần cứng

## Buổi 1 – Tổng quan hệ thống IoT và môi trường thực hành

### Mục tiêu

Hiểu luồng hoạt động cơ bản:

**Sensor → Microcontroller → Network → Server/Cloud → Application**

### Nội dung

- Nhận diện các thành phần trong hệ thống IoT.
- Phân biệt:
  - Sensor
  - Actuator
  - Microcontroller
  - Gateway
  - Server/Cloud
- Làm quen Arduino/ESP32 hoặc Raspberry Pi.
- Cài đặt Arduino IDE hoặc môi trường Python.
- Kiểm tra kết nối thiết bị với máy tính.

### Bài thực hành

- Kết nối board với máy tính.
- Nạp chương trình mẫu.
- In thông tin ra Serial Monitor.

### Sản phẩm

- Board hoạt động.
- Ảnh kết quả chạy chương trình.
- Source code bài thực hành.

---

## Buổi 2 – GPIO, LED, Button và Buzzer

### Mục tiêu

Hiểu cách đọc và điều khiển tín hiệu số.

### Nội dung

- GPIO Input/Output.
- Digital HIGH/LOW.
- Debounce button.
- Điều khiển LED.
- Điều khiển buzzer.

### Bài thực hành

Thiết kế hệ thống:

**Button → Microcontroller → LED + Buzzer**

Khi nhấn Button:

- LED bật.
- Buzzer phát âm thanh.
- Khi thả Button, thiết bị trở về trạng thái ban đầu.

### Bài mở rộng

- Nhấn Button lần 1: bật LED.
- Nhấn Button lần 2: tắt LED.
- Đếm số lần nhấn.

---

# 4. Giai đoạn 2 – Thu thập dữ liệu cảm biến

## Buổi 3 – Cảm biến nhiệt độ và độ ẩm

### Mục tiêu

Đọc dữ liệu môi trường từ cảm biến.

### Thiết bị

- DHT11 hoặc DHT22.
- Arduino/ESP32/Raspberry Pi.

### Nội dung

- Kết nối DHT.
- Đọc nhiệt độ.
- Đọc độ ẩm.
- Kiểm tra dữ liệu lỗi.
- Hiển thị dữ liệu trên Serial Monitor.

### Bài thực hành

Đọc dữ liệu mỗi 2 giây:

```text
Temperature: 29.5 °C
Humidity: 72 %
```

### Bài mở rộng

Đặt ngưỡng:

```text
Temperature > 35°C
→ bật buzzer
```

---

## Buổi 4 – Cảm biến ánh sáng và chuyển động

### Thiết bị

- LDR.
- PIR.
- LED/Buzzer.

### Nội dung

- Đọc giá trị ánh sáng.
- Phát hiện chuyển động.
- Kết hợp nhiều cảm biến.

### Bài thực hành

Xây dựng hệ thống:

**LDR + PIR → Controller → LED/Buzzer**

Ví dụ:

```text
Nếu trời tối và phát hiện chuyển động
→ bật đèn.
```

### Kết quả

Sinh viên hiểu cách kết hợp dữ liệu từ nhiều cảm biến để tạo ra một hành động.

---

## Buổi 5 – Giao tiếp giữa các thiết bị

### Mục tiêu

Làm quen với các giao tiếp phần cứng thường gặp.

### Nội dung

- UART/Serial.
- I2C.
- SPI.
- Địa chỉ thiết bị I2C.
- Đọc dữ liệu từ nhiều thiết bị.

### Bài thực hành

Kết nối:

```text
Microcontroller
 ├── DHT11
 ├── OLED
 └── Sensor khác
```

Hiển thị dữ liệu cảm biến trên OLED.

---

# 5. Giai đoạn 3 – Raspberry Pi và kết nối Internet

## Buổi 6 – Raspberry Pi và Linux

### Mục tiêu

Làm quen với Raspberry Pi như một IoT Gateway/Edge Device.

### Nội dung

- Raspbian/Raspberry Pi OS.
- Linux command line.
- GPIO trên Raspberry Pi.
- Python GPIO.
- Chạy Python script.

### Bài thực hành

Điều khiển LED bằng Python.

Sau đó đọc cảm biến và hiển thị dữ liệu.

### Bài mở rộng

Thiết lập chương trình chạy tự động khi Raspberry Pi khởi động.

---

## Buổi 7 – Kết nối mạng Wi-Fi

### Mục tiêu

Đưa thiết bị IoT lên mạng.

### Nội dung

- IPv4 cơ bản.
- IP address.
- Gateway.
- DNS.
- Wi-Fi.
- TCP/IP ở mức khái niệm.
- Kiểm tra kết nối bằng ping.

### Bài thực hành

Thiết bị:

```text
Sensor
   ↓
ESP32/Raspberry Pi
   ↓
Wi-Fi
   ↓
Local Network
```

Kiểm tra thiết bị có thể giao tiếp với máy tính/server.

---

# 6. Giai đoạn 4 – Giao thức truyền thông IoT

## Buổi 8 – MQTT

### Mục tiêu

Hiểu và triển khai mô hình Publish/Subscribe.

### Kiến trúc

```text
Sensor Device
      |
   Publish
      |
      v
   MQTT Broker
      |
   Subscribe
      |
      v
 Dashboard/Application
```

### Nội dung

- MQTT Broker.
- Publisher.
- Subscriber.
- Topic.
- Message.
- QoS.

### Bài thực hành

Tạo topic:

```text
iot/device01/temperature
iot/device01/humidity
```

Thiết bị publish dữ liệu.

Máy tính hoặc Raspberry Pi subscribe dữ liệu.

### Bài mở rộng

Tạo topic điều khiển:

```text
iot/device01/led
```

Gửi:

```text
ON
OFF
```

để điều khiển LED từ xa.

---

## Buổi 9 – HTTP và REST API

### Mục tiêu

Hiểu cách thiết bị IoT gửi dữ liệu đến backend.

### Nội dung

- HTTP.
- GET.
- POST.
- JSON.
- REST API.
- Request/Response.

### Bài thực hành

Thiết bị gửi:

```json
{
  "deviceId": "device01",
  "temperature": 29.5,
  "humidity": 72
}
```

đến server.

### Bài mở rộng

Server trả về trạng thái điều khiển:

```json
{
  "led": true
}
```

Thiết bị đọc response và điều khiển LED.

---

# 7. Giai đoạn 5 – Backend, Database và Dashboard

## Buổi 10 – Lưu trữ dữ liệu IoT

### Mục tiêu

Xây dựng pipeline:

```text
Sensor
→ Device
→ Network
→ Backend
→ Database
```

### Nội dung

- Thiết kế bảng dữ liệu.
- Timestamp.
- Device ID.
- Sensor value.
- Query dữ liệu.
- Lưu lịch sử dữ liệu.

### Ví dụ dữ liệu

| device_id | sensor | value | timestamp |
|---|---|---:|---|
| device01 | temperature | 29.5 | 10:00 |
| device01 | humidity | 72 | 10:00 |

### Bài thực hành

Lưu dữ liệu cảm biến vào database.

---

## Buổi 11 – Dashboard giám sát

### Mục tiêu

Trực quan hóa dữ liệu IoT.

### Dashboard cần có

- Nhiệt độ hiện tại.
- Độ ẩm hiện tại.
- Trạng thái thiết bị.
- Biểu đồ theo thời gian.
- Lịch sử dữ liệu.

### Luồng

```text
Sensor
→ MQTT/HTTP
→ Backend
→ Database
→ Dashboard
```

### Sản phẩm

Một dashboard có thể theo dõi dữ liệu theo thời gian thực hoặc gần thời gian thực.

---

# 8. Giai đoạn 6 – Edge Computing và AI/ML

## Buổi 12 – Edge Computing

### Mục tiêu

Hiểu tại sao không phải toàn bộ dữ liệu đều cần gửi lên Cloud.

### Ví dụ

Thay vì gửi liên tục:

```text
Sensor → Cloud
```

có thể xử lý tại Edge:

```text
Sensor
   ↓
Edge Device
   ↓
Phân tích
   ↓
Chỉ gửi dữ liệu quan trọng
```

### Bài thực hành

Thiết lập quy tắc:

```text
Nếu nhiệt độ < 35°C
→ chỉ ghi nhận dữ liệu.

Nếu nhiệt độ >= 35°C
→ gửi cảnh báo lên server.
```

### Kết quả

Sinh viên hiểu khái niệm giảm độ trễ và giảm lượng dữ liệu truyền qua mạng.

---

## Buổi 13 – AI/ML cơ bản trong IoT

### Mục tiêu

Hiểu cách AI/ML có thể được tích hợp vào hệ thống IoT.

### Nội dung

- Dataset cảm biến.
- Feature.
- Label.
- Training.
- Prediction.
- Classification/Regression.

### Bài thực hành đề xuất

Dùng dữ liệu:

```text
Temperature
Humidity
Light
```

để phân loại trạng thái:

```text
Normal
Warning
Danger
```

### Quy trình

```text
Sensor Data
     ↓
Data Collection
     ↓
Preprocessing
     ↓
ML Model
     ↓
Prediction
     ↓
IoT Action
```

> Bài này tập trung vào quy trình tích hợp AI/ML với IoT, không yêu cầu xây dựng mô hình quá phức tạp.

---

# 9. Giai đoạn 7 – Tự động hóa, OTA và bảo mật

## Buổi 14 – Điều khiển tự động và OTA

### Phần A – Tự động hóa

Xây dựng rule:

```text
IF temperature > threshold
THEN turn_on_fan
```

Hoặc:

```text
IF motion_detected AND light_level < threshold
THEN turn_on_light
```

### Phần B – OTA/Firmware Update

Tìm hiểu:

- Firmware.
- Firmware version.
- Remote update.
- OTA.
- Rollback ở mức khái niệm.

### Bài thực hành

Thiết kế quy trình:

```text
Device
   ↓
Check version
   ↓
Download firmware
   ↓
Update
   ↓
Restart
   ↓
Verify
```

---

# 10. Giai đoạn 8 – Đồ án IoT

## Buổi 15 – Tích hợp hệ thống

Sinh viên lựa chọn một bài toán thực tế.

### Đề tài 1 – Giám sát ao nuôi tôm

### Thiết bị

- Temperature sensor.
- Water quality sensor nếu có.
- ESP32/Raspberry Pi.
- Buzzer.
- Relay/Actuator.

### Chức năng

- Đo nhiệt độ.
- Theo dõi chất lượng nước.
- Gửi dữ liệu lên server.
- Cảnh báo khi vượt ngưỡng.
- Dashboard theo dõi.

### Kiến trúc

```text
Sensors
   ↓
ESP32
   ↓
Wi-Fi
   ↓
MQTT/HTTP
   ↓
Backend
   ↓
Database
   ↓
Dashboard
```

---

## Đề tài 2 – Bãi đỗ xe thông minh

### Thiết bị

- Ultrasonic sensor.
- ESP32/Arduino.
- LED.
- Servo nếu cần mô phỏng barrier.

### Chức năng

- Phát hiện vị trí trống.
- Xác định vị trí có xe.
- Hiển thị số chỗ trống.
- Gửi dữ liệu lên server.
- Dashboard quản lý.

### Kiến trúc

```text
Ultrasonic Sensors
        ↓
      ESP32
        ↓
       Wi-Fi
        ↓
      Backend
        ↓
    Database
        ↓
    Dashboard
```

---

## Đề tài 3 – Giám sát chất lượng không khí

### Thiết bị

- Temperature/Humidity sensor.
- Gas/Air Quality sensor.
- ESP32/Raspberry Pi.
- OLED.
- Buzzer.

### Chức năng

- Đo nhiệt độ.
- Đo độ ẩm.
- Đo chỉ số chất lượng không khí theo cảm biến sử dụng.
- Cảnh báo.
- Lưu lịch sử.
- Dashboard.

---

# 11. Yêu cầu đầu ra của đồ án

Mỗi nhóm cần hoàn thành:

### Phần cứng

- Sơ đồ kết nối.
- Danh sách thiết bị.
- Prototype hoạt động.
- Hình ảnh mạch thực tế.

### Phần mềm

- Source code firmware.
- Backend/API nếu có.
- Database.
- Dashboard.
- Cấu hình MQTT/HTTP.

### Tài liệu

- Mô tả bài toán.
- Kiến trúc hệ thống.
- Sơ đồ hoạt động.
- Sơ đồ kết nối.
- Thiết kế database.
- Mô tả giao tiếp.
- Kết quả thực nghiệm.
- Hạn chế.
- Hướng phát triển.

---

# 12. Checklist kỹ năng sau khi hoàn thành môn học

## Phần cứng

- [ ] Hiểu GPIO.
- [ ] Đọc được dữ liệu cảm biến.
- [ ] Điều khiển được actuator.
- [ ] Sử dụng được Arduino/ESP32.
- [ ] Có thể sử dụng Raspberry Pi ở mức cơ bản.
- [ ] Biết UART/I2C/SPI ở mức thực hành.

## Network

- [ ] Hiểu IP và Wi-Fi.
- [ ] Hiểu MQTT.
- [ ] Hiểu Publisher/Subscriber.
- [ ] Hiểu HTTP/REST.
- [ ] Gửi được JSON.
- [ ] Kết nối thiết bị với backend.

## Backend và dữ liệu

- [ ] Lưu dữ liệu cảm biến.
- [ ] Truy vấn dữ liệu.
- [ ] Xây dựng API cơ bản.
- [ ] Hiển thị dữ liệu trên dashboard.

## IoT nâng cao

- [ ] Hiểu Cloud Computing.
- [ ] Hiểu Edge Computing.
- [ ] Hiểu Context-awareness.
- [ ] Biết vị trí của AI/ML trong IoT.
- [ ] Hiểu OTA.
- [ ] Biết các vấn đề bảo mật cơ bản của IoT.

## Project

- [ ] Phân tích bài toán thực tế.
- [ ] Thiết kế kiến trúc IoT.
- [ ] Chọn sensor/actuator.
- [ ] Thiết kế giao tiếp.
- [ ] Xây dựng prototype.
- [ ] Thu thập dữ liệu.
- [ ] Lưu trữ dữ liệu.
- [ ] Xây dựng dashboard.
- [ ] Kiểm thử.
- [ ] Viết báo cáo.
- [ ] Demo hệ thống.

---

# 13. Kiến trúc hệ thống mục tiêu

Sau khi hoàn thành toàn bộ lộ trình, sinh viên hướng tới việc có thể tự xây dựng pipeline:

```text
┌──────────────────────────────┐
│        SENSOR LAYER          │
│ Temperature / Humidity / PIR │
│ Light / Air Quality / ...    │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       DEVICE LAYER           │
│ Arduino / ESP32 / RaspberryPi│
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       NETWORK LAYER          │
│ Wi-Fi / MQTT / HTTP          │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│     EDGE / CLOUD LAYER       │
│ Processing / API / Database  │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│      APPLICATION LAYER       │
│ Dashboard / Alert / Control  │
└──────────────────────────────┘
```

---

# 14. Cách học đề xuất cho mỗi bài thực hành

Mỗi bài nên được thực hiện theo 5 bước:

```text
1. Hiểu lý thuyết
        ↓
2. Lắp mạch
        ↓
3. Lập trình
        ↓
4. Kiểm thử
        ↓
5. Ghi lại kết quả
```

Sau mỗi buổi nên lưu:

```text
iot-lab/
├── lab01/
│   ├── README.md
│   ├── src/
│   ├── circuit/
│   └── result/
├── lab02/
├── lab03/
├── ...
└── project/
    ├── hardware/
    ├── firmware/
    ├── backend/
    ├── dashboard/
    ├── database/
    ├── docs/
    └── README.md
```

---

# 15. Mục tiêu cuối khóa

Hoàn thành lộ trình, sinh viên có thể:

**Thiết kế → Lắp đặt → Lập trình → Kết nối → Thu thập dữ liệu → Xử lý → Lưu trữ → Trực quan hóa → Điều khiển → Đánh giá**

một hệ thống IoT hoàn chỉnh.

Trọng tâm của quá trình thực hành là chuyển từ:

```text
"Biết IoT là gì"
```

sang:

```text
"Có thể tự xây dựng một prototype IoT hoạt động được
và giải thích được kiến trúc, giao tiếp, dữ liệu
và cách hệ thống vận hành."
```
