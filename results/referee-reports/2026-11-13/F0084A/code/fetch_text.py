#!/usr/bin/env python3
"""Download a paper into memory and keep only its extracted plain text."""
import argparse, hashlib, json, subprocess, time
from pathlib import Path
import requests
p = argparse.ArgumentParser()
p.add_argument('name')
p.add_argument('url')
a = p.parse_args()
r = requests.get(a.url, timeout=90)
r.raise_for_status()
blob = r.content
if not blob.startswith(b'%PDF'):
    raise SystemExit(f'Not a PDF: {r.status_code}, {r.headers.get("content-type")}, {blob[:80]!r}')
result = subprocess.run(['pdftotext', '-layout', '-', '-'], input=blob, capture_output=True, check=True)
out = Path('sources') / (a.name + '.txt')
out.write_bytes(result.stdout)
entry = dict(name=a.name, url=a.url, final_url=r.url, fetched=time.strftime('%Y-%m-%dT%H:%M:%S%z'), pdf_sha256=hashlib.sha256(blob).hexdigest(), text_sha256=hashlib.sha256(result.stdout).hexdigest(), pages=result.stdout.count(b'\f'), bytes=len(result.stdout))
with Path('sources/manifest.jsonl').open('a') as f:
    f.write(json.dumps(entry) + '\n')
print(json.dumps(entry))
