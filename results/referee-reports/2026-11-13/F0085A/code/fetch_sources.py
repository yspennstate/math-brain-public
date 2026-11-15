"""Fetch PDFs into RAM, save extracted plain text only. No PDF files are written."""
import os
for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[k] = "1"
import argparse
from io import BytesIO
from pathlib import Path
import hashlib
import json
import urllib.request
import subprocess
from datetime import datetime, timezone
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]

def fetch(name, url, engine="pypdf"):
    request = urllib.request.Request(url, headers={"User-Agent": "F0085 literature audit (plain text extraction)"})
    with urllib.request.urlopen(request, timeout=90) as response:
        payload = response.read(30_000_000)
    if not payload.startswith(b"%PDF"):
        raise ValueError(f"Not a PDF: {url}: {payload[:80]!r}")
    reader = PdfReader(BytesIO(payload))
    if engine == "pdftotext":
        converted = subprocess.run(["pdftotext", "-layout", "-", "-"], input=payload,
                                   capture_output=True, check=True)
        pages = converted.stdout.decode("utf-8").split("\f")
        if not pages[-1].strip():
            pages.pop()
        assert len(pages) == len(reader.pages)
    else:
        pages = [page.extract_text(extraction_mode="layout") for page in reader.pages]
    # Some PDF fonts decode a glyph as NUL; retain only plain-text controls.
    pages = ["".join(c for c in page if ord(c) >= 32 or c in "\n\r\t") for page in pages]
    result = f"SOURCE: {url}\nPDF SHA256: {hashlib.sha256(payload).hexdigest()}\nPDF PAGES: {len(pages)}\nEXTRACTION ENGINE: {engine}\nExtracted {datetime.now(timezone.utc).isoformat()}\n\n"
    result += "\n\n".join(f"===== PDF PAGE {i} =====\n{text}" for i, text in enumerate(pages, 1))
    target = ROOT / "sources" / f"{name}.txt"
    target.write_text(result)
    print(json.dumps({"file": str(target.relative_to(ROOT)), "pages": len(pages), "pdf_bytes_RAM_only": len(payload), "text_chars": len(result)}), flush=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("url")
    parser.add_argument("--engine", choices=["pypdf", "pdftotext"], default="pypdf")
    args = parser.parse_args()
    try:
        os.nice(10)
    except OSError:
        pass
    fetch(args.name, args.url, args.engine)
