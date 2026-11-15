"""Check cited theorem locations, source formats and report integrity offline."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    ("talagrand_prizes_archival.txt", 2, "4 Add another"),
    ("talagrand_prizes_archival.txt", 3, "Problem."),
    ("talagrand_convolution_note_2016.txt", 4, "Conjecture 6"),
    ("chen_2026_v2.txt", 2, "Theorem 1."),
    ("xiang_zhang_2026_v2.txt", 5, "Theorem 1.4"),
    ("lu_guo_fang_2026_v1.txt", 2, "Theorem 1.1."),
    ("shaposhnikov_2026_v2.txt", 7, "Theorem 3.3."),
    ("shaposhnikov_2026_v2.txt", 4, "Theorem 2.5."),
    ("lehec_2016_published.txt", 4, "Theorem 2.1."),
    ("lehec_2016_published.txt", 5, "Theorem 2.3."),
    ("eldan_lee_2017_v3.txt", 4, "Theorem 1.2."),
    ("eldan_lee_2017_v3.txt", 5, "Corollary 1.4."),
    ("ball_et_al_author_draft.txt", 4, "Theorem 4."),
    ("gozlan_et_al_2022.txt", 25, "Theorem 3.11"),
    ("talagrand_current_Korea2b.txt", 16, "This has now been proved."),
]


def main():
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
    results = []
    sources = {}
    for path in sorted((ROOT / "sources").iterdir()):
        assert path.is_file() and path.suffix == ".txt", path
        raw = path.read_bytes()
        assert not raw.startswith(b"%PDF"), path
        content = raw.decode("utf-8")
        meta, _ = json.JSONDecoder().raw_decode(content)
        sources[path.name] = {
            **meta,
            "sha256_saved_text": hashlib.sha256(raw).hexdigest(),
            "saved_text_bytes": len(raw),
        }
    for name, page, needle in CHECKS:
        content = (ROOT / "sources" / name).read_text()
        marker = f"===== PDF PAGE {page} ====="
        body = content.split(marker, 1)[1].split("===== PDF PAGE ", 1)[0]
        assert re.sub(r"\s+", "", needle) in re.sub(r"\s+", "", body), (name, page, needle)
        results.append({"file": name, "pdf_page_one_based": page,
                        "verified_text": needle, "passed": True})
    report = (ROOT / "REPORT.md").read_text()
    assert report.splitlines()[0] == "RESOLVED_IN_LITERATURE"
    assert not any(ord(c) < 32 and c not in "\n\t" for c in report), "control character in report"
    for token in [r"\lambda", r"\phi_a", r"\mu_a", r"\frac", r"\right", r"\mathbb"]:
        assert token in report, ("missing math token", token)
    forbidden = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}:
            forbidden.append(str(path.relative_to(ROOT)))
    assert not forbidden, forbidden
    result = {
        "audit_time_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "classification": "RESOLVED_IN_LITERATURE",
        "publication_status": "Resolving cube references are preprints; journal acceptance not verified",
        "theorem_location_checks": results,
        "source_manifest": sources,
        "report_sha256": hashlib.sha256(report.encode()).hexdigest(),
        "forbidden_document_or_image_files": forbidden,
        "nice": os.getpriority(os.PRIO_PROCESS, 0),
        "numerical_extremizer_search": "Not run: literature stopping instruction",
        "limitations": [
            "Text extraction validates locations, not proof correctness by itself",
            "The infinite-product consequence is proved in REPORT.md using the cited finite theorem",
            "Citation search was targeted rather than an exhaustive citing-paper census",
            "SSRN 7462079 full text returned HTTP 403 and was not used for a theorem",
        ],
    }
    output = ROOT / "data" / "literature_checks.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"checks_passed": len(results), "source_files": len(sources),
                      "nice": result["nice"], "forbidden_files": forbidden}))


if __name__ == "__main__":
    main()
