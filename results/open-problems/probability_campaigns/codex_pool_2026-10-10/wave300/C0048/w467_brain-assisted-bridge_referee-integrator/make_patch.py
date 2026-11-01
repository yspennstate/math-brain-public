"""Render the staged draft as a unified diff without touching the inbox."""

import difflib
from pathlib import Path

root = Path(__file__).resolve().parent
source = root / "bundle_001.json"
target = "~/math-brain-inbox/w467/bundle_001.json"
patch = "".join(
    difflib.unified_diff(
        [],
        source.read_text(encoding="utf-8").splitlines(keepends=True),
        fromfile=f"a/{target}",
        tofile=f"b/{target}",
    )
)
out = root / "patches" / "01_bundle_001.diff"
out.parent.mkdir(exist_ok=True)
out.write_text(patch, encoding="utf-8")
print(out, len(patch), "bytes")
