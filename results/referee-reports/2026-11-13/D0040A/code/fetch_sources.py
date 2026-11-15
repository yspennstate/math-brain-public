#!/usr/bin/env python3
"""Fetch primary-source PDFs into memory; retain only extracted plain text.
No PDF or page image is written to disk. Page markers use 1-based PDF pages.
Usage: python3 code/fetch_sources.py NAME URL [NAME URL ...]
"""
import sys, hashlib, json, datetime, os, subprocess
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import requests
from pathlib import Path
root = Path(__file__).resolve().parents[1]
for name, url in zip(sys.argv[1::2], sys.argv[2::2]):
    response = requests.get(url, timeout=90)
    response.raise_for_status()
    content = response.content
    extracted = subprocess.run(["pdftotext", "-layout", "-", "-"], input=content, capture_output=True, check=True).stdout.decode("utf-8")
    pages = extracted.split("\f")
    if not pages[-1].strip():
        pages.pop()
    chunks = [f'SOURCE: {url}\nRETRIEVED: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\nPDF SHA256 (not retained): {hashlib.sha256(content).hexdigest()}\nPDF PAGES: {len(pages)}\n']
    for i, page in enumerate(pages, 1):
        chunks.append(f'\n\n===== PDF PAGE {i} =====\n\n' + page)
    out = root / 'sources' / (name + '.txt')
    out.write_text('\n'.join(chunks))
    print(json.dumps({'file':str(out.relative_to(root)), 'pages':len(pages), 'bytes_text':out.stat().st_size}))
