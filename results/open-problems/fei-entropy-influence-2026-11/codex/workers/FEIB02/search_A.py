from general_search import Evaluator
import json,time,random
from pathlib import Path
rng=random.Random(20261110)
for n in [24,32,64,128,256,512,1000,1024,2000]:
 p=Path(f'hill_A_{n:04d}.json')
 if p.exists():continue
 t=time.monotonic();e=Evaluator(n);f=[1]*n+[-1];v=e(f);history=[]
 # Include local flips near the rare tail and broader block proposals in the bulk.
 for step in range(16):
  if step<8:j=max(0,n-step-1);width=1
  else:j=rng.randrange(n+1);width=rng.randrange(1,max(2,int(n**.5)))
  trial=f[:]
  for k in range(j,min(n+1,j+width)):trial[k]*=-1
  w=e(trial)
  if w['A/I']>v['A/I']+1e-11:f=trial;v=w;history.append({'step':step,'A/I':v['A/I']})
 row={'n':n,'objective':'A/I','final':v,'value_vector':''.join('+' if x>0 else '-' for x in f),'proposals':16,'accepted_moves':history,'wall_seconds':time.monotonic()-t}
 p.write_text(json.dumps(row,indent=2)+'\n');print(n,v,'seconds',row['wall_seconds'],flush=True)
