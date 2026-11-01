from pathlib import Path
import subprocess,datetime
p=Path(__file__).parent
with (p/'lean_check.txt').open('w',encoding='utf8',buffering=1) as log:
 log.write('STARTED_UTC: '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'\n')
 log.write('COMMAND: lake env lean '+str(p/'Capacity.lean')+'\n')
 log.flush()
 try:
  r=subprocess.run(['lake','env','lean',str(p/'Capacity.lean')],cwd='~/lean_verify',stdout=log,stderr=subprocess.STDOUT,timeout=3600)
  log.write('\nEXIT_CODE: '+str(r.returncode)+'\n');log.flush();print('Lean exit code:',r.returncode)
 except subprocess.TimeoutExpired:
  log.write('\nCHECK_UNVERIFIED: exceeded the requested one-hour compiler timeout.\n');log.flush();print('Lean timed out; no certificate claimed.')
