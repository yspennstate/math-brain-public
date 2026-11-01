"""Create a minimal unified diff for the C0017 parafermionic spin error."""
from pathlib import Path
import difflib

root = Path("~/<private-repo>")
relative = Path("06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl")
source = root / relative
lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
matches = [i for i, line in enumerate(lines) if '"attempt_id": "C0017-A001"' in line]
assert matches == [16], matches
old = lines[matches[0]]
assert old.count("spin sigma = 2/3") == 1
new_lines = lines.copy()
new_lines[matches[0]] = old.replace("spin sigma = 2/3", "spin sigma = 1/3")
rel = relative.as_posix()
diff = "".join(difflib.unified_diff(lines, new_lines, fromfile=f"a/{rel}", tofile=f"b/{rel}", n=1))
assert diff and diff.count("spin sigma = 2/3") == 1 and diff.count("spin sigma = 1/3") == 1
out = Path(__file__).parent / "patches" / "01_c0017_spin_correction.diff"
out.parent.mkdir(exist_ok=True)
out.write_text(diff, encoding="utf-8", newline="")
print(f"C0017-A001 old incorrect spin occurrences: {old.count('spin sigma = 2/3')}")
print(f"Patched row incorrect spin occurrences: {new_lines[matches[0]].count('spin sigma = 2/3')}")
print(f"Patched row correct spin occurrences: {new_lines[matches[0]].count('spin sigma = 1/3')}")
print(out)
