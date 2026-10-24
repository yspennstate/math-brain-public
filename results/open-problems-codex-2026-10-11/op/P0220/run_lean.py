import subprocess,time
from pathlib import Path
start=time.monotonic()
p=subprocess.run(['lake','env','lean',str(Path('FiniteCertificate.lean').resolve())],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
Path('lean_check.txt').write_text('Command: lake env lean '+str(Path('FiniteCertificate.lean').resolve())+'\nWorking directory: ~/lean_verify\nTimeout: 3600 seconds\nExit: '+str(p.returncode)+'\nElapsed: '+str(time.monotonic()-start)+' seconds\n'+p.stdout+p.stderr,encoding='utf8')
print(p.returncode,p.stdout,p.stderr)
