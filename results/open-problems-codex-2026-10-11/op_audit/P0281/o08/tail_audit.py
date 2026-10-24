import mpmath as mp, json
from collections import defaultdict
from pathlib import Path
mp.mp.dps=85
cases=[(2,2,(28,1),(30,1)),(3,1,(14,9,0),(16,9,0)),(3,2,(16,11,6),(16,13,6))]
results=[]
for n,t,a,b in cases:
 mid=tuple((x+y)//2 for x,y in zip(a,b)); cap=tuple(max(x,y) for x,y in zip(a,b)); targets=[a,b,mid]
 v={(0,)*n:mp.mpf(1)}; probs=defaultdict(mp.mpf); factor=mp.exp(-n*t)
 for k in range(141):
  for d in targets:probs[d]+=factor*v.get(d,0)
  if k==140:break
  nv=defaultdict(mp.mpf)
  for d,z in v.items():
   moves=[i for i in range(n) if i==0 or d[i]<d[i-1]]
   nv[d]+=z*(n-len(moves))/n
   for i in moves:
    if d[i]==cap[i]:continue
    e=list(d); e[i]+=1; nv[tuple(e)]+=z/n
  v=nv;factor*=mp.mpf(n*t)/(k+1)
 ratio=probs[mid]**2/(probs[a]*probs[b]);assert ratio>1
 tail=mp.exp(-n*t)*mp.mpf(n*t)**141/mp.factorial(141)/(1-mp.mpf(n*t)/142)
 results.append({'n':n,'t':t,'a':a,'b':b,'ratio':mp.nstr(ratio,40),'absolute_uniformization_tail_bound':mp.nstr(tail,6)})
Path('tail_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8');print(json.dumps(results,indent=2))
