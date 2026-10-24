#!/usr/bin/env python3
"""Stage the complete frozen research snapshot; run from the workspace root."""
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "deliverables" / "T228_Research_Package"
EXCLUDED = {"a06/arxiv2608.20638v2.html"}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    if DEST.exists():
        raise SystemExit("Refusing to overwrite an existing frozen package.")
    DEST.mkdir(parents=True)
    files = []
    for directory in ["a01", "a02", "a03", "a04", "a05", "a06", "campaign"]:
        for source in sorted((ROOT / directory).rglob("*")):
            if not source.is_file():
                continue
            relative = source.relative_to(ROOT)
            if any(part in {"__pycache__", ".git", ".pytest_cache"} for part in relative.parts):
                continue
            if source.suffix in {".pyc", ".pyo", ".aux", ".log"} or source.name.endswith(".synctex.gz"):
                continue
            if relative.as_posix() in EXCLUDED:
                continue
            target = DEST / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            data = target.read_bytes()
            files.append({"path": relative.as_posix(), "sha256": digest(data), "bytes": len(data)})
    readme = (ROOT / "campaign/admin/PACKAGE_README.md").read_bytes()
    (DEST / "README.md").write_bytes(readme)
    files.append({"path": "README.md", "sha256": digest(readme), "bytes": len(readme)})
    manifest = {
        "schema": "t228-file-manifest-v1",
        "date": "2026-10-23",
        "scope": "All substantive campaign files, preserved prior sources and partial results; declared external cache and reproducible build auxiliaries excluded.",
        "self_reference_policy": "Manifest and subsequent final verification/archive/persistence receipts are excluded from their own hash coverage.",
        "files": sorted(files, key=lambda item: item["path"]),
    }
    (DEST / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"staged_files": len(files), "bytes": sum(f["bytes"] for f in files), "root": str(DEST)}))

if __name__ == "__main__":
    main()
