from fractions import Fraction as F
from pathlib import Path
import sys,json,time
R=Path(__file__).resolve().parents[1];START=time.perf_counter()
checks=nodes=trees=resets=ghosts=positive_caps=zero_rows=0
def eq(a,b):
 global checks
 assert a==b,(a,b);checks+=1
def coeff(v):
 a=list(v);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):x,y=a[i],a[i+h];a[i],a[i+h]=x+y,x-y
  h*=2
 return [F(x,len(a)) for x in a]
def source(v,s):
 a=coeff(v);p=[x*x for x in a]
 P=[(s+a[0])**2/4,(s-a[0])**2/4]+[x/4 for x in p[1:] for _ in range(2)]
 return p,P
def essential(p):
 m=0
 for t,x in enumerate(p):
  if x:m|=t
 return m
def fresh(p,P,gamma):
 v=1-p[0];M=essential(p)
 q=[p[0]]+[(1-gamma)*x for x in p[1:]]
 if M:q[M]+=gamma*v
 return [P[0],P[1]]+[x/4 for x in q[1:] for _ in range(2)],(1-gamma,gamma*v,M,P[0],P[1])
def model(p,state):
 A,B,M,V0,V1=state
 return [V0,V1]+[(A*p[t]+B*(t==M))/4 for t in range(1,len(p)) for _ in range(2)]
def drop(t,i):return (t&((1<<i)-1))|((t>>(i+1))<<i)
def ins(t,i,b):return (t&((1<<i)-1))|(b<<i)|((t>>i)<<(i+1))
def restrict(v,i,b):return [v[ins(t,i,b)] for t in range(len(v)//2)]
def erase(v,i):
 out=[F(0)]*(len(v)//2)
 for t,x in enumerate(v):out[drop(t,i)]+=x
 return out
def transport(v,s,Q,state,i,b):
 global zero_rows
 p,P=source(v,s);w=restrict(v,i,b);pc,Pc=source(w,s)
 E=erase(P,i+1);D=erase(Q,i+1);raw=[]
 for e,d,pp in zip(E,D,Pc):
  if not e:zero_rows+=1
  raw.append(d*(pp/(2*e) if e else F(1,2)))
 Z=sum(raw);assert Z>0;old=[x/Z for x in raw]
 A,B,M,V0,V1=state;Mn=drop(M,i)
 V=[]
 for c in range(2):
  er=P[c]+p[1<<i]/4
  dr=(V0 if c==0 else V1)+(A*p[1<<i]+B*(M==1<<i))/4
  V.append(dr*(Pc[c]/(2*er) if er else F(1,2))/Z)
 if Mn:
  t=ins(Mn,i,0);e=p[t]+p[t|(1<<i)]
  km=pc[Mn]/(2*e) if e else F(1,2)
  Bn=B*km/Z
 else:Bn=F(0)
 st=(A/(2*Z),Bn,Mn,V[0],V[1]);eq(model(pc,st),old);eq(sum(old),1)
 return w,pc,Pc,old,st
def return_reference(p,P,old,state,half):
 global resets,ghosts,positive_caps
 A,B,M,V0,V1=state;v=1-p[0];ess=essential(p)
 assert ess&~M==0
 if not v:
  new,st=fresh(p,P,F(0));return new,st,F(0),F(0)
 beta=B/(A*v+B);assert 0<=beta<1
 gamma=beta/2 if half else beta
 assert 0<=gamma<=beta
 if gamma:positive_caps+=1
 if M!=ess:eq(p[M],0);ghosts+=1
 pi=v/2;rho=sum(old[2:]);assert rho>0
 # Exact canonical nonempty conditional profile, before optional retarget/clamp.
 canonical=[P[0],P[1]]+[(1-beta)*p[t]/4+beta*v*(t==M)/4 for t in range(1,len(p)) for _ in range(2)]
 eq([x*pi/rho for x in old[2:]],canonical[2:])
 new,st=fresh(p,P,gamma);eq(sum(new),1);resets+=1
 return new,st,beta,gamma
def recurse(v,s,Q,state,order,policy,depth=0):
 global nodes
 nodes+=1;assert time.perf_counter()-START<55,'frozen runtime exceeded'
 p,P=source(v,s);eq(model(p,state),Q);eq(sum(Q),1)
 if not order:return
 i=order[0]
 for b in (0,1):
  w,pc,Pc,old,st=transport(v,s,Q,state,i,b)
  remaining=[j-(j>i) for j in order[1:]]
  if policy!=1 or (depth+1)%2==0 or not remaining:
   old,st,_,_=return_reference(pc,Pc,old,st,policy!=0)
  recurse(w,s,old,st,remaining,policy,depth+1)
def main():
 global trees
 pilot='--pilot' in sys.argv
 for n in range(3 if pilot else 4):
  orders=[tuple(range(n))]
  if n<=2:orders=list(dict.fromkeys(orders+[tuple(reversed(range(n)))]))
  for table in range(1<<(1<<n)):
   vals=[1 if table>>x&1 else -1 for x in range(1<<n)]
   for s in ((1,) if n==3 else (-1,1)):
    p,P=source(vals,s)
    for alpha in ((F(1,7),) if n==3 else (F(1,7),F(1,2))):
     for policy in ((2,) if n==3 else (0,1)):
      for order in orders:
       Q,st=fresh(p,P,alpha);trees+=1;recurse(vals,s,Q,st,list(order),policy)
 result={'status':'PASS','pilot':pilot,'trees':trees,'nodes':nodes,'assertions':checks,'positive_parameter_returns':positive_caps,'source_zero_kernel_evaluations':zero_rows,'ghost_mask_retargets':ghosts,'nonconstant_returns':resets,'seconds':time.perf_counter()-START,'scope':'exact dense/four-scalar transport and sufficient return conditions; all-n nonpositive theorem is analytic, not inferred from counts'}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
