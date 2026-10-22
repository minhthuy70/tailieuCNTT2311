# Mục lục môn học

1. [Chương 1: Giới thiệu](#chương-1-giới-thiệu)
2. [Chương 2: Các lĩnh vực ứng dụng IoT](#chương-2-các-lĩnh-vực-ứng-dụng-iot)
3. [Chương 3: Các kiến trúc mạng và bộ giao thức mạng IoT](#chương-3-các-kiến-trúc-mạng-và-bộ-giao-thức-mạng-iot)
4. [Chương 4: Các nền tảng phần cứng và phần mềm IoT thông dụng](#chương-4-các-nền-tảng-phần-cứng-và-phần-mềm-iot-thông-dụng)
5. [Chương 5: Điện toán đám mây, điện toán cận biên và IoT](#chương-5-điện-toán-đám-mây-điện-toán-cận-biên-và-iot)
6. [Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT](#chương-6-quản-lý-ngữ-cảnh-thông-minh-và-trí-tuệ-nhân-tạo-trong-iot)
7. [Chương 7: Tái cấu hình trong IoT](#chương-7-tái-cấu-hình-trong-iot)
8. [Kết luận](#kết-luận)
9. [Tài liệu tham khảo](#tài-liệu-tham-khảo)
10. [Thông tin xuất bản](#thông-tin-xuất-bản)

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

# Các ký hiệu viết tắt

| Ký hiệu | Giải thích |
| --- | --- |
| 6LoWPAN | IPV6 over Low - Power Wireless Personal Area Networks |
| AI | Artificial Intelligence |
| CPS | Chip Package System |
| CPU | Central Processing Unit |
| GPU | Graphics Processing Unit |
| HTTP | HyperText Transfer Protocol |
| ICT | Information & Communication Technologies |
| IoTs | Internet of Things |
| MQTT | Message Queuing Telemetry Transport |
| NFV | Network Function Virtualization |
| OIC | Open InterConnect Consortium |
| OTAP | Over The Air Programming |
| REST | Representational state transfer |
| SDN | Software Defined Network |
| TPU | Tensor Processing Unit |
| VM | Virtual Machine |

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
### 1.1.5. Why Do We Want to Monitor and Control Things?
There are many reasons to monitor and control things remotely over the Internet:
(*Có nhiều lý do để theo dõi và điều khiển các thiết bị từ xa qua Internet:*)
- Monitoring and controlling things by experts (e.g., a patient’s temperature or blood pressure
while the patient is at the comfort of his or her own home).
 (*Theo dõi và điều khiển các thiết bị bởi các chuyên gia (ví dụ: nhiệt độ hoặc huyết áp của bệnh nhân trong khi bệnh nhân đang ở nhà một cách thoải mái).*)
- Learning about things by pointing a smartphone to a thing of interest, for instance; searching
for things that search engines (e.g., Google) do not provide today (e.g., where are my car keys).
 (*Tìm hiểu về mọi thứ bằng cách hướng điện thoại thông minh vào một thứ gì đó thú vị, ví dụ; tìm kiếm những thứ mà công cụ tìm kiếm (ví dụ: Google) không cung cấp ngày nay (ví dụ: chìa khóa xe của tôi ở đâu).*)
- Allowing authorities to manage things in smart cities in an optimal manner (e.g., energy, driver
licenses, and other documents from Department Motor Vehicle, senior citizen).
 (*Cho phép các cơ quan quản lý các thiết bị trong các thành phố thông minh một cách tối ưu (ví dụ: năng lượng, bằng lái xe và các tài liệu khác từ Bộ Giao thông Vận tải, người cao tuổi).*) 
- Providing more affordable entertainment and games for children and adults. All of these are
examples of huge business and service opportunities to boost the economic impact for
consumers, businesses, governments, hospitals, and many other entities.
 (*Cung cấp giải trí và trò chơi giá cả phải chăng hơn cho trẻ em và người lớn. Tất cả những điều này là ví dụ về các cơ hội kinh doanh và dịch vụ lớn để thúc đẩy tác động kinh tế cho người tiêu dùng, doanh nghiệp, chính phủ, bệnh viện và nhiều tổ chức khác.*)
### 1.1.6. Who will monitor and control?
(*Ai sẽ giám sát và điều khiển?*)
Generally speaking, monitoring and control of IoT services may be done by any person or any machine.
 (*Nhìn chung, việc giám sát và điều khiển các dịch vụ IoT có thể được thực hiện bởi bất kỳ người nào hoặc bất kỳ máy nào.*)
- Homeowner monitoring his own home on a mobile device based on a security system she or he has installed and configured. The homeowner may also control lights, turn on the air conditioning, shut off the heater, etc.
 (*Chủ nhà giám sát ngôi nhà của mình trên thiết bị di động dựa trên hệ thống an ninh mà cô ấy hoặc anh ấy đã cài đặt và cấu hình. Chủ nhà cũng có thể điều khiển đèn, bật điều hòa, tắt lò sưởi, v.v.*)
- Another example is for a service provider to monitor and control services for its customers in a network operations center (NOC) .
 (*Một ví dụ khác là nhà cung cấp dịch vụ giám sát và điều khiển dịch vụ cho khách hàng của mình tại một trung tâm vận hành mạng (NOC).*)

Obviously, security is a major concern to prevent access by non-authorized people and, more importantly, prevent a malicious hacker from gaining access to the system and sending old views to the homeowner while a thief is breaking in. The areas of control are far more critical for enterprise-sensitive applications such as healthcare monitoring of patients and banking applications.
(*Rõ ràng, bảo mật là một mối quan tâm lớn để ngăn chặn truy cập trái phép và quan trọng hơn là ngăn chặn hacker độc hại truy cập hệ thống và gửi cảnh báo cũ cho chủ nhà khi có trộm đột nhập. Các lĩnh vực kiểm soát quan trọng hơn đối với các ứng dụng nhạy cảm của doanh nghiệp như theo dõi sức khỏe bệnh nhân và các ứng dụng ngân hàng.*)

### 1.1.7. How Is Security Guaranteed?
(*Làm thế nào để đảm bảo an ninh?*)
Securing IoT is perhaps the biggest opportunity for technology companies and will remain so far some time in the future. Before IoT, information technology security professionals worked in a bubble as they literally owned and controlled their entire networks and secured all devices behind firewalls.
(*Trước IoT, các chuyên gia bảo mật công nghệ thông tin làm việc trong một bong bóng vì họ thực sự sở hữu và kiểm soát toàn bộ mạng lưới của mình và bảo mật tất cả các thiết bị đằng sau tường lửa.*)
With IoT, data will be collected from external, often mobile, sensors that are placed in public sites (e.g., city streets) allowing strangers to send harmful data to any network.
(*Với IoT, dữ liệu sẽ được thu thập từ các cảm biến bên ngoài, thường là di động, được đặt ở các địa điểm công cộng (ví dụ: đường phố thành phố) cho phép người lạ gửi dữ liệu độc hại đến bất kỳ mạng nào.*)
Bring your own device (BYOD) is another example where third-party devices and hence
noncorporate data sources are allowed to enter the network.
(*Bring your own device (BYOD) là một ví dụ khác trong đó các thiết bị của bên thứ ba và do đó các nguồn dữ liệu phi doanh nghiệp được phép truy cập vào mạng.*)
IoT areas that are considered to be most vulnerable include:
- Accessing data during transport (network and transport security). Data will be transported in IoT networks at all time, for example, from sensors tongateways and from gateways to data centers in enterprises or from sensors to gateways for residential services such as video from home monitoring system to the homeowner’s smartphone while he is in a coffee shop. This data may be sniffed by the man in the middle unless the transport protocols are fully secured and encrypted.
(*Truy cập dữ liệu trong quá trình truyền (bảo mật mạng và truyền tải). Dữ liệu sẽ được truyền trong mạng IoT mọi lúc, ví dụ, từ cảm biến đến cổng và từ cổng đến trung tâm dữ liệu trong doanh nghiệp hoặc từ cảm biến đến cổng cho các dịch vụ dân cư như video từ hệ thống giám sát nhà đến điện thoại thông minh của chủ nhà trong khi anh ấy đang ở quán cà phê. Dữ liệu này có thể bị nghe lén bởi người ở giữa trừ khi các giao thức truyền tải được bảo mật và mã hóa đầy đủ.*)
- Having control of IoT devices (control of the APIs) allows unauthorized persons to take full control of entire networks. Examples include shutting down cameras at home and shutting down patient monitoring systems
(*Việc kiểm soát các thiết bị IoT (kiểm soát API) cho phép những người không được ủy quyền kiểm soát hoàn toàn toàn bộ mạng. Ví dụ bao gồm tắt camera tại nhà và tắt hệ thống theo dõi bệnh nhân*)
- Having access to the IoT data itself. Is the data easily accessible? Is it stored encrypted?
Shared storage in the cloud is another problem where customer may log in as customer
B and look at his data. Another common problem is spoofing data via Bluetooth. Many companies are adding Bluetooth support to their devices making it more feasible for
unauthorized persons to access the device’s data.
(*Truy cập vào chính dữ liệu IoT. Dữ liệu có dễ dàng truy cập không? Nó có được lưu trữ dưới dạng mã hóa không?
Lưu trữ chia sẻ trên đám mây là một vấn đề khác, trong đó khách hàng có thể đăng nhập với tư cách khách hàng B và xem dữ liệu của mình. Một vấn đề phổ biến khác là mạo danh dữ liệu qua Bluetooth. Nhiều công ty đang bổ sung hỗ trợ Bluetooth cho thiết bị của họ, giúp những người không được ủy quyền truy cập dữ liệu của thiết bị dễ dàng hơn.*)
- Stealing official user or network identity (stealing user or network credentials). Many websites provide default passwords for vendors
(*Đánh cắp danh tính người dùng hoặc mạng chính thức (đánh cắp thông tin đăng nhập người dùng hoặc mạng). Nhiều trang web cung cấp mật khẩu mặc định cho nhà cung cấp*)
### 1.1.8. Level IoT
(*Cấp độ IoT*)
1. IoT Device Level includes all IoT sensors and actuators (i.e., the Things in IoT).
(*Cấp độ thiết bị IoT bao gồm tất cả các cảm biến và bộ truyền động IoT (tức là các Things trong IoT).*)
2. IoT Network Level includes all IoT network components including IoT gateways, routers, switches, etc.
(*Cấp độ mạng IoT bao gồm tất cả các thành phần mạng IoT bao gồm cổng IoT, bộ định tuyến, bộ chuyển mạch, v.v.*)
3. IoT Application Services Platform Level The functions of the IoT Services Platform include the ability to deploy, configure, troubleshoot, secure, manage, and monitor IoT devices.
(*Cấp độ nền tảng dịch vụ ứng dụng IoT Các chức năng của Nền tảng dịch vụ IoT bao gồm khả năng triển khai, cấu hình, khắc phục sự cố, bảo mật, quản lý và giám sát các thiết bị IoT.*)
4. IoT Application Level includes all applications operating in the IoT network.
(*Cấp độ ứng dụng IoT bao gồm tất cả các ứng dụng hoạt động trong mạng IoT.*)

Advantages of the proposed IoT four-level model include:
- Reduced Complexity: It breaks IoT elements and communication processes into smaller
and simpler components, thereby helping IoT component development, design, and
troubleshooting.
(*Giảm độ phức tạp: Nó chia các yếu tố IoT và quy trình truyền thông thành các
thành phần nhỏ hơn và đơn giản hơn, do đó giúp phát triển, thiết kế và
khắc phục sự cố thành phần IoT. *)
- Standardized Components and Interfaces: The model standardizes the specific components within each level (e.g., what are the key components for general IoT
Services Platform) as well as the interfaces between the various levels. This would allow different vendors to develop joint solutions and common support models.
(*Các thành phần và giao diện tiêu chuẩn: Mô hình tiêu chuẩn hóa các thành phần cụ thể
trong mỗi cấp độ (ví dụ: các thành phần chính cho Nền tảng dịch vụ IoT chung)
cũng như các giao diện giữa các cấp độ khác nhau. Điều này sẽ cho phép
các nhà cung cấp khác nhau phát triển các giải pháp chung và mô hình hỗ trợ chung. *)
- Module Engineering: It allows various types of IoT hardware and software systems to communicate with each other.
(*Kỹ thuật module: Nó cho phép các loại hệ thống phần cứng và phần mềm IoT khác nhau giao tiếp với nhau. *)
- Interoperability between vendors by ensuring the various technology building blocks can interwork and interoperate.
(*Khả năng tương tác giữa các nhà cung cấp bằng cách đảm bảo các khối công nghệ xây dựng khác nhau có thể làm việc và tương tác với nhau. *)
- Accelerate Innovation: It allows developers to focus on solving the main problem at hand without worrying about basic functions that can be implemented once across different business verticals.
(*Thúc đẩy đổi mới: Nó cho phép các nhà phát triển tập trung vào việc giải quyết vấn đề chính trước mắt mà không phải lo lắng về các chức năng cơ bản có thể được triển khai một lần trên các lĩnh vực kinh doanh khác nhau. *)
- Simplified Education: It breaks down the overall complex IoT solution into smaller more manageable components to make learning easier.
(*Giáo dục đơn giản: Nó chia giải pháp IoT phức tạp tổng thể thành các thành phần nhỏ hơn và dễ quản lý hơn để giúp việc học dễ dàng hơn. *)
### 1.1.9. IoT Driving Factors
- IoT has already become a powerful force for business transformation, and its disruptive impact is already felt across all industries and all areas of society.
(*IoT đã trở thành một lực lượng mạnh mẽ cho sự chuyển đổi kinh doanh, và tác động đột phá của nó đã được cảm nhận trên tất cả các ngành và tất cả các lĩnh vực của xã hội.*)
- There is a perfect storm of market disruptions happening at an unprecedented pace triggered by technology as well as new business and social requirements.
(*Có một cơn bão hoàn hảo về sự gián đoạn thị trường đang diễn ra với tốc độ chưa từng có được kích hoạt bởi công nghệ cũng như các yêu cầu kinh doanh và xã hội mới.*)
- IoT Driving Factors:
    - OT & IT Convergence: The integration of Information Technology (IT) and Operational Technology (OT) is blurring the lines between the physical and digital worlds.
    (*Sự hội tụ OT & IT: Sự tích hợp của Công nghệ Thông tin (IT) và Công nghệ Vận hành (OT) đang làm mờ ranh giới giữa thế giới vật lý và kỹ thuật số. *)
    - Internet-based businesses: A trend that has been seen for a few years is the shift from traditional brick-and-mortar businesses to internet-based businesses. The Internet has reshaped every aspect of human's life, business, and even government.
    (*Các doanh nghiệp dựa trên nền tảng Internet: Một xu hướng đã được thấy trong vài năm gần đây là sự chuyển đổi từ các doanh nghiệp truyền thống sang doanh nghiệp dựa trên nền tảng Internet. Internet đã định hình lại mọi khía cạnh của cuộc sống, kinh doanh và thậm chí cả chính phủ của con người.*)
    - Mobile Explosion: The exponential increase in the number of smartphones has driven the need for more mobile computing power, connectivity, and data analytics
    (*Sự bùng nổ di động: Số lượng điện thoại thông minh tăng theo cấp số nhân đã thúc đẩy nhu cầu về sức mạnh tính toán di động, kết nối và phân tích dữ liệu nhiều hơn*)
    - Social Media Explosion: The number of people using social media has exploded in the past few years. Social media has become a powerful force for business transformation, and its disruptive impact is already felt across all industries and all areas of society.
    (*Sự bùng nổ mạng xã hội: Số lượng người sử dụng mạng xã hội đã tăng lên đáng kể trong vài năm gần đây. Mạng xã hội đã trở thành một lực lượng mạnh mẽ cho sự chuyển đổi kinh doanh, và tác động đột phá của nó đã được cảm nhận trên tất cả các ngành và tất cả các lĩnh vực của xã hội.*)
    - Analytics at the Edge: The need for real-time data processing and analytics has driven the development of edge computing, which allows data to be processed closer to the source.
    (*Phân tích tại biên: Nhu cầu về xử lý và phân tích dữ liệu thời gian thực đã thúc đẩy sự phát triển của điện toán biên, cho phép xử lý dữ liệu gần nguồn hơn.*)
    - Technology Explosion: The convergence of technologies such as big data, artificial intelligence, cloud computing, and the Internet of Things (IoT) is creating new opportunities for innovation and transformation.
    (*Sự bùng nổ công nghệ: Sự hội tụ của các công nghệ như dữ liệu lớn, trí tuệ nhân tạo, điện toán đám mây và Internet vạn vật (IoT) đang tạo ra những cơ hội mới cho sự đổi mới và chuyển đổi.*)
    - Virtualization & Cloud: The rise of virtualization and cloud computing has enabled the development of scalable and flexible IoT solutions.
    (*Ảo hóa và Điện toán đám mây: Sự gia tăng của ảo hóa và điện toán đám mây đã cho phép phát triển các giải pháp IoT có khả năng mở rộng và linh hoạt.*)
    - Digital Transformation: The need for digital transformation has driven the development of IoT solutions, which can help businesses to transform their operations and processes.
    (*Chuyển đổi số: Nhu cầu chuyển đổi số đã thúc đẩy sự phát triển của các giải pháp IoT, có thể giúp doanh nghiệp chuyển đổi hoạt động và quy trình của họ.*)
    - Enhanced UI/UX: IoT solutions can provide enhanced UI/UX by providing seamless and intuitive user experiences.
    (*Nâng cao trải nghiệm người dùng (UI/UX): Các giải pháp IoT có thể cung cấp trải nghiệm người dùng (UI/UX) được nâng cao bằng cách cung cấp trải nghiệm người dùng liền mạch và trực quan.*)
    - Fast Adaption: The rapid evolution of technology and the increasing demand for innovative solutions have driven the need for fast adaptation to new technologies. IoT solutions can provide fast adaptation to new technologies by providing seamless integration with existing systems.
    (*Thích ứng nhanh: Sự phát triển nhanh chóng của công nghệ và nhu cầu ngày càng tăng đối với các giải pháp sáng tạo đã thúc đẩy nhu cầu thích ứng nhanh với các công nghệ mới. Các giải pháp IoT có thể cung cấp khả năng thích ứng nhanh với các công nghệ mới bằng cách cung cấp khả năng tích hợp liền mạch với các hệ thống hiện có.*)
    - Rise of security: The rise of security has been a major concern for businesses and governments. IoT solutions can help to address this concern by providing enhanced security features.
    (*Sự gia tăng của an ninh: Sự gia tăng của an ninh đã trở thành một mối quan tâm lớn đối với các doanh nghiệp và chính phủ. Các giải pháp IoT có thể giúp giải quyết mối lo ngại này bằng cách cung cấp các tính năng bảo mật nâng cao.*)
    - Moore's Law: The doubling of processor speeds approximately every two years has driven the development of IoT solutions, which can provide enhanced processing power and analytics capabilities.
    (*Định luật Moore: Sự tăng gấp đôi tốc độ xử lý khoảng hai năm một lần đã thúc đẩy sự phát triển của các giải pháp IoT, có thể cung cấp khả năng xử lý và phân tích nâng cao.*)
### 1.1.10.Convergence of IT and OT
- Operation technology (OT) is the world of industrial plants and industrial control and automation equipment that include machines and systems to run the business, controllers, sensors, and actuators.
(*Công nghệ vận hành (OT) là thế giới của các nhà máy công nghiệp và thiết bị điều khiển và tự động hóa công nghiệp bao gồm máy móc và hệ thống để vận hành doanh nghiệp, bộ điều khiển, cảm biến và bộ truyền động.*)
- Information technology (IT) is the world of end- to-end information systems focusing on compute, data storage, and networking to support business operation in some context such as business process automation systems, customer relation management (CRM) systems, supply chain management systems, logistics systems, and human resources systems.
(*Công nghệ thông tin (IT) là thế giới của các hệ thống thông tin đầu cuối tập trung vào tính toán, lưu trữ dữ liệu và mạng để hỗ trợ hoạt động kinh doanh trong một số bối cảnh như hệ thống tự động hóa quy trình kinh doanh, hệ thống quản lý quan hệ khách hàng (CRM), hệ thống quản lý chuỗi cung ứng, hệ thống hậu cần và hệ thống nguồn nhân lực.*)
- Historically, IT and OT were always managed by two separate organizations with different cultures, philosophies, and set of technologies.
(*Theo truyền thống, IT và OT luôn được quản lý bởi hai tổ chức riêng biệt với các nền văn hóa, triết lý và bộ công nghệ khác nhau.*)
- IT departments were originally created by companies to create efficient and effective forms of telephony communication among various departments. Then they were extended to provide video and web conferences and network internal communications and secure external electronic communications such as emails. Often the final decision with the selection of communication systems, website hosting, and backup servers was the responsibility of the IT department.
(*Các bộ phận IT ban đầu được các công ty tạo ra để tạo ra các hình thức giao tiếp điện thoại hiệu quả và hiệu quả giữa các phòng ban khác nhau. Sau đó, chúng được mở rộng để cung cấp hội nghị truyền hình và hội nghị web cũng như mạng truyền thông nội bộ và truyền thông điện tử bên ngoài an toàn như email. Thông thường, quyết định cuối cùng với việc lựa chọn hệ thống giao tiếp, lưu trữ trang web và máy chủ sao lưu là trách nhiệm của bộ phận IT.*)
- OT relies on real-time data that drives safety, security, and control. It depends on very well-defined, tested, and trusted processes. Many plants need to run 24 × 7 with zero downtime (e.g., City Water Filtration System), and thus industrial processes cannot tolerate shutdown for software updates. IT is more lenient with software updates, introduction of new technologies, etc.
(*OT dựa vào dữ liệu thời gian thực thúc đẩy an toàn, bảo mật và kiểm soát. Nó phụ thuộc vào các quy trình được xác định rõ ràng, đã được thử nghiệm và tin cậy. Nhiều nhà máy cần chạy 24 × 7 với số lần ngừng hoạt động bằng không (ví dụ: Hệ thống lọc nước thành phố), do đó, các quy trình công nghiệp không thể chấp nhận việc ngừng hoạt động để cập nhật phần mềm. IT linh hoạt hơn với các cập nhật phần mềm, giới thiệu các công nghệ mới, v.v.*)
### 1.1.11. The Astonishing Introduction of Creative Internet-Based Businesses
(*Sự ra đời đáng kinh ngạc của các doanh nghiệp sáng tạo dựa trên Internet*)
Uber
- The key component of Uber’s solution is the Internet-based platform connecting customers (passengers) with the service providers (car drivers). Because the consumers are not Uber’s employees and because there is practically an infinite number of cars that could potentially join Uber, Uber has the requirement to scale at an incredibly fast rate at zero marginal cost.
(*Thành phần chính của giải pháp Uber là nền tảng dựa trên Internet kết nối khách hàng (hành khách) với nhà cung cấp dịch vụ (tài xế ô tô). Bởi vì người tiêu dùng không phải là nhân viên của Uber và vì có vô số ô tô có thể tham gia Uber, Uber có yêu cầu mở rộng với tốc độ cực nhanh với chi phí cận biên bằng không.*)
- Uber uses sensor technologies in driver’s smartphones to track their behaviors. If you ride with Uber and your driver speeds, breaks too hard, or takes you on a wildly lengthy route to your destination, it is no longer your word against theirs. Uber is using Gyrometer and GPS data to track the behavior of their drivers. Gyrometers in smartphones measure small movements, while GPS combined with accelerometers shows how often a vehicle starts and stops and the overall speed.
(*Uber sử dụng công nghệ cảm biến trong điện thoại thông minh của tài xế để theo dõi hành vi của họ. Nếu bạn đi Uber và tài xế của bạn lái xe quá tốc độ, phanh gấp hoặc đi một lộ trình cực kỳ dài đến đích, đó không còn là lời nói của bạn chống lại họ. Uber đang sử dụng dữ liệu Gyrometer và GPS để theo dõi hành vi của tài xế. Gyrometer trong điện thoại thông minh đo các chuyển động nhỏ, trong khi GPS kết hợp với gia tốc kế cho thấy tần suất xe khởi động và dừng cũng như tốc độ tổng thể.*)
- Uber Eat: Today Uber is one of the leading transportation services in the world with a market
value over 20 billion dollars.
(*Uber Eat: Ngày nay Uber là một trong những dịch vụ vận tải hàng đầu thế giới với giá trị thị trường trên 20 tỷ đô la.*)

Airbnb is an Internet-based service for people to list, find, and rent lodging. It was founded in 2008 in San Francisco, California, by Brian Check and Joe Gebbia shortly after creating AirBed and Breakfast during a conference. The original site offered rooms,breakfast, and business networking opportunity for the conference attendees who were unable to find a hotel. Shortly thereafter, the newly created company focused on high-profile events where alternative lodging was very limited.
(*Airbnb là một dịch vụ dựa trên Internet để mọi người liệt kê, tìm kiếm và cho thuê chỗ ở. Nó được thành lập vào năm 2008 tại San Francisco, California, bởi Brian Check và Joe Gebbia ngay sau khi tạo ra AirBed and Breakfast trong một hội nghị. Trang web ban đầu cung cấp chỗ ở, bữa sáng và cơ hội kết nối kinh doanh cho những người tham dự hội nghị không tìm được khách sạn. Ngay sau đó, công ty mới thành lập tập trung vào các sự kiện nổi tiếng nơi chỗ ở thay thế rất hạn chế.*)

Amazon.com is the largest Internet retailer company in the world started, in 1994, as an Internet-based book seller and swiftly expanded into music, movies, electronics, and
household goods; Amazon utilized the Internet to break the traditional retailer model. It did not need to stock many of the merchandises it was selling on its website. Instead, it identified matching partner companies and issued customer orders over a secure Internet-based platform.
(*Amazon.com là công ty bán lẻ Internet lớn nhất thế giới bắt đầu vào năm 1994 với tư cách là người bán sách dựa trên Internet và nhanh chóng mở rộng sang âm nhạc, phim ảnh, đồ điện tử và hàng gia dụng; Amazon đã sử dụng Internet để phá vỡ mô hình bán lẻ truyền thống. Nó không cần phải lưu trữ nhiều hàng hóa mà nó đang bán trên trang web của mình. Thay vào đó, nó xác định các công ty đối tác phù hợp và phát hành đơn đặt hàng của khách hàng thông qua một nền tảng an toàn dựa trên Internet.*)

Tesla
- Tesla Motors was founded in 2003 by a group of engineers in Silicon Valley with a mission to develop a successful luxurious electrical car and then invest the resulting profits to make a less expensive electric car. With instant torque, incredible power, and zero emissions, Tesla’s products would be cars without compromise.
(*Tesla Motors được thành lập vào năm 2003 bởi một nhóm kỹ sư tại Thung lũng Silicon với sứ mệnh phát triển một chiếc xe điện sang trọng thành công và sau đó đầu tư lợi nhuận thu được để chế tạo một chiếc xe điện rẻ hơn. Với mô-men xoắn tức thời, công suất ấn tượng và không phát thải, các sản phẩm của Tesla sẽ là những chiếc xe không thỏa hiệp.*)
- Tesla’s engineers first designed a power train for a sports car built around an AC induction motor, patented in 1888 by Nikola Tesla, the inventor who inspired the company’s name. The resulting Tesla Roadster was launched in 2008 with an incredible range of 245 miles per charge of its lithium ion battery. The Roadster was able to set a new standard for electric mobility. In 2012, Tesla launched Model S, the world’s first premium electric sedan.
(*Các kỹ sư của Tesla lần đầu tiên thiết kế một hệ truyền động cho một chiếc xe thể thao được chế tạo xung quanh động cơ cảm ứng AC, được cấp bằng sáng chế vào năm 1888 bởi Nikola Tesla, nhà phát minh đã truyền cảm hứng cho tên của công ty. Chiếc Tesla Roadster ra đời đã được ra mắt vào năm 2008 với phạm vi hoạt động đáng kinh ngạc là 245 dặm sau mỗi lần sạc pin lithium ion. Roadster đã có thể thiết lập một tiêu chuẩn mới cho khả năng di chuyển bằng điện. Vào năm 2012, Tesla đã ra mắt Model S, chiếc sedan điện cao cấp đầu tiên trên thế giới.*)
- Tesla is considered as the best example yet of IoT. It did not only bend the traditional industry manufacturing model to Internet-based model with thousands of sensors.
(*Tesla được coi là ví dụ điển hình nhất của IoT cho đến nay. Nó không chỉ bẻ cong mô hình sản xuất công nghiệp truyền thống sang mô hình dựa trên Internet với hàng ngàn cảm biến.*)

Self-Driving Cars
- Self-driving cars can be divided into two main categories: semiautonomous and fully autonomous. A semiautonomous car performs certain self-driving tasks (e.g., fully brakes when it gets too close to an object, drives itself on the freeway), while a fully autonomous car drives itself from origin to destination without any driver interaction. Fully autonomous cars are further divided into user-operated and driverless.
(*Xe tự lái có thể được chia thành hai loại chính: bán tự lái và hoàn toàn tự lái. Một chiếc xe bán tự lái thực hiện các nhiệm vụ tự lái nhất định (ví dụ: tự động phanh khi quá gần vật thể, tự lái trên đường cao tốc), trong khi một chiếc xe hoàn toàn tự lái tự lái từ điểm gốc đến điểm đích mà không cần sự tương tác của người lái. Xe hoàn toàn tự lái được chia nhỏ hơn thành xe do người dùng vận hành và xe không người lái.*)
- Safety is considered one of the biggest advantages of self-driving cars. In general, self-driving cars are equipped with a large number of sensors including laser range finders (to measure a subject’s distance and take photos that are in sharp focus), radars, and video cameras collecting information from the road. They are also equipped with actuators to control steering and braking. The collected data (from sensors, radars, and video) is promptly processed with the positional information from the car’s GPS unit and the navigation system to determine its position and to build a three-dimensional model of its surroundings.
(*An toàn được coi là một trong những lợi thế lớn nhất của xe tự lái. Nói chung, xe tự lái được trang bị một số lượng lớn các cảm biến bao gồm bộ tìm phạm vi laser (để đo khoảng cách của vật thể và chụp ảnh sắc nét), radar và camera video thu thập thông tin từ đường. Chúng cũng được trang bị các cơ cấu chấp hành để kiểm soát lái và phanh. Dữ liệu thu thập được (từ cảm biến, radar và video) là được xử lý nhanh chóng với thông tin vị trí từ đơn vị GPS của xe và hệ thống định vị để xác định vị trí của nó và xây dựng mô hình ba chiều của nó
bao quanh.*)
- The resulting model is then processed by the car’s control system to make navigation decisions. Self-driving car control systems typically use stored maps to find optimal path to destination, avoid obstacles, and send decisions to the car’s actuators. IoT applies to interactions and communications between self-driving care components, between the car and roadside infrastructure, as well as among self- driving cars.
(*Mô hình kết quả sau đó được xử lý bởi hệ thống điều khiển của xe để đưa ra quyết định điều hướng. Các hệ thống điều khiển xe tự lái thường sử dụng bản đồ lưu trữ để tìm đường đi tối ưu đến đích, tránh chướng ngại vật và gửi quyết định đến các cơ cấu chấp hành của xe. IoT áp dụng cho các tương tác và giao tiếp giữa các thành phần của xe tự lái, giữa xe và cơ sở hạ tầng ven đường, cũng như giữa các xe tự lái.*)
- Mobile Device Explosion: Mobile data traffic has grown 18-fold in the last few years. The increase in mobile data traffic is driven by two factors: the increase in the number of users and the data consumption per user. The average smartphone generated 4 GB of traffic per month in 2019. This growth is fueled by IoT connecting things with people and more importantly allowing people to monitor and control things from anywhere in the world in real time.
(*Bùng nổ thiết bị di động: Lưu lượng dữ liệu di động đã tăng gấp 18 lần trong vài năm qua. Sự gia tăng lưu lượng dữ liệu di động được thúc đẩy bởi hai yếu tố: sự gia tăng số lượng người dùng và mức tiêu thụ dữ liệu trên mỗi người dùng. Trung bình một điện thoại thông minh tạo ra 4 GB lưu lượng truy cập mỗi tháng vào năm 2019. Sự tăng trưởng này được thúc đẩy bởi IoT kết nối mọi thứ với mọi người và quan trọng hơn là cho phép mọi người theo dõi và kiểm soát mọi thứ từ bất kỳ đâu trên thế giới trong thời gian thực.*)

Social Network Explosion: Social networks, such as Facebook, Instagram, Twitter, and YouTube, and the adoption of cloud-based services, such as Amazon’s AWS and Salesforce.com, are all examples of the large-scale migration to the cloud across virtually every industry. In fact, two-thirds of all data center traffic will be from the cloud in 3 years. All of this leads to data explosion, where, already, the data being created on the Internet each day is equal to half of all the data that has been accumulated since the dawn of humanity.
(*Bùng nổ mạng xã hội: Các mạng xã hội, như Facebook, Instagram, Twitter và YouTube, và việc áp dụng các dịch vụ dựa trên đám mây, như AWS của Amazon và Salesforce.com, đều là những ví dụ về việc di chuyển quy mô lớn lên đám mây trên hầu hết mọi ngành. Trên thực tế, hai phần ba lưu lượng truy cập trung tâm dữ liệu sẽ đến từ đám mây trong 3 năm. Tất cả những điều này dẫn đến sự bùng nổ dữ liệu, nơi mà, ngay cả bây giờ, dữ liệu được tạo ra trên Internet mỗi ngày đã bằng một nửa tất cả dữ liệu đã được tích lũy kể từ khi loài người ra đời.*)

Analytics at the Edge: 
- Before introducing the different versions of analytics, it is important to define the terms: big data, structured data, and unstructured data. Big data refers to the extremely large amount of data being generated and accumulated by IT systems as the result of the operation of an associated system. The latter could be a product, process, service, etc. This massive amount of data can be analyzed to identify patterns and gain insights into the operation of the associated system. The analysis often involves applying statistical techniques since human processing is not viable due to the sheer volume of the data.
(*Phân tích tại biên: Trước khi giới thiệu các phiên bản khác nhau của phân tích, điều quan trọng là phải định nghĩa các thuật ngữ: dữ liệu lớn, dữ liệu có cấu trúc và dữ liệu phi cấu trúc. Dữ liệu lớn đề cập đến lượng dữ liệu cực lớn đang được tạo ra và tích lũy bởi các hệ thống CNTT như là kết quả của hoạt động của một hệ thống liên quan. Hệ thống sau này có thể là một sản phẩm, quy trình, dịch vụ, vv. Lượng dữ liệu khổng lồ này có thể được phân tích để xác định các mẫu và hiểu rõ hơn về hoạt động của hệ thống liên quan. Phân tích thường liên quan đến việc áp dụng các kỹ thuật thống kê vì việc xử lý của con người không khả thi do khối lượng dữ liệu khổng lồ.*)
- Structured data refers to organized data that can fit in rows and columns. Examples of such data include customer data, sales data, and stock records. Structured data is often
high value, cleansed, and indexed. Unstructured data, on the other hand, is difficult to
organize or bring together. Examples of unstructured data include images, X-rays, video,
social media data, and some machine outputs mixed with text.
(*Dữ liệu có cấu trúc đề cập đến dữ liệu được tổ chức có thể nằm trong các hàng và cột. Ví dụ về dữ liệu như vậy bao gồm dữ liệu khách hàng, dữ liệu bán hàng và hồ sơ chứng khoán. Dữ liệu có cấu trúc thường có giá trị cao, được làm sạch và lập chỉ mục. Mặt khác, dữ liệu phi cấu trúc khó tổ chức hoặc tổng hợp lại. Ví dụ về dữ liệu phi cấu trúc bao gồm hình ảnh, X-quang, video, dữ liệu truyền thông xã hội và một số kết quả máy móc trộn lẫn với văn bản.*)

Cloud Computing and Virtualization: Cloud computing, which was introduced in 2008, allows enterprises to outsource their computing infrastructure fully or partially to public cloud provides (e.g., Amazon AWS, Microsoft Azure, Google Compute Engine).
(*Điện toán đám mây, được giới thiệu vào năm 2008, cho phép các doanh nghiệp thuê ngoài toàn bộ hoặc một phần cơ sở hạ tầng điện toán của họ cho các nhà cung cấp đám mây công cộng (ví dụ: Amazon AWS, Microsoft Azure, Google Compute Engine).*)

Technology Explosion: IoT hardware (e.g., sensors, inexpensive computers such as Raspberry Pi, open - source microcontrollers such as Arduino) and software technologies are not only being developed faster than ever before but with much lower prices. Such devices are already transforming user behaviors and creating new business opportunities.
(*Bùng nổ Công nghệ: Phần cứng IoT (ví dụ: cảm biến, máy tính giá rẻ như Raspberry Pi, vi điều khiển mã nguồn mở như Arduino) và các công nghệ phần mềm không chỉ được phát triển nhanh hơn bao giờ hết mà còn với giá rẻ hơn nhiều. Những thiết bị như vậy đã và đang thay đổi hành vi người dùng và tạo ra các cơ hội kinh doanh mới.*)

Digital Convergence/Transformation: 
(*Số hóa hội tụ/chuyển đổi số:*)
- Digital convergence has initially started with a limited scope: move to “paperless” operation and save trees.
(*Số hóa hội tụ ban đầu bắt đầu với phạm vi hạn chế: chuyển sang hoạt động “không giấy tờ” và tiết kiệm cây xanh.*)
- Convergence is a concept that describes how previously separate technologies, processes, and data combine to create new products, services, end experiences that reshape industries.
(*Hội tụ là một khái niệm mô tả cách các công nghệ, quy trình và dữ liệu riêng biệt trước đây kết hợp để tạo ra các sản phẩm, dịch vụ, trải nghiệm cuối cùng định hình lại các ngành.*)
- The smartphone is a classic example of convergence. It’s a camera, address book, map, and media player.
(*Điện thoại thông minh là một ví dụ điển hình về sự hội tụ. Nó là một máy ảnh, danh bạ, bản đồ và trình phát đa phương tiện.*)

Enhanced User Interfaces (*Giao diện người dùng được cải tiến*):

Fast Rate of IoT Technology Adoption (Five Times More than Electricity and
Telephony) 
(*Tỷ lệ áp dụng công nghệ IoT nhanh chóng (Năm lần so với Điện và Điện thoại)*)

### 1.1.12. The Rise of Security Requirements
(*Sự gia tăng yêu cầu bảo mật*)

- Protection of business and personal data and systems has been an issue since the inception of data networks. With the commercialization of the Internet, security concerns expanded to cover personal privacy, financial transactions, and the threat of cyber robbery. Today, security of the network is being expanded to include safety or physical security.
(*Bảo vệ dữ liệu và hệ thống kinh doanh và cá nhân đã là một vấn đề kể từ khi bắt đầu mạng dữ liệu. Với việc thương mại hóa Internet, các mối quan tâm về bảo mật mở rộng để bao gồm quyền riêng tư cá nhân, giao dịch tài chính và các mối đe dọa của tội phạm mạng. Ngày nay, bảo mật mạng đang được mở rộng để bao gồm sự an toàn hoặc an ninh vật chất.*)

### 1.1.13. The Nonstop Moore’s Law
(*Luật Moore không ngừng*) 

It is possible to summarize Moore’s Law impact with three key observation:
(*Có thể tóm tắt tác động của Luật Moore với ba quan sát chính:*)
1. Over the history of computing hardware, computer power has been doubling approximately every 18 months.
(*Trong lịch sử phần cứng máy tính, sức mạnh máy tính đã tăng gấp đôi xấp xỉ mỗi 18 tháng.*)
2. Silicon transistor storage technology size has continued to shrink over the years and is approaching atomic level. For years now, we have been putting more power and more storage on the same size device.
(*Công nghệ lưu trữ bóng bán dẫn silicon ngày càng thu nhỏ qua các năm và đang tiến gần đến cấp độ nguyên tử. Trong nhiều năm nay, chúng ta đã đưa nhiều sức mạnh và dung lượng lưu trữ hơn vào cùng một thiết bị.*)
3. The price of the transistor is being reduced by more than 50% every year.
(*Giá của bóng bán dẫn giảm hơn 50% mỗi năm.*)

### 1.1.14. Applications of IoT
(*Ứng dụng IoT*)

Transport (*Vận tải*):
- Reducing travel times by analyzing traffic
(*Giảm thời gian di chuyển bằng cách phân tích giao thông*)
- Ride-sharing apps-determining the price, supply chain prediction
(*Ứng dụng chia sẻ xe - xác định giá, dự đoán chuỗi cung ứng*)
- Autonomous vehicles
(*Xe tự lái*)

Workplace (*Nơi làm việc*):
- Robotics in manufacturing (*Robot trong sản xuất*)
- Automated safety checks in factories (*Kiểm tra an toàn tự động trong nhà máy*)
- Autonomous haulage (*Vận tải tự động*)
- Enriched recruitment (*Tuyển dụng phong phú*)
- Automated timesheets(e.g., Blackbelt) (*Bảng chấm công tự động (ví dụ: Blackbelt)*)

Education (*Giáo dục*):
- Plagiarism checkers (*Kiểm tra đạo văn*)
- Automated grading (*Chấm điểm tự động*)
- Customized digital learning interfaces (*Giao diện học tập kỹ thuật số tùy chỉnh*)
- Virtual teachers or lecturers (*Giáo viên hoặc giảng viên ảo*)

Sport (*Thể thao*):
- Wearable tech to analyze performance (*Công nghệ đeo để phân tích hiệu suất*)
- Smart ticketing (*Bán vé thông minh*)
- Automated video highlights (*Tự động hóa video nổi bật*)
- Computer vision referee (*Trọng tài thị giác máy tính*)

Healthcare (*Chăm sóc sức khỏe*):
- Autonomous surgical robots (*Robot phẫu thuật tự động*)
- Automatic disease identificationand diagnosis (*Nhận dạng và chẩn đoán bệnh tự động*)
- Epidemic outbreak prediction (*Dự đoán bùng phát dịch bệnh*)

Agriculture (*Nông nghiệp*):
- Robot harvesters (*Thu hoạch robot*)
- Computer vision to monitor crop and soil health
(*Thị giác máy tính để theo dõi sức khỏe cây trồng và đất*)
- Predictive analysis for environmental impacts on crops
(*Phân tích dự đoán các tác động môi trường đến cây trồng*)

Entertainment (*Giải trí*):
- Music suggestions (Spotify, Apple Music, Google Play music)
(*Gợi ý âm nhạc (Spotify, Apple Music, Google Play music)*)
- Automatic music creation (*Tạo nhạc tự động*)
- Film and TV suggestions (Netfix, Amazon Prime, Hulu)
(*Gợi ý phim và TV (Netfix, Amazon Prime, Hulu)*)

Smart homes (*Nhà thông minh*):
- Personal assistants (*Trợ lý cá nhân*)
- Automatic goods ordering (*Đặt hàng tự động*)
- Home security (*Bảo mật gia đình*)
- Temperature and light control (*Điều khiển nhiệt độ và ánh sáng*)

Defence (*Quốc phòng*):
- Unmanned Aerial Vehicles (UAVs) (*Phương tiện bay không người lái (UAV)*)
- Civilian detection (*Phát hiện dân sự*)
- Autonomous decision making (*Ra quyết định tự động*)
- Target identification (*Nhận dạng mục tiêu*)
- Diagnosis and maintenance of weapons systems (*Chẩn đoán và bảo trì hệ thống vũ khí*)

### 1.1.15. Internet of Things for a Better Life (*Internet vạn vật cho cuộc sống tốt đẹp hơn*)

**Automatic transportation** (*Vận tải tự động*): The goal is for all transportation to become automated in the future (*Mục tiêu là tất cả giao thông trở nên tự động trong tương lai*)

**Cyborg technology** (*Công nghệ người máy*): AI and robotics will help us overcome our cognitive and physical limitations, including robotic limbs capable of communicating with our brains (*AI và robot sẽ giúp chúng ta vượt qua những hạn chế về nhận thức và thể chất, bao gồm cả chi giả có khả năng giao tiếp với bộ não của chúng ta*)

**Solving climate change** (*Giải quyết biến đổi khí hậu*): Using big data, AI and IoT could one day identify trends and use that information to present solutions to the world’s biggest problems like climate change (*Sử dụng big data, AI và IoT có thể một ngày nào đó xác định xu hướng và sử dụng thông tin đó để trình bày giải pháp cho các vấn đề lớn nhất thế giới như biến đổi khí hậu*)

**Predicting the future** (*Dự đoán tương lai*): Machine learning uses the past to make predictions about the future. It will be able to predict things as intimate as who will start dating or who will get divorced. (*Máy học sử dụng quá khứ để đưa ra dự đoán về tương lai. Nó sẽ có thể dự đoán những điều thân mật như ai sẽ bắt đầu hẹn hò hoặc ai sẽ ly hôn*)

This system is capable of collecting, analyzing and presenting data on a Graphical User Interface (GUI), programmed with LabVIEW. It also allows the user to get the updated sensor information online based on Google Spreadsheets application, via Internet connectivity, or at any time through the SMS gateway service and sends alert message promptly enabling user interventions when needed. (*Hệ thống này có khả năng thu thập, phân tích và trình bày dữ liệu trên Giao diện người dùng đồ họa (GUI), được lập trình với LabVIEW. Nó cũng cho phép người dùng nhận thông tin cảm biến cập nhật trực tuyến dựa trên ứng dụng Google Spreadsheets, thông qua kết nối Internet, hoặc bất cứ lúc nào thông qua dịch vụ cổng SMS và gửi cảnh báo kịp thời cho phép can thiệp người dùng khi cần thiết.*)

### 1.1.16. Examples of IoT deployment
(*Ví dụ về triển khai IoT*)

**ORing, NCU (National Central University), and Chunghwa Telecom Join Hands on 5G Smart Manufacturing** (*ORing, NCU (National Central University) và Chunghwa Telecom hợp tác sản xuất thông minh 5G*)
- The Department of Mechanical Engineering has established a smart factory based on Industry 4.0 under the support of Jing-Yang Jou, President of NCU, to develop laser, discharge, and electrochemical machining technologies. The smart factory has integrated a variety of smart technologies including AI, big data analytics, and edge computing. (*Khoa Cơ khí đã thành lập nhà máy thông minh dựa trên Công nghiệp 4.0 dưới sự hỗ trợ của Chủ tịch NCU, Jing-Yang Jou, để phát triển các công nghệ gia công laser, phóng điện và điện hóa. Nhà máy thông minh đã tích hợp nhiều công nghệ thông minh bao gồm AI, phân tích dữ liệu lớn và điện toán biên.*)

**Smart Transportation System with Floating Car Data** (*Hệ thống giao thông thông minh với dữ liệu xe nổi*)

- The Smart Transportation System (STS) applies big data, cloud computing, and fog computing to traffic control. It collects real-time traffic information from traffic surveillance cameras, floating car data from GPS-equipped vehicles, and payment information from public transport to provide navigation, traffic control, and transport services. (*Hệ thống Giao thông Thông minh (STS) áp dụng big data, điện toán đám mây và điện toán sương mù để kiểm soát giao thông. Nó thu thập thông tin giao thông thời gian thực từ camera giám sát giao thông, dữ liệu xe nổi từ các xe được trang bị GPS và thông tin thanh toán từ giao thông công cộng để cung cấp dịch vụ điều hướng, kiểm soát giao thông và giao thông vận tải.*)

## 1.2. Trends of applying IoT and related technologies to smart cities in Vietnam
(*Xu thế ứng dụng IoTs và các công nghệ liên quan cho đô thị thông minh ở Việt Nam*)
- Công nghệ IoTs/5G và kỹ thuật xử lý dữ liệu lớn (Big Data), trí tuệ nhân tạo (AI) đóng vai trò quan trọng trong việc tạo ra những đổi mới đột phá trong CNTT và truyền thông, và các lĩnh vực ứng dụng liên quan.
- Thành phố thông minh là một trong những ứng dụng như vậy, đã thu hút được sự chú ý lớn từ các chính phủ, cộng đồng ngành học thuật và CNTT tại nhiều quốc gia. Đặc biệt, Big Data/AI và IoT/5G cung cấp các công cụ và công nghệ cho phép quan trọng để thúc đẩy sự chuyển đổi của các thành phố lớn trên toàn thế giới thành những nơi đáng sống, làm việc và tận hưởng.
- Các công nghệ IoTs/5 mới, một khi được tích hợp đúng vào cơ sở hạ tầng thành phố thông minh (Smart Cities), có thể hỗ trợ số lượng lớn kết nối không dây từ các loại thiết bị không dây khác nhau (ví dụ: cảm biến, máy ảnh, thiết bị AR/VR, xe thông minh) thông qua môi trường mạng có tốc độ cao, truyền dữ liệu cực kỳ đáng tin cậy và độ trễ thấp.
- Tại Việt Nam, mặc dù còn nhiều bất cập, song hiện nay, các đô thị ở Việt Nam đang phát triển theo hướng tiếp cận với nhiều mô hình tiên tiến theo xu thế hội nhập quốc tế, tạo ra nhiều tiền đề về ứng dụng và phát triển CNTT, truyền thông để phát triển đô thị thông minh và quản lý thông minh.

Cụ thể, tại Việt Nam, tỷ lệ người sử dụng Internet/tổng dân số năm 2014 đã đạt 43,8% (cao hơn tỷ lệ trung bình thế giới là 42,2% và châu Á là 34,8%). Cả nước có gần 14.000 doanh nghiệp CNTT với hơn 500.000 lao động. Việt Nam cũng đạt được nhiều bước tiến lớn trong ứng dụng CNTT vào hoạt động quản lý nhà nước và đời sống xã hội: quản lý ngân sách, kho bạc, thuế, hải quan, bảo hiểm xã hội, giáo dục, y tế, giao thông, đất đai, quy hoạch và môi trường.

Đồng chí Nguyễn Thiện Nhân - Nguyên Bí thư Thành ủy Thành phố Hồ Chí Minh từng nhấn mạnh: *“Từ bức tranh của các đô thị Việt Nam, có thể thấy Việt Nam cần phát triển các đô thị theo hướng đô thị thông minh”*. Đô thị thông minh nhằm hướng tới 4 mục tiêu trụ cột:
1. **Hiệu quả kinh tế:** Dự kiến đến năm 2025, diện tích đô thị chiếm khoảng 15% diện tích cả nước, tỷ lệ đô thị hóa khoảng 50% dân số, đóng góp khoảng 75% GDP quốc gia.
2. **Môi trường sống tốt hơn:** Nâng cao chất lượng không khí, quản lý nguồn nước, giảm thiểu ùn tắc và ô nhiễm.
3. **Phục vụ người dân tốt hơn:** Cung cấp dịch vụ công trực tuyến nhanh chóng, minh bạch và tiện ích y tế, giáo dục số.
4. **Người dân tham gia quản trị:** Cho phép người dân tham gia phản ánh, giám sát và quản lý đô thị cùng chính quyền.

Để xây dựng và vận hành thành công một thành phố thông minh bền vững, chính quyền và các đối tác công nghệ cần nhất quán lựa chọn các giải pháp đạt chuẩn Internet of Things mở quốc tế. Việc triển khai các giải pháp IoT phân mảnh và phi tiêu chuẩn (*Non-Standardized*) sẽ khiến các hệ sinh thái không thể kết nối, giao tiếp được với nhau, dẫn đến nguy cơ lãng phí ngân sách và nhân lực. Đô thị thông minh hiện đại là sự hội tụ giữa công nghệ điện toán đám mây (*Cloud Computing*), điện toán cận biên (*Edge Computing*), dữ liệu lớn (*Big Data*) và trí tuệ nhân tạo (*AI*) trên nền tảng các chuẩn mở.

### 1.1.17. Các tổ chức tiêu chuẩn hóa và liên minh IoT quốc tế

Nhằm giải quyết bài toán phân mảnh và đảm bảo khả năng tương thích liên thông giữa hàng tỷ thiết bị thông minh từ các nhà sản xuất khác nhau, nhiều liên minh công nghệ và tổ chức tiêu chuẩn quốc tế đã ra đời:

- **Open Interconnect Consortium (OIC)** [12]: Được thành lập bởi các tập đoàn công nghệ hàng đầu (Intel, Samsung, Broadcom, Dell...) nhằm xác định đặc tả kỹ thuật và tiêu chuẩn truyền thông mở, cho phép các thiết bị kết nối không dây giao tiếp liền mạch mà không phụ thuộc vào hệ điều hành hay giao thức mạng vật lý bên dưới.
- **AllSeen Alliance** [13]: Liên minh gồm các tập đoàn công nghệ lớn như Haier, LG Electronics, Panasonic, Qualcomm, Sharp, Technicolor, Silicon Image, TP-LINK và Microsoft, phối hợp phát triển khung hạ tầng phần mềm nguồn mở AllJoyn (khởi xướng bởi Qualcomm).
- **IEEE 802.15.4** [14]: Chuẩn truyền thông vật lý (PHY) và điều khiển truy cập môi trường (MAC) cho mạng cảm biến không dây công suất thấp (LR-WPAN).
- **IETF CoAP (Constrained Application Protocol)** [15]: Giao thức tầng ứng dụng tối ưu theo mô hình REST cho các thiết bị tài nguyên hạn chế hoạt động trên UDP.
- **Zigbee Alliance** [16]: Liên minh xây dựng bộ giao thức mạng lưới (mesh) công suất thấp ứng dụng trong nhà thông minh và tự động hóa tòa nhà.
- **Bluetooth Special Interest Group (SIG) & Bluetooth Smart (BLE)** [17]: Chuẩn giao tiếp tầm ngắn năng lượng thấp cho thiết bị đeo và di động.
- **W3C Semantic Sensor Networks (SSN)** [18]: Chuẩn hóa ngữ nghĩa dữ liệu cảm biến dựa trên mô hình bản thể học Ontology (OWL/RDF).
- **Open Geospatial Consortium (OGC) Sensor Web Enablement (SWE)** [19] và **CityGML** [20]: Chuẩn hóa dịch vụ web cảm biến không gian địa lý và mô hình hóa dữ liệu không gian 3D cho đô thị thông minh.
- **European Sensor Network Architecture (ESNA)** [21]: Khung kiến trúc mạng cảm biến châu Âu.
- **IETF 6LoWPAN** [22]: Tiêu chuẩn đưa giao thức IPv6 trực tiếp xuống các mạng cảm biến không dây năng lượng thấp thông qua kỹ thuật nén tiêu đề và phân mảnh gói tin.

### 1.1.18. Các thách thức kỹ thuật cốt lõi trong phát triển hệ thống IoT

Tốc độ tăng trưởng nhanh chóng của Internet of Things đặt ra nhiều thách thức kỹ thuật phức tạp cần giải quyết đồng thời:

1. **Phần mềm (Software):** Đóng vai trò sống còn trong toàn bộ vòng đời phát triển của thiết bị và hệ thống IoT, bao gồm thiết kế mạch tích hợp (ICs) và phát triển phần mềm nhúng. Việc làm chủ công nghệ và tăng cường tính bảo mật đòi hỏi ưu tiên lựa chọn các thiết bị được hỗ trợ bởi các nền tảng phần mềm mã nguồn mở thông dụng, được kiểm định bởi các tổ chức uy tín quốc tế.
2. **Tăng tốc độ và mở rộng băng thông (Speed & Bandwidth):** Khi hàng triệu thiết bị cùng truyền dữ liệu, luồng video giám sát và dịch vụ phản hồi thời gian thực, áp lực về băng thông và độ trễ gia tăng mạnh mẽ trên các máy chủ, cổng định tuyến (Gateway) và bộ thu phát biên.
3. **Tối ưu năng lượng và hiệu suất (Energy Optimization):** Thiết bị IoT thường chạy bằng pin và đặt tại nơi khó tiếp cận. Xu thế thiết kế hiện đại chuyển từ tối ưu hóa rời rạc sang phương pháp thiết kế tích hợp vi mạch - đóng gói - hệ thống (**Chip-Package-System - CPS**), cho phép tối ưu đồng thời xuyên suốt toàn bộ hệ thống, cân bằng điện áp hoạt động thấp với độ tin cậy vận hành.
4. **Kiến trúc Cloud/Edge-based IoT:** Đòi hỏi sự kết hợp chặt chẽ giữa khả năng lưu trữ, tính toán quy mô lớn của điện toán đám mây với khả năng xử lý thời gian thực, bảo vệ quyền riêng tư của điện toán cận biên (Edge Computing).

## Bài tập Chương 1

1. Hãy liệt kê những thiết bị có thể kết nối vào Internet trong thực tế đời sống.
2. Hãy phân tích những đặc điểm kỹ thuật cơ bản của thiết bị phần cứng được sử dụng trong hệ thống IoT.
3. Hãy trình bày những xu thế phát triển chính của IoT trên thế giới và triển vọng tại Việt Nam.
4. Hãy nêu các lợi ích then chốt mà công nghệ IoT mang lại cho các ngành kinh tế - xã hội.
5. Hãy phân tích những thách thức lớn nhất mà IoT đang phải đối mặt hiện nay (bảo mật, năng lượng, tiêu chuẩn hóa).

# Chương 2: Các lĩnh vực ứng dụng IoT

## Nội dung chương

- **2.1.** Nhà thông minh (Smart Home).
- **2.2.** Đô thị thông minh (Smart City) và Trạm quan trắc môi trường UIT-SmartCity.
- **2.3.** Nông nghiệp thông minh (Smart Agriculture).
- **Bài tập Chương 2.**


Trong những năm gần đây, các thuật ngữ liên quan đến IoT như smart home, smart garden, smart parking,... và đặc biệt là smart city (thành phố thông minh/đô thị thông minh) được nhắc đến khá nhiều trong giới học thuật và cũng đã có những sản phẩm được bán ra ngoài thị trường. Mục tiêu cuối cùng của các ứng dụng IoT là làm cho cuộc sống trở nên dễ dàng, thân thiện hơn với con người. Máy móc, đồ vật, môi trường có thể hiểu được suy nghĩ của con người và hành động theo ý muốn của con người.

Trong chương này, tác giả đề cập đến một số ứng dụng IoT phổ biến, đã và đang được nghiên cứu phát triển hiện nay. Tuy mỗi giải pháp của mỗi nhà khoa học, công ty có thể khác nhau về hình thức, quy mô, nhưng chung quy lại những sản phẩm, giải pháp này đều có chung một số tính năng cơ bản được đề cập trong chương này.

Giải pháp đầu tiên mà khi nhắc đến IoT người ta hay liên tưởng đến đầu tiên, đó là smart home (nhà thông minh). Trong giải pháp nhà thông minh, các vật dụng gia đình có thể được điều khiển từ xa hoặc nếu cao cấp hơn, chúng có thể tự hoạt động mà không cần sự tác động trực tiếp của gia chủ.

Giải pháp IoT thứ hai được nhắc đến trong chương này là Smart City. Đây không phải là một ứng dụng đơn lẻ mà bao gồm cả một hệ sinh thái các ứng dụng được tích hợp với nhau thông qua một kiến trúc phân cấp từ nhà quản lý, nhà điều hành đến các cư dân của thành phố.

Ứng dụng thứ ba được giới thiệu trong chương này là Smart Agriculture (nông nghiệp thông minh). Một kiến trúc tổng quát về nông nghiệp thông minh được đưa ra để giúp người đọc có cái nhìn tổng quát về ứng dụng này.

Hình 2.1 mô tả các loại ứng dụng IoT, bao gồm phân loại về nội dung (Multimedia hoặc Scalar) và phân loại về chủ thể (Hệ thống hoặc con người).

Hình 2.1. Phân loại ứng dụng Internet of Things [28]

Các ứng dụng IoT vừa nêu trên sẽ được giới thiệu một cách tổng quát trong Chương 2. Phần kiến trúc cụ thể của một ứng dụng IoT sẽ được trình bày trong Chương 3 của giáo trình này; các phần mềm, phần cứng phân loại phần cứng được sử dụng trong IoT sẽ nằm trong Chương 4.

## 2.1. Nhà thông minh (Smart Home)

Smart Home là ứng dụng phổ biến nhất trong IoT. Mục tiêu cốt lõi của Smart Home là tạo ra ngôi nhà tiện nghi, thích ứng với nhu cầu của gia chủ. Trong Smart Home, các cảm biến được đặt tại nhiều vị trí trong nhà thu thập dữ liệu như nhiệt độ, độ ẩm, ánh sáng bên trong nhà và ngoài trời để các ứng dụng có thể điều khiển các thiết bị trong nhà cho phù hợp với từng ngữ cảnh. Hình 2.4 mô tả một số thiết bị trong gia đình có thể được điều khiển qua các ứng dụng IoT.

Nhiều giải pháp được tích hợp để đưa ra một ứng dụng smart home. Tùy vào quy mô, mức độ của smart home mà các giải pháp được tích hợp nhiều hay ít. Sau đây là một số giải pháp trong ứng dụng smart home:

- **Giám sát an ninh:** Hệ thống camera giám sát được trang bị xung quanh ngôi nhà để đảm bảo không có sự xâm nhập bất hợp pháp vào ngôi nhà của gia chủ. Tính thông minh của hệ thống này có thể được tích hợp vào hệ thống cửa ra vào nếu trang bị hệ thống nhận diện gia chủ. Hệ thống thứ hai là cảm biến đặt tại cửa ra vào, cửa sổ, cảm biến chuyển động, cảm biến khí ga, hay cảm biến khói có thể cho gia chủ biết được tình trạng ngôi nhà của mình khi vắng nhà. Hình 2.2 là ví dụ về bảng điều khiển của hệ thống cảm biến đặt trong nhà thông minh, bao gồm giá trị của các cảm biến nhiệt độ, độ ẩm và các thiết bị chiếu sáng ở các vị trí trong nhà. Bên cạnh đó, hệ thống phát hiện và ngăn ngừa xâm nhập cũng có thể được tích hợp vào hệ thống để tăng mức độ an ninh cho ngôi nhà.

Hình 2.2. Ví dụ về Giao diện của Hệ thống giám sát trong Nhà thông minh

- **Điều khiển thiết bị gia đình:** Gia chủ có thể điều khiển từ xa bật/tắt bóng đèn, quạt, rèm cửa,... thông qua một chiếc điện thoại thông minh. Hình 2.3 là ví dụ về giao diện điều khiển các thiết bị trong nhà thông minh, bao gồm các hệ thống điều khiển cửa ra vào và hệ thống chiếu sáng trong mỗi phòng. Ngoài ra, các ứng dụng smart home hay smart building còn tập trung vào việc điều khiển hệ thống sưởi, hệ thống lọc gió. Ứng dụng tự điều chỉnh nhiệt độ của điều hòa nhiệt độ hoặc điều khiển mở rèm cửa hay bật bóng đèn khi nhận thấy trong phòng có người và cường độ ánh sáng thấp.

Hình 2.3. Ví dụ về Giao diện của Hệ thống điều khiển trong Nhà thông minh

- **Quản lý năng lượng:** Giúp gia chủ theo dõi mức tiêu thụ điện năng của từng thiết bị trong nhà theo thời gian thực, từ đó đưa ra các gợi ý hoặc tự động tối ưu hóa việc sử dụng điện nhằm tiết kiệm chi phí.

- **Quản lý các thiết bị nhà bếp:** Tủ lạnh thông minh có thể nhận biết các loại thực phẩm bên trong, hạn sử dụng và tự động lên danh sách mua sắm, máy pha cà phê tự động kích hoạt theo lịch trình báo thức của gia chủ.

Hình 2.4. Các thiết bị trong Smart Home [29]

## 2.2. Đô thị thông minh (Smart City)

Smart cities - Thành phố thông minh là một bước tiến mới cho sự phát triển đô thị. Trong đó, cơ sở hạ tầng công nghệ thông tin và truyền thông (Information and Communication Technology - ICT), bao gồm các lĩnh vực trọng tâm như trí tuệ nhân tạo, điện toán đám mây, dữ liệu lớn và Internet vạn vật đóng vai trò nền tảng để tối ưu hóa việc quản lý các nguồn lực và phục vụ cư dân tốt hơn.

Sự bùng nổ dân số đô thị và tốc độ đô thị hóa nhanh chóng đang đặt ra nhiều thách thức lớn về giao thông, môi trường, y tế, giáo dục và quản lý an ninh trật tự. Đô thị thông minh ra đời nhằm giải quyết những bài toán cấp bách này bằng cách áp dụng công nghệ số vào mọi mặt của đời sống đô thị.

Xu thế này sẽ làm ảnh hưởng đến cuộc sống của mỗi cư dân và vào việc di chuyển của cư dân trong thành phố.

Khái niệm smart cities đã được đề xuất từ khoảng 10 năm trước đây. Trong đó, châu Âu là nơi có nhiều dự án nghiên cứu và phát triển về vấn đề này nhiều nhất. Một số dự án tại châu Âu có thể kể đến như FP7 SmartSantander [1], OUTSMART [2], BUTLER...

Các nước châu Á cũng đã bước đầu đề xuất và xây dựng các thành phố thông minh như Singapore, Seoul, Tokyo,... Tại Việt Nam, nhiều thành phố lớn như Hà Nội, TP. Hồ Chí Minh, Đà Nẵng, Cần Thơ, Bình Dương,... cũng đang trong quá trình xây dựng đề án và triển khai từng phần của thành phố thông minh.

---
[1] http://smartsantander.eu  
[2] https://www.worldsensing.com/innovation/  

**Các hướng tiếp cận trong việc phát triển thành phố thông minh:**

- **Từ trên xuống (Top-down):** xây dựng kiến trúc tổng thể rồi sau đó tiến hành xây dựng các dự án cụ thể.
- **Từ dưới lên (Bottom-up):** xây dựng từng dự án cụ thể sau đó tiến hành tích hợp các dự án này thành một kiến trúc tổng thể.
- **Lai ghép (Hybrid):** thực hiện xây dựng theo cả hai hướng tiếp cận trên, đưa ra kiến trúc chung, vừa xây dựng từng dự án, vừa tích hợp.

Hình 2.7. Giao diện điều khiển của Trạm quan trắc môi trường tại ĐH Công nghệ Thông tin

Hệ thống quan trắc này gồm các nút cảm biến về các loại khí CO, NO2, Nhiệt độ, Độ ẩm, Lượng mưa, Tốc độ gió, Cường độ ánh sáng. Dữ liệu này được thu thập và chuyển đến UIT Cloud. Tại đây, dữ liệu cảm biến được phân tích và hiển thị cho người dùng thông qua giao diện bên trên.

### 2.2.1. Kiến trúc tổng quát

Hạ tầng IoT cho một smart city là kiến trúc 4 lớp được mô tả trong Hình 2.8 bên dưới. Dữ liệu được truyền từ các thiết bị cảm biến thông qua các cổng giao tiếp và mạng diện rộng về trung tâm dữ liệu để xử lý và cung cấp dịch vụ đến người dùng.

Hình 2.8. Kiến trúc tổng quát của Smart City (Nguồn: Cisco Press)

người hoặc ứng dụng. Thiết bị cảm biến (sensor) và actuator sẽ được trình bày chi tiết trong Chương 4 của giáo trình này.

Tùy vào mục đích của ứng dụng mà các loại cảm biến khác nhau có thể sử dụng. Sau đây là một số loại cảm biến được sử dụng trong những ứng dụng cụ thể:

- **Cảm biến gần (Proximity Sensor):** được dùng để phát hiện sự kiện đỗ xe bằng cách phân tích những thay đổi trong phạm vi xung quanh nó khi một vật thể xuất hiện.
- **Cảm biến từ:** dùng để phát hiện phương tiện kim loại di chuyển qua các nút giao thông.
- **Cảm biến môi trường:** đo nồng độ bụi mịn PM2.5, nhiệt độ, độ ẩm, nồng độ các chất khí độc hại trong không khí.
- **Camera thông minh:** dùng để nhận diện biển số xe, nhận diện khuôn mặt, phát hiện tai nạn hoặc ùn tắc giao thông tự động.

Hình 2.9. Kiến trúc mạng phổ biến trong City Layer (Nguồn: Cisco Press)

**Data Center Layer:** Dữ liệu thu thập từ Street Layer sẽ được chuyển tiếp đến Data Center Layer. Lớp này chịu trách nhiệm lưu trữ, xử lý để đưa ra các quyết định kịp thời cho toàn bộ hệ thống đô thị.

**Service Layer:** Cung cấp các giao diện lập trình ứng dụng (APIs) và các dịch vụ trực quan hóa dữ liệu đến các cơ quan quản lý và người dân.

Ví dụ trong ứng dụng Smart parking có hai nhóm người dùng có thể truy cập vào hệ thống: Người lái xe và Người quản lý bãi đỗ xe. Người lái xe có thể tìm kiếm chỗ đỗ xe còn trống gần nhất, đặt chỗ và thanh toán phí tự động. Người quản lý có thể theo dõi tỷ lệ lấp đầy, doanh thu và tối ưu hóa phân luồng xe.

### 2.2.2. Giao thông thông minh

Giao thông thông minh (Intelligent Transportation Systems - ITS) là một trong những hợp phần quan trọng nhất của đô thị thông minh. Mục tiêu là giảm thiểu ùn tắc, tai nạn giao thông, giảm lượng khí thải CO2 và nâng cao trải nghiệm đi lại của người dân.

Hình 2.10. Các ứng dụng trong Giao thông thông minh

Tại Việt Nam, các dự án đường sắt đô thị cũng đang được xây dựng tại Hà Nội và TP.HCM kết hợp với các hệ thống vé thông minh, quản lý điều hành tự động.

### 2.2.3. Môi trường thông minh

Môi trường thông minh là việc ứng dụng công nghệ IoT và dữ liệu lớn để theo dõi, phân tích chất lượng môi trường không khí, nước, tiếng ồn, đồng thời quản lý hiệu quả hệ thống chiếu sáng công cộng và thu gom rác thải.

### 2.2.4. Cuộc sống thông minh

Nâng cao chất lượng cuộc sống cho người dân thông qua các dịch vụ công trực tuyến, y tế thông minh, giáo dục thông minh và các hoạt động văn hóa giải trí số hóa.

Hình 2.11. Kiến trúc của một hệ thống Dự báo chất lượng không khí

### 2.2.5. Một số dự án thành phố thông minh

Nhiều thành phố lớn trên thế giới đã triển khai thành công các dự án thành phố thông minh với quy mô lớn. Dưới đây là một số ví dụ tiêu biểu:

**Thành phố Amsterdam (Hà Lan):** Dự án Amsterdam Smart City (ASC) được khởi xướng từ năm 2009, tập trung vào các lĩnh vực như Smart Mobility, Smart Living, Smart Society, Smart Economy và Smart Areas.

trong chiến lược Thành phố thông minh của Amsterdam. Trong đó, hệ thống chiếu sáng thông minh Smart Lighting cho phép điều chỉnh độ sáng đèn đường tùy theo lưu lượng người qua lại và điều kiện thời tiết, giúp tiết kiệm đến 50% điện năng tiêu thụ.

Các dự án năng lượng tái tạo và lưới điện thông minh (Smart Grid) tại khu vực Nieuw-West cho phép các hộ gia đình tự sản xuất điện từ pin mặt trời và bán lại lượng điện dư thừa vào lưới điện thành phố.

Hệ thống quản lý giao thông kết hợp với dữ liệu thời gian thực giúp giảm thiểu tình trạng kẹt xe và khuyến khích người dân sử dụng xe đạp hoặc phương tiện giao thông công cộng.

Hình 2.12. Các đặc điểm của Thành phố thông minh tại Amsterdam [3]

**Thành phố Barcelona (Tây Ban Nha):** Barcelona được xem là một trong những hình mẫu thành công nhất về đô thị thông minh tại châu Âu. Thành phố đã triển khai mạng lưới cảm biến diện rộng phục vụ nhiều mục đích khác nhau.

---
[3] https://smartcommunities.media/truly-smart-city-five-lessons/  

Barcelona cũng đã thành lập các dự án Thành phố thông minh từ rất sớm. Thành phố triển khai hệ thống tưới tiêu thông minh cho các công viên, hệ thống chiếu sáng LED kết hợp cảm biến chuyển động, và hệ thống thùng rác thông minh có gắn cảm biến báo mức đầy để tối ưu lộ trình thu gom rác.

Hình 2.13. Chương trình trong dự án Thành phố thông minh tại Barcelona [6]

---
[6] https://journals.openedition.org/factsreports/4367  

- **Cảm biến tiếng ồn:** Hệ thống cảm biến chi phí thấp và dễ sử dụng, có thể phát hiện được ô nhiễm không khí, tiếng ồn, độ ẩm và nhiệt độ đã giúp phát hiện được mức độ ô nhiễm tiếng ồn ở gần các quảng trường đạt mức 100 decibel - vượt quá khuyến nghị của Tổ chức Y tế Thế giới (WHO).

- **Hệ thống thủy lợi:** Các cảm biến khác nhau được đặt trong lòng đất cung cấp dữ liệu về độ ẩm, nhiệt độ, tốc độ gió, ánh sáng mặt trời và áp suất khí quyển. Các dữ liệu này được cung cấp đến nhà nông để họ điều chỉnh loại cây trồng phù hợp cho từng thời điểm. Ngoài năng suất và chất lượng cây trồng được tăng lên, lượng nước sử dụng cũng giảm đi đáng kể. Theo ước tính, lượng nước sử dụng cho nông nghiệp của Thành phố đã giảm một phần tư so với trước đó.

Hình 2.14. Kiến trúc của Chính quyền thành phố trong dự án Thành phố thông minh của Barcelona [7]

Hình 2.14 mô tả kiến trúc của Chính quyền thông minh trong dự án Thành phố thông minh của Barcelona. Kiến trúc này tạo ra sự liên thông trong toàn bộ quy trình xử lý công việc tại mỗi bộ phận trong Chính quyền thành phố. Từ đó, sự phối hợp giữa các bên liên quan (lãnh đạo, phòng ban, và người dân) trở nên dễ dàng.

---
[7] https://journals.openedition.org/factsreports/4367  

Năm 2014, dự án “Connecting Copenhagen” đã được nhận giải thưởng The World's Best Smart City Project. Dự án này được quản lý bởi Cơ quan Quản lý Kỹ thuật và Môi trường của Copenhagen và được điều phối bởi Copenhagen Solutions Lab. Copenhagen đặt mục tiêu trở thành thủ đô trung hòa carbon đầu tiên của thế giới vào năm 2025 và Đan Mạch quyết tâm trở nên hoàn toàn độc lập với nhiên liệu hóa thạch vào năm 2050.

Hình 2.15. Chiến lược thành phố thông minh của Copenhagen [8]

## 2.3. Nông nghiệp thông minh (Smart Agriculture)

Nông nghiệp hiện đại (Precision Agriculture) là một hướng đi mới bằng cách sử dụng Công nghệ thông tin, Hệ thống thông tin địa lý (Geographic Information System - GIS), GPS, WSN,... nhằm tăng năng suất cây trồng và giảm thiểu tác động môi trường. Theo đó, IoT và các công nghệ liên quan như WSN,

---
[8] https://www.niras.dk/media/1585/kimspiegelbergsteltzer.pdf  

Cloud Computing, Big Data, Data Analytic, AI... là một giải pháp hoàn chỉnh cho Nông nghiệp hiện đại. Ngoài ra, nông nghiệp hiện đại đang tìm cách thay đổi nông nghiệp truyền thống thành chất lượng cao, năng suất cao, tiết kiệm chi phí và tài nguyên.

Hình 2.16 mô tả kiến trúc của một hệ thống nông nghiệp thông minh.

Cũng giống như các ứng dụng thông minh khác, một giải pháp Nông nghiệp thông minh bao gồm 4 lớp: WSN, Edge, Cloud Computing và Service. Các thông tin về môi trường như nhiệt độ, độ ẩm, ánh sáng.... được thu thập qua cảm biến và gửi về Cloud thông qua các nút biên (Edge), các dịch vụ lưu trữ, phân tích được thực hiện ngay tại Cloud và đưa ra các quyết định và truyền các tín hiệu điều khiển này ngược về các nút tại WSN để điều khiển các thiết bị như máy bơm nước, đèn,...

Hình 2.16. Kiến trúc của một ứng dụng nông nghiệp thông minh

Hình 2.16 mô tả kiến trúc của một ứng dụng Nông nghiệp thông minh. Lớp đầu tiên của kiến trúc này là Lớp thiết bị. Các đối tượng trong lớp này bao gồm máy móc trong nông nghiệp, vật nuôi, cây trồng.... được gắn các thiết bị cảm biến để thu thập dữ liệu từ môi trường thực tế. Sau đó, dữ liệu này được truyền

đến Gateway thông qua nhiều bộ giao thức khác nhau như Zigbee, Bluetooth, LoRa, WLAN,... Các bộ giao thức này sẽ được trình bày trong Chương 3 của giáo trình này. Dữ liệu từ Gateway được chuyển tiếp đến Cloud thông qua các bộ giao thức như TCP/IP, Cellular. Tại đây, dữ liệu cảm biến được lưu trữ, phân tích và đưa ra các dự đoán và chuyển tiếp đến Web App trên thiết bị của người dùng. Lớp cuối cùng trong ứng dụng Nông nghiệp thông minh là Lớp người dùng. Tại đây, người dùng có thể xem được các thông số của môi trường, vật nuôi từ dữ liệu thô (raw data) hoặc dữ liệu sau khi được phân tích, dự đoán. Các loại dữ liệu này còn được gọi là ngữ cảnh - được trình bày trong Chương 6 của giáo trình. Ngoài ra, người dùng có thể đưa ra tín hiệu điều khiển ngược lại đến các thiết bị tại Lớp thiết bị để điều khiển các công cụ trong lớp này.

## Bài tập Chương 2

1. Hãy liệt kê những ứng dụng IoT trên thế giới và ở Việt Nam.
2. Hãy liệt kê những ứng dụng trong Thành phố thông minh.
3. Hãy liệt kê các thành phần chính trong một kiến trúc IoT.
4. Hãy thiết kế kiến trúc IoT cho nông nghiệp tại Việt Nam.
5. Hãy thiết kế kiến trúc IoT và liệt kê các chức năng của ứng dụng nhà thông minh.
6. Hãy trình bày ý tưởng và xây dựng kiến trúc IoT phục vụ cho việc giám sát giao thông tại Việt Nam.
7. Hãy trình bày ý tưởng và xây dựng kiến trúc IoT trong giám sát chất lượng không khí tại Thành phố Hồ Chí Minh.

# Chương 3: Các kiến trúc mạng và bộ giao thức mạng IoT

## 3.1. The Open System Interconnection Model
(*Mô hình kết nối hệ thống mở*)
- Nearly all data networks in use today are based on the Open Systems Interconnection (OSI) standard.
(*Mạng máy tính ngày nay chủ yếu dựa trên tiêu chuẩn Open Systems Interconnection (OSI).*)
- The OSI model was introduced by the International Organization for Standardization (ISO), in 1984, to address this complex problem. ISO is a global federation of national standards organizations representing over 100 countries.
(*Mô hình OSI được giới thiệu bởi Tổ chức Tiêu chuẩn hóa Quốc tế (ISO), vào năm 1984, để giải quyết vấn đề phức tạp này. ISO là một liên đoàn toàn cầu gồm các tổ chức tiêu chuẩn quốc gia đại diện cho hơn 100 quốc gia.*)
- The model is intended to describe and standardize the main communication functions of any telecommunication or computing system without regard to their underlying internal structure and technology. Its goal is the interoperability of diverse communication systems with standard protocols.
(*Mô hình nhằm mục đích mô tả và chuẩn hóa các chức năng giao tiếp chính của bất kỳ hệ thống viễn thông hoặc máy tính nào mà không quan tâm đến cấu trúc và công nghệ nội bộ cơ bản của chúng. Mục tiêu của nó là khả năng tương tác của các hệ thống giao tiếp đa dạng với các giao thức chuẩn.*)
- The OSI is a conceptual model of how various components communicate in data-based networks. It uses “divide and conquer” concept to virtually break down network communication responsibilities into smaller functions, called layers, so they are easier to learn and develop.
(*OSI là một mô hình khái niệm về cách các thành phần khác nhau giao tiếp trong mạng dựa trên dữ liệu. Nó sử dụng khái niệm "chia để trị" để chia nhỏ các trách nhiệm giao tiếp mạng thành các chức năng nhỏ hơn, gọi là các lớp, để chúng dễ học và phát triển.*)

## 3.2. Transmission Control Protocol/Internet Protocol (TCP/IP)
(*Bộ giao thức Internet Transmission Control Protocol/Internet*)
- TCP/IP (Transmission Control Protocol/Internet Protocol) is a connection-oriented transport protocol suite that sends data as an unstructured stream of bytes.
(*TCP/IP (Transmission Control Protocol/Internet Protocol) là một bộ giao thức truyền tải hướng kết nối, gửi dữ liệu dưới dạng luồng byte không cấu trúc.*)
- TCP/IP was in the process of development when the OSI standard was published in 1984. The TCP/IP model is not exactly the same as OSI model. OSI is a seven layered standard, but TCP/IP is a four-layered standard.
(*TCP/IP đã được phát triển khi tiêu chuẩn OSI được công bố vào năm 1984. Mô hình TCP/IP không hoàn toàn giống với mô hình OSI. OSI là một tiêu chuẩn bảy lớp, nhưng TCP/IP là một tiêu chuẩn bốn lớp.*)
- TCP/IP Layer 4: Application Layer (*Lớp Ứng dụng*)
    - As with the OSI model, the Application Layer is the topmost layer of TCP/IP model. It combines the Application, Presentation, and Session Layers of the OSI model.
    (*Tương tự như mô hình OSI, Lớp Ứng dụng là lớp trên cùng của mô hình TCP/IP. Nó kết hợp Lớp Ứng dụng, Lớp Trình bày và Lớp Phiên của mô hình OSI.*)
    - The Application Layer defines TCP/IP application protocols and how host programs interface with Transport Layer services to use the network.
    (*Lớp Ứng dụng định nghĩa các giao thức ứng dụng TCP/IP và cách các chương trình máy chủ giao tiếp với các dịch vụ Lớp Truyền tải để sử dụng mạng.*)
- TCP/IP Layer 3: Internet Layer (*Lớp Mạng*)
    - The Transport Layer is the third layer of the four-layer TCP/IP model. Its main tenacity is to permit devices on the source and destination hosts to carry on a conversation.
    (*Lớp Truyền tải là lớp thứ ba của mô hình TCP/IP bốn lớp. Chức năng chính của nó là cho phép các thiết bị trên máy chủ gửi và nhận giao tiếp với nhau.*)
    - The Transport Layer defines the level of service and status of the connection used when transporting data. The main protocols included at the Transport Layer are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
    (*Lớp Truyền tải định nghĩa mức độ dịch vụ và trạng thái của kết nối được sử dụng khi truyền dữ liệu. Các giao thức chính bao gồm TCP (Transmission Control Protocol) và UDP (User Datagram Protocol).*)    
- TCP/IP Layer 2: Internet Layer (*Lớp Internet*)
    - The Internet Layer of the TCP/IP stack packs data into data packets known as IP datagrams, which contain source and destination address information that is used to forward the datagrams between hosts and across networks.
    (*Lớp Internet của ngăn xếp TCP/IP đóng gói dữ liệu thành các gói dữ liệu được gọi là datagram IP, chứa thông tin địa chỉ nguồn và đích được sử dụng để chuyển tiếp datagram giữa các máy chủ và qua các mạng.*)    
- TCP/IP Layer 1: Network Access Layer (*Lớp Truy cập Mạng*)
    - The Network Access Layer combines the OSI Link and Physical layers. It is the lowest layer of the TCP/IP model.
    (*Lớp Truy cập Mạng kết hợp Lớp Liên kết và Lớp Vật lý của OSI. Nó là lớp thấp nhất của mô hình TCP/IP.*)
    - The Network Access Layer defines the network access protocols, such as Ethernet and Wi-Fi, and how they are used to transport datagrams over the physical medium.
    (*Lớp Truy cập Mạng định nghĩa các giao thức truy cập mạng, chẳng hạn như Ethernet và Wi-Fi, và cách chúng được sử dụng để truyền datagram qua môi trường vật lý.*)    
    - The Network Access Layer: The Network Access Layer defines details of how data is physically sent through the network. This includes how bits are electrically or optically signaled by hardware devices that interface directly with a network medium, such as coaxial cable, optical fiber, radio links, or twisted pair copper wire.
    (*Lớp Truy cập Mạng: Lớp Truy cập Mạng định nghĩa chi tiết cách dữ liệu được gửi vật lý qua mạng. Điều này bao gồm cách các bit được báo hiệu bằng điện hoặc quang bởi các thiết bị phần cứng giao tiếp trực tiếp với môi trường mạng, chẳng hạn như cáp đồng trục, cáp quang, liên kết vô tuyến hoặc dây đồng xoắn đôi.*)
- Router Main Components (*Các thành phần chính của Router*)
    - NVRAM (Nonvolatile RAM): NVRAM is used to store the startup configuration file “startup config,” which is used during system startup to configure the software.
    (*NVRAM (RAM không bay hơi): NVRAM được sử dụng để lưu trữ tệp cấu hình khởi động “startup config,” được sử dụng trong quá trình khởi động hệ thống để cấu hình phần mềm.*)
    This is due to the fact that NVRAM does not lose its content when the power is turned off. In other words, the router’s configuration is not erased when the router is reloaded.
    (*Điều này là do NVRAM không mất nội dung khi mất nguồn điện. Nói cách khác, cấu hình của router không bị xóa khi router được khởi động lại.*)
    - Console (Management) Interface: Console port or interface is the management port which is used by administrators to log on to a router directly (i.e., without using a network connection) via a computer with an RJ-45 or miniUSB connector.
    (*Cổng Console (Quản lý): Cổng hoặc giao diện Console là cổng quản lý được sử dụng bởi quản trị viên để đăng nhập trực tiếp vào router (tức là không sử dụng kết nối mạng) thông qua máy tính có đầu nối RJ-45 hoặc miniUSB.*)
    - Flash Memory: Flash memory is used to store the Cisco IOS image, the operating system of the router. It is a type of nonvolatile memory that is electrically erasable and reprogrammable. Like NVRAM, flash memory retains its contents when power is turned off.
    (*Bộ nhớ Flash: Bộ nhớ Flash được sử dụng để lưu trữ ảnh Cisco IOS, hệ điều hành của router. Nó là một loại bộ nhớ không bay hơi có thể xóa và lập trình lại bằng điện. Giống như NVRAM, bộ nhớ flash giữ nguyên nội dung khi tắt nguồn.*)
    - DRAM (Dynamic Random Access Memory): DRAM is volatile memory and is used to store information such as the routing table, ARP cache, frame tables, and packet buffers.
    (*DRAM (Bộ nhớ truy cập ngẫu nhiên động): DRAM là bộ nhớ bay hơi và được sử dụng để lưu trữ thông tin như bảng định tuyến, bộ đệm ARP, bảng khung và bộ đệm gói.*)
    
## 3.3. IoT Network Level: Key Performance Characteristics
(*Một số đặc điểm hiệu năng chính của mạng IoT*)
- Data Rate: The rate at which data can be transferred between devices on the network.
(*Tốc độ dữ liệu: Tốc độ dữ liệu có thể được truyền giữa các thiết bị trên mạng.*)
- Latency: The time it takes for data to travel from one device to another on the network.
(*Độ trễ: Thời gian để dữ liệu di chuyển từ thiết bị này sang thiết bị khác trên mạng.*)
- Jitter: The variation in the time it takes for data to travel from one device to another on the network.
(*Jitter: Sự biến đổi trong thời gian để dữ liệu di chuyển từ thiết bị này sang thiết bị khác trên mạng.*)
- Reliability: The probability that data will be transferred successfully from one device to another on the network.
(*Độ tin cậy: Xác suất dữ liệu được truyền thành công từ thiết bị này sang thiết bị khác trên mạng.*)
- Scalability: The ability of the network to support a large number of devices and users.
(*Khả năng mở rộng: Khả năng của mạng hỗ trợ một số lượng lớn thiết bị và người dùng.*)
- Security: The ability of the network to protect data from unauthorized access and use.
(*Bảo mật: Khả năng của mạng bảo vệ dữ liệu khỏi truy cập và sử dụng trái phép.*)
- Energy Efficiency: The ability of the network to operate with low power consumption.
(*Hiệu quả năng lượng: Khả năng của mạng hoạt động với mức tiêu thụ năng lượng thấp.*)
- The IoT Network Level is in fact the TCP/IP Layers. It should be noted that we have
removed TCP/IP’s Application Layer to prevent overlap with the IoT Application Level.
(*Cấp Độ Mạng IoT thực chất là các lớp TCP/IP. Cần lưu ý rằng chúng ta đã loại bỏ Lớp Ứng dụng của TCP/IP để tránh trùng lặp với Lớp Ứng dụng IoT.*)
- IoT Network Level key characteristics may be grouped into three main areas: end-to-end delay, packet loss, and network element throughput. Ideally, engineers want the IoT network to move data between any end points (or source and destination) instantaneously, without any delay or packet loss. 
(*Các đặc điểm chính của Cấp Độ Mạng IoT có thể được nhóm thành ba lĩnh vực chính: độ trễ đầu cuối, mất gói và thông lượng phần tử mạng. Lý tưởng nhất, các kỹ sư muốn mạng IoT di chuyển dữ liệu giữa bất kỳ điểm cuối nào (hoặc nguồn và đích) ngay lập tức, không có độ trễ hoặc mất gói.*) 
- End-to-End Delay: End-to-end delay across the IoT network is perhaps the most essential performance characteristic for real-time applications especially in wide area networks (WAN) that connect multiple geographies
(*Độ trễ đầu cuối trên mạng IoT có lẽ là đặc điểm hiệu năng thiết yếu nhất đối với các ứng dụng thời gian thực, đặc biệt là trong các mạng diện rộng (WAN) kết nối nhiều khu vực địa lý.*)
    - Processing delay: which is defined as the time a router takes to process the packet header and determine where to forward the packet. It may also include the time needed to check for bit-level errors in the packet (typically in the order of microseconds).
    (*Độ trễ xử lý: được định nghĩa là thời gian router xử lý tiêu đề gói và xác định nơi chuyển tiếp gói. Nó cũng có thể bao gồm thời gian cần thiết để kiểm tra lỗi bit trong gói (thường trong khoảng micro giây).*)   
    - Queuing delay: which is defined as the time the packet spends in router queues as it awaits to be transmitted onto the outgoing link. Clearly Queuing delay depends on the number of earlier-arriving packets in the same queue (typically in the order of microseconds to milliseconds).
    (*Độ trễ hàng đợi: được định nghĩa là thời gian gói tin nằm trong hàng đợi của router khi chờ được truyền trên liên kết đi. Rõ ràng, độ trễ hàng đợi phụ thuộc vào số lượng gói tin đến trước trong cùng một hàng đợi (thường trong khoảng micro giây đến mili giây).*) 
    - Transmission delay: which is defined as the time it takes to push the packet’s bits onto the link. Transmission delay of packet of length L bits is defined L/R where R is the transmission rate of a link between two devices. For example, for a packet of length 1000 bits and a link of speed of 100 Mbps, the delay is 0.01 ms. (Transmission delay is typically in the order of microseconds to milliseconds.)
    (*Độ trễ truyền: được định nghĩa là thời gian cần thiết để đẩy các bit của gói tin vào liên kết. Độ trễ truyền của một gói có độ dài L bit được xác định bằng L/R, trong đó R là tốc độ truyền của liên kết giữa hai thiết bị. Ví dụ, đối với một gói có độ dài 1000 bit và một liên kết có tốc độ 100 Mbps, độ trễ là 0.01 ms. (Độ trễ truyền thường trong khoảng micro giây đến mili giây).*) 
    - Propagation delay: which is defined as the time for a bit (of the packet) to propagate from the beginning of a link (once it leaves the source router) to reach its destination router. Hence, Propagation delay on a given link depends on the physical medium of the link itself (e.g., twisted pair copper, fiber, coaxial cable) and is equal to the distance of the link (between two routers) divided by the propagation speed (e.g., speed of light). (Propagation delay is typically in the order of milliseconds). It should be noted that unlike Transmission delay (i.e., the amount of time required to push a packet out), Propagation delay is independent of the packet length.
    (*Độ trễ lan truyền: được định nghĩa là thời gian để một bit (của gói tin) lan truyền từ đầu liên kết (sau khi rời khỏi router nguồn) đến router đích. Do đó, độ trễ lan truyền trên một liên kết cụ thể phụ thuộc vào môi trường vật lý của chính liên kết đó (ví dụ: cáp đồng xoắn đôi, cáp quang, cáp đồng trục) và bằng khoảng cách của liên kết (giữa hai router) chia cho tốc độ lan truyền (ví dụ: tốc độ ánh sáng). (Độ trễ lan truyền thường trong khoảng mili giây). Cần lưu ý rằng không giống như độ trễ truyền (tức là lượng thời gian cần thiết để đẩy một gói tin ra ngoài), độ trễ lan truyền không phụ thuộc vào độ dài gói tin.*)
    - Nodal processing delay: which is defined as the time a router takes to process the packet header and determine where to forward the packet. It may also include the time needed to check for bit-level errors in the packet (typically in the order of microseconds).
    (*Độ trễ xử lý tại nút: được định nghĩa là thời gian router xử lý tiêu đề gói và xác định nơi chuyển tiếp gói. Nó cũng có thể bao gồm thời gian cần thiết để kiểm tra lỗi bit trong gói (thường trong khoảng micro giây).*) 
    - Hence, the total delay (dTotal), between two end points, is the sum of the Processing delay (dProcess), the Queuing delay (dQueue), the Transmission delay (dTrans), and the Propagation delay (dProp) across utilized network elements in the path, i.e
        dTotal = dProcess + dQueue + dTrans + dProp
    (*Do đó, độ trễ đầu cuối (dTotal), giữa hai điểm cuối, là tổng của độ trễ xử lý (dProcess), độ trễ hàng đợi (dQueue), độ trễ truyền (dTrans), và độ trễ lan truyền (dProp) qua các phần tử mạng được sử dụng trên đường đi, tức là*)
        dTotal = dProcess + dQueue + dTrans + dProp
    - End-to-end delay is typically measured using Traceroute utility (available on many modern operating systems) as well as vendor-specific tools (e.g., Cisco’s IP SLA (service-level agreement) that continuously collects data about delay, jitter, response time, and packet loss).
    (*Độ trễ đầu cuối thường được đo bằng tiện ích Traceroute (có sẵn trên nhiều hệ điều hành hiện đại) cũng như các công cụ dành riêng cho nhà cung cấp (ví dụ: IP SLA của Cisco (thỏa thuận mức dịch vụ) liên tục thu thập dữ liệu về độ trễ, jitter, thời gian phản hồi và mất gói).*) 
- Packet loss: Packet loss is defined as the fraction of packets that fail to reach their destination, and it is often measured as a percentage (i.e., from 0 to 100%). Ideally, the IoT network should be able to deliver all packets from the source to the destination. However, in practice, packet loss occurs due to various reasons, including network congestion, router or link failures, software bugs, or interference (e.g., in wireless networks).
(*Mất gói: Mất gói được định nghĩa là tỷ lệ các gói không đến được đích, và nó thường được đo dưới dạng phần trăm (tức là từ 0 đến 100%). Lý tưởng nhất, mạng IoT sẽ có khả năng gửi tất cả các gói từ nguồn đến đích. Tuy nhiên, trên thực tế, mất gói xảy ra do nhiều lý do, bao gồm tắc nghẽn mạng, lỗi router hoặc liên kết, lỗi phần mềm hoặc nhiễu (ví dụ: trong mạng không dây).*)
    - Packet loss occurs when at least one packet of data traveling across a network fails to reach its destination.
    (*Mất gói xảy ra khi ít nhất một gói dữ liệu đi qua mạng không đến được đích.*)
    - In general, packets are dropped and consequently lost when the network is congested (i.e., one of the network elements is already operating at full capacity and cannot keep up with arriving packets). This is due to the fact that both queues and links have finite capacities.
    (*Thông thường, các gói tin bị loại bỏ và do đó bị mất khi mạng bị tắc nghẽn (tức là một trong các phần tử mạng đã hoạt động hết công suất và không thể theo kịp các gói đến). Điều này là do cả hàng đợi và liên kết đều có dung lượng hữu hạn.*)
    - Hence, a main reason for packet loss is link or queue congestion (i.e., a link between two devices, and its associated queues, is fully occupied when data arrives).
    (*Do đó, một nguyên nhân chính gây mất gói là tắc nghẽn liên kết hoặc hàng đợi (tức là một liên kết giữa hai thiết bị và các hàng đợi liên quan của nó đã đầy khi dữ liệu đến).*) 
- Throughput
    - Throughput may be defined as the maximum amount of data moved successfully between two end points in a given amount of time. Related measures include the link and device speed (how fast a link or a device can process the information) and response time (the amount of time to receive a response once the request is sent).
    (*Thông lượng có thể được định nghĩa là lượng dữ liệu tối đa được di chuyển thành công giữa hai điểm cuối trong một khoảng thời gian nhất định. Các số liệu liên quan bao gồm tốc độ liên kết và thiết bị (tốc độ liên kết hoặc thiết bị có thể xử lý thông tin) và thời gian phản hồi (lượng thời gian để nhận được phản hồi sau khi yêu cầu được gửi).*)    
    - Throughput is one of the key performance measures for network and computing devices and is typically measured in bits per second (bps) or gigabits per second (Gbps) at least for larger network devices. The system throughput is typically calculated by aggregating all throughputs across end points in a network (i.e., sum of successful data delivered to all destination terminals in a given amount of time).
    (*Thông lượng là một trong những thước đo hiệu suất quan trọng đối với các thiết bị mạng và máy tính và thường được đo bằng bit trên giây (bps) hoặc gigabit trên giây (Gbps) đối với các thiết bị mạng lớn. Thông lượng hệ thống thường được tính bằng cách tổng hợp tất cả thông lượng qua các điểm cuối trong một mạng (tức là tổng dữ liệu được gửi thành công đến tất cả các thiết bị đầu cuối trong một khoảng thời gian nhất định).*)  

## 3.4. Internet Protocol Suite (Bộ giao thức Internet)
- Mạng Internetworking và giao thức TCP/IP. Được phát triển chủ yếu bởi Robert Kahn và Vint Cerf từ những năm 1970, bộ giao thức này cho phép kết nối nhiều mạng máy tính khác nhau thành một "mạng của các mạng" (Internet). 
- As we mentioned earlier, TCP/IP provides end-to-end connectivity specifying how data should be packetized, addressed, transmitted, routed, and received at the destination. The objective of this chapter is not to provide an exhaustive list of the TCP/IP protocols but rather to provide a summary of the key protocols that are essential for IoT.
(*Như đã đề cập ở trên, TCP/IP cung cấp kết nối đầu cuối quy định cách dữ liệu phải được đóng gói, định địa chỉ, truyền, định tuyến và nhận tại đích. Mục tiêu của chương này không phải là cung cấp một danh sách đầy đủ các giao thức TCP/IP mà là cung cấp một bản tóm tắt về các giao thức chính cần thiết cho IoT.*)  
- IoT Network Level: Addressing (Định địa chỉ)
    - IP addresses are globally unique numbers assigned by the Network Information Center. Globally unique addresses permit IP networks anywhere in the world to communicate
    with each other. Most of existing networks today use IP version 4 (IPv4). Advanced
    networks use IP version 6 (IPv6). 
    (*Địa chỉ IP là các số duy nhất toàn cầu được gán bởi Trung tâm Thông tin Mạng. Địa chỉ duy nhất toàn cầu cho phép các mạng IP ở bất kỳ đâu trên thế giới giao tiếp với nhau. Hầu hết các mạng hiện nay sử dụng IP phiên bản 4 (IPv4). Các mạng tiên tiến sử dụng IP phiên bản 6 (IPv6).*)   
- IP Version 4 (IPv4)
    - IPv4 addresses are normally expressed in dotted-decimal format, with four numbers separated by periods, such as 192.168.10.10. It consists of 4-octets (32-bit) number that uniquely identifies a specific TCP/IP (or IoT) network and a host (computer, printer, router, IP-enabled sensor, any device requiring a network interface card) within the identified network. IPv4 address consists of two main parts: the network address part and the host address part.    
    (*Địa chỉ IPv4 thường được biểu thị dưới dạng thập phân chấm, với bốn số được ngăn cách bởi dấu chấm, ví dụ: 192.168.10.10. Nó bao gồm số 4-octets (32-bit) xác định duy nhất một mạng TCP/IP (hoặc IoT) cụ thể và một máy chủ (máy tính, máy in, bộ định tuyến, cảm biến hỗ trợ IP, bất kỳ thiết bị nào yêu cầu thẻ giao diện mạng) trong mạng đã xác định. Địa chỉ IPv4 bao gồm hai phần chính: phần địa chỉ mạng và phần địa chỉ máy chủ. *)
    - For example, the dotted-decimal IP address 192.168.10.8 is (in binary notation) the 32-bit number 11000000.10101000.00001010.00001000. The decimal numbers separated by periods are the octets converted from binary to decimal notation.    
    (*Ví dụ, địa chỉ IP thập phân chấm 192.168.10.8 là số 32-bit (dưới dạng ký hiệu nhị phân) 11000000.10101000.00001010.00001000. Các số thập phân được ngăn cách bởi dấu chấm là các octet được chuyển đổi từ ký hiệu nhị phân sang ký hiệu thập phân.*)
    - The first part of an IP address is used as a network address and the last part as a host address. If you take the example 192.168.10.8 and divide it into these two parts, you get the following: 192.168.10.0 network address and .8 host address or 192.168.10.0 network address and 0.0.0.8 host address.
    (*Phần đầu tiên của địa chỉ IP được sử dụng làm địa chỉ mạng và phần cuối cùng làm địa chỉ máy chủ. Nếu bạn lấy ví dụ 192.168.10.8 và chia nó thành hai phần này, bạn sẽ nhận được như sau: địa chỉ mạng 192.168.10.0 và địa chỉ máy chủ .8 hoặc địa chỉ mạng 192.168.10.0 và địa chỉ máy chủ 0.0.0.8. *)
    - In TCP/IP, the parts of the IP address that are used as the network and host addresses are not fixed, so the network and host addresses above cannot be determined unless you have more information. This information is supplied in another 32-bit number called a subnet mask. In the above example, the subnet mask is 255.255.255.0. It is not obvious what this number means unless you know that 255 in binary notation equals 11111111; so, the subnet mask is 11111111.11111111.11111111.00000000.     
    (*Trong TCP/IP, các phần của địa chỉ IP được sử dụng làm địa chỉ mạng và địa chỉ máy chủ không cố định, vì vậy không thể xác định địa chỉ mạng và địa chỉ máy chủ ở trên trừ khi bạn có thêm thông tin. Thông tin này được cung cấp trong một số 32-bit khác gọi là subnet mask. Trong ví dụ trên, subnet mask là 255.255.255.0. Không thể biết con số này có ý nghĩa gì trừ khi bạn biết rằng 255 trong ký hiệu nhị phân bằng 11111111; vì vậy, subnet mask là 11111111.11111111.11111111.00000000.*)
    - Lining up the IP address and the subnet mask together, the network and host portions of the address can be separated: 
    (*Kết hợp địa chỉ IP và subnet mask lại, các phần mạng và máy chủ của địa chỉ có thể được phân tách:*)
        - 11000000.10101000.00001010.00001000--IP Address (192.168.10.8)
        - 11111111.11111111.11111111.00000000--Subnet Mask (255.255.255.0)
    - Five classes (A, B, C, D, and E) have been established to identify the network and host parts. All the five classes are identified by the first octet of IP address. Classes A, B, and C are used in actual networks. Class D is reserved for multicasting (data is not destined for a particular host; hence there is no need to extract host address from the IP address). Class E is reserved for experimental purposes.
    (*Năm lớp (A, B, C, D, và E) đã được thiết lập để xác định các phần mạng và máy chủ. Tất cả năm lớp được xác định bởi octet đầu tiên của địa chỉ IP. Lớp A, B, và C được sử dụng trong các mạng thực tế. Lớp D được dành riêng cho multicasting (dữ liệu không destinada cho một máy chủ cụ thể; do đó không cần trích xuất địa chỉ máy chủ từ địa chỉ IP). Lớp E dành riêng cho mục đích thử nghiệm.*)
    - Class A networks provide only 8 bits for the network address field and 24 bits for host address. It is intended mainly for use with very large networks with large number of hosts.
    (*Các mạng lớp A chỉ cung cấp 8 bit cho trường địa chỉ mạng và 24 bit cho địa chỉ máy chủ. Nó chủ yếu được sử dụng cho các mạng rất lớn với số lượng lớn máy chủ.*)
    - The first bit of the first octet is always set to 0 (zero). Thus the first octet ranges from 1 to 127, i.e., 00000001–011111111. Class A addresses only include IP starting from 1.x.x.x to 126.x.x.x only. The IP range 127.x.x.x is reserved for loopback IP addresses. The default subnet mask for class A IP address is 255.0.0.0 which implies that class A addressing can have 126 networks (27–2) and 16,777,214 hosts (224–2).
    (*Bit đầu tiên của octet đầu tiên luôn được đặt thành 0 (zero). Do đó, octet đầu tiên dao động từ 1 đến 127, tức là 00000001–011111111. Địa chỉ lớp A chỉ bao gồm địa chỉ IP bắt đầu từ 1.x.x.x đến 126.x.x.x. Dải địa chỉ IP 127.x.x.x được dành riêng cho địa chỉ IP loopback. Mặt nạ mạng mặc định cho địa chỉ IP lớp A là 255.0.0.0, điều này ngụ ý rằng địa chỉ lớp A có thể có 126 mạng (27–2) và 16.777.214 máy chủ (224–2).*)
    - Class B networks allocate 16 bits for the network address field and 16 bits for the host address filed. An IP address which belongs to class B has the first two bits in the first octet set to 10, i.e., 10000000–10111111 or 128–191 in decimal. Class B IP addresses range from 128.0.x.x to 191.255.x.x. The default subnet mask for class B is 255.255.x.x. Class B has 16,384 (214) network addresses and 65,534 (216–2) host addresses.
    (*Các mạng lớp B cấp phát 16 bit cho trường địa chỉ mạng và 16 bit cho trường địa chỉ máy chủ. Một địa chỉ IP thuộc lớp B có hai bit đầu tiên trong octet đầu tiên được đặt thành 10, tức là 10000000–10111111 hoặc 128–191 ở hệ thập phân. Địa chỉ IP lớp B dao động từ 128.0.x.x đến 191.255.x.x. Mặt nạ mạng mặc định cho lớp B là 255.255.x.x. Lớp B có 16.384 (214) địa chỉ mạng và 65.534 (216–2) địa chỉ máy chủ.*)
    - Class C networks allocate 24 bits for the network address field only 8 bits for the host field. Hence, the number of hosts per network may be a limiting factor. The first octet of Class C IP address has its first 3 bits set to 110, that is: 1110 0000–1110 1111 or 224–239 in decimal. Class C IP addresses range from 192.0.0.x to 223.255.255.x. The default subnet mask for Class C is 255.255.255.x. Class C gives 2,097,152 (221) Network addresses and 254 (28–2) Host addresses.
    (*Các mạng lớp C cấp phát 24 bit cho trường địa chỉ mạng và chỉ 8 bit cho trường địa chỉ máy chủ. Do đó, số lượng máy chủ trên mỗi mạng có thể là yếu tố hạn chế. Octet đầu tiên của địa chỉ IP lớp C có 3 bit đầu tiên được đặt thành 110, tức là: 1110 0000–1110 1111 hoặc 224–239 ở hệ thập phân. Địa chỉ IP lớp C dao động từ 192.0.0.x đến 223.255.255.x. Mặt nạ mạng mặc định cho lớp C là 255.255.255.x. Lớp C cung cấp 2.097.152 (221) địa chỉ mạng và 254 (28–2) địa chỉ máy chủ.*)
- IP Version 6 (IPv6)    
    - IPv4 has room for about 4.3 billion addresses, which is not nearly enough for the world’s people, let alone IoT with a forecast of 20 billion devices by 2020.
    (*IPv4 có đủ chỗ cho khoảng 4,3 tỷ địa chỉ, không đủ cho số người trên thế giới, chứ chưa nói đến IoT với dự báo 20 tỷ thiết bị vào năm 2020.*)
    - The IPv6 address is 128 bits long. It is divided into blocks of 16 bits. Each 16-bit block is then converted to a 4-digit hexadecimal number, separated by colons. The resulting representation is called colon-hexadecimal. This is in contrast to the 32-bit IPv4 address represented in dotted-decimal format, divided along 8-bit boundaries, and then converted to its decimal equivalent, separated by periods
    (*Địa chỉ IPv6 dài 128 bit. Nó được chia thành các khối 16 bit. Mỗi khối 16 bit sau đó được chuyển đổi thành một số thập lục phân 4 chữ số, được phân tách bằng dấu hai chấm. Biểu diễn kết quả được gọi là colon-hexadecimal. Điều này trái ngược với địa chỉ IPv4 32 bit được biểu diễn ở định dạng thập phân chấm, được chia theo ranh giới 8 bit, sau đó được chuyển đổi thành giá trị thập phân tương ứng, được phân tách bằng dấu chấm*)
## 3.5. Network Types
(*Các loại mạng*)
- Connection types (*Kiểu kết nối*):   
    - Point-to-point: Point-to-point connections are used to establish direct connections between two hosts. Day-to-day systems such as a remote control for an air conditioner or television is a point to point connection, where the connection has the whole channel dedicated to it only. These networks were designed to work over duplex links and are functional for both synchronous as well as asynchronous systems.
    (*Kết nối điểm-điểm được sử dụng để thiết lập các kết nối trực tiếp giữa hai máy chủ. Các hệ thống hàng ngày như điều khiển từ xa cho máy điều hòa không khí hoặc TV là kết nối điểm-điểm, nơi kết nối có toàn bộ kênh dành riêng cho nó. Các mạng này được thiết kế để hoạt động qua các liên kết song công và hoạt động cho cả hệ thống đồng bộ và không đồng bộ.*)
    - Point-to-multipoint: In a point-to-multipoint connection, more than two hosts share the same link. This type of configuration is similar to the one-to-many connection type. Point-to-multipoint connections find popular use in wireless networks and IP telephony.The channel is shared between the various hosts, either spatially or temporally.
    (*Điểm-đến-nhiều điểm: Trong kết nối điểm-đến-nhiều điểm, nhiều máy chủ cùng chia sẻ một liên kết. Loại cấu hình này giống với loại kết nối một-nhiều. Kết nối điểm-đến-nhiều điểm thường được sử dụng trong mạng không dây và điện thoại IP. Kênh được chia sẻ giữa các máy chủ khác nhau, hoặc theo không gian hoặc theo thời gian.*)
- Physical topology: Depending on the physical manner in which communication paths between the hosts are connected, computer networks can have the following four broad topologies: Star, Mesh, Bus, and Ring.
(*Tùy thuộc vào cách thức vật lý mà các đường truyền giữa các máy chủ được kết nối, mạng máy tính có thể có bốn loại topo rộng sau: Hình sao, Lưới, Bus và Vòng.*)
- Star: In a star topology, every host has a point-to-point link to a central controller or hub. The hosts cannot communicate with one another directly; they can only do so through the central hub. The hub acts as the network traffic exchange. For large-scale systems, the hub, essentially, has to be a powerful server to handle all the simultaneous traffic flowing through it. The main advantages of the star topology are easy installation and the ease of fault identification within the network. However, the main disadvantage of this topology is the danger of a single point of failure. If the hub fails, the whole network fails.
    (*Trong topo hình sao, mọi máy chủ có một liên kết điểm-điểm tới một bộ điều khiển hoặc trung tâm. Các máy chủ không thể giao tiếp trực tiếp với nhau; chúng chỉ có thể làm như vậy thông qua bộ trung tâm. Bộ trung tâm đóng vai trò trao đổi lưu lượng mạng. Đối với các hệ thống quy mô lớn, bộ trung tâm, về cơ bản, phải là một máy chủ mạnh mẽ để xử lý tất cả lưu lượng truy cập đồng thời chảy qua nó. Ưu điểm chính của topo hình sao là dễ lắp đặt và dễ xác định lỗi trong mạng. Tuy nhiên, nhược điểm chính của topo này là nguy cơ lỗi điểm duy nhất. Nếu bộ trung tâm bị lỗi, toàn bộ mạng sẽ ngừng hoạt động.*)
- Mesh: 
    - In a mesh topology, every host is connected to every other host is connected to every other host using a dedicated link (in a point-to-point manner).
    (*Trong topo hình lưới, mọi máy chủ có một liên kết điểm-điểm tới mọi máy chủ khác là kết nối với mọi máy chủ khác bằng một liên kết dành riêng (theo cách điểm-điểm).*) 
    - The first significant advantage is the robustness and resilience of the system. Even if a link is down or broken, the network is still fully functional as there remain other pathways for the traffic to flow through. The second advantage is the security and privacy of the traffic as the data is only seen by the intended recipients and not by all members of the network. 
    (*Ưu điểm quan trọng đầu tiên là sự mạnh mẽ và phục hồi của hệ thống. Ngay cả khi một liên kết bị ngắt hoặc hỏng, mạng vẫn hoạt động đầy đủ vì còn các đường truyền khác cho lưu lượng đi qua. Ưu điểm thứ hai là tính bảo mật và riêng tư của lưu lượng vì dữ liệu chỉ được nhìn thấy bởi người nhận dự định chứ không phải tất cả các thành viên trong mạng.*) 
    - The third advantage is the reduced data load on a single host, as every host in this network takes care of its traffic load. However, owing to the complexities in forming physical connection between devices and the cost of establishing these links, mesh networks are used very selectively, such as in backbone networks.
    (*Ưu điểm thứ ba là giảm tải dữ liệu cho một máy chủ vì mọi máy chủ trong mạng này đều xử lý tải lưu lượng của chính nó. Tuy nhiên, do sự phức tạp trong việc hình thành kết nối vật lý giữa các thiết bị và chi phí thiết lập các liên kết này, mạng lưới chỉ được sử dụng rất hạn chế, chẳng hạn như trong mạng lõi.*) 
- Bus
    - A bus topology follows the point-to-multipoint connection. A backbone cable or bus serves as the primary traffic pathway between the hosts. The hosts are connected to the main bus employing drop lines or taps. The main advantage of this topology is the ease of installation. However, there is a restriction on the length of the bus and the number of hosts that can be simultaneously connected to the bus due to signal loss over the extended bus.
    (*Topo bus tuân theo kết nối điểm-đến-nhiều điểm. Một cáp hoặc bus chính phục vụ như là đường truyền chính giữa các máy chủ. Các máy chủ được kết nối với bus chính bằng các đường truyền hoặc vòi phụ. Ưu điểm chính của topo này là dễ lắp đặt. Tuy nhiên, có một hạn chế về chiều dài của bus và số lượng máy chủ có thể được kết nối đồng thời với bus do mất tín hiệu trên bus kéo dài.*) 
    - A ring topology works on the principle of a point-to-point connection. Here, each host is configured to have a dedicated point-to-point connection with its two immediate neighboring hosts on either side of it through repeaters at each host. The repetition of this system forms a ring. The repeaters at each host capture the incoming signal intended for other hosts, regenerates the bit stream, and passes it onto the next repeater. Fault identification and set up of the ring topology is quite simple and straightforward. However, the main disadvantage of this system is the high probability of a single point of failure. If even one repeater fails, the whole network goes down.
    (*Topo vòng hoạt động dựa trên nguyên tắc kết nối điểm-điểm. Tại đây, mỗi máy chủ được cấu hình để có một kết nối điểm-điểm dành riêng với hai máy chủ lân cận ở hai bên thông qua các bộ lặp tại mỗi máy chủ. Sự lặp lại của hệ thống này tạo thành một vòng tròn. Các bộ lặp tại mỗi máy chủ thu nhận tín hiệu đến được dự định cho các máy chủ khác, tái tạo lại dòng bit và truyền nó cho bộ lặp tiếp theo. Việc xác định lỗi và thiết lập topo vòng khá đơn giản và thẳng thắn. Tuy nhiên, nhược điểm chính của hệ thống này là xác suất lỗi điểm duy nhất cao. Nếu ngay cả một bộ lặp bị lỗi, toàn bộ mạng sẽ ngừng hoạt động.*)
- Physical topology (*Topo vật lý*): 
    Network topology comparison (*So sánh topo mạng*)
    Topology (*Topo* ) | Feature (*Đặc điểm*) | Advantage (*Ưu điểm*) | Disadvantage (*Nhược điểm*) |
    |---|---|---|---|
    | Star (*Hình sao*) | Point-to-point (*Điểm-điểm*) | Cheap (*Rẻ*) ; ease of installation (*dễ lắp đặt*) ; ease of fault identification (*dễ xác định lỗi*) | Single point of failure (*điểm lỗi duy nhất*) ; traffic visible to network entities (*lưu lượng nhìn thấy được bởi các thực thể mạng*) |
    | Mesh (*Hình lưới*) | Point-to-point (*Điểm-điểm*) | Resilient against single point of failures (*khả năng phục hồi với lỗi điểm duy nhất*) ; scalable (*có thể mở rộng*) ; traffic privacy and security ensured (*đảm bảo quyền riêng tư và bảo mật lưu lượng*) | Costly (*tốn kém*) ; complex connections (*kết nối phức tạp*) |
    | Bus (*Hình bus*) | Point-to-multipoint (*Điểm-đến-nhiều điểm*) | Ease of installation (*dễ lắp đặt*) ; cheap (*rẻ*) | Length of backbone cable limited (*chiều dài cáp chính hạn chế*) ; number of hosts limited (*số lượng máy chủ hạn chế*) ; hard to localize faults (*khó xác định vị trí lỗi*) |
    | Ring (*Hình vòng*) | Point-to-point (*Điểm-điểm*) | Ease of installation (*dễ lắp đặt*) ; cheap (*rẻ*) ; ease of fault identification (*dễ xác định lỗi*) | Prone to single point of failure (*dễ bị lỗi điểm duy nhất*) |
    
## 3.6. Network Reachability (*Kiểm tra kết nối mạng*)
- Personal Area Networks (PAN) (*Mạng cá nhân*): PANs, as the name suggests, are mostly restricted to individual usage. A good example of PANs may be connected wireless headphones, wireless speakers, laptops, smartphones, wireless keyboards, wireless mouse, and printers within a house. Generally, PANs are wireless networks, which make use of low-range and low-power technologies such as Bluetooth. The reachability of PANs lies in the range of a few centimeters to a few meters. (*Mạng cá nhân (PAN) chủ yếu giới hạn trong phạm vi sử dụng cá nhân. Ví dụ điển hình về PAN có thể là tai nghe không dây, loa không dây, máy tính xách tay, điện thoại thông minh, bàn phím không dây, chuột không dây và máy in trong một ngôi nhà. Nói chung, PAN là mạng không dây sử dụng các công nghệ phạm vi ngắn và công suất thấp như Bluetooth. Phạm vi kết nối của PAN nằm trong khoảng từ vài cm đến vài mét.*)

- Local Area Networks (LAN) (*Mạng cục bộ*): A LAN is a collection of hosts linked to a single network through wired or wireless connections. However, LANs are restricted to buildings organizations, or campuses. Typically, a few leased lines connected to the Internet provide web access to the whole organization or a campus; the lines are further redistributed to multiple hosts within the LAN enabling hosts. Typically, the present-day data access rates within the LANs range from 100 Mbps to 1000 Mbps, with very high fault-tolerance levels. Commonly used network components in a LAN are servers, hubs, routers, switches, terminals, and
computers. (*Mạng cục bộ (LAN) là một tập hợp các máy chủ được kết nối với một mạng duy nhất thông qua kết nối có dây hoặc không dây. Tuy nhiên, LAN bị giới hạn trong các tòa nhà, tổ chức hoặc khuôn viên. Thông thường, một vài đường dây thuê bao được kết nối với Internet cung cấp quyền truy cập web cho toàn bộ tổ chức hoặc khuôn viên; các đường dây được phân phối tiếp cho nhiều máy chủ trong LAN cho phép máy chủ truy cập. Thông thường, tốc độ truy cập dữ liệu hiện tại trong LAN dao động từ 100 Mbps đến 1000 Mbps, với mức độ chịu lỗi rất cao. Các thành phần mạng thường dùng trong LAN là máy chủ, hub, router, switch, thiết bị đầu cuối và máy tính.*)
- Wide Area Networks (WAN) (*Mạng diện rộng*): WANs typically connect diverse geographic locations. However, they are restricted within the boundaries of a state or country. The data rate of WANs is in the order of a fraction of LAN’s data rate. Typically, WANs connecting two LANs or MANs may use public switched telephone networks (PSTNs) or satellite-based links. Due to the long transmission ranges, WANs tend to have more errors and noise during transmission and are very costly to maintain. The fault tolerance of WANs are also generally low. (*Mạng diện rộng (WAN) kết nối các địa điểm địa lý khác nhau. Tuy nhiên, chúng bị giới hạn trong phạm vi của một tiểu bang hoặc quốc gia. Tốc độ dữ liệu của WAN có giá trị bằng một phần của tốc độ dữ liệu LAN. Thông thường, WAN kết nối hai LAN hoặc MAN có thể sử dụng mạng điện thoại chuyển mạch công cộng (PSTN) hoặc đường truyền vệ tinh. Do phạm vi truyền dẫn dài, WAN có xu hướng có nhiều lỗi và nhiễu trong quá trình truyền và rất tốn kém để bảo trì. Mức độ chịu lỗi của WAN cũng thường thấp.*)

## 3.7. Các kiến trúc và topo mạng dùng trong IoT

## 3.7.1. Một số kiến trúc mạng đơn giản

**Kiến trúc mắt lưới (mesh)**

Trong mô hình mạng Mesh, gói tin từ một nút có thể có nhiều đường đi đến đích. Đây là một trong những ưu điểm của mô hình mạng mesh (trong mô hình dạng vòng mặc dù có hai đường đi, tin nhắn chỉ có thể đi theo một hướng). Trong Hình 3.1, các nút có thể kết nối đến tất cả các nút còn lại trong mạng được gọi là một mạng mesh đầy đủ (full mesh). Trong Hình 3.2, mô hình mạng mesh có một số nút có kết nối gián tiếp đến các nút khác trong mạng được gọi là mạng mesh một phần (partial mesh).

**Hình 3.1.** Kiến trúc full mesh | **Hình 3.2.** Kiến trúc Partial Mesh

**Kiến trúc cây (tree)**

Mạng sử dụng một hub trung tâm được gọi là một nút gốc, xem như là một bộ định tuyến thông tin liên lạc chính. Hình 3.3 mô tả một hệ thống phân cấp, cấp dưới nút gốc là các hub trung tâm, mức thấp này tạo thành một mạng sao. Các mạng dạng cây có thể được coi là sự lai tạo của mạng hình sao và mạng Peer to Peer. Trong đường dẫn mạng cảm biến có thể là single hop hoặc multi hop, các nút cảm biến nhận dữ liệu của môi trường rồi gửi chúng đến bộ phận thu nhận (Sink), sau đó chuyển tiếp chúng đến các nút cha mẹ. Điều quan trọng là để tìm đường đi ngắn nhất sao cho tối ưu với thời gian sống tối đa và độ trễ ngắn hơn mặc dù độ phức tạp thời gian hơi cao nhưng phù hợp hơn cho việc thực hiện phân phối. Mạng dạng cây có vấn đề trong

chương trình cân bằng tải tại mỗi mức của cây và có thông tin liên lạc giữa hai nút. Nếu có một liên kết có vấn đề trong truyền dẫn trên tuyến đường hoạt động thì việc truyền thông cũng bị phá vỡ.

**Hình 3.3.** Kiến trúc Tree

**Kiến trúc vòng (ring)**

Hình 3.4 mô tả một mô hình mạng có kiến trúc vòng, mỗi nút có đúng hai người hàng xóm cho mục đích truyền thông. Tất cả các tin nhắn đi qua một vòng trong cùng một hướng (hoặc là "chiều kim đồng hồ" hay "ngược chiều kim đồng hồ"). Nếu một nút trong vòng gặp vấn đề thì có thể phá vỡ các vòng lặp và cũng có thể làm sụp đổ toàn bộ mạng. Tin nhắn trong mô hình này có hai đường đi nhưng chỉ có thể đi theo một hướng.

**Hình 3.4.** Kiến trúc Ring

**Kiến trúc chuỗi (chain)**

Trong một mạng dạng chain, các nút kết nối với nhau thành dạng chuỗi như Hình 3.5 bên dưới. Ngoài nút đầu và nút cuối,

mỗi nút trong mạng chain có đúng hai người hàng xóm cho mục đích truyền thông. Nếu một nút trong chuỗi gặp vấn đề thì có thể ảnh hưởng đến việc gửi nhận thông tin của cả mạng.

**Hình 3.5.** Kiến trúc chuỗi

**Kiến trúc sao (Star)**

Mạng hình sao được kết nối với một hub đóng vai trò là bộ phận truyền thông trung tâm (Sink) và các nút (các nút này không thể giao tiếp trực tiếp với nhau). Hình 3.6 là một ví dụ về mô hình mạng sao có một nút trung tâm và năm nút đầu cuối. Toàn bộ thông tin liên lạc phải được định tuyến thông qua hub trung tâm. Mỗi nút là một "client", trong khi hub trung tâm là "server hoặc sink". Nhưng mô hình này có nhược điểm là chỉ có một đường giao tiếp duy nhất.

**Hình 3.6.** Star Topology

**Kiến trúc lưới (Grid)**

Các trường cảm biến mạng được chia thành các đường kẻ ô. Các vùng mạng được chia thành lưới ô vuông không chồng lên nhau với cùng một kích thước. Hình 3.7 mô tả một ứng dụng dựa trên kiến trúc lưới. Nên có ít nhất một và chỉ một nút trong trạng thái làm việc trong mỗi lưới tại bất cứ khoảng thời gian nào. Để kéo dài thời gian sống mạng, các nút trong một mạng lưới nên hoạt động lần lượt. Bên trong mỗi lưới, một nút được chọn như là lưới đầu tiên có trách nhiệm chuyển tiếp thông tin

định tuyến và truyền gói dữ liệu. Định tuyến được thực hiện trong lần lượt từ lưới này đến các lưới khác. Mô hình dựa vào giao thức định tuyến đa đường dựa vào các lưới mạng để định tuyến các gói tin một cách nhanh nhất, tận dụng và mở rộng các nút cảm biến năng lượng ngoài để tránh và xử lý tắc nghẽn mạng khi chúng xảy ra trong mạng.

**Hình 3.7.** Kiến trúc lưới

## 3.7.2. Một số kiến trúc mạng phức tạp

**Kiến trúc dựa theo cụm (cluster-based)**

Kiến trúc dựa theo cụm/nhóm (cluster-based) là kiến trúc mà các thiết bị cảm biến thu thập dữ liệu và gửi về một thiết bị đầu cụm (cluster head). Hình 3.8 là một ví dụ về mạng cảm biến có kiến trúc gồm 6 cluster, mỗi cluster được quản lý bởi một Cluster Head. Cách làm này mang đến hiệu quả cao trong trường hợp hệ thống mạng cảm biến có kích thước lớn, khoảng cách xa nhau và định tuyến qua nhiều mức (multihop routing). Kiến trúc dựa trên cụm này làm giảm lượng dữ liệu truyền gửi giữa tất cả các cảm biến so với kiến trúc khác như mesh. Một số kỹ thuật tinh giảm dữ liệu (reduction techniques) có thể được áp dụng để tăng cường hiệu quả. Tuy nhiên, kiến trúc dựa trên cụm này có khuyết điểm là nếu thiết bị đầu cụm ở quá xa các thiết bị cảm biến thì sẽ làm tăng chi phí truyền thông, năng lượng tiêu thụ.

**Hình 3.8.** Kiến trúc dựa theo cụm (cluster-based)

**Kiến trúc dựa trên địa hình phụ lưu - đồng bằng (Tributary - Delta)**

Kiến trúc Tributary - Delta [1], được hình thành từ ý tưởng dòng chảy của con sông, là một cách tiếp cận mới trong tập hợp dữ liệu trong mạng. Kiến trúc này là kết quả của việc kết hợp các ưu thế của kiến trúc dựa trên kiến trúc cây (tree-based) và định tuyến đa luồng (multi-path routing). Hình 3.9 là một ví dụ về kiến trúc Tributary - Delta, mô hình mạng được chia làm hai vùng riêng biệt: Tributary và Delta. Trong mạng độ lỗi thấp, kiến trúc cây được sử dụng cho các thông điệp có kích thước nhỏ, trong trường hợp độ lỗi cao, dữ liệu thu thập từ rất nhiều cảm biến thì multi-path routing được sử dụng để đảm bảo hiệu quả.

**Hình 3.9.** Kiến trúc Tributary - Delta [1]

**Kiến trúc dựa theo làn sóng (Sweep)**

**Hình 3.10.** Kiến trúc dựa theo làn sóng [2]

Đây là kiến trúc thu thập dữ liệu dựa trên ý tưởng hoạt động của làn sóng mà ở đó dữ liệu đi ngang qua mỗi thiết bị đúng một lần và thực hiện các hành động theo ý muốn [2]. Kiến trúc mạng sweep được hiện thực bởi một nhóm nhỏ các nốt hoạt động, các nốt này di chuyển qua mạng bằng cách phát một thông điệp lời mời tới các nốt mới để tham gia vào nhóm và loại bỏ các nốt đã thực hiện rồi nhưng không đóng vai trò quan trọng gì khác. Đặc trưng quan trọng của kiến trúc này là tính chất bền vững bởi mặc dù một kiến trúc cây được sử dụng cho một phần tác vụ tổng hợp dữ liệu trong một nhóm hoạt động thì những cây này là cục bộ và được dùng hầu hết ngay khi chúng được xây dựng. Đường tổng hợp dữ liệu được phân chia trên đường quét và không cần thiết phải có một cấu trúc cây cố định cho việc tính toán. Vì vậy, cách tiếp cận này có tính vững vàng ngay cả với các liên kết có sự biến động và nhiều nút bị hỏng. Hình 3.10 mô tả kiến trúc mạng theo làn sóng, trong đó, các nốt trong vùng màu đỏ đang hoạt động, các nốt trong vùng màu xanh đã hoạt động và các nốt màu trắng chưa tham gia vào mạng.

## 3.8. Các bộ giao thức mạng không dây thường dùng trong IoT

### 3.8.0. Tổng quan các chuẩn mạng không dây trong IoT
- Để triển khai được các kiến trúc truyền tải dữ liệu, các nền tảng phần
mềm, hệ điều hành chạy trên thiết bị IoT phải hỗ trợ các chuẩn kết nối
không dây mà ở đó những cơ chế, giải thuật định tuyến, điều khiển
kết nối giữa các thiết bị hoạt động đúng như thiết kế. Tập hợp tất cả
cơ chế, giải thuật, quy trình đó được định nghĩa và thiết kế theo một
tiêu chuẩn mạng, tạo nên các bộ giao thức mạng đảm bảo chức năng
truyền gửi dữ liệu và tín hiệu điều khiển trong mạng cảm biến không
dây cũng như mạng Internet bên ngoài.
- Bộ giao thức 6LowPAN: 6LowPAN là viết tắt của “IPv6 over Low-Power Wireless Personal Area Network”, là công nghệ mạng cho phép gói tin IPv6 được sử dụng trong những link layer nhỏ như định nghĩa trong IEEE 802.15.4.
Là lựa chọn tốt cho các ứng dung IoT khi mạng cảm biến không dây có kích thước lớn.
- Kiến trúc mạng 6LoWPAN: Có hai loại thiết bị phổ biến bên trong mạng 6LoWPAN là: router và host; trong đó router dùng để định tuyến đường đi tới các node trong mạng 6LoWPAN, host chính là các thiết bị cuối, không có khả năng định tuyến., host có thể hoạt động ở chế độ “ngủ” và được đánh thức định kỳ để tiết kiệm năng lượng tiêu thụ.
- Nền tảng hiện thực bộ giao thức 6LoWPAN:
    - Bộ giao thức mạng 6LoWPAN là một chuẩn giao thức được sử dung phổ biến trong nhiều giải pháp IoT.
    - Với đặc trưng cho phép thiết bị IoT giao tiếp trực tiếp với mạng Internet bên ngoài thông qua địa chỉ IPv6, giao thức 6LoWPAN đã được nghiên cứu và hiện thực trên nhiều nền tảng phần cứng, phần mềm khác nhau.
- Một số nền tảng phần cứng hỗ trợ chuẩn 6LoWPAN: 
    - CC2650 SimpleLink 6LoWPAN/ZigBee Wireless MCUs
    - CC1310 SimpleLink Wireless MCUs
    - ZWIR4532 IoT 6LoWPAN Module
    - Contiki 
    - Mbed OS
- Bộ giao thức Zigbee: Mạng Zigbee có 3 nhóm thiết bị logic (theo chức năng):
    - Thiết bị điều phối mạng (Coordinator).
    - Bộ định tuyến (Router).
    - Thiết bị đầu cuối.
- Kiến trúc mạng Zigbee:
    - Coordinator: Được sử dụng để tạo mạng Zigbee. Khi một nút kết nối, nó sẽ cấp cho địa chỉ cho nút con. Mỗi mạng Zigbee cần và chỉ cần một Coordinator. Các mạng khác nhau phải có PAN ID khác nhau. Nếu có hai Coordinator có cùng PAN ID thì Coordinator khởi động sau sẽ tự động them một vào PAN ID để tránh xung đột.
    - Router: Chịu trách nhiệm chuyển tiếp các gói dữ liệu để tìm đường truyền thích hợp nhất. Mỗi mạng Zigbee có thể yêu cầu nhiều hơn 1 Router. Mỗi Router không những có thể gửi hoặc nhận dữ liệu mà còn có thể chuyển tiếp dữ lieu. Cấu trúc mạng Zigbee:
        - Mạng Zigbee chứa 1 Coordinator và n Router, tất cả chúng đều phải có chung PAN ID.
        - Mỗi nút có thể gửi và nhận dữ liệu, cũng có thể chuyển tiếp. Mỗi nút có thể kết nối tối đa đến 6 nút con.
        - Router được nhận một địa chỉ (địa chỉ ngắn – Short Address) là hằng số, có thể được sử dụng trong truyền điểm – điểm.
        - Kể cả khi Coordinator bị ngắt điện, Router vẫn có thể duy trì mạng lưới, vì vậy, giữa Router và Router vẫn có thể giao tiếp được.
        - Khi một nút được thêm vào ngay cả khi Coordinator bị ngắt điện, nó vẫn có thể thông qua các địa chỉ của Router hiện hữu để tham gia vào mạng lưới. Mô tả về 1 mạng Zigbee bao gồm 1 Coordinator, 6 Router, và một số End Devices.
- Một số đặc điểm của chuẩn Zigbee trong ứng dung mạng cảm biến không dây:
    - Zigbee có độ tin cậy cao.
    - Zigbee có chi phí thấp.
    - Zigbee sử dụng năng lượng thấp.
    - Zigbee bảo mật cao.
    - Zigbee là một chuẩn mở toàn bộ.
    - Zigbee có tốc độ truyền dữ liệu thấp.
    - Zigbee bảo mật cao.
    - Zigbee là một chuẩn mở toàn bộ.
    - Zigbee có tốc độ dữ liệu thấp.

- Nền tảng hiện thực bộ giao thức mạng Zigbee
    - CC2530 
    - CC2538
    - Digi Xbee Zigbee 
    - CC2530 Module Connector
    - Arduino-based
    - nRF5 SDK

Để triển khai được các kiến trúc truyền tải dữ liệu như trình bày ở phần trên, các nền tảng phần mềm, hệ điều hành chạy trên thiết bị IoT phải hỗ trợ các chuẩn kết nối không dây mà ở đó những cơ chế, giải thuật định tuyến, điều khiển kết nối giữa các thiết bị hoạt động đúng như thiết kế. Tập hợp tất cả cơ chế, giải thuật, quy trình đó được định nghĩa và thiết kế theo một tiêu chuẩn mạng, tạo nên các bộ giao thức mạng đảm bảo chức năng truyền gửi dữ liệu và tín hiệu điều khiển trong mạng cảm biến không dây cũng như mạng Internet bên ngoài.

Trong kiến trúc mạng IoT, có hai cách tiếp cận để các thiết bị IoT có thể truyền dữ liệu ra bên ngoài mạng Internet đó là: (i) thiết bị IoT có một địa chỉ mạng riêng biệt (địa chỉ IPv6) để giao tiếp trực tiếp với mạng bên ngoài; (ii) các thiết bị IoT giao tiếp nội bộ trong mạng IoT của mình, sau đó gửi dữ liệu ra ngoài thông qua thiết bị cổng (IoT Gateway) hoặc các thiết bị trạm (base station). Hai bộ giao thức mạng đặc trưng cho hai cơ chế kết nối này đó là bộ giao thức 6LoWPAN (thiết bị IoT kết nối trực tiếp với mạng bên ngoài qua IPv6) và bộ giao thức Zigbee. Bên cạnh hai bộ giao thức đặc trưng đó, ngày nay giải pháp kết nối thiết bị IoT qua mạng WLAN truyền thống cũng được sử dụng phổ biến trong các ngữ cảnh đơn giản. Đặc biệt, với sự ra đời của các nền tảng phần cứng hỗ trợ kết nối WiFi như ESP8266, ESP32 cho phép người mới bắt đầu với công nghệ IoT có thể hiện thực giải pháp IoT đơn giản với kết nối WiFi quen thuộc. Phần tiếp theo của phần này trình bày chi tiết đặc trưng kỹ thuật của các bộ giao thức không dây vừa kể trên.

### 3.8.1. Bộ giao thức 6LoWPAN

6LoWPAN là viết tắt của "IPv6 over Low-Power Wireless Personal Area Network", là công nghệ mạng cho phép gói tin IPv6 được sử dụng trong những link layer nhỏ như định nghĩa trong IEEE 802.15.4. Là lựa chọn tốt cho các ứng dụng IoT khi mạng cảm biến không dây có kích thước lớn [3].

6LoWPAN là chuẩn mở được định nghĩa trong RFC 6282 bởi IETF. Tính năng nổi bật của 6LoWPAN là ban đầu chỉ hỗ trợ cho IEEE 802.15.4 trong mạng cảm biến không dây tiết kiệm năng lượng trong băng tần 2.4GHz nhưng giờ đây đã mở rộng ra nhiều loại mạng khác bao gồm Sub-1 GHz low-power RF, Bluetooth, Smart Power Line Control (PLC) và low-power Wi-Fi [3].

#### 3.8.1.1. Kiến trúc mạng 6LoWPAN

Hình 3.11 trình bày kiến trúc mạng mesh 6LoWPAN. Hướng uplink ra Internet được quản lý bởi Access Point (AP) hoạt động như một IPv6 Router. Một số thiết bị khác kết nối vào Router như: PC, server... Mạng 6LoWPAN được kết nối với mạng IPv6 thông qua edge router. Các edge router quản lý 3 việc là: 1) trao đổi dữ liệu giữa thiết bị chạy 6LoWPAN và Internet (hay mạng IPv6 khác); 2) trao đổi dữ liệu nội bộ giữa các thiết bị bên trong mạng 6LoWPAN; và 3) là tạo và duy trì radio subnet (mạng 6LoWPAN).

**Hình 3.11.** Kiến trúc mạng mesh 6LoWPAN [3]

Bằng cách giao tiếp với IP truyền thống, mạng 6LoWPAN kết nối với các mạng khác thông qua router IP. Như hình trên thì mạng 6LoWPAN hoạt động trên một góc như một stub network. Điều đó có nghĩa là dữ liệu đi vào mạng để dành riêng cho một thiết bị cụ thể ở trong mạng 6LoWPAN. Bên ngoài, mạng IP truyền thống có thể được cung cấp bởi các loại liên kết khác nhau như: ethernet, Wi-Fi hay 3G/4G. Bởi vì 6LoWPAN chỉ chuyên hoạt động với IPv6 thông qua chuẩn IEEE 802.15.4, một router 6LoWPAN là một router kết nối giữa hai mạng với nhau. Các thiết bị trong mạng 6LoWPAN giao tiếp với nhau bằng giao thức định tuyến chuẩn IPv6 hoặc giao thức định tuyến 6LoWPAN. Một thiết bị trong mạng 6LoWPAN có thể là Host hoặc Router:
- **Host:** Là thiết bị đầu cuối không có chức năng chuyển tiếp gói tin đến các thiết bị khác trong mạng.
- **Router:** Là thiết bị có chức năng định tuyến chuyển tiếp gói tin giữa các nút mạng 6LoWPAN.

#### 3.8.1.2. Mô hình phân lớp các tầng giao thức trong 6LoWPAN

**Hình 3.12.** Mô hình phân lớp các tầng giao thức trong 6LoWPAN [3]

Hình 3.12 mô tả mô hình phân lớp các tầng giao thức trong 6LoWPAN. Tầng ứng dụng (Application Layer) bao gồm các giao thức ứng dụng phổ biến như CoAP, MQTT, HTTP... Tầng giao vận (Transport Layer) hỗ trợ UDP và TCP. Tầng mạng (Network Layer) sử dụng giao thức IPv6 cùng với giao thức định tuyến RPL. Tầng thích ứng (Adaptation Layer) nằm giữa tầng mạng và tầng liên kết dữ liệu, thực hiện chức năng nén tiêu đề IPv6 và phân mảnh gói tin để phù hợp với kích thước gói tin của chuẩn IEEE 802.15.4 (tối đa 127 byte). Tầng liên kết dữ liệu (Data Link Layer - MAC) và tầng vật lý (Physical Layer - PHY) tuân theo tiêu chuẩn IEEE 802.15.4.

Đặc biệt, từ phiên bản năm 2006, có hai cải tiến mới cho IEEE 802.15.4 là e và g, trong đó IEEE 802.15.4e là một MAC được cải tiến và cung cấp nhiều cơ chế nâng cấp như Time Slotted Channel Hopping (TSCH) và Coordinated Sampled Listening (CSL), cả hai cơ chế này đều hỗ trợ hoạt động tiết kiệm năng lượng. Chuẩn IEEE 802.15.4g là một cải tiến tầng PHY với mục đích ứng dụng trong các mạng tiện ích thông minh (Smart Utility Networks - SUN).

Tầng thích ứng (Adaptation layer) trong bộ giao thức 6LoWPAN chịu trách nhiệm thực hiện 3 cơ chế quan trọng:
- **Nén tiêu đề (Header Compression):** Do tiêu đề IPv6 chuẩn có kích thước cố định là 40 byte, trong khi kích thước MTU tối đa của IEEE 802.15.4 chỉ là 127 byte (sau khi trừ đi tiêu đề MAC còn khoảng 81-102 byte cho tải trọng), nếu giữ nguyên tiêu đề IPv6 sẽ chiếm gần một nửa tải trọng của khung truyền. Tầng thích ứng sử dụng các kỹ thuật nén tiêu đề theo RFC 4944 và RFC 6282 để nén tiêu đề IPv6 xuống còn vài byte (tối thiểu là 2-7 byte).
- **Phân mảnh và ghép mảnh (Fragmentation and Reassembly):** Tiêu chuẩn IPv6 yêu cầu mọi liên kết phải hỗ trợ kích thước gói tin MTU tối thiểu là 1280 byte. Vì khung truyền IEEE 802.15.4 không thể chứa trực tiếp một gói tin 1280 byte, tầng thích ứng phải chia gói tin IPv6 thành nhiều mảnh nhỏ ở phía gửi và ghép chúng lại ở phía nhận trước khi đưa lên tầng mạng IPv6.
- **Định tuyến mức liên kết (Mesh Routing / Layer-two Routing):** Hỗ trợ truyền gói tin qua nhiều chặng ở tầng liên kết dữ liệu khi cần thiết (Mesh-Under).

#### 3.8.1.3. Cấu trúc gói tin của chuẩn mạng 6LoWPAN

**Hình 3.13.** Cấu trúc gói tin IPv6 và 6LoWPAN [3]

Tiêu đề IPv6 chuẩn bao gồm các trường: Version (4 bit), Traffic Class (8 bit), Flow Label (20 bit), Payload Length (16 bit), Next Header (8 bit), Hop Limit (8 bit), Source Address (128 bit = 16 byte), và Destination Address (128 bit = 16 byte). Tổng cộng tiêu đề IPv6 cố định chiếm 40 byte.

Khi truyền qua mạng 6LoWPAN, kỹ thuật nén tiêu đề LOWPAN_IPHC (theo RFC 6282) khai thác các đặc điểm liên kết cục bộ và địa chỉ MAC sẵn có để nén tiêu đề:
- Nếu địa chỉ IPv6 nguồn hoặc đích có tiền tố liên kết cục bộ (Link-Local: `FE80::/64`) hoặc tiền tố mạng đã biết trước, tiền tố đó có thể được lược bỏ hoàn toàn.
- Phần định danh giao diện (IID - Interface Identifier) 64 bit có thể được suy ra trực tiếp từ địa chỉ MAC 64 bit (hoặc 16 bit ngắn) của tầng liên kết IEEE 802.15.4, do đó không cần truyền trong tiêu đề gói tin.
- Các trường Traffic Class và Flow Label nếu bằng 0 có thể được nén bỏ.
- Trường Next Header có thể được nén thành vài bit nếu mang giá trị phổ biến như UDP, TCP hoặc ICMPv6.

Nhờ đó, tiêu đề IPv6 từ 40 byte có thể được nén xuống chỉ còn 2 đến 7 byte trong các tình huống truyền dữ liệu thông thường.

**Hình 3.14.** Cách bố trí các header để truyền dữ liệu trong mạng 6LoWPAN [4]

Hình 3.14 mô tả cách bố trí các tiêu đề (header) khi đóng gói dữ liệu:
- Gói tin chưa phân mảnh gồm: Tiêu đề IEEE 802.15.4 MAC, tiêu đề nén 6LoWPAN (IPHC), tiêu đề UDP nén, và tải trọng ứng dụng (Payload).
- Trong trường hợp gói tin IPv6 lớn hơn MTU của IEEE 802.15.4, gói tin sẽ được phân mảnh:
  - Mảnh đầu tiên (First Fragment): chứa tiêu đề IEEE 802.15.4, tiêu đề phân mảnh (Fragment Header: Datagram Size, Datagram Tag), tiêu đề nén IPv6, tiêu đề UDP và phần đầu của dữ liệu.
  - Các mảnh tiếp theo (Subsequent Fragments): chứa tiêu đề IEEE 802.15.4, tiêu đề phân mảnh (Datagram Size, Datagram Tag, Datagram Offset) và phần dữ liệu kế tiếp.

#### 3.8.1.4. Nền tảng hiện thực bộ giao thức 6LoWPAN

Bộ giao thức 6LoWPAN hiện nay được hỗ trợ rộng rãi trên nhiều hệ điều hành và nền tảng phần cứng IoT:
- **Hệ điều hành mạng nhúng:** Contiki OS (với chồng giao thức uIPv6 / ContikiMAC), TinyOS (với BLIP - Berkeley Low-power IP Stack), RIOT OS, FreeRTOS, Zephyr OS.
- **Nền tảng phần cứng:** Các vi điều khiển hỗ trợ chuẩn IEEE 802.15.4 như TI CC2538, CC2650, CC1352, Atmel SAMR21, Nordic Semiconductor nRF52840, và các module OpenMote.

### 3.8.2. Bộ giao thức Zigbee

#### 3.8.2.1. Kiến trúc mạng Zigbee

Mạng Zigbee có 3 nhóm thiết bị logic (theo chức năng):
- **Thiết bị điều phối mạng (Coordinator - ZC):** Mỗi mạng Zigbee chỉ có duy nhất một Coordinator. Thiết bị này có trách nhiệm khởi tạo mạng, lựa chọn tần số và PAN ID (Personal Area Network Identifier), cho phép các thiết bị khác gia nhập mạng, lưu trữ thông tin cấu hình mạng và bảng định tuyến. Coordinator luôn luôn hoạt động (mains-powered).
- **Bộ định tuyến (Router - ZR):** Thiết bị định tuyến có chức năng chuyển tiếp gói tin giữa các nút trong mạng, mở rộng phạm vi bao phủ của mạng Zigbee. Router có thể cho phép các nút con (End Devices hoặc Router khác) kết nối vào mình và quản lý truyền thông cho các nút con đó. Router thường được cấp nguồn liên tục.
- **Thiết bị đầu cuối (End Device - ZED):** Là các thiết bị cảm biến hoặc cơ cấu chấp hành hoạt động bằng pin, chỉ giao tiếp trực tiếp với nút cha của nó (Coordinator hoặc Router). Thiết bị đầu cuối không có chức năng chuyển tiếp dữ liệu cho các nút khác. Khi không có dữ liệu cần truyền nhận, End Device có thể chuyển sang chế độ ngủ sâu (sleep mode) để tiết kiệm năng lượng tối đa.

**Hình 3.15.** Mô hình một mạng Zigbee

- Router được nhận một địa chỉ (địa chỉ ngắn - Short Address) là hằng số, có thể được sử dụng trong truyền điểm - điểm.
- Kể cả khi Coordinator bị ngắt điện, Router vẫn có thể duy trì mạng lưới, vì vậy giữa Router và Router vẫn có thể giao tiếp được.

Khi một nút được thêm vào ngay cả khi Coordinator bị ngắt điện, nó vẫn có thể thông qua các địa chỉ của Router hiện hữu để tham gia vào mạng lưới. Hình 3.15 mô tả về một mạng Zigbee bao gồm 1 Coordinator, 6 Router và một số End Devices.

#### 3.8.2.2. Mô hình phân lớp các tầng giao thức trong chuẩn không dây Zigbee

**Hình 3.16.** Các chồng giao thức tham chiếu giữa 802.15.4 và Zigbee

Trong Hình 3.16, lớp vật lý (PHY) và lớp MAC tuân theo chuẩn IEEE 802.15.4, các lớp phía trên bao gồm Tầng mạng (Network Layer - NWK), Tầng hỗ trợ ứng dụng (Application Support Sublayer - APS), và Đối tượng thiết bị Zigbee (Zigbee Device Objects - ZDO) cùng Khung ứng dụng (Application Framework) được định nghĩa bởi Liên minh Zigbee (Zigbee Alliance).

**Lớp vật lý (PHY)**
Theo chuẩn IEEE 802.15.4, đường truyền không dây có thể hoạt động ở 3 tần số không chính thức sau: 868MHz, 902-

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

- Truyền dữ liệu trực tiếp hoặc gián tiếp.
- Giao thức điều khiển truy cập môi trường dựa trên lập lịch và đụng độ.
- Quản lý hiệu quả năng lượng để tăng tuổi thọ của mạng.
- Dễ dàng triển khai cho mạng cỡ lớn.

#### 3.8.2.3. Cấu trúc frame của chuẩn 802.15.4

**Hình 3.18.** Cấu trúc superframe của 802.15.4

Chuẩn IEEE 802.15.4 định nghĩa một cấu trúc superframe theo yêu cầu: superframe bắt đầu bằng beacon (báo hiệu) và được chia thành 16 khe như nhau, được mô tả trong Hình 3.18. Khe thời gian đầu tiên của siêu khung dùng để phát beacon. Các khe còn lại được dùng bởi các thiết bị tranh chấp để thông tin trong thời gian truy cập tranh chấp (Contention Access Period - CAP). Các thiết bị dùng giao thức CSMA/CA phân khe thời gian để tranh chấp truy cập với các thiết bị khác. Việc thông tin giữa các thiết bị phải hoàn thành trước khi kết thúc CAP của superframe hiện tại và bắt đầu phát beacon của superframe kế tiếp.

Tiêu chuẩn IEEE 802.15.4 quy định MAC frame gồm 3 thành phần: MAC header, MAC payload và MAC footer như trong Hình 3.19. MAC header gồm trường điều khiển frame và trường địa chỉ. MAC payload chứa dữ liệu cần trao đổi, và MAC footer chứa các trường kiểm tra frame.

**Hình 3.19.** Data Frame trong chuẩn 802.15.4

IEEE 802.15.4 cũng định nghĩa 4 dạng frame cơ bản: beacon frame, frame dữ liệu, frame xác nhận ACK và MAC command frame:
- **Beacon frame:** Được bộ điều phối mạng phát theo chu kỳ để xác nhận mạng và cấu trúc mạng, đánh thức các thiết bị từ trạng thái ngủ và đồng bộ hoạt động mạng. Beacon frame rất quan trọng trong cấu hình mô mạng Mesh và Tree. Chúng hỗ trợ cho tất cả các nút mạng đồng bộ mà không cần các nút phải hoạt động ở chế độ tích cực trong thời gian dài.
- **Data frame:** Có thể dài tới 104 octets dữ liệu (1 octet = 1 byte). Mỗi frame dữ liệu mang một chuỗi số thứ tự xác nhận. Chuỗi số đảm bảo tất cả các khung được đếm và nhận hợp lệ. Trường FCS (checksum) dùng để phát hiện lỗi frame.
- **ACK frame:** Thiết bị nhận gửi frame ACK tương ứng cho phía phát để thông báo frame dữ liệu nhận được là hợp lệ và không có lỗi.
- **MAC command frame:** Được dùng để thông báo và thông tin phục vụ mục đích quản lý mạng tập trung để điều khiển và cấu hình thiết bị từ xa. Nhóm lệnh bao gồm phối hợp thiết bị, yêu cầu dữ liệu, thông báo PAN ID, yêu cầu beacon, GTS, tổ chức lại coordinator.

Thiết kế lớp giao thức MAC rất quan trọng trong mạng WSNs, nó đảm bảo hiệu quả sử dụng năng lượng để kéo dài thời gian sống của mạng, tạo nên khả năng mở rộng phù hợp kích thước mạng, mật độ node và cấu hình mạng. Các thuộc tính quan trọng khác cần lưu ý của thiết kế giao thức MAC là sự công bằng giữa các node, giảm độ trễ, hạn chế lưu lượng cao của băng thông.

#### 3.8.2.4. Một số đặc điểm của chuẩn Zigbee trong ứng dụng mạng cảm biến không dây

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

Điều đầu tiên là dựa vào một kỹ thuật không dây rất tin cậy, khoảng cách thấp và dùng sự đặc tả IEEE 802.15.4. Đặc tả này là một kỹ thuật radio mạnh, rất hiện đại được xây dựng trên 40 năm kinh nghiệm của IEEE. Nó dùng Offset-Quadrature Phase-Shift Keying (O-QPSK) và Direct Sequence Spread Spectrum (DSSS), một sự kết hợp của các kỹ thuật nhằm cung cấp hiệu suất tín hiệu trên nhiễu (Signal-to-Noise Ratio - SNR) rất cao ở công suất truyền phát thấp.

Thứ hai, chuẩn IEEE 802.15.4 định nghĩa cơ chế đa truy cập cảm nhận sóng mang tránh xung đột (CSMA-CA). Trước khi truyền tin, thiết bị lắng nghe kênh truyền để đảm bảo không có thiết bị nào khác đang phát sóng, qua đó giảm thiểu va chạm dữ liệu trên môi trường truyền.

Thứ ba, mỗi khung truyền đều đi kèm mã kiểm tra độ dư thừa vòng 16 bit (16-bit CRC) trong trường FCS. Phía nhận thực hiện kiểm tra CRC trên toàn bộ khung dữ liệu; nếu phát hiện sai sót bit, khung truyền sẽ bị hủy bỏ ngay lập tức.

Thứ tư, cơ chế báo nhận (ACK) tại mỗi hop đảm bảo tính toàn vẹn của việc truyền tin giữa hai nút kế cận. Nếu phía phát không nhận được ACK trong một khoảng thời gian chờ định trước, nó sẽ tự động phát lại khung tin (lên tới số lần truyền lại tối đa quy định).

Thứ năm, kiến trúc định tuyến mạng lưới (mesh networking) với thuật toán AODV cho phép các gói tin tự động tìm đường vòng qua các nút trung gian khác nếu một nút hoặc liên kết trên đường đi chính bị hỏng hoặc nghẽn.

Thêm vào đó, Zigbee cung cấp việc broadcast tin cậy. Zigbee cũng cung cấp multicasting có thể gửi một message đến một nhóm các nút trong mạng.

Cuối cùng, Zigbee cung cấp tự động ACK end-to-end. Ứng dụng nguồn có thể yêu cầu một xác nhận mức ứng dụng từ nút đích cuối cùng để đảm bảo rằng gói tin không chỉ đến được nút mạng mà còn được xử lý thành công bởi ứng dụng đích.

**Bảo mật trong Zigbee**

Bên cạnh độ tin cậy, bảo mật là một yếu tố sống còn đối với các hệ thống điều khiển tự động hóa và IoT:
- Zigbee sử dụng thuật toán mã hóa tiêu chuẩn tiên tiến AES-128 (Advanced Encryption Standard với độ dài khóa 128 bit) để bảo vệ tính bảo mật của dữ liệu.
- Tính toàn vẹn của thông điệp được đảm bảo thông qua mã xác thực thông điệp CBC-MAC (Cipher Block Chaining Message Authentication Code) gắn kèm gói tin.
- Cơ chế chống phát lại (Replay Protection) sử dụng số thứ tự khung tuần tự (Frame Counter) để ngăn chặn kẻ tấn công ghi lại và phát lại các gói tin hợp lệ nhằm chiếm quyền điều khiển hệ thống.
- Zigbee hỗ trợ 3 loại khóa bảo mật chính: Master Key (dùng để thiết lập các khóa khác), Network Key (dùng chung cho toàn bộ các nút trong mạng), và Link Key (dùng riêng biệt giữa hai nút cụ thể để bảo mật thông tin liên lạc ngang hàng).

Hiệp hội Zigbee đã quyết định giữ giao thức trong một môi trường tốc độ truyền dữ liệu thấp.

Với tần số 2.4GHz, tốc độ truyền tối đa của Zigbee là 250kbps, nhưng do số lần truyền lại, sự mã hóa và giải mã, và giao thức lưới đầy đủ được dùng nên throughput thực sự khoảng 25kbps. Transceivers là half-duplex, đây cũng là một yếu tố giảm throughput từ 250 tới 25kbps.

#### 3.8.2.5. Nền tảng hiện thực bộ giao thức mạng Zigbee

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

### 3.8.3. Bộ giao thức WiFi 802.11

#### 3.8.3.1. Kiến trúc mạng WiFi 802.11

Mạng không dây theo chuẩn kết nối 802.11 có thể hoạt động theo kiến trúc dựa theo hạ tầng mạng (infrastructure-based) hoặc kiến trúc không hạ tầng, kết nối không dây trực tiếp giữa các thiết bị với nhau (ad-hoc).

Kiến trúc mạng theo hạ tầng bao gồm các thành phần: thiết bị đầu cuối (station - STA), thiết bị điểm truy cập (access point - AP). Các thiết bị đầu cuối kết nối với một điểm truy cập cùng một tần số tạo nên một tập dịch vụ cơ bản (Basic Service Set - BSS). Hình 3.20 minh họa kiến trúc mạng 802.11 dựa trên kiến trúc hạ tầng.

**Hình 3.20.** Minh họa mạng 802.11 theo kiến trúc hạ tầng

Kiến trúc không dựa theo hạ tầng (adhoc-based) là kiến trúc mạng mà các thiết bị không dây đầu cuối kết nối trực tiếp với nhau, truyền dữ liệu trực tiếp cho nhau mà không cần thông qua một hạ tầng mạng phân phối. Các thiết bị đầu cuối này kết nối lại với nhau tạo thành một nhóm dịch vụ cơ bản độc lập (IBSS), trao đổi dữ liệu trên cùng tần số radio. Hình 3.21 minh họa hai nhóm dịch vụ cơ bản kết nối theo mô hình mạng Ad-hoc (adhoc network).

**Hình 3.21.** Minh họa mạng 802.11 theo kiến trúc ad-hoc

#### 3.8.3.2. Mô hình phân lớp tầng giao thức trong chuẩn không dây 802.11

**Hình 3.22.** Ánh xạ 802.11 trong mô hình OSI

Chuẩn IEEE 802.11 được xây dựng cho mạng cục bộ không dây bao gồm hai tầng con là tầng PHY và tầng MAC trong mô hình OSI. Tầng LLC (Logic Link Control) được mô tả trong chuẩn 802.2. Với các tầng mức cao hơn, kiến trúc phân tầng cung cấp một giao diện trong suốt (nghĩa là không có sự thay đổi đối với các ứng dụng mức cao hơn). Vì vậy, với các tầng từ LLC trở lên có thể hoán chuyển các trạm đang hoạt động mạng WLAN với các mạng cục bộ khác. Hình 3.22 mô tả kiến trúc của WLAN trong mô hình OSI. Điều này cho phép giao thức TCP/IP hiện tại có thể hoạt động dựa trên mạng IEEE 802.11 WLAN giống như hoạt động triển khai trên một mạng có dây Ethernet.

Hình 3.23 mô tả sự khác biệt về các chuẩn hoạt động dựa trên chuẩn 802 WLAN ở tầng PHY và tầng MAC.

Trong Hình 3.23, ở tầng PHY sẽ gồm các tuỳ chọn phát sóng: InfraRed (IR), Frequency Hopping Spread Spectrum (FHSS) và Direct Sequence Spread Spectrum (DSSS). Tất cả các tuỳ chọn ban đầu đều hỗ trợ tốc độ 1 và 2Mbps. Năm 1999, tổ chức IEEE định nghĩa ra hai chuẩn tốc độ cao mở rộng tương ứng với hai chuẩn 802.11b (hoạt động ở băng tần 2.4GHz, tốc độ 11Mbps) và chuẩn 802.11a (hoạt động ở băng tần 5GHz, tốc độ lên đến 54Mbps, dựa trên công nghệ Orthogonal Frequency Division Multiplexing - OFDM). Gần đây, chuẩn 802.11g được đưa ra. Đây là một chuẩn mở rộng của chuẩn 802.11b trong đó hỗ trợ tốc độ truyền lên đến 54Mbps và vẫn hoạt động ở băng tần 2.4GHz.

**Hình 3.23.** Các giao thức sử dụng trong hệ thống mạng cục bộ không dây dựa trên chuẩn IEEE 802.11 của tầng vật lý (PHY layer) và tầng điều khiển truy cập môi trường truyền (MAC layer)

#### 3.8.3.3. Cấu trúc frame của chuẩn không dây 802.11

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

#### 3.8.3.4. Một số chuẩn con của 802.11

**802.11b**
IEEE đã mở rộng trên chuẩn 802.11 gốc vào tháng 7 năm 1999, đó chính là chuẩn 802.11b. Chuẩn này hỗ trợ băng thông lên đến 11Mbps, tương đương với Ethernet truyền thống. 802.11b sử dụng tần số vô tuyến (2.4GHz) giống như chuẩn ban đầu.

Các hãng sản xuất thích sử dụng tần số 2.4GHz này để chi phí sản xuất của họ được giảm. Các thiết bị 802.11b có thể bị xuyên nhiễu từ các thiết bị điện thoại không dây (kéo dài), lò vi sóng hoặc các thiết bị khác sử dụng cùng dải tần 2.4GHz. Mặc dù vậy, bằng cách cài đặt các thiết bị 802.11b cách xa các thiết bị như vậy có thể giảm được hiện tượng xuyên nhiễu này.

**Ưu điểm của 802.11b:** Giá thành rẻ; phạm vi tín hiệu tốt và không dễ bị che khuất.
**Nhược điểm của 802.11b:** Tốc độ tối đa thấp nhất; các thiết bị trong gia đình có thể làm xuyên nhiễu với băng tần này.

**802.11a**
Trong khi 802.11b vẫn đang được phát triển, IEEE đã tạo một mở rộng thứ cấp cho chuẩn 802.11 có tên gọi 802.11a. Vì 802.11b được sử dụng rộng rãi quá nhanh so với 802.11a, nên một số người cho rằng 802.11a được tạo sau 802.11b. Tuy nhiên trong thực tế, 802.11a và 802.11b được tạo một cách đồng thời. Do giá thành cao hơn nên 802.11a chỉ được sử dụng trong các mạng doanh nghiệp còn 802.11b thích hợp hơn với thị trường mạng gia đình.

802.11a hỗ trợ băng thông lên đến 54Mbps và sử dụng tần số vô tuyến 5GHz. Tần số của 802.11a cao hơn so với 802.11b, chính vì vậy đã làm cho phạm vi của hệ thống này hẹp hơn so với các mạng 802.11b. Với tần số này, các tín hiệu 802.11a khó xuyên qua các vách tường và các vật cản khác hơn.

Do 802.11a và 802.11b sử dụng các tần số khác nhau nên hai công nghệ này không thể tương thích với nhau. Chính vì vậy, một số hãng đã cung cấp các thiết bị mạng hybrid cho 802.11a/b nhưng các sản phẩm này chỉ đơn thuần là bổ sung thêm hai chuẩn này.

**Ưu điểm của 802.11a:** Tốc độ cao; tần số 5GHz tránh được sự xuyên nhiễu từ các thiết bị khác.
**Nhược điểm của 802.11a:** Giá thành đắt; phạm vi hẹp và dễ bị che khuất.

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

So với 802.11n, 802.11ac có độ rộng kênh truyền lớn hơn (80 hoặc 160MHz so với 40MHz) trong dải băng tần 5GHz, nhiều luồng không gian hơn (8 so với 4) và điều chế bậc cao hơn (256-QAM so với 64-QAM) và bổ sung tính năng Multi User - Multi Input Multi Output (MU-MIMO). Tính năng này cho phép các điểm truy cập phát nhiều chùm tia đến từng máy trạm. Từ đó, giảm thiểu được việc đụng độ giữa các máy trạm và tăng thông lượng tổng thể.

Liên minh WiFi đã tách việc phát triển 802.11ac thành hai pha, được đặt tên là Wave 1 và Wave 2. Các sản phẩm 802.11ac Wave 1 được sản xuất từ năm 2013 và đến năm 2016 các sản phẩm Wave 2 được đưa ra thị trường nhằm bổ sung các tính năng mới của 802.11ac như băng thông cao hơn, MU-MIMO, độ rộng kênh 160MHz, hỗ trợ nhiều kênh tại băng tần 5GHz, tăng luồng (4 anten so với 3 anten của 802.11ac Wave 1).

**Ưu điểm của 802.11ac:** So với các chuẩn trước, 802.11ac sử dụng băng tần kép 2.4GHz và 5GHz nên tốc độ truyền cao hơn, ít nhiễu hơn.
**Nhược điểm của 802.11ac:** Do sử dụng băng tần 5GHz nên mức suy hao tín hiệu cao hơn so với 2.4GHz khi qua vật cản.

**802.11ax**
Chuẩn 802.11ax được kế thừa từ 802.11ac, và được IEEE chuẩn hóa vào tháng 9 năm 2020, còn được gọi là WiFi 6. Mục tiêu của 802.11ax là cung cấp thông lượng lên gấp 4 lần so với 802.11ac ở mức người dùng, trong khi tốc độ dữ liệu chỉ tăng 37% ở mức vật lý. 802.11ax sử dụng kỹ thuật ghép kênh OFDMA, mỗi máy trạm được sử dụng các đơn vị tài nguyên khác nhau trong phạm vi khả dụng của điểm truy cập. 802.11ax cung cấp nhiều sóng mang hơn so với 802.11ac, cụ thể ở 802.11ax các kênh 20, 40, 80, và 160MHz có lần lượt 256, 512, 1024, và 2048 sóng mang con so với 64, 128, 256 và 512 sóng mang con trong 802.11ac.

**Ưu điểm của 802.11ax:** Tốc độ truyền cao hơn 40% so với 802.11ac, tối ưu cho nhiều người dùng trong cùng một thời điểm.

Nhược điểm của 802.11ax do mới được chuẩn hóa nên thiết bị phát sóng và thiết bị đầu cuối hỗ trợ 802.11ax chưa có nhiều ngoài thị trường.

#### 3.8.3.5. Nền tảng hiện thực bộ giao thức mạng WiFi

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

## 3.9. Cảm biến trong IoT (IoT Sensors) (*Cảm biến IoT*)
- Definition (*Định nghĩa*)
    - A sensor is a device (typically electronic)
    that detects events or changes in its
    physical environment (e.g., temperature,
    sound, heat, pressure, flow, magnetism,
    motion, chemical and biochemical
    parameters) and provides a corresponding
    output. (*Một thiết bị (thường là thiết bị điện tử) phát hiện các sự kiện hoặc thay đổi trong môi trường vật lý của nó (ví dụ: nhiệt độ, âm thanh, nhiệt, áp suất, dòng chảy, từ tính, chuyển động, các thông số hóa học và sinh hóa) và cung cấp một đầu ra tương ứng.*)
    - Most sensors take analog inputs and
    deliver digital, often electrical, outputs. (*Hầu hết các cảm biến nhận đầu vào analog và cung cấp đầu ra kỹ thuật số, thường là điện.*)
- Why Sensors?
    - As we mentioned above, a sensor’s main purpose is collecting data from its surrounding
    enviroment and providing output to its adjoining devices (e.g., gateways, actuators) or
    applications. (*Mục đích chính của cảm biến là thu thập dữ liệu từ môi trường xung quanh và cung cấp đầu ra cho các thiết bị liền kề (ví dụ: cổng, bộ truyền động) hoặc ứng dụng.*
    - Sensors typically collect data using physical interfaces (inputs) that sense the environment
    and then convert input signals into electrical signals (outputs) that are understood by the
    communication and computing devices. Output signals are then processed by the gateways
    and/or by applications of the IoT Platform. (*Cảm biến thường thu thập dữ liệu bằng giao diện vật lý (đầu vào) để cảm nhận môi trường và sau đó chuyển đổi tín hiệu đầu vào thành tín hiệu điện (đầu ra) được hiểu bởi các thiết bị truyền thông và tính toán. Tín hiệu đầu ra sau đó được xử lý bởi các cổng và/hoặc bởi các ứng dụng của Nền tảng IoT.*)
- Sensor Types
    - Temperature Sensors: Temperature is perhaps the most commonly measured
    conservational quantity. This is anticipated since most physical, electronic, chemical,
    mechanical, and biological systems are affected by temperature. (*Cảm biến nhiệt độ: Nhiệt độ có lẽ là đại lượng bảo tồn được đo nhiều nhất. Điều này được dự đoán vì hầu hết các hệ thống vật lý, điện tử, hóa học, cơ học và sinh học đều bị ảnh hưởng bởi nhiệt độ.*)
    - Pressure Sensors: Pressure sensors are used to measure the pressure of gases or
    liquids including water level, flow, speed, and altitude. Practical examples include
    sensors for pumps and compressors, hydraulic systems, and refrigerators. (*Cảm biến áp suất: Cảm biến áp suất được sử dụng để đo áp suất của khí hoặc chất lỏng bao gồm mực nước, lưu lượng, tốc độ và độ cao. Các ví dụ thực tế bao gồm cảm biến cho máy bơm và máy nén, hệ thống thủy lực và tủ lạnh.*)
    - Flow Sensors: Flow sensors are used to detect and record the rate of fluid flow in a
    pipe or a system. They are also used to measure the flow/transfer of heat caused by
    the moving medium. Sensing and measuring the flow are critical for many
    applications ranging from bereave machine to more serious applications such as flow
    monitoring for high-purity acids. (*Cảm biến lưu lượng: Cảm biến lưu lượng được sử dụng để phát hiện và ghi lại tốc độ dòng chảy của chất lỏng trong ống hoặc hệ thống. Chúng cũng được sử dụng để đo lưu lượng/truyền nhiệt do môi trường di chuyển. Cảm biến và đo lưu lượng là rất quan trọng đối với nhiều ứng dụng, từ máy móc đơn giản đến các ứng dụng nghiêm túc hơn như theo dõi lưu lượng axit có độ tinh khiết cao.*)
    - Level Sensors: Level sensors are used to measure the level of fluids continuously or
    at point values. The element to be measured can be inside a container or can be in its
    natural form such as a well in an oil rig. (*Cảm biến mức: Cảm biến mức được sử dụng để đo mức chất lỏng liên tục hoặc tại các giá trị điểm. Phần tử cần đo có thể nằm bên trong một vật chứa hoặc có thể ở dạng tự nhiên như giếng khoan dầu.*)
    - Imaging Sensors: Imaging sensors are sophisticated sensors used in digital cameras,
    medical imaging machines, and night vision equipment. They are utilized to measure
    image information by capturing and then converting variable attenuation of waves into
    signals. (*Cảm biến hình ảnh: Cảm biến hình ảnh là các cảm biến tinh vi được sử dụng trong máy ảnh kỹ thuật số, máy chụp ảnh y tế và thiết bị nhìn đêm. Chúng được sử dụng để đo thông tin hình ảnh bằng cách chụp và sau đó chuyển đổi sự suy giảm khác nhau của sóng thành tín hiệu.*)
    - Noise Sensors: High noise can have damaging effects on humans (e.g., cardiovascular) as well as animals (e.g., hearing loss). Such noise is often caused by machines, airplanes, trains, construction, and loud music especially in closed spaces. (*Cảm biến tiếng ồn: Tiếng ồn cao có thể gây hại cho con người (ví dụ: tim mạch) cũng như động vật (ví dụ: mất thính lực). Tiếng ồn như vậy thường do máy móc, máy bay, tàu hỏa, công trình xây dựng và âm nhạc lớn đặc biệt là trong không gian kín gây ra.*)
    - Air Pollution Sensors: Many governments have established agencies to monitor and
    control the air quality in major cities. For instance, the USA has established the EPA
    (Environmental Protection Agency), in 1970, with a mission to protect Americans
    from significant health risks by providing accurate environmental information to its
    citizens. (*Cảm biến ô nhiễm không khí: Nhiều chính phủ đã thành lập các cơ quan để giám sát và kiểm soát chất lượng không khí ở các thành phố lớn. Ví dụ, Hoa Kỳ đã thành lập Cơ quan Bảo vệ Môi trường (EPA) vào năm 1970 với nhiệm vụ bảo vệ người Mỹ khỏi các rủi ro sức khỏe đáng kể bằng cách cung cấp thông tin môi trường chính xác cho công dân của mình.*)
    - Infrared Sensors: Infrared sensors are used to track an object’s movement. They
    produce and receive infrared waves in the form of heat. (*Cảm biến hồng ngoại: Cảm biến hồng ngoại được sử dụng để theo dõi chuyển động của vật thể. Chúng tạo ra và nhận sóng hồng ngoại dưới dạng nhiệt.*)
    - Moisture and Humidity Sensors: Moisture and humidity sensors (sometimes
    referred to as hygrometer sensors) are used to measure and report the relative
    humidity in the air. They use capacitive measurement by relying on electrical
    capacitance. (*Cảm biến độ ẩm: Cảm biến độ ẩm (đôi khi được gọi là cảm biến ẩm kế) được sử dụng để đo và báo cáo độ ẩm tương đối trong không khí. Chúng sử dụng phép đo điện dung bằng cách dựa vào điện dung.*)
    - Speed Sensors: Speed sensors are commonly used to detect the speed of transport
    vehicles. Examples include wheel speed sensors, speedometers, Doppler radar, and
    laser surface velocimeter. (*Cảm biến tốc độ: Cảm biến tốc độ được sử dụng phổ biến để phát hiện tốc độ của phương tiện giao thông. Ví dụ bao gồm cảm biến tốc độ bánh xe, đồng hồ tốc độ, radar Doppler và máy đo vận tốc bề mặt laser.*)
## 3.10. RFID
- Another way of capturing information from “Things” is through the use of RFID (radio-frequency identification). RFID is not a sensor but a mechanism to capture information pre-embedded into the so-called Tag of a thing or an object using radio waves. (*Một cách khác để thu thập thông tin từ “Vật” là thông qua RFID (nhận dạng tần số vô tuyến). RFID không phải là một cảm biến mà là một cơ chế để thu thập thông tin được nhúng sẵn vào Thẻ của một vật hoặc đối tượng bằng sóng vô tuyến.*)
- RFID consists of two parts: a tag and a reader. Further, the tag has two parts: a microchip that stores and processes information and an antenna to receive and transmit a signal. The tag contains the specific serial number for one specific object. The reader reads the information encoded on a tag, using a two-way radio transmitterreceiver, by emitting a signal to the tag using an antenna. (*RFID bao gồm hai phần: thẻ và đầu đọc. Hơn nữa, thẻ có hai phần: một vi mạch lưu trữ và xử lý thông tin và một ăng-ten để nhận và truyền tín hiệu. Thẻ chứa số sê-ri cụ thể cho một đối tượng cụ thể. Đầu đọc đọc thông tin được mã hóa trên thẻ, sử dụng máy thu phát sóng vô tuyến hai chiều, bằng cách phát tín hiệu đến thẻ bằng ăng-ten.*)
- An RFID-based solution has some advantages over older reader-tag-based solutions, such as barcode, including:
 (*Giải pháp dựa trên RFID có một số ưu điểm so với các giải pháp cũ dựa trên đầu đọc-thẻ, chẳng hạn như mã vạch, bao gồm: *)
    - RFID tag does not need to be within direct line of sight of the reader and can be read from a distance up to 12 m for passive ultrahigh frequency (UHF) system. Battery-powered tags typically have a reading range of 100 m. (*Thẻ RFID không cần phải nằm trong tầm nhìn thẳng với đầu đọc và có thể được đọc từ khoảng cách lên tới 12 m đối với hệ thống tần số siêu cao (UHF) thụ động. Các thẻ chạy bằng pin thường có phạm vi đọc 100 m.*)
    - RFID data on the tag can be modified based on business needs. The barcode data is very difficult to change once deployed. (*Dữ liệu RFID trên thẻ có thể được sửa đổi dựa trên nhu cầu kinh doanh. Dữ liệu mã vạch rất khó thay đổi sau khi triển khai.*)
    - RFID tags are durable. Barcodes, in comparison, are printed on a product for everyone to see. They can be damaged or changed. RFID tags are hidden and may be reused across multiple products. Also RFID tags are capable of storing much more data. (*Thẻ RFID bền. Ngược lại, mã vạch được in trên sản phẩm để mọi người có thể nhìn thấy. Chúng có thể bị hỏng hoặc thay đổi. Thẻ RFID được ẩn và có thể được tái sử dụng trên nhiều sản phẩm. Ngoài ra, thẻ RFID có khả năng lưu trữ nhiều dữ liệu hơn.*)
    - RFID data may be encrypted on the tag, thereby preventing unauthorized users from changing the data or counterfeiting. (*Dữ liệu RFID có thể được mã hóa trên thẻ, do đó ngăn chặn người dùng trái phép thay đổi dữ liệu hoặc làm hàng giả.*)
    - RFID systems can read hundreds of tags simultaneously. This is significant in a retail store as it saves the staff valuable time that they can spend on higher value tasks. (*Hệ thống RFID có thể đọc hàng trăm thẻ đồng thời. Điều này rất quan trọng trong một cửa hàng bán lẻ vì nó tiết kiệm thời gian quý báu của nhân viên mà họ có thể dành cho các nhiệm vụ có giá trị cao hơn.*)
    - The RFID main components: a programmable RFID tag for storing data, a reader with an antenna to read the tags, and an application software hosted on a computer to analyze the data. (*Các thành phần chính của RFID: thẻ RFID có thể lập trình để lưu trữ dữ liệu, đầu đọc có ăng-ten để đọc thẻ và phần mềm ứng dụng được lưu trữ trên máy tính để phân tích dữ liệu.*)
## 3.11. Giám sát bằng video (Video Tracking) 
- Video tracking is the process of capturing and analyzing the video feeds, frame by frame, of a particular object or person over a short time interval. It is used to measure and analyze movements, visual attention, as well as behavior. Video tracking is used for customer identification, surveillance, augmented reality, traffic control, and medical imaging. (*Theo dõi video là quá trình thu thập và phân tích các luồng video, từng khung hình, của một đối tượng hoặc cá nhân cụ thể trong khoảng thời gian ngắn. Nó được sử dụng để đo lường và phân tích chuyển động, sự chú ý thị giác, cũng như hành vi. Theo dõi video được sử dụng để nhận dạng khách hàng, giám sát, thực tế tăng cường, kiểm soát giao thông và hình ảnh y tế.*)
- It is yet another mechanism to identify and monitor “things” when sensors or RFID tags are not available. Video tracking may also be used in conjunction with sensors and/or RFID to provide a more comprehensive solution. (*Nó là một cơ chế khác để xác định và giám sát “vật” khi cảm biến hoặc thẻ RFID không có sẵn. Theo dõi video cũng có thể được sử dụng kết hợp với cảm biến và/hoặc RFID để cung cấp một giải pháp toàn diện hơn.*)
## 3.12. Cơ cấu chấp hành trong IoT (IoT Actuators)
-  An actuator is a type of motor that is responsible for controlling or taking action in a system. It takes a source of data or energy (e.g., hydraulic fluid pressure, other sources of power) and converts the data/energy to motion to control a system. (*Actuator là một loại động cơ chịu trách nhiệm kiểm soát hoặc thực hiện hành động trong một hệ thống. Nó lấy một nguồn dữ liệu hoặc năng lượng (ví dụ: áp suất chất lỏng thủy lực, các nguồn năng lượng khác) và chuyển đổi dữ liệu/năng lượng đó thành chuyển động để điều khiển một hệ thống.*)
- Mechanical Linear Actuators: Mechanical actuators convert rotary motion to linear motion. Devices such as screws and chains are utilized in this conversion. The simplest example of mechanical liner actuators is referred to as the “screw” where leadscrew, screw jack, ball screw, and roller screw actuators all operate on the same principle by rotating the actuator’s nut, the screw shaft moves in a line. (*Actuator tuyến tính cơ khí: Actuator cơ khí chuyển đổi chuyển động quay thành chuyển động thẳng. Các thiết bị như vít và xích được sử dụng trong chuyển đổi này. Ví dụ đơn giản nhất của actuator tuyến tính cơ khí được gọi là “vít” trong đó các actuator vít dẫn hướng, kích vít, vít bi và vít con lăn đều hoạt động theo cùng một nguyên tắc bằng cách xoay đai ốc của actuator, trục vít di chuyển theo một đường thẳng.*)
- Hydraulic Actuators: Hydraulic actuators are simple devices with mechanical parts that are used on linear or quarter-turn valves. They are designed based on Pascal’s Law: when there is an increase in pressure at any point in a confined incompressible fluid, then there is an equal increase at every point in the container. (*Actuator thủy lực: Actuator thủy lực là các thiết bị đơn giản với các bộ phận cơ khí được sử dụng trên các van tuyến tính hoặc van góc phần tư. Chúng được thiết kế dựa trên Định luật Pascal: khi có sự tăng áp suất tại bất kỳ điểm nào trong chất lỏng nén không thể nén được, thì có sự tăng áp suất tương ứng tại mọi điểm trong bình.*)
- Pneumatic Actuators: Pneumatic actuators work on the same concept as hydraulic actuators except compressed gas is used instead of liquid. (*Actuator khí nén: Actuator khí nén hoạt động dựa trên cùng một khái niệm như actuator thủy lực ngoại trừ việc sử dụng khí nén thay vì chất lỏng.*)

## Bài tập Chương 3

1. Hãy liệt kê những kiến trúc mạng trong IoT và đưa ra ưu, nhược điểm của mỗi kiến trúc.
2. Hãy so sánh các bộ giao thức không dây được sử dụng trong IoT và liệt kê các ứng dụng cho từng bộ giao thức.
3. Hãy sử dụng kiến trúc Zigbee để xây dựng ứng dụng Giám sát chất lượng không khí.
4. Hãy sử dụng kiến trúc WLAN 802.11 để xây dựng ứng dụng Nhà thông minh.
5. Hãy thiết kế kiến trúc mạng cho ứng dụng Nông nghiệp thông minh áp dụng tại Việt Nam. Sau đó hãy chọn bộ giao thức mạng phù hợp với ứng dụng này và giải thích vì sao.
6. Hãy thiết kế kiến trúc mạng cho ứng dụng giám sát chất lượng không khí tại Thành phố Hồ Chí Minh. Sau đó hãy chọn bộ giao thức mạng phù hợp với ứng dụng này và giải thích vì sao.
7. Hãy trình bày ý tưởng cho ứng dụng giám sát giao thông thông minh sử dụng công nghệ 5G.

# Chương 4: Các nền tảng phần cứng và phần mềm IoT thông dụng

## Nội dung chương

- **4.1.** Mạng cảm biến không dây (Wireless Sensor Networks - WSN)
- **4.2.** Phân loại mạng cảm biến không dây (Class of Wireless Sensor Networks)
- **4.3.** Vai trò của mã nguồn mở trong IoT (The Role of Open Source in IoT)
- **4.4.** Các nền tảng phần cứng (Hardware Platforms)
- **4.5.** Các nền tảng phần mềm (Software Platforms)
- **4.6.** Ngôn ngữ lập trình Arduino (Arduino Programming Language)

---

## 4.1. Wireless Sensor Networks (WSN)
*(Mạng cảm biến không dây)*

- **Wireless sensor networks (WSN)**, as the name suggests, is a networking paradigm that makes use of spatially distributed sensors for gathering information concerning the immediate environment of the sensors and collecting the information centrally.
(*Mạng cảm biến không dây (WSN), đúng như tên gọi của nó, là một mô hình mạng sử dụng các cảm biến phân bố rải rác trong không gian để thu thập thông tin liên quan đến môi trường xung quanh trực tiếp của các cảm biến và tập hợp thông tin về một vị trí trung tâm.*)
- Here, the sensors are not standalone devices but a combination of sensors, processors, and radio units—referred to as **sensor nodes**—sensing the environment and communicating the sensed data wirelessly to a remote location, which may or may not be connected to a backbone network.
(*Ở đây, các cảm biến không phải là các thiết bị độc lập mà là sự kết hợp của cảm biến, bộ xử lý và khối thu phát vô tuyến—được gọi là các **nút cảm biến (sensor nodes)**—làm nhiệm vụ cảm nhận môi trường và truyền dữ liệu cảm biến được qua đường truyền không dây đến một vị trí từ xa, nơi có thể có hoặc không kết nối với mạng xương sống (backbone network).* )

### Các đặc tính nổi bật của WSN (WSNs Distinguishing Features)

WSNs must have the following distinguishing features:
(*WSN phải có các đặc tính nổi bật sau:*)

- **Fault Tolerance:** The occurrence of faults in WSN nodes should not take down the whole WSN implementation, or hamper the transmission of data from non-faulty nodes to the central location.
(*Khả năng chịu lỗi: Sự xuất hiện sự cố/lỗi tại các nút WSN không được làm sập toàn bộ hệ thống triển khai WSN, hoặc cản trở việc truyền dữ liệu từ các nút không bị lỗi về vị trí trung tâm.*)
- **Scalability:** WSN implementations must have the feature of scalability associated with their architectures and deployments. In the event of a future increase or decrease of sensor node units, the WSN must support the scaling of the infrastructure without changing the whole implementation.
(*Khả năng mở rộng: Việc triển khai WSN phải có tính năng mở rộng gắn liền với kiến trúc và cách bố trí triển khai của chúng. Trong trường hợp số lượng đơn vị nút cảm biến tăng hoặc giảm trong tương lai, WSN phải hỗ trợ việc co giãn quy mô hạ tầng mà không cần phải thay đổi toàn bộ hệ thống.*)
- **Long Lifetime:** The lifetime or the energy replenishment cycle of WSNs must be long enough to make large-scale applications feasible. WSNs have been used for monitoring remote, harsh, and hard to access environments; in these environments, it is not feasible to regularly replenish the energy source of the WSN nodes, which necessitates the need for long node lifetimes.
(*Tuổi thọ hoạt động lâu dài: Vòng đời hoạt động hoặc chu kỳ tái nạp năng lượng của WSN phải đủ dài để các ứng dụng quy mô lớn có tính khả thi. WSN từng được sử dụng để giám sát các môi trường xa xôi, khắc nghiệt và khó tiếp cận; trong các môi trường này, việc thường xuyên thay thế hay nạp lại nguồn năng lượng cho các nút WSN là không khả thi, do đó đòi hỏi các nút phải có tuổi thọ cao.*)
- **Security:** The security of WSNs, if not considered, can easily compromise the security of the whole system, right back to the central server. As WSNs are used for a wide range of applications, some of which are crucial, security is one aspect that must be properly addressed to prevent intrusion and maintain the integrity of the data.
(*Tính bảo mật: Bảo mật của WSN nếu không được chú trọng có thể dễ dàng làm tổn hại đến tính bảo mật của toàn bộ hệ thống, ảnh hưởng trực tiếp đến tận máy chủ trung tâm. Vì WSN được sử dụng cho nhiều ứng dụng đa dạng, trong đó có một số ứng dụng đặc biệt quan trọng, nên bảo mật là một khía cạnh cần được giải quyết thỏa đáng để ngăn chặn sự xâm nhập và duy trì tính toàn vẹn của dữ liệu.*)
- **Programmability:** The programmability of WSNs is important as it ensures the robustness of these systems. WSNs deployed in one application area can be reused for other applications just as easily with a change in sensors and the backend programs associated with it. Programmability also helps in providing a means of adjusting the parameters of the system in the event of a scale-up or scale-down operation.
(*Khả năng lập trình: Khả năng lập trình của WSN rất quan trọng vì nó đảm bảo tính linh hoạt và độ tin cậy của các hệ thống này. WSN được triển khai trong một lĩnh vực ứng dụng có thể được tái sử dụng cho các ứng dụng khác một cách dễ dàng chỉ bằng cách thay đổi cảm biến và các chương trình phần mềm liên quan ở phía backend. Khả năng lập trình cũng giúp cung cấp phương tiện để điều chỉnh các tham số của hệ thống khi mở rộng hoặc thu hẹp quy mô hoạt động.*)
- **Affordability:** As WSNs generally require multiple units, typically in the range of tens or hundreds of WSN nodes, the cost of the nodes and its affordability is vastly responsible for the acceptability of the system. Except for some specialized domains such as the military and the industry, where the sensing requirements are quite high and that too in harsh and challenging conditions, the majority of WSN applications are regular. To some extent, the cost of WSN deployments in these regular domains decide the acceptability of a WSN-based solution for that domain.
(*Giá cả phải chăng / Khả năng chi trả: Vì WSN thường yêu cầu nhiều đơn vị, điển hình từ vài chục đến hàng trăm nút WSN, nên chi phí của các nút và khả năng chi trả quyết định phần lớn đến mức độ được chấp nhận của hệ thống. Ngoại trừ một số lĩnh vực chuyên biệt như quân sự và công nghiệp, nơi các yêu cầu cảm biến rất cao và phải hoạt động trong điều kiện khắc nghiệt, phần lớn các ứng dụng WSN thuộc dạng thông thường. Ở một mức độ nhất định, chi phí triển khai WSN trong các lĩnh vực thông thường này sẽ quyết định việc giải pháp dựa trên WSN có được đón nhận hay không.*)
- **Heterogeneity:** The WSNs must support a wide number and various types of sensors and solutions, thus enabling heterogeneity. In the absence of heterogeneity, the WSN will tend to become very application-specific, which in turn would require major customizations even in the event of minor changes to the network or architecture.
(*Tính không đồng nhất / Đa dạng chủng loại: WSN phải hỗ trợ số lượng lớn và nhiều loại cảm biến cùng các giải pháp khác nhau, nhờ đó mang lại tính không đồng nhất. Nếu thiếu tính không đồng nhất, WSN sẽ có xu hướng trở nên quá chuyên biệt cho một ứng dụng cụ thể, điều này đòi hỏi phải tùy biến chỉnh sửa lớn ngay cả khi có những thay đổi nhỏ trong mạng hoặc kiến trúc.*)
- **Mobility:** WSNs must support the notion of mobility of nodes such that the nodes may be easily relocatable or mobile. Mobility would ensure the rapid deployability of WSN-based solutions in all environments types.
(*Tính di động: WSN phải hỗ trợ khái niệm về tính di động của các nút để các nút có thể dễ dàng di chuyển hoặc đổi vị trí. Tính di động sẽ đảm bảo khả năng triển khai nhanh chóng các giải pháp dựa trên WSN trong mọi loại môi trường.*)

---

## 4.2. Class of Wireless Sensor Networks
*(Phân loại mạng cảm biến không dây)*

### Lĩnh vực ứng dụng (Applications of WSN)

- **Military Applications:** WSNs are used for the detection of enemy soldiers, vehicles, intrusion, weapon systems, and armaments.
(*Ứng dụng quân sự: WSN được sử dụng để phát hiện binh lính đối phương, phương tiện, sự xâm nhập, các hệ thống vũ khí và khí tài.*)
- **Health Applications:** WSNs in healthcare are being used to monitor patients in hospitals, ambulances, and homes. Nowadays, a new class of healthcare devices—wearable appliances—enable a user to have a miniature health sensor on them without additional discomfort.
(*Ứng dụng y tế: WSN trong chăm sóc sức khỏe đang được sử dụng để theo dõi bệnh nhân trong bệnh viện, xe cứu thương và tại nhà. Ngày nay, một nhóm thiết bị y tế mới—các thiết bị đeo—cho phép người dùng mang theo cảm biến sức khỏe thu nhỏ trên người mà không cảm thấy khó chịu.*)
- **Environmental Applications:** WSNs are used for environmental monitoring of pollution, tracking of wildlife, forests, and others.
(*Ứng dụng môi trường: WSN được sử dụng để giám sát môi trường về ô nhiễm, theo dõi động vật hoang dã, rừng cây và các yếu tố khác.*)
- **Home Applications:** WSNs in the home have given rise to home automation systems and smart home connectivity systems.
(*Ứng dụng gia đình: WSN trong gia đình đã thúc đẩy sự ra đời của các hệ thống tự động hóa nhà ở và hệ thống kết nối nhà thông minh.*)
- **Commercial Applications:** WSNs are used for tracking of vehicles, packages in transport, logistics, and others.
(*Ứng dụng thương mại: WSN được sử dụng để theo dõi phương tiện, các kiện hàng trong quá trình vận chuyển, hậu cần (logistics) và các lĩnh vực khác.*)
- **Industrial Monitoring:** WSNs in industries keep track of various industrial processes, monitor factory floors, ensure worker safety, and perform stock management.
(*Giám sát công nghiệp: WSN trong các ngành công nghiệp theo dõi các quy trình công nghiệp khác nhau, giám sát sàn nhà máy, đảm bảo an toàn cho công nhân và thực hiện quản lý kho bãi.*)

### Các miền triển khai WSN (Domains of Implementation)

WSNs can be organized broadly into the following domains of implementation:
(*WSN có thể được phân loại khái quát thành các miền triển khai sau:*)

- **Wireless Multimedia Sensor Networks (WMSN):** This class of WSNs boasts of the ability to retrieve videos, audios, images, or all three in addition to regular scalar sensor readings. The sensing range and coverage area of a camera-based WMSN are defined by the field of view (FOV) of the constituent cameras. Because of their superlative capabilities, WMSNs are popularly sought after in critical domains such as surveillance and road traffic monitoring. However, due to the use of multimedia sensors, the power and processing requirements of this class of WSNs are very high as compared to the other classes of WSNs. Additionally, WMSNs typically demand high network bandwidths for convenient operation.
(*Mạng cảm biến đa phương tiện không dây (WMSN): Nhóm WSN này nổi bật với khả năng thu thập video, âm thanh, hình ảnh hoặc cả ba bên cạnh các giá trị đo cảm biến vô hướng thông thường. Phạm vi cảm nhận và vùng phủ sóng của WMSN dựa trên camera được xác định bởi trường nhìn (FOV) của các camera cấu thành. Do có khả năng vượt trội, WMSN rất được ưa chuộng trong các lĩnh vực quan trọng như giám sát an ninh và theo dõi giao thông đường bộ. Tuy nhiên, do sử dụng các cảm biến đa phương tiện, nhu cầu về năng lượng và xử lý của nhóm WSN này rất cao so với các nhóm WSN khác. Ngoài ra, WMSN thường đòi hỏi băng thông mạng cao để hoạt động thuận tiện.*)
- **Underwater Sensor Networks (UWSN):** This class of WSN is designed specifically to work in underwater environments. Compared to terrestrial or aerial environments, wireless underwater communications are severely restricted in terms of data rate, range, and bandwidth due to the high underwater attenuation of electromagnetic signals. The reliable use of light-based underwater communication is also limited in terms of range and noise. The most accepted global means of underwater communication is by acoustic waves. However, the long propagation delays and uneven data rate makes it necessary to develop newer topologies and architectures, which can work under the conditions of severe limitations of the physical layer.
(*Mạng cảm biến dưới nước (UWSN): Nhóm WSN này được thiết kế chuyên biệt để hoạt động trong môi trường dưới nước. So với môi trường trên cạn hoặc trên không, truyền thông không dây dưới nước bị hạn chế nghiêm ngặt về tốc độ dữ liệu, cự ly và băng thông do sự suy hao cao của tín hiệu điện từ dưới nước. Việc sử dụng đáng tin cậy truyền thông quang học dưới nước cũng bị giới hạn về cự ly và nhiễu. Phương tiện truyền thông dưới nước được chấp nhận rộng rãi nhất trên toàn cầu là sóng âm (acoustic waves). Tuy nhiên, độ trễ lan truyền lớn và tốc độ dữ liệu không đồng đều đòi hỏi phải phát triển các cấu trúc mạng (topologies) và kiến trúc mới hơn, có khả năng hoạt động trong điều kiện hạn chế nghiêm ngặt của tầng vật lý.*)
- **Wireless Underground Sensor Networks (WUSN):** This class of WSNs is designed to be deployed entirely underground. The underground environment poses challenges of attenuation due to the rocks and minerals in the soil. Another significant problem associated with this class is the need for digging up of the nodes to replenish their energy sources. Typical usage scenarios of this class of WSNs are underground mines and monitoring of underground plumbing systems. WUSNs need denser deployment architectures owing to the limited range of wireless communication in underground environments.
(*Mạng cảm biến ngầm không dây (WUSN): Nhóm WSN này được thiết kế để triển khai hoàn toàn dưới lòng đất. Môi trường ngầm đặt ra các thách thức về suy hao tín hiệu do đất đá và khoáng chất trong đất. Một vấn đề đáng kể khác liên quan đến nhóm này là nhu cầu phải đào các nút lên để nạp lại nguồn năng lượng. Các kịch bản sử dụng điển hình của nhóm WSN này là hầm mỏ ngầm và giám sát hệ thống đường ống dẫn nước dưới lòng đất. WUSN cần các kiến trúc triển khai dày đặc hơn do phạm vi truyền thông không dây bị giới hạn trong môi trường ngầm.*)
- **Wireless Mobile Sensor Networks (MSN):** This class of WSNs is characterized by its mobility and low power requirements. The sensor nodes are mobile, which requires them to rapidly connect to networks, disconnect from them, and then again connect to new networks until the nodes are mobile. Typical examples of MSNs include smartphone networks, wearables, vehicular networks, and others.
(*Mạng cảm biến di động không dây (MSN): Nhóm WSN này có đặc trưng là tính di động và yêu cầu tiêu thụ năng lượng thấp. Các nút cảm biến có tính di động, đòi hỏi chúng phải kết nối nhanh chóng vào mạng, ngắt kết nối và sau đó lại kết nối vào mạng mới khi các nút di chuyển. Các ví dụ điển hình của MSN bao gồm mạng điện thoại thông minh, thiết bị đeo, mạng phương tiện giao thông (vehicular networks) và các hệ thống khác.*)

---

## 4.3. The Role of Open Source in IoT
*(Vai trò của mã nguồn mở trong IoT)*

### Phong trào mã nguồn mở (The Open Source Movement)

Open source in the computer industry is the publishing of source code or hardware design, with associated licensing that permits the reuse, modification, improvement, and potential commercialization under favorable terms.
(*Mã nguồn mở trong ngành công nghiệp máy tính là việc công bố mã nguồn hoặc thiết kế phần cứng, đi kèm với giấy phép liên quan cho phép tái sử dụng, sửa đổi, cải tiến và có tiềm năng thương mại hóa theo các điều khoản thuận lợi.*)

Example of favorable distribution terms includes the following criteria:
(*Ví dụ về các điều khoản phân phối thuận lợi bao gồm các tiêu chí sau:*)

- **Free Distribution:** Any party may sell or give away the open-source component as part of a larger system without being obligated to pay a royalty or other fee for such sale.
(*Phân phối miễn phí: Bất kỳ bên nào cũng có thể bán hoặc tặng thành phần mã nguồn mở như một phần của hệ thống lớn hơn mà không có nghĩa vụ phải trả tiền bản quyền hoặc phí khác cho việc bán đó.*)
- **Source Code/Design:** The source code or design must be distributed and made publicly available.
(*Mã nguồn/Thiết kế: Mã nguồn hoặc bản thiết kế phải được phân phối và cung cấp công khai.*)
- **Derived Works:** Derivation and modification of the original open-source component are allowed under the original licensing terms.
(*Tác phẩm phái sinh: Việc phát triển tác phẩm phái sinh và sửa đổi thành phần nguồn mở ban đầu được cho phép theo các điều khoản cấp phép gốc.*)

> While any system can potentially be released under an open source license by its owner, successful open source projects have associated communities of interest that are integral to their success.
> (*Mặc dù bất kỳ hệ thống nào cũng có khả năng được chủ sở hữu phát hành theo giấy phép mã nguồn mở, nhưng các dự án mã nguồn mở thành công đều gắn liền với các cộng đồng có cùng mối quan tâm—yếu tố không thể thiếu đối với sự thành công của chúng.*)

---

## 4.4. Các nền tảng phần cứng (Hardware Platforms)

### Thiết bị nhúng Arduino

- Board mạch Arduino đa dạng từ đơn giản tới những sản phẩm phục vụ thiết bị có thể mang theo tới các máy in 3D... Nhiều nhà nghiên cứu, sinh viên thực hiện các dự án với Arduino và cung cấp nhiều hướng dẫn, hỗ trợ online.
- Một số dòng thiết bị nổi tiếng như **Arduino Yún**, board Wi-Fi (IEEE 802.11 b/g/n) và Ethernet (IEEE 802.3 10/100Mb/s).
- Board này sử dụng ATmega32, xung clock 16MHz; board này có 1 khe micro-SD, 1 port USB, 7 chân PWM pin, 12 analog input và 1 cổng micro USB.

### GizmoSphere

- **GizmoSphere** is an open source development platform for the embedded design community; the site includes code downloads and hardware schematics along with free user guides, specification sheets, and other documentation.
(*GizmoSphere là một nền tảng phát triển mã nguồn mở dành cho cộng đồng thiết kế nhúng; trang web bao gồm việc tải xuống mã nguồn và sơ đồ phần cứng cùng với sách hướng dẫn sử dụng miễn phí, bảng thông số kỹ thuật và các tài liệu khác.*)

### Tinkerforge

- **Tinkerforge** is a system of open source stackable microcontroller building blocks. It allows the control of motors and reading out sensors with the following programming languages: C, C++, C#, Object Pascal, Java, PHP, Python, and Ruby over a USB or Wi-Fi connection on Windows, Linux, and Mac OS X.
(*Tinkerforge là một hệ thống các khối vi điều khiển mã nguồn mở có thể xếp chồng lên nhau dạng mô-đun. Nó cho phép điều khiển động cơ và đọc giá trị cảm biến bằng các ngôn ngữ lập trình sau: C, C++, C#, Object Pascal, Java, PHP, Python và Ruby qua kết nối USB hoặc Wi-Fi trên Windows, Linux và Mac OS X.*)
- All of the hardware is licensed under **CERN OHL** (CERN Open Hardware License).
(*Tất cả phần cứng đều được cấp phép theo CERN OHL (Giấy phép Phần cứng Mở CERN).* )

### BeagleBoard / BeagleBone

- **BeagleBoard** offers credit-card sized computers that can run Android and Linux.
(*BeagleBoard cung cấp các máy tính nhỏ gọn có kích thước bằng thẻ tín dụng có thể chạy hệ điều hành Android và Linux.*)
- Because they have very low-power requirements, they are a good option for IoT devices.
(*Vì chúng có yêu cầu tiêu thụ năng lượng rất thấp, chúng là một lựa chọn tốt cho các thiết bị IoT.*)
- Both the hardware designs and the software they run are open source, and BeagleBoard hardware (often sold under the name **BeagleBone**) is available through a wide variety of distributors.
(*Cả thiết kế phần cứng và phần mềm chúng chạy đều là mã nguồn mở, và phần cứng BeagleBoard (thường được bán dưới tên BeagleBone) có sẵn thông qua nhiều nhà phân phối khác nhau.*)

### Raspberry Pi

- As of 2020, the **Raspberry Pi** is the most used edge device for building IoT solutions among the DIY and maker communities.
(*Tính đến năm 2020, Raspberry Pi là thiết bị biên được sử dụng phổ biến nhất để xây dựng các giải pháp IoT trong cộng đồng DIY và các nhà sáng chế (maker).* )
- The affordable price and accessibility made it extremely popular.
(*Giá cả phải chăng và khả năng tiếp cận dễ dàng đã khiến nó trở nên cực kỳ phổ biến.*)
- The computing and storage capabilities of the Raspberry Pi enables people to use it as an edge device within the IoT projects they are building *(ví dụ: Raspberry Pi B+, Raspberry Pi Zero...)*.
(*Khả năng tính toán và lưu trữ của Raspberry Pi cho phép mọi người sử dụng nó như một thiết bị biên trong các dự án IoT mà họ đang xây dựng (ví dụ: Raspberry Pi B+, Raspberry Pi Zero...).*)

### Kiến trúc ngăn xếp IoT và thiết bị biên (The Internet of Things Stack & Edge Devices)

- Based on Figure, we notice that the sensors and actuators are placed at the bottom of the stack, as they are the ones communicating directly with the environment.
(*Dựa trên hình vẽ, chúng ta nhận thấy rằng các cảm biến và cơ cấu chấp hành được đặt ở dưới cùng của ngăn xếp, vì chúng là những thành phần giao tiếp trực tiếp với môi trường.*)
- Up the stack, we place the local processing and storage devices, also called **edge devices**.
(*Phía trên ngăn xếp, chúng ta đặt các thiết bị lưu trữ và xử lý cục bộ, còn được gọi là các **thiết bị biên (edge devices)**.*)
- These are computers such as a Raspberry Pi, which are capable of exchanging information with the peripherals and have minimal computing capabilities so they can preprocess the data received from the sensors.
(*Đây là các máy tính chẳng hạn như Raspberry Pi, có khả năng trao đổi thông tin với các thiết bị ngoại vi và có khả năng tính toán tối thiểu để chúng có thể tiền xử lý dữ liệu nhận được từ các cảm biến.*)

### NVIDIA Jetson Nano

- The **Nvidia Jetson Nano** was announced as a development system in mid-March of 2019. This product is intended for Internet of Things (IoT) makers.
(*Nvidia Jetson Nano được công bố như một hệ thống phát triển vào giữa tháng 3 năm 2019. Sản phẩm này hướng tới các nhà sáng chế Internet vạn vật (IoT).* )
- The board consists of a CPU with 1.43 GHz and a GPU with 128 cores of the Maxwell generation *(phiên bản: NVIDIA Jetson Nano A02, B01)*.
(*Bo mạch bao gồm CPU xung nhịp 1.43 GHz và GPU với 128 lõi thuộc thế hệ kiến trúc Maxwell (phiên bản: NVIDIA Jetson Nano A02, B01).* )

### ESP8266

- **ESP8266** is a Wi-Fi SoC (system on a chip) produced by Espressif Systems. It is a highly integrated chip designed to provide full Internet connectivity in a small package *(ví dụ: ESP8266-01, ESP8266-03, Olimex ESP8266)*.
(*ESP8266 là một SoC (hệ thống trên một vi mạch) Wi-Fi do Espressif Systems sản xuất. Đây là một con chip tích hợp cao được thiết kế để cung cấp khả năng kết nối Internet toàn diện trong một kích thước nhỏ gọn (ví dụ: ESP8266-01, ESP8266-03, Olimex ESP8266).* )
- ESP8266 can be used as an external Wi-Fi module, using the standard AT Command set Firmware by connecting it to any microcontroller using the serial UART, or directly serve as a Wi-Fi-enabled microcontroller, by programming a new firmware using the provided SDK.
(*ESP8266 có thể được sử dụng như một mô-đun Wi-Fi gắn ngoài sử dụng Firmware tập lệnh AT tiêu chuẩn bằng cách kết nối với bất kỳ vi điều khiển nào qua cổng nối tiếp UART, hoặc trực tiếp đóng vai trò như một vi điều khiển hỗ trợ Wi-Fi bằng cách nạp firmware mới sử dụng bộ SDK được cung cấp.*)

### ESP32

- **ESP32** is a low-cost System on Chip (SoC) Microcontroller from Espressif Systems, the developers of the famous ESP8266 SoC *(ví dụ: ESP32 DevKit board)*.
(*ESP32 là vi điều khiển Hệ thống trên vi mạch (SoC) chi phí thấp từ Espressif Systems, nhà phát triển dòng SoC ESP8266 nổi tiếng (ví dụ: board ESP32 DevKit).* )
- It is a successor to ESP8266 SoC and comes in both single-core and dual-core variations of the Tensilica’s 32-bit Xtensa LX6 Microprocessor with integrated Wi-Fi and Bluetooth.
(*Đây là sản phẩm kế thừa của SoC ESP8266 và có cả hai phiên bản đơn nhân và đa nhân của bộ vi xử lý 32-bit Tensilica Xtensa LX6 tích hợp sẵn Wi-Fi và Bluetooth.*)

### Nền tảng Zerynth & Thiết bị đeo (Wearables + IoT)

- **The Zerynth IoT Platform:** A full set of hardware-software tools designed by IoT experts to enable an easy transition from the prototyping phase to mass production in a flexible, scalable, and efficient way.
(*Nền tảng Zerynth IoT: Một bộ công cụ phần cứng - phần mềm hoàn chỉnh được thiết kế bởi các chuyên gia IoT nhằm cho phép chuyển đổi dễ dàng từ giai đoạn tạo mẫu thử nghiệm sang sản xuất hàng loạt một cách linh hoạt, có thể mở rộng và hiệu quả.*)
- **Zerynth OS:** An operating system designed to simplify the development process. It features a Python/C Development environment and seamless integration with other hardware vendors.
(*Hệ điều hành Zerynth: Một hệ điều hành được thiết kế để đơn giản hóa quá trình phát triển. Nó cung cấp môi trường phát triển Python/C và tích hợp liền mạch với các nhà cung cấp phần cứng khác.*)
- **Zerynth Cloud:** Makes it possible to manage IoT devices, store data, visualize data, and gain insights from a single interface.
(*Zerynth Cloud: Giúp quản lý các thiết bị IoT, lưu trữ dữ liệu, trực quan hóa dữ liệu và thu nhận thông tin chi tiết chuyên sâu từ một giao diện duy nhất.*)
- **Dự án thực tế - Smartwatch hỗ trợ bệnh nhân Alzheimer:**
  - Alzheimer's is an extremely destructive disease that destroys the very essence of oneself by degrading memory and thinking abilities. Because 1 in 9 people aged 65 and above suffer from it, Abdullah Sadiq decided to build an assistive smartwatch that displays basic reminders, shows the time, monitors the wearer's location, and can even alert caretakers in the event of an emergency.
  (*Bệnh Alzheimer là một căn bệnh tàn phá cực kỳ nghiêm trọng làm suy giảm bản chất con người do làm suy giảm trí nhớ và khả năng tư duy. Do cứ 9 người từ 65 tuổi trở lên thì có 1 người mắc bệnh, Abdullah Sadiq đã quyết định chế tạo một chiếc smartwatch hỗ trợ hiển thị các lời nhắc cơ bản, xem giờ, theo dõi vị trí người đeo và thậm chí có thể cảnh báo người chăm sóc trong trường hợp khẩn cấp.*)
  - It works by using an Infineon Sensor Hub in conjunction with an Arduino MKR1000 board to read sensor information and send it to either a smartphone or to an IoT platform.
  (*Nó hoạt động bằng cách sử dụng bộ tập trung cảm biến Infineon Sensor Hub kết hợp với bo mạch Arduino MKR1000 để đọc thông tin cảm biến và gửi đến điện thoại thông minh hoặc nền tảng IoT.*)

### Thiết bị thực tế ảo mã nguồn mở (Open Source VR Headset)

- Probably the most advanced project in this list, the **Relativity device** is an open source VR headset that supports SteamVR and even body-tracking through the use of a neural network that estimates 3D positions.
(*Có lẽ là dự án tiên tiến nhất trong danh sách này, thiết bị Relativity là một kính thực tế ảo (VR) mã nguồn mở hỗ trợ SteamVR và thậm chí hỗ trợ theo dõi chuyển động cơ thể thông qua việc sử dụng mạng nơ-ron để ước tính vị trí không gian 3D.*)
- The headset was made possible thanks to its dual 2K displays that can output images at 120 fps.
(*Kính đeo này khả thi nhờ màn hình 2K kép có thể xuất hình ảnh ở tốc độ 120 khung hình/giây.*)
- All of the computational horsepower comes from an Microchip SAM3X8E Cortex-M3 processor mounted to a custom PCB along with an MPU-6050 IMU for motion tracking.
(*Toàn bộ sức mạnh tính toán đến từ bộ xử lý Microchip SAM3X8E Cortex-M3 được gắn trên một bo mạch PCB tùy chỉnh cùng với cảm biến quán tính IMU MPU-6050 để theo dõi chuyển động.*)

---

## 4.5. Các nền tảng phần mềm (Software Platforms)

### Giao thức MQTT

- **Tổng quan:** MQTT được thiết kế chủ yếu để kết nối các thiết bị bị hạn chế tài nguyên/nguồn trên băng thông thấp. Mặc dù đã tồn tại trong hơn một thập kỷ nhưng chỉ khi có sự ra đời của M2M và IoT mới làm cho MQTT trở thành một giao thức phổ biến.
- **Định nghĩa:** MQTT (Message Queuing Telemetry Transport) là một giao thức truyền thông điệp (message) theo mô hình **publish/subscribe** (xuất bản – theo dõi), sử dụng băng thông thấp, độ tin cậy cao và có khả năng hoạt động trong điều kiện đường truyền không ổn định.
- **Các thành phần chính của MQTT:**
  - Client
  - Broker
  - Topic
  - Message
  - Publish
  - Subscribe
  - Connection
- **Nguyên lý hoạt động:**
  - Giống như bất kỳ giao thức Internet nào khác, MQTT dựa trên các client và một máy chủ. Tương tự như vậy, máy chủ (**broker**) là bên chịu trách nhiệm xử lý các yêu cầu của client về việc nhận hoặc gửi dữ liệu giữa client và server với nhau.
  - *Ví dụ minh họa:* Giả sử có một thiết bị gắn cảm biến nhiệt độ. Nó sẽ gửi dữ liệu đọc được cho broker. Ở phía bên kia, ứng dụng của điện thoại hoặc PC nhận được giá trị của nhiệt độ này:
    - Thiết bị xác định chủ đề (**topic**) mà nó muốn xuất bản (**publish**), ví dụ `"temp"`. Sau đó, nó xuất bản thông báo *"giá trị nhiệt độ"*.
    - Ứng dụng điện thoại/máy tính PC đăng ký (**subscribe**) chủ đề `"temp"`. Sau đó, nó nhận được thông báo rằng thiết bị đã xuất bản, đó là giá trị nhiệt độ.

### Mosquitto Broker

- Có nhiều broker triển khai giao thức MQTT. Một trong những broker phổ biến nhất và thường được sử dụng là **Mosquitto broker**.
- Mosquitto là một broker thông điệp nguồn mở thực hiện giao thức MQTT. Nó gọn nhẹ và phù hợp để sử dụng trên tất cả các thiết bị từ một bo mạch đơn giản như Arduino, ESP8266 và ESP32 đến máy tính và máy chủ đầy đủ.
- Nhưng thay vì sử dụng Mosquitto trên máy tính cục bộ, chúng ta sẽ cần phải sử dụng một máy chủ dựa trên đám mây để triển khai broker Mosquitto. Điều đó là cần thiết để làm cho các dự án IoT có thể kiểm soát được trên Internet.
- *Các Cloud Mosquitto Broker phổ biến:* ThingMQ, ThingStudio, MQTT.io, Heroku, CloudMQTT.

### Nền tảng Blynk

- **Định nghĩa:** Blynk là một nền tảng với các ứng dụng iOS và Android để điều khiển Arduino, Raspberry Pi và các ứng dụng tương tự qua Internet.
- Blynk là một bảng điều khiển kỹ thuật số nhờ đó bạn có thể xây dựng giao diện đồ họa cho dự án của mình bằng cách kéo và thả các widget.
- Blynk không bị ràng buộc với một số board mạch hoặc shield cụ thể. Thay vào đó, nó hỗ trợ phần cứng mà bạn lựa chọn. Cho dù Arduino hoặc Raspberry Pi của bạn được liên kết với Internet qua Wi-Fi, Blynk sẽ giúp bạn online và sẵn sàng cho IoT.

#### Blynk có thể làm được những gì?

- Triển khai một hệ thống nhà thông minh, điều khiển giám sát từ xa, v.v... Giới hạn duy nhất là khả năng cũng như sự sáng tạo của bạn.
- **Các Widget:** Nút ấn, hiển thị giá trị, thanh kéo giá trị, vẽ sơ đồ, v.v... Cho phép điều khiển GPIO của thiết bị bo mạch, từ đó bật tắt relay, điều khiển các thiết bị trong nhà.
- **Ưu điểm:**
  - Điểm mạnh của Blynk là có thể kết nối ở bất kỳ nơi nào có mạng.
  - Có thể chia sẻ bảng điều khiển cho nhiều người dùng để sử dụng chung 1 hệ thống.

#### Điều khiển và giao tiếp thiết bị:

- Thiết bị Arduino chịu trách nhiệm điều khiển các thiết bị trong nhà thông qua relay lắp trực tiếp vào các GPIO của Arduino, hoặc bất kì kiểu giao tiếp nào khác nếu bạn đủ khả năng (RF, UART). Thiết bị này yêu cầu phải kết nối mạng (ESP8266, ESP32, …).
- App Blynk từ điện thoại thông qua đám mây sẽ gửi tín hiệu đến board và ngược lại. Các board Arduino được đánh dấu bằng 1 token (chữ ký số), tạo ra trong quá trình setup ứng dụng.

---

## 4.6. Ngôn ngữ lập trình Arduino (Arduino Programming Language)

> *Chương 6: Arduino Programming Language – A Tour of Open-Source Activities in IoT*
> (*Chương 6: Ngôn ngữ lập trình Arduino – Khám phá các hoạt động mã nguồn mở trong IoT*)

### Điện toán vật lý (What is Physical Computing?)

- Physical Computing uses electronics to prototype new materials for designers and artists.
(*Điện toán vật lý (Physical Computing) sử dụng các linh kiện điện tử để tạo mẫu các chất liệu mới dành cho các nhà thiết kế và nghệ sĩ.*)
- It involves the design of interactive objects that can communicate with humans using sensors and actuators controlled by a behaviour implemented as software running inside a microcontroller (a small computer on a single chip).
(*Nó liên quan đến việc thiết kế các đối tượng tương tác có thể giao tiếp với con người bằng các cảm biến và cơ cấu chấp hành được điều khiển bởi hành vi triển khai dưới dạng phần mềm chạy bên trong vi điều khiển (một máy tính nhỏ tích hợp trên một vi mạch đơn).* )
- In the past, using electronics meant having to deal with engineers all the time, and building circuits one small component at the time; these issues kept creative people from playing around with the medium directly. Most of the tools were meant for engineers and required extensive knowledge. In recent years, microcontrollers have become cheaper and easier to use, allowing the creation of better tools.
(*Trong quá khứ, việc sử dụng đồ điện tử đồng nghĩa với việc lúc nào cũng phải làm việc với các kỹ sư và xây dựng mạch điện với từng linh kiện nhỏ một; những rào cản này đã ngăn những người sáng tạo tiếp cận trực tiếp với phương tiện này. Hầu hết các công cụ đều dành cho kỹ sư và đòi hỏi kiến thức chuyên sâu. Trong những năm gần đây, vi điều khiển đã trở nên rẻ hơn và dễ sử dụng hơn, cho phép tạo ra các công cụ tốt hơn.*)
- The progress that we have made with Arduino is to bring these tools one step closer to the novice, allowing people to start building stuff after only two or three days of a workshop.
(*Tiến bộ mà chúng tôi đạt được với Arduino là mang các công cụ này đến gần hơn một bước với người mới bắt đầu, cho phép mọi người bắt đầu chế tạo các sản phẩm chỉ sau hai hoặc ba ngày tham gia buổi thảo luận thực hành (workshop).* )
- With Arduino, a designer or artist can get to know the basics of electronics and sensors very quickly and can start building prototypes with very little investment.
(*Với Arduino, một nhà thiết kế hoặc nghệ sĩ có thể nhanh chóng nắm bắt các kiến thức cơ bản về điện tử và cảm biến, đồng thời có thể bắt đầu xây dựng các nguyên mẫu thử nghiệm với chi phí đầu tư rất ít.*)

### Triết lý Arduino (The Arduino Way)

- The Arduino philosophy is based on making designs rather than talking about them. It is a constant search for faster and more powerful ways to build better prototypes. We have explored many prototyping techniques and developed ways of thinking with our hands.
(*Triết lý của Arduino dựa trên việc tạo ra các thiết kế thay vì chỉ nói về chúng. Đó là một cuộc tìm kiếm liên tục các phương pháp nhanh hơn và mạnh mẽ hơn để xây dựng các nguyên mẫu tốt hơn. Chúng tôi đã khám phá nhiều kỹ thuật tạo mẫu và phát triển các cách tư duy bằng chính đôi tay của mình.*)
- Classic engineering relies on a strict process for getting from A to B; the Arduino Way delights in the possibility of getting lost on the way and finding C instead.
(*Kỹ thuật truyền thống dựa trên một quy trình nghiêm ngặt để đi từ A đến B; trong khi Triết lý Arduino tìm thấy sự thú vị ở khả năng có thể đi lạc trên đường đi và thay vào đó lại tìm ra điểm C.*)
- This is the tinkering process that we are so fond of—playing with the medium in an open-ended way and finding the unexpected. In this search for ways to build better prototypes, we also selected a number of software packages that enable the process of constant manipulation of the software and hardware medium.
(*Đây chính là quá trình mày mò, thử nghiệm mà chúng tôi rất yêu thích—khám phá môi trường theo hướng mở và tìm thấy những điều bất ngờ ngoài mong đợi. Trong quá trình tìm kiếm các phương thức xây dựng nguyên mẫu tốt hơn, chúng tôi cũng lựa chọn một số gói phần mềm cho phép liên tục tương tác và điều khiển giữa môi trường phần mềm và phần cứng.*)

### Kỹ thuật tạo mẫu nhanh (Prototyping)

- Prototyping is at the heart of the Arduino Way: we make things and build objects that interact with other objects, people, and networks. We strive to find a simpler and faster way to prototype in the cheapest possible way.
(*Tạo mẫu nhanh là trọng tâm của Triết lý Arduino: chúng tôi chế tạo các đồ vật và xây dựng các đối tượng có thể tương tác với các đối tượng khác, con người và mạng lưới. Chúng tôi nỗ lực tìm kiếm một phương pháp đơn giản hơn và nhanh hơn để tạo mẫu với chi phí tiết kiệm nhất có thể.*)
- A lot of beginners approaching electronics for the first time think that they have to learn how to build everything from scratch. This is a waste of energy: what you want is to be able to confirm that something's working very quickly so that you can motivate yourself to take the next step or maybe even motivate somebody else to give you a lot of cash to do it.
(*Nhiều người mới bắt đầu tiếp cận lĩnh vực điện tử lần đầu thường nghĩ rằng họ phải học cách xây dựng mọi thứ từ con số không. Điều này rất lãng phí năng lượng: điều bạn mong muốn là có thể xác nhận một thứ gì đó đang hoạt động thật nhanh chóng để có động lực bước tiếp hoặc thậm chí thuyết phục người khác đầu tư nhiều tiền cho dự án của bạn.*)
- This is why we developed **"opportunistic prototyping"**: why spend time and energy building from scratch, a process that requires time and in-depth technical knowledge, when we can take ready-made devices and hack them in order to exploit the hard work done by large companies and good engineers?
(*Đó là lý do tại sao chúng tôi phát triển phương pháp **"tạo mẫu cơ hội" (opportunistic prototyping)**: tại sao phải tốn thời gian và công sức xây dựng từ đầu—một quá trình đòi hỏi thời gian và kiến thức kỹ thuật chuyên sâu—trong khi chúng ta có thể tận dụng các thiết bị làm sẵn và cải biến (hack) chúng để khai thác thành quả công sức của các công ty lớn và những kỹ sư giỏi?*)

### Nền tảng Arduino (The Arduino Platform)

Arduino is composed of two major parts: the **Arduino board**, which is the piece of hardware you work on when you build your objects; and the **Arduino IDE**, the piece of software you run on your computer.
(*Arduino bao gồm hai phần chính: **board Arduino**, là phần cứng bạn làm việc trực tiếp khi xây dựng các đối tượng; và **Arduino IDE**, là phần mềm bạn chạy trên máy tính của mình.*)

Cấu hình các chân I/O tiêu chuẩn (ví dụ trên Arduino Uno, Duemilanove):

- **14 Digital IO pins (pins 0–13):** These can be inputs or outputs, which is specified by the sketch you create in the IDE.
(*14 chân I/O số (chân 0–13): Các chân này có thể là ngõ vào (input) hoặc ngõ ra (output), được chỉ định bởi bản phác thảo (sketch) bạn tạo trong IDE.*)
- **6 Analogue In pins (pins 0–5):** These dedicated analogue input pins take analogue values (i.e., voltage readings from a sensor) and convert them into a number between 0 and 1023.
(*6 chân ngõ vào Analog (chân 0–5): Các chân ngõ vào analog chuyên dụng này nhận các giá trị analog (tức là số đọc điện áp từ cảm biến) và chuyển đổi chúng thành một số trong khoảng từ 0 đến 1023.*)
- **6 Analogue Out pins (pins 3, 5, 6, 9, 10, and 11):** These are actually six of the digital pins that can be reprogrammed for analogue output using the sketch you create in the IDE.
(*6 chân ngõ ra Analog (chân 3, 5, 6, 9, 10 và 11): Đây thực chất là 6 trong số các chân digital có thể được tái lập trình cho ngõ ra analog (PWM) thông qua bản phác thảo sketch bạn tạo trong IDE.*)

### Phần mềm Arduino (The Software - IDE)

The IDE (Integrated Development Environment) is a special program running on your computer that allows you to write sketches for the Arduino board in a simple language modeled after the [Processing](https://www.processing.org) language.
(*IDE (Môi trường phát triển tích hợp) là một chương trình đặc biệt chạy trên máy tính, cho phép bạn viết các bản phác thảo (sketch) cho board Arduino bằng một ngôn ngữ đơn giản được xây dựng dựa trên ngôn ngữ [Processing](https://www.processing.org).* )

**The programming cycle on Arduino is basically as follows:**
(*Quy trình chu trình lập trình trên Arduino về cơ bản như sau:*)

1. Plug your board into a USB port on your computer.
(*Cắm board của bạn vào cổng USB trên máy tính.*)
2. Write a sketch that will bring the board to life.
(*Viết một đoạn chương trình (sketch) để làm cho board hoạt động.*)
3. Upload this sketch to the board through the USB connection and wait a couple of seconds for the board to restart.
(*Nạp (upload) chương trình sketch này lên board qua kết nối USB và đợi vài giây để board khởi động lại.*)
4. The board executes the sketch that you wrote.
(*Board thực thi chương trình sketch mà bạn đã viết.*)

#### Cài đặt Arduino trên máy tính (Installing Arduino on Your Computer)

- To program the Arduino board, you must first download the development environment (the IDE) from here: [www.arduino.cc/en/Main/Software](https://www.arduino.cc/en/Main/Software). Choose the right version for your operating system.
(*Để lập trình board Arduino, trước tiên bạn phải tải xuống môi trường phát triển (IDE) từ địa chỉ: [www.arduino.cc/en/Main/Software](https://www.arduino.cc/en/Main/Software). Chọn phiên bản phù hợp với hệ điều hành của bạn.*)

### Cấu trúc thiết bị tương tác (Anatomy of an Interactive Device)

- All of the objects we will build using Arduino follow a very simple pattern that we call the **“Interactive Device”**. The Interactive Device is an electronic circuit that is able to sense the environment using sensors (electronic components that convert real-world measurements into electrical signals).
(*Tất cả các đối tượng mà chúng ta xây dựng bằng Arduino đều tuân theo một mô hình rất đơn giản mà chúng tôi gọi là **“Thiết bị tương tác” (Interactive Device)**. Thiết bị tương tác là một mạch điện tử có khả năng cảm nhận môi trường xung quanh bằng các cảm biến (các linh kiện điện tử chuyển đổi các đại lượng đo lường trong thế giới thực thành tín hiệu điện).* )
- The device processes the information it gets from the sensors with behaviour that’s implemented as software. The device will then be able to interact with the world using actuators, electronic components that can convert an electric signal into a physical action.
(*Thiết bị xử lý thông tin nhận được từ các cảm biến bằng hành vi được hiện thực hóa dưới dạng phần mềm. Sau đó, thiết bị sẽ có thể tương tác với thế giới xung quanh bằng các cơ cấu chấp hành (actuators), các linh kiện điện tử có thể chuyển đổi tín hiệu điện thành một hành động vật lý.*)

### Cảm biến và Cơ cấu chấp hành (Sensors and Actuators)

- Sensors and actuators are electronic components that allow a piece of electronics to interact with the world.
(*Cảm biến và cơ cấu chấp hành là các linh kiện điện tử cho phép một thiết bị điện tử tương tác với thế giới bên ngoài.*)
- As the microcontroller is a very simple computer, it can process only electric signals (a bit like the electric pulses that are sent between neurons in our brains). For it to sense light, temperature, or other physical quantities, it needs something that can convert them into electricity.
(*Vì vi điều khiển là một máy tính rất đơn giản, nó chỉ có thể xử lý các tín hiệu điện (tương tự như các xung điện được truyền giữa các tế bào thần kinh trong não chúng ta). Để nó có thể cảm nhận ánh sáng, nhiệt độ hoặc các đại lượng vật lý khác, nó cần một linh kiện có thể chuyển đổi chúng thành điện năng.*)
- In our body, for example, the eye converts light into signals that get sent to the brain using nerves. In electronics, we can use a simple device called a **light-dependent resistor (an LDR or photoresistor)** that can measure the amount of light that hits it and report it as a signal that can be understood by the microcontroller.
(*Trong cơ thể chúng ta, ví dụ, mắt chuyển đổi ánh sáng thành các tín hiệu được truyền đến não thông qua dây thần kinh. Trong điện tử, chúng ta có thể sử dụng một linh kiện đơn giản gọi là **quang điện trở (LDR hoặc photoresistor)** có khả năng đo lượng ánh sáng chiếu vào nó và báo cáo dưới dạng một tín hiệu mà vi điều khiển có thể hiểu được.*)

### Cấu trúc một bản phác thảo (Structure of an Arduino Sketch)

An Arduino sketch runs in two parts:
(*Một bản phác thảo chương trình Arduino (sketch) hoạt động theo hai phần:*)

- `void setup()`: This is where you place the initialisation code—the instructions that set up the board before the main loop of the sketch starts.
(*`void setup()`: Đây là nơi bạn đặt mã khởi tạo—các chỉ lệnh thiết lập cấu hình board trước khi vòng lặp chính của sketch bắt đầu.*)
- `void loop()`: This contains the main code of your sketch. It contains a set of instructions that get repeated over and over until the board is switched off.
(*`void loop()`: Phần này chứa mã chính của sketch. Nó bao gồm một tập hợp các chỉ lệnh được lặp đi lặp lại liên tục cho đến khi tắt nguồn board mạch.*)

```cpp
void setup() {
  // Mã khởi tạo: Chạy 1 lần duy nhất khi khởi động hoặc reset board
}

void loop() {
  // Thân chương trình chính: Lặp lại liên tục cho đến khi tắt nguồn
}
```

### Các ký hiệu đặc biệt (Special Symbols)

Arduino includes a number of symbols to delineate lines of code, comments, and blocks of code.
(*Arduino bao gồm một số ký hiệu để phân định các dòng mã lệnh, chú thích và các khối mã.*)

- **`;` (semicolon):** Every instruction (line of code) is terminated by a semicolon. This syntax lets you format the code freely. You could even put two instructions on the same line, as long as you separate them with a semicolon. (However, this would make the code harder to read.)
(*`;` (dấu chấm phẩy): Mỗi chỉ lệnh (dòng mã) đều được kết thúc bằng một dấu chấm phẩy. Cú pháp này cho phép bạn định dạng code một cách tự do. Bạn thậm chí có thể đặt hai lệnh trên cùng một dòng, miễn là phân tách chúng bằng dấu chấm phẩy. (Tuy nhiên, điều này sẽ khiến mã khó đọc hơn).*)

*Example:*
(*Ví dụ:*)

```cpp
delay(100);
```

- **`//` (single-line comment):** Dùng để ghi chú trên một dòng đơn. Trình biên dịch sẽ bỏ qua tất cả ký tự từ dấu `//` cho đến cuối dòng.
- **`/* ... */` (multi-line comment):** Dùng để ghi chú trên nhiều dòng liên tiếp. Rất hữu ích khi cần giải thích chi tiết khối thuật toán hoặc tạm thời vô hiệu hóa một đoạn mã.
- **`{}` (curly braces):** Cặp dấu ngoặc nhọn dùng để xác định phạm vi của một khối mã lệnh (block of code), ví dụ như thân hàm `setup()`, `loop()`, hoặc khối lệnh sau `if`, `for`, `while`.

#### Các hàm vào/ra cơ bản trong Arduino (Basic I/O Functions)

1. **`pinMode(pin, mode)`:** Cấu hình chân số (digital pin) làm đầu vào (`INPUT`), đầu vào có điện trở kéo lên (`INPUT_PULLUP`), hoặc đầu ra (`OUTPUT`).
2. **`digitalWrite(pin, value)`:** Xuất mức điện áp ra chân số: mức cao `HIGH` (thường là 5V hoặc 3.3V) hoặc mức thấp `LOW` (0V).
3. **`digitalRead(pin)`:** Đọc trạng thái logic từ chân số, trả về `HIGH` hoặc `LOW`.
4. **`analogRead(pin)`:** Đọc giá trị điện áp tương tự từ chân Analog (A0-A5), chuyển đổi qua bộ ADC 10-bit thành giá trị nguyên từ `0` đến `1023`.
5. **`analogWrite(pin, value)`:** Xuất tín hiệu điều chế độ rộng xung (PWM) ra các chân hỗ trợ (~), nhận giá trị từ `0` (luôn tắt) đến `255` (luôn bật).
6. **`delay(ms)`:** Tạm dừng chương trình trong khoảng thời gian xác định tính bằng mili-giây.

#### Giao tiếp nối tiếp qua cổng Serial (Serial Communication)

- **`Serial.begin(speed)`:** Khởi tạo giao tiếp Serial với tốc độ baud (thông dụng: 9600, 115200).
- **`Serial.print()` / `Serial.println()`:** Gửi dữ liệu hoặc chuỗi ký tự lên máy tính để xem trên Serial Monitor.
- **`Serial.available()` / `Serial.read()`:** Kiểm tra và đọc dữ liệu gửi từ máy tính xuống board.

*Ví dụ hoàn chỉnh: Chương trình điều khiển đèn LED chớp tắt (Blink):*

```cpp
// Khai báo hằng số chân cắm LED
const int LED_PIN = 13; // Chân số 13 tích hợp sẵn LED trên board Arduino Uno

void setup() {
  // Cấu hình chân LED_PIN làm ngõ ra (OUTPUT)
  pinMode(LED_PIN, OUTPUT);
  // Khởi động giao tiếp Serial với tốc độ 9600 bps
  Serial.begin(9600);
  Serial.println("Arduino Blink Program Started!");
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // Bật sáng đèn LED
  Serial.println("LED ON");
  delay(1000);                  // Chờ 1 giây (1000 ms)

  digitalWrite(LED_PIN, LOW);  // Tắt đèn LED
  Serial.println("LED OFF");
  delay(1000);                  // Chờ 1 giây
}
```

## 4.7. Thiết bị cảm biến không dây TelosB

TelosB là loại thiết bị cảm biến không dây tiết kiệm năng lượng, được xếp vào loại thiết bị IoT thuộc lớp 0 như đã trình bày ở phần trên. Hình 4.1 là hình ảnh bề ngoài của thiết bị TelosB.

**Hình 4.1.** Mote cảm biến không dây TelosB [6]

Thiết bị TelosB (được phát triển ban đầu bởi UC Berkeley) là một nền tảng phần cứng mã nguồn mở tiêu chuẩn cho các nghiên cứu về mạng cảm biến không dây (WSN):
- **Bộ vi điều khiển:** TI MSP430F1611 16-bit RISC, xung nhịp 8MHz, 10kB RAM, 48kB ROM (Flash) và 1MB bộ nhớ Flash ngoài dùng lưu trữ dữ liệu.
- **Bộ thu phát không dây:** Chip RF Chipcon/TI CC2420 tương thích chuẩn IEEE 802.15.4 / Zigbee, hoạt động ở dải tần 2.4GHz với tốc độ truyền dữ liệu 250kbps, tích hợp ăng-ten onboard.
- **Cảm biến tích hợp:** Tích hợp sẵn cảm biến nhiệt độ và độ ẩm kỹ thuật số Sensirion SHT11, cảm biến ánh sáng nhìn thấy và toàn phổ Hamamatsu.
- **Giao tiếp lập trình:** Cổng USB tích hợp qua chip FTDI cho phép vừa lập trình, gỡ lỗi vừa nạp nguồn và giao tiếp dữ liệu nối tiếp với máy tính.
- **Hệ điều hành hỗ trợ:** TinyOS và Contiki OS.

### 4.1.5. Tổng hợp một số nền tảng phần cứng IoT phổ biến

Bảng 4.1 tóm tắt lại 3 nền tảng phần cứng IoT phổ biến, đặc trưng cho 3 nhóm thiết bị IoT thường được sử dụng trong các giải pháp IoT thực tế từ nghiên cứu đến triển khai ứng dụng thương mại.

**Bảng 4.1.** Tổng hợp 3 nền tảng phần cứng IoT đặc trưng

| Đặc điểm | TelosB Mote | Arduino-based boards | Raspberry Pi |
|:---|:---|:---|:---|
| **Bộ xử lý** | TI MSP430 16-bit @ 8MHz | ATmega328P 8-bit @ 16MHz (hoặc ESP8266/ESP32 32-bit) | Broadcom BCM2837/2711 Quad-core ARM 64-bit @ 1.4 - 1.5GHz |
| **Bộ nhớ** | 10kB RAM, 48kB Flash | 2kB SRAM, 32kB Flash (ESP32: 520kB RAM, 4MB Flash) | 1GB - 8GB LPDDR4 RAM, thẻ nhớ MicroSD ngoài |
| **Kết nối mạng** | IEEE 802.15.4 / Zigbee (2.4GHz, 250kbps) | Cần shield gắn thêm (hoặc tích hợp Wi-Fi/BLE trên ESP) | Gigabit Ethernet, Wi-Fi Dual-band 802.11ac, Bluetooth 5.0 |

| Đặc điểm | TelosB Mote | Arduino-based boards | Raspberry Pi |
|:---|:---|:---|:---|
| **Cảm biến** | Tích hợp sẵn nhiệt độ, độ ẩm, ánh sáng | Kết nối cảm biến ngoài qua chân GPIO, ADC, I2C, SPI | Kết nối cảm biến ngoài qua GPIO, USB, Camera CSI |
| **Phần mềm** | TinyOS, Contiki OS | Arduino IDE, FreeRTOS, MicroPython | Linux (Raspbian OS), Python, Node.js, C/C++, Java |
| **Nguồn điện** | Nguồn pin 2xAA công suất cực thấp | Cổng USB (5V) hoặc DC 7-12V, tiêu thụ thấp | Cổng USB-C (5V - 3A), tiêu thụ công suất 2W - 5W |
| **Vai trò** | Nút cảm biến không dây (Sensor Node) | Thiết bị đo đạc, cơ cấu chấp hành (End Device / Node) | Cổng kết nối (IoT Gateway), máy chủ biên (Edge Server) |

## 4.8.0. Đặc trưng và phân loại hệ điều hành dùng cho thiết bị IoT

Một hệ điều hành dùng cho thiết bị IoT thông thường gồm 3 thành phần chính:
- **Thành phần phần cứng (Hardware) và lớp trừu tượng phần cứng (Hardware Abstraction Layer - HAL):** Bao gồm các cơ chế giao tiếp, điều khiển ngoại vi của thiết bị như GPIO, UART, SPI, I2C, ADC, bộ định thời và chip vô tuyến RF.
- **Thành phần hệ thống (System Services / Kernel):** Bao gồm nhân hệ điều hành (kernel), bộ lập lịch (scheduler), các hiện thực ngăn xếp giao thức mạng (network stack), trình điều khiển thiết bị (device drivers), hệ thống tệp và các thư viện hỗ trợ quản lý bộ nhớ, năng lượng.
- **Thành phần ứng dụng (Application Layer):** Cho phép lập trình viên xây dựng và thực thi các chương trình ứng dụng IoT phục vụ mục tiêu thu thập dữ liệu, xử lý và điều khiển cụ thể.

**Hình 4.4.** Các thành phần chính của một hệ điều hành cho thiết bị IoT [5]

**Phân loại hệ điều hành cho thiết bị IoT**

Tương tự như sự đa dạng của nền tảng phần cứng, các hệ điều hành phát triển cho thiết bị IoT cũng rất đa dạng nhằm phục vụ tốt các ngữ cảnh ứng dụng cụ thể:
- **Event-driven OS (Hệ điều hành hướng sự kiện):** Đây là hướng tiếp cận phổ biến nhất cho các mạng cảm biến không dây tài nguyên rất hạn chế như TinyOS, Contiki. Mọi tác vụ xử lý trên hệ thống được kích hoạt bởi các sự kiện từ bên ngoài (ngắt phần cứng hoặc bộ định thời). Nhân hệ điều hành chỉ chạy một vòng lặp quản lý hàng đợi sự kiện, không cần duy trì ngăn xếp (stack) riêng cho từng tiến trình, giúp tiết kiệm bộ nhớ RAM tối đa và giảm độ phức tạp.
- **Multi-threading OS (Hệ điều hành đa luồng):** Tiếp cận theo mô hình truyền thống của hệ điều hành máy tính, mỗi luồng có ngăn xếp riêng và thực thi độc lập. Bộ lập lịch thực hiện chuyển đổi ngữ cảnh (context switch) giữa các luồng dựa theo độ ưu tiên hoặc phân chia thời gian. Mô hình này lập trình tự nhiên, dễ sử dụng nhưng tiêu tốn bộ nhớ RAM hơn cho các ngăn xếp luồng. Đại diện tiêu biểu gồm RIOT OS, FreeRTOS, NuttX, ChibiOS.
- **Pure RTOSs (Hệ điều hành thời gian thực thuần túy):** Tập trung vào việc đảm bảo tính xác định và thời gian đáp ứng nghiêm ngặt cho các ứng dụng công nghiệp, y tế hoặc xe tự hành. Các đại diện phổ biến là FreeRTOS, RTEMS, VxWorks, QNX.

Trong đó, FreeRTOS là một đại diện mã nguồn mở được dùng rất phổ biến trên các vi điều khiển nhúng 32-bit như STM32 hay ESP32.

Nội dung tiếp theo trong chương này giới thiệu chi tiết một số hệ điều hành tiêu biểu được sử dụng trong các hệ thống IoT: TinyOS, Contiki và Raspbian OS.

## 4.8. Hệ điều hành TinyOS

TinyOS là hệ điều hành mã nguồn mở, hướng sự kiện (event-driven), được thiết kế chuyên biệt cho các thiết bị mạng cảm biến không dây có tài nguyên bộ nhớ rất hạn chế (vi điều khiển 8-bit đến 16-bit, RAM vài kB) [7]. TinyOS được phát triển ban đầu tại Đại học UC Berkeley kết hợp với Intel Research.

Các ứng dụng trên TinyOS được lập trình bằng ngôn ngữ **nesC** (Network Embedded Systems C), một phần mở rộng của ngôn ngữ C hỗ trợ lập trình dựa trên thành phần (component-based) và hướng sự kiện [8]. TinyOS hỗ trợ giao tiếp mạng cảm biến thông qua chồng giao thức mạng BLIP (Berkeley Low-power IP Stack) hiện thực chuẩn 6LoWPAN và RPL.

## 4.8.1. Cấu trúc một ứng dụng trên TinyOS

Một ứng dụng TinyOS bao gồm nhiều thành phần (component) liên kết với nhau thông qua các giao diện (interface) [9]. Kiến trúc nesC phân biệt rõ ràng giữa hai khái niệm:
- **Interface (Giao diện):** Định nghĩa hợp đồng giao tiếp giữa các thành phần, bao gồm các hàm lệnh (**commands**) do bên cung cấp (provider) hiện thực và các sự kiện (**events**) do bên sử dụng (user) hiện thực để xử lý kết quả báo về.
- **Component (Thành phần):** Bao gồm hai loại:
  - **Module:** Chứa mã nguồn thực thi bằng ngôn ngữ nesC (hiện thực các command và event).
  - **Configuration:** Định nghĩa cách nối dây (wiring) giữa các interface của các component với nhau để tạo thành ứng dụng hoàn chỉnh.

**Hình 4.5.** Mô hình hoạt động dựa trên sự kiện của hệ điều hành TinyOS

Mô hình hoạt động của TinyOS dựa trên hai khái niệm xử lý cơ bản:
- **Tasks (Tác vụ):** Đại diện cho các đoạn tính toán dài hạn trong chương trình, được đưa vào hàng đợi FIFO và thực thi tuần tự theo cơ chế không ưu tiên chiếm quyền (non-preemptive). Task không thể chiếm quyền của Task khác nhưng có thể bị ngắt bởi Hardware Event.
- **Hardware Event Handlers (Trình xử lý sự kiện phần cứng):** Được kích hoạt khi có ngắt từ phần cứng (như bộ định thời đếm xong hoặc gói tin truyền thông đến). Các hàm xử lý ngắt thực thi ngay lập tức và có thể chiếm quyền của Task đang chạy để đảm bảo tính thời gian thực.

Một ứng dụng TinyOS viết bằng nesC gồm các tệp thành phần cơ bản [10]:
1. Tệp cấu hình ứng dụng cao nhất (Top-level Configuration, ví dụ `BlinkAppC.nc`).
2. Tệp module hiện thực logic ứng dụng (Module, ví dụ `BlinkC.nc`).
3. Các tệp giao diện (Interfaces, nếu tự định nghĩa mới).
4. Tệp Makefile để biên dịch chương trình.

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

## 4.8.2. Các thành phần, dịch vụ cơ bản của TinyOS

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

**Cấu trúc thông điệp và truyền thông trong TinyOS**

Giao tiếp không dây trong TinyOS xoay quanh kiểu dữ liệu thông điệp cơ bản `message_t`. Định dạng của `message_t` bao gồm 3 phần: tiêu đề (header), vùng dữ liệu tải trọng (payload) và phần chân (footer):

- Kích thước tải trọng tối đa của gói tin mặc định là 28 byte (được định nghĩa qua hằng số `TOSH_DATA_LENGTH = 28`). Lập trình viên có thể cấu hình lại khi biên dịch bằng tùy chọn `-DTOSH_DATA_LENGTH=x` trong Makefile. Nếu một gói tin vượt quá kích thước này, nó sẽ bị loại bỏ.
- Phần header chứa địa chỉ nguồn, địa chỉ đích, độ dài dữ liệu, chỉ số nhóm (group ID) và loại thông điệp Active Message (AM Type).
- Phần footer chứa các trường kiểm tra lỗi CRC và cờ báo nhận (ACK).

TinyOS cung cấp mô hình trừu tượng Active Message (AM) cho phép các ứng dụng phân biệt các luồng dữ liệu khác nhau thông qua trường định danh `am_id_t` (tương tự như số cổng port trong TCP/UDP).

**Hình 4.11.** Mô hình kiến trúc phần cứng của hệ điều hành TinyOS

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

**Ngăn xếp vô tuyến CC2420 (CC2420 Radio Stack)**

Ngăn xếp phần mềm CC2420 chứa nhiều lớp (layer) thành phần được xếp chồng lên nhau nằm giữa ứng dụng và phần cứng thu phát:

**Hình 4.16.** Kiến trúc lớp trong CC2420 Radio Stack

Mỗi lớp trong ngăn xếp cung cấp và sử dụng các giao diện chuẩn (`Send`, `Receive`, `SplitControl`). Các lớp chính bao gồm:
- **ActiveMessageP:** Lớp trên cùng, điền các trường tiêu đề Active Message và tương tác trực tiếp với tầng ứng dụng.
- **UniqueSendLayer:** Tự động tạo và gắn số thứ tự dữ liệu duy nhất (Data Sequence Number - DSN) vào tiêu đề để bên nhận có thể phát hiện và loại bỏ các gói tin bị trùng lặp.
- **PacketLink:** Cung cấp dịch vụ truyền lại tự động (Automatic Retransmission) nếu không nhận được tín hiệu ACK từ nút kế cận.

- **Low Power Listening (LPL):** Hiện thực kỹ thuật lắng nghe năng lượng thấp bất đồng bộ. Nút gửi sẽ phát chuỗi gói tin liên tiếp (preamble packets) để đánh thức nút nhận đang trong chu kỳ ngủ định kỳ, giúp giảm tiêu hao năng lượng tối đa khi mạng nhàn rỗi.
- **UniqueReceive:** Duy trì bảng lịch sử các gói tin gần nhất để lọc bỏ các gói tin trùng lặp nhận được do truyền lại.
- **TinyOSNetworkC:** Cho phép nhận dạng và chuyển tiếp các gói tin chuẩn IEEE 802.15.4 liên mạng (như 6LoWPAN).
- **CSMA/CA:** Quản lý truy cập môi trường truyền không dây, thực hiện thuật toán backoff ngẫu nhiên để tránh va chạm tín hiệu trên kênh.
- **TransmitP / ReceiveP:** Tương tác trực tiếp với phần cứng chip CC2420 thông qua bus SPI, chân ngắt và GPIO.

## 4.9. Hệ điều hành Contiki

Contiki là hệ điều hành mã nguồn mở, gọn nhẹ (lightweight), đa nhiệm được thiết kế chuyên biệt cho các thiết bị mạng cảm biến không dây và Internet of Things có tài nguyên bộ nhớ hạn chế [14]. Contiki được sáng lập bởi Adam Dunkels tại Viện Khoa học Máy tính Thụy Điển (SICS).

Đặc tính nổi bật của Contiki là tính linh hoạt cao, hỗ trợ nạp động (dynamic loading) và thay thế từng chương trình hoặc dịch vụ riêng lẻ trong lúc hệ thống đang chạy. Contiki được xây dựng theo mô hình hướng sự kiện (event-driven) kết hợp với cơ chế tiểu luồng **Protothreads**, mang lại phong cách lập trình tuần tự tuyến tính mà không tốn kém chi phí ngăn xếp luồng độc lập.

## 4.9.1. Cấu trúc một ứng dụng trên Contiki

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

## 4.9.2. Các thành phần, dịch vụ cơ bản trên hệ điều hành Contiki

**Kiến trúc nhân hệ điều hành (Kernel Architecture)**

Nhân Contiki bao gồm một bộ định thời gọn nhẹ và bộ điều phối sự kiện. Hệ thống hỗ trợ hai loại sự kiện:
- **Sự kiện bất đồng bộ (Asynchronous Event):** Sự kiện được đưa vào hàng đợi và được xử lý tuần tự bởi tiến trình đích khi đến lượt.
- **Sự kiện đồng bộ (Synchronous Event):** Kích hoạt tiến trình đích thực thi ngay lập tức (tương tự như một lời gọi hàm trực tiếp), tiến trình gửi sẽ tạm dừng cho đến khi tiến trình đích xử lý xong sự kiện.

**Cơ chế thăm dò (Polling Mechanism):** Là một dạng sự kiện có độ ưu tiên cao, được hệ thống thực thi xen giữa các sự kiện thông thường nhằm kiểm tra nhanh các trạng thái phần cứng và phản hồi các ngắt ngoại vi tức thời.

**Các cơ chế định thời (Timers) trong Contiki**
Contiki cung cấp 4 thư viện định thời đa dạng phục vụ các nhu cầu khác nhau:
- **timer:** Bộ định thời đơn giản, chỉ kiểm tra xem một khoảng thời gian đã trôi qua hay chưa (thăm dò thụ động).
- **etimer (Event Timer):** Tạo ra một sự kiện gửi đến tiến trình khi hết thời gian định trước, giúp tiến trình tự động đánh thức từ trạng thái chờ.
- **ctimer (Callback Timer):** Tự động gọi một hàm callback được chỉ định khi hết thời gian, rất hữu ích cho các giao thức mạng.
- **rtimer (Real-time Timer):** Bộ định thời thời gian thực độ chính xác cao dựa trên ngắt phần cứng, phục vụ các tác vụ đòi hỏi thời gian đáp ứng nghiêm ngặt như điều khiển chu kỳ nhiệm vụ radio.

**Chế độ tiết kiệm năng lượng**
Contiki tự động đưa bộ vi xử lý vào trạng thái nghỉ công suất thấp (Low Power Mode - LPM) mỗi khi hàng đợi sự kiện rỗng. Khi có ngắt phần cứng hoặc bộ định thời kích hoạt, MCU sẽ thức dậy để xử lý và sau đó lại quay về trạng thái ngủ, giúp kéo dài tối đa thời gian hoạt động bằng pin của thiết bị.

**Kiến trúc dịch vụ và nạp động (Dynamic Services)**

Trong Contiki, một dịch vụ (service) là một tiến trình cung cấp các chức năng dùng chung (như giao thức mạng, bộ điều khiển cảm biến) cho các tiến trình khác. Điểm đặc sắc là các dịch vụ có thể được biên dịch độc lập, nạp vào bộ nhớ hoặc gỡ bỏ trong lúc hệ thống đang hoạt động mà không cần khởi động lại bo mạch.

Lớp quản lý dịch vụ (Service Layer) duy trì danh sách các dịch vụ hiện có trong hệ thống và phiên bản tương ứng. Ứng dụng gọi dịch vụ thông qua một thư viện gốc (stub library) để liên kết động với tiến trình dịch vụ tại thời điểm chạy.

**Ngăn xếp truyền thông trong Contiki**

Contiki hỗ trợ hai ngăn xếp mạng mạnh mẽ:
- **uIP / uIPv6:** Ngăn xếp TCP/IP và IPv6 siêu nhỏ gọn tuân thủ chuẩn RFC, hỗ trợ 6LoWPAN, RPL, UDP, TCP, CoAP và MQTT, cho phép nút cảm biến kết nối trực tiếp với Internet toàn cầu.
- **Rime:** Ngăn xếp truyền thông mạng cảm biến nhẹ tùy biến, cung cấp các khối giao tiếp phân tầng từ cơ bản (broadcast, unicast một chặng) đến nâng cao (truyền đa chặng, thu thập dữ liệu cây hop-by-hop) với chi phí bộ nhớ tối thiểu.

**Hệ thống tệp Coffee (Coffee Flash File System)**
Contiki tích hợp sẵn hệ thống tệp Coffee chuyên biệt cho chip nhớ Flash ngoài của các mote cảm biến, cho phép lưu trữ cấu hình và nhật ký dữ liệu cảm biến bền vững với cơ chế san phẳng độ mòn (wear leveling).

**Hình 4.18.** Sơ đồ các cơ chế giao tiếp trên Contiki

## 4.10. Hệ điều hành Raspbian OS

Hệ điều hành Raspbian (hiện nay được đổi tên chính thức là **Raspberry Pi OS**) là hệ điều hành mã nguồn mở miễn phí dựa trên nền tảng bản phân phối Linux Debian, được tối ưu hóa đặc biệt cho dòng máy tính nhúng phần cứng Raspberry Pi [15].

Ban đầu Raspbian được khởi xướng bởi Mike Thompson và Peter Green như một dự án cộng đồng độc lập, sau đó được Raspberry Pi Foundation chính thức bảo trợ và phát triển thành hệ điều hành chính thức. Kho phần mềm của Raspbian cung cấp hơn 35.000 gói ứng dụng (packages) được biên dịch sẵn, đáp ứng đầy đủ từ các nhu cầu học tập, phát triển phần mềm nhúng đến triển khai các dịch vụ máy chủ mạng và IoT Gateway phức tạp.

**Hình 4.19.** Kiến trúc hệ điều hành Raspbian OS

**Kiến trúc và các đặc điểm kỹ thuật của Raspbian OS**
- **Kiến trúc nhân:** Nhân Linux monolithic đầy đủ hỗ trợ đa nhiệm, đa người dùng, bộ nhớ ảo và cơ chế đa luồng ưu tiên chiếm quyền (preemptive multi-threading).
- **Ngôn ngữ phát triển:** Hỗ trợ toàn diện các ngôn ngữ lập trình hiện đại như Python, C, C++, Java, Node.js, PHP, Ruby, Scratch. Thư viện Python (`RPi.GPIO`, `gpiozero`) cho phép lập trình điều khiển các chân phần cứng cực kỳ nhanh chóng và trực quan.
- **Giao thức và kết nối:** Hỗ trợ đầy đủ bộ giao thức TCP/IP tiêu chuẩn, Bluetooth/BLE, Wi-Fi, Ethernet và các chuẩn giao tiếp công nghiệp như MQTT, HTTP/HTTPS, WebSockets, CoAP, Modbus.
- **Công cụ mô phỏng:** Có thể giả lập chạy toàn bộ hệ thống Raspbian trên máy tính thông qua công cụ máy ảo QEMU ARM.
- **Bảo mật:** Cung cấp đầy đủ các cơ chế bảo mật cấp doanh nghiệp của Linux như xác thực người dùng SSH, tường lửa iptables/ufw, mã hóa OpenSSL, VPN và phân quyền truy cập tệp.

- **Hỗ trợ đa phương tiện mạnh mẽ:** Tận dụng bộ tăng tốc đồ họa phần cứng VideoCore GPU tích hợp trên bo mạch Raspberry Pi, Raspbian hỗ trợ hiển thị giao diện đồ họa mượt mà (môi trường máy tính để bàn PIXEL / LXDE), xử lý video độ phân giải cao 1080p và 4K, hỗ trợ các chuẩn OpenMAX, OpenGL ES, OpenVG và các thư viện thị giác máy tính như OpenCV. Hệ điều hành cũng hỗ trợ truyền phát âm thanh/hình ảnh thời gian thực qua các giao thức VoIP như SIP và RTP.
- **Mức tiêu thụ năng lượng:** Mặc dù tiêu thụ nhiều năng lượng hơn so với các vi điều khiển cấp thấp, một bo mạch Raspberry Pi chạy Raspbian chỉ tiêu thụ công suất trung bình từ 1.5W đến 5W (tùy thuộc vào tác vụ và tải CPU), hoàn toàn có thể chạy bằng nguồn sạc dự phòng di động hoặc hệ thống pin năng lượng mặt trời cho các trạm giám sát thông minh ngoài trời.

Nhờ những ưu điểm vượt trội trên, Raspberry Pi chạy Raspbian thường đóng vai trò là **Edge Gateway** hoặc **Edge Computing Node** trong kiến trúc IoT hiện đại, chịu trách nhiệm thu thập dữ liệu từ các mạng cảm biến cục bộ (qua Zigbee, LoRa, BLE), thực hiện tiền xử lý, nén dữ liệu, chạy các mô hình AI/Machine Learning suy luận nhẹ tại biên và chuyển tiếp dữ liệu lên đám mây.

## 4.11. Bảng tổng hợp so sánh các hệ điều hành IoT phổ biến

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

Thông qua phần tổng hợp từ hai bảng, Bảng 4.2 và Bảng 4.3 ta thấy hiện nay có rất nhiều nền tảng phần mềm, hệ điều hành hỗ trợ phát triển các giải pháp IoT với nhiều đặc trưng, đặc tính kỹ thuật khác nhau. Chính vì thế, tùy theo nhu cầu sử dụng, tùy theo tính năng, yêu cầu của giải pháp IoT muốn phát triển mà các nhà phát triển hệ thống có thể chọn lựa cho mình một môi trường phù hợp. Ví dụ, trong môi trường nghiên cứu học thuật ở nhiều trường đại học trên thế giới, khi nghiên cứu về mạng cảm biến không dây, thiết bị IoT tiết kiệm năng lượng, tài nguyên hạn chế thì các hệ điều hành như TinyOS, Contiki thường được lựa chọn. Ngoài ra, một nền tảng khá phổ biến và dễ dàng tiếp cận hiện nay đó là máy tính nhúng Raspberry Pi với hệ điều hành Raspbian. Đây là một thiết bị nhúng hỗ trợ khá đầy đủ chức năng của một máy tính thu nhỏ, cho phép người lập trình sử dụng những tiện ích của ngôn ngữ lập trình bậc cao như Python, Node.js, Java... để phát triển các ứng dụng của mình một cách tiện lợi. Tóm lại, với sự phát triển không ngừng của công nghệ, lần lượt ngày càng nhiều nền tảng phần cứng được sản xuất chế tạo, kèm theo đó là các giải pháp phần mềm cũng được tạo ra, mang đến sự đa dạng chủng loại và nhiều sự lựa chọn cho người học, người phát triển giải pháp IoT với nhiều cấp độ, nhiều cách tiếp cận khác nhau.

## Bài tập Chương 4

1. Hãy so sánh các nhóm phần cứng dùng trong IoT và liệt kê các thiết bị thuộc mỗi nhóm.
2. Hãy trình bày kiến trúc và hoạt động của một chương trình nesC trên TinyOS.
3. Hãy trình bày kiến trúc và hoạt động của một chương trình C trên Contiki OS.
4. Hãy liệt kê các loại phần cứng, phần mềm và các cảm biến (nếu có) để xây dựng một ứng dụng giám sát chất lượng không khí.
5. Từ nền tảng Arduino và Raspberry Pi 3, hãy thiết kế ứng dụng giám sát môi trường và điều khiển thiết bị cho nhà thông minh.

6. Từ nền tảng CC2530, hãy thiết kế ứng dụng Nông nghiệp thông minh.
7. Hãy xác định loại phần cứng, phần mềm, cảm biến để xây dựng hệ thống cảnh báo cháy rừng có các nút cảm biến được cấp nguồn bằng pin với yêu cầu tối ưu năng lượng sử dụng để thời gian hoạt động của ứng dụng là lớn nhất.

# Chương 5: Điện toán đám mây, điện toán cận biên và IoT

## Nội dung chương

- **5.1.** Kiến trúc tổng quan hệ thống IoT tích hợp điện toán đám mây và điện toán cận biên.
- **5.2.** Nền tảng điện toán đám mây và ứng dụng trong IoT (Mô hình dịch vụ, OpenStack và Docker).
- **5.3.** Nền tảng điện toán cận biên (Edge Computing) và ứng dụng trong IoT.
- **5.4.** Các vấn đề tồn tại và hướng nghiên cứu trong tương lai.
- **Bài tập Chương 5.**


Vạn vật kết nối Internet mở ra nhiều thách thức không chỉ với việc thiết kế phần cứng và phần mềm cho các thiết bị IoT mà còn đặt ra những bài toán hóc búa về hạ tầng xử lý, lưu trữ và phân tích dữ liệu khổng lồ sinh ra từ hàng triệu nút cảm biến. Sự bùng nổ của các ứng dụng IoT thời gian thực như xe tự hành, thành phố thông minh, giám sát y tế khẩn cấp đòi hỏi năng lực tính toán cực lớn cùng với độ trễ phản hồi tính bằng mili-giây.

Để giải quyết bài toán này, sự kết hợp giữa **Điện toán đám mây (Cloud Computing)** và **Điện toán cận biên (Edge Computing / Fog Computing)** đã trở thành mô hình kiến trúc chuẩn mực. Điện toán đám mây cung cấp nguồn tài nguyên lưu trữ và tính toán vô hạn ở trung tâm dữ liệu, trong khi điện toán cận biên đưa khả năng tính toán và ra quyết định đến gần nơi sinh ra dữ liệu nhất (tại các gateway, router hoặc trạm gốc kế cận thiết bị IoT).

Nội dung chương này trình bày kiến trúc tích hợp giữa IoT, điện toán đám mây và điện toán cận biên; phân tích các mô hình dịch vụ đám mây (IaaS, PaaS, SaaS) và ứng dụng thực tiễn trong việc xây dựng hệ thống giả lập mạng cảm biến không dây quy mô lớn trên nền tảng OpenStack; đồng thời làm rõ các công nghệ cốt lõi và xu hướng nghiên cứu trong tính toán cận biên.

Thông qua nội dung trình bày trong chương này, người đọc có thể nắm bắt được kiến trúc tổng quan của một hệ thống IoT kết hợp hạ tầng điện toán đám mây và tính toán cận biên. Nắm được những đặc điểm, lợi ích, phân loại các mô hình dịch vụ trong điện toán đám mây cũng như các vấn đề nghiên cứu, thách thức trong IoT kết hợp tính toán cận biên giúp người đọc dễ dàng định hướng giải pháp khi triển khai thực tế.

## 5.1. Kiến trúc tổng quan hệ thống IoT tích hợp điện toán đám mây và điện toán cận biên

### 5.1.1. Kiến trúc tổng quan

Trong những năm gần đây, sự hội tụ giữa công nghệ IoT và điện toán đám mây (thường được gọi là Cloud-IoT) đã tạo ra một mô hình mới đầy tiềm năng. Tuy nhiên, việc truyền toàn bộ dữ liệu thô từ các thiết bị IoT về trung tâm dữ liệu đám mây tập trung bộc lộ nhiều điểm nghẽn nghiêm trọng: tiêu tốn băng thông mạng viễn thông, độ trễ truyền dẫn lớn, không đáp ứng kịp các tác vụ thời gian thực và nguy cơ rò rỉ dữ liệu nhạy cảm.

Chính vì vậy, kiến trúc điện toán phân tán đa tầng bao gồm 3 lớp chính đã được đề xuất và áp dụng rộng rãi:
1. **Lớp thiết bị IoT (Things Layer / End Devices):** Các cảm biến, cơ cấu chấp hành, thiết bị đeo thông minh thực hiện thu thập dữ liệu và thực thi lệnh điều khiển.
2. **Lớp cận biên (Edge / Fog Layer):** Các thiết bị có năng lực tính toán trung bình đặt tại biên mạng (Edge Gateways, Edge Routers, trạm phát sóng di động base station) thực hiện lọc dữ liệu, tiền xử lý, lưu trữ tạm và phản hồi tức thời.
3. **Lớp đám mây (Cloud Layer):** Các trung tâm dữ liệu quy mô lớn (Data Centers) thực hiện lưu trữ lâu dài (Big Data), khai phá dữ liệu chuyên sâu và huấn luyện các mô hình AI/Machine Learning.

Sự phát triển bùng nổ của công nghệ IoT dẫn đến kiến trúc hệ thống mạng ngày càng phức tạp và phân chia thành nhiều lớp để đáp ứng nhu cầu ngày càng cao của con người. Trong xu hướng đó, các hệ thống, ứng dụng IoT hiện đại ngày nay thường được tổ chức thành các lớp bao gồm: lớp thiết bị IoT, lớp thiết bị cận biên, lớp trung tâm dữ liệu trên hạ tầng điện toán đám mây.

**Hình 5.1.** Kiến trúc tổng quan hệ thống IoT kết hợp Điện toán đám mây và Điện toán biên [1]

- **Lớp thiết bị IoT:** Bao gồm hàng tỷ thiết bị cảm biến, cơ cấu chấp hành kết nối với nhau thông qua các giao thức mạng không dây tầm ngắn và tiết kiệm năng lượng (Zigbee, Bluetooth, 6LoWPAN, Wi-Fi, LoRa).
- **Lớp thiết bị cận biên:** Đóng vai trò là cầu nối thông minh trung gian giữa mạng cảm biến cục bộ và mạng diện rộng Internet. Lớp này thực hiện phân loại dữ liệu, nén dữ liệu, loại bỏ dữ liệu dư thừa và giải quyết các bài toán cục bộ mà không cần phụ thuộc vào kết nối đám mây.

cao trải nghiệm người dùng cũng là chủ đề mở và đang thu hút giới nghiên cứu.

- **Trung tâm dữ liệu (Data Center):** Là nơi hiện thực hạ tầng điện toán đám mây, với khả năng tính toán và lưu trữ khổng lồ. Trung tâm dữ liệu thực hiện quản lý, điều khiển, phân phối nguồn tài nguyên tính toán dựa trên các công nghệ ảo hóa (Virtual Machines, Containers), chạy các dịch vụ phân tích dữ liệu lớn và cung cấp giao diện quản lý toàn diện cho người dùng và các doanh nghiệp.

### 5.1.2. Các yêu cầu và đặc trưng cơ bản của các hệ thống tính toán cho IoT

Để đáp ứng được yêu cầu của các ứng dụng IoT phức tạp, các hệ thống tính toán (cả ở biên và đám mây) cần thỏa mãn các tiêu chí kỹ thuật cốt lõi sau:
- **Độ trễ truyền thông thấp (Low Latency):** Đối với các ứng dụng điều khiển thời gian thực (như xe tự hành, điều khiển robot công nghiệp, phẫu thuật từ xa), thời gian đáp ứng phải dưới mức hàng chục mili-giây.
- **Khả năng mở rộng (Scalability):** Hệ thống phải có khả năng tiếp nhận và xử lý mượt mà khi số lượng thiết bị IoT kết nối tăng vọt từ hàng nghìn lên hàng triệu nút.
- **Tính sẵn sàng và độ tin cậy (Availability & Reliability):** Đảm bảo dịch vụ hoạt động liên tục 24/7, có cơ chế sao lưu, dự phòng và tự phục hồi khi có sự cố nút mạng.
- **Tiết kiệm băng thông mạng (Bandwidth Optimization):** Tiền xử lý và nén dữ liệu tại biên giúp giảm tải đường truyền uplink lên đám mây.

- **Khả năng bảo mật dữ liệu (Data Security):** Đảm bảo hệ thống chịu được các cuộc tấn công từ bên ngoài nhắm vào dữ liệu bí mật lưu trữ trong hệ thống hay truyền trên mạng bằng các cơ chế mã hóa đầu-cuối.
- **Các dịch vụ bảo mật (Service Security):** Giúp hệ thống chịu được các cuộc tấn công từ bên ngoài nhắm vào việc làm tê liệt các dịch vụ (như tấn công từ chối dịch vụ phân tán DDoS).
- **Tính không đồng nhất (Heterogeneity):** Có khả năng tích hợp và làm việc ăn khớp giữa nhiều nền tảng phần cứng, hệ điều hành và giao thức truyền thông khác nhau.

## 5.2. Nền tảng điện toán đám mây và ứng dụng trong IoT

Theo định nghĩa của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST): *Điện toán đám mây là một mô hình cho phép truy cập mạng thuận tiện, theo yêu cầu tới một nhóm tài nguyên tính toán có thể cấu hình được (ví dụ: mạng, máy chủ, lưu trữ, ứng dụng và dịch vụ) mà có thể được cung cấp và giải phóng nhanh chóng với nỗ lực quản lý tối thiểu hoặc sự tương tác tối thiểu từ nhà cung cấp dịch vụ.*

Trong ngữ cảnh IoT, điện toán đám mây đóng vai trò là "bộ não trung tâm" thu thập, tích hợp dữ liệu từ mọi nguồn phân tán, cung cấp tài nguyên tính toán vô hạn cho việc phân tích dữ liệu lớn (Big Data Analytics) và đưa ra các quyết định thông minh mang tính chiến lược.

nối và ảo hóa một cách linh động và được thể hiện như một hoặc nhiều tài nguyên tính toán đồng nhất dựa trên các thỏa thuận ở mức dịch vụ được thiết lập thông qua việc đàm phán giữa nhà cung cấp dịch vụ và người tiêu dùng.

### 5.2.1. Đặc trưng cơ bản của điện toán đám mây

NIST xác định 5 đặc trưng cơ bản của điện toán đám mây:
1. **Tự phục vụ theo nhu cầu (On-demand Self-service):** Người dùng có thể tự cấu hình các tài nguyên tính toán (như thời gian máy chủ, dung lượng lưu trữ mạng) một cách tự động khi cần mà không cần tương tác trực tiếp với con người bên phía nhà cung cấp.
2. **Truy cập mạng rộng rãi (Broad Network Access):** Các tài nguyên được cung cấp qua mạng Internet và có thể truy cập thông qua các cơ chế tiêu chuẩn từ nhiều loại thiết bị khách khác nhau (máy tính, điện thoại di động, máy tính bảng).
3. **Dùng chung tài nguyên (Resource Pooling):** Nguồn tài nguyên tính toán của nhà cung cấp được gộp lại để phục vụ nhiều người dùng (multi-tenant model), với các tài nguyên vật lý và ảo hóa được phân bổ linh hoạt theo nhu cầu.
4. **Co giãn nhanh chóng (Rapid Elasticity):** Tài nguyên có thể được cấp phát và giải phóng một cách nhanh chóng, co giãn linh hoạt theo lưu lượng tải thực tế.
5. **Đo lường dịch vụ (Measured Service):** Hệ thống đám mây tự động kiểm soát và tối ưu hóa việc sử dụng tài nguyên bằng cách đo lường chi tiết ở mức dịch vụ (dung lượng lưu trữ, băng thông tiêu thụ, chu kỳ CPU sử dụng) để tính phí theo mức độ sử dụng (pay-as-you-go).

thuật như: tính toán song song (parallel computing), cân bằng tải (load balancing), định thời tác vụ (job scheduling).

Khả năng truy cập và tính linh động thể hiện qua việc các thiết bị, sản phẩm, dịch vụ và môi trường điện toán đám mây có thể truy cập với nhiều người nhất có thể. Tính linh động dịch vụ cho phép người dùng chuyển đổi các ứng dụng và dữ liệu giữa các đám mây khác nhau mà không bị trói buộc vào một nhà cung cấp duy nhất.

### 5.2.2. Lợi ích của điện toán đám mây

Việc ứng dụng điện toán đám mây mang lại nhiều lợi ích to lớn cho các tổ chức và doanh nghiệp phát triển hệ thống IoT:
- **Tiết kiệm chi phí đầu tư ban đầu (Cost Reduction):** Doanh nghiệp không cần phải đầu tư chi phí mua sắm máy chủ vật lý, xây dựng phòng máy lạnh và thuê đội ngũ bảo trì tốn kém. Thay vào đó chỉ cần trả phí thuê bao theo mức sử dụng thực tế.
- **Tập trung vào nghiệp vụ cốt lõi:** Các nhà phát triển giải pháp IoT có thể tập trung toàn lực vào việc phát triển ứng dụng và thuật toán kinh doanh, để việc quản trị hạ tầng máy chủ cho các nhà cung cấp đám mây chuyên nghiệp đảm nhiệm.

doanh nghiệp có thể cải tiến hiệu năng các dịch vụ IT, dễ dàng vận hành và quản lý tập trung các dịch vụ thông qua nhà cung cấp dịch vụ.
- **Nâng cao hiệu quả sử dụng tài nguyên:** Doanh nghiệp có thể hợp tác với nhà cung cấp dịch vụ điện toán đám mây để tận dụng công nghệ ảo hóa, tránh lãng phí năng lực tính toán dư thừa khi hệ thống nhàn rỗi.
- **Khả năng phục hồi sau thảm họa (Disaster Recovery):** Dữ liệu được lưu trữ phân tán và sao lưu tự động trên nhiều trung tâm dữ liệu ở các khu vực địa lý khác nhau, đảm bảo dữ liệu không bị mất mát khi xảy ra sự cố thiên tai hoặc hỏng hóc phần cứng.

**Hình 5.2.** Khung phân cấp dịch vụ điện toán đám mây

Mô hình phân cấp dịch vụ điện toán đám mây truyền thống được chia thành 3 lớp cơ bản (Hình 5.2):
1. **IaaS (Infrastructure as a Service - Hạ tầng như một dịch vụ)**
2. **PaaS (Platform as a Service - Nền tảng như một dịch vụ)**
3. **SaaS (Software as a Service - Phần mềm như một dịch vụ)**

### 5.2.3. Mô hình IaaS

Các dịch vụ trên hạ tầng điện toán đám mây được phát triển theo 3 loại mô hình dịch vụ cơ bản. Trong đó, mô hình thấp nhất là **Hạ tầng như một dịch vụ (Infrastructure as a Service - IaaS)**:

Trong mô hình IaaS, nhà cung cấp dịch vụ cung cấp cho người dùng các tài nguyên phần cứng máy tính được ảo hóa thô, bao gồm:
- **Năng lực tính toán (Compute):** Các máy ảo (Virtual Machines) hoặc bare-metal servers với số lượng CPU core, dung lượng RAM xác định.
- **Không gian lưu trữ (Storage):** Lưu trữ khối (Block Storage), lưu trữ đối tượng (Object Storage), lưu trữ tệp (File Storage).
- **Tài nguyên mạng (Networking):** Bộ định tuyến ảo (Virtual Routers), tường lửa ảo (Firewalls), địa chỉ IP tĩnh công cộng, mạng riêng ảo (VPC/VLAN).

Người dùng có toàn quyền kiểm soát hệ điều hành được cài đặt trên máy ảo, cấu hình các dịch vụ mạng, triển khai các phần mềm trung gian (middleware) và các ứng dụng của mình. Nhà cung cấp IaaS chịu trách nhiệm quản lý và bảo trì toàn bộ phần cứng vật lý bên dưới (máy chủ, hệ thống lưu trữ SAN/NAS, thiết bị chuyển mạch mạng, nguồn điện và phòng máy).

Người dùng không thể quản lý hay điều khiển hạ tầng bên dưới của nhà cung cấp dịch vụ điện toán đám mây nhưng có thể điều khiển hệ điều hành, bộ nhớ, ứng dụng được triển khai cũng như những cài đặt liên quan tới các thành phần kết nối mạng giữa các máy ảo mà mình quản lý. Một số nền tảng cung cấp dịch vụ này như: Amazon EC2, Google Compute Engine, Microsoft Azure Virtual Machines, OpenNebula, OpenStack...

**Hình 5.3.** Các thành phần chính trong dịch vụ hạ tầng IaaS

Hình 5.3 mô tả các thành phần chức năng cốt lõi của một hệ thống IaaS:
- **Quản lý máy chủ ảo (Virtual Compute Management):** Cung cấp các công cụ tạo mới, xóa bỏ, khởi động, tạm dừng, di chuyển nóng (live migration) các máy ảo giữa các máy chủ vật lý.
- **Quản lý lưu trữ ảo (Virtual Storage Management):** Cấp phát và gắn kết các ổ đĩa ảo, quản lý ảnh đĩa hệ điều hành (Image Repository).
- **Quản lý mạng ảo (Virtual Network Management):** Cấu hình các subnet, cấp phát địa chỉ IP qua DHCP ảo, thiết lập định tuyến và quy tắc bảo mật an ninh mạng (Security Groups).

(virtual storage) bao gồm phân bổ không gian lưu trữ, giải phóng bộ nhớ, ghi dữ liệu, đọc dữ liệu...; quản lý mạng ảo (virtual network) bao gồm việc cấp phát địa chỉ IP, đăng ký tên miền, thiết lập kết nối, phân bổ băng thông đường truyền...

### 5.2.4. Mô hình PaaS

**Nền tảng như một dịch vụ (Platform as a Service - PaaS)** là mô hình cung cấp một môi trường hoàn chỉnh trên đám mây để các nhà phát triển có thể xây dựng, thử nghiệm, triển khai và quản lý các ứng dụng mà không cần quan tâm đến việc mua sắm, cài đặt và bảo trì hạ tầng phần cứng cũng như hệ điều hành bên dưới.

Trong mô hình PaaS, nhà cung cấp quản lý toàn bộ hạ tầng (máy chủ, mạng, lưu trữ) cùng với hệ điều hành, runtime ngôn ngữ lập trình, hệ quản trị cơ sở dữ liệu và các phần mềm trung gian. Người dùng chỉ cần tải lên mã nguồn ứng dụng và cấu hình các thiết lập ứng dụng.

Đối với IoT, các nền tảng **IoT Cloud Platforms (IoT PaaS)** rất phát triển, cung cấp sẵn các dịch vụ chuyên biệt cho IoT như:
- Cổng giao tiếp thiết bị (Device Gateway hỗ trợ giao thức MQTT, CoAP, HTTP).
- Quản lý danh mục và trạng thái thiết bị (Device Registry, Device Shadow).
- Động cơ xử lý luật thời gian thực (Rule Engine).
- Cơ sở dữ liệu chuỗi thời gian (Time-series Database).
- Công cụ trực quan hóa bảng điều khiển (Dashboard Visualization).

Các nền tảng IoT PaaS nổi tiếng bao gồm: AWS IoT Core, Google Cloud IoT, Microsoft Azure IoT Hub, ThingsBoard, Blynk, ThingSpeak.

Kỹ thuật được sử dụng để hiện thực mô hình này đó là thiết kế môi trường chạy ứng dụng (runtime environment design). Môi trường chạy ứng dụng liên quan tới việc thu thập các dịch vụ phần mềm có sẵn, cần thiết để ứng dụng thực thi như các thư viện, gói phần mềm, gói công cụ cần thiết.

### 5.2.5. Mô hình SaaS

**Phần mềm như một dịch vụ (Software as a Service - SaaS)** là mô hình dịch vụ đám mây hoàn chỉnh nhất ở tầng trên cùng, nơi nhà cung cấp phân phối một ứng dụng phần mềm hoàn thiện tới người dùng đầu cuối qua mạng Internet, thường là thông qua trình duyệt web hoặc ứng dụng di động.

Trong mô hình SaaS, người dùng không cần cài đặt phần mềm lên máy tính cá nhân, không cần quản lý hạ tầng hay nền tảng mà chỉ cần đăng nhập tài khoản và sử dụng các tính năng của phần mềm. Mọi vấn đề về cập nhật tính năng mới, vá lỗi bảo mật, sao lưu dữ liệu đều do nhà cung cấp đảm nhiệm hoàn toàn.

các hạ tầng bên dưới bao gồm mạng, máy chủ, hệ điều hành, bộ nhớ hay thậm chí là các khả năng riêng lẻ của các ứng dụng trong khuôn khổ cấu hình giới hạn cho từng người dùng riêng lẻ.

Một số dịch vụ cung cấp theo mô hình SaaS phổ biến như: các ứng dụng của Google (Gmail, Google Docs, Google Drive), Microsoft 365, Dropbox, Salesforce CRM.

Trong lĩnh vực IoT, các ứng dụng SaaS thường là các giải pháp đóng gói hoàn chỉnh cho từng lĩnh vực chuyên ngành:
- **Hệ thống Quản lý Tòa nhà thông minh (Smart Building Management System):** Cho phép ban quản lý theo dõi tiêu thụ năng lượng điện, nước, điều khiển hệ thống chiếu sáng và HVAC.
- **Hệ thống Giám sát Hạm đội xe (Fleet Management):** Định vị phương tiện GPS, theo dõi hành trình xe, giám sát mức tiêu hao nhiên liệu.
- **Hệ thống Nông nghiệp thông minh SaaS:** Phân tích độ ẩm đất, dự báo sâu bệnh và tự động hóa hệ thống tưới nhỏ giọt.

trụ, mô phỏng hóa sinh; các ứng dụng cho chính phủ như hệ thống y tế quốc gia, hệ thống giao thông vận tải...
- **Cổng thông tin (web portal):** cung cấp các dịch vụ tìm kiếm thông tin chuẩn, ngoài ra cũng có các dịch vụ khác như e-mail, tin tức, giá chứng khoán. Cổng thông tin cung cấp một giao diện web thống nhất cho người dùng truy cập tới nhiều dịch vụ khác nhau.

### 5.2.6. Ứng dụng công nghệ điện toán đám mây trong xây dựng hệ thống giả lập WSN với số lượng nút lớn

Trong nghiên cứu và phát triển các giải pháp IoT và mạng cảm biến không dây (WSN), việc thử nghiệm trên các mạng quy mô lớn (hàng trăm đến hàng nghìn nút) gặp nhiều rào cản lớn:
- Chi phí mua sắm thiết bị phần cứng thực tế rất đắt đỏ.
- Khó khăn trong việc triển khai thực địa, nạp lại mã nguồn đồng loạt và giám sát trạng thái từng nút.
- Khó tái lập lại chính xác môi trường thử nghiệm khi cần đánh giá so sánh hiệu năng các giao thức định tuyến.

Để giải quyết bài toán trên, giải pháp ứng dụng hạ tầng đám mây mã nguồn mở **OpenStack** kết hợp với công nghệ ảo hóa nhẹ **Docker Containers** đã được nghiên cứu và xây dựng nhằm giả lập các mạng WSN quy mô lớn với chi phí thấp và độ linh hoạt cao.

nguyên phục vụ cho các nghiên cứu khác giúp tối ưu việc sử dụng tài nguyên. Bên cạnh đó, việc triển khai ảo hóa lớp thứ hai với kỹ thuật Container cho phép tạo ra một số lượng rất lớn các nút ảo với lượng tài nguyên yêu cầu thấp giúp đáp ứng yêu cầu phục vụ các thử nghiệm có số lượng nút lớn.

**Hình 5.4.** Giải pháp tích hợp mạng cảm biến không dây trên hạ tầng đám mây OpenStack

Kiến trúc thử nghiệm tích hợp được mô tả trong Hình 5.4 bao gồm hai tầng ảo hóa:
1. **Tầng ảo hóa phần cứng OpenStack (IaaS):** Quản lý cụm máy chủ vật lý, tạo ra các máy ảo Linux (Swarm Workers) được kết nối với nhau qua mạng ảo diện rộng.
2. **Tầng ảo hóa nhẹ Docker Containers:** Chạy trên các máy ảo OpenStack. Mỗi container đóng vai trò giả lập một nút cảm biến không dây hoàn chỉnh, chạy hệ điều hành mạng nhúng (như Contiki hoặc Linux rút gọn), cài đặt giao thức định tuyến (như OLSR) và mã nguồn ứng dụng cảm biến.

Quá trình triển khai ảnh sẽ gồm 5 bước được thực hiện ở 3 vị trí luận lý khác nhau:
1. Người dùng tạo ra tập tin đặc tả kịch bản thử nghiệm trên giao diện front-end của UIT-IoT Testbed tại máy người dùng.
2. Hệ thống biên dịch kịch bản thành tệp cấu hình triển khai Docker Compose và các tệp cấu hình mạng.
3. Master Node trên OpenStack nhận yêu cầu, phân tích số lượng nút và tự động khởi tạo các mạng ảo và container tương ứng trên các máy Swarm Workers.
4. Các container khởi động, kết nối vào các card mạng ảo tương ứng theo đúng cấu trúc tô-pô định trước và kích hoạt tiến trình định tuyến.
5. Dữ liệu giám sát từ các container được thu thập và gửi về giao diện người dùng theo thời gian thực.

#### 5.2.6.1. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý MESH của WSNs trên OpenStack

Trong cấu trúc mạng MESH, mọi nút mạng trong cùng phạm vi phát sóng đều có thể truyền tin trực tiếp với nhau hoặc qua nhiều chặng trung gian.

giữa máy host và các container, các biến môi trường, các lệnh sẽ được thực thi khi khởi chạy containers. Ngoài ra, tập tin này còn đặc tả thông tin về các mạng ảo và kết nối giữa các containers thông qua các mạng ảo này.

**Hình 5.5.** Mô hình mạng luận lý dạng MESH trên OpenStack

Hình 5.5 mô tả giải pháp xây dựng mạng luận lý MESH trên OpenStack:
- Một mạng ảo OpenStack Neutron (mạng dùng chung) được tạo ra đóng vai trò như môi trường truyền sóng không dây chung.
- Tất cả các container giả lập nút mạng WSN đều gắn card mạng ảo kết nối vào cùng mạng con này.
- Giao thức định tuyến mạng cảm biến (như OLSR - Optimized Link State Routing) chạy bên trong mỗi container sẽ tự động trao đổi các bản tin HELLO và TC (Topology Control) để khám phá các láng giềng và xây dựng bảng định tuyến đa chặng tối ưu.

#### 5.2.6.2. Thiết kế kiến trúc, giải pháp xây dựng kiến trúc mạng luận lý TREE của WSNs trên OpenStack

**Hình 5.6.** Mô hình mạng luận lý dạng TREE trên OpenStack

Điểm khác biệt so với kiến trúc mạng MESH là trong kiến trúc mạng TREE, các nút mạng được phân chia theo cấu trúc thứ bậc hình cây (cha - con). Mỗi nút chỉ giao tiếp trực tiếp với nút cha hoặc các nút con của nó mà không được truyền thông ngang hàng trực tiếp với các nhánh khác.

Để hiện thực cấu trúc mạng TREE trên OpenStack, hệ thống tự động sinh ra nhiều mạng ảo riêng biệt: mỗi mạng ảo đại diện cho một liên kết điểm - điểm (Point-to-Point) hoặc một nhóm cha - con cục bộ. Nhờ đó, các container chỉ có thể trao đổi gói tin qua các liên kết hợp lệ theo đúng cấu trúc cây định trước.

#### 5.2.6.3. Giải pháp tích hợp, triển khai kiến trúc mạng WSNs (MESH/TREE) và giao thức định tuyến WSNs (olsr), mô hình giả lập thiết bị WSNs trên OpenStack

Để tự động hóa hoàn toàn quy trình khởi tạo và điều khiển mạng thử nghiệm WSN trên hạ tầng đám mây OpenStack, hệ thống sử dụng tập hợp các giao diện lập trình ứng dụng RESTful APIs do OpenStack cung cấp.

**Bảng 5.1.** Tóm lược một số APIs OpenStack (phần 1)

| Nhóm API | Root URL | API | Chức năng | Input | Output |
|:---|:---|:---|:---|:---|:---|
| **Identity (Keystone)** | `https://mitaka.uit.edu.vn:5000/v2.0` | `POST /v2.0/tokens` | Chứng thực người dùng, trả về token để thực thi các APIs khác | `tenantName` (tên project), `username`, `password` | `token` |
| **Networking (Neutron)** | `https://mitaka.uit.edu.vn:9696/v2.0` | `GET /v2.0/networks` | Liệt kê thông tin tất cả các networks | Không có | Danh sách networks |
| | | `POST /v2.0/networks` | Tạo mới một network ảo | `name` (tên network), `admin_state_up` | Thông tin network vừa tạo |
| | | `POST /v2.0/subnets` | Tạo mới một subnet ảo | `network_id`, `ip_version`, `cidr`, `enable_dhcp` | Thông tin subnet vừa tạo |
| **Compute (Nova)** | `https://mitaka.uit.edu.vn:8774/v2.1` | `GET /images` | Liệt kê thông tin các images có trong OpenStack | Không có | Danh sách images |

**Bảng 5.1.** Tóm lược một số APIs OpenStack (phần 2 - Compute APIs)

| Nhóm API | Root URL | API | Chức năng | Input | Output |
|:---|:---|:---|:---|:---|:---|
| **Compute (Nova)** *(tiếp theo)* | `https://mitaka.uit.edu.vn:8774/v2.1` | `GET /flavors` | Liệt kê thông tin các flavors (thông số cấu hình CPU, RAM... cho máy ảo) | Không có | Danh sách flavors |
| | | `GET /os-keypairs` | Liệt kê thông tin các keypairs (cặp SSH key dùng chứng thực) | Không có | Danh sách keypairs |
| | | `POST /servers` | Tạo một máy ảo mới trong OpenStack | `name`, `image_id`, `flavor_id`, danh sách networks, `key_name` | Thông tin máy ảo vừa tạo |

Chức năng chính của Compute API là tạo, xóa, sửa các Instance (máy ảo) có trong OpenStack. Ngoài ra, Compute API cung cấp các APIs hỗ trợ việc tạo, xóa, sửa, lấy thông tin images, flavors... Nhờ hệ thống APIs này, hệ thống UIT-IoT Testbed có thể tự động cấp phát tài nguyên tính toán và thiết lập mạng ảo chỉ trong vài phút.

**Hình 5.7.** Kiến trúc mô phỏng thiết bị WSN sử dụng container/VM trên OpenStack

**Hình 5.8.** Cấu trúc liên kết mạng mô phỏng

Hình 5.7 và Hình 5.8 mô tả kiến trúc triển khai thử nghiệm:
- Mỗi máy ảo OpenStack đóng vai trò là một Host chứa cụm Docker Engine.
- Các container được khởi tạo với hình ảnh chứa sẵn hệ điều hành Linux gọn nhẹ (Alpine Linux hoặc Ubuntu Core) cùng gói phần mềm giao thức định tuyến OLSR (`olsrd`).
- Tập tin cấu hình `olsrd.conf` được tự động sinh ra và gắn vào container khi khởi chạy để thiết lập các tham số định tuyến (chu kỳ gửi gói tin HELLO, thời gian sống của tuyến đường).
- Ứng dụng mô phỏng gửi dữ liệu cảm biến định kỳ qua socket UDP đến nút Sink để đánh giá tỷ lệ chuyển gói thành công (PDR - Packet Delivery Ratio) và độ trễ truyền gói tin trung bình.

Quy trình triển khai cụm Docker Swarm được thực hiện tuần tự qua các bước: gọi API chứng thực `POST /v2.0/tokens` để lấy access token; sau đó gọi các APIs lấy danh sách hình ảnh (`GET /images`), cấu hình máy ảo (`GET /flavors`), khóa SSH (`GET /os-keypairs`) và mạng ảo (`GET /v2.0/networks`). Cuối cùng, hệ thống gửi yêu cầu `POST /servers` để khởi tạo các máy ảo worker và kích hoạt các containers.

## 5.3. Nền tảng điện toán cận biên và ứng dụng trong IoT

### 5.3.1. Kiến trúc triển khai điện toán cận biên trong IoT

Điện toán cận biên (Edge Computing) là mô hình xử lý tính toán phân tán, trong đó các tác vụ xử lý thông tin, lưu trữ và điều khiển được đặt tại vị trí biên của mạng – gần với nguồn phát sinh dữ liệu (các thiết bị cảm biến và người dùng). Mô hình này giải quyết triệt để các hạn chế cố hữu của điện toán đám mây truyền thống về độ trễ, lưu lượng mạng và tính riêng tư.

Hình 5.9 mô tả kiến trúc tổng quan các thành phần của hệ thống tính toán cận biên áp dụng trong IoT. Hệ thống bao gồm:
1. **Các thiết bị IoT:** Như các cảm biến, thiết bị động cơ, mạch điều khiển thu thập dữ liệu từ môi trường vật lý.
2. **Các thiết bị tính toán cận biên:** Bao gồm các IoT Gateway, thiết bị biên chuyên dụng (Edge Nodes), máy tính nhúng, trạm gốc viễn thông di động (eNodeB trong 4G/5G).
3. **Các máy chủ đám mây:** Thực hiện các chức năng lưu trữ dài hạn, phân tích dữ liệu lớn và quản lý chiến lược toàn mạng.

**Hình 5.9.** Kiến trúc điện toán sương mù / điện toán biên trong hệ thống IoT

### 5.3.2. Các công nghệ, kỹ thuật nổi bật cho tính toán cận biên trong IoT

Để hiện thực hóa tính toán cận biên hiệu quả, nhiều công nghệ và kỹ thuật tiên tiến đã được nghiên cứu và ứng dụng:

- **Quản lý tài nguyên phân tán (Resource Management):** Điều phối linh hoạt các nguồn tài nguyên tính toán (CPU, GPU, RAM) và lưu trữ hạn chế tại biên nhằm phục vụ tối ưu đồng thời nhiều ứng dụng IoT khác nhau.
- **Tính toán kết hợp truyền thông (Joint Communication and Computing):** Tối ưu hóa đồng thời việc phân bổ kênh truyền vô tuyến và phân bổ năng lực xử lý tính toán để giảm thiểu tổng năng lượng tiêu thụ và độ trễ xử lý của các thiết bị IoT di động.
- **Di chuyển tác vụ tính toán (Computation Offloading):** Cơ chế cho phép thiết bị IoT có năng lực xử lý yếu hoặc sắp cạn pin chuyển giao một phần hoặc toàn bộ tác vụ tính toán nặng (như giải mã tín hiệu, nhận dạng hình ảnh) sang cho thiết bị biên kế cận xử lý thay.

**Công nghệ xử lý thông minh tại thiết bị cận biên (Edge Intelligence / Edge AI)**

Lượng dữ liệu khổng lồ từ các thiết bị IoT thu thập đóng vai trò quan trọng trong việc xây dựng các tập dữ liệu (dataset) dùng cho việc huấn luyện và phát triển các giải pháp máy học. Tuy nhiên, việc truyền toàn bộ dữ liệu về đám mây gây tắc nghẽn mạng nghiêm trọng. Xu hướng mới là đưa trí tuệ nhân tạo ra biên:
- **Suy luận tại biên (Edge Inference):** Sử dụng các mô hình học sâu đã được nén nhẹ (bằng kỹ thuật lượng tử hóa Quantization, cắt tỉa Pruning, tri thức chưng cất Knowledge Distillation) như TensorFlow Lite, TinyML, ONNX để thực thi nhận dạng khuôn mặt, phát hiện dị thường trực tiếp ngay trên vi điều khiển hoặc máy tính nhúng tại chỗ với độ trễ tính bằng mili-giây.
- **Học liên kết (Federated Learning):** Các nút biên tự huấn luyện mô hình máy học cục bộ dựa trên dữ liệu riêng tư của mình và chỉ gửi các trọng số mô hình (model updates/gradients) về đám mây để tổng hợp mô hình chung toàn cầu, qua đó bảo vệ tuyệt đối tính riêng tư dữ liệu người dùng.

rộng hệ thống bằng việc cho phép chia sẻ tài nguyên dựa trên nhu cầu trong lúc chạy (runtime needs).

## 5.4. Các vấn đề tồn tại và hướng nghiên cứu trong tương lai

Mặc dù việc kết hợp giữa điện toán đám mây và điện toán cận biên mở ra nhiều cơ hội phát triển vượt bậc cho hệ sinh thái IoT, nhiều thách thức kỹ thuật quan trọng vẫn đang cần tiếp tục nghiên cứu:
- **Quản lý tính di động (Mobility Management):** Khi các nút IoT hoặc phương tiện di chuyển liên tục qua các vùng phủ sóng của các trạm biên khác nhau, việc di chuyển trạng thái dịch vụ (Service / Container Migration) liền mạch không làm gián đoạn kết nối là bài toán phức tạp.
- **Bảo mật và quyền riêng tư tại biên:** Các thiết bị biên thường đặt ở môi trường công cộng bên ngoài, dễ bị tấn công vật lý, cài mã độc hoặc giả mạo. Cần phát triển các cơ chế xác thực phân tán dựa trên công nghệ chuỗi khối (Blockchain) hoặc môi trường thực thi tin cậy (Trusted Execution Environment - TEE).
- **Cân bằng năng lượng và tài nguyên xanh (Green Computing):** Tối ưu hóa hiệu suất tiêu thụ năng lượng của các cụm máy chủ biên khi hoạt động bằng năng lượng tái tạo.

pháp mã hóa, bảo mật đã được nghiên cứu và triển khai thành công trên thiết bị IoT có tài nguyên hạn chế.

## Bài tập Chương 5

1. Hãy phân tích các yêu cầu và đặc trưng cơ bản của các hệ thống tính toán cho IoT.
2. Hãy so sánh ưu và nhược điểm của các mô hình điện toán đám mây (IaaS, PaaS, SaaS).
3. Hãy so sánh ưu và nhược điểm của các công nghệ điện toán đám mây và điện toán cận biên. Liệt kê những ứng dụng IoT phù hợp cho mỗi công nghệ điện toán này.
4. Hãy so sánh các công nghệ ảo hóa được sử dụng trong IoT (máy ảo truyền thống so với container).
5. Hãy xây dựng một kịch bản ứng dụng tính toán cận biên trong IoT.
6. Từ nền tảng Arduino và Raspberry Pi 3, hãy xây dựng ứng dụng y tế thông minh áp dụng điện toán đám mây và điện toán cận biên.
7. Hãy xây dựng ứng dụng Nông nghiệp thông minh áp dụng kỹ thuật điện toán đám mây và điện toán cận biên. Sau đó so sánh ưu và nhược điểm của hai hướng tiếp cận này.
8. Trong ứng dụng giám sát giao thông thông minh, các camera được đặt trên đường và truyền tín hiệu video về các gateway. Dữ liệu từ các gateway sau đó được truyền về Cloud. Hãy xây dựng ứng dụng giám sát giao thông thông minh để đếm số phương tiện qua lại trong một khoảng thời gian. Xây dựng hai kịch bản đếm số phương tiện tại gateway và tại cloud. Sau đó so sánh hai kịch bản này.

# Chương 6: Quản lý ngữ cảnh thông minh và trí tuệ nhân tạo trong IoT

## Nội dung chương

- **6.1.** Ngữ cảnh và thích ứng ngữ cảnh trong IoT.
- **6.2.** Quản lý ngữ cảnh trong IoT (Vòng đời 4 giai đoạn).
- **6.3.** Các kỹ thuật mô hình hóa ngữ cảnh.
- **6.4.** Các kỹ thuật suy luận ngữ cảnh (Rule-based, Fuzzy Logic kiểm soát vi khí hậu nhà kính, Ontology, CBR).
- **6.5.** Trí tuệ nhân tạo và Machine Learning trong IoT.
- **Bài tập Chương 6.**


Để tạo ra tính thông minh cho mỗi ứng dụng IoT đòi hỏi hệ thống không chỉ dừng lại ở việc thu thập và lưu trữ các giá trị cảm biến đơn thuần, mà cần phải có khả năng hiểu được ngữ cảnh xung quanh môi trường hoạt động và tự động thích ứng với các thay đổi của ngữ cảnh đó. Khái niệm nhận thức ngữ cảnh (Context-Awareness) và quản lý ngữ cảnh (Context Management) đóng vai trò trung tâm trong việc biến các thiết bị IoT thụ động thành các hệ thống thông minh chủ động phục vụ con người.

Bên cạnh đó, sự bùng nổ của các kỹ thuật Trí tuệ nhân tạo (AI), Học máy (Machine Learning) và Học sâu (Deep Learning) mang lại những công cụ đột phá giúp hệ thống IoT có thể xử lý các tập dữ liệu chuỗi thời gian khổng lồ, phát hiện các mẫu hành vi phức tạp, đưa ra các dự báo chính xác và tự động hóa quá trình ra quyết định.

Nội dung chương này trình bày các khái niệm nền tảng về ngữ cảnh và thích ứng ngữ cảnh; quy trình 4 giai đoạn trong vòng đời quản lý ngữ cảnh; phân tích chi tiết các kỹ thuật mô hình hóa ngữ cảnh và suy luận ngữ cảnh phổ biến; đồng thời giới thiệu các ứng dụng tiêu biểu của học máy và trí tuệ nhân tạo trong hệ sinh thái IoT hiện đại.

cho phép các dịch vụ được tạo và tái lập trình theo ngữ cảnh sử dụng. Khái niệm nhận thức ngữ cảnh (context-awareness) được định nghĩa như sau: *"Nhận thức ngữ cảnh (context-awareness) đề cập đến khả năng của một ứng dụng, dịch vụ hoặc thậm chí là một thiết bị đầu cuối nhận thức được môi trường vật chất, trạng thái mạng, hoàn cảnh người dùng và tự động điều chỉnh hành vi của mình cho phù hợp với ngữ cảnh đó mà không cần sự can thiệp trực tiếp của con người."*

## 6.1. Ngữ cảnh và thích ứng ngữ cảnh

Trong các hệ thống tính toán phổ dụng (Ubiquitous Computing) và IoT, ngữ cảnh là nhân tố quyết định tính "thông minh" của dịch vụ. Một dịch vụ thông minh không chỉ phản hồi thụ động theo các câu lệnh cố định mà phải chủ động thích ứng linh hoạt theo thời gian, không gian và trạng thái của người sử dụng.

Ngoài ra, các kỹ thuật trí tuệ nhân tạo cũng đang được chú ý trong quản lý ngữ cảnh trong IoT vì các yếu tố biến động, không chắc chắn, phức tạp và mơ hồ của dữ liệu. Trong phạm vi giáo trình này, tác giả đề cập đến những nội dung cơ bản nhất của trí tuệ nhân tạo được phục vụ trong quản lý ngữ cảnh và suy luận ngữ cảnh trong IoT.

### 6.1.1. Ngữ cảnh

Định nghĩa kinh điển và được chấp nhận rộng rãi nhất về ngữ cảnh trong khoa học máy tính là định nghĩa của Anind Dey (năm 2001):

> *"Ngữ cảnh là thông tin bất kỳ được sử dụng để mô tả trạng thái của một thực thể. Thực thể có thể là con người, địa điểm hoặc đối tượng vật lý/luận lý có liên quan đến sự tương tác giữa người dùng và ứng dụng, bao gồm cả người dùng và ứng dụng đó."*

**Hình 6.1.** Không gian ngữ cảnh hoạt động của thực thể

Dựa trên bản chất và nguồn gốc dữ liệu, ngữ cảnh trong IoT được phân loại thành 2 nhóm chính:
- **Ngữ cảnh sơ cấp (Primary Context / Low-level Context):** Là các dữ liệu đo đạc trực tiếp từ cảm biến vật lý hoặc thiết bị phần cứng mà chưa qua xử lý ngữ nghĩa. Ví dụ: vị trí tọa độ GPS (kinh độ, vĩ độ), nhiệt độ số thực (25.5°C), cường độ ánh sáng (300 Lux), độ ẩm đất (70%).
- **Ngữ cảnh thứ cấp (Secondary Context / High-level Context):** Là các thông tin trừu tượng có mức ngữ nghĩa cao hơn, được tính toán hoặc suy luận từ ngữ cảnh sơ cấp kết hợp với tri thức chuyên gia. Ví dụ: từ tọa độ GPS suy ra người dùng đang "ở nơi làm việc" hay "ở nhà"; từ nhiệt độ và độ ẩm suy ra thời tiết "dễ chịu" hay "nắng nóng oi bức".

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

**Đặc điểm của ngữ cảnh trong IoT:**
1. **Được thu thập từ nút cảm biến hay mạng cảm biến:** Dữ liệu mang tính phân tán, phát sinh liên tục theo dòng thời gian (streaming data).
2. **Được thu thập từ những thiết bị nhỏ và tài nguyên hạn chế:** Dẫn đến dữ liệu có thể bị trễ, ngắt quãng hoặc thiếu chính xác do hạn chế về pin và phần cứng.
3. **Tính không hoàn hảo và bất định (Imperfect & Uncertain):** Dữ liệu cảm biến thường xuyên chứa nhiễu, lỗi đo đạc hoặc bị mất gói tin trong quá trình truyền sóng vô tuyến.
4. **Tính phụ thuộc thời gian (Temporal Aspect):** Ngữ cảnh luôn biến đổi theo thời gian; giá trị ngữ cảnh chỉ có giá trị sử dụng trong một khoảng thời gian hiệu lực nhất định.

### 6.1.2. Thích ứng ngữ cảnh

Thích ứng ngữ cảnh (Context Adaptation) là quá trình hệ thống IoT tự động thay đổi hành vi, giao diện hoặc cấu hình dịch vụ dựa trên ngữ cảnh đã được nhận diện nhằm tối ưu hóa trải nghiệm người dùng và tiết kiệm tài nguyên năng lượng.

Ví dụ về thích ứng ngữ cảnh trong hệ thống chiếu sáng thông minh tại tòa nhà văn phòng:
- **Trường hợp 1:** Nếu chỉ có 1 người ngồi tại một vị trí trong phòng làm việc, hệ thống chỉ bật cụm đèn chiếu sáng tại khu vực bàn làm việc đó, tắt toàn bộ các bóng đèn khác để tiết kiệm điện.
- **Trường hợp 2:** Nếu có nhiều người ngồi tại nhiều vị trí khác nhau trong phòng hoặc đang tổ chức cuộc họp, hệ thống tự động bật toàn bộ hệ thống đèn chiếu sáng trong phòng.

**Hình 6.2.** Vòng đời quản lý ngữ cảnh trong IoT

## 6.2. Quản lý ngữ cảnh trong IoT

Quá trình quản lý ngữ cảnh trong các hệ thống IoT hiện đại tuân theo một chu trình khép kín gồm 4 giai đoạn chính (Hình 6.2):
1. **Thu thập ngữ cảnh (Context Acquisition)**
2. **Mô hình hóa ngữ cảnh (Context Modeling)**
3. **Suy luận ngữ cảnh (Context Reasoning)**
4. **Phân phối ngữ cảnh (Context Dissemination)**

### 6.2.1. Thu thập ngữ cảnh

**Thu thập ngữ cảnh (Context Acquisition):** Là bước đầu tiên chịu trách nhiệm lấy dữ liệu từ nhiều nguồn khác nhau: cảm biến vật lý (nhiệt độ, gia tốc), dịch vụ mạng (thông tin thời tiết từ API web), người dùng (nhập liệu trực tiếp) hoặc trạng thái thiết bị (mức pin, địa chỉ IP). Thu thập ngữ cảnh có thể thực hiện theo cơ chế thăm dò định kỳ (polling) hoặc hướng sự kiện theo ngưỡng (event-triggered).

### 6.2.2. Mô hình hóa ngữ cảnh

**Mô hình hóa ngữ cảnh (Context Modeling):** Chuyển đổi dữ liệu thô thu thập được thành các cấu trúc dữ liệu chuẩn mực, có tổ chức để hệ thống phần mềm có thể lưu trữ, truy vấn, chia sẻ và suy luận hiệu quả.

### 6.2.3. Suy luận ngữ cảnh

**Suy luận ngữ cảnh (Context Reasoning):** Là giai đoạn cốt lõi sử dụng các thuật toán tính toán để suy ra ngữ cảnh cấp cao từ ngữ cảnh cấp thấp, phát hiện mâu thuẫn dữ liệu và đưa ra quyết định hành động thích ứng cho hệ thống.

### 6.2.4. Phân phối ngữ cảnh

**Phân phối ngữ cảnh (Context Dissemination):** Cung cấp dữ liệu ngữ cảnh đã được xử lý tới các ứng dụng hoặc cơ cấu chấp hành thông qua mô hình Publish/Subscribe (như giao thức MQTT) hoặc giao thức Request/Response (REST API).

## 6.3. Các kỹ thuật mô hình hóa ngữ cảnh

Phần này trình bày chi tiết các hướng tiếp cận chính được sử dụng để mô hình hóa ngữ cảnh trong các hệ thống IoT:

### 6.3.1. Mô hình khóa/giá trị (Key-Value Model)

Mô hình khóa/giá trị là mô hình đơn giản nhất, trong đó mỗi phần tử ngữ cảnh được biểu diễn dưới dạng một cặp `(Khóa, Giá trị)`:
```
Location = "Room_E101"
Temperature = 25.5
Status = "Active"
```
- **Ưu điểm:** Cực kỳ đơn giản, dễ cài đặt, chi phí xử lý và lưu trữ rất nhỏ.
- **Nhược điểm:** Không biểu diễn được mối quan hệ phân cấp phức tạp giữa các thực thể; không có cơ chế kiểm tra tính hợp lệ của dữ liệu; khả năng suy luận bị hạn chế tối đa.

### 6.3.2. Mô hình sơ đồ (Markup Model - XML / JSON)

Mô hình sơ đồ sử dụng các thẻ phân cấp (tags) để cấu trúc hóa dữ liệu ngữ cảnh, phổ biến nhất là XML và JSON.

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

### 6.3.3. Mô hình đồ họa (Graphical Model)

Sử dụng các sơ đồ đồ họa chuẩn như UML (Unified Modeling Language) hoặc ORM (Object-Role Modeling) để trực quan hóa cấu trúc dữ liệu ngữ cảnh và các quan hệ giữa các đối tượng trong giai đoạn phân tích thiết kế hệ thống.

### 6.3.4. Mô hình dựa trên đối tượng (Object-based Model)

Mô hình hóa ngữ cảnh dựa trên các nguyên lý lập trình hướng đối tượng (OOP): đóng gói (encapsulation), kế thừa (inheritance) và đa hình (polymorphism).

trên việc phân cấp và quan hệ giữa các lớp. Mô hình này cho phép đóng gói (encapsulation) và tái sử dụng. Hầu hết các ngôn ngữ lập trình cấp cao hỗ trợ các khái niệm hướng đối tượng, mô hình hóa có thể được tích hợp vào hệ thống nhận biết ngữ cảnh một cách dễ dàng. Do đó, mô hình dựa trên đối tượng phù hợp để sử dụng bên trong mã nguồn phần mềm của từng thiết bị.

### 6.3.5. Mô hình dựa trên logic (Logic-based Model)

Biểu diễn ngữ cảnh dưới dạng các biểu thức logic vị từ (Predicate Logic) hoặc logic mệnh đề. Một tập hợp các sự kiện và quy tắc suy diễn (rules) được định nghĩa hình thức:
```prolog
inRoom(userA, roomE101).
isDark(roomE101).
lightOn(Room) :- inRoom(User, Room), isDark(Room).
```
- **Ưu điểm:** Tính hình thức toán học cao, cho phép suy luận logic chặt chẽ và kiểm tra tính nhất quán tri thức.
- **Nhược điểm:** Khó biểu diễn các dữ liệu có tính mơ hồ, không chắc chắn; độ phức tạp tính toán tăng nhanh khi tập luật lớn.

### 6.3.6. Mô hình dựa trên ontology (Ontology-based Model)

Ontology là sự đặc tả hình thức, tường minh của một khái niệm hóa chung (an explicit specification of a conceptualization). Đây là kỹ thuật mô hình hóa ngữ cảnh mạnh mẽ và toàn diện nhất hiện nay trong IoT và Web ngữ nghĩa (Semantic Web).

Ontology được mô tả bằng ngôn ngữ chuẩn W3C như OWL (Web Ontology Language) hoặc RDF (Resource Description Framework), bao gồm:
- **Classes (Lớp khái niệm):** Đại diện cho các tập hợp thực thể (ví dụ: `Device`, `Sensor`, `Person`, `Location`).
- **Object Properties (Thuộc tính đối tượng):** Mô tả quan hệ giữa hai thực thể.

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

**Bảng 6.2.** So sánh các kỹ thuật mô hình hóa ngữ cảnh

| Kỹ thuật mô hình hóa | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Khóa / Giá trị (Key-Value)** | • Đơn giản, dễ cài đặt<br>• Tốc độ truy xuất nhanh<br>• Chi phí lưu trữ nhỏ | • Không có cấu trúc phân cấp<br>• Không hỗ trợ xác thực<br>• Không thể suy luận | Ứng dụng nhỏ, lưu trữ cấu hình tạm thời |
| **Sơ đồ (Markup - XML / JSON)** | • Linh hoạt, có cấu trúc phân cấp<br>• Xác thực qua Schema<br>• Công cụ parser có sẵn rộng rãi | • Thiếu ngữ nghĩa tường minh<br>• Kích thước tệp lớn<br>• Khó biểu diễn quan hệ ngang | Trao đổi dữ liệu giữa các dịch vụ web, định dạng bản tin cảm biến (SensorML, JSON) |
| **Đồ họa (Graphical - UML)** | • Trực quan, dễ hiểu<br>• Biểu diễn quan hệ thực thể tốt<br>• Chuẩn hóa cao | • Chỉ dùng ở pha thiết kế<br>• Khó truy vấn tự động lúc chạy | Phân tích và thiết kế kiến trúc hệ thống ban đầu |
| **Dựa trên đối tượng (Object-based)** | • Đóng gói và tái sử dụng mã nguồn tốt<br>• Tích hợp tự nhiên vào ngôn ngữ OOP (Java, Python, C++) | • Khó chia sẻ giữa các hệ thống không đồng nhất<br>• Phụ thuộc ngôn ngữ | Xử lý nội bộ bên trong mã nguồn phần mềm trên thiết bị |

**Bảng 6.2.** (tiếp theo)

| Kỹ thuật mô hình hóa | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Dựa trên logic (Logic-based)** | • Hình thức toán học chặt chẽ<br>• Hỗ trợ suy luận logic chính xác<br>• Kiểm tra tính nhất quán | • Khó biểu diễn dữ liệu không chắc chắn<br>• Độ phức tạp tính toán cao khi dữ liệu lớn | Xử lý các quy tắc và ràng buộc logic hình thức |
| **Dựa trên Ontology (Ontology-based)** | • Ngữ nghĩa phong phú, biểu diễn tri thức sâu<br>• Cho phép liên tác giữa các hệ thống không đồng nhất<br>• Hỗ trợ cỗ máy suy luận tự động mạnh mẽ | • Mô tả phức tạp<br>• Chi phí tính toán và bộ nhớ cao khi suy diễn | Hệ thống IoT phức tạp, Smart Home, Smart City, chia sẻ tri thức liên miền |

## 6.4. Các kỹ thuật suy luận ngữ cảnh

Suy luận ngữ cảnh (Context Reasoning) là quá trình trích xuất thông tin mới có mức ngữ nghĩa cao hơn từ dữ liệu ngữ cảnh sẵn có. Các kỹ thuật suy luận ngữ cảnh được chia làm 6 nhóm chính:
1. Học có giám sát (Supervised Learning)
2. Học không giám sát (Unsupervised Learning)
3. Dựa trên luật (Rule-based)
4. Dựa trên logic mờ (Fuzzy Logic)
5. Dựa trên ontology (Ontology reasoning)
6. Dựa trên logic xác suất (Probabilistic Logic)

### 6.4.1. Học có giám sát (Supervised Learning)

Học có giám sát sử dụng một tập dữ liệu huấn luyện đã được gán nhãn (labeled data) để học hàm ánh xạ từ đầu vào (dữ liệu cảm biến) tới đầu ra (ngữ cảnh hành vi):
- **Phân loại (Classification):** Dự đoán đầu ra là các nhãn ngữ cảnh rời rạc (ví dụ: người dùng đang "Đi bộ", "Chạy", "Ngồi", "Nằm"). Các thuật toán thông dụng: Cây quyết định (Decision Tree), Support Vector Machine (SVM), K láng giềng gần nhất (k-NN), Mạng nơ-ron nhân tạo (ANN).
- **Hồi quy (Regression):** Dự đoán đầu ra là các giá trị liên tục (ví dụ: dự báo nhiệt độ không khí trong 1 giờ tới, ước lượng mức tiêu thụ điện năng). Các thuật toán: Hồi quy tuyến tính (Linear Regression), Hồi quy phi tuyến.

### 6.4.2. Học không giám sát (Unsupervised Learning)

Học không giám sát làm việc trên dữ liệu chưa gán nhãn (unlabeled data), tự động phân tích cấu trúc tiềm ẩn và gom nhóm các mẫu dữ liệu tương đồng:
- **Phân cụm (Clustering - K-Means, DBSCAN):** Phân chia các vị trí đo đạc cảm biến thành các vùng có đặc tính môi trường giống nhau mà không cần nhãn định trước.

sử dụng trong các ứng dụng thích ứng ngữ cảnh. Cụ thể, kỹ thuật phân cụm được sử dụng ở mức thấp (mức phần cứng) trong mạng cảm biến như định tuyến hay mức cao (mức ứng dụng) như xác định vị trí trong nhà hay ngoài trời. Kỹ thuật mạng nơ-ron không giám sát như Kohonen Self Organizing Map (KSOM) được sử dụng để phân loại dữ liệu cảm biến theo thời gian.
- **Phát hiện dị thường (Anomaly Detection):** Nhận diện các giá trị cảm biến bất thường hoặc các sự kiện nguy hiểm (như rò rỉ khí gas, xâm nhập trái phép) dựa trên độ lệch so với các cụm hoạt động bình thường.

### 6.4.3. Dựa trên luật (Rule-based Reasoning)

Suy luận dựa trên luật sử dụng tập các luật IF-THEN được định nghĩa trước bởi chuyên gia:
```
IF (Temperature > 30) AND (Presence == TRUE) THEN TurnOn(AirConditioner)
IF (SoilMoisture < 40) THEN StartPumping(Water)
```
- **Ưu điểm:** Rất trực quan, đơn giản, dễ cài đặt và thực thi rất nhanh ngay cả trên vi điều khiển nhỏ.
- **Nhược điểm:** Khó duy trì khi số lượng luật tăng lên hàng trăm luật; dễ xảy ra mâu thuẫn giữa các luật; không xử lý được các trạng thái trung gian mơ hồ.

### 6.4.4. Dựa trên logic mờ (Fuzzy Logic)

Trong thế giới thực, nhiều khái niệm không thể phân định rạch ròi đúng (1) hoặc sai (0) mà mang tính mơ hồ: thế nào là "trời nóng", "trời mát", "độ ẩm thấp". Logic mờ (Fuzzy Logic) do Lotfi Zadeh đề xuất giải quyết bài toán này bằng cách gán cho mỗi phần tử một độ liên thuộc (membership degree) nằm trong đoạn `[0, 1]`.

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

**Hình 6.5.** Quy trình suy luận mờ Mamdani

Các trường hợp suy luận mờ thực tế thông qua công cụ MATLAB Fuzzy Logic Toolbox:
- **Trường hợp 1:** Nhiệt độ vào là 16.8°C và chiều hướng nhiệt độ là Up (0.92): kết quả đầu ra rơi vào vùng Nothing (không cần tác động điều hòa vì nhiệt độ mát mẻ và đang có xu hướng tăng nhẹ về mức tối ưu).
- **Trường hợp 2:** Nhiệt độ vào là 10.5°C và chiều hướng nhiệt độ là Down (-0.85): kết quả giải mờ đầu ra kích hoạt Heating High với công suất sưởi cực đại để tránh rét hại cho cây trồng.

**Hình 6.6.** Giao diện Rule Viewer trong MATLAB Fuzzy Logic Toolbox

Giao diện Rule Viewer (Hình 6.6) cho phép trực quan hóa đồng thời tất cả các luật mờ được kích hoạt, xem diện tích phủ mờ của từng luật và điểm trọng tâm giải mờ kết quả cuối cùng.

- **Trường hợp 3:** Ta có dữ liệu đầu vào là 14.2°C, chiều hướng nhiệt độ là đang giảm (Down) thì kết quả đầu ra kích hoạt Heating High với giá trị tính toán cụ thể là 20.1%.

### 6.4.5. Dựa trên Ontology (Ontology Reasoning)

Suy luận dựa trên ontology tận dụng cấu trúc hình thức và ngữ nghĩa của OWL-DL:
- **Suy diễn quan hệ phân cấp (Subsumption Reasoning):** Tự động xác định một lớp này có phải là lớp con của lớp khác hay không dựa trên các thuộc tính ràng buộc.
- **Kiểm tra tính nhất quán (Consistency Checking):** Phát hiện các mâu thuẫn logic trong cơ sở tri thức (ví dụ: một cảm biến không thể đồng thời vừa ở trạng thái `TurnedOff` vừa phát ra giá trị `MeasuringActive`).
- **Khám phá tri thức ẩn (Implicit Knowledge Deduction):** Từ các quan hệ bắc cầu, đối xứng để suy ra các sự thật mới mà không cần lập trình viên khai báo thủ công.

### 6.4.6. Dựa trên Logic xác suất (Probabilistic Logic)

Kỹ thuật suy luận dựa trên logic xác suất (như Mạng Bayes - Bayesian Networks, Mô hình Markov ẩn - Hidden Markov Models, Lý thuyết Dempster-Shafer) cho phép hệ thống ra quyết định trong điều kiện dữ liệu cảm biến không chắc chắn, không đầy đủ hoặc chứa nhiều nhiễu.

Mỗi phát biểu hoặc trạng thái được gắn một phân phối xác suất có điều kiện $P(A|B)$ dựa trên định lý Bayes:
$$P(A|B) = 
rac{P(B|A) \cdot P(A)}{P(B)}$$

Ví dụ: Xác định xác suất một người dùng đang ngủ trong phòng dựa trên tập hợp nhiều bằng chứng: cảm biến áp lực đệm giường kích hoạt, cường độ ánh sáng bằng 0, độ ồn dưới 20dB và thời gian là ban đêm. Dù một cảm biến có thể bị lỗi, mạng Bayes vẫn tổng hợp các nguồn bằng chứng còn lại để đưa ra kết luận có độ tin cậy cao nhất.

**Bảng 6.6.** So sánh các kỹ thuật suy luận ngữ cảnh

| Kỹ thuật suy luận | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Học có giám sát (Supervised Learning)** | • Độ chính xác cao khi có nhãn<br>• Xử lý tốt dữ liệu phi tuyến tính | • Cần tập dữ liệu huấn luyện lớn có gán nhãn<br>• Tốn tài nguyên tính toán | Nhận dạng hoạt động người dùng, dự báo thời tiết, nhận diện biển số xe |
| **Học không giám sát (Unsupervised Learning)** | • Không cần dữ liệu gán nhãn<br>• Tự động phát hiện cấu trúc ẩn | • Khó đánh giá độ chính xác<br>• Ngữ nghĩa đầu ra cần chuyên gia giải thích | Phát hiện bất thường, phân cụm nút cảm biến theo vùng môi trường |
| **Dựa trên luật (Rule-based)** | • Trực quan, dễ hiểu (IF-THEN)<br>• Cài đặt đơn giản, chạy nhanh | • Phải định nghĩa luật thủ công<br>• Dễ mâu thuẫn khi số luật lớn | Điều khiển tự động theo ngưỡng cố định (bật tắt đèn, tưới nước) |
| **Logic mờ (Fuzzy Logic)** | • Xử lý tốt tính mơ hồ, không rạch ròi<br>• Gần với tư duy con người | • Phải thiết kế hàm liên thuộc thủ công<br>• Không tự thích nghi | Điều khiển hệ thống nhiệt độ, thông gió, tưới tiêu nông nghiệp |

**Bảng 6.6.** (tiếp theo)

| Kỹ thuật suy luận | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Dựa trên Ontology** | • Tận dụng tri thức ngữ nghĩa sâu sắc<br>• Tự động kiểm tra mâu thuẫn logic | • Chi phí tính toán cao<br>• Không phù hợp xử lý dữ liệu số chuỗi thời gian | Tích hợp dữ liệu ngữ cảnh đa nguồn trong Smart Home, Smart City |
| **Logic xác suất (Probabilistic Logic)** | • Xử lý xuất sắc tính không chắc chắn và dữ liệu nhiễu<br>• Kết hợp nhiều bằng chứng độc lập | • Cần biết phân phối xác suất tiên nghiệm<br>• Độ phức tạp tính toán cao | Định vị trong nhà, nhận dạng ngữ cảnh hành vi từ cảm biến nhiễu |

## 6.5. Trí tuệ nhân tạo và IoT

Sự kết hợp giữa Trí tuệ nhân tạo (AI) và Internet vạn vật (IoT) đã khai sinh ra thuật ngữ **AIoT (Artificial Intelligence of Things)**. Trong kỷ nguyên AIoT, IoT đóng vai trò là "hệ thần kinh kỹ thuật số" thu thập dữ liệu khổng lồ từ thế giới vật lý, còn AI đóng vai trò là "bộ não" phân tích thông minh và ra quyết định tự động.

Sự đột phá của các kỹ thuật Trí tuệ nhân tạo trong thập kỷ qua được đánh dấu bằng những cột mốc lịch sử:
- Tháng 3/2016, hệ thống AI AlphaGo của Google DeepMind đã làm chấn động thế giới khi đánh bại kỳ thủ cờ vây số một thế giới Lee Sedol với tỉ số 4-1.
- Năm 2017, DeepMind tiếp tục công bố AlphaGo Zero với khả năng tự học hoàn toàn từ đầu thông qua học tăng cường (Reinforcement Learning) mà không cần dữ liệu ván đấu của con người và chiến thắng áp đảo phiên bản AlphaGo tiền nhiệm.

Những bước tiến nhảy vọt này đã mở ra làn sóng ứng dụng AI mạnh mẽ vào mọi ngóc ngách của đời sống, trong đó hệ sinh thái IoT là môi trường ứng dụng giàu tiềm năng bậc nhất.

Hai nút thắt cổ chai lớn nhất của Học máy và Học sâu ở các giai đoạn trước đây là: (1) thiếu hụt tài nguyên tính toán mạnh mẽ và (2) thiếu dữ liệu lớn để huấn luyện.

Những năm gần đây, sự phát triển vượt bậc của các bộ tăng tốc phần cứng chuyên dụng như GPU (Graphics Processing Unit), TPU (Tensor Processing Unit), NPU (Neural Processing Unit) cùng với hạ tầng đám mây phân tán đã giải quyết triệt để nút thắt về năng lực tính toán. Đồng thời, hàng chục tỷ thiết bị IoT kết nối liên tục tạo ra nguồn dữ liệu lớn vô tận hàng ngày, trở thành mảnh đất màu mỡ cho các mô hình học máy phát triển.

### 6.5.1. Học máy (Machine Learning)

#### 6.5.1.1. Quá trình xử lý trong học máy

Quá trình xây dựng và triển khai một mô hình học máy trong hệ thống IoT bao gồm 5 bước tuần tự:
1. **Thu thập dữ liệu (Data Collection):** Thu thập dữ liệu cảm biến từ các thiết bị IoT.
2. **Tiền xử lý dữ liệu (Data Preprocessing):** Làm sạch dữ liệu, xử lý các giá trị khuyết thiếu, lọc nhiễu tín hiệu và chuẩn hóa thang đo dữ liệu.

3. **Trích xuất đặc trưng (Feature Extraction & Selection):** Lựa chọn các đặc trưng quan trọng nhất đại diện cho bài toán nhằm giảm số chiều dữ liệu và tăng tốc độ huấn luyện.
4. **Huấn luyện mô hình (Model Training):** Sử dụng tập dữ liệu huấn luyện (training set) và thuật toán học máy phù hợp để tối ưu hóa các tham số mô hình nhằm giảm thiểu hàm mất mát (loss function).
5. **Đánh giá mô hình (Model Evaluation):** Đánh giá độ chính xác của mô hình trên tập dữ liệu thử nghiệm độc lập (test set) thông qua các chỉ số đo lường như Accuracy, Precision, Recall, F1-Score.

**Hình 6.7.** Quy trình huấn luyện và dự đoán tổng quát trong học máy

Thuật toán học máy lấy tập dữ liệu huấn luyện và học các thuộc tính cụ thể trong đó để giảm thiểu lỗi trong quá trình đánh giá mô hình. Sau khi huấn luyện, mô hình được kiểm tra trên tập dữ liệu thử nghiệm để đánh giá hiệu quả của mô hình được chọn và dự đoán độ chính xác của mô hình khi sử dụng trong thực tế. Một mô hình có thể cho kết quả khác nhau nếu huấn luyện và thử nghiệm trên các tập dữ liệu có phân phối khác biệt, do đó việc áp dụng kỹ thuật kiểm chứng chéo (k-fold cross validation) là rất cần thiết.

**Thực thi mô hình (Inference / Deployment):** Đây là bước cuối cùng trong vòng đời học máy. Sau khi được đánh giá đạt độ chính xác yêu cầu, mô hình được triển khai vào môi trường vận hành thực tế (trên đám mây hoặc trên thiết bị biên) để thực hiện dự đoán thời gian thực khi có dữ liệu cảm biến mới gửi về.

#### 6.5.1.2. Phân loại các kỹ thuật học máy

Các thuật toán học máy được chia thành 3 nhánh chính (Hình 6.8):
1. **Học có giám sát (Supervised Learning):** Dữ liệu có nhãn đầu vào và đầu ra mong muốn. Gồm hai bài toán chính: Phân loại (Classification) và Hồi quy (Regression).
2. **Học không giám sát (Unsupervised Learning):** Dữ liệu không có nhãn. Gồm hai bài toán chính: Phân cụm (Clustering) và Giảm chiều dữ liệu (Dimensionality Reduction).
3. **Học tăng cường (Reinforcement Learning):** Tác nhân (Agent) học thông qua quá trình tương tác thử-sai với môi trường để tối đa hóa phần thưởng tích lũy (Reward).

**Hình 6.8.** Phân loại các thuật toán học máy phổ biến trong IoT

Các thuật toán học có giám sát phổ biến bao gồm: Hồi quy tuyến tính, Hồi quy Logistic, K láng giềng gần nhất (k-NN), Máy hỗ trợ véc-tơ (SVM), Naive Bayes, Cây quyết định, Rừng ngẫu nhiên (Random Forest) và Mạng nơ-ron nhân tạo sâu (Deep Neural Networks - DNN).

Đối với bài toán phân loại, đầu ra là các nhãn lớp rời rạc (ví dụ: phát hiện đám cháy hay không có cháy; nhận diện loại cây trồng). Trong khi đó, đối với bài toán hồi quy, đầu ra là các giá trị số thực liên tục (ví dụ: nồng độ bụi mịn PM2.5 dự báo trong không khí).

**Hình 6.9.** Minh họa bài toán phân lớp nhị phân bằng thuật toán SVM

Hình 6.9 minh họa bài toán phân lớp nhị phân sử dụng thuật toán Máy hỗ trợ véc-tơ (SVM). Thuật toán tìm kiếm một siêu phẳng phân cách tối ưu (optimal hyperplane) sao cho khoảng cách lề (margin) giữa hai lớp dữ liệu là lớn nhất, qua đó tăng cường khả năng tổng quát hóa của mô hình khi gặp dữ liệu mới.

### 6.5.2. Ứng dụng của học máy trong IoTs và các định hướng nghiên cứu

Với sự phát triển mạnh mẽ của cuộc cách mạng công nghiệp lần thứ tư, sự kết hợp giữa học máy và công nghệ IoT đang tạo ra những bước chuyển mình sâu sắc trong nhiều lĩnh vực:

1. **Giao thông thông minh (Smart Transportation):**
   - Đếm lưu lượng phương tiện giao thông tự động qua camera sử dụng các mô hình thị giác máy tính như YOLO, SSD.
   - Điều khiển đèn tín hiệu giao thông thích ứng dựa trên thuật toán học tăng cường nhằm giảm thiểu tình trạng ùn tắc vào giờ cao điểm.
   - Nhận diện biển số xe tự động và phát hiện các hành vi vi phạm giao thông (vượt đèn đỏ, lấn làn).

2. **Giám sát môi trường và cảnh báo thiên tai:**
   - Dự báo chất lượng không khí (chỉ số AQI, nồng độ bụi mịn PM2.5, PM10) dựa trên chuỗi thời gian sử dụng mô hình LSTM (Long Short-Term Memory).
   - Cảnh báo sớm cháy rừng thông qua phân tích dữ liệu nhiệt độ, độ ẩm và hình ảnh từ camera giám sát trên tháp quan sát.
   - Dự báo lũ quét và sạt lở đất dựa trên dữ liệu đo mưa và độ ẩm đất tự động.

3. **Nông nghiệp thông minh (Smart Agriculture):**
   - Nhận diện bệnh hại trên lá cây trồng thông qua hình ảnh chụp từ điện thoại hoặc máy bay không người lái (UAV) sử dụng mạng nơ-ron tích chập (CNN).
   - Tự động hóa lịch tưới tiêu và bón phân tối ưu dựa trên mô hình học máy phân tích nhu cầu sinh trưởng của cây trồng và điều kiện thời tiết.

4. **Thành phố thông minh và Tòa nhà thông minh (Smart Cities & Smart Buildings):**
   - Tối ưu hóa tiêu thụ năng lượng điện trong các tòa nhà văn phòng dựa trên học thói quen người dùng.
   - Giám sát bãi đỗ xe thông minh, hướng dẫn lái xe đến vị trí đỗ còn trống nhanh nhất.
   - Quản lý thu gom rác thải đô thị thông minh dựa trên cảm biến mức độ đầy của thùng rác.

**Định hướng nghiên cứu tương lai:**
- **TinyML (Machine Learning trên vi điều khiển siêu nhỏ):** Nghiên cứu nén mô hình học sâu để có thể thực thi suy luận trực tiếp trên các vi điều khiển cấp thấp có RAM dưới 256kB như ARM Cortex-M, ESP32 mà không cần kết nối mạng.
- **Học liên kết bảo vệ quyền riêng tư (Privacy-preserving Federated Learning):** Cho phép huấn luyện mô hình cộng tác giữa hàng nghìn thiết bị IoT mà không cần thu thập dữ liệu nhạy cảm của người dùng về máy chủ trung tâm.
- **Lưu trữ dữ liệu thông minh tại biên (Edge Caching & Content Delivery):** Tối ưu hóa việc phân phối nội dung video và dữ liệu số trên mạng di động 5G/6G.

các hệ thống Big Data. Sự phát triển của các thiết bị IoT/5G hỗ trợ cho việc thu thập dữ liệu hàng ngày, hàng giờ, mỗi phút hoặc thậm chí trong một phần nghìn giây. Đó là lý do tại sao chuỗi thời gian là rất lớn và nhiều chiều. Ngoài ra, loại dữ liệu này cũng không cố định, tức là nó có chu kỳ không đều và dựa vào các đặc điểm thống kê của nó như giá trị trung bình, giá trị trung vị, phương sai và sự thay đổi tiêu chuẩn theo thời gian. Do đó, làm thế nào để lưu trữ và làm thế nào để đối phó với tập dữ liệu lớn cho một vấn đề nhất định trong một thời gian thích hợp đòi hỏi sức mạnh, các phương pháp tự động để lấy thông tin quan trọng mà không phụ thuộc nhiều vào sự can thiệp của con người.

## Bài tập Chương 6

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

# Chương 7: Tái cấu hình trong IoT

## Nội dung chương

- **7.1.** Tổng quan về tái cấu hình trong IoT.
- **7.2.** Các hướng tiếp cận trong tái cấu hình IoT (5 hướng tiếp cận cốt lõi).
- **7.3.** Một số giải pháp hiện thực tái cấu hình trên các loại thiết bị phổ biến (Deluge OTA, ESP8266 OTA, Mender/Docker).
- **7.4.** Khung kiến trúc giải pháp tái cấu hình IoT đa nền tảng dựa trên SDN (SD-IoTR).
- **7.5.** Ứng dụng của chức năng tái cấu hình và các định hướng nghiên cứu.
- **Bài tập Chương 7.**


Tái cấu hình trong IoT là khả năng cho phép thay đổi tính năng, hành vi ứng dụng hoặc cấu hình hoạt động của các thiết bị IoT từ xa sau khi chúng đã được triển khai vào môi trường thực tế nhằm đáp ứng nhu cầu ngày càng cao của người sử dụng và môi trường vận hành biến đổi.

Trong thực tế triển khai các hệ thống IoT và mạng cảm biến không dây quy mô lớn (hàng trăm đến hàng nghìn nút phân bố trên các cánh đồng, trong rừng sâu hoặc gắn trong các kết cấu hạ tầng giao thông, công trình xây dựng), việc tiếp cận vật lý trực tiếp tới từng thiết bị để nạp lại phần mềm bằng dây cáp hay thay thế linh kiện là điều bất khả thi về mặt kinh tế, thời gian và công sức. Do đó, các kỹ thuật **tái lập trình qua mạng (Over-The-Air Programming - OTA)** và **tái cấu hình phần mềm động (Dynamic Software Reconfiguration)** trở thành yêu cầu sống còn.

Nội dung chương này trình bày tổng quan về các hướng tiếp cận tái cấu hình trong IoT; giới thiệu các giải pháp hiện thực OTA tiêu biểu trên các nền tảng phổ biến như TinyOS, ESP8266 và Raspberry Pi; đồng thời đề xuất khung kiến trúc tái cấu hình IoT đa nền tảng hiện đại dựa trên cách tiếp cận Mạng điều khiển bằng phần mềm (Software-Defined Networking - SDN).

Thông qua chương này, người đọc có cái nhìn tổng quan về tái cấu hình trong IoT, ý nghĩa và cơ chế hiện thực của một số giải pháp hiện có. Bên cạnh đó, thông qua minh họa phát triển một giải pháp tái cấu hình cụ thể, người đọc có thể áp dụng những kỹ năng kỹ thuật, vận dụng những kiến thức liên quan để tự xây dựng các cơ chế cập nhật từ xa cho hệ thống IoT của mình.

## 7.1. Tổng quan về tái cấu hình trong IoT

Trong vòng đời hoạt động của một hệ thống IoT, nhu cầu tái cấu hình nảy sinh từ nhiều lý do:
1. **Sửa lỗi phần mềm và vá lỗ hổng bảo mật:** Phần mềm nhúng ban đầu có thể phát sinh lỗi logic hoặc lộ các lỗ hổng bảo mật cần phải được khắc phục kịp thời.
2. **Cập nhật tính năng mới:** Người dùng hoặc nhà cung cấp dịch vụ muốn bổ sung các thuật toán xử lý dữ liệu mới, hỗ trợ thêm các loại cảm biến mới.
3. **Thích ứng với sự thay đổi của môi trường và nhiệm vụ:** Thay đổi tần suất lấy mẫu cảm biến theo mùa, chuyển đổi giao thức định tuyến khi tô-pô mạng thay đổi, hoặc thay đổi ngưỡng kích hoạt cảnh báo.
4. **Tối ưu hóa năng lượng:** Điều chỉnh chu kỳ thức-ngủ (duty cycle) của nút mạng khi pin sắp cạn để kéo dài tối đa thời gian sống của mạng.

## 7.2. Các hướng tiếp cận trong tái cấu hình IoT

Dựa trên mức độ trừu tượng hóa và dung lượng dữ liệu cần truyền tải qua mạng không dây, các kỹ thuật tái cấu hình trong IoT được chia thành 5 hướng tiếp cận chính:
1. Hướng tiếp cận thay thế toàn bộ image (Full Image Replacement)
2. Hướng tiếp cận dựa trên module (Module-based Approach)
3. Hướng tiếp cận dựa trên cơ sở dữ liệu (Database-based Approach)
4. Hướng tiếp cận máy ảo (Virtual Machine-based Approach)
5. Hướng tiếp cận hướng tới dịch vụ (Service-Oriented Approach)

**Hình 7.1.** Các hướng tiếp cận tái cấu hình trong IoT

### 7.2.1. Hướng tiếp cận thay thế toàn bộ image

Là cơ chế truyền tải và thay thế toàn bộ một tệp ảnh nhị phân nhúng (binary firmware image) đang chạy trên thiết bị IoT qua sóng vô tuyến (OTA). Một dịch vụ điển hình đã hiện thực cơ chế này trên thiết bị cảm biến không dây là giao thức **Deluge** trên TinyOS [18].

Trong hướng tiếp cận này, chương trình mới được biên dịch hoàn chỉnh tại máy chủ thành tệp nhị phân duy nhất. Tệp này sau đó được chia nhỏ thành các gói tin và lan truyền qua mạng không dây tới các nút cảm biến. Tại mỗi nút, ảnh nhị phân mới được ghi tạm vào bộ nhớ Flash ngoài. Sau khi toàn bộ ảnh được tải về và kiểm tra tính toàn vẹn (qua mã CRC/SHA), bộ nạp khởi động (bootloader) sẽ chép ảnh mới vào bộ nhớ Flash trong của vi điều khiển và khởi động lại thiết bị.

- **Ưu điểm:** Độ tin cậy rất cao, đơn giản về mặt kiến trúc; cho phép thay đổi toàn bộ hệ điều hành và ngăn xếp mạng; không phụ thuộc vào ngôn ngữ lập trình.
- **Nhược điểm:** Kích thước tệp truyền qua mạng rất lớn (vài chục đến vài trăm kB), tiêu tốn nhiều năng lượng truyền thông không dây của các nút cảm biến; thời gian cập nhật mạng lâu.

**Hình 7.2.** Quy trình nạp ảnh toàn phần OTA

### 7.2.2. Hướng tiếp cận dựa trên module

Thay vì thay thế toàn bộ phần mềm, hướng tiếp cận này chỉ truyền tải các module phần mềm nhị phân cần cập nhật (dạng tệp mã đối tượng ELF hoặc thư viện liên kết động). Cơ chế nạp động (Dynamic Loader) trên hệ điều hành sẽ liên kết nóng module mới vào không gian bộ nhớ đang chạy.

sao chép các native code được liên kết vào một nơi trong bộ nhớ mà ở đó chương trình có thể thực thi. Hình 7.3 mô tả kiến trúc bộ nhớ trong Contiki OS [19], giải thích vì sao hệ điều hành này có thể hỗ trợ cơ chế nạp module động. Không gian phần "Loaded program" chính là nơi các chương trình được nạp vào bộ nhớ RAM/Flash để thực thi mà không làm gián đoạn phần còn lại của nhân hệ điều hành.

**Hình 7.3.** Kiến trúc tái cấu hình dựa trên module [19]

- **Ưu điểm:** Kích thước gói tin cập nhật nhỏ hơn nhiều so với Full Image (chỉ từ 1kB đến vài kB), tiết kiệm đáng kể năng lượng vô tuyến và thời gian nạp mạng.
- **Nhược điểm:** Đòi hỏi hệ điều hành phải hỗ trợ bảng ký hiệu (symbol table) và cơ chế liên kết động phức tạp; có nguy cơ phân mảnh bộ nhớ RAM sau nhiều lần nạp/gỡ module.

### 7.2.3. Hướng tiếp cận cơ sở dữ liệu (Database-based Approach)

Trong hướng tiếp cận này, toàn bộ mạng cảm biến không dây được trừu tượng hóa như một bảng cơ sở dữ liệu phân tán khổng lồ (Virtual Database Table), trong đó mỗi hàng đại diện cho một nút cảm biến và mỗi cột đại diện cho một loại cảm biến (nhiệt độ, ánh sáng, độ ẩm) hoặc thuộc tính của nút (mức pin, định danh nút).

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

Các hệ thống trao đổi thông điệp Publish-Subscribe thông thường bao gồm ba thành phần:
1. **Publisher (Bên phát hành):** Sản xuất và phát hành các sự kiện dữ liệu (ví dụ: nhiệt độ phòng đo được bởi nút cảm biến không dây).
2. **Subscriber (Bên đăng ký):** Các ứng dụng hoặc thiết bị người dùng đăng ký nhận các chủ đề dữ liệu mà mình quan tâm.
3. **Broker (Bộ môi giới / Gateway):** Điểm trung tâm tiếp nhận thông điệp từ Publisher, lọc theo chủ đề (topic) và chuyển tiếp tới các Subscriber tương ứng.

Việc tái cấu hình trong mô hình này được thực hiện thông qua việc thay đổi các bộ lọc đăng ký (subscription filters) tại Broker hoặc gửi các thông điệp điều khiển cấu hình qua các kênh điều khiển chuyên dụng.

**MOSDEN Middleware** [22] là một giải pháp trung gian IoT tiêu biểu hỗ trợ cơ chế này trên các thiết bị di động và gateway có tài nguyên hạn chế.

các sự kiện cụ thể của hệ thống. Mỗi client được phân biệt bằng một số điện thoại (phone number) hoặc UUID. Gateway đóng vai trò event-broker trong mô hình Publish-Subscribe. Mỗi gateway sẽ nhận thông tin từ nhiều nút cảm biến (publisher). Các thông tin này sẽ được phân loại vào những kênh được quy định trước (predefined channels). Sau đó, tương ứng với mỗi kênh, gateway sẽ thông báo tới các subscriber đã đăng ký.

### 7.2.4. Hướng tiếp cận máy ảo (Virtual Machine-based Approach)

Hướng tiếp cận này cài đặt một máy ảo siêu nhỏ (Bytecode Virtual Machine) chạy trực tiếp trên vi điều khiển của nút cảm biến (nằm phía trên hệ điều hành nhúng). Các chương trình ứng dụng được biên dịch thành các chỉ lệnh mã byte (bytecode) nhỏ gọn để máy ảo thông dịch thực thi.

Đại diện tiêu biểu nhất cho hướng tiếp cận này là máy ảo **Maté** [18] chạy trên nền hệ điều hành TinyOS. Maté là một máy ảo hướng tới bối cảnh sự kiện dựa trên điều khiển (context-based event-driven virtual machine) với một chồng quy ước gọi hàm dựa trên ngăn xếp (stack-based calling convention).

**Hình 7.5.** Kiến trúc tái cấu hình dựa trên máy ảo VM

Máy ảo Maté tổ chức mã thực thi thành các viên nang (capsules) độc lập, mỗi capsule có kích thước cố định chỉ 24 byte (chứa tối đa 24 chỉ lệnh bytecode):
- **Capsule thông điệp (Message Capsule):** Chạy khi có gói tin mạng đến.
- **Capsule bộ định thời (Timer Capsule):** Chạy khi bộ định thời kích hoạt.
- **Capsule chương trình con (Subroutine Capsule):** Thực thi các hàm tính toán dùng chung.

Nhờ tập lệnh bytecode ngắn gọn được thiết kế riêng cho mạng cảm biến (chỉ thị đọc cảm biến, gửi gói tin, bật đèn LED chỉ tốn 1 byte mã lệnh), các chương trình phức tạp có thể được mã hóa thành các tệp tin có kích thước dưới 100 byte.

cho phép các chương trình phức tạp có thể hiện thực với mã nguồn kích thước rất nhỏ (ít hơn 100 bytes). Điều này cho phép các nhà lập trình ứng dụng có thể tái cấu hình một mạng lưới rộng lớn các nút một cách hiệu quả, giảm chi phí truyền tải một chương trình mới đến các nút qua sóng vô tuyến.

- **Ưu điểm:** Kích thước truyền nạp siêu nhỏ, lan truyền cập nhật mạng cực nhanh, an toàn cao (mã bytecode chạy trong môi trường sandbox của máy ảo nên không thể gây treo hệ thống hay xung đột bộ nhớ).
- **Nhược điểm:** Tốc độ thực thi chậm hơn so với mã máy gốc (native code) do phải thông qua bước thông dịch; tốn thêm dung lượng bộ nhớ RAM và Flash của nút để chứa chương trình máy ảo.

### 7.2.5. Hướng tiếp cận hướng tới dịch vụ (Service-Oriented Approach)

Trong hướng tiếp cận hướng dịch vụ (SOA), mỗi thiết bị IoT đóng vai trò là một nhà cung cấp dịch vụ (Service Provider) hoặc người tiêu thụ dịch vụ (Service Consumer). Các chức năng của thiết bị (đo nhiệt độ, điều khiển van tưới, định tuyến mạng) được trừu tượng hóa và đóng gói thành các dịch vụ web gọn nhẹ (CoAP, RESTful HTTP).

**Hình 7.6.** Kiến trúc tái cấu hình hướng dịch vụ

Hệ thống trung gian IoT (IoT Middleware) quản lý danh mục dịch vụ (Service Registry). Khi cần tái cấu hình hệ thống, người quản trị chỉ cần thay đổi quy trình kết hợp dịch vụ (Service Orchestration / Composition) hoặc nạp thêm các dịch vụ mới mà không làm ảnh hưởng đến các dịch vụ đang hoạt động khác.

## 7.3. Một số giải pháp hiện thực tái cấu hình trên các loại thiết bị phổ biến

### 7.3.1. Cơ chế hỗ trợ tái lập trình từ xa trên TinyOS

Trên hệ điều hành TinyOS, giao thức tái lập trình mạng nổi tiếng nhất là **Deluge T2** [18]. Deluge là giao thức lan truyền dữ liệu tin cậy (reliable data dissemination) được thiết kế đặc biệt để phân phối các tệp ảnh nhị phân kích thước lớn qua mạng cảm biến không dây đa chặng (multi-hop WSN).

**Hình 7.7.** Quy trình truyền nạp Deluge trong TinyOS

**Một số đặc điểm kỹ thuật nổi bật của giao thức Deluge:**
1. **Thuật toán Trickle thích ứng mật độ (Density-aware Trickle Algorithm):** Deluge sử dụng cơ chế quảng bá thông điệp tóm tắt (Advertisement - ADV) dựa trên bộ định thời thích ứng Trickle. Khi mạng ổn định, chu kỳ phát ADV tăng theo cấp số nhân để tiết kiệm tối đa năng lượng vô tuyến. Khi phát hiện một nút có phiên bản ảnh mới hơn, chu kỳ Trickle lập tức được thu ngắn lại về mức mili-giây để nhanh chóng cập nhật cho toàn mạng.
2. **Cơ chế ức chế truyền trùng lặp (Suppression Mechanism):** Nếu một nút nghe thấy nhiều láng giềng đã gửi bản tin ADV hoặc yêu cầu tương tự trong chu kỳ hiện tại, nó sẽ tự động ức chế (không phát lại) để tránh va chạm và nghẽn kênh truyền.

3. **Phân trang dữ liệu (Data Paging):** Một đối tượng dữ liệu nhị phân lớn ($S_{obj}$) được chia thành nhiều trang (Pages) có kích thước cố định (ví dụ 1024 byte), và mỗi trang được chia tiếp thành các gói tin nhỏ ($S_{pkt}$, khoảng 23 byte) để vừa với khung truyền IEEE 802.15.4.
   - Các nút mạng phải hoàn thành việc nhận và kiểm tra toàn vẹn toàn bộ các gói tin của Trang $i$ trước khi chuyển sang yêu cầu Trang $i+1$. Cơ chế này giúp các nút cảm biến chỉ cần duy trì một vùng đệm RAM nhỏ cho một trang đơn lẻ thay vì phải giữ toàn bộ ảnh nhị phân trong bộ nhớ.
4. **Cơ chế an toàn Golden Image:** Bộ nhớ Flash ngoài của mote cảm biến được dành riêng một phân vùng lưu trữ phiên bản phần mềm chuẩn xuất xưởng (Golden Image). Nếu quá trình nạp ảnh mới bị gián đoạn do hết pin hoặc ảnh mới bị lỗi không khởi động được, hệ thống sẽ tự động khôi phục lại Golden Image để đảm bảo nút mạng không bao giờ bị "biến thành cục gạch" (bricked).

Trong các giải pháp hiện đại, một máy tính nhúng nhỏ gọn như **Raspberry Pi** thường được cấu hình chạy môi trường TinyOS đóng vai trò là trạm gốc (Base Station Gateway) kết nối qua cổng USB với nút điều phối Coordinator. Raspberry Pi nhận các tệp ảnh nhị phân biên dịch từ đám mây qua Wi-Fi/Ethernet và tự động kích hoạt tiến trình nạp Deluge xuống mạng cảm biến.

### 7.3.2. Cơ chế tái lập trình từ xa trên ESP8266

Họ vi điều khiển ESP8266 và ESP32 của Espressif Systems được tích hợp sẵn ngăn xếp Wi-Fi và TCP/IP, cung cấp khả năng cập nhật phần mềm không dây (OTA) cực kỳ mạnh mẽ và tiện lợi trong môi trường Arduino IDE và ESP-IDF.

Hiện tại, trong hệ thống phần mềm và kho thư viện lập trình của ESP8266 trên nền tảng Arduino có 3 phương pháp tái cấu hình, cập nhật OTA từ xa qua mạng:
1. **Arduino IDE OTA:** Nạp mã trực tiếp từ máy tính của lập trình viên qua giao thức mạng nội bộ LAN tới thiết bị ESP8266 mà không cần cắm cáp USB.
2. **Web Browser OTA:** ESP8266 khởi tạo một Web Server nội bộ; người dùng truy cập địa chỉ IP của ESP8266 qua trình duyệt web trên điện thoại hoặc máy tính, chọn tệp nhị phân `.bin` và bấm nút Upload để nạp chương trình mới.
3. **HTTP Server Auto-Update (OTA qua máy chủ đám mây):** ESP8266 định kỳ gửi yêu cầu HTTP GET đến máy chủ web trung tâm kiểm tra phiên bản phần mềm. Nếu có phiên bản mới hơn, thiết bị tự động tải tệp nhị phân về và nạp vào bộ nhớ.

**Hình 7.8.** Cơ chế phân vùng Flash hỗ trợ OTA trên ESP8266

**Cơ chế phân vùng bộ nhớ Flash (Dual-Bank OTA):**

Bộ nhớ Flash của ESP8266 được phân chia thành hai vùng lưu trữ ứng dụng riêng biệt có kích thước bằng nhau:
- **Phân vùng Sketch 1 (OTA slot 0)**
- **Phân vùng Sketch 2 (OTA slot 1)**

**Hình 7.9.** Quy trình cập nhật OTA trên ESP8266 qua Web Server

Khi thiết bị đang chạy chương trình từ Phân vùng 1, tệp nhị phân mới tải về sẽ được ghi tuần tự vào Phân vùng 2. Sau khi ghi xong và xác thực mã kiểm tra MD5 thành công, cờ nạp khởi động (boot flag) trong bộ nhớ RTC/EEPROM sẽ được chuyển sang chỉ định Phân vùng 2. Thiết bị tự khởi động lại và chạy chương trình mới. Nếu quá trình ghi bị ngắt quãng, thiết bị vẫn khởi động an toàn từ Phân vùng 1 cũ.

### 7.3.3. Cơ chế tái cấu hình từ xa trên Raspberry Pi

Đối với các thiết bị máy tính nhúng mạnh mẽ chạy hệ điều hành Linux như Raspberry Pi, việc tái cấu hình có thể thực hiện ở hai mức độ:
1. **Mức hệ điều hành và Firmware (Full OS OTA):** Sử dụng các nền tảng quản lý cập nhật hệ thống nhúng chuyên nghiệp như **Mender** [23] hoặc **balenaOS**.
2. **Mức ứng dụng và dịch vụ:** Sử dụng công nghệ ảo hóa nhẹ **Docker Containers** kết hợp các công cụ quản lý cấu hình tự động như **Ansible**.

**Giải pháp cập nhật hệ điều hành Mender:**

Mender là nền tảng mã nguồn mở quản lý cập nhật OTA cho hệ điều hành Linux nhúng. Mender áp dụng kiến trúc cập nhật **A/B Dual Rootfs Partitioning**:
- Ổ đĩa lưu trữ (thẻ nhớ MicroSD hoặc eMMC) được chia thành 2 phân vùng hệ thống tệp gốc: `rootfsA` và `rootfsB`.
- Thiết bị đang hoạt động trên `rootfsA`. Khi có bản cập nhật mới từ Mender Server, tệp ảnh hệ thống mới sẽ được ghi vào `rootfsB`.
- Bộ nạp khởi động U-Boot được cấu hình thử khởi động vào `rootfsB`. Nếu hệ thống khởi động thành công và xác nhận dịch vụ mạng hoạt động bình thường, phân vùng B sẽ trở thành phân vùng hoạt động chính thức. Nếu khởi động thất bại hoặc dịch vụ bị lỗi, U-Boot tự động quay ngược (rollback) về phân vùng A, đảm bảo tính liên tục tuyệt đối của hệ thống.

**Giải pháp tái cấu hình mức dịch vụ bằng Docker Containers trên Raspberry Pi:**

Thay vì cập nhật toàn bộ hệ điều hành cồng kềnh (hàng trăm MB đến vài GB), giải pháp hiện đại là đóng gói từng ứng dụng IoT (dịch vụ đọc cảm biến, dịch vụ gateway MQTT, dịch vụ phân tích AI) vào các Docker Container riêng biệt chạy trên Raspbian OS.

**Hình 7.10.** Kiến trúc tái cấu hình trên Raspberry Pi sử dụng Ansible/Docker

- Khi cần cập nhật tính năng mới hoặc sửa lỗi, người quản trị chỉ cần đẩy (push) image container mới lên Docker Hub hoặc máy chủ lưu trữ riêng.
- Một tiến trình quản trị trên Raspberry Pi (hoặc công cụ Ansible/Docker Compose) nhận lệnh và tự động tải image mới về, dừng container cũ và khởi chạy container mới chỉ trong vài giây mà không cần khởi động lại bo mạch Raspberry Pi.

Một điểm quan trọng khác là Docker là một nền tảng mã nguồn mở, chính vì thế Docker được cộng đồng phát triển mạnh mẽ để đóng góp và mở rộng khả năng của nó cho phù hợp với các nhu cầu ngày càng cao. Gần đây, trong nhiều nghiên cứu về phát triển hạ tầng IoT đa nền tảng, đảm bảo khả năng đáp ứng linh hoạt các yêu cầu khác nhau, công cụ ảo hóa Docker đang trở thành tiêu chuẩn thực tế.

## 7.4. Khung kiến trúc phát triển một giải pháp tái cấu hình IoT đa nền tảng dựa trên cách tiếp cận SDN

### 7.4.1. Kiến trúc quản lý hệ thống IoT dựa trên SDN

Mạng điều khiển bằng phần mềm (Software-Defined Networking - SDN) là mô hình mạng tiên tiến phân tách rạch ròi giữa:
- **Mặt phẳng điều khiển (Control Plane):** Tập trung hóa logic định tuyến, quản lý cấu hình và ra quyết định thông minh vào bộ điều khiển trung tâm (SDN Controller).
- **Mặt phẳng chuyển tiếp dữ liệu (Data Plane):** Các thiết bị mạng chỉ thực hiện chuyển tiếp gói tin thuần túy theo các bảng luật (Flow Tables) được chỉ định bởi bộ điều khiển.

Mạng cận biên (edge network) bao gồm một lượng lớn các thiết bị IoT đầu cuối như cảm biến, động cơ, thiết bị di động... Những thiết bị này thu thập dữ liệu và sau đó gửi về thiết bị cổng, máy trạm (gateway) trong vùng mạng truy cập. Để có thể giải quyết nhu cầu về khả năng đáp ứng, khả năng lập trình lại, những thiết bị này thường chạy những dịch vụ hỗ trợ khả năng cấu hình mềm dẻo.

**Hình 7.11.** Kiến trúc quản lý hệ thống IoT dựa trên SDN

Việc áp dụng SDN vào IoT mang lại khả năng tái cấu hình linh hoạt:
- **Tập trung hóa quản trị:** Người quản trị có thể giám sát toàn bộ trạng thái mạng và cập nhật chính sách phân phối dữ liệu từ một vị trí trung tâm duy nhất.
- **Tái cấu hình luồng dữ liệu mềm dẻo:** Thay đổi đường truyền gói tin, ưu tiên chất lượng dịch vụ (QoS) cho các gói tin cảnh báo khẩn cấp mà không cần thay đổi phần cứng thiết bị mạng.

thực và thử nghiệm cách làm quản lý tập trung, lập trình lại cho kiến trúc IoT ở mức độ vùng mạng cận biên (edge network) và vùng mạng truy cập (access network).

### 7.4.2. Khung kiến trúc xây dựng giải pháp tái cấu hình IoT (SD-IoTR)

Giải pháp kiến trúc **SD-IoTR (Software-Defined IoT Reconfiguration Framework)** được đề xuất nhằm hỗ trợ tái cấu hình đồng nhất cho các hệ thống IoT đa nền tảng (kết hợp đồng thời giữa các nút cảm biến TinyOS, nút vi điều khiển ESP8266/Arduino và các gateway Raspberry Pi).

Khung kiến trúc SD-IoTR bao gồm 3 lớp phân cấp theo chiều dọc (Hình 7.12):
1. **Lớp hệ thống (System / Device Layer):** Bao gồm các nút cảm biến và gateway vật lý, cài đặt các agent tái cấu hình tương ứng với từng nền tảng phần cứng (Deluge Agent trên TinyOS, OTA Handler trên ESP8266, Docker Daemon trên Raspberry Pi).
2. **Lớp trung gian (Middleware / Control Layer):** Là trung tâm điều khiển trung tâm (SD-IoTR Controller), tiếp nhận các yêu cầu tái cấu hình từ tầng trên, biên dịch thành các lệnh điều khiển cụ thể cho từng loại thiết bị và giám sát tiến trình cập nhật.
3. **Lớp ứng dụng (Application Layer):** Cung cấp giao diện đồ họa web cho người quản trị thực hiện quản lý danh mục thiết bị, giám sát trạng thái mạng và phát lệnh cập nhật phần mềm.

**Hình 7.12.** Khung kiến trúc tái cấu hình đa nền tảng SD-IoTR

Lớp trung gian Middleware cung cấp các bộ điều khiển logic:
- **Device Manager:** Quản lý vòng đời và thông tin cấu hình phần cứng của từng nút.
- **Reconfiguration Engine:** Quyết định chiến lược tái cấu hình phù hợp nhất cho từng thiết bị (chọn nạp Full Image, nạp Module hay nạp Container tùy theo tài nguyên thiết bị).
- **Security & Verification Module:** Ký số các bản cập nhật phần mềm và kiểm tra tính toàn vẹn nhằm ngăn chặn việc kẻ tấn công nạp mã độc vào hệ thống IoT.

Hệ thống cung cấp tập hợp các giao diện lập trình ứng dụng RESTful APIs phong phú để các ứng dụng ở tầng trên có thể kích hoạt quá trình tái cấu hình:
- `POST /api/v1/devices/{id}/firmware`: Phát lệnh cập nhật firmware từ xa cho thiết bị có định danh `{id}`.
- `GET /api/v1/devices/{id}/status`: Kiểm tra trạng thái tiến độ nạp mã hiện tại.
- `POST /api/v1/containers/{id}/restart`: Khởi động lại hoặc cập nhật container dịch vụ trên gateway.
- `POST /api/v1/network/rules`: Cập nhật bảng luật định tuyến luồng dữ liệu SDN cho toàn mạng.

giao tiếp chủ yếu bằng các REST APIs. HTTP REST được hiện thực mang đến khả năng giao tiếp dựa trên nền tảng web giữa các ứng dụng IoT cụ thể với hệ thống điều khiển ở trung tâm. Bên cạnh đó, giao thức MQTT với cơ chế Publish/Subscribe cũng được sử dụng kết hợp để gửi các bản tin đánh thức và kích hoạt nạp mã tức thời tới hàng nghìn thiết bị phân tán.

## 7.5. Ứng dụng của chức năng tái cấu hình trong hệ thống IoT và các định hướng nghiên cứu

Khả năng tái cấu hình từ xa mở ra nhiều ứng dụng thiết thực và quan trọng:
1. **Bảo trì và vận hành hệ thống quy mô lớn tự động:** Cập nhật đồng loạt hàng nghìn thiết bị đo đếm điện tử thông minh (Smart Metering) trên toàn quốc mà không cần cử nhân viên kỹ thuật tới từng hộ gia đình.
2. **Thích ứng với sự cố mạng và tiết kiệm năng lượng:** Tự động điều chỉnh cấu trúc mạng tô-pô khi có một số nút trung gian bị hết pin, chuyển giao vai trò Cluster Head cho các nút còn nhiều năng lượng hơn.

3. **Thay đổi dịch vụ mạng, kiến trúc, kết nối mạng từ xa:** Ngày nay, khi IoT được ứng dụng và triển khai trong nhiều lĩnh vực khác nhau, kiến trúc mạng của hệ thống IoT thường rất phức tạp và triển khai với quy mô lớn. Chính vì thế, các công nghệ mạng hiện đại như SDN/NFV cho phép thực hiện việc cấu hình kết nối mạng từ xa, thay đổi các chức năng mạng, dịch vụ mạng một cách tiện lợi mang lại nhiều ý nghĩa trong việc vận hành và tối ưu hệ thống.

## Bài tập Chương 7

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

# Kết luận

Trong cuốn sách này, chúng tôi đã tập trung vào những nội dung sau:

**Chương 1:** Trình bày tổng quan về công nghệ Internet vạn vật (IoT), các xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam. Trong đó, chúng tôi đặc biệt chú trọng đến quy chuẩn về IoT của các tổ chức hoặc liên minh quốc tế nhằm cung cấp đến người đọc, đặc biệt là sinh viên kiến thức về các tiêu chuẩn IoT. Mục tiêu là để định hướng khi thiết kế và phát triển các ứng dụng và giải pháp IoT có tính tương thích (compatibility) và sẵn sàng cao (portability).

**Chương 2:** Trình bày các lĩnh vực và ứng dụng IoT cụ thể nhằm giới thiệu đến sinh viên các ứng dụng IoT thực tế. Để tăng tính thực tiễn, chúng tôi cũng đã giới thiệu các ứng dụng IoT đã và đang triển khai ở Trường Đại học Công nghệ Thông tin – Đại học Quốc gia TP.HCM, ví dụ như trạm quan trắc môi trường SmartCity đặt trong khuôn viên Trường Đại học CNTT.

**Chương 3:** Trình bày các kiến trúc mạng khác nhau được sử dụng trong việc kiến thiết mạng IoT như kiến trúc cây (Tree), kiến trúc vòng (Ring), kiến trúc chuỗi (Chain), kiến trúc không cần hạ tầng (Mesh). Các bộ giao thức mạng IoT phổ dụng cũng đã được giới thiệu chi tiết về kiến trúc và cách vận hành. Trong khi bộ giao thức ZigBee đại diện cho xu hướng giao thức IoT chạy độc lập, và do đó muốn kết nối đến thiết bị đầu cuối từ mạng Internet cần thông qua một Internet gateway, bộ giao thức 6LoWPAN đại diện cho xu hướng mở rộng mạng IP (Spanning IP), tức là có thể truy cập và điều khiển trực tiếp thiết bị IoT từ Internet.

**Chương 4:** Trình bày về các nền tảng phần cứng và phần mềm phổ dụng để phát triển các ứng dụng và giải pháp IoT hiện nay. Chúng tôi giới thiệu chủ yếu các nền tảng phần cứng dễ dàng làm việc với các nền tảng mã nguồn mở (open-source

platforms) và có sẵn ở Việt Nam với giá thành hợp lý, từ đó sinh viên có thể dễ dàng phát triển sản phẩm và làm chủ công nghệ.

**Chương 5:** Trình bày về các công nghệ nền, bao gồm điện toán đám mây (cloud computing) và tính toán cận biên (edge computing). Đây là các công nghệ nền phát triển hiện nay để hiện thực hoàn chỉnh giải pháp phần backend hoặc edge của giải pháp IoT. Chúng tôi cũng đã giới thiệu giải pháp ứng dụng điện toán đám mây để phát triển hệ thống giả lập mạng cảm biến không dây quy mô lớn trên nền tảng OpenStack.

**Chương 6:** Trình bày các khái niệm cơ bản về ngữ cảnh, quản lý ngữ cảnh thông minh và ứng dụng của trí tuệ nhân tạo, học máy trong IoT. Các kỹ thuật mô hình hóa ngữ cảnh và suy luận ngữ cảnh (như logic mờ, học máy) được phân tích chi tiết nhằm trang bị cho sinh viên năng lực xây dựng các hệ thống IoT có khả năng tự nhận thức và thích ứng thông minh với môi trường.

**Chương 7:** Trình bày về các kỹ thuật tái cấu hình và tái lập trình từ xa (OTA) trong IoT. Phân tích các hướng tiếp cận tái cấu hình từ mức nạp ảnh nhị phân, nạp module, nạp bytecode máy ảo cho đến nạp container trên các thiết bị phổ biến như TinyOS, ESP8266 và Raspberry Pi, cùng khung kiến trúc SDN hỗ trợ quản lý và tái cấu hình mạng IoT đa nền tảng tập trung.

Mặc dù đã có những bước tiến vượt bậc, nhiều thách thức kỹ thuật lớn trong lĩnh vực IoT vẫn đang là các chủ đề nghiên cứu mở đầy sôi động:

- **Vấn đề bảo mật và quyền riêng tư (Security & Privacy):** Bên cạnh tính riêng tư, tính bảo mật cho ứng dụng IoT cũng là một vấn đề lớn đang được nghiên cứu. Các kỹ thuật bảo mật truyền thống khó có thể được triển khai trực tiếp trên các thiết bị IoT bởi vì như đã trình bày trong Chương 4, các thiết bị IoT hầu như là các thiết bị nhúng có năng lực tính toán, bộ nhớ và năng lượng tiêu thụ thấp. Một số rủi ro bảo mật chính gồm: nghe lén trên đường truyền vô tuyến, giả mạo nút mạng, chiếm quyền điều khiển thiết bị cơ cấu chấp hành và tấn công từ chối dịch vụ (DDoS) thông qua mạng botnet IoT.
- **Tiêu chuẩn hóa và tính liên tác (Standardization & Interoperability):** Sự phân mảnh của hàng trăm chuẩn kết nối và nền tảng phần mềm khác nhau từ các nhà sản xuất đòi hỏi các chuẩn giao tiếp chung ở mức ngữ nghĩa (như Web of Things - WoT của W3C) để các thiết bị có thể tự động khám phá và liên tác không rào cản.
- **Công nghệ mạng 5G và 6G trong IoT:** Hỗ trợ kết nối mật độ siêu lớn (massive Machine-Type Communications - mMTC) và truyền thông độ trễ cực thấp độ tin cậy cực cao (Ultra-Reliable Low-Latency Communications - URLLC) mở ra tương lai cho các hệ thống xe tự hành thông minh và phẫu thuật y tế từ xa.

- **Học sâu và Trí tuệ nhân tạo trên thiết bị biên (Edge AI / TinyML):** Để giảm kích thước sử dụng bộ nhớ, các hệ điều hành IoT thường được tối giản các chức năng và sử dụng thư viện bên thứ ba ở mức tối thiểu, trong khi đó các ứng dụng Học sâu lại yêu cầu tài nguyên cao và sử dụng năng lượng nhiều. Do đó, việc nghiên cứu tối ưu hóa các thuật toán học máy, lượng tử hóa mô hình để có thể chạy suy luận thời gian thực trực tiếp trên các vi điều khiển công suất thấp mà vẫn đảm bảo độ chính xác cao là một trong những định hướng nghiên cứu then chốt trong giai đoạn hiện nay.

Cuốn giáo trình này được biên soạn với mong muốn cung cấp một tài liệu học tập, tham khảo có hệ thống, kết hợp hài hòa giữa lý thuyết nền tảng và hướng dẫn thực hành thực tiễn cho sinh viên ngành Công nghệ Thông tin, Kỹ thuật Máy tính, Điện tử Viễn thông và các kỹ sư đang nghiên cứu, phát triển trong lĩnh vực Internet of Things.

# Tài liệu tham khảo

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

36. Abu Sufian, Aniruddha Ghosh, Ali Safaa Sadiq, Florentin Smarandache, "A Survey on Deep Transfer Learning to Edge Computing for Mitigating the COVID-19 Pandemic", *Journal of Systems Architecture*, tập 108, tr. 101830, 2020.
37. W. Y. B. Lim et al., "Federated Learning in Mobile Edge Networks: A Comprehensive Survey", *IEEE Communications Surveys & Tutorials*, tập 22, số 3, pp. 2031-2063, 2020.
38. Jie Tang, Dawei Sun, Shaoshan Liu và Jean-Luc Gaudiot, "Enabling Deep Learning on IoT Devices", *Computer*, tập 50, số 6, pp. 92-96, 2017.

# Thông tin xuất bản

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

*(Trang bìa sau của sách giáo trình)*
