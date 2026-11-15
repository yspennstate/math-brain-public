#!/usr/bin/env python3
"""Fetch scholarly PDFs in memory; retain only page-marked plain text."""
import argparse, io, json, pathlib, urllib.request, hashlib, datetime
from pypdf import PdfReader
p=argparse.ArgumentParser(); p.add_argument('name'); p.add_argument('url'); a=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]
req=urllib.request.Request(a.url,headers={'User-Agent':'Research audit plain-text extraction contact-free'})
with urllib.request.urlopen(req,timeout=90) as r: raw=r.read()
if not raw.startswith(b'%PDF'): raise RuntimeError('Response is not PDF')
reader=PdfReader(io.BytesIO(raw))
text='Source URL: '+a.url+'\nExtracted UTC: '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'\nPDF SHA256 (not retained): '+hashlib.sha256(raw).hexdigest()+'\nPages: '+str(len(reader.pages))+'\n'
for i,page in enumerate(reader.pages,1): text+='\n\n===== PDF PAGE '+str(i)+' =====\n\n'+(page.extract_text(extraction_mode='layout') or '').replace('\x00','')
(root/'sources'/f'{a.name}.txt').write_text(text)
print(json.dumps({'name':a.name,'pages':len(reader.pages),'characters':len(text),'url':a.url}))
