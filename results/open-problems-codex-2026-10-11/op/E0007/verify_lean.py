import subprocess,time
from pathlib import Path
out=Path('~/brain_workers/TRIO_1011/op/E0007/lean_check.txt')
t=time.time()
try:
 p=subprocess.run(['lake','env','lean','~/brain_workers/TRIO_1011/op/E0007/RatioIdentity.lean'],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 out.write_text('Command: lake env lean ~/brain_workers/TRIO_1011/op/E0007/RatioIdentity.lean\nExit: '+str(p.returncode)+'\nElapsed: '+str(time.time()-t)+'\n'+p.stdout+p.stderr,encoding='utf8');print(out.read_text(encoding='utf8'))
except Exception as e:out.write_text(str(e),encoding='utf8');print(e)
