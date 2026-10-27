# Giáo trình Công nghệ Internet of Things và ứng dụng

> OCR từ tài liệu scan `GT IoT-Cong nghe IoT va ung dung.pdf`. Kết quả nhận dạng được đối chiếu và hiệu chỉnh trực tiếp theo từng trang ảnh gốc.

- **Số trang:** 214
- **Nguồn:** `Thamkhao/GT IoT-Cong nghe IoT va ung dung.pdf`

## Trang 1

ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH
TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN

LÊ TRUNG QUÂN - HUỲNH VĂN ĐẶNG - NGUYỄN KHÁNH THUẬT

GIÁO TRÌNH

CÔNG NGHỆ INTERNET OF THINGS VÀ ỨNG DỤNG

NHÀ XUẤT BẢN ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH

## Trang 2

_Không nhận dạng được chữ; xem trang ảnh trong PDF gốc._

## Trang 3

ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH
TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN

TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN

GIÁO TRÌNH

CÔNG NGHỆ INTERNET OF THINGS VÀ ỨNG DỤNG

Lê Trung Quân
Huỳnh Văn Đặng
Nguyễn Khánh Thuật

NHÀ XUẤT BẢN ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH - 2021

## Trang 4

_Không nhận dạng được chữ; xem trang ảnh trong PDF gốc._

## Trang 5

PHẦN MỞ ĐẦU

Trong bối cảnh cuộc cách mạng công nghiệp 4.0 và xã hội đang ngày càng phát triển, công nghệ Internet vạn vật IoTs/5G và kỹ thuật xử lý dữ liệu lớn (Big Data), trí tuệ nhân tạo (AI) đóng vai trò quan trọng trong việc tạo ra những đổi mới đột phá trong công nghệ thông tin (CNTT) và truyền thông, và các lĩnh vực ứng dụng liên quan. Thành phố thông minh (Smart Cities) là một trong những ứng dụng như vậy, đã thu hút được sự chú ý lớn từ các chính phủ, cộng đồng ngành học thuật và CNTT tại nhiều quốc gia. Đặc biệt, Big Data/AI và IoTs/5G cung cấp các công cụ và công nghệ cho phép quan trọng để thúc đẩy Sự chuyển đổi số (Digital Transformation) của các thành phố lớn trên toàn thế giới thành những nơi đáng sống, làm việc và tận hưởng. Các công nghệ IoTs/5G mới, một khi được tích hợp đúng vào cơ sở hạ tầng thành phố thông minh (Smart Cities), có thể hỗ trợ số lượng lớn kết nối không dây từ các loại thiết bị không dây khác nhau (ví dụ: cảm biến, máy ảnh, thiết bị thực tế ảo VR/AR, xe thông minh) thông qua môi trường mạng tốc độ cao, truyền dữ liệu cực kỳ đáng tin cậy và độ trễ thấp. Ngoài ra, các công nghệ IoTs/5G cho phép truyền thông, lưu trữ và xử lý dữ liệu hiệu quả, rất cần thiết để xử lý và phân tích lượng dữ liệu thành phố thông minh khổng lồ và chuyển dữ liệu thu thập được thành các quy trình giám sát, ra quyết định và ứng dụng kịp thời cũng như cung cấp các dịch vụ kỹ thuật số đa phương tiện phong phú đến di động cho người dân thành thị.

Giáo trình này được viết với mục tiêu mang lại những kiến thức nền tảng về công nghệ Internet vạn vật, lĩnh vực ứng dụng và các công nghệ liên quan nhằm cung cấp đến sinh viên các khái niệm mới, tri thức và tiêu chuẩn mới trong lĩnh vực IoTs và các công nghệ liên quan như điện toán đám mây (cloud computing), tính toán cận biên (edge computing), để sinh viên có thể phát triển ứng dụng và giải pháp IoTs hoàn chỉnh.

## Trang 6

Các nền tảng phần cứng được giới thiệu đều có thể dễ dàng tìm thấy ở thị trường Việt Nam với giá thành hợp lý, và dễ dàng làm việc được với các nền tảng phần mềm mã nguồn mở phổ dụng hiện nay được giới thiệu trong giáo trình. Mục tiêu của chúng tôi là nhằm khuyến khích sinh viên có điều kiện phát triển tự thân các ứng dụng và giải pháp IoTs, hoàn toàn làm chủ công nghệ.

Cuốn sách gồm có 8 chương. Chương 1 giới thiệu tổng quan về công nghệ IoTs. Chương 2 trình bày về các lĩnh vực ứng dụng IoTs, trong đó có một số ứng dụng được triển khai trong khuôn viên Trường Đại học Công nghệ Thông tin — Đại học Quốc gia Tp.HCM. Chương 3 trình bày về các bộ giao thức mạng IoTs. Chương 4 trình bày về các nền tảng phần cứng và phần mềm mã nguồn mở IoTs phổ dụng. Chương 5 giới thiệu về các nền tảng điện toán đám mây (cloud computing), tính toán cận biên (edge computing), cũng như khả năng phối hợp với công nghệ IoTs trong kiến trúc N-Tier để phát triển các giải pháp và ứng dụng IoTs. Kiến trúc mạng do chúng tôi phát triển IoTs network testbed được giới thiệu để minh họa. Chương 6 trình bày về quản lý ngữ cảnh thông minh trong các ứng dụng và giải pháp IoTs thông minh. Chương 7 trình bày về giải pháp tái cấu hình từ xa qua mạng không dây thiết bị và giao thức IoTs. Cuối cùng là phần Kết luận và tóm tắt lại nội dung được trình bày trong cuốn sách này.

CÁC TÁC GIẢ

## Trang 7

# MỤC LỤC

PHẦN MỞ ĐẦU .......................................................................... iii
DANH MỤC HÌNH ẢNH ............................................................. xi
DANH MỤC BẢNG BIỂU ........................................................... xvi
CÁC KÝ HIỆU VIẾT TẮT ......................................................... xviii

CHƯƠNG 1. GIỚI THIỆU ........................................................... 1
1.1. Tổng quan về công nghệ Internet vạn vật ................................. 1
1.2. Xu thế ứng dụng IoTs và các công nghệ liên quan cho đô thị thông minh ở Việt Nam ... 9
BÀI TẬP CHƯƠNG 1 ................................................................. 11

CHƯƠNG 2. CÁC LĨNH VỰC ỨNG DỤNG IOT ......................... 12
2.1. Nhà thông minh (Smart Home) ............................................ 13
2.2. Đô thị thông minh (Smart City) ............................................ 16
  2.2.1. Kiến trúc tổng quát ........................................................ 19
  2.2.2. Giao thông thông minh ................................................... 22
  2.2.3. Môi trường thông minh .................................................. 23
  2.2.4. Cuộc sống thông minh .................................................... 24
  2.2.5. Một số dự án thành phố thông minh ................................. 24
2.3. Nông nghiệp thông minh (Smart Agriculture) ....................... 29
BÀI TẬP CHƯƠNG 2 ................................................................. 31

CHƯƠNG 3. CÁC KIẾN TRÚC MẠNG VÀ BỘ GIAO THỨC MẠNG IOT ... 32
3.1. Các kiến trúc mạng dùng trong IoT ...................................... 33
  3.1.1. Một số kiến trúc mạng đơn giản ..................................... 33
  3.1.2. Một số kiến trúc mạng phức tạp ...................................... 36
3.2. Các bộ giao thức mạng không dây thường dùng trong IoT ..... 39
  3.2.1. Bộ giao thức 6LoWPAN .................................................. 39

## Trang 8

    3.2.1.1. Kiến trúc mạng 6LoWPAN ....................................... 40
    3.2.1.2. Mô hình phân lớp các tầng giao thức trong 6LoWPAN ... 41
    3.2.1.3. Cấu trúc gói tin của chuẩn mạng 6LoWPAN ............... 43
    3.2.1.4. Nền tảng hiện thực bộ giao thức 6LoWPAN ............... 44
  3.2.2. Bộ giao thức Zigbee ...................................................... 45
    3.2.2.1. Kiến trúc mạng Zigbee ............................................ 45
    3.2.2.2. Mô hình phân lớp các tầng giao thức trong chuẩn không dây Zigbee ... 46
    3.2.2.3. Cấu trúc frame của chuẩn 802.15.4 ........................... 48
    3.2.2.4. Một số đặc điểm của chuẩn Zigbee trong ứng dụng mạng cảm biến không dây ... 50
    3.2.2.5. Nền tảng hiện thực bộ giao thức mạng Zigbee ............. 53
  3.2.3. Bộ giao thức WiFi 802.11 .............................................. 54
    3.2.3.1. Kiến trúc mạng WiFi 802.11 ...................................... 54
    3.2.3.2. Mô hình phân lớp tầng giao thức trong chuẩn không dây 802.11 ... 55
    3.2.3.3. Cấu trúc frame của chuẩn không dây 802.11 ............... 56
    3.2.3.4. Một số chuẩn con của 802.11 ................................... 57
    3.2.3.5. Nền tảng hiện thực bộ giao thức mạng WiFi .............. 61
BÀI TẬP CHƯƠNG 3 ................................................................. 61

CHƯƠNG 4. CÁC NỀN TẢNG PHẦN CỨNG VÀ PHẦN MỀM IOT THÔNG DỤNG ... 63
4.1. Các nền tảng phần cứng .................................................... 64
  4.1.1. Những đặc trưng và phân loại các nền tảng phần cứng dùng cho IoT ... 64
  4.1.2. Thiết bị cảm biến không dây TelosB ............................... 66
  4.1.3. Thiết bị nhúng Arduino ................................................. 66
  4.1.4. Thiết bị máy tính nhúng Raspberry Pi ............................. 68
  4.1.5. Tổng hợp một số nền tảng phần cứng IoT phổ biến ......... 70

## Trang 9

4.2. Các nền tảng phần mềm dùng trong IoT .............................. 71
  4.2.1. Những đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT ... 71
  4.2.2. Hệ điều hành TinyOS .................................................... 73
    4.2.2.1. Cấu trúc một ứng dụng trên TinyOS .......................... 73
    4.2.2.2. Các thành phần, dịch vụ cơ bản của TinyOS ............... 76
  4.2.3. Hệ điều hành Contiki ................................................... 83
    4.2.3.1. Cấu trúc một ứng dụng trên Contiki .......................... 84
    4.2.3.2. Các thành phần, dịch vụ cơ bản trên hệ điều hành Contiki ... 85
  4.2.4. Hệ điều hành Raspbian OS ........................................... 88
  4.2.5. Tổng hợp một số nền tảng phần mềm IoT phổ biến ......... 91
BÀI TẬP CHƯƠNG 4 ................................................................. 94

CHƯƠNG 5. ĐIỆN TOÁN ĐÁM MÂY, ĐIỆN TOÁN CẬN BIÊN VÀ IOT ... 96
5.1. Kiến trúc tổng quan hệ thống IoT tích hợp điện toán đám mây và điện toán cận biên ... 97
  5.1.1. Kiến trúc tổng quan ..................................................... 97
  5.1.2. Các yêu cầu và đặc trưng cơ bản của các hệ thống tính toán cho IoT ... 99
5.2. Nền tảng điện toán đám mây và ứng dụng trong IoT .......... 100
  5.2.1. Đặc trưng cơ bản của điện toán đám mây ....................... 101
  5.2.2. Lợi ích của điện toán đám mây ..................................... 102
  5.2.3. Mô hình IaaS .............................................................. 104
  5.2.4. Mô hình PaaS .............................................................. 106
  5.2.5. Mô hình SaaS .............................................................. 107
  5.2.6. Ứng dụng công nghệ điện toán đám mây trong xây dựng hệ thống giả lập WSN với số lượng nút lớn ... 109

## Trang 10

    5.2.6.1. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý MESH của WSNs trên OpenStack ... 111
    5.2.6.2. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý TREE của WSNs trên OpenStack ... 112
    5.2.6.3. Giải pháp tích hợp, triển khai kiến trúc mạng WSNs (MESH/TREE) và giao thức định tuyến WSNs (olsr), mô hình giả lập thiết bị WSNs trên OpenStack ... 113
5.3. Nền tảng điện toán cận biên và ứng dụng trong IoT ............ 117
  5.3.1. Kiến trúc triển khai điện toán cận biên trong IoT .......... 117
  5.3.2. Các công nghệ, kỹ thuật nổi bật cho tính toán cận biên trong IoT ... 118
5.4. Các vấn đề tồn tại và hướng nghiên cứu trong tương lai .... 121
BÀI TẬP CHƯƠNG 5 ............................................................... 122

CHƯƠNG 6. QUẢN LÝ NGỮ CẢNH THÔNG MINH VÀ TRÍ TUỆ NHÂN TẠO TRONG IOT ... 123
6.1. Ngữ cảnh và thích ứng ngữ cảnh ....................................... 123
  6.1.1. Ngữ cảnh ................................................................... 125
  6.1.2. Thích ứng ngữ cảnh ...................................................... 128
6.2. Quản lý ngữ cảnh trong IoT ............................................ 129
  6.2.1. Thu thập ngữ cảnh ...................................................... 130
  6.2.2. Mô hình hóa ngữ cảnh ................................................. 130
  6.2.3. Suy luận ngữ cảnh ....................................................... 130
  6.2.4. Phân phối ngữ cảnh .................................................... 130
6.3. Các kỹ thuật mô hình hóa ngữ cảnh .................................. 131
  6.3.1. Mô hình khóa/giá trị .................................................. 131
  6.3.2. Mô hình sơ đồ ............................................................ 131
  6.3.3. Mô hình đồ họa .......................................................... 132
  6.3.4. Mô hình dựa trên đối tượng ......................................... 132

## Trang 11

  6.3.5. Mô hình dựa trên logic ............................................... 133
  6.3.6. Mô hình dựa trên ontology .......................................... 133
6.4. Các kỹ thuật suy luận ngữ cảnh ........................................ 136
  6.4.1. Học có giám sát ......................................................... 136
  6.4.2. Học không giám sát .................................................... 137
  6.4.3. Dựa trên luật ............................................................. 138
  6.4.4. Dựa trên logic mờ ...................................................... 138
  6.4.5. Dựa trên ontology ..................................................... 143
  6.4.6. Dựa trên Logic xác suất .............................................. 144
6.5. Trí tuệ nhân tạo và IoT .................................................... 148
  6.5.1. Học máy ................................................................... 148
    6.5.1.1. Quá trình xử lý trong học máy ................................. 148
    6.5.1.2. Phân loại các kỹ thuật học máy ............................... 151
  6.5.2. Ứng dụng của học máy trong IoTs và các định hướng nghiên cứu ... 154
BÀI TẬP CHƯƠNG 6 ............................................................... 158

CHƯƠNG 7. TÁI CẤU HÌNH TRONG IOT ................................. 159
7.1. Tổng quan về tái cấu hình trong IoT ................................. 160
7.2. Các hướng tiếp cận trong tái cấu hình IoT ......................... 161
  7.2.1. Hướng tiếp cận thay thế toàn bộ image .......................... 161
  7.2.2. Hướng tiếp cận dựa trên module ................................... 162
  7.2.3. Hướng tiếp cận cơ sở dữ liệu (database) ........................ 163
  7.2.4. Hướng tiếp cận máy ảo (Virtual Machine) ...................... 166
  7.2.5. Hướng tiếp cận hướng tới dịch vụ (service-oriented) ..... 168
7.3. Một số giải pháp hiện thực tái cấu hình trên các loại thiết bị phổ biến ... 169
  7.3.1. Cơ chế hỗ trợ tái lập trình từ xa trên TinyOS ................. 169
  7.3.2. Cơ chế tái lập trình từ xa trên ESP8266 ........................ 172
  7.3.3. Cơ chế tái cấu hình từ xa trên Raspberry Pi .................. 175

## Trang 12

7.4. Khung kiến trúc phát triển một giải pháp tái cấu hình IoT đa nền tảng dựa trên cách tiếp cận SDN ... 178
  7.4.1. Kiến trúc quản lý hệ thống IoT dựa trên SDN ............... 178
  7.4.2. Khung kiến trúc xây dựng giải pháp tái cấu hình IoT ..... 180
7.5. Ứng dụng của chức năng tái cấu hình trong hệ thống IoT và các định hướng nghiên cứu ... 183
BÀI TẬP CHƯƠNG 7 ............................................................... 184

KẾT LUẬN ............................................................................. 185
TÀI LIỆU THAM KHẢO ........................................................... 189

## Trang 13

# DANH MỤC HÌNH ẢNH

Hình 1.1. Số liệu minh họa số lượng thiết bị IoT cho đến năm 2020 ........................................ 3
Hình 1.2. Lược đồ quy chuẩn kỹ thuật của OIC ................................................................... 5
Hình 1.3. Kiến trúc mạng tổng quan của một ứng dụng cloud-based IoT ................................... 7
Hình 1.4. Các ứng dụng điển hình IoT/5G trong đô thị thông minh ........................................... 8
Hình 2.1. Phân loại ứng dụng Internet of Things .................................................................. 13
Hình 2.2. Ví dụ về Giao diện của Hệ thống giám sát trong Nhà thông minh .............................. 14
Hình 2.3. Ví dụ về Giao diện của Hệ thống điều khiển trong Nhà thông minh ............................ 15
Hình 2.4. Các thiết bị trong Smart Home ............................................................................ 16
Hình 2.5. Kiến trúc tổng thể của Thành phố thông minh ....................................................... 17
Hình 2.6. Các thành phần trong Thành phố thông minh ....................................................... 18
Hình 2.7. Giao diện điều khiển của Trạm quan trắc môi trường tại ĐH Công nghệ Thông tin .... 18
Hình 2.8. Kiến trúc tổng quát của Smart City ...................................................................... 19
Hình 2.9. Kiến trúc mạng phổ biến trong City Layer ............................................................ 21
Hình 2.10. Các ứng dụng trong Giao thông thông minh ........................................................ 22
Hình 2.11. Kiến trúc của một hệ thống Dự báo chất lượng không khí ...................................... 24
Hình 2.12. Các đặc điểm của Thành phố thông minh tại Amsterdam ...................................... 26
Hình 2.13. Chương trình trong dự án Thành phố thông minh tại Barcelona ............................ 27

## Trang 14

Hình 2.14. Kiến trúc của Chính quyền thành phố trong dự án Thành phố thông minh của Barcelona ... 28
Hình 2.15. Chiến lược thành phố thông minh của Copenhagen ............................................... 29
Hình 2.16. Kiến trúc của một ứng dụng Nông nghiệp thông minh ........................................... 30
Hình 3.1. Kiến trúc Full Mesh ............................................................................................ 33
Hình 3.2. Kiến trúc Partial Mesh ......................................................................................... 33
Hình 3.3. Kiến trúc Tree .................................................................................................... 34
Hình 3.4. Kiến trúc Ring .................................................................................................... 34
Hình 3.5. Kiến trúc chuỗi ................................................................................................... 35
Hình 3.6. Star Topology .................................................................................................... 35
Hình 3.7. Kiến trúc lưới ..................................................................................................... 36
Hình 3.8. Kiến trúc dựa theo cụm (cluster-based) ................................................................ 37
Hình 3.9. Kiến trúc Tributary Delta ..................................................................................... 37
Hình 3.10. Kiến trúc dựa theo làn sóng ................................................................................ 38
Hình 3.11. Kiến trúc mạng 6LoWPAN [3] ............................................................................ 40
Hình 3.12. Mô hình phân lớp 6LoWPAN Stack .................................................................... 41
Hình 3.13. Minh họa cấu trúc phần đầu gói tin IPv6 trong 6LoWPAN ..................................... 43
Hình 3.14. Cách bố trí các header để truyền dữ liệu trong mạng 6LoWPAN ........................... 44
Hình 3.15. Mô hình truyền dẫn mạng Zigbee ....................................................................... 45
Hình 3.16. Các chồng giao thức tham chiếu giữa 802.15.4 và Zigbee ...................................... 46
Hình 3.17. Cấu trúc frame của chuẩn 802.15.4 .................................................................... 47
Hình 3.18. Cấu trúc superframe của 802.15.4 ...................................................................... 48
Hình 3.19. Data Frame trong chuẩn 802.15.4 ...................................................................... 49

## Trang 15

Hình 3.20. Minh họa mạng 802.11 theo kiến trúc hạ tầng ...................................................... 54
Hình 3.21. Minh họa mạng 802.11 theo kiến trúc Ad-hoc ...................................................... 54
Hình 3.22. Ánh xạ 802.11 trong mô hình OSI 7 tầng ............................................................ 55
Hình 3.23. Các giao thức sử dụng trong hệ thống mạng cục bộ không dây dựa trên chuẩn IEEE 802.11 của tầng vật lý (PHY layer) và tầng con điều khiển truy cập môi trường truyền (MAC layer) ... 56
Hình 3.24. Cấu trúc Media Access Control (MAC) frame trong chuẩn không dây 802.11 ........ 56
Hình 4.1. Phân loại một số thiết bị phần cứng IoT phổ biến ................................................. 65
Hình 4.2. Thiết bị TelosB ................................................................................................... 66
Hình 4.3. Thiết bị Arduino UNO ......................................................................................... 66
Hình 4.4. Mạch WiFi ESP8266 ........................................................................................... 67
Hình 4.5. Thiết bị Raspberry Pi 2 ........................................................................................ 68
Hình 4.6. Thiết bị Raspberry Pi 4 Model B .......................................................................... 72
Hình 4.7. Các thành phần chính của một hệ điều hành cho thiết bị IoT ................................. 73
Hình 4.8. Các thành phần trong một ứng dụng trên TinyOS .................................................. 74
Hình 4.9. Cấu trúc của một gói tin message_t .................................................................... 77
Hình 4.10. Kiến trúc lớp trong CC2420 Radio Stack ............................................................. 82
Hình 4.11. Sơ đồ các cơ chế giao tiếp trên Contiki .............................................................. 88
Hình 4.12. Kiến trúc hệ điều hành Raspbian OS ................................................................... 89
Hình 5.1. Kiến trúc tổng quan phân lớp Edge, Fog và Cloud trong IoT ................................... 97
Hình 5.2. Các mô hình dịch vụ điện toán đám mây và các thành phần cấu tạo ...................... 104

## Trang 16

Hình 5.3. Kiến trúc mô hình IaaS ...................................................................................... 104
Hình 5.4. Minh họa kỹ thuật ảo hóa dựa trên máy ảo (VM) ................................................. 105
Hình 5.5. Kiến trúc mô hình dịch vụ PaaS .......................................................................... 106
Hình 5.6. Kiến trúc mô hình dịch vụ SaaS .......................................................................... 108
Hình 5.7. Mô hình triển khai ảo hóa lớp với OpenStack ....................................................... 109
Hình 5.8. Tổng quan quá trình xây dựng và triển khai ảnh lên hệ thống mạng thử nghiệm WSN ... 110
Hình 5.9. Minh họa triển khai kiến trúc mạng Mesh với nền tảng Docker Container .............. 112
Hình 5.10. Minh họa triển khai kiến trúc mạng Tree với nền tảng Docker Container ............. 113
Hình 5.11. Minh họa triển khai kiến trúc mạng Tree với nền tảng Docker Container .............. 116
Hình 5.12. Kiến trúc triển khai tính toán cận biên trong IoT ................................................ 117
Hình 5.13. Các công nghệ tính toán cận biên cho hệ thống IoT phân tán .............................. 119
Hình 6.1. Ứng dụng Smart Lighting ................................................................................... 128
Hình 6.2. Vòng đời ngữ cảnh ............................................................................................ 130
Hình 6.3. Thông tin liên quan đến IoT Node được xây dựng từ ontology .............................. 134
Hình 6.4. Sơ đồ fuzzy logic điều khiển nhiệt độ ................................................................. 139
Hình 6.5. Mô phỏng điều khiển nhiệt độ Trường hợp 1 ........................................................ 142
Hình 6.6. Mô phỏng điều khiển nhiệt độ Trường hợp 2 ........................................................ 142
Hình 6.7. Mô phỏng điều khiển nhiệt độ Trường hợp 3 ........................................................ 143
Hình 6.8. Quan hệ giữa Trí tuệ nhân tạo, Học máy và Học sâu ............................................. 147
Hình 6.9. Quá trình xử lý trong học máy ........................................................................... 150

## Trang 17

Hình 6.10. Các kỹ thuật trong học máy ............................................................................. 151
Hình 6.11. Minh họa kết quả của quá trình phân lớp bằng kỹ thuật SVM .............................. 152
Hình 6.12. Ví dụ về Học không giám sát ............................................................................ 153
Hình 6.13. Hoạt động của học tăng cường ......................................................................... 153
Hình 7.1. Sơ đồ trạng thái của Deluge ............................................................................... 162
Hình 7.2. Tổ chức vùng nhớ ROM/RAM trên Contiki .......................................................... 163
Hình 7.3. Câu lệnh truy vấn và kết quả được truyền đi trong mạng ...................................... 164
Hình 7.4. Kiến trúc tổng quan cơ chế pub/sub .................................................................... 166
Hình 7.5. Kiến trúc mạng pub/sub ..................................................................................... 166
Hình 7.6. Kiến trúc nút MATE ........................................................................................... 167
Hình 7.7. Kích thước mã nguồn các thành phần trong nút MATE ......................................... 167
Hình 7.8. Mô hình tổng quan MOSDEN ............................................................................. 169
Hình 7.9. Biểu diễn gói dữ liệu trên Deluge ....................................................................... 170
Hình 7.10. Quá trình thay thế một sketch trên vùng nhớ của ESP8266 ................................ 172
Hình 7.11. Giải pháp cải tiến tái lập trình từ xa qua mạng trên ESP8266 ............................. 174
Hình 7.12. Mô hình tái cấu hình OTA cho thiết bị Raspberry Pi bằng Mender ...................... 176
Hình 7.13. So sánh kiến trúc Docker và VM ....................................................................... 177
Hình 7.14. Công nghệ SDN dùng trong kiến trúc hệ thống IoT ............................................ 178
Hình 7.15. Kiến trúc nền tảng SD-IoTR đề xuất ................................................................. 180
Hình 8.1. Kiến trúc phần cứng IoT ứng dụng Học sâu ........................................................ 188

## Trang 18

# DANH MỤC BẢNG BIỂU

Bảng 3.1. Một số nền tảng phần cứng hỗ trợ chuẩn 6LoWPAN ............................................ 44
Bảng 3.2. Một số nền tảng phần mềm hỗ trợ bộ giao thức 6LoWPAN ................................... 44
Bảng 3.3. Một số nền tảng phần cứng hỗ trợ chuẩn Zigbee ................................................... 53
Bảng 3.4. Một số nền tảng phần mềm hỗ trợ bộ giao thức Zigbee ........................................ 53
Bảng 3.5. Bảng chức năng của trạm phát dựa theo bit "To DS" và "From DS" ...................... 57
Bảng 3.6. Một số nền tảng phần cứng hỗ trợ chuẩn WiFi ..................................................... 61
Bảng 3.7. Một số nền tảng phần mềm hỗ trợ bộ giao thức WiFi ........................................... 61
Bảng 4.1. Tổng hợp 3 nền tảng phần cứng IoT đặc trưng ..................................................... 70
Bảng 4.2. Bảng tổng hợp đặc tính một số nền tảng hệ điều hành nổi tiếng trong IoT ........... 91
Bảng 4.3. Bảng tổng hợp đặc tính kỹ thuật một số nền tảng hệ điều hành nổi tiếng trong IoT ... 92
Bảng 5.1. Tóm lược một số APIs OpenStack ..................................................................... 114
Bảng 6.1. Quy đổi giá trị và mức nhiệt độ ......................................................................... 127
Bảng 6.2. Sensed-context và Learned-context ................................................................... 127
Bảng 6.3. Luật suy luận Learned-context .......................................................................... 127
Bảng 6.4. So sánh các hướng tiếp cận trong mô hình hóa ngữ cảnh ..................................... 134
Bảng 6.5. Bảng biểu diễn thang input nhiệt độ ................................................................... 140
Bảng 6.6. Bảng biểu diễn thang giá trị input trade (hướng đi của dữ liệu) ........................... 140

## Trang 19

Bảng 6.7. Bảng biểu diễn output cho điều khiển nhiệt độ ................................................... 140
Bảng 6.8. Bảng dữ liệu nhiệt độ đầu vào ........................................................................... 141
Bảng 6.9. So sánh các hướng tiếp cận trong suy luận ngữ cảnh ........................................... 144

## Trang 20

# CÁC KÝ HIỆU VIẾT TẮT

| Viết tắt | Tên đầy đủ tiếng Anh |
| :--- | :--- |
| **6LoWPAN** | IPv6 over Low-Power Wireless Personal Area Networks |
| **AI** | Artificial Intelligence |
| **CPS** | Cyber-Physical Systems (hoặc Chip Package System) |
| **CPU** | Central Processing Unit |
| **GPU** | Graphics Processing Unit |
| **HTTP** | HyperText Transfer Protocol |
| **ICT** | Information & Communication Technologies |
| **IoT / IoTs** | Internet of Things |
| **MQTT** | Message Queuing Telemetry Transport |
| **NFV** | Network Function Virtualization |
| **OIC** | Open InterConnect Consortium |
| **OTAP** | Over The Air Programming |
| **REST** | Representational State Transfer |
| **SDN** | Software Defined Network |
| **TPU** | Tensor Processing Unit |
| **VM** | Virtual Machine |

## Trang 21

# CHƯƠNG 1. GIỚI THIỆU

### 1.1. Tổng quan về công nghệ Internet vạn vật

Thế giới hiện có khoảng 20 tỷ thiết bị kết nối Internet và đang tăng trung bình 80 thiết bị mới mỗi giây. Tốc độ tăng này sẽ đạt 50 tỷ thiết bị vào năm 2020 [1]. Đây là một trong những thống kê của Cisco về viễn cảnh “Internet của vạn vật” (Internet of Things - IoTs) [2]. Công nghệ mạng Internet of Things (IoTs) hiện đang được phát triển để mọi thiết bị, đồ vật... đều có thể kết nối và tương tác với nhau, giúp chúng ta có thể tra cứu thông tin về thực phẩm ngay trên tủ lạnh, điều khiển ôtô từ xa mà không cần trực tiếp lái xe, hoặc 4-5 triệu xe máy ở Hà Nội, hoặc Tp.HCM được tích hợp cảm biến để nhà quản lý dễ dàng kiểm soát lưu lượng giao thông. Hình 1.1 dưới đây cung cấp các số liệu minh họa.

Hình 1.1. Số liệu minh họa số lượng thiết bị IoTs cho đến năm 2020 (Nguồn: Cisco IBSG)

Một thế giới kết nối, hay “Internet của vạn vật” (Internet of Things - IoTs), sẽ mang lại giá trị kinh tế lớn. Tuy nhiên, hiện mới chỉ có khoảng 1% thiết bị được kết nối trên toàn cầu. Báo cáo của Cisco trình bày “Internet của vạn vật” đã mang lại 613 tỷ USD lợi nhuận trong năm 2013 và những công ty tối ưu hóa

## Trang 22

Một thế giới kết nối, hay “Internet của vạn vật” (Internet of Things - IoTs), sẽ mang lại giá trị kinh tế lớn. Tuy nhiên, hiện mới chỉ có khoảng 1% thiết bị được kết nối trên toàn cầu. Báo cáo của Cisco trình bày “Internet của vạn vật” đã mang lại 613 tỷ USD lợi nhuận trong năm 2013 và những công ty tối ưu hóa được các kết nối giữa con người, quá trình, dữ liệu hoặc mọi vật sẽ sinh lời ở mức lớn nhất trong tương lai. Intel, đơn vị mới tham gia vào thị trường sản xuất chip cho các thiết bị thông minh phục vụ IoT cũng đã thu về hơn 2 tỷ USD trong năm 2014 từ lĩnh vực này, tăng trưởng 19% so với năm 2013 [3]. “Internet của vạn vật có tiềm năng thay đổi đáng kể bộ mặt nền kinh tế của chúng ta và chuyển đổi những ngành công nghiệp chủ chốt”, Rob Lloyd, chuyên gia của Cisco, nhận định. “Câu hỏi đặt ra là ai sẽ là người dẫn đầu và chiến thắng trong nền kinh tế mới này. Thành công không phụ thuộc vào vị trí địa lý hay quy mô của công ty mà phụ thuộc vào yếu tố: ai là người có thể thích ứng nhanh nhất”. Nghiên cứu mới cũng cho thấy các nhà lãnh đạo doanh nghiệp cũng tin tưởng rằng Internet của vạn vật - nơi mọi thứ tương tác với nhau - sẽ giúp thúc đẩy an toàn thông tin tốt hơn.

Ủy ban quản lý nghiên cứu Âu châu về ICT, trong chương trình FP7 về chuyên ngành “Internet of Things and Future Internet Enterprise Systems” [4] đã thông báo sẽ tiếp tục hỗ trợ kinh phí và điều phối nghiên cứu việc phát triển các công nghệ liên quan đến Internet of Things and Future Internet Enterprise System. Ủy ban quản lý nghiên cứu Âu châu khởi đầu với thông báo hỗ trợ kinh phí cho các dự án nghiên cứu về Internet of Things trong Call 5 of FP7-ICT (2009-2010 Work Program) [5], Call 7 (2011-2012 Work Program) [6], và trong giai đoạn từ 2015-2020 là Horizon-2020/ICT-30-2015 [7]. Hướng nghiên cứu trọng điểm tập trung vào Internet của vạn vật và các nền tảng để kết

---
[3] http://www.techz.vn/internet-of-things-la-gi-tai-sao-no-se-la-xu-huong-cua-tuong-lai-qv1-ylt41541.html  
[4] http://cordis.europa.eu/fp7/ict/enet/home2_en.html  
[5] http://cordis.europa.eu/fp7/ict/enet/d4-20101008-infoday_en.html  
[6] http://ec.europa.eu/research/participants/portal/desktop/en/opportunities/h2020/topics/9091-ict-30-2015.html  

## Trang 23

nối các thiết bị thông minh (Internet of Things and Platforms for Connected Smart Objects), bao gồm quản lý các thiết bị hỗn hợp (sensor, RFID, actuator), quản lý người dùng, quản lý mạng, bảo mật hệ thống mạng. Vì vậy, vấn đề phát triển các ứng dụng thông minh IoT phục vụ đời sống sử dụng các công nghệ IoT mới đã và đang là một trong những vấn đề trọng điểm cần nghiên cứu trong các chương trình nghiên cứu ICT hiện nay của Âu châu. Tương tự, tại các nước lớn và phát triển khác trên thế giới, ví dụ như Mỹ, Nhật Bản, hay Trung Quốc, đều đã và đang triển khai các chương trình nghiên cứu quốc gia khác nhau về lĩnh vực Internet of Things [8, 9, 10, 11].

Trong việc phát triển các ứng dụng IoT và các giải pháp IoT phục vụ xây dựng ứng dụng IoT thông minh, do sự đa dạng của các chuẩn IoT hiện nay và thường xuyên có những tiêu chuẩn mới xuất hiện, chúng tôi hướng tới việc phát triển các ứng dụng và giải pháp IoT sẽ tuân thủ nghiêm ngặt các quy định, quy trình trong các tổ chức quốc tế có uy tín, để tăng sự tương thích và portability. Một số bộ tiêu chuẩn, quy tắc có thể liệt kê dưới đây:

**Open InterConnect Consortium (OIC)** [12]: Hiệp hội kết nối mở OIC là một tổ chức phi lợi nhuận ở bang Oregon (Mỹ), được thành lập bởi các công ty công nghệ hàng đầu như Intel, Samsung, Dell, Atmel, Broadcom và Wind River, với mục tiêu xác định các yêu cầu kết nối và đảm bảo khả năng tương tác của hàng tỷ thiết bị tạo nên “Internet của vạn vật” (Internet of Things - IoT). Bên cạnh đó, OIC dự định cung cấp các chỉ dẫn kỹ thuật, bổ sung mã nguồn mở và chương trình chứng nhận (certification program) cho

---
[8] http://www.nsf.gov/funding/pgm_summ.jsp?pims_id=504949  
[9] IT Strategic Headquarters, “i-Japan Strategy 2015”, http://www.kantei.go.jp/foreign/policy/it/i-JapanStrategy.pdf  
[10] The Ministry of Industry and Information Technology, “The 12th Five-Year Plan for the Internet of Things”, 2012.  
[11] http://www.chinadaily.com.cn/bizchina/2010-04/09/content_9706692.htm  
[12] http://openinterconnect.org/  

## Trang 24

các thiết bị kết nối không dây. Hình 1.2 dưới đây trình bày lược đồ quy chuẩn kỹ thuật của OIC.

**AllSeen Alliance** [13]: gồm các công ty công nghệ như Haier, LG Electronics, Panasonic, Qualcomm, Sharp, Technicolor, Silicon Image và TP-LINK. Liên minh này đã có đến 51 thành viên bao gồm Microsoft cùng phối hợp với dự án nguồn mở AllJoyn của Qualcomm để triển khai khung hạ tầng nền IoT đầu tiên.

Ngoài ra, còn rất nhiều các chuẩn kỹ thuật, công nghệ và dự án nghiên cứu liên quan đến Internet of Things đã và đang được phát triển bởi các tổ chức quốc tế có uy tín khác, ví dụ:
- IEEE 802.15.4 [14] cho mạng cảm biến không dây (Wireless Sensor Networks - WSNs).
- IETF CoAP (Constrained Application Protocol) [15].
- Zigbee Alliance [16], Bluetooth Smart [17].
- W3C Semantic Sensor Networks [18].
- Open Geospatial Consortium (OGC) Sensor Web Enablement (SWE) [19] và CityGML [20].

---
[13] https://allseenalliance.org  
[14] IEEE 802.15 WPAN Task Group 4 (TG4), http://www.ieee802.org/15/pub/TG4.html  
[15] IETF CoRE Working Group, http://datatracker.ietf.org/wg/core/charter/  
[16] http://www.zigbee.org/  
[17] http://www.bluetooth.com/Pages/Bluetooth-Smart.aspx  
[18] W3C Semantic Sensor Network Incubator Group, http://www.w3.org/2005/Incubator/ssn/  
[19] http://www.opengeospatial.org/domain/swe  
[20] http://www.opengeospatial.org/standards/citygml  

## Trang 25

- European Sensor Network Architecture (ESNA) [21]
- IETF 6LoWPAN [22], uIP / uIPv6

Hình 1.2. Lược đồ quy chuẩn kỹ thuật của OIC (Nguồn: OIC)

Tốc độ tăng trưởng nhanh chóng của Internet of Things hiện nay cũng đem đến nhiều thách thức lớn. Số lượng các thiết bị được tạo ra nhiều bao nhiêu thì sự mong đợi của khách hàng cho các kết nối, hiệu suất năng lượng, tính tin cậy, dễ sử dụng và kết cấu sẽ càng tăng cao. Các thiết bị điện tử không chỉ phải được cải tiến để đem lại hiệu năng cao mà còn phải có tính hấp dẫn. Và tất nhiên, tất cả các tính năng vượt trội và hình thức bắt mắt đó phải đi cùng với giá cả hợp lý. Dưới đây là một số đặc điểm kỹ thuật cần xem xét:

**Phần mềm:** Trong quy trình phức tạp của việc thiết kế và đóng gói một hệ thống IoT, phần mềm thực sự đóng vai trò quan trọng qua việc hỗ trợ đầy đủ cho toàn bộ vòng đời phát

---
[21] European Sensor Network Architecture (ESNA): http://www.it.lut.fi/project/esna/  
[22] IETF 6LoWPAN Working Group: http://datatracker.ietf.org/wg/6lowpan/charter/  

## Trang 26

triển của sản phẩm. Cụ thể, phần mềm có thể hỗ trợ một cách hoàn thiện cho chu trình thiết kế các thiết bị công nghệ cao, bao gồm mạch tích hợp (ICs) và phần mềm nhúng. Những giải pháp phần mềm góp phần giải quyết các thách thức lớn cho các nhà thiết kế công nghệ cao: cải thiện tốc độ và băng thông, tối ưu công suất và hiệu năng, tối ưu đặc tính ăng-ten, và kết hợp các vật liệu tiên tiến. Ngoài ra, để hoàn toàn làm chủ công nghệ và gia tăng tính bảo mật của hệ thống, chúng tôi hướng tới lựa chọn các thiết bị IoT được phát triển và hỗ trợ bởi các nền tảng phần mềm mã nguồn mở thông dụng, và được chứng nhận hoặc kiểm định bởi các tổ chức IoT quốc tế có uy tín.

**Tăng tốc độ và mở rộng băng thông:** Do số lượng các thiết bị di động, thiết bị IoT ngày một tăng nhanh nên ngày càng nhiều dữ liệu được truyền và nhận, việc truyền tải chúng cần nhanh hơn trên cả mạng truyền thông có dây và không dây. Luồng video, tương tác chơi game và dịch vụ web tốc độ cao đang đẩy đến giới hạn không chỉ trên các thiết bị di động, thiết bị IoT, mà còn trên các máy chủ, bộ định tuyến và cổng chia.

**Tối ưu năng lượng và hiệu suất:** Một vấn đề không kém phần quan trọng trong công nghiệp công nghệ cao là quản lý năng lượng một cách hiệu quả. Để giúp giải quyết vấn đề này, các thiết bị IoT được lựa chọn phục vụ nghiên cứu bảo mật IoT có hỗ trợ thiết kế cho các thiết bị điện tử thông minh, hiệu suất năng lượng cao, khả năng tiêu thụ nguồn thấp. Trước đây, các kỹ thuật phân tích các vấn đề tiêu thụ và phân phối năng lượng thông qua một cách tiếp cận kín, xem xét riêng ở chip, bản mạch và package (nhóm linh kiện). Nhưng hiện nay, các giải pháp tiết kiệm năng lượng mới thực sự hỗ trợ phương pháp thiết kế tích hợp chip-package-system (CPS), cho phép tối ưu thành phần cũng như phân tích và tối ưu đồng thời xuyên suốt toàn bộ hệ thống. Cách tiếp cận này cân bằng điện thế hoạt động thấp cần thiết để tiết kiệm năng lượng với tính nhất quán và tin cậy đáp ứng được yêu cầu để loại bỏ lỗi.

**Cloud/edge-based Internet of Things:** Hỗ trợ khả năng phát triển và tích hợp các ứng dụng và giải pháp IoT vào nền tảng

## Trang 27

điện toán đám mây (cloud computing) và tính toán cận biên (edge computing). Hình 1.3 minh họa ý tưởng triển khai các ứng dụng và giải pháp IoT trên cloud, bao gồm hạ tầng kiến trúc mạng của một ứng dụng IoT thực tế dự định được triển khai.

Hình 1.3. Kiến trúc mạng tổng quan của một ứng dụng cloud-based IoT (Nguồn: IBM)

### 1.2. Xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam

Công nghệ IoT/5G và kỹ thuật xử lý dữ liệu lớn (Big Data), trí tuệ nhân tạo (AI) [32] đóng vai trò quan trọng trong việc tạo ra những đổi mới đột phá trong CNTT và truyền thông, và các lĩnh vực ứng dụng liên quan. Thành phố thông minh là một trong những ứng dụng như vậy, đã thu hút được sự chú ý lớn từ các chính phủ, cộng đồng ngành học thuật và CNTT tại nhiều quốc gia. Đặc biệt, Big Data/AI và IoT/5G cung cấp các công cụ và công nghệ cho phép quan trọng để thúc đẩy sự chuyển đổi của các thành phố lớn trên toàn thế giới thành những nơi đáng sống, làm việc và tận hưởng. Các công nghệ IoT/5G

---
[32] GSMA.com/IC, “Intelligent Connectivity: How the combination of 5G, AI, and IoT is set to change the Americas”.  

## Trang 28

mới, một khi được tích hợp đúng vào cơ sở hạ tầng thành phố thông minh (Smart Cities), có thể hỗ trợ số lượng lớn kết nối không dây từ các loại thiết bị không dây khác nhau (ví dụ: cảm biến, máy ảnh, thiết bị VR/AR, xe thông minh) thông qua môi trường mạng tốc độ cao, truyền dữ liệu cực kỳ đáng tin cậy và độ trễ thấp. Ngoài ra, các công nghệ IoTs/5G cho phép truyền thông, lưu trữ và xử lý dữ liệu hiệu quả, rất cần thiết để xử lý và phân tích lượng dữ liệu khổng lồ của thành phố thông minh và chuyển dữ liệu thu thập được thành các quy trình giám sát, ra quyết định và ứng dụng kịp thời cũng như cung cấp các dịch vụ kỹ thuật số đa phương tiện phong phú đến thiết bị di động cho người dân thành thị.

Hình 1.4 dưới đây minh họa ứng dụng IoTs/5G trong đô thị thông minh.

Hình 1.4. Các ứng dụng điển hình IoTs/5G trong đô thị thông minh

Trong các đô thị thông minh, mạng cảm biến không dây thường

## Trang 29

thường được triển khai ở các khu vực khó tiếp cận về mặt địa lý, hoặc ở xa. Mặc dù dữ liệu cảm biến thường được phân tích thống kê trong các ứng dụng giám sát, các truy vấn trực tiếp để yêu cầu dữ liệu cảm biến ngay lập tức và để điều chỉnh hành vi của các thiết bị cảm biến trong thời gian thực, thường được yêu cầu trong môi trường thay đổi động, tồn tại các yếu tố, sự kiện tác động không lường trước. Các công cụ quản trị mạng cảm biến, mạng IoTs/5G, cùng với các tiêu chuẩn để xử lý và quản lý dữ liệu cảm biến, dữ liệu IoTs/5G có thể hỗ trợ xây dựng các ứng dụng và giải pháp trên hạ tầng IoTs/5G mạnh hơn. Ngoài ra, các công nghệ mới để phát triển và tích hợp các thiết bị nhỏ sẽ cho phép đa dạng hóa các loại cảm biến, thiết bị IoTs/5G được triển khai. Số lượng thiết bị, ứng dụng và dự án IoTs/5G ngày càng tăng, khối lượng dữ liệu lớn được thu thập bởi các cảm biến, thiết bị IoTs/5G ngày càng lớn, đòi hỏi các nỗ lực nghiên cứu thích hợp để xử lý và phân tích dữ liệu, sử dụng hiệu quả tài nguyên, khả năng mở rộng, khả dụng và độ tin cậy của hệ thống. Tương tự, giám sát môi trường cần phải liên tục, tích hợp và không mất dữ liệu, đòi hỏi phải có đặc điểm kỹ thuật và triển khai cơ sở hạ tầng đáng tin cậy cho IoTs/5G.

Trong các ứng dụng IoTs không đồng nhất quy mô lớn, các cảm biến nhỏ và giá rẻ, và các thiết bị IoTs/5G có thể được triển khai độc lập hoặc kết hợp với các thiết bị tùy chỉnh nhiều tài nguyên hơn và đắt tiền hơn. Do đó, để giải quyết vấn đề này, hướng tiếp cận là tích hợp các thiết bị IoTs/5G không đồng nhất bằng cách phát triển một nền tảng phần mềm (middlewares) mở và đa quy mô trên cơ sở hạ tầng điện toán đám mây để triển khai các dịch vụ quản lý tích hợp nhiều loại thiết bị IoTs/5G. Một nền tảng dịch vụ như vậy sẽ bao gồm các danh mục dịch vụ khác nhau có thể được triển khai trong hệ thống mạng thử nghiệm IoTs/5G hoặc các ứng dụng thực tế để đạt được các mục tiêu như phát hiện sự kiện, vị trí đối tượng, theo dõi hoặc giám sát.

---
[31] https://techbeacon.com/app-dev-testing/67-open-source-tools-resources-iot  
[32] https://www.datamation.com/mobile-wireless/51-open-source-tools-for-the-internet-of-things-1.html  

## Trang 30

sát. Các dịch vụ và hạ tầng mạng thử nghiệm này nên xem xét các đặc điểm cụ thể của công nghệ IoTs/5G và tài nguyên vật lý bị hạn chế của các cảm biến, thiết bị IoTs/5G, bao gồm tuổi thọ pin, sức mạnh tính toán, bộ nhớ, băng thông mạng và chất lượng đường truyền.

Tại Việt Nam, mặc dù còn nhiều bất cập, song hiện nay, các đô thị Việt Nam đang phát triển theo hướng tiếp cận với nhiều mô hình tiên tiến theo xu thế hội nhập quốc tế, tạo ra nhiều tiền đề về ứng dụng và phát triển CNTT, truyền thông để phát triển đô thị thông minh và quản lý thông minh. Cụ thể, tỷ lệ người sử dụng internet/tổng dân số năm 2014 đạt 43,8%, cao hơn tỷ lệ của thế giới là 42,2% và châu Á là 34,8%. Việt Nam có gần 14.000 doanh nghiệp CNTT với 500.000 lao động và doanh thu lớn. Việt Nam cũng đã đạt được nhiều thành tựu trong việc ứng dụng CNTT vào hoạt động quản lý nhà nước và các lĩnh vực đời sống xã hội, rõ nhất là ở các lĩnh vực quản lý ngân sách và kho bạc, quản lý thuế, hải quan, bảo hiểm xã hội, giáo dục, y tế, quản lý giao thông, quản lý đất đai, quy hoạch, xây dựng, môi trường...

“Từ bức tranh của các đô thị Việt Nam, có thể thấy Việt Nam cần phát triển các đô thị theo hướng đô thị thông minh”, đồng chí Nguyễn Thiện Nhân - Nguyên Bí thư Thành ủy Thành phố Hồ Chí Minh nêu. Đô thị thông minh nhằm đạt tới 4 mục tiêu: hiệu quả kinh tế ở các đô thị ngày càng cao (đến năm 2025: diện tích đô thị khoảng 15% diện tích cả nước, tỷ lệ đô thị hóa khoảng 50% dân số, tạo ra khoảng 75% GDP); môi trường sống ngày càng tốt hơn; người dân được phục vụ tốt hơn; người dân tham gia quản lý đô thị và giám sát chính quyền.

Để có thể xây dựng và vận hành có hiệu quả một thành phố thông minh theo đúng nghĩa của nó thì ngay từ đầu chính quyền thành phố và các đối tác công nghệ cần phát triển và lựa chọn các giải pháp đạt chuẩn Internet of Things - IoTs. Bởi lẽ, trong trường hợp ngược lại, tức là chính quyền thành phố áp dụng triển khai giải pháp IoTs phân mảnh và phi tiêu chuẩn (Non-Standardized) thì việc vận hành cũng như mức độ kết nối giữa các thành phần trong hệ thống thành phố thông minh sẽ không

## Trang 31

mang lại kết quả như mong muốn ban đầu. Trong trường hợp này, việc phải đối mặt với các rủi ro tài chính và lãng phí nhân lực là điều khó tránh khỏi. Ngoài ra, thành phố thông minh là thành phố dùng công nghệ điện toán đám mây (Cloud computing) và CNTT thế hệ mới để quy hoạch đô thị, sử dụng các công cụ của CNTT và truyền thông để thu nhận, phân tích và tích hợp thông tin để vận hành thành phố, hỗ trợ cuộc sống của người dân, bảo vệ môi trường, giữ an toàn cộng đồng, phát triển các dịch vụ đô thị và đáp ứng các nhu cầu khác một cách thông minh, giúp cho nền kinh tế đô thị tăng trưởng, duy trì tiến bộ xã hội và phát triển bền vững.

Theo đánh giá của chúng tôi, xây dựng đô thị thông minh gắn liền với việc sử dụng công nghệ Internet of Things - IoTs và điện toán đám mây (cloud computing) hiện đại. Trong khi công nghệ IoTs với rất nhiều chuẩn giao tiếp hỗ trợ đa dạng, đa số các thiết bị đầu cuối hiện nay phục vụ thu thập dữ liệu, giám sát, công nghệ điện toán đám mây (cloud computing) và tính toán cận biên (edge computing) là các nền tảng hoàn hảo phục vụ tính toán, tích hợp dịch vụ và mạng Internet, và công nghệ trí tuệ nhân tạo (Artificial Intelligence - AI) cùng kỹ thuật xử lý dữ liệu lớn (Big Data) mang lại tính thông minh và tiện nghi hơn cho ứng dụng. Ngoài ra, nhằm làm chủ công nghệ, các nền tảng mã nguồn mở nên được ưu tiên lựa chọn triển khai.

## BÀI TẬP CHƯƠNG 1

1. Hãy liệt kê những thiết bị có thể kết nối vào Internet.
2. Hãy liệt kê những đặc điểm kỹ thuật của thiết bị được sử dụng trong IoT.
3. Hãy liệt kê những xu thế của IoT trên thế giới và ở Việt Nam.
4. Hãy liệt kê những ưu điểm mà IoT có thể mang lại cho cuộc sống.
5. Hãy liệt kê những thách thức mà IoT đang gặp phải.

## Trang 32

# CHƯƠNG 2. CÁC LĨNH VỰC ỨNG DỤNG IOT

Trong những năm gần đây, các thuật ngữ liên quan đến IoT như smart home, smart garden, smart parking,... và đặc biệt là smart city (thành phố thông minh/đô thị thông minh) được nhắc đến khá nhiều trong giới học thuật và cũng đã có những sản phẩm được bán ra ngoài thị trường. Mục tiêu cuối cùng của các ứng dụng IoT là làm cho cuộc sống trở nên dễ dàng, thân thiện hơn với con người. Máy móc, đồ vật, môi trường có thể hiểu được suy nghĩ của con người và hành động theo ý muốn của con người.

Trong chương này, tác giả đề cập đến một số ứng dụng IoT phổ biến, đã và đang được nghiên cứu phát triển hiện nay. Tuy mỗi giải pháp của mỗi nhà khoa học, công ty có thể khác nhau về hình thức, quy mô, nhưng chung quy lại những sản phẩm, giải pháp này đều có chung một số tính năng cơ bản được đề cập trong chương này.

Giải pháp đầu tiên mà khi nhắc đến IoT người ta hay liên tưởng đến đầu tiên, đó là smart home (nhà thông minh). Trong giải pháp nhà thông minh, các vật dụng gia đình có thể được điều khiển từ xa hoặc nếu cao cấp hơn, chúng có thể tự hoạt động mà không cần sự tác động trực tiếp của gia chủ.

Giải pháp IoT thứ hai được nhắc đến trong chương này là Smart City. Đây không phải là một ứng dụng đơn lẻ mà bao gồm cả một hệ sinh thái các ứng dụng được tích hợp với nhau thông qua một kiến trúc phân cấp từ nhà quản lý, nhà điều hành đến các cư dân của thành phố.

Ứng dụng thứ ba được giới thiệu trong chương này là Smart Agriculture (nông nghiệp thông minh). Một kiến trúc tổng quát về nông nghiệp thông minh được đưa ra để giúp người đọc có cái nhìn tổng quát về ứng dụng này.

Hình 2.1 mô tả các loại ứng dụng IoT, bao gồm phân loại về nội dung (Multimedia hoặc Scalar) và phân loại về chủ thể (Hệ thống hoặc con người).

## Trang 33

Hình 2.1. Phân loại ứng dụng Internet of Things [28]

Các ứng dụng IoT vừa nêu trên sẽ được giới thiệu một cách tổng quát trong Chương 2. Phần kiến trúc cụ thể của một ứng dụng IoT sẽ được trình bày trong Chương 3 của giáo trình này; các phần mềm, phần cứng phân loại phần cứng được sử dụng trong IoT sẽ nằm trong Chương 4.

### 2.1. Nhà thông minh (Smart Home)

Smart Home là ứng dụng phổ biến nhất trong IoT. Mục tiêu cốt lõi của Smart Home là tạo ra ngôi nhà tiện nghi, thích ứng với nhu cầu của gia chủ. Trong Smart Home, các cảm biến được đặt tại nhiều vị trí trong nhà thu thập dữ liệu như nhiệt độ, độ ẩm, ánh sáng bên trong nhà và ngoài trời để các ứng dụng có thể điều khiển các thiết bị trong nhà cho phù hợp với từng ngữ cảnh. Hình 2.4 mô tả một số thiết bị trong gia đình có thể được điều khiển qua các ứng dụng IoT.

Nhiều giải pháp được tích hợp để đưa ra một ứng dụng smart home. Tùy vào quy mô, mức độ của smart home mà các giải pháp được tích hợp nhiều hay ít. Sau đây là một số giải pháp trong ứng dụng smart home:

## Trang 34

- **Giám sát an ninh:** Hệ thống camera giám sát được trang bị xung quanh ngôi nhà để đảm bảo không có sự xâm nhập bất hợp pháp vào ngôi nhà của gia chủ. Tính thông minh của hệ thống này có thể được tích hợp vào hệ thống cửa ra vào nếu trang bị hệ thống nhận diện gia chủ. Hệ thống thứ hai là cảm biến đặt tại cửa ra vào, cửa sổ, cảm biến chuyển động, cảm biến khí ga, hay cảm biến khói có thể cho gia chủ biết được tình trạng ngôi nhà của mình khi vắng nhà. Hình 2.2 là ví dụ về bảng điều khiển của hệ thống cảm biến đặt trong nhà thông minh, bao gồm giá trị của các cảm biến nhiệt độ, độ ẩm và các thiết bị chiếu sáng ở các vị trí trong nhà. Bên cạnh đó, hệ thống phát hiện và ngăn ngừa xâm nhập cũng có thể được tích hợp vào hệ thống để tăng mức độ an ninh cho ngôi nhà.

Hình 2.2. Ví dụ về Giao diện của Hệ thống giám sát trong Nhà thông minh

## Trang 35

- **Điều khiển thiết bị gia đình:** Gia chủ có thể điều khiển từ xa bật/tắt bóng đèn, quạt, rèm cửa,... thông qua một chiếc điện thoại thông minh. Hình 2.3 là ví dụ về giao diện điều khiển các thiết bị trong nhà thông minh, bao gồm các hệ thống điều khiển cửa ra vào và hệ thống chiếu sáng trong mỗi phòng. Ngoài ra, các ứng dụng smart home hay smart building còn tập trung vào việc điều khiển hệ thống sưởi, hệ thống lọc gió. Ứng dụng tự điều chỉnh nhiệt độ của điều hòa nhiệt độ hoặc điều khiển mở rèm cửa hay bật bóng đèn khi nhận thấy trong phòng có người và cường độ ánh sáng thấp.

Hình 2.3. Ví dụ về Giao diện của Hệ thống điều khiển trong Nhà thông minh

- **Quản lý năng lượng:** Giúp gia chủ theo dõi mức tiêu thụ điện năng của từng thiết bị trong nhà theo thời gian thực, từ đó đưa ra các gợi ý hoặc tự động tối ưu hóa việc sử dụng điện nhằm tiết kiệm chi phí.

- **Quản lý các thiết bị nhà bếp:** Tủ lạnh thông minh có thể nhận biết các loại thực phẩm bên trong, hạn sử dụng và tự động lên danh sách mua sắm, máy pha cà phê tự động kích hoạt theo lịch trình báo thức của gia chủ.

## Trang 36

Hình 2.4. Các thiết bị trong Smart Home [29]

### 2.2. Đô thị thông minh (Smart City)

Smart cities - Thành phố thông minh là một bước tiến mới cho sự phát triển đô thị. Trong đó, cơ sở hạ tầng công nghệ thông tin và truyền thông (Information and Communication Technology - ICT), bao gồm các lĩnh vực trọng tâm như trí tuệ nhân tạo, điện toán đám mây, dữ liệu lớn và Internet vạn vật đóng vai trò nền tảng để tối ưu hóa việc quản lý các nguồn lực và phục vụ cư dân tốt hơn.

Sự bùng nổ dân số đô thị và tốc độ đô thị hóa nhanh chóng đang đặt ra nhiều thách thức lớn về giao thông, môi trường, y tế, giáo dục và quản lý an ninh trật tự. Đô thị thông minh ra đời nhằm giải quyết những bài toán cấp bách này bằng cách áp dụng công nghệ số vào mọi mặt của đời sống đô thị.

## Trang 37

Xu thế này sẽ làm ảnh hưởng đến cuộc sống của mỗi cư dân và vào việc di chuyển của cư dân trong thành phố.

Khái niệm smart cities đã được đề xuất từ khoảng 10 năm trước đây. Trong đó, châu Âu là nơi có nhiều dự án nghiên cứu và phát triển về vấn đề này nhiều nhất. Một số dự án tại châu Âu có thể kể đến như FP7 SmartSantander [1], OUTSMART [2], BUTLER...

Các nước châu Á cũng đã bước đầu đề xuất và xây dựng các thành phố thông minh như Singapore, Seoul, Tokyo,... Tại Việt Nam, nhiều thành phố lớn như Hà Nội, TP. Hồ Chí Minh, Đà Nẵng, Cần Thơ, Bình Dương,... cũng đang trong quá trình xây dựng đề án và triển khai từng phần của thành phố thông minh.

---
[1] http://smartsantander.eu  
[2] https://www.worldsensing.com/innovation/  

## Trang 38

**Các hướng tiếp cận trong việc phát triển thành phố thông minh:**

- **Từ trên xuống (Top-down):** xây dựng kiến trúc tổng thể rồi sau đó tiến hành xây dựng các dự án cụ thể.
- **Từ dưới lên (Bottom-up):** xây dựng từng dự án cụ thể sau đó tiến hành tích hợp các dự án này thành một kiến trúc tổng thể.
- **Lai ghép (Hybrid):** thực hiện xây dựng theo cả hai hướng tiếp cận trên, đưa ra kiến trúc chung, vừa xây dựng từng dự án, vừa tích hợp.

Hình 2.7. Giao diện điều khiển của Trạm quan trắc môi trường tại ĐH Công nghệ Thông tin

## Trang 39

Hệ thống quan trắc này gồm các nút cảm biến về các loại khí CO, NO2, Nhiệt độ, Độ ẩm, Lượng mưa, Tốc độ gió, Cường độ ánh sáng. Dữ liệu này được thu thập và chuyển đến UIT Cloud. Tại đây, dữ liệu cảm biến được phân tích và hiển thị cho người dùng thông qua giao diện bên trên.

#### 2.2.1. Kiến trúc tổng quát

Hạ tầng IoT cho một smart city là kiến trúc 4 lớp được mô tả trong Hình 2.8 bên dưới. Dữ liệu được truyền từ các thiết bị cảm biến thông qua các cổng giao tiếp và mạng diện rộng về trung tâm dữ liệu để xử lý và cung cấp dịch vụ đến người dùng.

Hình 2.8. Kiến trúc tổng quát của Smart City (Nguồn: Cisco Press)

## Trang 40

người hoặc ứng dụng. Thiết bị cảm biến (sensor) và actuator sẽ được trình bày chi tiết trong Chương 4 của giáo trình này.

Tùy vào mục đích của ứng dụng mà các loại cảm biến khác nhau có thể sử dụng. Sau đây là một số loại cảm biến được sử dụng trong những ứng dụng cụ thể:

- **Cảm biến gần (Proximity Sensor):** được dùng để phát hiện sự kiện đỗ xe bằng cách phân tích những thay đổi trong phạm vi xung quanh nó khi một vật thể xuất hiện.
- **Cảm biến từ:** dùng để phát hiện phương tiện kim loại di chuyển qua các nút giao thông.
- **Cảm biến môi trường:** đo nồng độ bụi mịn PM2.5, nhiệt độ, độ ẩm, nồng độ các chất khí độc hại trong không khí.
- **Camera thông minh:** dùng để nhận diện biển số xe, nhận diện khuôn mặt, phát hiện tai nạn hoặc ùn tắc giao thông tự động.

## Trang 41

Hình 2.9. Kiến trúc mạng phổ biến trong City Layer (Nguồn: Cisco Press)

**Data Center Layer:** Dữ liệu thu thập từ Street Layer sẽ được chuyển tiếp đến Data Center Layer. Lớp này chịu trách nhiệm lưu trữ, xử lý để đưa ra các quyết định kịp thời cho toàn bộ hệ thống đô thị.

**Service Layer:** Cung cấp các giao diện lập trình ứng dụng (APIs) và các dịch vụ trực quan hóa dữ liệu đến các cơ quan quản lý và người dân.

## Trang 42

Ví dụ trong ứng dụng Smart parking có hai nhóm người dùng có thể truy cập vào hệ thống: Người lái xe và Người quản lý bãi đỗ xe. Người lái xe có thể tìm kiếm chỗ đỗ xe còn trống gần nhất, đặt chỗ và thanh toán phí tự động. Người quản lý có thể theo dõi tỷ lệ lấp đầy, doanh thu và tối ưu hóa phân luồng xe.

#### 2.2.2. Giao thông thông minh

Giao thông thông minh (Intelligent Transportation Systems - ITS) là một trong những hợp phần quan trọng nhất của đô thị thông minh. Mục tiêu là giảm thiểu ùn tắc, tai nạn giao thông, giảm lượng khí thải CO2 và nâng cao trải nghiệm đi lại của người dân.

Hình 2.10. Các ứng dụng trong Giao thông thông minh

## Trang 43

Tại Việt Nam, các dự án đường sắt đô thị cũng đang được xây dựng tại Hà Nội và TP.HCM kết hợp với các hệ thống vé thông minh, quản lý điều hành tự động.

#### 2.2.3. Môi trường thông minh

Môi trường thông minh là việc ứng dụng công nghệ IoT và dữ liệu lớn để theo dõi, phân tích chất lượng môi trường không khí, nước, tiếng ồn, đồng thời quản lý hiệu quả hệ thống chiếu sáng công cộng và thu gom rác thải.

#### 2.2.4. Cuộc sống thông minh

Nâng cao chất lượng cuộc sống cho người dân thông qua các dịch vụ công trực tuyến, y tế thông minh, giáo dục thông minh và các hoạt động văn hóa giải trí số hóa.

## Trang 44

Hình 2.11. Kiến trúc của một hệ thống Dự báo chất lượng không khí

#### 2.2.5. Một số dự án thành phố thông minh

Nhiều thành phố lớn trên thế giới đã triển khai thành công các dự án thành phố thông minh với quy mô lớn. Dưới đây là một số ví dụ tiêu biểu:

**Thành phố Amsterdam (Hà Lan):** Dự án Amsterdam Smart City (ASC) được khởi xướng từ năm 2009, tập trung vào các lĩnh vực như Smart Mobility, Smart Living, Smart Society, Smart Economy và Smart Areas.

## Trang 45

trong chiến lược Thành phố thông minh của Amsterdam. Trong đó, hệ thống chiếu sáng thông minh Smart Lighting cho phép điều chỉnh độ sáng đèn đường tùy theo lưu lượng người qua lại và điều kiện thời tiết, giúp tiết kiệm đến 50% điện năng tiêu thụ.

Các dự án năng lượng tái tạo và lưới điện thông minh (Smart Grid) tại khu vực Nieuw-West cho phép các hộ gia đình tự sản xuất điện từ pin mặt trời và bán lại lượng điện dư thừa vào lưới điện thành phố.

Hệ thống quản lý giao thông kết hợp với dữ liệu thời gian thực giúp giảm thiểu tình trạng kẹt xe và khuyến khích người dân sử dụng xe đạp hoặc phương tiện giao thông công cộng.

## Trang 46

Hình 2.12. Các đặc điểm của Thành phố thông minh tại Amsterdam [3]

**Thành phố Barcelona (Tây Ban Nha):** Barcelona được xem là một trong những hình mẫu thành công nhất về đô thị thông minh tại châu Âu. Thành phố đã triển khai mạng lưới cảm biến diện rộng phục vụ nhiều mục đích khác nhau.

---
[3] https://smartcommunities.media/truly-smart-city-five-lessons/  

## Trang 47

Barcelona cũng đã thành lập các dự án Thành phố thông minh từ rất sớm. Thành phố triển khai hệ thống tưới tiêu thông minh cho các công viên, hệ thống chiếu sáng LED kết hợp cảm biến chuyển động, và hệ thống thùng rác thông minh có gắn cảm biến báo mức đầy để tối ưu lộ trình thu gom rác.

Hình 2.13. Chương trình trong dự án Thành phố thông minh tại Barcelona [6]

---
[6] https://journals.openedition.org/factsreports/4367  

## Trang 48

- **Cảm biến tiếng ồn:** Hệ thống cảm biến chi phí thấp và dễ sử dụng, có thể phát hiện được ô nhiễm không khí, tiếng ồn, độ ẩm và nhiệt độ đã giúp phát hiện được mức độ ô nhiễm tiếng ồn ở gần các quảng trường đạt mức 100 decibel - vượt quá khuyến nghị của Tổ chức Y tế Thế giới (WHO).

- **Hệ thống thủy lợi:** Các cảm biến khác nhau được đặt trong lòng đất cung cấp dữ liệu về độ ẩm, nhiệt độ, tốc độ gió, ánh sáng mặt trời và áp suất khí quyển. Các dữ liệu này được cung cấp đến nhà nông để họ điều chỉnh loại cây trồng phù hợp cho từng thời điểm. Ngoài năng suất và chất lượng cây trồng được tăng lên, lượng nước sử dụng cũng giảm đi đáng kể. Theo ước tính, lượng nước sử dụng cho nông nghiệp của Thành phố đã giảm một phần tư so với trước đó.

Hình 2.14. Kiến trúc của Chính quyền thành phố trong dự án Thành phố thông minh của Barcelona [7]

Hình 2.14 mô tả kiến trúc của Chính quyền thông minh trong dự án Thành phố thông minh của Barcelona. Kiến trúc này tạo ra sự liên thông trong toàn bộ quy trình xử lý công việc tại mỗi bộ phận trong Chính quyền thành phố. Từ đó, sự phối hợp giữa các bên liên quan (lãnh đạo, phòng ban, và người dân) trở nên dễ dàng.

---
[7] https://journals.openedition.org/factsreports/4367  

## Trang 49

Năm 2014, dự án “Connecting Copenhagen” đã được nhận giải thưởng The World's Best Smart City Project. Dự án này được quản lý bởi Cơ quan Quản lý Kỹ thuật và Môi trường của Copenhagen và được điều phối bởi Copenhagen Solutions Lab. Copenhagen đặt mục tiêu trở thành thủ đô trung hòa carbon đầu tiên của thế giới vào năm 2025 và Đan Mạch quyết tâm trở nên hoàn toàn độc lập với nhiên liệu hóa thạch vào năm 2050.

Hình 2.15. Chiến lược thành phố thông minh của Copenhagen [8]

### 2.3. Nông nghiệp thông minh (Smart Agriculture)

Nông nghiệp hiện đại (Precision Agriculture) là một hướng đi mới bằng cách sử dụng Công nghệ thông tin, Hệ thống thông tin địa lý (Geographic Information System - GIS), GPS, WSN,... nhằm tăng năng suất cây trồng và giảm thiểu tác động môi trường. Theo đó, IoT và các công nghệ liên quan như WSN,

---
[8] https://www.niras.dk/media/1585/kimspiegelbergsteltzer.pdf  

## Trang 50

Cloud Computing, Big Data, Data Analytic, AI... là một giải pháp hoàn chỉnh cho Nông nghiệp hiện đại. Ngoài ra, nông nghiệp hiện đại đang tìm cách thay đổi nông nghiệp truyền thống thành chất lượng cao, năng suất cao, tiết kiệm chi phí và tài nguyên.

Hình 2.16 mô tả kiến trúc của một hệ thống nông nghiệp thông minh.

Cũng giống như các ứng dụng thông minh khác, một giải pháp Nông nghiệp thông minh bao gồm 4 lớp: WSN, Edge, Cloud Computing và Service. Các thông tin về môi trường như nhiệt độ, độ ẩm, ánh sáng.... được thu thập qua cảm biến và gửi về Cloud thông qua các nút biên (Edge), các dịch vụ lưu trữ, phân tích được thực hiện ngay tại Cloud và đưa ra các quyết định và truyền các tín hiệu điều khiển này ngược về các nút tại WSN để điều khiển các thiết bị như máy bơm nước, đèn,...

Hình 2.16. Kiến trúc của một ứng dụng nông nghiệp thông minh

Hình 2.16 mô tả kiến trúc của một ứng dụng Nông nghiệp thông minh. Lớp đầu tiên của kiến trúc này là Lớp thiết bị. Các đối tượng trong lớp này bao gồm máy móc trong nông nghiệp, vật nuôi, cây trồng.... được gắn các thiết bị cảm biến để thu thập dữ liệu từ môi trường thực tế. Sau đó, dữ liệu này được truyền

## Trang 51

đến Gateway thông qua nhiều bộ giao thức khác nhau như Zigbee, Bluetooth, LoRa, WLAN,... Các bộ giao thức này sẽ được trình bày trong Chương 3 của giáo trình này. Dữ liệu từ Gateway được chuyển tiếp đến Cloud thông qua các bộ giao thức như TCP/IP, Cellular. Tại đây, dữ liệu cảm biến được lưu trữ, phân tích và đưa ra các dự đoán và chuyển tiếp đến Web App trên thiết bị của người dùng. Lớp cuối cùng trong ứng dụng Nông nghiệp thông minh là Lớp người dùng. Tại đây, người dùng có thể xem được các thông số của môi trường, vật nuôi từ dữ liệu thô (raw data) hoặc dữ liệu sau khi được phân tích, dự đoán. Các loại dữ liệu này còn được gọi là ngữ cảnh - được trình bày trong Chương 6 của giáo trình. Ngoài ra, người dùng có thể đưa ra tín hiệu điều khiển ngược lại đến các thiết bị tại Lớp thiết bị để điều khiển các công cụ trong lớp này.

## BÀI TẬP CHƯƠNG 2

1. Hãy liệt kê những ứng dụng IoT trên thế giới và ở Việt Nam.
2. Hãy liệt kê những ứng dụng trong Thành phố thông minh.
3. Hãy liệt kê các thành phần chính trong một kiến trúc IoT.
4. Hãy thiết kế kiến trúc IoT cho nông nghiệp tại Việt Nam.
5. Hãy thiết kế kiến trúc IoT và liệt kê các chức năng của ứng dụng nhà thông minh.
6. Hãy trình bày ý tưởng và xây dựng kiến trúc IoT phục vụ cho việc giám sát giao thông tại Việt Nam.
7. Hãy trình bày ý tưởng và xây dựng kiến trúc IoT trong giám sát chất lượng không khí tại Thành phố Hồ Chí Minh.

## Trang 52


# CHƯƠNG 3. CÁC KIẾN TRÚC MẠNG VÀ BỘ GIAO THỨC MẠNG IOT

Các hệ thống Internet của vạn vật thường bao gồm rất nhiều thiết bị kết nối với nhau để trao đổi dữ liệu thu thập cũng như các tín hiệu điều khiển trong mạng. Nhiều kiến trúc mạng cũng như các bộ giao thức mạng đặc biệt dùng trong IoT đã được nghiên cứu và phát triển để tạo nên một cơ chế truyền gửi dữ liệu một cách hiệu quả giữa các nốt trong mạng IoT.

Nội dung chương này trình bày những kiến thức cơ bản về một số kiến trúc mạng thường sử dụng trong IoT cũng như giới thiệu một số chuẩn kết nối mạng được dùng nhiều trong các hệ thống IoT. Các kiến trúc mạng được trình bày theo thứ tự từ những kiến trúc mạng truyền thống được sử dụng thường xuyên trong các hệ thống mạng máy tính thông thường như kiến trúc cây (tree), kiến trúc mắt lưới (mesh), kiến trúc vòng (ring), kiến trúc chuỗi (chain) và kiến trúc lưới (grid). Tiếp theo đó, một số kiến trúc mạng hiện đại cũng được đề cập như kiến trúc phụ lưu - đồng bằng (Tributary - Delta), kiến trúc dựa theo cụm (cluster-based), kiến trúc làn sóng (sweep). Phần còn lại của chương này trình bày một số đặc điểm kỹ thuật của các bộ giao thức mạng thường dùng trong IoT, bao gồm: 6LoWPAN, giao thức WiFi, Zigbee. Đây là các bộ giao thức được dùng phổ biến để hiện thực cơ chế truyền thông giữa các thiết bị trong mạng IoT.

Thông qua nội dung chương này, người đọc có cái nhìn tổng quan về cơ chế truyền gửi dữ liệu giữa các nốt IoT trong mạng cùng các tiêu chuẩn kỹ thuật, những đặc trưng cơ bản của các chồng giao thức mạng không dây được trình bày. Nắm vững những đặc điểm cơ bản này, người đọc có thể thực hiện các nghiên cứu, phân tích, đánh giá, chọn lựa các kiến trúc mạng, các bộ giao thức IoT phù hợp khi triển khai các giải pháp IoT trong thực tế.

## Trang 53


### 3.1. Các kiến trúc mạng dùng trong IoT

#### 3.1.1. Một số kiến trúc mạng đơn giản

**Kiến trúc mắt lưới (mesh)**

Trong mô hình mạng Mesh, gói tin từ một nút có thể có nhiều đường đi đến đích. Đây là một trong những ưu điểm của mô hình mạng mesh (trong mô hình dạng vòng mặc dù có hai đường đi, tin nhắn chỉ có thể đi theo một hướng). Trong Hình 3.1, các nút có thể kết nối đến tất cả các nút còn lại trong mạng được gọi là một mạng mesh đầy đủ (full mesh). Trong Hình 3.2, mô hình mạng mesh có một số nút có kết nối gián tiếp đến các nút khác trong mạng được gọi là mạng mesh một phần (partial mesh).

**Hình 3.1.** Kiến trúc full mesh | **Hình 3.2.** Kiến trúc Partial Mesh

**Kiến trúc cây (tree)**

Mạng sử dụng một hub trung tâm được gọi là một nút gốc, xem như là một bộ định tuyến thông tin liên lạc chính. Hình 3.3 mô tả một hệ thống phân cấp, cấp dưới nút gốc là các hub trung tâm, mức thấp này tạo thành một mạng sao. Các mạng dạng cây có thể được coi là sự lai tạo của mạng hình sao và mạng Peer to Peer. Trong đường dẫn mạng cảm biến có thể là single hop hoặc multi hop, các nút cảm biến nhận dữ liệu của môi trường rồi gửi chúng đến bộ phận thu nhận (Sink), sau đó chuyển tiếp chúng đến các nút cha mẹ. Điều quan trọng là để tìm đường đi ngắn nhất sao cho tối ưu với thời gian sống tối đa và độ trễ ngắn hơn mặc dù độ phức tạp thời gian hơi cao nhưng phù hợp hơn cho việc thực hiện phân phối. Mạng dạng cây có vấn đề trong

## Trang 54


chương trình cân bằng tải tại mỗi mức của cây và có thông tin liên lạc giữa hai nút. Nếu có một liên kết có vấn đề trong truyền dẫn trên tuyến đường hoạt động thì việc truyền thông cũng bị phá vỡ.

**Hình 3.3.** Kiến trúc Tree

**Kiến trúc vòng (ring)**

Hình 3.4 mô tả một mô hình mạng có kiến trúc vòng, mỗi nút có đúng hai người hàng xóm cho mục đích truyền thông. Tất cả các tin nhắn đi qua một vòng trong cùng một hướng (hoặc là "chiều kim đồng hồ" hay "ngược chiều kim đồng hồ"). Nếu một nút trong vòng gặp vấn đề thì có thể phá vỡ các vòng lặp và cũng có thể làm sụp đổ toàn bộ mạng. Tin nhắn trong mô hình này có hai đường đi nhưng chỉ có thể đi theo một hướng.

**Hình 3.4.** Kiến trúc Ring

**Kiến trúc chuỗi (chain)**

Trong một mạng dạng chain, các nút kết nối với nhau thành dạng chuỗi như Hình 3.5 bên dưới. Ngoài nút đầu và nút cuối,

## Trang 55


mỗi nút trong mạng chain có đúng hai người hàng xóm cho mục đích truyền thông. Nếu một nút trong chuỗi gặp vấn đề thì có thể ảnh hưởng đến việc gửi nhận thông tin của cả mạng.

**Hình 3.5.** Kiến trúc chuỗi

**Kiến trúc sao (Star)**

Mạng hình sao được kết nối với một hub đóng vai trò là bộ phận truyền thông trung tâm (Sink) và các nút (các nút này không thể giao tiếp trực tiếp với nhau). Hình 3.6 là một ví dụ về mô hình mạng sao có một nút trung tâm và năm nút đầu cuối. Toàn bộ thông tin liên lạc phải được định tuyến thông qua hub trung tâm. Mỗi nút là một "client", trong khi hub trung tâm là "server hoặc sink". Nhưng mô hình này có nhược điểm là chỉ có một đường giao tiếp duy nhất.

**Hình 3.6.** Star Topology

**Kiến trúc lưới (Grid)**

Các trường cảm biến mạng được chia thành các đường kẻ ô. Các vùng mạng được chia thành lưới ô vuông không chồng lên nhau với cùng một kích thước. Hình 3.7 mô tả một ứng dụng dựa trên kiến trúc lưới. Nên có ít nhất một và chỉ một nút trong trạng thái làm việc trong mỗi lưới tại bất cứ khoảng thời gian nào. Để kéo dài thời gian sống mạng, các nút trong một mạng lưới nên hoạt động lần lượt. Bên trong mỗi lưới, một nút được chọn như là lưới đầu tiên có trách nhiệm chuyển tiếp thông tin

## Trang 56


định tuyến và truyền gói dữ liệu. Định tuyến được thực hiện trong lần lượt từ lưới này đến các lưới khác. Mô hình dựa vào giao thức định tuyến đa đường dựa vào các lưới mạng để định tuyến các gói tin một cách nhanh nhất, tận dụng và mở rộng các nút cảm biến năng lượng ngoài để tránh và xử lý tắc nghẽn mạng khi chúng xảy ra trong mạng.

**Hình 3.7.** Kiến trúc lưới

#### 3.1.2. Một số kiến trúc mạng phức tạp

**Kiến trúc dựa theo cụm (cluster-based)**

Kiến trúc dựa theo cụm/nhóm (cluster-based) là kiến trúc mà các thiết bị cảm biến thu thập dữ liệu và gửi về một thiết bị đầu cụm (cluster head). Hình 3.8 là một ví dụ về mạng cảm biến có kiến trúc gồm 6 cluster, mỗi cluster được quản lý bởi một Cluster Head. Cách làm này mang đến hiệu quả cao trong trường hợp hệ thống mạng cảm biến có kích thước lớn, khoảng cách xa nhau và định tuyến qua nhiều mức (multihop routing). Kiến trúc dựa trên cụm này làm giảm lượng dữ liệu truyền gửi giữa tất cả các cảm biến so với kiến trúc khác như mesh. Một số kỹ thuật tinh giảm dữ liệu (reduction techniques) có thể được áp dụng để tăng cường hiệu quả. Tuy nhiên, kiến trúc dựa trên cụm này có khuyết điểm là nếu thiết bị đầu cụm ở quá xa các thiết bị cảm biến thì sẽ làm tăng chi phí truyền thông, năng lượng tiêu thụ.

## Trang 57


**Hình 3.8.** Kiến trúc dựa theo cụm (cluster-based)

**Kiến trúc dựa trên địa hình phụ lưu - đồng bằng (Tributary - Delta)**

Kiến trúc Tributary - Delta [1], được hình thành từ ý tưởng dòng chảy của con sông, là một cách tiếp cận mới trong tập hợp dữ liệu trong mạng. Kiến trúc này là kết quả của việc kết hợp các ưu thế của kiến trúc dựa trên kiến trúc cây (tree-based) và định tuyến đa luồng (multi-path routing). Hình 3.9 là một ví dụ về kiến trúc Tributary - Delta, mô hình mạng được chia làm hai vùng riêng biệt: Tributary và Delta. Trong mạng độ lỗi thấp, kiến trúc cây được sử dụng cho các thông điệp có kích thước nhỏ, trong trường hợp độ lỗi cao, dữ liệu thu thập từ rất nhiều cảm biến thì multi-path routing được sử dụng để đảm bảo hiệu quả.

**Hình 3.9.** Kiến trúc Tributary - Delta [1]

## Trang 58


**Kiến trúc dựa theo làn sóng (Sweep)**

**Hình 3.10.** Kiến trúc dựa theo làn sóng [2]

Đây là kiến trúc thu thập dữ liệu dựa trên ý tưởng hoạt động của làn sóng mà ở đó dữ liệu đi ngang qua mỗi thiết bị đúng một lần và thực hiện các hành động theo ý muốn [2]. Kiến trúc mạng sweep được hiện thực bởi một nhóm nhỏ các nốt hoạt động, các nốt này di chuyển qua mạng bằng cách phát một thông điệp lời mời tới các nốt mới để tham gia vào nhóm và loại bỏ các nốt đã thực hiện rồi nhưng không đóng vai trò quan trọng gì khác. Đặc trưng quan trọng của kiến trúc này là tính chất bền vững bởi mặc dù một kiến trúc cây được sử dụng cho một phần tác vụ tổng hợp dữ liệu trong một nhóm hoạt động thì những cây này là cục bộ và được dùng hầu hết ngay khi chúng được xây dựng. Đường tổng hợp dữ liệu được phân chia trên đường quét và không cần thiết phải có một cấu trúc cây cố định cho việc tính toán. Vì vậy, cách tiếp cận này có tính vững vàng ngay cả với các liên kết có sự biến động và nhiều nút bị hỏng. Hình 3.10 mô tả kiến trúc mạng theo làn sóng, trong đó, các nốt trong vùng màu đỏ đang hoạt động, các nốt trong vùng màu xanh đã hoạt động và các nốt màu trắng chưa tham gia vào mạng.

## Trang 59


### 3.2. Các bộ giao thức mạng không dây thường dùng trong IoT

Để triển khai được các kiến trúc truyền tải dữ liệu như trình bày ở phần trên, các nền tảng phần mềm, hệ điều hành chạy trên thiết bị IoT phải hỗ trợ các chuẩn kết nối không dây mà ở đó những cơ chế, giải thuật định tuyến, điều khiển kết nối giữa các thiết bị hoạt động đúng như thiết kế. Tập hợp tất cả cơ chế, giải thuật, quy trình đó được định nghĩa và thiết kế theo một tiêu chuẩn mạng, tạo nên các bộ giao thức mạng đảm bảo chức năng truyền gửi dữ liệu và tín hiệu điều khiển trong mạng cảm biến không dây cũng như mạng Internet bên ngoài.

Trong kiến trúc mạng IoT, có hai cách tiếp cận để các thiết bị IoT có thể truyền dữ liệu ra bên ngoài mạng Internet đó là: (i) thiết bị IoT có một địa chỉ mạng riêng biệt (địa chỉ IPv6) để giao tiếp trực tiếp với mạng bên ngoài; (ii) các thiết bị IoT giao tiếp nội bộ trong mạng IoT của mình, sau đó gửi dữ liệu ra ngoài thông qua thiết bị cổng (IoT Gateway) hoặc các thiết bị trạm (base station). Hai bộ giao thức mạng đặc trưng cho hai cơ chế kết nối này đó là bộ giao thức 6LoWPAN (thiết bị IoT kết nối trực tiếp với mạng bên ngoài qua IPv6) và bộ giao thức Zigbee. Bên cạnh hai bộ giao thức đặc trưng đó, ngày nay giải pháp kết nối thiết bị IoT qua mạng WLAN truyền thống cũng được sử dụng phổ biến trong các ngữ cảnh đơn giản. Đặc biệt, với sự ra đời của các nền tảng phần cứng hỗ trợ kết nối WiFi như ESP8266, ESP32 cho phép người mới bắt đầu với công nghệ IoT có thể hiện thực giải pháp IoT đơn giản với kết nối WiFi quen thuộc. Phần tiếp theo của phần này trình bày chi tiết đặc trưng kỹ thuật của các bộ giao thức không dây vừa kể trên.

#### 3.2.1. Bộ giao thức 6LoWPAN

6LoWPAN là viết tắt của "IPv6 over Low-Power Wireless Personal Area Network", là công nghệ mạng cho phép gói tin IPv6 được sử dụng trong những link layer nhỏ như định nghĩa trong IEEE 802.15.4. Là lựa chọn tốt cho các ứng dụng IoT khi mạng cảm biến không dây có kích thước lớn [3].

## Trang 60


6LoWPAN là chuẩn mở được định nghĩa trong RFC 6282 bởi IETF. Tính năng nổi bật của 6LoWPAN là ban đầu chỉ hỗ trợ cho IEEE 802.15.4 trong mạng cảm biến không dây tiết kiệm năng lượng trong băng tần 2.4GHz nhưng giờ đây đã mở rộng ra nhiều loại mạng khác bao gồm Sub-1 GHz low-power RF, Bluetooth, Smart Power Line Control (PLC) và low-power Wi-Fi [3].

##### 3.2.1.1. Kiến trúc mạng 6LoWPAN

Hình 3.11 trình bày kiến trúc mạng mesh 6LoWPAN. Hướng uplink ra Internet được quản lý bởi Access Point (AP) hoạt động như một IPv6 Router. Một số thiết bị khác kết nối vào Router như: PC, server... Mạng 6LoWPAN được kết nối với mạng IPv6 thông qua edge router. Các edge router quản lý 3 việc là: 1) trao đổi dữ liệu giữa thiết bị chạy 6LoWPAN và Internet (hay mạng IPv6 khác); 2) trao đổi dữ liệu nội bộ giữa các thiết bị bên trong mạng 6LoWPAN; và 3) là tạo và duy trì radio subnet (mạng 6LoWPAN).

**Hình 3.11.** Kiến trúc mạng mesh 6LoWPAN [3]

## Trang 61


Bằng cách giao tiếp với IP truyền thống, mạng 6LoWPAN kết nối với các mạng khác thông qua router IP. Như hình trên thì mạng 6LoWPAN hoạt động trên một góc như một stub network. Điều đó có nghĩa là dữ liệu đi vào mạng để dành riêng cho một thiết bị cụ thể ở trong mạng 6LoWPAN. Bên ngoài, mạng IP truyền thống có thể được cung cấp bởi các loại liên kết khác nhau như: ethernet, Wi-Fi hay 3G/4G. Bởi vì 6LoWPAN chỉ chuyên hoạt động với IPv6 thông qua chuẩn IEEE 802.15.4, một router 6LoWPAN là một router kết nối giữa hai mạng với nhau. Các thiết bị trong mạng 6LoWPAN giao tiếp với nhau bằng giao thức định tuyến chuẩn IPv6 hoặc giao thức định tuyến 6LoWPAN. Một thiết bị trong mạng 6LoWPAN có thể là Host hoặc Router:
- **Host:** Là thiết bị đầu cuối không có chức năng chuyển tiếp gói tin đến các thiết bị khác trong mạng.
- **Router:** Là thiết bị có chức năng định tuyến chuyển tiếp gói tin giữa các nút mạng 6LoWPAN.

##### 3.2.1.2. Mô hình phân lớp các tầng giao thức trong 6LoWPAN

**Hình 3.12.** Mô hình phân lớp các tầng giao thức trong 6LoWPAN [3]

Hình 3.12 mô tả mô hình phân lớp các tầng giao thức trong 6LoWPAN. Tầng ứng dụng (Application Layer) bao gồm các giao thức ứng dụng phổ biến như CoAP, MQTT, HTTP... Tầng giao vận (Transport Layer) hỗ trợ UDP và TCP. Tầng mạng (Network Layer) sử dụng giao thức IPv6 cùng với giao thức định tuyến RPL. Tầng thích ứng (Adaptation Layer) nằm giữa tầng mạng và tầng liên kết dữ liệu, thực hiện chức năng nén tiêu đề IPv6 và phân mảnh gói tin để phù hợp với kích thước gói tin của chuẩn IEEE 802.15.4 (tối đa 127 byte). Tầng liên kết dữ liệu (Data Link Layer - MAC) và tầng vật lý (Physical Layer - PHY) tuân theo tiêu chuẩn IEEE 802.15.4.

## Trang 62


Đặc biệt, từ phiên bản năm 2006, có hai cải tiến mới cho IEEE 802.15.4 là e và g, trong đó IEEE 802.15.4e là một MAC được cải tiến và cung cấp nhiều cơ chế nâng cấp như Time Slotted Channel Hopping (TSCH) và Coordinated Sampled Listening (CSL), cả hai cơ chế này đều hỗ trợ hoạt động tiết kiệm năng lượng. Chuẩn IEEE 802.15.4g là một cải tiến tầng PHY với mục đích ứng dụng trong các mạng tiện ích thông minh (Smart Utility Networks - SUN).

Tầng thích ứng (Adaptation layer) trong bộ giao thức 6LoWPAN chịu trách nhiệm thực hiện 3 cơ chế quan trọng:
- **Nén tiêu đề (Header Compression):** Do tiêu đề IPv6 chuẩn có kích thước cố định là 40 byte, trong khi kích thước MTU tối đa của IEEE 802.15.4 chỉ là 127 byte (sau khi trừ đi tiêu đề MAC còn khoảng 81-102 byte cho tải trọng), nếu giữ nguyên tiêu đề IPv6 sẽ chiếm gần một nửa tải trọng của khung truyền. Tầng thích ứng sử dụng các kỹ thuật nén tiêu đề theo RFC 4944 và RFC 6282 để nén tiêu đề IPv6 xuống còn vài byte (tối thiểu là 2-7 byte).
- **Phân mảnh và ghép mảnh (Fragmentation and Reassembly):** Tiêu chuẩn IPv6 yêu cầu mọi liên kết phải hỗ trợ kích thước gói tin MTU tối thiểu là 1280 byte. Vì khung truyền IEEE 802.15.4 không thể chứa trực tiếp một gói tin 1280 byte, tầng thích ứng phải chia gói tin IPv6 thành nhiều mảnh nhỏ ở phía gửi và ghép chúng lại ở phía nhận trước khi đưa lên tầng mạng IPv6.
- **Định tuyến mức liên kết (Mesh Routing / Layer-two Routing):** Hỗ trợ truyền gói tin qua nhiều chặng ở tầng liên kết dữ liệu khi cần thiết (Mesh-Under).

## Trang 63


##### 3.2.1.3. Cấu trúc gói tin của chuẩn mạng 6LoWPAN

**Hình 3.13.** Cấu trúc gói tin IPv6 và 6LoWPAN [3]

Tiêu đề IPv6 chuẩn bao gồm các trường: Version (4 bit), Traffic Class (8 bit), Flow Label (20 bit), Payload Length (16 bit), Next Header (8 bit), Hop Limit (8 bit), Source Address (128 bit = 16 byte), và Destination Address (128 bit = 16 byte). Tổng cộng tiêu đề IPv6 cố định chiếm 40 byte.

Khi truyền qua mạng 6LoWPAN, kỹ thuật nén tiêu đề LOWPAN_IPHC (theo RFC 6282) khai thác các đặc điểm liên kết cục bộ và địa chỉ MAC sẵn có để nén tiêu đề:
- Nếu địa chỉ IPv6 nguồn hoặc đích có tiền tố liên kết cục bộ (Link-Local: `FE80::/64`) hoặc tiền tố mạng đã biết trước, tiền tố đó có thể được lược bỏ hoàn toàn.
- Phần định danh giao diện (IID - Interface Identifier) 64 bit có thể được suy ra trực tiếp từ địa chỉ MAC 64 bit (hoặc 16 bit ngắn) của tầng liên kết IEEE 802.15.4, do đó không cần truyền trong tiêu đề gói tin.
- Các trường Traffic Class và Flow Label nếu bằng 0 có thể được nén bỏ.
- Trường Next Header có thể được nén thành vài bit nếu mang giá trị phổ biến như UDP, TCP hoặc ICMPv6.

Nhờ đó, tiêu đề IPv6 từ 40 byte có thể được nén xuống chỉ còn 2 đến 7 byte trong các tình huống truyền dữ liệu thông thường.

## Trang 64


**Hình 3.14.** Cách bố trí các header để truyền dữ liệu trong mạng 6LoWPAN [4]

Hình 3.14 mô tả cách bố trí các tiêu đề (header) khi đóng gói dữ liệu:
- Gói tin chưa phân mảnh gồm: Tiêu đề IEEE 802.15.4 MAC, tiêu đề nén 6LoWPAN (IPHC), tiêu đề UDP nén, và tải trọng ứng dụng (Payload).
- Trong trường hợp gói tin IPv6 lớn hơn MTU của IEEE 802.15.4, gói tin sẽ được phân mảnh:
  - Mảnh đầu tiên (First Fragment): chứa tiêu đề IEEE 802.15.4, tiêu đề phân mảnh (Fragment Header: Datagram Size, Datagram Tag), tiêu đề nén IPv6, tiêu đề UDP và phần đầu của dữ liệu.
  - Các mảnh tiếp theo (Subsequent Fragments): chứa tiêu đề IEEE 802.15.4, tiêu đề phân mảnh (Datagram Size, Datagram Tag, Datagram Offset) và phần dữ liệu kế tiếp.

##### 3.2.1.4. Nền tảng hiện thực bộ giao thức 6LoWPAN

Bộ giao thức 6LoWPAN hiện nay được hỗ trợ rộng rãi trên nhiều hệ điều hành và nền tảng phần cứng IoT:
- **Hệ điều hành mạng nhúng:** Contiki OS (với chồng giao thức uIPv6 / ContikiMAC), TinyOS (với BLIP - Berkeley Low-power IP Stack), RIOT OS, FreeRTOS, Zephyr OS.
- **Nền tảng phần cứng:** Các vi điều khiển hỗ trợ chuẩn IEEE 802.15.4 như TI CC2538, CC2650, CC1352, Atmel SAMR21, Nordic Semiconductor nRF52840, và các module OpenMote.

## Trang 65


#### 3.2.2. Bộ giao thức Zigbee

##### 3.2.2.1. Kiến trúc mạng Zigbee

Mạng Zigbee có 3 nhóm thiết bị logic (theo chức năng):
- **Thiết bị điều phối mạng (Coordinator - ZC):** Mỗi mạng Zigbee chỉ có duy nhất một Coordinator. Thiết bị này có trách nhiệm khởi tạo mạng, lựa chọn tần số và PAN ID (Personal Area Network Identifier), cho phép các thiết bị khác gia nhập mạng, lưu trữ thông tin cấu hình mạng và bảng định tuyến. Coordinator luôn luôn hoạt động (mains-powered).
- **Bộ định tuyến (Router - ZR):** Thiết bị định tuyến có chức năng chuyển tiếp gói tin giữa các nút trong mạng, mở rộng phạm vi bao phủ của mạng Zigbee. Router có thể cho phép các nút con (End Devices hoặc Router khác) kết nối vào mình và quản lý truyền thông cho các nút con đó. Router thường được cấp nguồn liên tục.
- **Thiết bị đầu cuối (End Device - ZED):** Là các thiết bị cảm biến hoặc cơ cấu chấp hành hoạt động bằng pin, chỉ giao tiếp trực tiếp với nút cha của nó (Coordinator hoặc Router). Thiết bị đầu cuối không có chức năng chuyển tiếp dữ liệu cho các nút khác. Khi không có dữ liệu cần truyền nhận, End Device có thể chuyển sang chế độ ngủ sâu (sleep mode) để tiết kiệm năng lượng tối đa.

**Hình 3.15.** Mô hình một mạng Zigbee

## Trang 66


- Router được nhận một địa chỉ (địa chỉ ngắn - Short Address) là hằng số, có thể được sử dụng trong truyền điểm - điểm.
- Kể cả khi Coordinator bị ngắt điện, Router vẫn có thể duy trì mạng lưới, vì vậy giữa Router và Router vẫn có thể giao tiếp được.

Khi một nút được thêm vào ngay cả khi Coordinator bị ngắt điện, nó vẫn có thể thông qua các địa chỉ của Router hiện hữu để tham gia vào mạng lưới. Hình 3.15 mô tả về một mạng Zigbee bao gồm 1 Coordinator, 6 Router và một số End Devices.

##### 3.2.2.2. Mô hình phân lớp các tầng giao thức trong chuẩn không dây Zigbee

**Hình 3.16.** Các chồng giao thức tham chiếu giữa 802.15.4 và Zigbee

Trong Hình 3.16, lớp vật lý (PHY) và lớp MAC tuân theo chuẩn IEEE 802.15.4, các lớp phía trên bao gồm Tầng mạng (Network Layer - NWK), Tầng hỗ trợ ứng dụng (Application Support Sublayer - APS), và Đối tượng thiết bị Zigbee (Zigbee Device Objects - ZDO) cùng Khung ứng dụng (Application Framework) được định nghĩa bởi Liên minh Zigbee (Zigbee Alliance).

**Lớp vật lý (PHY)**
Theo chuẩn IEEE 802.15.4, đường truyền không dây có thể hoạt động ở 3 tần số không chính thức sau: 868MHz, 902-

## Trang 67


928MHz và 2.4GHz. Dựa trên các dải tần đó, tiêu chuẩn IEEE 802.15.4 định nghĩa 3 dạng lớp vật lý sau:
- Trải phổ chuỗi trực tiếp dùng BPSK hoạt động ở dải tần số 868MHz, tốc độ dữ liệu xấp xỉ 20kbps.
- Trải phổ chuỗi trực tiếp dùng BPSK hoạt động ở dải tần số 915MHz, tốc độ dữ liệu xấp xỉ 40kbps.
- Trải phổ chuỗi trực tiếp dùng O-QPSK hoạt động ở dải tần số 2.4GHz, tốc độ dữ liệu xấp xỉ 250kbps.

Cấu trúc khung dữ liệu của lớp vật lý IEEE 802.15.4 được mô tả ở hình sau:

**Hình 3.17.** Cấu trúc frame của chuẩn 802.15.4

Trong Hình 3.17, trường đầu tiên của frame gồm 32 bit preamble (đồng bộ hóa) dùng cho đồng bộ ký tự. Trường tiếp theo là SFD (Start of Frame Delimiter) có độ dài 1 byte đánh dấu điểm bắt đầu của phân giải gói. Trường Frame Length 8 bit kế tiếp xác định chiều dài của đơn vị dữ liệu trong lớp PHY (PSDU). Trường PSDU mang tối đa 127 bytes dữ liệu.

**Lớp MAC**
Các thông số lớp MAC theo tiêu chuẩn IEEE 802.15.4 được thiết kế cho các ứng dụng yêu cầu tốc độ dữ liệu thấp và độ trễ vừa phải. Các thông số MAC layer 802.15.4 có nhiều điểm đáp ứng cho yêu cầu về khả năng phân bố mạng một cách mềm dẻo và công suất thấp. Một số đặc điểm như sau:
- Cung cấp thiết bị mạng và cấu hình mạng đa dạng.
- Cấu trúc siêu khung thay đổi được phù hợp cho điều khiển chu kỳ nhiệm vụ các thiết bị mạng.

## Trang 68


- Truyền dữ liệu trực tiếp hoặc gián tiếp.
- Giao thức điều khiển truy cập môi trường dựa trên lập lịch và đụng độ.
- Quản lý hiệu quả năng lượng để tăng tuổi thọ của mạng.
- Dễ dàng triển khai cho mạng cỡ lớn.

##### 3.2.2.3. Cấu trúc frame của chuẩn 802.15.4

**Hình 3.18.** Cấu trúc superframe của 802.15.4

Chuẩn IEEE 802.15.4 định nghĩa một cấu trúc superframe theo yêu cầu: superframe bắt đầu bằng beacon (báo hiệu) và được chia thành 16 khe như nhau, được mô tả trong Hình 3.18. Khe thời gian đầu tiên của siêu khung dùng để phát beacon. Các khe còn lại được dùng bởi các thiết bị tranh chấp để thông tin trong thời gian truy cập tranh chấp (Contention Access Period - CAP). Các thiết bị dùng giao thức CSMA/CA phân khe thời gian để tranh chấp truy cập với các thiết bị khác. Việc thông tin giữa các thiết bị phải hoàn thành trước khi kết thúc CAP của superframe hiện tại và bắt đầu phát beacon của superframe kế tiếp.

Tiêu chuẩn IEEE 802.15.4 quy định MAC frame gồm 3 thành phần: MAC header, MAC payload và MAC footer như trong Hình 3.19. MAC header gồm trường điều khiển frame và trường địa chỉ. MAC payload chứa dữ liệu cần trao đổi, và MAC footer chứa các trường kiểm tra frame.

## Trang 69


**Hình 3.19.** Data Frame trong chuẩn 802.15.4

IEEE 802.15.4 cũng định nghĩa 4 dạng frame cơ bản: beacon frame, frame dữ liệu, frame xác nhận ACK và MAC command frame:
- **Beacon frame:** Được bộ điều phối mạng phát theo chu kỳ để xác nhận mạng và cấu trúc mạng, đánh thức các thiết bị từ trạng thái ngủ và đồng bộ hoạt động mạng. Beacon frame rất quan trọng trong cấu hình mô mạng Mesh và Tree. Chúng hỗ trợ cho tất cả các nút mạng đồng bộ mà không cần các nút phải hoạt động ở chế độ tích cực trong thời gian dài.
- **Data frame:** Có thể dài tới 104 octets dữ liệu (1 octet = 1 byte). Mỗi frame dữ liệu mang một chuỗi số thứ tự xác nhận. Chuỗi số đảm bảo tất cả các khung được đếm và nhận hợp lệ. Trường FCS (checksum) dùng để phát hiện lỗi frame.
- **ACK frame:** Thiết bị nhận gửi frame ACK tương ứng cho phía phát để thông báo frame dữ liệu nhận được là hợp lệ và không có lỗi.
- **MAC command frame:** Được dùng để thông báo và thông tin phục vụ mục đích quản lý mạng tập trung để điều khiển và cấu hình thiết bị từ xa. Nhóm lệnh bao gồm phối hợp thiết bị, yêu cầu dữ liệu, thông báo PAN ID, yêu cầu beacon, GTS, tổ chức lại coordinator.

Thiết kế lớp giao thức MAC rất quan trọng trong mạng WSNs, nó đảm bảo hiệu quả sử dụng năng lượng để kéo dài thời gian sống của mạng, tạo nên khả năng mở rộng phù hợp kích thước mạng, mật độ node và cấu hình mạng. Các thuộc tính quan trọng khác cần lưu ý của thiết kế giao thức MAC là sự công bằng giữa các node, giảm độ trễ, hạn chế lưu lượng cao của băng thông.

## Trang 70


##### 3.2.2.4. Một số đặc điểm của chuẩn Zigbee trong ứng dụng mạng cảm biến không dây

Đặc điểm của công nghệ này là tốc độ truyền tin thấp, nhưng tiêu hao ít năng lượng và là giao thức mạng không dây hướng tới các ứng dụng điều khiển từ xa và tự động hóa trong công nghệ IoT (Internet of Things) trong tương lai. Zigbee có thể dùng trong các mạng lưới rộng hơn là sử dụng Bluetooth. Các thiết bị không dây sử dụng công nghệ Zigbee có thể truyền tin trong khoảng cách từ vài mét đến vài chục mét tùy thuộc vào môi trường truyền tin và mức công suất được yêu cầu ở mỗi ứng dụng. Tốc độ dữ liệu là 250kbps ở dải băng tần 2.4GHz được sử dụng rộng rãi. Các dữ liệu được truyền theo gói, gói tối đa là 128 bytes cho phép tải trọng tối đa 104 bytes.

**Zigbee có độ tin cậy cao**

Thực tế, sự truyền thông không dây là không tin cậy. Chứng minh điều này bằng việc đi lòng vòng với một chiếc điện thoại di động, sau đó bước vào thang máy. Bất cứ ai sử dụng điện thoại đều gặp sự cố cuộc gọi bị ngắt hoặc đường truyền yếu. Tất cả bởi vì sóng radio cũng chỉ là các sóng. Chúng chạy qua các vật cản, có thể bị chặn bởi kim loại, nước hoặc khối bê tông và phụ thuộc vào nhiều yếu tố phức tạp gồm thiết kế ăng-ten, sự khuếch đại năng lượng và thậm chí các điều kiện thời tiết.

Tuy nhiên, điều khiển không dây thường không có cùng vấn đề như trong một cuộc điện thoại, di chuyển để tìm điểm nhận sóng tốt hơn hay đợi để thử lại sau. Hiệp hội Zigbee hiểu điều này, giao thức Zigbee được thiết kế với độ tin cậy cao. Điều này được thể hiện trong các đặc tả Zigbee:
- IEEE 802.15.4 với O-QPSK và DSSS.
- CSMA-CA.
- 16-bit CRCs.
- ACK tại mỗi hop (chặng).
- Việc nối mạng lưới (mesh) để tìm ra đường đi tin cậy.
- End-to-end ACK để kiểm tra dữ liệu đến đích.

## Trang 71


Điều đầu tiên là dựa vào một kỹ thuật không dây rất tin cậy, khoảng cách thấp và dùng sự đặc tả IEEE 802.15.4. Đặc tả này là một kỹ thuật radio mạnh, rất hiện đại được xây dựng trên 40 năm kinh nghiệm của IEEE. Nó dùng Offset-Quadrature Phase-Shift Keying (O-QPSK) và Direct Sequence Spread Spectrum (DSSS), một sự kết hợp của các kỹ thuật nhằm cung cấp hiệu suất tín hiệu trên nhiễu (Signal-to-Noise Ratio - SNR) rất cao ở công suất truyền phát thấp.

Thứ hai, chuẩn IEEE 802.15.4 định nghĩa cơ chế đa truy cập cảm nhận sóng mang tránh xung đột (CSMA-CA). Trước khi truyền tin, thiết bị lắng nghe kênh truyền để đảm bảo không có thiết bị nào khác đang phát sóng, qua đó giảm thiểu va chạm dữ liệu trên môi trường truyền.

Thứ ba, mỗi khung truyền đều đi kèm mã kiểm tra độ dư thừa vòng 16 bit (16-bit CRC) trong trường FCS. Phía nhận thực hiện kiểm tra CRC trên toàn bộ khung dữ liệu; nếu phát hiện sai sót bit, khung truyền sẽ bị hủy bỏ ngay lập tức.

Thứ tư, cơ chế báo nhận (ACK) tại mỗi hop đảm bảo tính toàn vẹn của việc truyền tin giữa hai nút kế cận. Nếu phía phát không nhận được ACK trong một khoảng thời gian chờ định trước, nó sẽ tự động phát lại khung tin (lên tới số lần truyền lại tối đa quy định).

Thứ năm, kiến trúc định tuyến mạng lưới (mesh networking) với thuật toán AODV cho phép các gói tin tự động tìm đường vòng qua các nút trung gian khác nếu một nút hoặc liên kết trên đường đi chính bị hỏng hoặc nghẽn.

## Trang 72


Thêm vào đó, Zigbee cung cấp việc broadcast tin cậy. Zigbee cũng cung cấp multicasting có thể gửi một message đến một nhóm các nút trong mạng.

Cuối cùng, Zigbee cung cấp tự động ACK end-to-end. Ứng dụng nguồn có thể yêu cầu một xác nhận mức ứng dụng từ nút đích cuối cùng để đảm bảo rằng gói tin không chỉ đến được nút mạng mà còn được xử lý thành công bởi ứng dụng đích.

**Bảo mật trong Zigbee**

Bên cạnh độ tin cậy, bảo mật là một yếu tố sống còn đối với các hệ thống điều khiển tự động hóa và IoT:
- Zigbee sử dụng thuật toán mã hóa tiêu chuẩn tiên tiến AES-128 (Advanced Encryption Standard với độ dài khóa 128 bit) để bảo vệ tính bảo mật của dữ liệu.
- Tính toàn vẹn của thông điệp được đảm bảo thông qua mã xác thực thông điệp CBC-MAC (Cipher Block Chaining Message Authentication Code) gắn kèm gói tin.
- Cơ chế chống phát lại (Replay Protection) sử dụng số thứ tự khung tuần tự (Frame Counter) để ngăn chặn kẻ tấn công ghi lại và phát lại các gói tin hợp lệ nhằm chiếm quyền điều khiển hệ thống.
- Zigbee hỗ trợ 3 loại khóa bảo mật chính: Master Key (dùng để thiết lập các khóa khác), Network Key (dùng chung cho toàn bộ các nút trong mạng), và Link Key (dùng riêng biệt giữa hai nút cụ thể để bảo mật thông tin liên lạc ngang hàng).

## Trang 73


Hiệp hội Zigbee đã quyết định giữ giao thức trong một môi trường tốc độ truyền dữ liệu thấp.

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
| 3 | ZBOSS 3.0 | https://dsr-zboss.com |

## Trang 74


#### 3.2.3. Bộ giao thức WiFi 802.11

##### 3.2.3.1. Kiến trúc mạng WiFi 802.11

Mạng không dây theo chuẩn kết nối 802.11 có thể hoạt động theo kiến trúc dựa theo hạ tầng mạng (infrastructure-based) hoặc kiến trúc không hạ tầng, kết nối không dây trực tiếp giữa các thiết bị với nhau (ad-hoc).

Kiến trúc mạng theo hạ tầng bao gồm các thành phần: thiết bị đầu cuối (station - STA), thiết bị điểm truy cập (access point - AP). Các thiết bị đầu cuối kết nối với một điểm truy cập cùng một tần số tạo nên một tập dịch vụ cơ bản (Basic Service Set - BSS). Hình 3.20 minh họa kiến trúc mạng 802.11 dựa trên kiến trúc hạ tầng.

**Hình 3.20.** Minh họa mạng 802.11 theo kiến trúc hạ tầng

Kiến trúc không dựa theo hạ tầng (adhoc-based) là kiến trúc mạng mà các thiết bị không dây đầu cuối kết nối trực tiếp với nhau, truyền dữ liệu trực tiếp cho nhau mà không cần thông qua một hạ tầng mạng phân phối. Các thiết bị đầu cuối này kết nối lại với nhau tạo thành một nhóm dịch vụ cơ bản độc lập (IBSS), trao đổi dữ liệu trên cùng tần số radio. Hình 3.21 minh họa hai nhóm dịch vụ cơ bản kết nối theo mô hình mạng Ad-hoc (adhoc network).

**Hình 3.21.** Minh họa mạng 802.11 theo kiến trúc ad-hoc

## Trang 75


##### 3.2.3.2. Mô hình phân lớp tầng giao thức trong chuẩn không dây 802.11

**Hình 3.22.** Ánh xạ 802.11 trong mô hình OSI

Chuẩn IEEE 802.11 được xây dựng cho mạng cục bộ không dây bao gồm hai tầng con là tầng PHY và tầng MAC trong mô hình OSI. Tầng LLC (Logic Link Control) được mô tả trong chuẩn 802.2. Với các tầng mức cao hơn, kiến trúc phân tầng cung cấp một giao diện trong suốt (nghĩa là không có sự thay đổi đối với các ứng dụng mức cao hơn). Vì vậy, với các tầng từ LLC trở lên có thể hoán chuyển các trạm đang hoạt động mạng WLAN với các mạng cục bộ khác. Hình 3.22 mô tả kiến trúc của WLAN trong mô hình OSI. Điều này cho phép giao thức TCP/IP hiện tại có thể hoạt động dựa trên mạng IEEE 802.11 WLAN giống như hoạt động triển khai trên một mạng có dây Ethernet.

Hình 3.23 mô tả sự khác biệt về các chuẩn hoạt động dựa trên chuẩn 802 WLAN ở tầng PHY và tầng MAC.

## Trang 76


Trong Hình 3.23, ở tầng PHY sẽ gồm các tuỳ chọn phát sóng: InfraRed (IR), Frequency Hopping Spread Spectrum (FHSS) và Direct Sequence Spread Spectrum (DSSS). Tất cả các tuỳ chọn ban đầu đều hỗ trợ tốc độ 1 và 2Mbps. Năm 1999, tổ chức IEEE định nghĩa ra hai chuẩn tốc độ cao mở rộng tương ứng với hai chuẩn 802.11b (hoạt động ở băng tần 2.4GHz, tốc độ 11Mbps) và chuẩn 802.11a (hoạt động ở băng tần 5GHz, tốc độ lên đến 54Mbps, dựa trên công nghệ Orthogonal Frequency Division Multiplexing - OFDM). Gần đây, chuẩn 802.11g được đưa ra. Đây là một chuẩn mở rộng của chuẩn 802.11b trong đó hỗ trợ tốc độ truyền lên đến 54Mbps và vẫn hoạt động ở băng tần 2.4GHz.

**Hình 3.23.** Các giao thức sử dụng trong hệ thống mạng cục bộ không dây dựa trên chuẩn IEEE 802.11 của tầng vật lý (PHY layer) và tầng điều khiển truy cập môi trường truyền (MAC layer)

## Trang 77


##### 3.2.3.3. Cấu trúc frame của chuẩn không dây 802.11

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
IEEE đã mở rộng trên chuẩn 802.11 gốc vào tháng 7 năm 1999, đó chính là chuẩn 802.11b. Chuẩn này hỗ trợ băng thông lên đến 11Mbps, tương đương với Ethernet truyền thống. 802.11b sử dụng tần số vô tuyến (2.4GHz) giống như chuẩn ban đầu.

## Trang 78


Các hãng sản xuất thích sử dụng tần số 2.4GHz này để chi phí sản xuất của họ được giảm. Các thiết bị 802.11b có thể bị xuyên nhiễu từ các thiết bị điện thoại không dây (kéo dài), lò vi sóng hoặc các thiết bị khác sử dụng cùng dải tần 2.4GHz. Mặc dù vậy, bằng cách cài đặt các thiết bị 802.11b cách xa các thiết bị như vậy có thể giảm được hiện tượng xuyên nhiễu này.

**Ưu điểm của 802.11b:** Giá thành rẻ; phạm vi tín hiệu tốt và không dễ bị che khuất.
**Nhược điểm của 802.11b:** Tốc độ tối đa thấp nhất; các thiết bị trong gia đình có thể làm xuyên nhiễu với băng tần này.

**802.11a**
Trong khi 802.11b vẫn đang được phát triển, IEEE đã tạo một mở rộng thứ cấp cho chuẩn 802.11 có tên gọi 802.11a. Vì 802.11b được sử dụng rộng rãi quá nhanh so với 802.11a, nên một số người cho rằng 802.11a được tạo sau 802.11b. Tuy nhiên trong thực tế, 802.11a và 802.11b được tạo một cách đồng thời. Do giá thành cao hơn nên 802.11a chỉ được sử dụng trong các mạng doanh nghiệp còn 802.11b thích hợp hơn với thị trường mạng gia đình.

802.11a hỗ trợ băng thông lên đến 54Mbps và sử dụng tần số vô tuyến 5GHz. Tần số của 802.11a cao hơn so với 802.11b, chính vì vậy đã làm cho phạm vi của hệ thống này hẹp hơn so với các mạng 802.11b. Với tần số này, các tín hiệu 802.11a khó xuyên qua các vách tường và các vật cản khác hơn.

Do 802.11a và 802.11b sử dụng các tần số khác nhau nên hai công nghệ này không thể tương thích với nhau. Chính vì vậy, một số hãng đã cung cấp các thiết bị mạng hybrid cho 802.11a/b nhưng các sản phẩm này chỉ đơn thuần là bổ sung thêm hai chuẩn này.

**Ưu điểm của 802.11a:** Tốc độ cao; tần số 5GHz tránh được sự xuyên nhiễu từ các thiết bị khác.
**Nhược điểm của 802.11a:** Giá thành đắt; phạm vi hẹp và dễ bị che khuất.

## Trang 79


**802.11g**
Vào năm 2002 và 2003, các sản phẩm WLAN hỗ trợ một chuẩn mới hơn đó là 802.11g, được đánh giá cao trên thị trường. 802.11g thực hiện sự kết hợp tốt nhất giữa 802.11a và 802.11b. Nó hỗ trợ băng thông lên đến 54Mbps và sử dụng tần số 2.4GHz để có phạm vi rộng. 802.11g có khả năng tương thích với các chuẩn 802.11b, điều đó có nghĩa là các điểm truy cập 802.11g sẽ làm việc với các adapter mạng không dây 802.11b và ngược lại.

**Ưu điểm của 802.11g:** Tốc độ cao; phạm vi tín hiệu tốt và ít bị che khuất.
**Nhược điểm của 802.11g:** Giá thành đắt hơn 802.11b; các thiết bị có thể bị xuyên nhiễu từ nhiều thiết bị khác sử dụng cùng băng tần.

**802.11n**
802.11n hay còn được gọi là WiFi 4, được chuẩn hóa vào năm 2009. Đây là chuẩn được thiết kế để cải thiện cho 802.11g trong tổng số băng thông được hỗ trợ bằng cách tận dụng nhiều tín hiệu không dây và các anten (công nghệ Multi Input Multi Output - MIMO).

Khi chuẩn này được đưa ra, các kết nối 802.11n hỗ trợ tốc độ dữ liệu lên đến 100Mbps (lý thuyết lên tới 600Mbps). 802.11n cũng cung cấp phạm vi bao phủ tốt hơn so với các chuẩn Wi-Fi trước nó nhờ cường độ tín hiệu mạnh của nó. Thiết bị 802.11n tương thích với các thiết bị 802.11g và 802.11b.

**Ưu điểm của 802.11n:** Tốc độ nhanh và phạm vi tín hiệu tốt nhất; khả năng chịu đựng tốt hơn từ việc xuyên nhiễu từ các nguồn bên ngoài.
**Nhược điểm của 802.11n:** Giá thành đắt hơn 802.11g; sử dụng tín hiệu có thể gây nhiễu với các mạng 802.11b/g ở gần.

**802.11ac**
802.11ac được Liên minh WiFi chuẩn hóa vào năm 2013, còn được gọi là WiFi 5. 802.11ac được kế thừa từ chuẩn 802.11n trước đó.

## Trang 80


So với 802.11n, 802.11ac có độ rộng kênh truyền lớn hơn (80 hoặc 160MHz so với 40MHz) trong dải băng tần 5GHz, nhiều luồng không gian hơn (8 so với 4) và điều chế bậc cao hơn (256-QAM so với 64-QAM) và bổ sung tính năng Multi User - Multi Input Multi Output (MU-MIMO). Tính năng này cho phép các điểm truy cập phát nhiều chùm tia đến từng máy trạm. Từ đó, giảm thiểu được việc đụng độ giữa các máy trạm và tăng thông lượng tổng thể.

Liên minh WiFi đã tách việc phát triển 802.11ac thành hai pha, được đặt tên là Wave 1 và Wave 2. Các sản phẩm 802.11ac Wave 1 được sản xuất từ năm 2013 và đến năm 2016 các sản phẩm Wave 2 được đưa ra thị trường nhằm bổ sung các tính năng mới của 802.11ac như băng thông cao hơn, MU-MIMO, độ rộng kênh 160MHz, hỗ trợ nhiều kênh tại băng tần 5GHz, tăng luồng (4 anten so với 3 anten của 802.11ac Wave 1).

**Ưu điểm của 802.11ac:** So với các chuẩn trước, 802.11ac sử dụng băng tần kép 2.4GHz và 5GHz nên tốc độ truyền cao hơn, ít nhiễu hơn.
**Nhược điểm của 802.11ac:** Do sử dụng băng tần 5GHz nên mức suy hao tín hiệu cao hơn so với 2.4GHz khi qua vật cản.

**802.11ax**
Chuẩn 802.11ax được kế thừa từ 802.11ac, và được IEEE chuẩn hóa vào tháng 9 năm 2020, còn được gọi là WiFi 6. Mục tiêu của 802.11ax là cung cấp thông lượng lên gấp 4 lần so với 802.11ac ở mức người dùng, trong khi tốc độ dữ liệu chỉ tăng 37% ở mức vật lý. 802.11ax sử dụng kỹ thuật ghép kênh OFDMA, mỗi máy trạm được sử dụng các đơn vị tài nguyên khác nhau trong phạm vi khả dụng của điểm truy cập. 802.11ax cung cấp nhiều sóng mang hơn so với 802.11ac, cụ thể ở 802.11ax các kênh 20, 40, 80, và 160MHz có lần lượt 256, 512, 1024, và 2048 sóng mang con so với 64, 128, 256 và 512 sóng mang con trong 802.11ac.

**Ưu điểm của 802.11ax:** Tốc độ truyền cao hơn 40% so với 802.11ac, tối ưu cho nhiều người dùng trong cùng một thời điểm.

## Trang 81


Nhược điểm của 802.11ax do mới được chuẩn hóa nên thiết bị phát sóng và thiết bị đầu cuối hỗ trợ 802.11ax chưa có nhiều ngoài thị trường.

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
| 3 | WLAN drivers | Tùy thuộc loại phần cứng |

## Trang 82


## BÀI TẬP CHƯƠNG 3

1. Hãy liệt kê những kiến trúc mạng trong IoT và đưa ra ưu, nhược điểm của mỗi kiến trúc.
2. Hãy so sánh các bộ giao thức không dây được sử dụng trong IoT và liệt kê các ứng dụng cho từng bộ giao thức.
3. Hãy sử dụng kiến trúc Zigbee để xây dựng ứng dụng Giám sát chất lượng không khí.
4. Hãy sử dụng kiến trúc WLAN 802.11 để xây dựng ứng dụng Nhà thông minh.
5. Hãy thiết kế kiến trúc mạng cho ứng dụng Nông nghiệp thông minh áp dụng tại Việt Nam. Sau đó hãy chọn bộ giao thức mạng phù hợp với ứng dụng này và giải thích vì sao.
6. Hãy thiết kế kiến trúc mạng cho ứng dụng giám sát chất lượng không khí tại Thành phố Hồ Chí Minh. Sau đó hãy chọn bộ giao thức mạng phù hợp với ứng dụng này và giải thích vì sao.
7. Hãy trình bày ý tưởng cho ứng dụng giám sát giao thông thông minh sử dụng công nghệ 5G.

## Trang 83


# CHƯƠNG 4. CÁC NỀN TẢNG PHẦN CỨNG VÀ PHẦN MỀM IOT THÔNG DỤNG

Công nghệ IoT được phát triển để phục vụ cho nhiều lĩnh vực khác nhau trong cuộc sống, từ nông nghiệp, công nghiệp, y tế, giáo dục cho đến quản lý đô thị. Để xây dựng nên một hệ thống IoT hoàn chỉnh, các nhà phát triển cần phải kết hợp chặt chẽ giữa các nền tảng phần cứng và các nền tảng phần mềm phù hợp.

Mỗi ứng dụng IoT có những yêu cầu rất khác nhau về kích thước thiết bị, nguồn năng lượng cung cấp, năng lực tính toán, dung lượng bộ nhớ, khả năng kết nối mạng và độ trễ xử lý. Do đó, việc hiểu rõ các đặc tính kỹ thuật, ưu nhược điểm của các loại phần cứng cũng như các hệ điều hành chuyên dụng cho IoT là kiến thức nền tảng quan trọng giúp thiết kế và triển khai các hệ thống IoT hoạt động ổn định, hiệu quả và tối ưu chi phí.

Nội dung chương này trình bày tổng quan về các nền tảng phần cứng và phần mềm phổ biến trong IoT. Về phần cứng, chương này giới thiệu từ các mote cảm biến công suất siêu thấp (TelosB), các vi điều khiển mã nguồn mở thông dụng (Arduino, ESP8266, ESP32) cho đến các máy tính nhúng mạnh mẽ (Raspberry Pi). Về phần mềm, chương này phân tích kiến trúc và cơ chế hoạt động của các hệ điều hành mạng cảm biến nhúng chuyên dụng như TinyOS, Contiki cũng như hệ điều hành Linux nhúng đa năng Raspbian OS trên Raspberry Pi.

## Trang 84


Thông qua những nội dung được trình bày trong chương này, người đọc có cái nhìn tổng quan về các loại thiết bị phần cứng dùng trong IoT cũng như các giải pháp phần mềm tương ứng. Từ đó, trước nhu cầu triển khai một giải pháp IoT trong một ngữ cảnh cụ thể, với các yêu cầu cụ thể, nhà phát triển có thể chọn lựa một loại thiết bị, một môi trường phát triển ứng dụng phù hợp nhất.

### 4.1. Các nền tảng phần cứng

#### 4.1.1. Những đặc trưng và phân loại các nền tảng phần cứng dùng cho IoT

Trong hệ thống IoT, "Vạn vật" (Things) đề cập đến một tập hợp phong phú và đa dạng các đối tượng vật lý được gắn các cảm biến, cơ cấu chấp hành và bộ xử lý tính toán nhúng để có thể cảm nhận môi trường xung quanh, xử lý dữ liệu và trao đổi thông tin thông qua mạng Internet. Các thiết bị IoT có thể được phân loại theo nhiều tiêu chí khác nhau như năng lực tính toán, mức độ tiêu thụ năng lượng, kích thước bộ nhớ và khả năng kết nối mạng.

## Trang 85


mạng kết nối. Những đối tượng này có thể triển khai trên một mạng thông qua Bluetooth (IEEE 802.15.1), Zigbee (IEEE 802.15.4), Wi-Fi (IEEE 802.11), Ethernet (IEEE 802.3) hay các chuẩn giao tiếp khác.

Khả năng phát triển phần cứng và phần mềm cho IoT là vô tận. Phần cứng IoT có thể phân chia thành hai nhóm chính:
- **Nhóm thiết bị hạn chế tài nguyên (Constrained Devices):** Là các thiết bị có bộ vi điều khiển (MCU) 8-bit hoặc 16-bit, dung lượng bộ nhớ RAM từ vài kilobyte (kB) đến vài chục kB, bộ nhớ Flash từ vài chục kB đến vài trăm kB, hoạt động với nguồn năng lượng pin hạn chế. Nhóm này thường chạy các hệ điều hành siêu nhẹ như TinyOS, Contiki, FreeRTOS hoặc chạy firmware trực tiếp (bare-metal).
- **Nhóm thiết bị tính toán nhúng đa năng (Smart Gateway / Single-Board Computers):** Là các máy tính đơn bo mạch (SBC) trang bị bộ vi xử lý (MPU) 32-bit hoặc 64-bit đa nhân, bộ nhớ RAM từ hàng trăm megabyte (MB) đến vài gigabyte (GB), chạy hệ điều hành Linux nhúng đầy đủ (như Raspbian, Ubuntu Core). Nhóm này đóng vai trò là trạm điều khiển, cổng kết nối (IoT Gateway) hoặc nút tính toán cận biên (Edge Node).

Theo chuẩn RFC 7228 của IETF, các thiết bị IoT hạn chế tài nguyên được phân chia thành 3 lớp cơ bản:
- **Lớp 0 (Class 0 - C0):** Thiết bị rất hạn chế (RAM << 10 kB, Flash << 100 kB). Thiết bị không thể giao tiếp trực tiếp với Internet qua IPv6 mà phải thông qua Gateway hoặc trạm thu phát.
- **Lớp 1 (Class 1 - C1):** Thiết bị hạn chế (RAM ~ 10 kB, Flash ~ 100 kB). Có thể hỗ trợ các chồng giao thức mạng rút gọn như CoAP qua 6LoWPAN/UDP.
- **Lớp 2 (Class 2 - C2):** Thiết bị ít hạn chế hơn (RAM ~ 50 kB, Flash ~ 250 kB). Có thể hỗ trợ ngăn xếp TCP/IP đầy đủ và các giao thức bảo mật nhẹ.

## Trang 86


#### 4.1.2. Thiết bị cảm biến không dây TelosB

TelosB là loại thiết bị cảm biến không dây tiết kiệm năng lượng, được xếp vào loại thiết bị IoT thuộc lớp 0 như đã trình bày ở phần trên. Hình 4.1 là hình ảnh bề ngoài của thiết bị TelosB.

**Hình 4.1.** Mote cảm biến không dây TelosB [6]

Thiết bị TelosB (được phát triển ban đầu bởi UC Berkeley) là một nền tảng phần cứng mã nguồn mở tiêu chuẩn cho các nghiên cứu về mạng cảm biến không dây (WSN):
- **Bộ vi điều khiển:** TI MSP430F1611 16-bit RISC, xung nhịp 8MHz, 10kB RAM, 48kB ROM (Flash) và 1MB bộ nhớ Flash ngoài dùng lưu trữ dữ liệu.
- **Bộ thu phát không dây:** Chip RF Chipcon/TI CC2420 tương thích chuẩn IEEE 802.15.4 / Zigbee, hoạt động ở dải tần 2.4GHz với tốc độ truyền dữ liệu 250kbps, tích hợp ăng-ten onboard.
- **Cảm biến tích hợp:** Tích hợp sẵn cảm biến nhiệt độ và độ ẩm kỹ thuật số Sensirion SHT11, cảm biến ánh sáng nhìn thấy và toàn phổ Hamamatsu.
- **Giao tiếp lập trình:** Cổng USB tích hợp qua chip FTDI cho phép vừa lập trình, gỡ lỗi vừa nạp nguồn và giao tiếp dữ liệu nối tiếp với máy tính.
- **Hệ điều hành hỗ trợ:** TinyOS và Contiki OS.

#### 4.1.3. Thiết bị nhúng Arduino

Arduino là một nền tảng tạo mẫu điện tử mã nguồn mở dựa trên phần cứng và phần mềm linh hoạt, dễ sử dụng. Nền tảng Arduino bao gồm các bo mạch vi điều khiển với nhiều cấu hình khác nhau và môi trường phát triển tích hợp Arduino IDE.

## Trang 87


Bo mạch phổ biến nhất là **Arduino Uno R3**, sử dụng vi điều khiển ATmega328P:
- Vi điều khiển 8-bit AVR RISC với xung nhịp 16MHz.
- Bộ nhớ: 32kB Flash (trong đó 0.5kB dùng cho bootloader), 2kB SRAM và 1kB EEPROM.
- Giao tiếp I/O: 14 chân Digital I/O (trong đó 6 chân hỗ trợ PWM) và 6 chân Analog Input (độ phân giải ADC 10-bit).
- Cổng kết nối: Cổng USB Type-B để nạp chương trình và cấp nguồn, giắc cắm nguồn DC ngoài 7-12V, hỗ trợ các giao tiếp nối tiếp UART, SPI, I2C.

**Hình 4.2.** Mạch Arduino Uno R3

Ngoài Arduino Uno, hệ sinh thái Arduino còn có nhiều dòng bo mạch khác phục vụ các nhu cầu đa dạng:
- **Arduino Mega 2560:** Sử dụng vi điều khiển ATmega2560 với 256kB Flash, 8kB SRAM, 54 chân Digital I/O và 16 chân Analog Input, phù hợp cho các dự án phức tạp cần nhiều chân kết nối.
- **Arduino Nano / Pro Mini:** Kích thước siêu nhỏ gọn, phù hợp tích hợp vào các thiết bị IoT yêu cầu tiết kiệm diện tích.
- **Arduino Yún:** Kết hợp vi điều khiển ATmega32u4 với một vi xử lý Atheros AR9331 (MIPS @ 400MHz) chạy hệ điều hành Linux OpenWrt-Yun, hỗ trợ kết nối Wi-Fi và Ethernet.

## Trang 88


Bên cạnh các dòng Arduino truyền thống, sự xuất hiện của các module Wi-Fi giá rẻ tương thích với môi trường Arduino IDE như ESP8266 và ESP32 của hãng Espressif Systems đã tạo nên bước phát triển nhảy vọt cho các ứng dụng IoT DIY và công nghiệp:
- **ESP8266 (NodeMCU, ESP-12E):** Sử dụng vi xử lý Tensilica Xtensa 32-bit LX106 @ 80/160MHz, tích hợp đầy đủ Wi-Fi 802.11 b/g/n, hỗ trợ giao thức TCP/IP, giá thành rất rẻ, dễ dàng kết nối trực tiếp vào mạng Internet.
- **ESP32:** Dòng vi điều khiển nâng cấp mạnh mẽ với vi xử lý 2 nhân Tensilica Xtensa 32-bit LX6 @ 160/240MHz, tích hợp cả Wi-Fi 802.11 b/g/n và Bluetooth kép (Bluetooth v4.2 BR/EDR và BLE), 520kB SRAM, hỗ trợ nhiều cổng ngoại vi ADC, DAC, I2C, SPI, UART, PWM, cảm biến chạm điện dung và mã hóa phần cứng (AES, RSA, SHA-2).

#### 4.1.4. Thiết bị máy tính nhúng Raspberry Pi

Raspberry Pi là dòng máy tính bảng đơn (Single-Board Computer - SBC) kích thước nhỏ bằng thẻ tín dụng, được phát triển tại Vương quốc Anh bởi Raspberry Pi Foundation nhằm mục đích thúc đẩy việc giảng dạy khoa học máy tính cơ bản tại các trường học và sau đó nhanh chóng trở thành nền tảng phổ biến bậc nhất cho các nhà phát triển hệ thống nhúng và IoT.

## Trang 89


**Raspberry Pi 3 Model B+** (ra mắt năm 2018):
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
- Hỗ trợ 2 cổng ra màn hình Micro-HDMI độ phân giải lên đến 4K @ 60fps.

## Trang 90


- Giải mã video phần cứng H.265 (4kp60 decode), H.264 (1080p60 decode, 1080p30 encode), hỗ trợ đồ họa OpenGL ES 3.0.
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
| **Kết nối mạng** | IEEE 802.15.4 / Zigbee (2.4GHz, 250kbps) | Cần shield gắn thêm (hoặc tích hợp Wi-Fi/BLE trên ESP) | Gigabit Ethernet, Wi-Fi Dual-band 802.11ac, Bluetooth 5.0 |

## Trang 91


| Đặc điểm | TelosB Mote | Arduino-based boards | Raspberry Pi |
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
- **Thành phần ứng dụng (Application Layer):** Cho phép lập trình viên xây dựng và thực thi các chương trình ứng dụng IoT phục vụ mục tiêu thu thập dữ liệu, xử lý và điều khiển cụ thể.

## Trang 92


**Hình 4.4.** Các thành phần chính của một hệ điều hành cho thiết bị IoT [5]

**Phân loại hệ điều hành cho thiết bị IoT**

Tương tự như sự đa dạng của nền tảng phần cứng, các hệ điều hành phát triển cho thiết bị IoT cũng rất đa dạng nhằm phục vụ tốt các ngữ cảnh ứng dụng cụ thể:
- **Event-driven OS (Hệ điều hành hướng sự kiện):** Đây là hướng tiếp cận phổ biến nhất cho các mạng cảm biến không dây tài nguyên rất hạn chế như TinyOS, Contiki. Mọi tác vụ xử lý trên hệ thống được kích hoạt bởi các sự kiện từ bên ngoài (ngắt phần cứng hoặc bộ định thời). Nhân hệ điều hành chỉ chạy một vòng lặp quản lý hàng đợi sự kiện, không cần duy trì ngăn xếp (stack) riêng cho từng tiến trình, giúp tiết kiệm bộ nhớ RAM tối đa và giảm độ phức tạp.
- **Multi-threading OS (Hệ điều hành đa luồng):** Tiếp cận theo mô hình truyền thống của hệ điều hành máy tính, mỗi luồng có ngăn xếp riêng và thực thi độc lập. Bộ lập lịch thực hiện chuyển đổi ngữ cảnh (context switch) giữa các luồng dựa theo độ ưu tiên hoặc phân chia thời gian. Mô hình này lập trình tự nhiên, dễ sử dụng nhưng tiêu tốn bộ nhớ RAM hơn cho các ngăn xếp luồng. Đại diện tiêu biểu gồm RIOT OS, FreeRTOS, NuttX, ChibiOS.
- **Pure RTOSs (Hệ điều hành thời gian thực thuần túy):** Tập trung vào việc đảm bảo tính xác định và thời gian đáp ứng nghiêm ngặt cho các ứng dụng công nghiệp, y tế hoặc xe tự hành. Các đại diện phổ biến là FreeRTOS, RTEMS, VxWorks, QNX.

## Trang 93


Trong đó, FreeRTOS là một đại diện mã nguồn mở được dùng rất phổ biến trên các vi điều khiển nhúng 32-bit như STM32 hay ESP32.

Nội dung tiếp theo trong chương này giới thiệu chi tiết một số hệ điều hành tiêu biểu được sử dụng trong các hệ thống IoT: TinyOS, Contiki và Raspbian OS.

#### 4.2.2. Hệ điều hành TinyOS

TinyOS là hệ điều hành mã nguồn mở, hướng sự kiện (event-driven), được thiết kế chuyên biệt cho các thiết bị mạng cảm biến không dây có tài nguyên bộ nhớ rất hạn chế (vi điều khiển 8-bit đến 16-bit, RAM vài kB) [7]. TinyOS được phát triển ban đầu tại Đại học UC Berkeley kết hợp với Intel Research.

Các ứng dụng trên TinyOS được lập trình bằng ngôn ngữ **nesC** (Network Embedded Systems C), một phần mở rộng của ngôn ngữ C hỗ trợ lập trình dựa trên thành phần (component-based) và hướng sự kiện [8]. TinyOS hỗ trợ giao tiếp mạng cảm biến thông qua chồng giao thức mạng BLIP (Berkeley Low-power IP Stack) hiện thực chuẩn 6LoWPAN và RPL.

##### 4.2.2.1. Cấu trúc một ứng dụng trên TinyOS

Một ứng dụng TinyOS bao gồm nhiều thành phần (component) liên kết với nhau thông qua các giao diện (interface) [9]. Kiến trúc nesC phân biệt rõ ràng giữa hai khái niệm:
- **Interface (Giao diện):** Định nghĩa hợp đồng giao tiếp giữa các thành phần, bao gồm các hàm lệnh (**commands**) do bên cung cấp (provider) hiện thực và các sự kiện (**events**) do bên sử dụng (user) hiện thực để xử lý kết quả báo về.
- **Component (Thành phần):** Bao gồm hai loại:
  - **Module:** Chứa mã nguồn thực thi bằng ngôn ngữ nesC (hiện thực các command và event).
  - **Configuration:** Định nghĩa cách nối dây (wiring) giữa các interface của các component với nhau để tạo thành ứng dụng hoàn chỉnh.

## Trang 94


**Hình 4.5.** Mô hình hoạt động dựa trên sự kiện của hệ điều hành TinyOS

Mô hình hoạt động của TinyOS dựa trên hai khái niệm xử lý cơ bản:
- **Tasks (Tác vụ):** Đại diện cho các đoạn tính toán dài hạn trong chương trình, được đưa vào hàng đợi FIFO và thực thi tuần tự theo cơ chế không ưu tiên chiếm quyền (non-preemptive). Task không thể chiếm quyền của Task khác nhưng có thể bị ngắt bởi Hardware Event.
- **Hardware Event Handlers (Trình xử lý sự kiện phần cứng):** Được kích hoạt khi có ngắt từ phần cứng (như bộ định thời đếm xong hoặc gói tin truyền thông đến). Các hàm xử lý ngắt thực thi ngay lập tức và có thể chiếm quyền của Task đang chạy để đảm bảo tính thời gian thực.

Một ứng dụng TinyOS viết bằng nesC gồm các tệp thành phần cơ bản [10]:
1. Tệp cấu hình ứng dụng cao nhất (Top-level Configuration, ví dụ `BlinkAppC.nc`).
2. Tệp module hiện thực logic ứng dụng (Module, ví dụ `BlinkC.nc`).
3. Các tệp giao diện (Interfaces, nếu tự định nghĩa mới).
4. Tệp Makefile để biên dịch chương trình.

## Trang 95


Mã nguồn của một tệp cấu hình ứng dụng mẫu (`BlinkAppC.nc`):

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

**Hình 4.6.** Mã nguồn mô tả sự kết nối giữa các module thành phần trong ứng dụng BlinkC

## Trang 96


##### 4.2.2.2. Các thành phần, dịch vụ cơ bản của TinyOS

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
- `T32khz`: Bộ định thời chạy theo xung nhịp thạch anh 32.768kHz.

## Trang 97


Đặc trưng của bộ định thời trong TinyOS phản ánh:
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

Nếu hàng đợi Task còn chỗ trống, `post` trả về `SUCCESS` và Task sẽ được thực thi khi bộ xử lý rảnh rỗi. Ngược lại, nếu hàng đợi bị đầy, `post` trả về `FAIL`.

## Trang 98


**Cấu trúc thông điệp và truyền thông trong TinyOS**

Giao tiếp không dây trong TinyOS xoay quanh kiểu dữ liệu thông điệp cơ bản `message_t`. Định dạng của `message_t` bao gồm 3 phần: tiêu đề (header), vùng dữ liệu tải trọng (payload) và phần chân (footer):

- Kích thước tải trọng tối đa của gói tin mặc định là 28 byte (được định nghĩa qua hằng số `TOSH_DATA_LENGTH = 28`). Lập trình viên có thể cấu hình lại khi biên dịch bằng tùy chọn `-DTOSH_DATA_LENGTH=x` trong Makefile. Nếu một gói tin vượt quá kích thước này, nó sẽ bị loại bỏ.
- Phần header chứa địa chỉ nguồn, địa chỉ đích, độ dài dữ liệu, chỉ số nhóm (group ID) và loại thông điệp Active Message (AM Type).
- Phần footer chứa các trường kiểm tra lỗi CRC và cờ báo nhận (ACK).

TinyOS cung cấp mô hình trừu tượng Active Message (AM) cho phép các ứng dụng phân biệt các luồng dữ liệu khác nhau thông qua trường định danh `am_id_t` (tương tự như số cổng port trong TCP/UDP).

**Hình 4.11.** Mô hình kiến trúc phần cứng của hệ điều hành TinyOS

## Trang 99


**Giao diện gửi tin (AMSend Interface)**

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
- `getPayload(msg, len)`: Lấy con trỏ trỏ đến vùng dữ liệu tải trọng của gói tin.

## Trang 100


**Giao diện nhận tin (Receive Interface)**

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

**Hình 4.14.** Giao diện Packet

## Trang 101


**Giao diện PacketAcknowledgements**

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
- **I-Frame (IEEE 802.15.4 Frame):** Tuân thủ hoàn toàn định dạng chuẩn IEEE 802.15.4, cho phép TinyOS chia sẻ kênh truyền và giao tiếp liên mạng với các hệ thống khác như 6LoWPAN. Mặc định trong TinyOS 2.x, ngăn xếp radio sử dụng định dạng I-Frame.

## Trang 102


**Ngăn xếp vô tuyến CC2420 (CC2420 Radio Stack)**

Ngăn xếp phần mềm CC2420 chứa nhiều lớp (layer) thành phần được xếp chồng lên nhau nằm giữa ứng dụng và phần cứng thu phát:

**Hình 4.16.** Kiến trúc lớp trong CC2420 Radio Stack

Mỗi lớp trong ngăn xếp cung cấp và sử dụng các giao diện chuẩn (`Send`, `Receive`, `SplitControl`). Các lớp chính bao gồm:
- **ActiveMessageP:** Lớp trên cùng, điền các trường tiêu đề Active Message và tương tác trực tiếp với tầng ứng dụng.
- **UniqueSendLayer:** Tự động tạo và gắn số thứ tự dữ liệu duy nhất (Data Sequence Number - DSN) vào tiêu đề để bên nhận có thể phát hiện và loại bỏ các gói tin bị trùng lặp.
- **PacketLink:** Cung cấp dịch vụ truyền lại tự động (Automatic Retransmission) nếu không nhận được tín hiệu ACK từ nút kế cận.

## Trang 103


- **Low Power Listening (LPL):** Hiện thực kỹ thuật lắng nghe năng lượng thấp bất đồng bộ. Nút gửi sẽ phát chuỗi gói tin liên tiếp (preamble packets) để đánh thức nút nhận đang trong chu kỳ ngủ định kỳ, giúp giảm tiêu hao năng lượng tối đa khi mạng nhàn rỗi.
- **UniqueReceive:** Duy trì bảng lịch sử các gói tin gần nhất để lọc bỏ các gói tin trùng lặp nhận được do truyền lại.
- **TinyOSNetworkC:** Cho phép nhận dạng và chuyển tiếp các gói tin chuẩn IEEE 802.15.4 liên mạng (như 6LoWPAN).
- **CSMA/CA:** Quản lý truy cập môi trường truyền không dây, thực hiện thuật toán backoff ngẫu nhiên để tránh va chạm tín hiệu trên kênh.
- **TransmitP / ReceiveP:** Tương tác trực tiếp với phần cứng chip CC2420 thông qua bus SPI, chân ngắt và GPIO.

#### 4.2.3. Hệ điều hành Contiki

Contiki là hệ điều hành mã nguồn mở, gọn nhẹ (lightweight), đa nhiệm được thiết kế chuyên biệt cho các thiết bị mạng cảm biến không dây và Internet of Things có tài nguyên bộ nhớ hạn chế [14]. Contiki được sáng lập bởi Adam Dunkels tại Viện Khoa học Máy tính Thụy Điển (SICS).

Đặc tính nổi bật của Contiki là tính linh hoạt cao, hỗ trợ nạp động (dynamic loading) và thay thế từng chương trình hoặc dịch vụ riêng lẻ trong lúc hệ thống đang chạy. Contiki được xây dựng theo mô hình hướng sự kiện (event-driven) kết hợp với cơ chế tiểu luồng **Protothreads**, mang lại phong cách lập trình tuần tự tuyến tính mà không tốn kém chi phí ngăn xếp luồng độc lập.

## Trang 104


##### 4.2.3.1. Cấu trúc một ứng dụng trên Contiki

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

    printf("Hello, World! Contiki IoT
");

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
```

## Trang 105


Dòng đầu tiên chỉ ra đường dẫn tới thư mục gốc của Contiki; dòng thứ hai chỉ định tên ứng dụng cần biên dịch; và dòng cuối cùng nạp tệp `Makefile.include` của hệ thống Contiki.

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
- **Sự kiện đồng bộ (Synchronous Event):** Kích hoạt tiến trình đích thực thi ngay lập tức (tương tự như một lời gọi hàm trực tiếp), tiến trình gửi sẽ tạm dừng cho đến khi tiến trình đích xử lý xong sự kiện.

## Trang 106


**Cơ chế thăm dò (Polling Mechanism):** Là một dạng sự kiện có độ ưu tiên cao, được hệ thống thực thi xen giữa các sự kiện thông thường nhằm kiểm tra nhanh các trạng thái phần cứng và phản hồi các ngắt ngoại vi tức thời.

**Các cơ chế định thời (Timers) trong Contiki**
Contiki cung cấp 4 thư viện định thời đa dạng phục vụ các nhu cầu khác nhau:
- **timer:** Bộ định thời đơn giản, chỉ kiểm tra xem một khoảng thời gian đã trôi qua hay chưa (thăm dò thụ động).
- **etimer (Event Timer):** Tạo ra một sự kiện gửi đến tiến trình khi hết thời gian định trước, giúp tiến trình tự động đánh thức từ trạng thái chờ.
- **ctimer (Callback Timer):** Tự động gọi một hàm callback được chỉ định khi hết thời gian, rất hữu ích cho các giao thức mạng.
- **rtimer (Real-time Timer):** Bộ định thời thời gian thực độ chính xác cao dựa trên ngắt phần cứng, phục vụ các tác vụ đòi hỏi thời gian đáp ứng nghiêm ngặt như điều khiển chu kỳ nhiệm vụ radio.

**Chế độ tiết kiệm năng lượng**
Contiki tự động đưa bộ vi xử lý vào trạng thái nghỉ công suất thấp (Low Power Mode - LPM) mỗi khi hàng đợi sự kiện rỗng. Khi có ngắt phần cứng hoặc bộ định thời kích hoạt, MCU sẽ thức dậy để xử lý và sau đó lại quay về trạng thái ngủ, giúp kéo dài tối đa thời gian hoạt động bằng pin của thiết bị.

## Trang 107


**Kiến trúc dịch vụ và nạp động (Dynamic Services)**

Trong Contiki, một dịch vụ (service) là một tiến trình cung cấp các chức năng dùng chung (như giao thức mạng, bộ điều khiển cảm biến) cho các tiến trình khác. Điểm đặc sắc là các dịch vụ có thể được biên dịch độc lập, nạp vào bộ nhớ hoặc gỡ bỏ trong lúc hệ thống đang hoạt động mà không cần khởi động lại bo mạch.

Lớp quản lý dịch vụ (Service Layer) duy trì danh sách các dịch vụ hiện có trong hệ thống và phiên bản tương ứng. Ứng dụng gọi dịch vụ thông qua một thư viện gốc (stub library) để liên kết động với tiến trình dịch vụ tại thời điểm chạy.

**Ngăn xếp truyền thông trong Contiki**

Contiki hỗ trợ hai ngăn xếp mạng mạnh mẽ:
- **uIP / uIPv6:** Ngăn xếp TCP/IP và IPv6 siêu nhỏ gọn tuân thủ chuẩn RFC, hỗ trợ 6LoWPAN, RPL, UDP, TCP, CoAP và MQTT, cho phép nút cảm biến kết nối trực tiếp với Internet toàn cầu.
- **Rime:** Ngăn xếp truyền thông mạng cảm biến nhẹ tùy biến, cung cấp các khối giao tiếp phân tầng từ cơ bản (broadcast, unicast một chặng) đến nâng cao (truyền đa chặng, thu thập dữ liệu cây hop-by-hop) với chi phí bộ nhớ tối thiểu.

**Hệ thống tệp Coffee (Coffee Flash File System)**
Contiki tích hợp sẵn hệ thống tệp Coffee chuyên biệt cho chip nhớ Flash ngoài của các mote cảm biến, cho phép lưu trữ cấu hình và nhật ký dữ liệu cảm biến bền vững với cơ chế san phẳng độ mòn (wear leveling).

## Trang 108


**Hình 4.18.** Sơ đồ các cơ chế giao tiếp trên Contiki

#### 4.2.4. Hệ điều hành Raspbian OS

Hệ điều hành Raspbian (hiện nay được đổi tên chính thức là **Raspberry Pi OS**) là hệ điều hành mã nguồn mở miễn phí dựa trên nền tảng bản phân phối Linux Debian, được tối ưu hóa đặc biệt cho dòng máy tính nhúng phần cứng Raspberry Pi [15].

Ban đầu Raspbian được khởi xướng bởi Mike Thompson và Peter Green như một dự án cộng đồng độc lập, sau đó được Raspberry Pi Foundation chính thức bảo trợ và phát triển thành hệ điều hành chính thức. Kho phần mềm của Raspbian cung cấp hơn 35.000 gói ứng dụng (packages) được biên dịch sẵn, đáp ứng đầy đủ từ các nhu cầu học tập, phát triển phần mềm nhúng đến triển khai các dịch vụ máy chủ mạng và IoT Gateway phức tạp.

## Trang 109


**Hình 4.19.** Kiến trúc hệ điều hành Raspbian OS

**Kiến trúc và các đặc điểm kỹ thuật của Raspbian OS**
- **Kiến trúc nhân:** Nhân Linux monolithic đầy đủ hỗ trợ đa nhiệm, đa người dùng, bộ nhớ ảo và cơ chế đa luồng ưu tiên chiếm quyền (preemptive multi-threading).
- **Ngôn ngữ phát triển:** Hỗ trợ toàn diện các ngôn ngữ lập trình hiện đại như Python, C, C++, Java, Node.js, PHP, Ruby, Scratch. Thư viện Python (`RPi.GPIO`, `gpiozero`) cho phép lập trình điều khiển các chân phần cứng cực kỳ nhanh chóng và trực quan.
- **Giao thức và kết nối:** Hỗ trợ đầy đủ bộ giao thức TCP/IP tiêu chuẩn, Bluetooth/BLE, Wi-Fi, Ethernet và các chuẩn giao tiếp công nghiệp như MQTT, HTTP/HTTPS, WebSockets, CoAP, Modbus.
- **Công cụ mô phỏng:** Có thể giả lập chạy toàn bộ hệ thống Raspbian trên máy tính thông qua công cụ máy ảo QEMU ARM.
- **Bảo mật:** Cung cấp đầy đủ các cơ chế bảo mật cấp doanh nghiệp của Linux như xác thực người dùng SSH, tường lửa iptables/ufw, mã hóa OpenSSL, VPN và phân quyền truy cập tệp.

## Trang 110


- **Hỗ trợ đa phương tiện mạnh mẽ:** Tận dụng bộ tăng tốc đồ họa phần cứng VideoCore GPU tích hợp trên bo mạch Raspberry Pi, Raspbian hỗ trợ hiển thị giao diện đồ họa mượt mà (môi trường máy tính để bàn PIXEL / LXDE), xử lý video độ phân giải cao 1080p và 4K, hỗ trợ các chuẩn OpenMAX, OpenGL ES, OpenVG và các thư viện thị giác máy tính như OpenCV. Hệ điều hành cũng hỗ trợ truyền phát âm thanh/hình ảnh thời gian thực qua các giao thức VoIP như SIP và RTP.
- **Mức tiêu thụ năng lượng:** Mặc dù tiêu thụ nhiều năng lượng hơn so với các vi điều khiển cấp thấp, một bo mạch Raspberry Pi chạy Raspbian chỉ tiêu thụ công suất trung bình từ 1.5W đến 5W (tùy thuộc vào tác vụ và tải CPU), hoàn toàn có thể chạy bằng nguồn sạc dự phòng di động hoặc hệ thống pin năng lượng mặt trời cho các trạm giám sát thông minh ngoài trời.

Nhờ những ưu điểm vượt trội trên, Raspberry Pi chạy Raspbian thường đóng vai trò là **Edge Gateway** hoặc **Edge Computing Node** trong kiến trúc IoT hiện đại, chịu trách nhiệm thu thập dữ liệu từ các mạng cảm biến cục bộ (qua Zigbee, LoRa, BLE), thực hiện tiền xử lý, nén dữ liệu, chạy các mô hình AI/Machine Learning suy luận nhẹ tại biên và chuyển tiếp dữ liệu lên đám mây.

## Trang 111


#### 4.2.5. Tổng hợp một số nền tảng phần mềm IoT phổ biến

**Bảng 4.2.** Bảng tổng hợp đặc tính một số nền tảng hệ điều hành nổi tiếng trong IoT [15]

| Hệ điều hành | Min RAM | Min ROM | Bộ xử lý / Xung nhịp | Kiến trúc nhân | Cơ chế lập lịch | Mô hình luồng | Ngôn ngữ | Hỗ trợ C++ |
|:---|:---:|:---:|:---|:---|:---|:---|:---|:---:|
| **TinyOS** | 1 kB | 4 kB | 4 - 8 bit | Monolithic | Non-preemptive FIFO | Event driven | NesC | NO |
| **Contiki** | 2 kB | 30 kB | 8 bit | Modular | Preemptive FIFO | Event driven, Protothreads | C | Partially |
| **RIOT** | 1.5 kB | 5 kB | 16/32 bit | Microkernel | Preemptive Priority | Multi-threading | C, C++ | YES |
| **LiteOS** | 4 kB | 128 kB | 8MHz | Modular | Preemptive Priority (Tickless) | Multi-threading | LiteC++ | NO |
| **FreeRTOS** | 0.5 - 10 kB | 12 kB | 32-bit | Microkernel | Preemptive Priority | Multi-threading | C | YES |
| **Mynewt** | 8 kB | 64 kB | 12 - 200MHz | Modular | Preemptive Priority | Multi-threading | Go, C | YES |
| **Mbed** | 16 kB | 32 kB | 32-bit | Monolithic | Non-preemptive | Singlethread / RTOS | C, C++ | YES |

## Trang 112


**Bảng 4.2.** (tiếp theo)

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
| **RIOT** | CÓ | Thứ bậc | CÓ | Cooja | TCP, UDP, IPv6, 6LoWPAN, RPL, CoAP, CBOR, UBJSON, OpenWSN, WiFi, Bluetooth, LTE, MQTT |

## Trang 113


**Bảng 4.3.** (tiếp theo)

| Hệ điều hành | Thực thi script từ xa | Cấu trúc hệ thống tệp | Bộ nhớ động | Công cụ mô phỏng | Chồng giao thức và các giao thức mạng có hỗ trợ |
|:---|:---:|:---|:---:|:---|:---|
| **LiteOS** | CÓ | Thứ bậc | CÓ | AVRORA | NB-IoT, 6LoWPAN, Zigbee, LTE, Bluetooth |
| **FreeRTOS** | CÓ | Thứ bậc | CÓ | QEMU | uIP, lwIP, TCP, 6LoWPAN, CoAP, MQTT |
| **Mynewt** | CÓ | Thứ bậc | CÓ | QEMU | BLE, IPv6, 6LoWPAN, HTTP, TCP, CoAP, MQTT, UDP, LoRa PHY, LoRaWAN |
| **Mbed** | CÓ | Thứ bậc | CÓ | QEMU | 6LoWPAN, Ethernet, Zigbee, HTTP, WiFi, BLE, IPv6, CoAP, MQTT |
| **uClinux** | CÓ | Thứ bậc | CÓ | GDB/ARMulator | uIP, lwIP, WiFi, Bluetooth, LTE, IPv6, MQTT |
| **Raspbian** | CÓ | Thứ bậc | CÓ | QEMU | RTP, LTE, HTTP, TCP, MQTT, CoAP, Bluetooth, WebSockets |
| **Android Things** | CÓ | Thứ bậc | CÓ | RPi3, Intel Edison, NXP Pico | Weave, Thread, Zigbee, Z-Wave, Bluetooth, WiFi |

## Trang 114


Thông qua phần tổng hợp từ hai bảng, Bảng 4.2 và Bảng 4.3 ta thấy hiện nay có rất nhiều nền tảng phần mềm, hệ điều hành hỗ trợ phát triển các giải pháp IoT với nhiều đặc trưng, đặc tính kỹ thuật khác nhau. Chính vì thế, tùy theo nhu cầu sử dụng, tùy theo tính năng, yêu cầu của giải pháp IoT muốn phát triển mà các nhà phát triển hệ thống có thể chọn lựa cho mình một môi trường phù hợp. Ví dụ, trong môi trường nghiên cứu học thuật ở nhiều trường đại học trên thế giới, khi nghiên cứu về mạng cảm biến không dây, thiết bị IoT tiết kiệm năng lượng, tài nguyên hạn chế thì các hệ điều hành như TinyOS, Contiki thường được lựa chọn. Ngoài ra, một nền tảng khá phổ biến và dễ dàng tiếp cận hiện nay đó là máy tính nhúng Raspberry Pi với hệ điều hành Raspbian. Đây là một thiết bị nhúng hỗ trợ khá đầy đủ chức năng của một máy tính thu nhỏ, cho phép người lập trình sử dụng những tiện ích của ngôn ngữ lập trình bậc cao như Python, Node.js, Java... để phát triển các ứng dụng của mình một cách tiện lợi. Tóm lại, với sự phát triển không ngừng của công nghệ, lần lượt ngày càng nhiều nền tảng phần cứng được sản xuất chế tạo, kèm theo đó là các giải pháp phần mềm cũng được tạo ra, mang đến sự đa dạng chủng loại và nhiều sự lựa chọn cho người học, người phát triển giải pháp IoT với nhiều cấp độ, nhiều cách tiếp cận khác nhau.

## BÀI TẬP CHƯƠNG 4

1. Hãy so sánh các nhóm phần cứng dùng trong IoT và liệt kê các thiết bị thuộc mỗi nhóm.
2. Hãy trình bày kiến trúc và hoạt động của một chương trình nesC trên TinyOS.
3. Hãy trình bày kiến trúc và hoạt động của một chương trình C trên Contiki OS.
4. Hãy liệt kê các loại phần cứng, phần mềm và các cảm biến (nếu có) để xây dựng một ứng dụng giám sát chất lượng không khí.
5. Từ nền tảng Arduino và Raspberry Pi 3, hãy thiết kế ứng dụng giám sát môi trường và điều khiển thiết bị cho nhà thông minh.

## Trang 115


6. Từ nền tảng CC2530, hãy thiết kế ứng dụng Nông nghiệp thông minh.
7. Hãy xác định loại phần cứng, phần mềm, cảm biến để xây dựng hệ thống cảnh báo cháy rừng có các nút cảm biến được cấp nguồn bằng pin với yêu cầu tối ưu năng lượng sử dụng để thời gian hoạt động của ứng dụng là lớn nhất.

## Trang 116


# CHƯƠNG 5. ĐIỆN TOÁN ĐÁM MÂY, ĐIỆN TOÁN CẬN BIÊN VÀ IOT

Vạn vật kết nối Internet mở ra nhiều thách thức không chỉ với việc thiết kế phần cứng và phần mềm cho các thiết bị IoT mà còn đặt ra những bài toán hóc búa về hạ tầng xử lý, lưu trữ và phân tích dữ liệu khổng lồ sinh ra từ hàng triệu nút cảm biến. Sự bùng nổ của các ứng dụng IoT thời gian thực như xe tự hành, thành phố thông minh, giám sát y tế khẩn cấp đòi hỏi năng lực tính toán cực lớn cùng với độ trễ phản hồi tính bằng mili-giây.

Để giải quyết bài toán này, sự kết hợp giữa **Điện toán đám mây (Cloud Computing)** và **Điện toán cận biên (Edge Computing / Fog Computing)** đã trở thành mô hình kiến trúc chuẩn mực. Điện toán đám mây cung cấp nguồn tài nguyên lưu trữ và tính toán vô hạn ở trung tâm dữ liệu, trong khi điện toán cận biên đưa khả năng tính toán và ra quyết định đến gần nơi sinh ra dữ liệu nhất (tại các gateway, router hoặc trạm gốc kế cận thiết bị IoT).

Nội dung chương này trình bày kiến trúc tích hợp giữa IoT, điện toán đám mây và điện toán cận biên; phân tích các mô hình dịch vụ đám mây (IaaS, PaaS, SaaS) và ứng dụng thực tiễn trong việc xây dựng hệ thống giả lập mạng cảm biến không dây quy mô lớn trên nền tảng OpenStack; đồng thời làm rõ các công nghệ cốt lõi và xu hướng nghiên cứu trong tính toán cận biên.

## Trang 117


Thông qua nội dung trình bày trong chương này, người đọc có thể nắm bắt được kiến trúc tổng quan của một hệ thống IoT kết hợp hạ tầng điện toán đám mây và tính toán cận biên. Nắm được những đặc điểm, lợi ích, phân loại các mô hình dịch vụ trong điện toán đám mây cũng như các vấn đề nghiên cứu, thách thức trong IoT kết hợp tính toán cận biên giúp người đọc dễ dàng định hướng giải pháp khi triển khai thực tế.

### 5.1. Kiến trúc tổng quan hệ thống IoT tích hợp điện toán đám mây và điện toán cận biên

#### 5.1.1. Kiến trúc tổng quan

Trong những năm gần đây, sự hội tụ giữa công nghệ IoT và điện toán đám mây (thường được gọi là Cloud-IoT) đã tạo ra một mô hình mới đầy tiềm năng. Tuy nhiên, việc truyền toàn bộ dữ liệu thô từ các thiết bị IoT về trung tâm dữ liệu đám mây tập trung bộc lộ nhiều điểm nghẽn nghiêm trọng: tiêu tốn băng thông mạng viễn thông, độ trễ truyền dẫn lớn, không đáp ứng kịp các tác vụ thời gian thực và nguy cơ rò rỉ dữ liệu nhạy cảm.

Chính vì vậy, kiến trúc điện toán phân tán đa tầng bao gồm 3 lớp chính đã được đề xuất và áp dụng rộng rãi:
1. **Lớp thiết bị IoT (Things Layer / End Devices):** Các cảm biến, cơ cấu chấp hành, thiết bị đeo thông minh thực hiện thu thập dữ liệu và thực thi lệnh điều khiển.
2. **Lớp cận biên (Edge / Fog Layer):** Các thiết bị có năng lực tính toán trung bình đặt tại biên mạng (Edge Gateways, Edge Routers, trạm phát sóng di động base station) thực hiện lọc dữ liệu, tiền xử lý, lưu trữ tạm và phản hồi tức thời.
3. **Lớp đám mây (Cloud Layer):** Các trung tâm dữ liệu quy mô lớn (Data Centers) thực hiện lưu trữ lâu dài (Big Data), khai phá dữ liệu chuyên sâu và huấn luyện các mô hình AI/Machine Learning.

## Trang 118


Sự phát triển bùng nổ của công nghệ IoT dẫn đến kiến trúc hệ thống mạng ngày càng phức tạp và phân chia thành nhiều lớp để đáp ứng nhu cầu ngày càng cao của con người. Trong xu hướng đó, các hệ thống, ứng dụng IoT hiện đại ngày nay thường được tổ chức thành các lớp bao gồm: lớp thiết bị IoT, lớp thiết bị cận biên, lớp trung tâm dữ liệu trên hạ tầng điện toán đám mây.

**Hình 5.1.** Kiến trúc tổng quan hệ thống IoT kết hợp Điện toán đám mây và Điện toán biên [1]

- **Lớp thiết bị IoT:** Bao gồm hàng tỷ thiết bị cảm biến, cơ cấu chấp hành kết nối với nhau thông qua các giao thức mạng không dây tầm ngắn và tiết kiệm năng lượng (Zigbee, Bluetooth, 6LoWPAN, Wi-Fi, LoRa).
- **Lớp thiết bị cận biên:** Đóng vai trò là cầu nối thông minh trung gian giữa mạng cảm biến cục bộ và mạng diện rộng Internet. Lớp này thực hiện phân loại dữ liệu, nén dữ liệu, loại bỏ dữ liệu dư thừa và giải quyết các bài toán cục bộ mà không cần phụ thuộc vào kết nối đám mây.

## Trang 119


cao trải nghiệm người dùng cũng là chủ đề mở và đang thu hút giới nghiên cứu.

- **Trung tâm dữ liệu (Data Center):** Là nơi hiện thực hạ tầng điện toán đám mây, với khả năng tính toán và lưu trữ khổng lồ. Trung tâm dữ liệu thực hiện quản lý, điều khiển, phân phối nguồn tài nguyên tính toán dựa trên các công nghệ ảo hóa (Virtual Machines, Containers), chạy các dịch vụ phân tích dữ liệu lớn và cung cấp giao diện quản lý toàn diện cho người dùng và các doanh nghiệp.

#### 5.1.2. Các yêu cầu và đặc trưng cơ bản của các hệ thống tính toán cho IoT

Để đáp ứng được yêu cầu của các ứng dụng IoT phức tạp, các hệ thống tính toán (cả ở biên và đám mây) cần thỏa mãn các tiêu chí kỹ thuật cốt lõi sau:
- **Độ trễ truyền thông thấp (Low Latency):** Đối với các ứng dụng điều khiển thời gian thực (như xe tự hành, điều khiển robot công nghiệp, phẫu thuật từ xa), thời gian đáp ứng phải dưới mức hàng chục mili-giây.
- **Khả năng mở rộng (Scalability):** Hệ thống phải có khả năng tiếp nhận và xử lý mượt mà khi số lượng thiết bị IoT kết nối tăng vọt từ hàng nghìn lên hàng triệu nút.
- **Tính sẵn sàng và độ tin cậy (Availability & Reliability):** Đảm bảo dịch vụ hoạt động liên tục 24/7, có cơ chế sao lưu, dự phòng và tự phục hồi khi có sự cố nút mạng.
- **Tiết kiệm băng thông mạng (Bandwidth Optimization):** Tiền xử lý và nén dữ liệu tại biên giúp giảm tải đường truyền uplink lên đám mây.

## Trang 120


- **Khả năng bảo mật dữ liệu (Data Security):** Đảm bảo hệ thống chịu được các cuộc tấn công từ bên ngoài nhắm vào dữ liệu bí mật lưu trữ trong hệ thống hay truyền trên mạng bằng các cơ chế mã hóa đầu-cuối.
- **Các dịch vụ bảo mật (Service Security):** Giúp hệ thống chịu được các cuộc tấn công từ bên ngoài nhắm vào việc làm tê liệt các dịch vụ (như tấn công từ chối dịch vụ phân tán DDoS).
- **Tính không đồng nhất (Heterogeneity):** Có khả năng tích hợp và làm việc ăn khớp giữa nhiều nền tảng phần cứng, hệ điều hành và giao thức truyền thông khác nhau.

### 5.2. Nền tảng điện toán đám mây và ứng dụng trong IoT

Theo định nghĩa của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST): *Điện toán đám mây là một mô hình cho phép truy cập mạng thuận tiện, theo yêu cầu tới một nhóm tài nguyên tính toán có thể cấu hình được (ví dụ: mạng, máy chủ, lưu trữ, ứng dụng và dịch vụ) mà có thể được cung cấp và giải phóng nhanh chóng với nỗ lực quản lý tối thiểu hoặc sự tương tác tối thiểu từ nhà cung cấp dịch vụ.*

Trong ngữ cảnh IoT, điện toán đám mây đóng vai trò là "bộ não trung tâm" thu thập, tích hợp dữ liệu từ mọi nguồn phân tán, cung cấp tài nguyên tính toán vô hạn cho việc phân tích dữ liệu lớn (Big Data Analytics) và đưa ra các quyết định thông minh mang tính chiến lược.

## Trang 121


nối và ảo hóa một cách linh động và được thể hiện như một hoặc nhiều tài nguyên tính toán đồng nhất dựa trên các thỏa thuận ở mức dịch vụ được thiết lập thông qua việc đàm phán giữa nhà cung cấp dịch vụ và người tiêu dùng.

#### 5.2.1. Đặc trưng cơ bản của điện toán đám mây

NIST xác định 5 đặc trưng cơ bản của điện toán đám mây:
1. **Tự phục vụ theo nhu cầu (On-demand Self-service):** Người dùng có thể tự cấu hình các tài nguyên tính toán (như thời gian máy chủ, dung lượng lưu trữ mạng) một cách tự động khi cần mà không cần tương tác trực tiếp với con người bên phía nhà cung cấp.
2. **Truy cập mạng rộng rãi (Broad Network Access):** Các tài nguyên được cung cấp qua mạng Internet và có thể truy cập thông qua các cơ chế tiêu chuẩn từ nhiều loại thiết bị khách khác nhau (máy tính, điện thoại di động, máy tính bảng).
3. **Dùng chung tài nguyên (Resource Pooling):** Nguồn tài nguyên tính toán của nhà cung cấp được gộp lại để phục vụ nhiều người dùng (multi-tenant model), với các tài nguyên vật lý và ảo hóa được phân bổ linh hoạt theo nhu cầu.
4. **Co giãn nhanh chóng (Rapid Elasticity):** Tài nguyên có thể được cấp phát và giải phóng một cách nhanh chóng, co giãn linh hoạt theo lưu lượng tải thực tế.
5. **Đo lường dịch vụ (Measured Service):** Hệ thống đám mây tự động kiểm soát và tối ưu hóa việc sử dụng tài nguyên bằng cách đo lường chi tiết ở mức dịch vụ (dung lượng lưu trữ, băng thông tiêu thụ, chu kỳ CPU sử dụng) để tính phí theo mức độ sử dụng (pay-as-you-go).

## Trang 122


thuật như: tính toán song song (parallel computing), cân bằng tải (load balancing), định thời tác vụ (job scheduling).

Khả năng truy cập và tính linh động thể hiện qua việc các thiết bị, sản phẩm, dịch vụ và môi trường điện toán đám mây có thể truy cập với nhiều người nhất có thể. Tính linh động dịch vụ cho phép người dùng chuyển đổi các ứng dụng và dữ liệu giữa các đám mây khác nhau mà không bị trói buộc vào một nhà cung cấp duy nhất.

#### 5.2.2. Lợi ích của điện toán đám mây

Việc ứng dụng điện toán đám mây mang lại nhiều lợi ích to lớn cho các tổ chức và doanh nghiệp phát triển hệ thống IoT:
- **Tiết kiệm chi phí đầu tư ban đầu (Cost Reduction):** Doanh nghiệp không cần phải đầu tư chi phí mua sắm máy chủ vật lý, xây dựng phòng máy lạnh và thuê đội ngũ bảo trì tốn kém. Thay vào đó chỉ cần trả phí thuê bao theo mức sử dụng thực tế.
- **Tập trung vào nghiệp vụ cốt lõi:** Các nhà phát triển giải pháp IoT có thể tập trung toàn lực vào việc phát triển ứng dụng và thuật toán kinh doanh, để việc quản trị hạ tầng máy chủ cho các nhà cung cấp đám mây chuyên nghiệp đảm nhiệm.

## Trang 123


doanh nghiệp có thể cải tiến hiệu năng các dịch vụ IT, dễ dàng vận hành và quản lý tập trung các dịch vụ thông qua nhà cung cấp dịch vụ.
- **Nâng cao hiệu quả sử dụng tài nguyên:** Doanh nghiệp có thể hợp tác với nhà cung cấp dịch vụ điện toán đám mây để tận dụng công nghệ ảo hóa, tránh lãng phí năng lực tính toán dư thừa khi hệ thống nhàn rỗi.
- **Khả năng phục hồi sau thảm họa (Disaster Recovery):** Dữ liệu được lưu trữ phân tán và sao lưu tự động trên nhiều trung tâm dữ liệu ở các khu vực địa lý khác nhau, đảm bảo dữ liệu không bị mất mát khi xảy ra sự cố thiên tai hoặc hỏng hóc phần cứng.

**Hình 5.2.** Khung phân cấp dịch vụ điện toán đám mây

Mô hình phân cấp dịch vụ điện toán đám mây truyền thống được chia thành 3 lớp cơ bản (Hình 5.2):
1. **IaaS (Infrastructure as a Service - Hạ tầng như một dịch vụ)**
2. **PaaS (Platform as a Service - Nền tảng như một dịch vụ)**
3. **SaaS (Software as a Service - Phần mềm như một dịch vụ)**

## Trang 124


#### 5.2.3. Mô hình IaaS

Các dịch vụ trên hạ tầng điện toán đám mây được phát triển theo 3 loại mô hình dịch vụ cơ bản. Trong đó, mô hình thấp nhất là **Hạ tầng như một dịch vụ (Infrastructure as a Service - IaaS)**:

Trong mô hình IaaS, nhà cung cấp dịch vụ cung cấp cho người dùng các tài nguyên phần cứng máy tính được ảo hóa thô, bao gồm:
- **Năng lực tính toán (Compute):** Các máy ảo (Virtual Machines) hoặc bare-metal servers với số lượng CPU core, dung lượng RAM xác định.
- **Không gian lưu trữ (Storage):** Lưu trữ khối (Block Storage), lưu trữ đối tượng (Object Storage), lưu trữ tệp (File Storage).
- **Tài nguyên mạng (Networking):** Bộ định tuyến ảo (Virtual Routers), tường lửa ảo (Firewalls), địa chỉ IP tĩnh công cộng, mạng riêng ảo (VPC/VLAN).

Người dùng có toàn quyền kiểm soát hệ điều hành được cài đặt trên máy ảo, cấu hình các dịch vụ mạng, triển khai các phần mềm trung gian (middleware) và các ứng dụng của mình. Nhà cung cấp IaaS chịu trách nhiệm quản lý và bảo trì toàn bộ phần cứng vật lý bên dưới (máy chủ, hệ thống lưu trữ SAN/NAS, thiết bị chuyển mạch mạng, nguồn điện và phòng máy).

## Trang 125


Người dùng không thể quản lý hay điều khiển hạ tầng bên dưới của nhà cung cấp dịch vụ điện toán đám mây nhưng có thể điều khiển hệ điều hành, bộ nhớ, ứng dụng được triển khai cũng như những cài đặt liên quan tới các thành phần kết nối mạng giữa các máy ảo mà mình quản lý. Một số nền tảng cung cấp dịch vụ này như: Amazon EC2, Google Compute Engine, Microsoft Azure Virtual Machines, OpenNebula, OpenStack...

**Hình 5.3.** Các thành phần chính trong dịch vụ hạ tầng IaaS

Hình 5.3 mô tả các thành phần chức năng cốt lõi của một hệ thống IaaS:
- **Quản lý máy chủ ảo (Virtual Compute Management):** Cung cấp các công cụ tạo mới, xóa bỏ, khởi động, tạm dừng, di chuyển nóng (live migration) các máy ảo giữa các máy chủ vật lý.
- **Quản lý lưu trữ ảo (Virtual Storage Management):** Cấp phát và gắn kết các ổ đĩa ảo, quản lý ảnh đĩa hệ điều hành (Image Repository).
- **Quản lý mạng ảo (Virtual Network Management):** Cấu hình các subnet, cấp phát địa chỉ IP qua DHCP ảo, thiết lập định tuyến và quy tắc bảo mật an ninh mạng (Security Groups).

## Trang 126


(virtual storage) bao gồm phân bổ không gian lưu trữ, giải phóng bộ nhớ, ghi dữ liệu, đọc dữ liệu...; quản lý mạng ảo (virtual network) bao gồm việc cấp phát địa chỉ IP, đăng ký tên miền, thiết lập kết nối, phân bổ băng thông đường truyền...

#### 5.2.4. Mô hình PaaS

**Nền tảng như một dịch vụ (Platform as a Service - PaaS)** là mô hình cung cấp một môi trường hoàn chỉnh trên đám mây để các nhà phát triển có thể xây dựng, thử nghiệm, triển khai và quản lý các ứng dụng mà không cần quan tâm đến việc mua sắm, cài đặt và bảo trì hạ tầng phần cứng cũng như hệ điều hành bên dưới.

Trong mô hình PaaS, nhà cung cấp quản lý toàn bộ hạ tầng (máy chủ, mạng, lưu trữ) cùng với hệ điều hành, runtime ngôn ngữ lập trình, hệ quản trị cơ sở dữ liệu và các phần mềm trung gian. Người dùng chỉ cần tải lên mã nguồn ứng dụng và cấu hình các thiết lập ứng dụng.

Đối với IoT, các nền tảng **IoT Cloud Platforms (IoT PaaS)** rất phát triển, cung cấp sẵn các dịch vụ chuyên biệt cho IoT như:
- Cổng giao tiếp thiết bị (Device Gateway hỗ trợ giao thức MQTT, CoAP, HTTP).
- Quản lý danh mục và trạng thái thiết bị (Device Registry, Device Shadow).
- Động cơ xử lý luật thời gian thực (Rule Engine).
- Cơ sở dữ liệu chuỗi thời gian (Time-series Database).
- Công cụ trực quan hóa bảng điều khiển (Dashboard Visualization).

Các nền tảng IoT PaaS nổi tiếng bao gồm: AWS IoT Core, Google Cloud IoT, Microsoft Azure IoT Hub, ThingsBoard, Blynk, ThingSpeak.

## Trang 127


Kỹ thuật được sử dụng để hiện thực mô hình này đó là thiết kế môi trường chạy ứng dụng (runtime environment design). Môi trường chạy ứng dụng liên quan tới việc thu thập các dịch vụ phần mềm có sẵn, cần thiết để ứng dụng thực thi như các thư viện, gói phần mềm, gói công cụ cần thiết.

#### 5.2.5. Mô hình SaaS

**Phần mềm như một dịch vụ (Software as a Service - SaaS)** là mô hình dịch vụ đám mây hoàn chỉnh nhất ở tầng trên cùng, nơi nhà cung cấp phân phối một ứng dụng phần mềm hoàn thiện tới người dùng đầu cuối qua mạng Internet, thường là thông qua trình duyệt web hoặc ứng dụng di động.

Trong mô hình SaaS, người dùng không cần cài đặt phần mềm lên máy tính cá nhân, không cần quản lý hạ tầng hay nền tảng mà chỉ cần đăng nhập tài khoản và sử dụng các tính năng của phần mềm. Mọi vấn đề về cập nhật tính năng mới, vá lỗi bảo mật, sao lưu dữ liệu đều do nhà cung cấp đảm nhiệm hoàn toàn.

## Trang 128


các hạ tầng bên dưới bao gồm mạng, máy chủ, hệ điều hành, bộ nhớ hay thậm chí là các khả năng riêng lẻ của các ứng dụng trong khuôn khổ cấu hình giới hạn cho từng người dùng riêng lẻ.

Một số dịch vụ cung cấp theo mô hình SaaS phổ biến như: các ứng dụng của Google (Gmail, Google Docs, Google Drive), Microsoft 365, Dropbox, Salesforce CRM.

Trong lĩnh vực IoT, các ứng dụng SaaS thường là các giải pháp đóng gói hoàn chỉnh cho từng lĩnh vực chuyên ngành:
- **Hệ thống Quản lý Tòa nhà thông minh (Smart Building Management System):** Cho phép ban quản lý theo dõi tiêu thụ năng lượng điện, nước, điều khiển hệ thống chiếu sáng và HVAC.
- **Hệ thống Giám sát Hạm đội xe (Fleet Management):** Định vị phương tiện GPS, theo dõi hành trình xe, giám sát mức tiêu hao nhiên liệu.
- **Hệ thống Nông nghiệp thông minh SaaS:** Phân tích độ ẩm đất, dự báo sâu bệnh và tự động hóa hệ thống tưới nhỏ giọt.

## Trang 129


trụ, mô phỏng hóa sinh; các ứng dụng cho chính phủ như hệ thống y tế quốc gia, hệ thống giao thông vận tải...
- **Cổng thông tin (web portal):** cung cấp các dịch vụ tìm kiếm thông tin chuẩn, ngoài ra cũng có các dịch vụ khác như e-mail, tin tức, giá chứng khoán. Cổng thông tin cung cấp một giao diện web thống nhất cho người dùng truy cập tới nhiều dịch vụ khác nhau.

#### 5.2.6. Ứng dụng công nghệ điện toán đám mây trong xây dựng hệ thống giả lập WSN với số lượng nút lớn

Trong nghiên cứu và phát triển các giải pháp IoT và mạng cảm biến không dây (WSN), việc thử nghiệm trên các mạng quy mô lớn (hàng trăm đến hàng nghìn nút) gặp nhiều rào cản lớn:
- Chi phí mua sắm thiết bị phần cứng thực tế rất đắt đỏ.
- Khó khăn trong việc triển khai thực địa, nạp lại mã nguồn đồng loạt và giám sát trạng thái từng nút.
- Khó tái lập lại chính xác môi trường thử nghiệm khi cần đánh giá so sánh hiệu năng các giao thức định tuyến.

Để giải quyết bài toán trên, giải pháp ứng dụng hạ tầng đám mây mã nguồn mở **OpenStack** kết hợp với công nghệ ảo hóa nhẹ **Docker Containers** đã được nghiên cứu và xây dựng nhằm giả lập các mạng WSN quy mô lớn với chi phí thấp và độ linh hoạt cao.

## Trang 130


nguyên phục vụ cho các nghiên cứu khác giúp tối ưu việc sử dụng tài nguyên. Bên cạnh đó, việc triển khai ảo hóa lớp thứ hai với kỹ thuật Container cho phép tạo ra một số lượng rất lớn các nút ảo với lượng tài nguyên yêu cầu thấp giúp đáp ứng yêu cầu phục vụ các thử nghiệm có số lượng nút lớn.

**Hình 5.4.** Giải pháp tích hợp mạng cảm biến không dây trên hạ tầng đám mây OpenStack

Kiến trúc thử nghiệm tích hợp được mô tả trong Hình 5.4 bao gồm hai tầng ảo hóa:
1. **Tầng ảo hóa phần cứng OpenStack (IaaS):** Quản lý cụm máy chủ vật lý, tạo ra các máy ảo Linux (Swarm Workers) được kết nối với nhau qua mạng ảo diện rộng.
2. **Tầng ảo hóa nhẹ Docker Containers:** Chạy trên các máy ảo OpenStack. Mỗi container đóng vai trò giả lập một nút cảm biến không dây hoàn chỉnh, chạy hệ điều hành mạng nhúng (như Contiki hoặc Linux rút gọn), cài đặt giao thức định tuyến (như OLSR) và mã nguồn ứng dụng cảm biến.

## Trang 131


Quá trình triển khai ảnh sẽ gồm 5 bước được thực hiện ở 3 vị trí luận lý khác nhau:
1. Người dùng tạo ra tập tin đặc tả kịch bản thử nghiệm trên giao diện front-end của UIT-IoT Testbed tại máy người dùng.
2. Hệ thống biên dịch kịch bản thành tệp cấu hình triển khai Docker Compose và các tệp cấu hình mạng.
3. Master Node trên OpenStack nhận yêu cầu, phân tích số lượng nút và tự động khởi tạo các mạng ảo và container tương ứng trên các máy Swarm Workers.
4. Các container khởi động, kết nối vào các card mạng ảo tương ứng theo đúng cấu trúc tô-pô định trước và kích hoạt tiến trình định tuyến.
5. Dữ liệu giám sát từ các container được thu thập và gửi về giao diện người dùng theo thời gian thực.

##### 5.2.6.1. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý MESH của WSNs trên OpenStack

Trong cấu trúc mạng MESH, mọi nút mạng trong cùng phạm vi phát sóng đều có thể truyền tin trực tiếp với nhau hoặc qua nhiều chặng trung gian.

## Trang 132


giữa máy host và các container, các biến môi trường, các lệnh sẽ được thực thi khi khởi chạy containers. Ngoài ra, tập tin này còn đặc tả thông tin về các mạng ảo và kết nối giữa các containers thông qua các mạng ảo này.

**Hình 5.5.** Mô hình mạng luận lý dạng MESH trên OpenStack

Hình 5.5 mô tả giải pháp xây dựng mạng luận lý MESH trên OpenStack:
- Một mạng ảo OpenStack Neutron (mạng dùng chung) được tạo ra đóng vai trò như môi trường truyền sóng không dây chung.
- Tất cả các container giả lập nút mạng WSN đều gắn card mạng ảo kết nối vào cùng mạng con này.
- Giao thức định tuyến mạng cảm biến (như OLSR - Optimized Link State Routing) chạy bên trong mỗi container sẽ tự động trao đổi các bản tin HELLO và TC (Topology Control) để khám phá các láng giềng và xây dựng bảng định tuyến đa chặng tối ưu.

## Trang 133


##### 5.2.6.2. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý TREE của WSNs trên OpenStack

**Hình 5.6.** Mô hình mạng luận lý dạng TREE trên OpenStack

Điểm khác biệt so với kiến trúc mạng MESH là trong kiến trúc mạng TREE, các nút mạng được phân chia theo cấu trúc thứ bậc hình cây (cha - con). Mỗi nút chỉ giao tiếp trực tiếp với nút cha hoặc các nút con của nó mà không được truyền thông ngang hàng trực tiếp với các nhánh khác.

Để hiện thực cấu trúc mạng TREE trên OpenStack, hệ thống tự động sinh ra nhiều mạng ảo riêng biệt: mỗi mạng ảo đại diện cho một liên kết điểm - điểm (Point-to-Point) hoặc một nhóm cha - con cục bộ. Nhờ đó, các container chỉ có thể trao đổi gói tin qua các liên kết hợp lệ theo đúng cấu trúc cây định trước.

## Trang 134


##### 5.2.6.3. Giải pháp tích hợp, triển khai kiến trúc mạng WSNs (MESH/TREE) và giao thức định tuyến WSNs (olsr), mô hình giả lập thiết bị WSNs trên OpenStack

Để tự động hóa hoàn toàn quy trình khởi tạo và điều khiển mạng thử nghiệm WSN trên hạ tầng đám mây OpenStack, hệ thống sử dụng tập hợp các giao diện lập trình ứng dụng RESTful APIs do OpenStack cung cấp.

**Bảng 5.1.** Tóm lược một số APIs OpenStack (phần 1)

| Nhóm API | Root URL | API | Chức năng | Input | Output |
|:---|:---|:---|:---|:---|:---|
| **Identity (Keystone)** | `https://mitaka.uit.edu.vn:5000/v2.0` | `POST /v2.0/tokens` | Chứng thực người dùng, trả về token để thực thi các APIs khác | `tenantName` (tên project), `username`, `password` | `token` |
| **Networking (Neutron)** | `https://mitaka.uit.edu.vn:9696/v2.0` | `GET /v2.0/networks` | Liệt kê thông tin tất cả các networks | Không có | Danh sách networks |
| | | `POST /v2.0/networks` | Tạo mới một network ảo | `name` (tên network), `admin_state_up` | Thông tin network vừa tạo |
| | | `POST /v2.0/subnets` | Tạo mới một subnet ảo | `network_id`, `ip_version`, `cidr`, `enable_dhcp` | Thông tin subnet vừa tạo |
| **Compute (Nova)** | `https://mitaka.uit.edu.vn:8774/v2.1` | `GET /images` | Liệt kê thông tin các images có trong OpenStack | Không có | Danh sách images |

## Trang 135


**Bảng 5.1.** Tóm lược một số APIs OpenStack (phần 2 - Compute APIs)

| Nhóm API | Root URL | API | Chức năng | Input | Output |
|:---|:---|:---|:---|:---|:---|
| **Compute (Nova)** *(tiếp theo)* | `https://mitaka.uit.edu.vn:8774/v2.1` | `GET /flavors` | Liệt kê thông tin các flavors (thông số cấu hình CPU, RAM... cho máy ảo) | Không có | Danh sách flavors |
| | | `GET /os-keypairs` | Liệt kê thông tin các keypairs (cặp SSH key dùng chứng thực) | Không có | Danh sách keypairs |
| | | `POST /servers` | Tạo một máy ảo mới trong OpenStack | `name`, `image_id`, `flavor_id`, danh sách networks, `key_name` | Thông tin máy ảo vừa tạo |

Chức năng chính của Compute API là tạo, xóa, sửa các Instance (máy ảo) có trong OpenStack. Ngoài ra, Compute API cung cấp các APIs hỗ trợ việc tạo, xóa, sửa, lấy thông tin images, flavors... Nhờ hệ thống APIs này, hệ thống UIT-IoT Testbed có thể tự động cấp phát tài nguyên tính toán và thiết lập mạng ảo chỉ trong vài phút.

## Trang 136


**Hình 5.7.** Kiến trúc mô phỏng thiết bị WSN sử dụng container/VM trên OpenStack

**Hình 5.8.** Cấu trúc liên kết mạng mô phỏng

Hình 5.7 và Hình 5.8 mô tả kiến trúc triển khai thử nghiệm:
- Mỗi máy ảo OpenStack đóng vai trò là một Host chứa cụm Docker Engine.
- Các container được khởi tạo với hình ảnh chứa sẵn hệ điều hành Linux gọn nhẹ (Alpine Linux hoặc Ubuntu Core) cùng gói phần mềm giao thức định tuyến OLSR (`olsrd`).
- Tập tin cấu hình `olsrd.conf` được tự động sinh ra và gắn vào container khi khởi chạy để thiết lập các tham số định tuyến (chu kỳ gửi gói tin HELLO, thời gian sống của tuyến đường).
- Ứng dụng mô phỏng gửi dữ liệu cảm biến định kỳ qua socket UDP đến nút Sink để đánh giá tỷ lệ chuyển gói thành công (PDR - Packet Delivery Ratio) và độ trễ truyền gói tin trung bình.

## Trang 137


Quy trình triển khai cụm Docker Swarm được thực hiện tuần tự qua các bước: gọi API chứng thực `POST /v2.0/tokens` để lấy access token; sau đó gọi các APIs lấy danh sách hình ảnh (`GET /images`), cấu hình máy ảo (`GET /flavors`), khóa SSH (`GET /os-keypairs`) và mạng ảo (`GET /v2.0/networks`). Cuối cùng, hệ thống gửi yêu cầu `POST /servers` để khởi tạo các máy ảo worker và kích hoạt các containers.

### 5.3. Nền tảng điện toán cận biên và ứng dụng trong IoT

#### 5.3.1. Kiến trúc triển khai điện toán cận biên trong IoT

Điện toán cận biên (Edge Computing) là mô hình xử lý tính toán phân tán, trong đó các tác vụ xử lý thông tin, lưu trữ và điều khiển được đặt tại vị trí biên của mạng – gần với nguồn phát sinh dữ liệu (các thiết bị cảm biến và người dùng). Mô hình này giải quyết triệt để các hạn chế cố hữu của điện toán đám mây truyền thống về độ trễ, lưu lượng mạng và tính riêng tư.

## Trang 138


Hình 5.9 mô tả kiến trúc tổng quan các thành phần của hệ thống tính toán cận biên áp dụng trong IoT. Hệ thống bao gồm:
1. **Các thiết bị IoT:** Như các cảm biến, thiết bị động cơ, mạch điều khiển thu thập dữ liệu từ môi trường vật lý.
2. **Các thiết bị tính toán cận biên:** Bao gồm các IoT Gateway, thiết bị biên chuyên dụng (Edge Nodes), máy tính nhúng, trạm gốc viễn thông di động (eNodeB trong 4G/5G).
3. **Các máy chủ đám mây:** Thực hiện các chức năng lưu trữ dài hạn, phân tích dữ liệu lớn và quản lý chiến lược toàn mạng.

**Hình 5.9.** Kiến trúc điện toán sương mù / điện toán biên trong hệ thống IoT

#### 5.3.2. Các công nghệ, kỹ thuật nổi bật cho tính toán cận biên trong IoT

Để hiện thực hóa tính toán cận biên hiệu quả, nhiều công nghệ và kỹ thuật tiên tiến đã được nghiên cứu và ứng dụng:

## Trang 139


- **Quản lý tài nguyên phân tán (Resource Management):** Điều phối linh hoạt các nguồn tài nguyên tính toán (CPU, GPU, RAM) và lưu trữ hạn chế tại biên nhằm phục vụ tối ưu đồng thời nhiều ứng dụng IoT khác nhau.
- **Tính toán kết hợp truyền thông (Joint Communication and Computing):** Tối ưu hóa đồng thời việc phân bổ kênh truyền vô tuyến và phân bổ năng lực xử lý tính toán để giảm thiểu tổng năng lượng tiêu thụ và độ trễ xử lý của các thiết bị IoT di động.
- **Di chuyển tác vụ tính toán (Computation Offloading):** Cơ chế cho phép thiết bị IoT có năng lực xử lý yếu hoặc sắp cạn pin chuyển giao một phần hoặc toàn bộ tác vụ tính toán nặng (như giải mã tín hiệu, nhận dạng hình ảnh) sang cho thiết bị biên kế cận xử lý thay.

## Trang 140


**Công nghệ xử lý thông minh tại thiết bị cận biên (Edge Intelligence / Edge AI)**

Lượng dữ liệu khổng lồ từ các thiết bị IoT thu thập đóng vai trò quan trọng trong việc xây dựng các tập dữ liệu (dataset) dùng cho việc huấn luyện và phát triển các giải pháp máy học. Tuy nhiên, việc truyền toàn bộ dữ liệu về đám mây gây tắc nghẽn mạng nghiêm trọng. Xu hướng mới là đưa trí tuệ nhân tạo ra biên:
- **Suy luận tại biên (Edge Inference):** Sử dụng các mô hình học sâu đã được nén nhẹ (bằng kỹ thuật lượng tử hóa Quantization, cắt tỉa Pruning, tri thức chưng cất Knowledge Distillation) như TensorFlow Lite, TinyML, ONNX để thực thi nhận dạng khuôn mặt, phát hiện dị thường trực tiếp ngay trên vi điều khiển hoặc máy tính nhúng tại chỗ với độ trễ tính bằng mili-giây.
- **Học liên kết (Federated Learning):** Các nút biên tự huấn luyện mô hình máy học cục bộ dựa trên dữ liệu riêng tư của mình và chỉ gửi các trọng số mô hình (model updates/gradients) về đám mây để tổng hợp mô hình chung toàn cầu, qua đó bảo vệ tuyệt đối tính riêng tư dữ liệu người dùng.

## Trang 141


rộng hệ thống bằng việc cho phép chia sẻ tài nguyên dựa trên nhu cầu trong lúc chạy (runtime needs).

### 5.4. Các vấn đề tồn tại và hướng nghiên cứu trong tương lai

Mặc dù việc kết hợp giữa điện toán đám mây và điện toán cận biên mở ra nhiều cơ hội phát triển vượt bậc cho hệ sinh thái IoT, nhiều thách thức kỹ thuật quan trọng vẫn đang cần tiếp tục nghiên cứu:
- **Quản lý tính di động (Mobility Management):** Khi các nút IoT hoặc phương tiện di chuyển liên tục qua các vùng phủ sóng của các trạm biên khác nhau, việc di chuyển trạng thái dịch vụ (Service / Container Migration) liền mạch không làm gián đoạn kết nối là bài toán phức tạp.
- **Bảo mật và quyền riêng tư tại biên:** Các thiết bị biên thường đặt ở môi trường công cộng bên ngoài, dễ bị tấn công vật lý, cài mã độc hoặc giả mạo. Cần phát triển các cơ chế xác thực phân tán dựa trên công nghệ chuỗi khối (Blockchain) hoặc môi trường thực thi tin cậy (Trusted Execution Environment - TEE).
- **Cân bằng năng lượng và tài nguyên xanh (Green Computing):** Tối ưu hóa hiệu suất tiêu thụ năng lượng của các cụm máy chủ biên khi hoạt động bằng năng lượng tái tạo.

## Trang 142


pháp mã hóa, bảo mật đã được nghiên cứu và triển khai thành công trên thiết bị IoT có tài nguyên hạn chế.

## BÀI TẬP CHƯƠNG 5

1. Hãy phân tích các yêu cầu và đặc trưng cơ bản của các hệ thống tính toán cho IoT.
2. Hãy so sánh ưu và nhược điểm của các mô hình điện toán đám mây (IaaS, PaaS, SaaS).
3. Hãy so sánh ưu và nhược điểm của các công nghệ điện toán đám mây và điện toán cận biên. Liệt kê những ứng dụng IoT phù hợp cho mỗi công nghệ điện toán này.
4. Hãy so sánh các công nghệ ảo hóa được sử dụng trong IoT (máy ảo truyền thống so với container).
5. Hãy xây dựng một kịch bản ứng dụng tính toán cận biên trong IoT.
6. Từ nền tảng Arduino và Raspberry Pi 3, hãy xây dựng ứng dụng y tế thông minh áp dụng điện toán đám mây và điện toán cận biên.
7. Hãy xây dựng ứng dụng Nông nghiệp thông minh áp dụng kỹ thuật điện toán đám mây và điện toán cận biên. Sau đó so sánh ưu và nhược điểm của hai hướng tiếp cận này.
8. Trong ứng dụng giám sát giao thông thông minh, các camera được đặt trên đường và truyền tín hiệu video về các gateway. Dữ liệu từ các gateway sau đó được truyền về Cloud. Hãy xây dựng ứng dụng giám sát giao thông thông minh để đếm số phương tiện qua lại trong một khoảng thời gian. Xây dựng hai kịch bản đếm số phương tiện tại gateway và tại cloud. Sau đó so sánh hai kịch bản này.

## Trang 143


# CHƯƠNG 6. QUẢN LÝ NGỮ CẢNH THÔNG MINH VÀ TRÍ TUỆ NHÂN TẠO TRONG IOT

Để tạo ra tính thông minh cho mỗi ứng dụng IoT đòi hỏi hệ thống không chỉ dừng lại ở việc thu thập và lưu trữ các giá trị cảm biến đơn thuần, mà cần phải có khả năng hiểu được ngữ cảnh xung quanh môi trường hoạt động và tự động thích ứng với các thay đổi của ngữ cảnh đó. Khái niệm nhận thức ngữ cảnh (Context-Awareness) và quản lý ngữ cảnh (Context Management) đóng vai trò trung tâm trong việc biến các thiết bị IoT thụ động thành các hệ thống thông minh chủ động phục vụ con người.

Bên cạnh đó, sự bùng nổ của các kỹ thuật Trí tuệ nhân tạo (AI), Học máy (Machine Learning) và Học sâu (Deep Learning) mang lại những công cụ đột phá giúp hệ thống IoT có thể xử lý các tập dữ liệu chuỗi thời gian khổng lồ, phát hiện các mẫu hành vi phức tạp, đưa ra các dự báo chính xác và tự động hóa quá trình ra quyết định.

Nội dung chương này trình bày các khái niệm nền tảng về ngữ cảnh và thích ứng ngữ cảnh; quy trình 4 giai đoạn trong vòng đời quản lý ngữ cảnh; phân tích chi tiết các kỹ thuật mô hình hóa ngữ cảnh và suy luận ngữ cảnh phổ biến; đồng thời giới thiệu các ứng dụng tiêu biểu của học máy và trí tuệ nhân tạo trong hệ sinh thái IoT hiện đại.

## Trang 144


cho phép các dịch vụ được tạo và tái lập trình theo ngữ cảnh sử dụng. Khái niệm nhận thức ngữ cảnh (context-awareness) được định nghĩa như sau: *"Nhận thức ngữ cảnh (context-awareness) đề cập đến khả năng của một ứng dụng, dịch vụ hoặc thậm chí là một thiết bị đầu cuối nhận thức được môi trường vật chất, trạng thái mạng, hoàn cảnh người dùng và tự động điều chỉnh hành vi của mình cho phù hợp với ngữ cảnh đó mà không cần sự can thiệp trực tiếp của con người."*

### 6.1. Ngữ cảnh và thích ứng ngữ cảnh

Trong các hệ thống tính toán phổ dụng (Ubiquitous Computing) và IoT, ngữ cảnh là nhân tố quyết định tính "thông minh" của dịch vụ. Một dịch vụ thông minh không chỉ phản hồi thụ động theo các câu lệnh cố định mà phải chủ động thích ứng linh hoạt theo thời gian, không gian và trạng thái của người sử dụng.

## Trang 145


Ngoài ra, các kỹ thuật trí tuệ nhân tạo cũng đang được chú ý trong quản lý ngữ cảnh trong IoT vì các yếu tố biến động, không chắc chắn, phức tạp và mơ hồ của dữ liệu. Trong phạm vi giáo trình này, tác giả đề cập đến những nội dung cơ bản nhất của trí tuệ nhân tạo được phục vụ trong quản lý ngữ cảnh và suy luận ngữ cảnh trong IoT.

#### 6.1.1. Ngữ cảnh

Định nghĩa kinh điển và được chấp nhận rộng rãi nhất về ngữ cảnh trong khoa học máy tính là định nghĩa của Anind Dey (năm 2001):

> *"Ngữ cảnh là thông tin bất kỳ được sử dụng để mô tả trạng thái của một thực thể. Thực thể có thể là con người, địa điểm hoặc đối tượng vật lý/luận lý có liên quan đến sự tương tác giữa người dùng và ứng dụng, bao gồm cả người dùng và ứng dụng đó."*

## Trang 146


**Hình 6.1.** Không gian ngữ cảnh hoạt động của thực thể

Dựa trên bản chất và nguồn gốc dữ liệu, ngữ cảnh trong IoT được phân loại thành 2 nhóm chính:
- **Ngữ cảnh sơ cấp (Primary Context / Low-level Context):** Là các dữ liệu đo đạc trực tiếp từ cảm biến vật lý hoặc thiết bị phần cứng mà chưa qua xử lý ngữ nghĩa. Ví dụ: vị trí tọa độ GPS (kinh độ, vĩ độ), nhiệt độ số thực (25.5°C), cường độ ánh sáng (300 Lux), độ ẩm đất (70%).
- **Ngữ cảnh thứ cấp (Secondary Context / High-level Context):** Là các thông tin trừu tượng có mức ngữ nghĩa cao hơn, được tính toán hoặc suy luận từ ngữ cảnh sơ cấp kết hợp với tri thức chuyên gia. Ví dụ: từ tọa độ GPS suy ra người dùng đang "ở nơi làm việc" hay "ở nhà"; từ nhiệt độ và độ ẩm suy ra thời tiết "dễ chịu" hay "nắng nóng oi bức".

## Trang 147


Bảng 6.1 minh họa quy tắc chuyển đổi từ ngữ cảnh sơ cấp (giá trị số đo thực tế) sang ngữ cảnh thứ cấp (mức định tính trừu tượng) phục vụ cho hệ thống điều hòa không khí:

**Bảng 6.1.** Quy đổi giá trị và mức nhiệt độ

| STT | Giá trị nhiệt độ (°C) | Mức nhiệt độ (Ngữ cảnh thứ cấp) |
|:---:|:---|:---|
| 1 | 0 - 15 | Very Low (Rất lạnh) |
| 2 | 16 - 20 | Low (Lạnh) |
| 3 | 21 - 25 | Medium (Mát mẻ / Bình thường) |
| 4 | 26 - 32 | High (Nóng) |
| 5 | > 32 | Very High (Rất nóng) |

Việc chuẩn hóa và trừu tượng hóa ngữ cảnh giúp giảm bớt sự phụ thuộc của ứng dụng vào chi tiết phần cứng cảm biến bên dưới, tạo điều kiện cho các thuật toán suy luận hoạt động nhất quán.

## Trang 148


**Đặc điểm của ngữ cảnh trong IoT:**
1. **Được thu thập từ nút cảm biến hay mạng cảm biến:** Dữ liệu mang tính phân tán, phát sinh liên tục theo dòng thời gian (streaming data).
2. **Được thu thập từ những thiết bị nhỏ và tài nguyên hạn chế:** Dẫn đến dữ liệu có thể bị trễ, ngắt quãng hoặc thiếu chính xác do hạn chế về pin và phần cứng.
3. **Tính không hoàn hảo và bất định (Imperfect & Uncertain):** Dữ liệu cảm biến thường xuyên chứa nhiễu, lỗi đo đạc hoặc bị mất gói tin trong quá trình truyền sóng vô tuyến.
4. **Tính phụ thuộc thời gian (Temporal Aspect):** Ngữ cảnh luôn biến đổi theo thời gian; giá trị ngữ cảnh chỉ có giá trị sử dụng trong một khoảng thời gian hiệu lực nhất định.

#### 6.1.2. Thích ứng ngữ cảnh

Thích ứng ngữ cảnh (Context Adaptation) là quá trình hệ thống IoT tự động thay đổi hành vi, giao diện hoặc cấu hình dịch vụ dựa trên ngữ cảnh đã được nhận diện nhằm tối ưu hóa trải nghiệm người dùng và tiết kiệm tài nguyên năng lượng.

## Trang 149


Ví dụ về thích ứng ngữ cảnh trong hệ thống chiếu sáng thông minh tại tòa nhà văn phòng:
- **Trường hợp 1:** Nếu chỉ có 1 người ngồi tại một vị trí trong phòng làm việc, hệ thống chỉ bật cụm đèn chiếu sáng tại khu vực bàn làm việc đó, tắt toàn bộ các bóng đèn khác để tiết kiệm điện.
- **Trường hợp 2:** Nếu có nhiều người ngồi tại nhiều vị trí khác nhau trong phòng hoặc đang tổ chức cuộc họp, hệ thống tự động bật toàn bộ hệ thống đèn chiếu sáng trong phòng.

**Hình 6.2.** Vòng đời quản lý ngữ cảnh trong IoT

### 6.2. Quản lý ngữ cảnh trong IoT

Quá trình quản lý ngữ cảnh trong các hệ thống IoT hiện đại tuân theo một chu trình khép kín gồm 4 giai đoạn chính (Hình 6.2):
1. **Thu thập ngữ cảnh (Context Acquisition)**
2. **Mô hình hóa ngữ cảnh (Context Modeling)**
3. **Suy luận ngữ cảnh (Context Reasoning)**
4. **Phân phối ngữ cảnh (Context Dissemination)**

## Trang 150


#### 6.2.1. Thu thập ngữ cảnh

**Thu thập ngữ cảnh (Context Acquisition):** Là bước đầu tiên chịu trách nhiệm lấy dữ liệu từ nhiều nguồn khác nhau: cảm biến vật lý (nhiệt độ, gia tốc), dịch vụ mạng (thông tin thời tiết từ API web), người dùng (nhập liệu trực tiếp) hoặc trạng thái thiết bị (mức pin, địa chỉ IP). Thu thập ngữ cảnh có thể thực hiện theo cơ chế thăm dò định kỳ (polling) hoặc hướng sự kiện theo ngưỡng (event-triggered).

#### 6.2.2. Mô hình hóa ngữ cảnh

**Mô hình hóa ngữ cảnh (Context Modeling):** Chuyển đổi dữ liệu thô thu thập được thành các cấu trúc dữ liệu chuẩn mực, có tổ chức để hệ thống phần mềm có thể lưu trữ, truy vấn, chia sẻ và suy luận hiệu quả.

#### 6.2.3. Suy luận ngữ cảnh

**Suy luận ngữ cảnh (Context Reasoning):** Là giai đoạn cốt lõi sử dụng các thuật toán tính toán để suy ra ngữ cảnh cấp cao từ ngữ cảnh cấp thấp, phát hiện mâu thuẫn dữ liệu và đưa ra quyết định hành động thích ứng cho hệ thống.

#### 6.2.4. Phân phối ngữ cảnh

**Phân phối ngữ cảnh (Context Dissemination):** Cung cấp dữ liệu ngữ cảnh đã được xử lý tới các ứng dụng hoặc cơ cấu chấp hành thông qua mô hình Publish/Subscribe (như giao thức MQTT) hoặc giao thức Request/Response (REST API).

## Trang 151


### 6.3. Các kỹ thuật mô hình hóa ngữ cảnh

Phần này trình bày chi tiết các hướng tiếp cận chính được sử dụng để mô hình hóa ngữ cảnh trong các hệ thống IoT:

#### 6.3.1. Mô hình khóa/giá trị (Key-Value Model)

Mô hình khóa/giá trị là mô hình đơn giản nhất, trong đó mỗi phần tử ngữ cảnh được biểu diễn dưới dạng một cặp `(Khóa, Giá trị)`:
```
Location = "Room_E101"
Temperature = 25.5
Status = "Active"
```
- **Ưu điểm:** Cực kỳ đơn giản, dễ cài đặt, chi phí xử lý và lưu trữ rất nhỏ.
- **Nhược điểm:** Không biểu diễn được mối quan hệ phân cấp phức tạp giữa các thực thể; không có cơ chế kiểm tra tính hợp lệ của dữ liệu; khả năng suy luận bị hạn chế tối đa.

#### 6.3.2. Mô hình sơ đồ (Markup Model - XML / JSON)

Mô hình sơ đồ sử dụng các thẻ phân cấp (tags) để cấu trúc hóa dữ liệu ngữ cảnh, phổ biến nhất là XML và JSON.

## Trang 152


Một ví dụ về mô hình hóa ngữ cảnh bằng XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Building id="E">
  <Room id="E101">
    <SensorNode id="E1.1.1">
      <Temperature unit="Celsius">25</Temperature>
      <Humidity unit="Percent">85</Humidity>
      <Status>Active</Status>
    </SensorNode>
  </Room>
</Building>
```

- **Ưu điểm:** Dễ đọc đối với cả con người và máy; hỗ trợ cấu trúc dữ liệu cây lồng nhau; có công cụ kiểm tra tính hợp lệ thông qua XML Schema (XSD) hoặc JSON Schema; được hỗ trợ phổ biến trong các giao thức truyền dữ liệu web (HTTP/REST, MQTT).
- **Nhược điểm:** Không biểu diễn được ngữ nghĩa tường minh; khả năng suy luận ngữ cảnh tự động vẫn còn hạn chế.

#### 6.3.3. Mô hình đồ họa (Graphical Model)

Sử dụng các sơ đồ đồ họa chuẩn như UML (Unified Modeling Language) hoặc ORM (Object-Role Modeling) để trực quan hóa cấu trúc dữ liệu ngữ cảnh và các quan hệ giữa các đối tượng trong giai đoạn phân tích thiết kế hệ thống.

#### 6.3.4. Mô hình dựa trên đối tượng (Object-based Model)

Mô hình hóa ngữ cảnh dựa trên các nguyên lý lập trình hướng đối tượng (OOP): đóng gói (encapsulation), kế thừa (inheritance) và đa hình (polymorphism).

## Trang 153


trên việc phân cấp và quan hệ giữa các lớp. Mô hình này cho phép đóng gói (encapsulation) và tái sử dụng. Hầu hết các ngôn ngữ lập trình cấp cao hỗ trợ các khái niệm hướng đối tượng, mô hình hóa có thể được tích hợp vào hệ thống nhận biết ngữ cảnh một cách dễ dàng. Do đó, mô hình dựa trên đối tượng phù hợp để sử dụng bên trong mã nguồn phần mềm của từng thiết bị.

#### 6.3.5. Mô hình dựa trên logic (Logic-based Model)

Biểu diễn ngữ cảnh dưới dạng các biểu thức logic vị từ (Predicate Logic) hoặc logic mệnh đề. Một tập hợp các sự kiện và quy tắc suy diễn (rules) được định nghĩa hình thức:
```prolog
inRoom(userA, roomE101).
isDark(roomE101).
lightOn(Room) :- inRoom(User, Room), isDark(Room).
```
- **Ưu điểm:** Tính hình thức toán học cao, cho phép suy luận logic chặt chẽ và kiểm tra tính nhất quán tri thức.
- **Nhược điểm:** Khó biểu diễn các dữ liệu có tính mơ hồ, không chắc chắn; độ phức tạp tính toán tăng nhanh khi tập luật lớn.

#### 6.3.6. Mô hình dựa trên ontology (Ontology-based Model)

Ontology là sự đặc tả hình thức, tường minh của một khái niệm hóa chung (an explicit specification of a conceptualization). Đây là kỹ thuật mô hình hóa ngữ cảnh mạnh mẽ và toàn diện nhất hiện nay trong IoT và Web ngữ nghĩa (Semantic Web).

Ontology được mô tả bằng ngôn ngữ chuẩn W3C như OWL (Web Ontology Language) hoặc RDF (Resource Description Framework), bao gồm:
- **Classes (Lớp khái niệm):** Đại diện cho các tập hợp thực thể (ví dụ: `Device`, `Sensor`, `Person`, `Location`).
- **Object Properties (Thuộc tính đối tượng):** Mô tả quan hệ giữa hai thực thể.

## Trang 154


Ví dụ về các khẳng định thuộc tính đối tượng (Object property assertions) và thuộc tính dữ liệu (Data property assertions) trong một Ontology:

```owl
Object property assertions:
  Sensor_101  isLocatedIn  Room_E101
  User_Nam    isInside     Room_E101
  Room_E101   isMemberOf   Building_E

Data property assertions:
  Sensor_101  hasTemperatureValue  28.5
  Sensor_101  hasBatteryLevel       85
```

**Hình 6.3.** Ví dụ về cây phân cấp Ontology trong nhà thông minh

- **Ưu điểm vượt trội của Ontology:**
  1. **Khả năng chia sẻ và liên tác tri thức (Interoperability):** Cung cấp một bộ từ vựng chung (shared vocabulary) giúp các hệ thống IoT không đồng nhất từ các hãng khác nhau có thể hiểu và trao đổi dữ liệu với nhau một cách thông suốt.
  2. **Hỗ trợ suy luận tự động mạnh mẽ:** Các cỗ máy suy diễn ontology (như Pellet, HermiT) có thể tự động suy luận ra các tri thức mới và phát hiện các mâu thuẫn dữ liệu dựa trên các quy tắc mô tả vị từ.

## Trang 155


**Bảng 6.2.** So sánh các kỹ thuật mô hình hóa ngữ cảnh

| Kỹ thuật mô hình hóa | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Khóa / Giá trị (Key-Value)** | • Đơn giản, dễ cài đặt<br>• Tốc độ truy xuất nhanh<br>• Chi phí lưu trữ nhỏ | • Không có cấu trúc phân cấp<br>• Không hỗ trợ xác thực<br>• Không thể suy luận | Ứng dụng nhỏ, lưu trữ cấu hình tạm thời |
| **Sơ đồ (Markup - XML / JSON)** | • Linh hoạt, có cấu trúc phân cấp<br>• Xác thực qua Schema<br>• Công cụ parser có sẵn rộng rãi | • Thiếu ngữ nghĩa tường minh<br>• Kích thước tệp lớn<br>• Khó biểu diễn quan hệ ngang | Trao đổi dữ liệu giữa các dịch vụ web, định dạng bản tin cảm biến (SensorML, JSON) |
| **Đồ họa (Graphical - UML)** | • Trực quan, dễ hiểu<br>• Biểu diễn quan hệ thực thể tốt<br>• Chuẩn hóa cao | • Chỉ dùng ở pha thiết kế<br>• Khó truy vấn tự động lúc chạy | Phân tích và thiết kế kiến trúc hệ thống ban đầu |
| **Dựa trên đối tượng (Object-based)** | • Đóng gói và tái sử dụng mã nguồn tốt<br>• Tích hợp tự nhiên vào ngôn ngữ OOP (Java, Python, C++) | • Khó chia sẻ giữa các hệ thống không đồng nhất<br>• Phụ thuộc ngôn ngữ | Xử lý nội bộ bên trong mã nguồn phần mềm trên thiết bị |

## Trang 156


**Bảng 6.2.** (tiếp theo)

| Kỹ thuật mô hình hóa | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Dựa trên logic (Logic-based)** | • Hình thức toán học chặt chẽ<br>• Hỗ trợ suy luận logic chính xác<br>• Kiểm tra tính nhất quán | • Khó biểu diễn dữ liệu không chắc chắn<br>• Độ phức tạp tính toán cao khi dữ liệu lớn | Xử lý các quy tắc và ràng buộc logic hình thức |
| **Dựa trên Ontology (Ontology-based)** | • Ngữ nghĩa phong phú, biểu diễn tri thức sâu<br>• Cho phép liên tác giữa các hệ thống không đồng nhất<br>• Hỗ trợ cỗ máy suy luận tự động mạnh mẽ | • Mô tả phức tạp<br>• Chi phí tính toán và bộ nhớ cao khi suy diễn | Hệ thống IoT phức tạp, Smart Home, Smart City, chia sẻ tri thức liên miền |

### 6.4. Các kỹ thuật suy luận ngữ cảnh

Suy luận ngữ cảnh (Context Reasoning) là quá trình trích xuất thông tin mới có mức ngữ nghĩa cao hơn từ dữ liệu ngữ cảnh sẵn có. Các kỹ thuật suy luận ngữ cảnh được chia làm 6 nhóm chính:
1. Học có giám sát (Supervised Learning)
2. Học không giám sát (Unsupervised Learning)
3. Dựa trên luật (Rule-based)
4. Dựa trên logic mờ (Fuzzy Logic)
5. Dựa trên ontology (Ontology reasoning)
6. Dựa trên logic xác suất (Probabilistic Logic)

## Trang 157


#### 6.4.1. Học có giám sát (Supervised Learning)

Học có giám sát sử dụng một tập dữ liệu huấn luyện đã được gán nhãn (labeled data) để học hàm ánh xạ từ đầu vào (dữ liệu cảm biến) tới đầu ra (ngữ cảnh hành vi):
- **Phân loại (Classification):** Dự đoán đầu ra là các nhãn ngữ cảnh rời rạc (ví dụ: người dùng đang "Đi bộ", "Chạy", "Ngồi", "Nằm"). Các thuật toán thông dụng: Cây quyết định (Decision Tree), Support Vector Machine (SVM), K láng giềng gần nhất (k-NN), Mạng nơ-ron nhân tạo (ANN).
- **Hồi quy (Regression):** Dự đoán đầu ra là các giá trị liên tục (ví dụ: dự báo nhiệt độ không khí trong 1 giờ tới, ước lượng mức tiêu thụ điện năng). Các thuật toán: Hồi quy tuyến tính (Linear Regression), Hồi quy phi tuyến.

#### 6.4.2. Học không giám sát (Unsupervised Learning)

Học không giám sát làm việc trên dữ liệu chưa gán nhãn (unlabeled data), tự động phân tích cấu trúc tiềm ẩn và gom nhóm các mẫu dữ liệu tương đồng:
- **Phân cụm (Clustering - K-Means, DBSCAN):** Phân chia các vị trí đo đạc cảm biến thành các vùng có đặc tính môi trường giống nhau mà không cần nhãn định trước.

## Trang 158


sử dụng trong các ứng dụng thích ứng ngữ cảnh. Cụ thể, kỹ thuật phân cụm được sử dụng ở mức thấp (mức phần cứng) trong mạng cảm biến như định tuyến hay mức cao (mức ứng dụng) như xác định vị trí trong nhà hay ngoài trời. Kỹ thuật mạng nơ-ron không giám sát như Kohonen Self Organizing Map (KSOM) được sử dụng để phân loại dữ liệu cảm biến theo thời gian.
- **Phát hiện dị thường (Anomaly Detection):** Nhận diện các giá trị cảm biến bất thường hoặc các sự kiện nguy hiểm (như rò rỉ khí gas, xâm nhập trái phép) dựa trên độ lệch so với các cụm hoạt động bình thường.

#### 6.4.3. Dựa trên luật (Rule-based Reasoning)

Suy luận dựa trên luật sử dụng tập các luật IF-THEN được định nghĩa trước bởi chuyên gia:
```
IF (Temperature > 30) AND (Presence == TRUE) THEN TurnOn(AirConditioner)
IF (SoilMoisture < 40) THEN StartPumping(Water)
```
- **Ưu điểm:** Rất trực quan, đơn giản, dễ cài đặt và thực thi rất nhanh ngay cả trên vi điều khiển nhỏ.
- **Nhược điểm:** Khó duy trì khi số lượng luật tăng lên hàng trăm luật; dễ xảy ra mâu thuẫn giữa các luật; không xử lý được các trạng thái trung gian mơ hồ.

#### 6.4.4. Dựa trên logic mờ (Fuzzy Logic)

Trong thế giới thực, nhiều khái niệm không thể phân định rạch ròi đúng (1) hoặc sai (0) mà mang tính mơ hồ: thế nào là "trời nóng", "trời mát", "độ ẩm thấp". Logic mờ (Fuzzy Logic) do Lotfi Zadeh đề xuất giải quyết bài toán này bằng cách gán cho mỗi phần tử một độ liên thuộc (membership degree) nằm trong đoạn `[0, 1]`.

## Trang 159


Hệ thống suy luận mờ bao gồm 4 khối chức năng chính:
1. **Mờ hóa (Fuzzification):** Chuyển đổi giá trị số đo thực tế (crisp input) thành các giá trị ngôn ngữ mờ thông qua các hàm liên thuộc (Membership Functions: dạng tam giác, hình thang, hình chuông Gaussian).
2. **Cơ sở luật mờ (Fuzzy Rule Base):** Tập hợp các luật mờ dạng: `IF x is A AND y is B THEN z is C`.
3. **Cỗ máy suy luận mờ (Fuzzy Inference Engine):** Kết hợp các luật mờ và tính toán mức kích hoạt của từng luật (phổ biến nhất là phương pháp Mamdani và Sugeno).
4. **Giải mờ (Defuzzification):** Chuyển đổi tập mờ kết quả đầu ra thành một giá trị điều khiển số thực cụ thể (sử dụng phương pháp trọng tâm Center of Gravity - COG).

**Ví dụ ứng dụng Logic mờ trong điều khiển nhiệt độ nhà kính nông nghiệp thông minh:**
- Đầu vào 1: Nhiệt độ hiện tại thu thập từ cảm biến.
- Đầu vào 2: Chiều hướng thay đổi nhiệt độ (đang tăng, không đổi, đang giảm).
- Đầu ra: Tín hiệu điều khiển cơ cấu chấp hành (Hệ thống sưởi, Quạt thông gió).

**Hình 6.4.** Minh họa hàm liên thuộc dạng tam giác và hình thang

## Trang 160


**Bảng 6.3.** Bảng biểu diễn thang input nhiệt độ

| Tên biến ngôn ngữ | Khoảng giá trị (°C) | Trạng thái tương ứng |
|:---|:---:|:---|
| **Cold** | < 12 | Lạnh |
| **Cool** | 11 - 15 | Hơi lạnh |
| **Normal** | 14 - 19 | Bình thường |
| **Warm** | 18 - 23 | Hơi nóng |
| **Hot** | > 22 | Nóng |

**Bảng 6.4.** Bảng biểu diễn thang input chiều hướng nhiệt độ

| Tên biến ngôn ngữ | Ý nghĩa |
|:---|:---|
| **Down** | Nhiệt độ đang giảm |
| **None** | Nhiệt độ ổn định / không đổi |
| **Up** | Nhiệt độ đang tăng |

**Bảng 6.5.** Bảng luật điều khiển nhiệt độ (Fuzzy Rules)

| STT | Nhiệt độ | Chiều hướng | Tác vụ điều khiển (Output) |
|:---:|:---:|:---:|:---|
| 1 | Cold | Down | Heating High (Sưởi mức cao) |
| 2 | Cold | None | Heating High (Sưởi mức cao) |
| 3 | Cold | Up | Heating Low (Sưởi mức thấp) |
| 4 | Cool | Down | Heating Low (Sưởi mức thấp) |
| 5 | Cool | None | Heating Low (Sưởi mức thấp) |
| 6 | Cool | Up | Nothing (Không làm gì) |
| 7 | Normal | Down / None / Up | Nothing (Không làm gì) |
| 8 | Warm | Down | Nothing (Không làm gì) |
| 9 | Warm | None | Ventilation Low (Thông gió mức thấp) |
| 10 | Warm | Up | Ventilation Low (Thông gió mức thấp) |
| 11 | Hot | Down | Ventilation Low (Thông gió mức thấp) |
| 12 | Hot | None / Up | Ventilation High (Thông gió mức cao) |

## Trang 161


**Hình 6.5.** Quy trình suy luận mờ Mamdani

Các trường hợp suy luận mờ thực tế thông qua công cụ MATLAB Fuzzy Logic Toolbox:
- **Trường hợp 1:** Nhiệt độ vào là 16.8°C và chiều hướng nhiệt độ là Up (0.92): kết quả đầu ra rơi vào vùng Nothing (không cần tác động điều hòa vì nhiệt độ mát mẻ và đang có xu hướng tăng nhẹ về mức tối ưu).
- **Trường hợp 2:** Nhiệt độ vào là 10.5°C và chiều hướng nhiệt độ là Down (-0.85): kết quả giải mờ đầu ra kích hoạt Heating High với công suất sưởi cực đại để tránh rét hại cho cây trồng.

## Trang 162


**Hình 6.6.** Giao diện Rule Viewer trong MATLAB Fuzzy Logic Toolbox

Giao diện Rule Viewer (Hình 6.6) cho phép trực quan hóa đồng thời tất cả các luật mờ được kích hoạt, xem diện tích phủ mờ của từng luật và điểm trọng tâm giải mờ kết quả cuối cùng.

## Trang 163


- **Trường hợp 3:** Ta có dữ liệu đầu vào là 14.2°C, chiều hướng nhiệt độ là đang giảm (Down) thì kết quả đầu ra kích hoạt Heating High với giá trị tính toán cụ thể là 20.1%.

#### 6.4.5. Dựa trên Ontology (Ontology Reasoning)

Suy luận dựa trên ontology tận dụng cấu trúc hình thức và ngữ nghĩa của OWL-DL:
- **Suy diễn quan hệ phân cấp (Subsumption Reasoning):** Tự động xác định một lớp này có phải là lớp con của lớp khác hay không dựa trên các thuộc tính ràng buộc.
- **Kiểm tra tính nhất quán (Consistency Checking):** Phát hiện các mâu thuẫn logic trong cơ sở tri thức (ví dụ: một cảm biến không thể đồng thời vừa ở trạng thái `TurnedOff` vừa phát ra giá trị `MeasuringActive`).
- **Khám phá tri thức ẩn (Implicit Knowledge Deduction):** Từ các quan hệ bắc cầu, đối xứng để suy ra các sự thật mới mà không cần lập trình viên khai báo thủ công.

## Trang 164


#### 6.4.6. Dựa trên Logic xác suất (Probabilistic Logic)

Kỹ thuật suy luận dựa trên logic xác suất (như Mạng Bayes - Bayesian Networks, Mô hình Markov ẩn - Hidden Markov Models, Lý thuyết Dempster-Shafer) cho phép hệ thống ra quyết định trong điều kiện dữ liệu cảm biến không chắc chắn, không đầy đủ hoặc chứa nhiều nhiễu.

Mỗi phát biểu hoặc trạng thái được gắn một phân phối xác suất có điều kiện $P(A|B)$ dựa trên định lý Bayes:
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

Ví dụ: Xác định xác suất một người dùng đang ngủ trong phòng dựa trên tập hợp nhiều bằng chứng: cảm biến áp lực đệm giường kích hoạt, cường độ ánh sáng bằng 0, độ ồn dưới 20dB và thời gian là ban đêm. Dù một cảm biến có thể bị lỗi, mạng Bayes vẫn tổng hợp các nguồn bằng chứng còn lại để đưa ra kết luận có độ tin cậy cao nhất.

## Trang 165


**Bảng 6.6.** So sánh các kỹ thuật suy luận ngữ cảnh

| Kỹ thuật suy luận | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Học có giám sát (Supervised Learning)** | • Độ chính xác cao khi có nhãn<br>• Xử lý tốt dữ liệu phi tuyến tính | • Cần tập dữ liệu huấn luyện lớn có gán nhãn<br>• Tốn tài nguyên tính toán | Nhận dạng hoạt động người dùng, dự báo thời tiết, nhận diện biển số xe |
| **Học không giám sát (Unsupervised Learning)** | • Không cần dữ liệu gán nhãn<br>• Tự động phát hiện cấu trúc ẩn | • Khó đánh giá độ chính xác<br>• Ngữ nghĩa đầu ra cần chuyên gia giải thích | Phát hiện bất thường, phân cụm nút cảm biến theo vùng môi trường |
| **Dựa trên luật (Rule-based)** | • Trực quan, dễ hiểu (IF-THEN)<br>• Cài đặt đơn giản, chạy nhanh | • Phải định nghĩa luật thủ công<br>• Dễ mâu thuẫn khi số luật lớn | Điều khiển tự động theo ngưỡng cố định (bật tắt đèn, tưới nước) |
| **Logic mờ (Fuzzy Logic)** | • Xử lý tốt tính mơ hồ, không rạch ròi<br>• Gần với tư duy con người | • Phải thiết kế hàm liên thuộc thủ công<br>• Không tự thích nghi | Điều khiển hệ thống nhiệt độ, thông gió, tưới tiêu nông nghiệp |

## Trang 166


**Bảng 6.6.** (tiếp theo)

| Kỹ thuật suy luận | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Dựa trên Ontology** | • Tận dụng tri thức ngữ nghĩa sâu sắc<br>• Tự động kiểm tra mâu thuẫn logic | • Chi phí tính toán cao<br>• Không phù hợp xử lý dữ liệu số chuỗi thời gian | Tích hợp dữ liệu ngữ cảnh đa nguồn trong Smart Home, Smart City |
| **Logic xác suất (Probabilistic Logic)** | • Xử lý xuất sắc tính không chắc chắn và dữ liệu nhiễu<br>• Kết hợp nhiều bằng chứng độc lập | • Cần biết phân phối xác suất tiên nghiệm<br>• Độ phức tạp tính toán cao | Định vị trong nhà, nhận dạng ngữ cảnh hành vi từ cảm biến nhiễu |

### 6.5. Trí tuệ nhân tạo và IoT

Sự kết hợp giữa Trí tuệ nhân tạo (AI) và Internet vạn vật (IoT) đã khai sinh ra thuật ngữ **AIoT (Artificial Intelligence of Things)**. Trong kỷ nguyên AIoT, IoT đóng vai trò là "hệ thần kinh kỹ thuật số" thu thập dữ liệu khổng lồ từ thế giới vật lý, còn AI đóng vai trò là "bộ não" phân tích thông minh và ra quyết định tự động.

## Trang 167


Sự đột phá của các kỹ thuật Trí tuệ nhân tạo trong thập kỷ qua được đánh dấu bằng những cột mốc lịch sử:
- Tháng 3/2016, hệ thống AI AlphaGo của Google DeepMind đã làm chấn động thế giới khi đánh bại kỳ thủ cờ vây số một thế giới Lee Sedol với tỉ số 4-1.
- Năm 2017, DeepMind tiếp tục công bố AlphaGo Zero với khả năng tự học hoàn toàn từ đầu thông qua học tăng cường (Reinforcement Learning) mà không cần dữ liệu ván đấu của con người và chiến thắng áp đảo phiên bản AlphaGo tiền nhiệm.

Những bước tiến nhảy vọt này đã mở ra làn sóng ứng dụng AI mạnh mẽ vào mọi ngóc ngách của đời sống, trong đó hệ sinh thái IoT là môi trường ứng dụng giàu tiềm năng bậc nhất.

## Trang 168


Hai nút thắt cổ chai lớn nhất của Học máy và Học sâu ở các giai đoạn trước đây là: (1) thiếu hụt tài nguyên tính toán mạnh mẽ và (2) thiếu dữ liệu lớn để huấn luyện.

Những năm gần đây, sự phát triển vượt bậc của các bộ tăng tốc phần cứng chuyên dụng như GPU (Graphics Processing Unit), TPU (Tensor Processing Unit), NPU (Neural Processing Unit) cùng với hạ tầng đám mây phân tán đã giải quyết triệt để nút thắt về năng lực tính toán. Đồng thời, hàng chục tỷ thiết bị IoT kết nối liên tục tạo ra nguồn dữ liệu lớn vô tận hàng ngày, trở thành mảnh đất màu mỡ cho các mô hình học máy phát triển.

#### 6.5.1. Học máy (Machine Learning)

##### 6.5.1.1. Quá trình xử lý trong học máy

Quá trình xây dựng và triển khai một mô hình học máy trong hệ thống IoT bao gồm 5 bước tuần tự:
1. **Thu thập dữ liệu (Data Collection):** Thu thập dữ liệu cảm biến từ các thiết bị IoT.
2. **Tiền xử lý dữ liệu (Data Preprocessing):** Làm sạch dữ liệu, xử lý các giá trị khuyết thiếu, lọc nhiễu tín hiệu và chuẩn hóa thang đo dữ liệu.

## Trang 169


3. **Trích xuất đặc trưng (Feature Extraction & Selection):** Lựa chọn các đặc trưng quan trọng nhất đại diện cho bài toán nhằm giảm số chiều dữ liệu và tăng tốc độ huấn luyện.
4. **Huấn luyện mô hình (Model Training):** Sử dụng tập dữ liệu huấn luyện (training set) và thuật toán học máy phù hợp để tối ưu hóa các tham số mô hình nhằm giảm thiểu hàm mất mát (loss function).
5. **Đánh giá mô hình (Model Evaluation):** Đánh giá độ chính xác của mô hình trên tập dữ liệu thử nghiệm độc lập (test set) thông qua các chỉ số đo lường như Accuracy, Precision, Recall, F1-Score.

**Hình 6.7.** Quy trình huấn luyện và dự đoán tổng quát trong học máy

## Trang 170


Thuật toán học máy lấy tập dữ liệu huấn luyện và học các thuộc tính cụ thể trong đó để giảm thiểu lỗi trong quá trình đánh giá mô hình. Sau khi huấn luyện, mô hình được kiểm tra trên tập dữ liệu thử nghiệm để đánh giá hiệu quả của mô hình được chọn và dự đoán độ chính xác của mô hình khi sử dụng trong thực tế. Một mô hình có thể cho kết quả khác nhau nếu huấn luyện và thử nghiệm trên các tập dữ liệu có phân phối khác biệt, do đó việc áp dụng kỹ thuật kiểm chứng chéo (k-fold cross validation) là rất cần thiết.

## Trang 171


**Thực thi mô hình (Inference / Deployment):** Đây là bước cuối cùng trong vòng đời học máy. Sau khi được đánh giá đạt độ chính xác yêu cầu, mô hình được triển khai vào môi trường vận hành thực tế (trên đám mây hoặc trên thiết bị biên) để thực hiện dự đoán thời gian thực khi có dữ liệu cảm biến mới gửi về.

##### 6.5.1.2. Phân loại các kỹ thuật học máy

Các thuật toán học máy được chia thành 3 nhánh chính (Hình 6.8):
1. **Học có giám sát (Supervised Learning):** Dữ liệu có nhãn đầu vào và đầu ra mong muốn. Gồm hai bài toán chính: Phân loại (Classification) và Hồi quy (Regression).
2. **Học không giám sát (Unsupervised Learning):** Dữ liệu không có nhãn. Gồm hai bài toán chính: Phân cụm (Clustering) và Giảm chiều dữ liệu (Dimensionality Reduction).
3. **Học tăng cường (Reinforcement Learning):** Tác nhân (Agent) học thông qua quá trình tương tác thử-sai với môi trường để tối đa hóa phần thưởng tích lũy (Reward).

**Hình 6.8.** Phân loại các thuật toán học máy phổ biến trong IoT

## Trang 172


Các thuật toán học có giám sát phổ biến bao gồm: Hồi quy tuyến tính, Hồi quy Logistic, K láng giềng gần nhất (k-NN), Máy hỗ trợ véc-tơ (SVM), Naive Bayes, Cây quyết định, Rừng ngẫu nhiên (Random Forest) và Mạng nơ-ron nhân tạo sâu (Deep Neural Networks - DNN).

Đối với bài toán phân loại, đầu ra là các nhãn lớp rời rạc (ví dụ: phát hiện đám cháy hay không có cháy; nhận diện loại cây trồng). Trong khi đó, đối với bài toán hồi quy, đầu ra là các giá trị số thực liên tục (ví dụ: nồng độ bụi mịn PM2.5 dự báo trong không khí).

## Trang 173


**Hình 6.9.** Minh họa bài toán phân lớp nhị phân bằng thuật toán SVM

Hình 6.9 minh họa bài toán phân lớp nhị phân sử dụng thuật toán Máy hỗ trợ véc-tơ (SVM). Thuật toán tìm kiếm một siêu phẳng phân cách tối ưu (optimal hyperplane) sao cho khoảng cách lề (margin) giữa hai lớp dữ liệu là lớn nhất, qua đó tăng cường khả năng tổng quát hóa của mô hình khi gặp dữ liệu mới.

## Trang 174


#### 6.5.2. Ứng dụng của học máy trong IoTs và các định hướng nghiên cứu

Với sự phát triển mạnh mẽ của cuộc cách mạng công nghiệp lần thứ tư, sự kết hợp giữa học máy và công nghệ IoT đang tạo ra những bước chuyển mình sâu sắc trong nhiều lĩnh vực:

1. **Giao thông thông minh (Smart Transportation):**
   - Đếm lưu lượng phương tiện giao thông tự động qua camera sử dụng các mô hình thị giác máy tính như YOLO, SSD.
   - Điều khiển đèn tín hiệu giao thông thích ứng dựa trên thuật toán học tăng cường nhằm giảm thiểu tình trạng ùn tắc vào giờ cao điểm.
   - Nhận diện biển số xe tự động và phát hiện các hành vi vi phạm giao thông (vượt đèn đỏ, lấn làn).

## Trang 175


2. **Giám sát môi trường và cảnh báo thiên tai:**
   - Dự báo chất lượng không khí (chỉ số AQI, nồng độ bụi mịn PM2.5, PM10) dựa trên chuỗi thời gian sử dụng mô hình LSTM (Long Short-Term Memory).
   - Cảnh báo sớm cháy rừng thông qua phân tích dữ liệu nhiệt độ, độ ẩm và hình ảnh từ camera giám sát trên tháp quan sát.
   - Dự báo lũ quét và sạt lở đất dựa trên dữ liệu đo mưa và độ ẩm đất tự động.

3. **Nông nghiệp thông minh (Smart Agriculture):**
   - Nhận diện bệnh hại trên lá cây trồng thông qua hình ảnh chụp từ điện thoại hoặc máy bay không người lái (UAV) sử dụng mạng nơ-ron tích chập (CNN).
   - Tự động hóa lịch tưới tiêu và bón phân tối ưu dựa trên mô hình học máy phân tích nhu cầu sinh trưởng của cây trồng và điều kiện thời tiết.

## Trang 176


4. **Thành phố thông minh và Tòa nhà thông minh (Smart Cities & Smart Buildings):**
   - Tối ưu hóa tiêu thụ năng lượng điện trong các tòa nhà văn phòng dựa trên học thói quen người dùng.
   - Giám sát bãi đỗ xe thông minh, hướng dẫn lái xe đến vị trí đỗ còn trống nhanh nhất.
   - Quản lý thu gom rác thải đô thị thông minh dựa trên cảm biến mức độ đầy của thùng rác.

## Trang 177


**Định hướng nghiên cứu tương lai:**
- **TinyML (Machine Learning trên vi điều khiển siêu nhỏ):** Nghiên cứu nén mô hình học sâu để có thể thực thi suy luận trực tiếp trên các vi điều khiển cấp thấp có RAM dưới 256kB như ARM Cortex-M, ESP32 mà không cần kết nối mạng.
- **Học liên kết bảo vệ quyền riêng tư (Privacy-preserving Federated Learning):** Cho phép huấn luyện mô hình cộng tác giữa hàng nghìn thiết bị IoT mà không cần thu thập dữ liệu nhạy cảm của người dùng về máy chủ trung tâm.
- **Lưu trữ dữ liệu thông minh tại biên (Edge Caching & Content Delivery):** Tối ưu hóa việc phân phối nội dung video và dữ liệu số trên mạng di động 5G/6G.

## Trang 178


các hệ thống Big Data. Sự phát triển của các thiết bị IoT/5G hỗ trợ cho việc thu thập dữ liệu hàng ngày, hàng giờ, mỗi phút hoặc thậm chí trong một phần nghìn giây. Đó là lý do tại sao chuỗi thời gian là rất lớn và nhiều chiều. Ngoài ra, loại dữ liệu này cũng không cố định, tức là nó có chu kỳ không đều và dựa vào các đặc điểm thống kê của nó như giá trị trung bình, giá trị trung vị, phương sai và sự thay đổi tiêu chuẩn theo thời gian. Do đó, làm thế nào để lưu trữ và làm thế nào để đối phó với tập dữ liệu lớn cho một vấn đề nhất định trong một thời gian thích hợp đòi hỏi sức mạnh, các phương pháp tự động để lấy thông tin quan trọng mà không phụ thuộc nhiều vào sự can thiệp của con người.

## BÀI TẬP CHƯƠNG 6

1. Hãy mô tả vai trò của Quản lý ngữ cảnh trong ứng dụng IoT.
2. Hãy mô tả kiến trúc của thành phần quản lý ngữ cảnh trong ứng dụng IoT.
3. Hãy so sánh các kỹ thuật mô hình hóa ngữ cảnh, và các ứng dụng có thể sử dụng mỗi loại kỹ thuật này.
4. Hãy so sánh các kỹ thuật suy luận ngữ cảnh, và các ứng dụng có thể sử dụng mỗi loại kỹ thuật này.
5. Hãy trình bày một kịch bản sử dụng trí tuệ nhân tạo trong quản lý ngữ cảnh của một ứng dụng IoT.
6. Hãy xây dựng ứng dụng đếm số lượng xe qua một giao lộ sử dụng trí tuệ nhân tạo.
7. Hãy xây dựng ứng dụng phát hiện đám cháy sử dụng kỹ thuật máy học.
8. Hãy xây dựng ứng dụng nông nghiệp thông minh sử dụng kỹ thuật học sâu.
9. Hãy xây dựng ứng dụng nhà thông minh sử dụng kỹ thuật học không giám sát.
10. Hãy xây dựng ứng dụng giám sát và cảnh báo chất lượng không khí tại Thành phố Hồ Chí Minh ứng dụng kỹ thuật máy học.

## Trang 179


# CHƯƠNG 7. TÁI CẤU HÌNH TRONG IOT

Tái cấu hình trong IoT là khả năng cho phép thay đổi tính năng, hành vi ứng dụng hoặc cấu hình hoạt động của các thiết bị IoT từ xa sau khi chúng đã được triển khai vào môi trường thực tế nhằm đáp ứng nhu cầu ngày càng cao của người sử dụng và môi trường vận hành biến đổi.

Trong thực tế triển khai các hệ thống IoT và mạng cảm biến không dây quy mô lớn (hàng trăm đến hàng nghìn nút phân bố trên các cánh đồng, trong rừng sâu hoặc gắn trong các kết cấu hạ tầng giao thông, công trình xây dựng), việc tiếp cận vật lý trực tiếp tới từng thiết bị để nạp lại phần mềm bằng dây cáp hay thay thế linh kiện là điều bất khả thi về mặt kinh tế, thời gian và công sức. Do đó, các kỹ thuật **tái lập trình qua mạng (Over-The-Air Programming - OTA)** và **tái cấu hình phần mềm động (Dynamic Software Reconfiguration)** trở thành yêu cầu sống còn.

Nội dung chương này trình bày tổng quan về các hướng tiếp cận tái cấu hình trong IoT; giới thiệu các giải pháp hiện thực OTA tiêu biểu trên các nền tảng phổ biến như TinyOS, ESP8266 và Raspberry Pi; đồng thời đề xuất khung kiến trúc tái cấu hình IoT đa nền tảng hiện đại dựa trên cách tiếp cận Mạng điều khiển bằng phần mềm (Software-Defined Networking - SDN).

## Trang 180


Thông qua chương này, người đọc có cái nhìn tổng quan về tái cấu hình trong IoT, ý nghĩa và cơ chế hiện thực của một số giải pháp hiện có. Bên cạnh đó, thông qua minh họa phát triển một giải pháp tái cấu hình cụ thể, người đọc có thể áp dụng những kỹ năng kỹ thuật, vận dụng những kiến thức liên quan để tự xây dựng các cơ chế cập nhật từ xa cho hệ thống IoT của mình.

### 7.1. Tổng quan về tái cấu hình trong IoT

Trong vòng đời hoạt động của một hệ thống IoT, nhu cầu tái cấu hình nảy sinh từ nhiều lý do:
1. **Sửa lỗi phần mềm và vá lỗ hổng bảo mật:** Phần mềm nhúng ban đầu có thể phát sinh lỗi logic hoặc lộ các lỗ hổng bảo mật cần phải được khắc phục kịp thời.
2. **Cập nhật tính năng mới:** Người dùng hoặc nhà cung cấp dịch vụ muốn bổ sung các thuật toán xử lý dữ liệu mới, hỗ trợ thêm các loại cảm biến mới.
3. **Thích ứng với sự thay đổi của môi trường và nhiệm vụ:** Thay đổi tần suất lấy mẫu cảm biến theo mùa, chuyển đổi giao thức định tuyến khi tô-pô mạng thay đổi, hoặc thay đổi ngưỡng kích hoạt cảnh báo.
4. **Tối ưu hóa năng lượng:** Điều chỉnh chu kỳ thức-ngủ (duty cycle) của nút mạng khi pin sắp cạn để kéo dài tối đa thời gian sống của mạng.

## Trang 181


### 7.2. Các hướng tiếp cận trong tái cấu hình IoT

Dựa trên mức độ trừu tượng hóa và dung lượng dữ liệu cần truyền tải qua mạng không dây, các kỹ thuật tái cấu hình trong IoT được chia thành 5 hướng tiếp cận chính:
1. Hướng tiếp cận thay thế toàn bộ image (Full Image Replacement)
2. Hướng tiếp cận dựa trên module (Module-based Approach)
3. Hướng tiếp cận dựa trên cơ sở dữ liệu (Database-based Approach)
4. Hướng tiếp cận máy ảo (Virtual Machine-based Approach)
5. Hướng tiếp cận hướng tới dịch vụ (Service-Oriented Approach)

**Hình 7.1.** Các hướng tiếp cận tái cấu hình trong IoT

#### 7.2.1. Hướng tiếp cận thay thế toàn bộ image

Là cơ chế truyền tải và thay thế toàn bộ một tệp ảnh nhị phân nhúng (binary firmware image) đang chạy trên thiết bị IoT qua sóng vô tuyến (OTA). Một dịch vụ điển hình đã hiện thực cơ chế này trên thiết bị cảm biến không dây là giao thức **Deluge** trên TinyOS [18].

## Trang 182


Trong hướng tiếp cận này, chương trình mới được biên dịch hoàn chỉnh tại máy chủ thành tệp nhị phân duy nhất. Tệp này sau đó được chia nhỏ thành các gói tin và lan truyền qua mạng không dây tới các nút cảm biến. Tại mỗi nút, ảnh nhị phân mới được ghi tạm vào bộ nhớ Flash ngoài. Sau khi toàn bộ ảnh được tải về và kiểm tra tính toàn vẹn (qua mã CRC/SHA), bộ nạp khởi động (bootloader) sẽ chép ảnh mới vào bộ nhớ Flash trong của vi điều khiển và khởi động lại thiết bị.

- **Ưu điểm:** Độ tin cậy rất cao, đơn giản về mặt kiến trúc; cho phép thay đổi toàn bộ hệ điều hành và ngăn xếp mạng; không phụ thuộc vào ngôn ngữ lập trình.
- **Nhược điểm:** Kích thước tệp truyền qua mạng rất lớn (vài chục đến vài trăm kB), tiêu tốn nhiều năng lượng truyền thông không dây của các nút cảm biến; thời gian cập nhật mạng lâu.

**Hình 7.2.** Quy trình nạp ảnh toàn phần OTA

#### 7.2.2. Hướng tiếp cận dựa trên module

Thay vì thay thế toàn bộ phần mềm, hướng tiếp cận này chỉ truyền tải các module phần mềm nhị phân cần cập nhật (dạng tệp mã đối tượng ELF hoặc thư viện liên kết động). Cơ chế nạp động (Dynamic Loader) trên hệ điều hành sẽ liên kết nóng module mới vào không gian bộ nhớ đang chạy.

## Trang 183


sao chép các native code được liên kết vào một nơi trong bộ nhớ mà ở đó chương trình có thể thực thi. Hình 7.3 mô tả kiến trúc bộ nhớ trong Contiki OS [19], giải thích vì sao hệ điều hành này có thể hỗ trợ cơ chế nạp module động. Không gian phần "Loaded program" chính là nơi các chương trình được nạp vào bộ nhớ RAM/Flash để thực thi mà không làm gián đoạn phần còn lại của nhân hệ điều hành.

**Hình 7.3.** Kiến trúc tái cấu hình dựa trên module [19]

- **Ưu điểm:** Kích thước gói tin cập nhật nhỏ hơn nhiều so với Full Image (chỉ từ 1kB đến vài kB), tiết kiệm đáng kể năng lượng vô tuyến và thời gian nạp mạng.
- **Nhược điểm:** Đòi hỏi hệ điều hành phải hỗ trợ bảng ký hiệu (symbol table) và cơ chế liên kết động phức tạp; có nguy cơ phân mảnh bộ nhớ RAM sau nhiều lần nạp/gỡ module.

#### 7.2.3. Hướng tiếp cận cơ sở dữ liệu (Database-based Approach)

Trong hướng tiếp cận này, toàn bộ mạng cảm biến không dây được trừu tượng hóa như một bảng cơ sở dữ liệu phân tán khổng lồ (Virtual Database Table), trong đó mỗi hàng đại diện cho một nút cảm biến và mỗi cột đại diện cho một loại cảm biến (nhiệt độ, ánh sáng, độ ẩm) hoặc thuộc tính của nút (mức pin, định danh nút).

## Trang 184


Việc tái cấu hình hành vi của mạng cảm biến được thực hiện đơn giản bằng cách gửi một câu lệnh truy vấn dạng SQL từ trạm gốc (Base Station) vào mạng. Hệ thống định tuyến sẽ tự động phân phối câu truy vấn qua các tuyến đường tối ưu năng lượng đến các nút cảm biến.

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

**Hướng tiếp cận Publish-Subscribe**

## Trang 185


Các hệ thống trao đổi thông điệp Publish-Subscribe thông thường bao gồm ba thành phần:
1. **Publisher (Bên phát hành):** Sản xuất và phát hành các sự kiện dữ liệu (ví dụ: nhiệt độ phòng đo được bởi nút cảm biến không dây).
2. **Subscriber (Bên đăng ký):** Các ứng dụng hoặc thiết bị người dùng đăng ký nhận các chủ đề dữ liệu mà mình quan tâm.
3. **Broker (Bộ môi giới / Gateway):** Điểm trung tâm tiếp nhận thông điệp từ Publisher, lọc theo chủ đề (topic) và chuyển tiếp tới các Subscriber tương ứng.

Việc tái cấu hình trong mô hình này được thực hiện thông qua việc thay đổi các bộ lọc đăng ký (subscription filters) tại Broker hoặc gửi các thông điệp điều khiển cấu hình qua các kênh điều khiển chuyên dụng.

**MOSDEN Middleware** [22] là một giải pháp trung gian IoT tiêu biểu hỗ trợ cơ chế này trên các thiết bị di động và gateway có tài nguyên hạn chế.

## Trang 186


các sự kiện cụ thể của hệ thống. Mỗi client được phân biệt bằng một số điện thoại (phone number) hoặc UUID. Gateway đóng vai trò event-broker trong mô hình Publish-Subscribe. Mỗi gateway sẽ nhận thông tin từ nhiều nút cảm biến (publisher). Các thông tin này sẽ được phân loại vào những kênh được quy định trước (predefined channels). Sau đó, tương ứng với mỗi kênh, gateway sẽ thông báo tới các subscriber đã đăng ký.

#### 7.2.4. Hướng tiếp cận máy ảo (Virtual Machine-based Approach)

Hướng tiếp cận này cài đặt một máy ảo siêu nhỏ (Bytecode Virtual Machine) chạy trực tiếp trên vi điều khiển của nút cảm biến (nằm phía trên hệ điều hành nhúng). Các chương trình ứng dụng được biên dịch thành các chỉ lệnh mã byte (bytecode) nhỏ gọn để máy ảo thông dịch thực thi.

Đại diện tiêu biểu nhất cho hướng tiếp cận này là máy ảo **Maté** [18] chạy trên nền hệ điều hành TinyOS. Maté là một máy ảo hướng tới bối cảnh sự kiện dựa trên điều khiển (context-based event-driven virtual machine) với một chồng quy ước gọi hàm dựa trên ngăn xếp (stack-based calling convention).

## Trang 187


**Hình 7.5.** Kiến trúc tái cấu hình dựa trên máy ảo VM

Máy ảo Maté tổ chức mã thực thi thành các viên nang (capsules) độc lập, mỗi capsule có kích thước cố định chỉ 24 byte (chứa tối đa 24 chỉ lệnh bytecode):
- **Capsule thông điệp (Message Capsule):** Chạy khi có gói tin mạng đến.
- **Capsule bộ định thời (Timer Capsule):** Chạy khi bộ định thời kích hoạt.
- **Capsule chương trình con (Subroutine Capsule):** Thực thi các hàm tính toán dùng chung.

Nhờ tập lệnh bytecode ngắn gọn được thiết kế riêng cho mạng cảm biến (chỉ thị đọc cảm biến, gửi gói tin, bật đèn LED chỉ tốn 1 byte mã lệnh), các chương trình phức tạp có thể được mã hóa thành các tệp tin có kích thước dưới 100 byte.

## Trang 188


cho phép các chương trình phức tạp có thể hiện thực với mã nguồn kích thước rất nhỏ (ít hơn 100 bytes). Điều này cho phép các nhà lập trình ứng dụng có thể tái cấu hình một mạng lưới rộng lớn các nút một cách hiệu quả, giảm chi phí truyền tải một chương trình mới đến các nút qua sóng vô tuyến.

- **Ưu điểm:** Kích thước truyền nạp siêu nhỏ, lan truyền cập nhật mạng cực nhanh, an toàn cao (mã bytecode chạy trong môi trường sandbox của máy ảo nên không thể gây treo hệ thống hay xung đột bộ nhớ).
- **Nhược điểm:** Tốc độ thực thi chậm hơn so với mã máy gốc (native code) do phải thông qua bước thông dịch; tốn thêm dung lượng bộ nhớ RAM và Flash của nút để chứa chương trình máy ảo.

#### 7.2.5. Hướng tiếp cận hướng tới dịch vụ (Service-Oriented Approach)

Trong hướng tiếp cận hướng dịch vụ (SOA), mỗi thiết bị IoT đóng vai trò là một nhà cung cấp dịch vụ (Service Provider) hoặc người tiêu thụ dịch vụ (Service Consumer). Các chức năng của thiết bị (đo nhiệt độ, điều khiển van tưới, định tuyến mạng) được trừu tượng hóa và đóng gói thành các dịch vụ web gọn nhẹ (CoAP, RESTful HTTP).

**Hình 7.6.** Kiến trúc tái cấu hình hướng dịch vụ

## Trang 189


Hệ thống trung gian IoT (IoT Middleware) quản lý danh mục dịch vụ (Service Registry). Khi cần tái cấu hình hệ thống, người quản trị chỉ cần thay đổi quy trình kết hợp dịch vụ (Service Orchestration / Composition) hoặc nạp thêm các dịch vụ mới mà không làm ảnh hưởng đến các dịch vụ đang hoạt động khác.

### 7.3. Một số giải pháp hiện thực tái cấu hình trên các loại thiết bị phổ biến

#### 7.3.1. Cơ chế hỗ trợ tái lập trình từ xa trên TinyOS

Trên hệ điều hành TinyOS, giao thức tái lập trình mạng nổi tiếng nhất là **Deluge T2** [18]. Deluge là giao thức lan truyền dữ liệu tin cậy (reliable data dissemination) được thiết kế đặc biệt để phân phối các tệp ảnh nhị phân kích thước lớn qua mạng cảm biến không dây đa chặng (multi-hop WSN).

## Trang 190


**Hình 7.7.** Quy trình truyền nạp Deluge trong TinyOS

**Một số đặc điểm kỹ thuật nổi bật của giao thức Deluge:**
1. **Thuật toán Trickle thích ứng mật độ (Density-aware Trickle Algorithm):** Deluge sử dụng cơ chế quảng bá thông điệp tóm tắt (Advertisement - ADV) dựa trên bộ định thời thích ứng Trickle. Khi mạng ổn định, chu kỳ phát ADV tăng theo cấp số nhân để tiết kiệm tối đa năng lượng vô tuyến. Khi phát hiện một nút có phiên bản ảnh mới hơn, chu kỳ Trickle lập tức được thu ngắn lại về mức mili-giây để nhanh chóng cập nhật cho toàn mạng.
2. **Cơ chế ức chế truyền trùng lặp (Suppression Mechanism):** Nếu một nút nghe thấy nhiều láng giềng đã gửi bản tin ADV hoặc yêu cầu tương tự trong chu kỳ hiện tại, nó sẽ tự động ức chế (không phát lại) để tránh va chạm và nghẽn kênh truyền.

## Trang 191


3. **Phân trang dữ liệu (Data Paging):** Một đối tượng dữ liệu nhị phân lớn ($S_{obj}$) được chia thành nhiều trang (Pages) có kích thước cố định (ví dụ 1024 byte), và mỗi trang được chia tiếp thành các gói tin nhỏ ($S_{pkt}$, khoảng 23 byte) để vừa với khung truyền IEEE 802.15.4.
   - Các nút mạng phải hoàn thành việc nhận và kiểm tra toàn vẹn toàn bộ các gói tin của Trang $i$ trước khi chuyển sang yêu cầu Trang $i+1$. Cơ chế này giúp các nút cảm biến chỉ cần duy trì một vùng đệm RAM nhỏ cho một trang đơn lẻ thay vì phải giữ toàn bộ ảnh nhị phân trong bộ nhớ.
4. **Cơ chế an toàn Golden Image:** Bộ nhớ Flash ngoài của mote cảm biến được dành riêng một phân vùng lưu trữ phiên bản phần mềm chuẩn xuất xưởng (Golden Image). Nếu quá trình nạp ảnh mới bị gián đoạn do hết pin hoặc ảnh mới bị lỗi không khởi động được, hệ thống sẽ tự động khôi phục lại Golden Image để đảm bảo nút mạng không bao giờ bị "biến thành cục gạch" (bricked).

## Trang 192


Trong các giải pháp hiện đại, một máy tính nhúng nhỏ gọn như **Raspberry Pi** thường được cấu hình chạy môi trường TinyOS đóng vai trò là trạm gốc (Base Station Gateway) kết nối qua cổng USB với nút điều phối Coordinator. Raspberry Pi nhận các tệp ảnh nhị phân biên dịch từ đám mây qua Wi-Fi/Ethernet và tự động kích hoạt tiến trình nạp Deluge xuống mạng cảm biến.

#### 7.3.2. Cơ chế tái lập trình từ xa trên ESP8266

Họ vi điều khiển ESP8266 và ESP32 của Espressif Systems được tích hợp sẵn ngăn xếp Wi-Fi và TCP/IP, cung cấp khả năng cập nhật phần mềm không dây (OTA) cực kỳ mạnh mẽ và tiện lợi trong môi trường Arduino IDE và ESP-IDF.

## Trang 193


Hiện tại, trong hệ thống phần mềm và kho thư viện lập trình của ESP8266 trên nền tảng Arduino có 3 phương pháp tái cấu hình, cập nhật OTA từ xa qua mạng:
1. **Arduino IDE OTA:** Nạp mã trực tiếp từ máy tính của lập trình viên qua giao thức mạng nội bộ LAN tới thiết bị ESP8266 mà không cần cắm cáp USB.
2. **Web Browser OTA:** ESP8266 khởi tạo một Web Server nội bộ; người dùng truy cập địa chỉ IP của ESP8266 qua trình duyệt web trên điện thoại hoặc máy tính, chọn tệp nhị phân `.bin` và bấm nút Upload để nạp chương trình mới.
3. **HTTP Server Auto-Update (OTA qua máy chủ đám mây):** ESP8266 định kỳ gửi yêu cầu HTTP GET đến máy chủ web trung tâm kiểm tra phiên bản phần mềm. Nếu có phiên bản mới hơn, thiết bị tự động tải tệp nhị phân về và nạp vào bộ nhớ.

**Hình 7.8.** Cơ chế phân vùng Flash hỗ trợ OTA trên ESP8266

## Trang 194


**Cơ chế phân vùng bộ nhớ Flash (Dual-Bank OTA):**

Bộ nhớ Flash của ESP8266 được phân chia thành hai vùng lưu trữ ứng dụng riêng biệt có kích thước bằng nhau:
- **Phân vùng Sketch 1 (OTA slot 0)**
- **Phân vùng Sketch 2 (OTA slot 1)**

**Hình 7.9.** Quy trình cập nhật OTA trên ESP8266 qua Web Server

Khi thiết bị đang chạy chương trình từ Phân vùng 1, tệp nhị phân mới tải về sẽ được ghi tuần tự vào Phân vùng 2. Sau khi ghi xong và xác thực mã kiểm tra MD5 thành công, cờ nạp khởi động (boot flag) trong bộ nhớ RTC/EEPROM sẽ được chuyển sang chỉ định Phân vùng 2. Thiết bị tự khởi động lại và chạy chương trình mới. Nếu quá trình ghi bị ngắt quãng, thiết bị vẫn khởi động an toàn từ Phân vùng 1 cũ.

## Trang 195


#### 7.3.3. Cơ chế tái cấu hình từ xa trên Raspberry Pi

Đối với các thiết bị máy tính nhúng mạnh mẽ chạy hệ điều hành Linux như Raspberry Pi, việc tái cấu hình có thể thực hiện ở hai mức độ:
1. **Mức hệ điều hành và Firmware (Full OS OTA):** Sử dụng các nền tảng quản lý cập nhật hệ thống nhúng chuyên nghiệp như **Mender** [23] hoặc **balenaOS**.
2. **Mức ứng dụng và dịch vụ:** Sử dụng công nghệ ảo hóa nhẹ **Docker Containers** kết hợp các công cụ quản lý cấu hình tự động như **Ansible**.

## Trang 196


**Giải pháp cập nhật hệ điều hành Mender:**

Mender là nền tảng mã nguồn mở quản lý cập nhật OTA cho hệ điều hành Linux nhúng. Mender áp dụng kiến trúc cập nhật **A/B Dual Rootfs Partitioning**:
- Ổ đĩa lưu trữ (thẻ nhớ MicroSD hoặc eMMC) được chia thành 2 phân vùng hệ thống tệp gốc: `rootfsA` và `rootfsB`.
- Thiết bị đang hoạt động trên `rootfsA`. Khi có bản cập nhật mới từ Mender Server, tệp ảnh hệ thống mới sẽ được ghi vào `rootfsB`.
- Bộ nạp khởi động U-Boot được cấu hình thử khởi động vào `rootfsB`. Nếu hệ thống khởi động thành công và xác nhận dịch vụ mạng hoạt động bình thường, phân vùng B sẽ trở thành phân vùng hoạt động chính thức. Nếu khởi động thất bại hoặc dịch vụ bị lỗi, U-Boot tự động quay ngược (rollback) về phân vùng A, đảm bảo tính liên tục tuyệt đối của hệ thống.

## Trang 197


**Giải pháp tái cấu hình mức dịch vụ bằng Docker Containers trên Raspberry Pi:**

Thay vì cập nhật toàn bộ hệ điều hành cồng kềnh (hàng trăm MB đến vài GB), giải pháp hiện đại là đóng gói từng ứng dụng IoT (dịch vụ đọc cảm biến, dịch vụ gateway MQTT, dịch vụ phân tích AI) vào các Docker Container riêng biệt chạy trên Raspbian OS.

**Hình 7.10.** Kiến trúc tái cấu hình trên Raspberry Pi sử dụng Ansible/Docker

- Khi cần cập nhật tính năng mới hoặc sửa lỗi, người quản trị chỉ cần đẩy (push) image container mới lên Docker Hub hoặc máy chủ lưu trữ riêng.
- Một tiến trình quản trị trên Raspberry Pi (hoặc công cụ Ansible/Docker Compose) nhận lệnh và tự động tải image mới về, dừng container cũ và khởi chạy container mới chỉ trong vài giây mà không cần khởi động lại bo mạch Raspberry Pi.

## Trang 198


Một điểm quan trọng khác là Docker là một nền tảng mã nguồn mở, chính vì thế Docker được cộng đồng phát triển mạnh mẽ để đóng góp và mở rộng khả năng của nó cho phù hợp với các nhu cầu ngày càng cao. Gần đây, trong nhiều nghiên cứu về phát triển hạ tầng IoT đa nền tảng, đảm bảo khả năng đáp ứng linh hoạt các yêu cầu khác nhau, công cụ ảo hóa Docker đang trở thành tiêu chuẩn thực tế.

### 7.4. Khung kiến trúc phát triển một giải pháp tái cấu hình IoT đa nền tảng dựa trên cách tiếp cận SDN

#### 7.4.1. Kiến trúc quản lý hệ thống IoT dựa trên SDN

Mạng điều khiển bằng phần mềm (Software-Defined Networking - SDN) là mô hình mạng tiên tiến phân tách rạch ròi giữa:
- **Mặt phẳng điều khiển (Control Plane):** Tập trung hóa logic định tuyến, quản lý cấu hình và ra quyết định thông minh vào bộ điều khiển trung tâm (SDN Controller).
- **Mặt phẳng chuyển tiếp dữ liệu (Data Plane):** Các thiết bị mạng chỉ thực hiện chuyển tiếp gói tin thuần túy theo các bảng luật (Flow Tables) được chỉ định bởi bộ điều khiển.

## Trang 199


Mạng cận biên (edge network) bao gồm một lượng lớn các thiết bị IoT đầu cuối như cảm biến, động cơ, thiết bị di động... Những thiết bị này thu thập dữ liệu và sau đó gửi về thiết bị cổng, máy trạm (gateway) trong vùng mạng truy cập. Để có thể giải quyết nhu cầu về khả năng đáp ứng, khả năng lập trình lại, những thiết bị này thường chạy những dịch vụ hỗ trợ khả năng cấu hình mềm dẻo.

**Hình 7.11.** Kiến trúc quản lý hệ thống IoT dựa trên SDN

Việc áp dụng SDN vào IoT mang lại khả năng tái cấu hình linh hoạt:
- **Tập trung hóa quản trị:** Người quản trị có thể giám sát toàn bộ trạng thái mạng và cập nhật chính sách phân phối dữ liệu từ một vị trí trung tâm duy nhất.
- **Tái cấu hình luồng dữ liệu mềm dẻo:** Thay đổi đường truyền gói tin, ưu tiên chất lượng dịch vụ (QoS) cho các gói tin cảnh báo khẩn cấp mà không cần thay đổi phần cứng thiết bị mạng.

## Trang 200


thực và thử nghiệm cách làm quản lý tập trung, lập trình lại cho kiến trúc IoT ở mức độ vùng mạng cận biên (edge network) và vùng mạng truy cập (access network).

#### 7.4.2. Khung kiến trúc xây dựng giải pháp tái cấu hình IoT (SD-IoTR)

Giải pháp kiến trúc **SD-IoTR (Software-Defined IoT Reconfiguration Framework)** được đề xuất nhằm hỗ trợ tái cấu hình đồng nhất cho các hệ thống IoT đa nền tảng (kết hợp đồng thời giữa các nút cảm biến TinyOS, nút vi điều khiển ESP8266/Arduino và các gateway Raspberry Pi).

Khung kiến trúc SD-IoTR bao gồm 3 lớp phân cấp theo chiều dọc (Hình 7.12):
1. **Lớp hệ thống (System / Device Layer):** Bao gồm các nút cảm biến và gateway vật lý, cài đặt các agent tái cấu hình tương ứng với từng nền tảng phần cứng (Deluge Agent trên TinyOS, OTA Handler trên ESP8266, Docker Daemon trên Raspberry Pi).
2. **Lớp trung gian (Middleware / Control Layer):** Là trung tâm điều khiển trung tâm (SD-IoTR Controller), tiếp nhận các yêu cầu tái cấu hình từ tầng trên, biên dịch thành các lệnh điều khiển cụ thể cho từng loại thiết bị và giám sát tiến trình cập nhật.
3. **Lớp ứng dụng (Application Layer):** Cung cấp giao diện đồ họa web cho người quản trị thực hiện quản lý danh mục thiết bị, giám sát trạng thái mạng và phát lệnh cập nhật phần mềm.

## Trang 201


**Hình 7.12.** Khung kiến trúc tái cấu hình đa nền tảng SD-IoTR

Lớp trung gian Middleware cung cấp các bộ điều khiển logic:
- **Device Manager:** Quản lý vòng đời và thông tin cấu hình phần cứng của từng nút.
- **Reconfiguration Engine:** Quyết định chiến lược tái cấu hình phù hợp nhất cho từng thiết bị (chọn nạp Full Image, nạp Module hay nạp Container tùy theo tài nguyên thiết bị).
- **Security & Verification Module:** Ký số các bản cập nhật phần mềm và kiểm tra tính toàn vẹn nhằm ngăn chặn việc kẻ tấn công nạp mã độc vào hệ thống IoT.

## Trang 202


Hệ thống cung cấp tập hợp các giao diện lập trình ứng dụng RESTful APIs phong phú để các ứng dụng ở tầng trên có thể kích hoạt quá trình tái cấu hình:
- `POST /api/v1/devices/{id}/firmware`: Phát lệnh cập nhật firmware từ xa cho thiết bị có định danh `{id}`.
- `GET /api/v1/devices/{id}/status`: Kiểm tra trạng thái tiến độ nạp mã hiện tại.
- `POST /api/v1/containers/{id}/restart`: Khởi động lại hoặc cập nhật container dịch vụ trên gateway.
- `POST /api/v1/network/rules`: Cập nhật bảng luật định tuyến luồng dữ liệu SDN cho toàn mạng.

## Trang 203


giao tiếp chủ yếu bằng các REST APIs. HTTP REST được hiện thực mang đến khả năng giao tiếp dựa trên nền tảng web giữa các ứng dụng IoT cụ thể với hệ thống điều khiển ở trung tâm. Bên cạnh đó, giao thức MQTT với cơ chế Publish/Subscribe cũng được sử dụng kết hợp để gửi các bản tin đánh thức và kích hoạt nạp mã tức thời tới hàng nghìn thiết bị phân tán.

### 7.5. Ứng dụng của chức năng tái cấu hình trong hệ thống IoT và các định hướng nghiên cứu

Khả năng tái cấu hình từ xa mở ra nhiều ứng dụng thiết thực và quan trọng:
1. **Bảo trì và vận hành hệ thống quy mô lớn tự động:** Cập nhật đồng loạt hàng nghìn thiết bị đo đếm điện tử thông minh (Smart Metering) trên toàn quốc mà không cần cử nhân viên kỹ thuật tới từng hộ gia đình.
2. **Thích ứng với sự cố mạng và tiết kiệm năng lượng:** Tự động điều chỉnh cấu trúc mạng tô-pô khi có một số nút trung gian bị hết pin, chuyển giao vai trò Cluster Head cho các nút còn nhiều năng lượng hơn.

## Trang 204


3. **Thay đổi dịch vụ mạng, kiến trúc, kết nối mạng từ xa:** Ngày nay, khi IoT được ứng dụng và triển khai trong nhiều lĩnh vực khác nhau, kiến trúc mạng của hệ thống IoT thường rất phức tạp và triển khai với quy mô lớn. Chính vì thế, các công nghệ mạng hiện đại như SDN/NFV cho phép thực hiện việc cấu hình kết nối mạng từ xa, thay đổi các chức năng mạng, dịch vụ mạng một cách tiện lợi mang lại nhiều ý nghĩa trong việc vận hành và tối ưu hệ thống.

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
10. Hãy trình bày một phương pháp tái cấu hình ứng dụng kiến trúc mạng được định nghĩa bởi phần mềm (Software Defined Networking) và mô tả vai trò của mỗi thành phần trong kiến trúc này.

## Trang 205


# KẾT LUẬN

Trong cuốn sách này, chúng tôi đã tập trung vào những nội dung sau:

**Chương 1:** Trình bày tổng quan về công nghệ Internet vạn vật (IoT), các xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam. Trong đó, chúng tôi đặc biệt chú trọng đến quy chuẩn về IoT của các tổ chức hoặc liên minh quốc tế nhằm cung cấp đến người đọc, đặc biệt là sinh viên kiến thức về các tiêu chuẩn IoT. Mục tiêu là để định hướng khi thiết kế và phát triển các ứng dụng và giải pháp IoT có tính tương thích (compatibility) và sẵn sàng cao (portability).

**Chương 2:** Trình bày các lĩnh vực và ứng dụng IoT cụ thể nhằm giới thiệu đến sinh viên các ứng dụng IoT thực tế. Để tăng tính thực tiễn, chúng tôi cũng đã giới thiệu các ứng dụng IoT đã và đang triển khai ở Trường Đại học Công nghệ Thông tin – Đại học Quốc gia TP.HCM, ví dụ như trạm quan trắc môi trường SmartCity đặt trong khuôn viên Trường Đại học CNTT.

**Chương 3:** Trình bày các kiến trúc mạng khác nhau được sử dụng trong việc kiến thiết mạng IoT như kiến trúc cây (Tree), kiến trúc vòng (Ring), kiến trúc chuỗi (Chain), kiến trúc không cần hạ tầng (Mesh). Các bộ giao thức mạng IoT phổ dụng cũng đã được giới thiệu chi tiết về kiến trúc và cách vận hành. Trong khi bộ giao thức ZigBee đại diện cho xu hướng giao thức IoT chạy độc lập, và do đó muốn kết nối đến thiết bị đầu cuối từ mạng Internet cần thông qua một Internet gateway, bộ giao thức 6LoWPAN đại diện cho xu hướng mở rộng mạng IP (Spanning IP), tức là có thể truy cập và điều khiển trực tiếp thiết bị IoT từ Internet.

**Chương 4:** Trình bày về các nền tảng phần cứng và phần mềm phổ dụng để phát triển các ứng dụng và giải pháp IoT hiện nay. Chúng tôi giới thiệu chủ yếu các nền tảng phần cứng dễ dàng làm việc với các nền tảng mã nguồn mở (open-source

## Trang 206


platforms) và có sẵn ở Việt Nam với giá thành hợp lý, từ đó sinh viên có thể dễ dàng phát triển sản phẩm và làm chủ công nghệ.

**Chương 5:** Trình bày về các công nghệ nền, bao gồm điện toán đám mây (cloud computing) và tính toán cận biên (edge computing). Đây là các công nghệ nền phát triển hiện nay để hiện thực hoàn chỉnh giải pháp phần backend hoặc edge của giải pháp IoT. Chúng tôi cũng đã giới thiệu giải pháp ứng dụng điện toán đám mây để phát triển hệ thống giả lập mạng cảm biến không dây quy mô lớn trên nền tảng OpenStack.

**Chương 6:** Trình bày các khái niệm cơ bản về ngữ cảnh, quản lý ngữ cảnh thông minh và ứng dụng của trí tuệ nhân tạo, học máy trong IoT. Các kỹ thuật mô hình hóa ngữ cảnh và suy luận ngữ cảnh (như logic mờ, học máy) được phân tích chi tiết nhằm trang bị cho sinh viên năng lực xây dựng các hệ thống IoT có khả năng tự nhận thức và thích ứng thông minh với môi trường.

**Chương 7:** Trình bày về các kỹ thuật tái cấu hình và tái lập trình từ xa (OTA) trong IoT. Phân tích các hướng tiếp cận tái cấu hình từ mức nạp ảnh nhị phân, nạp module, nạp bytecode máy ảo cho đến nạp container trên các thiết bị phổ biến như TinyOS, ESP8266 và Raspberry Pi, cùng khung kiến trúc SDN hỗ trợ quản lý và tái cấu hình mạng IoT đa nền tảng tập trung.

Mặc dù đã có những bước tiến vượt bậc, nhiều thách thức kỹ thuật lớn trong lĩnh vực IoT vẫn đang là các chủ đề nghiên cứu mở đầy sôi động:

## Trang 207


- **Vấn đề bảo mật và quyền riêng tư (Security & Privacy):** Bên cạnh tính riêng tư, tính bảo mật cho ứng dụng IoT cũng là một vấn đề lớn đang được nghiên cứu. Các kỹ thuật bảo mật truyền thống khó có thể được triển khai trực tiếp trên các thiết bị IoT bởi vì như đã trình bày trong Chương 4, các thiết bị IoT hầu như là các thiết bị nhúng có năng lực tính toán, bộ nhớ và năng lượng tiêu thụ thấp. Một số rủi ro bảo mật chính gồm: nghe lén trên đường truyền vô tuyến, giả mạo nút mạng, chiếm quyền điều khiển thiết bị cơ cấu chấp hành và tấn công từ chối dịch vụ (DDoS) thông qua mạng botnet IoT.
- **Tiêu chuẩn hóa và tính liên tác (Standardization & Interoperability):** Sự phân mảnh của hàng trăm chuẩn kết nối và nền tảng phần mềm khác nhau từ các nhà sản xuất đòi hỏi các chuẩn giao tiếp chung ở mức ngữ nghĩa (như Web of Things - WoT của W3C) để các thiết bị có thể tự động khám phá và liên tác không rào cản.
- **Công nghệ mạng 5G và 6G trong IoT:** Hỗ trợ kết nối mật độ siêu lớn (massive Machine-Type Communications - mMTC) và truyền thông độ trễ cực thấp độ tin cậy cực cao (Ultra-Reliable Low-Latency Communications - URLLC) mở ra tương lai cho các hệ thống xe tự hành thông minh và phẫu thuật y tế từ xa.

## Trang 208


- **Học sâu và Trí tuệ nhân tạo trên thiết bị biên (Edge AI / TinyML):** Để giảm kích thước sử dụng bộ nhớ, các hệ điều hành IoT thường được tối giản các chức năng và sử dụng thư viện bên thứ ba ở mức tối thiểu, trong khi đó các ứng dụng Học sâu lại yêu cầu tài nguyên cao và sử dụng năng lượng nhiều. Do đó, việc nghiên cứu tối ưu hóa các thuật toán học máy, lượng tử hóa mô hình để có thể chạy suy luận thời gian thực trực tiếp trên các vi điều khiển công suất thấp mà vẫn đảm bảo độ chính xác cao là một trong những định hướng nghiên cứu then chốt trong giai đoạn hiện nay.

Cuốn giáo trình này được biên soạn với mong muốn cung cấp một tài liệu học tập, tham khảo có hệ thống, kết hợp hài hòa giữa lý thuyết nền tảng và hướng dẫn thực hành thực tiễn cho sinh viên ngành Công nghệ Thông tin, Kỹ thuật Máy tính, Điện tử Viễn thông và các kỹ sư đang nghiên cứu, phát triển trong lĩnh vực Internet of Things.

## Trang 209


# TÀI LIỆU THAM KHẢO

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
14. A. Dunkels, B. Grönvall và T. Voigt, "Contiki - a lightweight and flexible operating system for tiny networked sensors", trong *29th Annual IEEE International Conference on Local Computer Networks (LCN)*, 2004.

## Trang 210


15. M. H. Qutqut, A. Al-Sakran, F. Almasalha và H. S. Hassanein, "Comprehensive survey of the IoT open source OSs", *IET Wireless Sensor Systems*, tập 8, số 6, pp. 323-339, 2018.
16. A. Alnoman, S. K. Sharma, W. Ejaz và A. Anpalagan, "Emerging Edge Computing Technologies for Distributed IoT Systems", *IEEE Network*, tập 33, số 6, pp. 140-147, 2019.
17. Charith Perera, Arkady Zaslavsky, Peter Christen và Dimitrios Georgakopoulos, "Context Aware Computing for The Internet of Things: A Survey", *IEEE Communications Surveys & Tutorials*, tập 16, số 1, pp. 414-454, 2014.
18. J. W. Hui và D. Culler, "The dynamic behavior of a data dissemination protocol for network programming at scale", trong *Proceedings of the 2nd International Conference on Embedded Networked Sensor Systems (SenSys '04)*, Baltimore, MD, USA, 2004, pp. 81-94.
19. A. Dunkels, N. Finne, J. Eriksson và T. Voigt, "Run-time dynamic linking for reprogramming wireless sensor networks", trong *Proceedings of the 4th International Conference on Embedded Networked Sensor Systems (SenSys '06)*, Boulder, Colorado, USA, 2006.
20. S. R. Madden, M. J. Franklin, J. M. Hellerstein và W. Hong, "TinyDB: an acquisitional query processing system for sensor networks", *ACM Transactions on Database Systems (TODS)*, tập 30, số 1, pp. 122-173, 2005.
21. T. D. Nguyen, Q. M. Nguyen và H.-A. Pham, "Publish-Subscribe Framework for Event Management in IoT-based Applications", trong *11th South East Asian Technical University Consortium (SEATUC) Symposium*, Ho Chi Minh City, Vietnam, 2017.
22. C. Perera, P. P. Jayaraman, A. Zaslavsky, P. Christen và D. Georgakopoulos, "MOSDEN: An Internet of Things Middleware for Resource Constrained Mobile Devices", trong *47th Hawaii International Conference on System Sciences*, Waikoloa, HI, USA, 2014, pp. 1053-1062.
23. I. Grokhotkov, "ESP8266 Arduino Core OTA Updates", [Trực tuyến]. Available: https://arduino-esp8266.readthedocs.io/en/latest/ota_updates/readme.html.
24. L.-V. Hung, H.-V. Dang và L.-T. Quan, "UITIoT-Vlab: A Low Cost Physical IoTs Testbed Based on Over-The-Air Programming Approach", trong *5th EAI International Conference on Industrial Networks and Intelligent Systems (INISCOM 2019)*, Ho Chi Minh City, Vietnam, 2019.

## Trang 211


25. O. Hahm, E. Baccelli, H. Petersen và N. Tsiftes, "Operating Systems for Low-End Devices in the Internet of Things: A Survey", *IEEE Internet of Things Journal*, tập 3, số 5, pp. 720-734, 2016.
26. F. Javed, M. K. Afzal, M. Sharif và B. S. Kim, "Internet of Things (IoT) Operating Systems Support, Networking Technologies, Applications, and Challenges: A Comparative Review", *IEEE Communications Surveys & Tutorials*, tập 20, số 3, pp. 2062-2100, 2018.
27. P. Mathur, "A Simple Weather Forecasting Model Using Mathematical Regression", *International Journal of Computer Science and Network Security*, 2012.
28. Alessandro Floris và Luigi Atzori, "Managing the Quality of Experience in the Multimedia Internet of Things: A Layered-Based Approach", *Sensors*, tập 16, số 12, tr. 2057, 2016.
29. T. F. Megahed, S. Abdelkader và A. Zakaria, "Energy Management in Zero-Energy Building Using Neural Network Predictive Control", *IEEE Internet of Things Journal*, 2019.
30. A. Gaur, B. Scotney, G. Parr và S. McClean, "Smart City Architecture and its Applications Based on IoT", *Procedia Computer Science*, tập 52, pp. 1089-1094, 2015.
31. P. Rahimi and C. Chrysostomou, "Improving the Network Lifetime and Performance of Wireless Sensor Networks for IoT Applications Based on Fuzzy Logic", trong *15th International Conference on Distributed Computing in Sensor Systems (DCOSS)*, Santorini Island, Greece, 2019, pp. 667-674.
32. Qianqian Li, Sarada Gochhayat, Mauro Conti và Fang-Ai Liu, "EnergIoT: A solution to improve network lifetime of IoT devices", *Pervasive and Mobile Computing*, tập 42, pp. 124-138, 2017.
33. V. Valls, G. Iosifidis and T. Salonidis, "Maximum Lifetime Analytics in IoT Networks", trong *IEEE INFOCOM 2019 - IEEE Conference on Computer Communications*, Paris, France, 2019, pp. 1369-1377.
34. F. Wang, M. Zhang, X. Wang, X. Ma and J. Liu, "Deep Learning for Edge Computing Applications: A State-of-the-Art Survey", *IEEE Access*, tập 8, pp. 58322-58336, 2020.
35. M. G. Sarwar Murshed, Christopher Murphy, Daqing Hou, Nazar Khan, Ganesh Ananthanarayanan và Faraz Hussain, "Machine Learning at the Network Edge: A Survey", *ACM Computing Surveys*, 2019.

## Trang 212


36. Abu Sufian, Aniruddha Ghosh, Ali Safaa Sadiq, Florentin Smarandache, "A Survey on Deep Transfer Learning to Edge Computing for Mitigating the COVID-19 Pandemic", *Journal of Systems Architecture*, tập 108, tr. 101830, 2020.
37. W. Y. B. Lim et al., "Federated Learning in Mobile Edge Networks: A Comprehensive Survey", *IEEE Communications Surveys & Tutorials*, tập 22, số 3, pp. 2031-2063, 2020.
38. Jie Tang, Dawei Sun, Shaoshan Liu và Jean-Luc Gaudiot, "Enabling Deep Learning on IoT Devices", *Computer*, tập 50, số 6, pp. 92-96, 2017.

## Trang 213


# THÔNG TIN XUẤT BẢN

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
- **Biên tập:** Nhà xuất bản Đại học Quốc gia TP. Hồ Chí Minh.

## Trang 214


*(Trang bìa sau của sách giáo trình)*

