"""Single sequential worker. Does not import or invoke claim_files code."""
import subprocess,json,pathlib,os,datetime,time
root=pathlib.Path(__file__).resolve().parents[1]
assert os.getpriority(os.PRIO_PROCESS,0)>=10
jobs=[]
for K,ds in [(1,[.15,.35,.3875,.5,.6125,.65,.85]),(2,[.35,.7,.8115,1,1.1885,1.3,1.65])]:
 for rho in ds: jobs.append((10000,K,rho,.1,20261113,871+len(jobs),10000,20000,8,'random'))
for K,ds in [(1,[.25,.5,.75]),(2,[.6,.8,1,1.2,1.4])]:
 for rho in ds: jobs.append((10000,K,rho,0,20261113,871+len(jobs),2000,8000,8,'random'))
# A second initial state tests center equilibration; second environment tests disorder sensitivity.
for K in (1,2):
 jobs.append((10000,K,K/2,.1,20261113,999+K,30000,30000,8,'packed'))
 jobs.append((10000,K,K/2,.1,20261114,1100+K,10000,20000,8,'random'))
out=root/'data'/'ring_results.jsonl'
for job in jobs:
 started=time.monotonic()
 p=subprocess.run([str(root/'code'/'ring_ctmc'),*map(str,job)],text=True,capture_output=True,check=True)
 row=json.loads(p.stdout);row['wall_seconds']=time.monotonic()-started;row['timestamp']=datetime.datetime.now().astimezone().isoformat()
 with out.open('a') as f:f.write(json.dumps(row)+'\n')
 print(f"K={row['K']} rho={row['rho']:.4f} p={row['p_slow']} J={row['current']:.8f} blocks={row['block_sd']:.6f} wall={row['wall_seconds']:.1f}s",flush=True)
