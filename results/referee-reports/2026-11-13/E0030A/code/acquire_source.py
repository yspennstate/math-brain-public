#!/usr/bin/env python3
"""Download a PDF into memory and retain only its page-labelled plain text."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import urllib.request

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('name')
    args = parser.parse_args()
    # launch.sh starts this session at nice 10, inherited by children.
    # The sandbox blocks setpriority (even a further priority reduction).
    root = Path(__file__).resolve().parents[1]
    dest = root / 'sources' / (args.name + '.txt')
    dest.parent.mkdir(exist_ok=True)
    request = urllib.request.Request(args.url, headers={'User-Agent': 'E0030 literature audit'})
    with urllib.request.urlopen(request, timeout=90) as response:
        raw = response.read(30_000_000)
        actual_url = response.url
    if not raw.startswith(b'%PDF'):
        raise ValueError('Not a PDF; refusing to mislabel response')
    # pdftotext takes the PDF on stdin. No PDF is written, even temporarily.
    converted = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    pages = converted.stdout.decode('utf-8').split('\f')
    if pages and not pages[-1].strip():
        pages.pop()
    header = {'url': args.url, 'resolved_url': actual_url,
              'pdf_sha256': hashlib.sha256(raw).hexdigest(), 'pdf_bytes': len(raw),
              'pages': len(pages), 'extraction': 'pdftotext -layout from stdin'}
    dest.write_text(json.dumps(header, indent=2) + '\n\n' + '\n\n'.join(
        f'===== PDF PAGE {i+1} =====\n\n{page}' for i,page in enumerate(pages)), encoding='utf-8')
    print(json.dumps({'file': str(dest.relative_to(root)), **header}))

if __name__ == '__main__':
    main()
