#!/usr/bin/env python3
"""Fetch a paper into memory and retain only pdftotext output, never a PDF file."""
import os
os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
import argparse, datetime, hashlib, json, pathlib, subprocess, urllib.request
p=argparse.ArgumentParser()
p.add_argument('url'); p.add_argument('name'); a=p.parse_args()
root=pathlib.Path(__file__).resolve().parent.parent
req=urllib.request.Request(a.url,headers={'User-Agent':'Mozilla/5.0 (research text extraction)'})
with urllib.request.urlopen(req, timeout=90) as response:
    body=response.read(40*1024*1024); final=response.url
if not body.startswith(b'%PDF'): raise SystemExit('Not a PDF: '+repr(body[:80]))
r=subprocess.run(['pdftotext','-layout','-','-'],input=body,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
text=r.stdout.decode('utf-8')
out=root/'sources'/(a.name+'.txt'); out.write_text(text)
record={'url':a.url,'final_url':final,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'text_file':out.name,'text_sha256':hashlib.sha256(r.stdout).hexdigest(),'pdf_bytes_in_memory_only':len(body),'pages_formfeed':text.count('\f')}
with (root/'data'/'source_manifest.jsonl').open('a') as f: f.write(json.dumps(record)+'\n')
print(json.dumps(record))
