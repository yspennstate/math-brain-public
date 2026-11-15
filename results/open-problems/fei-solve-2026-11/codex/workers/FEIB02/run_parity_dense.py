import subprocess,json,time,resource,os
from pathlib import Path
s=json.load(open('~/.claude/compute/compute_state.json'))
print('governor_at_launch',s['status'],s['mode'],s['ts'],flush=True)
print('inherited_nice',os.getpriority(os.PRIO_PROCESS,0),flush=True)
last=0
if Path('parity_dense.jsonl').exists():
 for line in Path('parity_dense.jsonl').read_text().splitlines():last=json.loads(line)['n']
print('resume_after_n',last,flush=True)
if last==2000:raise SystemExit(0)
start=time.monotonic()
with open('parity_dense.jsonl','a') as out,open('parity_dense.resources','w') as err:
 proc=subprocess.Popen(['./parity_dense','2000',str(last+1)],stdout=subprocess.PIPE,stderr=err,text=True)
 Path('parity_dense_child.pid').write_text(str(proc.pid)+'\n')
 for line in proc.stdout:
  row=json.loads(line);out.write(line);out.flush()
  if row['n']%25==0:print(row['n'],'wall_seconds',time.monotonic()-start,row['maxima']['Gamma/I'],flush=True)
 code=proc.wait()
r=resource.getrusage(resource.RUSAGE_CHILDREN)
metrics={'max_dimension':2000,'resumed_after_n':last,'wall_seconds':time.monotonic()-start,'cpu_seconds':r.ru_utime+r.ru_stime,'max_rss_bytes':r.ru_maxrss,'exit_code':code,'inherited_nice':os.getpriority(os.PRIO_PROCESS,0)}
Path('parity_dense.metrics.json').write_text(json.dumps(metrics,indent=2)+'\n');print(metrics,flush=True)
assert code==0
