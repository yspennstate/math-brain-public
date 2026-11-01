from pathlib import Path
from fractions import Fraction
import json,hashlib,subprocess,sys,os,time
run=Path(__file__).resolve().parents[1];out=run/'out'
w=json.loads((out/'WITNESS.json').read_text(encoding='utf-8'));x=Fraction(w['CE_minus_4I'][0])
source=f'theorem witness_margin : (6 * {x.numerator} : Nat) > {x.denominator} := by decide\n'
p=run/'code'/'Margin.lean';p.write_text(source,encoding='utf-8');digest=hashlib.sha256(p.read_bytes()).hexdigest()
env=dict(os.environ);env['LEAN_CHECK_DIR']=str(out/'lean');env['PYTHONDONTWRITEBYTECODE']='1'
cmd=[sys.executable,'-B','-X','utf8',r'lean_check.py','--file',str(p),'--core','--target','witness_margin','--reviewed-sha256',digest,'--timeout','35','--json']
try:
 result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,timeout=50)
 receipt={'source_sha256':digest,'command':cmd,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'scope':'Only exact lower-endpoint integer margin >1/6; not Fourier formulas, interval validity or global FEI.'}
except subprocess.TimeoutExpired as e:
 receipt={'source_sha256':digest,'status':'RUNTIME_UNVERIFIED','scope':'No Lean certificate; timeout','stdout':str(e.stdout),'stderr':str(e.stderr)}
(out/'LEAN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
