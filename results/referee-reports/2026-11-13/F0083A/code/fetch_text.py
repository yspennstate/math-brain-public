"""Fetch PDF into memory, convert through pipes, retain only UTF-8 text."""
import argparse, datetime, hashlib, json, pathlib, subprocess, urllib.request
p=argparse.ArgumentParser(); p.add_argument('url'); p.add_argument('name'); a=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]
req=urllib.request.Request(a.url,headers={'User-Agent':'F0083 mathematical literature verification'})
with urllib.request.urlopen(req,timeout=60) as r: raw=r.read(); url=r.url
if not raw.startswith(b'%PDF'): raise ValueError('Not a PDF')
s=subprocess.run(['pdftotext','-layout','-','-'],input=raw,stdout=subprocess.PIPE,check=True)
out=root/'sources'/(a.name+'.txt'); out.write_bytes(s.stdout)
rec={'requested_url':a.url,'final_url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pdf_sha256':hashlib.sha256(raw).hexdigest(),'text_sha256':hashlib.sha256(s.stdout).hexdigest(),'file':str(out.relative_to(root)),'pdf_stored':False}
with (root/'data'/'source_manifest.jsonl').open('a') as f: f.write(json.dumps(rec)+'\n')
print(json.dumps(rec))
