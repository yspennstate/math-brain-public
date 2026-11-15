"""Adversarial fork-comb prequotients, exact objectives, 170-second cap."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import time,json,random,resource
from fractions import Fraction as Q
from itertools import combinations
from q1_core import exact,lump,serialize
from q2_search import fork,partitions,correction,log

start=time.monotonic();rng=random.Random(711129);best={};count=net=0
def scan(w,origin):
    global count,net
    n=len(w);x=exact(w);F=x['F'];T=x['t'];ti=list(map(max,F));net+=1
    for bs in partitions(n,n-2):
        h=correction(F,bs);ss=[(k,b[0]) for k,b in enumerate(bs) if len(b)==1]
        shape='triple' if any(len(b)==3 for b in bs) else 'pairs'
        for k,i in ss:
            for l,j in ss:
                if i>=j:continue
                for obj,val in (('ratio',h[k][l]/T),('excess',(h[k][l]-ti[i]-ti[j])/T)):
                    key=f'{n}_{shape}_{obj}'
                    if key not in best or val>Q(best[key]['value']):
                        best[key]=serialize(dict(value=val,w=w,partition=bs,i=i,j=j,T=T,ti=ti[i],tj=ti[j],Fhat=h[k][l],origin=origin))
                        with open('k7_prequotient_results.json','w') as f:json.dump(dict(best=best,networks=net,partitions=count),f,indent=2)
                        log(f'Fork prequotient {key}: {float(val):.15g}; exact witness saved.')
                        if h[k][l]>3*T:raise RuntimeError('EXACT COUNTEREXAMPLE')
        count+=1
for t in (10,1000,10**6):
    w=fork(2,t)
    for a,b in combinations(range(8),2):
        bs=[[i] for i in range(8) if i not in (a,b)]+[[a,b]]
        scan(lump(w,bs),dict(N=2,t=t,prepartition=bs))
        if time.monotonic()-start>160:break
    if time.monotonic()-start>160:break
for trial in range(10000):
    if time.monotonic()-start>165:break
    N=3 if trial%2 else 2;t=rng.choice((10,100,10000));w=fork(N,t)
    target=rng.choice((6,7,8));bs=[[i] for i in range(len(w))]
    while len(bs)>target:
        a,b=rng.sample(range(len(bs)),2)
        bs[a]+=bs[b];bs.pop(b)
    scan(lump(w,bs),dict(N=N,t=t,prepartition=bs))
with open('k7_prequotient_results.json','w') as f:json.dump(dict(best=best,networks=net,partitions=count,seconds=time.monotonic()-start,peak_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),f,indent=2)
log(f'Fork prequotient scan finished: {net} networks, {count} rank-two partitions, {time.monotonic()-start:.3f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes.')
