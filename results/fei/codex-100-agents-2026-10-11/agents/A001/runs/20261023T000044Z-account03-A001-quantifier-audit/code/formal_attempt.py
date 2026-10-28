from pathlib import Path
import subprocess,sys,json,time
r=Path(__file__).resolve().parents[1]
flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
admit=subprocess.run([sys.executable,'-X','utf8',r'tools/memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=flags,timeout=50)
d={'admission_exit_code':admit.returncode,'admission_output':admit.stdout+admit.stderr,'scope':'rational convex interpolation upper envelope only; no logarithm/Fourier formalization'}
stmt='example (a b K t : ℚ) (ha : a ≤ K) (hb : b ≤ K) (ht : 0 ≤ t) (hu : t ≤ 1) : (1-t)*a+t*b ≤ K := by nlinarith'
d['statement']=stmt
if admit.returncode:
 d['status']='COMPUTE_ADMISSION_REFUSED_NO_COMPILER_LAUNCH'
else:
 ans=subprocess.run([sys.executable,'-X','utf8',r'lean_check.py','--stmt',stmt,'--timeout','20','--json'],capture_output=True,text=True,encoding='utf-8',creationflags=flags,timeout=55)
 d['exit_code']=ans.returncode
 try:d['receipt']=json.loads(ans.stdout);d['status']=d['receipt'].get('result',{}).get('status','UNVERIFIED')
 except json.JSONDecodeError:d['status']='UNVERIFIED';d['output']=ans.stdout+ans.stderr
(r/'out/FORMAL_ATTEMPT.json').write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'formal_attempt_status':d['status'],'admission':admit.returncode}))
