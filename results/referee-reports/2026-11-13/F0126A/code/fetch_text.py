"""Fetch PDFs into memory and retain only extracted plain text, with page markers."""
import argparse
import hashlib
import io
import json
import os
import re
from html import unescape
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
os.environ.setdefault("OMP_NUM_THREADS", "1")
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("slug")
parser.add_argument("url")
args = parser.parse_args()
response = requests.get(args.url, timeout=60, headers={"User-Agent": "F0126 literature research"})
response.raise_for_status()
raw = response.content
out = ["SOURCE URL: " + args.url, "RESPONSE SHA256 (bytes never saved): " + hashlib.sha256(raw).hexdigest()]
if raw.startswith(b"%PDF"):
    reader = PdfReader(io.BytesIO(raw))
    pages = len(reader.pages)
    for i, page in enumerate(reader.pages, 1):
        out.extend([f"\n===== PDF PAGE {i} =====\n", page.extract_text() or ""])
else:
    pages = None
    html = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", "", response.text, flags=re.I | re.S)
    html = re.sub(r"</?(p|div|h[1-6]|li|br|tr|section|article)\b[^>]*>", "\n", html, flags=re.I)
    out.append(unescape(re.sub(r"<[^>]*>", "", html)))
dest = ROOT / "sources" / (args.slug + ".txt")
dest.parent.mkdir(exist_ok=True)
clean = "".join(c if ord(c) >= 32 or c in "\n\t\r\f" else f"[U+{ord(c):04X}]" for c in "\n".join(out))
dest.write_text(clean, encoding="utf-8")
record = {"slug": args.slug, "url": args.url, "pages": pages, "response_sha256": hashlib.sha256(raw).hexdigest(), "text_sha256": hashlib.sha256(dest.read_bytes()).hexdigest()}
(ROOT / "data").mkdir(exist_ok=True)
with (ROOT / "data" / "source_manifest.jsonl").open("a") as f:
    f.write(json.dumps(record) + "\n")
print(json.dumps(record))
