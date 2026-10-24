from pathlib import Path
import subprocess,datetime
p=Path(__file__).parent
with (p/'round2_lean_check.txt').open('w',encoding='utf8',buffering=1) as log:
 log.write('STARTED_UTC: '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'\n');log.flush()
 r=subprocess.run(['lake','env','lean',str(p/'ColourCapacity.lean')],cwd='~/lean_verify',stdout=log,stderr=subprocess.STDOUT,timeout=3600)
 log.write('\nEXIT_CODE: '+str(r.returncode)+'\n');log.flush();print('Round-two Lean exit code:',r.returncode)
