from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,sys,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic();count=0
def ck(x):
 global count
 count+=1
 assert x,count
 if time.monotonic()-START>55: raise TimeoutError('frozen55seconds')
@lru_cache(None)
def ln(x):
 assert x>0
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 y=(x-1)/(x+1);z=y*y;term=y;s=F(0)
 for j in range(20):s+=term/F(2*j+1);term*=z
 lo=2*s;hi=lo+2*term/(41*(1-z))
 return lo,hi,k
def raw_ln2():
 y=F(1,3);z=y*y;term=y;s=F(0)
 for j in range(20):s+=term/F(2*j+1);term*=z
 return 2*s,2*s+2*term/(41*(1-z))
L2=raw_ln2()
@lru_cache(None)
def log(x):
 lo,hi,k=ln(x)
 lo,hi=F(k)+lo/L2[1],F(k)+hi/L2[0]
 grid=1<<100
 return F((lo*grid).__floor__(),grid),F((hi*grid).__ceil__(),grid)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def scale(a,t):return (a[0]*t,a[1]*t) if t>=0 else (a[1]*t,a[0]*t)
def cost(P,Q,mults):
 out=(F(0),F(0))
 for p,q,k in zip(P,Q,mults):
  if p:ck(q>0);out=add(out,scale(log(1/q),k*p))
 return out
def entropy(P,M):return cost(P,P,M)
def divergence(P,Q,M):return sub(cost(P,Q,M),entropy(P,M))
def walsh(a,table):
 vals=[F(1 if table>>x&1 else -1) for x in range(1<<a)]
 sign=vals[0];vals=[v*sign for v in vals]
 for b in range(a):
  for x in range(1<<a):
   if not x>>b&1:
    y=x|(1<<b);v,w=vals[x],vals[y];vals[x],vals[y]=v+w,v-w
 return [v/(1<<a) for v in vals]
def profile(a,table,m,mass,witness=False):
 A=walsh(a,table);e=F(1,1<<(a+m));M=[1]*len(A)
 # Additional dummy-nonempty masks all have A=0. Aggregation is exact.
 if m:A.append(F(0));M.append((1<<(a+m))-(1<<a))
 q=[(v-e)**2+e*e for v in A]
 P0=[(v-2*e)**2 for v in A];P1=[v*v for v in A]
 R=[mass*(v*v+3*e*e)/(1+3*e) for v in A]
 T=[(v*v+6*e*e)/(1+6*e) for v in A]
 for P in [q,P0,P1,T]:ck(sum(p*k for p,k in zip(P,M))==1)
 ck(sum(r*k for r,k in zip(R,M))==mass)
 C0=cost(q,R,M);H0=entropy(q,M) # joint conditional selector entropy added below
 # Joint selector spectrum: ((A-e)^2,e^2); parent R uses true selector kernel.
 PP=[];QQ=[];MM=[]
 for v,r,qv,k in zip(A,R,q,M):
  for p in [(v-e)**2,e*e]:PP.append(p);QQ.append(r*p/qv);MM.append(k)
 rootce=cost(PP,QQ,MM);rooth=entropy(PP,MM)
 Dparent=divergence(PP,QQ,MM);dchildren=[];cs=[];hs=[];outs=[];zs=[]
 positive=None
 for idx,P in enumerate([P0,P1]):
  raw=[r*p/qv for r,p,qv in zip(R,P,q)]
  Z=sum(r*k for r,k in zip(raw,M));zs.append(Z);ck(Z>0)
  Q=[mass*r/Z for r in raw]
  ck(sum(r*k for r,k in zip(Q,M))==mass)
  dchildren.append(divergence(P,Q,M));cs.append(cost(P,Q,M));hs.append(entropy(P,M))
  if witness:
   # A011 root rho=e/2, beta=3e; exposed child rho=e, beta=6e, U=e.
   target=[(v*v+6*e*e)/(1+6*e) for v in A] if idx==0 else [v*v for v in A]
  else:target=T if idx==0 else [v*v for v in A]
  outs.append(cost(P,target,M))
  if idx==0 and not witness:
   D=divergence(P,T,M);chi=sum(k*(p-t)**2/t for p,t,k in zip(P,T,M))
   ck(D[1]<2*e);ck(chi<F(4,3)*e)
   charge=sub(outs[-1],cs[-1]);ck(charge[1]<2*e)
   if a==4 and table==1 and mass==1:
    ck(charge[0]>0)
    # Source mask1 and a dummy-nonempty mask are both nonempty full masks.
    ck(T[1]*Q[-1]!=T[-1]*Q[1])
    positive={'m':m,'charge_interval':[str(v) for v in charge],'nonempty_cross_products_differ':True}
  if idx==1:ck(sub(outs[-1],cs[-1])[1]<F(1,10**15))
 ck(sum(zs)==2*mass)
 prod=zs[0]*zs[1]/(mass*mass);ck(prod<=1)
 delta=scale(neg(log(prod)),F(1,2))
 dcalc=sub(Dparent,scale(add(*dchildren),F(1,2)))
 ck(sub(delta,dcalc)[0]<=0<=sub(delta,dcalc)[1])
 charges=scale(add(sub(outs[0],cs[0]),sub(outs[1],cs[1])),F(1,2))
 lhs=add(rootce,charges)
 functional=add(rooth,scale(add(sub(outs[0],hs[0]),sub(outs[1],hs[1])),F(1,2)))
 residual=sub(sub(lhs,functional),delta);ck(residual[0]<=0<=residual[1])
 result={'a':a,'table':table,'m':m,'mass':str(mass),'Z0':str(zs[0]),'Z1':str(zs[1]),'product':str(prod),'delta_interval':[str(t) for t in delta]}
 if positive:result['positive_witness']=positive
 if witness:
  ck(prod<1);ck(delta[0]>0);ck(sub(lhs,functional)[0]>0)
  result.update({'CEroot_plus_actual_resets':[str(t) for t in lhs],'claimed_terminal_functional':[str(t) for t in functional]})
 return result
mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
cases=[(a,t) for a in range(4) for t in range(1<<(1<<a))]
if mode=='pilot':cases=cases[:6]
rows=[]
for a,t in cases:
 for mass in [F(1),F(1,2)]:rows.append(profile(a,t,8,mass))
if mode=='main':
 for m in [8,12]:
  for mass in [F(1),F(1,2)]:rows.append(profile(4,1,m,mass))
 witnesses=[profile(1,1,b,F(1),True) for b in [12,13]]
else:witnesses=[]
out={'mode':mode,'profiles':len(rows),'positive_witnesses':[r['positive_witness'] for r in rows if 'positive_witness' in r],'witnesses':witnesses,'assertions':count,'seconds':time.monotonic()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite exact checks; analytic proof recorded separately'}
ROOT.joinpath('out',mode.upper()+'.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}))
