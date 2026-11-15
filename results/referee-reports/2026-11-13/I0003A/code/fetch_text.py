#!/usr/bin/env python3
"""Fetch papers to plain text; PDF bytes exist only in memory."""
import argparse, datetime, hashlib, io, json, os, pathlib, urllib.request
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
from pypdf import PdfReader
p=argparse.ArgumentParser(); p.add_argument('name'); p.add_argument('url'); a=p.parse_args()
req=urllib.request.Request(a.url,headers={'User-Agent':'Mozilla/5.0 (mathematics literature study)'})
with urllib.request.urlopen(req,timeout=90) as r:
    raw=r.read(); final=r.url; ctype=r.headers.get('Content-Type','')
if raw.startswith(b'%PDF'):
    reader=PdfReader(io.BytesIO(raw)); parts=[]
    for i,page in enumerate(reader.pages,1):
        parts.append(f'\n\n===== PDF PAGE {i} =====\n\n'+(page.extract_text() or ''))
    content=''.join(parts)
else:
    content=raw.decode('utf-8',errors='replace')
content=''.join(c for c in content if ord(c)>=32 or c in '\n\r\t')
path=pathlib.Path('sources')/(a.name+'.txt'); path.write_text(content)
record={'name':a.name,'url':a.url,'final_url':final,'content_type':ctype,'source_sha256':hashlib.sha256(raw).hexdigest(),'text_sha256':hashlib.sha256(content.encode()).hexdigest(),'bytes':len(raw),'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
with open('data/source_manifest.jsonl','a') as f: f.write(json.dumps(record)+'\n')
print(json.dumps(record))
