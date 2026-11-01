from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1];start=time.monotonic();count=0
def add(*xs):
    out={}
    for x in xs:
        for p,v in x.items():out[p]=out.get(p,F(0))+v
    return {p:v for p,v in out.items() if v}
def scale(x,c):return {p:v*c for p,v in x.items() if v*c}
def log(x):
    x=F(x);out={}
    for n,s in ((x.numerator,1),(x.denominator,-1)):
        p=2
        while p*p<=n:
            while n%p==0:out[p]=out.get(p,F(0))+s;n//=p
            p+=1
        if n>1:out[n]=out.get(n,F(0))+s
    return {p:v for p,v in out.items() if v}
def eq(a,b):
    global count
    count+=1;assert not add(a,scale(b,-1)),(a,b)
@lru_cache(None)
def spectrum(a):
    N=len(a)
    return tuple(F(sum(a[x]*(-1 if (x&S).bit_count()%2 else 1) for x in range(N))**2,N*N) for S in range(N))
@lru_cache(None)
def upper(p):return tuple(sum(p[T] for T in range(len(p)) if T&S==S) for S in range(len(p)))
@lru_cache(None)
def v(a):
    p=spectrum(a);q=upper(p)
    return add(*(scale(log(q[S]/p[S]),p[S]) for S in range(1,len(p)) if p[S]))
@lru_cache(None)
def rem(a,c):
    h=tuple(a[z] if y==0 else c[z] for z in range(len(a)) for y in (0,1));p=spectrum(h);q=upper(p)
    jy=scale(log(q[1]/p[1]),p[1]) if p[1] else {}
    return add(v(h),scale(jy,-1),scale(add(v(a),v(c)),-F(1,2)))
def child(a,j,b):return tuple(x for z,x in enumerate(a) if z>>j&1==b)
def drift(a,c):return add(*(add(rem(a,c),scale(add(*(rem(child(a,j,b),child(c,j,b)) for b in (0,1))),-F(1,2))) for j in range(len(a).bit_length()-1)))
@lru_cache(None)
def ln(x):
    z=(x-1)/(x+1);power=z;low=F(0)
    for j in range(48):low+=2*power/(2*j+1);power*=z*z
    return low,low+2*power/(97*(1-z*z))
def interval(x):
    low=high=F(0);a,b=ln(F(2))
    for p,vv in x.items():
        k=p.bit_length()-1;c,d=ln(F(p,1<<k));lo=k+c/b;hi=k+d/a
        if vv<0:lo,hi=hi,lo
        low+=vv*lo;high+=vv*hi
    return low,high
def sign(x):
    if not x:return 'zero'
    a,b=interval(x);assert a>0 or b<0
    return 'positive' if a>0 else 'negative'
counts={name:dict(positive=0,negative=0,zero=0) for name in ('R','GR')}
prod=json.loads((ROOT/'out/selector_main.json').read_text(encoding='utf-8'))
for am in range(16):
    for cm in range(16):
        a=tuple(1 if am>>z&1 else -1 for z in range(4));c=tuple(1 if cm>>z&1 else -1 for z in range(4))
        for name,x in (('R',rem(a,c)),('GR',drift(a,c))):counts[name][sign(x)]+=1;count+=1
for name in counts:assert counts[name]==prod['sign_counts'][name];count+=1
for w in prod['witnesses'].values():
    a=tuple(1 if w['a_mask']>>z&1 else -1 for z in range(4));c=tuple(1 if w['c_mask']>>z&1 else -1 for z in range(4))
    eq(rem(a,c),{int(p):F(x) for p,x in w['R'].items()});eq(drift(a,c),{int(p):F(x) for p,x in w['GR'].items()})
for m in range(1,7):
    a=tuple(-1 if z==0 else 1 for z in range(1<<m));c=(1,)*len(a);r=F(1,1<<m)
    eq(v(a),{2:2*m*r-4*m*r*r} if 2*m*r-4*m*r*r else {})
    eq(rem(a,c),{2:r-r*r});eq(drift(a,c),{2:m*r*r})
    assert time.monotonic()-start<60
out={'status':'PASS','ordered_pairs':256,'point_family_m':'1..6','assertions':count,'sign_counts':counts,'elapsed_seconds':time.monotonic()-start,'implementation':'standalone direct characters/direct upper sums/48-term rational logs; no production imports','independent_person_review':'PENDING','peak_memory':'unmeasured'}
(ROOT/'out/independent.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
