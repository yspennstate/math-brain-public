"""Fetch a source, converting PDF bytes in memory; never write PDF files.

Usage: python3 code/get_source.py NAME URL [first_pdf_page last_pdf_page]
The optional interval limits *saved* text, retaining page indices for citation.
"""
import datetime
import hashlib
import io
import json
from pathlib import Path
import sys
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]

def main():
    name, url = sys.argv[1:3]
    assert name.replace('_', '').replace('-', '').isalnum()
    folder = ROOT / 'sources'
    folder.mkdir(exist_ok=True)
    response = requests.get(url, timeout=90)
    response.raise_for_status()
    content = response.content
    meta = dict(name=name, requested_url=url, final_url=response.url,
                accessed=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                downloaded_bytes=len(content), sha256_download=hashlib.sha256(content).hexdigest())
    if content.startswith(b'%PDF'):
        reader = PdfReader(io.BytesIO(content))
        meta['pdf_pages'] = len(reader.pages)
        if len(sys.argv) == 5 and sys.argv[3].startswith('find:'):
            needle = sys.argv[3][5:]
            lo = next(i+1 for i, page in enumerate(reader.pages) if needle in page.extract_text())
            hi = lo + int(sys.argv[4]) - 1
        else:
            lo, hi = (map(int, sys.argv[3:5]) if len(sys.argv) == 5 else (1, len(reader.pages)))
        meta['saved_pdf_pages'] = [lo, hi]
        text = '\n'.join(f'\n===== PDF PAGE {i+1} =====\n' + reader.pages[i].extract_text()
                         for i in range(lo-1, min(hi, len(reader.pages))))
    else:
        text = response.text
        meta['content_type'] = response.headers.get('content-type')
    dest = folder / (name + '.txt')
    dest.write_text(json.dumps(meta, ensure_ascii=False, indent=2)+'\n\n'+text.replace('\x00', ''))
    with (ROOT / 'LOG.md').open('a') as log:
        log.write(f"- {meta['accessed']}: saved {dest.relative_to(ROOT)} from {url}; PDF bytes never written.\n")
    print(json.dumps(meta))

if __name__ == '__main__':
    main()
