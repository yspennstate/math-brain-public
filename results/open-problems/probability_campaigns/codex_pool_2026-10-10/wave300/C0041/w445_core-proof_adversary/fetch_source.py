"""Fetch only the two named public C0041 source files into this worker folder."""
from pathlib import Path
import importlib.util
import json
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "sources"
OUT.mkdir(exist_ok=True)
base = "https://raw.githubusercontent.com/openai/math/main/"
items = [
    ("preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf", "recent_ballisticity.pdf"),
]
receipts = []
for rel, name in items:
    url = base + rel
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            raw = response.read(2_000_001)
        if len(raw) > 2_000_000:
            raise ValueError("named-source size gate exceeded")
        (OUT / name).write_bytes(raw)
        if name.endswith(".pdf"):
            import pymupdf
            with pymupdf.open(stream=raw, filetype="pdf") as document:
                if len(document) > 70:
                    raise ValueError("named-source page gate exceeded")
                with (OUT / "recent_ballisticity.txt").open("w", encoding="utf-8") as target:
                    for page in document:
                        target.write(f"\n[PDF page {page.number + 1}]\n")
                        target.write(page.get_text())
        receipts.append({"url": url, "local": str(OUT / name), "bytes": len(raw), "status": "downloaded"})
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        receipts.append({"url": url, "status": "unavailable", "reason": str(exc)})
(OUT / "pdf_receipts.json").write_text(json.dumps(receipts, indent=2), encoding="utf-8")
print(json.dumps(receipts, indent=2))
