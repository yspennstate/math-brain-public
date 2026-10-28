from pathlib import Path
import subprocess,sys,os,hashlib,json
R=Path(__file__).resolve().parents[1]
source=R/'code/occupied_ratio.lean'
env=os.environ.copy(); temp=R/'out/lean_tmp';temp.mkdir(exist_ok=True)
env.update({'TEMP':str(temp),'TMP':str(temp),'PYTHONDONTWRITEBYTECODE':'1'})
command=[sys.executable,'-X','utf8','-B',r'lean_check.py','--core','--file',str(source),'--target','occupied_ratio','--reviewed-sha256',hashlib.sha256(source.read_bytes()).hexdigest(),'--json','--timeout','45']
result=subprocess.run(command,env=env,cwd=R,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW,timeout=55)
(R/'out/LEAN_OUTPUT.txt').write_text(result.stdout+result.stderr,encoding='utf-8')
status={'exit_code':result.returncode,'scope':'Natural-number integer-gap comparison ONLY: if q>=1 and u<=2k^2 then u<=2k^2*q. Does not formalize signed-bucket identity, entropy, adaptive occupation or full theorem.','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'memory_estimate_mb':200,'max_runtime_seconds':55,'core_only_no_Mathlib':True,'command':command}
try: status['receipt']=json.loads(result.stdout)
except ValueError: status['diagnostic']=result.stdout[:1500]
(R/'out/LEAN_STATUS.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
print(json.dumps({'exit_code':result.returncode,'scope':status['scope'],'diagnostic':result.stdout[:1800]}))
