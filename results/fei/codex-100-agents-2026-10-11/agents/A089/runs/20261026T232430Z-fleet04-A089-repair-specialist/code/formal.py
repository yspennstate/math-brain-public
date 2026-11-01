from pathlib import Path
import os,subprocess,hashlib,json,time
R=Path(__file__).resolve().parents[1]
source='import Std.Tactic\ntheorem owner_total (s a e : Int) : (s + a) + e = (s + e) + a := by omega\n'
p=R/'code/Owner.lean';p.write_text(source,encoding='utf-8',newline='\n')
digest=hashlib.sha256(p.read_bytes()).hexdigest()
spec={'target':'owner_total','source_sha256':digest,'domain':'all integers s,a,e; ledger regrouping only','case_count':'universal kernel proof attempt','arithmetic':'Lean Int','memory_cap_mb':1400,'maximum_runtime_seconds':55,'helper':'lean_check.py --core with source target/hash and local receipt paths; memok exit0 observed before admission'}
(R/'out/FORMAL_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
env=dict(os.environ);env.update(LEAN_CHECK_DIR=str(R/'out/lean'),LEAN_PEAK_LOG=str(R/'out/LEAN_PEAKS.jsonl'),LEAN_JOB_MEMORY_MB='1400',LEAN_PRIORITY='belownormal',PYTHONDONTWRITEBYTECODE='1')
cmd=['python','-B','-X','utf8',r'lean_check.py','--core','--file',str(p),'--target','owner_total','--reviewed-sha256',digest,'--timeout','55','--json']
t=time.perf_counter();cp=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
(R/'out/FORMAL.json').write_text(json.dumps({'command':cmd,'exit_code':cp.returncode,'seconds':time.perf_counter()-t,'stdout':cp.stdout,'stderr':cp.stderr},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exit_code':cp.returncode,'seconds':time.perf_counter()-t,'stdout':cp.stdout[:2200],'stderr':cp.stderr[:500]}))
