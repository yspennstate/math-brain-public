"""Extract only requested pages from a downloaded primary source."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
target = root / sys.argv[1]
try:
    import pymupdf as fitz
except ImportError:
    import fitz
document = fitz.open(target)
print(f"PDF pages: {len(document)}")
for value in sys.argv[2:]:
    index = int(value)
    content = document[index].get_text()
    output = target.with_suffix(f".page{index+1}.txt")
    output.write_text(content, encoding="utf-8")
    print(f"PAGE {index+1}\n{content[:10500]}")
