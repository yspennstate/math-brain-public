from pathlib import Path
import subprocess, os, json, hashlib, time
B=Path(__file__).resolve().parents[1]
src=B/'code'/'Accounting.lean'; raw=src.read_bytes()
env=dict(os.environ);env['LEAN_CHECK_DIR']=str(B/'out'/'lean_receipts')
cmd=['python','-X','utf8',r'lean_check.py','--file',str(src),'--target','a008_accounting','--reviewed-sha256',hashlib.sha256(raw).hexdigest(),'--core','--timeout','40','--json']
spec={'source_sha256':hashlib.sha256(raw).hexdigest(),'command':cmd,'maximum_runtime_seconds':50,'estimated_memory_mb':200,'scope':'Integer accounting consequence C=D-B+Z, B>=0,Z<=0; not Fourier analysis, logarithms, domination, or the full prose theorem','admission':'Fresh standard lean_check admission; no threshold override; imports limited to bundled Lean Omega'}
(B/'FORMAL_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
st=time.perf_counter()
try:
    r=subprocess.run(cmd,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',timeout=50,creationflags=subprocess.CREATE_NO_WINDOW)
    result={'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'elapsed_seconds':time.perf_counter()-st}
except subprocess.TimeoutExpired as e:
    result={'status':'RUNTIME_UNVERIFIED','reason':'outer 50 second cap','elapsed_seconds':time.perf_counter()-st,'stdout':str(e.stdout or ''),'stderr':str(e.stderr or '')}
(B/'out'/'formal.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
