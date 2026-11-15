#!/usr/bin/env python3
"""Fetch PDFs into memory and persist only pdftotext output (form feeds retain pages)."""
import os, sys, subprocess, urllib.request, hashlib, json, datetime
from pathlib import Path

root=Path(__file__).resolve().parents[1]
name,url=sys.argv[1:]
req=urllib.request.Request(url,headers={'User-Agent':'D0025 research source verification'})
with urllib.request.urlopen(req,timeout=90) as r: raw=r.read()
if not raw.startswith(b'%PDF'): raise ValueError('not PDF')
p=subprocess.run(['pdftotext','-layout','-','-'],input=raw,capture_output=True,check=True)
(root/'sources'/f'{name}.txt').write_bytes(p.stdout)
record={'name':name,'url':url,'retrieved':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pdf_sha256':hashlib.sha256(raw).hexdigest(),'text_sha256':hashlib.sha256(p.stdout).hexdigest(),'pages':p.stdout.count(b'\x0c')}
with (root/'sources'/'manifest.jsonl').open('a') as f: f.write(json.dumps(record)+'\n')
print(json.dumps(record))
