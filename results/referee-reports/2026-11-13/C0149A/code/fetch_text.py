#!/usr/bin/env python3
"""Fetch a PDF into memory, save only its pdftotext output and provenance."""
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
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('name')
    args = parser.parse_args()
    if Path(args.name).name != args.name or not args.name.endswith('.txt'):
        raise SystemExit('name must be a plain .txt filename')
    req = urllib.request.Request(args.url, headers={'User-Agent': 'C0149-literature-audit/1.0'})
    with urllib.request.urlopen(req, timeout=50) as response:
        content = response.read(32 * 1024 * 1024 + 1)
        final_url = response.url
        headers = dict(response.headers)
    if len(content) > 32 * 1024 * 1024:
        raise SystemExit('source exceeds memory download limit')
    if not content.startswith(b'%PDF'):
        raise SystemExit('not a PDF response')
    result = subprocess.run(['pdftotext', '-layout', '-', '-'], input=content,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    text = result.stdout.decode('utf-8')
    target = ROOT / 'sources' / args.name
    target.write_text(text, encoding='utf-8')
    record = {'url': args.url, 'final_url': final_url,
              'retrieved': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'input_sha256': hashlib.sha256(content).hexdigest(),
              'text_sha256': hashlib.sha256(result.stdout).hexdigest(),
              'input_bytes': len(content), 'text_bytes': len(result.stdout),
              'pages_formfeed': text.count('\f'),
              'last_modified': headers.get('Last-Modified'),
              'conversion': 'pdftotext -layout - -; PDF bytes in memory only'}
    with (ROOT / 'data' / 'source_manifest.jsonl').open('a') as file:
        file.write(json.dumps(record, ensure_ascii=False) + '\n')
    print(json.dumps(record, ensure_ascii=False))

if __name__ == '__main__':
    main()
