"""Download a paper into memory and retain only its extracted plain text.

Usage: python3 code/fetch_text.py NAME URL
PDF bytes never touch disk. Form-feed boundaries preserve PDF page numbering.
"""
import io
import json
import sys
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import requests
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
name, url = sys.argv[1:]
r = requests.get(url, timeout=90)
r.raise_for_status()
raw = r.content
if not raw.startswith(b"%PDF"):
    raise ValueError(f"Expected PDF response, got {r.headers.get('Content-Type')}")
reader = PdfReader(io.BytesIO(raw))
def plain(s):
    # Some embedded math fonts extract as control codes. Keep text files text;
    # literal replacement characters flag unmapped glyphs rather than hiding them.
    return ''.join(c if ord(c)>=32 or c in '\n\t' else '\ufffd' for c in s)

pages = [f"[PDF PAGE {i+1}]\n" + plain(p.extract_text()) for i,p in enumerate(reader.pages)]
(root / "sources").mkdir(exist_ok=True)
(root / "sources" / (name + ".txt")).write_text("\n\f\n".join(pages))
meta = dict(name=name, url=url, final_url=r.url, pages=len(pages),
            sha256_pdf_in_memory=hashlib.sha256(raw).hexdigest(),
            downloaded_utc=datetime.now(timezone.utc).isoformat())
with (root / "sources" / "manifest.jsonl").open("a") as f:
    f.write(json.dumps(meta) + "\n")
print(json.dumps(meta))
