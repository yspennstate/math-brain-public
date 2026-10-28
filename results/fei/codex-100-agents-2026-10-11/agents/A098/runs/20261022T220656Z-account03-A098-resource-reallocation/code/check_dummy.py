from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,sys,hashlib,itertools
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
start=time.monotonic(); checks=0
def ck(v):
    global checks
    checks+=1
    assert v,checks
    assert time.monotonic()-start<55,'runtime cap'
def lnunit(x):
    z=(x-1)/(x+1)
    low=2*sum((z**(2*k+1)/F(2*k+1) for k in range(16)),F(0))
    return low,low+2*z**33/(33*(1-z*z))
L2=lnunit(F(2))
@lru_cache(maxsize=5000)
def log2(x):
    ck(x>0)
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/F(2)**k
    if y<1:y*=2;k-=1
    ck(1<=y<2)
    if y==1:return F(k),F(k)
    lo,hi=lnunit(y)
    return k+lo/L2[1],k+hi/L2[0]
def plus(x,y):return x[0]+y[0],x[1]+y[1]
def scale(x,c):return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def ce(p,q):
    z=(F(0),F(0))
    for u,v in zip(p,q):
        if u: ck(v>0);z=plus(z,scale(log2(v),-u))
    return z
def pairs(N,j):
    return [(x,x|(1<<j)) for x in range(N) if not x&(1<<j)]
def marginal(q,j):return [q[x]+q[y] for x,y in pairs(len(q),j)]
def calibrate(q,z):
    ck(sum(q)==1 and q[0]<1)
    return [z]+[x*(1-z)/(1-q[0]) for x in q[1:]]
def spectral(a,b,r):
    m=a+b+r;N=1<<m
    truth=[1-2*(x%(1<<a)==0)+2*(x==0) for x in range(N)]
    w=truth[:];h=1
    while h<N:
        for j in range(0,N,2*h):
            for k in range(j,j+h):u,v=w[k],w[k+h];w[k],w[k+h]=u+v,u-v
        h*=2
    amp=[F(x,N) for x in w];p=[x*x for x in amp]
    ck(sum(p)==1)
    for j in range(m):
        direct=F(sum(truth[x]!=truth[x^(1<<j)] for x in range(N)),N)
        ck(direct==sum(p[x] for x in range(N) if x&(1<<j)))
    return amp,p
def floor(a,b,r,R,amp,p):
    n=a+b;s=F(1,1<<a);t=F(1,1<<n);e=F(2,1<<(n+r));mu=1-2*s
    M=[sum(p[T+(U<<n)] for U in range(1<<r)) for T in range(1<<n)]
    re=[(1-e/s)*R[T]+(e/s)*mu*(T==0)+2*e*t for T in range(1<<n)]
    ck(sum(re)==1 and min(re)>0 and min(M)>0)
    q=[re[S%(1<<n)]*p[S]/M[S%(1<<n)] for S in range(len(p))]
    ck(sum(q)==1)
    return q
pilot='--pilot' in sys.argv
domain=[(1,1,1)] if pilot else list(itertools.product([1,2,3],[1,2],[1,2]))
rows=[];rootcount=0
for a,b,r in domain:
    n=a+b;s=F(1,1<<a);mu=1-2*s;e=F(2,1<<(n+r));N=1<<(n+r)
    P=[mu*mu]+[4*s*s if T<(1<<a) else F(0) for T in range(1,1<<n)]
    amp,p=spectral(a,b,r)
    for mode in ['matching','asymmetric','off_support_spiked']:
        weights=[F(0)]+[F((13*T+7)%17+1) for T in range(1,1<<n)]
        if mode=='off_support_spiked':weights[1<<a]=F(10000)
        R=P[:] if mode=='matching' else [P[0]]+[(1-P[0])*x/sum(weights) for x in weights[1:]]
        q=floor(a,b,r,R,amp,p);c=ce(P,R);rootcount+=1
        ck(ce(p,q)[1]<=c[0]+10*e*(n+r))
        for j in range(a,n):
            V=marginal(R,j);Rn=calibrate(V,mu*mu)
            Pn=[mu*mu]+[4*s*s if T<(1<<a) else F(0) for T in range(1,1<<(n-1))]
            ck(all(Rn[T]>=R[T] for T in range(1<<a)))
            ck(sum(Rn)==1)
            pp=pairs(N,j); on=[(amp[x]+amp[y])**2 for x,y in pp];off=[(amp[x]-amp[y])**2 for x,y in pp]
            qi=marginal(q,j)
            ck(sum(on)==sum(off)==sum(qi)==1)
            ck(off==Pn+[F(0)]*(len(off)-len(Pn)))
            aa,pa=spectral(a,b-1,r);ck(pa==on)
            qn=floor(a,b-1,r,Rn,aa,pa)
            h=e/s
            for T,u in enumerate(Pn):
                if u:
                    if T==0:ck(qi[0]>=R[0])
                    else:ck(qi[T]>=(1-h)*R[T]/(1+h/2))
            B=(F(0),F(0));absprod=F(0)
            for x,y in pp:
                u,v=p[x],p[y];absprod+=abs(amp[x]*amp[y])
                if u and v:B=plus(B,ce([u,v],[u/(u+v),v/(u+v)]))
            ck(absprod==e*(4-4*s+2*e-2*e/s));ck(absprod<=4*e)
            ck(B[1]<12*e)
            co=ce(off,qi);ck(co[1]-c[0]<11*e)
            cn=ce(Pn,Rn)
            # Pointwise dominance certifies cn<=c without overlapping-interval comparisons.
            Wn=plus(cn,(20*e*(n+r-1),)*2)
            local=plus(B,scale(plus(co,Wn),F(1,2)))
            ck(local[1]<c[0]+10*e*(n+r)+8*e)
            ck(ce(on,qn)[1]<=Wn[0])
            rows.append({'a':a,'b':b,'r':r,'reference':mode,'label':j,'e':str(e),'local_excess_upper':str(local[1]-c[0]-10*e*(n+r))})
    (OUT/('PILOT_CHECKPOINT.json' if pilot else 'CHECKPOINT.json')).write_text(json.dumps({'roots':rootcount,'queries':len(rows),'assertions':checks}),encoding='utf-8')
ck(L2[0]>F(2,3))
result={'status':'PASS','pilot':pilot,'physical_roots':len(domain),'reference_roots':rootcount,'dummy_queries':len(rows),'assertions':checks,'elapsed_seconds':time.monotonic()-start,'arithmetic':'exact Fraction / outward rational logarithm intervals','scope':'local dummy extension only; global mixed history uses imported active/control theorems','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/('PILOT_RESULT.json' if pilot else 'RESULT.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
(OUT/('PILOT_ROWS.json' if pilot else 'ROWS.json')).write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps(result))
