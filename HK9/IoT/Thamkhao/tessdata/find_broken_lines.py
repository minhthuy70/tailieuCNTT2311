import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md', 'r', encoding='utf-8') as f:
    text = f.read()

paras = text.split('\n\n')
print(f"Tổng số đoạn (paragraph blocks): {len(paras)}")

broken = []
for i in range(len(paras) - 1):
    p1 = paras[i].strip()
    p2 = paras[i+1].strip()
    
    if not p1 or not p2:
        continue
        
    # Bỏ qua nếu là bảng, code, heading, danh sách
    if any(p1.startswith(prefix) for prefix in ['```', '|', '#']):
        continue
    if any(p2.startswith(prefix) for prefix in ['```', '|', '#']):
        continue
    if p2.startswith('- ') or p2.startswith('* ') or re.match(r'^\d+\.\s', p2):
        continue
        
    last_char = p1[-1]
    first_char = p2[0]
    
    is_broken = False
    reasons = []
    
    # 1. p2 bắt đầu bằng chữ thường (ví dụ: "nền tảng phần cứng...")
    if first_char.islower():
        is_broken = True
        reasons.append(f'Đoạn sau bắt đầu bằng chữ thường: "{p2[:25]}"')
        
    # 2. p1 kết thúc không phải dấu kết câu (. ! ? : ” " ) * `)
    valid_ends = {'.', '!', '?', ':', '”', '"', ')', '*', '`', ';', '…'}
    if last_char not in valid_ends:
        is_broken = True
        reasons.append(f'Đoạn trước kết thúc lửng lơ bằng "{last_char}"')
        
    if is_broken:
        broken.append((i, reasons, p1, p2))

print(f"\nTìm thấy {len(broken)} vị trí ngắt đoạn bất thường giữa chừng câu:")
for idx, reasons, p1, p2 in broken:
    tail = p1[-60:].replace('\n', ' ')
    head = p2[:60].replace('\n', ' ')
    print(f"\n[Vị trí {idx}]: {'; '.join(reasons)}")
    print(f"  << Đoạn trước: ...{tail}")
    print(f"  >> Đoạn sau  : {head}...")
