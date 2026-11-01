"""Create a unified review diff for the submitted draft without touching external files."""
from difflib import unified_diff
from pathlib import Path

here = Path(__file__).resolve().parent
body = (here / "bundle_001.json").read_text(encoding="utf-8").splitlines(keepends=True)
live = "~/math-brain-inbox/w515/bundle_001.json"
patch = "".join(unified_diff([], body, fromfile="a/" + live, tofile="b/" + live))
out = here / "patches" / "01_bundle_001.diff"
out.parent.mkdir(exist_ok=True)
out.write_text(patch, encoding="utf-8")
print(out, len(patch.splitlines()), "lines")
