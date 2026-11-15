"""Reproduce all verification outputs without repeating optimization searches."""
import json,os,platform,resource,subprocess,sys,time
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)
env=os.environ.copy()
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    env[key]='1'
env['PYTHONDONTWRITEBYTECODE']='1'
priority=os.getpriority(os.PRIO_PROCESS,0)
assert priority>=10, 'Launch this script at nice >=10.'
rows=[]
for script,log in [('check_boolean.py','boolean_run.log'),('verify_counterexample.py','counterexample_run.log'),
                   ('audit_counterexample.py','audit_run.log'),('check_counter_exact_finite.py','exact_finite_run.log'),
                   ('repair_small.py','repair_run.log'),('check_properties.py','properties_run.log')]:
    start=time.monotonic()
    with open(log,'w') as out:
        result=subprocess.run([sys.executable,script],env=env,stdout=out,stderr=subprocess.STDOUT)
    assert result.returncode==0,(script,result.returncode)
    rss=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    if platform.system()!='Darwin': rss*=1024
    rows.append({'script':script,'exit_code':result.returncode,'seconds':time.monotonic()-start,
                 'children_peak_RSS_bytes_so_far':rss})
    print(script,'PASS',flush=True)
out={'python':sys.version,'platform':platform.platform(),'inherited_nice':priority,
     'thread_environment':{k:env[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS')},
     'checks':rows,'peak_child_RSS_bytes':max(r['children_peak_RSS_bytes_so_far'] for r in rows)}
assert out['peak_child_RSS_bytes']<3*(1024**3)
Path('verification_output.json').write_text(json.dumps(out,indent=2)+'\n')
