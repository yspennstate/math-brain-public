"""Fetch source PDFs into memory and retain only extracted UTF-8 plain text."""
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import time
import urllib.request

os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
out = root / "sources"
out.mkdir(exist_ok=True)
for spec in sys.argv[1:]:
    name, url = spec.split("=", 1)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Independent academic referee/1.0"})
        with urllib.request.urlopen(req, timeout=40) as response:
            raw = response.read(25_000_000)
        reader = PdfReader(io.BytesIO(raw))
        pages = []
        for i, page in enumerate(reader.pages, 1):
            s = page.extract_text() or ""
            s = "".join(c if c in "\n\t" or ord(c) >= 32 else " " for c in s)
            pages.append(f"\n\n=== PDF PAGE {i} ===\n\n{s}")
        body = f"Source: {url}\nFetched: {time.strftime('%Y-%m-%dT%H:%M:%S%z')}\nPDF SHA256 (bytes never saved): {hashlib.sha256(raw).hexdigest()}\n" + "".join(pages)
        target = out / (name + ".txt")
        target.write_text(body, encoding="utf-8")
        item = {"name": name, "url": url, "pages": len(pages), "text_sha256": hashlib.sha256(body.encode()).hexdigest(), "pdf_sha256": hashlib.sha256(raw).hexdigest()}
        print(json.dumps(item), flush=True)
        with (out / "manifest.txt").open("a") as f:
            f.write(json.dumps(item) + "\n")
    except Exception as exc:
        print(json.dumps({"name": name, "url": url, "error": str(exc)}), flush=True)
