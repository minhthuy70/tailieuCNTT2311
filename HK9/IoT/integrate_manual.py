# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

iotmain_path = r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\IoTmain.md'
manual_path = r'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\GT_IoT_Manual.md'

with open(iotmain_path, 'r', encoding='utf-8') as f:
    iotmain_content = f.read()

with open(manual_path, 'r', encoding='utf-8') as f:
    manual_content = f.read()

# Verify that original IoTmain content is not empty
print(f"Original IoTmain length: {len(iotmain_content)} chars, {len(iotmain_content.splitlines())} lines")
print(f"Manual length: {len(manual_content)} chars, {len(manual_content.splitlines())} lines")

# Create separator
separator = "\n\n---\n\n"

# Integrated content: Verbatim IoTmain + separator + Manual content
integrated_content = iotmain_content.rstrip() + separator + manual_content.strip() + "\n"

# Write to IoTmain.md
with open(iotmain_path, 'w', encoding='utf-8') as f:
    f.write(integrated_content)

print(f"Integrated file saved. Total length: {len(integrated_content)} chars, {len(integrated_content.splitlines())} lines")

# Verification: check that original IoTmain is completely preserved at the beginning
with open(iotmain_path, 'r', encoding='utf-8') as f:
    saved_content = f.read()

assert saved_content.startswith(iotmain_content.rstrip()), "Error: original IoTmain was not preserved verbatim!"
assert manual_content.strip() in saved_content, "Error: manual content was not integrated!"

print("VERIFICATION SUCCESSFUL: Original IoTmain.md was preserved verbatim, and GT_IoT_Manual.md was successfully integrated!")
