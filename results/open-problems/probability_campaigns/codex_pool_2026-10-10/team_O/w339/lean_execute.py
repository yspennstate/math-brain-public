import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

root=Path(__file__).resolve().parent
path=root/'BKCore.lean'
# Caller source review: one Mathlib import, one arithmetic theorem, no macros,
# unsafe code, axioms, sorry, output spoofing, or side-effecting Lean commands.
raw=path.read_bytes()
assert raw.decode('utf-8') == 'import Mathlib.Tactic\n\ntheorem w339_bk_product_bound (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) :\n    1 - a - b ≤ (1 - a) * (1 - b) := by\n  nlinarith [mul_nonneg ha hb]\n'
env=dict(os.environ)
env['PYTHONDONTWRITEBYTECODE']='1'
env['LEAN_CHECK_DIR']=str(root/'lean_receipts')
args=[sys.executable,'-X','utf8','~/.claude/dreaming/lean_check.py',
      '--file',str(path),'--target','w339_bk_product_bound',
      '--reviewed-sha256',hashlib.sha256(raw).hexdigest(),'--timeout','45','--json']
print('Checking final BK algebra step only; full combinatorial translation is not certified.',flush=True)
result=subprocess.run(args,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
root.joinpath('lean_receipt.json').write_text(result.stdout,encoding='utf-8')
root.joinpath('lean_stderr.txt').write_text(result.stderr,encoding='utf-8')
root.joinpath('lean_command.json').write_text(json.dumps({'argv':args,'returncode':result.returncode,
    'scope':'only the final product-bound algebra; does not certify full BK or SPDE proof'},indent=2)+'\n',encoding='utf-8')
print(result.stdout[:6000],flush=True)
if result.stderr:print(result.stderr[:1000],flush=True)
print('RETURN',result.returncode,flush=True)
