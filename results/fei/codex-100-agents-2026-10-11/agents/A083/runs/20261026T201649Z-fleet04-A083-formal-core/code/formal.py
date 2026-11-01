from pathlib import Path
import json,hashlib,subprocess,os,time
R=Path(__file__).resolve().parents[1]
src=R/'code/Derivative.lean'
sha=hashlib.sha256(src.read_bytes()).hexdigest()
def save(name,d): (R/'out'/name).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
p=subprocess.run(['python','-B','-X','utf8','tools/memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=60)
save('FORMAL_MEMOK.json',{'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
if p.returncode:
 save('LEAN_RESULT.json',{'status':'NOT_RUN_ADMISSION_HELD','source_sha256':sha,'target':'A083Stage21.derivative_regression','reason':p.stdout}); print('NOT_RUN_ADMISSION_HELD');raise SystemExit(0)
env=dict(os.environ);env['LEAN_CHECK_DIR']=str(R/'out/lean')
cmd=['python','-B','-X','utf8','lean_check.py','--file',str(src),'--core','--target','A083Stage21.derivative_regression','--reviewed-sha256',sha,'--timeout','45','--json']
t=time.perf_counter()
try:
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,timeout=90)
 d={'status':'CHECKER_RETURNED','checker_exit_code':p.returncode,'seconds':time.perf_counter()-t,'source_sha256':sha,'target':'A083Stage21.derivative_regression','stdout':p.stdout,'stderr':p.stderr,'command':cmd}
except subprocess.TimeoutExpired as e:
 d={'status':'TIMEOUT_UNRESOLVED','seconds':time.perf_counter()-t,'source_sha256':sha,'target':'A083Stage21.derivative_regression','stdout':str(e.stdout),'stderr':str(e.stderr)}
save('LEAN_RESULT.json',d)
print(json.dumps(d,indent=2)[-5500:])
