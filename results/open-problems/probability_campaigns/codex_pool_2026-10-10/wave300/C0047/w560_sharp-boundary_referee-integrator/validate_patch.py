"""Apply the generated correction patch only to a copy inside this worker folder."""
import json
import shutil
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
rel = Path("06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl")
source = Path("~/<private-repo>") / rel
copy_root = root / "patch_check"
target = copy_root / rel
target.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(source, target)
diff = root / "patches" / "01_c0047_spectral_correction.diff"
subprocess.run(["git", "apply", "--check", str(diff)], cwd=copy_root, check=True)
subprocess.run(["git", "apply", str(diff)], cwd=copy_root, check=True)
records = [json.loads(line) for line in target.read_text(encoding="utf-8").splitlines()]
old = [r for r in records if r.get("attempt_id") == "C0047-A001"]
correction = [r for r in records if r.get("attempt_id") == "C0047-A001-CORR-W560"]
assert len(old) == 1 and len(correction) == 1
assert correction[0]["corrects_attempt_id"] == old[0]["attempt_id"]
assert "rho*p_c*|S|<1" in correction[0]["result"]
print(json.dumps({"status": "PASS", "original_rows_preserved": len(records)-1, "correction_rows_added": 1}))
