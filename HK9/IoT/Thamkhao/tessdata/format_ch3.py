# -*- coding: utf-8 -*-
import sys, re

# Page 52 to 82 content
p = {}

p[52] = """# CHƯƠNG 3. CÁC KIẾN TRÚC MẠNG VÀ BỘ GIAO THỨC MẠNG IOT

Các hệ thống Internet của vạn vật thường bao gồm rất nhiều thiết bị kết nối với nhau để trao đổi dữ liệu thu thập cũng như các tín hiệu điều khiển trong mạng. Nhiều kiến trúc mạng cũng như các bộ giao thức mạng đặc biệt dùng trong IoT đã được nghiên cứu và phát triển để tạo nên một cơ chế truyền gửi dữ liệu một cách hiệu quả giữa các nốt trong mạng IoT.

Nội dung chương này trình bày những kiến thức cơ bản về một số kiến trúc mạng thường sử dụng trong IoT cũng như giới thiệu một số chuẩn kết nối mạng được dùng nhiều trong các hệ thống IoT. Các kiến trúc mạng được trình bày theo thứ tự từ những kiến trúc mạng truyền thống được sử dụng thường xuyên trong các hệ thống mạng máy tính thông thường như kiến trúc cây (tree), kiến trúc mắt lưới (mesh), kiến trúc vòng (ring), kiến trúc chuỗi (chain) và kiến trúc lưới (grid). Tiếp theo đó, một số kiến trúc mạng hiện đại cũng được đề cập như kiến trúc phụ lưu - đồng bằng (Tributary - Delta), kiến trúc dựa theo cụm (cluster-based), kiến trúc làn sóng (sweep). Phần còn lại của chương này trình bày một số đặc điểm kỹ thuật của các bộ giao thức mạng thường dùng trong IoT, bao gồm: 6LoWPAN, giao thức WiFi, Zigbee. Đây là các bộ giao thức được dùng phổ biến để hiện thực cơ chế truyền thông giữa các thiết bị trong mạng IoT.

Thông qua nội dung chương này, người đọc có cái nhìn tổng quan về cơ chế truyền gửi dữ liệu giữa các nốt IoT trong mạng cùng các tiêu chuẩn kỹ thuật, những đặc trưng cơ bản của các chồng giao thức mạng không dây được trình bày. Nắm vững những đặc điểm cơ bản này, người đọc có thể thực hiện các nghiên cứu, phân tích, đánh giá, chọn lựa các kiến trúc mạng, các bộ giao thức IoT phù hợp khi triển khai các giải pháp IoT trong thực tế."""

p[53] = """### 3.1. Các kiến trúc mạng dùng trong IoT

#### 3.1.1. Một số kiến trúc mạng đơn giản

**Kiến trúc mắt lưới (mesh)**

Trong mô hình mạng Mesh, gói tin từ một nút có thể có nhiều đường đi đến đích. Đây là một trong những ưu điểm của mô hình mạng mesh (trong mô hình dạng vòng mặc dù có hai đường đi, tin nhắn chỉ có thể đi theo một hướng). Trong Hình 3.1, các nút có thể kết nối đến tất cả các nút còn lại trong mạng được gọi là một mạng mesh đầy đủ (full mesh). Trong Hình 3.2, mô hình mạng mesh có một số nút có kết nối gián tiếp đến các nút khác trong mạng được gọi là mạng mesh một phần (partial mesh).

**Hình 3.1.** Kiến trúc full mesh | **Hình 3.2.** Kiến trúc Partial Mesh

**Kiến trúc cây (tree)**

Mạng sử dụng một hub trung tâm được gọi là một nút gốc, xem như là một bộ định tuyến thông tin liên lạc chính. Hình 3.3 mô tả một hệ thống phân cấp, cấp dưới nút gốc là các hub trung tâm, mức thấp này tạo thành một mạng sao. Các mạng dạng cây có thể được coi là sự lai tạo của mạng hình sao và mạng Peer to Peer. Trong đường dẫn mạng cảm biến có thể là single hop hoặc multi hop, các nút cảm biến nhận dữ liệu của môi trường rồi gửi chúng đến bộ phận thu nhận (Sink), sau đó chuyển tiếp chúng đến các nút cha mẹ. Điều quan trọng là để tìm đường đi ngắn nhất sao cho tối ưu với thời gian sống tối đa và độ trễ ngắn hơn mặc dù độ phức tạp thời gian hơi cao nhưng phù hợp hơn cho việc thực hiện phân phối. Mạng dạng cây có vấn đề trong"""

p[54] = """chương trình cân bằng tải tại mỗi mức của cây và có thông tin liên lạc giữa hai nút. Nếu có một liên kết có vấn đề trong truyền dẫn trên tuyến đường hoạt động thì việc truyền thông cũng bị phá vỡ.

**Hình 3.3.** Kiến trúc Tree

**Kiến trúc vòng (ring)**

Hình 3.4 mô tả một mô hình mạng có kiến trúc vòng, mỗi nút có đúng hai người hàng xóm cho mục đích truyền thông. Tất cả các tin nhắn đi qua một vòng trong cùng một hướng (hoặc là "chiều kim đồng hồ" hay "ngược chiều kim đồng hồ"). Nếu một nút trong vòng gặp vấn đề thì có thể phá vỡ các vòng lặp và cũng có thể làm sụp đổ toàn bộ mạng. Tin nhắn trong mô hình này có hai đường đi nhưng chỉ có thể đi theo một hướng.

**Hình 3.4.** Kiến trúc Ring

**Kiến trúc chuỗi (chain)**

Trong một mạng dạng chain, các nút kết nối với nhau thành dạng chuỗi như Hình 3.5 bên dưới. Ngoài nút đầu và nút cuối,"""

p[55] = """mỗi nút trong mạng chain có đúng hai người hàng xóm cho mục đích truyền thông. Nếu một nút trong chuỗi gặp vấn đề thì có thể ảnh hưởng đến việc gửi nhận thông tin của cả mạng.

**Hình 3.5.** Kiến trúc chuỗi

**Kiến trúc sao (Star)**

Mạng hình sao được kết nối với một hub đóng vai trò là bộ phận truyền thông trung tâm (Sink) và các nút (các nút này không thể giao tiếp trực tiếp với nhau). Hình 3.6 là một ví dụ về mô hình mạng sao có một nút trung tâm và năm nút đầu cuối. Toàn bộ thông tin liên lạc phải được định tuyến thông qua hub trung tâm. Mỗi nút là một "client", trong khi hub trung tâm là "server hoặc sink". Nhưng mô hình này có nhược điểm là chỉ có một đường giao tiếp duy nhất.

**Hình 3.6.** Star Topology

**Kiến trúc lưới (Grid)**

Các trường cảm biến mạng được chia thành các đường kẻ ô. Các vùng mạng được chia thành lưới ô vuông không chồng lên nhau với cùng một kích thước. Hình 3.7 mô tả một ứng dụng dựa trên kiến trúc lưới. Nên có ít nhất một và chỉ một nút trong trạng thái làm việc trong mỗi lưới tại bất cứ khoảng thời gian nào. Để kéo dài thời gian sống mạng, các nút trong một mạng lưới nên hoạt động lần lượt. Bên trong mỗi lưới, một nút được chọn như là lưới đầu tiên có trách nhiệm chuyển tiếp thông tin"""

p[56] = """định tuyến và truyền gói dữ liệu. Định tuyến được thực hiện trong lần lượt từ lưới này đến các lưới khác. Mô hình dựa vào giao thức định tuyến đa đường dựa vào các lưới mạng để định tuyến các gói tin một cách nhanh nhất, tận dụng và mở rộng các nút cảm biến năng lượng ngoài để tránh và xử lý tắc nghẽn mạng khi chúng xảy ra trong mạng.

**Hình 3.7.** Kiến trúc lưới

#### 3.1.2. Một số kiến trúc mạng phức tạp

**Kiến trúc dựa theo cụm (cluster-based)**

Kiến trúc dựa theo cụm/nhóm (cluster-based) là kiến trúc mà các thiết bị cảm biến thu thập dữ liệu và gửi về một thiết bị đầu cụm (cluster head). Hình 3.8 là một ví dụ về mạng cảm biến có kiến trúc gồm 6 cluster, mỗi cluster được quản lý bởi một Cluster Head. Cách làm này mang đến hiệu quả cao trong trường hợp hệ thống mạng cảm biến có kích thước lớn, khoảng cách xa nhau và định tuyến qua nhiều mức (multihop routing). Kiến trúc dựa trên cụm này làm giảm lượng dữ liệu truyền gửi giữa tất cả các cảm biến so với kiến trúc khác như mesh. Một số kỹ thuật tinh giảm dữ liệu (reduction techniques) có thể được áp dụng để tăng cường hiệu quả. Tuy nhiên, kiến trúc dựa trên cụm này có khuyết điểm là nếu thiết bị đầu cụm ở quá xa các thiết bị cảm biến thì sẽ làm tăng chi phí truyền thông, năng lượng tiêu thụ."""

p[57] = """**Hình 3.8.** Kiến trúc dựa theo cụm (cluster-based)

**Kiến trúc dựa trên địa hình phụ lưu - đồng bằng (Tributary - Delta)**

Kiến trúc Tributary - Delta [1], được hình thành từ ý tưởng dòng chảy của con sông, là một cách tiếp cận mới trong tập hợp dữ liệu trong mạng. Kiến trúc này là kết quả của việc kết hợp các ưu thế của kiến trúc dựa trên kiến trúc cây (tree-based) và định tuyến đa luồng (multi-path routing). Hình 3.9 là một ví dụ về kiến trúc Tributary - Delta, mô hình mạng được chia làm hai vùng riêng biệt: Tributary và Delta. Trong mạng độ lỗi thấp, kiến trúc cây được sử dụng cho các thông điệp có kích thước nhỏ, trong trường hợp độ lỗi cao, dữ liệu thu thập từ rất nhiều cảm biến thì multi-path routing được sử dụng để đảm bảo hiệu quả.

**Hình 3.9.** Kiến trúc Tributary - Delta [1]"""

p[58] = """**Kiến trúc dựa theo làn sóng (Sweep)**

**Hình 3.10.** Kiến trúc dựa theo làn sóng [2]

Đây là kiến trúc thu thập dữ liệu dựa trên ý tưởng hoạt động của làn sóng mà ở đó dữ liệu đi ngang qua mỗi thiết bị đúng một lần và thực hiện các hành động theo ý muốn [2]. Kiến trúc mạng sweep được hiện thực bởi một nhóm nhỏ các nốt hoạt động, các nốt này di chuyển qua mạng bằng cách phát một thông điệp lời mời tới các nốt mới để tham gia vào nhóm và loại bỏ các nốt đã thực hiện rồi nhưng không đóng vai trò quan trọng gì khác. Đặc trưng quan trọng của kiến trúc này là tính chất bền vững bởi mặc dù một kiến trúc cây được sử dụng cho một phần tác vụ tổng hợp dữ liệu trong một nhóm hoạt động thì những cây này là cục bộ và được dùng hầu hết ngay khi chúng được xây dựng. Đường tổng hợp dữ liệu được phân chia trên đường quét và không cần thiết phải có một cấu trúc cây cố định cho việc tính toán. Vì vậy, cách tiếp cận này có tính vững vàng ngay cả với các liên kết có sự biến động và nhiều nút bị hỏng. Hình 3.10 mô tả kiến trúc mạng theo làn sóng, trong đó, các nốt trong vùng màu đỏ đang hoạt động, các nốt trong vùng màu xanh đã hoạt động và các nốt màu trắng chưa tham gia vào mạng."""

p[59] = """### 3.2. Các bộ giao thức mạng không dây thường dùng trong IoT

Để triển khai được các kiến trúc truyền tải dữ liệu như trình bày ở phần trên, các nền tảng phần mềm, hệ điều hành chạy trên thiết bị IoT phải hỗ trợ các chuẩn kết nối không dây mà ở đó những cơ chế, giải thuật định tuyến, điều khiển kết nối giữa các thiết bị hoạt động đúng như thiết kế. Tập hợp tất cả cơ chế, giải thuật, quy trình đó được định nghĩa và thiết kế theo một tiêu chuẩn mạng, tạo nên các bộ giao thức mạng đảm bảo chức năng truyền gửi dữ liệu và tín hiệu điều khiển trong mạng cảm biến không dây cũng như mạng Internet bên ngoài.

Trong kiến trúc mạng IoT, có hai cách tiếp cận để các thiết bị IoT có thể truyền dữ liệu ra bên ngoài mạng Internet đó là: (i) thiết bị IoT có một địa chỉ mạng riêng biệt (địa chỉ IPv6) để giao tiếp trực tiếp với mạng bên ngoài; (ii) các thiết bị IoT giao tiếp nội bộ trong mạng IoT của mình, sau đó gửi dữ liệu ra ngoài thông qua thiết bị cổng (IoT Gateway) hoặc các thiết bị trạm (base station). Hai bộ giao thức mạng đặc trưng cho hai cơ chế kết nối này đó là bộ giao thức 6LoWPAN (thiết bị IoT kết nối trực tiếp với mạng bên ngoài qua IPv6) và bộ giao thức Zigbee. Bên cạnh hai bộ giao thức đặc trưng đó, ngày nay giải pháp kết nối thiết bị IoT qua mạng WLAN truyền thống cũng được sử dụng phổ biến trong các ngữ cảnh đơn giản. Đặc biệt, với sự ra đời của các nền tảng phần cứng hỗ trợ kết nối WiFi như ESP8266, ESP32 cho phép người mới bắt đầu với công nghệ IoT có thể hiện thực giải pháp IoT đơn giản với kết nối WiFi quen thuộc. Phần tiếp theo của phần này trình bày chi tiết đặc trưng kỹ thuật của các bộ giao thức không dây vừa kể trên.

#### 3.2.1. Bộ giao thức 6LoWPAN

6LoWPAN là viết tắt của "IPv6 over Low-Power Wireless Personal Area Network", là công nghệ mạng cho phép gói tin IPv6 được sử dụng trong những link layer nhỏ như định nghĩa trong IEEE 802.15.4. Là lựa chọn tốt cho các ứng dụng IoT khi mạng cảm biến không dây có kích thước lớn [3]."""

p[60] = """6LoWPAN là chuẩn mở được định nghĩa trong RFC 6282 bởi IETF. Tính năng nổi bật của 6LoWPAN là ban đầu chỉ hỗ trợ cho IEEE 802.15.4 trong mạng cảm biến không dây tiết kiệm năng lượng trong băng tần 2.4GHz nhưng giờ đây đã mở rộng ra nhiều loại mạng khác bao gồm Sub-1 GHz low-power RF, Bluetooth, Smart Power Line Control (PLC) và low-power Wi-Fi [3].

##### 3.2.1.1. Kiến trúc mạng 6LoWPAN

Hình 3.11 trình bày kiến trúc mạng mesh 6LoWPAN. Hướng uplink ra Internet được quản lý bởi Access Point (AP) hoạt động như một IPv6 Router. Một số thiết bị khác kết nối vào Router như: PC, server... Mạng 6LoWPAN được kết nối với mạng IPv6 thông qua edge router. Các edge router quản lý 3 việc là: 1) trao đổi dữ liệu giữa thiết bị chạy 6LoWPAN và Internet (hay mạng IPv6 khác); 2) trao đổi dữ liệu nội bộ giữa các thiết bị bên trong mạng 6LoWPAN; và 3) là tạo và duy trì radio subnet (mạng 6LoWPAN).

**Hình 3.11.** Kiến trúc mạng mesh 6LoWPAN [3]"""

p[61] = """Bằng cách giao tiếp với IP truyền thống, mạng 6LoWPAN kết nối với các mạng khác thông qua router IP. Như hình trên thì mạng 6LoWPAN hoạt động trên một góc như một stub network. Điều đó có nghĩa là dữ liệu đi vào mạng để dành riêng cho một thiết bị cụ thể ở trong mạng 6LoWPAN. Bên ngoài, mạng IP truyền thống có thể được cung cấp bởi các loại liên kết khác nhau như: ethernet, Wi-Fi hay 3G/4G. Bởi vì 6LoWPAN chỉ chuyên hoạt động với IPv6 thông qua chuẩn IEEE 802.15.4, một router 6LoWPAN là một router kết nối giữa hai mạng với nhau. Các thiết bị trong mạng 6LoWPAN giao tiếp với nhau bằng giao thức định tuyến chuẩn IPv6 hoặc giao thức định tuyến 6LoWPAN. Một thiết bị trong mạng 6LoWPAN có thể là Host hoặc Router:
- **Host:** Là thiết bị đầu cuối không có chức năng chuyển tiếp gói tin đến các thiết bị khác trong mạng.
- **Router:** Là thiết bị có chức năng định tuyến chuyển tiếp gói tin giữa các nút mạng 6LoWPAN.

##### 3.2.1.2. Mô hình phân lớp các tầng giao thức trong 6LoWPAN

**Hình 3.12.** Mô hình phân lớp các tầng giao thức trong 6LoWPAN [3]

Hình 3.12 mô tả mô hình phân lớp các tầng giao thức trong 6LoWPAN. Tầng ứng dụng (Application Layer) bao gồm các giao thức ứng dụng phổ biến như CoAP, MQTT, HTTP... Tầng giao vận (Transport Layer) hỗ trợ UDP và TCP. Tầng mạng (Network Layer) sử dụng giao thức IPv6 cùng với giao thức định tuyến RPL. Tầng thích ứng (Adaptation Layer) nằm giữa tầng mạng và tầng liên kết dữ liệu, thực hiện chức năng nén tiêu đề IPv6 và phân mảnh gói tin để phù hợp với kích thước gói tin của chuẩn IEEE 802.15.4 (tối đa 127 byte). Tầng liên kết dữ liệu (Data Link Layer - MAC) và tầng vật lý (Physical Layer - PHY) tuân theo tiêu chuẩn IEEE 802.15.4."""

p[62] = """Đặc biệt, từ phiên bản năm 2006, có hai cải tiến mới cho IEEE 802.15.4 là e và g, trong đó IEEE 802.15.4e là một MAC được cải tiến và cung cấp nhiều cơ chế nâng cấp như Time Slotted Channel Hopping (TSCH) và Coordinated Sampled Listening (CSL), cả hai cơ chế này đều hỗ trợ hoạt động tiết kiệm năng lượng. Chuẩn IEEE 802.15.4g là một cải tiến tầng PHY với mục đích ứng dụng trong các mạng tiện ích thông minh (Smart Utility Networks - SUN).

Tầng thích ứng (Adaptation layer) trong bộ giao thức 6LoWPAN chịu trách nhiệm thực hiện 3 cơ chế quan trọng:
- **Nén tiêu đề (Header Compression):** Do tiêu đề IPv6 chuẩn có kích thước cố định là 40 byte, trong khi kích thước MTU tối đa của IEEE 802.15.4 chỉ là 127 byte (sau khi trừ đi tiêu đề MAC còn khoảng 81-102 byte cho tải trọng), nếu giữ nguyên tiêu đề IPv6 sẽ chiếm gần một nửa tải trọng của khung truyền. Tầng thích ứng sử dụng các kỹ thuật nén tiêu đề theo RFC 4944 và RFC 6282 để nén tiêu đề IPv6 xuống còn vài byte (tối thiểu là 2-7 byte).
- **Phân mảnh và ghép mảnh (Fragmentation and Reassembly):** Tiêu chuẩn IPv6 yêu cầu mọi liên kết phải hỗ trợ kích thước gói tin MTU tối thiểu là 1280 byte. Vì khung truyền IEEE 802.15.4 không thể chứa trực tiếp một gói tin 1280 byte, tầng thích ứng phải chia gói tin IPv6 thành nhiều mảnh nhỏ ở phía gửi và ghép chúng lại ở phía nhận trước khi đưa lên tầng mạng IPv6.
- **Định tuyến mức liên kết (Mesh Routing / Layer-two Routing):** Hỗ trợ truyền gói tin qua nhiều chặng ở tầng liên kết dữ liệu khi cần thiết (Mesh-Under)."""

p[63] = """##### 3.2.1.3. Cấu trúc gói tin của chuẩn mạng 6LoWPAN

**Hình 3.13.** Cấu trúc gói tin IPv6 và 6LoWPAN [3]

Tiêu đề IPv6 chuẩn bao gồm các trường: Version (4 bit), Traffic Class (8 bit), Flow Label (20 bit), Payload Length (16 bit), Next Header (8 bit), Hop Limit (8 bit), Source Address (128 bit = 16 byte), và Destination Address (128 bit = 16 byte). Tổng cộng tiêu đề IPv6 cố định chiếm 40 byte.

Khi truyền qua mạng 6LoWPAN, kỹ thuật nén tiêu đề LOWPAN_IPHC (theo RFC 6282) khai thác các đặc điểm liên kết cục bộ và địa chỉ MAC sẵn có để nén tiêu đề:
- Nếu địa chỉ IPv6 nguồn hoặc đích có tiền tố liên kết cục bộ (Link-Local: `FE80::/64`) hoặc tiền tố mạng đã biết trước, tiền tố đó có thể được lược bỏ hoàn toàn.
- Phần định danh giao diện (IID - Interface Identifier) 64 bit có thể được suy ra trực tiếp từ địa chỉ MAC 64 bit (hoặc 16 bit ngắn) của tầng liên kết IEEE 802.15.4, do đó không cần truyền trong tiêu đề gói tin.
- Các trường Traffic Class và Flow Label nếu bằng 0 có thể được nén bỏ.
- Trường Next Header có thể được nén thành vài bit nếu mang giá trị phổ biến như UDP, TCP hoặc ICMPv6.

Nhờ đó, tiêu đề IPv6 từ 40 byte có thể được nén xuống chỉ còn 2 đến 7 byte trong các tình huống truyền dữ liệu thông thường."""

p[64] = """**Hình 3.14.** Cách bố trí các header để truyền dữ liệu trong mạng 6LoWPAN [4]

Hình 3.14 mô tả cách bố trí các tiêu đề (header) khi đóng gói dữ liệu:
- Gói tin chưa phân mảnh gồm: Tiêu đề IEEE 802.15.4 MAC, tiêu đề nén 6LoWPAN (IPHC), tiêu đề UDP nén, và tải trọng ứng dụng (Payload).
- Trong trường hợp gói tin IPv6 lớn hơn MTU của IEEE 802.15.4, gói tin sẽ được phân mảnh:
  - Mảnh đầu tiên (First Fragment): chứa tiêu đề IEEE 802.15.4, tiêu đề phân mảnh (Fragment Header: Datagram Size, Datagram Tag), tiêu đề nén IPv6, tiêu đề UDP và phần đầu của dữ liệu.
  - Các mảnh tiếp theo (Subsequent Fragments): chứa tiêu đề IEEE 802.15.4, tiêu đề phân mảnh (Datagram Size, Datagram Tag, Datagram Offset) và phần dữ liệu kế tiếp.

##### 3.2.1.4. Nền tảng hiện thực bộ giao thức 6LoWPAN

Bộ giao thức 6LoWPAN hiện nay được hỗ trợ rộng rãi trên nhiều hệ điều hành và nền tảng phần cứng IoT:
- **Hệ điều hành mạng nhúng:** Contiki OS (với chồng giao thức uIPv6 / ContikiMAC), TinyOS (với BLIP - Berkeley Low-power IP Stack), RIOT OS, FreeRTOS, Zephyr OS.
- **Nền tảng phần cứng:** Các vi điều khiển hỗ trợ chuẩn IEEE 802.15.4 như TI CC2538, CC2650, CC1352, Atmel SAMR21, Nordic Semiconductor nRF52840, và các module OpenMote."""

p[65] = """#### 3.2.2. Bộ giao thức Zigbee

##### 3.2.2.1. Kiến trúc mạng Zigbee

Mạng Zigbee có 3 nhóm thiết bị logic (theo chức năng):
- **Thiết bị điều phối mạng (Coordinator - ZC):** Mỗi mạng Zigbee chỉ có duy nhất một Coordinator. Thiết bị này có trách nhiệm khởi tạo mạng, lựa chọn tần số và PAN ID (Personal Area Network Identifier), cho phép các thiết bị khác gia nhập mạng, lưu trữ thông tin cấu hình mạng và bảng định tuyến. Coordinator luôn luôn hoạt động (mains-powered).
- **Bộ định tuyến (Router - ZR):** Thiết bị định tuyến có chức năng chuyển tiếp gói tin giữa các nút trong mạng, mở rộng phạm vi bao phủ của mạng Zigbee. Router có thể cho phép các nút con (End Devices hoặc Router khác) kết nối vào mình và quản lý truyền thông cho các nút con đó. Router thường được cấp nguồn liên tục.
- **Thiết bị đầu cuối (End Device - ZED):** Là các thiết bị cảm biến hoặc cơ cấu chấp hành hoạt động bằng pin, chỉ giao tiếp trực tiếp với nút cha của nó (Coordinator hoặc Router). Thiết bị đầu cuối không có chức năng chuyển tiếp dữ liệu cho các nút khác. Khi không có dữ liệu cần truyền nhận, End Device có thể chuyển sang chế độ ngủ sâu (sleep mode) để tiết kiệm năng lượng tối đa.

**Hình 3.15.** Mô hình một mạng Zigbee"""

p[66] = """- Router được nhận một địa chỉ (địa chỉ ngắn - Short Address) là hằng số, có thể được sử dụng trong truyền điểm - điểm.
- Kể cả khi Coordinator bị ngắt điện, Router vẫn có thể duy trì mạng lưới, vì vậy giữa Router và Router vẫn có thể giao tiếp được.

Khi một nút được thêm vào ngay cả khi Coordinator bị ngắt điện, nó vẫn có thể thông qua các địa chỉ của Router hiện hữu để tham gia vào mạng lưới. Hình 3.15 mô tả về một mạng Zigbee bao gồm 1 Coordinator, 6 Router và một số End Devices.

##### 3.2.2.2. Mô hình phân lớp các tầng giao thức trong chuẩn không dây Zigbee

**Hình 3.16.** Các chồng giao thức tham chiếu giữa 802.15.4 và Zigbee

Trong Hình 3.16, lớp vật lý (PHY) và lớp MAC tuân theo chuẩn IEEE 802.15.4, các lớp phía trên bao gồm Tầng mạng (Network Layer - NWK), Tầng hỗ trợ ứng dụng (Application Support Sublayer - APS), và Đối tượng thiết bị Zigbee (Zigbee Device Objects - ZDO) cùng Khung ứng dụng (Application Framework) được định nghĩa bởi Liên minh Zigbee (Zigbee Alliance).

**Lớp vật lý (PHY)**
Theo chuẩn IEEE 802.15.4, đường truyền không dây có thể hoạt động ở 3 tần số không chính thức sau: 868MHz, 902-"""

p[67] = """928MHz và 2.4GHz. Dựa trên các dải tần đó, tiêu chuẩn IEEE 802.15.4 định nghĩa 3 dạng lớp vật lý sau:
- Trải phổ chuỗi trực tiếp dùng BPSK hoạt động ở dải tần số 868MHz, tốc độ dữ liệu xấp xỉ 20kbps.
- Trải phổ chuỗi trực tiếp dùng BPSK hoạt động ở dải tần số 915MHz, tốc độ dữ liệu xấp xỉ 40kbps.
- Trải phổ chuỗi trực tiếp dùng O-QPSK hoạt động ở dải tần số 2.4GHz, tốc độ dữ liệu xấp xỉ 250kbps.

Cấu trúc khung dữ liệu của lớp vật lý IEEE 802.15.4 được mô tả ở hình sau:

**Hình 3.17.** Cấu trúc frame của chuẩn 802.15.4

Trong Hình 3.17, trường đầu tiên của frame gồm 32 bit preamble (đồng bộ hóa) dùng cho đồng bộ ký tự. Trường tiếp theo là SFD (Start of Frame Delimiter) có độ dài 1 byte đánh dấu điểm bắt đầu của phân giải gói. Trường Frame Length 8 bit kế tiếp xác định chiều dài của đơn vị dữ liệu trong lớp PHY (PSDU). Trường PSDU mang tối đa 127 bytes dữ liệu.

**Lớp MAC**
Các thông số lớp MAC theo tiêu chuẩn IEEE 802.15.4 được thiết kế cho các ứng dụng yêu cầu tốc độ dữ liệu thấp và độ trễ vừa phải. Các thông số MAC layer 802.15.4 có nhiều điểm đáp ứng cho yêu cầu về khả năng phân bố mạng một cách mềm dẻo và công suất thấp. Một số đặc điểm như sau:
- Cung cấp thiết bị mạng và cấu hình mạng đa dạng.
- Cấu trúc siêu khung thay đổi được phù hợp cho điều khiển chu kỳ nhiệm vụ các thiết bị mạng."""

p[68] = """- Truyền dữ liệu trực tiếp hoặc gián tiếp.
- Giao thức điều khiển truy cập môi trường dựa trên lập lịch và đụng độ.
- Quản lý hiệu quả năng lượng để tăng tuổi thọ của mạng.
- Dễ dàng triển khai cho mạng cỡ lớn.

##### 3.2.2.3. Cấu trúc frame của chuẩn 802.15.4

**Hình 3.18.** Cấu trúc superframe của 802.15.4

Chuẩn IEEE 802.15.4 định nghĩa một cấu trúc superframe theo yêu cầu: superframe bắt đầu bằng beacon (báo hiệu) và được chia thành 16 khe như nhau, được mô tả trong Hình 3.18. Khe thời gian đầu tiên của siêu khung dùng để phát beacon. Các khe còn lại được dùng bởi các thiết bị tranh chấp để thông tin trong thời gian truy cập tranh chấp (Contention Access Period - CAP). Các thiết bị dùng giao thức CSMA/CA phân khe thời gian để tranh chấp truy cập với các thiết bị khác. Việc thông tin giữa các thiết bị phải hoàn thành trước khi kết thúc CAP của superframe hiện tại và bắt đầu phát beacon của superframe kế tiếp.

Tiêu chuẩn IEEE 802.15.4 quy định MAC frame gồm 3 thành phần: MAC header, MAC payload và MAC footer như trong Hình 3.19. MAC header gồm trường điều khiển frame và trường địa chỉ. MAC payload chứa dữ liệu cần trao đổi, và MAC footer chứa các trường kiểm tra frame."""

p[69] = """**Hình 3.19.** Data Frame trong chuẩn 802.15.4

IEEE 802.15.4 cũng định nghĩa 4 dạng frame cơ bản: beacon frame, frame dữ liệu, frame xác nhận ACK và MAC command frame:
- **Beacon frame:** Được bộ điều phối mạng phát theo chu kỳ để xác nhận mạng và cấu trúc mạng, đánh thức các thiết bị từ trạng thái ngủ và đồng bộ hoạt động mạng. Beacon frame rất quan trọng trong cấu hình mô mạng Mesh và Tree. Chúng hỗ trợ cho tất cả các nút mạng đồng bộ mà không cần các nút phải hoạt động ở chế độ tích cực trong thời gian dài.
- **Data frame:** Có thể dài tới 104 octets dữ liệu (1 octet = 1 byte). Mỗi frame dữ liệu mang một chuỗi số thứ tự xác nhận. Chuỗi số đảm bảo tất cả các khung được đếm và nhận hợp lệ. Trường FCS (checksum) dùng để phát hiện lỗi frame.
- **ACK frame:** Thiết bị nhận gửi frame ACK tương ứng cho phía phát để thông báo frame dữ liệu nhận được là hợp lệ và không có lỗi.
- **MAC command frame:** Được dùng để thông báo và thông tin phục vụ mục đích quản lý mạng tập trung để điều khiển và cấu hình thiết bị từ xa. Nhóm lệnh bao gồm phối hợp thiết bị, yêu cầu dữ liệu, thông báo PAN ID, yêu cầu beacon, GTS, tổ chức lại coordinator.

Thiết kế lớp giao thức MAC rất quan trọng trong mạng WSNs, nó đảm bảo hiệu quả sử dụng năng lượng để kéo dài thời gian sống của mạng, tạo nên khả năng mở rộng phù hợp kích thước mạng, mật độ node và cấu hình mạng. Các thuộc tính quan trọng khác cần lưu ý của thiết kế giao thức MAC là sự công bằng giữa các node, giảm độ trễ, hạn chế lưu lượng cao của băng thông."""

p[70] = """##### 3.2.2.4. Một số đặc điểm của chuẩn Zigbee trong ứng dụng mạng cảm biến không dây

Đặc điểm của công nghệ này là tốc độ truyền tin thấp, nhưng tiêu hao ít năng lượng và là giao thức mạng không dây hướng tới các ứng dụng điều khiển từ xa và tự động hóa trong công nghệ IoT (Internet of Things) trong tương lai. Zigbee có thể dùng trong các mạng lưới rộng hơn là sử dụng Bluetooth. Các thiết bị không dây sử dụng công nghệ Zigbee có thể truyền tin trong khoảng cách từ vài mét đến vài chục mét tùy thuộc vào môi trường truyền tin và mức công suất được yêu cầu ở mỗi ứng dụng. Tốc độ dữ liệu là 250kbps ở dải băng tần 2.4GHz được sử dụng rộng rãi. Các dữ liệu được truyền theo gói, gói tối đa là 128 bytes cho phép tải trọng tối đa 104 bytes.

**Zigbee có độ tin cậy cao**

Thực tế, sự truyền thông không dây là không tin cậy. Chứng minh điều này bằng việc đi lòng vòng với một chiếc điện thoại di động, sau đó bước vào thang máy. Bất cứ ai sử dụng điện thoại đều gặp sự cố cuộc gọi bị ngắt hoặc đường truyền yếu. Tất cả bởi vì sóng radio cũng chỉ là các sóng. Chúng chạy qua các vật cản, có thể bị chặn bởi kim loại, nước hoặc khối bê tông và phụ thuộc vào nhiều yếu tố phức tạp gồm thiết kế ăng-ten, sự khuếch đại năng lượng và thậm chí các điều kiện thời tiết.

Tuy nhiên, điều khiển không dây thường không có cùng vấn đề như trong một cuộc điện thoại, di chuyển để tìm điểm nhận sóng tốt hơn hay đợi để thử lại sau. Hiệp hội Zigbee hiểu điều này, giao thức Zigbee được thiết kế với độ tin cậy cao. Điều này được thể hiện trong các đặc tả Zigbee:
- IEEE 802.15.4 với O-QPSK và DSSS.
- CSMA-CA.
- 16-bit CRCs.
- ACK tại mỗi hop (chặng).
- Việc nối mạng lưới (mesh) để tìm ra đường đi tin cậy.
- End-to-end ACK để kiểm tra dữ liệu đến đích."""

p[71] = """Điều đầu tiên là dựa vào một kỹ thuật không dây rất tin cậy, khoảng cách thấp và dùng sự đặc tả IEEE 802.15.4. Đặc tả này là một kỹ thuật radio mạnh, rất hiện đại được xây dựng trên 40 năm kinh nghiệm của IEEE. Nó dùng Offset-Quadrature Phase-Shift Keying (O-QPSK) và Direct Sequence Spread Spectrum (DSSS), một sự kết hợp của các kỹ thuật nhằm cung cấp hiệu suất tín hiệu trên nhiễu (Signal-to-Noise Ratio - SNR) rất cao ở công suất truyền phát thấp.

Thứ hai, chuẩn IEEE 802.15.4 định nghĩa cơ chế đa truy cập cảm nhận sóng mang tránh xung đột (CSMA-CA). Trước khi truyền tin, thiết bị lắng nghe kênh truyền để đảm bảo không có thiết bị nào khác đang phát sóng, qua đó giảm thiểu va chạm dữ liệu trên môi trường truyền.

Thứ ba, mỗi khung truyền đều đi kèm mã kiểm tra độ dư thừa vòng 16 bit (16-bit CRC) trong trường FCS. Phía nhận thực hiện kiểm tra CRC trên toàn bộ khung dữ liệu; nếu phát hiện sai sót bit, khung truyền sẽ bị hủy bỏ ngay lập tức.

Thứ tư, cơ chế báo nhận (ACK) tại mỗi hop đảm bảo tính toàn vẹn của việc truyền tin giữa hai nút kế cận. Nếu phía phát không nhận được ACK trong một khoảng thời gian chờ định trước, nó sẽ tự động phát lại khung tin (lên tới số lần truyền lại tối đa quy định).

Thứ năm, kiến trúc định tuyến mạng lưới (mesh networking) với thuật toán AODV cho phép các gói tin tự động tìm đường vòng qua các nút trung gian khác nếu một nút hoặc liên kết trên đường đi chính bị hỏng hoặc nghẽn."""

p[72] = """Thêm vào đó, Zigbee cung cấp việc broadcast tin cậy. Zigbee cũng cung cấp multicasting có thể gửi một message đến một nhóm các nút trong mạng.

Cuối cùng, Zigbee cung cấp tự động ACK end-to-end. Ứng dụng nguồn có thể yêu cầu một xác nhận mức ứng dụng từ nút đích cuối cùng để đảm bảo rằng gói tin không chỉ đến được nút mạng mà còn được xử lý thành công bởi ứng dụng đích.

**Bảo mật trong Zigbee**

Bên cạnh độ tin cậy, bảo mật là một yếu tố sống còn đối với các hệ thống điều khiển tự động hóa và IoT:
- Zigbee sử dụng thuật toán mã hóa tiêu chuẩn tiên tiến AES-128 (Advanced Encryption Standard với độ dài khóa 128 bit) để bảo vệ tính bảo mật của dữ liệu.
- Tính toàn vẹn của thông điệp được đảm bảo thông qua mã xác thực thông điệp CBC-MAC (Cipher Block Chaining Message Authentication Code) gắn kèm gói tin.
- Cơ chế chống phát lại (Replay Protection) sử dụng số thứ tự khung tuần tự (Frame Counter) để ngăn chặn kẻ tấn công ghi lại và phát lại các gói tin hợp lệ nhằm chiếm quyền điều khiển hệ thống.
- Zigbee hỗ trợ 3 loại khóa bảo mật chính: Master Key (dùng để thiết lập các khóa khác), Network Key (dùng chung cho toàn bộ các nút trong mạng), và Link Key (dùng riêng biệt giữa hai nút cụ thể để bảo mật thông tin liên lạc ngang hàng)."""

p[73] = """Hiệp hội Zigbee đã quyết định giữ giao thức trong một môi trường tốc độ truyền dữ liệu thấp.

Với tần số 2.4GHz, tốc độ truyền tối đa của Zigbee là 250kbps, nhưng do số lần truyền lại, sự mã hóa và giải mã, và giao thức lưới đầy đủ được dùng nên throughput thực sự khoảng 25kbps. Transceivers là half-duplex, đây cũng là một yếu tố giảm throughput từ 250 tới 25kbps.

##### 3.2.2.5. Nền tảng hiện thực bộ giao thức mạng Zigbee

Bộ giao thức mạng Zigbee là một chuẩn giao thức được sử dụng phổ biến trong nhiều giải pháp IoT. Với đặc trưng cho phép xây dựng một mạng IoT với số lượng nút lớn và tiết kiệm năng lượng, độ tin cậy cao, chuẩn kết nối Zigbee là lựa chọn hàng đầu trong việc triển khai các giải pháp giám sát trong thực tế. Bảng 3.3 và Bảng 3.4 giới thiệu một số nền tảng phần mềm, phần cứng hỗ trợ hiện thực, triển khai giải pháp IoT sử dụng bộ giao thức Zigbee.

**Bảng 3.3.** Một số nền tảng phần cứng hỗ trợ chuẩn Zigbee

| STT | Tên giải pháp | Nhà sản xuất | Thông tin chi tiết |
|:---:|:---|:---|:---|
| 1 | CC1352R, CC1352P, CC2652R, CC2530, CC2538 | Texas Instruments | https://www.ti.com/wireless-connectivity/zigbee/ |
| 2 | Digi XBee® Zigbee Modules | Digi | https://www.digi.com/ |
| 3 | Zigbee Modules (802.15.4) | Mouser Electronics | https://www.mouser.com/ |
| 4 | MGM12P02F1024GE-V2 | SILICON LABS | https://www.silabs.com/ |

**Bảng 3.4.** Một số nền tảng phần mềm hỗ trợ bộ giao thức Zigbee

| STT | Tên giải pháp | Thông tin chi tiết |
|:---:|:---|:---|
| 1 | Arduino-based | https://www.arduino.cc |
| 2 | nRF5 SDK | https://www.nordicsemi.com |
| 3 | ZBOSS 3.0 | https://dsr-zboss.com |"""

p[74] = """#### 3.2.3. Bộ giao thức WiFi 802.11

##### 3.2.3.1. Kiến trúc mạng WiFi 802.11

Mạng không dây theo chuẩn kết nối 802.11 có thể hoạt động theo kiến trúc dựa theo hạ tầng mạng (infrastructure-based) hoặc kiến trúc không hạ tầng, kết nối không dây trực tiếp giữa các thiết bị với nhau (ad-hoc).

Kiến trúc mạng theo hạ tầng bao gồm các thành phần: thiết bị đầu cuối (station - STA), thiết bị điểm truy cập (access point - AP). Các thiết bị đầu cuối kết nối với một điểm truy cập cùng một tần số tạo nên một tập dịch vụ cơ bản (Basic Service Set - BSS). Hình 3.20 minh họa kiến trúc mạng 802.11 dựa trên kiến trúc hạ tầng.

**Hình 3.20.** Minh họa mạng 802.11 theo kiến trúc hạ tầng

Kiến trúc không dựa theo hạ tầng (adhoc-based) là kiến trúc mạng mà các thiết bị không dây đầu cuối kết nối trực tiếp với nhau, truyền dữ liệu trực tiếp cho nhau mà không cần thông qua một hạ tầng mạng phân phối. Các thiết bị đầu cuối này kết nối lại với nhau tạo thành một nhóm dịch vụ cơ bản độc lập (IBSS), trao đổi dữ liệu trên cùng tần số radio. Hình 3.21 minh họa hai nhóm dịch vụ cơ bản kết nối theo mô hình mạng Ad-hoc (adhoc network).

**Hình 3.21.** Minh họa mạng 802.11 theo kiến trúc ad-hoc"""

p[75] = """##### 3.2.3.2. Mô hình phân lớp tầng giao thức trong chuẩn không dây 802.11

**Hình 3.22.** Ánh xạ 802.11 trong mô hình OSI

Chuẩn IEEE 802.11 được xây dựng cho mạng cục bộ không dây bao gồm hai tầng con là tầng PHY và tầng MAC trong mô hình OSI. Tầng LLC (Logic Link Control) được mô tả trong chuẩn 802.2. Với các tầng mức cao hơn, kiến trúc phân tầng cung cấp một giao diện trong suốt (nghĩa là không có sự thay đổi đối với các ứng dụng mức cao hơn). Vì vậy, với các tầng từ LLC trở lên có thể hoán chuyển các trạm đang hoạt động mạng WLAN với các mạng cục bộ khác. Hình 3.22 mô tả kiến trúc của WLAN trong mô hình OSI. Điều này cho phép giao thức TCP/IP hiện tại có thể hoạt động dựa trên mạng IEEE 802.11 WLAN giống như hoạt động triển khai trên một mạng có dây Ethernet.

Hình 3.23 mô tả sự khác biệt về các chuẩn hoạt động dựa trên chuẩn 802 WLAN ở tầng PHY và tầng MAC."""

p[76] = """Trong Hình 3.23, ở tầng PHY sẽ gồm các tuỳ chọn phát sóng: InfraRed (IR), Frequency Hopping Spread Spectrum (FHSS) và Direct Sequence Spread Spectrum (DSSS). Tất cả các tuỳ chọn ban đầu đều hỗ trợ tốc độ 1 và 2Mbps. Năm 1999, tổ chức IEEE định nghĩa ra hai chuẩn tốc độ cao mở rộng tương ứng với hai chuẩn 802.11b (hoạt động ở băng tần 2.4GHz, tốc độ 11Mbps) và chuẩn 802.11a (hoạt động ở băng tần 5GHz, tốc độ lên đến 54Mbps, dựa trên công nghệ Orthogonal Frequency Division Multiplexing - OFDM). Gần đây, chuẩn 802.11g được đưa ra. Đây là một chuẩn mở rộng của chuẩn 802.11b trong đó hỗ trợ tốc độ truyền lên đến 54Mbps và vẫn hoạt động ở băng tần 2.4GHz.

**Hình 3.23.** Các giao thức sử dụng trong hệ thống mạng cục bộ không dây dựa trên chuẩn IEEE 802.11 của tầng vật lý (PHY layer) và tầng điều khiển truy cập môi trường truyền (MAC layer)"""

p[77] = """##### 3.2.3.3. Cấu trúc frame của chuẩn không dây 802.11

**Hình 3.24.** Cấu trúc Media Access Control (MAC) frame trong chuẩn không dây 802.11

Hình 3.24 mô tả cấu trúc của một Frame trong 802.11. Tuỳ vào chức năng của trạm phát, quy định bởi các bit "To DS" và "From DS" trong phần Frame Control mà vai trò của các địa chỉ 1, 2, 3 và 4 trong MAC Header sẽ khác nhau cụ thể:

**Bảng 3.5.** Bảng chức năng của trạm phát dựa theo bit "To DS" và "From DS"

| Chức năng | Bit "To DS" | Bit "From DS" | Address 1 | Address 2 | Address 3 | Address 4 |
|:---|:---:|:---:|:---|:---|:---|:---|
| Independent BSS | 0 | 0 | RA = DA | SA | BSSID | Không có |
| Từ AP | 0 | 1 | RA = DA | BSSID | SA | Không có |
| Tới AP | 1 | 0 | RA = BSSID | SA | DA | Không có |
| Wireless DS | 1 | 1 | RA (Địa chỉ nhận) | TA (Địa chỉ truyền) | DA (Địa chỉ đích) | SA (Địa chỉ gửi) |

Chú thích:
- **AP** (Access Point): Điểm truy cập.
- **BSS** (Basic Service Set): Nhóm các thiết bị vận hành chung một kênh truyền sóng.
- **BSSID** (Basic Service Set Identifier): Định danh cho 1 BSS.
- **DS** (Distributed System): Hệ thống phân phối, chỉ các thiết bị cho phép kết nối nhiều AP lại với nhau.
- **RA** (Receiver Address): Địa chỉ trạm nhận.
- **TA** (Transmitter Address): Địa chỉ trạm truyền.
- **DA** (Destination Address): Địa chỉ trạm đích.
- **SA** (Sender Address): Địa chỉ trạm gửi.

##### 3.2.3.4. Một số chuẩn con của 802.11

**802.11b**
IEEE đã mở rộng trên chuẩn 802.11 gốc vào tháng 7 năm 1999, đó chính là chuẩn 802.11b. Chuẩn này hỗ trợ băng thông lên đến 11Mbps, tương đương với Ethernet truyền thống. 802.11b sử dụng tần số vô tuyến (2.4GHz) giống như chuẩn ban đầu."""

p[78] = """Các hãng sản xuất thích sử dụng tần số 2.4GHz này để chi phí sản xuất của họ được giảm. Các thiết bị 802.11b có thể bị xuyên nhiễu từ các thiết bị điện thoại không dây (kéo dài), lò vi sóng hoặc các thiết bị khác sử dụng cùng dải tần 2.4GHz. Mặc dù vậy, bằng cách cài đặt các thiết bị 802.11b cách xa các thiết bị như vậy có thể giảm được hiện tượng xuyên nhiễu này.

**Ưu điểm của 802.11b:** Giá thành rẻ; phạm vi tín hiệu tốt và không dễ bị che khuất.
**Nhược điểm của 802.11b:** Tốc độ tối đa thấp nhất; các thiết bị trong gia đình có thể làm xuyên nhiễu với băng tần này.

**802.11a**
Trong khi 802.11b vẫn đang được phát triển, IEEE đã tạo một mở rộng thứ cấp cho chuẩn 802.11 có tên gọi 802.11a. Vì 802.11b được sử dụng rộng rãi quá nhanh so với 802.11a, nên một số người cho rằng 802.11a được tạo sau 802.11b. Tuy nhiên trong thực tế, 802.11a và 802.11b được tạo một cách đồng thời. Do giá thành cao hơn nên 802.11a chỉ được sử dụng trong các mạng doanh nghiệp còn 802.11b thích hợp hơn với thị trường mạng gia đình.

802.11a hỗ trợ băng thông lên đến 54Mbps và sử dụng tần số vô tuyến 5GHz. Tần số của 802.11a cao hơn so với 802.11b, chính vì vậy đã làm cho phạm vi của hệ thống này hẹp hơn so với các mạng 802.11b. Với tần số này, các tín hiệu 802.11a khó xuyên qua các vách tường và các vật cản khác hơn.

Do 802.11a và 802.11b sử dụng các tần số khác nhau nên hai công nghệ này không thể tương thích với nhau. Chính vì vậy, một số hãng đã cung cấp các thiết bị mạng hybrid cho 802.11a/b nhưng các sản phẩm này chỉ đơn thuần là bổ sung thêm hai chuẩn này.

**Ưu điểm của 802.11a:** Tốc độ cao; tần số 5GHz tránh được sự xuyên nhiễu từ các thiết bị khác.
**Nhược điểm của 802.11a:** Giá thành đắt; phạm vi hẹp và dễ bị che khuất."""

p[79] = """**802.11g**
Vào năm 2002 và 2003, các sản phẩm WLAN hỗ trợ một chuẩn mới hơn đó là 802.11g, được đánh giá cao trên thị trường. 802.11g thực hiện sự kết hợp tốt nhất giữa 802.11a và 802.11b. Nó hỗ trợ băng thông lên đến 54Mbps và sử dụng tần số 2.4GHz để có phạm vi rộng. 802.11g có khả năng tương thích với các chuẩn 802.11b, điều đó có nghĩa là các điểm truy cập 802.11g sẽ làm việc với các adapter mạng không dây 802.11b và ngược lại.

**Ưu điểm của 802.11g:** Tốc độ cao; phạm vi tín hiệu tốt và ít bị che khuất.
**Nhược điểm của 802.11g:** Giá thành đắt hơn 802.11b; các thiết bị có thể bị xuyên nhiễu từ nhiều thiết bị khác sử dụng cùng băng tần.

**802.11n**
802.11n hay còn được gọi là WiFi 4, được chuẩn hóa vào năm 2009. Đây là chuẩn được thiết kế để cải thiện cho 802.11g trong tổng số băng thông được hỗ trợ bằng cách tận dụng nhiều tín hiệu không dây và các anten (công nghệ Multi Input Multi Output - MIMO).

Khi chuẩn này được đưa ra, các kết nối 802.11n hỗ trợ tốc độ dữ liệu lên đến 100Mbps (lý thuyết lên tới 600Mbps). 802.11n cũng cung cấp phạm vi bao phủ tốt hơn so với các chuẩn Wi-Fi trước nó nhờ cường độ tín hiệu mạnh của nó. Thiết bị 802.11n tương thích với các thiết bị 802.11g và 802.11b.

**Ưu điểm của 802.11n:** Tốc độ nhanh và phạm vi tín hiệu tốt nhất; khả năng chịu đựng tốt hơn từ việc xuyên nhiễu từ các nguồn bên ngoài.
**Nhược điểm của 802.11n:** Giá thành đắt hơn 802.11g; sử dụng tín hiệu có thể gây nhiễu với các mạng 802.11b/g ở gần.

**802.11ac**
802.11ac được Liên minh WiFi chuẩn hóa vào năm 2013, còn được gọi là WiFi 5. 802.11ac được kế thừa từ chuẩn 802.11n trước đó."""

p[80] = """So với 802.11n, 802.11ac có độ rộng kênh truyền lớn hơn (80 hoặc 160MHz so với 40MHz) trong dải băng tần 5GHz, nhiều luồng không gian hơn (8 so với 4) và điều chế bậc cao hơn (256-QAM so với 64-QAM) và bổ sung tính năng Multi User - Multi Input Multi Output (MU-MIMO). Tính năng này cho phép các điểm truy cập phát nhiều chùm tia đến từng máy trạm. Từ đó, giảm thiểu được việc đụng độ giữa các máy trạm và tăng thông lượng tổng thể.

Liên minh WiFi đã tách việc phát triển 802.11ac thành hai pha, được đặt tên là Wave 1 và Wave 2. Các sản phẩm 802.11ac Wave 1 được sản xuất từ năm 2013 và đến năm 2016 các sản phẩm Wave 2 được đưa ra thị trường nhằm bổ sung các tính năng mới của 802.11ac như băng thông cao hơn, MU-MIMO, độ rộng kênh 160MHz, hỗ trợ nhiều kênh tại băng tần 5GHz, tăng luồng (4 anten so với 3 anten của 802.11ac Wave 1).

**Ưu điểm của 802.11ac:** So với các chuẩn trước, 802.11ac sử dụng băng tần kép 2.4GHz và 5GHz nên tốc độ truyền cao hơn, ít nhiễu hơn.
**Nhược điểm của 802.11ac:** Do sử dụng băng tần 5GHz nên mức suy hao tín hiệu cao hơn so với 2.4GHz khi qua vật cản.

**802.11ax**
Chuẩn 802.11ax được kế thừa từ 802.11ac, và được IEEE chuẩn hóa vào tháng 9 năm 2020, còn được gọi là WiFi 6. Mục tiêu của 802.11ax là cung cấp thông lượng lên gấp 4 lần so với 802.11ac ở mức người dùng, trong khi tốc độ dữ liệu chỉ tăng 37% ở mức vật lý. 802.11ax sử dụng kỹ thuật ghép kênh OFDMA, mỗi máy trạm được sử dụng các đơn vị tài nguyên khác nhau trong phạm vi khả dụng của điểm truy cập. 802.11ax cung cấp nhiều sóng mang hơn so với 802.11ac, cụ thể ở 802.11ax các kênh 20, 40, 80, và 160MHz có lần lượt 256, 512, 1024, và 2048 sóng mang con so với 64, 128, 256 và 512 sóng mang con trong 802.11ac.

**Ưu điểm của 802.11ax:** Tốc độ truyền cao hơn 40% so với 802.11ac, tối ưu cho nhiều người dùng trong cùng một thời điểm."""

p[81] = """Nhược điểm của 802.11ax do mới được chuẩn hóa nên thiết bị phát sóng và thiết bị đầu cuối hỗ trợ 802.11ax chưa có nhiều ngoài thị trường.

##### 3.2.3.5. Nền tảng hiện thực bộ giao thức mạng WiFi

Bộ giao thức mạng WiFi là một chuẩn giao thức được sử dụng phổ biến trong nhiều giải pháp IoT, đặc biệt dễ dàng sử dụng cho người mới bắt đầu. Giao thức WiFi là một kiểu kết nối không dây được sử dụng phổ biến trong đời sống. Chính vì thế đã có rất nhiều giải pháp phần mềm, phần cứng hiện thực, tích hợp khả năng kết nối WiFi vào trong các thiết bị IoT nhỏ gọn. Bảng 3.6 và Bảng 3.7 giới thiệu một số nền tảng phần mềm, phần cứng hỗ trợ hiện thực triển khai giải pháp IoT sử dụng bộ giao thức WiFi.

**Bảng 3.6.** Một số nền tảng phần cứng hỗ trợ chuẩn WiFi

| STT | Tên giải pháp | Nhà sản xuất | Thông tin chi tiết |
|:---:|:---|:---|:---|
| 1 | ESP8266, ESP32 | Espressif Systems | https://www.espressif.com/ |
| 2 | Microchip's Wi-Fi® devices | Microchip | https://www.microchip.com |
| 3 | WiFi Modules (802.11) | Mouser | https://www.mouser.com |
| 4 | WE935B00 | WI2WI SEM | http://www.wi2wi.com |

**Bảng 3.7.** Một số nền tảng phần mềm hỗ trợ bộ giao thức WiFi

| STT | Tên giải pháp | Thông tin chi tiết |
|:---:|:---|:---|
| 1 | Arduino-based | https://www.arduino.cc |
| 2 | Linux-based | https://git.kernel.org |
| 3 | WLAN drivers | Tùy thuộc loại phần cứng |"""

p[82] = """## BÀI TẬP CHƯƠNG 3

1. Hãy liệt kê những kiến trúc mạng trong IoT và đưa ra ưu, nhược điểm của mỗi kiến trúc.
2. Hãy so sánh các bộ giao thức không dây được sử dụng trong IoT và liệt kê các ứng dụng cho từng bộ giao thức.
3. Hãy sử dụng kiến trúc Zigbee để xây dựng ứng dụng Giám sát chất lượng không khí.
4. Hãy sử dụng kiến trúc WLAN 802.11 để xây dựng ứng dụng Nhà thông minh.
5. Hãy thiết kế kiến trúc mạng cho ứng dụng Nông nghiệp thông minh áp dụng tại Việt Nam. Sau đó hãy chọn bộ giao thức mạng phù hợp với ứng dụng này và giải thích vì sao.
6. Hãy thiết kế kiến trúc mạng cho ứng dụng giám sát chất lượng không khí tại Thành phố Hồ Chí Minh. Sau đó hãy chọn bộ giao thức mạng phù hợp với ứng dụng này và giải thích vì sao.
7. Hãy trình bày ý tưởng cho ứng dụng giám sát giao thông thông minh sử dụng công nghệ 5G."""

# Apply to file
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(^## Trang \d+\s*$)', text, flags=re.MULTILINE)
pages_dict = {}
for i in range(1, len(parts), 2):
    p_num = int(re.search(r'\d+', parts[i]).group(0))
    pages_dict[p_num] = parts[i+1]

for page_num in range(52, 83):
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

print("Chapter 3 (pages 52-82) updated successfully!")
