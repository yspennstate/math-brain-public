"""Direct characters and physical branching; imports no main or prior helper."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time
RUN=Path(__file__).resolve().parents[1];START=time.monotonic();N=0
def ck(v):
    global N
    assert v
    N+=1
    assert time.monotonic()-START<60
def plus(*pairs):
    d={}
    for c,e in pairs:
        for k,v in e.items():d[k]=d.get(k,Q(0))+c*v
    return {k:v for k,v in d.items() if v}
def factor(n):
    z={};p=2
    while p*p<=n:
        while n%p==0:z[p]=z.get(p,0)+1;n//=p
        p+=1
    if n>1:z[n]=z.get(n,0)+1
    return z
def log(q):return plus((1,factor(q.numerator)),(-1,factor(q.denominator)))
def eta(q):return plus((-q,log(q))) if q else {}
def E(q):return eta(q*q)
@lru_cache(None)
def H(f):
    e={};mass=Q(0)
    for a in range(len(f)):
        z=Q(sum(v*(-1 if (j&a).bit_count()%2 else 1) for j,v in enumerate(f)),len(f))
        mass+=z*z;e=plus((1,e),(1,eta(z*z)))
    ck(mass==1);return e
def meanneg(f):return Q(f.count(-1),len(f))
def restricted(f,fixed):
    fixed=dict(fixed);free=[j for j in range(len(f).bit_length()-1) if j not in fixed]
    base=sum(b<<j for j,b in fixed.items())
    return tuple(f[base+sum(((k>>i)&1)<<j for i,j in enumerate(free))] for k in range(1<<len(free)))
def inf(f,i):return Q(sum(f[j]!=f[j^(1<<i)] for j in range(len(f))),len(f))
def I(f):return sum((inf(f,j) for j in range(len(f).bit_length()-1)),Q(0))
@lru_cache(None)
def G(r,d):
    if r==0:return {}
    p=Q(1,1<<r);V=4*p*(1-p)
    nonempty=plus((1,H((-1,)+(1,)*((1<<r)-1))),(-1,E(1-2*p)))
    return plus((d,nonempty),(4*d*(1-d),eta(p*p)),(2*d*(1-d)*V,{2:Q(1)}),(V,E(d)),(1,E(1-2*p*d)),(-p,E(1-2*d)))
def Gp(r,t):
    if r==0:return {}
    p=Q(1,1<<r);V=4*p*(1-p)
    ck(-2*V*t+4*p*(1-2*p*t)-4*p*(1-2*t)==0)
    nonempty=plus((1,H((-1,)+(1,)*((1<<r)-1))),(-1,E(1-2*p)))
    return plus((1,nonempty),(4*(1-2*t),eta(p*p)),(2*(1-2*t)*V,{2:Q(1)}),(-4*V*t,log(t)),(8*p*(1-2*p*t),log(1-2*p*t)),(-8*p*(1-2*t),log(1-2*t)))
def tangent(r,t,d):return plus((1,G(r,t)),(d-t,Gp(r,t)))
def bank(r,t,d):return plus((1,G(r,d)),(-1,tangent(r,t,d)))
def ln(q):
    y=(q-1)/(q+1);v=sum((2*y**(2*j+1)/(2*j+1) for j in range(32)),Q(0))
    return v,v+2*y**65/(65*(1-y*y))
LN2=ln(Q(2))
@lru_cache(None)
def lb(n):
    q=Q(n);a=0
    while q>=2:q/=2;a+=1
    lo,hi=ln(q);return a+lo/LN2[1],a+hi/LN2[0]
def bounds(e):
    lo=hi=Q(0)
    for k,c in e.items():
        a,b=lb(k);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
    den=1<<64
    return Q((lo*den).__floor__(),den),Q((hi*den).__ceil__(),den)
def enc(e):return {'prime_log':{str(k):str(v) for k,v in e.items()},'interval':[str(v) for v in bounds(e)]}
g=tuple(-1 if j<3 else 1 for j in range(16));h=tuple(-1 if j<4 else 1 for j in range(16))
u=tuple((g[j>>3] if not(j&4) else h[j>>3]) if not(j&3) else 1 for j in range(128))
F=tuple(u[j&127] if not(j&384) else 1 for j in range(512));t=meanneg(u);p0=Q(1,4)
order=[0,7,1,2];leaves=[];rows=[]
def walk(fixed,w,depth):
    f=restricted(F,fixed);v=restricted(u,{j:b for j,b in fixed.items() if j<7});r=2-sum(j in fixed for j in [7,8]);failed=any(fixed.get(j,0)==1 for j in [7,8]);d=meanneg(v)
    if failed or len(set(f))==1 or depth==len(order):leaves.append((w,failed,r,v,f));return
    j=order[depth];child=[]
    for bit in [0,1]:
        fix=dict(fixed);fix[j]=bit;child.append((fix,restricted(F,fix),restricted(u,{i:b for i,b in fix.items() if i<7})))
    delta=plus((1,H(f)),(Q(-1,2),H(child[0][1])),(Q(-1,2),H(child[1][1])))
    idx=j-sum(i<j for i in fixed);q=inf(f,idx)
    if j>=7:
        aa=plus((1,tangent(r,t,d)),(Q(-1,2),tangent(r-1,t,d)))
        release=plus((1,bank(r,t,d)),(Q(-1,2),bank(r-1,t,d)))
        ck(delta==plus((1,aa),(1,release)))
        ck(bounds(release)[0]>=0);ck(q==2*Q(1,1<<r)*d)
        e=delta
    else:
        aa={};release={}
        cd=plus((1,H(v)),(Q(-1,2),H(child[0][2])),(Q(-1,2),H(child[1][2])))
        e=plus((1,delta),(-Q(1,1<<r),cd))
        ck(e==plus((1,G(r,d)),(Q(-1,2),G(r,meanneg(child[0][2]))),(Q(-1,2),G(r,meanneg(child[1][2])))))
    rows.append((w,j,q,e,aa,release))
    for fixed2,_,_ in child:walk(fixed2,w/2,depth+1)
walk({},Q(1),0)
leafH=coreH=B={};leafI=coreI=Q(0);mass=Q(0)
for w,failed,r,v,f in leaves:
    leafH=plus((1,leafH),(w,H(f)));leafI+=w*I(f)
    if not failed:
        dw=w*Q(1,1<<r)/p0;mass+=dw;coreH=plus((1,coreH),(dw,H(v)));coreI+=dw*I(v)
        B=plus((1,B),(w,bank(r,t,meanneg(v))))
bill=errors={};Qc=Qd=Q(0);exit={};releaseexpr={}
for w,j,q,e,aa,release in rows:
    errors=plus((1,errors),(w,e))
    if j<7:
        Qd+=w*q
        if j==2:exit=e
    else:Qc+=w*q;bill=plus((1,bill),(w,aa));releaseexpr=release
error=plus((1,H(F)),(-1,leafH),(-p0,H(u)),(p0,coreH))
ck(mass==1);ck(I(F)==Qd+Qc+leafI);ck(Qd==p0*(I(u)-coreI))
ck(error==errors);ck(error==plus((1,bill),(-1,B)));ck(bounds(B)[0]>0);ck(bounds(exit)[0]>0)
ck(bounds(plus((1,error),(-Q(21,4)*Qc,{2:Q(1)})))[1]<0)
price=plus((1,Gp(1,Q(1,8))),(Q(1,6),log(Q(9,7))))
ck(bounds(price)[1]<Q(21,4))
s=Q(1,16);b=Q(3,10);support=plus((1,G(1,b)),(-1,G(1,s)),(-(b-s),Gp(1,s)))
ck(bounds(support)[0]>Q(17,1000))
# Actual omitted-hypothesis guards, reconstructed from full independent spectra.
pt=(-1,)+(1,)*15;act=pt+(1,)*16;endpointguard=plus((1,H(act)),(Q(-1,2),H(pt)))
ck(bounds(endpointguard)[0]>0)
v=tuple(g[j>>1] if not(j&1) else h[j>>1] for j in range(32));act=v+(1,)*32
rootguard=plus((1,H(act)),(Q(-1,2),H(g+(1,)*16)),(Q(-1,2),H(h+(1,)*16)),(Q(-1,2),H(v)),(Q(1,4),H(g)),(Q(1,4),H(h)))
ck(bounds(rootguard)[0]>0)
main=json.loads((RUN/'out/validation.json').read_text(encoding='utf-8'));mw=main['witness']
for key,e in [('full_signed_error',error),('control_tangent_bill',bill),('frontier_bank',B),('positive_exit',exit)]:ck(enc(e)['prime_log']==mw[key]['prime_log'])
ck(enc(price)['prime_log']==main['control_price_certificate']['prime_log'])
result={'status':'PASS','method':'direct character sums; separate32-term log bounds; original physical branches and edges','assertions':N,'elapsed_seconds':time.monotonic()-START,'r':2,'root_bias':str(t),'root_I':str(I(F)),'queried_core_I':str(Qd),'queried_control_I':str(Qc),'full_terminal_I':str(leafI),'full_signed_error':enc(error),'frontier_bank':enc(B),'control_release':enc(releaseexpr),'positive_exit':enc(exit),'support_certificate':enc(support),'control_price_certificate':enc(price),'guards':[enc(endpointguard),enc(rootguard)]}
(RUN/'out/independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if not isinstance(v,(list,dict))}))
