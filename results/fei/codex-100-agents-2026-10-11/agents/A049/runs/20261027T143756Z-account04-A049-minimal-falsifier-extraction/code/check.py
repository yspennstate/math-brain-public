from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
from itertools import product
import json,time,sys,math
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
 if time.perf_counter()-start>55:raise TimeoutError('frozen55s cap')
def clean(d):return {s:v for s,v in d.items() if v}
def add(*vs):
 d=defaultdict(F)
 for v in vs:
  for p,c in v.items():d[p]+=c
 return clean(d)
def mul(v,k):return clean({p:c*k for p,c in v.items()})
@lru_cache(None)
def factors(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def logv(x):
 ck(x>0)
 return add({p:F(c) for p,c in factors(x.numerator).items()},{p:F(-c) for p,c in factors(x.denominator).items()})
def ent(p):return mul(add(*(mul(logv(v),v) for v in p.values())),-1)
def kl(p,q):
 ck(sum(p.values())==sum(q.values())==1)
 return add(*(mul(logv(v/q[s]),v) for s,v in p.items()))
def sign(v):
 if not v:return 0
 den=math.lcm(*(c.denominator for c in v.values()))
 ex={p:int(c*den) for p,c in v.items()};ck(max(map(abs,ex.values()),default=0)<5000)
 a=math.prod(p**e for p,e in ex.items() if e>0);b=math.prod(p**(-e) for p,e in ex.items() if e<0)
 return (a>b)-(a<b)
@lru_cache(None)
def spectrum(t):
 a=list(t);step=1
 while step<len(a):
  for base in range(0,len(a),2*step):
   for j in range(base,base+step):u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
  step*=2
 return clean({s:F(v*v,len(t)**2) for s,v in enumerate(a)})
def child(t,i,b):return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
def erase(s,i):return (s&((1<<i)-1))|((s>>(i+1))<<i)
def marginal(p,i):
 d=defaultdict(F)
 for s,v in p.items():d[erase(s,i)]+=v
 return clean(d)
def influences(p,n):return [sum(v for s,v in p.items() if s&(1<<i)) for i in range(n)]
def transport(t,q,i):
 p=spectrum(t);ep=marginal(p,i);eq=marginal(q,i);ch=[];zs=[]
 for b in (0,1):
  tb=child(t,i,b);pb=spectrum(tb)
  w=clean({s:v*(pb.get(s,F())/(2*ep[s]) if ep.get(s,F()) else F(1,2)) for s,v in eq.items()})
  z=sum(w.values());ck(z>0);zs.append(z);ch.append((tb,{s:v/z for s,v in w.items()}))
 ck(sum(zs)==1)
 return ch,zs,ep,eq
def calibrate(p,q):
 r=p.get(0,F());z=q.get(0,F())
 if r==1:qs=dict(p)
 else:
  k=(1-r)/(1-z);qs=clean({s:(r if s==0 else k*v) for s,v in q.items()})
  if r:qs[0]=r
 d=kl(clean({0:r,1:1-r}),clean({0:z,1:1-z}))
 ck(qs.get(0,F())==r);ck(sum(qs.values())==1)
 ck(add(kl(p,q),mul(kl(p,qs),-1))==d)
 return qs,d
def mixture(p,b,atoms):
 q={s:b*v for s,v in p.items()}
 for s,c in atoms:q[s]=q.get(s,F())+c
 return clean(q)
pilot='--pilot' in sys.argv
tables=queries=calibrations=ghost_rows=full3=deformations=0
for n in (range(3) if pilot else range(4)):
 for t in product((-1,1),repeat=1<<n):
  tables+=1;p=spectrum(t);N=1<<n
  q={s:p.get(s,F())/2+F(1,2*N) for s in range(N)}
  b=F(1,2);atoms=[(s,F(1,2*N)) for s in range(N)]
  ck(q==mixture(p,b,atoms))
  for i in range(n):
   queries+=1;ch,zs,ep,eq=transport(t,q,i)
   E=add(kl(p,q),mul(kl(ep,eq),-1));O=kl({0:F(1,2),1:F(1,2)},dict(enumerate(zs)))
   ck(sign(E)>=0);ck(sign(O)>=0)
   J=ent(ep);childCE={};rawKL={};release={}
   for outcome,(tb,qb) in enumerate(ch):
    pb=spectrum(tb);qs,d=calibrate(pb,qb);calibrations+=1
    ghost_rows+=sum(s not in pb for s in qb)
    r=pb.get(0,F());z=qb.get(0,F());k=(1-r)/(1-z) if r<1 else F(0)
    bp=b/(2*zs[outcome]);new=[]
    if r<1:
     for W,c in atoms:
      U=erase(W,i);kernel=pb.get(U,F())/(2*ep[U]) if ep.get(U,F()) else F(1,2)
      if U:new.append((U,k*c*kernel/zs[outcome]))
     bc=k*bp;new.append((0,r*(1-bc)))
    else:bc=F(1)
    ck(0<bc<=1);ck(qs==mixture(pb,bc,new));ck(bc+sum(c for _,c in new)==1)
    rawKL=add(rawKL,mul(kl(pb,qb),F(1,2)));release=add(release,mul(d,F(1,2)))
    childCE=add(childCE,mul(add(ent(pb),kl(pb,qs)),F(1,2)));J=add(J,mul(ent(pb),F(-1,2)))
   ck(kl(p,q)==add(E,O,rawKL))
   B=add(ent(p),mul(ent(ep),-1))
   ck(add(B,childCE)==add(ent(p),kl(p,q),mul(add(J,E,O,release),-1)))
  if n==3 and len(p)==8:
   full3+=1
   dq={s:(F(0) if s==0 else F([0,1,-2,3][s.bit_count()],64)) for s in range(8)}
   qc={s:p[s]+dq[s] for s in range(8)}
   ck(min(qc.values())>0);ck(sum(qc.values())==1);ck(qc[0]==p[0]);ck(influences(qc,n)==influences(p,n));ck(qc!=p)
   for i in range(n):
    Ei=add(kl(p,qc),mul(kl(marginal(p,i),marginal(qc,i)),-1))
    ck(sign(Ei)>0);deformations+=1
# Parameter-free minimal Boolean circuit/reference certificate.
t=tuple(-1 if x==0 else 1 for x in range(8));p=spectrum(t)
direct={s:F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t))**2,64) for s in range(8)}
ck(p==direct);ck(p=={s:F(9 if s==0 else 1,16) for s in range(8)})
q={s:F([36,5,2,7][s.bit_count()],64) for s in range(8)}
ck(sum(q.values())==1);ck(q[0]==p[0]);ck(influences(q,3)==influences(p,3)==[F(1,4)]*3)
K=kl(p,q);ck(K==mul(logv(F(2048,875)),F(1,16)));rows=[]
for i in range(3):
 ch,zs,ep,eq=transport(t,q,i);L=add(K,mul(kl(ep,eq),-1));O=kl({0:F(1,2),1:F(1,2)},dict(enumerate(zs)))
 ck(ep=={0:F(5,8),1:F(1,8),2:F(1,8),3:F(1,8)})
 ck(eq=={0:F(41,64),1:F(7,64),2:F(7,64),3:F(9,64)})
 ck(zs==[F(39,80),F(41,80)])
 ck(ch[0][1]=={0:F(41,156),1:F(35,156),2:F(35,156),3:F(45,156)})
 ck(ch[1][1]=={0:F(1)})
 ck(O==mul(logv(F(1600,1599)),F(1,2)))
 ck(sign(add(L,{2:F(-7,100)}))>0)
 ck(sign(add(L,mul(K,F(-15,16))))>0)
 ck(sign(O)>0)
 avgchild=add(*(mul(kl(spectrum(tb),qb),F(1,2)) for tb,qb in ch))
 ck(K==add(L,O,avgchild));rows.append({'coordinate':i,'L_prime_log_bits':{str(p):str(v) for p,v in L.items()},'outcomes':[str(z) for z in zs]})
H=ent(p);I=sum(influences(p,3));ck(I==F(3,4));ck(sign(add({2:4*I},mul(add(H,K),-1)))>0)
result={'status':'PASS','checks':checks,'tables':tables,'calibration_queries':queries,'child_calibrations':calibrations,'retained_ghost_rows_before_calibration':ghost_rows,'full_support_3bit_tables':full3,'strict_calibrated_erasure_queries':deformations,'seconds':time.perf_counter()-start,'witness':{'truth_table':list(t),'variable_order':['x0','x1','x2'],'P':{str(s):str(v) for s,v in p.items()},'Q':{str(s):str(v) for s,v in q.items()},'I':'3/4','H_bits':'4-(9/8)log2(3)','K_bits':'log2(2048/875)/16','every_coordinate_L_bits_lower_bound':'7/100','every_coordinate_L_over_K_lower_bound':'15/16','every_coordinate_O_bits':'log2(1600/1599)/2','root_full_CE_less_than':'4I=3','rows':rows},'limits':'Universal equality theorem analytically proved separately; no FEI counterexample; no unpaid query KL removed.'}
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','tables','calibration_queries','child_calibrations','retained_ghost_rows_before_calibration','full_support_3bit_tables','strict_calibrated_erasure_queries','seconds']}))
