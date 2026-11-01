from pathlib import Path
import subprocess,sys,json,time,hashlib
r=Path(__file__).resolve().parents[1];out=r/'out';start=time.perf_counter()
p=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8')
result={'admission_exit':p.returncode,'admission_stdout':p.stdout,'admission_stderr':p.stderr,'scope':'Integer-scaled account identity and nonnegative zero-sum saturation only; not the real entropy/curvature theorem.'}
if p.returncode==0:
 cmd=[sys.executable,'-X','utf8',r'lean_check.py','--core','--timeout','40','--json','--file',str(r/'code/Ledger.lean'),'--target','A084.saturated_children']
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
 result.update(command=cmd,checker_exit=p.returncode,stdout=p.stdout,stderr=p.stderr,source_sha256=hashlib.sha256((r/'code/Ledger.lean').read_bytes()).hexdigest())
else:result['status']='HELD_NO_COMPILER_LAUNCHED'
result['seconds']=time.perf_counter()-start
(out/'LEAN_ATTEMPT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k in ['admission_exit','checker_exit','status','seconds','stdout']})[:2500])
