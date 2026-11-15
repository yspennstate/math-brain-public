"""Independent DFS checks of enumeration, FK identities, and heat-bath balance."""
import csv
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def graph(d,L):
    edges=[]
    for u in range(L**d):
        for a in range(d):
            step=L**a; x=(u//step)%L
            edges.append((u,u+(step if x<L-1 else -(L-1)*step),a))
    return edges

def obs(d,L,mask):
    edges=graph(d,L); n=L**d; adj=[[] for _ in range(n)]
    for e,(u,v,a) in enumerate(edges):
        if mask>>e&1:
            shift=tuple(int(j==a) for j in range(d))
            adj[u].append((v,shift));adj[v].append((u,tuple(-x for x in shift)))
    loc={}; sizes=[]; nonwrap=0; wrapping=0
    for s in range(n):
        if s in loc:continue
        loc[s]=(0,)*d; stack=[s]; size=0;wrap=False
        while stack:
            u=stack.pop();size+=1
            for v,w in adj[u]:
                z=tuple(a+b for a,b in zip(loc[u],w))
                if v in loc:wrap|=(loc[v]!=z)
                else:loc[v]=z;stack.append(v)
        sizes.append(size)
        if not wrap:nonwrap+=size**2
        wrapping|=wrap
    s2=sum(s*s for s in sizes);big=max(sizes)
    return (len(sizes),s2,s2-big*big,nonwrap,int(wrapping),big)

def main():
    results={}
    hist={}
    for mask in range(256):
        k,*vals=obs(2,2,mask); key=(mask.bit_count(),k)
        row=hist.setdefault(key,[0]*6);row[0]+=1
        for i,v in enumerate(vals,1):row[i]+=v
    with (ROOT/'data/exact_d2_L2.csv').open() as f:
        actual={(int(r['open']),int(r['k'])):[int(r[x]) for x in ['count','sum_s2','sum_excl','sum_nonwrap','wrap_count','sum_max']] for r in csv.DictReader(f)}
    assert actual==hist
    results['independent_DFS_all_256_states']='PASS: all integer histogram entries match'
    for d,L in [(2,2),(2,3),(3,2)]:
        with (ROOT/f'data/exact_d{d}_L{L}.csv').open() as f: rows=list(csv.DictReader(f))
        m=d*L**d
        assert sum(int(r['count']) for r in rows)==2**m
        for a in range(m+1):assert sum(int(r['count']) for r in rows if int(r['open'])==a)==math.comb(m,a)
        for p in [.17,.43,.79]:
            z=sum(int(r['count'])*p**int(r['open'])*(1-p)**(m-int(r['open'])) for r in rows)
            assert abs(z-1)<2e-13
        results[f'counts_d{d}_L{L}']=f'PASS: 2^{m} total, every binomial slice, q=1 Z=1 at three p'
    maxerr=0.
    edges=graph(2,2)
    ks=[obs(2,2,s)[0] for s in range(256)]
    for q,p in itertools.product([.25,.5,.75],[.2,.4,.6]):
        weights=[p**s.bit_count()*(1-p)**(8-s.bit_count())*q**ks[s] for s in range(256)]
        for s in range(256):
            for e in range(8):
                closed=s&~(1<<e);opened=s|(1<<e)
                r=p if ks[closed]==ks[opened] else p/(p+q*(1-p))
                left=weights[closed]*r;right=weights[opened]*(1-r)
                err=abs(left-right)/max(left,right)
                maxerr=max(err,maxerr);assert err<1e-12
    results['heat_bath_detailed_balance_max_relative_error']=maxerr
    # The triangle formula is checked using exact rational arithmetic, independently.
    edge_list=[(0,1),(1,2),(2,0)]
    def ktriangle(s):
        parents=list(range(3))
        def find(x):
            while parents[x]!=x:x=parents[x]
            return x
        for i,(u,v) in enumerate(edge_list):
            if s>>i&1:parents[find(u)]=find(v)
        return len({find(i) for i in range(3)})
    for q,p in itertools.product([F(1,4),F(1,2),F(3,4)],[F(1,5),F(1,2),F(4,5)]):
        v=p/(1-p);w=[v**s.bit_count()*q**ktriangle(s) for s in range(8)]
        Z=sum(w);a=sum(w[s] for s in range(8) if s&1)/Z
        b=sum(w[s] for s in range(8) if s&2)/Z
        ab=sum(w[s] for s in range(8) if s&3==3)/Z
        cov=ab-a*b
        assert cov==-v**3*q**2*(1-q)*(v+q)/Z**2
        p00=sum(w[s] for s in range(8) if s&3==0)/Z
        var=(1-p00)*p00
        osss=p00*(a+(1-a)*b)
        assert var-osss==-p00*cov>0
    results['triangle_covariance_and_OSSS_deficit']='PASS: nine exact rational parameter pairs'
    out=ROOT/'data/exact_checks.json';out.write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))

if __name__=='__main__':main()
