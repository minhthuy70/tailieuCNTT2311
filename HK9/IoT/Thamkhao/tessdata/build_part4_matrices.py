# -*- coding: utf-8 -*-
"""
Builder Part 4: Quick Comparison Matrices, Master Tables & Exam Tactics
"""
from word_helpers import (
    add_heading1, add_heading2, add_heading3, add_heading4,
    add_bullet, add_subbullet, add_callout, add_table
)

def build_part3_and_part4(doc):
    add_heading1(doc, "PHẦN III: CÁC BẢNG MA TRẬN SO SÁNH & TỔNG HỢP NHANH PHỤC VỤ THI ĐỀ MỞ")
    
    # Bảng 1: WiFi
    add_heading2(doc, "BẢNG 1: MA TRẬN SO SÁNH TOÀN DIỆN 6 CHUẨN CON WIFI (802.11 B, A, G, N, AC, AX)")
    wifi_headers = ["Chuẩn (Tên gọi)", "Năm", "Tần số", "Tốc độ tối đa", "Công nghệ cốt lõi", "Ưu điểm & Nhược điểm chính", "Tương thích"]
    wifi_data = [
        ["802.11b", "1999", "2.4 GHz", "11 Mbps", "DSSS, CCK", "Ưu: Giá rẻ, tầm phủ sóng tốt.\nNhược: Tốc độ thấp, dễ xuyên nhiễu lò vi sóng.", "Gốc"],
        ["802.11a", "1999", "5 GHz", "54 Mbps", "OFDM", "Ưu: Tốc độ cao, không nhiễu 2.4GHz.\nNhược: Giá đắt, tầm phủ hẹp, khó xuyên tường.", "Không tương thích 11b"],
        ["802.11g", "2003", "2.4 GHz", "54 Mbps", "OFDM", "Ưu: Tốc độ cao, tầm phủ rộng như 11b.\nNhược: Dễ bị nhiễu thiết bị cùng tần số 2.4GHz.", "Tương thích ngược 11b"],
        ["802.11n\n(WiFi 4)", "2009", "2.4 & 5 GHz", "100 - 600 Mbps", "MIMO (đa ăng-ten), kênh 40MHz", "Ưu: Tốc độ cao, tầm phủ mạnh, chống nhiễu tốt.\nNhược: Tín hiệu có thể gây nhiễu mạng 11b/g gần.", "Tương thích 11b/g"],
        ["802.11ac\n(WiFi 5)", "2013-2016", "5 GHz\n(kèm 2.4)", "Wave 1: 1.3Gbps\nWave 2: 3.5Gbps", "MU-MIMO, kênh 80/160MHz, 256-QAM", "Ưu: Băng thông cực lớn, ít nhiễu.\nNhược: Sóng 5GHz suy hao mạnh qua vật cản.", "Tương thích 11n/a"],
        ["802.11ax\n(WiFi 6)", "2020", "2.4 & 5 GHz", "Tăng 40% vật lý\n(x4 thông lượng)", "OFDMA, 2048 sóng mang con, 1024-QAM", "Ưu: Tối ưu mạng cực đông đúc, thông lượng x4.\nNhược: Mới ra đời, thiết bị hỗ trợ chưa phổ biến.", "Tương thích toàn bộ"]
    ]
    add_table(doc, wifi_headers, wifi_data, [1.0, 0.6, 0.8, 1.0, 1.2, 1.4, 0.67])

    # Bảng 2: Giao thức không dây
    add_heading2(doc, "BẢNG 2: MA TRẬN SO SÁNH CÁC BỘ GIAO THỨC MẠNG KHÔNG DÂY TRONG IOT")
    proto_headers = ["Giao thức", "Chuẩn nền tảng", "Băng tần", "Tốc độ dữ liệu", "Phạm vi", "Năng lượng", "Topo", "Ứng dụng tiêu biểu"]
    proto_data = [
        ["6LoWPAN", "RFC 6282\nIEEE 802.15.4", "2.4 GHz &\nSub-1 GHz", "20 - 250 kbps", "10 - 100 m", "Rất thấp\n(Pin nhiều năm)", "Mesh,\nStar", "Mạng cảm biến lớn kết nối trực tiếp IPv6 ra ngoài"],
        ["Zigbee", "Zigbee Alliance\nIEEE 802.15.4", "868/915 MHz\n2.4 GHz", "20 - 250 kbps\n(Thực tế 25kbps)", "10 - 75 m", "Cực kỳ thấp\n(1 cặp pin AA)", "Mesh, Tree,\nStar", "Tự động hóa tòa nhà, giám sát môi trường, Smart Home"],
        ["WiFi (WLAN)", "IEEE 802.11\na/b/g/n/ac/ax", "2.4 GHz &\n5 GHz", "11 Mbps đến\nhàng Gbps", "30 - 100 m", "Cao\n(Cần cấp nguồn)", "Star (BSS),\nAd-hoc (IBSS)", "Truyền video camera, Smart Home nguồn cắm trực tiếp"],
        ["Bluetooth\n/ BLE", "Bluetooth SIG\nIEEE 802.15.1", "2.4 GHz", "1 - 3 Mbps", "1 - 10 m", "Rất thấp\n(BLE)", "P2P, Star,\nMesh", "Thiết bị đeo cá nhân PAN, tai nghe, y tế cá nhân"],
        ["LoRaWAN", "LoRa Alliance\nProprietary RF", "Sub-1 GHz\n(433/868/915M)", "0.3 - 50 kbps", "2 - 15 km\n(Rất xa)", "Cực kỳ thấp\n(Pin 5-10 năm)", "Star-of-Stars", "Nông nghiệp thông minh diện rộng, Smart City tầm xa"]
    ]
    add_table(doc, proto_headers, proto_data, [0.8, 1.0, 0.9, 0.9, 0.7, 0.8, 0.7, 0.87])

    # Bảng 3: Topo mạng
    add_heading2(doc, "BẢNG 3: MA TRẬN SO SÁNH TOÀN DIỆN 10 KIẾN TRÚC & TOPO MẠNG IOT")
    topo_headers = ["Topo mạng", "Kiểu kết nối", "Cơ chế hoạt động", "Ưu điểm vượt trội", "Nhược điểm & Rủi ro", "Điểm lỗi duy nhất?"]
    topo_data = [
        ["Star\n(Hình sao)", "Point-to-Point về Hub", "Các nút client giao tiếp qua Hub/Sink trung tâm", "Dễ lắp đặt, dễ tìm lỗi, chi phí thấp", "Hub hỏng là toàn mạng sụp đổ; nghẽn tại Hub", "CÓ (Hub trung tâm)"],
        ["Full Mesh\n(Lưới đầy đủ)", "Point-to-Point riêng rẽ", "Mỗi nút kết nối trực tiếp đến tất cả các nút còn lại", "Độ chịu lỗi và phục hồi tối đa, bảo mật cao", "Cực kỳ tốn kém cáp/phần cứng, cấu hình phức tạp", "KHÔNG (Phục hồi tức thì)"],
        ["Partial Mesh\n(Lưới một phần)", "Hỗn hợp trực tiếp/gián tiếp", "Một số nút kết nối trực tiếp, nút khác qua trung gian", "Tiết kiệm chi phí hơn full mesh, chịu lỗi tốt", "Vẫn phức tạp trong định tuyến hơn sao và bus", "KHÔNG"],
        ["Bus\n(Hình bus)", "Point-to-Multipoint", "Dùng chung một đường cáp trục xương sống chính", "Dễ lắp đặt, cấu trúc đơn giản, chi phí rẻ", "Giới hạn chiều dài cáp, khó tìm vị trí đứt cáp", "CÓ (Đường cáp chính)"],
        ["Ring\n(Hình vòng)", "Point-to-Point qua repeater", "Vòng tròn khép kín, dữ liệu đi 1 chiều duy nhất", "Dễ lắp đặt, dễ định vị lỗi", "Hỏng một nút/repeater là sụp đổ toàn bộ mạng", "CÓ (Bất kỳ nút nào)"],
        ["Tree\n(Hình cây)", "Phân cấp (Gốc - Nhánh)", "Nút gốc kết nối các hub con, đa chặng multihop", "Phân tầng rõ ràng, mở rộng quy mô lớn tốt", "Mất cân bằng tải; đứt liên kết cha là cô lập nhánh", "CÓ (Nút cha / Nút gốc)"],
        ["Chain\n(Hình chuỗi)", "Nối tiếp thành chuỗi", "Mỗi nút nối tiếp nút kế tiếp (trừ nút đầu/cuối)", "Dễ thi công dọc tuyến đường, hành lang hẹp", "Hỏng một mắt xích làm gián đoạn toàn bộ phía sau", "CÓ (Mắt xích giữa)"],
        ["Grid\n(Lưới ô vuông)", "Chia ô không chồng lấn", "Mỗi ô chỉ 1 nút làm việc luân phiên, còn lại ngủ", "Kéo dài tối đa tuổi thọ pin mạng, tránh nghẽn", "Yêu cầu thuật toán điều phối luân phiên phức tạp", "KHÔNG"],
        ["Cluster-based\n(Dựa trên cụm)", "Thu thập về Đầu cụm (CH)", "Cảm biến gửi về CH, CH nén và gửi lên Gateway", "Giảm tải dữ liệu, tối ưu cho mạng cực lớn", "CH ở quá xa cảm biến sẽ tốn năng lượng truyền", "CÓ (Đầu cụm CH)"],
        ["Tributary-Delta\n(Phụ lưu - Đ.bằng)", "Lai ghép Cây & Đa đường", "Vùng nhánh dùng cây, vùng đồng bằng dùng đa luồng", "Tối ưu hóa: nhánh nhẹ, đồng bằng chịu lỗi cao", "Phải phân vùng mạng theo đặc tính lỗi", "KHÔNG"],
        ["Sweep\n(Làn sóng quét)", "Sóng quét động di chuyển", "Nhóm nút di chuyển qua mạng, dữ liệu đi qua 1 lần", "Cực kỳ bền vững, không cần duy trì cây cố định", "Độ trễ thu thập phụ thuộc vào chu kỳ quét", "KHÔNG"]
    ]
    add_table(doc, topo_headers, topo_data, [1.0, 0.9, 1.4, 1.2, 1.3, 0.87])

    # Bảng 4: 4 Địa chỉ MAC Frame 802.11
    add_heading2(doc, "BẢNG 4: TRA CỨU NHANH VAI TRÒ 4 ĐỊA CHỈ MAC TRONG FRAME WIFI 802.11")
    mac_headers = ["Chức năng truyền thông", "To DS", "From DS", "Address 1", "Address 2", "Address 3", "Address 4"]
    mac_data = [
        ["Independent BSS (Mạng Ad-hoc trực tiếp)", "0", "0", "RA = DA\n(Trạm nhận/đích)", "SA\n(Trạm gửi)", "BSSID\n(Định danh BSS)", "Không có"],
        ["Từ AP đến Station (Downlink từ trạm phát)", "0", "1", "RA = DA\n(Trạm nhận/đích)", "BSSID\n(Địa chỉ AP phát)", "SA\n(Trạm nguồn gửi)", "Không có"],
        ["Từ Station tới AP (Uplink lên trạm phát)", "1", "0", "RA = BSSID\n(Địa chỉ AP nhận)", "SA\n(Trạm gửi)", "DA\n(Trạm đích đến)", "Không có"],
        ["Wireless DS (Cầu nối WDS giữa 2 AP)", "1", "1", "RA\n(AP nhận sóng)", "TA\n(AP truyền sóng)", "DA\n(Trạm đích cuối)", "SA\n(Trạm nguồn đầu)"]
    ]
    add_table(doc, mac_headers, mac_data, [1.6, 0.6, 0.6, 1.0, 1.0, 1.0, 0.87])

    # Bảng 5: Cảm biến & Actuators
    add_heading2(doc, "BẢNG 5: TỔNG HỢP 10 LOẠI CẢM BIẾN & 3 LOẠI CƠ CẤU CHẤP HÀNH")
    sa_headers = ["Tên phần tử", "Phân loại", "Đại lượng đo / Chức năng", "Ứng dụng thực tế điển hình"]
    sa_data = [
        ["Cảm biến Nhiệt độ", "Sensor", "Nhiệt độ môi trường/vật thể", "Giám sát bệnh nhân, điều hòa thông minh, bảo quản thực phẩm"],
        ["Cảm biến Áp suất", "Sensor", "Áp suất khí nén, chất lỏng, độ cao", "Máy bơm, tủ lạnh, hệ thống thủy lực, dự báo thời tiết"],
        ["Cảm biến Lưu lượng", "Sensor", "Tốc độ dòng chảy chất lỏng/khí", "Đo nước sinh hoạt, theo dõi axit tinh khiết, truyền nhiệt"],
        ["Cảm biến Mức", "Sensor", "Mức chất lỏng liên tục hoặc theo điểm", "Bồn chứa nước thông minh, giếng khoan dầu khí"],
        ["Cảm biến Hình ảnh", "Sensor", "Thu nhận và chuyển đổi sóng quang học", "Camera giao thông thông minh, thiết bị y tế, camera nhìn đêm"],
        ["Cảm biến Tiếng ồn", "Sensor", "Cường độ âm thanh (Decibel - dB)", "Đo ô nhiễm tiếng ồn đô thị (WHO), an toàn nhà xưởng"],
        ["Cảm biến Bụi / Ô nhiễm", "Sensor", "Nồng độ bụi PM2.5, PM10, khí độc CO/NO2", "Trạm quan trắc không khí thành phố (EPA), máy lọc không khí"],
        ["Cảm biến Hồng ngoại", "Sensor", "Bức xạ nhiệt hồng ngoại chuyển động", "Chống trộm, tự động bật đèn khi có người, theo dõi mục tiêu"],
        ["Cảm biến Độ ẩm", "Sensor", "Độ ẩm không khí/đất (điện dung)", "Nhà kính nông nghiệp thông minh, máy hút ẩm, kho nông sản"],
        ["Cảm biến Tốc độ", "Sensor", "Vận tốc di chuyển của phương tiện", "Hệ thống phanh ABS, radar Doppler, giám sát tốc độ xe"],
        ["Actuator Tuyến tính cơ khí", "Actuator", "Chuyển động quay sang chuyển động thẳng", "Trục vít nâng hạ cửa, van đóng mở cơ học, robot công nghiệp"],
        ["Actuator Thủy lực", "Actuator", "Tác động lực lớn dựa trên Định luật Pascal", "Van điều khiển công nghiệp nặng, hệ thống phanh xe tải"],
        ["Actuator Khí nén", "Actuator", "Tác động lực nhanh bằng khí nén", "Tay gắp robot đóng gói, van đóng ngắt khẩn cấp an toàn"]
    ]
    add_table(doc, sa_headers, sa_data, [1.5, 0.8, 1.8, 2.57])

    # Bảng 6: Ma trận giải bài tập ôn tập
    add_heading2(doc, "BẢNG 6: MA TRẬN ĐỐI CHIẾU 19 CÂU HỎI BÀI TẬP ÔN TẬP VỚI VỊ TRÍ LÝ THUYẾT")
    ex_headers = ["Chương", "Câu hỏi bài tập", "Mục lý thuyết", "Dàn ý / Từ khóa trả lời"]
    ex_data = [
        ["C1", "1. Liệt kê thiết bị kết nối Internet?", "1.1.3", "Things: thiết bị gia dụng, xe cộ, thiết bị đeo, cảm biến, camera."],
        ["C1", "2. Đặc điểm kỹ thuật thiết bị IoT?", "1.1.2, 1.1.4", "Nhỏ gọn, chi phí thấp, nguồn pin lâu năm, có IP duy nhất, tích hợp cảm biến."],
        ["C1", "3. Xu thế IoT trên TG và ở VN?", "1.1.9, 1.5", "TG: Hội tụ OT/IT, Edge computing, 5G/AI. VN: Smart City, Smart Agri."],
        ["C1", "4. Ưu điểm IoT cho cuộc sống?", "1.1.5, 1.1.13", "Tự động hóa, nâng cao an toàn y tế, giao thông thông minh, bảo vệ môi trường."],
        ["C1", "5. Thách thức IoT đang gặp phải?", "1.1.7, 1.4", "4 lỗ hổng bảo mật, chuẩn hóa tránh phân mảnh, tối ưu năng lượng CPS."],
        ["C2", "1. Ứng dụng IoT trên TG và VN?", "2.1, 2.2, 2.3", "Smart City (Amsterdam, Barcelona), Smart Home, Nông nghiệp công nghệ cao."],
        ["C2", "2. Ứng dụng trong Smart City?", "2.2.1, 2.2.5", "Đỗ xe Mobypark, ưu tiên xe cấp cứu, đo tiếng ồn/PM2.5, thủy lợi thông minh."],
        ["C2", "3. Thành phần chính kiến trúc IoT?", "2.2.1, 2.3", "4 lớp: Thiết bị (Device) -> Gateway -> Đám mây (Cloud) -> Dịch vụ (App)."],
        ["C2", "4. Thiết kế IoT nông nghiệp VN?", "2.3", "Cảm biến đất -> Gateway LoRa/Zigbee -> Cloud phân tích -> App điều khiển bơm."],
        ["C2", "5. Chức năng ứng dụng Smart Home?", "2.1", "4 phân hệ: An ninh, Điều khiển thiết bị gia đình, Quản lý năng lượng, Nhà bếp."],
        ["C2", "6. Giám sát giao thông tại VN?", "2.2.2, 1.1.14", "Camera + GPS FCD từ xe buýt/taxi -> 4G/5G -> AI đếm xe -> Điều khiển đèn."],
        ["C2", "7. Giám sát không khí tại TP.HCM?", "2.2.3, 3.9", "Trạm cảm biến PM2.5/khí độc -> Zigbee/LoRa -> Cloud AI -> Cảnh báo dân."],
        ["C3", "1. Ưu nhược điểm các topo mạng?", "3.7, Bảng 3", "Star, Mesh, Tree, Ring, Chain, Grid, Cluster, Tributary-Delta, Sweep."],
        ["C3", "2. So sánh giao thức không dây?", "3.8, Bảng 2", "So sánh 6LoWPAN, Zigbee, WiFi, Bluetooth, LoRa (băng thông, pin, tầm xa)."],
        ["C3", "3. Dùng Zigbee giám sát không khí?", "3.8.2, 2.2.3", "ZED (cảm biến PM2.5) -> ZR (trạm lặp) -> ZC (Gateway) -> TCP/IP -> Cloud."],
        ["C3", "4. Dùng WLAN 802.11 làm Smart Home?", "3.8.3, 2.1", "Mạng hạ tầng BSS: WiFi Router (AP), các bóng đèn/công tắc ESP32 là STA."],
        ["C3", "5. Thiết kế mạng Nông nghiệp VN?", "2.3, 3.8", "Chọn LoRa hoặc Zigbee vì diện tích rộng, tiết kiệm pin nhiều năm, chi phí rẻ."],
        ["C3", "6. Mạng giám sát không khí HCM?", "2.2.3, 3.8", "Chọn LoRaWAN (xuyên vật cản xa) hoặc Cellular 4G/5G tại các nút lớn."],
        ["C3", "7. Giám sát giao thông bằng 5G?", "1.1.14, 1.5", "Băng thông siêu cao eMBB + độ trễ cực thấp URLLC (<1ms) truyền video 4K."]
    ]
    add_table(doc, ex_headers, ex_data, [0.6, 2.1, 1.0, 2.97])

    # Phần 4: Chiến thuật thi đề mở
    add_heading1(doc, "PHẦN IV: CẨM NANG CHIẾN THUẬT & MẸO LÀM BÀI THI ĐỀ MỞ IOT")
    
    add_callout(
        doc,
        "QUY TẮC VÀNG TRÌNH BÀY CÂU HỎI THIẾT KẾ HỆ THỐNG IOT (LUÔN ĐẠT ĐIỂM TỐI ĐA)",
        "Dù đề thi yêu cầu thiết kế bất kỳ hệ thống nào (Nhà thông minh, Giám sát không khí, Nông nghiệp, Giao thông...), bạn LUÔN LUÔN TRÌNH BÀY ĐỦ 4 LỚP KIẾN TRÚC THEO THỨ TỰ SAU:\n\n"
        "1. LỚP 1: THIẾT BỊ / THU THẬP DỮ LIỆU (SENSING & ACTUATION LAYER)\n"
        "   - Liệt kê cụ thể loại cảm biến sử dụng (Ví dụ: DHT22 đo nhiệt độ/độ ẩm, cảm biến bụi PM2.5 PMS5003, camera OV2640).\n"
        "   - Liệt kê vi điều khiển / thiết bị đầu cuối: ESP32, Arduino, TI CC2530 (Zigbee End Device).\n"
        "   - Liệt kê cơ cấu chấp hành: Relay kích hoạt máy bơm tưới, van điện từ, còi báo động.\n\n"
        "2. LỚP 2: MẠNG & CỔNG KẾT NỐI (NETWORK & GATEWAY LAYER)\n"
        "   - Kết nối nội bộ trường cảm biến: Dùng Zigbee (nếu cự ly 10-50m, nhiều nút) hoặc LoRaWAN (nếu cự ly vài km).\n"
        "   - Thiết bị cổng (IoT Gateway): Tiếp nhận dữ liệu không dây nội bộ và chuyển đổi giao thức.\n"
        "   - Hướng truyền lên Internet: Sử dụng kết nối WiFi (trong nhà) hoặc 4G/5G/Cellular (ngoài trời) qua giao thức TCP/IP.\n\n"
        "3. LỚP 3: LƯU TRỮ & XỬ LÝ ĐÁM MÂY (CLOUD / EDGE COMPUTING LAYER)\n"
        "   - Giao thức tầng ứng dụng: Dùng MQTT (Publish/Subscribe nhẹ) hoặc HTTP RESTful, CoAP.\n"
        "   - Lưu trữ: Cơ sở dữ liệu thời gian thực (Firebase, InfluxDB, MySQL) trên Cloud.\n"
        "   - Xử lý thông minh: Thuật toán AI / Machine Learning phân tích dữ liệu, nhận diện bất thường, dự báo xu thế.\n\n"
        "4. LỚP 4: DỊCH VỤ & ỨNG DỤNG NGƯỜI DÙNG (APPLICATION & USER LAYER)\n"
        "   - Giao diện người dùng: Mobile App (Flutter/Android) hoặc Web Dashboard (React/NodeJS).\n"
        "   - Chức năng: Hiển thị biểu đồ thông số thời gian thực, gửi cảnh báo tức thì (Push notification, SMS), và NÚT ĐIỀU KHIỂN TỪ XA PHÁT LỆNH NGƯỢC VỀ THIẾT BỊ (Vòng lặp điều khiển kín).",
        bg="F0FDF4", border_color="16A34A"
    )

    add_callout(
        doc,
        "MẸO TRẢ LỜI CÂU HỎI SO SÁNH (GIAO THỨC / TOPO / CHUẨN MẠNG)",
        "Khi gặp câu hỏi so sánh (ví dụ: So sánh Zigbee vs WiFi; So sánh Topo Star vs Mesh; So sánh 802.11a vs 802.11b):\n"
        "• TUYỆT ĐỐI KHÔNG VIẾT ĐOẠN VĂN DÀI DÒNG! Hãy lập ngay một BẢNG SO SÁNH gồm 5 tiêu chí chuẩn mực:\n"
        "  1. Tần số hoạt động & Băng thông (Tốc độ dữ liệu).\n"
        "  2. Mức tiêu thụ năng lượng (Tuổi thọ pin).\n"
        "  3. Phạm vi phủ sóng (Khoảng cách truyền).\n"
        "  4. Chi phí đầu tư & Độ phức tạp cấu hình.\n"
        "  5. Độ tin cậy & Khả năng chịu lỗi (Có điểm lỗi duy nhất hay không).\n"
        "• Sau bảng so sánh, chốt lại 1 câu kết luận về 'Trường hợp ứng dụng tối ưu' cho từng đối tượng.",
        bg="EFF6FF", border_color="2563EB"
    )

print("Part 4 (Matrices & Tactics) built successfully!")
