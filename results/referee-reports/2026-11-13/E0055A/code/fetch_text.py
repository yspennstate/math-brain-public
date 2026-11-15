#!/usr/bin/env python3
"""Fetch a PDF into memory and save only page-labelled plain text; no PDF file."""
import argparse, hashlib, io, json, os, resource, urllib.request
from pathlib import Path
from datetime import datetime, timezone
from pypdf import PdfReader

resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
p = argparse.ArgumentParser()
p.add_argument('name'); p.add_argument('url')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
req = urllib.request.Request(a.url, headers={'User-Agent': 'Mozilla/5.0 (academic source verification)'})
with urllib.request.urlopen(req, timeout=90) as resp:
    blob = resp.read(35_000_000)
    final_url = resp.url
if not blob.startswith(b'%PDF'): raise ValueError('not a PDF')
reader = PdfReader(io.BytesIO(blob))
parts = [f'SOURCE URL: {a.url}\nFINAL URL: {final_url}\nPDF SHA256: {hashlib.sha256(blob).hexdigest()}\nPDF PAGES: {len(reader.pages)}\nExtraction: pypdf, one-based PDF page markers; printed page numbers remain in text.\n']
for i, page in enumerate(reader.pages, 1):
    parts.append(f'\n\n===== PDF PAGE {i} =====\n\n'+(page.extract_text(extraction_mode='layout') or ''))
(root/'sources'/f'{a.name}.txt').write_text('\n'.join(parts))
meta={'name':a.name,'url':a.url,'final_url':final_url,'pdf_sha256':hashlib.sha256(blob).hexdigest(),'pdf_pages':len(reader.pages),'fetched_utc':datetime.now(timezone.utc).isoformat()}
(root/'data'/f'{a.name}_provenance.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta))
