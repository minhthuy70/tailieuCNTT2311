import re, sys

def clean_ocr_artifacts(text):
    # Regex word replacements
    subs = [
        # Dung / Dụng / Dựng / Dùng
        (r'\b(sử|ứng|áp|nội|phổ|thông|tác|xây|lạm|tận)\s+dùng\b', lambda m: m.group(1) + (' dựng' if m.group(1).lower() == 'xây' else (' dung' if m.group(1).lower() == 'nội' else ' dụng'))),
        (r'\b(Sử|Ứng|Áp|Nội|Phổ|Thông|Tác|Xây|Lạm|Tận)\s+dùng\b', lambda m: m.group(1) + (' dựng' if m.group(1).lower() == 'xây' else (' dung' if m.group(1).lower() == 'nội' else ' dụng'))),
        (r'\b(SỬ|ỨNG|ÁP|NỘI|PHỔ|THÔNG|TÁC|XÂY|LẠM|TẬN)\s+DÙNG\b', lambda m: m.group(1) + (' DỰNG' if m.group(1).lower() == 'xây' else (' DUNG' if m.group(1).lower() == 'nội' else ' DỤNG'))),
        (r'\bxây\s+dyng\b', 'xây dựng'),
        (r'\bXây\s+dyng\b', 'Xây dựng'),

        # Cúng / Cứng -> Cũng
        (r'\b(cúng|cứng)\s+(đã|như|có|là|được|cung|góp|hỗ|phải|rất|chỉ)\b', r'cũng \2'),
        (r'\b(Cúng|Cứng)\s+(đã|như|có|là|được|cung|góp|hỗ|phải|rất|chỉ)\b', r'Cũng \2'),

        # Thiết bị
        (r'\bthi[êé]t\s+bị\b', 'thiết bị'),
        (r'\bThi[êé]t\s+bị\b', 'Thiết bị'),
        (r'\bTHI[ÊÉ]T\s+BỊ\b', 'THIẾT BỊ'),
        (r'\bthiêt\s+bi\b', 'thiết bị'),

        # Kiến trúc
        (r'\bki[eê]n\s+trúc\b', 'kiến trúc'),
        (r'\bKi[eê]n\s+trúc\b', 'Kiến trúc'),
        (r'\bKI[EÊ]N\s+TRÚC\b', 'KIẾN TRÚC'),
        (r'\bkiến\s+ưrúc\b', 'kiến trúc'),

        # Dữ liệu
        (r'\bdữ\s+li[cqeê]u\b', 'dữ liệu'),
        (r'\bDữ\s+li[cqeê]u\b', 'Dữ liệu'),

        # Nốt -> nút
        (r'\b(các|mỗi|những|giữa|trong|vùng|vào|của|cho)\s+nôt\b', r'\1 nút'),
        (r'\bnôt\s+(mạng|cảm|biến|lá|cha|con|gốc|ảo|thử|này|kia|đó)\b', r'nút \1'),
        (r'\bsố\s+lượng\s+nôt\b', 'số lượng nút'),
        (r'\bso\s+lượng\s+nôt\b', 'số lượng nút'),

        # Tiêu chuẩn / quy chuẩn
        (r'\b(tiêu|quy)\s+chu[aâ]n\b', r'\1 chuẩn'),
        (r'\b(Tiêu|Quy)\s+chu[aâ]n\b', r'\1 chuẩn'),
        (r'\bchuân\b', 'chuẩn'),
        (r'\bChuân\b', 'Chuẩn'),

        # Hình / Bảng
        (r'\bHinh\s+(\d+)', r'Hình \1'),
        (r'\bhinh\s+(\d+)', r'hình \1'),
        (r'\bB[aà]ng\s+(\d+)', r'Bảng \1'),
        (r'\bb[aà]ng\s+(\d+)', r'bảng \1'),

        # Kết nối
        (r'\bk[eê]t\s+n[oô]i\b', 'kết nối'),
        (r'\bK[eê]t\s+n[oô]i\b', 'Kết nối'),
        (r'\bkết\s+nổỉ\b', 'kết nối'),

        # So với, số lượng
        (r'\bs0\s+với\b', 'so với'),
        (r'\bS0\s+với\b', 'So với'),
        (r'\b(số|sô|s0)\s+l[uư]ợng\b', 'số lượng'),
        (r'\b(Số|Sô|S0)\s+l[uư]ợng\b', 'Số lượng'),
        (r'\btần\s+s0\b', 'tần số'),

        # Nghiên cứu
        (r'\bnghiên\s+c[iuí]u\b', 'nghiên cứu'),
        (r'\bNghiên\s+c[iuí]u\b', 'Nghiên cứu'),

        # Mô hình
        (r'\bmô\s+hinh\b', 'mô hình'),
        (r'\bMô\s+hinh\b', 'Mô hình'),

        # Thông minh
        (r'\bthông\s+m[iì]nh\b', 'thông minh'),
        (r'\bthông\s+mnh\b', 'thông minh'),

        # Phát triển
        (r'\bphát\s+tri[eê]n\b', 'phát triển'),
        (r'\bPhát\s+tri[eê]n\b', 'Phát triển'),

        # Tùy chỉnh, hoàn chỉnh
        (r'\b(tùy|tuy)\s+chính\b', 'tùy chỉnh'),
        (r'\bhoàn\s+chính\b', 'hoàn chỉnh'),

        # Hoạt động
        (r'\bhoat\s+động\b', 'hoạt động'),
        (r'\bHoat\s+động\b', 'Hoạt động'),
        (r'\bhoat\s+dộng\b', 'hoạt động'),

        # Bài tập, chương
        (r'\bBÀ[lI]\s+TẬP\b', 'BÀI TẬP'),
        (r'\bBẢI\s+TẠP\b', 'BÀI TẬP'),
        (r'\bch[uư]ong\b', 'chương'),
        (r'\bCh[uư]ong\b', 'Chương'),
        (r'\bCHƯ?ONG\b', 'CHƯƠNG'),
    ]

    for p, r in subs:
        if callable(r):
            text = re.sub(p, r, text, flags=re.IGNORECASE)
        else:
            text = re.sub(p, r, text, flags=re.IGNORECASE)

    return text

if __name__ == '__main__':
    with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
        content = f.read()

    parts = re.split(r'(^## Trang \d+\s*$)', content, flags=re.MULTILINE)
    out_parts = [parts[0]] # header
    for i in range(1, len(parts), 2):
        marker = parts[i]
        page_text = parts[i+1]
        p_num = int(re.search(r'\d+', marker).group(0))

        if p_num <= 51:
            # pages 1 to 51 are already fully verified and formatted
            out_parts.append(marker)
            out_parts.append(page_text)
        else:
            cleaned = clean_ocr_artifacts(page_text)
            out_parts.append(marker)
            out_parts.append(cleaned)

    result = ''.join(out_parts)
    with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'w', encoding='utf-8') as f:
        f.write(result)
    print('Deep clean on pages 52-214 completed successfully!')
