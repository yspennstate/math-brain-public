#!/usr/bin/env python3
"""Extract remote papers to plain text. PDF bytes stay in memory, never on disk."""
import os
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
import datetime, hashlib, json, pathlib, subprocess, sys, urllib.request
root = pathlib.Path(__file__).resolve().parents[1]
url, name = sys.argv[1:]
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research source verification)'})
with urllib.request.urlopen(req, timeout=55) as response:
    raw = response.read(25_000_001)
    content_type = response.headers.get('Content-Type','')
if len(raw)>25_000_000:
    raise ValueError('source exceeds 25 MB limit')
meta = {'url':url, 'retrieved':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'sha256':hashlib.sha256(raw).hexdigest(), 'bytes':len(raw),'content_type':content_type}
if raw.startswith(b'%PDF'):
    extracted = subprocess.run(['pdftotext','-layout','-','-'], input=raw, capture_output=True,check=True).stdout.decode()
    pages=extracted.split('\f')
    if not pages[-1].strip(): pages.pop()
    body=''.join(f'\n===== PDF PAGE {i} =====\n\n{page}' for i,page in enumerate(pages,1))
    meta['pages']=len(pages)
else:
    body=raw.decode('utf-8')
(root/'sources'/name).write_text(json.dumps(meta,ensure_ascii=False)+'\n'+body)
with (root/'data'/'fetch_manifest.jsonl').open('a') as f: f.write(json.dumps(meta|{'file':name})+'\n')
print(json.dumps(meta|{'file':name}))
