"""Fetch papers into memory; retain only page-labelled plain text and metadata.

Run from the workspace root. No PDF is ever written to disk.
"""
import hashlib
import fcntl
import io
import json
import os
import pathlib
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import requests
from pypdf import PdfReader

ROOT = pathlib.Path(__file__).resolve().parents[1]


def fetch(key, url):
    out = ROOT / "sources"
    out.mkdir(exist_ok=True)
    (ROOT / "data").mkdir(exist_ok=True)
    manifest_path = ROOT / "data" / "source_manifest.json"
    response = requests.get(url, timeout=90)
    response.raise_for_status()
    raw = response.content
    if not raw.startswith(b"%PDF"):
        raise ValueError(f"Not a PDF: {url}, {response.headers.get('Content-Type')}")
    reader = PdfReader(io.BytesIO(raw))
    pages = [page.extract_text(extraction_mode="layout") for page in reader.pages]
    target = out / (key + ".txt")
    target.write_text("SOURCE: " + url + "\n" + "\n".join(
        f"\n========== PDF PAGE {i} ==========\n{text}\n"
        for i, text in enumerate(pages, 1)), encoding="utf-8")
    record = {"url": url, "final_url": response.url,
                     "accessed_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                     "pdf_sha256": hashlib.sha256(raw).hexdigest(),
                     "text_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                     "pages": len(pages), "pdf_retained": False}
    with (ROOT / 'data' / '.source_manifest.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
        manifest[key] = record
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(key, len(pages), "pages", len(raw), "bytes converted in memory", flush=True)


if __name__ == "__main__":
    fetch(sys.argv[1], sys.argv[2])
