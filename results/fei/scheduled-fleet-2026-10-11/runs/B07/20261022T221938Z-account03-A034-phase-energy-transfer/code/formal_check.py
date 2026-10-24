from pathlib import Path
import sys,os,json,hashlib
sys.dont_write_bytecode=True
sys.path.insert(0,r'~\.claude\dreaming')
import lean_check
RUN=Path(__file__).resolve().parents[1]
source=b'import Lean.Elab.Tactic.Omega\n\ntheorem A034_energy (a b c : Int) (h : 3*c <= a+b) : a+b <= 3*(a+b-2*c) := by omega\n'
(RUN/'code'/'Energy.lean').write_bytes(source)
try:
    receipt=lean_check.check_source(source,target='A034_energy',reviewed_sha256=hashlib.sha256(source).hexdigest(),timeout=45,output_root=RUN/'out'/'lean',use_mathlib=False)
except (RuntimeError,OSError,ValueError) as exc:
    receipt={'status':'RUNTIME_UNVERIFIED','reason':str(exc),'no_certificate':True}
(RUN/'out'/'lean_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
