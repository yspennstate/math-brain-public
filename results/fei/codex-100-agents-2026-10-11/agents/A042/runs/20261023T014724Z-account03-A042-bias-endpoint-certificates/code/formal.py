from pathlib import Path
import subprocess,sys,json,hashlib,time
R=Path(__file__).resolve().parents[1]
p=R/'code/BudgetKernel.lean';h=hashlib.sha256(p.read_bytes()).hexdigest()
cmd=[sys.executable,'-X','utf8',r'lean_check.py','--core','--file',str(p),'--target','endpoint_scale_budget','--reviewed-sha256',h,'--timeout','30']
t=time.perf_counter();x=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace')
d={'command':cmd,'source_sha256':h,'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr,'wall_seconds':time.perf_counter()-t,'translation_scope':'Integer linear numerator identity ONLY; not the logarithm, expectation or universal approximation theorem'}
(R/'out/LEAN_ATTEMPT.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print(json.dumps(d))
