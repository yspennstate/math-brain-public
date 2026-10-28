import check as c
from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
start=time.monotonic();n=0
def ck(v,s):
    global n
    assert v,s;n+=1
def activate(v,a):return tuple(v[t] if z==-1 else 1 for z in a for t in range(len(v)))
def target(v,a,ra,depth):
    f=activate(v,a);p=c.law(f);q=[F(0)]*len(p);m=len(v);beta=1-ra[0]
    for t in range(m):
        mass=sum(p[t+u*m] for u in range(len(a)))
        if not mass:continue
        k=sum(p[t+u*m] for u in range(1,len(a)))/mass
        lam=F(1) if depth==0 else (F(1,2) if t%2==0 else F(2))
        ell=lam*k/(1+(lam-1)*k);q[t]=mass*(1-ell)
        for u in range(1,len(a)):q[t+u*m]=mass*ell*ra[u]/beta
    return f,tuple(q)
v=(-1,)+(1,)*7;a=(1,-1,-1,-1);pa=c.law(a);theta=F(1,8)
ra=tuple(z if u==0 else z*(1-theta+3*theta*(u==1)) for u,z in enumerate(pa))
root,q=target(v,a,ra,0);ck(c.walsh(root)==c.direct(root),'independent direct-character selected root')
raw=c.D(c.law(root),q);total_loss={};terminal={}
def walk(v,depth,w):
    global raw,total_loss,terminal
    f,q=target(v,a,ra,depth);p=c.law(f)
    ck(sum(q)==1,'complete target normalized')
    if len(set(f))==1 or depth==3:
        terminal=c.add((1,terminal),(w,c.D(p,q)));return
    ch,ps,refs,zs,loss=c.query(f,q,0)
    total_loss=c.add((1,total_loss),(w,loss))
    for b in (0,1):
        vc=c.restrict(v,0,b);fc,rc=target(vc,a,ra,depth+1)
        ck(fc==ch[b],'direct child activation agrees')
        raw=c.add((1,raw),(w/2,c.D(ps[b],rc)),(-w/2,c.D(ps[b],refs[b])))
        walk(vc,depth+1,w/2)
walk(v,0,F(1))
ck(c.bounds(c.add((1,raw),(-1,terminal),(-1,total_loss)))[0]<=0<=c.bounds(c.add((1,raw),(-1,terminal),(-1,total_loss)))[1],'independent full telescope interval diagnostic')
eta=F(3,32);T=c.add((F(1,8),c.D(pa,ra)),(1,{F(2):F(4,9)*eta}))
excess=c.add((1,raw),(-1,T));ck(c.bounds(excess)[0]>F(1,128),'strict envelope counterexample more than1/128')
out={'status':'PASS','checks':n,'elapsed_seconds':time.monotonic()-start,'excess':c.enc(excess),'query_loss':c.enc(total_loss),'raw_debt':c.enc(raw),'scope':'new selected-family implementation; imports only current standalone rational channel/log primitives, never stage21 helpers'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({'status':'PASS','checks':n,'excess_interval':out['excess']['interval']}))
