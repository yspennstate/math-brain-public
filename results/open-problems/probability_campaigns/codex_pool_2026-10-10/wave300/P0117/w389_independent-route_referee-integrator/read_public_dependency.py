"""Read just the claimed proof's imported theorem and how it cites its source."""
import json
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent
document = fitz.open(ROOT / "public_no_bigeodesics_20260924.pdf")
saved = []
for index in (2, 4, 5, 35, 36, 37, 38):
    text = document[index].get_text()
    saved.append({"pdf_page": index + 1, "text": text})
    if index in (2, 4, 5):
        print("PDF PAGE", index + 1)
        print(text[:7000])
    else:
        lines = text.splitlines()
        for position, line in enumerate(lines):
            if "AH19" in line or "moment" in line.lower():
                print("PDF PAGE", index + 1, "\n" + "\n".join(lines[max(0, position-2):position+4]))
(ROOT / "public_dependency_pages.json").write_text(json.dumps(saved, indent=2) + "\n", encoding="utf-8")
