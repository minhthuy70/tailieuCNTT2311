# -*- coding: utf-8 -*-
"""
Builder Parts 1 & 2 (Title, Abbreviations, Quick Keyword Index, Chapter 1 & 2 Details)
"""
from word_helpers import (
    add_heading1, add_heading2, add_heading3, add_heading4,
    add_bullet, add_subbullet, add_callout, add_table
)
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_cover_and_info(doc):
    # Cover / Header
    p_top = doc.add_paragraph()
    p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_top.paragraph_format.space_before = Pt(10)
    p_top.paragraph_format.space_after = Pt(2)
    r_sub = p_top.add_run("TRƯỜNG ĐẠI HỌC KỸ THUẬT – CÔNG NGHỆ CẦN THƠ\nKHOA KỸ THUẬT CƠ KHÍ – BỘ MÔN CƠ ĐIỆN TỬ")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("MỤC LỤC CHI TIẾT & SỔ TAY TRA CỨU NHANH\nPHỤC VỤ THI ĐỀ MỞ")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(15, 76, 129)

    p_course = doc.add_paragraph()
    p_course.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_course.paragraph_format.space_before = Pt(2)
    p_course.paragraph_format.space_after = Pt(12)
    r_c = p_course.add_run("HỌC PHẦN: PHÁT TRIỂN ỨNG DỤNG IOT (MÃ HP: TT188)\nTài liệu trọng tâm: CHƯƠNG 1 – CHƯƠNG 2 – CHƯƠNG 3")
    r_c.font.name = "Calibri"
    r_c.font.size = Pt(11.5)
    r_c.font.bold = True
    r_c.font.color.rgb = RGBColor(2, 132, 199)

    add_callout(
        doc,
        "CẨM NANG CHIẾN LƯỢC CHO KỲ THI ĐỀ MỞ (HƯỚNG DẪN SỬ DỤNG NHANH)",
        "1. KHI ĐỌC ĐỀ THI: Hãy khoanh tròn 'Từ khóa chính' (Ví dụ: CSMA-CA, 6LoWPAN, Zigbee, Topo Ring, Bụi PM2.5, RFID, Pascal, 4 Cấp độ IoT, IT vs OT...).\n"
        "2. BƯỚC 1 - TRA NHANH: Tra từ khóa tại PHẦN I (BẢNG CHỈ MỤC TỪ KHÓA A-Z) ở ngay trang sau để định vị chính xác Số mục, Số trang và Định nghĩa/Đặc điểm cốt lõi.\n"
        "3. BƯỚC 2 - LẤY LUẬN ĐIỂM: Mở đến PHẦN II (MỤC LỤC PHÂN CẤP CHI TIẾT) để lấy toàn bộ các ý phân tích, thông số kỹ thuật, cấu trúc gói tin, ưu/nhược điểm.\n"
        "4. BƯỚC 3 - CÂU HỎI SO SÁNH / THIẾT KẾ: Lật ngay tới PHẦN III (BẢNG MA TRẬN SO SÁNH & ĐỐI CHIẾU) để chép bảng so sánh WiFi, Topo, Giao thức và bám sát Khung thiết kế 4 lớp đạt điểm tuyệt đối."
    )

    add_heading2(doc, "THÔNG TIN HỌC PHẦN & TÀI LIỆU GỐC")
    add_bullet(doc, "Học phần: Phát triển ứng dụng IoT (IoT Application Development) — Mã học phần: TT188 (03 tín chỉ: 30 tiết LT, 30 tiết TH).", "Môn học: ")
    add_bullet(doc, "TS. Nguyễn Đình Tứ (Trưởng Bộ môn Cơ điện tử, Khoa Kỹ thuật Cơ khí, ĐH KT-CN Cần Thơ — Email: ndtu@ctuet.edu.vn — SĐT: 0776181954).", "Giảng viên biên soạn: ")
    add_bullet(doc, "Giới thiệu kiến thức cơ bản về IoT, các yêu cầu, tiêu chuẩn, kiến trúc mạng, bộ giao thức không dây và ứng dụng; giúp sinh viên có kỹ năng thiết kế, đánh giá hệ thống giám sát và điều khiển qua Internet.", "Mục tiêu & Kỹ năng: ")
    add_bullet(doc, "File IoTmainC123.docx (Bao gồm Phần mở đầu, Chương 1, Chương 2, Chương 3 và hệ thống câu hỏi bài tập ôn tập).", "Phạm vi tài liệu: ")

    add_heading2(doc, "BẢNG KÝ HIỆU VIẾT TẮT TIÊU CHUẨN TRONG IOT")
    abbr_headers = ["Ký hiệu", "Tên tiếng Anh đầy đủ", "Ý nghĩa / Vai trò trong IoT"]
    abbr_data = [
        ["6LoWPAN", "IPv6 over Low-Power Wireless PAN", "Giao thức cho phép truyền gói tin IPv6 qua mạng không dây công suất thấp (IEEE 802.15.4)"],
        ["AI", "Artificial Intelligence", "Trí tuệ nhân tạo dùng để phân tích dữ liệu, nhận dạng và ra quyết định thông minh"],
        ["CPS", "Chip Package System", "Phương pháp thiết kế tích hợp vi mạch - đóng gói - hệ thống giúp tối ưu năng lượng IoT"],
        ["CPU", "Central Processing Unit", "Bộ xử lý trung tâm của các hệ thống máy tính, bộ định tuyến và thiết bị IoT"],
        ["GPU", "Graphics Processing Unit", "Bộ xử lý đồ họa, hỗ trợ tính toán song song lớn cho các thuật toán AI/thị giác máy tính"],
        ["HTTP", "HyperText Transfer Protocol", "Giao thức truyền tải siêu văn bản truyền thống trên tầng Application (TCP/IP)"],
        ["ICT", "Information & Communication Technologies", "Công nghệ Thông tin và Truyền thông nền tảng cho Smart City"],
        ["IoTs", "Internet of Things", "Mạng lưới vạn vật kết nối Internet trao đổi dữ liệu tự động"],
        ["MQTT", "Message Queuing Telemetry Transport", "Giao thức nhắn tin nhẹ theo mô hình Publish/Subscribe chạy trên nền TCP"],
        ["CoAP", "Constrained Application Protocol", "Giao thức bản tin hướng web nhẹ cho thiết bị hạn chế tài nguyên, chạy trên UDP"],
        ["NFV", "Network Function Virtualization", "Ảo hóa các chức năng mạng giúp tăng tính linh hoạt và mở rộng cho IoT"],
        ["OIC", "Open InterConnect Consortium", "Hiệp hội liên minh IoT do Intel, Samsung, Dell... thành lập đảm bảo tương tác"],
        ["OTAP", "Over The Air Programming", "Lập trình và cập nhật vi điều khiển từ xa qua kết nối không dây"],
        ["REST", "Representational State Transfer", "Kiểu kiến trúc phần mềm phổ biến cho các dịch vụ web và API IoT"],
        ["SDN", "Software Defined Network", "Mạng điều khiển bằng phần mềm tách rời tầng điều khiển và tầng dữ liệu"],
        ["TPU", "Tensor Processing Unit", "Mạch tích hợp chuyên dụng cho máy học/AI do Google phát triển"],
        ["VM", "Virtual Machine", "Máy ảo phục vụ triển khai nền tảng đám mây và tính toán biên"]
    ]
    add_table(doc, abbr_headers, abbr_data, [1.0, 2.3, 3.37])

def build_part1_keyword_index(doc):
    add_heading1(doc, "PHẦN I: BẢNG CHỈ MỤC TỪ KHÓA & TRA CỨU NHANH THEO CÂU HỎI (INDEX A-Z)")
    
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run("Bảng tra cứu dưới đây sắp xếp theo thứ tự bảng chữ cái và các chủ đề nóng nhất trong đề thi. Khi thấy từ khóa trong đề bài, hãy tra ngay dòng tương ứng để biết Mục tài liệu và các luận điểm mấu chốt:")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.italic = True

    idx_headers = ["Từ khóa / Chủ đề thi", "Mục", "Định nghĩa / Đặc điểm cốt lõi & Từ khóa cần trả lời"]
    idx_data = [
        ["6LoWPAN (Tổng quan)", "3.8.1", "IPv6 over Low-Power Wireless PAN; RFC 6282 IETF; mở rộng Sub-1GHz, Bluetooth, PLC, Wi-Fi. Kết nối trực tiếp ra Internet."],
        ["6LoWPAN (Cấu trúc gói & Nén Header)", "3.8.1.3", "3 ngữ cảnh nén IPv6 header: Nội bộ link-local (2B); Ra ngoài biết prefix (12B); Ra ngoài không biết prefix (20B). Chồng stacked headers."],
        ["6LoWPAN (Kiến trúc & Phân lớp)", "3.8.1.1\n3.8.1.2", "Host (thiết bị cuối, ngủ định kỳ) & Router (định tuyến); Edge router; PHY 802.15.4e/g; MAC CSMA-CA; Tầng ứng dụng: CoAP (UDP), MQTT (TCP)."],
        ["Actuator (Cơ cấu chấp hành)", "3.12", "Chuyển năng lượng/dữ liệu thành chuyển động. 3 loại: Cơ khí tuyến tính (trục vít), Thủy lực (Định luật Pascal), Khí nén (khí nén)."],
        ["AllSeen Alliance / AllJoyn", "1.3", "Liên minh IoT gồm Qualcomm, Haier, LG, Panasonic, Microsoft... phát triển hạ tầng AllJoyn mã nguồn mở."],
        ["Analytics at the Edge", "1.1.9\n1.1.11", "Xử lý/phân tích dữ liệu thời gian thực gần nguồn; Phân biệt Big Data, Structured (có cấu trúc), Unstructured (phi cấu trúc); Analytics 1.0/2.0/3.0."],
        ["Bảo mật IoT (4 lĩnh vực dễ bị tấn công)", "1.1.7", "1) Dữ liệu trên đường truyền (sniffing, man-in-the-middle); 2) Kiểm soát API thiết bị; 3) Truy cập dữ liệu lưu trữ/Cloud/Bluetooth spoofing; 4) Đánh cắp định danh/mật khẩu mặc định."],
        ["Bài tập Chương 1 (5 câu hỏi)", "1.Bài tập", "Thiết bị kết nối; Đặc điểm kỹ thuật; Xu thế TG & VN; Ưu điểm cho cuộc sống; Thách thức kỹ thuật."],
        ["Bài tập Chương 2 (7 câu hỏi)", "2.Bài tập", "Ứng dụng Smart City/Home; 4 lớp kiến trúc; Thiết kế Nông nghiệp VN; Giám sát giao thông; Giám sát không khí HCM."],
        ["Bài tập Chương 3 (7 câu hỏi)", "3.Bài tập", "Ưu nhược điểm các topo mạng; So sánh giao thức không dây; Thiết kế hệ thống Zigbee, WiFi, Nông nghiệp, Giám sát không khí, 5G."],
        ["Barcelona Smart City (CityOS)", "2.2.5", "Giao thông thông minh ưu tiên xe buýt và đèn xanh xe khẩn cấp; Đèn LED tiết kiệm; Cảm biến tiếng ồn (>100dB WHO); Thủy lợi giảm 25% nước; Chính quyền liên thông."],
        ["Cảm biến (IoT Sensors - 10 loại)", "3.9", "Biến đổi Analog thành Digital electrical output. 10 loại: Nhiệt độ, Áp suất, Lưu lượng, Mức, Hình ảnh, Tiếng ồn, Ô nhiễm bụi PM2.5, Hồng ngoại, Độ ẩm, Tốc độ."],
        ["Cấp độ IoT (4-Level IoT Model)", "1.1.8", "1-Device Level (Things, Sensor/Actuator); 2-Network Level (Gateway/Router); 3-Services Platform Level; 4-Application Level. 6 ưu điểm nổi bật."],
        ["Chuyển đổi số & Hội tụ (Convergence)", "1.1.9\n1.1.10", "Hội tụ OT (nhà máy, thời gian thực 24/7 zero downtime) và IT (hệ thống thông tin tính toán, lưu trữ, mạng). Điện thoại thông minh là ví dụ hội tụ."],
        ["Định luật Moore (Moore's Law)", "1.1.11", "3 quan sát: 1) Sức mạnh máy tính tăng gấp đôi mỗi 18 tháng; 2) Kích thước bóng bán dẫn thu nhỏ tiệm cận nguyên tử; 3) Giá bóng bán dẫn giảm >50% mỗi năm."],
        ["Định địa chỉ IPv4 và Lớp mạng", "3.4", "IPv4 32-bit (4 octet). Chia Network/Host bằng Subnet Mask. 5 lớp: A (1-126), B (128-191), C (192-223), D (Multicast 224-239), E (Thử nghiệm 240-255). Loopback 127.x.x.x."],
        ["Định địa chỉ IPv6", "3.4", "IPv6 128-bit, 8 khối 16-bit, colon-hexadecimal. Giải quyết triệt để cạn kiệt địa chỉ cho 50 tỷ thiết bị IoT."],
        ["Độ trễ đầu cuối (End-to-End Delay)", "3.3", "dTotal = dProcess + dQueue + dTrans + dProp. dTrans = L/R (phụ thuộc độ dài gói). dProp = Khoảng cách/Vận tốc (độc lập độ dài gói). Đo bằng Traceroute, Cisco IP SLA."],
        ["Giao thông thông minh (Smart Traffic)", "2.2.2", "Đường sắt đô thị, thẻ thông minh, xe điện, FCD (Floating Car Data) từ GPS, điều khiển đèn giao thông theo mật độ camera thời gian thực."],
        ["Mất gói tin (Packet Loss) & Thông lượng", "3.3", "Mất gói do nghẽn liên kết và hàng đợi router đầy; Throughput: lượng dữ liệu tối đa truyền thành công (bps/Gbps), phân biệt tốc độ liên kết và thời gian phản hồi."],
        ["Mô hình OSI vs TCP/IP", "3.1\n3.2", "OSI: 7 tầng (ISO 1984, chia để trị). TCP/IP: 4 tầng (Application, Transport [TCP/UDP], Internet [IP datagram], Network Access [Ethernet/WiFi])."],
        ["Nhà thông minh (Smart Home)", "2.1", "4 giải pháp tích hợp: 1) Giám sát an ninh (Camera nhận diện, cảm biến cửa/gas/khói); 2) Điều khiển thiết bị (đèn, rèm, HVAC); 3) Quản lý năng lượng; 4) Thiết bị nhà bếp."],
        ["Nông nghiệp thông minh (Smart Agriculture)", "2.3", "Nông nghiệp chính xác (Precision Agriculture). Kiến trúc 4 lớp: Thiết bị (WSN cảm biến cây/vật nuôi) -> Edge/Gateway -> Cloud Computing -> Service (Web App điều khiển vòng kín)."],
        ["OIC (Open InterConnect Consortium)", "1.3", "Tổ chức tiêu chuẩn do Intel, Samsung, Dell, Broadcom thành lập, thúc đẩy tương tác cho hàng tỷ thiết bị IoT."],
        ["Phạm vi mạng (PAN, LAN, MAN, WAN)", "3.6", "PAN (vài mét, Bluetooth); LAN (tòa nhà, 100-1000Mbps, switch/router); MAN (thành phố, ISP); WAN (quốc gia/toàn cầu, PSTN/vệ tinh, độ trễ và lỗi cao)."],
        ["RFID (Nhận dạng tần số vô tuyến)", "3.10", "Tag (Microchip + Ăng-ten) + Reader + Phần mềm. 5 ưu điểm vượt trội so với mã vạch: không cần line of sight (12m-100m), sửa được data, bền ẩn, mã hóa, đọc hàng trăm thẻ cùng lúc."],
        ["Router (4 thành phần phần cứng chính)", "3.2", "NVRAM (lưu startup config, không mất khi tắt điện); Console port (quản lý trực tiếp qua RJ45/USB); Flash memory (lưu Cisco IOS); DRAM (lưu routing table, ARP, buffer)."],
        ["Thành phố thông minh (Smart City - 4 lớp)", "2.2.1", "1) Street Layer (cảm biến đỗ xe, đèn, video, PM2.5); 2) City Layer (chuyển tiếp đa giao thức, chịu lỗi cao); 3) Data Center Layer (Cloud phân tích AI); 4) Service Layer (dịch vụ người dân & quản lý)."],
        ["Thành phố thông minh (3 hướng tiếp cận)", "2.2", "1) Top-down (Từ trên xuống: quy hoạch kiến trúc tổng thể trước); 2) Bottom-up (Từ dưới lên: làm từng dự án rồi ghép); 3) Hybrid (Lai ghép cả hai)."],
        ["Thách thức kỹ thuật trong phát triển IoT", "1.4", "1) Phần mềm toàn bộ vòng đời & mã nguồn mở; 2) Băng thông và tốc độ truyền; 3) Tối ưu công suất/năng lượng (thiết kế CPS Chip-Package-System); 4) Tích hợp Cloud/Edge."],
        ["Topo mạng đơn giản (Mesh, Tree, Ring, Chain, Star, Grid)", "3.7.1", "Full/Partial Mesh (đa đường, chịu lỗi cao); Tree (phân cấp gốc-sink, dễ đứt tuyến); Ring (1 chiều, hỏng 1 nút sụp cả mạng); Chain (chuỗi); Star (hub trung tâm, single point of failure); Grid (ô vuông luân phiên)."],
        ["Topo mạng phức tạp (Cluster, Tributary-Delta, Sweep)", "3.7.2", "Cluster-based (đầu cụm Cluster Head, nén dữ liệu); Tributary-Delta (cây ở vùng lỗi thấp, đa luồng ở vùng lỗi cao); Sweep (làn sóng quét qua mạng 1 lần, cực bền vững)."],
        ["Video Tracking (Theo dõi bằng Video)", "3.11", "Thu thập phân tích từng khung hình (frame-by-frame), đo chuyển động, sự chú ý và hành vi. Bổ trợ khi không có cảm biến/RFID."],
        ["WiFi 802.11 (Kiến trúc & Phân lớp)", "3.8.3.1\n3.8.3.2", "Kiến trúc hạ tầng (AP + STA -> BSS) vs Ad-hoc (IBSS không có AP); PHY (IR, FHSS, DSSS, OFDM); MAC (CSMA-CA); LLC 802.2 giao tiếp trong suốt với TCP/IP."],
        ["WiFi 802.11 (Frame MAC & Bit To DS / From DS)", "3.8.3.3", "Bảng tra 4 địa chỉ: 00 (Independent BSS: Addr1=RA/DA, Addr2=SA, Addr3=BSSID); 01 (Từ AP: Addr1=RA/DA, Addr2=BSSID, Addr3=SA); 10 (Tới AP: Addr1=RA/BSSID, Addr2=SA, Addr3=DA); 11 (WDS: Addr1=RA, Addr2=TA, Addr3=DA, Addr4=SA)."],
        ["WiFi 802.11 (So sánh các chuẩn a/b/g/n/ac/ax)", "3.8.3.4", "11b (2.4GHz, 11M); 11a (5GHz, 54M, OFDM); 11g (2.4GHz, 54M); 11n/WiFi 4 (MIMO, 100-600M); 11ac/WiFi 5 (5GHz, MU-MIMO, Wave 1/2); 11ax/WiFi 6 (OFDMA, 2048 sóng mang, x4 thông lượng)."],
        ["Zigbee (3 loại thiết bị mạng logic)", "3.8.2.1", "Coordinator ZC (duy nhất 1 ZC khởi tạo mạng, cấp địa chỉ, mains-powered); Router ZR (chuyển tiếp gói, mở rộng mạng, cấp nguồn liên tục, ZC tắt ZR vẫn giữ mạng); End Device ZED (cảm biến/chấp hành, pin, ngủ sâu)."],
        ["Zigbee (Phân lớp & Tần số 802.15.4)", "3.8.2.2", "PHY & MAC theo IEEE 802.15.4; NWK, APS, ZDO theo Zigbee Alliance. 3 dải tần: 868MHz (BPSK 20k), 915MHz (BPSK 40k), 2.4GHz (O-QPSK 250k). PSDU max 127B."],
        ["Zigbee (Superframe & 4 loại frame)", "3.8.2.3", "Superframe 16 khe thời gian (khe 0 Beacon, các khe sau là CAP tranh chấp dùng CSMA/CA); 4 dạng frame: Beacon frame, Data frame (max 104B payload), ACK frame, MAC command frame."],
        ["Zigbee (6 đặc điểm nổi bật)", "3.8.2.4", "1) Độ tin cậy cao (O-QPSK/DSSS, CSMA-CA, CRC-16, ACK mỗi hop, Mesh AODV, End-to-end ACK); 2) Chi phí thấp; 3) Tiêu thụ năng lượng cực thấp (pin AA nhiều năm); 4) Bảo mật cao (NIST AES-128); 5) Chuẩn mở toàn bộ; 6) Tốc độ thấp (danh định 250kbps, thực tế 25kbps half-duplex)."]
    ]
    add_table(doc, idx_headers, idx_data, [1.8, 0.9, 3.97])

print("Part 1 built successfully!")
