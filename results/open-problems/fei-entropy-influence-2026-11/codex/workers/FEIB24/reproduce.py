"""Sequential reproduction; all output stays in this worker directory."""
import json,os,resource,subprocess,time
from pathlib import Path
os.chdir(Path(__file__).resolve().parent)
for name in ['OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
level=os.getpriority(os.PRIO_PROCESS,0)
if level<10:os.nice(10-level)
Path('run_logs').mkdir(exist_ok=True);rows=[];start=time.time()
units=[('compile_census',['clang++','-O3','-std=c++17','census.cpp','-o','census']),('compile_hill',['clang++','-O3','-std=c++17','hill.cpp','-o','hill']),('census',['./census']),('npn',['./census','npn']),('unrestricted',['./census','unrestricted']),('audit',['python3','analysis.py']),('hill',['./hill']),('structured',['python3','structured.py']),('paired_hidden',['python3','paired_hidden.py']),('profile',['python3','profile_search.py']),('more_constructions',['python3','more_constructions.py']),('extra_rules',['python3','extra_rules.py']),('proof_checks',['python3','proof_checks.py']),('interval_census',['python3','interval_census.py']),('records',['python3','records.py']),('highprecision',['python3','highprecision.py'])]
for index,(name,cmd) in enumerate(units):
 state=json.loads(Path.home().joinpath('.claude/compute/compute_state.json').read_text())
 if state.get('status')=='distress':
  Path('STATUS.md').write_text(f'# FEIB24 status\n\nNEXT: Resume reproduction at {name} after resolving governor distress. Existing completed units and results are preserved.\n')
  raise RuntimeError('Governor reports distress before a new compute unit; no child was killed.')
 Path('STATUS.md').write_text(f'# FEIB24 status\n\nNEXT: Reproduction unit {index+1}/{len(units)}: {name}; completed work is saved in per-unit logs.\n\nThe mathematics and finite search are complete. Final integration checks and report consolidation remain.\n')
 t=time.time()
 with open(name+'.log','w') as out,open('run_logs/'+name+'.err','w') as err:
  subprocess.run(cmd,stdout=out,stderr=err,check=True)
 rows.append(dict(unit=name,elapsed_seconds=time.time()-t,command=cmd,nice=os.getpriority(os.PRIO_PROCESS,0),governor_status=state.get('status'),governor_mode=state.get('mode')))
 Path('reproduction_progress.json').write_text(json.dumps(rows,indent=2));print(name,'passed',flush=True)
usage=resource.getrusage(resource.RUSAGE_CHILDREN)
result=dict(units=rows,elapsed_seconds=time.time()-start,children_cpu_seconds=usage.ru_utime+usage.ru_stime,max_child_rss_bytes=usage.ru_maxrss,parent_nice=os.getpriority(os.PRIO_PROCESS,0),numerical_threads_per_process=1,concurrent_units=1)
Path('resources.json').write_text(json.dumps(result,indent=2));print('all reproduction units passed',flush=True)
