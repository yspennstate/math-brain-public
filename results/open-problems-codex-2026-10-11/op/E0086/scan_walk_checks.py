from pathlib import Path
from collections import Counter
import numpy as np,json,math
N=4096;alpha=.375;lower=(2*N)**alpha;upper=2*N**alpha;b=math.ceil(upper)
A=sorted((x,y) for x in range(-b,b+1) for y in range(-b,b+1) if lower**2<x*x+y*y<=upper**2)
assert len(A)<=N
out=[]
for seed in range(20):
 rng=np.random.default_rng(seed);choices=rng.integers(0,4,size=2*N);steps=np.array([(1,0),(-1,0),(0,1),(0,-1)])[choices]
 pos=np.vstack((np.zeros((1,2),dtype=int),np.cumsum(steps,axis=0)));pts=[tuple(map(int,z)) for z in pos];full=set(pts);counts=Counter(pts[:N+1]);x,L=counts.most_common(1)[0]
 witnesses=[(i,h) for i,h in enumerate(A) if (x[0]+h[0],x[1]+h[1]) not in full]
 if not witnesses:
  out.append({'seed':seed,'holes':0,'note':'finite geometric implication has no premise'});continue
 i,h=witnesses[0];n=N+i;prefix=set(pts[:n+1]);local=pts[:n+1].count(x);target=(x[0]+h[0],x[1]+h[1]);eligible=x in prefix and target not in prefix
 assert eligible and local>=L and n<=2*N and n**(2*alpha)<h[0]**2+h[1]**2<=4*n**(2*alpha)
 out.append({'seed':seed,'holes':len(witnesses),'favorite_at_N':x,'global_max_at_N':L,'scheduled_time':n,'offset':h,'eligible_at_scheduled_time':eligible,'local_time_at_scheduled_time':local})
Path('scan_walk_checks.json').write_text(json.dumps({'N':N,'alpha':alpha,'scan_offsets':len(A),'runs':out},indent=2));print('walk implication checks passed; runs with holes',sum(v['holes']>0 for v in out),'of',len(out))
