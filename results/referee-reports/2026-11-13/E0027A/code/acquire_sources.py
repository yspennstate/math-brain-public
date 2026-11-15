#!/usr/bin/env python3
"""Download public papers into memory; save page-delimited plain text only."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import urllib.request
from datetime import datetime, timezone


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('arxiv_id')
    parser.add_argument('stem')
    parser.add_argument('--url', help='Use another primary-source PDF URL instead of arXiv')
    args = parser.parse_args()
    # The task launcher already uses nice 10. Do not stack os.nice():
    # macOS can reject it when the inherited value is already at its limit.
    root = Path(__file__).resolve().parents[1]
    sources = root / 'sources'
    data = root / 'data'
    sources.mkdir(exist_ok=True)
    data.mkdir(exist_ok=True)
    url = args.url or ('https://arxiv.org/pdf/' + args.arxiv_id)
    req = urllib.request.Request(url, headers={'User-Agent': 'E0027-literature-audit/1.0'})
    with urllib.request.urlopen(req, timeout=90) as response:
        raw = response.read(20_000_001)
    if len(raw) > 20_000_000 or not raw.startswith(b'%PDF'):
        raise ValueError('Unexpected or oversized response')
    # pdftotext accepts stdin and stdout. Neither PDF nor page images touch disk.
    proc = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    pages = proc.stdout.decode('utf-8').split('\f')
    if not pages[-1].strip():
        pages.pop()
    text = '\n'.join(f'===== PDF PAGE {i} =====\n{p}'
                     for i, p in enumerate(pages, 1))
    destination = sources / (args.stem + '.txt')
    destination.write_text(text, encoding='utf-8')
    metadata = {
        'arxiv_id': None if args.url else args.arxiv_id, 'url': url,
        'retrieved_utc': datetime.now(timezone.utc).isoformat(),
        'response_sha256': hashlib.sha256(raw).hexdigest(),
        'response_bytes': len(raw), 'pdf_pages': len(pages),
        'text_file': str(destination.relative_to(root)),
        'text_sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
        'method': 'PDF in memory -> pdftotext -layout stdin/stdout; text only persisted',
    }
    (data / (args.stem + '_provenance.json')).write_text(
        json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(metadata, indent=2))


if __name__ == '__main__':
    main()
