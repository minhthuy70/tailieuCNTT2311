# -*- coding: utf-8 -*-
import sys, re

p = {}

p[143] = """# CHƯƠNG 6. QUẢN LÝ NGỮ CẢNH THÔNG MINH VÀ TRÍ TUỆ NHÂN TẠO TRONG IOT

Để tạo ra tính thông minh cho mỗi ứng dụng IoT đòi hỏi hệ thống không chỉ dừng lại ở việc thu thập và lưu trữ các giá trị cảm biến đơn thuần, mà cần phải có khả năng hiểu được ngữ cảnh xung quanh môi trường hoạt động và tự động thích ứng với các thay đổi của ngữ cảnh đó. Khái niệm nhận thức ngữ cảnh (Context-Awareness) và quản lý ngữ cảnh (Context Management) đóng vai trò trung tâm trong việc biến các thiết bị IoT thụ động thành các hệ thống thông minh chủ động phục vụ con người.

Bên cạnh đó, sự bùng nổ của các kỹ thuật Trí tuệ nhân tạo (AI), Học máy (Machine Learning) và Học sâu (Deep Learning) mang lại những công cụ đột phá giúp hệ thống IoT có thể xử lý các tập dữ liệu chuỗi thời gian khổng lồ, phát hiện các mẫu hành vi phức tạp, đưa ra các dự báo chính xác và tự động hóa quá trình ra quyết định.

Nội dung chương này trình bày các khái niệm nền tảng về ngữ cảnh và thích ứng ngữ cảnh; quy trình 4 giai đoạn trong vòng đời quản lý ngữ cảnh; phân tích chi tiết các kỹ thuật mô hình hóa ngữ cảnh và suy luận ngữ cảnh phổ biến; đồng thời giới thiệu các ứng dụng tiêu biểu của học máy và trí tuệ nhân tạo trong hệ sinh thái IoT hiện đại."""

p[144] = """cho phép các dịch vụ được tạo và tái lập trình theo ngữ cảnh sử dụng. Khái niệm nhận thức ngữ cảnh (context-awareness) được định nghĩa như sau: *"Nhận thức ngữ cảnh (context-awareness) đề cập đến khả năng của một ứng dụng, dịch vụ hoặc thậm chí là một thiết bị đầu cuối nhận thức được môi trường vật chất, trạng thái mạng, hoàn cảnh người dùng và tự động điều chỉnh hành vi của mình cho phù hợp với ngữ cảnh đó mà không cần sự can thiệp trực tiếp của con người."*

### 6.1. Ngữ cảnh và thích ứng ngữ cảnh

Trong các hệ thống tính toán phổ dụng (Ubiquitous Computing) và IoT, ngữ cảnh là nhân tố quyết định tính "thông minh" của dịch vụ. Một dịch vụ thông minh không chỉ phản hồi thụ động theo các câu lệnh cố định mà phải chủ động thích ứng linh hoạt theo thời gian, không gian và trạng thái của người sử dụng."""

p[145] = """Ngoài ra, các kỹ thuật trí tuệ nhân tạo cũng đang được chú ý trong quản lý ngữ cảnh trong IoT vì các yếu tố biến động, không chắc chắn, phức tạp và mơ hồ của dữ liệu. Trong phạm vi giáo trình này, tác giả đề cập đến những nội dung cơ bản nhất của trí tuệ nhân tạo được phục vụ trong quản lý ngữ cảnh và suy luận ngữ cảnh trong IoT.

#### 6.1.1. Ngữ cảnh

Định nghĩa kinh điển và được chấp nhận rộng rãi nhất về ngữ cảnh trong khoa học máy tính là định nghĩa của Anind Dey (năm 2001):

> *"Ngữ cảnh là thông tin bất kỳ được sử dụng để mô tả trạng thái của một thực thể. Thực thể có thể là con người, địa điểm hoặc đối tượng vật lý/luận lý có liên quan đến sự tương tác giữa người dùng và ứng dụng, bao gồm cả người dùng và ứng dụng đó."*"""

p[146] = """**Hình 6.1.** Không gian ngữ cảnh hoạt động của thực thể

Dựa trên bản chất và nguồn gốc dữ liệu, ngữ cảnh trong IoT được phân loại thành 2 nhóm chính:
- **Ngữ cảnh sơ cấp (Primary Context / Low-level Context):** Là các dữ liệu đo đạc trực tiếp từ cảm biến vật lý hoặc thiết bị phần cứng mà chưa qua xử lý ngữ nghĩa. Ví dụ: vị trí tọa độ GPS (kinh độ, vĩ độ), nhiệt độ số thực (25.5°C), cường độ ánh sáng (300 Lux), độ ẩm đất (70%).
- **Ngữ cảnh thứ cấp (Secondary Context / High-level Context):** Là các thông tin trừu tượng có mức ngữ nghĩa cao hơn, được tính toán hoặc suy luận từ ngữ cảnh sơ cấp kết hợp với tri thức chuyên gia. Ví dụ: từ tọa độ GPS suy ra người dùng đang "ở nơi làm việc" hay "ở nhà"; từ nhiệt độ và độ ẩm suy ra thời tiết "dễ chịu" hay "nắng nóng oi bức"."""

p[147] = """Bảng 6.1 minh họa quy tắc chuyển đổi từ ngữ cảnh sơ cấp (giá trị số đo thực tế) sang ngữ cảnh thứ cấp (mức định tính trừu tượng) phục vụ cho hệ thống điều hòa không khí:

**Bảng 6.1.** Quy đổi giá trị và mức nhiệt độ

| STT | Giá trị nhiệt độ (°C) | Mức nhiệt độ (Ngữ cảnh thứ cấp) |
|:---:|:---|:---|
| 1 | 0 - 15 | Very Low (Rất lạnh) |
| 2 | 16 - 20 | Low (Lạnh) |
| 3 | 21 - 25 | Medium (Mát mẻ / Bình thường) |
| 4 | 26 - 32 | High (Nóng) |
| 5 | > 32 | Very High (Rất nóng) |

Việc chuẩn hóa và trừu tượng hóa ngữ cảnh giúp giảm bớt sự phụ thuộc của ứng dụng vào chi tiết phần cứng cảm biến bên dưới, tạo điều kiện cho các thuật toán suy luận hoạt động nhất quán."""

p[148] = """**Đặc điểm của ngữ cảnh trong IoT:**
1. **Được thu thập từ nút cảm biến hay mạng cảm biến:** Dữ liệu mang tính phân tán, phát sinh liên tục theo dòng thời gian (streaming data).
2. **Được thu thập từ những thiết bị nhỏ và tài nguyên hạn chế:** Dẫn đến dữ liệu có thể bị trễ, ngắt quãng hoặc thiếu chính xác do hạn chế về pin và phần cứng.
3. **Tính không hoàn hảo và bất định (Imperfect & Uncertain):** Dữ liệu cảm biến thường xuyên chứa nhiễu, lỗi đo đạc hoặc bị mất gói tin trong quá trình truyền sóng vô tuyến.
4. **Tính phụ thuộc thời gian (Temporal Aspect):** Ngữ cảnh luôn biến đổi theo thời gian; giá trị ngữ cảnh chỉ có giá trị sử dụng trong một khoảng thời gian hiệu lực nhất định.

#### 6.1.2. Thích ứng ngữ cảnh

Thích ứng ngữ cảnh (Context Adaptation) là quá trình hệ thống IoT tự động thay đổi hành vi, giao diện hoặc cấu hình dịch vụ dựa trên ngữ cảnh đã được nhận diện nhằm tối ưu hóa trải nghiệm người dùng và tiết kiệm tài nguyên năng lượng."""

p[149] = """Ví dụ về thích ứng ngữ cảnh trong hệ thống chiếu sáng thông minh tại tòa nhà văn phòng:
- **Trường hợp 1:** Nếu chỉ có 1 người ngồi tại một vị trí trong phòng làm việc, hệ thống chỉ bật cụm đèn chiếu sáng tại khu vực bàn làm việc đó, tắt toàn bộ các bóng đèn khác để tiết kiệm điện.
- **Trường hợp 2:** Nếu có nhiều người ngồi tại nhiều vị trí khác nhau trong phòng hoặc đang tổ chức cuộc họp, hệ thống tự động bật toàn bộ hệ thống đèn chiếu sáng trong phòng.

**Hình 6.2.** Vòng đời quản lý ngữ cảnh trong IoT

### 6.2. Quản lý ngữ cảnh trong IoT

Quá trình quản lý ngữ cảnh trong các hệ thống IoT hiện đại tuân theo một chu trình khép kín gồm 4 giai đoạn chính (Hình 6.2):
1. **Thu thập ngữ cảnh (Context Acquisition)**
2. **Mô hình hóa ngữ cảnh (Context Modeling)**
3. **Suy luận ngữ cảnh (Context Reasoning)**
4. **Phân phối ngữ cảnh (Context Dissemination)**"""

p[150] = """#### 6.2.1. Thu thập ngữ cảnh

**Thu thập ngữ cảnh (Context Acquisition):** Là bước đầu tiên chịu trách nhiệm lấy dữ liệu từ nhiều nguồn khác nhau: cảm biến vật lý (nhiệt độ, gia tốc), dịch vụ mạng (thông tin thời tiết từ API web), người dùng (nhập liệu trực tiếp) hoặc trạng thái thiết bị (mức pin, địa chỉ IP). Thu thập ngữ cảnh có thể thực hiện theo cơ chế thăm dò định kỳ (polling) hoặc hướng sự kiện theo ngưỡng (event-triggered).

#### 6.2.2. Mô hình hóa ngữ cảnh

**Mô hình hóa ngữ cảnh (Context Modeling):** Chuyển đổi dữ liệu thô thu thập được thành các cấu trúc dữ liệu chuẩn mực, có tổ chức để hệ thống phần mềm có thể lưu trữ, truy vấn, chia sẻ và suy luận hiệu quả.

#### 6.2.3. Suy luận ngữ cảnh

**Suy luận ngữ cảnh (Context Reasoning):** Là giai đoạn cốt lõi sử dụng các thuật toán tính toán để suy ra ngữ cảnh cấp cao từ ngữ cảnh cấp thấp, phát hiện mâu thuẫn dữ liệu và đưa ra quyết định hành động thích ứng cho hệ thống.

#### 6.2.4. Phân phối ngữ cảnh

**Phân phối ngữ cảnh (Context Dissemination):** Cung cấp dữ liệu ngữ cảnh đã được xử lý tới các ứng dụng hoặc cơ cấu chấp hành thông qua mô hình Publish/Subscribe (như giao thức MQTT) hoặc giao thức Request/Response (REST API)."""

p[151] = """### 6.3. Các kỹ thuật mô hình hóa ngữ cảnh

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

Mô hình sơ đồ sử dụng các thẻ phân cấp (tags) để cấu trúc hóa dữ liệu ngữ cảnh, phổ biến nhất là XML và JSON."""

p[152] = """Một ví dụ về mô hình hóa ngữ cảnh bằng XML:

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

Mô hình hóa ngữ cảnh dựa trên các nguyên lý lập trình hướng đối tượng (OOP): đóng gói (encapsulation), kế thừa (inheritance) và đa hình (polymorphism)."""

p[153] = """trên việc phân cấp và quan hệ giữa các lớp. Mô hình này cho phép đóng gói (encapsulation) và tái sử dụng. Hầu hết các ngôn ngữ lập trình cấp cao hỗ trợ các khái niệm hướng đối tượng, mô hình hóa có thể được tích hợp vào hệ thống nhận biết ngữ cảnh một cách dễ dàng. Do đó, mô hình dựa trên đối tượng phù hợp để sử dụng bên trong mã nguồn phần mềm của từng thiết bị.

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
- **Object Properties (Thuộc tính đối tượng):** Mô tả quan hệ giữa hai thực thể."""

p[154] = """Ví dụ về các khẳng định thuộc tính đối tượng (Object property assertions) và thuộc tính dữ liệu (Data property assertions) trong một Ontology:

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
  2. **Hỗ trợ suy luận tự động mạnh mẽ:** Các cỗ máy suy diễn ontology (như Pellet, HermiT) có thể tự động suy luận ra các tri thức mới và phát hiện các mâu thuẫn dữ liệu dựa trên các quy tắc mô tả vị từ."""

p[155] = """**Bảng 6.2.** So sánh các kỹ thuật mô hình hóa ngữ cảnh

| Kỹ thuật mô hình hóa | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Khóa / Giá trị (Key-Value)** | • Đơn giản, dễ cài đặt<br>• Tốc độ truy xuất nhanh<br>• Chi phí lưu trữ nhỏ | • Không có cấu trúc phân cấp<br>• Không hỗ trợ xác thực<br>• Không thể suy luận | Ứng dụng nhỏ, lưu trữ cấu hình tạm thời |
| **Sơ đồ (Markup - XML / JSON)** | • Linh hoạt, có cấu trúc phân cấp<br>• Xác thực qua Schema<br>• Công cụ parser có sẵn rộng rãi | • Thiếu ngữ nghĩa tường minh<br>• Kích thước tệp lớn<br>• Khó biểu diễn quan hệ ngang | Trao đổi dữ liệu giữa các dịch vụ web, định dạng bản tin cảm biến (SensorML, JSON) |
| **Đồ họa (Graphical - UML)** | • Trực quan, dễ hiểu<br>• Biểu diễn quan hệ thực thể tốt<br>• Chuẩn hóa cao | • Chỉ dùng ở pha thiết kế<br>• Khó truy vấn tự động lúc chạy | Phân tích và thiết kế kiến trúc hệ thống ban đầu |
| **Dựa trên đối tượng (Object-based)** | • Đóng gói và tái sử dụng mã nguồn tốt<br>• Tích hợp tự nhiên vào ngôn ngữ OOP (Java, Python, C++) | • Khó chia sẻ giữa các hệ thống không đồng nhất<br>• Phụ thuộc ngôn ngữ | Xử lý nội bộ bên trong mã nguồn phần mềm trên thiết bị |"""

p[156] = """**Bảng 6.2.** (tiếp theo)

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
6. Dựa trên logic xác suất (Probabilistic Logic)"""

p[157] = """#### 6.4.1. Học có giám sát (Supervised Learning)

Học có giám sát sử dụng một tập dữ liệu huấn luyện đã được gán nhãn (labeled data) để học hàm ánh xạ từ đầu vào (dữ liệu cảm biến) tới đầu ra (ngữ cảnh hành vi):
- **Phân loại (Classification):** Dự đoán đầu ra là các nhãn ngữ cảnh rời rạc (ví dụ: người dùng đang "Đi bộ", "Chạy", "Ngồi", "Nằm"). Các thuật toán thông dụng: Cây quyết định (Decision Tree), Support Vector Machine (SVM), K láng giềng gần nhất (k-NN), Mạng nơ-ron nhân tạo (ANN).
- **Hồi quy (Regression):** Dự đoán đầu ra là các giá trị liên tục (ví dụ: dự báo nhiệt độ không khí trong 1 giờ tới, ước lượng mức tiêu thụ điện năng). Các thuật toán: Hồi quy tuyến tính (Linear Regression), Hồi quy phi tuyến.

#### 6.4.2. Học không giám sát (Unsupervised Learning)

Học không giám sát làm việc trên dữ liệu chưa gán nhãn (unlabeled data), tự động phân tích cấu trúc tiềm ẩn và gom nhóm các mẫu dữ liệu tương đồng:
- **Phân cụm (Clustering - K-Means, DBSCAN):** Phân chia các vị trí đo đạc cảm biến thành các vùng có đặc tính môi trường giống nhau mà không cần nhãn định trước."""

p[158] = """sử dụng trong các ứng dụng thích ứng ngữ cảnh. Cụ thể, kỹ thuật phân cụm được sử dụng ở mức thấp (mức phần cứng) trong mạng cảm biến như định tuyến hay mức cao (mức ứng dụng) như xác định vị trí trong nhà hay ngoài trời. Kỹ thuật mạng nơ-ron không giám sát như Kohonen Self Organizing Map (KSOM) được sử dụng để phân loại dữ liệu cảm biến theo thời gian.
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

Trong thế giới thực, nhiều khái niệm không thể phân định rạch ròi đúng (1) hoặc sai (0) mà mang tính mơ hồ: thế nào là "trời nóng", "trời mát", "độ ẩm thấp". Logic mờ (Fuzzy Logic) do Lotfi Zadeh đề xuất giải quyết bài toán này bằng cách gán cho mỗi phần tử một độ liên thuộc (membership degree) nằm trong đoạn `[0, 1]`."""

p[159] = """Hệ thống suy luận mờ bao gồm 4 khối chức năng chính:
1. **Mờ hóa (Fuzzification):** Chuyển đổi giá trị số đo thực tế (crisp input) thành các giá trị ngôn ngữ mờ thông qua các hàm liên thuộc (Membership Functions: dạng tam giác, hình thang, hình chuông Gaussian).
2. **Cơ sở luật mờ (Fuzzy Rule Base):** Tập hợp các luật mờ dạng: `IF x is A AND y is B THEN z is C`.
3. **Cỗ máy suy luận mờ (Fuzzy Inference Engine):** Kết hợp các luật mờ và tính toán mức kích hoạt của từng luật (phổ biến nhất là phương pháp Mamdani và Sugeno).
4. **Giải mờ (Defuzzification):** Chuyển đổi tập mờ kết quả đầu ra thành một giá trị điều khiển số thực cụ thể (sử dụng phương pháp trọng tâm Center of Gravity - COG).

**Ví dụ ứng dụng Logic mờ trong điều khiển nhiệt độ nhà kính nông nghiệp thông minh:**
- Đầu vào 1: Nhiệt độ hiện tại thu thập từ cảm biến.
- Đầu vào 2: Chiều hướng thay đổi nhiệt độ (đang tăng, không đổi, đang giảm).
- Đầu ra: Tín hiệu điều khiển cơ cấu chấp hành (Hệ thống sưởi, Quạt thông gió).

**Hình 6.4.** Minh họa hàm liên thuộc dạng tam giác và hình thang"""

p[160] = """**Bảng 6.3.** Bảng biểu diễn thang input nhiệt độ

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
| 12 | Hot | None / Up | Ventilation High (Thông gió mức cao) |"""

p[161] = """**Hình 6.5.** Quy trình suy luận mờ Mamdani

Các trường hợp suy luận mờ thực tế thông qua công cụ MATLAB Fuzzy Logic Toolbox:
- **Trường hợp 1:** Nhiệt độ vào là 16.8°C và chiều hướng nhiệt độ là Up (0.92): kết quả đầu ra rơi vào vùng Nothing (không cần tác động điều hòa vì nhiệt độ mát mẻ và đang có xu hướng tăng nhẹ về mức tối ưu).
- **Trường hợp 2:** Nhiệt độ vào là 10.5°C và chiều hướng nhiệt độ là Down (-0.85): kết quả giải mờ đầu ra kích hoạt Heating High với công suất sưởi cực đại để tránh rét hại cho cây trồng."""

p[162] = """**Hình 6.6.** Giao diện Rule Viewer trong MATLAB Fuzzy Logic Toolbox

Giao diện Rule Viewer (Hình 6.6) cho phép trực quan hóa đồng thời tất cả các luật mờ được kích hoạt, xem diện tích phủ mờ của từng luật và điểm trọng tâm giải mờ kết quả cuối cùng."""

p[163] = """- **Trường hợp 3:** Ta có dữ liệu đầu vào là 14.2°C, chiều hướng nhiệt độ là đang giảm (Down) thì kết quả đầu ra kích hoạt Heating High với giá trị tính toán cụ thể là 20.1%.

#### 6.4.5. Dựa trên Ontology (Ontology Reasoning)

Suy luận dựa trên ontology tận dụng cấu trúc hình thức và ngữ nghĩa của OWL-DL:
- **Suy diễn quan hệ phân cấp (Subsumption Reasoning):** Tự động xác định một lớp này có phải là lớp con của lớp khác hay không dựa trên các thuộc tính ràng buộc.
- **Kiểm tra tính nhất quán (Consistency Checking):** Phát hiện các mâu thuẫn logic trong cơ sở tri thức (ví dụ: một cảm biến không thể đồng thời vừa ở trạng thái `TurnedOff` vừa phát ra giá trị `MeasuringActive`).
- **Khám phá tri thức ẩn (Implicit Knowledge Deduction):** Từ các quan hệ bắc cầu, đối xứng để suy ra các sự thật mới mà không cần lập trình viên khai báo thủ công."""

p[164] = """#### 6.4.6. Dựa trên Logic xác suất (Probabilistic Logic)

Kỹ thuật suy luận dựa trên logic xác suất (như Mạng Bayes - Bayesian Networks, Mô hình Markov ẩn - Hidden Markov Models, Lý thuyết Dempster-Shafer) cho phép hệ thống ra quyết định trong điều kiện dữ liệu cảm biến không chắc chắn, không đầy đủ hoặc chứa nhiều nhiễu.

Mỗi phát biểu hoặc trạng thái được gắn một phân phối xác suất có điều kiện $P(A|B)$ dựa trên định lý Bayes:
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

Ví dụ: Xác định xác suất một người dùng đang ngủ trong phòng dựa trên tập hợp nhiều bằng chứng: cảm biến áp lực đệm giường kích hoạt, cường độ ánh sáng bằng 0, độ ồn dưới 20dB và thời gian là ban đêm. Dù một cảm biến có thể bị lỗi, mạng Bayes vẫn tổng hợp các nguồn bằng chứng còn lại để đưa ra kết luận có độ tin cậy cao nhất."""

p[165] = """**Bảng 6.6.** So sánh các kỹ thuật suy luận ngữ cảnh

| Kỹ thuật suy luận | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Học có giám sát (Supervised Learning)** | • Độ chính xác cao khi có nhãn<br>• Xử lý tốt dữ liệu phi tuyến tính | • Cần tập dữ liệu huấn luyện lớn có gán nhãn<br>• Tốn tài nguyên tính toán | Nhận dạng hoạt động người dùng, dự báo thời tiết, nhận diện biển số xe |
| **Học không giám sát (Unsupervised Learning)** | • Không cần dữ liệu gán nhãn<br>• Tự động phát hiện cấu trúc ẩn | • Khó đánh giá độ chính xác<br>• Ngữ nghĩa đầu ra cần chuyên gia giải thích | Phát hiện bất thường, phân cụm nút cảm biến theo vùng môi trường |
| **Dựa trên luật (Rule-based)** | • Trực quan, dễ hiểu (IF-THEN)<br>• Cài đặt đơn giản, chạy nhanh | • Phải định nghĩa luật thủ công<br>• Dễ mâu thuẫn khi số luật lớn | Điều khiển tự động theo ngưỡng cố định (bật tắt đèn, tưới nước) |
| **Logic mờ (Fuzzy Logic)** | • Xử lý tốt tính mơ hồ, không rạch ròi<br>• Gần với tư duy con người | • Phải thiết kế hàm liên thuộc thủ công<br>• Không tự thích nghi | Điều khiển hệ thống nhiệt độ, thông gió, tưới tiêu nông nghiệp |"""

p[166] = """**Bảng 6.6.** (tiếp theo)

| Kỹ thuật suy luận | Ưu điểm | Nhược điểm | Phạm vi ứng dụng |
|:---|:---|:---|:---|
| **Dựa trên Ontology** | • Tận dụng tri thức ngữ nghĩa sâu sắc<br>• Tự động kiểm tra mâu thuẫn logic | • Chi phí tính toán cao<br>• Không phù hợp xử lý dữ liệu số chuỗi thời gian | Tích hợp dữ liệu ngữ cảnh đa nguồn trong Smart Home, Smart City |
| **Logic xác suất (Probabilistic Logic)** | • Xử lý xuất sắc tính không chắc chắn và dữ liệu nhiễu<br>• Kết hợp nhiều bằng chứng độc lập | • Cần biết phân phối xác suất tiên nghiệm<br>• Độ phức tạp tính toán cao | Định vị trong nhà, nhận dạng ngữ cảnh hành vi từ cảm biến nhiễu |

### 6.5. Trí tuệ nhân tạo và IoT

Sự kết hợp giữa Trí tuệ nhân tạo (AI) và Internet vạn vật (IoT) đã khai sinh ra thuật ngữ **AIoT (Artificial Intelligence of Things)**. Trong kỷ nguyên AIoT, IoT đóng vai trò là "hệ thần kinh kỹ thuật số" thu thập dữ liệu khổng lồ từ thế giới vật lý, còn AI đóng vai trò là "bộ não" phân tích thông minh và ra quyết định tự động."""

p[167] = """Sự đột phá của các kỹ thuật Trí tuệ nhân tạo trong thập kỷ qua được đánh dấu bằng những cột mốc lịch sử:
- Tháng 3/2016, hệ thống AI AlphaGo của Google DeepMind đã làm chấn động thế giới khi đánh bại kỳ thủ cờ vây số một thế giới Lee Sedol với tỉ số 4-1.
- Năm 2017, DeepMind tiếp tục công bố AlphaGo Zero với khả năng tự học hoàn toàn từ đầu thông qua học tăng cường (Reinforcement Learning) mà không cần dữ liệu ván đấu của con người và chiến thắng áp đảo phiên bản AlphaGo tiền nhiệm.

Những bước tiến nhảy vọt này đã mở ra làn sóng ứng dụng AI mạnh mẽ vào mọi ngóc ngách của đời sống, trong đó hệ sinh thái IoT là môi trường ứng dụng giàu tiềm năng bậc nhất."""

p[168] = """Hai nút thắt cổ chai lớn nhất của Học máy và Học sâu ở các giai đoạn trước đây là: (1) thiếu hụt tài nguyên tính toán mạnh mẽ và (2) thiếu dữ liệu lớn để huấn luyện.

Những năm gần đây, sự phát triển vượt bậc của các bộ tăng tốc phần cứng chuyên dụng như GPU (Graphics Processing Unit), TPU (Tensor Processing Unit), NPU (Neural Processing Unit) cùng với hạ tầng đám mây phân tán đã giải quyết triệt để nút thắt về năng lực tính toán. Đồng thời, hàng chục tỷ thiết bị IoT kết nối liên tục tạo ra nguồn dữ liệu lớn vô tận hàng ngày, trở thành mảnh đất màu mỡ cho các mô hình học máy phát triển.

#### 6.5.1. Học máy (Machine Learning)

##### 6.5.1.1. Quá trình xử lý trong học máy

Quá trình xây dựng và triển khai một mô hình học máy trong hệ thống IoT bao gồm 5 bước tuần tự:
1. **Thu thập dữ liệu (Data Collection):** Thu thập dữ liệu cảm biến từ các thiết bị IoT.
2. **Tiền xử lý dữ liệu (Data Preprocessing):** Làm sạch dữ liệu, xử lý các giá trị khuyết thiếu, lọc nhiễu tín hiệu và chuẩn hóa thang đo dữ liệu."""

p[169] = """3. **Trích xuất đặc trưng (Feature Extraction & Selection):** Lựa chọn các đặc trưng quan trọng nhất đại diện cho bài toán nhằm giảm số chiều dữ liệu và tăng tốc độ huấn luyện.
4. **Huấn luyện mô hình (Model Training):** Sử dụng tập dữ liệu huấn luyện (training set) và thuật toán học máy phù hợp để tối ưu hóa các tham số mô hình nhằm giảm thiểu hàm mất mát (loss function).
5. **Đánh giá mô hình (Model Evaluation):** Đánh giá độ chính xác của mô hình trên tập dữ liệu thử nghiệm độc lập (test set) thông qua các chỉ số đo lường như Accuracy, Precision, Recall, F1-Score.

**Hình 6.7.** Quy trình huấn luyện và dự đoán tổng quát trong học máy"""

p[170] = """Thuật toán học máy lấy tập dữ liệu huấn luyện và học các thuộc tính cụ thể trong đó để giảm thiểu lỗi trong quá trình đánh giá mô hình. Sau khi huấn luyện, mô hình được kiểm tra trên tập dữ liệu thử nghiệm để đánh giá hiệu quả của mô hình được chọn và dự đoán độ chính xác của mô hình khi sử dụng trong thực tế. Một mô hình có thể cho kết quả khác nhau nếu huấn luyện và thử nghiệm trên các tập dữ liệu có phân phối khác biệt, do đó việc áp dụng kỹ thuật kiểm chứng chéo (k-fold cross validation) là rất cần thiết."""

p[171] = """**Thực thi mô hình (Inference / Deployment):** Đây là bước cuối cùng trong vòng đời học máy. Sau khi được đánh giá đạt độ chính xác yêu cầu, mô hình được triển khai vào môi trường vận hành thực tế (trên đám mây hoặc trên thiết bị biên) để thực hiện dự đoán thời gian thực khi có dữ liệu cảm biến mới gửi về.

##### 6.5.1.2. Phân loại các kỹ thuật học máy

Các thuật toán học máy được chia thành 3 nhánh chính (Hình 6.8):
1. **Học có giám sát (Supervised Learning):** Dữ liệu có nhãn đầu vào và đầu ra mong muốn. Gồm hai bài toán chính: Phân loại (Classification) và Hồi quy (Regression).
2. **Học không giám sát (Unsupervised Learning):** Dữ liệu không có nhãn. Gồm hai bài toán chính: Phân cụm (Clustering) và Giảm chiều dữ liệu (Dimensionality Reduction).
3. **Học tăng cường (Reinforcement Learning):** Tác nhân (Agent) học thông qua quá trình tương tác thử-sai với môi trường để tối đa hóa phần thưởng tích lũy (Reward).

**Hình 6.8.** Phân loại các thuật toán học máy phổ biến trong IoT"""

p[172] = """Các thuật toán học có giám sát phổ biến bao gồm: Hồi quy tuyến tính, Hồi quy Logistic, K láng giềng gần nhất (k-NN), Máy hỗ trợ véc-tơ (SVM), Naive Bayes, Cây quyết định, Rừng ngẫu nhiên (Random Forest) và Mạng nơ-ron nhân tạo sâu (Deep Neural Networks - DNN).

Đối với bài toán phân loại, đầu ra là các nhãn lớp rời rạc (ví dụ: phát hiện đám cháy hay không có cháy; nhận diện loại cây trồng). Trong khi đó, đối với bài toán hồi quy, đầu ra là các giá trị số thực liên tục (ví dụ: nồng độ bụi mịn PM2.5 dự báo trong không khí)."""

p[173] = """**Hình 6.9.** Minh họa bài toán phân lớp nhị phân bằng thuật toán SVM

Hình 6.9 minh họa bài toán phân lớp nhị phân sử dụng thuật toán Máy hỗ trợ véc-tơ (SVM). Thuật toán tìm kiếm một siêu phẳng phân cách tối ưu (optimal hyperplane) sao cho khoảng cách lề (margin) giữa hai lớp dữ liệu là lớn nhất, qua đó tăng cường khả năng tổng quát hóa của mô hình khi gặp dữ liệu mới."""

p[174] = """#### 6.5.2. Ứng dụng của học máy trong IoTs và các định hướng nghiên cứu

Với sự phát triển mạnh mẽ của cuộc cách mạng công nghiệp lần thứ tư, sự kết hợp giữa học máy và công nghệ IoT đang tạo ra những bước chuyển mình sâu sắc trong nhiều lĩnh vực:

1. **Giao thông thông minh (Smart Transportation):**
   - Đếm lưu lượng phương tiện giao thông tự động qua camera sử dụng các mô hình thị giác máy tính như YOLO, SSD.
   - Điều khiển đèn tín hiệu giao thông thích ứng dựa trên thuật toán học tăng cường nhằm giảm thiểu tình trạng ùn tắc vào giờ cao điểm.
   - Nhận diện biển số xe tự động và phát hiện các hành vi vi phạm giao thông (vượt đèn đỏ, lấn làn)."""

p[175] = """2. **Giám sát môi trường và cảnh báo thiên tai:**
   - Dự báo chất lượng không khí (chỉ số AQI, nồng độ bụi mịn PM2.5, PM10) dựa trên chuỗi thời gian sử dụng mô hình LSTM (Long Short-Term Memory).
   - Cảnh báo sớm cháy rừng thông qua phân tích dữ liệu nhiệt độ, độ ẩm và hình ảnh từ camera giám sát trên tháp quan sát.
   - Dự báo lũ quét và sạt lở đất dựa trên dữ liệu đo mưa và độ ẩm đất tự động.

3. **Nông nghiệp thông minh (Smart Agriculture):**
   - Nhận diện bệnh hại trên lá cây trồng thông qua hình ảnh chụp từ điện thoại hoặc máy bay không người lái (UAV) sử dụng mạng nơ-ron tích chập (CNN).
   - Tự động hóa lịch tưới tiêu và bón phân tối ưu dựa trên mô hình học máy phân tích nhu cầu sinh trưởng của cây trồng và điều kiện thời tiết."""

p[176] = """4. **Thành phố thông minh và Tòa nhà thông minh (Smart Cities & Smart Buildings):**
   - Tối ưu hóa tiêu thụ năng lượng điện trong các tòa nhà văn phòng dựa trên học thói quen người dùng.
   - Giám sát bãi đỗ xe thông minh, hướng dẫn lái xe đến vị trí đỗ còn trống nhanh nhất.
   - Quản lý thu gom rác thải đô thị thông minh dựa trên cảm biến mức độ đầy của thùng rác."""

p[177] = """**Định hướng nghiên cứu tương lai:**
- **TinyML (Machine Learning trên vi điều khiển siêu nhỏ):** Nghiên cứu nén mô hình học sâu để có thể thực thi suy luận trực tiếp trên các vi điều khiển cấp thấp có RAM dưới 256kB như ARM Cortex-M, ESP32 mà không cần kết nối mạng.
- **Học liên kết bảo vệ quyền riêng tư (Privacy-preserving Federated Learning):** Cho phép huấn luyện mô hình cộng tác giữa hàng nghìn thiết bị IoT mà không cần thu thập dữ liệu nhạy cảm của người dùng về máy chủ trung tâm.
- **Lưu trữ dữ liệu thông minh tại biên (Edge Caching & Content Delivery):** Tối ưu hóa việc phân phối nội dung video và dữ liệu số trên mạng di động 5G/6G."""

p[178] = """các hệ thống Big Data. Sự phát triển của các thiết bị IoT/5G hỗ trợ cho việc thu thập dữ liệu hàng ngày, hàng giờ, mỗi phút hoặc thậm chí trong một phần nghìn giây. Đó là lý do tại sao chuỗi thời gian là rất lớn và nhiều chiều. Ngoài ra, loại dữ liệu này cũng không cố định, tức là nó có chu kỳ không đều và dựa vào các đặc điểm thống kê của nó như giá trị trung bình, giá trị trung vị, phương sai và sự thay đổi tiêu chuẩn theo thời gian. Do đó, làm thế nào để lưu trữ và làm thế nào để đối phó với tập dữ liệu lớn cho một vấn đề nhất định trong một thời gian thích hợp đòi hỏi sức mạnh, các phương pháp tự động để lấy thông tin quan trọng mà không phụ thuộc nhiều vào sự can thiệp của con người.

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
10. Hãy xây dựng ứng dụng giám sát và cảnh báo chất lượng không khí tại Thành phố Hồ Chí Minh ứng dụng kỹ thuật máy học."""

# Apply to file
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(^## Trang \d+\s*$)', text, flags=re.MULTILINE)
pages_dict = {}
for i in range(1, len(parts), 2):
    p_num = int(re.search(r'\d+', parts[i]).group(0))
    pages_dict[p_num] = parts[i+1]

for page_num in range(143, 179):
    if page_num in p:
        pages_dict[page_num] = '\n\n' + p[page_num].strip() + '\n\n'

out = [parts[0]]
for i in range(1, len(parts), 2):
    marker = parts[i]
    p_num = int(re.search(r'\d+', parts[i]).group(0))
    out.append(marker)
    out.append(pages_dict[p_num])

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'w', encoding='utf-8') as f:
    f.write(''.join(out))

print("Chapter 6 (pages 143-178) updated successfully!")
