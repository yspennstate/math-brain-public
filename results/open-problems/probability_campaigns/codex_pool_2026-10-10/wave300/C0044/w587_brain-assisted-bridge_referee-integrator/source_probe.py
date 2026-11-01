"""Fetch only the named public C0044 manuscript for scoped source inspection."""

import hashlib
import importlib.util
from pathlib import Path
from urllib.request import urlopen

URL = (
    "https://raw.githubusercontent.com/openai/math/main/preprints/"
    "A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf"
)
DEST = Path(__file__).with_name("strict_ellipticity_2026.pdf")

if not DEST.exists():
    with urlopen(URL, timeout=45) as response:
        DEST.write_bytes(response.read(2_000_000))
print("pdf_bytes", DEST.stat().st_size)
print("pdf_sha256", hashlib.sha256(DEST.read_bytes()).hexdigest())
for name in ("fitz", "pypdf"):
    print("module", name, importlib.util.find_spec(name) is not None)

if importlib.util.find_spec("fitz") is not None:
    import fitz

    doc = fitz.open(DEST)
    print("pages", len(doc))
    for i in range(min(len(doc), 5)):
        page = doc[i].get_text()
        print(f"PAGE {i + 1}")
        print(page[:7000])
