import subprocess,random,json
from pathlib import Path
import mpmath as mp
mp.mp.dps=100
rng=random.Random(196)
values=set([1,2,3,255,256,257,511,512,(1<<48)-1,1<<48])
for e in range(1,49):
 for x in [1<<e,(1<<e)-1,(1<<e)+1]:
  if x<=1<<48:values.add(x)
for _ in range(10000):values.add(rng.randrange(1,1<<48))
rows=subprocess.check_output(['./interval_log_probe'],input=''.join(str(x)+'\n' for x in sorted(values)),text=True).splitlines()
maxwidth=0
for row in rows:
 x,lo,hi=map(int,row.split());truth=mp.log(x,2);assert mp.mpf(lo)/(1<<56)<=truth<=mp.mpf(hi)/(1<<56),(x,lo,hi,truth)
 maxwidth=max(maxwidth,(hi-lo)/(1<<56))
print(json.dumps({'random_and_boundary_values_checked':len(rows),'largest_log_interval_width_bits':maxwidth,'all_enclosures_pass':True},indent=2))
