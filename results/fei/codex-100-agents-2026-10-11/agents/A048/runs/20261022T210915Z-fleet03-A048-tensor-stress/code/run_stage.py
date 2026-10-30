"""Bounded sequential verification and local persistence; no detached children."""
from pathlib import Path
import subprocess,sys,json,hashlib,time

B=Path(__file__).resolve().parents[1]
def dump(name,x):(B/'out'/name).write_text(json.dumps(x,indent=2),encoding='utf-8')
def execute(name,args,limit):
    start=time.monotonic()
    try:
        r=subprocess.run(args,cwd=B,capture_output=True,text=True,encoding='utf-8',timeout=limit,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        out={'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'wall_seconds':time.monotonic()-start,'command':args}
    except subprocess.TimeoutExpired as e:
        out={'exit_code':None,'status':'TIMEOUT','wall_seconds':time.monotonic()-start,'command':args,'stdout':str(e.stdout),'stderr':str(e.stderr)}
    dump(name,out);return out

dump('FAILED_PILOT_v1.json',{'status':'IMPLEMENTATION_FAILURE_NOT_MATHEMATICAL_REFUTATION','failure':'Python Fraction string conversion exceeded 4300 digits while serializing exact unrounded interval endpoints. No failed run counted as PASS.','repair':'Outward 2^-96 interval rounding at each operation retains rigorous inclusions and compact receipts; coherent replay also permits inherited reference-zero/source-zero atoms.','domain_change':'None for selected target; final frozen spec additionally records 64 explicit symbolic sparse-account checks.'})
if (B/'out/MAIN_EXECUTION.json').exists() and not (B/'out/MAIN_TIMEOUT_v2.json').exists():
    previous=json.loads((B/'out/MAIN_EXECUTION.json').read_text(encoding='utf-8'))
    if previous.get('status')=='TIMEOUT':dump('MAIN_TIMEOUT_v2.json',previous)
for mode,name,limit in [(['--pilot'],'PILOT_EXECUTION.json',60),([], 'MAIN_EXECUTION.json',120)]:
    if mode and (B/'out/CHECK_PILOT.json').exists():
        prior=json.loads((B/'out/CHECK_PILOT.json').read_text(encoding='utf-8'))
        frozen=json.loads((B/'out/FROZEN_PILOT.json').read_text(encoding='utf-8'))
        if prior.get('status')=='PASS' and frozen.get('helper_sha256')==hashlib.sha256((B/'code/check.py').read_bytes()).hexdigest():
            dump(name,{'status':'REUSED_FINAL_SAME_SESSION_PILOT','source':'CHECK_PILOT.json','helper_sha256':frozen['helper_sha256']})
            continue
    r=execute(name,[sys.executable,'-X','utf8',str(B/'code/check.py')]+mode,limit)
    if r['exit_code']!=0:
        print(json.dumps({'status':'CHECK_FAILED','receipt':name,'details':r}));sys.exit(1)

# Mathlib compilation is documented to exceed the campaign's 1.5GB/job cap.
# Do not start it. Save an exact scalar target and a fresh admission receipt.
statement='theorem a048_scalar (A D R : Real) : A + max (D - 4 * R) 0 = max A (A + D - 4 * R) := by\n  by_cases h : D - 4 * R <= 0\n  · rw [max_eq_right h, max_eq_left (by linarith : A + D - 4 * R <= A)]\n    ring\n  · rw [max_eq_left (by linarith : 0 <= D - 4 * R), max_eq_right (by linarith : A <= A + D - 4 * R)]\n    ring\n'
source='import Mathlib.Tactic\n\n'+statement
(B/'code/payment.lean').write_text(source,encoding='utf-8')
mem=execute('MEMOK.json',[sys.executable,'-X','utf8',r'tools\memok.py'],30)
dump('LEAN.json',{'status':'NOT_LAUNCHED_RESOURCE_CAP_OR_ADMISSION','exact_source':'code/payment.lean','source_sha256':hashlib.sha256(source.encode('utf-8')).hexdigest(),'target':'a048_scalar','rung':'ANALYTIC_PROOF_WITH_EXACT_RATIONAL_CHECKS_NOT_LEAN_CHECKED','reason':'Read lean_check.py: Mathlib compiler documented around4.1GB; campaign cap1.5GB. Earlier memok exited1. Fresh gate saved; no compiler process launched and no compiler/source/import/axiom certification asserted.','memok_exit_code':mem['exit_code'],'scope':'Only scalar max identity submitted as source; full Fourier/entropy proof is not formalized.'})
r=execute('FINALIZE_EXECUTION.json',[sys.executable,'-X','utf8',str(B/'code/finalize.py')],45)
print(json.dumps({'status':'COMPLETE_LOCAL' if r['exit_code']==0 else 'FINALIZE_FAILED','finalize':r,'checks':json.loads((B/'out/CHECK.json').read_text(encoding='utf-8'))['assertions']}))
sys.exit(0 if r['exit_code']==0 else 1)
