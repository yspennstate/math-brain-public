import subprocess,time,json
from pathlib import Path
root=Path(__file__).parent
start=time.time()
try:
 p=subprocess.run(['cmd','/c','lake','env','lean',str(root/'ContactRigidity.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf-8',timeout=3600)
 (root/'second_lean_output.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
 result={'command':'lake env lean '+str(root/'ContactRigidity.lean'),'cwd':'~/lean_verify','timeout_seconds':3600,'exit_code':p.returncode,'elapsed_seconds':time.time()-start}
except Exception as e: result={'error':str(e),'elapsed_seconds':time.time()-start}
(root/'second_lean_result.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(result,flush=True)
