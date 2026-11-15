"""Download a paper into memory and save only extracted text in sources/."""
import argparse
import hashlib
import io
import json
import pathlib
import shutil
import subprocess
import urllib.request
from datetime import datetime, timezone
from pypdf import PdfReader

parser = argparse.ArgumentParser()
parser.add_argument("url")
parser.add_argument("name")
args = parser.parse_args()
root = pathlib.Path(__file__).resolve().parents[1]
req = urllib.request.Request(args.url, headers={"User-Agent": "I0005-literature-audit/1.0"})
with urllib.request.urlopen(req, timeout=90) as response:
    body = response.read(30_000_001)
if len(body) > 30_000_000 or not body.startswith(b"%PDF"):
    raise ValueError("Expected PDF bytes, at most 30 MB")
reader = PdfReader(io.BytesIO(body))
if shutil.which("pdftotext"):
    converted = subprocess.run(["pdftotext", "-layout", "-", "-"], input=body,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    extracted = converted.stdout.decode("utf-8")
    method = "pdftotext -layout via stdin/stdout; PDF bytes never written to disk"
else:
    extracted = "\f".join(page.extract_text(extraction_mode="layout") for page in reader.pages)
    method = "pypdf layout extraction; PDF bytes never written to disk"
# PDF font mappings can produce NUL and other non-text controls.
extracted = "".join(c for c in extracted if ord(c) >= 32 or c in "\n\t\f")
target = root / "sources" / (args.name + ".txt")
target.write_text(extracted, encoding="utf-8")
metadata = {"url": args.url, "retrieved_utc": datetime.now(timezone.utc).isoformat(),
            "pdf_sha256": hashlib.sha256(body).hexdigest(), "pages": len(reader.pages),
            "text_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
            "method": method}
(root / "sources" / (args.name + "-provenance.txt")).write_text(
    json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
print(json.dumps(metadata))
