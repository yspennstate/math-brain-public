"""Download into memory, extract text, and retain text only. No PDF files."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]

def fetch(name, url):
    response = requests.get(url, timeout=90)
    response.raise_for_status()
    raw = response.content
    if not raw.startswith(b'%PDF'):
        raise ValueError(f'Not a PDF: {url}: {raw[:80]!r}')
    reader = PdfReader(io.BytesIO(raw))
    pages = [f'\n\n===== PDF PAGE {i} =====\n\n' + ''.join(
                ch for ch in (p.extract_text() or '') if ord(ch) >= 32 or ch in '\n\t\r')
             for i, p in enumerate(reader.pages, 1)]
    dest = ROOT / 'sources' / f'{name}.txt'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text('URL: '+url+'\nSHA256 of transient source bytes: '+hashlib.sha256(raw).hexdigest()+'\n'+''.join(pages))
    meta = dict(name=name, url=url, pages=len(pages), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    with (ROOT/'sources'/'manifest.txt').open('a') as f:
        f.write(json.dumps(meta)+'\n')
    print(json.dumps(meta), flush=True)

if __name__ == '__main__':
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
    p=argparse.ArgumentParser()
    p.add_argument('name'); p.add_argument('url')
    a=p.parse_args(); fetch(a.name,a.url)
