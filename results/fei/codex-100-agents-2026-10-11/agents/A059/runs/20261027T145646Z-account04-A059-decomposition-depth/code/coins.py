from pathlib import Path
from fractions import Fraction as Q
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=cases=direct=0
def ck(x):
 global checks
 checks+=1
 assert x
for b in range(13):
 B=1<<b
 for k in range(B+1):
  cases+=1
  if k in (0,B):
   ck(Q(k,B) in (0,1));continue
  kill=live=cost=Q(0)
  for j in range(b):
   mass=Q(1,1<<j);nextmass=mass/2;cost+=mass
   if (k>>(b-1-j))&1:kill+=nextmass
   else:live+=nextmass
  live+=Q(1,B) # Exact equality of all b sampled bits means U=k, hence survival.
  ck(kill==Q(k,B));ck(kill+live==1);ck(cost==2*(1-Q(1,B)));ck(cost<2)
  if b<=6:
   actualkill=actualcost=0
   for word in range(B):
    direct+=1;t=0;event=False
    for j in range(b):
     t+=1;x=(word>>(b-1-j))&1;y=(k>>(b-1-j))&1
     if x!=y:event=x<y;break
    actualkill+=int(event);actualcost+=t
   ck(Q(actualkill,B)==kill);ck(Q(actualcost,B)==cost)
  if time.perf_counter()-start>55:raise RuntimeError('frozen cap')
out={'status':'PASS','assertions':checks,'threshold_cases':cases,'independently_enumerated_words':direct,'seconds':time.perf_counter()-start}
(R/'out/coins.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
