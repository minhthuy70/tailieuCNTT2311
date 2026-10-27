# -*- coding: utf-8 -*-
"""
Script to generate the complete bilingual translation for slides 48 to 160 of Chapter 4
and integrate it into IoTmain.md at the exact appropriate location.
"""
import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

# 1. Đoạn dịch chi tiết cho Slides 62 đến 91 (Hoàn thiện Lập trình Arduino)
arduino_slides_text = """
- **`{}` (curly braces):** This is used to mark blocks of code. For example, when you write code for the loop() function, you have to use curly braces before and after the code.
(*`{}` (dấu ngoặc nhọn): Dùng để phân định các khối mã lệnh (block of code). Ví dụ, khi bạn viết mã cho hàm loop(), bạn phải đặt các dấu ngoặc nhọn ở trước và sau khối mã lệnh đó.*)

*Example:*
(*Ví dụ:*)

```cpp
void loop() {
  Serial.println("ciao");
}
```

- **Comments (Chú thích mã nguồn):** These are portions of text ignored by the Arduino processor, but are extremely useful to remind yourself (or others) of what a piece of code does.
(*Chú thích là những đoạn văn bản được bộ xử lý Arduino bỏ qua không thực thi, nhưng lại cực kỳ hữu ích để nhắc nhở chính bạn (hoặc người khác) về chức năng của từng đoạn mã.*)

There are two styles of comments in Arduino:
(*Có hai kiểu chú thích trong Arduino:*)

- `// single-line:` this text is ignored until the end of the line. (*`// chú thích trên một dòng:` trình biên dịch sẽ bỏ qua toàn bộ văn bản từ dấu // cho đến hết dòng.*)
- `/* multiple-line: you can write a whole poem in here */:` this block is ignored between the opening and closing markers. (*`/* chú thích nhiều dòng: bạn có thể viết cả một bài thơ trong khối này */:` toàn bộ văn bản nằm giữa dấu mở và dấu đóng đều bị bỏ qua.*)

### Hằng số trong Arduino (Constants)

Arduino includes a set of predefined keywords with special values:
(*Arduino tích hợp sẵn một tập hợp các từ khóa định sẵn với các giá trị đặc biệt:* )

- **`HIGH` and `LOW`**: Used when you want to turn on or off an Arduino pin (HIGH sets the pin to 5V or 3.3V, LOW sets it to 0V / GND).
(*`HIGH` và `LOW`: Được sử dụng khi bạn muốn bật hoặc tắt một chân cắm của Arduino (HIGH đặt chân ở mức điện áp cao 5V hoặc 3.3V, LOW đặt chân ở mức 0V / GND).*)
- **`INPUT` and `OUTPUT`**: Used to set a specific pin to be either an input (to read sensors) or an output (to drive actuators/LEDs).
(*`INPUT` và `OUTPUT`: Dùng để cấu hình một chân cụ thể là chân ngõ vào (để đọc cảm biến) hoặc chân ngõ ra (để điều khiển cơ cấu chấp hành/đèn LED).*)
- **`true` and `false`**: Indicate exactly what their names suggest: the truth or falsehood of a condition or expression (false is 0, true is any non-zero value, usually 1).
(*`true` và `false`: Thể hiện giá trị đúng hoặc sai của một điều kiện hoặc biểu thức logic (false tương ứng với 0, true tương ứng với bất kỳ giá trị khác 0, thường là 1).*)

### Biến và Kiểu dữ liệu trong Arduino (Variables and Data Types)

- Variables are named areas of the Arduino’s memory where you can store data that you can use and manipulate in your sketch. As the name suggests, they can be changed as many times as you like.
(*Biến (Variables) là các vùng nhớ được đặt tên trong bộ nhớ của Arduino, nơi bạn có thể lưu trữ dữ liệu để sử dụng và xử lý trong chương trình sketch của mình. Đúng như tên gọi, giá trị của biến có thể thay đổi bao nhiêu lần tùy ý trong quá trình thực thi.*)
- Because Arduino is a very simple processor, when you declare a variable you have to specify its type. This means telling the processor the size of the value you want to store.
(*Vì Arduino là một bộ vi điều khiển rất đơn giản, khi bạn khai báo một biến, bạn phải chỉ định rõ kiểu dữ liệu của nó. Điều này giúp bộ vi xử lý biết trước kích thước bộ nhớ cần cấp phát cho giá trị mà bạn muốn lưu trữ.*)

Here are the datatypes that are available:
(*Dưới đây là các kiểu dữ liệu thông dụng sẵn có trong Arduino:*)

- **`boolean`**: Can have one of two values: `true` or `false`. Takes 1 byte of memory.
(*`boolean`: Chỉ có thể nhận một trong hai giá trị: `true` (đúng) hoặc `false` (sai). Chiếm 1 byte bộ nhớ.*)
- **`char`**: Holds a single character, such as `'A'`. Like any computer, Arduino stores it as a number, even though you see text. When chars are used to store numbers, they can hold values from -128 to 127. Takes 1 byte.
(*`char`: Lưu trữ một ký tự đơn, ví dụ như `'A'`. Giống như mọi máy tính, Arduino lưu trữ ký tự dưới dạng một con số mã ASCII. Khi dùng để lưu số nguyên nhỏ có dấu, kiểu char có giá trị từ -128 đến 127. Chiếm 1 byte bộ nhớ.*)
- **`byte`**: Holds a number between 0 and 255. As with chars, bytes use only one byte of memory (8 bits unsigned).
(*`byte`: Lưu trữ một số nguyên không dấu từ 0 đến 255. Chiếm đúng 1 byte bộ nhớ (8 bit).* )
- **`int`**: Uses 2 bytes of memory to represent a number between -32,768 and 32,767; it’s the most common data type used in Arduino.
(*`int`: Sử dụng 2 byte bộ nhớ (16 bit) để biểu diễn một số nguyên có dấu trong khoảng từ -32.768 đến 32.767; đây là kiểu dữ liệu phổ biến nhất trong lập trình Arduino.*)
- **`unsigned int`**: Like int, uses 2 bytes but the unsigned prefix means that it can’t store negative numbers, so its range goes from 0 to 65,535.
(*`unsigned int`: Tương tự như int, sử dụng 2 byte bộ nhớ nhưng tiền tố unsigned nghĩa là không lưu số âm, do đó phạm vi giá trị tăng lên từ 0 đến 65.535.*)
- **`long`**: This is twice the size of an int and holds numbers from -2,147,483,648 to 2,147,483,647 (4 bytes / 32 bits).
(*`long`: Có kích thước gấp đôi kiểu int (4 byte / 32 bit), lưu trữ số nguyên lớn từ -2.147.483.648 đến 2.147.483.647.*)
- **`unsigned long`**: Unsigned version of long; it goes from 0 to 4,294,967,295 (4 bytes). Frequently used with `millis()` timer.
(*`unsigned long`: Phiên bản không dấu của kiểu long (4 byte), có phạm vi giá trị từ 0 đến 4.294.967.295. Thường được sử dụng để lưu thời gian hoạt động của hàm `millis()`.*)
- **`float`**: Holds floating-point numbers (numbers with a decimal point). It eats up 4 bytes of RAM and floating-point math functions require substantial processor time and code memory, so use floats sparingly.
(*`float`: Lưu trữ số thực dấu phẩy động (số có phần thập phân). Kiểu float chiếm 4 byte RAM và các phép tính số thực tiêu tốn nhiều bộ nhớ chương trình cũng như thời gian xử lý, vì vậy chỉ nên sử dụng khi thật sự cần thiết.*)
- **`double`**: Double-precision floating-point number. On basic 8-bit Arduino boards (like Uno), double has the same 4-byte size as float. On 32-bit boards (like Due, ESP32), it provides full 8-byte 64-bit precision up to $1.797 \times 10^{308}$.
(*`double`: Số thực dấu phẩy động độ chính xác kép. Trên các board Arduino 8-bit như Uno, double có cùng kích thước 4 byte như float. Trên các board vi điều khiển 32-bit như ESP32, nó hỗ trợ đầy đủ độ chính xác kép 8 byte.*)
- **`string` (char array)**: A set of ASCII characters that are used to store textual information. For storage, they use one byte for each character in the string, plus a terminating null character (`\0`) to tell Arduino that it’s the end of the string.
(*`string (mảng ký tự)`: Một tập hợp các ký tự ASCII dùng để lưu trữ thông tin dạng văn bản (để gửi qua cổng nối tiếp hoặc hiển thị trên màn hình LCD). Chiếm 1 byte cho mỗi ký tự cộng thêm 1 ký tự null (`\0`) ở cuối để báo hiệu kết thúc chuỗi.*)

```cpp
char string1[] = "Arduino";    // 7 ký tự + 1 ký tự null '\0'
char string2[8] = "Arduino";   // Khai báo rõ kích thước mảng 8 phần tử
```

- **`array` (Mảng dữ liệu)**: A list of variables that can be accessed via an index. They are used to build tables of values that can easily be accessed.
(*`array` (Mảng): Một danh sách các phần tử có cùng kiểu dữ liệu được truy cập thông qua chỉ số (index, bắt đầu từ 0). Chúng được dùng để tạo bảng giá trị dễ dàng quản lý.*)

```cpp
int light[5] = {0, 20, 50, 75, 100}; // Mảng gồm 5 mức độ sáng
// light[0] là 0, light[1] là 20, ..., light[4] là 100
```

### Các cấu trúc điều khiển luồng (Control Structures)

Arduino includes keywords for controlling the logical flow of your sketch:
(*Arduino cung cấp các từ khóa để kiểm soát luồng thực thi logic của chương trình:* )

#### Cấu trúc rẽ nhánh điều kiện `if...else`

- This structure makes decisions in your program. `if` must be followed by a condition specified as an expression contained in parentheses. If the expression is true, the block of code will be executed. If it’s false, the block of code following `else` will be executed.
(*Cấu trúc này đưa ra quyết định trong chương trình. Từ khóa `if` theo sau là một biểu thức điều kiện đặt trong dấu ngoặc đơn. Nếu điều kiện đúng (true), khối lệnh bên trong sẽ được thực thi. Nếu sai (false), khối lệnh theo sau `else` sẽ được thực thi. Ta cũng có thể dùng `if` đơn lẻ mà không cần mệnh đề `else`.*)

```cpp
if (val == 1) {
  digitalWrite(LED, HIGH); // Bật LED nếu val bằng 1
} else {
  digitalWrite(LED, LOW);  // Tắt LED nếu val khác 1
}
```

#### Vòng lặp `for`

- Lets you repeat a block of code a specified number of times with an index counter.
(*Cho phép bạn lặp lại một khối mã lệnh với số lần xác định trước thông qua một biến đếm chỉ số.*)

```cpp
for (int i = 0; i < 10; i++) {
  Serial.print("ciao"); // In chuỗi "ciao" 10 lần ra cổng Serial
}
```

#### Cấu trúc chọn lựa `switch...case`

- While the `if` statement is like a fork in the road, `switch...case` is like a massive roundabout. It lets your program take a variety of directions depending on the value of a single variable, keeping your code neat instead of writing long chains of `if...else if` statements.
(*Trong khi câu lệnh `if` giống như ngã ba rẽ đường, thì `switch...case` giống như một vòng xoay giao thông lớn. Nó cho phép chương trình chọn một hướng thực thi phù hợp trong nhiều nhánh dựa trên giá trị của một biến, giúp mã nguồn gọn gàng hơn nhiều so với việc viết hàng loạt câu lệnh `if...else if` liên tiếp.*)

```cpp
switch (sensorValue) {
  case 23:
    digitalWrite(13, HIGH); // Bật chân 13 nếu cảm biến bằng 23
    break;
  case 46:
    digitalWrite(12, HIGH); // Bật chân 12 nếu cảm biến bằng 46
    break;
  default: // Được thực thi nếu không có trường hợp nào ở trên khớp
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);
    break;
}
```

#### Vòng lặp `while`

- Similar to `if`, this executes a block of code repeatedly as long as a certain condition remains true.
(*Tương tự như `if`, vòng lặp này thực thi liên tục khối mã lệnh bên trong chừng nào điều kiện kiểm tra vẫn còn đúng.*)

```cpp
// Nhấp nháy đèn LED chừng nào giá trị cảm biến còn nhỏ hơn 512
sensorValue = analogRead(1);
while (sensorValue < 512) {
  digitalWrite(13, HIGH);
  delay(100);
  digitalWrite(13, LOW);
  delay(100);
  sensorValue = analogRead(1); // Cập nhật lại giá trị cảm biến
}
```

### Toán tử số học và biểu thức (Arithmetic and Formulas)

- Arduino supports standard mathematical arithmetic: `+` (addition), `-` (subtraction), `*` (multiplication), and `/` (division).
(*Arduino hỗ trợ các phép toán số học tiêu chuẩn: `+` (cộng), `-` (trừ), `*` (nhân), và `/` (chia).* )
- There is an additional operator called **modulo (`%`)**, which returns the remainder of an integer division. Parentheses `()` can be used freely to group expressions and determine the order of evaluation.
(*Ngoài ra còn có toán tử chia lấy phần dư **modulo (`%`)**. Dấu ngoặc đơn `()` có thể được sử dụng tự do để nhóm các biểu thức và quyết định thứ tự thực hiện phép tính.*)

```cpp
int light = ((12 * sensorValue) - 5) / 2;
int remainder = 3 % 2; // remainder nhận giá trị 1
```

### Toán tử so sánh (Comparison Operators)

Used in `if`, `while`, and `for` statements to evaluate conditions:
(*Được sử dụng trong các câu lệnh `if`, `while`, và `for` để đánh giá điều kiện logic:*)

- `==` : equal to (*bằng*)
- `!=` : not equal to (*khác / không bằng*)
- `<`  : less than (*nhỏ hơn*)
- `>`  : greater than (*lớn hơn*)
- `<=` : less than or equal to (*nhỏ hơn hoặc bằng*)
- `>=` : greater than or equal to (*lớn hơn hoặc bằng*)

### Toán tử Logic / Boolean (Boolean Operators)

Used to combine multiple conditions into a single compound expression:
(*Dùng để kết hợp nhiều điều kiện logic thành một biểu thức phức hợp:*)

- `&&` : logical AND (*phép VÀ logic: đúng khi TẤT CẢ các điều kiện đều đúng*)
- `||` : logical OR (*phép HOẶC logic: đúng khi CÓ ÍT NHẤT MỘT điều kiện đúng*)
- `!`  : logical NOT (*phép PHỦ ĐỊNH logic: đảo ngược giá trị từ true sang false và ngược lại*)

*Example:*
(*Ví dụ: Kiểm tra xem giá trị cảm biến có nằm trong khoảng từ 5 đến 10 hay không:*)

```cpp
if ((sensor >= 5) && (sensor <= 10)) {
  // Thực hiện tác vụ khi cảm biến nằm trong ngưỡng [5, 10]
}
```

### Toán tử phức hợp (Compound Operators)

Special operators used to make code more concise for common update operations:
(*Các toán tử đặc biệt dùng để viết mã ngắn gọn hơn cho các thao tác cập nhật biến thường gặp:*)

- **`++` and `--` (increment and decrement):**
  - `i++` (post-increment): evaluates the value of `i`, then increments `i` by 1. (*Định trị biểu thức với giá trị hiện tại của i, sau đó mới tăng i lên 1.*)
  - `++i` (pre-increment): increments `i` by 1 first, then evaluates the expression. (*Tăng i lên 1 trước, sau đó mới định trị biểu thức.*)
- **`+=`, `-=`, `*=`, `/=`:**
  - `a += 5;` is equivalent to `a = a + 5;` (*Tương đương với `a = a + 5;`*)
  - `a -= 3;` is equivalent to `a = a - 3;` (*Tương đương với `a = a - 3;`*)

### Các hàm toán học trong Arduino (Math Functions)

Arduino includes a rich set of mathematical and trigonometric helper functions:
(*Arduino tích hợp sẵn một tập hợp phong phú các hàm hỗ trợ toán học và lượng giác:*)

- **`min(x, y)`:** Returns the smaller of two numbers. (*Trả về giá trị nhỏ hơn giữa x và y.*)
  ```cpp
  val = min(10, 20); // val là 10
  ```
- **`max(x, y)`:** Returns the larger of two numbers. (*Trả về giá trị lớn hơn giữa x và y.*)
  ```cpp
  val = max(10, 20); // val là 20
  ```
- **`abs(x)`:** Returns the absolute value of x (turns negative numbers into positive). (*Trả về giá trị tuyệt đối của x.*)
  ```cpp
  val = abs(-5); // val là 5
  ```
- **`constrain(x, a, b)`:** Returns x constrained between lower bound `a` and upper bound `b`. If $x < a$, returns $a$; if $x > b$, returns $b$; otherwise returns $x$. (*Giới hạn giá trị của x trong đoạn [a, b].*)
  ```cpp
  val = constrain(analogRead(0), 0, 255); // Giới hạn giá trị đọc không vượt quá 255
  ```
- **`map(value, fromLow, fromHigh, toLow, toHigh)`:** Maps a value from one range `[fromLow, fromHigh]` to another range `[toLow, toHigh]`. Extremely useful for converting analog sensor values (0–1023) to PWM duty cycles (0–255) or percentage.
  (*Ánh xạ một giá trị từ dải đo này sang dải đo khác. Rất hữu ích để chuyển đổi giá trị cảm biến tương tự (0-1023) sang dải điều khiển PWM (0-255) hoặc phần trăm.*)
  ```cpp
  val = map(analogRead(0), 0, 1023, 100, 200); // Ánh xạ 0-1023 thành 100-200
  ```
- **`pow(base, exponent)`:** Returns base raised to the exponent power ($base^{exponent}$). (*Hàm lũy thừa.*)
  ```cpp
  double x = pow(y, 3); // x = y^3
  ```
- **`sqrt(x)`:** Returns the square root of a number ($\sqrt{x}$). (*Hàm căn bậc hai.*)
  ```cpp
  double a = sqrt(16); // a = 4.0
  ```
- **`sin(rad)`, `cos(rad)`, `tan(rad)`:** Return trigonometric sine, cosine, and tangent of an angle specified in radians. (*Các hàm lượng giác sin, cos, tan với góc tính bằng radian.*)

### Dự án thực hành 01: Điều khiển đèn LED chớp tắt (Project 01: Blinking an LED)

- The LED blinking sketch is the first program that you should run to test whether your Arduino board is working and is configured correctly. A light-emitting diode (LED) is a small semiconductor electronic component that is much more efficient than traditional light bulbs and requires very low voltages and currents to operate.
(*Chương trình chớp tắt đèn LED là dự án nhập môn đầu tiên mà bạn nên thực hiện để kiểm tra xem board mạch Arduino có hoạt động bình thường và môi trường lập trình đã được cấu hình chính xác hay chưa. Đèn đi-ốt phát quang (LED) là linh kiện bán dẫn nhỏ gọn, tiết kiệm năng lượng hơn nhiều so với bóng đèn truyền thống và hoạt động ở điện áp thấp.*)

**Hình minh họa slide 82–83:** Sơ đồ kết nối phần cứng và giao diện phần mềm Arduino IDE:
- Chân cắm LED tích hợp sẵn trên board Arduino Uno nằm ở chân số 13 (**Pin 13**), có kèm sẵn một điện trở bảo vệ onboard nối xuống mass (GND).
- Các nút chức năng trên thanh công cụ Arduino IDE: nút **Verify** (hình dấu kiểm tròn để biên dịch kiểm tra lỗi cú pháp) và nút **Upload** (hình mũi tên sang phải để nạp mã nguồn biên dịch vào vi điều khiển).

#### Mã nguồn hoàn chỉnh (Example 01: Blinking LED)

```cpp
// Example 01 : Blinking LED
// Chương trình mẫu 01: Điều khiển đèn LED nhấp nháy

const int LED = 13; // Khai báo hằng số LED gắn với chân Digital 13

void setup() {
  pinMode(LED, OUTPUT); // Cấu hình chân số 13 làm ngõ ra (OUTPUT)
}

void loop() {
  digitalWrite(LED, HIGH); // Xuất mức cao (5V): Bật sáng đèn LED
  delay(1000);             // Tạm dừng chương trình trong 1000 ms (1 giây)
  digitalWrite(LED, LOW);  // Xuất mức thấp (0V): Tắt đèn LED
  delay(1000);             // Tạm dừng chương trình trong 1 giây
}
```

#### Phân tích chi tiết từng bước của chương trình (The Code, Step by Step)

1. `// Example 01 : Blinking LED`
   - A comment is a useful way for us to write little notes. The preceding title comment just reminds us that this program blinks an LED.
   (*Dòng chú thích tiêu đề giúp người lập trình ghi nhớ mục đích và chức năng của tập tin mã nguồn.*)
2. `const int LED = 13;`
   - `const int` means that `LED` is an integer number that cannot be changed (i.e., a constant) whose value is fixed to 13. It tells Arduino to replace the identifier `LED` with the number 13 throughout the program, specifying that the LED is wired to digital pin 13.
   (*`const int` chỉ định `LED` là một hằng số nguyên có giá trị cố định là 13. Nó báo cho trình biên dịch thay thế từ khóa `LED` bằng số 13 ở mọi vị trí xuất hiện, giúp mã nguồn rõ ràng, dễ bảo trì khi cần đổi sang chân cắm khác.*)
3. `void setup() { ... }`
   - `void setup()` tells Arduino that this block initializes the board configuration. The opening brace `{` marks the start of the block and the closing brace `}` marks its end. It runs only once when the board is powered on or reset.
   (*Hàm `setup()` được vi điều khiển thực thi một lần duy nhất khi khởi động hoặc nhấn nút reset để thiết lập cấu hình ban đầu.*)
4. `pinMode(LED, OUTPUT);`
   - `pinMode()` is a built-in function that configures a specified pin as either `INPUT` (to read) or `OUTPUT` (to provide current). In this project, to drive current into the LED, pin 13 must be configured as `OUTPUT`.
   (*Hàm `pinMode()` cấu hình chế độ hoạt động của chân vi điều khiển. Để cấp dòng điện điều khiển đèn LED phát sáng, chân 13 phải được cấu hình là ngõ ra `OUTPUT`.*)
5. `void loop() { ... }`
   - `loop()` specifies the main interactive behavior of the device. It executes sequentially instruction by instruction and then repeats indefinitely until the board is switched off.
   (*Hàm `loop()` chứa thân chương trình chính, được lặp đi lặp lại tuần hoàn vô tận cho đến khi ngắt nguồn điện.*)
6. `digitalWrite(LED, HIGH);`
   - `digitalWrite()` sets the output voltage level on a pin configured as `OUTPUT`. The first argument specifies the pin (`LED` = 13), and the second argument specifies the state (`HIGH` = 5V, turning the LED on).
   (*Hàm `digitalWrite()` điều khiển mức điện áp ngõ ra. Tham số thứ nhất là chân điều khiển (chân 13), tham số thứ hai là trạng thái `HIGH` (mức cao 5V), kích hoạt đèn LED sáng lên.*)
7. `delay(1000);`
   - `delay()` makes the processor wait quietly and do nothing for the specified number of milliseconds (1000 ms = 1 second). During this interval, the LED remains in its current ON state.
   (*Hàm `delay()` tạm dừng bộ xử lý trong khoảng thời gian xác định tính bằng mili-giây (1000 ms = 1 giây). Trong thời gian này, đèn LED duy trì trạng thái bật sáng.*)
8. `digitalWrite(LED, LOW);`
   - Sets digital pin 13 to `LOW` (0V / Ground), shutting off the current and extinguishing the LED.
   (*Xuất mức điện áp thấp `LOW` (0V) ra chân 13, ngắt dòng điện và làm đèn LED tắt.*)
9. `delay(1000);`
   - Pauses execution for another 1 second with the LED in the OFF state. When the end of `loop()` is reached, the processor immediately jumps back to the top of `loop()`, creating a continuous, rhythmic 1-second ON / 1-second OFF blinking cycle.
   (*Tiếp tục dừng 1 giây khi đèn LED đang tắt. Khi kết thúc thân hàm `loop()`, bộ xử lý quay lại dòng lệnh đầu tiên của `loop()` để lặp lại chu kỳ chớp tắt đều đặn.*)

### Dự án thực hành 02: Dùng nút nhấn điều khiển đèn LED (Project 02: Using a Pushbutton to Control the LED)

- In interactive electronics, buttons and switches are basic sensors that detect human touch. Unlike an automatic blinker, this project creates an interactive system where the LED turns ON only while a physical pushbutton is held down, and turns OFF as soon as the button is released.
(*Trong các hệ thống điện tử tương tác, nút nhấn và công tắc là các cảm biến tiếp xúc cơ bản nhất phát hiện tác động của con người. Khác với mạch chớp tắt tự động, dự án này tạo ra một hệ thống tương tác thực thụ: đèn LED chỉ bật sáng khi người dùng ấn giữ nút nhấn và lập tức tắt đi khi nhả nút.*)

**Hình minh họa slide 90:** Sơ đồ đấu nối nút nhấn với Arduino Uno:
- **Đèn LED:** Chân dương (Anode, chân dài) nối với chân **Pin 13**, chân âm (Cathode, chân ngắn) nối về **GND**.
- **Nút nhấn (Pushbutton):**
  - Một chân của nút nhấn nối với nguồn dương **+5V**.
  - Chân đối diện của nút nhấn nối vào chân tín hiệu ngõ vào **Pin 7** của Arduino, đồng thời nối qua một điện trở kéo xuống (**Pull-down resistor 10k$\Omega$**) về cực âm **GND**.
  - *Nguyên lý điện trở kéo xuống:* Khi nút nhấn không được ấn, chân 7 được nối chắc chắn về GND qua điện trở 10k$\Omega$, giữ chân ở mức logic `LOW` (0V) ổn định, chống hiện tượng nhiễu trôi nổi (floating input). Khi ấn nút, dòng điện từ 5V chạy thẳng vào chân 7, đưa chân lên mức logic `HIGH` (5V).

#### Mã nguồn hoàn chỉnh (Example 02: Pushbutton LED)

```cpp
// Example 02: Turn on LED while the button is pressed
// Chương trình mẫu 02: Bật sáng đèn LED khi ấn giữ nút nhấn

const int LED = 13;    // Chân số 13 điều khiển đèn LED
const int BUTTON = 7;  // Chân số 7 nhận tín hiệu từ nút nhấn

int val = 0;           // Biến lưu trữ trạng thái đọc được từ chân nút nhấn

void setup() {
  pinMode(LED, OUTPUT);   // Thiết lập chân LED (13) là ngõ ra (OUTPUT)
  pinMode(BUTTON, INPUT); // Thiết lập chân BUTTON (7) là ngõ vào (INPUT)
}

void loop() {
  val = digitalRead(BUTTON); // Đọc mức điện áp logic từ chân 7 và gán vào val

  // Kiểm tra xem nút có đang được ấn (mức HIGH) hay không
  if (val == HIGH) {
    digitalWrite(LED, HIGH); // Bật sáng đèn LED
  } else {
    digitalWrite(LED, LOW);  // Tắt đèn LED
  }
}
```

#### Phân tích mã nguồn dự án nút nhấn

- `pinMode(BUTTON, INPUT);`: Cấu hình chân 7 làm ngõ vào để lắng nghe điện áp từ mạch nút nhấn.
- `val = digitalRead(BUTTON);`: Hàm `digitalRead()` kiểm tra mức điện áp trên chân số 7. Nếu có điện áp 5V (nút được ấn), hàm trả về giá trị `HIGH` (1); nếu là 0V (nút nhả), hàm trả về `LOW` (0).
- `if (val == HIGH)`: Cấu trúc rẽ nhánh điều khiển đèn LED tức thời theo trạng thái ấn/nhả nút của người dùng mà không cần dùng hàm `delay()`.
"""

print("Generated Arduino continuation text (length:", len(arduino_slides_text), ")")
