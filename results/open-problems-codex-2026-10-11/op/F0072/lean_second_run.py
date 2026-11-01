from pathlib import Path
import subprocess,time,json,hashlib
R=Path(__file__).resolve().parent
source=R/'ReflectionArithmetic.lean';t=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(source)],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 r={'command':['lake','env','lean',str(source)],'cwd':'~/lean_verify','exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'seconds':time.time()-t,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
except Exception as e:r={'error':repr(e),'seconds':time.time()-t}
(R/'lean_second_check.json').write_text(json.dumps(r,indent=2),encoding='utf8');print(json.dumps(r),flush=True)
