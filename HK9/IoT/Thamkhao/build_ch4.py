# -*- coding: utf-8 -*-
import sys, os, re

# Let's inspect OCR text for chapter 4 to build clean text
def get_ocr(p):
    with open(rf'd:\CNTT2311\tailieuCNTT2311\HK9\IoT\Thamkhao\ocr_results\page_{p:03d}.txt', 'r', encoding='utf-8') as f:
        return f.read().strip()

print('OCR loader ready')
