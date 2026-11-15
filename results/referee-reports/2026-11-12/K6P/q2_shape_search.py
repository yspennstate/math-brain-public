"""Exact shape maxima and proposed entrywise inequalities on fresh networks."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,time,random
from fractions import Fraction as Q
import q2_search as s
from q1_core import exact,serialize
start=time.monotonic();best={};checks=0;fail={}
for n in range(4,9):
    rng=random.Random(991+n)
    networks=list(s.structures(n))+[(f'fresh_random{k}',s.random_w(n,rng)) for k in range(10)]
    for name,w in networks:
        x=exact(w);F=x['F'];T=x['t'];ts=list(map(max,F))
        for r in (2,3):
            for bs in s.partitions(n,n-r):
                h=s.correction(F,bs);ratio=max(map(max,h))/T
                shape=tuple(sorted((len(b) for b in bs if len(b)>1),reverse=True));key=str((n,r,shape))
                if key not in best or ratio>Q(best[key]['ratio']):
                    best[key]=serialize(dict(ratio=ratio,w=w,partition=bs,T=T,That=max(map(max,h)),source=name))
                for a,b in ((a,b) for a in range(len(bs)) for b in range(a,len(bs))):
                    for i in bs[a]:
                        for j in bs[b]:
                            checks+=1
                            bounds={'entry_ti_tj_rminus1T':ts[i]+ts[j]+(r-1)*T,'nonsingleton_plus1':(len(shape)+1)*T}
                            for label,bound in bounds.items():
                                if h[a][b]>bound and label not in fail:
                                    fail[label]=serialize(dict(n=n,r=r,w=w,partition=bs,i=i,j=j,Fhat=h[a][b],bound=bound))
                                    s.log('Proposed inequality FAILED: '+label+'; witness saved in q2_shape_results.json.')
    s.log(f'Exact shape scan n={n} complete, {len(networks)} networks; cumulative entrywise checks {checks}.')
    with open('q2_shape_results.json','w') as f:json.dump(dict(best=best,failures=fail,checks=checks),f,indent=2)
print('SHAPE AUDIT COMPLETE',time.monotonic()-start,checks,flush=True)
