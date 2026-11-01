"""Run an unchanged local copy of the cached check and the exact replacement."""
from pathlib import Path
import json
import os
import re
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
ORIGINAL=Path('~/<private-repo>/06_math_research/prob1000_lean_20260908/p0209.py')
baseline=ROOT/'baseline_p0209.py'
shutil.copyfile(ORIGINAL,baseline)
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
runs=[]
for filename in ('baseline_p0209.py','p0209_check.py'):
    start=time.perf_counter()
    result=subprocess.run([sys.executable,'-X','utf8',str(ROOT/filename)],cwd=ROOT,
                          env=env,capture_output=True,text=True,encoding='utf-8')
    elapsed=time.perf_counter()-start
    (ROOT/'measurements'/(filename+'.stdout.txt')).write_text(result.stdout,encoding='utf-8')
    (ROOT/'measurements'/(filename+'.stderr.txt')).write_text(result.stderr,encoding='utf-8')
    if result.returncode:
        raise RuntimeError(filename+' failed: '+result.stderr[:1000])
    runs.append({'command':'python -X utf8 '+filename,'returncode':result.returncode,'elapsed_wall_seconds':elapsed})
old=(ROOT/'measurements'/'baseline_p0209.py.stdout.txt').read_text(encoding='utf-8')
old_cases=re.findall(r'^s=\s*(\d+).*Kolmogorov distance to N\(0,1\) = ([0-9.]+)',old,re.M)
assert len(old_cases)==4
new=json.loads((ROOT/'measurements'/'p0209.json').read_text(encoding='utf-8'))
data={'command':'python -X utf8 benchmark_p0209.py','runs':runs,
      'baseline':{'unchanged_copy_of':ORIGINAL.as_posix(),'monte_carlo_scale_count':len(old_cases),
                  'monte_carlo_paths':80000,'gaussian_fast_process_surrogate':True,
                  'exact_fraction_identity_cases':0,'analytic_lower_bound_cases':0,
                  'measured_K_distances':[{"s":int(s),"distance":float(d)} for s,d in old_cases]},
      'replacement':{'monte_carlo_paths':0,'gaussian_fast_process_surrogate':False,
                     'exact_fraction_identity_cases':len(new['cases']),
                     'analytic_lower_bound_cases':len(new['cases']),
                     'largest_scale':new['cases'][-1]['s'],
                     'largest_scale_K_lower_bound':new['cases'][-1]['kolmogorov_lower_bound']},
      'scope':'Verification-quality comparison only. No deployed recall-performance or speedup claim.'}
(ROOT/'measurements'/'p0209_before_after.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(data,indent=2))
