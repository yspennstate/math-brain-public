"""Keep all compiler artifacts in this worker's folder."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

here=Path(__file__).resolve().parent
source=here/"ArithmeticChecks.lean"
# Exact local source has been inspected: only the three named standard mathlib
# imports and one theorem, no sorry, custom axioms, macros, or output commands.
assert not any(word in source.read_text(encoding="utf-8") for word in ["sorry", "axiom", "#eval", "run_cmd"])
reviewed=hashlib.sha256(source.read_bytes()).hexdigest()
env=dict(os.environ, LEAN_CHECK_DIR=str(here/"lean_artifacts"), PYTHONDONTWRITEBYTECODE="1")
cmd=[sys.executable,"-B","-X","utf8","~/.claude/dreaming/lean_check.py","--file",str(source),"--target","w334_arithmetic_checks","--reviewed-sha256",reviewed,"--timeout","60","--json"]
try:
    p=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding="utf-8",timeout=90)
    out=p.stdout+p.stderr
    result={"command":cmd,"exit_code":p.returncode,"stdout":out}
except subprocess.TimeoutExpired as exc:
    result={"command":cmd,"exit_code":None,"status":"TIMEOUT_UNVERIFIED","stdout":"Lean wrapper reached 90 seconds; no formal check is claimed."}
(here/"lean_receipt.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2)[:6500])
