"""Exact initial probes; all writes stay in the current directory."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import json, random, time, resource
from fractions import Fraction as Q
from q1_core import exact, lump, serialize
from q2_search import partitions, correction, fork, random_w, log

start=time.monotonic(); rng=random.Random(17071112)
best={}; counts=0
def record(key,val,data):
    if key not in best or val>Q(best[key]['value']):
        best[key]=serialize(dict(value=val,**data))
        with open('k7_probe_results.json','w') as f:json.dump(best,f,indent=2)
        if key.startswith('reject'):
            log('Initial probe: '+key+' = '+str(val)+'; exact witness saved.')

seq=[]
with open('q2_obstacle_results.json') as f:o=json.load(f)['nonparallel_singleton']
seq.append(('obstacle',[[Q(v) for v in row] for row in o['w']]))
for n in (6,7,8):
    for t in (3,10,1000):
        w=fork(1,t)
        while len(w)<n:
            from q2_search import split_leaf
            w=split_leaf(w,2)
        seq.append(('fork_'+str(t),w))
    for k in range(8):seq.append(('random_'+str(k),random_w(n,rng)))
for source,w in seq:
    n=len(w);x=exact(w); F=x['F'];ti=list(map(max,F));T=x['t']
    for bs in partitions(n,n-2):
        h=correction(F,bs); single=[(k,b[0]) for k,b in enumerate(bs) if len(b)==1]
        shape='triple' if any(len(b)==3 for b in bs) else 'pairs'
        for k,i in single:
            a=h[k][k]-F[i][i]
            data=dict(source=source,n=n,w=w,partition=bs,i=i,T=T,ti=ti[i],a=a)
            record('diagonal_'+shape,a/T,data)
            if a>ti[i]:record('reject_a_le_ti_'+shape,a/ti[i],data)
            if a>ti[i]+T:record('reject_a_le_ti_plus_T_'+shape,a/(ti[i]+T),data)
            for l,j in single:
                if j<=i:continue
                data=dict(source=source,n=n,w=w,partition=bs,i=i,j=j,T=T,ti=ti[i],tj=ti[j],Fij=F[i][j],Fhat=h[k][l])
                record('ratio_'+shape,h[k][l]/T,data)
                record('excess_'+shape,(h[k][l]-ti[i]-ti[j])/T,data)
        counts+=1
    if time.monotonic()-start>170:break
for key,z in best.items():print(key,float(Q(z['value'])),z['value'],flush=True)
log(f'Initial exact probes complete: {counts} rank-two partitions in {time.monotonic()-start:.3f}s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes. Details in k7_probe_results.json.')
