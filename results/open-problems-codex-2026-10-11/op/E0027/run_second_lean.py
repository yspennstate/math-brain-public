from pathlib import Path
import subprocess,time
root=Path(__file__).resolve().parent
start=time.time()
p=subprocess.run(['lake','env','lean',str(root/'SecondScalarChecks.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf-8',timeout=3600)
log=p.stdout+p.stderr+'\nEXIT_CODE: '+str(p.returncode)+'\nELAPSED_SECONDS: '+str(time.time()-start)+'\n'
(root/'second_lean_check.log').write_text(log,encoding='utf-8')
print(log,flush=True)
