"""Exact finite checks; analytic proof is in DERIVATION.md. No third party modules."""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from pathlib import Path
import json, time

OUT=Path(__file__).resolve().parents[1]/'out'
BITS=192
SCALE=1<<BITS
K=28
def rounded(lo,hi):
    return (F((lo*SCALE).__floor__(),SCALE),F((hi*SCALE).__ceil__(),SCALE))
def add(a,b): return a[0]+b[0],a[1]+b[1]
def sub(a,b): return a[0]-b[1],a[1]-b[0]
def mul(a,t): return (a[0]*t,a[1]*t) if t>=0 else (a[1]*t,a[0]*t)
@lru_cache(None)
def log_unit(x):
    assert 1<=x<=2
    z=(x-1)/(x+1)
    total=sum((2*z**(2*j+1)/F(2*j+1) for j in range(K)),F(0))
    tail=2*z**(2*K+1)/(F(2*K+1)*(1-z*z))
    return rounded(total,total+tail)
LN2=log_unit(F(2))
@lru_cache(None)
def ln(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/F(2)**k
    if y<1: y*=2; k-=1
    assert 1<=y<2
    return add(log_unit(y),mul(LN2,k))
@lru_cache(None)
def ent(x):
    p=x*x
    return (F(0),F(0)) if not p else mul(ln(p),-p)
def total(terms):
    result=(F(0),F(0))
    for a,t in terms: result=add(result,mul(a,t))
    return result
def quantities(m,r,s):
    n=1<<m; a=F(1,1<<r); b=F(1,1<<s); d=F(1,n); root=F(1,1<<(m//2))
    pi=(1-a,a*(1-b),a*b); w=1-2*b
    va=2*a*(1-a)*d*(1+w*w); vb=8*a*b*(1-b)*d; v=va+vb
    ic=2*r*a*d+4*s*a*b*d
    l=add(mul(LN2,va*(2*r-2)+vb*(2*r+2*s-4)),mul(ln(w*w),-2*a*(1-a)*d*w*w) if w else (F(0),F(0)))
    terms=[]
    for t in (-1,1):
        for u in (-1,1):
            count=F(n,4)+F(1<<(m//2),4)*(t+u)
            assert count.denominator==1 and count>=0
            terms.append((ent(root-2*d*(pi[1]*t+pi[2]*u)),count))
    terms.extend([(ent(2*a*d),F(n,2)*(1/a-1)),(ent(2*a*d*w),F(n,2)*(1/a-1)),(ent(4*a*b*d),F(n,2)*(1/a)*(1/b-1))])
    hf=total(terms)
    he=total((ent(root-2*d*t),F(n+(1<<(m//2))*t,2)) for t in (-1,1))
    ht=add(mul(LN2,pi[0]*m),mul(he,a))
    diff=sub(hf,ht)
    rem=sub(sub(diff,mul(LN2,m*v)),l)
    err=sub(rem,(3*v,3*v))
    bound=8*root*v
    assert err[0]>=-bound and err[1]<=bound,(m,r,s,'error')
    low=mul(add((F(3),F(3)),mul(ln(1-2*root),2)),v)
    high=mul(add((F(3),F(3)),mul(ln(1+2*root),2)),v)
    assert rem[0]>=low[1] and rem[1]<=high[0],(m,r,s,'sharp Taylor')
    assert v<=2*ic and l[0]>=0 and l[1]<=4*ic*LN2[0]+F(1,1<<140)
    rows=[]
    for adj in (0,1):
        i12=4*(m-adj)*d
        rs=m*v-8*adj*d*pi[1]*pi[2]
        rd=2*a*(1-a)*((1-b)*2*m*d+b*2*m*d)+2*a*b*(1-b)*i12
        surcharge=2*a*(1-a)*b*(1-b)*i12
        assert rd-rs==surcharge
        excess=sub(diff,mul(LN2,rs))
        assert excess[0]>=0 and excess[1]<=18*ic*LN2[0]
        rows.append(dict(m=m,r=r,s=s,adjacency=adj,IC=str(ic),V=str(v),Rstar=str(rs),surcharge=str(surcharge),D_nat_interval=[str(x) for x in diff],error_nat_interval=[str(x) for x in err],error_bound_nat=str(bound)))
    return rows

def walsh(values):
    a=list(values); stride=1
    while stride<len(a):
        for start in range(0,len(a),2*stride):
            for j in range(start,start+stride):
                x,y=a[j],a[j+stride]; a[j],a[j+stride]=x+y,x-y
        stride*=2
    return a
def influence(w):
    den=len(w)**2
    return sum((F(x*x*i.bit_count(),den) for i,x in enumerate(w)),F(0))
def direct(m,r,s,vtx):
    n=1<<m; a=F(1,1<<r); b=F(1,1<<s); d=F(1,n); root=F(1,1<<(m//2)); pi=(1-a,a*(1-b),a*b)
    def seed(x): return (-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2))
    cores=[[(-1 if x==p else 1)*seed(x) for x in range(n)] for p in (-1,0,vtx)]
    vals=[]
    for x in range(1<<(m+1+r+s)):
        data=x&(n-1); z=-1 if (x>>m)&1 else 1
        aa=((x>>(m+1))&((1<<r)-1))==0
        bb=((x>>(m+1+r))&((1<<s)-1))==0
        vals.append(z*cores[0 if not aa else 2 if bb else 1][data])
    fw=walsh(vals); actual=Counter(F(abs(x),len(fw)) for x in fw)
    expected=Counter()
    for t in (-1,1):
        for u in (-1,1): expected[abs(root-2*d*(pi[1]*t+pi[2]*u))]+=int(F(n,4)+F(1<<(m//2),4)*(t+u))
    expected[2*a*d]+=int(F(n,2)*(1/a-1))
    expected[2*a*d*abs(1-2*b)]+=int(F(n,2)*(1/a-1))
    expected[4*a*b*d]+=int(F(n,2)*(1/a)*(1/b-1))
    expected[F(0)]+=int(F(n,2)*(1/a)*(1/b-1))+len(fw)//2
    assert actual==expected,(m,r,s,vtx,'spectrum')
    core_inf=[1+influence(walsh(g)) for g in cores]
    ic=2*r*a*d+4*s*a*b*d
    assert influence(fw)==ic+sum((p*i for p,i in zip(pi,core_inf)),F(0))
    adj=int(vtx.bit_count()==1)
    for j,k,pred in [(0,1,2*m*d),(0,2,2*m*d),(1,2,4*(m-adj)*d)]:
        assert influence(walsh([x*y for x,y in zip(cores[j],cores[k])]))==pred
    return dict(m=m,r=r,s=s,v=vtx,truth_table_size=len(vals),result='PASS')

def main():
    start=time.monotonic(); rows=[]
    with (OUT/'interval_cases.jsonl').open('w',encoding='utf-8') as out:
        for m in range(4,21,2):
            for r in range(1,5):
                for s in range(1,5):
                    for row in quantities(m,r,s): rows.append(row); out.write(json.dumps(row)+'\n'); out.flush()
            assert time.monotonic()-start<60,'pilot runtime limit'
    fixtures=[direct(m,r,s,v) for m in (4,6) for r in (1,2) for s in (1,2) for v in (1,3)]
    (OUT/'direct_fixtures.json').write_text(json.dumps(fixtures,indent=2)+'\n',encoding='utf-8')
    result=dict(helper_version='A021-coherent-reserve-v1',reserve_cases=len(rows),direct_fixtures=len(fixtures),log_series_terms=K,outward_dyadic_bits=BITS,elapsed_seconds=time.monotonic()-start,result='PASS')
    (OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); print(json.dumps(result))
if __name__=='__main__': main()
