"""Make a reviewable new-file diff entirely inside this worker folder."""
from difflib import unified_diff
from pathlib import Path

root = Path(__file__).parent
target = "~/math-brain-inbox/w365/bundle_001.json"
source = root / "brain_draft" / "bundle_001.json"
lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
diff = "".join(unified_diff([], lines, fromfile="a/" + target, tofile="b/" + target))
assert diff.startswith("--- a/" + target + "\n+++ b/" + target + "\n")
out = root / "patches" / "01_p0104_bundle.diff"
out.parent.mkdir(exist_ok=True)
out.write_text(diff, encoding="utf-8", newline="\n")
assert sum(line.startswith("+") and not line.startswith("+++") for line in diff.splitlines()) == len(lines)
print(f"PASS staged unified diff: {len(lines)} added lines at {out}")
