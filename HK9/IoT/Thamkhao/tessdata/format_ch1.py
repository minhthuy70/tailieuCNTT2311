import re, sys

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    text = f.read()

ch1_text = """## Trang 21

# CHƯƠNG 1. GIỚI THIỆU

### 1.1. Tổng quan về công nghệ Internet vạn vật

Thế giới hiện có khoảng 20 tỷ thiết bị kết nối Internet và đang tăng trung bình 80 thiết bị mới mỗi giây. Tốc độ tăng này sẽ đạt 50 tỷ thiết bị vào năm 2020 [1]. Đây là một trong những thống kê của Cisco về viễn cảnh “Internet của vạn vật” (Internet of Things - IoTs) [2]. Công nghệ mạng Internet of Things (IoTs) hiện đang được phát triển để mọi thiết bị, đồ vật... đều có thể kết nối và tương tác với nhau, giúp chúng ta có thể tra cứu thông tin về thực phẩm ngay trên tủ lạnh, điều khiển ôtô từ xa mà không cần trực tiếp lái xe, hoặc 4-5 triệu xe máy ở Hà Nội, hoặc Tp.HCM được tích hợp cảm biến để nhà quản lý dễ dàng kiểm soát lưu lượng giao thông. Hình 1.1 dưới đây cung cấp các số liệu minh họa.

Hình 1.1. Số liệu minh họa số lượng thiết bị IoTs cho đến năm 2020 (Nguồn: Cisco IBSG)

Một thế giới kết nối, hay “Internet của vạn vật” (Internet of Things - IoTs), sẽ mang lại giá trị kinh tế lớn. Tuy nhiên, hiện mới chỉ có khoảng 1% thiết bị được kết nối trên toàn cầu. Báo cáo của Cisco trình bày “Internet của vạn vật” đã mang lại 613 tỷ USD lợi nhuận trong năm 2013 và những công ty tối ưu hóa

## Trang 22

Một thế giới kết nối, hay “Internet của vạn vật” (Internet of Things - IoTs), sẽ mang lại giá trị kinh tế lớn. Tuy nhiên, hiện mới chỉ có khoảng 1% thiết bị được kết nối trên toàn cầu. Báo cáo của Cisco trình bày “Internet của vạn vật” đã mang lại 613 tỷ USD lợi nhuận trong năm 2013 và những công ty tối ưu hóa được các kết nối giữa con người, quá trình, dữ liệu hoặc mọi vật sẽ sinh lời ở mức lớn nhất trong tương lai. Intel, đơn vị mới tham gia vào thị trường sản xuất chip cho các thiết bị thông minh phục vụ IoT cũng đã thu về hơn 2 tỷ USD trong năm 2014 từ lĩnh vực này, tăng trưởng 19% so với năm 2013 [3]. “Internet của vạn vật có tiềm năng thay đổi đáng kể bộ mặt nền kinh tế của chúng ta và chuyển đổi những ngành công nghiệp chủ chốt”, Rob Lloyd, chuyên gia của Cisco, nhận định. “Câu hỏi đặt ra là ai sẽ là người dẫn đầu và chiến thắng trong nền kinh tế mới này. Thành công không phụ thuộc vào vị trí địa lý hay quy mô của công ty mà phụ thuộc vào yếu tố: ai là người có thể thích ứng nhanh nhất”. Nghiên cứu mới cũng cho thấy các nhà lãnh đạo doanh nghiệp cũng tin tưởng rằng Internet của vạn vật - nơi mọi thứ tương tác với nhau - sẽ giúp thúc đẩy an toàn thông tin tốt hơn.

Ủy ban quản lý nghiên cứu Âu châu về ICT, trong chương trình FP7 về chuyên ngành “Internet of Things and Future Internet Enterprise Systems” [4] đã thông báo sẽ tiếp tục hỗ trợ kinh phí và điều phối nghiên cứu việc phát triển các công nghệ liên quan đến Internet of Things and Future Internet Enterprise System. Ủy ban quản lý nghiên cứu Âu châu khởi đầu với thông báo hỗ trợ kinh phí cho các dự án nghiên cứu về Internet of Things trong Call 5 of FP7-ICT (2009-2010 Work Program) [5], Call 7 (2011-2012 Work Program) [6], và trong giai đoạn từ 2015-2020 là Horizon-2020/ICT-30-2015 [7]. Hướng nghiên cứu trọng điểm tập trung vào Internet của vạn vật và các nền tảng để kết

---
[3] http://www.techz.vn/internet-of-things-la-gi-tai-sao-no-se-la-xu-huong-cua-tuong-lai-qv1-ylt41541.html  
[4] http://cordis.europa.eu/fp7/ict/enet/home2_en.html  
[5] http://cordis.europa.eu/fp7/ict/enet/d4-20101008-infoday_en.html  
[6] http://ec.europa.eu/research/participants/portal/desktop/en/opportunities/h2020/topics/9091-ict-30-2015.html  

## Trang 23

nối các thiết bị thông minh (Internet of Things and Platforms for Connected Smart Objects), bao gồm quản lý các thiết bị hỗn hợp (sensor, RFID, actuator), quản lý người dùng, quản lý mạng, bảo mật hệ thống mạng. Vì vậy, vấn đề phát triển các ứng dụng thông minh IoT phục vụ đời sống sử dụng các công nghệ IoT mới đã và đang là một trong những vấn đề trọng điểm cần nghiên cứu trong các chương trình nghiên cứu ICT hiện nay của Âu châu. Tương tự, tại các nước lớn và phát triển khác trên thế giới, ví dụ như Mỹ, Nhật Bản, hay Trung Quốc, đều đã và đang triển khai các chương trình nghiên cứu quốc gia khác nhau về lĩnh vực Internet of Things [8, 9, 10, 11].

Trong việc phát triển các ứng dụng IoT và các giải pháp IoT phục vụ xây dựng ứng dụng IoT thông minh, do sự đa dạng của các chuẩn IoT hiện nay và thường xuyên có những tiêu chuẩn mới xuất hiện, chúng tôi hướng tới việc phát triển các ứng dụng và giải pháp IoT sẽ tuân thủ nghiêm ngặt các quy định, quy trình trong các tổ chức quốc tế có uy tín, để tăng sự tương thích và portability. Một số bộ tiêu chuẩn, quy tắc có thể liệt kê dưới đây:

**Open InterConnect Consortium (OIC)** [12]: Hiệp hội kết nối mở OIC là một tổ chức phi lợi nhuận ở bang Oregon (Mỹ), được thành lập bởi các công ty công nghệ hàng đầu như Intel, Samsung, Dell, Atmel, Broadcom và Wind River, với mục tiêu xác định các yêu cầu kết nối và đảm bảo khả năng tương tác của hàng tỷ thiết bị tạo nên “Internet của vạn vật” (Internet of Things - IoT). Bên cạnh đó, OIC dự định cung cấp các chỉ dẫn kỹ thuật, bổ sung mã nguồn mở và chương trình chứng nhận (certification program) cho

---
[8] http://www.nsf.gov/funding/pgm_summ.jsp?pims_id=504949  
[9] IT Strategic Headquarters, “i-Japan Strategy 2015”, http://www.kantei.go.jp/foreign/policy/it/i-JapanStrategy.pdf  
[10] The Ministry of Industry and Information Technology, “The 12th Five-Year Plan for the Internet of Things”, 2012.  
[11] http://www.chinadaily.com.cn/bizchina/2010-04/09/content_9706692.htm  
[12] http://openinterconnect.org/  

## Trang 24

các thiết bị kết nối không dây. Hình 1.2 dưới đây trình bày lược đồ quy chuẩn kỹ thuật của OIC.

**AllSeen Alliance** [13]: gồm các công ty công nghệ như Haier, LG Electronics, Panasonic, Qualcomm, Sharp, Technicolor, Silicon Image và TP-LINK. Liên minh này đã có đến 51 thành viên bao gồm Microsoft cùng phối hợp với dự án nguồn mở AllJoyn của Qualcomm để triển khai khung hạ tầng nền IoT đầu tiên.

Ngoài ra, còn rất nhiều các chuẩn kỹ thuật, công nghệ và dự án nghiên cứu liên quan đến Internet of Things đã và đang được phát triển bởi các tổ chức quốc tế có uy tín khác, ví dụ:
- IEEE 802.15.4 [14] cho mạng cảm biến không dây (Wireless Sensor Networks - WSNs).
- IETF CoAP (Constrained Application Protocol) [15].
- Zigbee Alliance [16], Bluetooth Smart [17].
- W3C Semantic Sensor Networks [18].
- Open Geospatial Consortium (OGC) Sensor Web Enablement (SWE) [19] và CityGML [20].

---
[13] https://allseenalliance.org  
[14] IEEE 802.15 WPAN Task Group 4 (TG4), http://www.ieee802.org/15/pub/TG4.html  
[15] IETF CoRE Working Group, http://datatracker.ietf.org/wg/core/charter/  
[16] http://www.zigbee.org/  
[17] http://www.bluetooth.com/Pages/Bluetooth-Smart.aspx  
[18] W3C Semantic Sensor Network Incubator Group, http://www.w3.org/2005/Incubator/ssn/  
[19] http://www.opengeospatial.org/domain/swe  
[20] http://www.opengeospatial.org/standards/citygml  

## Trang 25

- European Sensor Network Architecture (ESNA) [21]
- IETF 6LoWPAN [22], uIP / uIPv6

Hình 1.2. Lược đồ quy chuẩn kỹ thuật của OIC (Nguồn: OIC)

Tốc độ tăng trưởng nhanh chóng của Internet of Things hiện nay cũng đem đến nhiều thách thức lớn. Số lượng các thiết bị được tạo ra nhiều bao nhiêu thì sự mong đợi của khách hàng cho các kết nối, hiệu suất năng lượng, tính tin cậy, dễ sử dụng và kết cấu sẽ càng tăng cao. Các thiết bị điện tử không chỉ phải được cải tiến để đem lại hiệu năng cao mà còn phải có tính hấp dẫn. Và tất nhiên, tất cả các tính năng vượt trội và hình thức bắt mắt đó phải đi cùng với giá cả hợp lý. Dưới đây là một số đặc điểm kỹ thuật cần xem xét:

**Phần mềm:** Trong quy trình phức tạp của việc thiết kế và đóng gói một hệ thống IoT, phần mềm thực sự đóng vai trò quan trọng qua việc hỗ trợ đầy đủ cho toàn bộ vòng đời phát

---
[21] European Sensor Network Architecture (ESNA): http://www.it.lut.fi/project/esna/  
[22] IETF 6LoWPAN Working Group: http://datatracker.ietf.org/wg/6lowpan/charter/  

## Trang 26

triển của sản phẩm. Cụ thể, phần mềm có thể hỗ trợ một cách hoàn thiện cho chu trình thiết kế các thiết bị công nghệ cao, bao gồm mạch tích hợp (ICs) và phần mềm nhúng. Những giải pháp phần mềm góp phần giải quyết các thách thức lớn cho các nhà thiết kế công nghệ cao: cải thiện tốc độ và băng thông, tối ưu công suất và hiệu năng, tối ưu đặc tính ăng-ten, và kết hợp các vật liệu tiên tiến. Ngoài ra, để hoàn toàn làm chủ công nghệ và gia tăng tính bảo mật của hệ thống, chúng tôi hướng tới lựa chọn các thiết bị IoT được phát triển và hỗ trợ bởi các nền tảng phần mềm mã nguồn mở thông dụng, và được chứng nhận hoặc kiểm định bởi các tổ chức IoT quốc tế có uy tín.

**Tăng tốc độ và mở rộng băng thông:** Do số lượng các thiết bị di động, thiết bị IoT ngày một tăng nhanh nên ngày càng nhiều dữ liệu được truyền và nhận, việc truyền tải chúng cần nhanh hơn trên cả mạng truyền thông có dây và không dây. Luồng video, tương tác chơi game và dịch vụ web tốc độ cao đang đẩy đến giới hạn không chỉ trên các thiết bị di động, thiết bị IoT, mà còn trên các máy chủ, bộ định tuyến và cổng chia.

**Tối ưu năng lượng và hiệu suất:** Một vấn đề không kém phần quan trọng trong công nghiệp công nghệ cao là quản lý năng lượng một cách hiệu quả. Để giúp giải quyết vấn đề này, các thiết bị IoT được lựa chọn phục vụ nghiên cứu bảo mật IoT có hỗ trợ thiết kế cho các thiết bị điện tử thông minh, hiệu suất năng lượng cao, khả năng tiêu thụ nguồn thấp. Trước đây, các kỹ thuật phân tích các vấn đề tiêu thụ và phân phối năng lượng thông qua một cách tiếp cận kín, xem xét riêng ở chip, bản mạch và package (nhóm linh kiện). Nhưng hiện nay, các giải pháp tiết kiệm năng lượng mới thực sự hỗ trợ phương pháp thiết kế tích hợp chip-package-system (CPS), cho phép tối ưu thành phần cũng như phân tích và tối ưu đồng thời xuyên suốt toàn bộ hệ thống. Cách tiếp cận này cân bằng điện thế hoạt động thấp cần thiết để tiết kiệm năng lượng với tính nhất quán và tin cậy đáp ứng được yêu cầu để loại bỏ lỗi.

**Cloud/edge-based Internet of Things:** Hỗ trợ khả năng phát triển và tích hợp các ứng dụng và giải pháp IoT vào nền tảng

## Trang 27

điện toán đám mây (cloud computing) và tính toán cận biên (edge computing). Hình 1.3 minh họa ý tưởng triển khai các ứng dụng và giải pháp IoT trên cloud, bao gồm hạ tầng kiến trúc mạng của một ứng dụng IoT thực tế dự định được triển khai.

Hình 1.3. Kiến trúc mạng tổng quan của một ứng dụng cloud-based IoT (Nguồn: IBM)

### 1.2. Xu thế ứng dụng IoT và các công nghệ liên quan cho đô thị thông minh ở Việt Nam

Công nghệ IoT/5G và kỹ thuật xử lý dữ liệu lớn (Big Data), trí tuệ nhân tạo (AI) [32] đóng vai trò quan trọng trong việc tạo ra những đổi mới đột phá trong CNTT và truyền thông, và các lĩnh vực ứng dụng liên quan. Thành phố thông minh là một trong những ứng dụng như vậy, đã thu hút được sự chú ý lớn từ các chính phủ, cộng đồng ngành học thuật và CNTT tại nhiều quốc gia. Đặc biệt, Big Data/AI và IoT/5G cung cấp các công cụ và công nghệ cho phép quan trọng để thúc đẩy sự chuyển đổi của các thành phố lớn trên toàn thế giới thành những nơi đáng sống, làm việc và tận hưởng. Các công nghệ IoT/5G

---
[32] GSMA.com/IC, “Intelligent Connectivity: How the combination of 5G, AI, and IoT is set to change the Americas”.  

## Trang 28

mới, một khi được tích hợp đúng vào cơ sở hạ tầng thành phố thông minh (Smart Cities), có thể hỗ trợ số lượng lớn kết nối không dây từ các loại thiết bị không dây khác nhau (ví dụ: cảm biến, máy ảnh, thiết bị VR/AR, xe thông minh) thông qua môi trường mạng tốc độ cao, truyền dữ liệu cực kỳ đáng tin cậy và độ trễ thấp. Ngoài ra, các công nghệ IoTs/5G cho phép truyền thông, lưu trữ và xử lý dữ liệu hiệu quả, rất cần thiết để xử lý và phân tích lượng dữ liệu khổng lồ của thành phố thông minh và chuyển dữ liệu thu thập được thành các quy trình giám sát, ra quyết định và ứng dụng kịp thời cũng như cung cấp các dịch vụ kỹ thuật số đa phương tiện phong phú đến thiết bị di động cho người dân thành thị.

Hình 1.4 dưới đây minh họa ứng dụng IoTs/5G trong đô thị thông minh.

Hình 1.4. Các ứng dụng điển hình IoTs/5G trong đô thị thông minh

Trong các đô thị thông minh, mạng cảm biến không dây thường

## Trang 29

thường được triển khai ở các khu vực khó tiếp cận về mặt địa lý, hoặc ở xa. Mặc dù dữ liệu cảm biến thường được phân tích thống kê trong các ứng dụng giám sát, các truy vấn trực tiếp để yêu cầu dữ liệu cảm biến ngay lập tức và để điều chỉnh hành vi của các thiết bị cảm biến trong thời gian thực, thường được yêu cầu trong môi trường thay đổi động, tồn tại các yếu tố, sự kiện tác động không lường trước. Các công cụ quản trị mạng cảm biến, mạng IoTs/5G, cùng với các tiêu chuẩn để xử lý và quản lý dữ liệu cảm biến, dữ liệu IoTs/5G có thể hỗ trợ xây dựng các ứng dụng và giải pháp trên hạ tầng IoTs/5G mạnh hơn. Ngoài ra, các công nghệ mới để phát triển và tích hợp các thiết bị nhỏ sẽ cho phép đa dạng hóa các loại cảm biến, thiết bị IoTs/5G được triển khai. Số lượng thiết bị, ứng dụng và dự án IoTs/5G ngày càng tăng, khối lượng dữ liệu lớn được thu thập bởi các cảm biến, thiết bị IoTs/5G ngày càng lớn, đòi hỏi các nỗ lực nghiên cứu thích hợp để xử lý và phân tích dữ liệu, sử dụng hiệu quả tài nguyên, khả năng mở rộng, khả dụng và độ tin cậy của hệ thống. Tương tự, giám sát môi trường cần phải liên tục, tích hợp và không mất dữ liệu, đòi hỏi phải có đặc điểm kỹ thuật và triển khai cơ sở hạ tầng đáng tin cậy cho IoTs/5G.

Trong các ứng dụng IoTs không đồng nhất quy mô lớn, các cảm biến nhỏ và giá rẻ, và các thiết bị IoTs/5G có thể được triển khai độc lập hoặc kết hợp với các thiết bị tùy chỉnh nhiều tài nguyên hơn và đắt tiền hơn. Do đó, để giải quyết vấn đề này, hướng tiếp cận là tích hợp các thiết bị IoTs/5G không đồng nhất bằng cách phát triển một nền tảng phần mềm (middlewares) mở và đa quy mô trên cơ sở hạ tầng điện toán đám mây để triển khai các dịch vụ quản lý tích hợp nhiều loại thiết bị IoTs/5G. Một nền tảng dịch vụ như vậy sẽ bao gồm các danh mục dịch vụ khác nhau có thể được triển khai trong hệ thống mạng thử nghiệm IoTs/5G hoặc các ứng dụng thực tế để đạt được các mục tiêu như phát hiện sự kiện, vị trí đối tượng, theo dõi hoặc giám sát.

---
[31] https://techbeacon.com/app-dev-testing/67-open-source-tools-resources-iot  
[32] https://www.datamation.com/mobile-wireless/51-open-source-tools-for-the-internet-of-things-1.html  

## Trang 30

sát. Các dịch vụ và hạ tầng mạng thử nghiệm này nên xem xét các đặc điểm cụ thể của công nghệ IoTs/5G và tài nguyên vật lý bị hạn chế của các cảm biến, thiết bị IoTs/5G, bao gồm tuổi thọ pin, sức mạnh tính toán, bộ nhớ, băng thông mạng và chất lượng đường truyền.

Tại Việt Nam, mặc dù còn nhiều bất cập, song hiện nay, các đô thị Việt Nam đang phát triển theo hướng tiếp cận với nhiều mô hình tiên tiến theo xu thế hội nhập quốc tế, tạo ra nhiều tiền đề về ứng dụng và phát triển CNTT, truyền thông để phát triển đô thị thông minh và quản lý thông minh. Cụ thể, tỷ lệ người sử dụng internet/tổng dân số năm 2014 đạt 43,8%, cao hơn tỷ lệ của thế giới là 42,2% và châu Á là 34,8%. Việt Nam có gần 14.000 doanh nghiệp CNTT với 500.000 lao động và doanh thu lớn. Việt Nam cũng đã đạt được nhiều thành tựu trong việc ứng dụng CNTT vào hoạt động quản lý nhà nước và các lĩnh vực đời sống xã hội, rõ nhất là ở các lĩnh vực quản lý ngân sách và kho bạc, quản lý thuế, hải quan, bảo hiểm xã hội, giáo dục, y tế, quản lý giao thông, quản lý đất đai, quy hoạch, xây dựng, môi trường...

“Từ bức tranh của các đô thị Việt Nam, có thể thấy Việt Nam cần phát triển các đô thị theo hướng đô thị thông minh”, đồng chí Nguyễn Thiện Nhân - Nguyên Bí thư Thành ủy Thành phố Hồ Chí Minh nêu. Đô thị thông minh nhằm đạt tới 4 mục tiêu: hiệu quả kinh tế ở các đô thị ngày càng cao (đến năm 2025: diện tích đô thị khoảng 15% diện tích cả nước, tỷ lệ đô thị hóa khoảng 50% dân số, tạo ra khoảng 75% GDP); môi trường sống ngày càng tốt hơn; người dân được phục vụ tốt hơn; người dân tham gia quản lý đô thị và giám sát chính quyền.

Để có thể xây dựng và vận hành có hiệu quả một thành phố thông minh theo đúng nghĩa của nó thì ngay từ đầu chính quyền thành phố và các đối tác công nghệ cần phát triển và lựa chọn các giải pháp đạt chuẩn Internet of Things - IoTs. Bởi lẽ, trong trường hợp ngược lại, tức là chính quyền thành phố áp dụng triển khai giải pháp IoTs phân mảnh và phi tiêu chuẩn (Non-Standardized) thì việc vận hành cũng như mức độ kết nối giữa các thành phần trong hệ thống thành phố thông minh sẽ không

## Trang 31

mang lại kết quả như mong muốn ban đầu. Trong trường hợp này, việc phải đối mặt với các rủi ro tài chính và lãng phí nhân lực là điều khó tránh khỏi. Ngoài ra, thành phố thông minh là thành phố dùng công nghệ điện toán đám mây (Cloud computing) và CNTT thế hệ mới để quy hoạch đô thị, sử dụng các công cụ của CNTT và truyền thông để thu nhận, phân tích và tích hợp thông tin để vận hành thành phố, hỗ trợ cuộc sống của người dân, bảo vệ môi trường, giữ an toàn cộng đồng, phát triển các dịch vụ đô thị và đáp ứng các nhu cầu khác một cách thông minh, giúp cho nền kinh tế đô thị tăng trưởng, duy trì tiến bộ xã hội và phát triển bền vững.

Theo đánh giá của chúng tôi, xây dựng đô thị thông minh gắn liền với việc sử dụng công nghệ Internet of Things - IoTs và điện toán đám mây (cloud computing) hiện đại. Trong khi công nghệ IoTs với rất nhiều chuẩn giao tiếp hỗ trợ đa dạng, đa số các thiết bị đầu cuối hiện nay phục vụ thu thập dữ liệu, giám sát, công nghệ điện toán đám mây (cloud computing) và tính toán cận biên (edge computing) là các nền tảng hoàn hảo phục vụ tính toán, tích hợp dịch vụ và mạng Internet, và công nghệ trí tuệ nhân tạo (Artificial Intelligence - AI) cùng kỹ thuật xử lý dữ liệu lớn (Big Data) mang lại tính thông minh và tiện nghi hơn cho ứng dụng. Ngoài ra, nhằm làm chủ công nghệ, các nền tảng mã nguồn mở nên được ưu tiên lựa chọn triển khai.

## BÀI TẬP CHƯƠNG 1

1. Hãy liệt kê những thiết bị có thể kết nối vào Internet.
2. Hãy liệt kê những đặc điểm kỹ thuật của thiết bị được sử dụng trong IoT.
3. Hãy liệt kê những xu thế của IoT trên thế giới và ở Việt Nam.
4. Hãy liệt kê những ưu điểm mà IoT có thể mang lại cho cuộc sống.
5. Hãy liệt kê những thách thức mà IoT đang gặp phải.

"""

idx21 = text.find('## Trang 21\n')
idx32 = text.find('## Trang 32\n')
assert idx21 != -1 and idx32 != -1

new_text = text[:idx21] + ch1_text + text[idx32:]
with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Updated Chapter 1 successfully!')
