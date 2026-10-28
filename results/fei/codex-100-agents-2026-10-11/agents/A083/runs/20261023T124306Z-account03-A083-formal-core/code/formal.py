from pathlib import Path
import subprocess,json,time,hashlib,os
R=Path(__file__).resolve().parents[1]
def save(name,d):(R/'out'/name).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
src=R/'code/Orbit.lean';digest=hashlib.sha256(src.read_bytes()).hexdigest()
p=subprocess.run(['python','-X','utf8','tools/memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=60)
save('FORMAL_MEMOK.json',{'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
if p.returncode:
 save('LEAN_RESULT.json',{'status':'NOT_RUN_ADMISSION_HELD','source_sha256':digest,'target':'A083Stage20.structure_certificate','reason':p.stdout[-1500:]});print('Lean NOT_RUN_ADMISSION_HELD');raise SystemExit(0)
env=dict(os.environ);env['LEAN_CHECK_DIR']=str(R/'out/lean')
cmd=['python','-X','utf8','lean_check.py','--file',str(src),'--core','--target','A083Stage20.structure_certificate','--reviewed-sha256',digest,'--timeout','60','--json']
t=time.perf_counter()
try:
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,timeout=150)
 d={'status':'CHECKER_RETURNED','checker_exit_code':p.returncode,'seconds':time.perf_counter()-t,'source_sha256':digest,'target':'A083Stage20.structure_certificate','stdout':p.stdout,'stderr':p.stderr,'command':cmd}
except subprocess.TimeoutExpired as e:
 d={'status':'CHECKER_TIMEOUT_UNRESOLVED','seconds':time.perf_counter()-t,'source_sha256':digest,'target':'A083Stage20.structure_certificate','stdout':str(e.stdout),'stderr':str(e.stderr)}
save('LEAN_RESULT.json',d)
print(json.dumps({k:d[k] for k in d if k not in ['stdout','stderr','command']}));print(d.get('stdout','')[-4500:])
