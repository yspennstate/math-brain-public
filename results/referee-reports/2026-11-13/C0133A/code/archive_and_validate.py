"""Archive search provenance and validate saved deliverables, without new simulations."""
import csv
import datetime
import hashlib
import json
import os
import re
import urllib.request
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
ROOT = Path(__file__).resolve().parents[1]
queries = [
    '"Kosygina" "Zerner" "Problem 4.7"',
    '"excited random walk" "non-transient"',
    '"excited random walks" "non-transience"',
    '"excited random walks" "nontransient"',
    '"excited random walks" "recurrent event" speed',
    '"excited random walk" "recurrent" "infinite stacks" speed',
    '"excited random walks" "finite cookies" "speed" recurrent',
    '"excited random walks" "sublinear range" recurrent',
    '"excited random walks" "non-ballistic law"',
    '"excited random walks" "law of large numbers" "2022"',
    '"excited random walks" "law of large numbers" "2024"',
    '"excited random walks" "law of large numbers" "2026"',
    '"excited random walks" "Problem 4.7" solution',
    '"An excited random walk counter-example"',
]
archive = []
for arxiv_id in ["2201.10666", "2610.12138", "2610.10162"]:
    url = f"https://arxiv.org/abs/{arxiv_id}"
    record = {"arxiv_id": arxiv_id, "url": url}
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            content = response.read()
        name = f"{arxiv_id}-abstract.html"
        (ROOT / "sources" / name).write_bytes(content)
        record["saved"] = name
    except Exception as error:
        record["error"] = f"{type(error).__name__}: {error}"
    archive.append(record)
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
(ROOT/"sources/search-log.json").write_text(json.dumps({
    "recorded_at_utc": stamp, "keyword_queries": queries,
    "openalex_records": ["W2962897620", "W2276429711"],
    "date_filter": ["2012-01-01", "2026-11-13"],
    "limitations": "Keyword and OpenAlex searches are not exhaustive; no arbitrary-dimensional printed resolution was identified.",
    "official_metadata": archive,
}, indent=2)+"\n")

report = (ROOT/"REPORT.md").read_text()
assert report.splitlines()[0] == "PROVED"
assert not any(x in report for x in ["Interim status", "Checks in progress", "under audit"])
links = re.findall(r"\]\(([^)]+)\)", report)
missing = [x for x in links if not x.startswith("http") and not (ROOT/x).exists()]
assert not missing, missing
manifest = json.loads((ROOT/"sources/manifest.json").read_text())
verified_sources = 0
for row in manifest:
    if "sha256" in row:
        path = ROOT/"sources"/(row["name"]+".pdf")
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"]
        assert path.with_suffix(".txt").stat().st_size > 0
        verified_sources += 1
with (ROOT/"data/walks.csv").open() as f:
    walks = list(csv.DictReader(f))
assert len(walks) == 256
assert len({(r["model"],r["run"]) for r in walks}) == 256
checks = json.loads((ROOT/"data/checks.json").read_text())
assert checks["peak_rss_bytes_macos"] < 4_000_000_000
assert checks["workers"] <= 4 and checks["priority"] >= 10
for model, s in checks["models"].items():
    subset = [r for r in walks if r["model"] == model]
    assert sum(int(r["return_in_second_half"]) for r in subset) == s["return_in_second_half_count"]
    assert max(int(r["max_completed_excursion"]) for r in subset) == s["max_completed_excursion"]
prefix = json.loads((ROOT/"data/prefix-checks.json").read_text())
assert prefix["all_passed"] and len(prefix["cases"]) == 18
for row in prefix["cases"]:
    assert abs(row["direct_probability"]-row["factorized_probability"]) < 1e-12
    assert row["direct_probability"] <= row["unweighted_prefix_bound"] + 1e-12
for path in (ROOT/"code").glob("*.py"):
    compile(path.read_text(), str(path), "exec")
result = {"at_utc":stamp,"report_status":"PROVED","local_links_checked":len(links),
    "pdf_hashes_verified":verified_sources,"walk_records":len(walks),
    "prefix_cases":len(prefix["cases"]),"counting_cases":checks["counting_checks"]["sum_checks"],
    "peak_rss_bytes":checks["peak_rss_bytes_macos"],"all_passed":True,
    "scope":"Artifact consistency and finite numerical checks; mathematical audit is written in REPORT.md."}
(ROOT/"data/validation.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
