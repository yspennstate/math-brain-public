#!/usr/bin/env python3
"""Fetch a paper, converting PDF bytes in memory; retain plain text only."""
import argparse
import hashlib
import io
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
import requests
from pypdf import PdfReader

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('name')
    ap.add_argument('url')
    args = ap.parse_args()
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
    root = Path(__file__).resolve().parents[1]
    response = requests.get(args.url, timeout=90)
    response.raise_for_status()
    raw = response.content
    if not raw.startswith(b'%PDF'):
        raise ValueError('Expected PDF bytes; nothing saved')
    reader = PdfReader(io.BytesIO(raw))
    # Poppler's text converter reads stdin and writes stdout: no PDF on disk.
    converted = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    pages = converted.stdout.decode('utf-8').split('\f')
    if pages and not pages[-1].strip():
        pages.pop()
    assert len(pages) == len(reader.pages), (len(pages), len(reader.pages))
    out = root / 'sources' / (args.name + '.txt')
    out.write_text('\n'.join(f'\n===== PDF PAGE {i} =====\n\n{p}\n' for i,p in enumerate(pages,1)))
    metadata = {'file':out.name, 'url':args.url, 'resolved_url':response.url,
                'retrieved_utc':datetime.now(timezone.utc).isoformat(),
                'pdf_sha256_in_memory':hashlib.sha256(raw).hexdigest(),
                'text_sha256':hashlib.sha256(out.read_bytes()).hexdigest(), 'pages':len(pages)}
    with (root/'data'/'source_manifest.jsonl').open('a') as f:
        f.write(json.dumps(metadata)+'\n')
    print(json.dumps(metadata))

if __name__ == '__main__':
    main()
