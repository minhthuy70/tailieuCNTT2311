# -*- coding: utf-8 -*-
"""
Builder Part 2: Detailed TOC & Summaries for Chapter 1 and Chapter 2
"""
from word_helpers import (
    add_heading1, add_heading2, add_heading3, add_heading4,
    add_bullet, add_subbullet, add_callout, add_table
)

def build_part2_chapter1(doc):
    add_heading1(doc, "PHẦN II: MỤC LỤC PHÂN CẤP CHI TIẾT & TÓM TẮT TRỌNG TÂM CÁC CHƯƠNG")
    
    add_heading1(doc, "CHƯƠNG 1: GIỚI THIỆU VỀ CÔNG NGHỆ INTERNET VẠN VẬT (IOT)")
    
    # 1.1
    add_heading2(doc, "1.1. Tổng quan về công nghệ Internet vạn vật")
    
    # 1.1.1
    add_heading3(doc, "1.1.1. Khái niệm và bối cảnh phát triển")
    add_bullet(doc, "Quy mô kết nối: Hiện có hơn 20 tỷ thiết bị kết nối Internet, tăng trung bình 80 thiết bị mới mỗi giây, dự báo đạt 50 tỷ thiết bị vào năm 2020 (Thống kê của Cisco).", "Số liệu phát triển: ")
    add_bullet(doc, "Mọi thiết bị, đồ vật đều có thể kết nối và tương tác thông minh (tra cứu thực phẩm trên tủ lạnh, điều khiển xe tự lái, cảm biến giao thông trên hàng triệu xe máy tại Hà Nội và TP.HCM).", "Bản chất mạng IoT: ")
    add_bullet(doc, "5 giai đoạn phát triển của Internet (Evolution of IoT):", "Quá trình tiến hóa: ")
    add_subbullet(doc, "Giai đoạn con người giao tiếp với con người (Điện thoại cố định, SMS, thư tín).", "1. Pre-Internet: ")
    add_subbullet(doc, "Con người truy cập nội dung số trên mạng (World Wide Web - WWW, Email, giải trí, thông tin).", "2. Internet of Content: ")
    add_subbullet(doc, "Internet cung cấp dịch vụ trực tuyến (E-commerce thương mại điện tử, E-productivity...).", "3. Internet of Services: ")
    add_subbullet(doc, "Mạng xã hội kết nối con người với con người trên quy mô toàn cầu (Facebook, YouTube, Twitter, Skype...).", "4. Internet of People: ")
    add_subbullet(doc, "Máy móc/thiết bị giao tiếp tự động với máy móc (M2M) - Thiết bị tự nhận diện, theo dõi, giám sát, đo lường và chia sẻ dữ liệu mà không cần con người can thiệp.", "5. Internet of Things: ")
    add_callout(doc, "TỔNG KẾT QUÁ TRÌNH TIẾN HÓA", "Internet phát triển tuần tự: Người => Nội dung => Dịch vụ => Con người => Thiết bị. IoT là đỉnh cao nơi các thiết bị thông minh kết nối và tự động trao đổi dữ liệu.", bg="F8FAFC", border_color="0EA5E9")

    # 1.1.2
    add_heading3(doc, "1.1.2. Định nghĩa IoT (Dạng đơn giản)")
    add_bullet(doc, "IoT ở dạng đơn giản là mạng lưới các phần tử vật lý được kích hoạt và trao quyền bởi 4 thành phần nền tảng:", "Định nghĩa cốt lõi: ")
    add_subbullet(doc, "Thu thập thông tin và dữ liệu từ môi trường vật lý xung quanh.", "1. Sensors (Cảm biến): ")
    add_subbullet(doc, "Định danh và xác định duy nhất nguồn gốc dữ liệu (ví dụ: địa chỉ IP, MAC, RFID tag).", "2. Identifiers (Bộ nhận dạng): ")
    add_subbullet(doc, "Phân tích, xử lý và chuyển đổi dữ liệu thành tri thức.", "3. Software (Phần mềm): ")
    add_subbullet(doc, "Truyền thông tin, trao đổi dữ liệu và gửi thông báo qua mạng toàn cầu.", "4. Internet connectivity (Kết nối Internet): ")

    # 1.1.3
    add_heading3(doc, "1.1.3. Nguồn gốc và định nghĩa IoT hoàn chỉnh hơn")
    add_bullet(doc, "'Things' (Vật/Đồ vật) là bất cứ thứ gì và mọi thứ trong đời sống (từ thiết bị gia dụng, tòa nhà, ô tô, con người, động vật, đến cây cỏ...).", "Khái niệm 'Things': ")
    add_bullet(doc, "Bao gồm cả Tiêu chuẩn (Standards) và Quy trình (Processes) cho phép các 'Vật' kết nối qua 'Internet' để trao đổi 'Dữ liệu', đảm bảo khả năng tương tác liên thông và tự động hóa quy trình:", "Định nghĩa đầy đủ: ")
    add_subbullet(doc, "Chuyển đổi dữ liệu thô (raw data) thành thông tin chi tiết, có giá trị để ra quyết định tốt hơn.", "• Dữ liệu (Data): ")
    add_subbullet(doc, "Cung cấp đúng thông tin cho đúng người hoặc đúng máy móc vào đúng thời điểm.", "• Quy trình (Process): ")
    add_subbullet(doc, "Các thiết bị và thực thể vật lý kết nối vào Internet để tương tác thông minh.", "• Đồ vật (Things): ")

    # 1.1.4
    add_heading3(doc, "1.1.4. Làm thế nào để theo dõi và điều khiển mọi vật từ bất cứ đâu?")
    add_bullet(doc, "1) Định danh duy nhất (Unique Identity/IP address); 2) Khả năng giao tiếp không dây (Wireless communications); 3) Khả năng cảm nhận thông tin vật lý (Sensors).", "3 Yêu cầu nền tảng: ")
    add_bullet(doc, "Phương tiện truyền thông (Medium to communicate) được đảm nhận bởi hạ tầng mạng viễn thông toàn cầu.", "Môi trường truyền dẫn: ")
    add_bullet(doc, "4 Yêu cầu cơ bản của một giải pháp IoT hoàn chỉnh:", "4 Yêu cầu giải pháp: ")
    add_subbullet(doc, "Mỗi thực thể phải có một địa chỉ định danh duy nhất (IPv4/IPv6).", "1. Unique Address: ")
    add_subbullet(doc, "Khả năng cảm nhận môi trường và khả năng tác động/điều khiển thực tế.", "2. Sensing & Actuating: ")
    add_subbullet(doc, "Khả năng truyền nhận dữ liệu qua các liên kết mạng có dây/không dây.", "3. Ability to communicate: ")
    add_subbullet(doc, "Khả năng gửi cảnh báo kịp thời và chấp nhận lệnh điều khiển từ xa.", "4. Notification & Control: ")

    # 1.1.5 & 1.1.6
    add_heading3(doc, "1.1.5 & 1.1.6. Lý do giám sát điều khiển & Chủ thể giám sát")
    add_bullet(doc, "Theo dõi từ xa bởi chuyên gia y tế (bệnh nhân tại nhà); Học hỏi và tra cứu thông tin vật thể qua smartphone; Quản lý tối ưu nguồn lực Smart City; Cung cấp giải trí chi phí thấp và cơ hội kinh doanh khổng lồ.", "4 Lý do chính: ")
    add_bullet(doc, "Bất kỳ ai hoặc bất kỳ máy móc nào: Chủ nhà (giám sát an ninh, đèn, HVAC); Doanh nghiệp / Nhà cung cấp dịch vụ mạng (giám sát hạ tầng tại Trung tâm Vận hành Mạng - NOC).", "Chủ thể giám sát: ")

    # 1.1.7
    add_heading3(doc, "1.1.7. Làm thế nào để đảm bảo an ninh trong IoT?")
    add_bullet(doc, "Trước IoT, bảo mật CNTT hoạt động trong 'bong bóng an toàn' khép kín đằng sau tường lửa (firewalls). Trong kỷ nguyên IoT, dữ liệu được thu thập từ các cảm biến công cộng ngoài đường phố và qua chính sách mang thiết bị cá nhân (BYOD), khiến mạng dễ bị xâm nhập bởi dữ liệu độc hại.", "Sự thay đổi bối cảnh: ")
    add_bullet(doc, "4 LĨNH VỰC IOT DỄ BỊ TỔN THƯƠNG NHẤT (Vulnerable Areas):", "4 Lỗ hổng trọng yếu: ")
    add_subbullet(doc, "Dữ liệu truyền từ cảm biến đến gateway và lên cloud rất dễ bị nghe lén nếu không được mã hóa đầu cuối.", "1. Truy cập dữ liệu trong quá trình truyền (Network & Transport Security): ")
    add_subbullet(doc, "Hacker chiếm quyền kiểm soát giao diện lập trình ứng dụng (APIs) để vô hiệu hóa toàn bộ hệ thống (ví dụ: tắt camera giám sát, ngắt máy theo dõi bệnh nhân).", "2. Chiếm quyền điều khiển thiết bị (Control of APIs): ")
    add_subbullet(doc, "Dữ liệu lưu trữ chia sẻ trên đám mây không mã hóa, bị xâm nhập trái phép hoặc tấn công giả mạo dữ liệu qua kết nối Bluetooth (Bluetooth spoofing).", "3. Truy cập vào chính kho dữ liệu IoT (Data Storage Security): ")
    add_subbullet(doc, "Thiết bị IoT sử dụng mật khẩu mặc định của nhà sản xuất (default passwords), dễ bị dò quét và đánh cắp tài khoản quản trị.", "4. Đánh cắp danh tính người dùng hoặc mạng (Credential Theft): ")

    # 1.1.8
    add_heading3(doc, "1.1.8. Mô hình Cấp độ IoT (4-Level IoT Model) & 6 Ưu điểm vượt trội")
    add_bullet(doc, "Gồm tất cả các cảm biến (sensors) và bộ truyền động (actuators) - tức các 'Things' thu thập dữ liệu và chấp hành lệnh.", "1. Cấp độ Thiết bị (IoT Device Level): ")
    add_bullet(doc, "Bao gồm toàn bộ các thành phần mạng như IoT Gateway, Router, Switch, Access Point làm nhiệm vụ chuyển tiếp dữ liệu.", "2. Cấp độ Mạng (IoT Network Level): ")
    add_bullet(doc, "Cung cấp các hàm dịch vụ quản lý thiết bị: triển khai (deploy), cấu hình, khắc phục sự cố, bảo mật, quản lý và giám sát.", "3. Cấp độ Nền tảng Dịch vụ Ứng dụng (IoT Services Platform Level): ")
    add_bullet(doc, "Bao gồm tất cả các ứng dụng người dùng cuối chạy trên nền tảng IoT (Web App, Mobile App, ứng dụng phân tích dữ liệu chuyên ngành).", "4. Cấp độ Ứng dụng (IoT Application Level): ")
    add_callout(
        doc,
        "6 ƯU ĐIỂM CỦA MÔ HÌNH IOT 4 CẤP (HAY HỎI TRONG ĐỀ THI)",
        "1. Giảm độ phức tạp (Reduced Complexity): Chia nhỏ quy trình thành phần, dễ phát triển và sửa lỗi.\n"
        "2. Chuẩn hóa thành phần và giao diện (Standardized Components & Interfaces): Chuẩn hóa giao tiếp giữa các cấp, giúp các nhà sản xuất hợp tác phát triển giải pháp chung.\n"
        "3. Kỹ thuật module (Module Engineering): Cho phép phần cứng và phần mềm không đồng nhất giao tiếp liên thông.\n"
        "4. Khả năng tương tác giữa các hãng (Interoperability): Đảm bảo các khối công nghệ của các hãng khác nhau hoạt động ăn khớp.\n"
        "5. Thúc đẩy đổi mới (Accelerate Innovation): Lập trình viên tập trung vào bài toán cốt lõi mà không cần làm lại từ đầu các tính năng nền tảng.\n"
        "6. Đơn giản hóa việc đào tạo (Simplified Education): Giúp người học tiếp cận từng phần dễ hiểu, dễ quản lý."
    )

    # 1.1.9 & 1.1.10
    add_heading3(doc, "1.1.9 & 1.1.10. Các yếu tố thúc đẩy IoT & Sự hội tụ OT - IT")
    add_bullet(doc, "12 Yếu tố thúc đẩy chính: 1) Hội tụ OT & IT; 2) Doanh nghiệp nền tảng Internet; 3) Bùng nổ di động; 4) Bùng nổ mạng xã hội; 5) Phân tích tại biên (Edge Analytics); 6) Bùng nổ công nghệ; 7) Ảo hóa & Điện toán đám mây; 8) Chuyển đổi số; 9) Nâng cao trải nghiệm UI/UX; 10) Tốc độ thích ứng nhanh; 11) Sự gia tăng yêu cầu an ninh; 12) Định luật Moore.", "12 Yếu tố thúc đẩy IoT: ")
    add_bullet(doc, "Thế giới công nghệ công nghiệp, nhà máy, thiết bị điều khiển tự động hóa (SCADA, PLC, cảm biến, van). Yêu cầu dữ liệu thời gian thực nghiêm ngặt, an toàn, ổn định cao, hoạt động 24/7 với thời gian dừng bằng không (Zero downtime), không chấp nhận ngừng máy để cập nhật phần mềm.", "• Công nghệ Vận hành (OT): ")
    add_bullet(doc, "Thế giới các hệ thống thông tin tính toán, lưu trữ dữ liệu và mạng hỗ trợ kinh doanh (ERP, CRM, Email, Web). Linh hoạt hơn với việc cập nhật phần mềm.", "• Công nghệ Thông tin (IT): ")
    add_bullet(doc, "Sự xóa nhòa ranh giới giữa thế giới vật lý (OT) và kỹ thuật số (IT), kết hợp dữ liệu nhà máy với hệ thống điều hành thông minh.", "• Ý nghĩa của sự hội tụ: ")

    # 1.1.11
    add_heading3(doc, "1.1.11. Các doanh nghiệp sáng tạo dựa trên Internet & Đột phá công nghệ")
    add_bullet(doc, "Nền tảng kết nối hành khách và tài xế với chi phí cận biên bằng không (zero marginal cost); Sử dụng con quay hồi chuyển (Gyrometer) và GPS trên smartphone tài xế để phân tích tốc độ, gia tốc và phanh gấp.", "• Uber: ")
    add_bullet(doc, "Dịch vụ chia sẻ lưu trú phòng nghỉ, kết nối trực tuyến toàn cầu không cần sở hữu bất động sản.", "• Airbnb: ")
    add_bullet(doc, "Bán lẻ phá vỡ mô hình truyền thống, tối ưu chuỗi cung ứng trực tuyến không cần lưu trữ kho bãi lớn.", "• Amazon: ")
    add_bullet(doc, "Ví dụ kinh điển nhất của IoT - Biến đổi mô hình sản xuất xe hơi truyền thống sang phương tiện kết nối với hàng ngàn cảm biến và cập nhật phần mềm không dây OTAP; sử dụng động cơ cảm ứng AC Nikola Tesla.", "• Tesla: ")
    add_bullet(doc, "Bán tự lái (Semiautonomous) vs Tự lái hoàn toàn (Fully autonomous). Trang bị Laser range finder, Radar, Camera video, Actuator lái/phanh, GPS để xây dựng mô hình không gian 3D thời gian thực.", "• Xe tự lái (Self-Driving Cars): ")
    add_bullet(doc, "Lưu lượng di động tăng 18 lần; smartphone trung bình tiêu thụ 4GB/tháng (2019).", "• Bùng nổ di động: ")
    add_bullet(doc, "2/3 lưu lượng trung tâm dữ liệu đến từ đám mây (AWS, Azure, GCP). Dữ liệu sinh ra mỗi ngày bằng nửa tổng dữ liệu từ thuở sơ khai loài người.", "• Bùng nổ mạng xã hội & Cloud: ")
    add_bullet(doc, "Dữ liệu có cấu trúc (Structured - bảng biểu, hàng cột) vs Dữ liệu phi cấu trúc (Unstructured - video, ảnh, text, tín hiệu máy). Tiến hóa từ Analytics 1.0 (mô tả), 2.0 (dự đoán) đến 3.0 (tự động hóa quyết định tại biên).", "• Phân tích dữ liệu & Dữ liệu lớn: ")
    add_bullet(doc, "Sự sẵn sàng của các vi điều khiển và máy tính nhúng giá rẻ như Arduino, ESP8266, ESP32, Raspberry Pi.", "• Bùng nổ công nghệ phần cứng: ")
    add_bullet(doc, "1) Sức mạnh tính toán tăng gấp đôi mỗi 18 tháng; 2) Kích thước bóng bán dẫn thu nhỏ tới cấp độ nguyên tử; 3) Giá bóng bán dẫn giảm trên 50% mỗi năm.", "• 3 Quan sát của Định luật Moore: ")

    # 1.1.12 - 1.1.14
    add_heading3(doc, "1.1.12 - 1.1.14. Các lĩnh vực ứng dụng & Ví dụ thực tế")
    add_bullet(doc, "9 Lĩnh vực: 1) Vận tải; 2) Nơi làm việc (Robot tự hành); 3) Giáo dục; 4) Thể thao (Wearable tech); 5) Chăm sóc sức khỏe (Robot phẫu thuật, cảnh báo dịch); 6) Nông nghiệp (Robot thu hoạch); 7) Giải trí; 8) Smart Home; 9) Quốc phòng (UAV không người lái).", "Ứng dụng đa ngành: ")
    add_bullet(doc, "Vận tải tự động, công nghệ người máy Cyborg khắc phục hạn chế con người, giải quyết biến đổi khí hậu bằng Big Data, dự đoán tương lai bằng Machine Learning.", "IoT cho cuộc sống tốt đẹp hơn: ")
    add_bullet(doc, "1) Nhà máy thông minh 5G (Hợp tác NCU, ORing, Chunghwa Telecom); 2) Hệ thống giao thông thông minh STS sử dụng dữ liệu xe nổi (Floating Car Data - FCD) kết hợp camera và GPS.", "Ví dụ triển khai: ")

    # 1.2 - 1.5
    add_heading2(doc, "1.2 - 1.5. Thống kê, Tiêu chuẩn hóa, Thách thức kỹ thuật & Xu thế tại Việt Nam")
    add_bullet(doc, "Báo cáo Cisco: IoT mang lại 613 tỷ USD năm 2013, nhưng mới chỉ 1% thiết bị được kết nối. Châu Âu hỗ trợ qua chương trình FP7 (Call 5, Call 7) và Horizon-2020.", "1.2. Thống kê toàn cầu: ")
    add_bullet(doc, "OIC (Intel, Samsung, Dell thành lập); AllSeen Alliance (Qualcomm AllJoyn, Microsoft); IEEE 802.15.4; IETF CoAP, 6LoWPAN; Zigbee Alliance; W3C; OGC.", "1.3. Các tổ chức tiêu chuẩn: ")
    add_bullet(doc, "1) Phần mềm hỗ trợ toàn diện vòng đời; 2) Tăng tốc độ và băng thông; 3) Tối ưu năng lượng theo hướng Chip-Package-System (CPS); 4) Kiến trúc Cloud/Edge-based IoT.", "1.4. 4 Thách thức cốt lõi: ")
    add_bullet(doc, "Xây dựng đô thị thông minh gắn với IoT/5G, AI, Big Data và Cloud/Edge. Yêu cầu bắt buộc tuân theo chuẩn quốc tế để tránh phân mảnh và lãng phí tài chính. 4 Mục tiêu đô thị thông minh: Hiệu quả kinh tế cao (75% GDP), môi trường sống tốt hơn, phục vụ người dân tốt hơn, người dân tham gia giám sát chính quyền.", "1.5. Xu thế tại Việt Nam: ")

    # Bai tap C1
    add_callout(
        doc,
        "ĐÁP ÁN NHANH BÀI TẬP ÔN TẬP CHƯƠNG 1 (TRẢ LỜI NGAY TRONG PHÒNG THI)",
        "Câu 1: Các thiết bị có thể kết nối Internet? Trả lời: Bất kỳ thứ gì (Things) gồm thiết bị gia dụng (tủ lạnh, đèn), phương tiện (ô tô, xe máy), thiết bị đeo y tế, cảm biến công nghiệp, camera, điện thoại.\n"
        "Câu 2: Đặc điểm kỹ thuật của thiết bị IoT? Trả lời: Kích thước nhỏ, năng lượng tiêu thụ thấp (pin chạy nhiều năm), chi phí rẻ, có địa chỉ định danh duy nhất (IP/MAC), tích hợp cảm biến/cơ cấu chấp hành và kết nối không dây.\n"
        "Câu 3: Xu thế IoT trên thế giới và ở Việt Nam? Trả lời: Trên TG là hội tụ OT/IT, điện toán biên (Edge), mạng 5G/AI/Big Data. Ở VN là phát triển Đô thị thông minh (Smart City), giao thông thông minh, nông nghiệp công nghệ cao và ưu tiên mã nguồn mở.\n"
        "Câu 4: Ưu điểm IoT mang lại cho cuộc sống? Trả lời: Giám sát từ xa, tự động hóa quy trình, tiết kiệm năng lượng, nâng cao an toàn sức khỏe, tối ưu hóa giao thông và bảo vệ môi trường.\n"
        "Câu 5: Thách thức mà IoT đang gặp phải? Trả lời: Bảo mật và quyền riêng tư (4 lỗ hổng), chuẩn hóa giao tiếp tránh phân mảnh (Interoperability), quản lý tiêu thụ năng lượng và hạ tầng băng thông."
    )

def build_part2_chapter2(doc):
    add_heading1(doc, "CHƯƠNG 2: CÁC LĨNH VỰC ỨNG DỤNG IOT")
    
    add_bullet(doc, "Phân loại ứng dụng IoT (Hình 2.1): Phân loại theo Nội dung (Multimedia - video/ảnh hoặc Scalar - dữ liệu cảm biến đo đạc) và Phân loại theo Chủ thể (Hệ thống hoặc Con người).", "Tổng quan: ")

    # 2.1
    add_heading2(doc, "2.1. Nhà thông minh (Smart Home)")
    add_bullet(doc, "Mục tiêu tạo ra không gian sống tiện nghi, tự động thích ứng với ngữ cảnh và nhu cầu sinh hoạt của gia chủ.", "Mục tiêu cốt lõi: ")
    add_bullet(doc, "4 PHÂN HỆ GIẢI PHÁP TÍCH HỢP TRONG SMART HOME:", "4 Phân hệ giải pháp: ")
    add_subbullet(doc, "Camera giám sát nhận diện khuôn mặt; Cảm biến gắn cửa ra vào, cửa sổ; Cảm biến phát hiện chuyển động; Cảm biến khí ga, cảm biến khói cảnh báo cháy sớm.", "1. Giám sát an ninh: ")
    add_subbullet(doc, "Bật/tắt đèn chiếu sáng, quạt, rèm cửa từ xa qua smartphone; Tự động bật đèn khi có người và ánh sáng yếu; Tự điều chỉnh điều hòa/hệ thống sưởi.", "2. Điều khiển thiết bị gia đình: ")
    add_subbullet(doc, "Đo lường mức tiêu thụ điện năng theo thời gian thực của từng thiết bị, tự động ngắt thiết bị không cần thiết nhằm tiết kiệm chi phí.", "3. Quản lý năng lượng: ")
    add_subbullet(doc, "Tủ lạnh thông minh nhận biết thực phẩm, kiểm soát hạn sử dụng, tự lên danh sách mua sắm; Máy pha cà phê tự động kích hoạt theo chuông báo thức.", "4. Quản lý thiết bị nhà bếp: ")

    # 2.2
    add_heading2(doc, "2.2. Thành phố thông minh (Smart City)")
    add_bullet(doc, "Tích hợp công nghệ ICT (AI, Điện toán đám mây phân tán, Mạng cảm biến) vào cơ sở hạ tầng đô thị để nâng cao chất lượng sống và phát triển bền vững. Dự báo 60% dân số sống tại đô thị vào 2025.", "Định nghĩa & Bối cảnh: ")
    add_bullet(doc, "3 Hướng tiếp cận phát triển Smart City:", "3 Hướng tiếp cận: ")
    add_subbullet(doc, "Xây dựng kiến trúc khung tổng thể trước, sau đó triển khai các dự án con.", "• Từ trên xuống (Top-down): ")
    add_subbullet(doc, "Triển khai từng dự án cụ thể độc lập trước rồi tích hợp dần thành hệ thống lớn (Ví dụ: Amsterdam).", "• Từ dưới lên (Bottom-up): ")
    add_subbullet(doc, "Kết hợp cả hai hướng: vừa định hình khung kiến trúc chung vừa xây dựng dự án thành phần và tích hợp đồng thời.", "• Lai ghép (Hybrid): ")

    # 2.2.1
    add_heading3(doc, "2.2.1. Kiến trúc tổng quát 4 lớp của Smart City (Cisco Press)")
    add_bullet(doc, "Bao gồm toàn bộ các thiết bị cảm biến và cơ cấu chấp hành thu thập dữ liệu đường phố (cảm biến gần phát hiện đỗ xe, cảm biến ánh sáng đèn đường, camera video giao thông, cảm biến đo ô nhiễm không khí PM2.5, AI đếm xe).", "1. Lớp Thiết bị Đường phố (Street Layer): ")
    add_bullet(doc, "Lớp mạng trung gian chuyển tiếp dữ liệu và điều khiển giữa Street Layer và Data Center. Chuyển tiếp đa giao thức, yêu cầu cao về khả năng chịu lỗi phục hồi, băng thông lớn và độ trễ thấp.", "2. Lớp Đô thị / Mạng chuyển tiếp (City Layer): ")
    add_bullet(doc, "Được xây dựng trên nền tảng Điện toán đám mây (Cloud Computing). Chịu trách nhiệm lưu trữ tập trung, xử lý dữ liệu lớn, chạy thuật toán AI phân tích và đưa ra quyết định điều phối (ví dụ: điều khiển đèn giao thông).", "3. Lớp Trung tâm Dữ liệu (Data Center Layer): ")
    add_bullet(doc, "Cung cấp giao diện dịch vụ đa dạng cho 3 nhóm đối tượng: Cơ quan quản lý điều hành, Người dân đô thị, và Doanh nghiệp. (Ví dụ Smart Parking: người dân tìm chỗ đỗ rẻ nhất, cơ quan quản lý điều tiết giao thông).", "4. Lớp Dịch vụ Người dùng (Service Layer): ")

    # 2.2.2 - 2.2.4
    add_heading3(doc, "2.2.2 - 2.2.4. Các lĩnh vực trọng điểm của Smart City")
    add_bullet(doc, "Tàu điện ngầm có Internet (Seoul, New York); Phương tiện xanh xe điện/xe đạp (Barcelona); Thẻ thông minh và thông tin thời gian thực; Giảm thiểu xe cá nhân tại Hà Nội & TP.HCM.", "Giao thông thông minh: ")
    add_bullet(doc, "Kiến trúc hệ thống dự báo bụi PM2.5: Cảm biến bụi PM2.5 thu thập dữ liệu -> truyền qua mạng không dây Zigbee về Gateway -> Gateway gửi qua TCP/IP lên Cloud -> Thuật toán AI phân tích dự báo -> Hiển thị trên Mobile/Web App.", "Môi trường thông minh: ")
    add_bullet(doc, "Nâng cao chất lượng y tế từ xa, giáo dục số hóa tùy biến, bảo đảm an ninh công cộng.", "Cuộc sống thông minh: ")

    # 2.2.5
    add_heading3(doc, "2.2.5. Các dự án Thành phố thông minh tiêu biểu trên thế giới")
    add_bullet(doc, "Tiếp cận từ dưới lên (Bottom-up). Bãi đỗ xe Mobypark; Điểm trao đổi Internet lớn thứ 2 thế giới; Phòng lab IoT 3700m2 dùng LoRaWAN cho đèn tín hiệu; Lưới điện thông minh GridFriends; Ga tàu Zonstation 1 năng lượng mặt trời; Làm mát nhà bằng nước sông IJ; Xe điện Car2Grid; Toogethr chia sẻ xe; Cư dân tự đo chất lượng nước/không khí.", "• Amsterdam (Hà Lan): ")
    add_bullet(doc, "Chiến lược CityOS. Giao thông thông minh ưu tiên xe buýt và luôn bật đèn xanh trên lộ trình xe cứu hỏa/cứu thương; Chuyển toàn bộ sang đèn LED; Cảm biến tiếng ồn phát hiện điểm vượt 100dB (ngưỡng an toàn WHO); Hệ thống thủy lợi thông minh giảm 25% lượng nước tưới; Kiến trúc Chính quyền thông minh liên thông các phòng ban.", "• Barcelona (Tây Ban Nha): ")
    add_bullet(doc, "Dự án Connecting Copenhagen đoạt giải The World's Best Smart City Project 2014. Mục tiêu trung hòa carbon vào 2025 và độc lập hoàn toàn nhiên liệu hóa thạch vào 2050.", "• Copenhagen (Đan Mạch): ")

    # 2.3
    add_heading2(doc, "2.3. Nông nghiệp thông minh (Smart Agriculture)")
    add_bullet(doc, "Nông nghiệp chính xác (Precision Agriculture) ứng dụng GIS, GPS, WSN, IoT, Cloud, AI để tăng năng suất và giảm tác động môi trường.", "Khái niệm cốt lõi: ")
    add_bullet(doc, "KIẾN TRÚC 4 LỚP NÔNG NGHIỆP THÔNG MINH (HÌNH 2.16):", "Kiến trúc 4 lớp: ")
    add_subbullet(doc, "Máy móc nông nghiệp, cây trồng, vật nuôi được gắn cảm biến đo độ ẩm đất, nhiệt độ, ánh sáng, dinh dưỡng NPK.", "1. Lớp Thiết bị (Device Layer / WSN): ")
    add_subbullet(doc, "Nút Gateway thu thập dữ liệu từ cảm biến qua Zigbee, Bluetooth, LoRa, WLAN.", "2. Lớp Cổng kết nối (Gateway / Edge): ")
    add_subbullet(doc, "Chuyển tiếp dữ liệu từ Gateway qua mạng di động Cellular hoặc TCP/IP lên Cloud để lưu trữ, phân tích và suy diễn ngữ cảnh.", "3. Lớp Đám mây (Cloud Computing Layer): ")
    add_subbullet(doc, "Người dùng theo dõi thông số ngữ cảnh trên Web/Mobile App và phát tín hiệu điều khiển ngược lại van tưới, máy bơm, hệ thống chiếu sáng (Vòng lặp điều khiển kín).", "4. Lớp Người dùng (User Layer / Service): ")

    # Bai tap C2
    add_callout(
        doc,
        "ĐÁP ÁN NHANH BÀI TẬP ÔN TẬP CHƯƠNG 2 (TRẢ LỜI NGAY TRONG PHÒNG THI)",
        "Câu 1: Ứng dụng IoT trên thế giới và ở VN? Trả lời: Thế giới có Smart City (Amsterdam, Barcelona), xe tự lái Tesla, y tế thông minh. VN có đề án đô thị thông minh tại HN, TP.HCM, Đà Nẵng, Cần Thơ, nông nghiệp thông minh tại ĐBSCL/Lâm Đồng.\n"
        "Câu 2: Các ứng dụng trong Smart City? Trả lời: Bãi đỗ xe thông minh (Mobypark), giao thông thông minh (ưu tiên xe cấp cứu), quan trắc môi trường (bụi PM2.5), chiếu sáng thông minh (đèn LED tự động), chính quyền liên thông.\n"
        "Câu 3: Các thành phần chính trong kiến trúc IoT? Trả lời: 4 Thành phần/lớp: Thiết bị (Sensors/Actuators) -> Cổng kết nối (Gateway) -> Đám mây/Xử lý dữ liệu (Cloud/Edge) -> Giao diện ứng dụng người dùng (Service/App).\n"
        "Câu 4: Thiết kế kiến trúc IoT nông nghiệp tại VN? Trả lời: Áp dụng kiến trúc 4 lớp Mục 2.3: Cảm biến độ ẩm đất/nhiệt độ -> Kết nối LoRa/Zigbee về Gateway -> Truyền 4G/Cellular lên Cloud phân tích -> Nông dân điều khiển máy bơm qua app điện thoại.\n"
        "Câu 5: Chức năng ứng dụng Smart Home? Trả lời: 4 phân hệ Mục 2.1: Giám sát an ninh, Điều khiển chiếu sáng/HVAC, Quản lý điện năng thời gian thực, Quản lý thiết bị nhà bếp.\n"
        "Câu 6: Giám sát giao thông tại VN? Trả lời: Camera giao thông + FCD (Floating Car Data từ GPS xe buýt/taxi) -> Truyền về trung tâm qua 4G/5G -> Phân tích AI đếm xe và phát hiện kẹt xe -> Điều khiển chu kỳ đèn giao thông theo thời gian thực.\n"
        "Câu 7: Giám sát chất lượng không khí tại TP.HCM? Trả lời: Các trạm cảm biến đo bụi PM2.5/PM10, khí CO/NO2 tại các ngã tư lớn -> Kết nối Zigbee/LoRa về Gateway -> Đẩy lên Cloud -> AI phân tích mô hình phát tán ô nhiễm -> Cảnh báo người dân qua app/bảng điện tử đường phố."
    )

print("Part 2 (C1 & C2) built successfully!")
