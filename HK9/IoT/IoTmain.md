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
# Chương 3: Các kiến trúc mạng và bộ giao thức IoT

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
## 3.7: Các bộ giao thức mạng không dây thường dùng trong IoT
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
## 3.8: IoT Sensors (*Cảm biến IoT*)
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
## 3.9: RFID
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
## 3.10: Video Tracking 
- Video tracking is the process of capturing and analyzing the video feeds, frame by frame, of a particular object or person over a short time interval. It is used to measure and analyze movements, visual attention, as well as behavior. Video tracking is used for customer identification, surveillance, augmented reality, traffic control, and medical imaging. (*Theo dõi video là quá trình thu thập và phân tích các luồng video, từng khung hình, của một đối tượng hoặc cá nhân cụ thể trong khoảng thời gian ngắn. Nó được sử dụng để đo lường và phân tích chuyển động, sự chú ý thị giác, cũng như hành vi. Theo dõi video được sử dụng để nhận dạng khách hàng, giám sát, thực tế tăng cường, kiểm soát giao thông và hình ảnh y tế.*)
- It is yet another mechanism to identify and monitor “things” when sensors or RFID tags are not available. Video tracking may also be used in conjunction with sensors and/or RFID to provide a more comprehensive solution. (*Nó là một cơ chế khác để xác định và giám sát “vật” khi cảm biến hoặc thẻ RFID không có sẵn. Theo dõi video cũng có thể được sử dụng kết hợp với cảm biến và/hoặc RFID để cung cấp một giải pháp toàn diện hơn.*)
## 3.11: IoT Actuators
-  An actuator is a type of motor that is responsible for controlling or taking action in a system. It takes a source of data or energy (e.g., hydraulic fluid pressure, other sources of power) and converts the data/energy to motion to control a system. (*Actuator là một loại động cơ chịu trách nhiệm kiểm soát hoặc thực hiện hành động trong một hệ thống. Nó lấy một nguồn dữ liệu hoặc năng lượng (ví dụ: áp suất chất lỏng thủy lực, các nguồn năng lượng khác) và chuyển đổi dữ liệu/năng lượng đó thành chuyển động để điều khiển một hệ thống.*)
- Mechanical Linear Actuators: Mechanical actuators convert rotary motion to linear motion. Devices such as screws and chains are utilized in this conversion. The simplest example of mechanical liner actuators is referred to as the “screw” where leadscrew, screw jack, ball screw, and roller screw actuators all operate on the same principle by rotating the actuator’s nut, the screw shaft moves in a line. (*Actuator tuyến tính cơ khí: Actuator cơ khí chuyển đổi chuyển động quay thành chuyển động thẳng. Các thiết bị như vít và xích được sử dụng trong chuyển đổi này. Ví dụ đơn giản nhất của actuator tuyến tính cơ khí được gọi là “vít” trong đó các actuator vít dẫn hướng, kích vít, vít bi và vít con lăn đều hoạt động theo cùng một nguyên tắc bằng cách xoay đai ốc của actuator, trục vít di chuyển theo một đường thẳng.*)
- Hydraulic Actuators: Hydraulic actuators are simple devices with mechanical parts that are used on linear or quarter-turn valves. They are designed based on Pascal’s Law: when there is an increase in pressure at any point in a confined incompressible fluid, then there is an equal increase at every point in the container. (*Actuator thủy lực: Actuator thủy lực là các thiết bị đơn giản với các bộ phận cơ khí được sử dụng trên các van tuyến tính hoặc van góc phần tư. Chúng được thiết kế dựa trên Định luật Pascal: khi có sự tăng áp suất tại bất kỳ điểm nào trong chất lỏng nén không thể nén được, thì có sự tăng áp suất tương ứng tại mọi điểm trong bình.*)
- Pneumatic Actuators: Pneumatic actuators work on the same concept as hydraulic actuators except compressed gas is used instead of liquid. (*Actuator khí nén: Actuator khí nén hoạt động dựa trên cùng một khái niệm như actuator thủy lực ngoại trừ việc sử dụng khí nén thay vì chất lỏng.*)
## 3.10: Video Tracking

## 3.11: IoT Actuators
## 3.10: Video Tracking

## 3.11: IoT Actuators


## 3.4. Internet Protocol Suite

## 3.5. Network Types

## 3.6. Network Reachability

## 3.7: Các bộ giao thức mạng không dây thường dùng trong IoT

## 3.8: IoT Sensors

## 3.9: RFID

## 3.10: Video Tracking

## 3.11: IoT Actuators
