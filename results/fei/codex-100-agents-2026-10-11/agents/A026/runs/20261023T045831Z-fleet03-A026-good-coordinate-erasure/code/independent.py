"""Alternate direct characters and amplitude-pair matrix; no main helper import."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import time,json
import exact_helper as logs
R=Path(__file__).resolve().parents[1];START=time.monotonic();checks=0;coords=0
def ck(x):
 global checks
 assert x,checks;checks+=1
 assert time.monotonic()-START<55
@lru_cache(None)
def chars(v):return tuple(F(sum(y*(-1 if (x&T).bit_count()%2 else 1) for x,y in enumerate(v)),len(v)) for T in range(len(v)))
def sq(v):return tuple(x*x for x in chars(v))
def child(v,j,b):return tuple(y for x,y in enumerate(v) if ((x>>j)&1)==b)
def mat(v,Q,j):
 a=chars(v);out=[[],[]]
 for T in range(len(v)//2):
  i=(T&((1<<j)-1))|((T>>j)<<(j+1));k=i|(1<<j)
  z=a[i]*a[i]+a[k]*a[k];q=Q[i]+Q[k]
  for b in (0,1):out[b].append(q*((a[i]+(-1)**b*a[k])**2/(2*z) if z else F(1,2)))
 rho=tuple(sum(x) for x in out);ck(sum(rho)==1 and min(rho)>0)
 return tuple(tuple(x/rho[b] for x in out[b]) for b in (0,1)),rho
def kl(p,q):return logs.add(*(logs.scale(logs.lg(x/y),x) for x,y in zip(p,q) if x))
def sub(x,y):return logs.add(x,logs.scale(y,-1))
def bounds(x):return list(map(str,logs.enclosure(x)))
def mux(a,g,h):return tuple((g if z==1 else h)[x] for x in range(len(g)) for z in a)
def profile(a,g,h,rg,rh):
 v=mux(a,g,h);P=sq(v);pg=sq(g);ph=sq(h);Q=[]
 for t in range(len(g)):
  q=F(5,8)*pg[t]+F(3,8)*ph[t];r=F(5,8)*rg[t]+F(3,8)*rh[t]
  Q.extend(r*P[8*t+u]/q if q else r*int(u==0) for u in range(8))
 ck(sum(Q)==1);return v,tuple(Q)
def parts(Q):return tuple(Q[i] for i in range(0,len(Q),8)),tuple(sum(Q[i+1:i+8]) for i in range(0,len(Q),8))
def reshape(x,y,b):return tuple(x[t] if u==0 else y[t]*b[u-1] for t in range(len(x)) for u in range(8))
a=tuple(-1 if x in (0,1,2) else 1 for x in range(8));pa=sq(a);V=1-pa[0];pi=tuple(z/V for z in pa[1:]);targets=(F(0),F(1,8),F(3,16))
bs={t:tuple((1-t)*z+t/F(7) for z in pi) for t in targets};D={t:kl(pi,b) for t,b in bs.items()}
guard={};rows=[]
for m in (0,1,2):
 g=tuple((-1 if x%8==0 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(1<<(m+3)))
 h=tuple((-1 if (x%8).bit_count()>=2 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(len(g)))
 rr=(F(1,len(g)),)*len(g);rg,rhog=mat(g,rr,0);rh,rhoh=mat(h,rr,0)
 gg=child(g,0,1);hh=child(h,0,1);v,Q=profile(a,gg,hh,rg[1],rh[1]);P=sq(v);x,y=parts(Q)
 eta=sum(p for i,p in enumerate(P) if i%8);ck(eta==F(45,64));ck(Q==reshape(x,y,pi))
 M=1<<(m+2);beta=F(40*M,55*M-36)
 W=logs.add(logs.scale(kl(sq(gg),rg[1]),F(5,8)),logs.scale(kl(sq(hh),rh[1]),F(3,8)))
 q=tuple(F(5,8)*z+F(3,8)*w for z,w in zip(sq(gg),sq(hh)))
 r=tuple(F(5,8)*z+F(3,8)*w for z,w in zip(rg[1],rh[1]))
 Z=sub(W,kl(q,r));formula=logs.scale(kl((F(20,23),F(3,23)),(beta,1-beta)),F(23,32));ck(not sub(Z,formula))
 endpoint=logs.scale(D[F(3,16)],eta)
 if m==0:ck(not Z);ck(logs.enclosure(endpoint)[0]>0);guard['m0']={'Z_exact':'0','positive_endpoint_interval':bounds(endpoint)}
 else:ck(logs.enclosure(sub(Z,endpoint))[0]>F(19,10304))
 for t in targets:
  Qt=reshape(x,y,bs[t]);delta=sub(kl(P,Qt),kl(P,Q));ck(not sub(delta,logs.scale(D[t],eta)))
  for j in range(3,3+m+2):
   coords+=1;base,rhob=mat(v,Q,j);changed,rhot=mat(v,Qt,j);ck(rhob==rhot)
   for b in (0,1):
    xx,yy=parts(base[b]);ck(changed[b]==reshape(xx,yy,bs[t]))
    Pc=sq(child(v,j,b));etac=sum(z for i,z in enumerate(Pc) if i%8)
    if j==3 and m>=1:
     ck(len(set(child(gg,0,b)))==len(set(child(hh,0,b)))==len(set(child(v,3,b)))==2)
     first=reshape(xx,yy,bs[F(1,8)]);second=reshape(xx,yy,bs[F(3,16)])
     actual=sub(kl(Pc,second),kl(Pc,first));pred=logs.scale(sub(D[F(3,16)],D[F(1,8)]),etac)
     ck(not sub(actual,pred));ck(logs.enclosure(actual)[0]>0)
 if m==1:
  bquarter=tuple(F(3,4)*z+F(1,28) for z in pi)
  overshoot=logs.scale(kl(pi,bquarter),eta)
  ck(logs.enclosure(sub(overshoot,Z))[0]>0)
  guard['quarter']={'cost_interval':bounds(overshoot),'inherited_Z_interval':bounds(Z),'shortfall_interval':bounds(sub(overshoot,Z))}
  first=reshape(x,y,bs[F(1,8)]);_,r0=mat(v,Q,0);_,r1=mat(v,first,0)
  ck(r0!=r1);guard['controller_query']={'old_profile_rho':list(map(str,r0)),'changed_profile_rho':list(map(str,r1)),'meaning':'DATA profile-independence of physical branch normalizers does not extend to controller queries'}
 rows.append({'m':m,'Z_interval':bounds(Z),'total_endpoint_cost_interval':bounds(endpoint)})
ck(16807**9<2*15606**9)
ck(F(45,2576)-F(1,64)==F(19,10304));ck(F(19,10304)/2==F(19,20608))
out={'status':'PASS','roots':3,'data_coordinates_with_profile':coords,'assertions':checks,'seconds':time.monotonic()-START,'representation':'direct character amplitudes and independently coded pair matrix; only exact log-vector primitive shared','rows':rows,'guards':guard}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k not in ('rows','guards')}))
