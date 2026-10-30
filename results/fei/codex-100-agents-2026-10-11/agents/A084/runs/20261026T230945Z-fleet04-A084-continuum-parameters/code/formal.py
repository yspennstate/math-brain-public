from pathlib import Path
import subprocess,hashlib,json,time
R=Path(__file__).resolve().parents[1]
src=R/'code/row_transfer.lean'
cmd=['python','-X','utf8',r'lean_check.py','--file',str(src),'--target','A084_row_transfer','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest()]
start=time.perf_counter()
try:
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=120)
 result={'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'runtime_seconds':time.perf_counter()-start,'scope':'algebraic final transfer l<=k*b,b<=d,k>=0 implies l<=k*d; entropy monotonicity/derivatives are NOT formalized'}
except subprocess.TimeoutExpired as e:
 result={'command':cmd,'status':'TIMEOUT_UNRESOLVED','runtime_seconds':time.perf_counter()-start}
(R/'out/FORMAL.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
