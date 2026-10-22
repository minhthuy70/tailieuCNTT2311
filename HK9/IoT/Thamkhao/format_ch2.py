import re, sys

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    text = f.read()

ch2_text = """## Trang 32

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

"""

idx32 = text.find('## Trang 32\n')
idx52 = text.find('## Trang 52\n')
assert idx32 != -1 and idx52 != -1

new_text = text[:idx32] + ch2_text + text[idx52:]
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Updated Chapter 2 successfully!')
