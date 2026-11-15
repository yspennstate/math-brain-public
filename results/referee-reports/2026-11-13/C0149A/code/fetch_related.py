#!/usr/bin/env python3
"""Fetch the requested related literature sequentially; retain text only."""
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
 ('https://rdlyons.pages.iu.edu/pdf/factor.pdf', 'lyons_nazarov_2010.txt'),
 ('https://arxiv.org/pdf/1105.3200', 'abert_elek_1105.3200.txt'),
 ('https://arxiv.org/pdf/1204.0449', 'elek_1204.0449.txt'),
 ('https://arxiv.org/pdf/0711.3808', 'schramm_0711.3808.txt'),
 ('https://arxiv.org/pdf/math/0701925', 'abert_jaikin_nikolov_0701925.txt'),
 ('https://arxiv.org/pdf/1810.11015', 'hutchcroft_pete_1810.11015.txt'),
 ('https://arxiv.org/pdf/1901.03963', 'kun_thom_1901.03963.txt'),
 ('https://arxiv.org/pdf/1608.02242', 'alekseev_finn_sell_1608.02242.txt'),
 ('https://arxiv.org/pdf/2406.06741', 'alekseev_thom_2406.06741.txt'),
 ('https://arxiv.org/pdf/2511.16515', 'drigalla_2511.16515.txt'),
 ('https://arxiv.org/pdf/2512.15494', 'alekseev_thom_2512.15494.txt'),
]
for url,name in SOURCES:
    if (ROOT/'sources'/name).exists():
        continue
    r = subprocess.run([sys.executable, str(ROOT/'code'/'fetch_text.py'),url,name],cwd=ROOT)
    if r.returncode:
        print('FAILED',url, flush=True)
