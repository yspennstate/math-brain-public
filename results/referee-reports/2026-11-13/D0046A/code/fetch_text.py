#!/usr/bin/env python3
"""Fetch a paper PDF into memory and retain only pdftotext output, with form feeds."""
import argparse, hashlib, json, pathlib, subprocess, urllib.request
p = argparse.ArgumentParser()
p.add_argument('url'); p.add_argument('name')
a = p.parse_args()
root = pathlib.Path(__file__).resolve().parents[1]
with urllib.request.urlopen(a.url, timeout=90) as r:
    blob = r.read()
if not blob.startswith(b'%PDF'):
    raise SystemExit('Response is not a PDF')
t = subprocess.run(['pdftotext','-layout','-','-'], input=blob, capture_output=True, check=True).stdout
out = root / 'sources' / (a.name+'.txt')
out.write_bytes(t)
meta = {'url':a.url,'pdf_bytes_transient':len(blob),'pdf_sha256':hashlib.sha256(blob).hexdigest(), 'text_sha256':hashlib.sha256(t).hexdigest(),'pages':t.count(b'\x0c'),'pdf_retained':False}
(root/'sources'/(a.name+'.metadata.txt')).write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps({'file':str(out),**meta}))
