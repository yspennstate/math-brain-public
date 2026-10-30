from pathlib import Path
import subprocess,json
R=Path(__file__).resolve().parents[1]
for name in ['verify.py','gu_guard.py','finalize.py']:
 p=subprocess.run(['python','-X','utf8',str(R/'code'/name)],capture_output=True,text=True,encoding='utf-8',timeout=180)
 print(p.stdout,flush=True)
 if p.returncode:
  print(p.stderr,flush=True);raise SystemExit(p.returncode)
files=[str(p) for p in sorted(R.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and p.suffix in ['.py','.json','.md','.lean'] and p.name not in ['PUBLICATION.json','SECRET_SCAN.json']]
p=subprocess.run(['python','-X','utf8',r'scan_secrets.py',*files],capture_output=True,text=True,encoding='utf-8',timeout=60)
result={'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'mode':'complete FILE inputs for single-commit API publication; no local git invocation','files':len(files)}
(R/'out/SECRET_SCAN.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result),flush=True)
raise SystemExit(p.returncode)
