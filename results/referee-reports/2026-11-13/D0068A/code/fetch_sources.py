"""Fetch papers into memory and save page-labelled plain text only."""
import hashlib
import io
import json
import os
from pathlib import Path
import urllib.request

os.environ.setdefault('OMP_NUM_THREADS', '1')
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ('grimmett_li_2017', 'https://www.statslab.cam.ac.uk/~grg1000/papers/rev-final11.pdf'),
    ('lacoin_planar_2014', 'https://arxiv.org/pdf/1203.6051'),
    ('lacoin_highdim_2014', 'https://arxiv.org/pdf/1212.4641'),
]

def fetch(name, url):
    req = urllib.request.Request(url, headers={'User-Agent': 'D0068 literature audit'})
    with urllib.request.urlopen(req, timeout=90) as r:
        payload = r.read()
    reader = PdfReader(io.BytesIO(payload))
    blocks = [f'SOURCE URL: {url}\nPDF SHA256 (bytes never saved): {hashlib.sha256(payload).hexdigest()}\n']
    for i, page in enumerate(reader.pages, 1):
        blocks.append(f'\n\n===== PDF PAGE {i} =====\n\n{page.extract_text()}')
    target = ROOT / 'sources' / f'{name}.txt'
    target.parent.mkdir(exist_ok=True)
    target.write_text(''.join(blocks))
    print(json.dumps({'file': str(target.relative_to(ROOT)), 'pages': len(reader.pages), 'url': url}), flush=True)

if __name__ == '__main__':
    for name, url in SOURCES:
        fetch(name, url)
