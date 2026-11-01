from pathlib import Path
import subprocess,json,hashlib,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();gate=subprocess.run(['python','-X','utf8',r'tools/memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=60)
result={'memok_exit_code':gate.returncode,'memok_output':gate.stdout+gate.stderr,'scope':'positive-part one-sided budget only; entropy continuity and stopping argument are analytic, not formalized'}
if gate.returncode==0:
 src=R/'code/positive_part.lean';args=['python','-X','utf8',r'lean_check.py','--file',str(src),'--target','A084_positive_part_budget','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest()]
 try:
  p=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=120)
  result.update({'command':args,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 except subprocess.TimeoutExpired:result.update({'status':'TIMEOUT_UNRESOLVED'})
else:result.update({'status':'NOT_RUN_MEMOK_HELD'})
result['runtime_seconds']=time.perf_counter()-start
(R/'out/FORMAL.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
