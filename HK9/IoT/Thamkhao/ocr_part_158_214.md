## Trang 158

sử dung trong các ứng dunp thích ửng ngữ cảnh. Cụ thể, kỹ thuật phân cụm duoc sừ dung muc thâp (mức phàn cung) trong mạng cảm bien như dịnh tuyến hay muc (mức ửng dung) nhu xác dinh vị trí hrong nhà hay ngoài trời. Kỹ thuật mang nơ- không giám Sát nhu Kohonen   Self-Organizing Map (KSOM) duoc sử dung dê phân loau dữ licu cảm biên thco thời gian thuc.

6.4.3. Dựa trên luật Dựa trên luật (Rule-based): Đây là phương pháp dơn giản và dễ hiểu nhất trong việc suy luận. Luật thuởng có cấu trúc IF- THEN-ELSE. Phuong pháp này cho phép tạo ra ngữ canh cấp bang  ngữ cảnh câp thẩp: Mirc là một công cu nhận biêt ngữ cảnh cho thiết bj di dộng. Hẩu hết các tùy chon nguvi dung (user preferences) dưyc mã hóa (encode) thông qua luật. Kỹ thuật này con dưac sử dung trong phát hien sự kiện. Suy luân dura trên luật duvc dự doán sẽ dóng vai trò quan trong trong IoT bởi vì dây là cách dễ dang và don gian nhât đê mô hinh hóa suy nghĩ của con ngưòi và suy luan bằng máy móc. PRIAMOS là một ví du về sử dung các lugl  ngữ nghĩa đê chuyên dữ liệu cảm biến thành thông tin ngữ cảnh_

6.4.4. Dựa trên logic mờ Dua trên logic mờ (Fuzzy logic): Kỹ thuat này cho phép suy luân xâp xi thay vỉ suy Iuan chinh Xác và rõ rang Trong thuyết truyên thống. giá tri chi có thể biều dạt bang hoác (True False). Tuy nhiên; lý thuyết mờ dưa ra cách diễn tà nhiên hơn như các kich bản trong thực tế để mở rông khả năng suy diên không chác chan. Ví du như các khái niệm Chu ngan, tôi , dáng tin . có dược biêu đat trong logic mờ. Nhuvc diêm của phuong pháp này là tất cả những giá trj này đều phải dưvc Xac   dịnh từ trước Trong hâu hêt các trường hợP; logic mờ không thễ sử dụng dộc lập mà phải kết hợp với một kỹ thuat khác như dựa trên luật, lý thuyết xác suất hay dya trên ontology . Sau dây là một case study vễ dỉều khien nhiệt độ trong ig dung Nông nghiệp thông minh sử dung kỹ thuât Logic mnở: 138

## Trang 159

Việc đỉều khiển nhiệt độ dựa trén nhiệt độ mà các nút thu thap dugc trong các nông trai và nhiệt độ không khí duợc đặt truớc cho các loai cây trông để dưa ra cac đề nghj điều chinh nhiet độ thich họp cho sy phat , triên tôt nhât của cây trông. Hinh bicu dicn sơ dô fuzry logic đicu khiên nhiệt độ Irong ing dụng Nông nghiệp thông minh. Sơ đô

Ienpurelure

Terperature Fuzzy logic Controller

Acuon

Truc e

Hình 64 Sơ đồ fuzzy logic điều khỉển nhỉệt dộ Mô tả thuật todn Giải thuật bao gổm các gỉá trị input như sau; Input Temperature. là nhiệt độ mà cam biên thiêt bị thu nhận dưoc. Giá ưrị này se có thuêc khoáng giá trị là Cold; Cool,  Normal,  Warm; Hot  (tương ửng với lanh hơi lanh, binh thường- âm, và nóng) và một yêu tô nhó dê Xác dịnh dộ rông cúa các khodng giá trị này là delta (riêng biệt với tung loau  cây trong) Trade: hướng đi cúa nhiệt dộ hiện tại. Trade có 3 giá trị lan lugt   là Down; None, Up (tuong ửmg với  giảm, không dối, và tẵng). Phần tính toán này do Thuật toán Lincar Regression xử lý. Output; giá tri   điéu   khiên tuong imng HeatHi,  HeatLo, Nothing,   VcnLo, VenHi   (tưong ứng với làm   nóng nhieu, lam nong ít, không làm gi, làm mát ít, làm mát nhieu) Trong casc sludy này dugc áp dung trên cây xà lách, khoảng nhiệt độ ổn dịnh là từ 15-18 €.

139

## Trang 160

Bảng 65. Bảng biêu diên _ (hane input nhiệt dộ Khoảng gỉá trị Trang thái tưong ứng Cold (lanh) 11 > 15 Cool (hơi lanh) 14 > 19 Normal (binh thuong) 18 > 22 Wann (Omn) 21 9 100 Hot (nóng)

Bang 6.6 Bảng bỉêu dỉễn  Ohong giá trp input trade (hướng di của dữ liêu) Giả trị Trang thái tưong ửng oun None Up

Rank  6 7. Bảng bỉểu dỉễn output cho diều khiễn nhiệt dộ Khoảng giá tri Kêt qu4 tưong ung 7 20 HcatHi 15 > 40 HeutLo 35 > 60 Nothing VenLo VenHi

Luât suy diễn IF tempcraturc (Cold, Cool Nonnal, Warmn; Hot) AND trade Ououn None Up) THEN Action (HcatHi, HcatLo, Nothing VenLo, Venlli)

Bảng suy ludn Rulc rcmncraturc

Kchauun

Then

Action Heating (High) Hcating (High) Hcating

Cold

AND

THEN

Cool

AND

Lwn

THEN

Cool

AND

anc

THEN

140

Irdc

## Trang 161

(Low) THEN Nothỉng THEN Nothing Lown THEN Nothing or THEN Ventilation (Low) Ventilation THEN (High) THEN Ventilation (High)

Cool Normal Warm

AND AND AND

Wann

AND

Warn

AND

Hlot

AND

Bang 6.& Bảng dữ lỉệu nhỉệt độ dâu vào Trường họP Trurng hơp Truòng hop 3

i

16,1 16,3 16,3 16,5 16,5 16.7 16,6 16,8 16,7

14,8 14,6 14,8 14,5 14,6 143 14,3 14,2 14,2

19,1 19,3 19,2 19,5 19,5 19,3 19,2 19,1

Trung binh Input Hurớng dữ liỆu

16,45

19,23

14,53

16,75

19.15

14,2

Không đổi

Giam

Trường hợp Ta có dữ liệu dẩu vào là 16,75 chicu huớng nhiệt dộ là dang tang thi kêt quả dâu ra thuộc phần Do Nothing (không làm gì, với giá trj cu thẻ là 50). 0 mô phỏng kjch bản trong trưởng hợp này:

141

Tung

## Trang 162

Kuic Yipypr

Hinh 6.5 M phỏng diều khiễn nhiệt độ Trường hợp

Trường hợp

Ta có dữ liệu dầu vào là 16,75- chieu hướng nhiỆt dộ là không dôi thi kêt qua dâu ra thuộc phân Ventilation Low (với giá trị cu thê là 70). Kịch ban này được thê hiện trong bên đưới:

Hinh 66 Mô phỏng điẻu khiển nhiệt độ Trwờng hợp _

142

## Trang 163

Trường hop 3: Ta có dữ liệu dầu vào là   14.2, chieu hướng nhiệt dộ là dang giảm thỉ kêt quả dâu ra thuộc phần Heating High (voi giá trj cu thé là 20,1). Thông tin chi tiết của tnrờng hợp 3 được mô tả trong Hinh 6.7 bên dưới: auicvener

Hinh 67. Mô phong diẻu khiển nhiệt độ Trưrờng hop 3

6.4.5. Dựa trên ontology Dira trên ontology (ontology-based): Kỹ thuật này dya trên logic mô tà Suy luận dựa trên ontology chủ yêu duoc hỗ trợ bởi hai ngôn ngữ cúa web ngữ nghia là RDF và OWL (2) Kỹ thuật này thuờng đưvc sử dung rộng rẵi trong nhận dang hoat dộng  suy luận lai hay phát hiện sự kiện. Lợi thé cúa suy luận dựa trên ontology là nó tích hap tot với các mô hinh ontology Nhung ngược lai, kỹ thuật nảy không có khả nang suy luận các dữ liệu còn thieu hoặc không chẳc chẳn   Diêu này dưoc giải quyêt bàng cách thêm vào các luât cho phép các giá trị bị thiêu có thê thay thê bang các giá trị phù hợp dã duợc xác dinh trước SWRL là một trong những ludl dưvc sử dụng phô biên trong ontology hỉện nay.

143

## Trang 164

6.4.6. Dựa trên Logic xác suất Dira tren Logic xác suất   (Probabilistic   logic-based): Kỹ thuật này cho phép quyêt dịnh dua trên xác suất. Mỗi cóẳng dinh logic sẽ duoc gán cho một xác suât. Kỹ thuật này dưgc sử dụng dé kêt hợp dữ liệu cảm bién từ những nguôn khác nhau hay Xác djnh xung dột giữa các ngữ cánh. Hâu hêt các kỹ thuat loui này thuùng dưgc sử dung de giai thích việc xuft hien cúa các sV kiện.  Dempster-Shafer dựra trên logic xác suất, cho phép kêt hợp các bàng chứng khác nhau dề tính xác suât cua mnột sự kien Mô hinh Markov ân (Hidden Markov Model) được sử dụng đê thê hiện các trang thái thông qua các bang  chứng khác nhau mà không cân doc trang thái trực tiêp. Mô hinh Markov ẩn thuởng duvc dung dẻ nhận dạng hoat dong trong các ứng dụng thích ig ngữ cảnh. Những sánh, dánh giá vê uu nhược diêm cúa các hướng tỉếp cận này được mô tả trong bảng sau: Bang 6.9 So sánh các hwớng tỉep cận trong suy luan ngữ cảnh Kỹ thuật Ưu diém Nhưyc điém Ứng dung Hoc có Chính xác luong dữ liu Nhận dỉện giám sát Hien có nhỉều nhieu hoat dong (Mang nơ- mnô hỉnh Chi xửlỷ duvc Xúc djnh gỉả ronnhd Nên ! Ung loan tri s6 Uri cun thicu Marrg hoc vả tonng Khó chon bộ dặc Bavesian tinh Duru vào Tón nhieu tài Irirung hợp Cúy quyêt nguyên (lưu tnè, xử (ent lý và thoi gian) Support Ngữ nghia c p veclor thap hon có ít ý machinei nghỉa hon Phảỉ có dữ ligu huan luyen Mâ hinh phửc tạp Khó mô tri thửc hien có

144

## Trang 165

Hoc không Khủng cin đữ giamn sat ligu hunn luyen (Phân cum Khong cin dự K láng doin kêt quà gieng gan nhát)

Mô hinh phức tạp Phát hien Ngữ nghia cap hanh thâp hon có ítý thuòng nghia hon Xac dinh vi Khó dánh giá ưri thích hgp Không thẻ dựr đoán trong môt gỉả tri diu ra loai ciy ting uên cánh Ton nhicu tài dong Dong nguyên (luu ưrỮ, xử nghỉcp. lỷ và thoi Rian) Định nghia bing Xac định sự kiin Cóthé bi lỗi trong qi trinh dinh nghia Không thẻ đánh gia honc kiêm tra chat luong Định nghia bẳng Chuyên dỏi ngữ cẳnh Có thé bi lỗi ~ Vong murc thàp quá trinh dinh thanh ngữ nghia canh cáp cao Không thẻ đánh VD: Hệ thong giá hoac kiem Ga tưới nuớc chât luong dong trong {Xộ chính xác có nong nghiệp thong Mrn thé bi giam xuong domo ly nhiên Dữ ligu phủi duuc Luu trữ và xử dinh nghia theo ngữ canh dinh dane (UUnE de cho ra tri thich (OWLRDF) thức khi có Suy Juan só hoc bi yêu cau han ché Hiệu suất thấp (xử lý và thòi gian)

Dua trên lual

Đinh nghia don giun Dé mở rpng Íttốn tàỉ nguyên (xửlỷ, luu trữ)

Logic mờ

Cho phép biêu dien linh hoat (lyr nhicn) Đinh nghia don gian Dễ mở rong Ít ton tài nguyen Cóthê xửlý việc không chắc chán

Dya trên ontology

Cho phép biêu dien và suy luan ngữ Conn phuc

Kêt qua cóỷ nghia mức cao Có the kiem tra và dunh gỉả chât luonp Có thé xử lý dữ

145

## Trang 166

lỉệu dang s8 và dang van ban Cho phép két Phảỉ bỉct xác suat hợp cúc bhng Chi suy dien đưoc chung giá tri s8 hoc Có te xử lý tinh huong không nhỉn thấy (không Jhê dy doán) Hien có nhiéu mô hinh Có thé xử lý viic không chác chan Cung cấp kÉt qua có nghia muc trung binh

Dya trên logic xac

Xác dinh xác suat một sự kỉện diên ra từ nhiêu bẳng chửng khác nhau

(poemipster Shafer, hidden uarko1 Models; Ure Baves)

VD: xac dinh mot con vêt bay vào cánh dong nông nghiip từ dữ licu cúa máy ành, càm bién hong ngoai, cem bỉen âm thanh và cám bien chuyen dông

6.5.Trí tuệ nhân tạo và IoT Trong những năm gàn đây, thuât ngữ trí tuệ nhân tao duvc dac bift chú trong giới hoc thuật lan công nghỉệp Sự kỷ vong vào lợi ích mà trí tuệ nhân tao mang dên dã giúp cho nó dược nghiên cứu; phát triên trong hơn 50 nẵm qua. Những thành qua mà trí tuệ nhân tao dat dugc có thễ dên như: Xc tự hành cúa Tesla. Hệ thong gvi ý sản phẩm của sàn thuong mại diện tử Amazon. Trg lý ảo Siri của Apple: dược tích hợp sãn trên thiết bị dong của Apple; giúp chủ nhân thiết bị có thể tuơng tác với thiết bị thông qua giong nói mà không cân chạm vào thiết bị. Máy chơi cờ vây AlphaGo và dặc biỆt là AlphaGo Zcro cùa Google DccpMind.

146

## Trang 167

Tháng 3/2016 AlphaGo của Google DeepMind  dã chien tháng kỳ thủ cờ vây số một thế giới là Lee Sedol với tong ti sô 4 - 1. Vào nam 2017, Google DcepMind dà cong bố AlphaGo Zero đã dược huản luyện và chiên thăng tuyệt đổi phiên bản AlphaGo trước dó Thuật ngữ trí tuệ nhân tao được khởi xuớng bởi nhà khoa học John McCarthy , Marvin L Minsky, Nathaniel Rochester, và Claude E. Shannon vào mùa hè năng 1956, tai Hội nghị khoa hoc tại truòng Dartmouth, Mỹ- Bôn nhà khoa học này dêu trở thành những nhà khoa hoc hang dau vê lĩnh vực trí tuệ nhân tao sau dó Iri lue nhân lao hay con g0I là   thông   minh nhân lao (Artificial Intelligence AI) là một ngành trong khoa học máy tính nham làm cho máy tính có khả năng suy luan, tinh toán, và hoc cách thích nghi nhu con nguời.

MageiNe Fasang

PEERNING

Hinh 68. Quan hệ gitru Trítuệ nhuirr tao, Hoc máy và Học sâu (Nxuon Nvidia)

Xu thê học máy và hoc sâu dugc chú ý và phát trien trong khoảng 10 nẳm trở laỉ đây bởi nhiêu nguyên nhân; Thứ nhát; phn cứng phát triên. Thử hai: dữr liệu bùng nô. 147

## Trang 168

Đây là hai nút thẳt cổ chai lớn nhất của Học máy và Học sâu giai doan trước dây . Những nẫm gản dây, các hệ thong tính toán hỗ trợ Học máy và Học sâu phát trien mạnh mẽ và giá thành ngày cang thấp. Những phân cimg hỗ trợ Hoc máy và Học sâu có thê kễ dén như CPU, GPU, TPU. Bên cạnh dó, luong licu khổng lồ duvc tao ra hàng ngày cung là môt dong lực cho Học máy và Học sâu phát triên. Bởi vì một trong những muc tiêu cuối cùng của Khoa học máy tính là có thể tim ra những tri thức ân có trong dữ liệu có sẵn, hoặc từ dữ liệu có sẵn máy móc có thể xử lý và dua  các du doán trong tuơng lai. Hinh 6.8 mô tả quan hệ giữa Trí tuệ nhân tao, Hoc máy và Hoc sâu. Học máy là một tập con trong Trí tuệ nhân tao và Học sâu là một tập con trong học máy.

6.5.1. Hoc máy Hoc máy là thuật ngữ mô tả quá trình xử lý dữ liệu như phân tích, dự doán và dua ra quyêt  djnh trong mỗi tổ chức. Đây là một nhành cúa Trí tuệ nhân tao giúp máy tinh có thê "hoc" mà không cân hoặc cân rât Sự can thiệp cúa con nguời. Máy móc có thê lự dộng diêu chinh mà không cản lập trình trước và đua ra các quyêt dịnh tùy thuộc vào mỗi ngữ cảnh cu thé. Hệ thống khuyến nghị trên các sàn thưong mại diện tử là một ví dụ dien hinh cua ứng dung hoc máy .

6.5.1.1. Quá trình xử lý trong hoc mày Hinh 6.9 mô tả quá trình xử lý trong học máy. Quá trình này bẳt dau từ việc xác dịnh được tập dữ lisu ban dầu, thông qua các yếu tố biến dêng không chắc chắn; phức tap và mơ hổ của dữ lieu mà loai thujt toán học máy dưvc sừ dung Kêt quả cuoi cùng của thuật toán là dưả ra kết quà tương ứng với tập dữ liệu ban dâu và thuật toán dưgc sử dung Thu thập dữ liệu: Đây là bước dầu tiên và quan trong nhất trong quá trinh thực thi hoc máy. Tại bước này, dữ lieu dược thu thập liên quan đến viec phát biểu bài toán. Dữ liệu được thu thập 148

## Trang 169

phai phù hợp theo yêu cẩu của vẩn đề dẻ dộ chính xác của mô hỉnh là cao nhât. Nêu dữ liệu dược thu thập không lien CUanl hoặc rât ít liên quan đén vấn dề cần xử lý thì qu4 trinh xử lý sau dó dược xem là vô nghĩa. Bộ dữ liệu dược thu thập trong quá trình này được goi là đữ liệu huấn luyện (training set). Ví du: nêu bài toán là xác dinh khuôn mặt một ngưòỉ thi dữ liệu ảnh thu thập phải băt buôc có mặt ngưởỉ  dó, Tiên xử lý dữ liệu: Trong bước này, kỹ thuật trích xuất các thuộc tính duợc sử dung dê dữ liệu thu thập dưgc không dây dủ không nhất quán hoặc có sai sót hay nhiễu thành dữ liệu khả thi đê thích hợp với mô hỉnh hoc máy. Sau khi loai bỏ các lói như khong nhât quán, dư thừa và thiêu dữ liệu thì các thuộc tính dugc trích xuât và, sau dó, các thuộc tính này duợc sử dung cho việc huân luyện mô hinh Xẩy dựng mô hình: Đây là bước lyra chon kỹ thuật hoc máy phù hợp de dánh giá kêt quả cùa bàí toán dugc dua ra lúc ban dau, Một số kỹ thuật học máy khác nhau nhu: Hoc , co giám sát (Supervised   learning)   Hoc   không glamn (Unsupervised learing)   và Hoc tang CuOng (Reinforced   learning) duợc sử dung. Một sổ thuật toán thường dược sử dung của các kỹ thuật này như Hổi quy logic (Logistic rcgression), Máy hỗ trợ véc tơ (Support Vector Machine SVM), Naive Bayes; Hôi quy tuyén tinh (Lincar regression), K-Trung binh (K-means) Một sô kỹ thuat trên dây phù hợp cho xử lý hinh ảnh, môt só khác dược sử dung trong xử lý tín hiệu như giong nói, âm thanh, ván bản. Huấn luyện và thử nghiệm mô hình: Sau khi chon xong mô hinh, dữ lỉệu từ kết 4u4 cúa bước tien xử lý dưvc chia làm hai phần: Dữ liệu huấn luyện (Training set) và dữ liệu tử nghỉệm (Test set) Tỷ lệ phân trám của hai tập dữ liêu này trên tập dữ lieu ban đâu thưởng là 70/30, nghĩa là 70% dữ liệu ban dằu được sử dung cho quá trinh huân luyện và 30% đữ liệu còn lai dưvc dung cho quá trinh thử nghiệm. Tuy nhien, tỷ le này không có dịnh mà tùy thuôc vào tính chât của dữ lieu, mô hinh dược sử dung và bài toán dặt ra Trong quá trinh huân luyện, thuât toán

149

## Trang 170

hoc máy ly tập dữ liệu huân luyện và hoc các thuộc tính cụ thẻ trong đó đê giám thieu lỗi tong quá trinh dánh giá mô hinh. Sau khỉ huânluyen; mô hinh đugc kiêm tra trên tập dữ liệu thử nghiệm dê dánh giá hiêu quà cua mô hinh dưvc chon và dự doán dộ chính xác của mô hinh khi sử dung trong thuc tê. Một mô hình có the cho kêt quà khác nhau nêu huân luyen và thử nghiem trên những bộ dữ lieu khác nhau cho cùng một bài toán. Mội , do mô hinh thuờng duoc sử dung nhu: Fl Scorc, Mcan Absolute Error (MAF) Mean Squared Error (MSE) đễ đánh giá tập dữ liệu thử nghiệm. Dánh gỉá hỉệu suẩt: Trong buớc này , hiệu suât của mô hình đuợc dánh giá đê cải thiện trên cà tập dữ liệu huân luyện và thử nghism. Một sỗ phưong pháp dánh giá khác nhau như: dánh giá chéo Crossvalidation) đỉêu chinh sieu tham (Hypcr- parameter   tuning) hay sừ dung Các thuat toán máy hoc khác nhau dê chon thuật toán tổi nhât .

aiocoileul

gcn bubidipk Lo,

Cbujluhiilg vnuullaic 7karnnn

icurioibiide

ral (

"riormebc{ Lyalubilod

vdclerernlon Fiulcilod O( Delind

Hinh 6.9 Qud trinh xử lý [rong hoc may

150

## Trang 171

Thuc thi mổ hình: Đây là buớc cuôi cung trong thuật toán máy hoc. Kết quả cuối cùng cúa mỗi thuật toán máy hoc là đự doán hoặc nhận ra, Mô hinh lúc này duợc sử dung dê dự doán kêt quả mong muon với đdộ chính xác cuo nhat Ví dụ: trong phân loại ảnh, nêu bài toán là dpr doán khuôn mat cua một nguài thi mô hinh có thê dự doán hoặc phát hien khuôn mat của nguvi đó một cách hiệu quả với dộ chính xác cao 6.5.1.2, Phân loai các kỹ thuât hoc máy Như dã dề cập trong phần truớc, hoc máy duuc chia làm loai: Học không giám sáL Học có giámn sát, và Hoc ing cuởng Các kỹ thuật này dưyc sử dụng với những mục dích khác nhau; duợc mô tả trong Hinh 10.

Merbes (lilibr Abaree

Webre

Wretiatohdotn n

Genke3g

l4212i7enl "

Cideaee M ll Aneaesh Unlortni

8oered

rr

L6ie Oldbins rfan (aene n

Loranca

t

fio

Hinh 610. Cảc kythuật (runk học may

Hoc có giám sát: cả dâu vào và dâu ra của mô hinh duợc dịnh nghĩa trước khi huấn luyện dữ liệu; sau đó giảm dần sai số bẳng cách s0 sánh dâu ra dược dự doán và dâu ra mong muôn. Một số kỹ thuật học có giám sát nhu; Hổi quy logic, Hổi quy 151

oon

## Trang 172

tuyên tính, K láng giêng gân nhất, Máy hỗ trg véc tơ, Naive Bayes, Mang No-ron_ Các thuật toán này dưvc chia làm nhóm: phân lowi và hồi quỵ. Đối với phân loại, dầu ra là các giá trị xác dinh hoặc các giá ưrị rời rạc, trong khi hôi quy cho ra cúc giá trị liên tục trong dâu ra: 0 mô tả kêt quả của quá trinh phân lớp dựa trên kỹ thuật Máy hỗ trợ véc to.

Hình 6.11. Minh hoa kết quả cua quá trình phân lởp bảng kỹ thuật SVM

Học không giám sát: Chỉ dữ liệu dầu vào dưvc Xác dịnh, dữ liệu đâu ra không dugc cung cấp sẵn:. Các mô hinh dược sử dung dê huân luyen tập dữ licu dê đó cho ra kết quả không doán trước được. Kỹ thuật này được chia làm hai nhóm: phân cum và nén dữ liju Trong phân cum, dữ lieu duvc gom nhóm dựa trên các diêm tương dong và khác biệt giữa các mẩu, trong khi đó, quá trinh nén dữ liệu làm sao giảm kích thuớc dữ liệu dến mức tôi thieu dên mức cân thiết vi du như giảm số chiều của dữ liệu nhiêu chiêu. Hinh 6.12 mô tả kết quả phân chia cumn tong kỹ thuật phân cum dữ lieu.

152

## Trang 173

1025 Q01

Hinh 6.12 Vỉdụ vẻ Hoc khổng giám sát Hoc táng cubng: là loai hoc máy ve hành dệng và kinh nghiệm khi tuong tác với môi trưròng Kỹ thuật loui _ này lựa chon hành dộng ' đê cực dại hóa một khodn thưởng (reward) nào đó vè lâu dài. Các thuật toán hoc tang cường cô gắng tim kiêm một chiên lược ánh xạ các trang thái của thế giới thanh các hành dộng mà một thuc thẻ (agent) nên chon trong các trạng thái dó Hinh 6.13 mô tả hoat  dộng của hoc lang cường

Agent

rowara

ecboi

Environment

Hinh 613. Hoar đpng của học tăng cường

hutps://www kdnuggets.con2018 03/5-things-reinforcement - learing html

153

ono

aeon

## Trang 174

6.5.2 Ửng dụng của học máy trong IoT vả các định hướng "ghỉên Cltu Với sy phát trien cúa cuộc cách mang cong nghiệp 4,0 dóng góp cua các thành tựu CNTT và truyên thông mới nhất vào thành phỗ thông minh dóng vai trò nòng côt. Sự kết nổi trong cả ba lĩnh vực Ván hóa (Culture). Trao dôi Hữu (Metabolism) và Quản trj (Governance) sẽ đưpc vận hành và tối ưu trên các hệ thống IoT Khi vận hảnh, các he thông IoTs này sè sinh ra một lượng dữ liệu rất lớn; dược Iưu ưrữ và xử lý trên cúc hệ thóng dữ liệu lón. Các kỹ thuật dặc biệt  là Hoc máy (Machine Learning sẽ giúp các dữ liệu này dugc phân tích dê vận hành Các các hoat dông Van hóa, Trao đốỉ chât và Quản trị một cách lur dông và thong minh. Với dữ lieu sinh ra từ các hệ thong IoTs khi van hành trong thyc te là Fât lớn, các kỹ thuât tinh toán can biên (fogledge computỉng) thường dược đê xuar đê xử lý dữ lieu phin tán trên hệ thông các thiêt bị Canh (edge devices) Do vây, sự áp dung cùa Al vào thành phô thông minh là một kịch bàn cua Việc áp dung vào các hệ thong diện toán cân biên_ Làm việc với các hệ thong dữ lieu và thuờng xuyên dược cập nhật thởi gian thực nhu vậy các hệ thong thuờng dugc xem là các hệ thóng AI tiên tién (Advanced AI - AAI) Học máy duợc sử dung trong IoT với nhiêu muc đích khác nhau nhu phân loai, dự doán, phát hiện bât thuòng nhan dang, và duơc chia làm bon nhóm chính sau: Giám sát qua hinh ảnh: Các thiết bi thông mỉnh dược trien khai đề giám sát môi truờng xung quanh; vÍ đụ như cảm biến camcra an ninh;. Dữ liệu sau khi thu thập từ các thiêt bi này sẽ dugc xử lý dê phân tích, dánh giá và hiêu rõ hon vê môi truờng xung quanh, Các thông tin này có thê dê cập dên các yêu tổ tự nhien như nhi)t độ độ âm, ánh sáng; hàm luợng COICO2 trong không khí. . và cũng có thẻ là các thông tin bên trong các he thông như áp suẩt dường ông 7 nưởc nhiet độ cúa dâu trong bng dàn dâu,_ Các kỹ thuật máy học có thê dược sử dung trong truờng hợp này dê phát hiện sớm các diêu kiện hư hỏng, bẩt thuòng hay đê dánh giá chât luong không khí hay diều kiện của mlôi truờng 154

## Trang 175

Kiêm soát_hành vi: các cơ ché giám sát thường đi kèm với diều khiễn; kiềm soát hảnh vi. Khi một sự kien, hiện tượng dat dên một nguỡng nhât dịnh nào dó (dưvc dịnh nphia truởc) cac chuc nang canh báo sẽ duợc dua ra Ví dụ: khi mật dộ giao thông trên một khu vực hay con dưòng quá cao thì hệ thông diêu khiên se dưa ra cảnh báo với nhà chửc trách dê họ có thẻ dua ra các quyêt định diêu tiêt giao thông hợp lý, hay nêu ở mức dộ cao hon, các cánh báo sẽ được dua dên ngườỉ diêu khien giao thông thong qua diện thoai thông minh và hệ thong đên tin hiệu giao thông sẽ dưoc dièu chinh đẻ phân luòng giao thông tốt hon han che tinh trang kẹt xe diễn ra Tói ưu hóa hoat dộng; Các hành dong kiêm soát hành vi thường dược sử dung dé dua ra các hành dong dua trên các ngưỡng: Tuy nhiên, phân tich dữ lieu cũng có thế dua ra những quyêt dịnh nhàm thay đỗi các quyết đjnh.  Vi du một hệ thônp kiem soát và điêu khiên cho nông nghiệp thông minh cân thu thập, phân tích, dánh giá vê dặc diêm cúa môi loại cây trong dựa vào các thông tin như vong dời, giai doan sinh trưởng của cây, thô nhuong khí hậu, tinh trang sâu bệnh cúa cây được dung dê phân tich; dánh giá và dua ra quyêt dinh ve viỆc sử dung nước phán bón; thuôc trừr sáu đê đảm bảo cho việc phát trien cúa cây là tôt nhât và tiêt kiem chi phi nhât . Tự phục hổi tự tổi ưu: SỤ phát triên nhanh chóng của hoc sâu là lặp khép kin Các hệ thong ớòng glam sat dựa trên hoc máy có thay dôi hanh và hoat dộng một cách tối ưu nhat . Vi đụ trong một hệ thóng giám sát, việc tối vong của một thiêt bị càm biên có thê dựa vào mức nang lưong còn lại cùa môi ứng dung và sự biến thiên của các giá trị cảm biến. Từ các kỹ thuât hoc máy có thê dự doán và dua Fa các quyêt dinh giảm tân suât thu thap _ dữ liệu và gửi di của mỗi nút cảm biên dê có thê kéo dài tổi da vong đời hoat dộng của mỗi nút cảm biến. Ví dụ này sẽ được mô tả rõ hơn trong chương Tải câu hìnhtái lập trình trong IoT. Trong   thành phó thông minh   (Smant   Cities),  một luợng khổng lồ dữ liệu cảm biến đuợc thu thập từ nhièu loai cảm biến, camera và thỉết bj thông minh khác nhau và những dữ liệu này 155

## Trang 176

có thẻ duvc tận dụng cho các úvp dung khác nhau của dô thi thông minh nhu giám sát môi truờng theo dõi Iuu lượng giao thông, dicu khiên den giao thông nhân   dỉện pham  giao thông; Ihêm vào dó khả nẳng cam biên tuyệt vời cúa các con đường thông minh trong tương lai, dạt dugc bẳng cách triển khai cac cong nghệ càm bien cho hạ Lang giao thông (inlrastructure sensing) sê giúp chúng ta hỗ trợ tốt hon cho ô-tô ty lái và kết nối bang cách giúp cho các quyêt dịnh diêu khiên đưgc thực hỉện nhanh và chính xác hơn. Thông thuờng dữ lỉệu cam biến phai dưoc truyên vê trung tâm dữ licu dê duvc xử lý, dua vào dó các quyêt dịnh diêu khien được dua ra và thuc thỉ cho các chúc img dung cúa thành phó óăng thông minh. Cả quá trinh này có dẫn đên độ tễ khá lớn vì thế có thể không đáp ứng dƯvc ycu cau cúa Cac ửg dung thời gian thực. Công nphe không dây SG với khả nẳng cung câp các kêt nổi không dây tôc độ cao với dộ trễ thâp và độ tin cuy rât cao cùng vói khả náng phân tích dữ liệu tai rÌa mang; có thê giúp giải quyêt các hạn chể cơ bản của các hạ tang ICT hiện có. Cu thé dữliệu cảm biên của đô thị thông minh dược thu thập từ các thiêt bị cảm biên; camera và thiết bi thông minh có thê dưgc offload vè fog scrver duoc trien khai tai các tram gôc 5G dê đuợc phân tích và xử lý nhẳm đua ra các quyêt định gân thời gian thực. Tuy nhiên; các tiem năng của công ngh; 5G này chi có the dược hiện thực hóa qua việc thiết ke các thuật toán ofjload tác vu tính toán cho các đô thị thóng minh tich hợp cóng nghé 5G, trong dó các quyêt đjnh vê việc chon dữ liệu và tác vu tính toán nào dề offload lên và xử lý tại fog server và việc phân chia tài nguyên vô tuyến và tính toán phảỉ được tối ưu dễ dạt được chất luợng tốt nhẩt và hiệu năng sử dung tài nguyên mang cao nhat . Bằng cách trang bị các công nghệ 5G- các đô thị thông minh trong tuơng lai có thê cung cấp các djch vu nội dung sô nhu TV di dộng, video độ phân giai theo yêu câu với chi phí phải chãng Mẵt khác, với việc công nghe ô-tô t lái s7 di vào cuộc song trong tuong lai gân, các tài xê ngôi sau vô lang sđ quan tim tan huởng các dịch vu nội dung sỖ vi họ sê không con ban tâm vê việc diêu khiên ô-tô cúa minh. Thực ra, luợng dữ lieu video dộng dã ting lên rât nhanh trong thời gian qua và Cisco dự 156

