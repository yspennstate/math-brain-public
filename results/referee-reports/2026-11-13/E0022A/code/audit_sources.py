#!/usr/bin/env python3
"""Check key source locators through an independent PDF text extractor."""
import hashlib
import json
import re
import shutil
import subprocess
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parents[1]
url = "https://arxiv.org/pdf/1908.06825v1"
with urllib.request.urlopen(url, timeout=60) as response:
    pdf_in_memory = response.read(25 * 1024**2)
records = [json.loads(line) for line in (root / "data" / "sources.jsonl").read_text().splitlines()]
record = next(x for x in records if x["file"] == "sources/hunts_hypothesis_survey_2019.txt")
assert hashlib.sha256(pdf_in_memory).hexdigest() == record["pdf_sha256"]
command = [shutil.which("pdftotext"), "-f", "15", "-l", "18", "-layout", "-", "-"]
result = subprocess.run(command, input=pdf_in_memory, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, check=True, timeout=30)
pages = result.stdout.decode("utf-8").split("\f")
expected = {15: ["Question 1", "Question 2", "Question 4"],
            16: ["Example 3.5", "Theorem 3.6"],
            17: ["Theorem 3.7"], 18: ["Remark 3.8"]}
out = ["SOURCE: " + url, "SECOND EXTRACTOR: pdftotext -layout (in-memory PDF input)"]
for number in range(15, 19):
    text = "".join(c for c in pages[number - 15] if c in "\n\r\t" or ord(c) >= 32)
    normalized = re.sub(r"\s+", " ", text)
    for marker in expected[number]:
        assert marker in normalized, (number, marker)
    out.append(f"\n===== PDF PAGE {number} =====\n{text}")
(root / "sources" / "survey_second_extraction_15_18.txt").write_text("\n".join(out))
question_page = re.sub(r"\s+", " ", pages[0])
question = question_page.split("Question 1.", 1)[1].split("Question 2.", 1)[0].strip()

controls = {}
for path in (root / "sources").iterdir():
    assert path.suffix == ".txt", path
    data = path.read_bytes()
    assert not data.startswith(b"%PDF-"), path
    text = data.decode("utf-8")
    bad = [ord(c) for c in text if ord(c) < 32 and c not in "\n\r\t"]
    assert not bad, (path, bad[:10])
    controls[path.name] = "UTF-8 text, no prohibited control bytes"
for path in root.rglob("*"):
    assert path.suffix.lower() not in (".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff"), path

report = {"survey_pdf_hash_matches": True, "independent_extractor": command[0],
          "key_page_markers_verified": expected,
          "question_from_independent_extraction": question,
          "source_text_checks": controls,
          "pdfs_or_page_images_in_workspace": 0}
(root / "data" / "source_audit.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
