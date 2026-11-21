# -*- coding: utf-8 -*-
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = r'D:\CNTT2311\tailieuCNTT2311\HK9\Blockchain\Tom tat kien thuc Blockchain - on thi.docx'

doc = docx.Document()

def title(text):
    p = doc.add_paragraph(); r = p.add_run(text); r.bold = True; r.font.size = Pt(16)

def h1(text):
    p = doc.add_paragraph(); r = p.add_run(text); r.bold = True; r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1F, 0x3B, 0x63)

def h2(text):
    p = doc.add_paragraph(); r = p.add_run(text); r.bold = True; r.font.size = Pt(11.5)

def para(text, bold_prefix=None):
    p = doc.add_paragraph()
    if bold_prefix:
        r = p.add_run(bold_prefix); r.bold = True; r.font.size = Pt(10.5)
    r = p.add_run(text); r.font.size = Pt(10.5)

def bullet(text):
    p = doc.add_paragraph(style='List Bullet')
    r = p.add_run(text); r.font.size = Pt(10.5)

def steps(items):
    for i, t in enumerate(items, 1):
        p = doc.add_paragraph()
        r = p.add_run(f'{i}. '); r.bold = True; r.font.size = Pt(10.5)
        r = p.add_run(t); r.font.size = Pt(10.5)

# ================= TITLE =================
title('TÓM TẮT KIẾN THỨC BLOCKCHAIN — TÀI LIỆU ÔN THI')
para('Ghi chú học bài tổng hợp từ 300 câu hỏi ôn tập. Các ý liên quan được gom nhóm thành chủ đề, trình bày theo dạng khái niệm – quy trình – so sánh để dễ nhớ.')

# ================= PHẦN 1 =================
h1('PHẦN 1 — KHÁI NIỆM CỐT LÕI, LỊCH SỬ & CÁC THẾ HỆ BLOCKCHAIN')

h2('1.1. Sổ cái phân tán (DLT) và vấn đề nó giải quyết')
para('DLT lưu sổ cái trên nhiều nút và dùng cơ chế đồng thuận để xác thực, giúp loại bỏ hoàn toàn: sự phụ thuộc vào bên trung gian tin cậy, chi phí cao và nguy cơ điểm lỗi đơn lẻ (Single Point of Failure) của hệ thống tài chính tập trung.')
para('Mô hình cơ sở dữ liệu truyền thống (Centralized DB) lưu dữ liệu trên máy chủ trung tâm, quản trị viên có toàn quyền sửa/xóa — khác căn bản với Blockchain vốn phân tán và bất biến.')
para('Blockchain khác Cloud DB ở chỗ: Cloud DB do một nhà cung cấp kiểm soát và sửa được; Public Blockchain phân tán, không ai sửa được.')
para('P2P network dùng Gossip Protocol (giao thức "lan truyền tin đồn") để lan truyền giao dịch và khối giữa các nút lân cận.')

h2('1.2. Lịch sử hình thành')
para('Khủng hoảng tài chính 2008 làm sụp đổ niềm tin vào hệ thống ngân hàng tập trung và nhu cầu giao dịch minh bạch → thúc đẩy Blockchain ra đời.')
bullet('Tháng 10/2008: Satoshi Nakamoto công bố Whitepaper "Bitcoin: A Peer-to-Peer Electronic Cash System".')
bullet('03/01/2009: khai thác thành công Genesis Block (khối #0) — sự kiện khởi chạy chính thức mạng Bitcoin.')
bullet('Thông điệp trong Genesis Block: chỉ trích sự bất ổn của hệ thống ngân hàng tập trung và chính sách in tiền cứu trợ.')
bullet('2016: Vụ hack DAO trên Ethereum → Hard Fork tạo Ethereum (ETH) và Ethereum Classic (ETC).')
bullet('2017: Block Size War → Hard Fork tạo Bitcoin Cash (BCH) với block lớn hơn.')

h2('1.3. Các thế hệ Blockchain')
steps([
 'Blockchain 1.0 (Bitcoin): tiền mã hóa phi tập trung phục vụ thanh toán ngang hàng P2P.',
 'Blockchain 2.0 (Ethereum): Smart Contract + EVM — cỗ máy ảo phân tán cho phép thực thi mã hợp đồng thống nhất.',
 'Blockchain 3.0 (Cardano, Polkadot, Solana): tối ưu hiệu năng, tăng scalability, giảm phí, hỗ trợ interoperability — giải quyết thách thức scalability/tốc độ chậm/phí cao của 2.0 bằng Sharding (chia mạng thành các shard song song).',
 'Blockchain 4.0: tích hợp AI, IoT, Big Data làm hạ tầng chuyển đổi số cho doanh nghiệp và chính phủ.',
])
para('Các giải pháp mở rộng: Layer 2 (Lightning Network, Polygon, Rollups, State Channels) xử lý giao dịch off-chain rồi gửi proof về Layer 1; Sidechain là chuỗi độc lập kết nối Mainchain qua Bridge.', bold_prefix='Lưu ý: ')
para('Blockchain hỗ trợ Financial Inclusion cho người vùng sâu không có tài khoản ngân hàng nhưng có Internet. Estonia là quốc gia tiên phong áp dụng Blockchain vào chính phủ điện tử (hồ sơ công dân, y tế, dịch vụ công).')

h2('1.4. Các khái niệm tính chất cốt lõi')
para('Bất biến (Immutability): dữ liệu không thể thay đổi nhờ liên kết băm giữa các khối + Merkle tree + đồng thuận đa số. Một giao dịch đã ghi và đủ confirmations gần như không thể đảo ngược trừ khi kiểm soát >51% tài nguyên mạng.', bold_prefix='Bất biến — ')
para('Một chiều giải quyết triệt để: sổ cái P2P đồng bộ + PoW ngăn một đồng coin bị chi tiêu hai lần.', bold_prefix='Double-Spending — ')
para('Mọi giao dịch công khai, ai cũng truy vết và kiểm chứng lịch sử sổ cái.', bold_prefix='Minh bạch (Transparency) — ')
para('Danh tính gắn với địa chỉ ví chuỗi băm thay vì tên pháp lý.', bold_prefix='Ẩn danh tương đối (Pseudonymity) — ')
para('Theo dõi minh bạch toàn bộ hành trình sản phẩm từ sản xuất đến tay người tiêu dùng — lợi ích lớn cho logistics.', bold_prefix='Traceability — ')
para('Trạng thái giao dịch không thể bị đảo ngược, hủy bỏ hay chỉnh sửa.', bold_prefix='Finality (Hoàn tất) — ')
para('Giao dịch chưa đóng vào khối, chỉ nằm trong Mempool hoặc vừa phát tán.', bold_prefix='Unconfirmed — ')

h2('1.5. Coin, Token và các loại token')
para('Coin là tài sản gốc chạy trên Blockchain riêng (BTC, ETH); Token phát hành trên Blockchain có sẵn.')
para('Stablecoin (USDT, USDC, DAI) neo giá vào tài sản thực để giảm biến động mạnh của tiền mã hóa.')
para('Chuẩn token trên Ethereum: ERC-20 (token thay thế được), ERC-721 (NFT — token không thể thay thế).')
para('Utility Token: dùng để truy cập dịch vụ trong hệ sinh thái. Security Token: đại diện quyền sở hữu tài sản/lợi nhuận.')

h2('1.6. Fork và các vấn đề bảo mật')
para('Soft Fork: tương thích ngược, không tạo chuỗi mới. Hard Fork: không tương thích ngược, có thể tạo chuỗi mới.', bold_prefix='Phân tách (Fork) — ')
para('Khi một thực thể kiểm soát >50% tổng Hashrate toàn mạng PoW → có thể đảo giao dịch, chi tiêu kép.', bold_prefix='Tấn công 51% — ')
para('Rủi ro quản lý Private Key: mất hoặc lộ key = mất tài sản vĩnh viễn, không ai hỗ trợ — đây cũng là thách thức UX lớn nhất. Ví lạnh (Cold Wallet) lưu khóa offline chống tấn công mạng; ví nóng (Hot Wallet) tiện nhưng rủi ro hơn.', bold_prefix='Private Key & ví — ')
para('Lỗ hổng Smart Contract: lỗi lập trình trong mã nguồn bị khai thác rút tiền/chiếm quyền. Smart Contract khó sửa sau khi deploy vì tính bất biến.', bold_prefix='Smart Contract — ')
para('Sàn giao dịch tập trung (CEX): người dùng không nắm Private Key; sàn bị hack/phá sản → mất tài sản.', bold_prefix='Rủi ro CEX — ')
para('Khung pháp lý tiền mã hóa chưa đồng nhất giữa các quốc gia → rào cản triển khai. ICO 2017 bị siết vì thiếu bảo vệ nhà đầu tư, nhiều dự án lừa đảo.', bold_prefix='Rủi ro pháp lý & ICO — ')

h2('1.7. Giá trị & ứng dụng')
steps([
 'Chuyển tiền quốc tế: rút ngắn thời gian, giảm chi phí trung gian, hoạt động 24/7.',
 'Smart Contract tự động hóa If-Then: giảm chi phí nhân lực, loại trung gian, loại tranh chấp.',
 'DApp khác Web2: backend chạy trên Blockchain qua Smart Contract.',
 'DAO: quản trị phi tập trung bằng quy tắc lập trình sẵn trong Smart Contract + quyền biểu quyết của token holder.',
 'Oracle: cầu nối đưa dữ liệu thực tế off-chain (thời tiết, chuyến bay) vào Smart Contract — nền tảng cho bảo hiểm tự động.',
 'Tokenomics: nghiên cứu mô hình kinh tế, phân phối, cung cầu, tiện ích của token.',
])
para('PoW tiêu thụ điện năng khổng lồ — thách thức môi trường lớn nhất. Scalability thấp (vài chục TPS so với Visa hàng chục nghìn TPS) là nút thắt khiến chuỗi nghẽn, phí tăng.')

# ================= PHẦN 2 =================
h1('PHẦN 2 — CẤU TRÚC HỆ THỐNG, THÀNH PHẦN & MỞ RỘNG')

h2('2.1. Vòng đời một giao dịch (Mempool)')
para('Mempool (Memory Pool) là bộ nhớ tạm tại mỗi nút chứa các giao dịch hợp lệ đang chờ miner/validator gom vào khối. Giao dịch chỉ nằm ở Mempool hoặc vừa phát tán = chưa xác nhận.')
para('Full Node lưu toàn bộ lịch sử sổ cái và trực tiếp kiểm tra tính hợp lệ của mọi khối/giao dịch. Light Node (SPV client) chỉ tải Block Header + dùng Merkle Proof để xác minh, tiết kiệm băng thông/dung lượng — lý tưởng cho ví di động; dùng Bloom Filter để tìm nhanh giao dịch liên quan đến ví mình mà không lộ toàn bộ ví.')

h2('2.2. Cấu trúc một khối (Block)')
para('Block gồm 2 phần: Block Header (~80 bytes, chứa dữ liệu quản lý/bảo mật) và Block Body (danh sách giao dịch, sắp xếp dạng cây Merkle).')
h2('Các trường trong Block Header')
steps([
 'Version: chỉ định phiên bản quy tắc đồng thuận, hỗ trợ nâng cấp mạng (fork).',
 'Previous Block Hash: kết quả SHA-256 trên toàn bộ Block Header của khối liền trước → liên kết chuỗi, tạo bất biến ("sợi xích mã hóa").',
 'Merkle Root: mã băm tổng hợp đại diện cho toàn bộ giao dịch trong Block Body — tóm tắt để kiểm tra nhanh.',
 'Timestamp: thời điểm tạo khối, định dạng Unix Epoch Time (số giây từ 00:00:00 UTC 01/01/1970), chuẩn toàn cầu không phụ thuộc múi giờ.',
 'Nonce: số nguyên 32-bit miner thay đổi liên tục để tìm Block Hash đạt độ khó.',
 'Difficulty Target: mức độ khó của bài toán mật mã — yêu cầu số bit 0 nhất định ở đầu mã băm.',
])
para('Block Hash = SHA-256(SHA-256(toàn bộ dữ liệu Block Header)) — hàm băm 2 lần tăng an toàn, chống Length Extension Attack.')
para('Lưu ý: Genesis Block có Previous Block Hash = 0 (không trỏ khối nào), coin thưởng không chi tiêu được. Hai nút có Genesis Block khác nhau = thuộc 2 mạng hoàn toàn riêng biệt. Sửa 1 giao dịch ở khối #50 → Merkle Root #50 đổi → Block Hash #50 đổi → Previous Hash khối #51 sai → cả chuỗi sau vô hiệu; muốn sửa phải tính lại PoW cho khối đó và TẤT CẢ khối sau nhanh hơn toàn mạng → gần như bất khả thi.', bold_prefix='Chuỗi liên kết & tính bất biến — ')

h2('2.3. Cây Merkle trong Block Body')
para('Giao dịch trong Block Body được tổ chức thành Merkle Tree (cây nhị phân) để đảm bảo toàn vẹn, xác minh nhanh và tiết kiệm dung lượng Header. Merkle Root nằm trong Header; giao dịch lẻ cuối được nhân đôi để tạo cặp băm (ví dụ T1..T5 → nhân đôi T5). Sửa 1 ký tự ở T2 → Hash(T2) đổi → Parent Hash đổi → Merkle Root đổi hoàn toàn.')
para('Merkle Proof: tập hợp ngắn các mã băm bổ sung để tính ngược từ 1 giao dịch lên Merkle Root → Light Node/SPV kiểm tra giao dịch tồn tại trong khối mà không cần tải cả block. Trong khối 1.000.000 giao dịch chỉ cần khoảng log2(1.000.000) ≈ 20 mã băm. Merkle Tree có tính Tamper-evident: sửa nhỏ ở đáy cây → Merkle Root đổi ngay.')
para('Khác với Merkle DAG (IPFS/Ethereum): DAG là đồ thị hướng không chu trình, một nút con có thể có nhiều nút cha và tham chiếu nội dung.')

h2('2.4. Coinbase Transaction & kinh tế khối')
para('Coinbase Transaction là giao dịch đầu tiên (index 0) trong Block Body, thưởng cho miner/validator. Phần thưởng = Block Reward (coin mới đúc) + tổng phí giao dịch trong khối. Tạo Coinbase với số dư cao hơn quy định → toàn mạng từ chối khối.')
steps([
 'Bitcoin Halving: sau mỗi 210.000 khối (~4 năm) cắt giảm 50% coin mới đúc.',
 'Difficulty Target tự điều chỉnh để giữ thời gian tạo khối trung bình ~10 phút ổn định.',
 'Block Size Limit (~1MB trong Bitcoin gốc) giới hạn số giao dịch/khối → nghẽn mạng, phí tăng.',
])
para('Block Size War → Hard Fork 2017 tạo Bitcoin Cash (BCH). Trong Ethereum/Blockchain 2.0, Block Body chứa thêm dữ liệu Smart Contract, gọi hàm, tạo Token, giao dịch DApps.')

h2('2.5. Xác nhận, Reorg và mô hình tài khoản')
para('Confirmations = số khối được tạo tiếp theo kể từ khối chứa giao dịch (tính cả khối chứa nó). Bitcoin thường cần ≥6 confirmations để an toàn cao vì đảo 6 khối liên tiếp đòi hỏi hashrate khổng lồ. Giao dịch "không thể đảo ngược" khi đạt đủ số confirmations an toàn.')
para('Reorg (Reorganization): hai thợ đào tạo khối cùng lúc → chuỗi tách 2 nhánh, nhánh dài hơn thắng. Orphan/Stale Block: khối hợp lệ nhưng bị loại vì khối đối thủ lan truyền nhanh hơn.')
para('UTXO (Bitcoin): số dư = tổng các đầu ra giao dịch chưa chi tiêu (unspent outputs) gắn với địa chỉ ví. Account-based (Ethereum): quản lý số dư trực tiếp theo trạng thái tài khoản như tài khoản ngân hàng.')
para('Nakamoto Consensus = PoW + mạng P2P Gossip + Longest Chain Rule (chọn chuỗi có tổng độ khó lớn nhất). Mục đích của mọi cơ chế đồng thuận: các nút không tin nhau thống nhất duy nhất 1 bản ghi sổ cái đúng. Auditability đạt được nhờ lịch sử ghi theo thời gian + liên kết băm bất biến + công khai toàn mạng.')

h2('2.6. Tổng quan các cơ chế đồng thuận (chi tiết ở Phần 6)')
bullet('PBFT: 3 giai đoạn bỏ phiếu pre-prepare → Prepare → Commit; Leader (Primary) nhận giao dịch, sắp xếp, đóng gói và phát tán Pre-prepare; Replica phát hiện Leader hỏng/gian lận → View Change bầu Leader mới; cần n = 3f + 1 nút để chịu f nút lỗi (điều kiện f < n/3, nút trung thực còn >2/3); đạt ≥2/3 phiếu ở Commit → Finality tức thì; nhược điểm O(n²) thông điệp → chỉ hợp Permissioned/Consortium blockchain.')
bullet('PoS: thay sức mạnh tính toán bằng stake; Slashing tịch thu coin stake nếu validator gian lận/bỏ phiếu sai → ngăn double-spending và Nothing at Stake.')
bullet('DPoS: người giữ token bầu ra nhóm delegates nhỏ (EOS: 21 Block Producers) → TPS rất cao nhưng tập trung quyền lực, nguy cơ thông đồng.')
bullet('PoA: quyền xác thực giao cho số ít Authorities đã xác minh danh tính, uy tín, trách nhiệm pháp lý → hiệu suất cao, chi phí rẻ, hợp Private/Testnet/chuỗi cung ứng; điểm yếu: tập trung cao, phụ thuộc bên thứ ba.')
bullet('PoH (Solana): chuỗi băm tính tuần tự đóng vai trò "đồng hồ toàn cầu" ghi thứ tự thời gian → không cần chờ đồng bộ mạng. Tower BFT tận dụng PoH để validator bỏ phiếu nhanh.')
bullet('Smart Contract: tự thực thi theo logic If-Then.')

# ================= PHẦN 3 =================
h1('PHẦN 3 — PHÂN LOẠI MÔ HÌNH BLOCKCHAIN & ỨNG DỤNG THỰC TIỄN')

h2('3.1. Bốn mô hình Blockchain')
para('Tiêu chí phân loại cốt lõi: quyền truy cập (đọc/ghi dữ liệu) và mức độ tập trung/phi tập trung trong quản trị.')
steps([
 'Public Blockchain: mọi người tự do tham gia, đọc dữ liệu, làm nút xác thực, không cần cấp phép. Ưu: minh bạch, phi tập trung. Nhược: chậm, tốn tài nguyên, khó bảo mật dữ liệu nội bộ, phí gas cao có thể lớn hơn giá trị hàng bán lẻ.',
 'Private Blockchain: một tổ chức kiểm soát duy nhất; chỉ thành viên được cấp quyền tham gia; giao dịch do Authorized Nodes xác thực. Ưu: rất nhanh, chi phí thấp, bảo mật tối đa. Nhược: phụ thuộc vendor, nguy cơ Vendor Lock-in, khó tương thích mạng ngoài. Ví dụ: Hyperledger Fabric (IBM).',
 'Consortium (Federated) Blockchain: quyền quản trị/phân bổ cho nhóm tổ chức liên minh; khối mới cần đồng thuận đa số đại diện thành viên. Ưu: chia sẻ dữ liệu tin cậy giữa các bên (ngân hàng liên minh R3 Corda). Nhược: phức tạp thỏa thuận, xung đột lợi ích khi mở rộng. Ví dụ: R3 Corda.',
 'Hybrid Blockchain: kết hợp linh hoạt Public + Private — dữ liệu riêng tư bảo mật, dữ liệu chung công khai; công chúng xem chứng nhận tổng hợp, kiểm toán viên xem chi tiết theo quyền. Ví dụ: IBM Food Trust, Dragonchain — phù hợp y tế (bệnh án riêng tư + dữ liệu dịch tễ công khai).',
])
para('Ngân hàng xây thanh toán nội bộ tốc độ cao → chọn Private Blockchain. Public Blockchain KHÔNG phù hợp lưu bí mật kinh doanh vì sổ cái công khai toàn mạng.')

h2('3.2. Tài sản số & DeFi')
steps([
 'CBDC (e-CNY của Trung Quốc): tiền kỹ thuật số do Ngân hàng Trung ương phát hành, quản lý, đảm bảo giá trị pháp lý.',
 'DeFi: cho vay, tiết kiệm, giao dịch, bảo hiểm tự động qua Smart Contract không qua ngân hàng.',
 'DeFi Composability: các protocol ghép như Lego — kết hợp Smart Contract DeFi với nhau.',
 'Uniswap: AMM (Automated Market Maker) tạo thanh khoản tự động qua Smart Contract, không dùng sổ lệnh.',
 'RWA (Real World Assets): bất động sản, trái phiếu, vàng, hàng hóa, tác phẩm nghệ thuật đưa lên chuỗi dạng token.',
 'NFT: xác nhận quyền sở hữu độc bản/tính nguyên gốc của tài sản số hoặc sản phẩm độc quyền.',
 'Loyalty Program trên Blockchain: token thưởng quy đổi/trao đổi linh hoạt giữa nhiều thương hiệu.',
])
para('Ripple (RippleNet): chuyển tiền quốc tế gần như tức thì vài giây, chi phí cực thấp, thanh khoản cao — vượt trội SWIFT.')
para('Cross-chain: chuyển giao tài sản/dữ liệu trực tiếp giữa 2 blockchain độc lập. Interoperability Protocol (Blockchain 3.0): bộ quy chuẩn để các nền tảng truyền tin, chuyển tài sản an toàn — giải quyết vấn đề thiếu chuẩn hóa giữa hàng nghìn blockchain.')
para('Sovereign Identity (SSI): người dùng tự quản lý/kiểm soát dữ liệu định danh, không phụ thuộc bên thứ 3. Zero-Knowledge Proof: chứng minh một nhận định đúng mà không tiết lộ nội dung chi tiết trên sổ cái.')
para('Mô hình triển khai doanh nghiệp: Proof of Concept (PoC) là giai đoạn thử nghiệm quy mô nhỏ chứng minh tính khả thi kỹ thuật và giá trị kinh doanh.')

h2('3.3. Ứng dụng theo ngành')
steps([
 'Y tế: Smart Contract tự động chi trả bảo hiểm khi dữ liệu khám bệnh xác minh hợp lệ; MediLedger (Mỹ) quản lý chuỗi cung ứng thuốc, chống thuốc giả.',
 'Dược phẩm & Chuỗi cung ứng: VeChain truy xuất nguồn gốc hàng hiệu, nông sản sạch; IBM Food Trust (Maersk) số hóa chứng từ vận tải biển TradeLens, giảm thời gian chờ nhập cảng; truy xuất nguồn gốc lô nhiễm khuẩn chỉ vài giây thay vì nhiều ngày.',
 'Nông nghiệp Việt Nam: truy xuất nguồn gốc xuất khẩu xoài, vải thiều, gạo, thủy hải sản.',
 'Quản trị công: đăng ký đất đai chống giả giấy chứng nhận, tranh chấp trùng hồ sơ; bầu cử điện tử Ukraine — mỗi phiếu là giao dịch bất biến, chống gian lận đếm phiếu; bằng cấp số giáo dục — triệt tiêu bằng giả, nhà tuyển dụng xác thực tức thì.',
 'Bất động sản: cắt giảm thủ tục giấy tờ, minh bạch lịch sử giao dịch, hỗ trợ chia nhỏ sở hữu (Fractionalization).',
 'Bảo hiểm: Smart Contract tự động bồi thường dựa trên Oracle (dữ liệu thời tiết, chuyến bay bị hoãn).',
 'Trade Finance: số hóa chứng từ (vận đơn, L/C), chia sẻ tức thì giữa ngân hàng, hải quan, hãng tàu.',
 'Smart City: kết hợp IoT + Blockchain minh bạch dữ liệu cảm biến đô thị (giao thông, năng lượng), tự động hóa thanh toán dịch vụ công.',
 'Ngân hàng: Consortium Blockchain (R3 Corda) chia sẻ dữ liệu xác thực tín dụng, thanh toán liên ngân hàng an toàn giữa thành viên.',
])

# ================= PHẦN 4 =================
h1('PHẦN 4 — QUY TRÌNH GIAO DỊCH, CẤU TRÚC KHỐI & GENESIS BLOCK')

h2('4.1. Quy trình 6 bước xử lý giao dịch')
steps([
 'Bước 1 — Khởi tạo: người gửi tạo lệnh, điền thông tin và ký chữ ký số bằng Private Key. Giao dịch bắt buộc chứa: Public Key gửi/nhận, số lượng tài sản, timestamp, chữ ký số. (Ví dụ: Alice gửi 1 BTC cho Bob → Alice ký bằng Private Key của mình.)',
 'Bước 2 — Phát tán & kiểm tra sơ bộ: broadcast lên mạng P2P; các nút kiểm tra chữ ký hợp lệ và người gửi đủ số dư → đưa vào Mempool.',
 'Bước 3 — Đóng khối: miner/validator gom giao dịch hợp lệ từ Mempool thành khối mới, xây dựng Merkle Tree.',
 'Bước 4 — Đồng thuận: các nút thống nhất duy nhất một phiên bản khối hợp lệ (PoW, PoS...) để thêm vào chuỗi.',
 'Bước 5 — Liên kết & lưu trữ: thêm khối mới vào chuỗi bằng Previous Block Hash trỏ về khối trước → khiến việc sửa lịch sử gần như bất khả thi.',
 'Bước 6 — Xác nhận: giao dịch an toàn tuyệt đối khi khối chứa nó được ghi vào chuỗi và có thêm đủ số khối tiếp theo nối sau (ví dụ ≥6 confirmations).',
])

h2('4.2. Genesis Block')
para('Genesis Block (khối #0) là khối khởi nguyên đầu tiên, nền móng liên kết cả chuỗi. Đặc điểm riêng: Previous Block Hash = 0 (không trỏ khối nào), coin thưởng không thể chi tiêu được. Bitcoin Genesis Block do Satoshi tạo ngày 03/01/2009.')

# ================= PHẦN 5 =================
h1('PHẦN 5 — MẬT MÃ HỌC, HÀM BĂM SHA-256 & CÂY MERKLE')

h2('5.1. Hashing vs Encryption')
para('Hashing KHÔNG phải Encryption: Hash là hàm 1 chiều, không thể giải mã ngược; Encryption là hàm 2 chiều, giải mã được bằng Key.')
para('HMAC = hàm băm + Secret Key để xác thực tính toàn vẹn và nguồn gốc. Blind Signature cho phép ký xác thực nội dung mà người ký không cần xem nội dung (bảo vệ riêng tư).')

h2('5.2. Hàm băm SHA-256')
steps([
 'Đầu ra cố định 256 bit = 64 ký tự hex, dù đầu vào 1 từ hay cả cuốn sách.',
 'Deterministic: cùng đầu vào → luôn cùng đầu ra. Hai giao dịch giống nhau nhưng khác timestamp → hash hoàn toàn khác.',
 'One-way: dễ tính hash từ dữ liệu, bất khả thi suy ngược dữ liệu gốc.',
 'Avalanche Effect: đổi 1 bit đầu vào → đầu ra đổi hoàn toàn.',
 'Collision Resistance: cực khó tìm 2 đầu vào khác nhau cho cùng 1 hash; Pre-image Attack: tìm lại dữ liệu gốc x khi chỉ biết h = Hash(x).',
 'An toàn brute-force: không gian đầu ra 2^256, lớn hơn tổng số hạt nguyên tử trong vũ trụ quan sát được → đụng độ gần như không thể xảy ra.',
])
para('SHA-256 do NSA (Cơ quan An ninh Quốc gia Mỹ) thiết kế, viết tắt Secure Hash Algorithm; gồm 64 vòng lặp biến đổi cho mỗi khối dữ liệu. Trong Bitcoin, giao dịch băm 2 lần (Double SHA-256) để chống Length Extension Attack. Ethereum dùng Keccak-256 — chuẩn gốc của SHA-3, thuật toán nội bộ khác SHA-256.')
para('Post-Quantum Cryptography: thuật toán chữ ký/băm mới chống tấn công máy tính lượng tử. Rủi ro lượng tử: ECDSA có thể bị bẻ bởi thuật toán Shor; SHA-256 chỉ giảm một nửa độ bảo mật (Grover).')

h2('5.3. Mật mã khóa công khai & chữ ký số')
para('Mật mã bất đối xứng dùng cặp khóa: Public Key + Private Key. Private Key → Public Key qua hàm toán học 1 chiều, không suy ngược được. ECDSA (đường cong elip secp256k1) dùng trong Bitcoin/Ethereum để khởi tạo cặp khóa và ký — an toàn vì tìm Private Key từ Public Key là bất khả thi.')
steps([
 'Ký số: người gửi dùng Private Key mã hóa băm giao dịch → tạo chữ ký số đính kèm lệnh gửi.',
 'Xác minh: các nút dùng Public Key người gửi + chữ ký để kiểm tra hợp lệ, không cần biết Private Key. Nếu khớp → chứng tỏ người gửi nắm đúng Private Key → xác nhận chủ quyền tài sản.',
 'Sửa đổi giao dịch đã ký (ví dụ đổi số tiền) → hash mới không khớp chữ ký → chữ ký vô hiệu ngay lập tức.',
])

h2('5.4. Địa chỉ ví & các loại ví')
steps([
 'Tạo địa chỉ Bitcoin: Public Key → băm SHA-256 + RIPEMD-160 → định dạng Base58Check (loại ký tự dễ nhầm 0, O, I, l + thêm mã kiểm lỗi) → địa chỉ Pay-to-Public-Key-Hash (P2PKH).',
 'Công khai địa chỉ ví vẫn an toàn vì không thể suy ngược ra Private Key.',
 'HD Wallet (Hierarchical Deterministic): từ 1 Seed Phrase tạo cây vô hạn cặp khóa. BIP-39 chuẩn hóa: Entropy ngẫu nhiên → 12-24 từ khôi phục. Entropy yếu → hacker dễ đoán Private Key.',
 'Seed Phrase lộ cho người khác = mất toàn bộ tài sản vì khôi phục được mọi Private Key.',
 'Multisig (m-of-n): giao dịch cần m chữ ký trên n khóa (ví dụ 2/3) mới chi tiêu được → doanh nghiệp tránh mất tài sản khi 1 người lộ key và chống gian lận nội bộ.',
])

h2('5.5. Cây Merkle (Merkle Tree) — chi tiết')
para('Do Ralph Merkle sáng chế năm 1979. Cấu trúc cây nhị phân: mỗi nút cha = hash của 2 nút con ghép lại; lá cây là hash các giao dịch; gốc là Merkle Root.')
steps([
 'Ví dụ 4 giao dịch: root = Hash(Hash(T1+T2) + Hash(T3+T4)).',
 'Giao dịch lẻ (T1..T5): nhân đôi T5 để tạo cặp băm nhị phân.',
 'Merkle Proof: chỉ cần ~log2(n) hash (≈20 cho 1 triệu giao dịch) để kiểm tra 1 giao dịch thuộc khối.',
])
para('Merkle Root đặt trong Header (không đặt cả cây) để Header nhỏ gọn cố định ~80 bytes. Tamper-evident: sửa nhỏ ở đáy → Root đổi ngay. Nút nhẹ di động dùng Merkle Proof + Bloom Filter để xác minh nhanh, tiết kiệm băng thông và dung lượng.')

# ================= PHẦN 6 =================
h1('PHẦN 6 — CÁC CƠ CHẾ ĐỒNG THUẬN CHUYÊN SÂU')

h2('6.1. Tổng quan')
para('Mục đích của mọi cơ chế đồng thuận: các nút không tin nhau thống nhất duy nhất 1 bản ghi sổ cái đúng. Mạng Synchronous giả định độ trễ truyền tin có giới hạn cố định tối đa; Asynchronous không giả định giới hạn.')
para('PoW dựa trên Năng lượng/Phần cứng · PoS dựa trên Tài sản Stake · PoA dựa trên Danh tính/Uy tín — đây là khác biệt cốt lõi của 3 cơ chế.')

h2('6.2. Proof of Work (PoW)')
para('Miner liên tục thử các giá trị Nonce khác nhau để tìm Block Hash ≤ Difficulty Target (đủ số bit 0 đầu mã băm). Ưu điểm: cực kỳ an toàn lịch sử nhờ năng lượng/hashrate thực tế, bảo vệ Bitcoin >17 năm. Nhược điểm: tốn điện khổng lồ, TPS thấp, nguy cơ tập trung mỏ đào.')
steps([
 'Mining Pool: gộp sức mạnh nhiều miner nhỏ để tăng xác suất giải khối, chia đều thưởng.',
 '51% Attack: kiểm soát >50% hashrate → đảo giao dịch, chi tiêu kép. Rủi ro: vài pool lớn hợp tác vượt ngưỡng.',
 'Selfish Mining: giấu khối vừa giải, đào tiếp chuỗi bí mật dài hơn để cuỗm thưởng.',
 'Eclipse Attack: chiếm toàn bộ kết nối P2P của 1 nút → cung cấp sổ cái giả. Sybil Attack bị vô hiệu vì tạo danh tính giả không tạo quyền lực — cần tài nguyên thực (năng lượng/stake).',
])

h2('6.3. Proof of Stake (PoS)')
para('Thay sức mạnh tính toán bằng stake: khóa/đặt cược coin để nhận quyền đề xuất và xác thực khối. Validator được chọn ngẫu nhiên có trọng số — stake càng lớn xác suất càng cao. Ethereum 2.0 yêu cầu tối thiểu 32 ETH/validator. Ưu điểm lớn: giảm năng lượng >99.9% so với PoW.')
steps([
 'Slashing: validator gian lận/bỏ phiếu sai → tịch thu ngay một phần/toàn bộ stake + loại khỏi mạng. Double Sign (ký 2 khối cùng chiều cao 2 nhánh) → phát hiện bằng chứng → Slashing trừ sạch ETH.',
 'Nothing at Stake: validator không tốn chi phí năng lượng nên có thể vote mọi nhánh fork để trục lợi. Khắc phục: Slashing + trừng phạt khi vote 2 nhánh; chi tiêu kép trong PoS bị ngăn nhờ Slashing đe dọa lợi ích tài chính.',
 'Unbonding Period: thời gian chờ giữ tiền cược sau khi ngừng làm validator → ngăn tấn công rồi bỏ chạy.',
 '51% Stake Attack khác PoW: kẻ tấn công không chiếm vĩnh viễn mạng — cộng đồng Hard Fork loại bỏ + slashing toàn bộ stake.',
 'Liquid Staking (Lido Finance): stake ETH nhận lại stETH → vẫn tham gia DeFi mà không khóa vốn.',
])

h2('6.4. Delegated Proof of Stake (DPoS)')
para('Người giữ token bỏ phiếu bầu ra nhóm đại biểu (Delegates/Block Producers) xác thực khối — ví như dân chủ đại diện. EOS: cố định 21 Block Producers → TPS hàng ngàn nhưng đánh đổi phi tập trung (tập trung quyền lực vào ít đại biểu, nguy cơ thông đồng). Người dùng kiểm soát bằng cách Unvote bất kỳ lúc nào nếu delegate gian lận, trễ khối hoặc kém hiệu quả.')

h2('6.5. Proof of Authority (PoA)')
para('Trao quyền xác thực cho số ít Authorities đã xác minh danh tính, uy tín, trách nhiệm pháp lý → uy tín và pháp luật là động lực duy trì trung thực. Hiệu suất cực cao, chi phí cực rẻ (không giải toán mật mã, ít nút, không bỏ phiếu phức tạp). Ứng dụng: Private Blockchain doanh nghiệp, Testnet, chuỗi cung ứng. Điểm yếu: tập trung cao, phụ thuộc tin tưởng bên thứ ba.')

h2('6.6. Practical Byzantine Fault Tolerance (PBFT)')
para('Giải bài toán Byzantine Generals: đạt đồng thuận khi có nút gian lận. Cấu trúc: 1 Leader (Primary Node) + các Replica. Leader nhận giao dịch, sắp xếp thứ tự, đóng gói khối và phát tán giai đoạn Pre-prepare.')
para('Ba giai đoạn bỏ phiếu chính:')
steps([
 'Pre-prepare (Tiền chuẩn bị): Leader đề xuất khối.',
 'Prepare (Chuẩn bị): các Replica bỏ phiếu kiểm tra đề xuất.',
 'Commit (Cam kết): các Replica xác nhận và chốt khối.',
])
para('Điều kiện chịu lỗi: cần tối thiểu n = 3f + 1 nút để chịu f nút gian lận/hỏng — đảm bảo khi f nút không phản hồi và f nút gian lận, nút trung thực còn lại vẫn đạt đa số >2/3. Ngưỡng an toàn: số nút lỗi < 1/3 tổng số nút (f < n/3). Đạt đủ 2/3 phiếu ở Commit → Finality tức thì, khối vĩnh viễn không fork.')
para('Nếu Leader hỏng/gian lận/không phát tín hiệu đúng giờ → Replica phát hiện không nhất quán → View Change bầu Leader mới.')
para('Hạn chế: số thông điệp trao đổi tăng O(n²) → khó scale cho public blockchain hàng nghìn nút; chỉ hợp Private/Consortium với số nút vừa phải. So với Raft: Raft chỉ chịu Crash Fault (máy hỏng/ngắt kết nối), KHÔNG chịu Byzantine Fault → doanh nghiệp chọn Raft cho private chain tin tưởng nhau cần tốc độ tối đa.')

h2('6.7. Proof of History (PoH) — Solana')
para('PoH là "giải pháp mã hóa thời gian": chuỗi băm tính toán tuần tự đóng vai trò đồng hồ toàn cầu ghi nhận thứ tự sự kiện → validator không cần chờ toàn mạng đồng bộ, thứ tự giao dịch định sẵn → Solana đạt >50.000 TPS. Kết hợp Tower BFT (dùng dòng thời gian PoH để bỏ phiếu nhanh, giảm độ trễ) → kiến trúc đồng thuận Solana.')
para('Thách thức hạ tầng Solana: validator cần phần cứng siêu mạnh (CPU nhiều nhân, RAM lớn, mạng high-bandwidth), chi phí cao.')

h2('6.8. Các cơ chế khác')
steps([
 'Proof of Burn (PoB): gửi coin vào Burn Address (ví không có Private Key) để nhận quyền đúc/khai thác coin mới.',
 'Proof of Space/Capacity (Chia Network): dùng dung lượng đĩa trống lưu sẵn file dữ liệu băm (Plots) thay vì CPU/GPU.',
 'Casper FFG Checkpoints (Ethereum PoS): ấn định trạng thái hoàn tất vĩnh viễn cho các khối sau mỗi Epoch (32 slots), ngăn fork lịch sử xa — cơ chế tạo Deterministic Finality.',
])
para('Finality: PoW = Probabilistic (càng nhiều block sau càng an toàn); PBFT/PoA = Deterministic tức thì.')

h2('6.9. MEV và Ethereum PoS')
para('MEV (Maximal Extractable Value): lợi nhuận validator/miner thu thêm nhờ quyền chèn, xóa, sắp xếp lại giao dịch trong khối. Giải pháp Proposer-Builder Separation (PBS): tách vai trò Builder (xây khối) và Proposer (đề xuất) → giảm tập trung hóa MEV.')

h2('6.10. Blockchain Trilemma')
para('Do Vitalik Buterin đề xuất: một hệ thống Blockchain không thể đạt trọn vẹn cả 3 yếu tố Phi tập trung, Bảo mật và Mở rộng (Scalability) ở mức tối đa. Bitcoin đánh đổi: ưu tiên phi tập trung + bảo mật → chấp nhận scalability thấp (~7 TPS).')

doc.save(OUT)
print('saved', OUT)
print('paragraphs', len(doc.paragraphs))
PY = None
import os
print('size', os.path.getsize(OUT))
