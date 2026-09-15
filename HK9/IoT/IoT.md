# Phát triển ứng dụng IoT

> Tài liệu tổng hợp môn học Internet vạn vật (IoT). File này được tổ chức để tiếp tục bổ sung các chương và tài liệu tham khảo khác.
>
> Nguồn Chương 1: `Baigiang/Chuong1/Phat trien ung dung IoT_Chuong1.pdf`.

## Mục lục môn học

1. [Chương 1: Giới thiệu](#chương-1-giới-thiệu)
2. [Chương 2: Các lĩnh vực ứng dụng IoT](#chương-2-các-lĩnh-vực-ứng-dụng-iot)
3. [Chương 3: Các kiến trúc mạng và bộ giao thức mạng IoT](#chương-3-các-kiến-trúc-mạng-và-bộ-giao-thức-mạng-iot)
4. [Chương 4: Các nền tảng phần cứng và phần mềm IoT thông dụng](#chương-4-các-nền-tảng-phần-cứng-và-phần-mềm-iot-thông-dụng)
5. [Chương 5: Điện toán đám mây, điện toán cận biên và IoT](#chương-5-điện-toán-đám-mây-điện-toán-cận-biên-và-iot)
6. [Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT](#chương-6-quản-lý-ngữ-cảnh-thông-minh-và-trí-tuệ-nhân-tạo-trong-iot)
7. [Tài liệu tham khảo](#tài-liệu-tham-khảo)

## Thông tin học phần

- **Giảng viên:** TS. Nguyễn Đình Tứ, Trưởng Bộ môn Cơ điện tử, Khoa Kỹ thuật Cơ khí, Đại học Kỹ thuật – Công nghệ Cần Thơ.
- **Email:** `ndtu@ctuet.edu.vn`
- **Điện thoại:** `0776181954`
- **Tên tiếng Việt:** Phát triển ứng dụng IoT
- **Tên tiếng Anh:** IoT Application Development
- **Mã học phần:** TT188
- **Số tín chỉ:** 03 tín chỉ, gồm 30 tiết lý thuyết và 30 tiết thực hành.
- **Mục tiêu:** Giới thiệu kiến thức cơ bản về Internet vạn vật, các yêu cầu, tiêu chuẩn và ứng dụng IoT; từ đó giúp sinh viên thiết kế, đánh giá các hệ thống theo dõi và điều khiển qua Internet.
- **Kỹ năng:** Thiết kế các hệ thống theo dõi và điều khiển qua Internet trên hệ thống thực.

## Chương 1: Giới thiệu

### Nội dung chương

- **1.1.** Tổng quan về công nghệ Internet vạn vật.
- **1.2.** Xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam.
- Bài tập Chương 1.

### 1.1. Tổng quan về công nghệ Internet vạn vật

#### Khái niệm và bối cảnh

Thế giới có khoảng 20 tỷ thiết bị kết nối Internet và số lượng này tăng trung bình khoảng 80 thiết bị mới mỗi giây. Theo thống kê được trình bày trong bài giảng, tốc độ tăng này hướng tới khoảng 50 tỷ thiết bị vào năm 2020. Đây là viễn cảnh **Internet vạn vật** (*Internet of Things*, thường viết là IoT hoặc IoTs).

Công nghệ mạng IoT được phát triển để thiết bị và đồ vật có thể kết nối, trao đổi và tương tác với nhau. Ví dụ:

- Tra cứu thông tin thực phẩm ngay trên tủ lạnh.
- Điều khiển ô tô từ xa mà không cần trực tiếp lái xe.
- Tích hợp cảm biến cho khoảng 4–5 triệu xe máy ở Hà Nội hoặc Thành phố Hồ Chí Minh để hỗ trợ nhà quản lý kiểm soát lưu lượng giao thông.

**Hình minh họa trang 7:** Sơ đồ tiến hóa của Internet, từ kết nối máy tính và con người đến kết nối các vật thể, dữ liệu và dịch vụ trong IoT.

**Hình minh họa trang 9:** Biểu đồ số lượng thiết bị IoT theo thời gian, minh họa xu hướng tăng nhanh đến năm 2020.

#### Định nghĩa IoT

IoT là mạng lưới các vật thể có nhận dạng rõ ràng, được tích hợp năng lực xử lý phần mềm, cảm biến và khả năng kết nối phổ biến với Internet.

Ở dạng đơn giản, một hệ thống IoT là mạng các phần tử vật lý được hỗ trợ bởi:

- **Cảm biến (sensors):** Thu thập thông tin từ môi trường hoặc đối tượng.
- **Bộ nhận dạng (identifiers):** Xác định nguồn dữ liệu, chẳng hạn địa chỉ IP hoặc mã của thiết bị.
- **Phần mềm (software):** Phân tích dữ liệu và tạo ra thông tin có ích.
- **Kết nối Internet:** Truyền thông, trao đổi dữ liệu và gửi thông báo.

Trong định nghĩa đầy đủ hơn, IoT cần bao gồm cả **tiêu chuẩn (standards)** và **quy trình (processes)** để các vật thể kết nối qua Internet, trao đổi dữ liệu bằng các tiêu chuẩn công nghiệp, bảo đảm khả năng liên thông và thực hiện các quy trình hữu ích, phần lớn được tự động hóa.

- **Dữ liệu (data):** Được chuyển đổi thành thông tin và tri thức để hỗ trợ quyết định tốt hơn.
- **Quy trình (process):** Đưa đúng thông tin đến đúng người hoặc máy tại đúng thời điểm.
- **Vật thể (things):** Các thiết bị và đối tượng vật lý kết nối với Internet và với nhau nhằm đưa ra quyết định thông minh.

Trong IoT, “things” có thể là bất cứ thứ gì: thiết bị gia dụng, tòa nhà, ô tô, con người, động vật, cây cối hoặc các loại máy móc.

**Hình minh họa trang 11–12:** Các sơ đồ mô tả IoT như sự kết hợp giữa *Things*, Internet, dữ liệu, tiêu chuẩn và quy trình; dữ liệu được biến đổi thành thông tin phục vụ quyết định thông minh.

#### Yêu cầu cơ bản của một giải pháp IoT

Một giải pháp IoT cơ bản cần có:

1. **Nhận dạng duy nhất cho mỗi vật thể:** Ví dụ địa chỉ IP hoặc mã nhận dạng thiết bị.
2. **Khả năng giao tiếp giữa các vật thể:** Có thể dùng truyền thông không dây hoặc các phương thức mạng khác.
3. **Khả năng cảm nhận thông tin:** Dùng cảm biến để đo một hoặc nhiều thuộc tính của vật thể/môi trường.
4. **Môi trường truyền thông:** Thường là mạng viễn thông hoặc hạ tầng mạng cho phép dữ liệu đi từ cảm biến đến hệ thống xử lý.

Với các yêu cầu này, người dùng có thể theo dõi và điều khiển vật thể từ bất kỳ nơi nào trên thế giới.

#### Vì sao cần theo dõi và điều khiển từ xa?

Các lý do chính gồm:

- Chuyên gia theo dõi và điều khiển thiết bị từ xa, ví dụ theo dõi nhiệt độ hoặc huyết áp của bệnh nhân tại nhà.
- Dùng điện thoại thông minh để tìm hiểu một vật thể; chẳng hạn tìm vị trí chìa khóa ô tô, một loại thông tin mà công cụ tìm kiếm thông thường không cung cấp trực tiếp.
- Cơ quan quản lý điều hành thành phố thông minh tối ưu hơn, chẳng hạn quản lý năng lượng, giấy phép lái xe, hồ sơ hành chính và dịch vụ cho người cao tuổi.
- Cung cấp các hình thức giải trí và trò chơi có chi phí phù hợp hơn.

Các khả năng này tạo ra cơ hội lớn cho người tiêu dùng, doanh nghiệp, chính phủ, bệnh viện và nhiều tổ chức khác.

#### Ai sẽ theo dõi và điều khiển?

Dịch vụ IoT có thể được theo dõi và điều khiển bởi con người hoặc máy móc:

- Chủ nhà theo dõi ngôi nhà bằng điện thoại dựa trên hệ thống an ninh đã cài đặt; đồng thời điều khiển đèn, máy điều hòa, máy sưởi và các thiết bị khác.
- Nhà cung cấp dịch vụ theo dõi và điều khiển dịch vụ cho khách hàng từ trung tâm vận hành mạng (NOC).

#### Bảo đảm an toàn và bảo mật

Bảo mật là mối quan tâm lớn của IoT. Hệ thống phải ngăn người không được cấp quyền truy cập, đồng thời ngăn kẻ tấn công chiếm quyền điều khiển và gửi dữ liệu giả. Rủi ro đặc biệt nghiêm trọng trong các hệ thống chăm sóc sức khỏe, ngân hàng và các hệ thống điều khiển có ảnh hưởng vật lý.

Trước IoT, nhân sự an ninh CNTT thường kiểm soát toàn bộ mạng và các thiết bị phía sau tường lửa. Với IoT, dữ liệu được thu thập từ các cảm biến bên ngoài, thường là cảm biến di động đặt ở nơi công cộng. Thiết bị của bên thứ ba và mô hình **BYOD (Bring Your Own Device)** cũng đưa nguồn dữ liệu ngoài tổ chức vào mạng.

Các vùng dễ bị tổn thương gồm:

- **Dữ liệu khi truyền:** Dữ liệu đi từ cảm biến đến gateway, từ gateway đến trung tâm dữ liệu hoặc đến điện thoại người dùng. Nếu giao thức truyền không được bảo vệ và mã hóa, dữ liệu có thể bị nghe lén hoặc tấn công trung gian.
- **API và quyền điều khiển thiết bị:** Nếu bị chiếm quyền, kẻ xâm nhập có thể tắt camera, vô hiệu hóa hệ thống theo dõi bệnh nhân hoặc kiểm soát cả mạng.
- **Bản thân dữ liệu IoT:** Cần kiểm soát quyền truy cập và mã hóa dữ liệu lưu trữ. Lưu trữ dùng chung trên đám mây có thể làm lộ dữ liệu giữa các khách hàng; dữ liệu cũng có thể bị giả mạo qua Bluetooth.
- **Thông tin định danh:** Tài khoản, thông tin xác thực của người dùng hoặc mạng có thể bị đánh cắp. Việc sử dụng mật khẩu mặc định của nhà cung cấp làm tăng rủi ro.

**Hình minh họa trang 15–16:** Các ảnh minh họa việc giám sát nhà ở và chăm sóc bệnh nhân bằng camera/hệ thống IoT; người dùng có thể theo dõi trên thiết bị di động nhưng phải kiểm soát quyền truy cập.

#### Mô hình IoT bốn lớp

Mô hình bốn lớp được trình bày trong bài giảng gồm:

1. **Lớp thiết bị IoT (IoT Device Level):** Cảm biến và cơ cấu chấp hành, tức các “things” trong IoT.
2. **Lớp mạng IoT (IoT Network Level):** Gateway, router, switch và các thành phần mạng IoT.
3. **Lớp nền tảng dịch vụ ứng dụng IoT (IoT Application Services Platform Level):** Triển khai, cấu hình, xử lý sự cố, bảo mật, quản lý và giám sát thiết bị IoT.
4. **Lớp ứng dụng IoT (IoT Application Level):** Các ứng dụng vận hành trên mạng IoT.

Ưu điểm của mô hình:

- **Giảm độ phức tạp:** Chia các phần tử và quy trình giao tiếp thành các thành phần nhỏ, dễ phát triển, thiết kế và xử lý sự cố.
- **Chuẩn hóa thành phần và giao diện:** Xác định thành phần trong từng lớp và giao diện giữa các lớp, giúp nhiều nhà cung cấp phối hợp.
- **Kỹ thuật mô-đun:** Cho phép nhiều loại phần cứng và phần mềm IoT giao tiếp với nhau.
- **Khả năng liên thông giữa nhà cung cấp:** Các khối công nghệ có thể phối hợp và tương tác.
- **Tăng tốc đổi mới:** Nhà phát triển tập trung vào bài toán chính thay vì lặp lại các chức năng nền tảng.
- **Đơn giản hóa đào tạo:** Bài toán IoT lớn được chia thành các thành phần dễ học và quản lý hơn.

**Hình minh họa trang 20–22:** Sơ đồ bốn lớp từ thiết bị/cảm biến, mạng, nền tảng dịch vụ đến ứng dụng; các mũi tên thể hiện giao tiếp giữa các lớp.

#### Các yếu tố thúc đẩy IoT

IoT đã trở thành lực lượng quan trọng thúc đẩy chuyển đổi doanh nghiệp và tạo ảnh hưởng gián đoạn trên nhiều ngành, nhiều lĩnh vực xã hội. Bài giảng trình bày các yếu tố thúc đẩy gồm sự hội tụ IT/OT, sự bùng nổ của thiết bị di động và mạng xã hội, phân tích dữ liệu tại biên, điện toán đám mây và ảo hóa, bùng nổ công nghệ phần cứng/phần mềm, chuyển đổi số, giao diện người dùng nâng cao, tốc độ tiếp nhận IoT, yêu cầu bảo mật và định luật Moore.

##### Hội tụ IT và OT

- **OT (Operation Technology):** Thế giới của nhà máy, thiết bị điều khiển và tự động hóa công nghiệp; bao gồm máy móc, bộ điều khiển, cảm biến và cơ cấu chấp hành phục vụ vận hành.
- **IT (Information Technology):** Hệ thống thông tin đầu cuối, điện toán, lưu trữ dữ liệu và mạng; hỗ trợ tự động hóa quy trình kinh doanh, CRM, chuỗi cung ứng, logistics và nhân sự.

Trước đây IT và OT thường do hai tổ chức riêng quản lý, với văn hóa, triết lý và công nghệ khác nhau. IT linh hoạt hơn trong cập nhật phần mềm và đưa công nghệ mới vào sử dụng. OT phụ thuộc vào dữ liệu thời gian thực cho an toàn, bảo mật và điều khiển; quy trình phải được kiểm thử, tin cậy và thường phải vận hành 24/7, như hệ thống lọc nước đô thị, nên không thể tùy ý dừng để cập nhật.

**Hình minh họa trang 23–25:** Các sơ đồ về động lực IoT và sự hội tụ giữa hệ thống CNTT với hệ thống vận hành công nghiệp.

##### Các mô hình kinh doanh dựa trên Internet

- **Uber:** Nền tảng Internet kết nối hành khách với tài xế. Vì tài xế không phải nhân viên của Uber và số lượng xe có thể tham gia rất lớn, nền tảng phải mở rộng nhanh với chi phí biên thấp. Cảm biến trong điện thoại tài xế, gồm con quay hồi chuyển, GPS và gia tốc kế, được dùng để theo dõi tốc độ, gia tốc, phanh và hành vi lái xe.
- **Uber Eats:** Dịch vụ vận chuyển đồ ăn, là ví dụ về mở rộng nền tảng vận tải sang một dịch vụ Internet khác.
- **Airbnb:** Dịch vụ Internet cho phép đăng, tìm và thuê chỗ ở. Dịch vụ bắt đầu từ việc cung cấp phòng và bữa sáng cho người tham dự hội nghị ở San Francisco năm 2008, sau đó mở rộng tới các sự kiện lớn.
- **Amazon:** Bắt đầu năm 1994 như một nhà bán sách trực tuyến rồi mở rộng sang âm nhạc, phim, điện tử và hàng gia dụng. Amazon dùng nền tảng Internet bảo mật để kết nối đơn hàng với các đối tác, thay đổi mô hình bán lẻ truyền thống.
- **Tesla:** Thành lập năm 2003 với mục tiêu phát triển ô tô điện cao cấp, sau đó dùng lợi nhuận để phát triển xe điện giá thấp hơn. Tesla được xem là một ví dụ nổi bật của IoT trong sản xuất và phương tiện: xe có hàng nghìn cảm biến, được kết nối và cập nhật dựa trên dữ liệu.

**Hình minh họa trang 26–34:** Logo và ảnh minh họa Uber/Uber Eats, Airbnb, Amazon, các cửa hàng tự động và xe Tesla; nội dung nhấn mạnh nền tảng Internet, cảm biến và dữ liệu tạo ra mô hình kinh doanh mới.

##### Xe tự lái

Xe tự lái có thể chia thành:

- **Bán tự động:** Thực hiện một số tác vụ như phanh hoàn toàn khi đến gần vật cản hoặc tự lái trên đường cao tốc.
- **Hoàn toàn tự động:** Tự đi từ điểm xuất phát đến đích mà không cần tương tác của người lái. Nhóm này có thể là xe do người dùng vận hành hoặc xe không người lái.

An toàn là một ưu điểm lớn. Xe dùng nhiều cảm biến như cảm biến đo khoảng cách bằng laser, radar và camera. Cơ cấu chấp hành điều khiển vô lăng và phanh. Dữ liệu cảm biến kết hợp với GPS và hệ thống dẫn đường để xác định vị trí, dựng mô hình ba chiều môi trường xung quanh, tìm đường tối ưu, tránh vật cản và gửi lệnh đến cơ cấu chấp hành.

IoT được áp dụng trong giao tiếp giữa các bộ phận trên xe, giữa xe với hạ tầng bên đường và giữa các xe tự lái.

**Hình minh họa trang 35–37:** Ảnh xe tự lái và sơ đồ cảm biến/radar/camera; luồng xử lý đi từ cảm nhận môi trường đến mô hình hóa, ra quyết định và điều khiển xe.

##### Bùng nổ thiết bị di động và mạng xã hội

- Lưu lượng dữ liệu di động tăng khoảng 18 lần trong vài năm. Sự tăng trưởng đến từ số người dùng và lượng dữ liệu mỗi người tiêu thụ; điện thoại thông minh trung bình tạo khoảng 4 GB dữ liệu mỗi tháng vào năm 2019.
- IoT kết nối đồ vật với con người, cho phép theo dõi và điều khiển từ xa theo thời gian thực.
- Facebook, Instagram, Twitter, YouTube và các dịch vụ đám mây như AWS, Salesforce là biểu hiện của việc chuyển dịch quy mô lớn lên đám mây.
- Dữ liệu Internet tăng rất nhanh; dữ liệu được tạo ra mỗi ngày đã ở quy mô tương đương một phần rất lớn tổng dữ liệu được tích lũy trong lịch sử loài người.

**Hình minh họa trang 38–39:** Biểu đồ tăng lưu lượng dữ liệu di động và logo các mạng xã hội/dịch vụ đám mây.

##### Phân tích tại biên

- **Dữ liệu lớn (big data):** Lượng dữ liệu rất lớn được hệ thống CNTT tạo ra và tích lũy trong quá trình vận hành sản phẩm, quy trình hoặc dịch vụ. Có thể phân tích bằng kỹ thuật thống kê để nhận ra mẫu và rút ra hiểu biết; con người không thể xử lý thủ công do khối lượng quá lớn.
- **Dữ liệu có cấu trúc:** Dữ liệu có thể tổ chức thành hàng và cột, ví dụ dữ liệu khách hàng, doanh số và tồn kho. Loại dữ liệu này thường có giá trị cao, đã làm sạch và được lập chỉ mục.
- **Dữ liệu phi cấu trúc:** Khó tổ chức hoặc gom nhóm, ví dụ hình ảnh, ảnh X-quang, video, dữ liệu mạng xã hội và đầu ra máy móc trộn với văn bản.

Bài giảng giới thiệu so sánh các giai đoạn **Analytics 1.0, 2.0 và 3.0**. Hình so sánh trên trang 42 là bảng tổng hợp các yếu tố chính của ba giai đoạn phân tích.

**Hình minh họa trang 40–42:** Sơ đồ mô tả dữ liệu lớn, dữ liệu có cấu trúc/phi cấu trúc và bảng so sánh Analytics 1.0–3.0.

##### Điện toán đám mây và ảo hóa

Điện toán đám mây, được bài giảng giới thiệu từ năm 2008, cho phép doanh nghiệp thuê ngoài toàn bộ hoặc một phần hạ tầng tính toán cho các nhà cung cấp đám mây công cộng, chẳng hạn Amazon AWS, Microsoft Azure và Google Compute Engine.

##### Bùng nổ công nghệ phần cứng và phần mềm

Phần cứng IoT như cảm biến, máy tính giá rẻ Raspberry Pi và vi điều khiển mã nguồn mở Arduino, cùng với phần mềm IoT, được phát triển nhanh hơn và rẻ hơn. Các thiết bị này làm thay đổi hành vi người dùng và tạo ra cơ hội kinh doanh mới.

**Hình minh họa trang 43–44:** Logo AWS, Microsoft Azure, Google Compute Engine và ảnh Raspberry Pi B+, Raspberry Pi Zero, Arduino.

##### Hội tụ và chuyển đổi số

Hội tụ số ban đầu tập trung vào việc chuyển sang vận hành “không giấy”. Theo nghĩa rộng, hội tụ là quá trình các công nghệ, quy trình và dữ liệu vốn tách rời kết hợp để tạo ra sản phẩm, dịch vụ và trải nghiệm mới, từ đó làm thay đổi ngành. Điện thoại thông minh là ví dụ điển hình vì kết hợp camera, danh bạ, bản đồ và trình phát media.

Giao diện người dùng cũng được nâng cao, bao gồm giao diện đồ họa, giao diện di động, các phương thức tương tác trực quan và trải nghiệm thực tế tăng cường.

**Hình minh họa trang 45–46:** Hình mô tả chuyển đổi số/hội tụ chức năng trên điện thoại và ví dụ giao diện người dùng hiện đại.

##### Tốc độ tiếp nhận IoT

Bài giảng minh họa tốc độ tăng của lưu lượng IP toàn cầu trong giai đoạn 2015–2020 và nêu nhận định tốc độ tiếp nhận công nghệ IoT có thể nhanh hơn nhiều lần so với điện lực và điện thoại.

##### Sự gia tăng yêu cầu bảo mật

Bảo vệ dữ liệu, hệ thống doanh nghiệp và dữ liệu cá nhân là yêu cầu có từ khi mạng dữ liệu xuất hiện. Khi Internet thương mại phát triển, vấn đề mở rộng sang quyền riêng tư, giao dịch tài chính và tội phạm mạng. Với IoT, bảo mật mạng còn phải bao gồm cả **an toàn vật lý**, vì lệnh độc hại có thể tác động đến máy móc, phương tiện, nhà máy hoặc sức khỏe con người.

**Hình minh họa trang 47–48:** Biểu đồ lưu lượng IP tăng theo thời gian và hình minh họa mối liên hệ giữa an ninh mạng với an toàn thiết bị vật lý.

##### Định luật Moore

Tác động của định luật Moore được tóm tắt qua ba quan sát:

1. Trong lịch sử phần cứng máy tính, năng lực tính toán tăng gần gấp đôi sau khoảng 18 tháng.
2. Kích thước công nghệ lưu trữ bằng transistor silicon tiếp tục thu nhỏ, tiến gần giới hạn nguyên tử; ngày càng nhiều năng lực xử lý và lưu trữ được đặt trong cùng kích thước thiết bị.
3. Giá thành mỗi transistor giảm hơn 50% mỗi năm.

**Hình minh họa trang 49–50:** Biểu đồ/ảnh minh họa xu hướng thu nhỏ, tăng năng lực và giảm giá của phần cứng theo định luật Moore.

### Các lĩnh vực chịu tác động của AI và IoT

#### Giao thông và nơi làm việc

- **Giao thông:** Phân tích giao thông để giảm thời gian đi lại; ứng dụng gọi xe xác định giá; dự đoán chuỗi cung ứng; phương tiện tự hành.
- **Nơi làm việc:** Robot trong sản xuất; kiểm tra an toàn tự động trong nhà máy; vận chuyển tự hành; hỗ trợ tuyển dụng; bảng chấm công tự động.
- Hình minh họa có xe Tesla dùng AI/autopilot và robot hình người Pepper của SoftBank Robotics.

#### Giáo dục và thể thao

- **Giáo dục:** Kiểm tra đạo văn; chấm điểm tự động; giao diện học tập tùy biến; giáo viên hoặc giảng viên ảo.
- **Thể thao:** Thiết bị đeo để phân tích thành tích; bán vé thông minh; tự động tạo video nổi bật; trọng tài bằng thị giác máy tính.

#### Y tế và nông nghiệp

- **Y tế:** Robot phẫu thuật tự động; nhận dạng và chẩn đoán bệnh tự động; dự đoán bùng phát dịch.
- **Nông nghiệp:** Robot thu hoạch; thị giác máy tính theo dõi sức khỏe cây trồng và đất; phân tích dự đoán tác động môi trường lên cây trồng.

#### Giải trí và nhà thông minh

- **Giải trí:** Gợi ý âm nhạc trên Spotify, Apple Music và Google Play Music; tự động sáng tác nhạc; gợi ý phim/truyền hình trên Netflix, Amazon Prime và Hulu.
- **Nhà thông minh:** Trợ lý cá nhân; tự động đặt hàng; an ninh gia đình; điều khiển nhiệt độ và ánh sáng.

#### Quốc phòng và các xu hướng tương lai

- **Quốc phòng:** Phương tiện bay không người lái (UAV); phát hiện dân thường; ra quyết định tự động; nhận dạng mục tiêu; chẩn đoán và bảo trì hệ thống vũ khí.
- **Giao thông tự động:** Mục tiêu dài hạn là tự động hóa toàn bộ hoạt động vận tải.
- **Công nghệ cyborg:** AI và robot có thể hỗ trợ vượt qua giới hạn nhận thức và thể chất, gồm tay chân robot giao tiếp với não.
- **Giải quyết biến đổi khí hậu:** Big Data, AI và IoT có thể nhận dạng xu hướng và đề xuất giải pháp cho các vấn đề quy mô toàn cầu.
- **Dự đoán tương lai:** Học máy dùng dữ liệu quá khứ để dự đoán các sự kiện trong tương lai.

**Hình minh họa trang 51–56:** Các nhóm hình về giao thông, robot nhà máy, giáo dục, thể thao, y tế, nông nghiệp, giải trí, nhà thông minh, UAV, robot quân sự, cyborg và phân tích biến đổi khí hậu.

### Ví dụ hệ thống giám sát và điều khiển IoT

Một hệ thống được trình bày có khả năng:

- Thu thập dữ liệu cảm biến.
- Phân tích dữ liệu.
- Trình bày dữ liệu trên giao diện đồ họa GUI được lập trình bằng LabVIEW.
- Cập nhật thông tin cảm biến trực tuyến qua Google Spreadsheets và kết nối Internet.
- Truy cập dữ liệu qua dịch vụ SMS gateway.
- Gửi cảnh báo kịp thời để người dùng can thiệp khi cần.

**Trang 58 – hệ thống đo và điều khiển:** Sơ đồ cho thấy các cảm biến nhiệt độ, oxy và pH gửi dữ liệu vào MCU Tiva C Series TM4C123G LaunchPad. MCU giao tiếp UART với module SIM900 và module ZigBee; dữ liệu được đưa lên ứng dụng Android. Hệ thống có màn hình hiển thị và cơ cấu chấp hành để điều khiển.

**Trang 59 – giám sát ao nuôi tôm:** Các nút cảm biến cố định và di động truyền dữ liệu ở tần số 433 MHz về bộ xử lý trung tâm, sau đó dữ liệu đi qua Internet đến người dùng. Giao diện web hiển thị thông tin ao nuôi và biểu đồ nhiệt độ theo thời gian.

### Nhà máy thông minh, 5G và điện toán biên

Một ví dụ tại ORing, NCU (National Central University) và Chunghwa Telecom là nhà máy thông minh dựa trên Industry 4.0. Hệ thống phát triển các công nghệ gia công laser, phóng điện và điện hóa, đồng thời tích hợp AI, phân tích dữ liệu lớn và điện toán biên.

- **Trang 60:** 5G được dùng trong sản xuất thông minh; mô hình kết hợp AI, Big Data và Edge Computing để xử lý dữ liệu gần nguồn.
- **Trang 61:** Kiến trúc nhà máy có truyền thông 5G, hệ thống tính toán biên, bảo mật và khu vực sản xuất; dây chuyền có hệ thống AMR tự hành và kiểm tra quang học tự động (AOI).
- **Trang 62:** Dữ liệu hình ảnh và dữ liệu cảm biến từ máy gia công đi qua module ADC tốc độ cao, FPGA và các gateway công nghiệp 5G cố định/di động tới cụm tính toán biên. Thông tin điều khiển được gửi ngược về máy và AMR.
- **Trang 63:** So sánh gia công bằng laser xung dài và laser xung siêu ngắn; sơ đồ thể hiện vùng nóng chảy, vùng ảnh hưởng nhiệt, nứt vi mô, vật liệu bắn ra và plasma. Ảnh hiển vi/đồ thị cho thấy kết quả đo và ảnh hưởng của quá trình laser lên bề mặt.
- **Trang 64:** Ví dụ giao diện thực tế tăng cường (AR) dùng điện thoại để hiển thị thông số và trạng thái máy, hướng dẫn vận hành và dữ liệu máy trong bối cảnh nhà máy.

### 1.2. Xu thế ứng dụng IoT và công nghệ liên quan cho đô thị thông minh ở Việt Nam

Công nghệ IoT/5G, kỹ thuật xử lý dữ liệu lớn (Big Data) và trí tuệ nhân tạo (AI) đóng vai trò quan trọng trong các đổi mới của công nghệ thông tin, truyền thông và nhiều lĩnh vực ứng dụng.

**Thành phố thông minh** là một hướng ứng dụng thu hút sự chú ý của chính phủ, cộng đồng học thuật và ngành CNTT ở nhiều quốc gia. Big Data/AI và IoT/5G cung cấp các công cụ, công nghệ cần thiết để chuyển đổi các thành phố lớn thành nơi đáng sống, làm việc và tận hưởng.

Khi được tích hợp đúng vào hạ tầng thành phố thông minh, các công nghệ IoT/5G mới có thể:

- Hỗ trợ số lượng lớn kết nối không dây từ nhiều loại thiết bị như cảm biến, camera, thiết bị AR/VR và xe thông minh.
- Cung cấp mạng tốc độ cao.
- Truyền dữ liệu đáng tin cậy.
- Đáp ứng yêu cầu độ trễ thấp.
- Hỗ trợ quản lý, giám sát và tự động hóa đô thị.

Tại Việt Nam, dù vẫn còn nhiều bất cập, các đô thị đang phát triển theo hướng tiếp cận các mô hình tiên tiến và xu thế hội nhập quốc tế. Đây là tiền đề để ứng dụng CNTT, truyền thông, IoT, 5G, Big Data và AI trong phát triển đô thị thông minh và quản lý thông minh.

**Hình minh họa trang 65–66:** Các trang kết luận nhấn mạnh vai trò kết hợp IoT/5G, Big Data và AI trong hạ tầng đô thị thông minh Việt Nam; trang cuối có sơ đồ/các khối công nghệ liên quan đến kết nối thiết bị, dữ liệu và dịch vụ đô thị.

### Bài tập Chương 1

Bản PDF chỉ hiển thị tiêu đề **“BÀI TẬP CHƯƠNG 1”** ở trang nội dung, không có trang câu hỏi bài tập chi tiết kèm theo trong phần đã cung cấp.

## Chương 2: Các lĩnh vực ứng dụng IoT

> Chưa bổ sung nội dung. Sẽ nhập từ tài liệu Chương 2 khi có tài liệu nguồn.

## Chương 3: Các kiến trúc mạng và bộ giao thức mạng IoT

> Chưa bổ sung nội dung. Sẽ nhập từ tài liệu Chương 3 khi có tài liệu nguồn.

## Chương 4: Các nền tảng phần cứng và phần mềm IoT thông dụng

> Chưa bổ sung nội dung. Sẽ nhập từ tài liệu Chương 4 khi có tài liệu nguồn.

## Chương 5: Điện toán đám mây, điện toán cận biên và IoT

> Chưa bổ sung nội dung. Sẽ nhập từ tài liệu Chương 5 khi có tài liệu nguồn.

## Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT

> Chưa bổ sung nội dung. Sẽ nhập từ tài liệu Chương 6 khi có tài liệu nguồn.

## Tài liệu tham khảo

### Tài liệu đã chuyển sang Markdown

- [Giáo trình Công nghệ Internet of Things và Ứng dụng](Thamkhao/GT_IoT_Cong_nghe_IoT_va_ung_dung.md) — OCR từ bản scan 214 trang.
- [Internet of Things from Hype to Reality – The Road to Digitization, Third Edition](Thamkhao/2022_Internet_of_Things_from_Hype_to_Reality_3rd.md) — chuyển đổi từ bản PDF có lớp văn bản, 471 trang.
- [Automated Monitoring and Control System for Shrimp Farms](Thamkhao/2015_Automated_monitoring_and_control_shrimp_farms.md) — chuyển đổi từ bài báo 5 trang.

1. Lê Trung Quân, Huỳnh Văn Đặng và Nguyễn Khánh Thuật, *Giáo trình Công nghệ Internet of Things và Ứng dụng*, NXB Đại học Quốc gia Thành phố Hồ Chí Minh, 2021.
2. Ammar Rayes và Samer Salam, *Internet of Things from Hype to Reality – The Road to Digitization*, 3rd Edition, Springer, 2022.
3. Nguyen Tang Kha Duy, Nguyen Dinh Tu, Tra Hoang Son và Luong Hong Duy Khanh, “Automated Monitoring and Control System for Shrimp Farms based on Embedded System and Wireless Sensor Network”, *2015 IEEE International Conference on Electrical, Computer and Communication Technologies (ICECCT)*, Coimbatore, India, 2015, trang 1–5.
4. Neil Cameron, *Electronics Projects with the ESP8266 and ESP32*, 1st Edition, Apress, 2021.

### Liên kết được nêu trong bài giảng

- [AWS – What is AWS?](https://aws.amazon.com/vi/what-is-aws/)
- [Định luật Moore – Wikipedia tiếng Việt](https://vi.wikipedia.org/wiki/%C4%90%E1%BB%8Bnh_lu%E1%BA%ADt_Moore)
- Nguồn hình về nhà máy 5G thông minh: ORing, NCU và Chunghwa Telecom.
- Nguồn hình về điện toán biên: Bizfly Cloud.

## Ghi chú biên tập

- Nội dung chữ được trích xuất từ PDF Chương 1 và hiệu chỉnh lại lỗi dính chữ, ký hiệu đầu dòng và xuống dòng do bố cục slide.
- Các hình/sơ đồ đã được xem trực tiếp; những hình có ý nghĩa nội dung được chuyển thành mô tả, luồng xử lý hoặc danh sách thành phần ngay tại vị trí tương ứng.
- Các số liệu trong tài liệu được giữ theo slide gốc; khi dùng cho báo cáo hoặc nghiên cứu nên kiểm tra lại nguồn và mốc thời gian.
