from discover import *
from fractions import Fraction as F
start=time.perf_counter();groups={};count=0;comparisons=0;witness=None
for mask in range(0,65536,2):
 a=[1 if mask>>s&1 else -1 for s in range(16)];w=fw(a);supp=sum(1<<s for s,x in enumerate(w) if x)
 d=tuple(sum(w[s]**2 for s in range(16) if s>>i&1) for i in range(4));group=groups.setdefault(d,{})
 if supp not in group:group[supp]=(mask,w)
 count+=1
for d,group in groups.items():
 items=list(group.items());q=[math.prod(F(d[i],256) if s>>i&1 else 1-F(d[i],256) for i in range(4)) for s in range(16)]
 for a,(sm,(ma,wa)) in enumerate(items):
  for sn,(mb,wb) in items[a+1:]:
   comparisons+=1
   if comparisons>1000000:raise RuntimeError('comparison cap')
   if not sm&sn:
    rr=sum(q[s] for s in range(16) if sm>>s&1)+sum(q[s]/2 for s in range(16) if not (sm|sn)>>s&1)
    if rr!=F(1,2):
     witness=dict(child_masks=[ma,mb],walsh=[wa,wb],influence_numerators=d,supports=[sm,sn],r0=str(rr),r1=str(1-rr));break
  if witness:break
 if witness:break
 if time.perf_counter()-start>55:raise RuntimeError('runtime cap')
out=dict(tables=count,comparisons=comparisons,groups=len(groups),seconds=time.perf_counter()-start,witness=witness)
(R/'out'/'PAIR_DISCOVERY.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
