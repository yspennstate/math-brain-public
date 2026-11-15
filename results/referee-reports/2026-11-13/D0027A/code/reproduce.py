"""Reproduce the saved numerical study serially, with fixed random seeds.

Run from the task directory: python3 code/reproduce.py
Requires clang++, numpy, scipy, matplotlib. Fetches no papers and uses no LLM workers.
"""
import datetime, hashlib, json, os, pathlib, resource, subprocess, sys, time
ROOT=pathlib.Path(__file__).resolve().parents[1]
os.chdir(ROOT)
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'mpl_cache')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'cache')
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
commands=[['clang++','-O3','-std=c++17','-Wall','-Wextra','-pedantic','code/simulate.cpp','-o','code/simulate']]
for law,q,seed in [('renewal',.25,271001),('hmm',.25,271002),('renewal',.65,271003),('hmm',.65,271004),
                   ('equilibrium',.25,271005),('equilibrium',.65,271006)]:
    commands.append(['./code/simulate',law,str(q),'1024','500' if law=='equilibrium' else '1000',str(seed),
                     f'data/{law}_q{int(q*100):03d}.csv','256'])
for law,q,seed in [('renewal',.25,272001),('hmm',.65,272002),('equilibrium',.25,272003)]:
    commands.append(['./code/simulate',law,str(q),'8','6000',str(seed),
                     f'data/validation_{law}_q{int(q*100):03d}.csv','8'])
for law,q,seed in [('renewal',.25,17),('hmm',.65,18),('single',.25,19)]:
    commands.append(['./code/simulate',law,str(q),'32','3',str(seed),f'data/smoke_{law}.csv','8','audit'])
commands.append(['./code/simulate','hmm','.25','8192','500','273001','data/hmm_q025_long.csv','256','long'])
commands.extend([[sys.executable,f'code/{name}.py'] for name in ['verify','analyze','analyze_extra']])
metadata={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'nice':os.getpriority(os.PRIO_PROCESS,0),'commands':[],
          'code_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (ROOT/'code').iterdir() if p.suffix in ['.cpp','.py']}}
with (ROOT/'data'/'reproduction.log').open('w') as log:
    for command in commands:
        print('Running:', ' '.join(command), flush=True);start=time.monotonic()
        result=subprocess.run(command,stdout=log,stderr=log)
        metadata['commands'].append({'args':command,'wall_seconds':time.monotonic()-start,'exit_code':result.returncode})
        (ROOT/'data'/'reproduction_manifest.json').write_text(json.dumps(metadata,indent=2))
        if result.returncode:raise SystemExit(result.returncode)
metadata['peak_child_rss_bytes_macos']=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
(ROOT/'data'/'reproduction_manifest.json').write_text(json.dumps(metadata,indent=2))
