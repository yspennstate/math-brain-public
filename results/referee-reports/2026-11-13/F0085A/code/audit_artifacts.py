"""Final filesystem, source-format, and result-accounting audit."""
import ast
import csv
import hashlib
import json
import os
import platform
import sys
from importlib.metadata import version
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main():
    status = (ROOT / "REPORT.md").read_text().splitlines()[0]
    assert status in {"PROVED", "COUNTEREXAMPLE", "PARTIAL", "NO_PROGRESS", "RESOLVED_IN_LITERATURE"}
    forbidden = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
                 if p.is_file() and p.suffix.lower() in {".pdf", ".djvu", ".ps", ".eps"}]
    assert not forbidden, forbidden
    sources = sorted((ROOT / "sources").iterdir())
    for path in sources:
        assert path.is_file() and path.suffix == ".txt", path
        contents = path.read_text(encoding="utf-8")
        assert all(ord(c) >= 32 or c in "\n\r\t" for c in contents), path
    for path in (ROOT / "code").glob("*.py"):
        ast.parse(path.read_text(), filename=str(path))
    datasets = {}
    for path in sorted((ROOT / "data").glob("torus_*.csv")):
        with path.open() as file:
            rows = list(csv.DictReader(file))
        keys = [(r["seed"], r["alpha_requested"]) for r in rows]
        assert len(set(keys)) == len(keys), path
        datasets[path.name] = len(rows)
    assert sum(datasets.values()) == 536, datasets
    checks = json.loads((ROOT / "data" / "audit_summary.json").read_text())
    assert checks["runs"] == 536 and checks["blocking_pairs"] == 0
    assert checks["max_peak_rss_MiB"] < 3800
    assert not checks["monotonicity_violations"]
    manifest = {}
    paths = [ROOT / "REPORT.md", ROOT / "LOG.md"]
    paths += [p for p in (ROOT / "code").iterdir() if p.is_file()] + sources
    paths += [p for p in (ROOT / "data").glob("*") if p.is_file()
              and p.name not in {"manifest.json", "artifact_audit.json"}]
    for path in sorted(paths):
        payload = path.read_bytes()
        manifest[str(path.relative_to(ROOT))] = {"bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()}
    (ROOT / "data" / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    result = {"report_status": status, "source_text_files": len(sources), "datasets": datasets,
              "runs": sum(datasets.values()), "forbidden_files": forbidden,
              "python_syntax": "passed", "source_plain_text": "passed",
              "platform": platform.platform(), "python": sys.version,
              "audit_process_nice": os.getpriority(os.PRIO_PROCESS, 0),
              "packages": {p:version(p) for p in ("numpy", "scipy", "matplotlib", "pypdf")},
              "status": "passed"}
    (ROOT / "data" / "artifact_audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
