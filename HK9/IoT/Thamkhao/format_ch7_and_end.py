# -*- coding: utf-8 -*-
import sys, re

p = {}

p[179] = """# CHƯƠNG 7. TÁI CẤU HÌNH TRONG IOT

Tái cấu hình trong IoT là khả năng cho phép thay đổi tính năng, hành vi ứng dụng hoặc cấu hình hoạt động của các thiết bị IoT từ xa sau khi chúng đã được triển khai vào môi trường thực tế nhằm đáp ứng nhu cầu ngày càng cao của người sử dụng và môi trường vận hành biến đổi.

Trong thực tế triển khai các hệ thống IoT và mạng cảm biến không dây quy mô lớn (hàng trăm đến hàng nghìn nút phân bố trên các cánh đồng, trong rừng sâu hoặc gắn trong các kết cấu hạ tầng giao thông, công trình xây dựng), việc tiếp cận vật lý trực tiếp tới từng thiết bị để nạp lại phần mềm bằng dây cáp hay thay thế linh kiện là điều bất khả thi về mặt kinh tế, thời gian và công sức. Do đó, các kỹ thuật **tái lập trình qua mạng (Over-The-Air Programming - OTA)** và **tái cấu hình phần mềm động (Dynamic Software Reconfiguration)** trở thành yêu cầu sống còn.

Nội dung chương này trình bày tổng quan về các hướng tiếp cận tái cấu hình trong IoT; giới thiệu các giải pháp hiện thực OTA tiêu biểu trên các nền tảng phổ biến như TinyOS, ESP8266 và Raspberry Pi; đồng thời đề xuất khung kiến trúc tái cấu hình IoT đa nền tảng hiện đại dựa trên cách tiếp cận Mạng điều khiển bằng phần mềm (Software-Defined Networking - SDN)."""

p[180] = """Thông qua chương này, người đọc có cái nhìn tổng quan về tái cấu hình trong IoT, ý nghĩa và cơ chế hiện thực của một số giải pháp hiện có. Bên cạnh đó, thông qua minh họa phát triển một giải pháp tái cấu hình cụ thể, người đọc có thể áp dụng những kỹ năng kỹ thuật, vận dụng những kiến thức liên quan để tự xây dựng các cơ chế cập nhật từ xa cho hệ thống IoT của mình.

### 7.1. Tổng quan về tái cấu hình trong IoT

Trong vòng đời hoạt động của một hệ thống IoT, nhu cầu tái cấu hình nảy sinh từ nhiều lý do:
1. **Sửa lỗi phần mềm và vá lỗ hổng bảo mật:** Phần mềm nhúng ban đầu có thể phát sinh lỗi logic hoặc lộ các lỗ hổng bảo mật cần phải được khắc phục kịp thời.
2. **Cập nhật tính năng mới:** Người dùng hoặc nhà cung cấp dịch vụ muốn bổ sung các thuật toán xử lý dữ liệu mới, hỗ trợ thêm các loại cảm biến mới.
3. **Thích ứng với sự thay đổi của môi trường và nhiệm vụ:** Thay đổi tần suất lấy mẫu cảm biến theo mùa, chuyển đổi giao thức định tuyến khi tô-pô mạng thay đổi, hoặc thay đổi ngưỡng kích hoạt cảnh báo.
4. **Tối ưu hóa năng lượng:** Điều chỉnh chu kỳ thức-ngủ (duty cycle) của nút mạng khi pin sắp cạn để kéo dài tối đa thời gian sống của mạng."""

p[181] = """### 7.2. Các hướng tiếp cận trong tái cấu hình IoT

Dựa trên mức độ trừu tượng hóa và dung lượng dữ liệu cần truyền tải qua mạng không dây, các kỹ thuật tái cấu hình trong IoT được chia thành 5 hướng tiếp cận chính:
1. Hướng tiếp cận thay thế toàn bộ image (Full Image Replacement)
2. Hướng tiếp cận dựa trên module (Module-based Approach)
3. Hướng tiếp cận dựa trên cơ sở dữ liệu (Database-based Approach)
4. Hướng tiếp cận máy ảo (Virtual Machine-based Approach)
5. Hướng tiếp cận hướng tới dịch vụ (Service-Oriented Approach)

**Hình 7.1.** Các hướng tiếp cận tái cấu hình trong IoT

#### 7.2.1. Hướng tiếp cận thay thế toàn bộ image

Là cơ chế truyền tải và thay thế toàn bộ một tệp ảnh nhị phân nhúng (binary firmware image) đang chạy trên thiết bị IoT qua sóng vô tuyến (OTA). Một dịch vụ điển hình đã hiện thực cơ chế này trên thiết bị cảm biến không dây là giao thức **Deluge** trên TinyOS [18]."""

p[182] = """Trong hướng tiếp cận này, chương trình mới được biên dịch hoàn chỉnh tại máy chủ thành tệp nhị phân duy nhất. Tệp này sau đó được chia nhỏ thành các gói tin và lan truyền qua mạng không dây tới các nút cảm biến. Tại mỗi nút, ảnh nhị phân mới được ghi tạm vào bộ nhớ Flash ngoài. Sau khi toàn bộ ảnh được tải về và kiểm tra tính toàn vẹn (qua mã CRC/SHA), bộ nạp khởi động (bootloader) sẽ chép ảnh mới vào bộ nhớ Flash trong của vi điều khiển và khởi động lại thiết bị.

- **Ưu điểm:** Độ tin cậy rất cao, đơn giản về mặt kiến trúc; cho phép thay đổi toàn bộ hệ điều hành và ngăn xếp mạng; không phụ thuộc vào ngôn ngữ lập trình.
- **Nhược điểm:** Kích thước tệp truyền qua mạng rất lớn (vài chục đến vài trăm kB), tiêu tốn nhiều năng lượng truyền thông không dây của các nút cảm biến; thời gian cập nhật mạng lâu.

**Hình 7.2.** Quy trình nạp ảnh toàn phần OTA

#### 7.2.2. Hướng tiếp cận dựa trên module

Thay vì thay thế toàn bộ phần mềm, hướng tiếp cận này chỉ truyền tải các module phần mềm nhị phân cần cập nhật (dạng tệp mã đối tượng ELF hoặc thư viện liên kết động). Cơ chế nạp động (Dynamic Loader) trên hệ điều hành sẽ liên kết nóng module mới vào không gian bộ nhớ đang chạy."""

p[183] = """sao chép các native code được liên kết vào một nơi trong bộ nhớ mà ở đó chương trình có thể thực thi. Hình 7.3 mô tả kiến trúc bộ nhớ trong Contiki OS [19], giải thích vì sao hệ điều hành này có thể hỗ trợ cơ chế nạp module động. Không gian phần "Loaded program" chính là nơi các chương trình được nạp vào bộ nhớ RAM/Flash để thực thi mà không làm gián đoạn phần còn lại của nhân hệ điều hành.

**Hình 7.3.** Kiến trúc tái cấu hình dựa trên module [19]

- **Ưu điểm:** Kích thước gói tin cập nhật nhỏ hơn nhiều so với Full Image (chỉ từ 1kB đến vài kB), tiết kiệm đáng kể năng lượng vô tuyến và thời gian nạp mạng.
- **Nhược điểm:** Đòi hỏi hệ điều hành phải hỗ trợ bảng ký hiệu (symbol table) và cơ chế liên kết động phức tạp; có nguy cơ phân mảnh bộ nhớ RAM sau nhiều lần nạp/gỡ module.

#### 7.2.3. Hướng tiếp cận cơ sở dữ liệu (Database-based Approach)

Trong hướng tiếp cận này, toàn bộ mạng cảm biến không dây được trừu tượng hóa như một bảng cơ sở dữ liệu phân tán khổng lồ (Virtual Database Table), trong đó mỗi hàng đại diện cho một nút cảm biến và mỗi cột đại diện cho một loại cảm biến (nhiệt độ, ánh sáng, độ ẩm) hoặc thuộc tính của nút (mức pin, định danh nút)."""

p[184] = """Việc tái cấu hình hành vi của mạng cảm biến được thực hiện đơn giản bằng cách gửi một câu lệnh truy vấn dạng SQL từ trạm gốc (Base Station) vào mạng. Hệ thống định tuyến sẽ tự động phân phối câu truy vấn qua các tuyến đường tối ưu năng lượng đến các nút cảm biến.

**TinyDB** [20] là một giải pháp điển hình của thể loại này:
```sql
SELECT nodeid, light, temp
FROM sensors
WHERE temp > 25
SAMPLE PERIOD 10s
```

**Hình 7.4.** Kiến trúc tái cấu hình dựa trên cơ sở dữ liệu

- **Ưu điểm:** Rất trực quan và quen thuộc với người dùng; kích thước câu truy vấn cực kỳ nhỏ (vài chục byte), tiêu tốn rất ít năng lượng truyền thông; cho phép thay đổi tức thì chu kỳ lấy mẫu và điều kiện lọc dữ liệu.
- **Nhược điểm:** Tính linh hoạt bị giới hạn nghiêm ngặt trong khuôn khổ các toán tử truy vấn SQL sẵn có; không thể bổ sung logic tính toán phức tạp hoặc thuật toán định tuyến mới.

**Hướng tiếp cận Publish-Subscribe**"""

p[185] = """Các hệ thống trao đổi thông điệp Publish-Subscribe thông thường bao gồm ba thành phần:
1. **Publisher (Bên phát hành):** Sản xuất và phát hành các sự kiện dữ liệu (ví dụ: nhiệt độ phòng đo được bởi nút cảm biến không dây).
2. **Subscriber (Bên đăng ký):** Các ứng dụng hoặc thiết bị người dùng đăng ký nhận các chủ đề dữ liệu mà mình quan tâm.
3. **Broker (Bộ môi giới / Gateway):** Điểm trung tâm tiếp nhận thông điệp từ Publisher, lọc theo chủ đề (topic) và chuyển tiếp tới các Subscriber tương ứng.

Việc tái cấu hình trong mô hình này được thực hiện thông qua việc thay đổi các bộ lọc đăng ký (subscription filters) tại Broker hoặc gửi các thông điệp điều khiển cấu hình qua các kênh điều khiển chuyên dụng.

**MOSDEN Middleware** [22] là một giải pháp trung gian IoT tiêu biểu hỗ trợ cơ chế này trên các thiết bị di động và gateway có tài nguyên hạn chế."""

p[186] = """các sự kiện cụ thể của hệ thống. Mỗi client được phân biệt bằng một số điện thoại (phone number) hoặc UUID. Gateway đóng vai trò event-broker trong mô hình Publish-Subscribe. Mỗi gateway sẽ nhận thông tin từ nhiều nút cảm biến (publisher). Các thông tin này sẽ được phân loại vào những kênh được quy định trước (predefined channels). Sau đó, tương ứng với mỗi kênh, gateway sẽ thông báo tới các subscriber đã đăng ký.

#### 7.2.4. Hướng tiếp cận máy ảo (Virtual Machine-based Approach)

Hướng tiếp cận này cài đặt một máy ảo siêu nhỏ (Bytecode Virtual Machine) chạy trực tiếp trên vi điều khiển của nút cảm biến (nằm phía trên hệ điều hành nhúng). Các chương trình ứng dụng được biên dịch thành các chỉ lệnh mã byte (bytecode) nhỏ gọn để máy ảo thông dịch thực thi.

Đại diện tiêu biểu nhất cho hướng tiếp cận này là máy ảo **Maté** [18] chạy trên nền hệ điều hành TinyOS. Maté là một máy ảo hướng tới bối cảnh sự kiện dựa trên điều khiển (context-based event-driven virtual machine) với một chồng quy ước gọi hàm dựa trên ngăn xếp (stack-based calling convention)."""

p[187] = """**Hình 7.5.** Kiến trúc tái cấu hình dựa trên máy ảo VM

Máy ảo Maté tổ chức mã thực thi thành các viên nang (capsules) độc lập, mỗi capsule có kích thước cố định chỉ 24 byte (chứa tối đa 24 chỉ lệnh bytecode):
- **Capsule thông điệp (Message Capsule):** Chạy khi có gói tin mạng đến.
- **Capsule bộ định thời (Timer Capsule):** Chạy khi bộ định thời kích hoạt.
- **Capsule chương trình con (Subroutine Capsule):** Thực thi các hàm tính toán dùng chung.

Nhờ tập lệnh bytecode ngắn gọn được thiết kế riêng cho mạng cảm biến (chỉ thị đọc cảm biến, gửi gói tin, bật đèn LED chỉ tốn 1 byte mã lệnh), các chương trình phức tạp có thể được mã hóa thành các tệp tin có kích thước dưới 100 byte."""

p[188] = """cho phép các chương trình phức tạp có thể hiện thực với mã nguồn kích thước rất nhỏ (ít hơn 100 bytes). Điều này cho phép các nhà lập trình ứng dụng có thể tái cấu hình một mạng lưới rộng lớn các nút một cách hiệu quả, giảm chi phí truyền tải một chương trình mới đến các nút qua sóng vô tuyến.

- **Ưu điểm:** Kích thước truyền nạp siêu nhỏ, lan truyền cập nhật mạng cực nhanh, an toàn cao (mã bytecode chạy trong môi trường sandbox của máy ảo nên không thể gây treo hệ thống hay xung đột bộ nhớ).
- **Nhược điểm:** Tốc độ thực thi chậm hơn so với mã máy gốc (native code) do phải thông qua bước thông dịch; tốn thêm dung lượng bộ nhớ RAM và Flash của nút để chứa chương trình máy ảo.

#### 7.2.5. Hướng tiếp cận hướng tới dịch vụ (Service-Oriented Approach)

Trong hướng tiếp cận hướng dịch vụ (SOA), mỗi thiết bị IoT đóng vai trò là một nhà cung cấp dịch vụ (Service Provider) hoặc người tiêu thụ dịch vụ (Service Consumer). Các chức năng của thiết bị (đo nhiệt độ, điều khiển van tưới, định tuyến mạng) được trừu tượng hóa và đóng gói thành các dịch vụ web gọn nhẹ (CoAP, RESTful HTTP).

**Hình 7.6.** Kiến trúc tái cấu hình hướng dịch vụ"""

p[189] = """Hệ thống trung gian IoT (IoT Middleware) quản lý danh mục dịch vụ (Service Registry). Khi cần tái cấu hình hệ thống, người quản trị chỉ cần thay đổi quy trình kết hợp dịch vụ (Service Orchestration / Composition) hoặc nạp thêm các dịch vụ mới mà không làm ảnh hưởng đến các dịch vụ đang hoạt động khác.

### 7.3. Một số giải pháp hiện thực tái cấu hình trên các loại thiết bị phổ biến

#### 7.3.1. Cơ chế hỗ trợ tái lập trình từ xa trên TinyOS

Trên hệ điều hành TinyOS, giao thức tái lập trình mạng nổi tiếng nhất là **Deluge T2** [18]. Deluge là giao thức lan truyền dữ liệu tin cậy (reliable data dissemination) được thiết kế đặc biệt để phân phối các tệp ảnh nhị phân kích thước lớn qua mạng cảm biến không dây đa chặng (multi-hop WSN)."""

p[190] = """**Hình 7.7.** Quy trình truyền nạp Deluge trong TinyOS

**Một số đặc điểm kỹ thuật nổi bật của giao thức Deluge:**
1. **Thuật toán Trickle thích ứng mật độ (Density-aware Trickle Algorithm):** Deluge sử dụng cơ chế quảng bá thông điệp tóm tắt (Advertisement - ADV) dựa trên bộ định thời thích ứng Trickle. Khi mạng ổn định, chu kỳ phát ADV tăng theo cấp số nhân để tiết kiệm tối đa năng lượng vô tuyến. Khi phát hiện một nút có phiên bản ảnh mới hơn, chu kỳ Trickle lập tức được thu ngắn lại về mức mili-giây để nhanh chóng cập nhật cho toàn mạng.
2. **Cơ chế ức chế truyền trùng lặp (Suppression Mechanism):** Nếu một nút nghe thấy nhiều láng giềng đã gửi bản tin ADV hoặc yêu cầu tương tự trong chu kỳ hiện tại, nó sẽ tự động ức chế (không phát lại) để tránh va chạm và nghẽn kênh truyền."""

p[191] = """3. **Phân trang dữ liệu (Data Paging):** Một đối tượng dữ liệu nhị phân lớn ($S_{obj}$) được chia thành nhiều trang (Pages) có kích thước cố định (ví dụ 1024 byte), và mỗi trang được chia tiếp thành các gói tin nhỏ ($S_{pkt}$, khoảng 23 byte) để vừa với khung truyền IEEE 802.15.4.
   - Các nút mạng phải hoàn thành việc nhận và kiểm tra toàn vẹn toàn bộ các gói tin của Trang $i$ trước khi chuyển sang yêu cầu Trang $i+1$. Cơ chế này giúp các nút cảm biến chỉ cần duy trì một vùng đệm RAM nhỏ cho một trang đơn lẻ thay vì phải giữ toàn bộ ảnh nhị phân trong bộ nhớ.
4. **Cơ chế an toàn Golden Image:** Bộ nhớ Flash ngoài của mote cảm biến được dành riêng một phân vùng lưu trữ phiên bản phần mềm chuẩn xuất xưởng (Golden Image). Nếu quá trình nạp ảnh mới bị gián đoạn do hết pin hoặc ảnh mới bị lỗi không khởi động được, hệ thống sẽ tự động khôi phục lại Golden Image để đảm bảo nút mạng không bao giờ bị "biến thành cục gạch" (bricked)."""

p[192] = """Trong các giải pháp hiện đại, một máy tính nhúng nhỏ gọn như **Raspberry Pi** thường được cấu hình chạy môi trường TinyOS đóng vai trò là trạm gốc (Base Station Gateway) kết nối qua cổng USB với nút điều phối Coordinator. Raspberry Pi nhận các tệp ảnh nhị phân biên dịch từ đám mây qua Wi-Fi/Ethernet và tự động kích hoạt tiến trình nạp Deluge xuống mạng cảm biến.

#### 7.3.2. Cơ chế tái lập trình từ xa trên ESP8266

Họ vi điều khiển ESP8266 và ESP32 của Espressif Systems được tích hợp sẵn ngăn xếp Wi-Fi và TCP/IP, cung cấp khả năng cập nhật phần mềm không dây (OTA) cực kỳ mạnh mẽ và tiện lợi trong môi trường Arduino IDE và ESP-IDF."""

p[193] = """Hiện tại, trong hệ thống phần mềm và kho thư viện lập trình của ESP8266 trên nền tảng Arduino có 3 phương pháp tái cấu hình, cập nhật OTA từ xa qua mạng:
1. **Arduino IDE OTA:** Nạp mã trực tiếp từ máy tính của lập trình viên qua giao thức mạng nội bộ LAN tới thiết bị ESP8266 mà không cần cắm cáp USB.
2. **Web Browser OTA:** ESP8266 khởi tạo một Web Server nội bộ; người dùng truy cập địa chỉ IP của ESP8266 qua trình duyệt web trên điện thoại hoặc máy tính, chọn tệp nhị phân `.bin` và bấm nút Upload để nạp chương trình mới.
3. **HTTP Server Auto-Update (OTA qua máy chủ đám mây):** ESP8266 định kỳ gửi yêu cầu HTTP GET đến máy chủ web trung tâm kiểm tra phiên bản phần mềm. Nếu có phiên bản mới hơn, thiết bị tự động tải tệp nhị phân về và nạp vào bộ nhớ.

**Hình 7.8.** Cơ chế phân vùng Flash hỗ trợ OTA trên ESP8266"""

p[194] = """**Cơ chế phân vùng bộ nhớ Flash (Dual-Bank OTA):**

Bộ nhớ Flash của ESP8266 được phân chia thành hai vùng lưu trữ ứng dụng riêng biệt có kích thước bằng nhau:
- **Phân vùng Sketch 1 (OTA slot 0)**
- **Phân vùng Sketch 2 (OTA slot 1)**

**Hình 7.9.** Quy trình cập nhật OTA trên ESP8266 qua Web Server

Khi thiết bị đang chạy chương trình từ Phân vùng 1, tệp nhị phân mới tải về sẽ được ghi tuần tự vào Phân vùng 2. Sau khi ghi xong và xác thực mã kiểm tra MD5 thành công, cờ nạp khởi động (boot flag) trong bộ nhớ RTC/EEPROM sẽ được chuyển sang chỉ định Phân vùng 2. Thiết bị tự khởi động lại và chạy chương trình mới. Nếu quá trình ghi bị ngắt quãng, thiết bị vẫn khởi động an toàn từ Phân vùng 1 cũ."""

p[195] = """#### 7.3.3. Cơ chế tái cấu hình từ xa trên Raspberry Pi

Đối với các thiết bị máy tính nhúng mạnh mẽ chạy hệ điều hành Linux như Raspberry Pi, việc tái cấu hình có thể thực hiện ở hai mức độ:
1. **Mức hệ điều hành và Firmware (Full OS OTA):** Sử dụng các nền tảng quản lý cập nhật hệ thống nhúng chuyên nghiệp như **Mender** [23] hoặc **balenaOS**.
2. **Mức ứng dụng và dịch vụ:** Sử dụng công nghệ ảo hóa nhẹ **Docker Containers** kết hợp các công cụ quản lý cấu hình tự động như **Ansible**."""

p[196] = """**Giải pháp cập nhật hệ điều hành Mender:**

Mender là nền tảng mã nguồn mở quản lý cập nhật OTA cho hệ điều hành Linux nhúng. Mender áp dụng kiến trúc cập nhật **A/B Dual Rootfs Partitioning**:
- Ổ đĩa lưu trữ (thẻ nhớ MicroSD hoặc eMMC) được chia thành 2 phân vùng hệ thống tệp gốc: `rootfsA` và `rootfsB`.
- Thiết bị đang hoạt động trên `rootfsA`. Khi có bản cập nhật mới từ Mender Server, tệp ảnh hệ thống mới sẽ được ghi vào `rootfsB`.
- Bộ nạp khởi động U-Boot được cấu hình thử khởi động vào `rootfsB`. Nếu hệ thống khởi động thành công và xác nhận dịch vụ mạng hoạt động bình thường, phân vùng B sẽ trở thành phân vùng hoạt động chính thức. Nếu khởi động thất bại hoặc dịch vụ bị lỗi, U-Boot tự động quay ngược (rollback) về phân vùng A, đảm bảo tính liên tục tuyệt đối của hệ thống."""

p[197] = """**Giải pháp tái cấu hình mức dịch vụ bằng Docker Containers trên Raspberry Pi:**

Thay vì cập nhật toàn bộ hệ điều hành cồng kềnh (hàng trăm MB đến vài GB), giải pháp hiện đại là đóng gói từng ứng dụng IoT (dịch vụ đọc cảm biến, dịch vụ gateway MQTT, dịch vụ phân tích AI) vào các Docker Container riêng biệt chạy trên Raspbian OS.

**Hình 7.10.** Kiến trúc tái cấu hình trên Raspberry Pi sử dụng Ansible/Docker

- Khi cần cập nhật tính năng mới hoặc sửa lỗi, người quản trị chỉ cần đẩy (push) image container mới lên Docker Hub hoặc máy chủ lưu trữ riêng.
- Một tiến trình quản trị trên Raspberry Pi (hoặc công cụ Ansible/Docker Compose) nhận lệnh và tự động tải image mới về, dừng container cũ và khởi chạy container mới chỉ trong vài giây mà không cần khởi động lại bo mạch Raspberry Pi."""

p[198] = """Một điểm quan trọng khác là Docker là một nền tảng mã nguồn mở, chính vì thế Docker được cộng đồng phát triển mạnh mẽ để đóng góp và mở rộng khả năng của nó cho phù hợp với các nhu cầu ngày càng cao. Gần đây, trong nhiều nghiên cứu về phát triển hạ tầng IoT đa nền tảng, đảm bảo khả năng đáp ứng linh hoạt các yêu cầu khác nhau, công cụ ảo hóa Docker đang trở thành tiêu chuẩn thực tế.

### 7.4. Khung kiến trúc phát triển một giải pháp tái cấu hình IoT đa nền tảng dựa trên cách tiếp cận SDN

#### 7.4.1. Kiến trúc quản lý hệ thống IoT dựa trên SDN

Mạng điều khiển bằng phần mềm (Software-Defined Networking - SDN) là mô hình mạng tiên tiến phân tách rạch ròi giữa:
- **Mặt phẳng điều khiển (Control Plane):** Tập trung hóa logic định tuyến, quản lý cấu hình và ra quyết định thông minh vào bộ điều khiển trung tâm (SDN Controller).
- **Mặt phẳng chuyển tiếp dữ liệu (Data Plane):** Các thiết bị mạng chỉ thực hiện chuyển tiếp gói tin thuần túy theo các bảng luật (Flow Tables) được chỉ định bởi bộ điều khiển."""

p[199] = """Mạng cận biên (edge network) bao gồm một lượng lớn các thiết bị IoT đầu cuối như cảm biến, động cơ, thiết bị di động... Những thiết bị này thu thập dữ liệu và sau đó gửi về thiết bị cổng, máy trạm (gateway) trong vùng mạng truy cập. Để có thể giải quyết nhu cầu về khả năng đáp ứng, khả năng lập trình lại, những thiết bị này thường chạy những dịch vụ hỗ trợ khả năng cấu hình mềm dẻo.

**Hình 7.11.** Kiến trúc quản lý hệ thống IoT dựa trên SDN

Việc áp dụng SDN vào IoT mang lại khả năng tái cấu hình linh hoạt:
- **Tập trung hóa quản trị:** Người quản trị có thể giám sát toàn bộ trạng thái mạng và cập nhật chính sách phân phối dữ liệu từ một vị trí trung tâm duy nhất.
- **Tái cấu hình luồng dữ liệu mềm dẻo:** Thay đổi đường truyền gói tin, ưu tiên chất lượng dịch vụ (QoS) cho các gói tin cảnh báo khẩn cấp mà không cần thay đổi phần cứng thiết bị mạng."""

p[200] = """thực và thử nghiệm cách làm quản lý tập trung, lập trình lại cho kiến trúc IoT ở mức độ vùng mạng cận biên (edge network) và vùng mạng truy cập (access network).

#### 7.4.2. Khung kiến trúc xây dựng giải pháp tái cấu hình IoT (SD-IoTR)

Giải pháp kiến trúc **SD-IoTR (Software-Defined IoT Reconfiguration Framework)** được đề xuất nhằm hỗ trợ tái cấu hình đồng nhất cho các hệ thống IoT đa nền tảng (kết hợp đồng thời giữa các nút cảm biến TinyOS, nút vi điều khiển ESP8266/Arduino và các gateway Raspberry Pi).

Khung kiến trúc SD-IoTR bao gồm 3 lớp phân cấp theo chiều dọc (Hình 7.12):
1. **Lớp hệ thống (System / Device Layer):** Bao gồm các nút cảm biến và gateway vật lý, cài đặt các agent tái cấu hình tương ứng với từng nền tảng phần cứng (Deluge Agent trên TinyOS, OTA Handler trên ESP8266, Docker Daemon trên Raspberry Pi).
2. **Lớp trung gian (Middleware / Control Layer):** Là trung tâm điều khiển trung tâm (SD-IoTR Controller), tiếp nhận các yêu cầu tái cấu hình từ tầng trên, biên dịch thành các lệnh điều khiển cụ thể cho từng loại thiết bị và giám sát tiến trình cập nhật.
3. **Lớp ứng dụng (Application Layer):** Cung cấp giao diện đồ họa web cho người quản trị thực hiện quản lý danh mục thiết bị, giám sát trạng thái mạng và phát lệnh cập nhật phần mềm."""

p[201] = """**Hình 7.12.** Khung kiến trúc tái cấu hình đa nền tảng SD-IoTR

Lớp trung gian Middleware cung cấp các bộ điều khiển logic:
- **Device Manager:** Quản lý vòng đời và thông tin cấu hình phần cứng của từng nút.
- **Reconfiguration Engine:** Quyết định chiến lược tái cấu hình phù hợp nhất cho từng thiết bị (chọn nạp Full Image, nạp Module hay nạp Container tùy theo tài nguyên thiết bị).
- **Security & Verification Module:** Ký số các bản cập nhật phần mềm và kiểm tra tính toàn vẹn nhằm ngăn chặn việc kẻ tấn công nạp mã độc vào hệ thống IoT."""

p[202] = """Hệ thống cung cấp tập hợp các giao diện lập trình ứng dụng RESTful APIs phong phú để các ứng dụng ở tầng trên có thể kích hoạt quá trình tái cấu hình:
- `POST /api/v1/devices/{id}/firmware`: Phát lệnh cập nhật firmware từ xa cho thiết bị có định danh `{id}`.
- `GET /api/v1/devices/{id}/status`: Kiểm tra trạng thái tiến độ nạp mã hiện tại.
- `POST /api/v1/containers/{id}/restart`: Khởi động lại hoặc cập nhật container dịch vụ trên gateway.
- `POST /api/v1/network/rules`: Cập nhật bảng luật định tuyến luồng dữ liệu SDN cho toàn mạng."""

p[203] = """giao tiếp chủ yếu bằng các REST APIs. HTTP REST được hiện thực mang đến khả năng giao tiếp dựa trên nền tảng web giữa các ứng dụng IoT cụ thể với hệ thống điều khiển ở trung tâm. Bên cạnh đó, giao thức MQTT với cơ chế Publish/Subscribe cũng được sử dụng kết hợp để gửi các bản tin đánh thức và kích hoạt nạp mã tức thời tới hàng nghìn thiết bị phân tán.

### 7.5. Ứng dụng của chức năng tái cấu hình trong hệ thống IoT và các định hướng nghiên cứu

Khả năng tái cấu hình từ xa mở ra nhiều ứng dụng thiết thực và quan trọng:
1. **Bảo trì và vận hành hệ thống quy mô lớn tự động:** Cập nhật đồng loạt hàng nghìn thiết bị đo đếm điện tử thông minh (Smart Metering) trên toàn quốc mà không cần cử nhân viên kỹ thuật tới từng hộ gia đình.
2. **Thích ứng với sự cố mạng và tiết kiệm năng lượng:** Tự động điều chỉnh cấu trúc mạng tô-pô khi có một số nút trung gian bị hết pin, chuyển giao vai trò Cluster Head cho các nút còn nhiều năng lượng hơn."""

p[204] = """3. **Thay đổi dịch vụ mạng, kiến trúc, kết nối mạng từ xa:** Ngày nay, khi IoT được ứng dụng và triển khai trong nhiều lĩnh vực khác nhau, kiến trúc mạng của hệ thống IoT thường rất phức tạp và triển khai với quy mô lớn. Chính vì thế, các công nghệ mạng hiện đại như SDN/NFV cho phép thực hiện việc cấu hình kết nối mạng từ xa, thay đổi các chức năng mạng, dịch vụ mạng một cách tiện lợi mang lại nhiều ý nghĩa trong việc vận hành và tối ưu hệ thống.

## BÀI TẬP CHƯƠNG 7

1. Hãy trình bày mục đích và vai trò của tái cấu hình/tái lập trình trong ứng dụng IoT.
2. Hãy so sánh các phương pháp tái cấu hình trong IoT.
3. Hãy phân tích ưu, nhược điểm của phương pháp tái cấu hình Full image.
4. Hãy trình bày một kịch bản tái cấu hình trong ứng dụng Thành phố thông minh.
5. Hãy xây dựng ứng dụng giám sát chất lượng không khí sử dụng nền tảng Arduino và Jetson Nano. Sau đó xây dựng kịch bản tái cấu hình cho ứng dụng này.
6. Hãy xây dựng ứng dụng y tế thông minh áp dụng công nghệ Docker/Container trong tính toán cận biên và hỗ trợ tái cấu hình mức Docker/Container.
7. Hãy xây dựng ứng dụng nông nghiệp thông minh hỗ trợ tái cấu hình mức độ thay đổi tham số.
8. Hãy xây dựng ứng dụng giám sát giao thông thông minh sử dụng máy học. Sau đó xây dựng kịch bản tái cấu hình mức độ thay đổi chức năng của ứng dụng.
9. Hãy xây dựng ứng dụng Nông nghiệp thông minh có kiến trúc mạng cluster. Sau đó xây dựng kịch bản tái cấu hình cho một cluster trong mô hình.
10. Hãy trình bày một phương pháp tái cấu hình ứng dụng kiến trúc mạng được định nghĩa bởi phần mềm (Software Defined Networking) và mô tả vai trò của mỗi thành phần trong kiến trúc này."""

p[205] = """# KẾT LUẬN

Trong cuốn sách này, chúng tôi đã tập trung vào những nội dung sau:

**Chương 1:** Trình bày tổng quan về công nghệ Internet vạn vật (IoT), các xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam. Trong đó, chúng tôi đặc biệt chú trọng đến quy chuẩn về IoT của các tổ chức hoặc liên minh quốc tế nhằm cung cấp đến người đọc, đặc biệt là sinh viên kiến thức về các tiêu chuẩn IoT. Mục tiêu là để định hướng khi thiết kế và phát triển các ứng dụng và giải pháp IoT có tính tương thích (compatibility) và sẵn sàng cao (portability).

**Chương 2:** Trình bày các lĩnh vực và ứng dụng IoT cụ thể nhằm giới thiệu đến sinh viên các ứng dụng IoT thực tế. Để tăng tính thực tiễn, chúng tôi cũng đã giới thiệu các ứng dụng IoT đã và đang triển khai ở Trường Đại học Công nghệ Thông tin – Đại học Quốc gia TP.HCM, ví dụ như trạm quan trắc môi trường SmartCity đặt trong khuôn viên Trường Đại học CNTT.

**Chương 3:** Trình bày các kiến trúc mạng khác nhau được sử dụng trong việc kiến thiết mạng IoT như kiến trúc cây (Tree), kiến trúc vòng (Ring), kiến trúc chuỗi (Chain), kiến trúc không cần hạ tầng (Mesh). Các bộ giao thức mạng IoT phổ dụng cũng đã được giới thiệu chi tiết về kiến trúc và cách vận hành. Trong khi bộ giao thức ZigBee đại diện cho xu hướng giao thức IoT chạy độc lập, và do đó muốn kết nối đến thiết bị đầu cuối từ mạng Internet cần thông qua một Internet gateway, bộ giao thức 6LoWPAN đại diện cho xu hướng mở rộng mạng IP (Spanning IP), tức là có thể truy cập và điều khiển trực tiếp thiết bị IoT từ Internet.

**Chương 4:** Trình bày về các nền tảng phần cứng và phần mềm phổ dụng để phát triển các ứng dụng và giải pháp IoT hiện nay. Chúng tôi giới thiệu chủ yếu các nền tảng phần cứng dễ dàng làm việc với các nền tảng mã nguồn mở (open-source"""

p[206] = """platforms) và có sẵn ở Việt Nam với giá thành hợp lý, từ đó sinh viên có thể dễ dàng phát triển sản phẩm và làm chủ công nghệ.

**Chương 5:** Trình bày về các công nghệ nền, bao gồm điện toán đám mây (cloud computing) và tính toán cận biên (edge computing). Đây là các công nghệ nền phát triển hiện nay để hiện thực hoàn chỉnh giải pháp phần backend hoặc edge của giải pháp IoT. Chúng tôi cũng đã giới thiệu giải pháp ứng dụng điện toán đám mây để phát triển hệ thống giả lập mạng cảm biến không dây quy mô lớn trên nền tảng OpenStack.

**Chương 6:** Trình bày các khái niệm cơ bản về ngữ cảnh, quản lý ngữ cảnh thông minh và ứng dụng của trí tuệ nhân tạo, học máy trong IoT. Các kỹ thuật mô hình hóa ngữ cảnh và suy luận ngữ cảnh (như logic mờ, học máy) được phân tích chi tiết nhằm trang bị cho sinh viên năng lực xây dựng các hệ thống IoT có khả năng tự nhận thức và thích ứng thông minh với môi trường.

**Chương 7:** Trình bày về các kỹ thuật tái cấu hình và tái lập trình từ xa (OTA) trong IoT. Phân tích các hướng tiếp cận tái cấu hình từ mức nạp ảnh nhị phân, nạp module, nạp bytecode máy ảo cho đến nạp container trên các thiết bị phổ biến như TinyOS, ESP8266 và Raspberry Pi, cùng khung kiến trúc SDN hỗ trợ quản lý và tái cấu hình mạng IoT đa nền tảng tập trung.

Mặc dù đã có những bước tiến vượt bậc, nhiều thách thức kỹ thuật lớn trong lĩnh vực IoT vẫn đang là các chủ đề nghiên cứu mở đầy sôi động:"""

p[207] = """- **Vấn đề bảo mật và quyền riêng tư (Security & Privacy):** Bên cạnh tính riêng tư, tính bảo mật cho ứng dụng IoT cũng là một vấn đề lớn đang được nghiên cứu. Các kỹ thuật bảo mật truyền thống khó có thể được triển khai trực tiếp trên các thiết bị IoT bởi vì như đã trình bày trong Chương 4, các thiết bị IoT hầu như là các thiết bị nhúng có năng lực tính toán, bộ nhớ và năng lượng tiêu thụ thấp. Một số rủi ro bảo mật chính gồm: nghe lén trên đường truyền vô tuyến, giả mạo nút mạng, chiếm quyền điều khiển thiết bị cơ cấu chấp hành và tấn công từ chối dịch vụ (DDoS) thông qua mạng botnet IoT.
- **Tiêu chuẩn hóa và tính liên tác (Standardization & Interoperability):** Sự phân mảnh của hàng trăm chuẩn kết nối và nền tảng phần mềm khác nhau từ các nhà sản xuất đòi hỏi các chuẩn giao tiếp chung ở mức ngữ nghĩa (như Web of Things - WoT của W3C) để các thiết bị có thể tự động khám phá và liên tác không rào cản.
- **Công nghệ mạng 5G và 6G trong IoT:** Hỗ trợ kết nối mật độ siêu lớn (massive Machine-Type Communications - mMTC) và truyền thông độ trễ cực thấp độ tin cậy cực cao (Ultra-Reliable Low-Latency Communications - URLLC) mở ra tương lai cho các hệ thống xe tự hành thông minh và phẫu thuật y tế từ xa."""

p[208] = """- **Học sâu và Trí tuệ nhân tạo trên thiết bị biên (Edge AI / TinyML):** Để giảm kích thước sử dụng bộ nhớ, các hệ điều hành IoT thường được tối giản các chức năng và sử dụng thư viện bên thứ ba ở mức tối thiểu, trong khi đó các ứng dụng Học sâu lại yêu cầu tài nguyên cao và sử dụng năng lượng nhiều. Do đó, việc nghiên cứu tối ưu hóa các thuật toán học máy, lượng tử hóa mô hình để có thể chạy suy luận thời gian thực trực tiếp trên các vi điều khiển công suất thấp mà vẫn đảm bảo độ chính xác cao là một trong những định hướng nghiên cứu then chốt trong giai đoạn hiện nay.

Cuốn giáo trình này được biên soạn với mong muốn cung cấp một tài liệu học tập, tham khảo có hệ thống, kết hợp hài hòa giữa lý thuyết nền tảng và hướng dẫn thực hành thực tiễn cho sinh viên ngành Công nghệ Thông tin, Kỹ thuật Máy tính, Điện tử Viễn thông và các kỹ sư đang nghiên cứu, phát triển trong lĩnh vực Internet of Things."""

p[209] = """# TÀI LIỆU THAM KHẢO

1. Manjhi, Amit, Nath, Suman, Gibbons, P. B., "Tributaries and deltas: efficient and robust aggregation in sensor network streams", trong *Proceedings of the 2005 ACM SIGMOD International Conference on Management of Data*, Baltimore, Maryland, 2005.
2. P. Skraba, Q. Fang, A. Nguyen và L. Guibas, "Sweeps over wireless sensor networks", trong *Proceedings of the 5th International Conference on Information Processing in Sensor Networks (IPSN '06)*, Nashville, Tennessee, USA, 2006.
3. J. Olsson, "6LoWPAN demystified", Texas Instruments, Texas, 2014.
4. J. W. Hui và D. E. Culler, "Extending IP to Low-Power, Wireless Personal Area Networks", *IEEE Internet Computing*, tập 12, số 4, pp. 37-45, 2008.
5. O. Hahm, E. Baccelli, H. Petersen và N. Tsiftes, "Operating Systems for Low-End Devices in the Internet of Things: A Survey", *IEEE Internet of Things Journal*, tập 3, số 5, pp. 720-734, 2016.
6. Memsic, "TelosB Mote Datasheet", [Trực tuyến]. Available: http://www.memsic.com.
7. B. Kiran, J. Singh và D. S. Kapoor, "Create Your Own Internet of Things", *IEEE Consumer Electronics Magazine*, pp. 57-68, 2017.
8. D. Gay, P. Levis, D. Culler và E. Brewer, "nesC 1.3 Language Reference Manual", 2009.
9. D. I. A. Riener, "Sensor Network Application Development", Linz, 2007.
10. Advanticsys, "Tech Resources: Getting started with nesC", [Trực tuyến]. Available: http://www.advanticsys.com/wiki/.
11. P. Levis, "TEP 102: Timers", TinyOS Core Working Group, [Trực tuyến]. Available: http://www.tinyos.net/tinyos-2.1.0/doc/html/tep102.html.
12. P. Levis, "TEP 111: message_t", TinyOS Core Working Group, [Trực tuyến]. Available: http://www.tinyos.net/tinyos-2.1.0/doc/html/tep111.html.
13. J. Hui, P. Levis và D. Moss, "TinyOS 802.15.4 Frames", TinyOS Documentation.
14. A. Dunkels, B. Grönvall và T. Voigt, "Contiki - a lightweight and flexible operating system for tiny networked sensors", trong *29th Annual IEEE International Conference on Local Computer Networks (LCN)*, 2004."""

p[210] = """15. M. H. Qutqut, A. Al-Sakran, F. Almasalha và H. S. Hassanein, "Comprehensive survey of the IoT open source OSs", *IET Wireless Sensor Systems*, tập 8, số 6, pp. 323-339, 2018.
16. A. Alnoman, S. K. Sharma, W. Ejaz và A. Anpalagan, "Emerging Edge Computing Technologies for Distributed IoT Systems", *IEEE Network*, tập 33, số 6, pp. 140-147, 2019.
17. Charith Perera, Arkady Zaslavsky, Peter Christen và Dimitrios Georgakopoulos, "Context Aware Computing for The Internet of Things: A Survey", *IEEE Communications Surveys & Tutorials*, tập 16, số 1, pp. 414-454, 2014.
18. J. W. Hui và D. Culler, "The dynamic behavior of a data dissemination protocol for network programming at scale", trong *Proceedings of the 2nd International Conference on Embedded Networked Sensor Systems (SenSys '04)*, Baltimore, MD, USA, 2004, pp. 81-94.
19. A. Dunkels, N. Finne, J. Eriksson và T. Voigt, "Run-time dynamic linking for reprogramming wireless sensor networks", trong *Proceedings of the 4th International Conference on Embedded Networked Sensor Systems (SenSys '06)*, Boulder, Colorado, USA, 2006.
20. S. R. Madden, M. J. Franklin, J. M. Hellerstein và W. Hong, "TinyDB: an acquisitional query processing system for sensor networks", *ACM Transactions on Database Systems (TODS)*, tập 30, số 1, pp. 122-173, 2005.
21. T. D. Nguyen, Q. M. Nguyen và H.-A. Pham, "Publish-Subscribe Framework for Event Management in IoT-based Applications", trong *11th South East Asian Technical University Consortium (SEATUC) Symposium*, Ho Chi Minh City, Vietnam, 2017.
22. C. Perera, P. P. Jayaraman, A. Zaslavsky, P. Christen và D. Georgakopoulos, "MOSDEN: An Internet of Things Middleware for Resource Constrained Mobile Devices", trong *47th Hawaii International Conference on System Sciences*, Waikoloa, HI, USA, 2014, pp. 1053-1062.
23. I. Grokhotkov, "ESP8266 Arduino Core OTA Updates", [Trực tuyến]. Available: https://arduino-esp8266.readthedocs.io/en/latest/ota_updates/readme.html.
24. L.-V. Hung, H.-V. Dang và L.-T. Quan, "UITIoT-Vlab: A Low Cost Physical IoTs Testbed Based on Over-The-Air Programming Approach", trong *5th EAI International Conference on Industrial Networks and Intelligent Systems (INISCOM 2019)*, Ho Chi Minh City, Vietnam, 2019."""

p[211] = """25. O. Hahm, E. Baccelli, H. Petersen và N. Tsiftes, "Operating Systems for Low-End Devices in the Internet of Things: A Survey", *IEEE Internet of Things Journal*, tập 3, số 5, pp. 720-734, 2016.
26. F. Javed, M. K. Afzal, M. Sharif và B. S. Kim, "Internet of Things (IoT) Operating Systems Support, Networking Technologies, Applications, and Challenges: A Comparative Review", *IEEE Communications Surveys & Tutorials*, tập 20, số 3, pp. 2062-2100, 2018.
27. P. Mathur, "A Simple Weather Forecasting Model Using Mathematical Regression", *International Journal of Computer Science and Network Security*, 2012.
28. Alessandro Floris và Luigi Atzori, "Managing the Quality of Experience in the Multimedia Internet of Things: A Layered-Based Approach", *Sensors*, tập 16, số 12, tr. 2057, 2016.
29. T. F. Megahed, S. Abdelkader và A. Zakaria, "Energy Management in Zero-Energy Building Using Neural Network Predictive Control", *IEEE Internet of Things Journal*, 2019.
30. A. Gaur, B. Scotney, G. Parr và S. McClean, "Smart City Architecture and its Applications Based on IoT", *Procedia Computer Science*, tập 52, pp. 1089-1094, 2015.
31. P. Rahimi and C. Chrysostomou, "Improving the Network Lifetime and Performance of Wireless Sensor Networks for IoT Applications Based on Fuzzy Logic", trong *15th International Conference on Distributed Computing in Sensor Systems (DCOSS)*, Santorini Island, Greece, 2019, pp. 667-674.
32. Qianqian Li, Sarada Gochhayat, Mauro Conti và Fang-Ai Liu, "EnergIoT: A solution to improve network lifetime of IoT devices", *Pervasive and Mobile Computing*, tập 42, pp. 124-138, 2017.
33. V. Valls, G. Iosifidis and T. Salonidis, "Maximum Lifetime Analytics in IoT Networks", trong *IEEE INFOCOM 2019 - IEEE Conference on Computer Communications*, Paris, France, 2019, pp. 1369-1377.
34. F. Wang, M. Zhang, X. Wang, X. Ma and J. Liu, "Deep Learning for Edge Computing Applications: A State-of-the-Art Survey", *IEEE Access*, tập 8, pp. 58322-58336, 2020.
35. M. G. Sarwar Murshed, Christopher Murphy, Daqing Hou, Nazar Khan, Ganesh Ananthanarayanan và Faraz Hussain, "Machine Learning at the Network Edge: A Survey", *ACM Computing Surveys*, 2019."""

p[212] = """36. Abu Sufian, Aniruddha Ghosh, Ali Safaa Sadiq, Florentin Smarandache, "A Survey on Deep Transfer Learning to Edge Computing for Mitigating the COVID-19 Pandemic", *Journal of Systems Architecture*, tập 108, tr. 101830, 2020.
37. W. Y. B. Lim et al., "Federated Learning in Mobile Edge Networks: A Comprehensive Survey", *IEEE Communications Surveys & Tutorials*, tập 22, số 3, pp. 2031-2063, 2020.
38. Jie Tang, Dawei Sun, Shaoshan Liu và Jean-Luc Gaudiot, "Enabling Deep Learning on IoT Devices", *Computer*, tập 50, số 6, pp. 92-96, 2017."""

p[213] = """# THÔNG TIN XUẤT BẢN

**GIÁO TRÌNH: CÔNG NGHỆ INTERNET OF THINGS VÀ ỨNG DỤNG**

- **Tác giả:**
  - PGS. TS. Lê Trung Quân
  - TS. Huỳnh Văn Đặng
  - ThS. Nguyễn Khánh Thuật

- **Đơn vị công tác:** Trường Đại học Công nghệ Thông tin – Đại học Quốc gia Thành phố Hồ Chí Minh.
- **Nhà xuất bản:** Nhà xuất bản Đại học Quốc gia Thành phố Hồ Chí Minh.
- **Địa chỉ:** Khu phố 6, Phường Linh Trung, Thành phố Thủ Đức, Thành phố Hồ Chí Minh.
- **Năm xuất bản:** 2021.
- **Chịu trách nhiệm xuất bản:** Ban Giám đốc Nhà xuất bản ĐHQG-HCM.
- **Biên tập:** Nhà xuất bản Đại học Quốc gia TP. Hồ Chí Minh."""

p[214] = """*(Trang bìa sau của sách giáo trình)*"""

# Apply to GT_IoT_Manual.md
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(^## Trang \d+\s*$)', text, flags=re.MULTILINE)
pages_dict = {}
for i in range(1, len(parts), 2):
    p_num = int(re.search(r'\d+', parts[i]).group(0))
    pages_dict[p_num] = parts[i+1]

for page_num in range(179, 215):
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

print("Chapter 7 and Conclusion/References (pages 179-214) updated successfully!")
