# Mục lục môn học

1. [Chương 1: Giới thiệu](#chương-1-giới-thiệu)
2. [Chương 2: Các lĩnh vực ứng dụng IoT](#chương-2-các-lĩnh-vực-ứng-dụng-iot)
3. [Chương 3: Các kiến trúc mạng và bộ giao thức mạng IoT](#chương-3-các-kiến-trúc-mạng-và-bộ-giao-thức-mạng-iot)
4. [Chương 4: Các nền tảng phần cứng và phần mềm IoT thông dụng](#chương-4-các-nền-tảng-phần-cứng-và-phần-mềm-iot-thông-dụng)
5. [Chương 5: Điện toán đám mây, điện toán cận biên và IoT](#chương-5-điện-toán-đám-mây-điện-toán-cận-biên-và-iot)
6. [Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT](#chương-6-quản-lý-ngữ-cảnh-thông-minh-và-trí-tuệ-nhân-tạo-trong-iot)
7. [Tài liệu tham khảo](#tài-liệu-tham-khảo)

# Thông tin học phần

- **Giảng viên:** TS. Nguyễn Đình Tứ, Trưởng Bộ môn Cơ điện tử, Khoa Kỹ thuật Cơ khí, Đại học Kỹ thuật – Công nghệ Cần Thơ.
- **Email:** `ndtu@ctuet.edu.vn`
- **Điện thoại:** `0776181954`
- **Tên tiếng Việt:** Phát triển ứng dụng IoT
- **Tên tiếng Anh:** IoT Application Development
- **Mã học phần:** TT188
- **Số tín chỉ:** 03 tín chỉ, gồm 30 tiết lý thuyết và 30 tiết thực hành.
- **Mục tiêu:** Giới thiệu kiến thức cơ bản về Internet vạn vật, các yêu cầu, tiêu chuẩn và ứng dụng IoT; từ đó giúp sinh viên thiết kế, đánh giá các hệ thống theo dõi và điều khiển qua Internet.
- **Kỹ năng:** Thiết kế các hệ thống theo dõi và điều khiển qua Internet trên hệ thống thực.

# Chương 1: Giới thiệu

## Nội dung chương

- **1.1.** Tổng quan về công nghệ Internet vạn vật.
- **1.2.** Xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam.
- Bài tập Chương 1.

## 1.1. Tổng quan về công nghệ Internet vạn vật

### 1.1.1. Khái niệm và bối cảnh

Thế giới hiện có khoảng 20 tỷ thiết bị kết nối Internet và đang tăng trung bình 80 thiết bị mới mỗi giây. Tốc độ tăng này sẽ đạt 50 tỷ thiết bị vào năm 2020.

Đây là một trong những thống kê của Cisco về viễn cảnh “Internet vạn vật” (Internet of Things – IoTs).

Công nghệ mạng IoT đang được phát triển để mọi thiết bị, đồ vật… đều có thể kết nối và tương 
tác với nhau. Điều này cho phép chúng ta tra cứu thông tin về thực phẩm ngay trên tủ lạnh, điều 
khiển ô tô từ xa mà không cần trực tiếp lái xe, hoặc tích hợp cảm biến vào 4–5 triệu xe máy ở Hà 
Nội hoặc TP.HCM để nhà quản lý dễ dàng kiểm soát lưu lượng giao thông.

**Evolution of Internet of Things** ( Quá trình phát triển của Internet of Things (IoT)) qua 5 giai đoạn: 
- Pre-Internet: Con người giao tiếp với con người (Điện thoại, SMS) 
- Internet of Content: Con người truy cập nội dung trên Internet (WWW, Email, thông tin, 
giải trí) 
- Internet of Services: Internet cung cấp dịch vụ (E-commerce, E-productivity,...) 
- Internet of People: Con người kết nối với nhau (Facebook, YouTube, Twitter, Skype,...) 
- Internet of Things: Máy móc/thiết bị giao tiếp với máy móc (Thiết bị có thể nhận diện, 
theo dõi, giám sát, đo lường và chia sẻ dữ liệu) 

    ***Tóm lại:** Internet phát triển từ người => nội dung => dịch vụ => con người => thiết bị, và IoT là giai đoạn mà các thiết bị thông minh kết nối, trao đổi dữ liệu với nhau.*

**Hình minh họa trang 9:** Biểu đồ số lượng thiết bị IoT theo thời gian, minh họa xu hướng tăng nhanh đến năm 2020.

### 1.1.2 Định nghĩa IoT

Before defining IoT, it may be worthwhile listing the most generic enablement 
components. In its simple form, IoT may be considered as a network of 
physical elements empowered by: *(Trước khi định nghĩa IoT, có thể liệt kê các thành phần nền tảng quan trọng nhất. Ở dạng đơn 
giản, IoT có thể được xem là một mạng gồm các phần tử vật lý được hỗ trợ bởi:)*

- **Sensors**: to collect information. (*Cảm biến: thu thập thông tin.*)
- **Identifiers**: to identify the source of data (e.g., sensors, devices). (*Bộ nhận dạng: xác định nguồn dữ liệu (ví dụ: cảm biến, thiết bị). *)
- **Software**: to analyze data. (*Phần mềm: phân tích dữ liệu.*)
- **Internet connectivity**: to communicate and notify. (*Kết nối Internet: giao tiếp và gửi thông báo.*)
```
IoT is the network of things, with clear element identification, embedded with software intelligence, sensors, and ubiquitous connectivity to the Internet. (*IoT là mạng lưới các đối tượng/đồ vật có nhận dạng rõ ràng, được tích hợp trí thông minh phần mềm (software intelligence), cảm biến (sensors) và khả năng kết nối (ubiquitous connectivity) Internet ở mọi nơi.*)
```
### 1.1.3. Background and More Complete IoT Definition
*(Nguồn gốc và định nghĩa IoT hoàn chỉnh hơn)*

Before we give historical overview of the Internet
and consequently delve into the Internet of Things,
it is worthwhile providing a definition and the
fundamental requirements of IoT as a basis for the
inexperienced reader. (*Trước khi đưa ra tổng quan về lịch sử Internet và sau đó đi sâu vào Internet of Things, chúng ta cần cung cấp một định nghĩa và các yêu cầu cơ bản của IoT làm nền tảng cho người đọc mới bắt đầu.*)

We assume that the Internet is well known and bears
no further definition. The question is what do we
really mean by “Things”? Well, things are actually
“anything” and “everything” from appliances to
buildings to cars to people to animals to trees to
plants, etc.
(*Chúng ta giả định Internet đã quá quen thuộc và không cần định nghĩa thêm. Câu hỏi đặt ra là chúng ta thực sự hiểu “Things” (vật/đồ vật) nghĩa là gì? À, “things” thực chất là “bất cứ thứ gì” và “mọi thứ” từ thiết bị gia dụng, tòa nhà, ô tô, con người, động vật, cây cỏ, v.v.*)

A more complete definition, we believe, should also include
“Standards” and “Processes” allowing “Things” to be connected
over the “Internet” to exchange “Data” using industry “Standards”
that guarantee interoperability and enabling useful and mostly
automated “Processes”. (*Theo chúng tôi, một định nghĩa hoàn chỉnh hơn nên bao gồm cả “Tiêu chuẩn” và “Quy trình” cho phép “Vật” được kết nối qua “Internet” để trao đổi “Dữ liệu” sử dụng “Tiêu chuẩn” ngành đảm bảo khả năng tương tác và cho phép “Quy trình” hữu ích và chủ yếu tự động.*)
- **Data**: Converting data into intelligence to make better
decisions. (*Chuyển đổi dữ liệu thành thông tin chi tiết để đưa ra quyết định tốt hơn.*)
- **Process**: Delivering the right information to the right person or
machine at the right time. (*Cung cấp thông tin chính xác cho đúng người hoặc máy móc vào đúng thời điểm.*)
- **Things**: Physical devices and objects connected to the Internet
and each other for intelligent decision-making, often called
IoT. (*Thiết bị và vật thể vật lý được kết nối với Internet và với nhau để ra quyết định thông minh, thường được gọi là IoT.*)
### 1.1.4. How to Monitor and Control Things from Anywhere in the World?
(*Chúng ta có thể theo dõi và điều khiển các thiết bị từ bất cứ nơi đâu trên thế giới như thế nào?*)
- The basic requirements for IoT are the unique identity per “thing” (e.g., IP address), the ability to communicate between things (e.g., wireless communications), and the ability to sense specific information about the thing (sensors).
 (*Các yêu cầu cơ bản cho IoT là định danh duy nhất cho mỗi “vật” (ví dụ: địa chỉ IP), khả năng giao tiếp giữa các vật (ví dụ: truyền thông không dây) và khả năng cảm nhận thông tin cụ thể về vật (cảm biến).*)
- With these three requirements, one should be able to monitor things from anywhere in the world. Another foundation requirement is a medium to communicate. Such requirement is typically handled by a telecommunications network. (*Với ba yêu cầu này, một người nên có thể theo dõi các thiết bị từ bất cứ nơi đâu trên thế giới. Một yêu cầu nền tảng khác là phương tiện để giao tiếp. Yêu cầu này thường được xử lý bởi mạng viễn thông.*)
- Yêu cầu cơ bản của một giải pháp IoT:
    1. Unique Address (Địa chỉ duy nhất)
    2. Sensing & actuating (Cảm biến và tác động)
    3. Ability to communicate (Khả năng giao tiếp)
    4. Notification & Control (Thông báo và điều khiển)
    