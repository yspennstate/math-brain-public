from pathlib import Path
import subprocess,sys,os,json,hashlib
R=Path(__file__).resolve().parents[1]
flags=getattr(subprocess,'CREATE_NO_WINDOW',0)|getattr(subprocess,'BELOW_NORMAL_PRIORITY_CLASS',0)
admit=subprocess.run([sys.executable,'-B','-X','utf8','tools/memok.py'],capture_output=True,encoding='utf-8',creationflags=flags,timeout=55)
if admit.returncode:
    out={'status':'MEMORY_ADMISSION_HELD','formal_target_verified':False,'admission_exit_code':admit.returncode,'admission_output':admit.stdout+admit.stderr,'target':'signed_disagreement','compiler_started':False}
else:
    src=R/'code/Disagreement.lean';env=dict(os.environ)
    env['LEAN_CHECK_DIR']=str(R/'out/lean');env['PYTHONDONTWRITEBYTECODE']='1'
    cmd=[sys.executable,'-B','-X','utf8','lean_check.py','--file',str(src),'--target','signed_disagreement','--reviewed-sha256',hashlib.sha256(src.read_bytes()).hexdigest(),'--timeout','45','--json']
    try:
        p=subprocess.run(cmd,capture_output=True,encoding='utf-8',creationflags=flags,env=env,timeout=110)
        (R/'out/LEAN_STDOUT.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
        try:receipt=json.loads(p.stdout)
        except json.JSONDecodeError:receipt={'result':{'status':'RUNTIME_UNVERIFIED','formal_target_verified':False},'output':p.stdout+p.stderr}
        out={'status':receipt['result']['status'],'formal_target_verified':receipt['result'].get('formal_target_verified',False),'admission_exit_code':0,'admission_output':admit.stdout+admit.stderr,'checker_exit_code':p.returncode,'receipt':receipt}
    except subprocess.TimeoutExpired:
        out={'status':'RUNTIME_UNVERIFIED','formal_target_verified':False,'admission_exit_code':0,'reason':'bounded caller timeout','target':'signed_disagreement'}
(R/'out/FORMAL.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k not in ('receipt','output')}))
