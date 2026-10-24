from arithmetic import Q,add,scale,log,phi,sign,table,spectrum,entropy,hp,mean,variance,influence,edge_inf,ser
from pathlib import Path
import time,json,sys
from functools import lru_cache
from arithmetic import sign as product_sign
R=Path(__file__).resolve().parents[1]
@lru_cache(None)
def ln_bound(n):
 def enclosure(z):
  w=(z-1)/(z+1); total=Q(0); power=w
  for j in range(24):total+=2*power/(2*j+1); power*=w*w
  return total,total+2*power/(49*(1-w*w))
 k=n.bit_length()-1; l,u=enclosure(Q(n,1<<k)); l2,u2=enclosure(Q(2))
 l+=k*l2; u+=k*u2; unit=1<<64
 return (int(l*unit),-((-u.numerator*unit)//u.denominator))
def sign(v):
 if not v:return 0
 low=high=Q(0)
 for p,c in v.items():
  l,u=ln_bound(p)
  low+=c*(l if c>0 else u); high+=c*(u if c>0 else l)
 if low>0:return 1
 if high<0:return -1
 return product_sign(v)
def K(p,x,y):
 v=4*p*(1-p); q=(x-y)**2/4
 return add(add(add(phi((p*x+(1-p)*y)**2),phi(q),v),phi(x*x),-p),phi(y*y),-(1-p))
def ce(P,Qr):
 out={}
 for p,r in zip(P,Qr):
  if p: assert r>0; out=add(out,log(r),-p)
 return out
def kl(P,Qr):
 out=ce(P,Qr)
 for p in P:out=add(out,phi(p),-1)
 return out
def calibrated(P,shared,weighted):
 n=len(P); raw=[Q(i+1,n*(n+1)//2) if weighted else Q(1,n) for i in range(n)]
 v=sum(P[shared:],Q(0)); mass=sum(raw[shared:],Q(0))
 result=list(P[:shared])+[r*v/mass for r in raw[shared:]] if mass else list(P)
 assert sum(result)==1
 assert sign(add(ce(P,raw),ce(P,result),-1))>=0
 return result
def root(a,g,h,t,priv):
 # Physical layout: shared S, private X, private Y, controller W.
 count=1<<(t+2*priv+2); sm=(1<<t)-1; pm=(1<<priv)-1
 f=[]
 for x in range(count):
  si=x&sm; gx=si|(((x>>t)&pm)<<t); hy=si|(((x>>(t+priv))&pm)<<t)
  f.append(g[gx] if a[x>>(t+2*priv)]==-1 else h[hy])
 return tuple(f)
def check_root(a,g,h,t,priv):
 p=(1-mean(a))/2; va=variance(a); ag=spectrum(g); bh=spectrum(h); ah=spectrum(a)
 base=1<<(t+2*priv); shared=1<<t
 x=[Q(0)]*base; y=[Q(0)]*base
 for s,z in enumerate(ag):x[s]=z
 for s,z in enumerate(bh):y[(s&(shared-1))|((s>>t)<<(t+priv))]=z
 q=[(u-v)**2/4 for u,v in zip(x,y)]; d=sum(q,Q(0))
 f=root(a,g,h,t,priv); af=spectrum(f)
 for s in range(base):
  assert af[s]==p*x[s]+(1-p)*y[s]
  for u in range(1,4):assert af[s+base*u]==-ah[u]*(x[s]-y[s])/2
 assert influence(f)==p*influence(g)+(1-p)*influence(h)+d*influence(a)
 for i in range(2):assert edge_inf(f,t+2*priv+i)==d*edge_inf(a,i)
 path=add(add(entropy(f),entropy(g),-p),entropy(h),-(1-p))
 correction={}
 for u,v in zip(x,y):correction=add(correction,K(p,u,v))
 assert path==add(scale(hp(a),d),correction)
 # Exact integer-log verification of analytic constants C_1<11,C_2<13.
 cap=11 if t==1 else 13
 assert sign(add({2:cap*va*d},correction,-1))>=0
 vg=1-sum((z*z for z in ag[:shared]),Q(0)); vh=1-sum((z*z for z in bh[:shared]),Q(0))
 assert vg+vh<=4*d
 sigma=sum((abs(ag[i]**2-bh[i]**2) for i in range(shared)),Q(0))
 assert all(abs(ag[i]-bh[i])<=2*d for i in range(shared))
 for weighted in [False,True]:
  pg=[z*z for z in ag]; ph=[z*z for z in bh]
  rg=calibrated(pg,shared,weighted); rh=calibrated(ph,shared,weighted)
  xr=[Q(0)]*base; yr=[Q(0)]*base
  for s,z in enumerate(rg):xr[s]=z
  for s,z in enumerate(rh):yr[(s&(shared-1))|((s>>t)<<(t+priv))]=z
  ref=[Q(0)]*(4*base)
  for s in range(base):
   true=p*x[s]**2+(1-p)*y[s]**2; rr=p*xr[s]+(1-p)*yr[s]
   if true:
    ref[s]=rr*(p*x[s]+(1-p)*y[s])**2/true
    for u in range(1,4):ref[s+base*u]=rr*ah[u]**2*q[s]/true
   else:ref[s]=rr
  pf=[z*z for z in af]
  assert sum(ref)==1
  assert kl(pf,ref)==add(scale(kl(pg,rg),p),kl(ph,rh),1-p)
  cost=add(scale(ce(pg,rg),p),ce(ph,rh),1-p)
  assert ce(pf,ref)==add(cost,path)
 return {'p':str(p),'disagreement':str(d),'controller_variance':str(va),'shared_mass_difference':str(sigma),'correction':ser(correction)}
def main():
 start=time.perf_counter(); pilot='--pilot' in sys.argv; ns=nb=0
 for j in range(17):
  for x in ([1] if pilot else range(-8,9)):
   for y in ([-1,0,1] if pilot else range(-8,9)):
    p=Q(j,16); u=Q(x,8); v=Q(y,8); va=4*p*(1-p)
    rhs=va*(abs(u*u-v*v)+7*(u-v)**2/4)
    assert sign(add({2:rhs},K(p,u,v),-1))>=0; ns+=1
 for t,priv in [(2,0),(1,1)]:
  for ac in range(16):
   for gc in ([7] if pilot else range(16)):
    for hc in ([1] if pilot else range(16)):
     fixture=check_root(table(2,ac),table(2,gc),table(2,hc),t,priv); nb+=1
 result={'helper_version':'A056-biased-collision-v2-rational-interval','pilot':pilot,'scalar_cases':ns,'Boolean_roots':nb,'calibrated_reference_checks':2*nb,'result':'ALL PASS','seconds':time.perf_counter()-start,'last_fixture':fixture}
 (R/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
