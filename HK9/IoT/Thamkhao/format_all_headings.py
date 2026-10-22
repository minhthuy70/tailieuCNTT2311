import re, sys

# Map of major headings to look for and format nicely
headings = [
    # Chapter 3
    (52, r'CHƯƠNG\s+3.*?\n+CÁC\s+KIẾN\s+TRÚC.*?\n+', '# CHƯƠNG 3. CÁC KIẾN TRÚC MẠNG VÀ BỘ GIAO THỨC MẠNG IOT\n\n'),
    (53, r'3\.1\.\s+Các\s+kiến\s+trúc\s+mạng\s+dùng\s+trong\s+IoT', '### 3.1. Các kiến trúc mạng dùng trong IoT\n\n'),
    (53, r'3\.1\.1\.\s+Một\s+số\s+kiến\s+trúc\s+mạng\s+đơn\s+giản', '#### 3.1.1. Một số kiến trúc mạng đơn giản\n\n'),
    (56, r'3\.1\.2\.\s+Một\s+số\s+kiến\s+trúc\s+mạng\s+phức\s+tạp', '#### 3.1.2. Một số kiến trúc mạng phức tạp\n\n'),
    (59, r'3\.2\.\s+Các\s+bộ\s+giao\s+thức\s+mạng\s+không\s+dây\s+thường\s+dùng\s+trong\s+IoT', '### 3.2. Các bộ giao thức mạng không dây thường dùng trong IoT\n\n'),
    (59, r'3\.2\.1\.\s+Bộ\s+giao\s+thức\s+6LoWPAN', '#### 3.2.1. Bộ giao thức 6LoWPAN\n\n'),
    (60, r'3\.2\.1\.1\.\s+Kiến\s+trúc\s+mạng\s+6LoWPAN', '##### 3.2.1.1. Kiến trúc mạng 6LoWPAN\n\n'),
    (61, r'3\.2\.1\.2\.\s+Mô\s+hình\s+phân\s+lớp\s+các\s+tầng\s+giao\s+thức\s+trong\s+6LoWPAN', '##### 3.2.1.2. Mô hình phân lớp các tầng giao thức trong 6LoWPAN\n\n'),
    (63, r'3\.2\.1\.3\.\s+Cấu\s+trúc\s+gói\s+tin\s+của\s+chuẩn\s+mạng\s+6LoWPAN', '##### 3.2.1.3. Cấu trúc gói tin của chuẩn mạng 6LoWPAN\n\n'),
    (64, r'3\.2\.1\.4\.\s+Nền\s+tảng\s+hiện\s+thực\s+bộ\s+giao\s+thức\s+6LoWPAN', '##### 3.2.1.4. Nền tảng hiện thực bộ giao thức 6LoWPAN\n\n'),
    (65, r'3\.2\.2\.\s+Bộ\s+giao\s+thức\s+Zigbee', '#### 3.2.2. Bộ giao thức Zigbee\n\n'),
    (65, r'3\.2\.2\.1\.\s+Kiến\s+trúc\s+mạng\s+Zigbee', '##### 3.2.2.1. Kiến trúc mạng Zigbee\n\n'),
    (66, r'3\.2\.2\.2\.\s+Mô\s+hình\s+phân\s+lớp\s+các\s+tầng\s+giao\s+thức\s+trong\s+chuẩn\s+không\s+dây\s+Zigbee', '##### 3.2.2.2. Mô hình phân lớp các tầng giao thức trong chuẩn không dây Zigbee\n\n'),
    (68, r'3\.2\.2\.3\.\s+Cấu\s+trúc\s+frame\s+của\s+chuẩn\s+802\.15\.4', '##### 3.2.2.3. Cấu trúc frame của chuẩn 802.15.4\n\n'),
    (70, r'3\.2\.2\.4\.\s+Một\s+số\s+đặc\s+điểm\s+của\s+chuẩn\s+Zigbee\s+trong\s+ứng\s+dụng\s+mạng\s+cảm\s+biến\s+không\s+dây', '##### 3.2.2.4. Một số đặc điểm của chuẩn Zigbee trong ứng dụng mạng cảm biến không dây\n\n'),
    (73, r'3\.2\.2\.5\.\s+Nền\s+tảng\s+hiện\s+thực\s+bộ\s+giao\s+thức\s+mạng\s+Zigbee', '##### 3.2.2.5. Nền tảng hiện thực bộ giao thức mạng Zigbee\n\n'),
    (74, r'3\.2\.3\.\s+Bộ\s+giao\s+thức\s+WiFi\s+802\.11', '#### 3.2.3. Bộ giao thức WiFi 802.11\n\n'),
    (74, r'3\.2\.3\.1\.\s+Kiến\s+trúc\s+mạng\s+WiFi\s+802\.11', '##### 3.2.3.1. Kiến trúc mạng WiFi 802.11\n\n'),
    (75, r'3\.2\.3\.2\.\s+Mô\s+hình\s+phân\s+lớp\s+tầng\s+giao\s+thức\s+trong\s+chuẩn\s+không\s+dây\s+802\.11', '##### 3.2.3.2. Mô hình phân lớp tầng giao thức trong chuẩn không dây 802.11\n\n'),
    (77, r'3\.2\.3\.3\.\s+Cấu\s+trúc\s+frame\s+của\s+chuẩn\s+không\s+dây\s+802\.11', '##### 3.2.3.3. Cấu trúc frame của chuẩn không dây 802.11\n\n'),
    (78, r'3\.2\.3\.4\.\s+Một\s+số\s+chuẩn\s+con\s+của\s+802\.11', '##### 3.2.3.4. Một số chuẩn con của 802.11\n\n'),
    (81, r'3\.2\.3\.5\.\s+Nền\s+tảng\s+hiện\s+thực\s+bộ\s+giao\s+thức\s+mạng\s+WiFi', '##### 3.2.3.5. Nền tảng hiện thực bộ giao thức mạng WiFi\n\n'),
    (82, r'BÀI\s+TẬP\s+CHƯƠNG\s+3', '## BÀI TẬP CHƯƠNG 3\n\n'),

    # Chapter 4
    (83, r'CHƯƠNG.*?\n+CÁC\s+NỀN\s+TẢNG\s+PHẦN\s+CỨNG.*?\n+', '# CHƯƠNG 4. CÁC NỀN TẢNG PHẦN CỨNG VÀ PHẦN MỀM IOT THÔNG DỤNG\n\n'),
    (84, r'4\.1\.\s+Các\s+nền\s+tảng\s+phần\s+cứng', '### 4.1. Các nền tảng phần cứng\n\n'),
    (84, r'4\.1\.1\.\s+Những\s+đặc\s+trưng\s+và\s+phân\s+loại\s+các\s+nền\s+tảng\s+phần\s+cứng\s+dùng\s+cho\s+IoT', '#### 4.1.1. Những đặc trưng và phân loại các nền tảng phần cứng dùng cho IoT\n\n'),
    (86, r'4\.1\.2\.\s+Thiết\s+bị\s+cảm\s+biến\s+không\s+dây\s+TelosB', '#### 4.1.2. Thiết bị cảm biến không dây TelosB\n\n'),
    (86, r'4\.1\.3\.\s+Thiết\s+bị\s+nhúng\s+Arduino', '#### 4.1.3. Thiết bị nhúng Arduino\n\n'),
    (88, r'4\.1\.4\.\s+Thiết\s+bị\s+máy\s+tính\s+nhúng\s+Raspberry\s+Pi', '#### 4.1.4. Thiết bị máy tính nhúng Raspberry Pi\n\n'),
    (90, r'4\.1\.5\.\s+Tổng\s+hợp\s+một\s+số\s+nền\s+tảng\s+phần\s+cứng\s+IoT\s+phổ\s+biến', '#### 4.1.5. Tổng hợp một số nền tảng phần cứng IoT phổ biến\n\n'),
    (91, r'4\.2\.\s+Các\s+nền\s+tảng\s+phần\s+mềm\s+dùng\s+trong\s+IoT', '### 4.2. Các nền tảng phần mềm dùng trong IoT\n\n'),
    (91, r'4\.2\.1\.\s+Những\s+đặc\s+trưng\s+và\s+phân\s+loại\s+hệ\s+điều\s+hành\s+dùng\s+cho\s+thiết\s+bị\s+IoT', '#### 4.2.1. Những đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT\n\n'),
    (93, r'4\.2\.2\.\s+Hệ\s+điều\s+hành\s+TinyOS', '#### 4.2.2. Hệ điều hành TinyOS\n\n'),
    (93, r'4\.2\.2\.1\.\s+Cấu\s+trúc\s+một\s+ứng\s+dụng\s+trên\s+TinyOS', '##### 4.2.2.1. Cấu trúc một ứng dụng trên TinyOS\n\n'),
    (96, r'4\.2\.2\.2\.\s+Các\s+thành\s+phần,\s+dịch\s+vụ\s+cơ\s+bản\s+của\s+TinyOS', '##### 4.2.2.2. Các thành phần, dịch vụ cơ bản của TinyOS\n\n'),
    (103, r'4\.2\.3\.\s+Hệ\s+điều\s+hành\s+Contiki', '#### 4.2.3. Hệ điều hành Contiki\n\n'),
    (104, r'4\.2\.3\.1\.\s+Cấu\s+trúc\s+một\s+ứng\s+dụng\s+trên\s+Contiki', '##### 4.2.3.1. Cấu trúc một ứng dụng trên Contiki\n\n'),
    (105, r'4\.2\.3\.2\.\s+Các\s+thành\s+phần,\s+dịch\s+vụ\s+cơ\s+bản\s+trên\s+hệ\s+điều\s+hành\s+Contiki', '##### 4.2.3.2. Các thành phần, dịch vụ cơ bản trên hệ điều hành Contiki\n\n'),
    (108, r'4\.2\.4\.\s+Hệ\s+điều\s+hành\s+Raspbian\s+OS', '#### 4.2.4. Hệ điều hành Raspbian OS\n\n'),
    (111, r'4\.2\.5\.\s+Tổng\s+hợp\s+một\s+số\s+nền\s+tảng\s+phần\s+mềm\s+IoT\s+phổ\s+biến', '#### 4.2.5. Tổng hợp một số nền tảng phần mềm IoT phổ biến\n\n'),
    (114, r'BÀI\s+TẬP\s+CHƯƠNG\s+4', '## BÀI TẬP CHƯƠNG 4\n\n'),

    # Chapter 5
    (116, r'CHƯƠNG\s+5.*?\n+ĐIỆN\s+TOÁN\s+ĐÁM\s+MÂY.*?\n+', '# CHƯƠNG 5. ĐIỆN TOÁN ĐÁM MÂY, ĐIỆN TOÁN CẬN BIÊN VÀ IOT\n\n'),
    (117, r'5\.1\.\s+Kiến\s+trúc\s+tổng\s+quan\s+hệ\s+thống\s+IoT\s+tích\s+hợp\s+điện\s+toán\s+đám\s+mây\s+và\s+điện\s+toán\s+cận\s+biên', '### 5.1. Kiến trúc tổng quan hệ thống IoT tích hợp điện toán đám mây và điện toán cận biên\n\n'),
    (117, r'5\.1\.1\.\s+Kiến\s+trúc\s+tổng\s+quan', '#### 5.1.1. Kiến trúc tổng quan\n\n'),
    (119, r'5\.1\.2\.\s+Các\s+yêu\s+cầu\s+và\s+đặc\s+trưng\s+cơ\s+bản\s+của\s+các\s+hệ\s+thống\s+tính\s+toán\s+cho\s+IoT', '#### 5.1.2. Các yêu cầu và đặc trưng cơ bản của các hệ thống tính toán cho IoT\n\n'),
    (120, r'5\.2\.\s+Nền\s+tảng\s+điện\s+toán\s+đám\s+mây\s+và\s+ứng\s+dụng\s+trong\s+IoT', '### 5.2. Nền tảng điện toán đám mây và ứng dụng trong IoT\n\n'),
    (121, r'5\.2\.1\.\s+Đặc\s+trưng\s+cơ\s+bản\s+của\s+điện\s+toán\s+đám\s+mây', '#### 5.2.1. Đặc trưng cơ bản của điện toán đám mây\n\n'),
    (122, r'5\.2\.2\.\s+Lợi\s+ích\s+của\s+điện\s+toán\s+đám\s+mây', '#### 5.2.2. Lợi ích của điện toán đám mây\n\n'),
    (124, r'5\.2\.3\.\s+Mô\s+hình\s+IaaS', '#### 5.2.3. Mô hình IaaS\n\n'),
    (126, r'5\.2\.4\.\s+Mô\s+hình\s+PaaS', '#### 5.2.4. Mô hình PaaS\n\n'),
    (127, r'5\.2\.5\.\s+Mô\s+hình\s+SaaS', '#### 5.2.5. Mô hình SaaS\n\n'),
    (129, r'5\.2\.6\.\s+Ứng\s+dụng\s+công\s+nghệ\s+điện\s+toán\s+đám\s+mây\s+trong\s+xây\s+dựng\s+hệ\s+thống\s+giả\s+lập\s+WSN\s+với\s+số\s+lượng\s+nút\s+lớn', '#### 5.2.6. Ứng dụng công nghệ điện toán đám mây trong xây dựng hệ thống giả lập WSN với số lượng nút lớn\n\n'),
    (131, r'5\.2\.6\.1\.\s+Thiết\s+kế\s+kiến\s+trúc,\s+giải\s+pháp\s+xây\s+dựng\s+kiến\s+trúc\s+mạng\s+luận\s+lý\s+MESH\s+của\s+WSNs\s+trên\s+OpenStack', '##### 5.2.6.1. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý MESH của WSNs trên OpenStack\n\n'),
    (132, r'5\.2\.6\.2\.\s+Thiết\s+kế\s+kiến\s+trúc,\s+giải\s+pháp\s+xây\s+dựng\s+kiến\s+trúc\s+mạng\s+luận\s+lý\s+TREE\s+của\s+WSNs\s+trên\s+OpenStack', '##### 5.2.6.2. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý TREE của WSNs trên OpenStack\n\n'),
    (133, r'5\.2\.6\.3\.\s+Giải\s+pháp\s+tích\s+hợp,\s+triển\s+khai\s+kiến\s+trúc\s+mạng\s+WSNs.*?trên\s+OpenStack', '##### 5.2.6.3. Giải pháp tích hợp, triển khai kiến trúc mạng WSNs (MESH/TREE) và giao thức định tuyến WSNs (olsr), mô hình giả lập thiết bị WSNs trên OpenStack\n\n'),
    (137, r'5\.3\.\s+Nền\s+tảng\s+điện\s+toán\s+cận\s+biên\s+và\s+ứng\s+dụng\s+trong\s+IoT', '### 5.3. Nền tảng điện toán cận biên và ứng dụng trong IoT\n\n'),
    (137, r'5\.3\.1\.\s+Kiến\s+trúc\s+triển\s+khai\s+điện\s+toán\s+cận\s+biên\s+trong\s+IoT', '#### 5.3.1. Kiến trúc triển khai điện toán cận biên trong IoT\n\n'),
    (138, r'5\.3\.2\.\s+Các\s+công\s+nghệ,\s+kỹ\s+thuật\s+nổi\s+bật\s+cho\s+tính\s+toán\s+cận\s+biên\s+trong\s+IoT', '#### 5.3.2. Các công nghệ, kỹ thuật nổi bật cho tính toán cận biên trong IoT\n\n'),
    (141, r'5\.4\.\s+Các\s+vấn\s+đề\s+tồn\s+tại\s+và\s+hướng\s+nghiên\s+cứu\s+trong\s+tương\s+lai', '### 5.4. Các vấn đề tồn tại và hướng nghiên cứu trong tương lai\n\n'),
    (142, r'BÀI\s+TẬP\s+CHƯƠNG\s+5', '## BÀI TẬP CHƯƠNG 5\n\n'),

    # Chapter 6
    (143, r'CHƯƠNG.*?\n+QUẢN\s+LÝ\s+NGỮ\s+CẢNH.*?\n+', '# CHƯƠNG 6. QUẢN LÝ NGỮ CẢNH THÔNG MINH VÀ TRÍ TUỆ NHÂN TẠO TRONG IOT\n\n'),
    (143, r'6\.1\.\s+Ngữ\s+cảnh\s+và\s+thích\s+ứng\s+ngữ\s+cảnh', '### 6.1. Ngữ cảnh và thích ứng ngữ cảnh\n\n'),
    (145, r'6\.1\.1\.\s+Ngữ\s+cảnh', '#### 6.1.1. Ngữ cảnh\n\n'),
    (148, r'6\.1\.2\.\s+Thích\s+ứng\s+ngữ\s+cảnh', '#### 6.1.2. Thích ứng ngữ cảnh\n\n'),
    (149, r'6\.2\.\s+Quản\s+lý\s+ngữ\s+cảnh\s+trong\s+IoT', '### 6.2. Quản lý ngữ cảnh trong IoT\n\n'),
    (150, r'6\.2\.1\.\s+Thu\s+thập\s+ngữ\s+cảnh', '#### 6.2.1. Thu thập ngữ cảnh\n\n'),
    (150, r'6\.2\.2\.\s+Mô\s+hình\s+hóa\s+ngữ\s+cảnh', '#### 6.2.2. Mô hình hóa ngữ cảnh\n\n'),
    (150, r'6\.2\.3\.\s+Suy\s+luận\s+ngữ\s+cảnh', '#### 6.2.3. Suy luận ngữ cảnh\n\n'),
    (150, r'6\.2\.4\.\s+Phân\s+phối\s+ngữ\s+cảnh', '#### 6.2.4. Phân phối ngữ cảnh\n\n'),
    (151, r'6\.3\.\s+Các\s+kỹ\s+thuật\s+mô\s+hình\s+hóa\s+ngữ\s+cảnh', '### 6.3. Các kỹ thuật mô hình hóa ngữ cảnh\n\n'),
    (151, r'6\.3\.1\.\s+Mô\s+hình\s+khóa/giá\s+trị', '#### 6.3.1. Mô hình khóa/giá trị\n\n'),
    (151, r'6\.3\.2\.\s+Mô\s+hình\s+sơ\s+đồ', '#### 6.3.2. Mô hình sơ đồ\n\n'),
    (152, r'6\.3\.3\.\s+Mô\s+hình\s+đồ\s+họa', '#### 6.3.3. Mô hình đồ họa\n\n'),
    (152, r'6\.3\.4\.\s+Mô\s+hình\s+dựa\s+trên\s+đối\s+tượng', '#### 6.3.4. Mô hình dựa trên đối tượng\n\n'),
    (153, r'6\.3\.5\.\s+Mô\s+hình\s+dựa\s+trên\s+logic', '#### 6.3.5. Mô hình dựa trên logic\n\n'),
    (153, r'6\.3\.6\.\s+Mô\s+hình\s+dựa\s+trên\s+ontology', '#### 6.3.6. Mô hình dựa trên ontology\n\n'),
    (156, r'6\.4\.\s+Các\s+kỹ\s+thuật\s+suy\s+luận\s+ngữ\s+cảnh', '### 6.4. Các kỹ thuật suy luận ngữ cảnh\n\n'),
    (156, r'6\.4\.1\.\s+Học\s+có\s+giám\s+sát', '#### 6.4.1. Học có giám sát\n\n'),
    (157, r'6\.4\.2\.\s+Học\s+không\s+giám\s+sát', '#### 6.4.2. Học không giám sát\n\n'),
    (158, r'6\.4\.3\.\s+Dựa\s+trên\s+luật', '#### 6.4.3. Dựa trên luật\n\n'),
    (158, r'6\.4\.4\.\s+Dựa\s+trên\s+logic\s+mờ', '#### 6.4.4. Dựa trên logic mờ\n\n'),
    (163, r'6\.4\.5\.\s+Dựa\s+trên\s+ontology', '#### 6.4.5. Dựa trên ontology\n\n'),
    (164, r'6\.4\.6\.\s+Dựa\s+trên\s+Logic\s+xác\s+suất', '#### 6.4.6. Dựa trên Logic xác suất\n\n'),
    (168, r'6\.5\.\s+Trí\s+tuệ\s+nhân\s+tạo\s+và\s+IoT', '### 6.5. Trí tuệ nhân tạo và IoT\n\n'),
    (168, r'6\.5\.1\.\s+Học\s+máy', '#### 6.5.1. Học máy\n\n'),
    (168, r'6\.5\.1\.1\.\s+Quá\s+trình\s+xử\s+lý\s+trong\s+học\s+máy', '##### 6.5.1.1. Quá trình xử lý trong học máy\n\n'),
    (171, r'6\.5\.1\.2\.\s+Phân\s+loại\s+các\s+kỹ\s+thuật\s+học\s+máy', '##### 6.5.1.2. Phân loại các kỹ thuật học máy\n\n'),
    (174, r'6\.5\.2\.\s+Ứng\s+dụng\s+của\s+học\s+máy\s+trong\s+IoTs\s+và\s+các\s+định\s+hướng\s+nghiên\s+cứu', '#### 6.5.2. Ứng dụng của học máy trong IoTs và các định hướng nghiên cứu\n\n'),
    (178, r'BÀI\s+TẬP\s+CHƯƠNG\s+6', '## BÀI TẬP CHƯƠNG 6\n\n'),

    # Chapter 7
    (179, r'CHƯƠNG.*?\n+TÁ[lI]\s+CẤU\s+HÌNH.*?\n+', '# CHƯƠNG 7. TÁI CẤU HÌNH TRONG IOT\n\n'),
    (180, r'7\.1\.\s+Tổng\s+quan\s+về\s+tái\s+cấu\s+hình\s+trong\s+IoT', '### 7.1. Tổng quan về tái cấu hình trong IoT\n\n'),
    (181, r'7\.2\.\s+Các\s+hướng\s+tiếp\s+cận\s+trong\s+tái\s+cấu\s+hình\s+IoT', '### 7.2. Các hướng tiếp cận trong tái cấu hình IoT\n\n'),
    (181, r'7\.2\.1\.\s+Hướng\s+tiếp\s+cận\s+thay\s+thế\s+toàn\s+bộ\s+image', '#### 7.2.1. Hướng tiếp cận thay thế toàn bộ image\n\n'),
    (182, r'7\.2\.2\.\s+Hướng\s+tiếp\s+cận\s+dựa\s+trên\s+module', '#### 7.2.2. Hướng tiếp cận dựa trên module\n\n'),
    (183, r'7\.2\.3\.\s+Hướng\s+tiếp\s+cận\s+cơ\s+sở\s+dữ\s+liệu\s+\(database\)', '#### 7.2.3. Hướng tiếp cận cơ sở dữ liệu (database)\n\n'),
    (186, r'7\.2\.4\.\s+Hướng\s+tiếp\s+cận\s+máy\s+ảo\s+\(Virtual\s+Machine\)', '#### 7.2.4. Hướng tiếp cận máy ảo (Virtual Machine)\n\n'),
    (188, r'7\.2\.5\.\s+Hướng\s+tiếp\s+cận\s+hướng\s+tới\s+dịch\s+vụ\s+\(service-oriented\)', '#### 7.2.5. Hướng tiếp cận hướng tới dịch vụ (service-oriented)\n\n'),
    (189, r'7\.3\.\s+Một\s+số\s+giải\s+pháp\s+hiện\s+thực\s+tái\s+cấu\s+hình\s+trên\s+các\s+loại\s+thiết\s+bị\s+phổ\s+biến', '### 7.3. Một số giải pháp hiện thực tái cấu hình trên các loại thiết bị phổ biến\n\n'),
    (189, r'7\.3\.1\.\s+Cơ\s+chế\s+hỗ\s+trợ\s+tái\s+lập\s+trình\s+từ\s+xa\s+trên\s+TinyOS', '#### 7.3.1. Cơ chế hỗ trợ tái lập trình từ xa trên TinyOS\n\n'),
    (192, r'7\.3\.2\.\s+Cơ\s+chế\s+tái\s+lập\s+trình\s+từ\s+xa\s+trên\s+ESP8266', '#### 7.3.2. Cơ chế tái lập trình từ xa trên ESP8266\n\n'),
    (195, r'7\.3\.3\.\s+Cơ\s+chế\s+tái\s+cấu\s+hình\s+từ\s+xa\s+trên\s+Raspberry\s+Pi', '#### 7.3.3. Cơ chế tái cấu hình từ xa trên Raspberry Pi\n\n'),
    (198, r'7\.4\.\s+Khung\s+kiến\s+trúc\s+phát\s+triển\s+một\s+giải\s+pháp\s+tái\s+cấu\s+hình\s+IoT\s+đa\s+nền\s+tảng\s+dựa\s+trên\s+cách\s+tiếp\s+cận\s+SDN', '### 7.4. Khung kiến trúc phát triển một giải pháp tái cấu hình IoT đa nền tảng dựa trên cách tiếp cận SDN\n\n'),
    (198, r'7\.4\.1\.\s+Kiến\s+trúc\s+quản\s+lý\s+hệ\s+thống\s+IoT\s+dựa\s+trên\s+SDN', '#### 7.4.1. Kiến trúc quản lý hệ thống IoT dựa trên SDN\n\n'),
    (200, r'7\.4\.2\.\s+Khung\s+kiến\s+trúc\s+xây\s+dựng\s+giải\s+pháp\s+tái\s+cấu\s+hình\s+IoT', '#### 7.4.2. Khung kiến trúc xây dựng giải pháp tái cấu hình IoT\n\n'),
    (203, r'7\.5\.\s+Ứng\s+dụng\s+của\s+chức\s+năng\s+tái\s+cấu\s+hình\s+trong\s+hệ\s+thống\s+IoT\s+và\s+các\s+định\s+hướng\s+nghiên\s+cứu', '### 7.5. Ứng dụng của chức năng tái cấu hình trong hệ thống IoT và các định hướng nghiên cứu\n\n'),
    (204, r'BÀI\s+TẬP\s+CHƯƠNG\s+7', '## BÀI TẬP CHƯƠNG 7\n\n'),

    # Conclusion & References
    (205, r'K[EÊẼ]T\s+LUẬN', '# KẾT LUẬN\n\n'),
    (209, r'TÀI\s+LIỆU\s+THAM\s+KHẢO', '# TÀI LIỆU THAM KHẢO\n\n'),
]

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(^## Trang \d+\s*$)', text, flags=re.MULTILINE)
pages_dict = {}
for i in range(1, len(parts), 2):
    marker = parts[i]
    p_num = int(re.search(r'\d+', marker).group(0))
    pages_dict[p_num] = parts[i+1]

matched_count = 0
for p_num, pattern, replacement in headings:
    if p_num in pages_dict:
        cur_text = pages_dict[p_num]
        new_text, n = re.subn(pattern, replacement, cur_text, count=1, flags=re.IGNORECASE)
        if n > 0:
            matched_count += 1
            pages_dict[p_num] = new_text

print(f'Total headings matched and formatted: {matched_count} / {len(headings)}')

# Reassemble
out = [parts[0]]
for i in range(1, len(parts), 2):
    marker = parts[i]
    p_num = int(re.search(r'\d+', marker).group(0))
    out.append(marker)
    out.append(pages_dict[p_num])

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'w', encoding='utf-8') as f:
    f.write(''.join(out))

print('Headings formatted successfully!')
