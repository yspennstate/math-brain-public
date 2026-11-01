from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib
root=Path(__file__).resolve().parents[1]
assert (root/'out/FROZEN_INDEPENDENT.json').exists()
start=time.perf_counter();checks=0
def ck(x):
    global checks
    assert x;checks+=1
def cell(t):
    j=0
    while t<=F(1,2):t*=2;j+=1
    return j
def direct(values,p):
    n=len(p);N=1<<n;c=[];v=[]
    for S in range(N):
        mean=F(0)
        for x in range(N):
            weight=F(1);sign=1
            for i in range(n):
                if S>>i&1:
                    weight/=2
                    if not x>>i&1:sign=-sign
                else:weight*=p[i] if x>>i&1 else 1-p[i]
            mean+=sign*weight*values[x]
        c.append(mean)
        prod=F(1)
        for i in range(n):
            if S>>i&1:prod*=4*p[i]*(1-p[i])
        v.append(prod)
    P=[v[s]*c[s]**2 for s in range(N)]
    W=[v[s]/4**cell(abs(c[s])) if s and c[s] else F(0) for s in range(N)]
    w=1-P[0];Z=sum(W)
    Q=[P[0]]+[w*W[s]/Z if w else F(0) for s in range(1,N)]
    return c,P,W,Q,w,Z
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def times(k,a):return (k*a[0],k*a[1]) if k>=0 else (k*a[1],k*a[0])
def minus(a,b):return plus(a,times(-1,b))
z=F(1,3)
lo=2*sum((z**(2*i+1)/F(2*i+1) for i in range(32)),F(0))
LN2=(lo,lo+2*z**65/(65*(1-z*z)))
@lru_cache(None)
def log(x):
    if x==1:return F(0),F(0)
    if x<1:return times(-1,log(1/x))
    j=0
    while x>=2:x/=2;j+=1
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*i+1)/F(2*i+1) for i in range(32)),F(0))
    hi=lo+2*z**65/(65*(1-z*z))
    return plus((lo,hi),times(j,LN2))
def mant(c,P):
    r=(F(0),F(0))
    for s in range(1,len(P)):
        if P[s]:r=plus(r,times(P[s],log(1/(abs(c[s])*2**cell(abs(c[s])))**2)))
    return r
def norm(d):return times(d[4],log(d[5]/d[4]))
def KL(P,Q):
    r=(F(0),F(0))
    for p,q in zip(P,Q):
        if p:r=plus(r,times(p,log(p/q)))
    return r
rows=[]
for m in range(3,27):
    t=F(1,2**m);e=1-2*t;q=(1+t)/2
    g=direct([-1,-1,-1,1],(q,q))
    f=direct([1,1,1,1,-1,-1,-1,1],(q,q,e))
    a=(1-g[0][0])/2;V=g[4]
    o=direct([1,-1,1,1],(e,1-a))
    C=F(0)
    for s in (1,2,3):
        ck(f[0][s]==e*g[0][s])
        ck(f[0][s|4]==g[0][s]/2)
        k=cell(abs(f[0][s]))-cell(e)-cell(abs(g[0][s]))
        C+=f[1][s]*k
    Do=sum((s.bit_count()-1)*o[1][s] for s in range(1,4))
    ck(C/Do==e*(1+t)/(t*(3+t)))
    ck(C/Do>=F(6,25)/t)
    Lg=mant(g[0],g[1]);Lo=mant(o[0],o[1]);Lf=mant(f[0],f[1])
    ln4C=times(2*C,LN2)
    gap=minus(minus(plus(Lo,times(e,Lg)),Lf),ln4C)
    ck(gap[0]<=0<=gap[1])
    qt=[o[3][0]]+[F(0)]*7;qt[4]=o[3][1]
    for s in (1,2,3):
        qt[s]=o[3][2]*g[3][s]/V
        qt[s|4]=o[3][3]*g[3][s]/V
    ck(sum(qt)==1 and qt[0]==f[1][0])
    Ktree=KL(f[1],qt);Kg=KL(g[1],g[3]);Ko=KL(o[1],o[3])
    gap=minus(Ktree,plus(Ko,times(e,Kg)))
    ck(gap[0]<=0<=gap[1])
    transfer=minus(KL(f[1],f[3]),Ktree)
    bill=minus(minus(plus(ln4C,norm(f)),norm(o)),times(e,norm(g)))
    gap=minus(transfer,bill);ck(gap[0]<=0<=gap[1])
    if m>=8:ck(transfer[1]<0)
    if m>=16:
        ck(ln4C[0]>=F(999,1000)*Lg[1])
        ck(ln4C[1]<=F(1001,1000)*Lg[0])
    rows.append({'m':m,'transfer_upper_is_negative':transfer[1]<0,'carry_over_outer_deficit':str(C/Do),'carry_debit_over_seed_mantissa_between_0.999_and_1.001':m>=16})
out={'status':'PASS','exact_assertions':checks,'cases':len(rows),'runtime_seconds':time.perf_counter()-start,'arithmetic':'direct physical alternating sums; Fraction; 32-term atanh log intervals, range-reduced z<=1/3 with analytic tail bound','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
(root/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
