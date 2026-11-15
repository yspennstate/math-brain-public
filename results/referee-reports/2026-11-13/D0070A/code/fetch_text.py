#!/usr/bin/env python3
"""Fetch a paper into memory and retain only pdftotext output."""
import hashlib, json, pathlib, subprocess, sys, urllib.request, datetime
root = pathlib.Path(__file__).resolve().parents[1]
url, name = sys.argv[1:]
with urllib.request.urlopen(url, timeout=90) as r:
    raw = r.read(25_000_000)
if not raw.startswith(b'%PDF'):
    raise RuntimeError('Response is not PDF')
p = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
path = root/'sources'/name
path.write_bytes(p.stdout)
record = {'url':url,'text':name,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pdf_sha256_not_retained':hashlib.sha256(raw).hexdigest(),'text_sha256':hashlib.sha256(p.stdout).hexdigest(),'pages':p.stdout.count(b'\x0c')}
with (root/'data'/'sources.jsonl').open('a') as f: f.write(json.dumps(record)+'\n')
print(json.dumps(record))
