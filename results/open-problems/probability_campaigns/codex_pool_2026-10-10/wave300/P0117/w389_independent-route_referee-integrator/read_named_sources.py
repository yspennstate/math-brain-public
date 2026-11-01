"""Extract only the named survey page and the new manuscript's key headers."""
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def extract_survey():
    import fitz
    document = fitz.open(r"~/Downloads/Probability_1000_20h_20260906/sources/fpp_survey_2015/source.pdf")
    # The ledger cites physical PDF page 98. Also check the adjacent page in case
    # the ledger counted its title page differently; keep only matching pages.
    saved = []
    for index in (96, 97, 98):
        value = document[index].get_text()
        if "Question 31" in value or "bigeodesic" in value.lower():
            saved.append({"pdf_page": index + 1, "text": value})
    (ROOT / "survey_page_excerpt.json").write_text(json.dumps(saved, indent=2) + "\n", encoding="utf-8")
    for page in saved:
        lines = page["text"].splitlines()
        for index, line in enumerate(lines):
            if "Question 31" in line:
                print("SURVEY PDF PAGE", page["pdf_page"])
                print("\n".join(lines[max(0, index-6):index+9]))


def extract_new_manuscript():
    import fitz
    base = "https://raw.githubusercontent.com/openai/math/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/"
    target = ROOT / "public_no_bigeodesics_20260924.pdf"
    if not target.exists():
        raw = urllib.request.urlopen(base + "main.pdf", timeout=25).read(2_000_000)
        if not raw.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        target.write_bytes(raw)
    document = fitz.open(target)
    matches = []
    for index in range(len(document)):
        lines = document[index].get_text().splitlines()
        for position, line in enumerate(lines):
            if line.startswith(("Theorem 1", "Proposition 1", "Lemma 1", "Lemma 2", "Theorem 2")):
                matches.append({"pdf_page": index + 1,
                                "excerpt": "\n".join(lines[position:position+13])})
    result = {"url": base + "main.pdf", "pdf_pages": len(document),
              "first_page": document[0].get_text(), "key_headers": matches,
              "status": "CLAIMED PROOF; NOT MATHEMATICALLY CERTIFIED"}
    (ROOT / "public_manuscript_extract.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("MANUSCRIPT FIRST PAGE\n", result["first_page"][:4200])
    print("KEY HEADERS\n", json.dumps(matches, ensure_ascii=False)[:8500])


if __name__ == "__main__":
    for operation in (extract_survey, extract_new_manuscript):
        try:
            operation()
        except Exception as error:
            name = operation.__name__ + "_error.json"
            (ROOT / name).write_text(json.dumps({"error": str(error), "operation": operation.__name__}), encoding="utf-8")
            print(operation.__name__, type(error).__name__, str(error))
