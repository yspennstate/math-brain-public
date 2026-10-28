from fractions import Fraction as F
from functools import lru_cache
import check as C
import json,time
R=C.R;start=time.perf_counter()
def ln(x):
 z=(x-1)/(x+1);z2=z*z;t=z;lo=F(0)
 for j in range(32):lo+=2*t/F(2*j+1);t*=z2
 return lo,lo+2*t/F(65)/(1-z2)
L2=ln(F(2))
@lru_cache(maxsize=2048)
def log(x):
 e=0
 while x<1:x*=2;e-=1
 while x>=2:x/=2;e+=1
 a,b=ln(x);return e+a/L2[1],e+b/L2[0]
def kl(p,q):
 a=b=F(0)
 for x,y in zip(p,q):
  if x:
   u,v=log(x/y);a+=x*u;b+=x*v
 return a,b
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,c):return a[0]*c,a[1]*c
def qcore(p,alpha):
 m=C.essential(p);q=[p[0]]+[(1-alpha)*x for x in p[1:]]
 if m:q[m]+=alpha*(1-p[0])
 return q
def bare(v,i,alpha):
 p,_=C.source(v,1);q=qcore(p,alpha);e=C.erase(p,i);d=C.erase(q,i)
 fresh=old=(F(0),F(0));Z=[];children=[]
 for b in (0,1):
  w=C.restrict(v,i,b);pc,_=C.source(w,1);new=qcore(pc,alpha)
  raw=[dd*(pp/(2*ee) if ee else F(1,2)) for ee,dd,pp in zip(e,d,pc)]
  z=sum(raw);Z.append(z);qo=[x/z for x in raw]
  old=add(old,mul(kl(pc,qo),F(1,2)));fresh=add(fresh,mul(kl(pc,new),F(1,2)))
  children.append(w)
 return sub(fresh,old),kl([F(1,2),F(1,2)],Z),children,p
cores=[[-1 if x.bit_count()==1 else 1 for x in range(8)],
       [(-1 if x>>1&1 else 1) if not x&1 else (-1 if x>>2&1 else 1) for x in range(8)],
       [1 if x.bit_count()<=1 else -1 for x in range(8)],
       [(-1)**x.bit_count()*(-1 if x==7 else 1) for x in range(8)]]
residual=adaptive=shape_changes=0;fixtures=[]
for idx,v in enumerate(cores):
 for i in range(3):
  for alpha in (F(1,7),F(1,2)):
   sig,O,ch,p=bare(v,i,alpha)
   if all(C.essential(C.source(w,1)[0])==3 for w in ch):
    influence=sum(x for t,x in enumerate(p) if t&(1<<i))
    rhs=O[0]+(2+alpha/(1-alpha))*influence/L2[1]
    assert sig[1]<=rhs;residual+=1
 # Direct actual-selector transform, dense transport, inherited-cap return.
 for s in (-1,1):
  p,P=C.source(v,s);Q,st=C.fresh(p,P,F(1,7))
  actual=[a for g in v for a in (s,g)]
  assert [a*a for a in C.coeff(actual)]==P
  for b in (0,1):
   w,pc,Pc,old,state=C.transport(v,s,Q,st,0,b)
   new,ns,beta,gamma=C.return_reference(pc,Pc,old,state,True)
   pi=(1-pc[0])/2;rho=sum(old[2:])
   if pi and [x/rho for x in old[2:]]!=[x/pi for x in new[2:]]:shape_changes+=1
   if all(not x or old[j]==new[j] for j,x in enumerate(Pc)):delta=(F(0),F(0))
   else:delta=sub(kl(Pc,new),kl(Pc,old));assert delta[1]<0
   adaptive+=1;fixtures.append({'core':idx,'s':s,'b':b,'beta':str(beta),'gamma':str(gamma),'delta_interval':[str(x) for x in delta]})
# A047 literal stable-mask/equal-mean input at r4, independent direct definition.
r=4;g=[]
for x in range(1<<(r+1)):
 a=x&1;z=x>>1;h=(-1 if z>>1&1 else 1) if not z&1 else (-1 if z>>2&1 else 1)
 if z in ((1,4,5) if a else (1,)):h=-h
 g.append(h)
equal_mean=0
for alpha in (F(1,7),F(1,2)):
 sig,O,ch,p=bare(g,0,alpha)
 assert sum(ch[0])==sum(ch[1])
 # Exact analytical Gamma formula plus certified comparison to sigma-O.
 t=[C.source(w,1)[0][-1] for w in ch];E=sum(t)/2;mu=F(sum(g),len(g));c=alpha*(1-mu*mu);b=1-alpha
 gamma=(F(0),F(0))
 for tb in t:gamma=add(gamma,mul(log((b+c/E)/(b+c/tb)),tb/2))
 rest=sub(sig,O);assert max(rest[0],gamma[0])<=min(rest[1],gamma[1])
 influence=sum(x for j,x in enumerate(p) if j&1)
 assert gamma[0]>=0 and gamma[1]<=2*influence/L2[1];equal_mean+=1
# Adversarial guard: SAMEalpha fixed return is actually POSITIVE on weight-one3.
v=cores[0];p,P=C.source(v,1);Q,st=C.fresh(p,P,F(1,7));fixed=(F(0),F(0))
for b in (0,1):
 w,pc,Pc,old,state=C.transport(v,1,Q,st,0,b);new,_=C.fresh(pc,Pc,F(1,7))
 fixed=add(fixed,mul(sub(kl(Pc,new),kl(Pc,old)),F(1,2)))
assert fixed[0]>0
# A positive floor cannot be restored for free after a zero-cap canonical match.
gate=[]
for x in range(32):
 gate.append((-1 if x&1 else 1)*(-1 if (x>>1)&3==3 else 1)*(-1 if (x>>3)&3==3 else 1))
p,P=C.source(gate,1);Q,st=C.fresh(p,P,F(1,7));w,pc,Pc,old,state=C.transport(gate,1,Q,st,3,0)
matched,_,beta,_=C.return_reference(pc,Pc,old,state,False);assert beta==0 and matched==Pc
floor,_=C.fresh(pc,Pc,F(1,7));floor_price=kl(Pc,floor);assert floor_price[0]>0
assert time.perf_counter()-start<55
assert shape_changes>0
out={'status':'PASS','A049_generic_residual_cases':residual,'equal_mean_cases':equal_mean,'adaptive_child_cases':adaptive,'genuine_nonempty_profile_changes':shape_changes,'fixed_alpha_guard_interval':[str(x) for x in fixed],'zero_cap_floor_price':[str(x) for x in floor_price],'seconds':time.perf_counter()-start,'fixtures':fixtures,'independence':'Producer code not imported; current structural helper shared for source/transport; residual proof independently reconstructed; no external review of new adaptive theorem claimed'}
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('fixtures','fixed_alpha_guard_interval','zero_cap_floor_price')}))
