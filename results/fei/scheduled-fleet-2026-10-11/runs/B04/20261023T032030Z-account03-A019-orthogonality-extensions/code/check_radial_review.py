import json,time
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
src=(R.parent/'20261014T055119Z-account05-A019-orthogonality-extensions/code/check_exposure.py').read_text(encoding='utf-8')
ns={'Q':Q,'lru_cache':lru_cache,'checks':0};exec(src[src.index('def ck(x):'):src.index("transport={'positive'")],ns)
ck,sp,ce,add,psi,nn,lf=[ns[x] for x in ('ck','spectrum','ce','add','psi','nonnegative','logform')]
def wl(x,y):return add((x,lf(x/y))) if x else {}
def A(p,z):return add((Q(1,2),wl(p,z)),((1+p)/2,lf((1+z)/(1+p))))
def kl(p,q):return add((1,ce(p,q)),(-1,ce(p,p)))
def refs(p):return (p,tuple(Q(1,len(p)) for _ in p),tuple((v+int(i==0))/2 for i,v in enumerate(p)))
def act(h,q,s,qs):
 tt=tuple(1 if x==0 else h[y]*s[z] for z in range(4) for y in range(len(h)) for x in range(2));p=sp(tt);ref=[]
 for j in range(4*len(h)):
  qr=(q[j%len(h)]*qs[j//len(h)]+int(j==0))/2;mass=p[2*j]+p[2*j+1]
  ref.extend((qr*p[2*j]/mass,qr*p[2*j+1]/mass) if mass else (qr,Q(0)))
 ck(sum(ref)==1);cost=ce(p,ref)
 mu=Q(sum(h),len(h))*Q(sum(s),4)
 ck(cost==add((Q(1,2),ce(sp(h),q)),(Q(1,2),ce(sp(s),qs)),(1,psi(mu)),(-1,A(mu*mu,q[0]*qs[0]))))
 return cost
constant=(1,1,1,1);char=(1,-1,1,-1);point=(-1,1,1,1);uni=(Q(1,4),)*4
masks=[(constant,sp(constant)),(char,uni),(point,uni),(constant,tuple((p+u)/2 for p,u in zip(sp(constant),uni))),(char,sp(char))]
fs=[tuple(1-2*((m>>i)&1) for i in range(2)) for m in range(4)]
start=time.monotonic();cases=dominated=positive=0;boundaries=set()
for h0 in fs:
 for h1 in fs:
  ps=[sp(h0),sp(h1)]
  for q0 in refs(ps[0]):
   for q1 in refs(ps[1]):
    h=tuple(x for pair in zip(h0,h1) for x in pair);ph=sp(h);qh=[]
    for i in range(2):
     mass=ph[2*i]+ph[2*i+1];qr=(q0[i]+q1[i])/2
     qh.extend((qr*ph[2*i]/mass,qr*ph[2*i+1]/mass) if mass else (qr,Q(0)))
    beta=[Q(sum(z),len(z)) for z in (h0,h1)];b=sum(beta)/2;r=sum(v*v for v in beta)/2;nu=b*b/r if r else Q(1)
    a=(q0[0]+q1[0])/2
    dc=add((Q(1,2),kl(ps[0],q0)),(Q(1,2),kl(ps[1],q1)),(-1,kl(ph,qh)))
    e0=add((Q(1,2),wl(beta[0]**2,q0[0])),(Q(1,2),wl(beta[1]**2,q1[0])),(-1,wl(r,a)))
    er=add((1,dc),(-1,e0));ck(nn(e0));ck(nn(er));ck(qh[0]==nu*a)
    for s,qs in masks:
     sig=Q(sum(s),4);m=sig*sig;t=qs[0];p=m*r;z=t*a
     g=add((1,A(p,z)),(-1,A(nu*p,nu*z)))
     kp=add((Q(1,2),wl(1+m*beta[0]**2,1+t*q0[0])),(Q(1,2),wl(1+m*beta[1]**2,1+t*q1[0])),(-1,wl(1+p,1+z)))
     lam=add((Q(1,2),A(m*beta[0]**2,t*q0[0])),(Q(1,2),A(m*beta[1]**2,t*q1[0])),(-1,A(m*b*b,t*qh[0])),(-Q(1,2),dc))
     ck(lam==add((1,g),(-(1-m)/2,e0),(-Q(1,2),er),(-Q(1,2),kp)))
     ck(nn(g));ck(nn(kp))
     if p<=z:
      bd=add((Q(1,2),lf((1+z)/(1+nu*z))))
      ck(nn(add((1,bd),(-1,g))));dominated+=1
     if lam and ns['interval'](lam)[0]>0:positive+=1
     cr=act(h,qh,s,qs);cs=[act(h0,q0,s,qs),act(h1,q1,s,qs)]
     dh=add((1,ce(ph,ph)),(-Q(1,2),ce(ps[0],ps[0])),(-Q(1,2),ce(ps[1],ps[1])))
     curvature=add((1,psi(b*sig)),(-Q(1,2),psi(beta[0]*sig)),(-Q(1,2),psi(beta[1]*sig)))
     ck(add((1,cr),(-Q(1,2),cs[0]),(-Q(1,2),cs[1]))==add((Q(1,2),dh),(1,curvature),(1,lam)))
     for name,condition in [('p0',p==0),('z0',z==0),('nu0',nu==0),('nu1',nu==1),('m0',m==0),('m1',m==1),('t0',t==0),('t1',t==1)]:
      if condition:boundaries.add(name)
     cases+=1;assert time.monotonic()-start<60
out={'status':'PASS','cases':cases,'checks':ns['checks'],'seconds':time.monotonic()-start,'average_dominated_cases':dominated,'positive_Lambda_cases':positive,'boundaries':sorted(boundaries),'scope':'independent exact actual-Boolean full-reference reconstruction; analytic proof supplies arbitrary dimension','full_fei':'OPEN'}
(R/'out/REVIEW_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
