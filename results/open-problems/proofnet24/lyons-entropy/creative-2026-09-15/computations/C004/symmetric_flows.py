import json,itertools as it
from fractions import Fraction as F
from pathlib import Path
c=json.load(open(Path(__file__).with_name('exact_certificate.json')))
AB=[tuple(tuple(x) for x in ab) for ab in c['AB']];ix={ab:i for i,ab in enumerate(AB)};E=range(6)
reps=[(tuple(o['A']),tuple(o['B'])) for o in c['fourier']['orbits']]
# Exact R reconstruction from verifier, no output.
src=Path(__file__).with_name('verify_exact.py').read_text();exec(src[:src.index('# Orbit weights')])
ix={ab:i for i,ab in enumerate(AB)}
bf=c['fourier']['contrast_numerators'];xf=c['fourier']['weight_numerators']
k=[F(x,216)-F(sum(rr*b for rr,b in zip(row,bf)),2721600) for x,row in zip(xf,R)]
kv=[k[ix[ab]] for ab in reps]
seen={}
for h in E:
 for e in E:
  if h==e:continue
  for tri in it.combinations([i for i in E if i not in (h,e)],3):
   z=[0]*90
   for i in range(3):
    a,b=tri[i],tri[(i+1)%3]
    z[ix[(tuple(sorted((h,a))),tuple(sorted((e,b))))]]+=1
    z[ix[(tuple(sorted((h,b))),tuple(sorted((e,a))))]]-=1
   sym=[0]*90
   for sig in [-1,1]:
    for sh in E:
     for swap in [False,True]:
      for ab,v in zip(AB,z):
       a,b=[tuple(sorted((sig*i+sh)%6 for i in G)) for G in ab]
       if swap:a,b=b,a
       sym[ix[(a,b)]]+=v
   sv=tuple(sym[ix[ab]] for ab in reps)
   if any(sv) and sv not in seen:seen[sv]=(h,e,tri)
print('distinct symflows',len(seen))
for i,(sv,lab) in enumerate(seen.items()):print(i,lab,sv)
print('k orbit',kv)
