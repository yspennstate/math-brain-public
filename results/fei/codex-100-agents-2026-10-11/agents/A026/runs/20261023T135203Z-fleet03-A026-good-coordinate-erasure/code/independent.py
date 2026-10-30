from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=states=0
def ck(x,msg=''):
 global count
 assert x,(count,msg);count+=1
 assert time.monotonic()-start<55
@lru_cache(None)
def spec(v):
 return tuple((sum(x*(-1 if (s&t).bit_count()%2 else 1) for t,x in enumerate(v))/F(len(v)))**2 for s in range(len(v)))
def insert(x,j,b):return (x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)
def child(v,j,b):return tuple(v[insert(x,j,b)] for x in range(len(v)//2))
def influence(v):return sum(F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v)) for j in range(len(v).bit_length()-1))
def mux(a,g,h):return tuple((g if a[u]==1 else h)[t] for t in range(len(g)) for u in range(len(a)))
def physical(v,Q,j):
 P=spec(v);mp=tuple(P[insert(x,j,0)]+P[insert(x,j,1)] for x in range(len(v)//2));mq=tuple(Q[insert(x,j,0)]+Q[insert(x,j,1)] for x in range(len(v)//2));vv=[];qq=[];rr=[]
 for z in (0,1):
  vc=child(v,j,z);pc=spec(vc);joint=tuple(q*(p/(2*m) if m else F(1,2)) for q,p,m in zip(mq,pc,mp));rho=sum(joint);vv.append(vc);rr.append(rho);qq.append(tuple(x/rho for x in joint))
 ck(sum(rr)==1);return vv,qq,rr
def ln_interval(y):
 t=(y-1)/(y+1);v=2*sum(t**(2*j+1)/F(2*j+1) for j in range(24));tail=2*t**49/(49*(1-t*t));return v,v+tail
L2=ln_interval(F(2))
@lru_cache(None)
def log2(x):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=ln_interval(x)
 return F(k)+lo/L2[1],F(k)+hi/L2[0]
def KL(p,q):
 lo=hi=F(0)
 for x,y in zip(p,q):
  if x:
   u,v=log2(x/y);lo+=x*u;hi+=x*v
 return lo,hi
def energy(a,g,h):
 prob=F(sum(x==-1 for x in a),len(a));V=1-spec(a)[0];gamma=F(sum(x!=y for x,y in zip(g,h)),len(g));J=(1-prob)*influence(g)+prob*influence(h);return J/8+V*gamma/2,J,V*gamma
def check_state(a,g,h,ra,rg,rh):
 global states
 states+=1;c=len(a);prob=F(sum(x==-1 for x in a),c);P=spec(mux(a,g,h));pg,ph=spec(g),spec(h);q=tuple((1-prob)*x+prob*y for x,y in zip(pg,ph));r=tuple((1-prob)*x+prob*y for x,y in zip(rg,rh));E,J,eta=energy(a,g,h)
 ck(q==tuple(sum(P[c*t:c*t+c]) for t in range(len(g))));ck(sum(q[1:])<=J);ck(eta<=F(sum(x!=y for x,y in zip(g,h)),len(g))*influence(a));ck(E<=influence(mux(a,g,h))/2)
 s=1-ra[0];B=tuple(x/s for x in ra[1:]) if s else None;Clo=Chi=F(0);Q=[];Qstar=[]
 for t in range(len(q)):
  k=sum(P[c*t+1:c*t+c])/q[t] if q[t] else F(0);ell=k
  if q[t] and B is not None:ell=F(15,16)*k+F(1,32) if t else 2*k/(1+k)
  if q[t]:lo,hi=KL((1-k,k),(1-ell,ell));Clo+=q[t]*lo;Chi+=q[t]*hi
  for u in range(c):
   Q.append(r[t]*((1-ell) if u==0 else ell*B[u-1] if B else 0));Qstar.append(r[t]*((1-k) if u==0 else k*B[u-1] if B else 0))
 ck(sum(Q)==sum(Qstar)==1);ck(Chi<=E,'direct rigorous scalar KL envelope')
 # Direct full-spectrum KL difference must agree with the conditional sum.
 qlo,qhi=KL(P,tuple(Q));slo,shi=KL(P,tuple(Qstar));ck(qlo-shi<=Chi and qhi-slo>=Clo)
 return tuple(Q)
rows=[]
for m in (1,2):
 M=1<<(m+2);ch=((1<<m)-1)<<2;g=tuple(-1 if (x>>2).bit_count()%2 else 1 for x in range(M));h=tuple(g[x]*(1 if x%4==0 else -1) for x in range(M));a=tuple(-1 if x<3 else 1 for x in range(8));pa=spec(a);V=1-pa[0];pi=tuple(x/V for x in pa[1:]);ra=(pa[0],)+tuple(V*(F(7,8)*x+F(1,56)) for x in pi)
 rg=tuple(F(8,5*M-12) if x==ch else F(0) if x>>2==ch>>2 else F(5,5*M-12) for x in range(M));rh=(F(1,M),)*M
 Q=check_state(a,g,h,ra,rg,rh);E,_,_=energy(a,g,h)
 for j in range(3+m+2):
  if j<3:
   aa,ras,_=physical(a,ra,j);gg=[g,g];hh=[h,h];rgs=[rg,rg];rhs=[rh,rh]
  else:
   gg,rgs,_=physical(g,rg,j-3);hh,rhs,_=physical(h,rh,j-3);aa=[a,a];ras=[ra,ra]
  energies=[]
  for z in (0,1):check_state(aa[z],gg[z],hh[z],ras[z],rgs[z],rhs[z]);energies.append(energy(aa[z],gg[z],hh[z])[0])
  if j<3:
   ah=sum(a[x]*(-1 if (x>>j)&1 else 1) for x in range(len(a)))/F(len(a));gamma=F(sum(x!=y for x,y in zip(g,h)),len(g));expected=gamma*ah*ah/2
  else:
   vv=tuple(child(mux(a,g,h),j,z) for z in (0,1));expected=F(sum(x!=y for x,y in zip(*vv)),len(vv[0]))/8
  ck(E-sum(energies)/2==expected)
 rows.append({'m':m,'original_energy':str(E),'physical_coordinate_choices':m+5})
guards=[]
for n in (3,4,5):
 delta=F(1,1<<n);g=tuple(-1 if (x>>n)&1 else 1 for x in range(1<<(n+1)));h=tuple(g[x]*(-1 if x% (1<<n)==0 else 1) for x in range(len(g)));a=(1,-1);P=spec(mux(a,g,h));t=1<<n;q=sum(P[2*t:2*t+2]);k=P[2*t+1]/q;ck(q==1-2*delta+2*delta*delta and k==delta*delta/q)
 ell=F(15,16)*k+F(1,32);lam=ell*(1-k)/(k*(1-ell));ck(lam>=F(49,19));lo,hi=KL((1-k,k),(1-ell,ell));E,J,eta=energy(a,g,h);ck(q*hi<E);ck(J==1+n*delta and eta==delta)
 if n>=4:
  flo,fhi=KL((1-k,k),(F(31,32),F(1,32)));ck(q*flo>F(63,50176)>F(1,1024))
 guards.append({'n':n,'effective_lambda':str(lam),'energy':str(E)})
ck(16**8<2*15**8)
out={'status':'PASS','method':'direct characters and physical edge counting; independent scalar rational atanh enclosures; no main/helper import','assertions':count,'local_states':states,'seconds':time.monotonic()-start,'rows':rows,'outside_image_guards':guards}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k not in ('rows','outside_image_guards')}))
