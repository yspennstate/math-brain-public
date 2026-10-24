from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'~/.claude/dreaming')
import lean_check

raw=(ROOT/'variance_identity.lean').read_bytes()
try:
    result=lean_check.check_source(raw,target='w337_variance_identity',
           reviewed_sha256=hashlib.sha256(raw).hexdigest(),
           timeout=60,output_root=ROOT/'lean_receipts',
           source_path=str(ROOT/'variance_identity.lean'))
except Exception as exc:
    result={'status':'UNAVAILABLE','error':str(exc),'scope':'algebraic identity only; stochastic proof is not certified'}
(ROOT/'measurements').mkdir(exist_ok=True)
(ROOT/'measurements'/'lean_algebra.json').write_text(json.dumps(result,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2,default=str))
