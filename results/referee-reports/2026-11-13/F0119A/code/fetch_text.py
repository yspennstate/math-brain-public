#!/usr/bin/env python3
"""Fetch a PDF into RAM, extract text with page breaks, retain text only.

Run under nice 10. No PDF or page image is written, even temporarily.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request


def main():
    # The managed shell already runs at nice 10. Avoid macOS nice's failed
    # relative-priority change inside the sandbox; check the inherited value.
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
    p = argparse.ArgumentParser()
    p.add_argument('url')
    p.add_argument('name')
    a = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    if Path(a.name).name != a.name:
        p.error('name must be a basename')
    req = urllib.request.Request(a.url, headers={'User-Agent': 'F0119-literature-audit/1.0'})
    with urllib.request.urlopen(req, timeout=90) as r:
        payload = r.read(50_000_001)
        final_url = r.url
    if len(payload) > 50_000_000:
        raise ValueError('download exceeds 50 MB cap')
    if not payload.startswith(b'%PDF'):
        raise ValueError('response is not a PDF')
    env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
               VECLIB_MAXIMUM_THREADS='1', MKL_NUM_THREADS='1')
    proc = subprocess.run(['pdftotext', '-layout', '-', '-'], input=payload,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=True, env=env)
    pages = proc.stdout.decode('utf-8').split('\f')
    if not pages[-1].strip():
        pages.pop()
    out = '\n'.join(f'\n===== PDF PAGE {i} =====\n{page}'
                    for i, page in enumerate(pages, 1))
    dest = root / 'sources' / (a.name + '.txt')
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(out)
    metadata = {'requested_url': a.url, 'final_url': final_url,
                'accessed': datetime.datetime.now().astimezone().isoformat(),
                'pdf_sha256': hashlib.sha256(payload).hexdigest(),
                'text_sha256': hashlib.sha256(out.encode()).hexdigest(),
                'pdf_bytes_processed_in_memory': len(payload),
                'pages': len(pages), 'extractor': 'pdftotext -layout - -'}
    metadata['nice'] = os.getpriority(os.PRIO_PROCESS, 0)
    meta_dir = root / 'data'
    meta_dir.mkdir(exist_ok=True)
    (meta_dir / (a.name + '.metadata.json')).write_text(json.dumps(metadata, indent=2) + '\n')
    print(json.dumps({'saved': str(dest), 'pages': len(pages),
                      'sha256': metadata['pdf_sha256']}))


if __name__ == '__main__':
    main()
