#!/usr/bin/env python3
"""Retrieve a paper into RAM and persist only its pdftotext output and provenance."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('name')
    p.add_argument('url')
    a = p.parse_args()
    req = urllib.request.Request(a.url, headers={'User-Agent': 'F0129 literature research (text extraction)'})
    with urllib.request.urlopen(req, timeout=75) as response:
        blob = response.read(32 * 1024 * 1024)
        final_url = response.url
    if not blob.startswith(b'%PDF'):
        raise ValueError(f'Not PDF: {blob[:60]!r}')
    out = subprocess.run(['pdftotext', '-layout', '-', '-'], input=blob,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    path = ROOT / 'sources' / (a.name + '.txt')
    path.write_bytes(out.stdout)
    metadata = dict(url=a.url, final_url=final_url,
                    retrieved=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    pdf_sha256_in_memory=hashlib.sha256(blob).hexdigest(),
                    text_sha256=hashlib.sha256(out.stdout).hexdigest(),
                    pages=out.stdout.count(b'\f'), bytes=len(out.stdout),
                    method='PDF held only in RAM; pdftotext -layout - -; form feeds preserved')
    path.with_suffix('.metadata.txt').write_text(json.dumps(metadata, indent=2)+'\n')
    print(a.name, metadata['pages'], metadata['bytes'], final_url)

if __name__ == '__main__':
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 10:
        os.nice(10 - priority)
    main()
