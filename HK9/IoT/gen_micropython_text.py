# -*- coding: utf-8 -*-
"""
Generate Section 4.7 MicroPython Programming with ESP32 (Slides 92 to 160)
with rich bilingual formatting and full technical details.
"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

micropython_section_text = """
## 4.7. Lập trình MicroPython với ESP32 (MicroPython Programming with ESP32)

### Giới thiệu về MicroPython trên ESP32 (Introduction to MicroPython on ESP32)

- MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimized to run on microcontrollers and in constrained environments.
(*MicroPython là một bản hiện thực tinh gọn và hiệu quả cao của ngôn ngữ lập trình Python 3, bao gồm một tập con của thư viện chuẩn Python và được tối ưu hóa đặc biệt để chạy trên các bộ vi điều khiển cũng như các môi trường nhúng có tài nguyên bộ nhớ hạn chế.*)
- MicroPython packed full of advanced features such as an interactive prompt (REPL), arbitrary precision integers, closures, list comprehension, generators, exception handling and more. Yet it is compact enough to fit and run within just 256k of code space and 16k of RAM.
(*MicroPython chứa đầy đủ các tính năng nâng cao hiện đại như dấu nhắc lệnh tương tác thời gian thực (REPL), số nguyên có độ chính xác tùy ý, closure, list comprehension, generator, xử lý ngoại lệ và nhiều hơn nữa. Dù vậy, nó đủ nhỏ gọn để vận hành trơn tru chỉ với 256kB bộ nhớ flash và 16kB RAM.*)
- When paired with the ESP32—a powerful 32-bit dual-core microcontroller with integrated Wi-Fi and Bluetooth—MicroPython provides an ideal, productive platform for rapidly developing Internet of Things (IoT) prototypes and edge intelligence applications.
(*Khi kết hợp với ESP32—dòng vi điều khiển 32-bit 2 nhân mạnh mẽ tích hợp sẵn Wi-Fi và Bluetooth—MicroPython tạo nên một nền tảng lập trình lý tưởng, nâng cao năng suất để nhanh chóng xây dựng các giải pháp IoT và ứng dụng tính toán biên.*)

### Môi trường phát triển tích hợp (Integrated Development Environment - IDE)

There are different programs you can use to program the ESP32 and ESP8266 boards with MicroPython firmware:
(*Có nhiều phần mềm khác nhau mà bạn có thể sử dụng để lập trình các board ESP32 và ESP8266 nạp firmware MicroPython:* )

1. **uPyCraft IDE:**
   - To program the ESP32 or ESP8266 boards with MicroPython firmware, we recommend using **uPyCraft IDE** because it is simple, intuitive to use, lightweight, and works great with the ESP boards.
   (*Để lập trình board ESP32 hoặc ESP8266 chạy MicroPython, chúng tôi khuyến nghị sử dụng **uPyCraft IDE** vì đây là môi trường phát triển đơn giản, trực quan, nhẹ và tương thích hoàn hảo với các bo mạch dòng ESP.*)
   - uPyCraft IDE runs on all major operating systems: Windows, macOS, and Linux Ubuntu.
   (*uPyCraft IDE hoạt động đa nền tảng trên tất cả các hệ điều hành phổ biến: Windows, macOS và Linux.*)
2. **Thonny IDE (Giải pháp thay thế):**
   - An alternative IDE to program your ESP32/ESP8266 with MicroPython is **Thonny IDE** (originally developed at the University of Tartu for teaching Python).
   (*Một giải pháp môi trường thay thế phổ biến khác để lập trình ESP32/ESP8266 bằng MicroPython là **Thonny IDE**.*)

**Bảng so sánh giữa uPyCraft IDE và Thonny IDE:**

| Đặc điểm kỹ thuật | uPyCraft IDE | Thonny IDE |
|:---|:---|:---|
| **Mục đích thiết kế** | Chuyên biệt 100% cho MicroPython trên vi điều khiển ESP32/ESP8266 | IDE cho Python tiêu chuẩn, có tích hợp plugin hỗ trợ MicroPython |
| **Giao diện dòng lệnh REPL** | Hiển thị toàn bộ thông tin debug chi tiết trực tiếp trên Shell | Ẩn bớt các lỗi giao tiếp phần cứng phức tạp, thân thiện hơn với người mới |
| **Quản lý tập tin trên chip** | Cây thư mục trực quan, cho phép kéo thả, chỉnh sửa, xóa file trực tiếp trên bộ nhớ flash của ESP | Hỗ trợ tính năng nạp nhanh file dưới dạng `boot.py` hoặc `main.py` |
| **Khả năng tương thích OS** | Rất tốt trên Windows; cài đặt phức tạp hơn trên một số bản phân phối Linux | Cài đặt dễ dàng và đồng nhất trên mọi hệ điều hành |

### Quy trình cài đặt môi trường trên Windows (Installation Procedures on Windows)

#### Bước 1: Cài đặt Python 3.7.x trên máy tính

Before installing uPyCraft IDE, make sure you have the latest version of Python 3 installed on your computer:
(*Trước khi cài đặt uPyCraft IDE, hãy đảm bảo rằng máy tính của bạn đã được cài đặt Python 3:*)

1. Go to the official Python website: [www.python.org/downloads](https://www.python.org/downloads) and download the Windows installer (ví dụ phiên bản Python 3.7.x hoặc mới hơn).
(*Truy cập trang web chính thức của Python và tải về bộ cài đặt cho Windows.*)
2. Double-click the downloaded executable file (e.g., `python-3.7.X.exe`).
(*Nhấp đúp chuột vào tệp thực thi đã tải về để khởi chạy trình cài đặt.*)
3. **Lưu ý cực kỳ quan trọng:** Check the box at the bottom: **“Add Python 3.7 to PATH”** before clicking **“Install Now”**. This ensures that Python commands can be executed from the command prompt anywhere on your system.
(*Đánh dấu chọn vào ô **“Add Python 3.7 to PATH”** ở cạnh dưới cửa sổ cài đặt trước khi nhấn nút **“Install Now”**. Thao tác này giúp hệ điều hành nhận diện lệnh python từ mọi thư mục.*)
4. Wait a few seconds while the software completes the installation process.
(*Chờ vài giây để chương trình sao chép các tệp và thiết lập môi trường.*)
5. When finished, you will see the message **“Setup was successful”**. Click Close to exit.
(*Khi hoàn tất, xuất hiện thông báo “Setup was successful”. Nhấn Close để kết thúc.*)

#### Bước 2: Tải về và khởi chạy uPyCraft IDE

1. Download the uPyCraft IDE Windows executable from the official repository or source link (e.g., `uPyCraft_V1.1.exe`).
(*Tải về tệp thực thi uPyCraft IDE cho Windows từ liên kết cung cấp.*)
2. uPyCraft là phần mềm dạng portable (chạy ngay không cần cài đặt phức tạp). Bạn chỉ cần nhấp đúp vào tệp `uPyCraft_V1.1.exe` để mở giao diện làm việc của phần mềm.
(*Chỉ cần nhấp đúp chuột vào tệp exe để mở ngay giao diện phần mềm.*)

### Tổng quan giao diện uPyCraft IDE (uPyCraft IDE Overview)

Giao diện làm việc của uPyCraft IDE bao gồm 4 khu vực chức năng chính (Slides 105–109):

1. **Vùng quản lý thư mục và tệp (Folder and files):** Nằm ở cột bên trái, hiển thị hai cây thư mục:
   - `device`: Chứa các tệp và thư viện hiện đang lưu trữ trực tiếp trên bộ nhớ Flash của board ESP32 (như `boot.py`, `main.py`).
   - `workSpace`: Thư mục làm việc trên ổ cứng máy tính của bạn.
   - `uPy_lib`: Các thư viện MicroPython tích hợp sẵn trong IDE.
2. **Khung soạn thảo mã nguồn (Editor):** Nằm ở phần trung tâm bên trên, hỗ trợ mở nhiều tab để viết và chỉnh sửa mã nguồn Python/MicroPython với cú pháp được tô màu trực quan.
3. **Cửa sổ dòng lệnh MicroPython Shell / Terminal (REPL):**
   - On the MicroPython Shell you can type commands to be executed immediately by your ESP board without the need to upload new files.
   (*Trên cửa sổ dòng lệnh Shell, bạn có thể gõ trực tiếp các câu lệnh Python để board ESP thực thi tức thời mà không cần nạp tệp mới.*)
   - It also provides information about the state of an executing program, displays error traces (syntax errors, runtime exceptions), and prints outputs from `print()` statements.
   (*Cửa sổ này cũng hiển thị trạng thái của chương trình, thông báo lỗi biên dịch/thực thi và các chuỗi văn bản được in ra từ hàm `print()`.*)
4. **Thanh công cụ (Tools Bar):** Dãy nút bấm nằm ở thanh dọc bên phải giao diện:
   - **New file:** Tạo một tệp mã nguồn mới trên khung soạn thảo.
   - **Open file:** Mở một tệp mã nguồn có sẵn từ máy tính.
   - **Save file:** Lưu nội dung tệp đang soạn thảo.
   - **Download and run:** Nạp mã nguồn từ tab đang mở xuống vi điều khiển ESP và thực thi ngay lập tức.
   - **Stop:** Dừng ngay lập tức kịch bản đang chạy trên board mạch (tương đương với việc gửi tổ hợp phím `Ctrl + C` trên terminal).
   - **Connect / Disconnect:** Kết nối hoặc ngắt kết nối giao tiếp Serial qua cổng COM với bo mạch.
   - **Undo / Redo:** Hoàn tác hoặc làm lại thao tác chỉnh sửa mã trong Editor.
   - **Syntax check:** Kiểm tra lỗi cú pháp mã nguồn trước khi nạp.
   - **Clear:** Xóa sạch toàn bộ văn bản hiển thị trong cửa sổ Shell/Terminal.

### Thiết lập kết nối và giao tiếp nối tiếp với bo mạch ESP32 (Establishing Communication with the Board)

Sau khi board ESP32 đã được nạp sẵn firmware MicroPython và cắm vào máy tính qua cáp USB, thực hiện các bước kết nối sau (Slides 110–112):

1. Trên thanh menu, chọn `Tools > Board` và chọn loại bo mạch: **`esp32`**.
2. Chọn `Tools > Port` và chọn đúng cổng nối tiếp mà ESP32 đang kết nối (ví dụ: `COM3`, `COM4` trên Windows).
3. Nhấp vào biểu tượng **Connect** (hình sợi cáp kết nối) trên thanh công cụ bên phải.
4. **Kiểm tra kết nối thành công:** Sau khi kết nối thành công, dấu nhắc lệnh **`>>>`** sẽ xuất hiện trên cửa sổ Shell. Bạn có thể gõ lệnh kiểm tra:
   ```python
   >>> print('Hello')
   ```
   Nếu màn hình phản hồi in ra chuỗi `Hello` và quay lại dấu nhắc `>>>`, bo mạch đã sẵn sàng để lập trình.

### Tạo tệp `main.py` và nạp chương trình lên board ESP32 (Creating `main.py` & Uploading Scripts)

- When an ESP board boots up with MicroPython, it executes two special files sequentially:
  1. `boot.py`: Runs once on boot and prepares the board (e.g., setting up network connections).
  2. `main.py`: Runs immediately after `boot.py` and contains your main application script.
(*Khi bo mạch ESP32 khởi động với MicroPython, nó sẽ tự động thực thi tuần tự hai tệp đặc biệt:*
  *1. `boot.py`: Được thực thi đầu tiên khi cấp nguồn để cấu hình các thiết lập môi trường phần cứng và mạng.*
  *2. `main.py`: Được tự động thực thi ngay sau `boot.py` và chứa toàn bộ mã nguồn chương trình ứng dụng chính của bạn.*)

Quy trình tạo và nạp tập tin `main.py` (Slides 113–118):
1. Nhấn nút **New file** để tạo tab mới.
2. Nhấn nút **Save file**, đặt tên tập tin là **`main.py`** và lưu vào máy tính.
3. Soạn thảo mã nguồn ứng dụng (ví dụ kịch bản chớp tắt LED) vào tệp `main.py`.
4. Nhấn nút **Stop** để đảm bảo không có script nào khác đang chiếm quyền điều khiển vi điều khiển.
5. Nhấn nút **Download and run** để truyền tập tin `main.py` vào bộ nhớ flash của ESP32.
6. Khi nạp thành công, cửa sổ Shell sẽ hiển thị dòng thông báo:
   ```text
   download ok
   exec(open('main.py').read(), globals())
   ```
   và chương trình sẽ bắt đầu hoạt động ngay trên bo mạch.

### Kiến thức lập trình MicroPython cơ bản (MicroPython Programming Basics)

Programming in MicroPython is very similar to standard Python 3, but with special library support for low-level embedded hardware (Slides 119–144):
(*Lập trình bằng MicroPython rất tương đồng với Python 3 tiêu chuẩn, nhưng được tích hợp các thư viện chuyên biệt để điều khiển phần cứng nhúng tầng thấp:* )

#### 1. Toán tử toán học (Mathematical Operators)

MicroPython hỗ trợ đầy đủ các phép toán số học thực hiện trực tiếp trên REPL Shell (Slides 122–123):

- `+` (Cộng): `>>> 2 + 2` $\rightarrow$ `4`
- `-` (Trừ): `>>> 10 - 3` $\rightarrow$ `7`
- `*` (Nhân): `>>> 4 * 5` $\rightarrow$ `20`
- `/` (Chia trả về số thực): `>>> 7 / 2` $\rightarrow$ `3.5`
- `//` (Chia lấy phần nguyên): `>>> 7 // 2` $\rightarrow$ `3`
- `%` (Chia lấy phần dư - modulo): `>>> 7 % 2` $\rightarrow$ `1`
- `**` (Lũy thừa): `>>> 2 ** 3` $\rightarrow$ `8`

#### 2. Toán tử quan hệ và so sánh (Relational Operators)

Dùng để so sánh giữa hai giá trị, trả về kết quả kiểu boolean (`True` hoặc `False`) (Slides 124–125):

- `==` : So sánh bằng (`>>> 2 == 2` $\rightarrow$ `True`)
- `!=` : So sánh khác (`>>> 2 != 3` $\rightarrow$ `True`)
- `<`  : Nhỏ hơn (`>>> 5 < 10` $\rightarrow$ `True`)
- `>`  : Lớn hơn (`>>> 15 > 20` $\rightarrow$ `False`)
- `<=` : Nhỏ hơn hoặc bằng
- `>=` : Lớn hơn hoặc bằng

#### 3. Biến và cơ chế định kiểu động (Assigning Values to Variables)

- In Python/MicroPython, you don’t need to declare a variable before using it or specify its data type. A variable is created the moment you first assign a value to it using the `=` assignment operator (Dynamic Typing).
(*Trong Python và MicroPython, bạn không cần phải khai báo trước biến hoặc định rõ kiểu dữ liệu như trong C/C++. Biến được tự động khởi tạo ngay tại thời điểm bạn gán giá trị đầu tiên cho nó bằng toán tử `=` (cơ chế Định kiểu động - Dynamic Typing).* )

*Example:*
(*Ví dụ: Khai báo chân GPIO kết nối với đèn LED:*)

- Trong MicroPython:
  ```python
  led_pin = 23
  ```
- Trong Arduino IDE (C++):
  ```cpp
  const int led_pin = 23;
  ```
  Ta thấy cú pháp của MicroPython ngắn gọn, trong sáng và trực quan hơn nhiều.

#### 4. Các kiểu dữ liệu cơ bản (Data Types) & Hàm `type()`

Các kiểu dữ liệu thường dùng nhất trong các dự án IoT (Slides 128–131):

- **`int` (Số nguyên):** Lưu trữ các số nguyên không có phần thập phân:
  ```python
  a = 6  # Kiểu int
  ```
- **`float` (Số thực dấu phẩy động):** Lưu trữ các số có phần thập phân:
  ```python
  b = 95.32  # Kiểu float
  ```
- **`str` (Chuỗi ký tự):** Dãy các ký tự đặt bên trong cặp dấu nháy đơn `'...'` hoặc nháy kép `"..."`:
  ```python
  c = 'Hello World!'  # Kiểu str
  ```
- **`bool` (Kiểu logic Boolean):** Chỉ nhận một trong hai giá trị hằng số: `True` hoặc `False`:
  ```python
  d = True  # Kiểu bool
  ```

Hàm **`type(variable)`** cho phép kiểm tra kiểu dữ liệu thực tế của một biến trong lúc chương trình đang chạy:
```python
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'str'>
>>> type(d)
<class 'bool'>
```

#### 5. Hàm xuất dữ liệu `print()` và Chú thích mã nguồn (Comments)

- **Hàm `print()`:** In các chuỗi thông điệp hoặc giá trị biến ra cửa sổ Shell, là công cụ đắc lực để gỡ lỗi và theo dõi trạng thái chương trình:
  ```python
  print("LED is: on")
  ```
- **Chú thích mã nguồn (Comments):** Bắt đầu bằng ký tự `#` và kéo dài cho đến hết dòng. Trình thông dịch sẽ bỏ qua hoàn toàn nội dung chú thích:
  ```python
  # Đây là dòng ghi chú giải thích thuật toán
  ```
  *Lưu ý:* Vì bộ nhớ vi điều khiển có hạn, trong các dự án MicroPython dung lượng lớn cần tối ưu hóa mã, nên loại bỏ các dòng chú thích rườm rà trước khi nạp vào flash.

#### 6. Cấu trúc rẽ nhánh điều kiện (Conditional Statements)

MicroPython sử dụng cấu trúc `if...elif...else` với cú pháp dấu hai chấm `:` ở cuối mệnh đề và thụt đầu dòng (indentation 2 hoặc 4 khoảng trắng) để xác định khối lệnh (Slide 134):

```python
if temperature > 35:
  print("Canh bao: Nhiet do qua cao!")
elif temperature < 18:
  print("Canh bao: Nhiet do qua thap!")
else:
  print("Nhiet do ly tuong.")
```

#### 7. Vòng lặp `while` và `for` (Loops)

- **Vòng lặp `while`:** Thực thi lặp đi lặp lại khối lệnh chừng nào điều kiện còn thỏa mãn:
  ```python
  number = 1
  while number <= 10:
    print(number)
    number = number + 1
```
- **Vòng lặp `for` kết hợp `range()`:** Dùng khi số lần lặp được xác định trước. Hàm `range(start, stop)` sinh dãy số từ `start` đến `stop - 1`:
  ```python
  for number in range(1, 11):
    print(number)  # In các số từ 1 đến 10
```

#### 8. Hàm người dùng tự định nghĩa (User-defined Functions)

Hàm được định nghĩa bằng từ khóa `def`, theo sau là tên hàm, danh sách tham số trong ngoặc đơn, dấu hai chấm `:` và lệnh trả về kết quả `return` (Slides 137–138):

*Ví dụ hàm chuyển đổi nhiệt độ từ độ Celsius sang Fahrenheit:*

```python
def celsius_to_fahrenheit(temp_celsius):
  temp_fahrenheit = temp_celsius * (9 / 5) + 32
  return temp_fahrenheit


# Gọi hàm thực thi
t_f = celsius_to_fahrenheit(25)
print("Nhiet do F la:", t_f)  # In ra 77.0
```

#### 9. Quản lý Module và Thư viện trong MicroPython (Modules)

- A module is a Python file that contains a set of classes and functions you can use in your code.
(*Module (hoặc thư viện) là một tệp chứa các lớp (classes) và hàm (functions) đã được viết sẵn để tái sử dụng trong chương trình.*)
- Cú pháp nạp toàn bộ module:
  ```python
  import machine
  ```
- Cú pháp nạp chỉ các lớp cần thiết (tiết kiệm tối đa bộ nhớ RAM cho vi điều khiển):
  ```python
  from machine import Pin
  from time import sleep
  ```

#### 10. Bảng so sánh tổng hợp giữa MicroPython và C++ (Arduino IDE)

| Tiêu chí so sánh | MicroPython | C++ (Arduino IDE) |
|:---|:---|:---|
| **Cơ chế thực thi** | Ngôn ngữ thông dịch (Interpreted language) qua REPL | Ngôn ngữ biên dịch (Compiled language) sang mã máy |
| **Khai báo biến** | Định kiểu động (Dynamic typing), không cần khai báo kiểu trước | Định kiểu tĩnh (Static typing), bắt buộc khai báo kiểu dữ liệu rõ ràng |
| **Phân cách lệnh** | Không sử dụng dấu chấm phẩy `;` ở cuối dòng lệnh | Bắt buộc phải kết thúc mỗi câu lệnh bằng dấu chấm phẩy `;` |
| **Khối mã lệnh** | Sử dụng quy ước **thụt đầu dòng (Indentation)** đồng nhất | Sử dụng cặp **dấu ngoặc nhọn `{}`** |
| **Mệnh đề điều kiện** | Dùng dấu hai chấm `:` sau điều kiện (`if x > 0:`) | Dùng cặp dấu ngoặc đơn quanh điều kiện (`if (x > 0)`) |
| **Tốc độ tạo mẫu** | Rất nhanh, nạp và thử nghiệm tức thì | Mất thời gian biên dịch lại toàn bộ dự án trước mỗi lần nạp |
| **Hiệu năng và bộ nhớ** | Tốn RAM hơn, tốc độ chậm hơn một chút so với mã máy C++ | Tối ưu hóa cực kỳ cao, chiếm ít RAM và thực thi rất nhanh |

---

### Dự án thực hành: Tương tác với GPIO - Điều khiển LED chớp tắt trên ESP32 (Interacting with GPIOs - Blinking an LED on ESP32)

#### 1. Tổng quan dự án (Project Overview)

- The project consists of simply blinking the ESP32/ESP8266 on-board LED.
(*Dự án thực hành này xây dựng chương trình điều khiển đèn LED tích hợp sẵn trên board mạch ESP32 (on-board LED) nhấp nháy tuần hoàn theo chu kỳ xác định.*)
- On the ESP32 (and ESP8266), the on-board blue LED is connected to **GPIO 2**.
(*Trên hầu hết các board phát triển ESP32 thương mại (như ESP32 NodeMCU, ESP32 WROOM-32), đèn LED tích hợp trên bo mạch được đấu nối trực tiếp với chân **GPIO 2**.*)

**Giản đồ hoạt động chu kỳ (Timing Diagram - Slide 146):**
- Đèn LED bật sáng trong **0.5 giây** $\rightarrow$ chân GPIO 2 xuất mức điện áp `HIGH` (3.3V).
- Đèn LED tắt trong **0.5 giây** $\rightarrow$ chân GPIO 2 xuất mức điện áp `LOW` (0V).
- Chu trình bật 0.5s / tắt 0.5s lặp đi lặp lại tuần hoàn vô tận cho đến khi người dùng gửi lệnh dừng chương trình.

#### 2. Kịch bản mã nguồn hoàn chỉnh (Complete MicroPython Script)

```python
# Dự án chớp tắt LED trên ESP32 bằng MicroPython
from machine import Pin  # Nhập lớp Pin từ module machine để điều khiển chân phần cứng
from time import sleep  # Nhập hàm sleep từ module time để tạo trễ thời gian

# Khởi tạo đối tượng led gắn với chân GPIO 2 và cấu hình làm ngõ ra (OUT)
led = Pin(2, Pin.OUT)

# Vòng lặp vô hạn điều khiển chớp tắt
while True:
  led.value(not led.value())  # Đảo trạng thái hiện tại của LED (Bật -> Tắt, Tắt -> Bật)
  sleep(0.5)  # Tạm dừng 0.5 giây (500 ms)
```

#### 3. Phân tích chi tiết từng dòng lệnh của chương trình (How the Code Works)

##### a. Nạp các thư viện phần cứng và thời gian (`from ... import ...`)

- **Module `machine`:** Contains classes to interact with the physical hardware and GPIOs of the ESP microcontroller. Because we only need pin control, we import only the `Pin` class:
  ```python
  from machine import Pin
  ```
  Cách nạp này giúp tiết kiệm bộ nhớ RAM quý giá của vi điều khiển thay vì nạp toàn bộ module `machine`.
- **Module `time`:** Cung cấp các tiện ích xử lý thời gian, đọc đồng hồ hệ thống và tạo độ trễ. Ta nạp hàm `sleep`:
  ```python
  from time import sleep
  ```
  Hàm `sleep(seconds)` nhận tham số thời gian tính bằng giây (số thực, ví dụ `0.5` giây tương đương 500 mili-giây).

##### b. Khởi tạo đối tượng điều khiển chân `Pin`

Hàm khởi tạo của lớp `Pin` chấp nhận các thuộc tính cấu hình theo thứ tự sau:
$$\text{Pin}(\text{pin\_number}, \text{pin\_mode}, \text{pull}, \text{value})$$

- **`pin_number` (Số hiệu chân GPIO):** Trong dự án này là số `2` (chân GPIO 2 nối với LED onboard).
- **`pin_mode` (Chế độ hoạt động):**
  - `Pin.IN`: Cấu hình chân làm ngõ vào (để đọc cảm biến, nút nhấn).
  - `Pin.OUT`: Cấu hình chân làm ngõ ra (để cấp điện điều khiển thiết bị, LED, relay).
  - `Pin.OPEN_DRAIN`: Chế độ cực máng hở (dùng cho bus I2C, 1-Wire).
  Vì ta muốn cấp nguồn làm sáng đèn LED, ta chọn chế độ `Pin.OUT`.
- **`pull` (Điện trở kéo nội bên trong chip):**
  - `Pin.PULL_UP`: Kích hoạt điện trở kéo lên nguồn dương 3.3V.
  - `Pin.PULL_DOWN`: Kích hoạt điện trở kéo xuống mass GND.
  Ở chế độ xuất tín hiệu ra LED, ta không cần kích hoạt điện trở kéo nội, nên tham số này được để trống.
- **`value` (Trạng thái logic ban đầu):** Nhận giá trị `0` (hoặc `False` - mức thấp tắt) hoặc `1` (hoặc `True` - mức cao bật). Mặc định là `0`.

Do đó, câu lệnh khởi tạo đối tượng `led` được viết rất gọn gàng:
```python
led = Pin(2, Pin.OUT)
```

##### c. Vòng lặp vô hạn `while True:`

- `while True:` là kỹ thuật kinh điển trong lập trình hệ thống nhúng để tạo một vòng lặp chạy mãi mãi, tương đương với hàm `void loop()` trong môi trường Arduino C++.

##### d. Kỹ thuật đảo trạng thái thông minh `led.value(not led.value())`

Lớp `Pin` cung cấp phương thức `value()` với hai cách sử dụng:
1. `led.value(state)`: Thiết lập trạng thái logic cho chân (gán mức 0 hoặc 1).
2. `led.value()` (không có tham số): Đọc về trạng thái logic hiện tại của chân (trả về 0 nếu LED đang tắt, trả về 1 nếu LED đang bật).

Biểu thức `not led.value()` sử dụng toán tử logic `not` để đảo ngược giá trị:
- Nếu `led.value()` đang là `0` (tắt) $\rightarrow$ `not 0` cho kết quả là `True` (tương đương `1`) $\rightarrow$ lệnh `led.value(1)` được thực thi $\rightarrow$ **Đèn LED bật sáng**.
- Nếu `led.value()` đang là `1` (bật) $\rightarrow$ `not 1` cho kết quả là `False` (tương đương `0`) $\rightarrow$ lệnh `led.value(0)` được thực thi $\rightarrow$ **Đèn LED tắt**.

**Bảng vết thực thi qua từng chu kỳ lặp (Execution Trace Table - Slide 158):**

| Chu kỳ lặp | Trạng thái hiện tại `led.value()` | Kết quả đảo `not led.value()` | Lệnh thực thi `led.value(...)` | Trạng thái vật lý của LED |
|:---:|:---:|:---:|:---|:---|
| **Vòng lặp 1** | `0` (Mặc định tắt) | `1` | `led.value(1)` | **BẬT (ON)** - Sáng trong 0.5s |
| **Vòng lặp 2** | `1` | `0` | `led.value(0)` | **TẮT (OFF)** - Tắt trong 0.5s |
| **Vòng lặp 3** | `0` | `1` | `led.value(1)` | **BẬT (ON)** - Sáng trong 0.5s |
| **Vòng lặp 4** | `1` | `0` | `led.value(0)` | **TẮT (OFF)** - Tắt trong 0.5s |

Kỹ thuật này cho phép viết mã nguồn ngắn gọn trong đúng một dòng lệnh thay vì phải dùng khối lệnh điều kiện `if...else` dài dòng.

##### e. Hàm tạo trễ `sleep(0.5)`

- Sau mỗi lần đổi trạng thái bật hoặc tắt của đèn LED, hàm `sleep(0.5)` tạm dừng chương trình trong nửa giây (500 mili-giây) để mắt người có thể quan sát rõ ràng hiệu ứng nhấp nháy đều đặn của đèn.

#### 4. Nạp mã và kiểm thử thực tế trên bo mạch ESP32 (Upload & Demonstration)

1. Mở phần mềm uPyCraft IDE trên máy tính.
2. Kết nối bo mạch ESP32 vào cổng USB máy tính. Đảm bảo cổng COM đã được kết nối (có dấu nhắc `>>>`).
3. Mở tệp `main.py`, dán đoạn mã nguồn MicroPython ở trên vào cửa sổ Editor.
4. Nhấn nút **Download and run** (hình mũi tên xanh) trên thanh công cụ bên phải.
5. **Quan sát kết quả:** Đèn LED màu xanh dương tích hợp trên board mạch ESP32 (GPIO 2) sẽ bắt đầu chớp tắt nhịp nhàng với tần số 1Hz (chu kỳ 1 giây: 0.5s sáng và 0.5s tắt).
"""

print("Generated MicroPython Section 4.7 text (length:", len(micropython_section_text), ")")
