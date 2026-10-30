from pathlib import Path
import subprocess,sys,time,json
R=Path(__file__).resolve().parents[1];start=time.perf_counter();rows=[]
for script,args in [('check_forced_basis.py',[]),('check_forced_basis.py',['--four']),('independent.py',[])]:
 p=subprocess.run([sys.executable,'-X','utf8',str(R/'code'/script),*args],capture_output=True,text=True,encoding='utf-8',timeout=max(1,55-(time.perf_counter()-start)))
 row={'script':script,'args':args,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr};rows.append(row)
 (R/'out/CHECK_RUN_LOG.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
 if p.returncode:print(p.stderr);raise SystemExit(p.returncode)
 print(p.stdout.strip())
