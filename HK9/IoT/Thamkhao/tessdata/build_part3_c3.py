# -*- coding: utf-8 -*-
"""
Builder Part 3: Detailed TOC & Comprehensive Summaries for Chapter 3
"""
from word_helpers import (
    add_heading1, add_heading2, add_heading3, add_heading4,
    add_bullet, add_subbullet, add_callout, add_table
)

def build_part2_chapter3(doc):
    add_heading1(doc, "CHƯƠNG 3: CÁC KIẾN TRÚC MẠNG VÀ BỘ GIAO THỨC MẠNG IOT")
    
    # 3.1 & 3.2
    add_heading2(doc, "3.1 & 3.2. Mô hình OSI và Bộ giao thức TCP/IP")
    add_bullet(doc, "Do ISO giới thiệu năm 1984, chuẩn hóa chức năng truyền thông không phụ thuộc phần cứng bên dưới. Áp dụng nguyên lý 'Chia để trị' (Divide and Conquer) thành 7 tầng giúp đơn giản hóa việc phát triển và học tập.", "3.1. Mô hình OSI: ")
    add_bullet(doc, "Gồm 4 tầng (bỏ tầng Presentation và Session gộp vào Application):", "3.2. Mô hình TCP/IP: ")
    add_subbullet(doc, "Định nghĩa các giao thức ứng dụng mạng và cách chương trình người dùng giao tiếp với dịch vụ tầng dưới.", "• Lớp 4 - Application Layer (Ứng dụng): ")
    add_subbullet(doc, "Cho phép hai máy chủ truyền thông tin cậy hoặc phi kết nối. Hai giao thức cốt lõi: TCP (hướng kết nối, tin cậy) và UDP (phi kết nối, tốc độ nhanh, ít overhead).", "• Lớp 3 - Transport Layer (Truyền tải): ")
    add_subbullet(doc, "Đóng gói dữ liệu thành các IP Datagram mang địa chỉ IP nguồn và đích để định tuyến qua các mạng.", "• Lớp 2 - Internet Layer (Mạng Internet): ")
    add_subbullet(doc, "Kết hợp tầng Liên kết dữ liệu (Data Link) và tầng Vật lý (PHY) của OSI; định nghĩa các giao thức truy cập như Ethernet, Wi-Fi và phương thức truyền bit qua cáp đồng, cáp quang, sóng vô tuyến.", "• Lớp 1 - Network Access Layer (Truy cập mạng): ")
    
    add_bullet(doc, "4 Thành phần phần cứng cốt lõi của Router:", "Phần cứng Router: ")
    add_subbullet(doc, "RAM không bay hơi, lưu trữ tệp cấu hình khởi động (startup-config), không bị mất dữ liệu khi mất nguồn điện.", "1. NVRAM: ")
    add_subbullet(doc, "Cổng quản trị trực tiếp không cần mạng thông qua cáp RJ-45 hoặc miniUSB.", "2. Console Port: ")
    add_subbullet(doc, "Bộ nhớ bán dẫn lưu trữ hệ điều hành Cisco IOS, có thể xóa và ghi lại bằng điện, không mất dữ liệu khi tắt nguồn.", "3. Flash Memory: ")
    add_subbullet(doc, "Bộ nhớ truy cập ngẫu nhiên động (bay hơi), lưu trữ bảng định tuyến (routing table), bộ đệm ARP cache, bảng khung và hàng đợi gói tin.", "4. DRAM: ")

    # 3.3
    add_heading2(doc, "3.3. Các đặc điểm hiệu năng chính của Cấp độ Mạng IoT")
    add_bullet(doc, "Cấp độ mạng IoT thực chất là các lớp TCP/IP nhưng đã lược bỏ tầng Application để tránh trùng lặp với Cấp độ Ứng dụng IoT (IoT Application Level).", "Lưu ý cấu trúc: ")
    add_bullet(doc, "7 Đặc tính hiệu năng: 1) Data Rate (Tốc độ dữ liệu); 2) Latency (Độ trễ); 3) Jitter (Biến động độ trễ); 4) Reliability (Độ tin cậy); 5) Scalability (Khả năng mở rộng); 6) Security (Bảo mật); 7) Energy Efficiency (Hiệu quả năng lượng).", "7 Đặc tính cốt lõi: ")
    add_bullet(doc, "3 Chỉ số đo lường hiệu năng quan trọng nhất:", "3 Chỉ số quan trọng: ")
    
    add_heading4(doc, "1. Độ trễ đầu cuối (End-to-End Delay - dTotal)")
    add_bullet(doc, "Công thức xác định độ trễ tổng cộng giữa hai điểm cuối:", "Công thức tổng quát: ")
    add_callout(
        doc,
        "CÔNG THỨC TÍNH ĐỘ TRỄ ĐẦU CUỐI (END-TO-END DELAY)",
        "dTotal = dProcess + dQueue + dTrans + dProp\n\n"
        "Trong đó 4 thành phần trễ bao gồm:\n"
        "1. dProcess (Processing delay - Độ trễ xử lý tại nút): Thời gian router kiểm tra tiêu đề gói tin (header), kiểm tra lỗi bit và tìm đường chuyển tiếp (khoảng micro giây - µs).\n"
        "2. dQueue (Queuing delay - Độ trễ hàng đợi): Thời gian gói tin chờ trong hàng đợi của router trước khi được phát. Phụ thuộc số lượng gói đến trước và mức độ nghẽn (từ µs đến ms).\n"
        "3. dTrans (Transmission delay - Độ trễ truyền): Thời gian đẩy toàn bộ bit của gói tin vào đường truyền liên kết. Công thức: dTrans = L / R (L là độ dài gói tin tính bằng bit, R là tốc độ đường truyền bit/s - bps). Phụ thuộc trực tiếp vào độ dài gói tin.\n"
        "4. dProp (Propagation delay - Độ trễ lan truyền): Thời gian bit vật lý di chuyển từ đầu liên kết tới cuối liên kết. Công thức: dProp = Khoảng cách liên kết / Vận tốc lan truyền sóng (vận tốc ánh sáng). ĐẶC BIỆT: dProp HOÀN TOÀN ĐỘC LẬP VỚI ĐỘ DÀI GÓI TIN!\n\n"
        "📌 Công cụ đo lường độ trễ: Tiện ích Traceroute và công cụ chuyên dụng Cisco IP SLA.",
        bg="EFF6FF", border_color="1D4ED8"
    )

    add_heading4(doc, "2. Mất gói tin (Packet Loss)")
    add_bullet(doc, "Tỷ lệ phần trăm các gói tin bị mất trên đường truyền (0 - 100%).", "Định nghĩa: ")
    add_bullet(doc, "Do nghẽn mạng (Network Congestion). Cả hàng đợi và liên kết của router đều có dung lượng hữu hạn; khi một phần tử hoạt động hết công suất không thể xử lý kịp, các gói tin đến sau buộc phải bị loại bỏ (drop). Ngoài ra còn do lỗi phần cứng hoặc nhiễu vô tuyến.", "Nguyên nhân cốt lõi: ")

    add_heading4(doc, "3. Thông lượng (Throughput)")
    add_bullet(doc, "Lượng dữ liệu tối đa truyền thành công giữa hai điểm cuối trong một đơn vị thời gian (đơn vị: bps, kbps, Mbps, Gbps). Phân biệt giữa Thông lượng (thực tế nhận thành công), Tốc độ liên kết (Link speed lý thuyết) và Thời gian phản hồi (Response time).", "Định nghĩa & Đo lường: ")

    # 3.4
    add_heading2(doc, "3.4. Bộ giao thức Internet & Định địa chỉ IP")
    add_bullet(doc, "Do Robert Kahn và Vint Cerf phát triển từ những năm 1970 kết nối 'mạng của các mạng'. Địa chỉ IP do Trung tâm Thông tin Mạng (NIC) cấp phát duy nhất toàn cầu.", "Lịch sử & Nguyên lý: ")
    add_bullet(doc, "Độ dài 32-bit (4 octet, mỗi octet 8-bit, cách nhau bởi dấu chấm thập phân, ví dụ 192.168.10.8). Gồm 2 phần: Network Address (Địa chỉ mạng) và Host Address (Địa chỉ máy chủ), phân tách bằng Subnet Mask.", "• IPv4 (IP Version 4): ")
    
    add_bullet(doc, "5 Lớp địa chỉ IPv4 (Class A, B, C, D, E):", "Phân lớp IPv4: ")
    add_subbullet(doc, "Bit đầu là 0. Dải 1.x.x.x đến 126.x.x.x. Subnet mask mặc định 255.0.0.0 (8-bit mạng, 24-bit host). Cho phép 126 mạng và 16.777.214 máy chủ mỗi mạng. (Dải 127.x.x.x dành riêng cho Loopback nội bộ).", "– Lớp A: ")
    add_subbullet(doc, "Hai bit đầu là 10. Dải 128.0.x.x đến 191.255.x.x. Subnet mask 255.255.0.0 (16-bit mạng, 16-bit host). Có 16.384 mạng và 65.534 máy chủ mỗi mạng.", "– Lớp B: ")
    add_subbullet(doc, "Ba bit đầu là 110. Dải 192.0.0.x đến 223.255.255.x. Subnet mask 255.255.255.0 (24-bit mạng, 8-bit host). Có 2.097.152 mạng và 254 máy chủ mỗi mạng.", "– Lớp C: ")
    add_subbullet(doc, "Bốn bit đầu là 1110. Dải 224.0.0.0 đến 239.255.255.255. Dành riêng cho truyền đa hướng (Multicasting), không có phần host riêng lẻ.", "– Lớp D: ")
    add_subbullet(doc, "Dải 240.0.0.0 đến 255.255.255.255. Dành riêng cho mục đích nghiên cứu và thử nghiệm.", "– Lớp E: ")
    
    add_bullet(doc, "Độ dài 128-bit, chia thành 8 khối 16-bit biểu diễn dưới dạng thập lục phân cách nhau bởi dấu hai chấm (Colon-Hexadecimal). Cung cấp không gian địa chỉ khổng lồ giải quyết triệt để sự cạn kiệt 4.3 tỷ địa chỉ của IPv4 cho hàng chục tỷ thiết bị IoT.", "• IPv6 (IP Version 6): ")

    # 3.5 & 3.6
    add_heading2(doc, "3.5 & 3.6. Các loại mạng, Topo cơ bản & Phạm vi địa lý")
    add_bullet(doc, "1) Point-to-point (Điểm - điểm: kết nối trực tiếp riêng biệt giữa 2 nút, toàn bộ kênh truyền dành riêng, ví dụ remote máy lạnh); 2) Point-to-multipoint (Điểm - nhiều điểm: nhiều nút dùng chung liên kết, chia sẻ không gian hoặc thời gian).", "2 Kiểu kết nối: ")
    add_bullet(doc, "4 Topo vật lý cơ bản: Star (dễ lắp/sửa nhưng dính điểm lỗi duy nhất); Mesh (liên kết riêng giữa mọi cặp nút, chịu lỗi và bảo mật cao nhưng đắt và phức tạp); Bus (đường trục chính, dễ lắp nhưng giới hạn chiều dài và khó tìm lỗi); Ring (vòng tròn 1 chiều qua repeater, hỏng 1 nút đứt toàn mạng).", "4 Topo cơ bản: ")
    add_bullet(doc, "Phân loại theo phạm vi địa lý (Network Reachability):", "Phạm vi địa lý: ")
    add_subbullet(doc, "Vài cm đến vài mét. Dùng công nghệ công suất thấp như Bluetooth, BLE (tai nghe, chuột, đồng hồ thông minh).", "• PAN (Personal Area Network): ")
    add_subbullet(doc, "Trong phạm vi tòa nhà, cơ quan, khuôn viên trường. Tốc độ 100 - 1000 Mbps, độ chịu lỗi rất cao, thiết bị: switch, router, server.", "• LAN (Local Area Network): ")
    add_subbullet(doc, "Phạm vi thành phố hoặc đô thị. Do ISP cung cấp, chi phí cao, độ chịu lỗi trung bình, thiết bị: modem, cáp quang đô thị.", "• MAN (Metropolitan Area Network): ")
    add_subbullet(doc, "Phạm vi quốc gia, liên lục địa hoặc toàn cầu. Dùng đường dây PSTN hoặc vệ tinh, tốc độ thấp hơn LAN, chi phí bảo trì đắt, độ nhiễu và độ trễ cao.", "• WAN (Wide Area Network): ")

    # 3.7
    add_heading2(doc, "3.7. Các kiến trúc và Topo mạng dùng trong IoT")
    
    add_heading3(doc, "3.7.1. Một số kiến trúc mạng đơn giản")
    add_bullet(doc, "Gói tin có nhiều đường đi đến đích. Full Mesh: tất cả các nút kết nối trực tiếp với nhau. Partial Mesh: một số nút kết nối gián tiếp qua nút khác. Ưu điểm phục hồi lỗi cực cao.", "1. Kiến trúc mắt lưới (Mesh): ")
    add_bullet(doc, "Mạng phân cấp có một nút gốc (Root node) kiêm bộ thu nhận trung tâm (Sink). Các nhánh tạo thành mạng hình sao, kết hợp truyền single-hop hoặc multi-hop. Nhược điểm: khó cân bằng tải và nếu một liên kết trên nhánh hỏng thì toàn bộ nhánh con bị cô lập.", "2. Kiến trúc cây (Tree): ")
    add_bullet(doc, "Mỗi nút có đúng hai hàng xóm. Tin nhắn di chuyển theo một chiều duy nhất (chiều kim đồng hồ hoặc ngược lại). Nhược điểm: hỏng một nút là làm sụp đổ toàn bộ mạng.", "3. Kiến trúc vòng (Ring): ")
    add_bullet(doc, "Các nút nối tiếp thành hàng dài. Ngoài nút đầu và cuối, mỗi nút có 2 hàng xóm. Hỏng một mắt xích là gián đoạn truyền thông phía sau.", "4. Kiến trúc chuỗi (Chain): ")
    add_bullet(doc, "Các nút client kết nối về một Hub/Sink trung tâm đóng vai trò server. Nhược điểm: chỉ có duy nhất một đường giao tiếp, nếu Hub hỏng là mạng ngừng hoạt động (Single point of failure).", "5. Kiến trúc hình sao (Star): ")
    add_bullet(doc, "Trường cảm biến được chia thành các ô lưới vuông không chồng lấn. Mỗi ô vuông CHỈ CÓ DUY NHẤT 1 NÚT LÀM VIỆC TẠI MỘT THỜI ĐIỂM, các nút khác ngủ để luân phiên hoạt động kéo dài tuổi thọ mạng. Định tuyến đa đường giữa các ô lưới giúp tránh nghẽn hiệu quả.", "6. Kiến trúc lưới ô vuông (Grid): ")

    add_heading3(doc, "3.7.2. Một số kiến trúc mạng phức tạp (Hiện đại)")
    add_bullet(doc, "Các cảm biến thu thập dữ liệu và gửi về một Đầu cụm (Cluster Head - CH). CH tổng hợp, nén dữ liệu và gửi lên gateway. Rất hiệu quả cho mạng lớn, khoảng cách xa, đa chặng (multihop), giúp giảm tải lưu lượng so với mesh. Nhược điểm: nếu CH ở quá xa cảm biến sẽ tốn năng lượng.", "1. Kiến trúc theo cụm (Cluster-based): ")
    add_bullet(doc, "Hình thành từ ý tưởng dòng chảy sông ngòi. Kết hợp ưu thế của cây (tree) và định tuyến đa luồng (multi-path): Vùng nhánh (Tributary) có độ lỗi thấp dùng kiến trúc cây cho gói tin nhỏ; Vùng đồng bằng (Delta) có độ lỗi cao dùng định tuyến đa đường để đảm bảo dữ liệu gửi thành công.", "2. Kiến trúc Phụ lưu - Đồng bằng (Tributary - Delta): ")
    add_bullet(doc, "Thu thập dữ liệu theo làn sóng: dữ liệu đi qua mỗi thiết bị đúng 1 lần. Một nhóm nhỏ nút hoạt động di chuyển qua mạng, phát lời mời nút mới và loại bỏ nút cũ. Tính bền vững cực cao: không cần duy trì cây cố định, cực kỳ thích ứng với liên kết biến động và nút mạng thường xuyên bị hỏng.", "3. Kiến trúc Làn sóng (Sweep): ")

    # 3.8
    add_heading2(doc, "3.8. Các bộ giao thức mạng không dây thường dùng trong IoT")
    add_bullet(doc, "2 Cơ chế đưa dữ liệu ra Internet: (i) Thiết bị có địa chỉ IPv6 riêng kết nối trực tiếp ra ngoài (tiêu biểu: 6LoWPAN); (ii) Thiết bị giao tiếp nội bộ rồi đẩy ra ngoài qua IoT Gateway/Base Station (tiêu biểu: Zigbee). Ngoài ra mạng WLAN WiFi (ESP8266, ESP32) phổ biến cho người mới bắt đầu.", "3.8.0. Tổng quan 2 hướng tiếp cận: ")

    # 3.8.1
    add_heading3(doc, "3.8.1. Bộ giao thức 6LoWPAN")
    add_bullet(doc, "IPv6 over Low-Power Wireless Personal Area Networks (RFC 6282 IETF). Cho phép truyền gói tin IPv6 qua mạng công suất thấp IEEE 802.15.4 trong băng tần 2.4GHz và Sub-1GHz.", "Khái niệm cốt lõi: ")
    add_bullet(doc, "Hoạt động như một mạng nhánh cụt (stub network). Gồm 2 loại thiết bị: Host (thiết bị cuối, có chế độ ngủ định kỳ tiết kiệm pin) và Router (định tuyến chuyển tiếp). Mạng kết nối với IPv6 bên ngoài qua Edge Router (quản lý 3 việc: trao đổi ra ngoài, trao đổi nội bộ, và duy trì radio subnet).", "Kiến trúc mạng Mesh 6LoWPAN: ")
    add_bullet(doc, "Mô hình phân lớp các tầng trong 6LoWPAN:", "Phân lớp giao thức: ")
    add_subbullet(doc, "Chuẩn IEEE 802.15.4. Bản 802.15.4e bổ sung cơ chế TSCH (nhảy kênh theo khe thời gian) và CSL (lắng nghe mẫu phối hợp) tiết kiệm pin; Bản 802.15.4g mở rộng dải tần Sub-1 GHz.", "• Tầng PHY: ")
    add_subbullet(doc, "IEEE 802.15.4 MAC, điều khiển truy cập môi trường bằng cơ chế CSMA-CA (đa truy cập cảm nhận sóng mang tránh xung đột). Cung cấp lớp tương thích thích ứng từ IPv6 sang 802.15.4.", "• Tầng Data Link (MAC): ")
    add_subbullet(doc, "Đánh địa chỉ và định tuyến bằng chuẩn IPv6 toàn cầu.", "• Tầng Network: ")
    add_subbullet(doc, "UDP hoặc TCP tương tự mô hình chuẩn.", "• Tầng Transport: ")
    add_subbullet(doc, "Hai giao thức chuyên dụng nhẹ: CoAP (Constrained Application Protocol - chạy trên UDP, dạng RESTful) và MQTT (Message Queuing Telemetry Transport - cơ chế Publish/Subscribe chạy trên TCP do IBM phát minh).", "• Tầng Application: ")
    
    add_callout(
        doc,
        "CẤU TRÚC GÓI TIN 6LOWPAN & 3 NGỮ CẢNH NÉN HEADER (HAY RA THI NHẤT)",
        "Gói tin IPv6 chuẩn có Header rất lớn (40 bytes), không phù hợp với MTU nhỏ của 802.15.4 (127 bytes). Do đó 6LoWPAN đưa ra cơ chế nén Header theo 3 ngữ cảnh:\n"
        "1. Ngữ cảnh 1 (Nội bộ): Truyền giữa 2 thiết bị bên trong mạng 6LoWPAN dùng địa chỉ link-local -> IPv6 Header nén lại CHỈ CÒN 2 BYTES!\n"
        "2. Ngữ cảnh 2 (Ra mạng ngoài biết prefix): Truyền ra thiết bị mạng ngoài và tiền tố (prefix) của mạng đó ĐƯỢC BIẾT TRƯỚC -> IPv6 Header nén còn 12 BYTES.\n"
        "3. Ngữ cảnh 3 (Ra mạng ngoài không biết prefix): Truyền ra ngoài mà KHÔNG BIẾT TRƯỚC tiền tố -> IPv6 Header cần 20 BYTES.\n\n"
        "📌 Chồng phần đầu (Stacked Headers): IPv6 Payload + IPv6 Header Compression + Fragment Header (phân mảnh) + Mesh Addressing Header + IEEE 802.15.4 Header.",
        bg="F0FDF4", border_color="16A34A"
    )
    add_bullet(doc, "Phần cứng: CC2650 SimpleLink, CC1310 (TI), ZWIR4532. Phần mềm: Contiki OS, Mbed OS.", "Nền tảng hiện thực 6LoWPAN: ")

    # 3.8.2
    add_heading3(doc, "3.8.2. Bộ giao thức Zigbee")
    add_bullet(doc, "Mạng Zigbee gồm 3 nhóm thiết bị logic theo chức năng:", "Kiến trúc mạng Zigbee: ")
    add_subbullet(doc, "Mỗi mạng CHỈ CÓ DUY NHẤT 1 ZC. Nhiệm vụ khởi tạo mạng, chọn tần số, gán PAN ID, cấp địa chỉ cho nút con, lưu trữ bảng định tuyến. ZC luôn được cấp nguồn liên tục (mains-powered). Nếu có 2 ZC trùng PAN ID, ZC bật sau sẽ tự cộng thêm 1 vào PAN ID.", "1. Thiết bị điều phối (Coordinator - ZC): ")
    add_subbullet(doc, "Chuyển tiếp gói tin, mở rộng vùng phủ sóng, cho phép nút con kết nối (tối đa 6 nút con mỗi router). Cấp nguồn liên tục. ĐẶC BIỆT: KHI COORDINATOR BỊ NGẮT ĐIỆN, CÁC ROUTER VẪN DUY TRÌ MẠNG LƯỚI VÀ GIAO TIẾP VỚI NHAU BÌNH THƯỜNG!", "2. Thiết bị định tuyến (Router - ZR): ")
    add_subbullet(doc, "Là cảm biến hoặc cơ cấu chấp hành chạy bằng pin. Chỉ giao tiếp với nút cha (ZC hoặc ZR), không chuyển tiếp gói tin, có chế độ ngủ sâu (sleep mode) để tiết kiệm pin.", "3. Thiết bị đầu cuối (End Device - ZED): ")
    
    add_bullet(doc, "Tầng PHY và MAC tuân theo chuẩn IEEE 802.15.4; Các tầng trên gồm NWK (Mạng), APS (Hỗ trợ ứng dụng), ZDO (Đối tượng thiết bị) và Application Framework do Zigbee Alliance định nghĩa.", "Mô hình phân lớp: ")
    add_bullet(doc, "3 Dải tần lớp vật lý IEEE 802.15.4: 1) 868 MHz (BPSK, 20 kbps); 2) 902-928 MHz (BPSK, 40 kbps); 3) 2.4 GHz (O-QPSK, 250 kbps). Khung PSDU mang tối đa 127 bytes dữ liệu (gồm 32-bit Preamble, SFD 1 byte, Frame length 8-bit).", "3 Dải tần số: ")
    add_bullet(doc, "Cấu trúc Superframe 16 khe thời gian: khe đầu phát Beacon, các khe sau là thời gian truy cập tranh chấp CAP dùng CSMA-CA. 4 loại frame: 1) Beacon frame (đồng bộ mạng); 2) Data frame (tải trọng tối đa 104 bytes dữ liệu); 3) ACK frame (xác nhận); 4) MAC command frame (lệnh quản lý).", "Frame 802.15.4: ")

    add_callout(
        doc,
        "6 ĐẶC ĐIỂM NỔI BẬT CỦA CHUẨN ZIGBEE (TRỌNG TÂM THI ĐỀ MỞ)",
        "1. Độ tin cậy cực cao (High Reliability): Nhờ 6 cơ chế kết hợp: (1) O-QPSK và DSSS chống nhiễu SNR cao ở công suất thấp; (2) Cơ chế CSMA-CA lắng nghe tránh xung đột; (3) Mã kiểm tra 16-bit CRC loại bỏ gói lỗi; (4) Báo nhận ACK tại mỗi hop (hop-by-hop ACK) tự động phát lại; (5) Định tuyến mạng lưới Mesh với thuật toán AODV tự tìm đường vòng; (6) Xác nhận end-to-end ACK tại mức ứng dụng.\n"
        "2. Chi phí thấp (Low Cost): Nhiều hãng sản xuất chip giá rẻ (TI, Microchip, Atmel, ST...).\n"
        "3. Tiêu thụ năng lượng cực thấp (Low Power): Thiết bị chạy nhiều năm chỉ với 1 cặp pin AA nhờ chế độ ngủ sâu.\n"
        "4. Bảo mật rất cao (High Security): Dùng chuẩn mã hóa khối NIST AES-128 chuẩn quốc tế, miễn phí, chạy được trên cả vi điều khiển 8-bit.\n"
        "5. Chuẩn mở toàn bộ (Open Standard): Đặc tả kỹ thuật miễn phí tại zigbee.org.\n"
        "6. Tốc độ dữ liệu thấp (Low Data Rate): Tốc độ danh định 250 kbps, do mã hóa, truyền lại và hoạt động bán song công (half-duplex) nên thông lượng thực tế khoảng 25 kbps.",
        bg="FEF2F2", border_color="EF4444"
    )
    add_bullet(doc, "Phần cứng: CC1352R/P, CC2652R, CC2530, CC2538 (TI); Digi XBee; Silicon Labs MGM12P. Phần mềm: Arduino-based, nRF5 SDK, ZBOSS 3.0.", "Nền tảng hiện thực Zigbee: ")

    # 3.8.3
    add_heading3(doc, "3.8.3. Bộ giao thức WiFi 802.11")
    add_bullet(doc, "1) Infrastructure-based (Dựa trên hạ tầng: gồm Access Point AP và các trạm Station STA tạo thành Basic Service Set - BSS); 2) Ad-hoc / IBSS (Không hạ tầng: các thiết bị kết nối trực tiếp điểm-điểm không cần AP).", "2 Kiến trúc mạng: ")
    add_bullet(doc, "Hoạt động ở 2 tầng con PHY và MAC của OSI. Tầng LLC (IEEE 802.2) cung cấp giao diện trong suốt giúp mạng TCP/IP chạy trên WiFi giống hệt như trên mạng cáp có dây Ethernet.", "Mô hình phân lớp: ")
    
    add_callout(
        doc,
        "GIẢI MÃ 4 TRƯỜNG ĐỊA CHỈ MAC FRAME 802.11 THEO BIT 'TO DS' VÀ 'FROM DS'",
        "Trong Frame MAC của WiFi 802.11, vai trò của 4 địa chỉ (Address 1, 2, 3, 4) thay đổi tùy theo 2 bit To DS và From DS:\n\n"
        "• To DS = 0, From DS = 0 (Mạng Ad-hoc / IBSS):\n"
        "  - Address 1 = RA (Receiver) = DA (Destination - Đích đến)\n"
        "  - Address 2 = SA (Sender - Nguồn gửi)\n"
        "  - Address 3 = BSSID (Định danh mạng)\n"
        "  - Address 4 = Không sử dụng\n\n"
        "• To DS = 0, From DS = 1 (Gói tin truyền TỪ AP ĐẾN TRẠM THIẾT BỊ):\n"
        "  - Address 1 = RA = DA (Trạm nhận đích)\n"
        "  - Address 2 = BSSID (Địa chỉ của AP phát)\n"
        "  - Address 3 = SA (Trạm nguồn gửi ban đầu)\n"
        "  - Address 4 = Không sử dụng\n\n"
        "• To DS = 1, From DS = 0 (Gói tin truyền TỪ TRẠM LÊN ĐIỂM TRUY CẬP AP):\n"
        "  - Address 1 = RA = BSSID (Địa chỉ AP nhận)\n"
        "  - Address 2 = SA (Trạm gửi)\n"
        "  - Address 3 = DA (Đích đến cuối cùng)\n"
        "  - Address 4 = Không sử dụng\n\n"
        "• To DS = 1, From DS = 1 (Wireless Distribution System - Cầu nối không dây WDS giữa 2 AP):\n"
        "  - Address 1 = RA (AP nhận)\n"
        "  - Address 2 = TA (Transmitter - AP truyền)\n"
        "  - Address 3 = DA (Trạm đích cuối cùng)\n"
        "  - Address 4 = SA (Trạm nguồn phát ban đầu)\n\n"
        "📌 Chú thích: RA = Receiver, TA = Transmitter, DA = Destination, SA = Sender/Source, BSSID = Basic Service Set ID, DS = Distribution System.",
        bg="FFFBEB", border_color="F59E0B"
    )

    add_heading4(doc, "Chi tiết và tiến hóa 6 Chuẩn con WiFi (802.11 b, a, g, n, ac, ax)")
    add_bullet(doc, "Chuẩn hóa 1999, băng tần 2.4 GHz, tốc độ 11 Mbps. Giá rẻ, vùng phủ tốt nhưng dễ bị xuyên nhiễu bởi lò vi sóng, điện thoại không dây.", "• 802.11b: ")
    add_bullet(doc, "Chuẩn hóa cùng thời 11b, băng tần 5 GHz, tốc độ 54 Mbps dựa trên công nghệ OFDM. Tốc độ cao, không bị nhiễu 2.4GHz nhưng giá đắt, phạm vi hẹp, khó xuyên tường và KHÔNG tương thích với 802.11b.", "• 802.11a: ")
    add_bullet(doc, "Chuẩn hóa 2002-2003, băng tần 2.4 GHz, tốc độ 54 Mbps. Kết hợp ưu điểm của a và b: tốc độ cao, vùng phủ rộng, tương thích ngược hoàn toàn với 802.11b.", "• 802.11g: ")
    add_bullet(doc, "Chuẩn hóa 2009 (WiFi 4), hỗ trợ cả 2.4 GHz và 5 GHz. Bổ sung công nghệ MIMO (nhiều ăng-ten phát/thu), tốc độ 100 - 600 Mbps, tương thích ngược 11b/g.", "• 802.11n: ")
    add_bullet(doc, "Chuẩn hóa 2013 (WiFi 5), băng tần kép 2.4 & 5 GHz (chủ lực 5 GHz). Kênh rộng 80/160 MHz, điều chế 256-QAM, bổ sung MU-MIMO (đa người dùng). Chia làm 2 pha: Wave 1 (2013) và Wave 2 (2016 - bổ sung MU-MIMO, kênh 160MHz, 4 anten).", "• 802.11ac: ")
    add_bullet(doc, "Chuẩn hóa tháng 9/2020 (WiFi 6). Kế thừa 11ac, sử dụng kỹ thuật ghép kênh OFDMA, cung cấp tới 2048 sóng mang con. Tăng thông lượng gấp 4 lần ở mức người dùng, tối ưu hóa độ trễ trong môi trường cực đông đúc.", "• 802.11ax: ")
    add_bullet(doc, "Phần cứng: ESP8266, ESP32 (Espressif), Microchip, WI2WI WE935B00. Phần mềm: Arduino, Linux-based WLAN drivers.", "Nền tảng hiện thực WiFi: ")

    # 3.9 - 3.12
    add_heading2(doc, "3.9 - 3.12. Cảm biến, RFID, Video Tracking & Cơ cấu chấp hành")
    
    # 3.9
    add_heading3(doc, "3.9. Cảm biến trong IoT (IoT Sensors)")
    add_bullet(doc, "Thiết bị điện tử phát hiện các biến đổi vật lý trong môi trường và chuyển đổi tín hiệu đầu vào tương tự (Analog) thành tín hiệu đầu ra điện/kỹ thuật số (Digital Electrical Output) để gateway/cloud xử lý.", "Định nghĩa & Nguyên lý: ")
    add_bullet(doc, "10 LOẠI CẢM BIẾN PHỔ BIẾN TRONG IOT:", "10 Loại cảm biến: ")
    add_subbullet(doc, "Đo đại lượng nhiệt, phổ biến nhất vì ảnh hưởng đến mọi hệ thống vật lý, hóa học, sinh học.", "1. Cảm biến nhiệt độ (Temperature): ")
    add_subbullet(doc, "Đo áp suất khí, chất lỏng, mực nước, độ cao; ứng dụng trong máy bơm, máy nén, tủ lạnh, hệ thống thủy lực.", "2. Cảm biến áp suất (Pressure): ")
    add_subbullet(doc, "Đo vận tốc dòng chảy chất lỏng trong đường ống hoặc truyền nhiệt; ứng dụng trong giám sát axit độ tinh khiết cao.", "3. Cảm biến lưu lượng (Flow): ")
    add_subbullet(doc, "Đo mức chất lỏng liên tục hoặc tại điểm; ứng dụng trong bồn chứa, giếng khoan dầu mỏ.", "4. Cảm biến mức (Level): ")
    add_subbullet(doc, "Camera số, máy chụp ảnh y tế, thiết bị nhìn đêm; đo suy giảm sóng chuyển thành tín hiệu hình ảnh.", "5. Cảm biến hình ảnh (Imaging): ")
    add_subbullet(doc, "Đo độ ồn do máy móc, xe cộ, công trường; bảo vệ sức khỏe thính giác và tim mạch.", "6. Cảm biến tiếng ồn (Noise): ")
    add_subbullet(doc, "Quan trắc khí độc và nồng độ bụi mịn PM2.5, PM10 theo tiêu chuẩn môi trường EPA.", "7. Cảm biến ô nhiễm không khí (Air Pollution): ")
    add_subbullet(doc, "Phát và nhận sóng hồng ngoại dưới dạng nhiệt để theo dõi chuyển động vật thể.", "8. Cảm biến hồng ngoại (Infrared): ")
    add_subbullet(doc, "Đo độ ẩm tương đối trong không khí dựa vào biến thiên điện dung (Capacitive measurement).", "9. Cảm biến độ ẩm (Moisture & Humidity / Hygrometer): ")
    add_subbullet(doc, "Đo vận tốc xe cộ bằng cảm biến tốc độ bánh xe, speedometer, radar Doppler, laser velocimeter.", "10. Cảm biến tốc độ (Speed): ")

    # 3.10
    add_heading3(doc, "3.10. Công nghệ nhận dạng vô tuyến RFID (Radio-Frequency Identification)")
    add_bullet(doc, "RFID KHÔNG PHẢI LÀ CẢM BIẾN, mà là cơ chế thu thập thông tin được nhúng sẵn vào Thẻ (Tag) bằng sóng vô tuyến.", "Bản chất công nghệ: ")
    add_bullet(doc, "1) Thẻ RFID (Tag: gồm vi mạch microchip lưu trữ/xử lý thông tin và ăng-ten thu phát); 2) Đầu đọc RFID (Reader: bộ thu phát sóng 2 chiều và ăng-ten); 3) Phần mềm ứng dụng trên máy tính xử lý dữ liệu.", "3 Thành phần chính: ")
    add_callout(
        doc,
        "5 ƯU ĐIỂM VƯỢT TRỘI CỦA RFID SO VỚI MÃ VẠCH (BARCODE) - HAY HỎI THI",
        "1. Không cần tầm nhìn thẳng trực tiếp (No direct line of sight): Đầu đọc đọc được thẻ ẩn bên trong hàng hóa. Khoảng cách đọc xa: thẻ thụ động (passive UHF) đọc xa tới 12 mét; thẻ chủ động dùng pin (battery-powered) đọc xa tới 100 mét!\n"
        "2. Dữ liệu trên thẻ có thể sửa đổi/ghi đè (Modifiable data): Tùy chỉnh thông tin linh hoạt theo quy trình kinh doanh, trong khi mã vạch in ra là cố định vĩnh viễn.\n"
        "3. Độ bền cao và dung lượng lớn (Durable & High Capacity): Thẻ RFID đặt ẩn, chống chịu ẩm/bụi, tái sử dụng được nhiều lần và lưu trữ được lượng dữ liệu lớn hơn nhiều so với mã vạch.\n"
        "4. Bảo mật và mã hóa cao (Encrypted Data): Dữ liệu trên chip RFID có thể được mã hóa, ngăn chặn tuyệt đối việc làm giả, đánh cắp hoặc thay đổi trái phép.\n"
        "5. Đọc đồng thời hàng trăm thẻ (Simultaneous reading): Đầu đọc có thể quét và nhận dạng hàng trăm thẻ RFID cùng một lúc trong vài giây, tiết kiệm tối đa thời gian kiểm kê bán lẻ.",
        bg="F5F3FF", border_color="7C3AED"
    )

    # 3.11 & 3.12
    add_heading3(doc, "3.11 & 3.12. Giám sát bằng Video & Cơ cấu chấp hành (Actuators)")
    add_bullet(doc, "Quá trình thu thập và phân tích luồng video từng khung hình (frame-by-frame) trong khoảng thời gian ngắn để đo chuyển động, sự chú ý thị giác và hành vi. Dùng nhận dạng khách hàng, giám sát an ninh, thực tế tăng cường AR, kiểm soát giao thông. Là giải pháp thay thế/bổ trợ hoàn hảo khi không thể gắn cảm biến hoặc thẻ RFID.", "3.11. Giám sát bằng video (Video Tracking): ")
    add_bullet(doc, "Là một loại động cơ chịu trách nhiệm kiểm soát hoặc thực thi hành động trong hệ thống. Nhận nguồn dữ liệu hoặc năng lượng (điện, áp suất chất lỏng, khí nén) và CHUYỂN ĐỔI THÀNH CHUYỂN ĐỘNG CƠ HỌC để điều khiển hệ thống.", "3.12. Cơ cấu chấp hành (Actuator): ")
    add_bullet(doc, "3 LOẠI CƠ CẤU CHẤP HÀNH CỐT LÕI TRONG IOT:", "3 Loại Actuator: ")
    add_subbullet(doc, "Chuyển đổi chuyển động quay thành chuyển động thẳng bằng trục vít và đai ốc (leadscrew, screw jack, vít bi ball screw, vít con lăn roller screw).", "1. Actuator Tuyến tính Cơ khí (Mechanical Linear): ")
    add_subbullet(doc, "Điều khiển van tuyến tính hoặc van 1/4 vòng, hoạt động dựa trên ĐỊNH LUẬT PASCAL (khi có sự tăng áp suất tại bất kỳ điểm nào trong chất lỏng không nén được, áp suất sẽ tăng tương ứng tại mọi điểm trong bình chứa).", "2. Actuator Thủy lực (Hydraulic): ")
    add_subbullet(doc, "Cùng nguyên lý hoạt động như actuator thủy lực nhưng SỬ DỤNG KHÍ NÉN (compressed gas) thay vì chất lỏng.", "3. Actuator Khí nén (Pneumatic): ")

    # Bai tap C3
    add_callout(
        doc,
        "ĐÁP ÁN NHANH BÀI TẬP ÔN TẬP CHƯƠNG 3 (TRẢ LỜI NGAY TRONG PHÒNG THI)",
        "Câu 1: Liệt kê các kiến trúc mạng IoT và ưu nhược điểm? Trả lời: Bám sát Mục 3.7 và Bảng ma trận so sánh Topo ở Phần III (Star, Mesh, Tree, Ring, Chain, Grid, Cluster-based, Tributary-Delta, Sweep).\n"
        "Câu 2: So sánh các bộ giao thức không dây IoT và ứng dụng? Trả lời: Bám sát Mục 3.8 và Bảng ma trận so sánh Giao thức ở Phần III (6LoWPAN, Zigbee, WiFi, Bluetooth, LoRa).\n"
        "Câu 3: Dùng kiến trúc Zigbee xây dựng ứng dụng Giám sát chất lượng không khí? Trả lời: Nút cảm biến bụi PM2.5/khí độc đóng vai trò End Device (ZED) -> gửi dữ liệu về các Router (ZR) phân bố tại các trạm -> chuyển tiếp về Coordinator (ZC) đóng vai trò Gateway -> truyền TCP/IP lên Cloud lưu trữ và phân tích AI.\n"
        "Câu 4: Dùng kiến trúc WLAN 802.11 xây dựng Smart Home? Trả lời: Dùng kiến trúc hạ tầng (Infrastructure-based): Điểm truy cập Access Point (WiFi Router trong nhà) đóng vai trò trung tâm BSS. Các thiết bị đèn, công tắc, camera, cảm biến cửa dùng chip ESP8266/ESP32 đóng vai trò Station (STA) kết nối trực tiếp vào AP -> điều khiển nội bộ hoặc qua Cloud.\n"
        "Câu 5: Thiết kế mạng Nông nghiệp thông minh tại VN và chọn giao thức? Trả lời: Chọn LoRaWAN hoặc Zigbee cho vườn quy mô lớn/vườn nhà lưới vì tiêu thụ năng lượng cực thấp (chạy pin nhiều năm), tầm phủ xa, chịu thời tiết ẩm ướt tốt. Gateway kết nối 4G/Cellular đẩy dữ liệu lên Cloud.\n"
        "Câu 6: Thiết kế mạng giám sát không khí tại TP.HCM và chọn giao thức? Trả lời: Chọn kết hợp LoRaWAN (truyền xa hàng km qua nhà cao tầng) hoặc mạng di động NB-IoT/Cellular tại các trạm quan trắc lớn vì băng thông đủ gửi dữ liệu liên tục về trung tâm Sở TN&MT.\n"
        "Câu 7: Trình bày ý tưởng giám sát giao thông thông minh sử dụng công nghệ 5G? Trả lời: Tận dụng ưu điểm băng thông siêu cao (eMBB) và độ trễ cực thấp (URLLC < 1ms) của 5G: Truyền luồng video 4K thời gian thực từ camera giao thông -> AI tại Edge Server nhận diện biển số, đếm lưu lượng, phát hiện tai nạn ngay lập tức -> tự động điều chỉnh đèn tín hiệu xanh/đỏ và gửi cảnh báo đến các xe tự lái (V2X)."
    )

print("Part 3 (C3) built successfully!")
