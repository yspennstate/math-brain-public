#!/usr/bin/env python3
"""Fetch a paper as text, converting PDF bytes in memory; never save PDFs."""
import argparse, datetime, hashlib, io, json, pathlib, subprocess, urllib.request
p=argparse.ArgumentParser(); p.add_argument('url'); p.add_argument('output'); a=p.parse_args()
req=urllib.request.Request(a.url,headers={'User-Agent':'D0028 research (plain-text archive)'})
with urllib.request.urlopen(req, timeout=90) as r:
    raw=r.read(); mime=r.headers.get('Content-Type',''); final=r.url
if raw.startswith(b'%PDF'):
    text=subprocess.run(['pdftotext','-layout','-','-'],input=raw,stdout=subprocess.PIPE,check=True).stdout.decode('utf-8')
else:
    text=raw.decode('utf-8')
out=pathlib.Path(a.output); out.write_text(text)
meta={'url':a.url,'final_url':final,'accessed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mime':mime,'input_sha256':hashlib.sha256(raw).hexdigest(),'text_sha256':hashlib.sha256(text.encode()).hexdigest(),'bytes_input':len(raw),'chars_text':len(text),'conversion':'pdftotext -layout from stdin' if raw.startswith(b'%PDF') else 'UTF-8 decode'}
out.with_suffix(out.suffix+'.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
