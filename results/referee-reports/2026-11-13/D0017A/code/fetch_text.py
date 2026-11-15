#!/usr/bin/env python3
"""Fetch a public paper in memory; retain only page-separated plain text."""
import argparse, hashlib, json, os, pathlib, subprocess, urllib.request
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
p=argparse.ArgumentParser(); p.add_argument('url'); p.add_argument('name'); a=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]
req=urllib.request.Request(a.url,headers={'User-Agent':'D0017-literature-check/1.0'})
with urllib.request.urlopen(req,timeout=90) as response:
    raw=response.read(30_000_000)
    ctype=response.headers.get('Content-Type','')
if raw.startswith(b'%PDF'):
    proc=subprocess.run(['pdftotext','-layout','-','-'],input=raw,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
    pages=proc.stdout.decode('utf-8').split('\f')
    txt=''.join(f'\n===== PDF PAGE {i} =====\n\n{page}' for i,page in enumerate(pages,1) if page.strip())
else:
    txt=raw.decode('utf-8',errors='replace')
out=root/'sources'/a.name
out.write_text(txt)
meta={'url':a.url,'sha256_download':hashlib.sha256(raw).hexdigest(),'download_bytes':len(raw),'content_type':ctype,'retained':str(out.relative_to(root)),'pdf_saved':False}
with (root/'sources'/'manifest.jsonl').open('a') as f: f.write(json.dumps(meta)+'\n')
print(json.dumps(meta))
