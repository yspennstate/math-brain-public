#!/usr/bin/env python3
"""Fetch a PDF into memory and persist only its plain-text extraction."""
import argparse
import hashlib
import io
import json
import os
import subprocess
import urllib.request
from pathlib import Path

os.environ.update({key: '1' for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')})
p = argparse.ArgumentParser()
p.add_argument('url')
p.add_argument('output')
a = p.parse_args()
req = urllib.request.Request(a.url, headers={'User-Agent': 'I0006 private research text extraction'})
with urllib.request.urlopen(req, timeout=90) as response:
    pdf = response.read(40_000_000)
if not pdf.startswith(b'%PDF'):
    raise RuntimeError('Response is not a PDF')
r = subprocess.run(['pdftotext', '-layout', '-', '-'], input=pdf, capture_output=True, check=True)
text = r.stdout.decode('utf-8')
Path(a.output).write_text(text)
print(json.dumps({'url': a.url, 'output': a.output, 'pdf_bytes_in_memory': len(pdf), 'pdf_sha256': hashlib.sha256(pdf).hexdigest(), 'text_pages': len(text.split('\f'))-1}))
