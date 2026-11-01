from pathlib import Path
import subprocess,sys,os,json,hashlib,time
R=Path(__file__).resolve().parents[1];start=time.monotonic()
mem=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=20)
out={'memok_exit':mem.returncode,'memok_output':mem.stdout+mem.stderr,'status':'ADMISSION_HELD'}
if mem.returncode==0:
 src=R/'code/GammaCertificate.lean';env=dict(os.environ);env['LEAN_CHECK_DIR']=str(R/'out/lean')
 cmd=[sys.executable,'-X','utf8','-B',r'lean_check.py','--core','--file',str(src),'--target','gamma_coarse_price','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'--json','--timeout','25']
 try:
  run=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8',timeout=40)
  (R/'out/LEAN_RAW.json').write_text(run.stdout+'\n'+run.stderr,encoding='utf-8')
  out.update(status='CHECKER_RETURNED',exit_code=run.returncode,stdout=run.stdout,stderr=run.stderr)
 except subprocess.TimeoutExpired:out.update(status='UNVERIFIED_TIMEOUT')
out['seconds']=time.monotonic()-start
(R/'out/FORMAL.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['stdout','stderr']}))
