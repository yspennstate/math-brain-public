from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
helper=R/'code/arithmetic.py'
code=helper.read_text(encoding='utf-8')
code=code.replace('    tnum=yn-yd\n    low=', '    tnum=yn-yd\n    if tnum==0:\n        LOGCACHE[x]=(F(k),F(k))\n        return LOGCACHE[x]\n    low=')
code=code.replace('def phi(x,y):return sub(sub(xlx(x+y),xlx(x)),xlx(y))', 'def phi(x,y):\n    if x==0 or y==0:return F(0),F(0)\n    return sub(sub(xlx(x+y),xlx(x)),xlx(y))')
if code!=helper.read_text(encoding='utf-8'):helper.write_text(code,encoding='utf-8',newline='\n')
record={'helper_version':'A074-oneflip-direct-character-v5.1','amended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'domain_change':None,'precision_change':None,'reason':'First full run reached dummy coordinate and failed overly strict interval equality test: generic interval subtraction enclosed Phi(x,0)=0 rather than returning exact zero. Added exact symbolic Phi zero-argument and log2 power-of-two branches; no counterexample to mathematical target. Preserve original frozen spec and initial completed checkpoints.','failed_check':16861,'failed_command':'python -X utf8 code/verify.py','helper_sha256':hashlib.sha256((R/'code/arithmetic.py').read_bytes()).hexdigest(),'action':'Rerun pilot then unchanged full domain; do not raise dimension or precision.'}
(R/'out/IMPLEMENTATION_CORRECTION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
(R/'FROZEN_SPEC_AMENDMENT.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Frozen v5.1 helper amendment saved; search domain unchanged.')
