from pathlib import Path
import json,subprocess,sys,hashlib,time
R=Path(__file__).resolve().parents[1]
def write(n,x):(R/'out'/n).write_text(json.dumps(x,indent=2),encoding='utf-8')
p=Path(r'~\.claude\compute\interventions.tsv')
print('interventions latest:', '\n'.join(p.read_text(encoding='utf-8').splitlines()[-3:])[:1500])
mem=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=45)
write('MEMOK.json',{'exit_code':mem.returncode,'stdout':mem.stdout,'stderr':mem.stderr})
if mem.returncode:
 write('LEAN.json',{'status':'NOT_RUN_ADMISSION_FAILED','memok_exit':mem.returncode});print('Lean not admitted');sys.exit(0)
stmt='theorem a047_owner_obstruction (S A e CE I : ℚ) (ledger : S - (A + e) = 4 * I - CE) (excess : 4 * I < CE) : S < A + e := by linarith'
(R/'code/owner_obstruction.lean').write_text('import Mathlib\n'+stmt+'\n#print axioms a047_owner_obstruction\n',encoding='utf-8')
cmd=[sys.executable,'-X','utf8',r'lean_check.py','--stmt',stmt,'--target','a047_owner_obstruction','--timeout','40','--json']
start=time.perf_counter()
try:
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=55)
 write('LEAN.json',{'command':cmd,'exit_code':p.returncode,'elapsed':time.perf_counter()-start,'stdout':p.stdout,'stderr':p.stderr,'scope':'scalar rational ledger obstruction only; Fourier and asymptotic proof not formalized'})
 print('Lean exit',p.returncode,p.stdout[:1200],p.stderr[:300])
except subprocess.TimeoutExpired as e:
 write('LEAN.json',{'status':'TIMEOUT','elapsed':time.perf_counter()-start,'scope':'no formal acceptance'})
 print('Lean timeout; no formal acceptance')
