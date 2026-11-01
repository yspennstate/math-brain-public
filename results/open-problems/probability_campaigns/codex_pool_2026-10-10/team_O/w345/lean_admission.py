"""Read the production Lean admission guard; never starts or kills a compiler."""
import json
import os
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
os.environ['LEAN_CHECK_DIR']=str(ROOT/'formal'/'receipts')
sys.path.insert(0,'~/.claude/dreaming')
try:
    import lean_check
    lean_check.admission(start=True)
    status='ADMITTED_BUT_NOT_LAUNCHED'
    reason='Formal source is prepared. A compiler was not launched in this restricted research round.'
except Exception as exc:
    status='GUARD_REFUSED'
    reason=f'{type(exc).__name__}: {exc}'
data={'status':status,'compiler_launched':False,'lean_checked':False,'reason':reason,'source':'formal/hazard_factor.lean','command':'python -B -X utf8 lean_admission.py'}
(ROOT/'formal'/'admission.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(data))

