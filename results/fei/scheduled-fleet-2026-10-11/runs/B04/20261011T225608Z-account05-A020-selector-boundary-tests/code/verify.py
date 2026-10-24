"""A020 v1: integer Walsh census and rational outward natural logarithms."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json, math, time, argparse, hashlib

ROOT=Path(__file__).resolve().parents[1]
SCALE=1<<100
def floor(q): return q.numerator//q.denominator
def ceil(q): return -floor(-q)
def series(z):
    # ln((1+z)/(1-z)); 0 <= z <= 1/3.
    total=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(40)),Q(0))
    tail=2*z**81/(81*(1-z*z))
    return total,total+tail
L2=series(Q(1,3))
@lru_cache(None)
def lnint(k):
    assert k>0
    e=k.bit_length()-1; t=Q(k,1<<e); z=(t-1)/(t+1)
    lo,hi=series(z)
    return floor((lo+e*L2[0])*SCALE),ceil((hi+e*L2[1])*SCALE)
def lnrat(p,q):
    a,b=lnint(p); c,d=lnint(q)
    return a-d,b-c
@lru_cache(None)
def ent(hist,den):
    lo=hi=0
    for w in hist:
        if w:
            a,b=lnrat(den,w); lo+=w*a;hi+=w*b
    return lo//den,-(-hi//den)
def walsh(v):
    v=list(v); h=1
    while h<len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):u,w=v[j],v[j+h];v[j],v[j+h]=u+w,u-w
        h*=2
    return v
def table(mask,n): return [1-2*((mask>>j)&1) for j in range(1<<n)]
def spec(v):return walsh(v)
@lru_cache(None)
def branch(mask,m):
    v=table(mask,m); w=spec(v); return w,ent(tuple(sorted(t*t for t in w)),1<<(2*m))
@lru_cache(None)
def bound(a,snum,sden):
    # ln2 times target = 2*s + a*h_nat(s/a).
    lo=hi=2*snum*SCALE
    for num in [snum,a*sden-snum]:
        if num:
            l,h=lnrat(a*sden,num);lo+=num*l;hi+=num*h
    return lo//sden,-(-hi//sden)
def analyze(mask,a,m):
    n=a+m;N=1<<n;v=table(mask,n);w=walsh(v);squares=[z*z for z in w]
    assert sum(squares)==N*N
    H=ent(tuple(sorted(squares)),N*N)
    masks=[];bs=[]; eh=[]
    for x in range(1<<a):
        bm=sum(((mask>>(x+(y<<a)))&1)<<y for y in range(1<<m))
        masks.append(bm); bw,bh=branch(bm,m);bs.append(bw);eh.append(bh)
    dlo=H[0]-ceil(Q(sum(h[1] for h in eh),1<<a))
    dhi=H[1]-floor(Q(sum(h[0] for h in eh),1<<a))
    selnum=sum(squares[t]*(t&((1<<a)-1)).bit_count() for t in range(N))
    physical=sum(v[j]!=v[j^(1<<i)] for i in range(a) for j in range(N))
    assert selnum==physical*N
    data=sum(squares[t]*(t>>a).bit_count() for t in range(N))
    avgdata=sum(sum(bw[t]**2*t.bit_count() for t in range(1<<m)) for bw in bs)
    assert data==avgdata*(1<<a)
    # Partial Parseval, per data Fourier row: no dropped collisions.
    for t in range(1<<m):
        assert sum(squares[s+(t<<a)] for s in range(1<<a))==(1<<a)*sum(bw[t]**2 for bw in bs)
    B=bound(a,selnum,N*N)
    if selnum==0:
        assert len(set(masks))==1
        assert dlo<=0<=dhi
        margin=0
    else:
        margin=B[0]-dhi
        assert margin>0,(mask,a,m,margin)
    ratio=0.0 if selnum==0 else (dlo+dhi)/(B[0]+B[1])
    return dict(mask=mask,branch_masks=masks,a=a,m=m,selector_influence=str(Q(selnum,N*N)),
                density=str(Q(selnum,a*N*N)),delta_nats_interval=[str(Q(dlo,SCALE)),str(Q(dhi,SCALE))],
                bound_nats_interval=[str(Q(B[0],SCALE)),str(Q(B[1],SCALE))],
                margin_nats_lower=str(Q(margin,SCALE)),ratio_float=ratio,
                ratio_interval=None if selnum==0 else [str(Q(dlo,B[1])),str(Q(dhi,B[0]))])
def run(pilot=False):
    started=time.perf_counter(); records=[]; count=0;zero=0;upper_ratio=Q(0)
    domains=[(1,m) for m in range(4)]+[(2,m) for m in range(3)]
    if pilot:domains=[(1,2),(2,1)]
    for a,m in domains:
        cases=1<<(1<<(a+m));best=None;moderate=None;minmargin=None;z=0;bydensity={}
        for mask in range(cases):
            r=analyze(mask,a,m);count+=1
            if r['selector_influence']=='0':zero+=1;z+=1
            else:
                certified_upper=Q(r['ratio_interval'][1])
                assert certified_upper<Q(171,200)
                upper_ratio=max(upper_ratio,certified_upper)
                q=Q(r['margin_nats_lower'])
                if minmargin is None or q<minmargin:minmargin=q
                if best is None or r['ratio_float']>best['ratio_float']:best=r
                density=Q(r['density'])
                if Q(1,4)<=density<=Q(3,4) and (moderate is None or r['ratio_float']>moderate['ratio_float']):moderate=r
                key=str(density)
                if key not in bydensity or r['ratio_float']>bydensity[key]['ratio_float']:bydensity[key]=r
        row=dict(a=a,m=m,cases=cases,zero_selector=z,min_positive_margin_nats=str(minmargin),best=best,moderate_best=moderate,best_by_density=bydensity)
        records.append(row)
        (ROOT/'out'/('pilot.json' if pilot else 'census.json')).write_text(json.dumps(dict(cases=count,zero_selector=zero,domains=records,certified_ratio_cap='171/200',maximum_outward_ratio_upper=str(upper_ratio),runtime_seconds=time.perf_counter()-started),indent=2))
        print(json.dumps({k:row[k] for k in ['a','m','cases','zero_selector','min_positive_margin_nats','best','moderate_best']}),flush=True)
    print('PASS',count,'cases',time.perf_counter()-started,'seconds',flush=True)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args();run(args.pilot)
