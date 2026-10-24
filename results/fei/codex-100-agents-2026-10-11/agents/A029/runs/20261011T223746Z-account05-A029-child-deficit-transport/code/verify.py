"""Second implementation: direct Walsh sums, different log series, depth DP."""
import json,time
from fractions import Fraction as F
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
P=1<<72; Q=256*P

def log_series(x):
    t=1-1/x; power=t; total=F(0)
    for j in range(1,161):
        total+=power/j; power*=t
    return total,total+power/(161*(1-t))
L2=log_series(F(2))
def logint(x):
    if not x:return 0,0
    k=x.bit_length()-1
    if x==1<<k:return k*P,k*P
    a,b=log_series(F(x,1<<k))
    a=k+a/L2[1]; b=k+b/L2[0]
    return (a.numerator*P//a.denominator,(b.numerator*P+b.denominator-1)//b.denominator)
LOG={a*a:logint(a*a) for a in range(17)}

def child(table,i,b):
    return tuple(v for x,v in enumerate(table) if x>>i&1==b)

def spectral(table,n):
    # Direct character sum, no butterfly transform.
    w=[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)) for s in range(1<<n)]
    assert sum(a*a for a in w)==4**n
    mult=256//4**n
    lo=2*n*Q-mult*sum(a*a*LOG[a*a][1] for a in w)
    hi=2*n*Q-mult*sum(a*a*LOG[a*a][0] for a in w)
    d=[256*sum(table[x]!=table[x^(1<<i)] for x in range(1<<n))//(1<<n) for i in range(n)]
    assert sum(d)==mult*sum(s.bit_count()*a*a for s,a in enumerate(w))
    return lo,hi,sum(d),d

def main():
    start=time.monotonic(); small={}; count=0; exact_ties=[]; min_positive=None
    for n in range(5):
        for mask in range(1<<(1<<n)):
            table=tuple(1 if mask>>x&1 else -1 for x in range(1<<n))
            lo,hi,inf,d=spectral(table,n)
            if n<=3:small[table]=(lo,hi,inf,d)
            if not inf:continue
            roots=[]
            for i,di in enumerate(d):
                if not di:continue
                a=child(table,i,0); b=child(table,i,1)
                al,ah,ai,_=small[a]; bl,bh,bi,_=small[b]
                assert 2*(inf-di)==ai+bi
                roots.append((i,a,b,F(hi-(al+bl)//2,di)))
            # r1 upper in raw bits*P; K=(r1 upper)-2.
            K=min(r[3] for r in roots)-2*P
            minimum=None
            for i,a,b,_ in roots:
                al,ah,ai,ad=small[a]; bl,bh,bi,bd=small[b]
                cost=F(lo-(ah+bh)//2)-K*d[i]
                for t,tl,td in ((a,al,ad),(b,bl,bd)):
                    best=F(0)
                    for j,dj in enumerate(td):
                        if not dj:continue
                        c=child(t,j,0); e=child(t,j,1)
                        ch=small[c][1]; eh=small[e][1]
                        best=min(best,F(tl-(ch+eh)//2)-K*dj)
                    cost+=best/2
                minimum=cost if minimum is None else min(minimum,cost)
            assert minimum>=0,(n,mask,minimum)
            if minimum==0:exact_ties.append((n,mask))
            elif min_positive is None or minimum<min_positive:min_positive=minimum
            count+=1
        print(json.dumps({'dimension_verified':n,'nonconstant_count':count,'elapsed_seconds':time.monotonic()-start}),flush=True)
    census=json.loads((BASE/'out'/'census_n4.json').read_text())
    assert sorted(map(list,exact_ties))==sorted(census['possible_maximizers'])
    classification={}
    for n,mask in exact_ties:
        t=tuple(1 if mask>>x&1 else -1 for x in range(1<<n))
        relevant=[i for i in range(n) if any(t[x]!=t[x^(1<<i)] for x in range(1<<n))]
        key=f'n={n},essential={len(relevant)}'
        classification[key]=classification.get(key,0)+1
        if len(relevant)==2:
            compressed=tuple(t[sum(((y>>j)&1)<<i for j,i in enumerate(relevant))] for y in range(4))
            assert sum(v==1 for v in compressed) in (1,3)
    result={'status':'PASS','nonconstant_count':count,'maximum_gap_bits':2,'equality_count':len(exact_ties),
        'equality_counts_by_dimension':classification,'equality_class':'Two-essential-variable ties are signed AND2; four-essential-variable ties require orbit analysis',
        'minimum_positive_cost_raw':[min_positive.numerator,min_positive.denominator],
        'runtime_seconds':time.monotonic()-start,'independent_agent_review':False,
        'method':'Direct character sums; -log(1-t) rational intervals at 2^72; separate min-cost depth-two dynamic program'}
    (BASE/'out'/'verification.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
