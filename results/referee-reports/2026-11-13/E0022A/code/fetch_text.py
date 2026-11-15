#!/usr/bin/env python3
"""Fetch a paper in memory; save only page-marked plain text, never a PDF."""
import argparse, hashlib, io, json, os, resource, urllib.request
from datetime import datetime, timezone
from pathlib import Path
from pypdf import PdfReader
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
p = argparse.ArgumentParser()
p.add_argument("url")
p.add_argument("stem")
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
r = urllib.request.urlopen(urllib.request.Request(a.url, headers={"User-Agent":"E0022 research text extraction"}), timeout=60)
b = r.read(25 * 1024**2 + 1)
if len(b) > 25 * 1024**2:
    raise SystemExit("Source exceeds the 25 MiB input cap")
if not b.startswith(b"%PDF-"):
    raise SystemExit("Server did not return a PDF; no source file written")
reader = PdfReader(io.BytesIO(b))
parts = [f"SOURCE: {a.url}\nSHA256 (PDF, not retained): {hashlib.sha256(b).hexdigest()}\n"]
for i, page in enumerate(reader.pages, 1):
    parts.append(f"\n===== PDF PAGE {i} =====\n" + (page.extract_text(extraction_mode="layout") or ""))
out = root / "sources" / (a.stem + ".txt")
body = "\n".join(parts)
body = "".join(c for c in body if c in "\n\r\t" or ord(c) >= 32)
out.write_text(body)
record = {"url":a.url,"file":str(out.relative_to(root)),"pages":len(reader.pages),"pdf_sha256":hashlib.sha256(b).hexdigest(),"retrieved_utc":datetime.now(timezone.utc).isoformat(),"pdf_retained":False}
with (root / "data" / "sources.jsonl").open("a") as f: f.write(json.dumps(record) + "\n")
print(json.dumps(record))
