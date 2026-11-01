"""Bounded search of arbitrary random rooted partitions, not Potts tree models."""
from itertools import product
from pathlib import Path
from fractions import Fraction as F
import numpy as np,json,time
ROOT=Path(__file__).resolve().parent
def partitions(n):
    def rec(a):
        if len(a)==n:yield tuple(a);return
        for k in range(max(a)+2):yield from rec(a+[k])
    return list(rec([0]))
def matrix(q,N,parts,root):
    out=[]
    for word in product(range(1,q+1),repeat=N):
        labels=(root,)+word; row=[]
        for part in parts:
            vals={};ok=True
            for block,label in zip(part,labels):
                if block in vals and vals[block]!=label:ok=False;break
                vals[block]=label
            row.append(q**(N-max(part)) if ok else 0)
        out.append(row)
    return np.asarray(out,dtype=np.int64)
def screen(a,d,A,D,denq,denr):
    z=np.abs(a-d)/(a+d);Z=np.abs(A-D)/(A+D)
    w=(a+d)/(2*denq);W=(A+D)/(2*denr)
    ts=np.unique(np.concatenate([z,Z,np.array([0.,1.])]))
    # Histograms are small; vectorized payoff evaluation avoids approximate sorting recurrences.
    dif=np.maximum(Z[:,None]-ts,0).T@W-np.maximum(z[:,None]-ts,0).T@w
    j=int(np.argmin(dif));return float(dif[j]),float(ts[j])
def exact_hist(a,d,den):
    h={}
    for aa,dd in zip(a,d):
        aa=int(aa);dd=int(dd)
        if aa+dd:
            z=F(abs(aa-dd),aa+dd);h[z]=h.get(z,F(0))+F(aa+dd,2*den)
    assert sum(h.values())==1
    return h
def exact_witness(h,H):
    out=[]
    for t in sorted(set(h)|set(H)|{F(0),F(1)}):
        diff=sum(w*max(z-t,0) for z,w in H.items())-sum(w*max(z-t,0) for z,w in h.items())
        if diff<0:out.append((diff,t))
    return min(out) if out else None
rng=np.random.default_rng(11802);started=time.monotonic();found=False
for N in [2,3,4]:
    parts=partitions(N+1)
    for q,r in [(2,3),(3,4),(4,5)]:
        mats=[matrix(s,N,parts,hyp) for s in [q,r] for hyp in [1,2]]
        for trial in range(3000):
            if time.monotonic()-started>100:break
            weights=np.zeros(len(parts),dtype=np.int64)
            ix=rng.choice(len(parts),size=int(rng.integers(2,min(8,len(parts))+1)),replace=False)
            weights[ix]=rng.integers(1,10,len(ix))
            a,d,A,D=[m@weights for m in mats];denq=int(weights.sum())*q**N;denr=int(weights.sum())*r**N
            # Skip zero-probability atoms, which are irrelevant to the marginal.
            keep=a+d>0;Keep=A+D>0
            val,t=screen(a[keep],d[keep],A[Keep],D[Keep],denq,denr)
            if val < -1e-9:
                h=exact_hist(a,d,denq);H=exact_hist(A,D,denr);witness=exact_witness(h,H)
                if witness:
                    diff,threshold=witness
                    payload={'N':N,'q':q,'r':r,'prior':[[list(p),int(w)] for p,w in zip(parts,weights) if w],
                             'prior_denominator':int(weights.sum()),'threshold':str(threshold),'stop_loss_difference':str(diff),
                             'TV_q':str(sum(z*w for z,w in h.items())),'TV_r':str(sum(z*w for z,w in H.items())),
                             'hist_q':{str(z):str(w) for z,w in h.items()},'hist_r':{str(z):str(w) for z,w in H.items()}}
                    (ROOT/'partition_witness.json').write_text(json.dumps(payload,indent=2),encoding='utf8')
                    print('CERTIFIED ARBITRARY-PARTITION OBSTRUCTION',json.dumps(payload),flush=True);found=True;break
        print('completed',N,q,r,'elapsed',round(time.monotonic()-started,2),flush=True)
        if found or time.monotonic()-started>100:break
    if found or time.monotonic()-started>100:break
(ROOT/'partition_search_summary.json').write_text(json.dumps({'found':found,'seed':11802,'elapsed_seconds':time.monotonic()-started,'limit_seconds':100}),encoding='utf8')
