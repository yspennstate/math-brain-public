from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];START=time.monotonic();N=0;C=Q(21,4)
def ck(v):
    global N
    assert v
    N+=1
    assert time.monotonic()-START<60
def plus(*pairs):
    z={}
    for c,e in pairs:
        for k,v in e.items():z[k]=z.get(k,Q(0))+c*v
    return {k:v for k,v in z.items() if v}
def fac(n):
    z={};p=2
    while p*p<=n:
        while n%p==0:z[p]=z.get(p,0)+1;n//=p
        p+=1
    if n>1:z[n]=z.get(n,0)+1
    return z
def lg(q):return plus((1,fac(q.numerator)),(-1,fac(q.denominator)))
def eta(q):return plus((-q,lg(q))) if q else {}
@lru_cache(None)
def hat(f):return tuple(Q(sum(v*(-1 if (a&j).bit_count()%2 else 1) for j,v in enumerate(f)),len(f)) for a in range(len(f)))
def P(f):return tuple(v*v for v in hat(f))
def H(f):return plus(*[(1,eta(z)) for z in P(f)])
def I(f):return Q(sum(f[j]!=f[j^(1<<i)] for j in range(len(f)) for i in range(len(f).bit_length()-1)),len(f))
def restrict(f,i,b):
    n=len(f).bit_length()-1
    return tuple(f[(j&((1<<i)-1))+(b<<i)+((j>>i)<<(i+1))] for j in range(1<<(n-1)))
def activate(v,a):return tuple(v[j] if x==-1 else 1 for x in a for j in range(len(v)))
def D(p,q):return plus(*[(z,lg(z/r)) for z,r in zip(p,q) if z])
def ln(q):
    y=(q-1)/(q+1);v=sum((2*y**(2*j+1)/(2*j+1) for j in range(32)),Q(0))
    return v,v+2*y**65/(65*(1-y*y))
LN2=ln(Q(2))
@lru_cache(None)
def lb(k):
    x=Q(k);a=0
    while x>=2:x/=2;a+=1
    lo,hi=ln(x);return a+lo/LN2[1],a+hi/LN2[0]
def bounds(e):
    lo=hi=Q(0)
    for k,c in e.items():
        a,b=lb(k);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
    return lo,hi
def enc(e):return {'prime_log':{str(k):str(v) for k,v in e.items()},'interval':[str(v) for v in bounds(e)]}
def num(q):return {2:Q(q)} if q else {}
ck(Q(842,1215)>Q(9,13));ck(Q(25,36)<Q(3,4))
ck(Q(1,64)-Q(9,1792)-Q(1,96)==Q(1,5376))
for k in [Q(0),Q(1,64),Q(1,2),Q(1)]:
    for lam in [Q(1,2),Q(1),Q(2)]:
        ell=lam*k/(1+(lam-1)*k)
        d=D((1-k,k),(1-ell,ell))
        ck(d==plus((1,lg(1+(lam-1)*k)),(-k,lg(lam))))
        ck(bounds(plus((1,num(Q(4,9)*k)),(-1,d)))[0]>=0)
v=(-1,)+(1,)*7;a=(1,-1,-1,-1);f=activate(v,a);p=P(f)
gamma=Q(1,8);va=Q(3,4);owner=gamma*va
ck(owner/4*Q(4,9)==Q(1,96));ck(owner<=gamma*I(a))
for theta in [Q(0),Q(1,8)]:
    ra=tuple(z if j==0 else z*(1-theta+3*theta*(j==1)) for j,z in enumerate(P(a)))
    T=plus((gamma,D(P(a),ra)))
    for mode in range(3):
        rho=[Q(0)]*32;cost={}
        for t in range(8):
            q=sum(p[t+8*u] for u in range(4));k=sum(p[t+8*u] for u in range(1,4))/q
            lam=[Q(1,2),Q(1),Q(2)][(mode+t)%3]
            ell=lam*k/(1+(lam-1)*k);rho[t]=q*(1-ell)
            for u in range(1,4):rho[t+8*u]=q*ell*ra[u]/va
            cost=plus((1,cost),(q,D((1-k,k),(1-ell,ell))))
        ck(sum(rho)==1);ck(D(p,rho)==plus((1,T),(1,cost)))
        ck(bounds(plus((1,num(Q(4,9)*owner)),(-1,cost)))[0]>=0)
        ck(bounds(plus((1,T),(1,num(Q(4,9)*owner)),(-1,D(p,rho))))[0]>=0)
        for i in [0,3]:
            ch=[restrict(f,i,b) for b in (0,1)]
            childetas=[]
            for b in (0,1):
                vv=restrict(v,i,b) if i==0 else v
                aa=restrict(a,0,b) if i==3 else a
                childetas.append(Q(vv.count(-1),len(vv))*(1-hat(aa)[0]**2))
            release=owner-sum(childetas)/2
            ck(release==(0 if i==0 else gamma*hat(a)[1]**2))
out={'status':'PASS','assertions':N,'elapsed_seconds':time.monotonic()-START,'scope':'Separate direct-character fixture, row KL, scalar envelope, eta DATA/CONTROL release, exact residual; no main checker import','sharpness':'Analytic limit only; finite checks do not establish sharpness'}
(R/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
