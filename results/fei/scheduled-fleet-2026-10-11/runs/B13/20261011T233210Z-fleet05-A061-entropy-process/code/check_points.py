from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json,time

checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b); checks+=1
def ok(v):
    global checks
    assert v; checks+=1
def factor(x):
    r={}; p=2
    while p*p<=x:
        while x%p==0: r[p]=r.get(p,0)+1; x//=p
        p+=1
    if x>1:r[x]=r.get(x,0)+1
    return r
def logs(q):
    r=defaultdict(F)
    for p,v in factor(q.numerator).items():r[p]+=v
    for p,v in factor(q.denominator).items():r[p]-=v
    return {p:v for p,v in r.items() if v}
def add(*es):
    r=defaultdict(F)
    for c,e in es:
        for p,v in e.items():r[p]+=c*v
    return {p:v for p,v in r.items() if v}
def entropy(ps):return add(*[(-q,logs(q)) for q in ps if q])
def fwht(t):
    a=list(t); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return [F(v,len(t)) for v in a]
def ins(x,i,b):return (x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)
def restrict(t,i,b):return [t[ins(x,i,b)] for x in range(len(t)//2)]
def exact_H(d):
    return add(*[(-2*(1-d)**2,logs(1-d))] if d<1 else [],(-2*d*(2-d),logs(d)))

# Rational logarithmic enclosures. z<=1/3 after dyadic reduction.
TERMS=64
def ln_unit_bounds(q):
    z=(q-1)/(q+1); z2=z*z; term=z; s=F()
    for k in range(TERMS):s+=2*term/(2*k+1);term*=z2
    rem=2*term/((2*TERMS+1)*(1-z2))
    return s,s+rem
ln2=ln_unit_bounds(F(2))
def log_bounds(q):
    assert q>0; j=0
    # Preserve tiny logarithms rather than subtracting two ln(2) enclosures.
    if F(1,2)<=q<1:
        a,b=log_bounds(1/q)
        return -b,-a
    while q<1:q*=2;j-=1
    while q>=2:q/=2;j+=1
    lo,hi=ln_unit_bounds(q)
    # Positive remainder division; integer dyadic offset added afterwards.
    return F(j)+lo/ln2[1],F(j)+hi/ln2[0]
def ib_add(*terms):
    lo=hi=F()
    for c,(a,b) in terms:
        if c>=0:lo+=c*a;hi+=c*b
        else:lo+=c*b;hi+=c*a
    return lo,hi
def Hi(d):
    ts=[(-2*d*(2-d),log_bounds(d))]
    if d<1:ts.append((-2*(1-d)**2,log_bounds(1-d)))
    return ib_add(*ts)
def Ri(n):
    d=F(1,2**(n-1));hn=Hi(d);child=Hi(2*d) if n>1 else (F(),F())
    return ib_add((1/d,hn),(-1/(2*d),child))
def Li(n):
    d=F(1,2**(n-1));q=1-2*d+2*d*d
    a,b=log_bounds(q/d**2);return 1-d+d*a,1-d+d*b

start=time.perf_counter(); functions=0; splits=0
for n in range(1,7):
    d=F(1,2**(n-1));m=1<<n
    for x0 in range(m):
        t=[-1 if x==x0 else 1 for x in range(m)];a=fwht(t);functions+=1
        eq(a[0],1-d)
        for s in range(1,m):eq(a[s],-d*(-1 if (s&x0).bit_count()%2 else 1))
        H=entropy([v*v for v in a]);eq(H,exact_H(d))
        for i in range(n):
            ap=fwht(restrict(t,i,0));am=fwht(restrict(t,i,1))
            hp=entropy([v*v for v in ap]);hm=entropy([v*v for v in am]);
            dc=add((1,H),(-F(1,2),hp),(-F(1,2),hm))
            expected=add((1,exact_H(d)),(-F(1,2),exact_H(2*d))) if n>1 else {}
            eq(dc,expected)
            influence=sum((a[s]**2 for s in range(m) if s&(1<<i)),F());eq(influence,d)
            lam={};kl={}
            for w in range(m//2):
                u,v=a[ins(w,i,0)],a[ins(w,i,1)];q=u*u+v*v;e=v*v
                eq(ap[w],u+v);eq(am[w],u-v)
                if e:
                    lam=add((1,lam),(e,logs(q/e)))
                    kl=add((1,kl),(e/d,logs(e/(d*q))))
            q0=1-2*d+2*d*d
            expectedlam=add((1,{2:d-d*d}),(d*d,logs(q0/d**2)))
            eq(lam,expectedlam)
            eq(kl,add((1,logs(1/d)),(-1/d,lam)))
            splits+=1

rows=[];previous_R=None;previous_L=None
for n in range(1,129):
    d=F(1,2**(n-1));q=1-2*d+2*d*d;qh=1-d+d*d/2
    eq(q*q-8*d*d*qh,1-4*d)
    r=Ri(n);l=Li(n)
    if n>=4:
        assert previous_R[0]>r[1],('R monotonicity interval separation',n)
        checks+=1
    if n>=5:ok(previous_L[0]>l[1])
    if n>=3:ok(r[0]>4)
    if n>=2:ok(r[1]<5)
    ok(l[1]<F(8,5))
    previous_R=r;previous_L=l
    if n<=8 or n in (16,32,64,128):
        rows.append({'n':n,'R_display':[(float(v)) for v in r],'L_display':[float(v) for v in l], 'display_only':True})
r3=Ri(3);r4=Ri(4);l3=Li(3)
ok(r3[0]>F(4867,1000));ok(r3[1]<F(4868,1000))
ok(r4[0]>F(4742,1000));ok(r4[1]<F(4743,1000))
ok(l3[0]>F(1580,1000));ok(l3[1]<F(1581,1000))
eq(add((1,logs(F(50))),(-2,logs(F(10))),(1,{2:F(1)})),{})
ok(3**9<2**16);ok(3**9>2**14);ok(10**5<2**17)
result={'status':'PASS','actual_functions':functions,'coordinate_splits':splits,'formula_dimensions':128,'exact_assertions':checks,'log_series_terms':TERMS,'arithmetics':'integer FWHT, Fraction, exact prime-log symbolic expressions, proved-remainder rational log intervals','seconds':time.perf_counter()-start,'R3_interval':list(map(str,r3)),'R4_interval':list(map(str,r4)),'Lmax_interval':list(map(str,l3)),'rows':rows,'scope':'finite validation of analytic all-dimensional theorem; numeric displays are not certificates'}
out=Path(__file__).resolve().parents[1]/'out';out.mkdir(exist_ok=True)
(out/'POINT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('R3_interval','R4_interval','Lmax_interval','rows')},indent=2))
