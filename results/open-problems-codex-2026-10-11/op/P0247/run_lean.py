from pathlib import Path
import subprocess
p=Path(__file__).parent
try:
 r=subprocess.run(['lake','env','lean',str(p/'FiniteChecks.lean')],cwd='~/lean_verify',timeout=3600,capture_output=True,text=True,encoding='utf-8')
 output='exit_code='+str(r.returncode)+'\n'+r.stdout+r.stderr
except Exception as e:output=repr(e)
(p/'lean_check.txt').write_text(output,encoding='utf-8')
print(output)
