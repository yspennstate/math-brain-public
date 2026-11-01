"""Validate and apply the source patch only to a small synthetic local copy."""
import json
import re
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
fixture = root / "patch_validation"
fixture.mkdir(exist_ok=True)
patch = root / "patches/01_C0041_source_status.diff"
lines = patch.read_text(encoding="utf-8").splitlines()
relative = lines[0].removeprefix("--- a/")
number = int(re.search(r"@@ -(\d+)", lines[2]).group(1))
target = fixture / relative
assert target.resolve().is_relative_to(root.resolve())
target.parent.mkdir(parents=True, exist_ok=True)
original = (root / "sources/C0041.original.jsonl").read_text(encoding="utf-8").rstrip("\n")
pristine = "{}\n" * (number - 1) + original + "\n{}\n"
target.write_text(pristine, encoding="utf-8")
subprocess.run(["git", "init", "--quiet"], cwd=fixture, check=True, capture_output=True, timeout=30)
check = subprocess.run(["git", "apply", "--check", "--unidiff-zero", str(patch)], cwd=fixture,
                       capture_output=True, text=True, encoding="utf-8", timeout=30)
if check.returncode:
    raise RuntimeError(check.stderr)
applied = subprocess.run(["git", "apply", "--unidiff-zero", str(patch)], cwd=fixture,
                         capture_output=True, text=True, encoding="utf-8", timeout=30)
if applied.returncode:
    raise RuntimeError(applied.stderr)
after = target.read_text(encoding="utf-8").splitlines()
assert after[:number-1] == ["{}"] * (number - 1)
assert after[number:] == ["{}"]
actual = json.loads(after[number - 1])
expected = json.loads((root / "sources/C0041.proposed.jsonl").read_text(encoding="utf-8"))
assert actual == expected and actual["current_status"] == "unverified"
result = {"passed": True, "command": "python -X utf8 ~/brain_workers/w447/validate_patch.py",
          "git_apply_check_returncode": check.returncode, "local_apply_returncode": applied.returncode,
          "changed_rows": 1, "live_files_modified": 0, "fixture": str(fixture)}
(root / "PATCH_CHECK.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
