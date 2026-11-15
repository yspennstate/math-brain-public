"""Sequential reproduction, with per-process resource measurements on macOS."""
import os,json,time,subprocess,sys
from pathlib import Path
os.chdir(Path(__file__).resolve().parent)
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
if os.getpriority(os.PRIO_PROCESS,0)<10:
    os.setpriority(os.PRIO_PROCESS,0,10)
steps=[('compile',['clang++','-O3','-std=c++17','npn.cpp','-o','npn'])]
steps += [(f'npn{n}',['./npn',str(n)]) for n in range(1,6)]
steps += [(name,[sys.executable,script]+args) for name,script,args in [('census','experiment.py',['census']),('structured','experiment.py',['structured']),('families','families.py',[]),('mux','mux.py',[]),('audit','audit.py',[]),('finalize','finalize.py',[])]]
records=[]
for name,cmd in steps:
    start=time.monotonic()
    with open(name+'.log','w') as out,open(name+'.err','w') as err:
        child=subprocess.Popen(cmd,stdout=out,stderr=err)
        pid,status,usage=os.wait4(child.pid,0);child.returncode=os.waitstatus_to_exitcode(status)
    rec={'name':name,'command':cmd,'elapsed_seconds':time.monotonic()-start,'max_rss_bytes':usage.ru_maxrss,'exit_code':child.returncode,'nice':os.getpriority(os.PRIO_PROCESS,0)}
    records.append(rec);Path('resources.json').write_text(json.dumps(records,indent=2));print(rec,flush=True)
    if child.returncode:raise SystemExit(child.returncode)
print('REPRODUCTION PASS',flush=True)
