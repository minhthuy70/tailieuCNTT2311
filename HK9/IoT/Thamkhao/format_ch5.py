# -*- coding: utf-8 -*-
import sys, re

p = {}

p[116] = """# CHƯƠNG 5. ĐIỆN TOÁN ĐÁM MÂY, ĐIỆN TOÁN CẬN BIÊN VÀ IOT

Vạn vật kết nối Internet mở ra nhiều thách thức không chỉ với việc thiết kế phần cứng và phần mềm cho các thiết bị IoT mà còn đặt ra những bài toán hóc búa về hạ tầng xử lý, lưu trữ và phân tích dữ liệu khổng lồ sinh ra từ hàng triệu nút cảm biến. Sự bùng nổ của các ứng dụng IoT thời gian thực như xe tự hành, thành phố thông minh, giám sát y tế khẩn cấp đòi hỏi năng lực tính toán cực lớn cùng với độ trễ phản hồi tính bằng mili-giây.

Để giải quyết bài toán này, sự kết hợp giữa **Điện toán đám mây (Cloud Computing)** và **Điện toán cận biên (Edge Computing / Fog Computing)** đã trở thành mô hình kiến trúc chuẩn mực. Điện toán đám mây cung cấp nguồn tài nguyên lưu trữ và tính toán vô hạn ở trung tâm dữ liệu, trong khi điện toán cận biên đưa khả năng tính toán và ra quyết định đến gần nơi sinh ra dữ liệu nhất (tại các gateway, router hoặc trạm gốc kế cận thiết bị IoT).

Nội dung chương này trình bày kiến trúc tích hợp giữa IoT, điện toán đám mây và điện toán cận biên; phân tích các mô hình dịch vụ đám mây (IaaS, PaaS, SaaS) và ứng dụng thực tiễn trong việc xây dựng hệ thống giả lập mạng cảm biến không dây quy mô lớn trên nền tảng OpenStack; đồng thời làm rõ các công nghệ cốt lõi và xu hướng nghiên cứu trong tính toán cận biên."""

p[117] = """Thông qua nội dung trình bày trong chương này, người đọc có thể nắm bắt được kiến trúc tổng quan của một hệ thống IoT kết hợp hạ tầng điện toán đám mây và tính toán cận biên. Nắm được những đặc điểm, lợi ích, phân loại các mô hình dịch vụ trong điện toán đám mây cũng như các vấn đề nghiên cứu, thách thức trong IoT kết hợp tính toán cận biên giúp người đọc dễ dàng định hướng giải pháp khi triển khai thực tế.

### 5.1. Kiến trúc tổng quan hệ thống IoT tích hợp điện toán đám mây và điện toán cận biên

#### 5.1.1. Kiến trúc tổng quan

Trong những năm gần đây, sự hội tụ giữa công nghệ IoT và điện toán đám mây (thường được gọi là Cloud-IoT) đã tạo ra một mô hình mới đầy tiềm năng. Tuy nhiên, việc truyền toàn bộ dữ liệu thô từ các thiết bị IoT về trung tâm dữ liệu đám mây tập trung bộc lộ nhiều điểm nghẽn nghiêm trọng: tiêu tốn băng thông mạng viễn thông, độ trễ truyền dẫn lớn, không đáp ứng kịp các tác vụ thời gian thực và nguy cơ rò rỉ dữ liệu nhạy cảm.

Chính vì vậy, kiến trúc điện toán phân tán đa tầng bao gồm 3 lớp chính đã được đề xuất và áp dụng rộng rãi:
1. **Lớp thiết bị IoT (Things Layer / End Devices):** Các cảm biến, cơ cấu chấp hành, thiết bị đeo thông minh thực hiện thu thập dữ liệu và thực thi lệnh điều khiển.
2. **Lớp cận biên (Edge / Fog Layer):** Các thiết bị có năng lực tính toán trung bình đặt tại biên mạng (Edge Gateways, Edge Routers, trạm phát sóng di động base station) thực hiện lọc dữ liệu, tiền xử lý, lưu trữ tạm và phản hồi tức thời.
3. **Lớp đám mây (Cloud Layer):** Các trung tâm dữ liệu quy mô lớn (Data Centers) thực hiện lưu trữ lâu dài (Big Data), khai phá dữ liệu chuyên sâu và huấn luyện các mô hình AI/Machine Learning."""

p[118] = """Sự phát triển bùng nổ của công nghệ IoT dẫn đến kiến trúc hệ thống mạng ngày càng phức tạp và phân chia thành nhiều lớp để đáp ứng nhu cầu ngày càng cao của con người. Trong xu hướng đó, các hệ thống, ứng dụng IoT hiện đại ngày nay thường được tổ chức thành các lớp bao gồm: lớp thiết bị IoT, lớp thiết bị cận biên, lớp trung tâm dữ liệu trên hạ tầng điện toán đám mây.

**Hình 5.1.** Kiến trúc tổng quan hệ thống IoT kết hợp Điện toán đám mây và Điện toán biên [1]

- **Lớp thiết bị IoT:** Bao gồm hàng tỷ thiết bị cảm biến, cơ cấu chấp hành kết nối với nhau thông qua các giao thức mạng không dây tầm ngắn và tiết kiệm năng lượng (Zigbee, Bluetooth, 6LoWPAN, Wi-Fi, LoRa).
- **Lớp thiết bị cận biên:** Đóng vai trò là cầu nối thông minh trung gian giữa mạng cảm biến cục bộ và mạng diện rộng Internet. Lớp này thực hiện phân loại dữ liệu, nén dữ liệu, loại bỏ dữ liệu dư thừa và giải quyết các bài toán cục bộ mà không cần phụ thuộc vào kết nối đám mây."""

p[119] = """cao trải nghiệm người dùng cũng là chủ đề mở và đang thu hút giới nghiên cứu.

- **Trung tâm dữ liệu (Data Center):** Là nơi hiện thực hạ tầng điện toán đám mây, với khả năng tính toán và lưu trữ khổng lồ. Trung tâm dữ liệu thực hiện quản lý, điều khiển, phân phối nguồn tài nguyên tính toán dựa trên các công nghệ ảo hóa (Virtual Machines, Containers), chạy các dịch vụ phân tích dữ liệu lớn và cung cấp giao diện quản lý toàn diện cho người dùng và các doanh nghiệp.

#### 5.1.2. Các yêu cầu và đặc trưng cơ bản của các hệ thống tính toán cho IoT

Để đáp ứng được yêu cầu của các ứng dụng IoT phức tạp, các hệ thống tính toán (cả ở biên và đám mây) cần thỏa mãn các tiêu chí kỹ thuật cốt lõi sau:
- **Độ trễ truyền thông thấp (Low Latency):** Đối với các ứng dụng điều khiển thời gian thực (như xe tự hành, điều khiển robot công nghiệp, phẫu thuật từ xa), thời gian đáp ứng phải dưới mức hàng chục mili-giây.
- **Khả năng mở rộng (Scalability):** Hệ thống phải có khả năng tiếp nhận và xử lý mượt mà khi số lượng thiết bị IoT kết nối tăng vọt từ hàng nghìn lên hàng triệu nút.
- **Tính sẵn sàng và độ tin cậy (Availability & Reliability):** Đảm bảo dịch vụ hoạt động liên tục 24/7, có cơ chế sao lưu, dự phòng và tự phục hồi khi có sự cố nút mạng.
- **Tiết kiệm băng thông mạng (Bandwidth Optimization):** Tiền xử lý và nén dữ liệu tại biên giúp giảm tải đường truyền uplink lên đám mây."""

p[120] = """- **Khả năng bảo mật dữ liệu (Data Security):** Đảm bảo hệ thống chịu được các cuộc tấn công từ bên ngoài nhắm vào dữ liệu bí mật lưu trữ trong hệ thống hay truyền trên mạng bằng các cơ chế mã hóa đầu-cuối.
- **Các dịch vụ bảo mật (Service Security):** Giúp hệ thống chịu được các cuộc tấn công từ bên ngoài nhắm vào việc làm tê liệt các dịch vụ (như tấn công từ chối dịch vụ phân tán DDoS).
- **Tính không đồng nhất (Heterogeneity):** Có khả năng tích hợp và làm việc ăn khớp giữa nhiều nền tảng phần cứng, hệ điều hành và giao thức truyền thông khác nhau.

### 5.2. Nền tảng điện toán đám mây và ứng dụng trong IoT

Theo định nghĩa của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST): *Điện toán đám mây là một mô hình cho phép truy cập mạng thuận tiện, theo yêu cầu tới một nhóm tài nguyên tính toán có thể cấu hình được (ví dụ: mạng, máy chủ, lưu trữ, ứng dụng và dịch vụ) mà có thể được cung cấp và giải phóng nhanh chóng với nỗ lực quản lý tối thiểu hoặc sự tương tác tối thiểu từ nhà cung cấp dịch vụ.*

Trong ngữ cảnh IoT, điện toán đám mây đóng vai trò là "bộ não trung tâm" thu thập, tích hợp dữ liệu từ mọi nguồn phân tán, cung cấp tài nguyên tính toán vô hạn cho việc phân tích dữ liệu lớn (Big Data Analytics) và đưa ra các quyết định thông minh mang tính chiến lược."""

p[121] = """nối và ảo hóa một cách linh động và được thể hiện như một hoặc nhiều tài nguyên tính toán đồng nhất dựa trên các thỏa thuận ở mức dịch vụ được thiết lập thông qua việc đàm phán giữa nhà cung cấp dịch vụ và người tiêu dùng.

#### 5.2.1. Đặc trưng cơ bản của điện toán đám mây

NIST xác định 5 đặc trưng cơ bản của điện toán đám mây:
1. **Tự phục vụ theo nhu cầu (On-demand Self-service):** Người dùng có thể tự cấu hình các tài nguyên tính toán (như thời gian máy chủ, dung lượng lưu trữ mạng) một cách tự động khi cần mà không cần tương tác trực tiếp với con người bên phía nhà cung cấp.
2. **Truy cập mạng rộng rãi (Broad Network Access):** Các tài nguyên được cung cấp qua mạng Internet và có thể truy cập thông qua các cơ chế tiêu chuẩn từ nhiều loại thiết bị khách khác nhau (máy tính, điện thoại di động, máy tính bảng).
3. **Dùng chung tài nguyên (Resource Pooling):** Nguồn tài nguyên tính toán của nhà cung cấp được gộp lại để phục vụ nhiều người dùng (multi-tenant model), với các tài nguyên vật lý và ảo hóa được phân bổ linh hoạt theo nhu cầu.
4. **Co giãn nhanh chóng (Rapid Elasticity):** Tài nguyên có thể được cấp phát và giải phóng một cách nhanh chóng, co giãn linh hoạt theo lưu lượng tải thực tế.
5. **Đo lường dịch vụ (Measured Service):** Hệ thống đám mây tự động kiểm soát và tối ưu hóa việc sử dụng tài nguyên bằng cách đo lường chi tiết ở mức dịch vụ (dung lượng lưu trữ, băng thông tiêu thụ, chu kỳ CPU sử dụng) để tính phí theo mức độ sử dụng (pay-as-you-go)."""

p[122] = """thuật như: tính toán song song (parallel computing), cân bằng tải (load balancing), định thời tác vụ (job scheduling).

Khả năng truy cập và tính linh động thể hiện qua việc các thiết bị, sản phẩm, dịch vụ và môi trường điện toán đám mây có thể truy cập với nhiều người nhất có thể. Tính linh động dịch vụ cho phép người dùng chuyển đổi các ứng dụng và dữ liệu giữa các đám mây khác nhau mà không bị trói buộc vào một nhà cung cấp duy nhất.

#### 5.2.2. Lợi ích của điện toán đám mây

Việc ứng dụng điện toán đám mây mang lại nhiều lợi ích to lớn cho các tổ chức và doanh nghiệp phát triển hệ thống IoT:
- **Tiết kiệm chi phí đầu tư ban đầu (Cost Reduction):** Doanh nghiệp không cần phải đầu tư chi phí mua sắm máy chủ vật lý, xây dựng phòng máy lạnh và thuê đội ngũ bảo trì tốn kém. Thay vào đó chỉ cần trả phí thuê bao theo mức sử dụng thực tế.
- **Tập trung vào nghiệp vụ cốt lõi:** Các nhà phát triển giải pháp IoT có thể tập trung toàn lực vào việc phát triển ứng dụng và thuật toán kinh doanh, để việc quản trị hạ tầng máy chủ cho các nhà cung cấp đám mây chuyên nghiệp đảm nhiệm."""

p[123] = """doanh nghiệp có thể cải tiến hiệu năng các dịch vụ IT, dễ dàng vận hành và quản lý tập trung các dịch vụ thông qua nhà cung cấp dịch vụ.
- **Nâng cao hiệu quả sử dụng tài nguyên:** Doanh nghiệp có thể hợp tác với nhà cung cấp dịch vụ điện toán đám mây để tận dụng công nghệ ảo hóa, tránh lãng phí năng lực tính toán dư thừa khi hệ thống nhàn rỗi.
- **Khả năng phục hồi sau thảm họa (Disaster Recovery):** Dữ liệu được lưu trữ phân tán và sao lưu tự động trên nhiều trung tâm dữ liệu ở các khu vực địa lý khác nhau, đảm bảo dữ liệu không bị mất mát khi xảy ra sự cố thiên tai hoặc hỏng hóc phần cứng.

**Hình 5.2.** Khung phân cấp dịch vụ điện toán đám mây

Mô hình phân cấp dịch vụ điện toán đám mây truyền thống được chia thành 3 lớp cơ bản (Hình 5.2):
1. **IaaS (Infrastructure as a Service - Hạ tầng như một dịch vụ)**
2. **PaaS (Platform as a Service - Nền tảng như một dịch vụ)**
3. **SaaS (Software as a Service - Phần mềm như một dịch vụ)**"""

p[124] = """#### 5.2.3. Mô hình IaaS

Các dịch vụ trên hạ tầng điện toán đám mây được phát triển theo 3 loại mô hình dịch vụ cơ bản. Trong đó, mô hình thấp nhất là **Hạ tầng như một dịch vụ (Infrastructure as a Service - IaaS)**:

Trong mô hình IaaS, nhà cung cấp dịch vụ cung cấp cho người dùng các tài nguyên phần cứng máy tính được ảo hóa thô, bao gồm:
- **Năng lực tính toán (Compute):** Các máy ảo (Virtual Machines) hoặc bare-metal servers với số lượng CPU core, dung lượng RAM xác định.
- **Không gian lưu trữ (Storage):** Lưu trữ khối (Block Storage), lưu trữ đối tượng (Object Storage), lưu trữ tệp (File Storage).
- **Tài nguyên mạng (Networking):** Bộ định tuyến ảo (Virtual Routers), tường lửa ảo (Firewalls), địa chỉ IP tĩnh công cộng, mạng riêng ảo (VPC/VLAN).

Người dùng có toàn quyền kiểm soát hệ điều hành được cài đặt trên máy ảo, cấu hình các dịch vụ mạng, triển khai các phần mềm trung gian (middleware) và các ứng dụng của mình. Nhà cung cấp IaaS chịu trách nhiệm quản lý và bảo trì toàn bộ phần cứng vật lý bên dưới (máy chủ, hệ thống lưu trữ SAN/NAS, thiết bị chuyển mạch mạng, nguồn điện và phòng máy)."""

p[125] = """Người dùng không thể quản lý hay điều khiển hạ tầng bên dưới của nhà cung cấp dịch vụ điện toán đám mây nhưng có thể điều khiển hệ điều hành, bộ nhớ, ứng dụng được triển khai cũng như những cài đặt liên quan tới các thành phần kết nối mạng giữa các máy ảo mà mình quản lý. Một số nền tảng cung cấp dịch vụ này như: Amazon EC2, Google Compute Engine, Microsoft Azure Virtual Machines, OpenNebula, OpenStack...

**Hình 5.3.** Các thành phần chính trong dịch vụ hạ tầng IaaS

Hình 5.3 mô tả các thành phần chức năng cốt lõi của một hệ thống IaaS:
- **Quản lý máy chủ ảo (Virtual Compute Management):** Cung cấp các công cụ tạo mới, xóa bỏ, khởi động, tạm dừng, di chuyển nóng (live migration) các máy ảo giữa các máy chủ vật lý.
- **Quản lý lưu trữ ảo (Virtual Storage Management):** Cấp phát và gắn kết các ổ đĩa ảo, quản lý ảnh đĩa hệ điều hành (Image Repository).
- **Quản lý mạng ảo (Virtual Network Management):** Cấu hình các subnet, cấp phát địa chỉ IP qua DHCP ảo, thiết lập định tuyến và quy tắc bảo mật an ninh mạng (Security Groups)."""

p[126] = """(virtual storage) bao gồm phân bổ không gian lưu trữ, giải phóng bộ nhớ, ghi dữ liệu, đọc dữ liệu...; quản lý mạng ảo (virtual network) bao gồm việc cấp phát địa chỉ IP, đăng ký tên miền, thiết lập kết nối, phân bổ băng thông đường truyền...

#### 5.2.4. Mô hình PaaS

**Nền tảng như một dịch vụ (Platform as a Service - PaaS)** là mô hình cung cấp một môi trường hoàn chỉnh trên đám mây để các nhà phát triển có thể xây dựng, thử nghiệm, triển khai và quản lý các ứng dụng mà không cần quan tâm đến việc mua sắm, cài đặt và bảo trì hạ tầng phần cứng cũng như hệ điều hành bên dưới.

Trong mô hình PaaS, nhà cung cấp quản lý toàn bộ hạ tầng (máy chủ, mạng, lưu trữ) cùng với hệ điều hành, runtime ngôn ngữ lập trình, hệ quản trị cơ sở dữ liệu và các phần mềm trung gian. Người dùng chỉ cần tải lên mã nguồn ứng dụng và cấu hình các thiết lập ứng dụng.

Đối với IoT, các nền tảng **IoT Cloud Platforms (IoT PaaS)** rất phát triển, cung cấp sẵn các dịch vụ chuyên biệt cho IoT như:
- Cổng giao tiếp thiết bị (Device Gateway hỗ trợ giao thức MQTT, CoAP, HTTP).
- Quản lý danh mục và trạng thái thiết bị (Device Registry, Device Shadow).
- Động cơ xử lý luật thời gian thực (Rule Engine).
- Cơ sở dữ liệu chuỗi thời gian (Time-series Database).
- Công cụ trực quan hóa bảng điều khiển (Dashboard Visualization).

Các nền tảng IoT PaaS nổi tiếng bao gồm: AWS IoT Core, Google Cloud IoT, Microsoft Azure IoT Hub, ThingsBoard, Blynk, ThingSpeak."""

p[127] = """Kỹ thuật được sử dụng để hiện thực mô hình này đó là thiết kế môi trường chạy ứng dụng (runtime environment design). Môi trường chạy ứng dụng liên quan tới việc thu thập các dịch vụ phần mềm có sẵn, cần thiết để ứng dụng thực thi như các thư viện, gói phần mềm, gói công cụ cần thiết.

#### 5.2.5. Mô hình SaaS

**Phần mềm như một dịch vụ (Software as a Service - SaaS)** là mô hình dịch vụ đám mây hoàn chỉnh nhất ở tầng trên cùng, nơi nhà cung cấp phân phối một ứng dụng phần mềm hoàn thiện tới người dùng đầu cuối qua mạng Internet, thường là thông qua trình duyệt web hoặc ứng dụng di động.

Trong mô hình SaaS, người dùng không cần cài đặt phần mềm lên máy tính cá nhân, không cần quản lý hạ tầng hay nền tảng mà chỉ cần đăng nhập tài khoản và sử dụng các tính năng của phần mềm. Mọi vấn đề về cập nhật tính năng mới, vá lỗi bảo mật, sao lưu dữ liệu đều do nhà cung cấp đảm nhiệm hoàn toàn."""

p[128] = """các hạ tầng bên dưới bao gồm mạng, máy chủ, hệ điều hành, bộ nhớ hay thậm chí là các khả năng riêng lẻ của các ứng dụng trong khuôn khổ cấu hình giới hạn cho từng người dùng riêng lẻ.

Một số dịch vụ cung cấp theo mô hình SaaS phổ biến như: các ứng dụng của Google (Gmail, Google Docs, Google Drive), Microsoft 365, Dropbox, Salesforce CRM.

Trong lĩnh vực IoT, các ứng dụng SaaS thường là các giải pháp đóng gói hoàn chỉnh cho từng lĩnh vực chuyên ngành:
- **Hệ thống Quản lý Tòa nhà thông minh (Smart Building Management System):** Cho phép ban quản lý theo dõi tiêu thụ năng lượng điện, nước, điều khiển hệ thống chiếu sáng và HVAC.
- **Hệ thống Giám sát Hạm đội xe (Fleet Management):** Định vị phương tiện GPS, theo dõi hành trình xe, giám sát mức tiêu hao nhiên liệu.
- **Hệ thống Nông nghiệp thông minh SaaS:** Phân tích độ ẩm đất, dự báo sâu bệnh và tự động hóa hệ thống tưới nhỏ giọt."""

p[129] = """trụ, mô phỏng hóa sinh; các ứng dụng cho chính phủ như hệ thống y tế quốc gia, hệ thống giao thông vận tải...
- **Cổng thông tin (web portal):** cung cấp các dịch vụ tìm kiếm thông tin chuẩn, ngoài ra cũng có các dịch vụ khác như e-mail, tin tức, giá chứng khoán. Cổng thông tin cung cấp một giao diện web thống nhất cho người dùng truy cập tới nhiều dịch vụ khác nhau.

#### 5.2.6. Ứng dụng công nghệ điện toán đám mây trong xây dựng hệ thống giả lập WSN với số lượng nút lớn

Trong nghiên cứu và phát triển các giải pháp IoT và mạng cảm biến không dây (WSN), việc thử nghiệm trên các mạng quy mô lớn (hàng trăm đến hàng nghìn nút) gặp nhiều rào cản lớn:
- Chi phí mua sắm thiết bị phần cứng thực tế rất đắt đỏ.
- Khó khăn trong việc triển khai thực địa, nạp lại mã nguồn đồng loạt và giám sát trạng thái từng nút.
- Khó tái lập lại chính xác môi trường thử nghiệm khi cần đánh giá so sánh hiệu năng các giao thức định tuyến.

Để giải quyết bài toán trên, giải pháp ứng dụng hạ tầng đám mây mã nguồn mở **OpenStack** kết hợp với công nghệ ảo hóa nhẹ **Docker Containers** đã được nghiên cứu và xây dựng nhằm giả lập các mạng WSN quy mô lớn với chi phí thấp và độ linh hoạt cao."""

p[130] = """nguyên phục vụ cho các nghiên cứu khác giúp tối ưu việc sử dụng tài nguyên. Bên cạnh đó, việc triển khai ảo hóa lớp thứ hai với kỹ thuật Container cho phép tạo ra một số lượng rất lớn các nút ảo với lượng tài nguyên yêu cầu thấp giúp đáp ứng yêu cầu phục vụ các thử nghiệm có số lượng nút lớn.

**Hình 5.4.** Giải pháp tích hợp mạng cảm biến không dây trên hạ tầng đám mây OpenStack

Kiến trúc thử nghiệm tích hợp được mô tả trong Hình 5.4 bao gồm hai tầng ảo hóa:
1. **Tầng ảo hóa phần cứng OpenStack (IaaS):** Quản lý cụm máy chủ vật lý, tạo ra các máy ảo Linux (Swarm Workers) được kết nối với nhau qua mạng ảo diện rộng.
2. **Tầng ảo hóa nhẹ Docker Containers:** Chạy trên các máy ảo OpenStack. Mỗi container đóng vai trò giả lập một nút cảm biến không dây hoàn chỉnh, chạy hệ điều hành mạng nhúng (như Contiki hoặc Linux rút gọn), cài đặt giao thức định tuyến (như OLSR) và mã nguồn ứng dụng cảm biến."""

p[131] = """Quá trình triển khai ảnh sẽ gồm 5 bước được thực hiện ở 3 vị trí luận lý khác nhau:
1. Người dùng tạo ra tập tin đặc tả kịch bản thử nghiệm trên giao diện front-end của UIT-IoT Testbed tại máy người dùng.
2. Hệ thống biên dịch kịch bản thành tệp cấu hình triển khai Docker Compose và các tệp cấu hình mạng.
3. Master Node trên OpenStack nhận yêu cầu, phân tích số lượng nút và tự động khởi tạo các mạng ảo và container tương ứng trên các máy Swarm Workers.
4. Các container khởi động, kết nối vào các card mạng ảo tương ứng theo đúng cấu trúc tô-pô định trước và kích hoạt tiến trình định tuyến.
5. Dữ liệu giám sát từ các container được thu thập và gửi về giao diện người dùng theo thời gian thực.

##### 5.2.6.1. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý MESH của WSNs trên OpenStack

Trong cấu trúc mạng MESH, mọi nút mạng trong cùng phạm vi phát sóng đều có thể truyền tin trực tiếp với nhau hoặc qua nhiều chặng trung gian."""

p[132] = """giữa máy host và các container, các biến môi trường, các lệnh sẽ được thực thi khi khởi chạy containers. Ngoài ra, tập tin này còn đặc tả thông tin về các mạng ảo và kết nối giữa các containers thông qua các mạng ảo này.

**Hình 5.5.** Mô hình mạng luận lý dạng MESH trên OpenStack

Hình 5.5 mô tả giải pháp xây dựng mạng luận lý MESH trên OpenStack:
- Một mạng ảo OpenStack Neutron (mạng dùng chung) được tạo ra đóng vai trò như môi trường truyền sóng không dây chung.
- Tất cả các container giả lập nút mạng WSN đều gắn card mạng ảo kết nối vào cùng mạng con này.
- Giao thức định tuyến mạng cảm biến (như OLSR - Optimized Link State Routing) chạy bên trong mỗi container sẽ tự động trao đổi các bản tin HELLO và TC (Topology Control) để khám phá các láng giềng và xây dựng bảng định tuyến đa chặng tối ưu."""

p[133] = """##### 5.2.6.2. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý TREE của WSNs trên OpenStack

**Hình 5.6.** Mô hình mạng luận lý dạng TREE trên OpenStack

Điểm khác biệt so với kiến trúc mạng MESH là trong kiến trúc mạng TREE, các nút mạng được phân chia theo cấu trúc thứ bậc hình cây (cha - con). Mỗi nút chỉ giao tiếp trực tiếp với nút cha hoặc các nút con của nó mà không được truyền thông ngang hàng trực tiếp với các nhánh khác.

Để hiện thực cấu trúc mạng TREE trên OpenStack, hệ thống tự động sinh ra nhiều mạng ảo riêng biệt: mỗi mạng ảo đại diện cho một liên kết điểm - điểm (Point-to-Point) hoặc một nhóm cha - con cục bộ. Nhờ đó, các container chỉ có thể trao đổi gói tin qua các liên kết hợp lệ theo đúng cấu trúc cây định trước."""

p[134] = """##### 5.2.6.3. Giải pháp tích hợp, triển khai kiến trúc mạng WSNs (MESH/TREE) và giao thức định tuyến WSNs (olsr), mô hình giả lập thiết bị WSNs trên OpenStack

Để tự động hóa hoàn toàn quy trình khởi tạo và điều khiển mạng thử nghiệm WSN trên hạ tầng đám mây OpenStack, hệ thống sử dụng tập hợp các giao diện lập trình ứng dụng RESTful APIs do OpenStack cung cấp.

**Bảng 5.1.** Tóm lược một số APIs OpenStack (phần 1)

| Nhóm API | Root URL | API | Chức năng | Input | Output |
|:---|:---|:---|:---|:---|:---|
| **Identity (Keystone)** | `https://mitaka.uit.edu.vn:5000/v2.0` | `POST /v2.0/tokens` | Chứng thực người dùng, trả về token để thực thi các APIs khác | `tenantName` (tên project), `username`, `password` | `token` |
| **Networking (Neutron)** | `https://mitaka.uit.edu.vn:9696/v2.0` | `GET /v2.0/networks` | Liệt kê thông tin tất cả các networks | Không có | Danh sách networks |
| | | `POST /v2.0/networks` | Tạo mới một network ảo | `name` (tên network), `admin_state_up` | Thông tin network vừa tạo |
| | | `POST /v2.0/subnets` | Tạo mới một subnet ảo | `network_id`, `ip_version`, `cidr`, `enable_dhcp` | Thông tin subnet vừa tạo |
| **Compute (Nova)** | `https://mitaka.uit.edu.vn:8774/v2.1` | `GET /images` | Liệt kê thông tin các images có trong OpenStack | Không có | Danh sách images |"""

p[135] = """**Bảng 5.1.** Tóm lược một số APIs OpenStack (phần 2 - Compute APIs)

| Nhóm API | Root URL | API | Chức năng | Input | Output |
|:---|:---|:---|:---|:---|:---|
| **Compute (Nova)** *(tiếp theo)* | `https://mitaka.uit.edu.vn:8774/v2.1` | `GET /flavors` | Liệt kê thông tin các flavors (thông số cấu hình CPU, RAM... cho máy ảo) | Không có | Danh sách flavors |
| | | `GET /os-keypairs` | Liệt kê thông tin các keypairs (cặp SSH key dùng chứng thực) | Không có | Danh sách keypairs |
| | | `POST /servers` | Tạo một máy ảo mới trong OpenStack | `name`, `image_id`, `flavor_id`, danh sách networks, `key_name` | Thông tin máy ảo vừa tạo |

Chức năng chính của Compute API là tạo, xóa, sửa các Instance (máy ảo) có trong OpenStack. Ngoài ra, Compute API cung cấp các APIs hỗ trợ việc tạo, xóa, sửa, lấy thông tin images, flavors... Nhờ hệ thống APIs này, hệ thống UIT-IoT Testbed có thể tự động cấp phát tài nguyên tính toán và thiết lập mạng ảo chỉ trong vài phút."""

p[136] = """**Hình 5.7.** Kiến trúc mô phỏng thiết bị WSN sử dụng container/VM trên OpenStack

**Hình 5.8.** Cấu trúc liên kết mạng mô phỏng

Hình 5.7 và Hình 5.8 mô tả kiến trúc triển khai thử nghiệm:
- Mỗi máy ảo OpenStack đóng vai trò là một Host chứa cụm Docker Engine.
- Các container được khởi tạo với hình ảnh chứa sẵn hệ điều hành Linux gọn nhẹ (Alpine Linux hoặc Ubuntu Core) cùng gói phần mềm giao thức định tuyến OLSR (`olsrd`).
- Tập tin cấu hình `olsrd.conf` được tự động sinh ra và gắn vào container khi khởi chạy để thiết lập các tham số định tuyến (chu kỳ gửi gói tin HELLO, thời gian sống của tuyến đường).
- Ứng dụng mô phỏng gửi dữ liệu cảm biến định kỳ qua socket UDP đến nút Sink để đánh giá tỷ lệ chuyển gói thành công (PDR - Packet Delivery Ratio) và độ trễ truyền gói tin trung bình."""

p[137] = """Quy trình triển khai cụm Docker Swarm được thực hiện tuần tự qua các bước: gọi API chứng thực `POST /v2.0/tokens` để lấy access token; sau đó gọi các APIs lấy danh sách hình ảnh (`GET /images`), cấu hình máy ảo (`GET /flavors`), khóa SSH (`GET /os-keypairs`) và mạng ảo (`GET /v2.0/networks`). Cuối cùng, hệ thống gửi yêu cầu `POST /servers` để khởi tạo các máy ảo worker và kích hoạt các containers.

### 5.3. Nền tảng điện toán cận biên và ứng dụng trong IoT

#### 5.3.1. Kiến trúc triển khai điện toán cận biên trong IoT

Điện toán cận biên (Edge Computing) là mô hình xử lý tính toán phân tán, trong đó các tác vụ xử lý thông tin, lưu trữ và điều khiển được đặt tại vị trí biên của mạng – gần với nguồn phát sinh dữ liệu (các thiết bị cảm biến và người dùng). Mô hình này giải quyết triệt để các hạn chế cố hữu của điện toán đám mây truyền thống về độ trễ, lưu lượng mạng và tính riêng tư."""

p[138] = """Hình 5.9 mô tả kiến trúc tổng quan các thành phần của hệ thống tính toán cận biên áp dụng trong IoT. Hệ thống bao gồm:
1. **Các thiết bị IoT:** Như các cảm biến, thiết bị động cơ, mạch điều khiển thu thập dữ liệu từ môi trường vật lý.
2. **Các thiết bị tính toán cận biên:** Bao gồm các IoT Gateway, thiết bị biên chuyên dụng (Edge Nodes), máy tính nhúng, trạm gốc viễn thông di động (eNodeB trong 4G/5G).
3. **Các máy chủ đám mây:** Thực hiện các chức năng lưu trữ dài hạn, phân tích dữ liệu lớn và quản lý chiến lược toàn mạng.

**Hình 5.9.** Kiến trúc điện toán sương mù / điện toán biên trong hệ thống IoT

#### 5.3.2. Các công nghệ, kỹ thuật nổi bật cho tính toán cận biên trong IoT

Để hiện thực hóa tính toán cận biên hiệu quả, nhiều công nghệ và kỹ thuật tiên tiến đã được nghiên cứu và ứng dụng:"""

p[139] = """- **Quản lý tài nguyên phân tán (Resource Management):** Điều phối linh hoạt các nguồn tài nguyên tính toán (CPU, GPU, RAM) và lưu trữ hạn chế tại biên nhằm phục vụ tối ưu đồng thời nhiều ứng dụng IoT khác nhau.
- **Tính toán kết hợp truyền thông (Joint Communication and Computing):** Tối ưu hóa đồng thời việc phân bổ kênh truyền vô tuyến và phân bổ năng lực xử lý tính toán để giảm thiểu tổng năng lượng tiêu thụ và độ trễ xử lý của các thiết bị IoT di động.
- **Di chuyển tác vụ tính toán (Computation Offloading):** Cơ chế cho phép thiết bị IoT có năng lực xử lý yếu hoặc sắp cạn pin chuyển giao một phần hoặc toàn bộ tác vụ tính toán nặng (như giải mã tín hiệu, nhận dạng hình ảnh) sang cho thiết bị biên kế cận xử lý thay."""

p[140] = """**Công nghệ xử lý thông minh tại thiết bị cận biên (Edge Intelligence / Edge AI)**

Lượng dữ liệu khổng lồ từ các thiết bị IoT thu thập đóng vai trò quan trọng trong việc xây dựng các tập dữ liệu (dataset) dùng cho việc huấn luyện và phát triển các giải pháp máy học. Tuy nhiên, việc truyền toàn bộ dữ liệu về đám mây gây tắc nghẽn mạng nghiêm trọng. Xu hướng mới là đưa trí tuệ nhân tạo ra biên:
- **Suy luận tại biên (Edge Inference):** Sử dụng các mô hình học sâu đã được nén nhẹ (bằng kỹ thuật lượng tử hóa Quantization, cắt tỉa Pruning, tri thức chưng cất Knowledge Distillation) như TensorFlow Lite, TinyML, ONNX để thực thi nhận dạng khuôn mặt, phát hiện dị thường trực tiếp ngay trên vi điều khiển hoặc máy tính nhúng tại chỗ với độ trễ tính bằng mili-giây.
- **Học liên kết (Federated Learning):** Các nút biên tự huấn luyện mô hình máy học cục bộ dựa trên dữ liệu riêng tư của mình và chỉ gửi các trọng số mô hình (model updates/gradients) về đám mây để tổng hợp mô hình chung toàn cầu, qua đó bảo vệ tuyệt đối tính riêng tư dữ liệu người dùng."""

p[141] = """rộng hệ thống bằng việc cho phép chia sẻ tài nguyên dựa trên nhu cầu trong lúc chạy (runtime needs).

### 5.4. Các vấn đề tồn tại và hướng nghiên cứu trong tương lai

Mặc dù việc kết hợp giữa điện toán đám mây và điện toán cận biên mở ra nhiều cơ hội phát triển vượt bậc cho hệ sinh thái IoT, nhiều thách thức kỹ thuật quan trọng vẫn đang cần tiếp tục nghiên cứu:
- **Quản lý tính di động (Mobility Management):** Khi các nút IoT hoặc phương tiện di chuyển liên tục qua các vùng phủ sóng của các trạm biên khác nhau, việc di chuyển trạng thái dịch vụ (Service / Container Migration) liền mạch không làm gián đoạn kết nối là bài toán phức tạp.
- **Bảo mật và quyền riêng tư tại biên:** Các thiết bị biên thường đặt ở môi trường công cộng bên ngoài, dễ bị tấn công vật lý, cài mã độc hoặc giả mạo. Cần phát triển các cơ chế xác thực phân tán dựa trên công nghệ chuỗi khối (Blockchain) hoặc môi trường thực thi tin cậy (Trusted Execution Environment - TEE).
- **Cân bằng năng lượng và tài nguyên xanh (Green Computing):** Tối ưu hóa hiệu suất tiêu thụ năng lượng của các cụm máy chủ biên khi hoạt động bằng năng lượng tái tạo."""

p[142] = """pháp mã hóa, bảo mật đã được nghiên cứu và triển khai thành công trên thiết bị IoT có tài nguyên hạn chế.

## BÀI TẬP CHƯƠNG 5

1. Hãy phân tích các yêu cầu và đặc trưng cơ bản của các hệ thống tính toán cho IoT.
2. Hãy so sánh ưu và nhược điểm của các mô hình điện toán đám mây (IaaS, PaaS, SaaS).
3. Hãy so sánh ưu và nhược điểm của các công nghệ điện toán đám mây và điện toán cận biên. Liệt kê những ứng dụng IoT phù hợp cho mỗi công nghệ điện toán này.
4. Hãy so sánh các công nghệ ảo hóa được sử dụng trong IoT (máy ảo truyền thống so với container).
5. Hãy xây dựng một kịch bản ứng dụng tính toán cận biên trong IoT.
6. Từ nền tảng Arduino và Raspberry Pi 3, hãy xây dựng ứng dụng y tế thông minh áp dụng điện toán đám mây và điện toán cận biên.
7. Hãy xây dựng ứng dụng Nông nghiệp thông minh áp dụng kỹ thuật điện toán đám mây và điện toán cận biên. Sau đó so sánh ưu và nhược điểm của hai hướng tiếp cận này.
8. Trong ứng dụng giám sát giao thông thông minh, các camera được đặt trên đường và truyền tín hiệu video về các gateway. Dữ liệu từ các gateway sau đó được truyền về Cloud. Hãy xây dựng ứng dụng giám sát giao thông thông minh để đếm số phương tiện qua lại trong một khoảng thời gian. Xây dựng hai kịch bản đếm số phương tiện tại gateway và tại cloud. Sau đó so sánh hai kịch bản này."""

# Apply to file
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(^## Trang \d+\s*$)', text, flags=re.MULTILINE)
pages_dict = {}
for i in range(1, len(parts), 2):
    p_num = int(re.search(r'\d+', parts[i]).group(0))
    pages_dict[p_num] = parts[i+1]

for page_num in range(116, 143):
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

print("Chapter 5 (pages 116-142) updated successfully!")
