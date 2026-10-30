from pathlib import Path
import subprocess,sys,os,json,hashlib,time
R=Path(__file__).resolve().parents[1];B=Path(r'~');py=Path(sys.executable)
started=time.perf_counter();flags=0x08000000 if os.name=='nt' else 0
cmd=[str(py),'-B','-X','utf8',str(B/'brain_workers/FEI100_20261011/tools/memok.py')]
p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',creationflags=flags)
receipt={'memok_command':cmd,'memok_exit_code':p.returncode,'memok_stdout':p.stdout,'memok_stderr':p.stderr,'status':'NOT_ADMITTED','formal_target_verified':False}
if p.returncode==0:
 src=R/'code/SameOwner.lean';sha=hashlib.sha256(src.read_bytes()).hexdigest()
 env=dict(os.environ);env['LEAN_CHECK_DIR']=str(R/'out/lean')
 cmd=[str(py),'-B','-X','utf8',str(B/'.claude/dreaming/lean_check.py'),'--core','--file',str(src),'--target','same_owner_residual','--reviewed-sha256',sha,'--timeout','45','--json']
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,creationflags=flags)
 receipt.update({'command':cmd,'source_sha256':sha,'return_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 try:
  data=json.loads(p.stdout);receipt['detail']=data;receipt['status']=data.get('result',{}).get('status','UNVERIFIED');receipt['formal_target_verified']=data.get('result',{}).get('formal_target_verified',False)
 except ValueError:receipt['status']='UNVERIFIED'
receipt['seconds']=time.perf_counter()-started
(R/'out/LEAN_ATTEMPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:receipt[k] for k in ['status','formal_target_verified','memok_exit_code','seconds']}))
