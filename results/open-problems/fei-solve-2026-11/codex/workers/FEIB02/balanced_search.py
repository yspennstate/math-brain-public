from general_search import Evaluator
from pathlib import Path
import random,time,json
rng=random.Random(3008)
for n in [31,63,127,255,511,999,1023,1999]:
 p=Path(f'balanced_hill_v2_{n:04d}.json')
 if p.exists():continue
 start=time.monotonic();ev=Evaluator(n);records=[]
 for objective in ['B/I','Gamma/I']:
  r=(n+1)//2;w=max(1,round(n**.5*.45))
  seeds=[[1 if t<r else -1 for t in range(n+1)],
         [1 if ((2*t-n)//(2*w))%2==0 else -1 for t in range(n+1)]]
  for f in seeds:
   for t in range((n+1)//2):f[n-t]=-f[t]
  scores=[(ev(f),f) for f in seeds];v,f=max(scores,key=lambda x:x[0][objective]*x[0]['I']/(x[0]['I']-1));moves=[]
  for step in range(8):
   j=max(0,min(n//2,int(round(rng.gauss(n/2,n**.5/2)))));trial=f[:];trial[j]*=-1;trial[n-j]*=-1;s=ev(trial)
   if s[objective]*s['I']/(s['I']-1)>v[objective]*v['I']/(v['I']-1)+1e-11:f=trial;v=s;moves.append(step)
  I=v['I'];ratio={key.replace('/I','/(I-1)'):value*I/(I-1) for key,value in v.items() if key.endswith('/I')}
  records.append({'objective':objective.replace('/I','/(I-1)'),'ratios':v,'balanced_ratios':ratio,'accepted_moves':moves,'value_vector':''.join('+' if x>0 else '-' for x in f)})
 p.write_text(json.dumps({'n':n,'searches':records,'wall_seconds':time.monotonic()-start},indent=2)+'\n');print(n,[(r['objective'],r['balanced_ratios']) for r in records],flush=True)
