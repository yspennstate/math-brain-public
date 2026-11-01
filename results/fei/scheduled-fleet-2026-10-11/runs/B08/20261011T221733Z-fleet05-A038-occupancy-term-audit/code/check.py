from fractions import Fraction as F
from math import comb
from pathlib import Path
from functools import lru_cache
import json,time,hashlib

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0
def check(b):
    global assertions
    assertions+=1
    assert b
def walsh(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a
@lru_cache(None)
def factors(n):
    out={}; k=2
    # Residual composite integers are exact formal log atoms; zero cancellation
    # remains a sufficient identity certificate without prime factorization.
    while k*k<=n and k<=1000:
        while n%k==0: out[k]=out.get(k,0)+1; n//=k
        k=3 if k==2 else k+2
    if n>1: out[n]=out.get(n,0)+1
    return out
def logform(x):
    z={}
    for n,s in [(x.numerator,1),(x.denominator,-1)]:
        for p,e in factors(n).items(): z[p]=z.get(p,0)+s*e
    return {p:e for p,e in z.items() if e}
def addlog(z,x,c):
    if not c:return
    for p,e in logform(x).items(): z[p]=z.get(p,F(0))+c*e
def clean(z):return {p:c for p,c in z.items() if c}
def entropy(law):
    z={}
    for p in law:
        if p:addlog(z,p,-p)
    return clean(z)
def divergence(p,q):
    z={}
    for a,b in zip(p,q):
        if a:check(b>0);addlog(z,a/b,a)
    return clean(z)
def linear(*terms):
    z={}
    for c,t in terms:
        for p,a in t.items():z[p]=z.get(p,F(0))+c*a
    return clean(z)
def ln_base(x,n=20):
    t=(x-1)/(x+1); s=F(0); power=t
    for j in range(n):s+=2*power/(2*j+1);power*=t*t
    tail=2*power/((2*n+1)*(1-t*t))
    return s,s+tail
L2=ln_base(F(2))
@lru_cache(None)
def log2_interval(x):
    check(x>0);k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    a,b=ln_base(x)
    return F(k)+a/L2[1],F(k)+b/L2[0]
def interval_entropy(weighted):
    lo=hi=F(0)
    for count,p in weighted:
        if p:
            a,b=log2_interval(1/p);lo+=count*p*a;hi+=count*p*b
    return lo,hi
def outward(pair):
    scale=10**12;a,b=pair
    return [str(F((a*scale).__floor__(),scale)),str(F((b*scale).__ceil__(),scale))]

rows=[]
for m in range(2,17):
    N=2**m;d=F(2,N);v=2*d-d*d;r=d/v;c=F(N-1,N)
    check(c*r==F(1,2));check(1-c==(1-c*r)**m)
    check((N-1)*d*d==v);check(d*d/v==F(1,N-1))
    I=m*d;a=4*d*(1-d)
    vk=[F(1)]+[a**k*(1-F(2)**(2-k)*(1-d)**(m-k))**2 for k in range(1,m+1)]
    for k in range(1,m+1):check(0<=vk[k]<=a**k<=1)
    Z=sum(F(comb(m,k))*vk[k] for k in range(m+1))
    check(1<=Z<=(1+a)**m)
    L=interval_entropy([(comb(m,k),vk[k]) for k in range(1,m+1)])
    T=tuple(t/Z for t in L); ratio=tuple(t/(4*I) for t in T)
    H=interval_entropy([(1,(1-d)**2),(N-1,d*d)])
    Bh=interval_entropy([(m,d),(m,1-d)])
    K=(Bh[0]-H[1],Bh[1]-H[0])
    check(H[1]<=4*I)
    if m>=8:
        check((8*m-3)*(m-1)*d<=F(427,128))
        check(ratio[0]>m-7)
    if m==16:check(ratio[0]>8);check(K[0]>8*I)
    if m<=8:
        table=[-1]+[1]*(N-1);raw=walsh(table)
        check(raw==[N-2]+[-2]*(N-1))
        p=[F(x*x,N*N) for x in raw]
        check(sum(p)==1)
        di=[sum(p[s] for s in range(N) if s&(1<<i)) for i in range(m)]
        check(di==[d]*m)
        edge=sum(table[x]!=table[x^(1<<i)] for i in range(m) for x in range(N))
        check(F(edge,N)==I)
        q=[d**s.bit_count()*(1-d)**(m-s.bit_count()) for s in range(N)]
        pp=[F(0)]+[x/v for x in p[1:]]
        qr=[F(0)]+[F(1,N-1)]*(N-1)
        check(pp==qr);check(divergence(pp,qr)=={})
        mix=[1-v]+[v*x for x in qr[1:]]
        check(mix==p)
        Delta=linear((m,entropy([d,1-d])),(-1,entropy([v,1-v])),(-v,entropy(qr)))
        check(Delta==divergence(mix,q))
        check(divergence(p,q)==linear((v,divergence(pp,qr)),(1,Delta)))
        cd=1-q[0];qplus=[F(0)]+[x/cd for x in q[1:]]
        corr=linear((1,divergence([v,1-v],[cd,1-cd])),(v,divergence(qr,qplus)))
        check(corr==Delta)
        lifted=[table[x%N]*(1 if x<N else -1) for x in range(2*N)]
        lr=walsh(lifted);lp=[F(x*x,4*N*N) for x in lr]
        check(lp[:N]==[0]*N);check(lp[N:]==p)
        check(sum(lifted)==0)
        # The fresh mandatory character makes the nonempty I-projection Qd itself.
        lq=[F(0)]*N+q
        check(divergence(lp,lq)==divergence(p,q))
        if m<=7:
            for U in range(1,N):
                k=U.bit_count();outside=((N-1)^U);s=F(0)
                for S in range(N):
                    j=(S&outside).bit_count()
                    eps=(1 if S==0 else -1)*(1 if (S^U)==0 else -1)
                    s+=eps*d**j*(1-d)**(m-k-j)
                check((d*(1-d))**k*s*s==vk[k])
    rows.append({'m':m,'I':str(I),'v':str(v),'K_occ':'0 exact','K_full_over_I':outward((K[0]/I,K[1]/I)),'T_over_4I':outward(ratio)})

# Source-exact OR(literal,AND) Walsh control; no numerical root is used as proof.
check(walsh([1,-1,1,-1,1,-1,-1,-1])==[-2,6,2,2,2,2,-2,-2])
result={'status':'PASS','assertions':assertions,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer/Fraction and rigorous rational logarithm intervals','frozen_domain_completed':True,'rows':rows}
(ROOT/'out'/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}));print('m16',json.dumps(rows[-1]))
