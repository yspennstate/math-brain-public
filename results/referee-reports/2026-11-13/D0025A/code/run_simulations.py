#!/usr/bin/env python3
import csv,datetime,json,os,subprocess,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT)
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']: os.environ[k]='1'
header=['n','K','rho','r','p','env_seed','dynamics_seed','burn','measure','init','slow_count','longest_slow_run','current','block_sd','min_bond_current','max_bond_current','min_bin_density','max_bin_density','nice']+[f'block_{i}' for i in range(8)]
jobs=[]
for n,seeds,grid,burn,measure in [(2000,[125,126],[.05,.15,.25,.35,.45,.5,.55,.65,.75,.85,.95],10000,10000),(10000,[125],[.1,.25,.4,.5,.6,.75,.9],2000,4000),(100000,[125],[.1,.3,.5,.7,.9],1000,1000)]:
 for K in [1,2]:
  for es in seeds:
   for t in grid: jobs.append([n,K,t*K,.3,.2,es,900000+100*es+round(t*100)+K,burn,measure,'random'])
for K in [1,2]:
 jobs.append([100000,K,K/2,.3,.2,125,99321+K,1000,2000,'packed'])
 # Homogeneous K=2 maximum is not analytically replaced with rho*(K-rho).
 for t in [.1,.3,.5,.7,.9]:jobs.append([2000,K,t*K,1.,0.,125,98111+round(t*100)+K,3000,6000,'random'])
def job_key(values):
 return tuple(str(v) if i==9 else round(float(v),12) for i,v in enumerate(values))
out=ROOT/'data'/'ring_currents.csv';done=set()
if out.exists():
 with out.open() as f:
  for row in csv.DictReader(f):done.add(job_key([row[k] for k in header[:10]]))
else:
 with out.open('w') as f:csv.writer(f).writerow(header)
for idx,job in enumerate(jobs):
 if job_key(job) in done:continue
 state=Path('~/.claude/compute/compute_state.json')
 if state.exists():
  d=json.loads(state.read_text())
  if d.get('status')=='distress':
   print('Stopped at resource distress; completed rows remain saved.',flush=True);break
 begin=time.time();r=subprocess.run(['./code/ring_sim']+list(map(str,job)),capture_output=True,text=True,check=True)
 fields=next(csv.reader([r.stdout.strip()]));assert len(fields)==len(header)
 with out.open('a') as f:f.write(r.stdout)
 print(f'{idx+1}/{len(jobs)} n={job[0]} K={job[1]} rho={job[2]} init={job[-1]} J={fields[12]} wall={time.time()-begin:.1f}s',flush=True)
with (ROOT/'data'/'simulation_run.json').open('w') as f:json.dump({'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'planned_jobs':len(jobs),'workers':1,'thread_limit':1,'memory_policy':'bounded arrays; macOS address-space limit unsupported','algorithm':'exact fixed-time Poisson uniformization'},f,indent=2)
