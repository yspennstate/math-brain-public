from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
RUN=Path(__file__).resolve().parent.parent;t0=time.perf_counter();checks=0;cases=0
def ck(v):
    global checks
    checks+=1
    assert v,checks
    assert time.perf_counter()-t0<55,'frozen runtime guard'
@lru_cache(None)
def fac(n):
    z={};p=2
    while p*p<=n:
        while n%p==0:z[p]=z.get(p,0)+1;n//=p
        p+=1
    if n>1:z[n]=z.get(n,0)+1
    return z
def add(a,b,c=F(1)):
    a=dict(a)
    for p,v in b.items():
        a[p]=a.get(p,F(0))+c*v
        if not a[p]:del a[p]
    return a
def lg(x,c=F(1)):
    ck(x>0)
    return add({p:c*v for p,v in fac(x.numerator).items()},{p:c*v for p,v in fac(x.denominator).items()},F(-1))
def wl(t):
    a=t[:];w=1
    while w<len(a):
        for s in range(0,len(a),2*w):
            for j in range(s,s+w):a[j],a[j+w]=a[j]+a[j+w],a[j]-a[j+w]
        w*=2
    return [F(v,len(t)) for v in a]
def inf(t):return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)]
def KL(mu,q):
    ck(sum(mu.values())==sum(q.values())==1);ans={}
    for k,u in mu.items():
        if u:ans=add(ans,lg(u/q[k],u))
    return ans
def group(mu,q,key):
    um={};qm={}
    for k,v in q.items():
        c=key(k);qm[c]=qm.get(c,F(0))+v;um[c]=um.get(c,F(0))+mu.get(k,F(0))
    return um,qm
def table(n,mask):return [1 if (mask>>x)&1 else -1 for x in range(1<<n)]
parameters=[]
for d,masks in [(1,range(1,4,2)),(2,range(1,16,2)),(3,[1,7,23,105,127,255])]:
    for mask in masks:
        for r in [1,2]:
            for gm in range(1<<(1<<r)):parameters.append((d,table(d,mask),r,table(r,gm),False))
bent=[(-1)**(((y&1)*((y>>1)&1))+(((y>>2)&1)*((y>>3)&1))) for y in range(16)]
for r in [1,2]:
    for gm in range(1<<(1<<r)):parameters.append((4,bent,r,table(r,gm),True))
ck(len(parameters)==340)
if '--pilot' in sys.argv:parameters=parameters[:20]
for d,b,r,g,is_bent in parameters:
    delta=F(1,1<<d);beta=wl(b);a=wl(g);Eg=inf(g);cb=b[:];cb[0]=-1
    Ib=sum(inf(b));Ic=sum(inf(cb))
    if abs(sum(b))!=len(b):ck(Ib>=2*d*delta)
    if abs(sum(cb))!=len(cb):ck(Ic>=2*d*delta)
    parent=[g[x>>d] if (x&((1<<d)-1))==0 else b[x&((1<<d)-1)] for x in range(1<<(d+r))]
    amp=wl(parent);es=inf(parent);ck(sum(v*v for v in amp)==1)
    IY=sum(es[:d]);IX=sum(es[d:]);ck(IY==((1+a[0])*Ib+(1-a[0])*Ic)/2);ck(IX==delta*sum(Eg))
    W1=sum(a[1<<i]**2 for i in range(r));ck(d*delta*W1<=2*IY)
    if abs(sum(b))!=len(b) and abs(sum(cb))!=len(cb):ck(d*delta*W1<=IY/2)
    for V in range(1<<r):
        for T in range(1<<d):ck(amp[T|(V<<d)]==(beta[T] if V==0 else F(0))+delta*(a[V]-(1 if V==0 else 0)))
    Ltotal={};predicted={}
    for i in range(r):
        ai=a[1<<i];Ei=Eg[i];e=es[d+i];ck(e==delta*Ei);ck(abs(ai)<=Ei)
        if not Ei:continue
        mu={};q={}
        for V in range(1<<r):
            if (V>>i)&1:continue
            for T in range(1<<d):
                upper=amp[T|((V|(1<<i))<<d)]**2
                mu[T,V]=upper/e;q[T,V]=amp[T|(V<<d)]**2+upper
        df=KL(mu,q);um,qm=group(mu,q,lambda k:k[1]);dm=KL(um,qm)
        us,qs=group(mu,q,lambda k:(k[1],beta[k[0]]));ck(KL(us,qs)==df)
        L=add(df,dm,F(-1));L={p:e*v for p,v in L.items() if e*v};Ltotal=add(Ltotal,L)
        rho=1-delta+delta*(a[0]**2+ai**2);ck(rho<=1);ck(qm[0]==rho)
        if ai:
            cond={T:q[T,0]/rho for T in range(1<<d)};uniform={T:delta for T in cond};D0=KL(uniform,cond)
            expected={p:delta*ai**2*v for p,v in D0.items() if v};ck(L==expected);predicted=add(predicted,expected)
            for T in cond:
                ck(q[T,0]>=delta**2*ai**2)
                ck(delta/cond[T]<=1/(delta*ai**2))
                if is_bent:ck(delta/cond[T]<=4)
        else:ck(L=={})
    ck(Ltotal==predicted)
    if d>=2 and all(v==-1 for v in b[1:]) and g==[1,-1]:
        p0=(1-2*delta)**2;z=(1-delta)**2+delta**2;Hb={}
        for v in beta:
            if v:Hb=add(Hb,lg(1/(v*v),v*v))
        entropyformula=add(lg(1/p0,p0),lg(1/(4*delta**2),4*delta*(1-delta)))
        ck(Hb==entropyformula);ck(IY==d*delta)
        D0formula=add(lg(F(2),(1-delta)*(d-1)),lg(delta/z,delta))
        ck(Ltotal=={p:delta*v for p,v in D0formula.items() if v})
        S4=add(lg(F(2),4*d*delta),Hb,F(-1,2))
        Scformula=add(lg(F(2),4*delta+4*(d-1)*delta**2),lg(1/p0,p0),F(-1,2))
        ck(S4==Scformula)
    if is_bent:ck(2*delta<=es[0]/4)
    cases+=1
    (RUN/'out/CHECKPOINT.json').write_text(json.dumps({'completed_cases':cases,'assertions':checks}),encoding='utf-8')
symbolic=[]
if '--pilot' not in sys.argv:
    for d in [2,3,4,8,16,32]:
        delta=F(1,1<<d);z=(1-delta)**2+delta**2;p0=(1-2*delta)**2
        ck(0<z<=1);ck((2*d-1)*delta<=1);ck((d-1)*delta<=F(1,4))
        Sc4upper=4*delta+4*(d-1)*delta**2;ck(Sc4upper<=5*delta)
        ck(1-p0<=4*delta);ck((4*delta-4*delta**2)*(2*d-2)<=8*(d-1)*delta)
        for C in [F(4),F(9,2),F(19,4)]:
            Scupper=Sc4upper+(C-4)*d*delta
            ck(delta*(d-2)-Scupper>=delta*((5-C)*d-7))
        ck(d*delta>=delta*(d-2))
        symbolic.append({'d':d,'e':str(delta),'L_over_e_lower':d-2,'S4_over_e_upper':'5','price_C_deficit_over_e_lower':'(5-C)*d-7','C5_certificate':'S5>=d*e>=L'})
out={'status':'PASS','materialized_cases':cases,'symbolic_cases':len(symbolic),'assertions':checks,'runtime_seconds':time.perf_counter()-t0,'arithmetic':'Integer Walsh/direct physical edges; Fraction normalizers and prime-log identities; analytic rational inequalities','symbolic_certificates':symbolic}
name='PILOT.json' if '--pilot' in sys.argv else 'CHECK.json'
(RUN/'out'/name).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='symbolic_certificates'},indent=2))
