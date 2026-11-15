"""Fetch a PDF in RAM, write only pdftotext output; retain provenance as text."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
import requests

# The agent launcher already runs at nice 10. Avoid changing priority in sandbox.
parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('url')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
r = requests.get(args.url, timeout=120)
r.raise_for_status()
assert r.content.startswith(b'%PDF'), (r.status_code, r.headers.get('Content-Type'))
result = subprocess.run(['pdftotext', '-layout', '-', '-'], input=r.content,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
target = root / 'sources' / (args.name + '.txt')
target.write_bytes(result.stdout)
record = dict(name=args.name, url=args.url, final_url=r.url,
              retrieved_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
              pdf_sha256=hashlib.sha256(r.content).hexdigest(),
              text_sha256=hashlib.sha256(result.stdout).hexdigest(),
              pages=result.stdout.count(b'\f'), text_bytes=len(result.stdout))
with (root / 'sources' / 'manifest.jsonl.txt').open('a') as f:
    f.write(json.dumps(record) + '\n')
print(json.dumps(record))
