"""Fetch primary sources independently; retain only text and provenance.

PDF bytes exist only in memory and in pdftotext's stdin pipe.
Run with a source name and URL, optionally several name/URL pairs.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import ssl
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
try:
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
except (AttributeError, PermissionError):
    pass

def fetch(name, url):
    assert '/' not in name
    record = {'name': name, 'url': url, 'time_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Independent-mathematical-referee/1.0'})
        # Optional only for public legacy mathematical archives with broken chains.
        insecure = os.environ.get('FETCH_PUBLIC_LEGACY_INSECURE') == '1'
        record['tls_verified'] = not insecure
        context = ssl._create_unverified_context() if insecure else None
        with urllib.request.urlopen(req, timeout=50, context=context) as res:
            blob = res.read(25_000_001)
            record['resolved_url'] = res.url
        assert len(blob) <= 25_000_000
        assert blob.startswith(b'%PDF'), blob[:100]
        out = subprocess.run(['pdftotext', '-layout', '-', '-'], input=blob, capture_output=True, check=True)
        pages = out.stdout.decode('utf-8').split('\f')
        if not pages[-1].strip():
            pages.pop()
        text = '\n'.join(f'\n===== PDF PAGE {i} =====\n{p}' for i, p in enumerate(pages, 1))
        preface = f"URL: {url}\nRetrieved: {record['time_utc']}\nExtraction: pdftotext -layout, PDF streamed through memory\n\n"
        path = ROOT / 'sources' / (name + '.txt')
        path.parent.mkdir(exist_ok=True)
        path.write_text(preface + text)
        record.update(pdf_sha256=hashlib.sha256(blob).hexdigest(), text_sha256=hashlib.sha256(path.read_bytes()).hexdigest(), pages=len(pages), bytes=len(blob), success=True)
    except Exception as exc:
        record.update(success=False, error=repr(exc))
    (ROOT / 'data').mkdir(exist_ok=True)
    with (ROOT / 'data' / 'retrievals.jsonl').open('a') as f:
        f.write(json.dumps(record) + '\n')
    print(json.dumps(record), flush=True)

if __name__ == '__main__':
    assert len(sys.argv) % 2 == 1
    for name, url in zip(sys.argv[1::2], sys.argv[2::2]):
        fetch(name, url)
