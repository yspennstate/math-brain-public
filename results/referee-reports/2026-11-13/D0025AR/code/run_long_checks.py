import os,pathlib,subprocess,json,datetime,time
root=pathlib.Path(__file__).resolve().parents[1]
assert os.getpriority(os.PRIO_PROCESS,0)>=10
jobs=[]
for K,densities in [(1,[.3875,.5,.6125]),(2,[.8115,1,1.1885])]:
 for rho in densities: jobs.append((10000,K,rho,.1,20261113,5000+len(jobs),200000,200000,8,'random'))
for K in (1,2):jobs.append((10000,K,K/2,.1,20261113,6000+K,200000,200000,8,'packed'))
for job in jobs:
 start=time.monotonic()
 p=subprocess.run([str(root/'code'/'ring_ctmc'),*map(str,job)],text=True,capture_output=True,check=True)
 row=json.loads(p.stdout);row['wall_seconds']=time.monotonic()-start;row['timestamp']=datetime.datetime.now().astimezone().isoformat()
 with (root/'data'/'ring_long.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
 print(f"K={row['K']} rho={row['rho']} init={row['initial']} J={row['current']:.9f} blocks={row['blocks']} wall={row['wall_seconds']:.1f}s",flush=True)
