import subprocess,json,time
from pathlib import Path
p=Path('thresholds_dense.jsonl');last=0
if p.exists():
 for line in p.read_text().splitlines():last=json.loads(line)['n']
print('resume_after_n',last,flush=True)
t=time.monotonic()
with p.open('a') as out:
 proc=subprocess.Popen(['./threshold_dense',str(last+1),'2000'],stdout=subprocess.PIPE,text=True)
 for line in proc.stdout:
  row=json.loads(line);out.write(line);out.flush()
  if row['n']%25==0:print(row['n'],'wall_seconds',time.monotonic()-t,row['maxima']['B/I'],flush=True)
 assert proc.wait()==0
