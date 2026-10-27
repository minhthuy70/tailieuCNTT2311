import sys
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print(f"Tổng số dòng trong IoTmain.md: {len(lines)}")

# Tìm các vị trí chuyển tiếp dòng/đoạn bị gãy
issues = []
for idx in range(len(lines)):
    line = lines[idx].strip()
    if not line:
        continue
    
    # 1. Dòng hiện tại kết thúc lửng lơ nhưng dòng tiếp theo là dòng trống (tức là bị tách đoạn)
    # hoặc dòng tiếp theo bắt đầu bằng chữ thường
    if idx + 1 < len(lines):
        next_line = lines[idx + 1].strip()
        
        # Trường hợp A: Dòng tiếp theo không trống và bắt đầu bằng chữ thường (nhưng không phải code block hay url)
        # Trong markdown, nếu 2 dòng liên tiếp không có dòng trống, một số renderer nối lại, nhưng nhiều renderer hoặc khi có \n\n thì tách đoạn.
        pass

# Kiểm tra các cặp đoạn văn (paragraphs) ngăn cách bởi \n\n
paras = text.split('\n\n')
print(f"Tổng số khối đoạn văn: {len(paras)}")

para_breaks = []
for i in range(len(paras) - 1):
    p1 = paras[i].strip()
    p2 = paras[i+1].strip()
    
    if not p1 or not p2:
        continue
    
    # Bỏ qua nếu là heading, code block, table, list
    if any(p1.startswith(pfx) for pfx in ['#', '```', '|']):
        continue
    if any(p2.startswith(pfx) for pfx in ['#', '```', '|', '- ', '* ', '1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ']):
        continue
        
    last_char = p1[-1]
    first_char = p2[0]
    
    # Điều kiện phát hiện gãy câu giữa chừng:
    # 1. p2 bắt đầu bằng chữ thường
    # 2. p1 kết thúc bằng từ không có dấu kết câu (. ? ! : ” ")
    # 3. p1 kết thúc bằng từ ngắn nối câu như "Các", "và", "của", "được", "trong", "cho", "với", "là"
    connective_ends = ['các', 'và', 'của', 'được', 'trong', 'cho', 'với', 'là', 'như', 'về', 'để', 'có', 'kết', 'mở', 'giải', 'dựa', 'theo']
    p1_last_word = p1.split()[-1].lower() if p1.split() else ''
    # Xóa dấu câu khỏi last_word nếu có
    p1_last_clean = re.sub(r'[^\w\s]', '', p1_last_word)
    
    broken = False
    reason = ""
    
    if first_char.islower():
        broken = True
        reason = f"p2 bắt đầu chữ thường ('{p2[:20]}...')"
    elif last_char not in '.!?\":;*)`”’':
        broken = True
        reason = f"p1 không có dấu kết thúc ('...{p1[-20:]}')"
    elif p1_last_clean in connective_ends:
        broken = True
        reason = f"p1 kết thúc bằng từ nối '{p1_last_word}'"
        
    if broken:
        para_breaks.append((i, reason, p1, p2))

print(f"\nPhát hiện {len(para_breaks)} vị trí ngắt đoạn bị gãy câu:")
for i, reason, p1, p2 in para_breaks:
    print(f"\n--- [VỊ TRÍ {i}]: {reason} ---")
    print(f"ĐOẠN TRƯỚC (đuôi): ...{p1[-80:].replace(chr(10), ' ')}")
    print(f"ĐOẠN SAU   (đầu): {p2[:80].replace(chr(10), ' ')}...")
