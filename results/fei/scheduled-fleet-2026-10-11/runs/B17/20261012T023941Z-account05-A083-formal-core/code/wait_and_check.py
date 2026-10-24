from pathlib import Path
import subprocess,sys,time,json
R=Path(__file__).resolve().parents[1]
checks=[]
for attempt in range(6):
    p=subprocess.run([sys.executable,'-X','utf8',r'~\brain_workers\FEI100_20261011\tools\memok.py'],capture_output=True,text=True,timeout=45)
    checks.append({'attempt':attempt+1,'exit_code':p.returncode,'output':p.stdout.strip()})
    (R/'out/MEMORY_GATES.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
    print(p.stdout.strip(),flush=True)
    if p.returncode==0:
        p2=subprocess.run([sys.executable,'-X','utf8',str(R/'code/check_lean.py')])
        raise SystemExit(p2.returncode)
    if attempt<5: time.sleep(10)
raise SystemExit(75)
