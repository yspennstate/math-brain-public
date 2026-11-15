"""Fetch mathematical sources as plain text; PDFs never touch the filesystem."""
import io
import os
import hashlib
import json
from pathlib import Path
os.environ.update({k: '1' for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')})
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'sources'
OUT.mkdir(exist_ok=True)

def fetch(name, url):
    target = OUT / (name + '.txt')
    if target.exists():
        print('exists', name, flush=True)
        return
    response = requests.get(url, timeout=90)
    response.raise_for_status()
    data = response.content
    if not data.startswith(b'%PDF'):
        raise ValueError((url, response.headers.get('Content-Type'), data[:80]))
    reader = PdfReader(io.BytesIO(data))
    body = '\n\n'.join(f'=== PDF PAGE {i+1} ===\n' + (page.extract_text(extraction_mode='layout') or '') for i, page in enumerate(reader.pages))
    body = ''.join(ch for ch in body if ch in '\n\t' or ord(ch) >= 32)
    header = f'URL: {url}\nRetrieved UTC: {__import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat()}\nPDF SHA256 (in-memory download): {hashlib.sha256(data).hexdigest()}\nPages: {len(reader.pages)}\nExtraction: pypdf layout; no PDF retained\n\n'
    target.write_text(header + body)
    print(name, len(reader.pages), len(body), flush=True)

if __name__ == '__main__':
    print('inherited nice', os.getpriority(os.PRIO_PROCESS, 0), flush=True)
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    for name, url in [
        ('survey_1611.00411', 'https://arxiv.org/pdf/1611.00411'),
        ('LPS_1309.3267v4', 'https://arxiv.org/pdf/1309.3267v4'),
        ('LPS_1309.3267v1', 'https://arxiv.org/pdf/1309.3267v1'),
        ('LPS_1208.4839', 'https://arxiv.org/pdf/1208.4839'),
        ('LPS_Annals_published', 'https://annals.math.princeton.edu/wp-content/uploads/annals-v186-n1-p01-p.pdf'),
    ]:
        try:
            fetch(name, url)
        except Exception as exc:
            print('FAILED', name, repr(exc), flush=True)
