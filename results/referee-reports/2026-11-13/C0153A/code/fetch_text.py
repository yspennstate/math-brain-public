"""Fetch a paper into memory and save only its plain-text extraction.

Usage (from a nice-10 shell): python3 code/fetch_text.py NAME URL
No PDF file, image, or scan is written, including temporary files.
"""
import datetime
import hashlib
import io
import json
import os
import re
from pathlib import Path
import sys

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
import requests
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
name, url = sys.argv[1:]
if not name.replace("_", "").replace("-", "").isalnum():
    raise SystemExit("name must be a filename stem")
response = requests.get(url, timeout=(20, 180))
response.raise_for_status()
raw = response.content
if not raw.startswith(b"%PDF-"):
    raise SystemExit(f"URL returned a non-PDF response: {response.url}")
if len(raw) > 100_000_000:
    raise SystemExit("response too large")
reader = PdfReader(io.BytesIO(raw))
out = root / "sources" / (name + ".txt")
out.parent.mkdir(exist_ok=True)
with out.open("w") as stream:
    stream.write(f"SOURCE URL: {url}\nFINAL URL: {response.url}\n")
    stream.write(f"RETRIEVED UTC: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\n")
    stream.write(f"PDF RESPONSE SHA256 (not retained): {hashlib.sha256(raw).hexdigest()}\n")
    stream.write(f"PDF PAGES: {len(reader.pages)}\n")
    for i, page in enumerate(reader.pages, 1):
        stream.write(f"\n\f\n===== PDF PAGE {i} =====\n")
        extracted = page.extract_text(extraction_mode="layout")
        stream.write(re.sub(r"[\x00-\x08\x0b\x0e-\x1f]", "", extracted) + "\n")
print(json.dumps({"path": str(out), "pages": len(reader.pages), "bytes": out.stat().st_size}))
