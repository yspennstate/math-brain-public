#!/usr/bin/env python3
"""Fetch a paper into RAM, retain only extracted text and provenance."""
import io, json, hashlib, sys, urllib.request
from pathlib import Path
from datetime import datetime, timezone
from pypdf import PdfReader
url, name = sys.argv[1:]
r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=90)
b = r.read(45_000_000)
assert b.startswith(b'%PDF'), (r.status, r.headers.get('Content-Type'), b[:80])
pages=PdfReader(io.BytesIO(b)).pages
out='SOURCE: '+url+'\nEXTRACTED UTC: '+datetime.now(timezone.utc).isoformat()+'\nPDF SHA256 (not retained): '+hashlib.sha256(b).hexdigest()+'\n'
for i,page in enumerate(pages,1):
    out+='\n\n========== PDF PAGE '+str(i)+' ==========\n\n'+(page.extract_text() or '')
path=Path('sources')/(name+'.txt');path.write_text(out)
print(path, len(pages), 'pages',len(out),'characters')
