#!/usr/bin/env python3
"""Save the archive's existing OCR text; do not fetch its page images."""
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
import urllib.request

class Extract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, s):
        self.parts.append(s)

root = Path(__file__).resolve().parents[1]
texts, urls = [], []
for number in range(93, 100):
    url = f'https://gdz.sub.uni-goettingen.de/fulltext/PPN235181684_0303/{number:08d}?_format=xml'
    with urllib.request.urlopen(url, timeout=30) as r:
        raw = r.read().decode('utf-8')
    parser = Extract()
    parser.feed(raw)
    text = re.sub(r'\s+', ' ', ' '.join(parser.parts)).strip()
    texts.append(f'PRINTED PAGE {number-6}; archive OCR, formulas may be corrupted\n\n{text}\n\f')
    urls.append(url)
path = root / 'sources' / 'cranston_lejan_1995.txt'
path.write_text('\n'.join(texts))
path.with_suffix('.metadata.txt').write_text(json.dumps(dict(
    urls=urls, retrieved=datetime.now(timezone.utc).isoformat(),
    method='Archive OCR HTML text only; no images or PDF fetched',
    text_sha256=hashlib.sha256(path.read_bytes()).hexdigest(), pages=7), indent=2)+'\n')
print('Saved seven pages of archive OCR')
