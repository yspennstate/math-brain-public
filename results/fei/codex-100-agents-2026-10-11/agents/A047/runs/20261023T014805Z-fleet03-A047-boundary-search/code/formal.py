from pathlib import Path
import sys,subprocess,json,time
R=Path(__file__).resolve().parents[1]
def save(n,x):(R/'out'/n).write_text(json.dumps(x,indent=2),encoding='utf-8')
cmd=[sys.executable,'-X','utf8',r'tools\memok.py']
p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=45)
save('MEMOK.json',{'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
if p.returncode:
 save('LEAN.json',{'status':'ADMISSION_HELD','memok_exit':p.returncode,'formal_target_verified':False});print('Lean admission held');sys.exit(0)
# This checks the exact integer certificate for the delicate rational split.
# It does not formalize logarithms, Fourier transport or all-dimensional payment.
stmt='theorem a047_split_coefficient : 128 * 12 + 301 > 301 * 6 := by decide'
(R/'code/SplitCoefficient.lean').write_text(stmt+'\n#print axioms a047_split_coefficient\n',encoding='utf-8')
cmd=[sys.executable,'-X','utf8',r'lean_check.py','--core','--stmt',stmt,'--target','a047_split_coefficient','--timeout','25','--json']
start=time.perf_counter()
try:
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=40)
 save('LEAN.json',{'exit_code':p.returncode,'command':cmd,'elapsed':time.perf_counter()-start,'stdout':p.stdout,'stderr':p.stderr,'scope':'integer constant certificate only, not mathematical theorem formalization'})
 print('Lean exit',p.returncode,p.stdout[:1000])
except subprocess.TimeoutExpired:
 save('LEAN.json',{'status':'RUNTIME_UNVERIFIED','formal_target_verified':False,'elapsed':time.perf_counter()-start,'scope':'no formal claim'});print('Lean wrapper timed out; no formal claim')
