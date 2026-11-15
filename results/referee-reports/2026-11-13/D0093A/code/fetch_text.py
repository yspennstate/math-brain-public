#!/usr/bin/env python3
"""Download PDF into memory, extract page-separated plain text, save no PDF."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "D0093 literature check (plain text extraction)"})
    with urllib.request.urlopen(req, timeout=90) as r:
        blob = r.read()
    if not blob.startswith(b"%PDF"):
        raise ValueError(f"Not PDF: {url}, prefix {blob[:80]!r}")
    proc = subprocess.run(["pdftotext", "-layout", "-", "-"], input=blob, capture_output=True, check=True)
    output = ROOT / 'sources' / (name + '.txt')
    output.write_bytes(proc.stdout)
    metadata = {"file": str(output.relative_to(ROOT)), "url": url,
                "downloaded_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "pdf_bytes_processed_in_memory": len(blob), "pdf_sha256": hashlib.sha256(blob).hexdigest(),
                "text_sha256": hashlib.sha256(proc.stdout).hexdigest(),
                "pdf_pages": proc.stdout.count(b'\x0c'), "extractor": "pdftotext -layout - -"}
    with (ROOT/'sources'/'manifest.jsonl').open('a') as f:
        f.write(json.dumps(metadata)+'\n')
    print(json.dumps(metadata))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('name')
    p.add_argument('url')
    a = p.parse_args()
    fetch(a.name, a.url)
