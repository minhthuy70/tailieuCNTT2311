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