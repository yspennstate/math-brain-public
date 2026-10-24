from pathlib import Path
import subprocess,time,json
p=Path('~/brain_workers/TRIO_1011/op/F0021')
t=time.monotonic()
try:
 r=subprocess.run(['lake','env','lean',str(p/'F0021.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf-8',timeout=3600)
 p.joinpath('lean_output.txt').write_text(r.stdout+r.stderr,encoding='utf-8')
 result={'command':'lake env lean '+str(p/'F0021.lean'),'cwd':'~/lean_verify','timeout_seconds':3600,'exit_code':r.returncode,'elapsed_seconds':time.monotonic()-t}
except Exception as e:result={'error':str(e),'elapsed_seconds':time.monotonic()-t}
p.joinpath('LEAN_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(result)
