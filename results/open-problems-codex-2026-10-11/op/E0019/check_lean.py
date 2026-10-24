import subprocess,time,json
from pathlib import Path
root=Path(__file__).resolve().parent
start=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(root/'Algebra.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 result={'command':'lake env lean '+str(root/'Algebra.lean'),'cwd':'~/lean_verify','timeout_seconds':3600,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'elapsed_seconds':time.time()-start}
except Exception as e:result={'error':str(e),'elapsed_seconds':time.time()-start}
(root/'lean_result.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
