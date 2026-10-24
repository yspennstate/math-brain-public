import numpy as np,json,time
rng=np.random.default_rng(202609206)
records=[]
for n,d in [(7,3),(8,3),(9,3),(10,3),(10,4)]:
 N=1<<n;x=np.arange(N);wt=np.array([i.bit_count() for i in x]);c=2*wt-(n-d)
 mons=[j for j in x if int(j).bit_count()<=d]
 supports=[x[(x&m)==m] for m in mons]
 best=0;bp=None
 for restart in range(15):
  p=np.zeros(N,dtype=np.int8);active=set()
  if restart%2:
   for m in rng.choice(len(mons), size=min(8,len(mons)),replace=False):p[supports[m]]^=1;active.add(int(m))
  cur=int(c@p)
  for it in range(10000):
   k=int(rng.integers(len(mons)));ids=supports[k];delta=int(c[ids]@(1-2*p[ids]))
   temperature=max(.1,(1-it/10000)*N*.035)
   if delta<=0 or rng.random()<np.exp(-delta/temperature):
    p[ids]^=1;cur+=delta
    if k in active:active.remove(k)
    else:active.add(k)
   if cur<best:best=cur;bp=[int(mons[k]) for k in active]
 record={'n':n,'degree':d,'min_centroid_deficit':best,'witness_monomials':bp,'scope':'150000 seeded local moves, exact integer objective, not exhaustive'}
 records.append(record);print(record,flush=True)
open('/mnt/data/fei_active/exploratory/centroid_probe.json','w').write(json.dumps(records,indent=2))
