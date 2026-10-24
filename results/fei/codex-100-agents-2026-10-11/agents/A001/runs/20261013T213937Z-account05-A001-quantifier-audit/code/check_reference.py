from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import json, time

RUN=Path(__file__).resolve().parents[1]
assert json.loads((RUN/'out/FROZEN_SPEC.json').read_text())['case_count']==8
checks=0
def check(v):
    global checks
    checks+=1
    assert v, checks
def ln_unit(q):
    z=(q-1)/(q+1); s=sum((z**(2*j+1)/F(2*j+1) for j in range(24)),F(0))*2
    return s,s+2*z**49/(49*(1-z*z))
LN2=ln_unit(F(2))
@lru_cache(None)
def log2(q):
    q=F(q); k=0
    while q<1:q*=2;k-=1
    while q>=2:q/=2;k+=1
    lo,hi=ln_unit(q)
    corners=[a/b+k for a in (lo,hi) for b in LN2]
    scale=1<<70
    low=min(corners)*scale; high=max(corners)*scale
    return F(low.numerator//low.denominator,scale),F(-((-high.numerator)//high.denominator),scale)
def entropy(masses):
    lo=hi=F(0)
    for p in masses:
        if p:
            a,b=log2(1/p);lo+=p*a;hi+=p*b
    return lo,hi
def phi(x,y):
    if not x or not y:return F(0),F(0)
    a,b=log2((x+y)/x); c,d=log2((x+y)/y)
    return x*a+y*c,x*b+y*d
def walsh(values):
    w=values[:];step=1
    while step<len(w):
        for b in range(0,len(w),2*step):
            for j in range(b,b+step):
                u,v=w[j],w[j+step];w[j]=u+v;w[j+step]=u-v
        step*=2
    return w
def audit(values):
    n=(len(values)-1).bit_length(); N=len(values)
    w=walsh(values); p=[F(a*a,N*N) for a in w]
    check(sum(p)==1)
    eps=[];rows=[]
    for i in range(n):
        bit=1<<i
        flip=F(sum(values[x]!=values[x^bit] for x in range(N)),N)
        spectral=sum(p[s] for s in range(N) if s&bit)
        check(flip==spectral);eps.append(flip)
        # Reconstruct the actual ternary derivative on its own residual cube.
        deriv=[F(values[(x&(bit-1))|((x>>(i))<<(i+1))]-values[(x&(bit-1))|((x>>(i))<<(i+1))|bit],2) for x in range(N//2)]
        check(all(h in (-1,0,1) for h in deriv))
        check(F(sum(h!=0 for h in deriv),N//2)==flip)
        dw=walsh(deriv)
        for t,a in enumerate(dw):
            s=(t&(bit-1))|((t>>i)<<(i+1))|bit
            check(a*2==w[s])
        rows.append(sum(p[s] for s in range(N) if s&bit and s.bit_count()>=3))
    I=sum(eps);B0=B1=F(0)
    for i in range(n):
        for s in range(N):
            if not s&(1<<i):
                a,b=phi(p[s],p[s|(1<<i)]);B0+=a;B1+=b
    return p,eps,I,(B0,B1),rows

t0=time.perf_counter();out=[]
for r in (4,6,8,10):
    n=r+3;N=1<<n;delta=F(1,1<<r)
    values=[(-1 if ((x>>r).bit_count()&1) else 1) if (x&((1<<r)-1))==0 else 1 for x in range(N)]
    p,eps,I,B,rows=audit(values)
    check(eps==[delta]*n);check(I==n*delta)
    for s in range(N):
        target=(1-delta)**2 if s==0 else delta**2 if (s>>r) in (0,7) else F(0)
        check(p[s]==target)
    W=sum(p[1:]);check(W==2*delta-delta*delta)
    for i in range(r,n):
        check(rows[i]==delta)
        check(2*delta*(r+1)<1)
    Z=(1+delta)**n-1;check(Z>=delta)
    check(sum(delta**s.bit_count()/Z for s in range(1,N))==1)
    zlo,zhi=log2(Z)
    X=(r*I+W*zlo,r*I+W*zhi)
    check(X[0]/I>=r-F(2*r,r+3))
    H=entropy(p);check(H[1]<4*I);check(B[1]<4*I)
    check(H[0]<=entropy([p[0]])[1]+2*r*W and H[1]>=entropy([p[0]])[0]+2*r*W)
    out.append(dict(family='activated_parity3',r=r,I=str(I),row_tail=str(rows[-1]),X_over_I_interval=[str(v/I) for v in X],reference_lower_bound=str(r-F(2*r,r+3)),H_over_I_upper=str(H[1]/I),B_over_I_upper=str(B[1]/I)))
for n in (2,4,6,8):
    N=1<<n
    values=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(n//2)) for x in range(N)]
    p,eps,I,B,rows=audit(values)
    check(p==[F(1,N)]*N);check(eps==[F(1,2)]*n);check(I==F(n,2));check(B==(F(n),F(n)))
    weighted=sum(s.bit_count()*p[s]*n for s in range(N));check(weighted==n*I)
    row_entropy=sum(eps)*(n-1);check(row_entropy/I==n-1)
    R=F(n)-F(n*n*2,N);check(R>=0)
    out.append(dict(family='quadratic_bent',n=n,I=str(I),B_over_I='2',weighted_entropy_over_I=str(weighted/I),derivative_entropy_over_I=str(row_entropy/I),R_ge2=str(R)))
result=dict(status='PASS',failures=0,assertions=checks,cases=8,runtime_seconds=time.perf_counter()-t0,rows=out,full_FEI='OPEN',arithmetic='Integer/Fraction outward log intervals; no floating sign decision')
(RUN/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
