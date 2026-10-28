from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,time

root=Path(__file__).resolve().parents[1]
t0=time.monotonic(); assertions=0
def check(ok):
    global assertions
    assertions+=1
    if not ok:raise AssertionError(assertions)
    if time.monotonic()-t0>55:raise RuntimeError('frozen 55-second cap')

def fwht(f):
    a=f[:];h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def reflected(mask,n,sigma):
    return sum(((mask>>(x^sigma))&1)<<x for x in range(1<<n))

def essential(f,n):
    return all(any(f[x]!=f[x^(1<<i)] for x in range(1<<n)) for i in range(n))

def isprime(mask,n):
    for block in range(1,1<<n):
        if not 2<=block.bit_count()<n:continue
        inner=[i for i in range(n) if block>>i&1]
        outer=[i for i in range(n) if not block>>i&1]
        rows=set()
        for u in range(1<<len(inner)):
            inside=sum(((u>>k)&1)<<i for k,i in enumerate(inner))
            row=0
            for v in range(1<<len(outer)):
                outside=sum(((v>>k)&1)<<i for k,i in enumerate(outer))
                row|=((mask>>(inside|outside))&1)<<v
            rows.add(row)
            if len(rows)>=3:break
        if len(rows)<3:return False
    return True

def jscale(c):
    if not c:return 0
    c=abs(c);j=0
    while 2*c<=1:c*=2;j+=1
    return j

def biased(f,p):
    a=list(map(Q,f))
    for i,pi in enumerate(p):
        for x in range(len(a)):
            if x>>i&1:continue
            lo,hi=a[x],a[x|(1<<i)]
            a[x]=(1-pi)*lo+pi*hi
            a[x|(1<<i)]=(hi-lo)/2
    return a

small=[]
for n in (3,4):
    size=1<<n; allbits=(1<<size)-1
    base=sum((x.bit_count()>=2)<<x for x in range(size))
    qs=[reflected(base,n,s) for s in range(size)]
    qws=[fwht([1 if q>>x&1 else -1 for x in range(size)]) for q in qs]
    forbidden=[{q,q^allbits}|{reflected(q,n,1<<i) for i in range(n)} for q in qs]
    high=[s for s in range(size) if s.bit_count()>=2]
    num=0;primechecks=0;max_examined=0
    for mask in range(1<<size):
        f=[1 if mask>>x&1 else -1 for x in range(size)]
        if not essential(f,n):continue
        num+=1;w=fwht(f);chosen=None;examined=0
        for sigma,q in enumerate(qs):
            if mask in forbidden[sigma]:continue
            examined+=1
            outward=[s for s in high if w[s] and abs(w[s])&(abs(w[s])-1)==0
                     and abs(qws[sigma][s])>abs(w[s]) and qws[sigma][s]*w[s]>0]
            if not outward:chosen=sigma;break
        check(chosen is not None)
        max_examined=max(max_examined,examined)
        if n==3:
            check(isprime(mask|(qs[chosen]<<size),n+1));primechecks+=1
    expected=sum((-1)**k*comb(n,k)*(1<<(1<<(n-k))) for k in range(n+1))
    check(num==expected)
    small.append(dict(n=n,all_tables=1<<size,essential=num,zero_jump_completion=num,
                      completed_prime_checks=primechecks,max_candidates_examined=max_examined))

n=5;size=32;mask=1
f=[1 if x==0 else -1 for x in range(size)]
a=biased(f,[Q(1,2)]*5)
base=sum((x.bit_count()>=2)<<x for x in range(size))
high=[s for s in range(size) if s.bit_count()>=2]
M=sum(a[s]**2 for s in high);Jseed=sum(a[s]**2*jscale(a[s]) for s in high)
check(M==Q(26,256));check(Jseed==Q(104,256))
fixtures=[]
for sigma in range(size):
    qmask=reflected(base,n,sigma)
    q=[1 if qmask>>x&1 else -1 for x in range(size)]
    b=biased(q,[Q(1,2)]*5)
    check(mask not in {qmask,qmask^((1<<32)-1)}|{reflected(qmask,5,1<<i) for i in range(5)})
    check(isprime(mask|(qmask<<32),6))
    jump={s for s in high if a[s]*(b[s]-a[s])>0}
    r=sigma.bit_count()
    predicted=r*(5-r)+(r if r%2 else 5-r)+(0 if r%2 else 1)
    check(len(jump)==predicted)
    d=sum(a[s]**2 for s in jump)
    check(d==Q(predicted,256))
    A=B=C=Q(0)
    for s in high:
        jj=jscale(a[s])-(s in jump);h=b[s]-a[s]
        A+=a[s]**2*jj;B+=2*a[s]*h*jj;C+=h*h*jj
    for s in range(1,size):
        h=b[s]-a[s];jj=jscale(h/2)
        B+=h*h*jj;C-=h*h*jj
    check(A==Jseed-d)
    Wlimit=[Q(0)]*size
    for s in high:Wlimit[s]=a[s]**2*(4 if s in jump else 1)
    Zlimit=sum(Wlimit)
    check(Zlimit==M+3*d)
    Qlimit=[a[s]**2 if s.bit_count()<2 else M*Wlimit[s]/Zlimit for s in range(size)]
    check(sum(Qlimit)==1)
    for e in (Q(1,16),Q(1,256),Q(1,4096)):
        g=f+q;cs=biased(g,[Q(1,2)]*5+[e])
        vs=[Q(1)]*32+[4*e*(1-e)]*32
        P=[vs[s]*cs[s]**2 for s in range(64)]
        for s in range(size):
            check(cs[s]==(1-e)*a[s]+e*b[s])
            check(cs[s+size]==(b[s]-a[s])/2)
        check(sum(P)==1)
        J=sum(P[s]*jscale(cs[s]) for s in range(64) if s.bit_count()>=2)
        check(J==A+B*e+C*e*e)
        for s in high:check(jscale(cs[s])==jscale(a[s])-(s in jump))
        Hmass=sum(P[s] for s in range(64) if s.bit_count()>=2)
        W=[vs[s]*Q(1,4)**jscale(cs[s]) if cs[s] and s.bit_count()>=2 else Q(0) for s in range(64)]
        Z=sum(W)
        reference=[P[s] if s.bit_count()<2 else Hmass*W[s]/Z for s in range(64)]
        check(sum(reference)==1)
        for s in range(64):
            if P[s] and s.bit_count()>=2:
                check(P[s]/reference[s]==cs[s]**2*4**jscale(cs[s])*Z/Hmass)
        If=Q(5,16);Iq=Q(5,4)
        disagree=Q(sum(x!=y for x,y in zip(f,q)),32)
        actualI=sum(s.bit_count()*P[s] for s in range(64))
        check(actualI==(1-e)*If+e*Iq+4*e*(1-e)*disagree)
    fixtures.append(dict(sigma=sigma,reflection_weight=r,outward_atoms=predicted,
                         jump_mass=str(d),Jseed_over_ln4=str(Jseed),Jlimit_over_ln4=str(A),
                         quadratic_J_coefficients=list(map(str,(A,B,C))),Zlimit=str(Zlimit)))
check(min(x['outward_atoms'] for x in fixtures)==5)
out=dict(status='PASS',assertions=assertions,seconds=time.monotonic()-t0,small_core_exhaustion=small,
         point_core_reflections=fixtures,biased_fixtures=96,arithmetic='integer Walsh, physical cofactor transform and exact Fraction references')
(root/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','assertions','seconds','small_core_exhaustion','biased_fixtures']}))
