"""Sequential owned children with hard deadlines; nothing detached."""
from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parents[1]
commands=[('targeted.py',[],120),('independent.py',['scalar'],60),('fixture_gcd.py',[],60),('finalize.py',[],60)]
for script,args,cap in commands:
    cmd=[sys.executable,'-X','utf8',str(ROOT/'code'/script),*args]
    r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8',timeout=cap)
    (ROOT/'out'/('COMMAND_'+script+'.txt')).write_text(r.stdout,encoding='utf-8',newline='')
    print(json.dumps({'script':script,'exit':r.returncode,'output':r.stdout[-1800:]}),flush=True)
    if r.returncode: raise SystemExit(r.returncode)
