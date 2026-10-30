"""A077 v1: exact Boolean tower, physical tree and KL certificates."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, hashlib, sys
ROOT=Path(__file__).resolve().parents[1]
COUNT=0
def check(b):
    global COUNT
    COUNT+=1
    assert b, COUNT
def fwht(a):
    a=a[:]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return a
@lru_cache(None)
def ln_unit(x):
    # x in [1,2]. Positive atanh series with explicit tail enclosure.
    z=(x-1)/(x+1); N=32
    lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    err=2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
    return lo,lo+err
@lru_cache(None)
def log2(x):
    assert x>0
    k=0;y=x
    while y<1:y*=2;k-=1
    while y>=2:y/=2;k+=1
    a,b=ln_unit(y);c,d=ln_unit(F(2))
    low,high=F(k)+a/d,F(k)+b/c
    den=1<<120
    return F((low*den).__floor__(),den),F((high*den).__ceil__(),den)
def ent(ps):
    lo=hi=F(0)
    for p in ps:
        if p:
            a,b=log2(p);lo-=p*b;hi-=p*a
    return lo,hi
def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(tuple,list)):return [enc(t) for t in x]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x
def point(n):return [-1]+[1]*((1<<n)-1)
def point_entropy(n):
    p=F(1,1<<n);h0=ent([(1-2*p)**2])
    return h0[0]+8*p*(1-p)*(n-1),h0[1]+8*p*(1-p)*(n-1)
def compositions(n):
    if n==0:yield ();return
    for r in range(1,n+1):
        for tail in compositions(n-r):yield (r,)+tail
def tower_value(x,blocks):
    offset=0
    for r in blocks:
        if (x>>offset)&((1<<r)-1):return 1
        offset+=r
    return -1
def certify(n):
    p=F(1,1<<n);d=2*p
    if n<=12:
        spec=[(1-2*p)**2]+[4*p*p]*((1<<n)-1)
        vals=point(n)
        w=fwht(vals);check([F(v,1<<n)**2 for v in w]==spec)
        check(sum(spec)==1)
        energy=sum(F(i.bit_count())*q for i,q in enumerate(spec));check(energy==2*n*p)
        for i in range(n):
            direct=F(sum(vals[x]!=vals[x^(1<<i)] for x in range(1<<n)),1<<n)
            check(direct==d)
    I=2*n*p
    # Analytic compressed entropy; table and compressed implementations agree.
    q0=(1-2*p)**2
    h0=ent([q0]); H=(h0[0]+8*p*(1-p)*(n-1),h0[1]+8*p*(1-p)*(n-1))
    if n<=12:
        hh=ent(spec);check(hh[0]<=H[1] and H[0]<=hh[1])
    check(H[1]<=4*I)
    raw=F(0);corrected_lo=corrected_hi=F(0);B_lo=B_hi=F(0);J_lo=J_hi=F(0);rows=[]
    for m in range(n,1,-1):
        weight=F(1,1<<(n-m));dm=F(1,1<<(m-1));qempty=1-2*dm+2*dm*dm
        M=dm;raw+=weight*M*(m-1)
        lq,uq=log2(qempty)
        # log(1/M)-D(nu||q)=1-d+2d log(1/d)+d log(qempty).
        rem_lo=1-dm+2*dm*(m-1)+dm*lq
        rem_hi=1-dm+2*dm*(m-1)+dm*uq
        check(rem_lo>=0 and rem_hi<=2)
        corrected_lo+=weight*M*rem_lo;corrected_hi+=weight*M*rem_hi
        # Empty packet plus 2^(m-1)-1 exactly equal nonempty packets.
        tiny=dm*dm;non=(1/dm-1)*2*dm*dm
        E=ent([qempty-tiny,tiny]); Q=ent([qempty]);b=(non+E[0]-Q[1],non+E[1]-Q[0])
        B_lo+=weight*b[0];B_hi+=weight*b[1]
        tail_entropy=ent([2*dm*dm]);hq0=ent([qempty])
        hq=(hq0[0]+(1/dm-1)*tail_entropy[0],hq0[1]+(1/dm-1)*tail_entropy[1])
        hc=point_entropy(m-1)
        js=(hq[0]-hc[1]/2,hq[1]-hc[0]/2)
        J_lo+=weight*js[0];J_hi+=weight*js[1]
        hp=point_entropy(m)
        decrement=(hp[0]-hc[1]/2,hp[1]-hc[0]/2)
        check(b[0]+js[0]<=decrement[1] and decrement[0]<=b[1]+js[1])
        # Direct reconstruction of M, nu and q on all residual packets.
        if m<=10:
            z=fwht(point(m));N=1<<m
            u=[F(z[t],N) for t in range(N//2)];v=[F(z[t+N//2],N) for t in range(N//2)]
            q=[a*a+b*b for a,b in zip(u,v)];minor=[min(a*a,b*b) for a,b in zip(u,v)]
            check(sum(minor)==M);check(all(t==dm*dm for t in minor))
            check(q[0]==qempty and all(t==2*dm*dm for t in q[1:]))
            kl_lo=kl_hi=F(0)
            for t in q:
                a,b=log2(dm/t);kl_lo+=dm*a;kl_hi+=dm*b
            check((m-1)-kl_hi<=rem_hi and rem_lo<=(m-1)-kl_lo)
        rows.append(dict(residual_dimension=m,history_weight=weight,M=M,raw=weight*M*(m-1),corrected_interval=(weight*M*rem_lo,weight*M*rem_hi)))
    check(raw==p*n*(n-1));check(corrected_hi<=2*I)
    check(corrected_hi<=(1+F(3,n))*I)
    check(B_lo+J_lo<=H[1] and H[0]<=B_hi+J_hi)
    return dict(n=n,I=I,H_interval=H,raw=raw,raw_over_I=F(n-1,2),corrected_interval=(corrected_lo,corrected_hi),erasure_tree_interval=(B_lo,B_hi),JS_tree_interval=(J_lo,J_hi),scales=rows)
def main():
    start=time.perf_counter();mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
    ns=range(1,7) if mode=='pilot' else range(1,33)
    results=[certify(n) for n in ns]
    partitions=0
    for n in range(1,7 if mode=='pilot' else 9):
        for blocks in compositions(n):
            check([tower_value(x,blocks) for x in range(1<<n)]==point(n));partitions+=1
    # Separate tensor controls. Exact spectra on disjoint variables only.
    tensors=[]
    for blocks in [(2,3),(3,3),(1,2,3),(2,3,4),(4,4)]:
        n=sum(blocks);vals=[]
        for x in range(1<<n):
            val=1;off=0
            for r in blocks:
                val*=(-1 if ((x>>off)&((1<<r)-1))==0 else 1);off+=r
            vals.append(val)
        w=fwht(vals);ps=[F(z,1<<n)**2 for z in w]
        I=sum(i.bit_count()*q for i,q in enumerate(ps));check(I==sum(F(2*r,1<<r) for r in blocks))
        expected=[]
        for s in range(1<<n):
            q=F(1);off=0
            for r in blocks:
                t=(s>>off)&((1<<r)-1);p=F(1,1<<r)
                q*=((1-2*p)**2 if t==0 else 4*p*p);off+=r
            expected.append(q)
        check(ps==expected);hh=ent(ps);check(hh[1]<=4*I)
        tensors.append(dict(blocks=blocks,I=I,H_interval=hh))
    out=dict(helper_version='A077-v1',mode=mode,assertions=COUNT,dimensions=list(ns),partition_cases=partitions,tensor_cases=len(tensors),elapsed_seconds=time.perf_counter()-start,rows=results,tensors=tensors,arithmetic='integer Walsh, Fraction; 32-term rational atanh log intervals')
    dest=ROOT/'out'/('pilot.json' if mode=='pilot' else 'validation.json');dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(enc(out),indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['rows','tensors']}));print('saved',dest,'sha256',hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
