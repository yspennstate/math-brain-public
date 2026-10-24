import subprocess
from pathlib import Path
p=Path('ClusterConstants.lean').resolve()
r=subprocess.run(['lake','env','lean',str(p)],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf-8',timeout=3600)
Path('second_lean_check.txt').write_text(r.stdout+r.stderr+'\nEXIT_CODE='+str(r.returncode),encoding='utf-8');print(r.stdout+r.stderr);print('EXIT_CODE',r.returncode)
