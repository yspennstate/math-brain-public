from pathlib import Path
from itertools import product,islice
from collections import Counter
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]
def walsh(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
  h*=2
 return a
def ratio(A):
 p=q=1
 for a in A:
  t=a*a;p*=(t+1)**(t+1)
  if t:q*=t**t
 return p,q
start=time.perf_counter();best={};pilot='--pilot' in sys.argv;count=0
it=product([-2,-1,0,1,2],repeat=7)
if pilot:it=islice(it,1000)
for tail in it:
 S=sum(1<<j for j,v in enumerate(tail) if abs(v)!=1);A=sum(1<<j for j,v in enumerate(tail) if abs(v)==2)
 H=[1]+list(tail);p,q=ratio([w-1 for w in walsh(H)]);key=(S,A)
 if key not in best or p*best[key][1]>best[key][0]*q:best[key]=(p,q,H)
 count+=1
result=[];partitions=0
if not pilot:
 for S in range(128):
  inds=[j for j in range(7) if S>>j&1];winner=None;bad=0
  for owners in product(range(4),repeat=len(inds)):
   sets=[sum(1<<j for j,o in zip(inds,owners) if o==t) for t in range(4)]
   p=q=1
   for A in sets:
    x,y,H=best[(S,A)];p*=x;q*=y
   if p>q<<128:bad+=1
   if winner is None or p*winner[1]>winner[0]*q:winner=(p,q,sets)
   partitions+=1
  p,q,sets=winner
  result.append({'S':S,'intrusions':len(inds),'partitions':4**len(inds),'bad_relaxed_partitions':bad,'all_paid':bad==0,'P':str(p),'Q':str(q),'spike_sets':sets,'profiles':[best[(S,A)][2] for A in sets]})
byk={k:{'sets':sum(x['intrusions']==k for x in result),'bad_sets':sum(x['intrusions']==k and not x['all_paid'] for x in result),'bad_partitions':sum(x['bad_relaxed_partitions'] for x in result if x['intrusions']==k)} for k in range(8)}
out={'status':'COMPLETE','pilot':pilot,'scalar_cases':count,'spike_partition_cases':partitions,'by_intrusions':byk,'results':result,'elapsed_seconds':time.perf_counter()-start}
(R/'out'/('position_pilot.json' if pilot else 'position_certificate.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k!='results'}))
