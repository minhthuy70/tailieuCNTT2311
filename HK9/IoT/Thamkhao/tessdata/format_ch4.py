# -*- coding: utf-8 -*-
import sys, re

p = {}

p[83] = """# CHƯƠNG 4. CÁC NỀN TẢNG PHẦN CỨNG VÀ PHẦN MỀM IOT THÔNG DỤNG

Công nghệ IoT được phát triển để phục vụ cho nhiều lĩnh vực khác nhau trong cuộc sống, từ nông nghiệp, công nghiệp, y tế, giáo dục cho đến quản lý đô thị. Để xây dựng nên một hệ thống IoT hoàn chỉnh, các nhà phát triển cần phải kết hợp chặt chẽ giữa các nền tảng phần cứng và các nền tảng phần mềm phù hợp.

Mỗi ứng dụng IoT có những yêu cầu rất khác nhau về kích thước thiết bị, nguồn năng lượng cung cấp, năng lực tính toán, dung lượng bộ nhớ, khả năng kết nối mạng và độ trễ xử lý. Do đó, việc hiểu rõ các đặc tính kỹ thuật, ưu nhược điểm của các loại phần cứng cũng như các hệ điều hành chuyên dụng cho IoT là kiến thức nền tảng quan trọng giúp thiết kế và triển khai các hệ thống IoT hoạt động ổn định, hiệu quả và tối ưu chi phí.

Nội dung chương này trình bày tổng quan về các nền tảng phần cứng và phần mềm phổ biến trong IoT. Về phần cứng, chương này giới thiệu từ các mote cảm biến công suất siêu thấp (TelosB), các vi điều khiển mã nguồn mở thông dụng (Arduino, ESP8266, ESP32) cho đến các máy tính nhúng mạnh mẽ (Raspberry Pi). Về phần mềm, chương này phân tích kiến trúc và cơ chế hoạt động của các hệ điều hành mạng cảm biến nhúng chuyên dụng như TinyOS, Contiki cũng như hệ điều hành Linux nhúng đa năng Raspbian OS trên Raspberry Pi."""

p[84] = """Thông qua những nội dung được trình bày trong chương này, người đọc có cái nhìn tổng quan về các loại thiết bị phần cứng dùng trong IoT cũng như các giải pháp phần mềm tương ứng. Từ đó, trước nhu cầu triển khai một giải pháp IoT trong một ngữ cảnh cụ thể, với các yêu cầu cụ thể, nhà phát triển có thể chọn lựa một loại thiết bị, một môi trường phát triển ứng dụng phù hợp nhất.

### 4.1. Các nền tảng phần cứng

#### 4.1.1. Những đặc trưng và phân loại các nền tảng phần cứng dùng cho IoT

Trong hệ thống IoT, "Vạn vật" (Things) đề cập đến một tập hợp phong phú và đa dạng các đối tượng vật lý được gắn các cảm biến, cơ cấu chấp hành và bộ xử lý tính toán nhúng để có thể cảm nhận môi trường xung quanh, xử lý dữ liệu và trao đổi thông tin thông qua mạng Internet. Các thiết bị IoT có thể được phân loại theo nhiều tiêu chí khác nhau như năng lực tính toán, mức độ tiêu thụ năng lượng, kích thước bộ nhớ và khả năng kết nối mạng."""

p[85] = """mạng kết nối. Những đối tượng này có thể triển khai trên một mạng thông qua Bluetooth (IEEE 802.15.1), Zigbee (IEEE 802.15.4), Wi-Fi (IEEE 802.11), Ethernet (IEEE 802.3) hay các chuẩn giao tiếp khác.

Khả năng phát triển phần cứng và phần mềm cho IoT là vô tận. Phần cứng IoT có thể phân chia thành hai nhóm chính:
- **Nhóm thiết bị hạn chế tài nguyên (Constrained Devices):** Là các thiết bị có bộ vi điều khiển (MCU) 8-bit hoặc 16-bit, dung lượng bộ nhớ RAM từ vài kilobyte (kB) đến vài chục kB, bộ nhớ Flash từ vài chục kB đến vài trăm kB, hoạt động với nguồn năng lượng pin hạn chế. Nhóm này thường chạy các hệ điều hành siêu nhẹ như TinyOS, Contiki, FreeRTOS hoặc chạy firmware trực tiếp (bare-metal).
- **Nhóm thiết bị tính toán nhúng đa năng (Smart Gateway / Single-Board Computers):** Là các máy tính đơn bo mạch (SBC) trang bị bộ vi xử lý (MPU) 32-bit hoặc 64-bit đa nhân, bộ nhớ RAM từ hàng trăm megabyte (MB) đến vài gigabyte (GB), chạy hệ điều hành Linux nhúng đầy đủ (như Raspbian, Ubuntu Core). Nhóm này đóng vai trò là trạm điều khiển, cổng kết nối (IoT Gateway) hoặc nút tính toán cận biên (Edge Node).

Theo chuẩn RFC 7228 của IETF, các thiết bị IoT hạn chế tài nguyên được phân chia thành 3 lớp cơ bản:
- **Lớp 0 (Class 0 - C0):** Thiết bị rất hạn chế (RAM << 10 kB, Flash << 100 kB). Thiết bị không thể giao tiếp trực tiếp với Internet qua IPv6 mà phải thông qua Gateway hoặc trạm thu phát.
- **Lớp 1 (Class 1 - C1):** Thiết bị hạn chế (RAM ~ 10 kB, Flash ~ 100 kB). Có thể hỗ trợ các chồng giao thức mạng rút gọn như CoAP qua 6LoWPAN/UDP.
- **Lớp 2 (Class 2 - C2):** Thiết bị ít hạn chế hơn (RAM ~ 50 kB, Flash ~ 250 kB). Có thể hỗ trợ ngăn xếp TCP/IP đầy đủ và các giao thức bảo mật nhẹ."""

p[86] = """#### 4.1.2. Thiết bị cảm biến không dây TelosB

TelosB là loại thiết bị cảm biến không dây tiết kiệm năng lượng, được xếp vào loại thiết bị IoT thuộc lớp 0 như đã trình bày ở phần trên. Hình 4.1 là hình ảnh bề ngoài của thiết bị TelosB.

**Hình 4.1.** Mote cảm biến không dây TelosB [6]

Thiết bị TelosB (được phát triển ban đầu bởi UC Berkeley) là một nền tảng phần cứng mã nguồn mở tiêu chuẩn cho các nghiên cứu về mạng cảm biến không dây (WSN):
- **Bộ vi điều khiển:** TI MSP430F1611 16-bit RISC, xung nhịp 8MHz, 10kB RAM, 48kB ROM (Flash) và 1MB bộ nhớ Flash ngoài dùng lưu trữ dữ liệu.
- **Bộ thu phát không dây:** Chip RF Chipcon/TI CC2420 tương thích chuẩn IEEE 802.15.4 / Zigbee, hoạt động ở dải tần 2.4GHz với tốc độ truyền dữ liệu 250kbps, tích hợp ăng-ten onboard.
- **Cảm biến tích hợp:** Tích hợp sẵn cảm biến nhiệt độ và độ ẩm kỹ thuật số Sensirion SHT11, cảm biến ánh sáng nhìn thấy và toàn phổ Hamamatsu.
- **Giao tiếp lập trình:** Cổng USB tích hợp qua chip FTDI cho phép vừa lập trình, gỡ lỗi vừa nạp nguồn và giao tiếp dữ liệu nối tiếp với máy tính.
- **Hệ điều hành hỗ trợ:** TinyOS và Contiki OS.

#### 4.1.3. Thiết bị nhúng Arduino

Arduino là một nền tảng tạo mẫu điện tử mã nguồn mở dựa trên phần cứng và phần mềm linh hoạt, dễ sử dụng. Nền tảng Arduino bao gồm các bo mạch vi điều khiển với nhiều cấu hình khác nhau và môi trường phát triển tích hợp Arduino IDE."""

p[87] = """Bo mạch phổ biến nhất là **Arduino Uno R3**, sử dụng vi điều khiển ATmega328P:
- Vi điều khiển 8-bit AVR RISC với xung nhịp 16MHz.
- Bộ nhớ: 32kB Flash (trong đó 0.5kB dùng cho bootloader), 2kB SRAM và 1kB EEPROM.
- Giao tiếp I/O: 14 chân Digital I/O (trong đó 6 chân hỗ trợ PWM) và 6 chân Analog Input (độ phân giải ADC 10-bit).
- Cổng kết nối: Cổng USB Type-B để nạp chương trình và cấp nguồn, giắc cắm nguồn DC ngoài 7-12V, hỗ trợ các giao tiếp nối tiếp UART, SPI, I2C.

**Hình 4.2.** Mạch Arduino Uno R3

Ngoài Arduino Uno, hệ sinh thái Arduino còn có nhiều dòng bo mạch khác phục vụ các nhu cầu đa dạng:
- **Arduino Mega 2560:** Sử dụng vi điều khiển ATmega2560 với 256kB Flash, 8kB SRAM, 54 chân Digital I/O và 16 chân Analog Input, phù hợp cho các dự án phức tạp cần nhiều chân kết nối.
- **Arduino Nano / Pro Mini:** Kích thước siêu nhỏ gọn, phù hợp tích hợp vào các thiết bị IoT yêu cầu tiết kiệm diện tích.
- **Arduino Yún:** Kết hợp vi điều khiển ATmega32u4 với một vi xử lý Atheros AR9331 (MIPS @ 400MHz) chạy hệ điều hành Linux OpenWrt-Yun, hỗ trợ kết nối Wi-Fi và Ethernet."""

p[88] = """Bên cạnh các dòng Arduino truyền thống, sự xuất hiện của các module Wi-Fi giá rẻ tương thích với môi trường Arduino IDE như ESP8266 và ESP32 của hãng Espressif Systems đã tạo nên bước phát triển nhảy vọt cho các ứng dụng IoT DIY và công nghiệp:
- **ESP8266 (NodeMCU, ESP-12E):** Sử dụng vi xử lý Tensilica Xtensa 32-bit LX106 @ 80/160MHz, tích hợp đầy đủ Wi-Fi 802.11 b/g/n, hỗ trợ giao thức TCP/IP, giá thành rất rẻ, dễ dàng kết nối trực tiếp vào mạng Internet.
- **ESP32:** Dòng vi điều khiển nâng cấp mạnh mẽ với vi xử lý 2 nhân Tensilica Xtensa 32-bit LX6 @ 160/240MHz, tích hợp cả Wi-Fi 802.11 b/g/n và Bluetooth kép (Bluetooth v4.2 BR/EDR và BLE), 520kB SRAM, hỗ trợ nhiều cổng ngoại vi ADC, DAC, I2C, SPI, UART, PWM, cảm biến chạm điện dung và mã hóa phần cứng (AES, RSA, SHA-2).

#### 4.1.4. Thiết bị máy tính nhúng Raspberry Pi

Raspberry Pi là dòng máy tính bảng đơn (Single-Board Computer - SBC) kích thước nhỏ bằng thẻ tín dụng, được phát triển tại Vương quốc Anh bởi Raspberry Pi Foundation nhằm mục đích thúc đẩy việc giảng dạy khoa học máy tính cơ bản tại các trường học và sau đó nhanh chóng trở thành nền tảng phổ biến bậc nhất cho các nhà phát triển hệ thống nhúng và IoT."""

p[89] = """**Raspberry Pi 3 Model B+** (ra mắt năm 2018):
- Bộ vi xử lý Broadcom BCM2837B0, Quad-core Cortex-A53 64-bit SoC @ 1.4GHz.
- Bộ nhớ RAM: 1GB LPDDR2 SDRAM.
- Kết nối không dây: Wi-Fi băng tần kép 2.4GHz và 5GHz IEEE 802.11.b/g/n/ac, Bluetooth 4.2, BLE.
- Mạng có dây: Gigabit Ethernet over USB 2.0 (thông lượng tối đa 300Mbps).
- Hỗ trợ Power-over-Ethernet (PoE) thông qua PoE HAT mở rộng.
- Cổng ngoại vi: 40 chân GPIO mở rộng, 4 cổng USB 2.0, cổng HDMI kích thước chuẩn, cổng camera MIPI CSI, cổng màn hình MIPI DSI, cổng âm thanh/video 4-pole 3.5mm.

**Hình 4.3.** Bo mạch máy tính nhúng Raspberry Pi 3 Model B+

**Raspberry Pi 4 Model B** (ra mắt năm 2019):
Phiên bản Raspberry Pi 4 Model B mang lại sự nâng cấp rất đáng kể giúp tăng hiệu năng của máy tính mini này lên tới 3 lần so với thế hệ trước:
- Bộ vi xử lý Broadcom BCM2711, Quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz.
- Lựa chọn RAM: 1GB, 2GB, 4GB hoặc 8GB LPDDR4-2400 SDRAM.
- Wi-Fi chuẩn 2.4GHz và 5.0GHz IEEE 802.11ac, Bluetooth 5.0, BLE.
- Cổng mạng True Gigabit Ethernet (không qua cầu USB).
- 2 cổng USB 3.0 tốc độ cao và 2 cổng USB 2.0.
- Hỗ trợ 2 cổng ra màn hình Micro-HDMI độ phân giải lên đến 4K @ 60fps."""

p[90] = """- Giải mã video phần cứng H.265 (4kp60 decode), H.264 (1080p60 decode, 1080p30 encode), hỗ trợ đồ họa OpenGL ES 3.0.
- Khe cắm thẻ Micro-SD cho hệ điều hành và lưu trữ dữ liệu.
- Cấp nguồn qua cổng USB-C: 5V DC - 3A.
- Chân nguồn 5V DC qua đầu nối GPIO (tối thiểu 3A).
- Hỗ trợ Power over Ethernet (PoE) (yêu cầu PoE HAT rời).

Raspberry Pi có thể chạy nhiều hệ điều hành như Raspbian (Raspberry Pi OS), Ubuntu MATE, Windows 10 IoT Core. Hỗ trợ nhiều ngôn ngữ lập trình như C/C++, Python, Java, JavaScript (Node.js). Raspberry Pi dễ dàng giao tiếp với các bo mạch ngoại vi như Arduino qua cổng nối tiếp hoặc GPIO.

#### 4.1.5. Tổng hợp một số nền tảng phần cứng IoT phổ biến

Bảng 4.1 tóm tắt lại 3 nền tảng phần cứng IoT phổ biến, đặc trưng cho 3 nhóm thiết bị IoT thường được sử dụng trong các giải pháp IoT thực tế từ nghiên cứu đến triển khai ứng dụng thương mại.

**Bảng 4.1.** Tổng hợp 3 nền tảng phần cứng IoT đặc trưng

| Đặc điểm | TelosB Mote | Arduino-based boards | Raspberry Pi |
|:---|:---|:---|:---|
| **Bộ xử lý** | TI MSP430 16-bit @ 8MHz | ATmega328P 8-bit @ 16MHz (hoặc ESP8266/ESP32 32-bit) | Broadcom BCM2837/2711 Quad-core ARM 64-bit @ 1.4 - 1.5GHz |
| **Bộ nhớ** | 10kB RAM, 48kB Flash | 2kB SRAM, 32kB Flash (ESP32: 520kB RAM, 4MB Flash) | 1GB - 8GB LPDDR4 RAM, thẻ nhớ MicroSD ngoài |
| **Kết nối mạng** | IEEE 802.15.4 / Zigbee (2.4GHz, 250kbps) | Cần shield gắn thêm (hoặc tích hợp Wi-Fi/BLE trên ESP) | Gigabit Ethernet, Wi-Fi Dual-band 802.11ac, Bluetooth 5.0 |"""

p[91] = """| Đặc điểm | TelosB Mote | Arduino-based boards | Raspberry Pi |
|:---|:---|:---|:---|
| **Cảm biến** | Tích hợp sẵn nhiệt độ, độ ẩm, ánh sáng | Kết nối cảm biến ngoài qua chân GPIO, ADC, I2C, SPI | Kết nối cảm biến ngoài qua GPIO, USB, Camera CSI |
| **Phần mềm** | TinyOS, Contiki OS | Arduino IDE, FreeRTOS, MicroPython | Linux (Raspbian OS), Python, Node.js, C/C++, Java |
| **Nguồn điện** | Nguồn pin 2xAA công suất cực thấp | Cổng USB (5V) hoặc DC 7-12V, tiêu thụ thấp | Cổng USB-C (5V - 3A), tiêu thụ công suất 2W - 5W |
| **Vai trò** | Nút cảm biến không dây (Sensor Node) | Thiết bị đo đạc, cơ cấu chấp hành (End Device / Node) | Cổng kết nối (IoT Gateway), máy chủ biên (Edge Server) |

### 4.2. Các nền tảng phần mềm dùng trong IoT

#### 4.2.1. Những đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT

Một hệ điều hành dùng cho thiết bị IoT thông thường gồm 3 thành phần chính:
- **Thành phần phần cứng (Hardware) và lớp trừu tượng phần cứng (Hardware Abstraction Layer - HAL):** Bao gồm các cơ chế giao tiếp, điều khiển ngoại vi của thiết bị như GPIO, UART, SPI, I2C, ADC, bộ định thời và chip vô tuyến RF.
- **Thành phần hệ thống (System Services / Kernel):** Bao gồm nhân hệ điều hành (kernel), bộ lập lịch (scheduler), các hiện thực ngăn xếp giao thức mạng (network stack), trình điều khiển thiết bị (device drivers), hệ thống tệp và các thư viện hỗ trợ quản lý bộ nhớ, năng lượng.
- **Thành phần ứng dụng (Application Layer):** Cho phép lập trình viên xây dựng và thực thi các chương trình ứng dụng IoT phục vụ mục tiêu thu thập dữ liệu, xử lý và điều khiển cụ thể."""

p[92] = """**Hình 4.4.** Các thành phần chính của một hệ điều hành cho thiết bị IoT [5]

**Phân loại hệ điều hành cho thiết bị IoT**

Tương tự như sự đa dạng của nền tảng phần cứng, các hệ điều hành phát triển cho thiết bị IoT cũng rất đa dạng nhằm phục vụ tốt các ngữ cảnh ứng dụng cụ thể:
- **Event-driven OS (Hệ điều hành hướng sự kiện):** Đây là hướng tiếp cận phổ biến nhất cho các mạng cảm biến không dây tài nguyên rất hạn chế như TinyOS, Contiki. Mọi tác vụ xử lý trên hệ thống được kích hoạt bởi các sự kiện từ bên ngoài (ngắt phần cứng hoặc bộ định thời). Nhân hệ điều hành chỉ chạy một vòng lặp quản lý hàng đợi sự kiện, không cần duy trì ngăn xếp (stack) riêng cho từng tiến trình, giúp tiết kiệm bộ nhớ RAM tối đa và giảm độ phức tạp.
- **Multi-threading OS (Hệ điều hành đa luồng):** Tiếp cận theo mô hình truyền thống của hệ điều hành máy tính, mỗi luồng có ngăn xếp riêng và thực thi độc lập. Bộ lập lịch thực hiện chuyển đổi ngữ cảnh (context switch) giữa các luồng dựa theo độ ưu tiên hoặc phân chia thời gian. Mô hình này lập trình tự nhiên, dễ sử dụng nhưng tiêu tốn bộ nhớ RAM hơn cho các ngăn xếp luồng. Đại diện tiêu biểu gồm RIOT OS, FreeRTOS, NuttX, ChibiOS.
- **Pure RTOSs (Hệ điều hành thời gian thực thuần túy):** Tập trung vào việc đảm bảo tính xác định và thời gian đáp ứng nghiêm ngặt cho các ứng dụng công nghiệp, y tế hoặc xe tự hành. Các đại diện phổ biến là FreeRTOS, RTEMS, VxWorks, QNX."""

p[93] = """Trong đó, FreeRTOS là một đại diện mã nguồn mở được dùng rất phổ biến trên các vi điều khiển nhúng 32-bit như STM32 hay ESP32.

Nội dung tiếp theo trong chương này giới thiệu chi tiết một số hệ điều hành tiêu biểu được sử dụng trong các hệ thống IoT: TinyOS, Contiki và Raspbian OS.

#### 4.2.2. Hệ điều hành TinyOS

TinyOS là hệ điều hành mã nguồn mở, hướng sự kiện (event-driven), được thiết kế chuyên biệt cho các thiết bị mạng cảm biến không dây có tài nguyên bộ nhớ rất hạn chế (vi điều khiển 8-bit đến 16-bit, RAM vài kB) [7]. TinyOS được phát triển ban đầu tại Đại học UC Berkeley kết hợp với Intel Research.

Các ứng dụng trên TinyOS được lập trình bằng ngôn ngữ **nesC** (Network Embedded Systems C), một phần mở rộng của ngôn ngữ C hỗ trợ lập trình dựa trên thành phần (component-based) và hướng sự kiện [8]. TinyOS hỗ trợ giao tiếp mạng cảm biến thông qua chồng giao thức mạng BLIP (Berkeley Low-power IP Stack) hiện thực chuẩn 6LoWPAN và RPL.

##### 4.2.2.1. Cấu trúc một ứng dụng trên TinyOS

Một ứng dụng TinyOS bao gồm nhiều thành phần (component) liên kết với nhau thông qua các giao diện (interface) [9]. Kiến trúc nesC phân biệt rõ ràng giữa hai khái niệm:
- **Interface (Giao diện):** Định nghĩa hợp đồng giao tiếp giữa các thành phần, bao gồm các hàm lệnh (**commands**) do bên cung cấp (provider) hiện thực và các sự kiện (**events**) do bên sử dụng (user) hiện thực để xử lý kết quả báo về.
- **Component (Thành phần):** Bao gồm hai loại:
  - **Module:** Chứa mã nguồn thực thi bằng ngôn ngữ nesC (hiện thực các command và event).
  - **Configuration:** Định nghĩa cách nối dây (wiring) giữa các interface của các component với nhau để tạo thành ứng dụng hoàn chỉnh."""

p[94] = """**Hình 4.5.** Mô hình hoạt động dựa trên sự kiện của hệ điều hành TinyOS

Mô hình hoạt động của TinyOS dựa trên hai khái niệm xử lý cơ bản:
- **Tasks (Tác vụ):** Đại diện cho các đoạn tính toán dài hạn trong chương trình, được đưa vào hàng đợi FIFO và thực thi tuần tự theo cơ chế không ưu tiên chiếm quyền (non-preemptive). Task không thể chiếm quyền của Task khác nhưng có thể bị ngắt bởi Hardware Event.
- **Hardware Event Handlers (Trình xử lý sự kiện phần cứng):** Được kích hoạt khi có ngắt từ phần cứng (như bộ định thời đếm xong hoặc gói tin truyền thông đến). Các hàm xử lý ngắt thực thi ngay lập tức và có thể chiếm quyền của Task đang chạy để đảm bảo tính thời gian thực.

Một ứng dụng TinyOS viết bằng nesC gồm các tệp thành phần cơ bản [10]:
1. Tệp cấu hình ứng dụng cao nhất (Top-level Configuration, ví dụ `BlinkAppC.nc`).
2. Tệp module hiện thực logic ứng dụng (Module, ví dụ `BlinkC.nc`).
3. Các tệp giao diện (Interfaces, nếu tự định nghĩa mới).
4. Tệp Makefile để biên dịch chương trình."""

p[95] = """Mã nguồn của một tệp cấu hình ứng dụng mẫu (`BlinkAppC.nc`):

```nesc
configuration BlinkAppC
{
}
implementation
{
  components MainC, BlinkC, LedsC;
  components new TimerMilliC() as Timer0;

  BlinkC -> MainC.Boot;
  BlinkC.Leds -> LedsC;
  BlinkC.Timer0 -> Timer0;
}
```

Mã nguồn của tệp module tương ứng (`BlinkC.nc`):

```nesc
module BlinkC
{
  uses interface Boot;
  uses interface Leds;
  uses interface Timer<TMilli> as Timer0;
}
implementation
{
  event void Boot.booted() {
    call Timer0.startPeriodic(1000);
  }

  event void Timer0.fired() {
    call Leds.led0Toggle();
  }
}
```

**Hình 4.6.** Mã nguồn mô tả sự kết nối giữa các module thành phần trong ứng dụng BlinkC"""

p[96] = """##### 4.2.2.2. Các thành phần, dịch vụ cơ bản của TinyOS

**Dịch vụ định thời (Timer Interface)**

TinyOS cung cấp giao diện trừu tượng hóa bộ định thời đa năng `Timer<precision_tag>`, cho phép ứng dụng thiết lập các bộ đếm thời gian chu kỳ hoặc một lần với độ chính xác cao.

```nesc
interface Timer<precision_tag>
{
  command void startPeriodic(uint32_t dt);
  command void startOneShot(uint32_t dt);
  command void stop();
  event void fired();
  command bool isRunning();
  command bool isOneShot();
  command void startPeriodicAt(uint32_t t0, uint32_t dt);
  command void startOneShotAt(uint32_t t0, uint32_t dt);
  command uint32_t getNow();
  command uint32_t getSettled();
  command uint32_t getdt();
}
```

Giao diện `Timer` sử dụng các tham số kiểu (precision tag) để xác định độ phân giải thời gian:
- `TMilli`: Bộ định thời độ chính xác mili-giây (1/1024 giây hoặc 1/1000 giây).
- `TMicro`: Bộ định thời độ chính xác micro-giây.
- `T32khz`: Bộ định thời chạy theo xung nhịp thạch anh 32.768kHz."""

p[97] = """Đặc trưng của bộ định thời trong TinyOS phản ánh:
- **Độ rộng (Width):** Là 16-bit hoặc 32-bit (trong TelosB, Timer mặc định hỗ trợ 32-bit để tránh tràn số nhanh).
- **Độ chính xác (Accuracy):** Phản ánh sự phù hợp giữa nhịp thời gian cung cấp với thời gian thực tế, tránh hiện tượng trôi dạt đồng hồ (clock drift).

**Cơ chế lập lịch và Tác vụ (Task Scheduler)**

Trong TinyOS, các tính toán không yêu cầu tức thời được triển khai dưới dạng **Task**. Việc định nghĩa một Task trong nesC được thực hiện qua từ khóa `task`:

```nesc
task void processDataTask()
{
  // Xử lý dữ liệu thu thập từ cảm biến
  computeAverage();
  call Leds.led1Toggle();
}
```

**Hình 4.9.** Định nghĩa Task trong nesC

Để đưa Task vào hàng đợi của bộ lập lịch, chương trình sử dụng lệnh `post`:

```nesc
event void Sensor.readDone(error_t result, uint16_t data)
{
  if (result == SUCCESS) {
    sensorValue = data;
    post processDataTask();
  }
}
```

**Hình 4.10.** Khai báo gọi Task trong nesC

Nếu hàng đợi Task còn chỗ trống, `post` trả về `SUCCESS` và Task sẽ được thực thi khi bộ xử lý rảnh rỗi. Ngược lại, nếu hàng đợi bị đầy, `post` trả về `FAIL`."""

p[98] = """**Cấu trúc thông điệp và truyền thông trong TinyOS**

Giao tiếp không dây trong TinyOS xoay quanh kiểu dữ liệu thông điệp cơ bản `message_t`. Định dạng của `message_t` bao gồm 3 phần: tiêu đề (header), vùng dữ liệu tải trọng (payload) và phần chân (footer):

- Kích thước tải trọng tối đa của gói tin mặc định là 28 byte (được định nghĩa qua hằng số `TOSH_DATA_LENGTH = 28`). Lập trình viên có thể cấu hình lại khi biên dịch bằng tùy chọn `-DTOSH_DATA_LENGTH=x` trong Makefile. Nếu một gói tin vượt quá kích thước này, nó sẽ bị loại bỏ.
- Phần header chứa địa chỉ nguồn, địa chỉ đích, độ dài dữ liệu, chỉ số nhóm (group ID) và loại thông điệp Active Message (AM Type).
- Phần footer chứa các trường kiểm tra lỗi CRC và cờ báo nhận (ACK).

TinyOS cung cấp mô hình trừu tượng Active Message (AM) cho phép các ứng dụng phân biệt các luồng dữ liệu khác nhau thông qua trường định danh `am_id_t` (tương tự như số cổng port trong TCP/UDP).

**Hình 4.11.** Mô hình kiến trúc phần cứng của hệ điều hành TinyOS"""

p[99] = """**Giao diện gửi tin (AMSend Interface)**

Giao diện `AMSend` được sử dụng để gửi các gói tin Active Message đi qua mạng không dây:

```nesc
interface AMSend
{
  command error_t send(am_addr_t addr, message_t* msg, uint8_t len);
  command error_t cancel(message_t* msg);
  event void sendDone(message_t* msg, error_t error);
  command uint8_t maxPayloadLength();
  command void* getPayload(message_t* msg, uint8_t len);
}
```

**Hình 4.12.** Giao diện AMSend

Ý nghĩa các hàm trong `AMSend`:
- `send(addr, msg, len)`: Gửi gói tin `msg` có chiều dài `len` đến địa chỉ đích `addr`. Nếu gửi thành công lệnh trả về `SUCCESS` và sau đó hệ thống sẽ phát tín hiệu sự kiện `sendDone`.
- `cancel(msg)`: Hủy lệnh gửi gói tin nếu gói tin đang chờ truyền.
- `sendDone(msg, error)`: Sự kiện thông báo việc truyền tin đã hoàn tất (thành công hoặc thất bại). Phía gửi không được phép thay đổi nội dung vùng đệm `msg` cho đến khi sự kiện này được kích hoạt.
- `maxPayloadLength()`: Trả về độ dài tải trọng tối đa mà tầng này hỗ trợ.
- `getPayload(msg, len)`: Lấy con trỏ trỏ đến vùng dữ liệu tải trọng của gói tin."""

p[100] = """**Giao diện nhận tin (Receive Interface)**

Giao diện `Receive` dùng để nhận các gói tin đến và chuyển dữ liệu lên tầng ứng dụng:

```nesc
interface Receive
{
  event message_t* receive(message_t* msg, void* payload, uint8_t len);
}
```

**Hình 4.13.** Giao diện Receive

Hàm sự kiện `receive` nhận con trỏ gói tin `msg`, con trỏ dữ liệu `payload` và độ dài `len`. Hàm này bắt buộc phải trả về một con trỏ tới một vùng đệm `message_t` hợp lệ để tầng mạng sử dụng cho lần nhận gói tin tiếp theo (cơ chế tráo đổi vùng đệm buffer swapping để tránh sao chép dữ liệu):

```nesc
message_t buffer;
message_t* ptr = &buffer;

event message_t* Receive.receive(message_t* msg, void* payload, uint8_t len)
{
  message_t* tmp = ptr;
  ptr = msg; // Lưu gói tin vừa nhận
  processPacket(payload, len);
  return tmp; // Trả lại vùng đệm rảnh rỗi cho tầng dưới
}
```

**Giao diện Packet**

```nesc
interface Packet
{
  command void clear(message_t* msg);
  command uint8_t payloadLength(message_t* msg);
  command void setPayloadLength(message_t* msg, uint8_t len);
  command uint8_t maxPayloadLength();
  command void* getPayload(message_t* msg, uint8_t len);
}
```

**Hình 4.14.** Giao diện Packet"""

p[101] = """**Giao diện PacketAcknowledgements**

Giao diện `PacketAcknowledgements` cung cấp cơ chế yêu cầu và kiểm tra báo nhận (ACK) phần cứng ở tầng liên kết dữ liệu cho từng gói tin riêng lẻ:

```nesc
interface PacketAcknowledgements
{
  command error_t requestAck(message_t* msg);
  command error_t noAck(message_t* msg);
  command bool wasAcked(message_t* msg);
}
```

**Hình 4.15.** Giao diện PacketAcknowledgements

Khi gửi tin, ứng dụng có thể gọi `requestAck(msg)` để yêu cầu nút nhận gửi lại khung xác nhận ACK ngay sau khi nhận được gói tin. Trong sự kiện `sendDone`, ứng dụng gọi `wasAcked(msg)` để kiểm tra việc truyền tin có thành công đến đích kế cận hay không.

**Định dạng khung truyền trong TinyOS (T-Frame và I-Frame)**

Ngăn xếp radio CC2420 trong TinyOS hỗ trợ hai định dạng khung truyền:
- **T-Frame (TinyOS Frame):** Định dạng khung chuẩn của TinyOS, tối ưu hóa kích thước tiêu đề cho mạng cảm biến riêng biệt.
- **I-Frame (IEEE 802.15.4 Frame):** Tuân thủ hoàn toàn định dạng chuẩn IEEE 802.15.4, cho phép TinyOS chia sẻ kênh truyền và giao tiếp liên mạng với các hệ thống khác như 6LoWPAN. Mặc định trong TinyOS 2.x, ngăn xếp radio sử dụng định dạng I-Frame."""

p[102] = """**Ngăn xếp vô tuyến CC2420 (CC2420 Radio Stack)**

Ngăn xếp phần mềm CC2420 chứa nhiều lớp (layer) thành phần được xếp chồng lên nhau nằm giữa ứng dụng và phần cứng thu phát:

**Hình 4.16.** Kiến trúc lớp trong CC2420 Radio Stack

Mỗi lớp trong ngăn xếp cung cấp và sử dụng các giao diện chuẩn (`Send`, `Receive`, `SplitControl`). Các lớp chính bao gồm:
- **ActiveMessageP:** Lớp trên cùng, điền các trường tiêu đề Active Message và tương tác trực tiếp với tầng ứng dụng.
- **UniqueSendLayer:** Tự động tạo và gắn số thứ tự dữ liệu duy nhất (Data Sequence Number - DSN) vào tiêu đề để bên nhận có thể phát hiện và loại bỏ các gói tin bị trùng lặp.
- **PacketLink:** Cung cấp dịch vụ truyền lại tự động (Automatic Retransmission) nếu không nhận được tín hiệu ACK từ nút kế cận."""

p[103] = """- **Low Power Listening (LPL):** Hiện thực kỹ thuật lắng nghe năng lượng thấp bất đồng bộ. Nút gửi sẽ phát chuỗi gói tin liên tiếp (preamble packets) để đánh thức nút nhận đang trong chu kỳ ngủ định kỳ, giúp giảm tiêu hao năng lượng tối đa khi mạng nhàn rỗi.
- **UniqueReceive:** Duy trì bảng lịch sử các gói tin gần nhất để lọc bỏ các gói tin trùng lặp nhận được do truyền lại.
- **TinyOSNetworkC:** Cho phép nhận dạng và chuyển tiếp các gói tin chuẩn IEEE 802.15.4 liên mạng (như 6LoWPAN).
- **CSMA/CA:** Quản lý truy cập môi trường truyền không dây, thực hiện thuật toán backoff ngẫu nhiên để tránh va chạm tín hiệu trên kênh.
- **TransmitP / ReceiveP:** Tương tác trực tiếp với phần cứng chip CC2420 thông qua bus SPI, chân ngắt và GPIO.

#### 4.2.3. Hệ điều hành Contiki

Contiki là hệ điều hành mã nguồn mở, gọn nhẹ (lightweight), đa nhiệm được thiết kế chuyên biệt cho các thiết bị mạng cảm biến không dây và Internet of Things có tài nguyên bộ nhớ hạn chế [14]. Contiki được sáng lập bởi Adam Dunkels tại Viện Khoa học Máy tính Thụy Điển (SICS).

Đặc tính nổi bật của Contiki là tính linh hoạt cao, hỗ trợ nạp động (dynamic loading) và thay thế từng chương trình hoặc dịch vụ riêng lẻ trong lúc hệ thống đang chạy. Contiki được xây dựng theo mô hình hướng sự kiện (event-driven) kết hợp với cơ chế tiểu luồng **Protothreads**, mang lại phong cách lập trình tuần tự tuyến tính mà không tốn kém chi phí ngăn xếp luồng độc lập."""

p[104] = """##### 4.2.3.1. Cấu trúc một ứng dụng trên Contiki

Các ứng dụng trên Contiki được viết bằng ngôn ngữ C chuẩn kết hợp các macro Protothreads, có cấu trúc cơ bản như sau:

```c
#include "contiki.h"
#include <stdio.h>

/* Khai báo và khởi tạo một tiến trình */
PROCESS(hello_world_process, "Hello World Process");
AUTOSTART_PROCESSES(&hello_world_process);

/* Định nghĩa luồng thực thi của tiến trình */
PROCESS_THREAD(hello_world_process, ev, data)
{
  static struct etimer timer;

  PROCESS_BEGIN();

  /* Thiết lập timer định kỳ 5 giây */
  etimer_set(&timer, CLOCK_SECOND * 5);

  while(1) {
    /* Chờ cho đến khi sự kiện timer hết hạn xảy ra */
    PROCESS_WAIT_EVENT_UNTIL(ev == PROCESS_EVENT_TIMER);

    printf("Hello, World! Contiki IoT\n");

    /* Đặt lại timer */
    etimer_reset(&timer);
  }

  PROCESS_END();
}
```

**Biên dịch chương trình trong Contiki**
Để biên dịch một ứng dụng Contiki, cần có tệp mã nguồn C và tệp `Makefile` nằm trong thư mục dự án:

```makefile
CONTIKI = ../..
all: hello-world
include $(CONTIKI)/Makefile.include
```"""

p[105] = """Dòng đầu tiên chỉ ra đường dẫn tới thư mục gốc của Contiki; dòng thứ hai chỉ định tên ứng dụng cần biên dịch; và dòng cuối cùng nạp tệp `Makefile.include` của hệ thống Contiki.

Để biên dịch chương trình cho một nền tảng phần cứng cụ thể:

```bash
make TARGET=<tên_thiết_bị> <tên_ứng_dụng>
# Ví dụ biên dịch cho mote TelosB (sky):
make TARGET=sky hello-world
```

Để Contiki ghi nhớ nền tảng phần cứng cho các lần biên dịch tiếp theo:

```bash
make TARGET=sky savetarget
```

Để nạp chương trình lên bo mạch qua cổng kết nối:

```bash
make hello-world.upload TARGET=sky
```

Để theo dõi dữ liệu xuất ra từ cổng nối tiếp serial:

```bash
make login TARGET=sky
```

##### 4.2.3.2. Các thành phần, dịch vụ cơ bản trên hệ điều hành Contiki

**Kiến trúc nhân hệ điều hành (Kernel Architecture)**

Nhân Contiki bao gồm một bộ định thời gọn nhẹ và bộ điều phối sự kiện. Hệ thống hỗ trợ hai loại sự kiện:
- **Sự kiện bất đồng bộ (Asynchronous Event):** Sự kiện được đưa vào hàng đợi và được xử lý tuần tự bởi tiến trình đích khi đến lượt.
- **Sự kiện đồng bộ (Synchronous Event):** Kích hoạt tiến trình đích thực thi ngay lập tức (tương tự như một lời gọi hàm trực tiếp), tiến trình gửi sẽ tạm dừng cho đến khi tiến trình đích xử lý xong sự kiện."""

p[106] = """**Cơ chế thăm dò (Polling Mechanism):** Là một dạng sự kiện có độ ưu tiên cao, được hệ thống thực thi xen giữa các sự kiện thông thường nhằm kiểm tra nhanh các trạng thái phần cứng và phản hồi các ngắt ngoại vi tức thời.

**Các cơ chế định thời (Timers) trong Contiki**
Contiki cung cấp 4 thư viện định thời đa dạng phục vụ các nhu cầu khác nhau:
- **timer:** Bộ định thời đơn giản, chỉ kiểm tra xem một khoảng thời gian đã trôi qua hay chưa (thăm dò thụ động).
- **etimer (Event Timer):** Tạo ra một sự kiện gửi đến tiến trình khi hết thời gian định trước, giúp tiến trình tự động đánh thức từ trạng thái chờ.
- **ctimer (Callback Timer):** Tự động gọi một hàm callback được chỉ định khi hết thời gian, rất hữu ích cho các giao thức mạng.
- **rtimer (Real-time Timer):** Bộ định thời thời gian thực độ chính xác cao dựa trên ngắt phần cứng, phục vụ các tác vụ đòi hỏi thời gian đáp ứng nghiêm ngặt như điều khiển chu kỳ nhiệm vụ radio.

**Chế độ tiết kiệm năng lượng**
Contiki tự động đưa bộ vi xử lý vào trạng thái nghỉ công suất thấp (Low Power Mode - LPM) mỗi khi hàng đợi sự kiện rỗng. Khi có ngắt phần cứng hoặc bộ định thời kích hoạt, MCU sẽ thức dậy để xử lý và sau đó lại quay về trạng thái ngủ, giúp kéo dài tối đa thời gian hoạt động bằng pin của thiết bị."""

p[107] = """**Kiến trúc dịch vụ và nạp động (Dynamic Services)**

Trong Contiki, một dịch vụ (service) là một tiến trình cung cấp các chức năng dùng chung (như giao thức mạng, bộ điều khiển cảm biến) cho các tiến trình khác. Điểm đặc sắc là các dịch vụ có thể được biên dịch độc lập, nạp vào bộ nhớ hoặc gỡ bỏ trong lúc hệ thống đang hoạt động mà không cần khởi động lại bo mạch.

Lớp quản lý dịch vụ (Service Layer) duy trì danh sách các dịch vụ hiện có trong hệ thống và phiên bản tương ứng. Ứng dụng gọi dịch vụ thông qua một thư viện gốc (stub library) để liên kết động với tiến trình dịch vụ tại thời điểm chạy.

**Ngăn xếp truyền thông trong Contiki**

Contiki hỗ trợ hai ngăn xếp mạng mạnh mẽ:
- **uIP / uIPv6:** Ngăn xếp TCP/IP và IPv6 siêu nhỏ gọn tuân thủ chuẩn RFC, hỗ trợ 6LoWPAN, RPL, UDP, TCP, CoAP và MQTT, cho phép nút cảm biến kết nối trực tiếp với Internet toàn cầu.
- **Rime:** Ngăn xếp truyền thông mạng cảm biến nhẹ tùy biến, cung cấp các khối giao tiếp phân tầng từ cơ bản (broadcast, unicast một chặng) đến nâng cao (truyền đa chặng, thu thập dữ liệu cây hop-by-hop) với chi phí bộ nhớ tối thiểu.

**Hệ thống tệp Coffee (Coffee Flash File System)**
Contiki tích hợp sẵn hệ thống tệp Coffee chuyên biệt cho chip nhớ Flash ngoài của các mote cảm biến, cho phép lưu trữ cấu hình và nhật ký dữ liệu cảm biến bền vững với cơ chế san phẳng độ mòn (wear leveling)."""

p[108] = """**Hình 4.18.** Sơ đồ các cơ chế giao tiếp trên Contiki

#### 4.2.4. Hệ điều hành Raspbian OS

Hệ điều hành Raspbian (hiện nay được đổi tên chính thức là **Raspberry Pi OS**) là hệ điều hành mã nguồn mở miễn phí dựa trên nền tảng bản phân phối Linux Debian, được tối ưu hóa đặc biệt cho dòng máy tính nhúng phần cứng Raspberry Pi [15].

Ban đầu Raspbian được khởi xướng bởi Mike Thompson và Peter Green như một dự án cộng đồng độc lập, sau đó được Raspberry Pi Foundation chính thức bảo trợ và phát triển thành hệ điều hành chính thức. Kho phần mềm của Raspbian cung cấp hơn 35.000 gói ứng dụng (packages) được biên dịch sẵn, đáp ứng đầy đủ từ các nhu cầu học tập, phát triển phần mềm nhúng đến triển khai các dịch vụ máy chủ mạng và IoT Gateway phức tạp."""

p[109] = """**Hình 4.19.** Kiến trúc hệ điều hành Raspbian OS

**Kiến trúc và các đặc điểm kỹ thuật của Raspbian OS**
- **Kiến trúc nhân:** Nhân Linux monolithic đầy đủ hỗ trợ đa nhiệm, đa người dùng, bộ nhớ ảo và cơ chế đa luồng ưu tiên chiếm quyền (preemptive multi-threading).
- **Ngôn ngữ phát triển:** Hỗ trợ toàn diện các ngôn ngữ lập trình hiện đại như Python, C, C++, Java, Node.js, PHP, Ruby, Scratch. Thư viện Python (`RPi.GPIO`, `gpiozero`) cho phép lập trình điều khiển các chân phần cứng cực kỳ nhanh chóng và trực quan.
- **Giao thức và kết nối:** Hỗ trợ đầy đủ bộ giao thức TCP/IP tiêu chuẩn, Bluetooth/BLE, Wi-Fi, Ethernet và các chuẩn giao tiếp công nghiệp như MQTT, HTTP/HTTPS, WebSockets, CoAP, Modbus.
- **Công cụ mô phỏng:** Có thể giả lập chạy toàn bộ hệ thống Raspbian trên máy tính thông qua công cụ máy ảo QEMU ARM.
- **Bảo mật:** Cung cấp đầy đủ các cơ chế bảo mật cấp doanh nghiệp của Linux như xác thực người dùng SSH, tường lửa iptables/ufw, mã hóa OpenSSL, VPN và phân quyền truy cập tệp."""

p[110] = """- **Hỗ trợ đa phương tiện mạnh mẽ:** Tận dụng bộ tăng tốc đồ họa phần cứng VideoCore GPU tích hợp trên bo mạch Raspberry Pi, Raspbian hỗ trợ hiển thị giao diện đồ họa mượt mà (môi trường máy tính để bàn PIXEL / LXDE), xử lý video độ phân giải cao 1080p và 4K, hỗ trợ các chuẩn OpenMAX, OpenGL ES, OpenVG và các thư viện thị giác máy tính như OpenCV. Hệ điều hành cũng hỗ trợ truyền phát âm thanh/hình ảnh thời gian thực qua các giao thức VoIP như SIP và RTP.
- **Mức tiêu thụ năng lượng:** Mặc dù tiêu thụ nhiều năng lượng hơn so với các vi điều khiển cấp thấp, một bo mạch Raspberry Pi chạy Raspbian chỉ tiêu thụ công suất trung bình từ 1.5W đến 5W (tùy thuộc vào tác vụ và tải CPU), hoàn toàn có thể chạy bằng nguồn sạc dự phòng di động hoặc hệ thống pin năng lượng mặt trời cho các trạm giám sát thông minh ngoài trời.

Nhờ những ưu điểm vượt trội trên, Raspberry Pi chạy Raspbian thường đóng vai trò là **Edge Gateway** hoặc **Edge Computing Node** trong kiến trúc IoT hiện đại, chịu trách nhiệm thu thập dữ liệu từ các mạng cảm biến cục bộ (qua Zigbee, LoRa, BLE), thực hiện tiền xử lý, nén dữ liệu, chạy các mô hình AI/Machine Learning suy luận nhẹ tại biên và chuyển tiếp dữ liệu lên đám mây."""

p[111] = """#### 4.2.5. Tổng hợp một số nền tảng phần mềm IoT phổ biến

**Bảng 4.2.** Bảng tổng hợp đặc tính một số nền tảng hệ điều hành nổi tiếng trong IoT [15]

| Hệ điều hành | Min RAM | Min ROM | Bộ xử lý / Xung nhịp | Kiến trúc nhân | Cơ chế lập lịch | Mô hình luồng | Ngôn ngữ | Hỗ trợ C++ |
|:---|:---:|:---:|:---|:---|:---|:---|:---|:---:|
| **TinyOS** | 1 kB | 4 kB | 4 - 8 bit | Monolithic | Non-preemptive FIFO | Event driven | NesC | NO |
| **Contiki** | 2 kB | 30 kB | 8 bit | Modular | Preemptive FIFO | Event driven, Protothreads | C | Partially |
| **RIOT** | 1.5 kB | 5 kB | 16/32 bit | Microkernel | Preemptive Priority | Multi-threading | C, C++ | YES |
| **LiteOS** | 4 kB | 128 kB | 8MHz | Modular | Preemptive Priority (Tickless) | Multi-threading | LiteC++ | NO |
| **FreeRTOS** | 0.5 - 10 kB | 12 kB | 32-bit | Microkernel | Preemptive Priority | Multi-threading | C | YES |
| **Mynewt** | 8 kB | 64 kB | 12 - 200MHz | Modular | Preemptive Priority | Multi-threading | Go, C | YES |
| **Mbed** | 16 kB | 32 kB | 32-bit | Monolithic | Non-preemptive | Singlethread / RTOS | C, C++ | YES |"""

p[112] = """**Bảng 4.2.** (tiếp theo)

| Hệ điều hành | Min RAM | Min ROM | Bộ xử lý / Xung nhịp | Kiến trúc nhân | Cơ chế lập lịch | Mô hình luồng | Ngôn ngữ | Hỗ trợ C++ |
|:---|:---:|:---:|:---|:---|:---|:---|:---|:---:|
| **uClinux** | 512 kB | 512 - 2048 kB | 32-bit | Monolithic | Preemptive | Multi-threading | C | Partially |
| **Raspbian** | 512MB - 1GB | 256MB - 8GB | ARM Cortex-A53 | Monolithic | Preemptive | Multi-threading | Python, C, C++, Java, Node.js | YES |
| **Android Things** | 128MB | 32MB | ARM, Intel x86, MIPS | Modular | Preemptive | Multi-threading | Java, C, Weave | YES |

**Bảng 4.3.** Bảng tổng hợp đặc tính kỹ thuật một số nền tảng hệ điều hành nổi tiếng trong IoT

| Hệ điều hành | Thực thi script từ xa | Cấu trúc hệ thống tệp | Bộ nhớ động | Công cụ mô phỏng | Chồng giao thức và các giao thức mạng có hỗ trợ |
|:---|:---:|:---|:---:|:---|:---|
| **TinyOS** | KHÔNG | Đơn mức | KHÔNG | TOSSIM, PowerTOSSIM | BLIP, TinyRPL, CoAP, WiFi, LTE, MQTT, 6LoWPAN, TCP, IPv6, Bluetooth |
| **Contiki** | KHÔNG | Đơn mức (Coffee) | CÓ | Netsim, Cooja, MSPSim | RPL, uIP, uIPv6, MQTT, 6LoWPAN, CoAP, WiFi, Bluetooth |
| **RIOT** | CÓ | Thứ bậc | CÓ | Cooja | TCP, UDP, IPv6, 6LoWPAN, RPL, CoAP, CBOR, UBJSON, OpenWSN, WiFi, Bluetooth, LTE, MQTT |"""

p[113] = """**Bảng 4.3.** (tiếp theo)

| Hệ điều hành | Thực thi script từ xa | Cấu trúc hệ thống tệp | Bộ nhớ động | Công cụ mô phỏng | Chồng giao thức và các giao thức mạng có hỗ trợ |
|:---|:---:|:---|:---:|:---|:---|
| **LiteOS** | CÓ | Thứ bậc | CÓ | AVRORA | NB-IoT, 6LoWPAN, Zigbee, LTE, Bluetooth |
| **FreeRTOS** | CÓ | Thứ bậc | CÓ | QEMU | uIP, lwIP, TCP, 6LoWPAN, CoAP, MQTT |
| **Mynewt** | CÓ | Thứ bậc | CÓ | QEMU | BLE, IPv6, 6LoWPAN, HTTP, TCP, CoAP, MQTT, UDP, LoRa PHY, LoRaWAN |
| **Mbed** | CÓ | Thứ bậc | CÓ | QEMU | 6LoWPAN, Ethernet, Zigbee, HTTP, WiFi, BLE, IPv6, CoAP, MQTT |
| **uClinux** | CÓ | Thứ bậc | CÓ | GDB/ARMulator | uIP, lwIP, WiFi, Bluetooth, LTE, IPv6, MQTT |
| **Raspbian** | CÓ | Thứ bậc | CÓ | QEMU | RTP, LTE, HTTP, TCP, MQTT, CoAP, Bluetooth, WebSockets |
| **Android Things** | CÓ | Thứ bậc | CÓ | RPi3, Intel Edison, NXP Pico | Weave, Thread, Zigbee, Z-Wave, Bluetooth, WiFi |"""

p[114] = """Thông qua phần tổng hợp từ hai bảng, Bảng 4.2 và Bảng 4.3 ta thấy hiện nay có rất nhiều nền tảng phần mềm, hệ điều hành hỗ trợ phát triển các giải pháp IoT với nhiều đặc trưng, đặc tính kỹ thuật khác nhau. Chính vì thế, tùy theo nhu cầu sử dụng, tùy theo tính năng, yêu cầu của giải pháp IoT muốn phát triển mà các nhà phát triển hệ thống có thể chọn lựa cho mình một môi trường phù hợp. Ví dụ, trong môi trường nghiên cứu học thuật ở nhiều trường đại học trên thế giới, khi nghiên cứu về mạng cảm biến không dây, thiết bị IoT tiết kiệm năng lượng, tài nguyên hạn chế thì các hệ điều hành như TinyOS, Contiki thường được lựa chọn. Ngoài ra, một nền tảng khá phổ biến và dễ dàng tiếp cận hiện nay đó là máy tính nhúng Raspberry Pi với hệ điều hành Raspbian. Đây là một thiết bị nhúng hỗ trợ khá đầy đủ chức năng của một máy tính thu nhỏ, cho phép người lập trình sử dụng những tiện ích của ngôn ngữ lập trình bậc cao như Python, Node.js, Java... để phát triển các ứng dụng của mình một cách tiện lợi. Tóm lại, với sự phát triển không ngừng của công nghệ, lần lượt ngày càng nhiều nền tảng phần cứng được sản xuất chế tạo, kèm theo đó là các giải pháp phần mềm cũng được tạo ra, mang đến sự đa dạng chủng loại và nhiều sự lựa chọn cho người học, người phát triển giải pháp IoT với nhiều cấp độ, nhiều cách tiếp cận khác nhau.

## BÀI TẬP CHƯƠNG 4

1. Hãy so sánh các nhóm phần cứng dùng trong IoT và liệt kê các thiết bị thuộc mỗi nhóm.
2. Hãy trình bày kiến trúc và hoạt động của một chương trình nesC trên TinyOS.
3. Hãy trình bày kiến trúc và hoạt động của một chương trình C trên Contiki OS.
4. Hãy liệt kê các loại phần cứng, phần mềm và các cảm biến (nếu có) để xây dựng một ứng dụng giám sát chất lượng không khí.
5. Từ nền tảng Arduino và Raspberry Pi 3, hãy thiết kế ứng dụng giám sát môi trường và điều khiển thiết bị cho nhà thông minh."""

p[115] = """6. Từ nền tảng CC2530, hãy thiết kế ứng dụng Nông nghiệp thông minh.
7. Hãy xác định loại phần cứng, phần mềm, cảm biến để xây dựng hệ thống cảnh báo cháy rừng có các nút cảm biến được cấp nguồn bằng pin với yêu cầu tối ưu năng lượng sử dụng để thời gian hoạt động của ứng dụng là lớn nhất."""

# Apply to GT_IoT_Manual.md
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(^## Trang \d+\s*$)', text, flags=re.MULTILINE)
pages_dict = {}
for i in range(1, len(parts), 2):
    p_num = int(re.search(r'\d+', parts[i]).group(0))
    pages_dict[p_num] = parts[i+1]

for page_num in range(83, 116):
    if page_num in p:
        pages_dict[page_num] = '\n\n' + p[page_num].strip() + '\n\n'

out = [parts[0]]
for i in range(1, len(parts), 2):
    marker = parts[i]
    p_num = int(re.search(r'\d+', parts[i]).group(0))
    out.append(marker)
    out.append(pages_dict[p_num])

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'w', encoding='utf-8') as f:
    f.write(''.join(out))

print("Chapter 4 (pages 83-115) updated successfully!")
