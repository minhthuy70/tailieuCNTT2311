## Trang 100

Receive interface Reccive interface dùng de nhan gói tin; nó duợc djnh nghĩa như sau: Intcrtacc Reccive evcnt mcssage receive(messupe IsB. void* payload , uint8_t len);

Tham số payload trong sự kiện receive( phải thong nhẩt với lòi gọi phù hợp với Packet-getPayloadO) se trả vẻ và chicu dàỉ len phải phù họp với chiêu dài cúa Packet. getPayload() sê trả vê. Một nguời sử dung intertace Receive có lựa chon khi dieu khiên một sự kiện receive là: Trà vê msg mà không cham vào nó 2. Chép một số dữ liệu ra từ payload và trả về msg 3. Luu msg   trong một Irame cục vê   một message_ t* khác cho lớp thảp hơn sử dung. Ửng với từng tnrởng hợp trên có một sô ví dụ nhu sau: Truong hợp message Receive receive(message msE vaid* paylond, uint8 len) rclurn msg:

Truởng hợp Untlg valve, Mcssapc Reccivc reccive(mcssage Mse void* payload   uint8 len) if (len > sizeof(uint16_t)) { uint 16 nval (nx_uintl6 t*)payload; valuc "nval;

Tclum Mse

IfTrrong hop 3 message buf; message &buf;

## Trang 101

Mcssage

Receive reccivc(mcssagc

msg   void* payload , uint8

mcssage unp nisg; processTaskO; relurn Unp;

TinyoS 802.15.4 frame 802.15.4 là   một   dinh dang gói  tin tâng data-link physical cho mang không dây tiêt kiệm nang lượng dược dùng trong nhiêu TinyOS platform khác nhau [13] TinyOS có hai djnh dang frame cho 802.15.4, Dang thứ nhât là T-Frame (TinyOS Frame) cho mang TinyOS, không chia sẻ kênh tuyen cho các kién trúc mạng không dây khác Định dang TinyOS 802.15.4 T-Frame có dang su:

902,25

Heedey

202.19,4

Trong AM type là một truởng một byte đơn; chỉ ra kiêu active message chứa payload. Dạng thứ hai của 802.15.4 là I-Frame, cho phép   mang TinyOS chia sẻ kênh của nó với mạng 6lowpan. Ở dang này có thêm trường 6lowpan trước trường AM type đễ có thé hoạt dộng kêt hợp với mang lowpan. Định dang TinyOS 802.15.4 [-Framc có dang nhu sau:

4rt

61o*7 n

Rx &ye

Trong đó, trường AM type gióng như ở T-Frame Phần hiện thuc cúa T-Frame và [-Frame có thể được tim thây trong tinyos-2 .x/chips /cc2420/; Mặc dịnh, TinyOS 802.15,4 stack sử dung I-Frame, và khi muon sử dung dang 1-Frame thì có thê thêm tùy chon 'tframe' khi biên dịch. Khi sử dụng tùy chon nay thỉ giá trị TFRAMES_ENABLED (được định nghĩa trong CC2420h)

## Trang 102

CC2420 Radio Stack CC2420 software stack chửa nhieu lớp (layer) khác nhau nam giữa ung dung và phân cung Tang cao nhât cúa radio stack dieu chỉnh dữ liệu và hcader trong mỗi packet, trong Lhi ung thấp nhẩt xác dịnh các hành vi gửi và nhan. Kiến trúc Layer Trong CC2420 Radio stack mỗỉ layer là một thành phần phân biệt, nó có thê cung câp và sử dụng 3 bộ interface sau: Send, Reccive và SplitControl. Nêu một layer cung cáp một trong các interface dó thì nó cung có thẻ sử dung từ các layer bên duới nó trong stack . Víđu như: provides interface Send; Mscs intcrfacc Scnd SubSend; provides interface Receive: uscsIntcrlacc KCCCIvc1s SubReceive; provides interface SplitControl; interface SplitControl subControl; Mô tả Layer Các Layer trong hệ thống CC2420 radio stack được xếp từ trên xuống như hinh sau:

Hinh 4.10 Kiên (ruc lớp trong CC2420 Radio Stack

ActiveMessageP: đây là tầng cao nhất, chịu trách nhiệm diên dây dủ thông tin va packet header và cung cấp thông tin vê gói tin tới lớp ứng dung

## Trang 103

Unique Send Layer: Tầng này tao ra một chi số thứ tpr dữ lỉệu độc nhất Data   Senquencc   Number   (DSN) cho packct header. Byte giá trị nảy duyc tang lên mối lân gói tin gửi ra ngoài, bắt dau bng một sỗ gan ngẫu nhiên Ben nhan có the phát hiện những gói tin trùng nhau bẳng cách s0 sánh chỉ sô này với chi sô cúa gói tin đã nhận tvớc đó PackerLink: Cung cấp chức náng gửi lại tự dông và chịu trách nhiem gửi lại gói tin nêu không nhận duợc ACK từ bên nhận. Low Power Listening   Implementation: Cung cấp hiện thuc ling nghe nang luợng thâp bât dông bộ, dược kích hoat cho từng gói tin và tâng nảy sễ guỉ lai liên tỉêp các gói tin Ta ngoải cho dên khi nhận duợc phản hổỉ từ bên nhận hay hêt thòi han trao đỗi. UniqueReceive: luu trữ lịch sử các địa chỉ nguôn và DSN byte cúa một sò gói tin đã nhận và hỗ ưrợ loc ra các gói tin nhan trùng lai. TinyOSNetworkC: cho phép TinyOS2.x radio stack kêt hợp hoat dộng với mnang non-TinyOs nhu 6lowpan) CSMAC: lớp này chịu trách nhiỆm định nghĩa byte thông tin 802.15,4 FCF trong gói tin ra ngoai, cung câp gỉá tri thời gian chờ mặc dinh khi phát hiện một kênh dang dung và dịnh nghĩa thủ tục táVmở cho radio. TransmitP ReceiveP: các   lớp nay chju trách   nhiem tương tác trực tiếp vớỉ radio thông qua SPI bus, interrupts vả duong GPIO

4.2.3. Hệ diều hành Contiki Contỉki là hệ điều hanh nhỏ gon nhe (lightweight) hỗ trợ cơ chếdynamic loading và thay thế từng chuong trinh, dịch rienp Contiki dược xây dựng dựa trên cu chế thco sự kiện (event-driven) nhung cung câp thêm tùy chon preemptive multi - thrcading cung cấp cho từng process Tính chât dynamic loading

## Trang 104

phù hợp với môi tnrờng có nhiêu ráng buộc vể tài nguyên náng luong nhu trong mang cám biên khong day. [14] 4.2.3.1. Cẩu trúc một ứng dung trên Contiki Các ứng dung trên Contiki viét bing ngôn ngữ €, và có câu Lrúc như sau:

LCn

M=d Soostakchh" //1al Lia D{dcedl IoaSier Junae) ; Fenale 2222 dura Ler AhTs stn CerlTcie ! 7/252 42i9 Gha lcxncle , Jnh n

k

aiu  ucC ne n6o2 nirs shuledl

hen Der Ca Ehc) en nq1 4 Viac

Kxlnsna] Avenfa

{Hay Cu Clls1t

inceena] n

Ppocrys Doil;/ket

Biên dịch chu(g trinh Để biên dịch một ứng dung Contiki, ta cản file sau: File ứng duung contiki chúa các hiện thực, dịnh nghia úng dụng (mã nguôn) Makefile: cho phép chúng biên dịch và chi ra các file càn thiêt cho ứng dung; phai duợc luu trong thu muc project cung chung với  file nguon ửng dung trên Mộtmau Makcfile có dạng như sau: CCHIILI OfC nlzC 54Tu Anclas

Dòng đầu tiên chỉ ra nguôn cua thu muc Contiki (thông thuong lhomeluser Contiki); dong thứ hai là ứng dụng dê biên dịch và dong cuòi cung chứa dịnh nghĩa của Contiki core system và trỏ ra tới Makelile riêng biệt của từng loai platform mà ta sử

## Trang 105

dung Makefile include phải luôn nằm ngay trong thư muc góc Contiki (home/user/ContikiMakefile ỉnclude). Đê biên djch chuong trinh chúng ta phải chỉ platform mục tiêu mà ing dung se chay lên. Nêu không chỉ ra thì mặc dịnh úng dung chay tren máy hiện tại (Native Platform) make TARGET-<Tên thiết bj> <tên Project > Nêu ta muốn biên dịch nhiều hon một lần cho platform được chon dó ta có thễ chỉ dịnh cho Contiki nhớ Iựa chon phàn cung dó cùa minh bang cách chỉ ra savetarget nhu sau: make TARGET=<Tên thiét bj savctargct Đê upload Contiki lên thiét bị ta dung lenh: sudo chmod 666 /devl <tên porz (dê cẩp quyên nạp code lin thiet bị qua port) [IAKE clen ứng dung? upload TARGET=<tên thỉct bị> Đê xem output cúa chưong trinh dang chay trên thiêt bi, chung cân phải login vào serial port đê KeMn . Ta thực hiện lệnh: make login TARGET4ên thict bP

4.2.3.2 Cảc thành phẩn; dich vu co ban trên hệ đỉêu hành Contiki

Kiên trúc kernel Kerncl Contiki bao gôm một bộ dịnh thời gon nhe gửi các sự kien (event) tới các tiên trinh dang chay và goi các tien trinh thco chu kỳ. Tât cả các chuong trinh thuc thi dưgc kích houl (triggcr) bởi các sự kiện gửi từ kernel thông qua chê chon (polling mechanism). Kerel hỗ trợ loai sự kiện là: bất đồng bộ (asynchronous) và đổng bộ (synchronous). Su kiện bat donp là hinh thúc goi thủ tuc châm Su kiện dong bô tuong tự nhu bât dông bộ nhưng ngay lập tửc làm cho tien trinh muc tiêu duợc dịnh thòi_ Việc diêu khien thyc hiện tỉên trinh chi xảy sau khi muc tiêu da hoàn thành sự kỉện;

## Trang 106

Cơ chế bỏ phiếu chon (polling mechanism), cơ ché này duợc xem nhu các sự kien tiên cao (high priority) se duợc dịnh thởi trong khoảng giữa mỗi sự kien bal dông Viec bỏ phiếu dược sử dung bởi các tien trinh mà hout dong gân phân cứng dề kiểm tra trạng thái cập nhật của thiết bị phân cứng: Khi một lân bỏ phicu duợc djnh thởi, tất cả tiến trinh thực hiện việc quan lý bỏ phiêu sẽ dưrqc goi thco thứ tự ưu tien cúa chúng Contiki sử dung slack chung chia sé cho tât cả các tién trình thuc thi.

Loadable programs Các chuong trinh có thể load được sử dung hàm Lhay dổỉ vị tong thời gian chạy (run-time) và đinh dang nhị phân chứa thông tin đja chỉ. Khi một chưong trình dược load vào hệ thong. dâu tiên loader sẽ dịnh vi không gian bộ nhớ dựa trên thông đuoc cung câp trong dinh dang nhị phân. Nêu dja chi dịnh không thành công chuong trinh sẽ bị hủy bỏ. Nêu chưong trình dược load vằo bộ nhớ thành công, loader goi hàm khởi tạo, hàm khởi tao sè bẳt dâu và thay thê một hay nhiêu tiên trình đế chạy chưong trinh duợc load vào.

Chê độ tỉêt kiệm nảng Iượng Trong mnang cảm biên, dê tỉêt kiem nang luợng node cam bien có thê hoat dộng che đô inactive Contiki kernel không dinh nghĩa rõ ràng cho tiêt kiem nang Iượng nhung cho phép úng dụng chỉ dinh hệ thống hoạt dộng các cơ chế tương tự dê Liêt kiệm nang lưong  Đê ửng dung quyêtdinh diêu hành, hé thông djnh thởi buy ra kích thước cua event qucuc Thông tin nay dưpc sử dung dê giảm nẳng lưong tiêu thụ của bộ xử lý xuóng khi không có sựr kien nảo có lịch Bộ xử lý se dánh thúc lúc phản hổi interrupt, trinh bầu chọn sẽ chạy dễ quản lý sự kiện bên ngoài.

Các dịch vụ Trong Contiki, dịch vụ là một tiên trinh thuc chức nang thê đưoc dung bởi các tién trinh khác. Một dịch vu có thể có dang

## Trang 107

nhu môt thư viện chia sẻ. Dịch vu có thẻ thay dốỉ linh hoạt lúc chay (run-time) và vi vậy, có thê liên kêt done Thông thuip djch bao gôm bộ giao thức giao tiếp; các driver thỉễt bị cảm biên và các chúc nang lớp cao nhu quán lý dữ liệu cảm bicn. . . Dich vụ duợc quán lý bởỉ một servỉce layer ngay phía trên kernel . Server layer theo dõi các djch vu chay và quản lý cách cài dặt dich vu. Một djch vụ dược xác dịnh bởi một chuỗi text mlô tà dịch vu đó. Một dịch vu bao gôm nhiêu service interface và môt tién trình đê hiện thuc interface dó. Service interface bao gồm một version numbcr và bẳng chức năng với các con trỏ trỎ tới các hàm hiện thurc intcrface. Một chuong trinh ứng dung dung dịch vu là thư vỉện sơ khai (stub library) để giao tỉếp với các djch vụ khác. Stu library dugc liên kêt với ứng dung và sù dung service laycr dê tim tiên trình djch vụ Khi một djch vụ được dịnh vị, dich vụ gổc se ghi nhớ process ID cúa tiên trinh djch vu và sử dung ID dó cho tât cà Liên trình trong tuong lai. Chuơng trinh gọi dịch vụ thông service interface gâc Lân đẩu tiên dịch vu dưvc gọi, SCrVCi intertace gỗc thuc hien việc tim kiêm dịch vu trong service layer. Nếu dich vu chi ra dà tôn tại trong hệ thông, thì se trả vẻ con trỏ tới service interface dó. Chi sô version numbcr trong service interface duợc kiễm tra với version trong interface gỗc. Thêm vào dó, service interface chứa các con trỏ tớỉ tât cà các hàm dịch vụ Các hàm hiện thurc này chúa trong tiên trình dich vu. Nêu version của dich vụ gốc khớp với sô trong service interface, thì interface gổc gqi hiện thyc cúu hàm dược yêu câu.

Cơ ché giao tiếp Giao tiêp là khái niệm cơ bản trong mạng cảm bién. Trong Contiki, giao tiếp dưgc hien thyrc như một dịch vụ dề có thể thay thê trong lúc chay- Dich vu này có the load dòng thởi nhicu bộ giao tiêp khác nhau, việc này có nghia trong thử nghiem khi

## Trang 108

muôn so sánh nhiêu bộ giao thức giao tiếp khác nhau. Ngoài ra, các bộ giao tiêp này có thể chia thanh nhiều dịch vu khác nhau như trong Hinh 4.11:

Corrmunication stack

Applicaton

Aouting Frotocol ~

Routing protocol

Devico Oriver

Device driver 2

Haroware

Hình 4. 11. Sơ dỗ cúc cơ chê gỉao tỉếp trên Contiki 4.2.4. Hệ đỉều hành Raspbian OS Hệ diêu hành Raspbian là hệ điều hành miễn phí dựa trên nên tung Debian được tối ưu hóa để chạy trên thỉết bj Raspberry dicu hành   này ban dau dược   phát   triên   bởi Mike Thompson và Peter Green nhung sau dó dược công đồng nhiệt tinh hỗ trợ dê ngày cang hoàn thỉện nhu hiện nay Iheo thông tin lừ trang cong dong phát trien; bên trong hệ diều hành Raspbian này gôm hơn 35.000 gói thư viện (packages), nhiêu ửng dung biên dịch từ truớc (pre-compiled software) dược săp xêp tô chức một cách hợp lý đê cài đặt trên thiêt bị Raspberry Pi. Kiên trúc hệ diều hành Raspbian được thẻ hiện như Hinh 4.12

hutps://www raspbian org RaspbianAbout

## Trang 109

McoiaAppiicaton

Applicauon

Appiicauon

OpenmaX

Opencies

ponyc

Kernci Dnyer (vchioi

vidcocon

Hinh 4.12 Kiến trúc he điều hanh Raspbian OS

Kiến trúc và mô hinh nhân Raspbian OS dpra theo kiến trúc monolithic. Raspbian hỗ trợ nhiều ngôn ngữ lập trình khác nhau như Python; €, C++, Java; Scratch và Ruby cung như các ngôn ngữ khác nhu HTMLS, Javascripts, JQucry. Raspbian sử dung dịnh thời theo cơ chế real-time precmptive, Vê phưong dien giao tiêp mạng và giao thức mạng. Raspbian hỗ trợ khả nẵng kết nối dang thông qua SPL, UART, I2C, và USB giao tiêp mạng thông qua bộ giao thức TCPIIP, Bluetooth cũng như hỗ trợ các thu viện mở đê sử dung các giao thức mạng không dây khác như LTE Raspbian có thê duợc mô phóng khi sử dung công cu mô phỏng QEMU ARM đê mô phỏng kiên trúc ARM trên thiết bị Raspberry Pỉ. Về phuơng diện bẳo mật, Raspbian OS hỗ trợ nhiêu cong cụ mã hóa, chứng thực, phân quyen phù hợp cho cac úng dung IoT. Cộng dồng nguòn mở hỗ trợ phát triền các công cu mã hóa manh mẽ trên Raspbian như AES 128, AES 256, DES, Blowfish. Về phuong diện tiêu thụ nẫng luong môt đặt điêm tuyệt vời cúa các máy tính sử dung kiến trúc ARM là tiêu thụ nang luợng thấp, mỗi thiết bi Raspbenry Pi chay hệ dỉều

## Trang 110

hành Raspbian sử dung cong suât là 2W (khi chạy với tỗc dộ 70OMHz). Việc tiêu thu nẵng lưong trên Raspbian tùy thuộc vao loai thiêt bị, loại ứng dụng dang chạy trên thiêt bị dó. Ngoài các dặc diem trên, Raspbian còn hỗ trợ kêt nổi da phưong tien hiệu quà cho phép thuc hiện truyên audio, vidco bang cách sử dụng giao thức SIP (session initiation protocol) và giao thúc RTP Raspbian cũng hô trợ streaming HD Videos và Audios với dộ phân giải lên dên I08Op30, 720p60 thông qua khả năng kêt nổi với thiét bj camera qua cong giao tiêp có sán trên board mạch Raspberry Pi. Raspbian hỗ trợ nhiều thư viện; phân mềm mã nguon  mở đê xử lý hinh anh, video trên thiêt bị Vớỉ những dặc   diêm kỹ thuật  nôi bat  dó hệ  dieu hanh Raspbian cung với  thiết bị Raspberry Pi luôn dugc sử dung nhiêu [one Các ửg dung IoT như một máy tính thu nhỏ, có thê thyc hien nhiêu tác vu tinh náng khác nhau. Bên canh các hệ diều hành dã trinh bày trên; nền tane phán mêm dược sử dụng cho các thiêt bị IoT còn rât da dang và phong phú Một số hệ diều hành khác có thễ kể đến nhu: RIOT, LiteOS, FreeRTOS, uClinux;  Android Things Tùy thco nhu câu thuc tê, yêu câu cu thê của lung hệ thong IoT muon phát triên mà ngưòi phát triên cân chon lựa các nên tảng phân mêm phù hop- tôi ưu nhât cho hệ thong cua minh.

## Trang 111

1 5 1F # 5 2 9 } 9 ; 1 ; 1 1 111 1f f alal 1 Il | 1 mli Jul g : 91 1 9 1 1 1 1 / | Ẳ:|  5 ẵ 1 ẵ 1 449 1 1 429 1 9 2 ắ 1 = ắ 1 1 1

## Trang 112

ẵ

2 { 1 7E 1 Ễ Ẳ Hak 5 ý 5 5 1 1 F |a 12 8' 8 5 Ễ 1 É ÍF Í { 11 | 8 1 1 1 1 Ễ 888 1 1 @ 1 P pF ; 1 5 8i 8 4 7 5 | B f '{í438 6 é{ ! 7e 1I Ỉ Ii 5 1 f 7F 1 5 ắ 5 1

## Trang 113

2 ; ệ 9 ; [ 1 2 1 51 UI U 1f 8l 11kaai 18ia 1a 5 5 1 1 ; ; ; ẵ2 4/

8 8

3 f ẳ p 1/ /

í 1 ! 1 1 11

## Trang 114

Thóng phân tong hợp tù hai bảng; Bảng 4.2 và Bảng 4.3 thây hỉện nay có rât nhiêu nên tang phân mêm, hệ đỉêu hành hỗ trợ phát trien các giải pháp IoT với nhieu dfc trung, đặc tinh kỹ thujt khác nhau, Chính vi the tùy theo nhu cau sử dung, tùy theo tinh nang yêu câu cúa giải pháp IoT muôn phát triên mà các nhả phát trien hệ thống có thể chon lựa cho minh một môi truùng phù hợp. Ví dụ, Uong môi trường nphien cứu học thuật nhiêu tuởng dại học trên thê giới, khi nghiên cứu vê mang cảm biên không dây, thiêt bị IoT tiêt kiệm nang luợng  tài nguyên han chê thì các hệ diêu hành nhu TinyOS Contiki thuờng dưgc lựra chon. Ngoài ra, môt nên tang khá phổ biến và dễ dang tiep can hiện nay đó là máy tinh nhúng Raspberry Pi với hệ dieu hành   Raspbian Dây là một thiêt bj nhúng hỗ trg khá dầy đủ chức nang cúa một máy tính thu nhỏ, cho phép ngườỉ lập trinh sử dung những tien ích cúa ngôn ngữ lập trinh bậc cao như Python   NodeJS , Java. . dê phát triên các ứng dung cúa minh một cách tien lợi. Tóm lai, với sựr phát trien không ngừng cúa công nghelân luợt ngày càng nhiêu nên tang phân cúng duvc sản xuât chê tạo, kèm thco dó là các giải pháp phân mêm cũng duợc lao ra mang dên sự da dang chung loai và nhiêu sự lựa chon cho nguòi hoc, nguởi phát triên giải pháp IoT với nhiêu câp dộ, nhiêu cách tiêp cận khác nhau.

BAI TẠP CHƯƠNG

Hãy so sánh các nhóm phan cung dung trong oT và liet ké các thiet bi thuóc moi nhóm. Hay trinh bày kién trúc và hoat động cùa một chuong trinh NesC tren TinyOS . Hay trinh bày kién trúc và hoat động cúa môt chưong trinh tren ContikiOS. Hfy liệt ke các loai phan cứng phàn mèm và cảc cảm bién (néu có) đẻ xáy dung môt ủng dung gỉám sát chát luong không khí. Từ nen tảng Arduino và Raspberry PI hãy thiét kế úng dung giám sát môi trường và điều khiến thiết bi cho nhả thông minh

## Trang 115

Tu nen tảng CC2530, hãy thiét kế ửng dung Nông nghỉ#p thông minh. HJy xác đjnh loal Phan cung phan mem cám biến đé xảy dung hệ thong cảnh bảo cháy rung có các nút cảm bien đuoc cap nguón bang pin vói yeu câu tối ưu náng lưong sử dung đé thời gian hoat đông cúa Úng ' dung là lớn nhat.

## Trang 116

CHƯONG 5

ĐIỆN TOÁN ĐÁM MÂY,

ĐIỆN TOÁN CẬN BIÊN VÀ IOTS

Van vật kêt nổi Intcmnet mở ra nhiều thách thức không chỉ với vân dê phát triên gỉảỉ pháp phân cứng, phân mêm dê trien khai ung dung mà còn dut ra nhiêu cơ hội và thách thức trong viec luu trữ và xừ lý dữ lieu. Gan đây, Cúc công nghệ nôi bật vê hạ tang tính toán như đien toán dám mây (cloud computing) tính toán cận biên (edge computing mờ ra khà náng tích hợP 7 vớỉ các gỉảỉ pháp IoT, mang lar  những cai   thien lón vêkhả náng mo rông (scalability) san sàng cao (availability) cho các ứng dung IoT. Nội dung chuong này tập trung trinh bày những dặc diêm nổi bật của hạ tng diện toán dám mây; kiên trúc tính toán cân biên trong tich hop giải pháp IoT Phân dâu cùa chuong gỉới thiệu sa lugc vê dien toán dám mây, nhung dặc trung co ban, đặc diêm nỗi bật và lợi ích mang điện toán dám mây mang lai. Các kiêu mô hinh đien toán đám mây phổ biên cũng đuợc trinh bay , cac mô hinh nay bao  gôm   Infrastructure-as-a-Servicc (IaaS) Platform-as-a-Scrvicc (PaaS) và Soltwarc-as-a-Scrvicc (SaaS) Phân tiêp theo chuong tặp trinh bày vê kiên ânuag trúc tính toán can bien trong IoT. Các vân công nghệ, những đặc đdiêm kỹ thuật nôi bật cúa công nghe tính toán can biên trong Io cung duvc trinh bay nguởi đoc có cái nhin tong quan, nẵm bẳt dugc xu hướng phát triên cung như các van dê tôn tai dang thu hút sự quan tam cua giới nghiên cứu trong linh vực. Bên canh đó, một giai pháp tan dung nên tang tang  dien toán  dám mây của truờng UIT Cloud OpenStack cung dưuc trinh bày cuôi chuong nhu một minh họa cho khả nẵng sử dung ha tang dien toán dám mây trong việc triên khai giải pháp lol_ Minh hoa này trinh bày viec xây dựng một hệ thong thử nghiệm IoT với số lượng nốt lón thông qua các cơ chê ảo hóa mạng; ào hóa tài nguyên tính toán; tài nguyên kêt nôi trên nên tang hạ tang diện toán dám mây mã nguòn mở nổi tiéng là OpenStack.

## Trang 117

Thong qua nội dung trinh bảy trong chuong nảy, nguời dọc có thê nẳm bắt được kién trúc tong quan cua một hệ thong IoT kêt hợp hạ tang diện toán dám mây và tính toán cận biên; Nắm dược những dặc diêm, lợi ích, phân loai các mô hinh dịch vy trong diện toán dám mây cũng như các vấn dề nghiên cúu, thách thức trong IoT kết hợp tính toán cận biên giúp người đoc dễ dàng tiêp cận, khi thuc hiện khảo Sát cung như triên khai các nghiên cứu có liên quan trong lĩnh vực. 5.1. Kiên trúc tong quan hệ thống IoT tích hợp điện toán dam mây và điện toán can biên 5.1.1. Kién trúc tung quan

Eona

Hinh 5,1. Kién trúc lunk uan phân lởp Edge, Fog và Cloud trong IoT'

Industrial   Intcmct Things   (IoT) Applications  of Fdgc Computing: Review and Futurc Dircctions, hntpar a/xIV OTg abs 1912.00595

Fop

## Trang 118

phát triền bung nổ của công nghệ IoT dẫn dến kién trúc hệ thống mang ngày cang phức tap và phân chia thành nhiêu lớp dêdáp úng nhu câu ngày càng cao cúa con nguyỉ, Trong hưởng đó, các hệ thông, ứng dung IoT hiện đại ngày này thuờng dược tỗ chức thanh các lớp bao gôm: lớp thiêt bị IoT, lớp thiêt bị cận biên, lớp trung tâm dữ liệu tren ha tang dỉen toán dám mây - Hinh 5.1 trinh bay tong quai môi liên hệ gita các thành phân trong kiên trúc hệ thông IoT dpa trên nên tảng diện toán dám mây (cloud computing) và tính toán can biên (edge computing) Các thỉết bi IoT: là các thiết bị dầu cuối, bao gổm thiết bị cảm biến, dộng co diều khiễn phuc vu cho nhiêu ing dung khác nhau trong nhiêu lĩnh vuc dời song xà hội. Các thiêt bi IoT này có chúc nang thu thập dữ lieu từ môi truòng xung quanh gửi đên các thành phần phía sau cúa hệ thông Tùy theo lung loai giải pháp kết nối khác nhau mà thiêt bị IoT này có thê gửi dữ liệu trực tiếp đén trung tâm dữ liệu hoặc gửi trung gian den các thiết công (gateway) các thiêt bi mang cận biên (edge devices). Xu hướng hiện nay, dữ liệu thu thập đưgc từ các thiêt bị IoT biêrag dược gửi đến lưu trữ và xử lý trực tiếp tại các thiết bi cận biên  tận dụng khả năng tính toán; phản hôi thời gian tực, đảp ỉmng nhu câu ngày càng cao của người dùng Thiết bỉ tinh toán cân biên: là các thiết bị nằm ở ria hệ thông  ngay phía sau thiêt bi IoT dóng vai trò kêt nổi trung gian giữa thiễt bi IoT với các hệ thóng phía sau trung tâm dữ liệu. Ngày nay, với sy phát triên tiên tiên của cong nghệ phân cửng, các thỉêt bị mang cận biên này ngày cang mạnh mẽ, có khả năng tinh toán và xử lý lớn, duợc tận dung dê tổi ưu hóa trải nghiệm người dùng; dáp ứng thời gian thuc với các ứng dung yêu câu dộ trê thâp. Với xu huớng dó, Fât nhieu giải pháp kỹ thuật lien quan dên tinh toán cận biên duợc các nhà nghiên cứu quan tâm và phát triễn. Một só vấn đề nghiên cứu có thẻ kễ dén như giải pháp Iưu trữ dệm tại thiết bị can biên (edge caching) dê dáp ứng ngay lập tức dữ lieu cân thiêt khi ứng dung IoT có yêu câu truy vân. Ngoài ra các giải pháp liên quan dến phân tảỉ tính toán thông minh (intelligent oflloading) giữa thiêt bị cận biên và hệ thông dđiện toán dám mây góp phân tỗi nguyen tính toán, nâng

## Trang 119

trai nghiem nguời dung cũng là chủ đề mở và dang thu hút giới nghiên cứu. Trig lâm dữ liệư là nơi hien thyrc ha tang dien toán dám mây, với khả nẳng tính toán và lưu trữ lớn. Trung tâm dữ liệu thyrc hiện quản lý, diêu khiên, phân phỗi nguón tài nguyên tính toán và tài nguyên luu trữ của một tỗ chức, một co quan Các yêu cau cúa úng dụng. dịch vụ đòi hói khả nẵng tinh toán lớn dược chuyen dến xử lý tại trung tâm dữ liju này , Tuy nhiên, các tác vụ thực thi tại trung tâm dữ liệu thường cách xa thiêt bị IoT dâu cuoi, dẫn dên thời gian phản hổi chậm hon rât nhiêu so với các thiêt bị tính toán cận biên Chính vì thê; các gifi pháp kỹ thuật vê phân tải tính toán thông minh giữa thiêt bị cận biên và trung tâm dữ liệu dang là chủ dê mới và thu hút sự quan tâm,

5.1.2 Các yêu cầu và đặc trưng cơ bản của các hệ thống tính toán cho IoT Như đã trinh bảy ở phản trên; một gỉảỉ pháp IoT triễn khai thực tê sẽ liên quan tới rât nhiêu thành phan ở phía sau, từ thiết bị cận biên tới kêt nôi mang và cuoi cung là hạ tầng dien toán dám mây dê thực thi các tác vụ can thiêt . Trong dó, tính toán can biên có thê xem như việc mang giải phápdiện toán đám mây tuyên thông triển khai ở vị trí gàn với thiét bi đẩu cuói hơn dẻ dáp ứng nhu câu thời gian thực, cảithien trai nghiem nguởi dùng. Đề triến khai một giải pháp hoàn chỉnh trong thực tế, hệ thông IoT dựa trên kiên trúc tính toán cận bien, ha tang diện toán dám mây cân dáp ứng nhiêu yêu câu khác nhau, một sô yêu câu có thế kể đến như oa Kha năng có thê mở rổng (scalability): Đảm bào rang thông có khá nang mở rộng khi luong dữ liệu táng Iên cúng như khi có nhu cau phát triên nhieu thiêt bi mới mà khong anh huong dên độ tré hay thởi gian phản hôi. Khả năng chịu lỗỉ và tính tin cây Cdu (fault   lolerance; reliability): Đảm bảo cho hệ thống hoat động binh thuong duới tác dộng của các tác nhân bên ngoai  như tinh trang tải luong cao

## Trang 120

Khả năng bảo mật dữ lieu (data security): đảm bảo hệ thống chịu duợc các cuôc tan công từ bên ngoài nhắm vào dữ liệu bí mật luu trữ trong hệ thóng hay trên mạng- Các dich vu bảo mật (service sccurity): giúp hệ thống chju được các tân công bên ngoảỉ nhăm vào việc làm ngừng các dich vH duoc cung câp bởi hệ thông thông qua các tan công nhu Dos (Deniel-of-Service) hay tân cong Blackhold Bảo mật vật lý (physical security): Đảm bào hệ thống được thiêt ké và triền khai sao cho có thể không bj ảnh huởng bởi các tai nan thông thường như cháy nổ, rò rỉ nuớc, hóa chất . Tao ra dữ ligu và tính toán cận ke (data production and computation proximỉty): Đây là dặc trung cơ bản của hệ thống IoT dựa trên nên tung tính toán cận biên và diện toán dám mây. Tính nang này dàm bào dữ liệu thu thâp duợc bởi các thiêt bị và thóng dugc xử lý gan kê nhau giúp làm giảm thời gian cham ưê.

5.2. Nên (adg đỉện toán dám mây và írng dụng trong IoT khi ra   dời, công nghệ   đien toán dán   mây (Cloud Computing) đã thu hút duoc sy quan tâm của nhièu tỗ chức và nhà khoa học trên khăp thê gỉới Iheo Viện Tiêu chuân và Công nghệ Hòa Kỳ, diện toán dám mây là một mô hinh dế hien thực môt cách tiin lợi, theo nhu cau việc truy cập mang tới một nguon tài nguyên tính toán có thê cau hinh (ví du: mang; máy chù. bộ nhớ ứng dung và djch vụ); mô hình này có thễ duvc cung câp và phát hành môt cách thuan tiện, ít tôn công SUC trong việc quain lý và tuong tác với nhà cung cấp dịch vu. Theo trường ĐH Berkeley; diện toán dám mây dê cập tới việc các ứng dụng dưoc phân phiôi duới dang djch vụ mà hệ thong phân cứng và phân mêm trong các trung tâm dữ liệu dã cung cấp các djch vụ Còn theo nhà khoa học Buyya người có nhiêu ảnh hưởng trong cúc nghiên cứu ve công nghệ diện toán dám mây Internet van vật dien toán dám mây là một hệ thống xử lý song song và phan tan, bao gũmn một tập har các máy tinh dugc kêt 100

