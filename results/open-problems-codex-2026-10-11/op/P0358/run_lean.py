import subprocess,time
from pathlib import Path
start=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(Path('Bounds.lean').resolve())],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf-8',timeout=3600)
 out=p.stdout+p.stderr
 Path('lean_check.txt').write_text(out+'\nexit='+str(p.returncode)+' elapsed='+str(time.time()-start),encoding='utf-8')
 print(out, 'exit=',p.returncode,flush=True)
except Exception as e:
 Path('lean_check.txt').write_text(repr(e),encoding='utf-8')
 print(repr(e),flush=True)
