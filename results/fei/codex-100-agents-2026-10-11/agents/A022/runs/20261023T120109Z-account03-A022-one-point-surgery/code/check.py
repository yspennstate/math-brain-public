import json,sys,time
from pathlib import Path
from functools import lru_cache
from exact import *
ROOT=Path(__file__).resolve().parents[1]; assertions=0
def eq(a,b):
    global assertions
    assertions+=1; assert not plus(a,mul(b,-1)),(a,b)
def nn(a):
    global assertions
    assertions+=1; assert bounds(a)[0]>=0,a
def kl(p,r): return plus(ce(p,r),mul(entropy(p),-1))
def mix(p,eta):
    a=[eta*x for x in p]; a[0]+=1-eta; return tuple(a)
def phase(a,r,i):
    cs=[Q(x,len(a)) for x in fwht(a)]; out=[[],[]]; E={}
    for s in range(len(a)//2):
        j=(s&((1<<i)-1))+((s>>i)<<(i+1)); k=j+(1<<i)
        u=cs[j]**2+cs[k]**2; v=r[j]+r[k]
        for b in (0,1): out[b].append(v*(cs[j]+(-1)**b*cs[k])**2/(2*u) if u else v/2)
        if u: E=plus(E,mul(kl((cs[j]**2/u,cs[k]**2/u),(r[j]/v,r[k]/v)),u))
    norms=[sum(q) for q in out]; assert sum(norms)==1 and min(norms)>0
    kids=[tuple(restrict(a,i,b)) for b in (0,1)]; rr=[tuple(x/n for x in q) for q,n in zip(out,norms)]
    A=plus(kl(spectrum(a),r),mul(plus(*(kl(spectrum(k),s) for k,s in zip(kids,rr))),-Q(1,2)))
    O=kl((Q(1,2),Q(1,2)),norms); eq(A,plus(E,O)); nn(E); nn(O); nn(A)
    return kids,rr,A
@lru_cache(None)
def qdata(t,d,x):
    q=[Q(1)]
    for block in range(t):
        j=max(0,min(3,d-3*block)); u=x>>(3*block)&((1<<j)-1)
        if j==0: r=[Q(9,16)]+[Q(1,16)]*7
        elif j==1: r=[Q(1,4)]*4 if u==0 else [Q(13,16)]+[Q(1,16)]*3
        elif j==2: r=[Q(15,16) if z==(1 if u==0 else 0) else Q(1,16) for z in (0,1)]
        else:r=[Q(1)]
        q=[p*s for s in r for p in q]
    return tuple(q)
@lru_cache(None)
def physical(t,v,d,x,a):
    nd=2**(3*t-d); f=[]
    for z in range(len(a)):
        for y in range(nd):
            xx=x+(y<<d); b=1
            for j in range(t): b*=g(xx>>(3*j)&7)
            f.append(b*(a[z] if xx==v else 1))
    P=tuple(spectrum(f)); return P,entropy(P),sum(inf(f,i) for i in range(3*t-d)),tuple(f)
def inspect(t,v,nodes,eps):
    delta=Q(1,8**t); U=Q(t,64); I=Q(0); Co=Cn=H=LH=Lr=Ac=V={}
    for d,x,a,r,p,path in nodes:
        w=Q(1,2**d); rho=w*p; eta=delta/w; active=x==v%2**d
        P,hh,ii,f=physical(t,v,d,x,a); pa=tuple(spectrum(a)); ro=mix(pa,delta)
        actual=mix(pa,eta) if active else tuple([Q(1)]+[Q(0)]*(len(a)-1))
        rn=mix(r,eta) if active else tuple([Q(1)]+[Q(0)]*(len(a)-1))
        q=qdata(t,d,x); oldref=[u*z for z in ro for u in q]; newref=[u*z for z in rn for u in q]
        co=ce(P,oldref); cn=ce(P,newref)
        Co=plus(Co,mul(co,rho)); Cn=plus(Cn,mul(cn,rho)); H=plus(H,mul(hh,rho)); I+=rho*ii
        cal=kl(actual,ro); nn(cal); Ac=plus(Ac,mul(cal,rho))
        if active:
            ha=entropy(pa); cr=ce(pa,r); LH=plus(LH,mul(ha,delta*p)); Lr=plus(Lr,mul(cr,delta*p))
            vac=plus(mul(kl(pa,r),eta),mul(kl(actual,rn),-1)); nn(vac)
            p0=pa[0]; q0=r[0]; xx=actual[0]; yy=rn[0]
            explicit=plus(mul(lg(p0/q0),eta*p0) if p0 else {},mul(lg(xx/yy),-xx))
            eq(vac,explicit); V=plus(V,mul(vac,rho))
    old=plus(const(4*I-U),LH,mul(Co,-1)); new=plus(const(4*I-U),Lr,mul(Cn,-1),mul(eps,-1))
    eq(plus(new,mul(old,-1)),plus(Ac,V,mul(eps,-1)))
    nn(plus(old,const(-Q(t,32) if t==2 else -Q(t,16))))
    nn(plus(new,const(-Q(13*t,576))))
    return old,new,plus(Cn,mul(H,-1)),LH,Lr,H,Ac,V
def run(t,v,a,law,policy):
    delta=Q(1,8**t); pa=tuple(spectrum(a)); n=len(a)
    q=tuple(Q(1,n) for _ in a) if law==1 else tuple(Q(i+1,n*(n+1)//2) for i in range(n))
    r=pa if law==0 else tuple((p+u)/2 for p,u in zip(pa,q))
    D0=kl(pa,r); eps=mul(D0,delta); nn(plus(const(delta),mul(eps,-1)))
    nodes=[(0,0,a,r,Q(1),())]; K=A=E={}; root=inspect(t,v,nodes,eps)
    invariant=plus(root[1],root[2]); original=mul(ce(pa,r),delta)
    def audit():
        b=inspect(t,v,nodes,eps)
        eq(plus(K,A,b[4]),original); eq(plus(b[1],b[2],E),invariant)
        eq(plus(K,b[3]),mul(entropy(pa),delta))
    def query(idx,kind,i=0):
        nonlocal nodes,K,A,E
        d,x,aa,rr,p,path=nodes[idx]; rho=Q(1,2**d)*p; old=physical(t,v,d,x,aa)
        if kind=='data':
            ks=[(d+1,x+(b<<d),aa,rr,p,path) for b in (0,1)]
            nh=[physical(t,v,z[0],z[1],z[2])[1] for z in ks]
            dh=plus(old[1],mul(plus(*nh),-Q(1,2)))
            E=plus(E,mul(plus(const(4*inf(old[3],0)),mul(dh,-1)),rho))
        else:
            kids,refs,contraction=phase(aa,rr,i)
            ks=[(d,x,k,s,p/2,path+(b,)) for b,(k,s) in enumerate(zip(kids,refs))]
            dh=plus(old[1],mul(plus(*(physical(t,v,d,x,k)[1] for k in kids)),-Q(1,2)))
            hs=plus(entropy(spectrum(aa)),mul(plus(*(entropy(spectrum(k)) for k in kids)),-Q(1,2)))
            cs=plus(ce(spectrum(aa),rr),mul(plus(*(ce(spectrum(k),s) for k,s in zip(kids,refs))),-Q(1,2)))
            K=plus(K,mul(hs,delta*p)); A=plus(A,mul(contraction,delta*p)); E=plus(E,mul(cs,delta*p),mul(dh,-rho))
        nodes=nodes[:idx]+ks+nodes[idx+1:]; audit()
    audit(); query(0,'data')
    idx=next(i for i,e in enumerate(nodes) if e[1]==v%2**e[0]); query(idx,'control',policy)
    # Advance only one active control outcome; other depths remain unchanged.
    idx=next(i for i,e in enumerate(nodes) if e[1]==v%2**e[0] and e[5]==(policy,)); query(idx,'data')
    idx=next(i for i,e in enumerate(nodes) if e[1]==v%2**e[0] and e[5]==(policy,)); query(idx,'control')
    for unused in range(3):
        idx=next((i for i,e in enumerate(nodes) if e[1]==v%2**e[0] and e[5] and e[5][0]==policy and e[0]<5),None)
        if idx is not None: query(idx,'data')
    idx=next((i for i,e in enumerate(nodes) if e[1]!=v%2**e[0] and e[0]<3),None)
    if idx is not None:query(idx,'data')
    return len(nodes)
def main():
    mode=sys.argv[1]; start=time.monotonic()
    cases=[(2,v,tuple(1 if mask>>z&1 else -1 for z in range(4)),law,policy) for v in (0,1,7,63) for mask in range(16) for law in range(3) for policy in (0,1)]
    if mode=='pilot':cases=[cases[i] for i in (0,37,222,383)]
    elif mode=='targeted':cases=[(3,v,tuple(1 if mask>>z&1 else -1 for z in range(4)),1,0) for v in (0,511) for mask in (1,10)]
    else:assert mode=='main'
    for c in cases:
        run(*c); assert time.monotonic()-start<(300 if mode=='main' else 60)
    out={'status':'PASS','cases':len(cases),'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'peak_memory':'unmeasured','source_reference':'single original, physically inherited with all outcome normalizers','review':'author exact check'}
    (ROOT/'out'/f'{mode}.json').write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps(out))
if __name__=='__main__':main()
