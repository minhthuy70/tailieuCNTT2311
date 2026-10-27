import re, sys, os

def fix_vietnamese_ocr(text):
    # Specific two-word / three-word phrases first
    replacements_exact = [
        ('quân trọng trọng', 'quan trọng trong'),
        ('quân trọng', 'quan trọng'),
        ('liên quân', 'liên quan'),
        ('tổng quân', 'tổng quan'),
        ('quân trắc', 'quan trắc'),
        ('quân sát', 'quan sát'),
        ('quân hệ', 'quan hệ'),
        ('quân tâm', 'quan tâm'),
        ('quân điểm', 'quan điểm'),
        ('khách quân', 'khách quan'),
        ('chủ quân', 'chủ quan'),
        ('cứng cấp', 'cung cấp'),
        ('mạng lại', 'mang lại'),
        ('nctwork', 'network'),
        ('phẩm Eềm', 'phần mềm'),
        ('dám mây', 'đám mây'),
        ('cam biến', 'cảm biến'),
        ('thông kê', 'thống kê'),
        ('trúc tiếp', 'trực tiếp'),
        ('lang phí', 'lãng phí'),
        ('nhân Iực', 'nhân lực'),
        ('loai thiết bị', 'loại thiết bị'),
        ('chất Juợng', 'chất lượng'),
        ('giá đình', 'gia đình'),
        ('giá chủ', 'gia chủ'),
        ('tham giá', 'tham gia'),
        ('quốc giá', 'quốc gia'),
        ('tuy chính', 'tùy chỉnh'),
        ('tùy chính', 'tùy chỉnh'),
        ('hoàn chính', 'hoàn chỉnh'),
        ('di dộng', 'di động'),
        ('da phương tiện', 'đa phương tiện'),
        ('da phương tỉện', 'đa phương tiện'),
        ('dường truyền', 'đường truyền'),
        ('dối với', 'đối với'),
        ('dặc trưng', 'đặc trưng'),
        ('dịnh tuyến', 'định tuyến'),
        ('dịnh hướng', 'định hướng'),
        ('dối tượng', 'đối tượng'),
        ('dộ trễ', 'độ trễ'),
        ('dầu vào', 'đầu vào'),
        ('dầu ra', 'đầu ra'),
        ('dầy đủ', 'đầy đủ'),
        ('dơn giản', 'đơn giản'),
        ('dịa chỉ', 'địa chỉ'),
        ('dồng thời', 'đồng thời'),
        ('dời sống', 'đời sống'),
        ('dô thị', 'đô thị'),
        ('dầu tiên', 'đầu tiên'),
        ('dáp ứng', 'đáp ứng'),
        ('dại học', 'đại học'),
        ('dảm bảo', 'đảm bảo'),
        ('dồ vật', 'đồ vật'),
        ('dưa ra', 'đưa ra'),
        ('diều khiển', 'điều khiển'),
        ('diều chỉnh', 'điều chỉnh'),
        ('dổi mới', 'đổi mới'),
        ('dạt được', 'đạt được'),
        ('tương lại', 'tương lai'),
        ('thực tế ảo VRIAR', 'thực tế ảo VR/AR'),
        ('VR/AR xe thông minh', 'VR/AR, xe thông minh'),
        ('Smart Cities)', '(Smart Cities)'),
        ('thông minh Smart', 'thông minh (Smart'),
        ('thông minhldô thị', 'thông minh/đô thị'),
        ('Smart Home_', 'Smart Home)'),
        ('Smart City _', 'Smart City)'),
        ('Smart Agriculture _', 'Smart Agriculture)'),
    ]

    for old, new in replacements_exact:
        # replace case-insensitively while preserving capitalization
        pattern = re.compile(re.escape(old), re.IGNORECASE)
        def make_rep(match, rep=new):
            m = match.group(0)
            if m.isupper():
                return rep.upper()
            elif m[0].isupper():
                return rep.capitalize()
            return rep
        text = pattern.sub(make_rep, text)

    # Word boundary replacements for d -> đ
    d_words = {
        'dược': 'được',
        'dóng': 'đóng',
        'dến': 'đến',
        'dó': 'đó',
        'dể': 'để',
        'dã': 'đã',
        'dạt': 'đạt',
        'dặt': 'đặt',
        'dổi': 'đổi',
        'diểm': 'điểm',
        'dường': 'đường',
        'dầy': 'đầy',
        'dầu': 'đầu',
        'dưa': 'đưa',
        'dơn': 'đơn',
        'dịnh': 'định',
        'dặc': 'đặc',
        'dối': 'đối',
        'dộ': 'độ',
        'dồng': 'đồng',
    }
    for old_w, new_w in d_words.items():
        pattern = re.compile(r'\b' + re.escape(old_w) + r'\b', re.IGNORECASE)
        def make_rep(match, rep=new_w):
            m = match.group(0)
            if m.isupper():
                return rep.upper()
            elif m[0].isupper():
                return rep.capitalize()
            return rep
        text = pattern.sub(make_rep, text)

    # Replace 'trọng' with 'trong' except when valid
    valid_phrases = [
        'quan trọng', 'trọng số', 'trọng lượng', 'trọng tâm', 'chú trọng',
        'tôn trọng', 'coi trọng', 'thận trọng', 'trân trọng', 'bảo trọng',
        'trọng điểm', 'trọng yếu', 'trọng trường', 'trọng tài'
    ]

    def rep_trong(m):
        start = max(0, m.start() - 25)
        end = min(len(text), m.end() + 25)
        context = text[start:end].lower()
        for vp in valid_phrases:
            if vp in context:
                return m.group(0) # keep as is
        # otherwise replace with trong
        val = m.group(0)
        if val.isupper():
            return 'TRONG'
        elif val[0].isupper():
            return 'Trong'
        return 'trong'

    text = re.sub(r'\btrọng\b', rep_trong, text, flags=re.IGNORECASE)
    return text

if __name__ == '__main__':
    with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by pages
    parts = re.split(r'(^## Trang \d+\s*$)', content, flags=re.MULTILINE)
    # parts[0] is header, parts[1] is '## Trang 1', parts[2] is page 1 content, etc.

    out_parts = [parts[0]] # header
    for i in range(1, len(parts), 2):
        marker = parts[i]
        page_text = parts[i+1]
        p_num = int(re.search(r'\d+', marker).group(0))

        if p_num <= 20:
            # pages 1 to 20 already thoroughly verified and formatted
            out_parts.append(marker)
            out_parts.append(page_text)
        else:
            fixed_page = fix_vietnamese_ocr(page_text)
            out_parts.append(marker)
            out_parts.append(fixed_page)

    result = ''.join(out_parts)
    with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'w', encoding='utf-8') as f:
        f.write(result)
    print('Global systematic cleanup finished successfully!')
