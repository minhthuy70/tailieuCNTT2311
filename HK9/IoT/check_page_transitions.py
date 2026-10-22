# -*- coding: utf-8 -*-
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md', 'r', encoding='utf-8') as f:
    raw = f.read()

lines = raw.splitlines()
transitions = []

for i, line in enumerate(lines):
    if line.startswith('## Trang '):
        # find non-empty line before
        prev_idx = i - 1
        while prev_idx >= 0 and not lines[prev_idx].strip():
            prev_idx -= 1
        # find non-empty line after
        next_idx = i + 1
        while next_idx < len(lines) and not lines[next_idx].strip():
            next_idx += 1
        if prev_idx >= 0 and next_idx < len(lines):
            prev_l = lines[prev_idx].strip()
            next_l = lines[next_idx].strip()
            # check if previous line ends mid-sentence
            if prev_l and prev_l[-1] not in ('.', '!', '?', ':', ';', '"', '”', '`', '#', '|', '-', '>'):
                transitions.append((line, prev_l, next_l))

print(f"Total split-sentence transitions across page breaks: {len(transitions)}")
for t in transitions[:15]:
    print(f"[{t[0]}]")
    print(f"   PREV: {t[1]}")
    print(f"   NEXT: {t[2]}")

print("\n--- CHECKING REPEATED WORDS ACROSS PAGE BREAKS ---")
for i, line in enumerate(lines):
    if line.startswith('## Trang '):
        prev_idx = i - 1
        while prev_idx >= 0 and not lines[prev_idx].strip():
            prev_idx -= 1
        next_idx = i + 1
        while next_idx < len(lines) and not lines[next_idx].strip():
            next_idx += 1
        if prev_idx >= 0 and next_idx < len(lines):
            prev_words = lines[prev_idx].strip().split()
            next_words = lines[next_idx].strip().split()
            if prev_words and next_words:
                pw = re.sub(r'[^\w]', '', prev_words[-1]).lower()
                nw = re.sub(r'[^\w]', '', next_words[0]).lower()
                if pw == nw and len(pw) > 1:
                    print(f"{line}: repeated '{pw}'")
                    print(f"   PREV: {lines[prev_idx].strip()[-50:]}")
                    print(f"   NEXT: {lines[next_idx].strip()[:50]}")

