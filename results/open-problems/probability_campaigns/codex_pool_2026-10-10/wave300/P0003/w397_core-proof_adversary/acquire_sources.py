"""Download only the cited public sources; extract only the named relevant pages."""
import hashlib
import json
import urllib.request
from pathlib import Path

from pypdf import PdfReader

root = Path(__file__).resolve().parent / "sources"
root.mkdir(exist_ok=True)
specs = [
    ("grimmett_2205.07318v1", "https://arxiv.org/pdf/2205.07318v1", [2]),
    ("dcs_1007.0575v2", "https://arxiv.org/pdf/1007.0575v2", [1, 8, 9]),
]
receipts = []
for slug, url, pages in specs:
    path = root / (slug + ".pdf")
    try:
        data = urllib.request.urlopen(url, timeout=30).read()
        path.write_bytes(data)
        reader = PdfReader(path)
        text = "\n\n".join("PDF PAGE " + str(i + 1) + "\n" + reader.pages[i].extract_text()
                             for i in pages)
        excerpt = root / (slug + "_excerpts.txt")
        excerpt.write_text(text, encoding="utf-8")
        receipts.append({"slug": slug, "url": url, "sha256": hashlib.sha256(data).hexdigest(),
                         "pages_extracted": [i + 1 for i in pages],
                         "excerpt_path": str(excerpt), "bytes": len(data), "status": "downloaded"})
    except Exception as exc:
        receipts.append({"slug": slug, "url": url, "status": "download_unavailable",
                         "error": type(exc).__name__ + ": " + str(exc),
                         "fallback": "Primary PDF already read through the authorized web tool"})
    (root / "source_receipts.json").write_text(json.dumps(receipts, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipts[-1]), flush=True)
