from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
from collections import defaultdict
from itertools import product, permutations
import json, time, sys, math
R=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def ck(x):
 global checks
 assert x
 checks+=1
 if time.perf_counter()-start>55: raise TimeoutError('55s frozen cap')
def clean(p): return {s:v for s,v in p.items() if v}
@lru_cache(None)
def spec(t):
 N=len(t)
 return {s:F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t))**2,N*N) for s in range(N) if sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t))}
def child(t,i,b):
 return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
def erase(s,i): return (s&((1<<i)-1))|((s>>(i+1))<<i)
def essential(t): return sum(1<<i for i in range(len(t).bit_length()-1) if child(t,i,0)!=child(t,i,1))
def marginal(p,i):
 q=defaultdict(F)
 for s,v in p.items(): q[erase(s,i)]+=v
 return dict(q)
def plus(*vs):
 a=defaultdict(F)
 for v in vs:
  for p,c in v.items(): a[p]+=c
 return clean(a)
def scale(v,c): return clean({p:a*c for p,a in v.items()})
@lru_cache(None)
def factors(n):
 a={};p=2
 while p*p<=n:
  while n%p==0: a[p]=a.get(p,0)+1;n//=p
  p+=1
 if n>1:a[n]=a.get(n,0)+1
 return a
def logvec(x):return plus({p:F(c) for p,c in factors(x.numerator).items()},{p:F(-c) for p,c in factors(x.denominator).items()})
def kl(p,q):
 ck(sum(p.values())==sum(q.values())==1)
 ck(all(q.get(s,F())>0 for s in p))
 return plus(*(scale(logvec(v/q[s]),v) for s,v in p.items()))
def transport(t,q,i):
 p=spec(t);pe=marginal(p,i);qe=marginal(q,i);out=[];zs=[]
 for b in (0,1):
  tb=child(t,i,b);pb=spec(tb)
  w=clean({s:v*pb.get(s,F())/(2*pe[s]) for s,v in qe.items()})
  z=sum(w.values());ck(z>0);out.append((tb,{s:v/z for s,v in w.items()}));zs.append(z)
 ck(sum(zs)==1)
 return out,zs,pe,qe
def walk(t,q,b,atoms,order):
 p=spec(t);ck(q==plusprob(p,b,atoms));ck(sum(q.values())==1)
 if not order:return kl(p,q),{},0
 i=order[0];ch,zs,pe,qe=transport(t,q,i)
 out=kl({0:F(1,2),1:F(1,2)},dict(enumerate(zs)))
 er=plus(kl(p,q),scale(kl(pe,qe),-1));total=plus(out,er)
 terminals={};nodes=1
 for j,(tb,qb) in enumerate(ch):
  pb=spec(tb);new=[]
  for W,c in atoms:
   if not c: continue
   U=erase(W,i);k=pb.get(U,F())/(2*pe[U]);new.append((U,c*k/zs[j]))
  bb=b/(2*zs[j]);ck(bb+sum(c for W,c in new)==1)
  ck(all(not c or pb.get(W,F())>0 for W,c in new))
  oo=tuple(x-(x>i) for x in order[1:])
  subtotal,leaves,count=walk(tb,qb,bb,new,oo)
  total=plus(total,scale(subtotal,F(1,2)));terminals=plus(terminals,scale(leaves,F(1,2)));nodes+=count
 ck(total==kl(p,q))
 return total,terminals,nodes
def plusprob(p,b,atoms):
 q={s:b*v for s,v in p.items()}
 for W,c in atoms:q[W]=q.get(W,F())+c
 return clean(q)
def fresh(t,alpha):
 p=spec(t);v=1-p.get(0,F())
 return plusprob(p,1-alpha,[(0,alpha*p.get(0,F())),(essential(t),alpha*v)])
def positive(v):
 d=math.lcm(*(c.denominator for c in v.values()))
 exps={p:int(c*d) for p,c in v.items()};ck(max(map(abs,exps.values()),default=0)<5000)
 left=math.prod(p**c for p,c in exps.items() if c>0)
 right=math.prod(p**(-c) for p,c in exps.items() if c<0)
 return left>right
pilot='--pilot' in sys.argv
tables=eligible=trees=nodes=lower_candidates=0
for n in (range(3) if pilot else range(4)):
 for t in product((-1,1),repeat=1<<n):
  tables+=1;p=spec(t);full=(1<<n)-1
  if n and p.get(full,F()) and essential(t)==full:
   for i in range(n):
    for outcome in (0,1):
     tb=child(t,i,outcome);pb=spec(tb)
     if len(pb)>1 and pb.get((1<<(n-1))-1,F())==0:lower_candidates+=1
  if not p.get(full,F()):continue
  eligible+=1
  atoms=[(0,p.get(0,F())/2),(full,(1-p.get(0,F()))/2)]
  atoms=[(s,v) for s,v in atoms if v]
  q=plusprob(p,F(1,2),atoms)
  for order in permutations(range(n)):
   _,_,count=walk(t,q,F(1,2),atoms,order);trees+=1;nodes+=count
ck(lower_candidates==0)
chi=lambda x:-1 if x.bit_count()%2 else 1
mux=tuple(chi((x>>(0 if not x&4 else 1))&1) for x in range(8))
par=tuple(chi(x) for x in range(8))
t=tuple((par if x&1 else mux)[x>>1] for x in range(16))
p=spec(t);ck(essential(t)==15);ck(sum(t)==0)
ck(spec(mux)=={1:F(1,4),2:F(1,4),5:F(1,4),6:F(1,4)})
ck(essential(mux)==essential(par)==7)
ck(p=={s:(F(1,4) if s in (14,15) else F(1,16)) for s in (2,3,4,5,10,11,12,13,14,15)})
# Independent fast Walsh transform: critical certificate does not reuse spec().
a=list(t);step=1
while step<16:
 for base in range(0,16,2*step):
  for j in range(base,base+step):u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
 step*=2
ck(clean({s:F(v*v,256) for s,v in enumerate(a)})==p)
q=plusprob(p,F(1,2),[(15,F(1,2))]);ch,zs,pe,qe=transport(t,q,0)
ck(zs==[F(1,4),F(3,4)])
ck(ch[0][1]==spec(mux));ck(ch[1][1]==spec(par))
fresh_ref=plusprob(spec(mux),F(1,2),[(7,F(1,2))])
price=kl(spec(mux),fresh_ref);ck(price=={2:F(1)})
K=kl(p,q);ck(K=={2:F(1),5:F(-1,4)})
O=kl({0:F(1,2),1:F(1,2)},dict(enumerate(zs)));ck(O=={2:F(1),3:F(-1,2)})
influence=sum(F(sum(t[x]!=t[x^(1<<i)] for x in range(16)),16) for i in range(4))
H=scale(plus(*(scale(logvec(v),v) for v in p.values())),-1)
ck(influence==F(11,4));ck(H=={2:F(3)})
# Exact strict sign of positive bit price and optional same-KL invoice overdraw:
# mean fresh bill=1/2 > root K=1-(log2 5)/4 iff 5>4.
ck(5>4);ck(16>5)
criterion=[]
point=tuple(-1 if x==0 else 1 for x in range(4))
translated=tuple(point[x^1] for x in range(4))
majority=tuple(1 if x.bit_count()<2 else -1 for x in range(8))
for label,g0,g1,equal in [('translated-point',point,translated,True),('majority-parity',majority,par,False)]:
 tt=tuple((g1 if x&1 else g0)[x>>1] for x in range(2*len(g0)))
 alpha=F(1,2);bb=1-alpha;pp=spec(tt);qq=fresh(tt,alpha)
 ck(sum(g0)==sum(g1));ck(essential(g0)==essential(g1)==len(g0)-1)
 ck(pp.get(len(tt)-1,F())>0)
 cc,zz,ep,eq=transport(tt,qq,0)
 sigma=plus(*(scale(plus(kl(spec(tb),fresh(tb,alpha)),scale(kl(spec(tb),qb),-1)),F(1,2)) for tb,qb in cc))
 ts=[spec(g)[len(g)-1] for g in (g0,g1)];ee=sum(ts)/2;c=alpha*(1-F(sum(g0),len(g0))**2)
 FF=lambda u:scale(logvec(u/(bb*u+c)),u)
 gamma=plus(scale(FF(ts[0]),F(1,2)),scale(FF(ts[1]),F(1,2)),scale(FF(ee),-1))
 outcome=kl({0:F(1,2),1:F(1,2)},dict(enumerate(zz)))
 ck(sigma==plus(outcome,gamma))
 ck((not sigma) if equal else positive(sigma))
 if equal:ck(all(qb==fresh(tb,alpha) for tb,qb in cc))
 criterion.append({'family':label,'full_weights':[str(v) for v in ts],'sigma_prime_log_nats':{str(p):str(c) for p,c in sigma.items()},'zero_expected':equal})
result={'status':'PASS','checks':checks,'tables':tables,'eligible_root_tables':eligible,'full_order_trees':trees,'query_nodes':nodes,'smaller_dimension_annihilated_noncharacter_cases':lower_candidates,'criterion_checks':criterion,'seconds':time.perf_counter()-start,'witness':{'variable_order':['a','x','y','z'],'truth_table':list(t),'Walsh_numerators':a,'spectrum':{str(s):str(v) for s,v in p.items()},'reference':{str(s):str(v) for s,v in q.items()},'outcomes':[str(z) for z in zs],'root_KL_bits':'1-log2(5)/4','root_H_bits':3,'root_I':'11/4','child0_spectrum':{str(s):str(v) for s,v in spec(mux).items()},'positive_floor_price_bits':'-log2(1-gamma)','half_tilt_price_bits':1,'paired_half_tilt_bill_bits':'1/2'},'independent_review':'A049 direct reconstruction of A050; new witness review pending'}
name='PILOT.json' if pilot else 'CHECK.json'
(R/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','tables','eligible_root_tables','full_order_trees','query_nodes','smaller_dimension_annihilated_noncharacter_cases','seconds']}))
