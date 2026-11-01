"""Independent controller-shape tree reconstruction, direct characters only."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
import independent_base as b
R=Path(__file__).resolve().parents[1];START=time.monotonic()
nodes=leaves=0;positive_shape_nodes=0;nonzero_vacuum_nodes=0

def state(a,g,h,ra,rg,rh):
    global positive_shape_nodes,nonzero_vacuum_nodes
    pg,ph,pa=b.law(g),b.law(h),b.law(a)
    p=Q(a.count(-1),len(a));V=1-pa[0];beta=1-ra[0]
    gamma=Q(sum(x!=y for x,y in zip(g,h)),len(g))
    f=tuple((g if y==1 else h)[x] for x in range(len(g)) for y in a)
    pf=b.law(f);q=[];r=[];ref=[]
    for t in range(len(g)):
        row=pf[t*len(a):(t+1)*len(a)];qt=sum(row);rt=(1-p)*rg[t]+p*rh[t]
        b.ck(qt==(1-p)*pg[t]+p*ph[t]);q.append(qt);r.append(rt)
        non=sum(row[1:])
        for u in range(1,len(a)):
            b.ck(row[u]*V==non*pa[u])
        ref.append(rt*row[0]/qt if qt else rt)
        ref.extend(rt*non/qt*x/beta if qt and non else Q() for x in ra[1:])
    debt=b.D(pf,tuple(ref));data=b.D(tuple(q),tuple(r))
    Da=b.D(pa,ra);vac=b.D((1-V,V),(1-beta,beta))
    shape=b.D(tuple(x/V for x in pa[1:]),tuple(x/beta for x in ra[1:])) if V else {}
    W=b.add(b.mul(b.D(pg,rg),1-p),b.mul(b.D(ph,rh),p))
    Z=b.difference(W,data);T=b.add(W,b.mul(Da,gamma));S=b.add(Z,b.mul(vac,gamma))
    delta=b.mul(shape,V*gamma)
    b.ck(not b.difference(Da,b.add(vac,b.mul(shape,V))))
    b.ck(not b.difference(debt,b.add(data,delta)))
    b.ck(not b.difference(debt,b.difference(T,S)))
    if delta:positive_shape_nodes+=1
    if b.mul(vac,gamma):nonzero_vacuum_nodes+=1
    return dict(debt=debt,T=T,S=S,H=b.H(pf),ref=tuple(ref),f=f,p=p,gamma=gamma,delta=delta,vac=vac,Da=Da)
