#!/usr/bin/env python3
"""Fetch a named primary-source URL as text, converting PDF bytes in memory."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.request

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
root = Path(__file__).resolve().parents[1]
assert Path.cwd().resolve() == root
name, url = sys.argv[1:]
assert Path(name).name == name and name.endswith('.txt')
with urllib.request.urlopen(url, timeout=60) as response:
    body = response.read()
    final_url = response.geturl()
digest = hashlib.sha256(body).hexdigest()
if body.startswith(b'%PDF'):
    body = subprocess.run(['pdftotext', '-layout', '-', '-'], input=body,
                          capture_output=True, check=True).stdout
else:
    body = body.decode('utf-8', errors='replace').encode('utf-8')
(root / 'sources' / name).write_bytes(body)
record = dict(name=name, url=final_url, response_sha256=digest,
              text_sha256=hashlib.sha256(body).hexdigest(),
              retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
with (root / 'data/source_manifest.jsonl').open('a') as output:
    output.write(json.dumps(record) + '\n')
print(json.dumps(record))
