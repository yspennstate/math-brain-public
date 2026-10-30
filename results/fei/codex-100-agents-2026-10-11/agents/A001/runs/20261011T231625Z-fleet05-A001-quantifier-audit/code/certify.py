from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import json, time, math, argparse

RUN=Path(__file__).resolve().parents[1]
def fwht(v):
    a=list(v); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j]=x+y; a[j+h]=x-y
        h*=2
    return [F(x,len(a)) for x in a]
def bent(k,x):
    return -1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))%2 else 1
def core(k):
    N=1<<k
    return [bent(k,x%N)-2*int(x%N==0 and x//N==1) for x in range(2*N)]
def pairs(a,i):
    return Counter((abs(a[s]),abs(a[s|(1<<i)])) for s in range(len(a)) if not (s>>i)&1)
def merge(c): return +c
def predicted(k,family,typ):
    N=1<<k; d=F(1,N); s=F(1,1<<(k//2)); m=s-d; a=1-m; p=d*d; t=p*a
    plus=(N+(1<<(k//2)))//2; minus=(N-(1<<(k//2)))//2
    c=Counter()
    if family=='X009':
        if typ=='data':
            c[(m,m)]+=N//8+(1<<(k//2))//4
            c[(s+d,s+d)]+=N//8-(1<<(k//2))//4
            # Holding the paired bit at one leaves the same bent sign imbalance.
            c[(m,s+d)]+=N//8+(1<<(k//2))//4
            c[(s+d,m)]+=N//8-(1<<(k//2))//4
            c[(d,d)]+=N//2
        else:
            c[(m,d)]+=plus; c[(s+d,d)]+=minus
        return +c
    if typ=='control':
        # Nonempty core coefficients, each paired over 2^(r-1) control fibers.
        c[(p*m,p*m)]+=(plus-1)*(N*N//2)
        c[(p*(s+d),p*(s+d))]+=minus*(N*N//2)
        c[(p*d,p*d)]+=N*(N*N//2)
        c[(p*a,p*a)]+=N*N//2-1
        c[(1-t,t)]+=1
    elif typ=='selector':
        c[(p*m,p*d)]+=(plus-1)*N*N
        c[(p*(s+d),p*d)]+=minus*N*N
        c[(p*a,p*d)]+=N*N-1
        c[(1-t,p*d)]+=1
    else:
        base=predicted(k,'X009','data')
        base[(m,m)]-=1
        for (u,v),count in base.items():
            if count: c[(p*u,p*v)]+=count*N*N
        c[(p*a,p*m)]+=N*N-1
        c[(1-t,p*m)]+=1
    return +c

def add(x,y): return x[0]+y[0],x[1]+y[1]
def scale(x,c): return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def sub(x,y): return add(x,scale(y,-1))
@lru_cache(None)
def ln_unit(q):
    assert 1<=q<=2
    z=(q-1)/(q+1); power=z; val=F()
    for j in range(36):
        val+=power/F(2*j+1); power*=z*z
    lower=2*val
    upper=lower+2*power/(73*(1-z*z))
    return lower,upper
@lru_cache(None)
def log2(q):
    assert q>0
    exponent=q.numerator.bit_length()-q.denominator.bit_length()
    scaleq=F(1<<exponent) if exponent>=0 else F(1,1<<(-exponent))
    unit=q/scaleq
    if unit<1: exponent-=1; unit*=2
    if unit>=2: exponent+=1; unit/=2
    num=ln_unit(unit); den=ln_unit(F(2))
    corners=[x/y for x in num for y in den]
    low=min(corners)+exponent; high=max(corners)+exponent
    grid=1<<100
    # Exact outward rounding contains the rational series enclosure.
    low_int=(low.numerator*grid)//low.denominator
    high_int=-((-high.numerator*grid)//high.denominator)
    return F(low_int,grid),F(high_int,grid)
def ent(q): return scale(log2(q),-q) if q else (F(),F())
def phi(u,v): return sub(add(ent(u),ent(v)),ent(u+v))
def dec(a,b): return sub(add(ent(a*a),ent(b*b)),scale(add(ent((a+b)**2),ent((a-b)**2)),F(1,2)))
def value(hist,metric):
    total=(F(),F())
    for (a,b),count in hist.items(): total=add(total,scale(phi(a*a,b*b) if metric=='B' else dec(a,b),count))
    return total
def rational(q): return str(q.numerator)+'/'+str(q.denominator)
def box(x): return dict(lower=rational(x[0]),upper=rational(x[1]),illustrative_midpoint=float((x[0]+x[1])/2))
def certify():
    start=time.monotonic(); rows=[]; assertions=0
    for k in [4,6,8,10,12,14]:
        for family in ['X009','B05']:
            types=['data','selector'] if family=='X009' else ['data','control','selector']
            h={typ:predicted(k,family,typ) for typ in types}
            # Every pair histogram represents a normalized actual spectrum.
            inf={typ:sum((n*b*b for (a,b),n in hist.items()),F()) for typ,hist in h.items()}
            for typ,hist in h.items():
                assert sum((n*(a*a+b*b) for (a,b),n in hist.items()),F())==1; assertions+=1
            result=dict(k=k,family=family,influence={typ:rational(v) for typ,v in inf.items()},ratios={},argmin={})
            for metric in ['B','Delta']:
                vals={typ:scale(value(hist,metric),1/inf[typ]) for typ,hist in h.items()}
                win='data' if family=='X009' or (metric=='B' and k==4) or (metric=='Delta' and k<=12) else 'control'
                for typ in types:
                    if typ!=win: assert vals[win][1]<vals[typ][0],(k,family,metric,win,typ); assertions+=1
                result['argmin'][metric]=win; result['ratios'][metric]={typ:box(v) for typ,v in vals.items()}
            rows.append(result)
            if time.monotonic()-start>60: raise RuntimeError('Frozen 60 second cap exceeded')
    result=dict(rows=rows,assertions=assertions,failures=0,runtime_seconds=time.monotonic()-start,arithmetic='Fraction logarithm intervals; 36 atanh terms; proved remainder; all quotient corners')
    (RUN/'out'/'ORDER_CERTIFICATES.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}))

def verify():
    start=time.monotonic(); assertions=0;cases=0
    for k in [4,6,8,10]:
        N=1<<k; coeff=fwht(core(k))
        for i in range(k+1):
            typ='selector' if i==k else 'data'
            assert pairs(coeff,i)==predicted(k,'X009',typ),(k,i); assertions+=1
        # Independent restricted-core lift rather than the closed-form multiplicities.
        p=F(1,N*N); empty=coeff[0]-1; ctrl=N*N
        for i in range(k+1):
            actual=Counter()
            for u in range(len(coeff)):
                if (u>>i)&1: continue
                c,d=coeff[u],coeff[u|(1<<i)]
                if u==0:
                    actual[(abs(1+p*empty),abs(p*d))]+=1
                    actual[(abs(p*empty),abs(p*d))]+=ctrl-1
                else: actual[(abs(p*c),abs(p*d))]+=ctrl
            assert actual==predicted(k,'B05','selector' if i==k else 'data'),(k,i); assertions+=1
        cases+=2
    k=4;r=8; N=1<<k; n=k+r+1
    v=[]
    for x in range(1<<n):
        data=x&(N-1); y=(x>>k)&1; controls=x>>(k+1)
        v.append((bent(k,data)-2*int(data==0 and y==1)) if controls==0 else 1)
    coeff=fwht(v)
    for i in range(n):
        typ='data' if i<k else 'selector' if i==k else 'control'
        hist=pairs(coeff,i)
        assert hist==predicted(k,'B05',typ); assertions+=1
        exact=sum((count*b*b for (a,b),count in hist.items()),F())
        edges=sum(v[x]!=v[x|(1<<i)] for x in range(1<<n) if not (x>>i)&1)
        assert exact==F(edges,1<<(n-1)); assertions+=1
    assert time.monotonic()-start<60
    out=dict(cases=cases+1,assertions=assertions,failures=0,runtime_seconds=time.monotonic()-start,full_table_dimension=n,arithmetic='Integer FWHT, Fraction directed coefficient-pair histograms, direct Boolean edges')
    (RUN/'out'/'WALSH_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps(out))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['certify','verify'],required=True); a=p.parse_args()
    certify() if a.mode=='certify' else verify()
