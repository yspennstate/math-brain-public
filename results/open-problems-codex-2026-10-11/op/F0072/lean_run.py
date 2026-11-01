from pathlib import Path
import subprocess,json,time,hashlib
R=Path(__file__).resolve().parent
old=R/'lean_check.json'
if old.exists(): (R/'lean_check_initial.json').write_bytes(old.read_bytes())
source_hash=hashlib.sha256((R/'MixtureAlgebra.lean').read_bytes()).hexdigest()
t=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(R/'MixtureAlgebra.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 result={'command':['lake','env','lean',str(R/'MixtureAlgebra.lean')],'cwd':'~/lean_verify','exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'seconds':time.time()-t,'source_sha256':source_hash}
except Exception as e: result={'error':repr(e),'seconds':time.time()-t}
(R/'lean_check.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result),flush=True)
