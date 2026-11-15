"""Check source provenance, page anchors and the final artifact restrictions."""
from pathlib import Path
import hashlib
import json
import unicodedata
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
source_dir = root / "sources"
checks = []

def check(name, passed, detail=""):
    checks.append({"name": name, "passed": bool(passed), "detail": detail})

def anchor(filename, physical_page, phrase):
    pages = (source_dir / filename).read_text().split("\f")
    page = unicodedata.normalize("NFKC", pages[physical_page - 1])
    check(f"{filename}: page {physical_page}: {phrase}", phrase in page)

report = (root / "REPORT.md").read_text()
check("classification", report.splitlines()[0] == "RESOLVED_IN_LITERATURE")
check("weaker question distinguished", "remaining general, pair-dependent range question is not claimed solved" in report)
check("source extensions", all(p.suffix == ".txt" for p in source_dir.iterdir()))
for p in root.rglob("*"):
    if not p.is_file():
        continue
    check(f"no forbidden artifact: {p.relative_to(root)}", p.suffix.lower() not in
          {".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".djvu", ".webp"})
for p in source_dir.iterdir():
    blob = p.read_bytes()
    check(f"UTF-8 plain paper text: {p.name}", b"%PDF" not in blob[:4] and
          "<html" not in blob[:4000].decode("utf-8").lower())

records = [json.loads(line) for line in (root / "data/source_manifest.jsonl").read_text().splitlines()]
for p in source_dir.iterdir():
    matches = [r for r in records if r["file"] == str(p.relative_to(root)) and
               r["conversion"].startswith("PDF converted")]
    check(f"manifest exists: {p.name}", bool(matches))
    if matches:
        check(f"SHA256: {p.name}", hashlib.sha256(p.read_bytes()).hexdigest() == matches[-1]["text_sha256"])

survey = "Agresti_Veraar_survey_published.txt"
anchor(survey, 130, "Problem 3.")
anchor(survey, 136, "[29] Bechtel")
anchor(survey, 27, "Standing assumption")
anchor(survey, 28, "Definition 3.7.")
anchor(survey, 29, "Definition 3.8.")
anchor(survey, 34, "Theorem 3.17.")
anchor(survey, 37, "3.6.3.")
anchor("Agresti_Veraar_survey_2501.18561v5.txt", 92, "Problem 3")
anchor("Brzezniak_Veraar_parabolicity_1104.2768.txt", 13, "Theorem 4.1.")
anchor("Brzezniak_Veraar_parabolicity_1104.2768.txt", 16, "Theorem 5.1.")
anchor("Bechtel_Veraar_extrapolation_2311.01271.txt", 2, "the result is false")
anchor("Bechtel_Veraar_extrapolation_2311.01271.txt", 6, "Theorem 2.2.")
anchor("Lorist_Veraar_singular_1902.10620.txt", 41, "Theorem 8.2")
anchor("Portal_Veraar_rough_1810.01183.txt", 13, "Theorem 3.9.")
anchor("Agresti_Veraar_criticalI_2001.00512.txt", 18, "Assumption 3.2.")
anchor("Agresti_Veraar_criticalII_2012.04448.txt", 66, "Proposition 6.8")
anchor("Agresti_Veraar_periodic_2106.01274.txt", 12, "Theorem 5.2")
anchor("Bechtel_Mooney_Veraar_2401.05550.txt", 6, "Theorem 2.5")
anchor("Discrete_SMR_2505.22145.txt", 20, "Theorem 4.2.")
anchor("Lorist_vanNeerven_Veraar_Weis_2608.20266v2.txt", 11, "Corollary 3.8.")

result = {"checked_utc": datetime.now(timezone.utc).isoformat(),
          "passed": all(c["passed"] for c in checks), "checks": checks,
          "note": "Document/provenance audit; mathematical proof was also checked analytically. No simulation."}
(root / "data/verification.json").write_text(json.dumps(result, indent=2))
print(json.dumps({"passed": result["passed"], "checks": len(checks),
                  "failures": [c for c in checks if not c["passed"]]}, indent=2))
raise SystemExit(0 if result["passed"] else 1)
