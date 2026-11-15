"""Download papers into memory, save only pdftotext output and provenance."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

def fetch(name, url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (mathematics research)'})
    with urllib.request.urlopen(req, timeout=90) as response:
        body = response.read(32_000_000)
        final_url = response.url
    if body.startswith(b'%PDF'):
        proc = subprocess.run(['pdftotext', '-layout', '-', '-'], input=body, capture_output=True, check=True)
        output = proc.stdout.decode('utf-8')
        if len(output.strip()) < 100:
            raise ValueError('PDF has no useful extractable text; no PDF retained: ' + url)
        kind = 'pdf converted in memory by pdftotext -layout'
    else:
        output = body.decode('utf-8')
        if '<html' in output[:1000].lower() or '<!doctype html' in output[:1000].lower():
            raise ValueError('HTML returned instead of source text: ' + url)
        if len(output.strip()) < 100:
            raise ValueError('Response is too short to be a source paper: ' + url)
        kind = 'text'
    dest = ROOT / 'sources' / (name + '.txt')
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(output)
    record = dict(name=name, url=url, final_url=final_url, retrieved=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  source_sha256=hashlib.sha256(body).hexdigest(), text_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),
                  conversion=kind, pages=output.count('\f'))
    with (ROOT / 'sources' / 'manifest.jsonl').open('a') as stream:
        stream.write(json.dumps(record) + '\n')
    print(json.dumps(record), flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('url')
    args = parser.parse_args()
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
    try:
        fetch(args.name, args.url)
    except Exception as exc:
        import sys
        print(type(exc).__name__ + ': ' + str(exc), file=sys.stderr)
        sys.exit(1)
