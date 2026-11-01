from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json,time,itertools,sys
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v;checks+=1
 if time.perf_counter()-start>55:raise TimeoutError('frozen55s cap')
def plus(*xs):return sum((x[0] for x in xs),F()),sum((x[1] for x in xs),F())
def scale(x,k):return (x[0]*k,x[1]*k) if k>=0 else (x[1]*k,x[0]*k)
def rawln(x):
 z=(x-1)/(x+1);power=z;s=F()
 for j in range(32):s+=2*power/(2*j+1);power*=z*z
 return s,s+2*power/(65*(1-z*z))
LN2=rawln(F(2));GRID=1<<80
@lru_cache(None)
def ln(x):
 ck(x>0);k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
 if y<1:k-=1;y*=2
 a=plus(rawln(y),scale(LN2,k))
 return F(a[0].numerator*GRID//a[0].denominator,GRID),F(-((-a[1].numerator*GRID)//a[1].denominator),GRID)
def kl(p,q):
 ck(sum(p.values())==sum(q.values())==1)
 return plus(*(scale(ln(v/q[s]),v) for s,v in p.items() if v))
def entropy(p):return plus(*(scale(ln(v),-v) for v in p.values() if v))
def spectrum(t):
 a=list(t);step=1
 while step<len(a):
  for base in range(0,len(a),2*step):
   for j in range(base,base+step):x,y=a[j],a[j+step];a[j],a[j+step]=x+y,x-y
  step*=2
 return {s:F(v*v,len(t)**2) for s,v in enumerate(a) if v}
def child(t,j,b):return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))
def essential(t):return sum(1<<j for j in range(len(t).bit_length()-1) if child(t,j,0)!=child(t,j,1))
def fresh(t,a):
 p=spectrum(t);q={s:(v if s==0 else (1-a)*v) for s,v in p.items()}
 if 1-p.get(0,F()):q[essential(t)]=q.get(essential(t),F())+a*(1-p.get(0,F()))
 ck(sum(q.values())==1);return q
def transport(t,q,j):
 p=spectrum(t);pe=defaultdict(F);qe=defaultdict(F)
 erase=lambda u:(u&((1<<j)-1))|((u>>(j+1))<<j)
 for s,v in p.items():pe[erase(s)]+=v
 for s,v in q.items():qe[erase(s)]+=v
 out=[];Z=[]
 for b in (0,1):
  tb=child(t,j,b);pb=spectrum(tb)
  w={s:v*(pb.get(s,F())/(2*pe[s]) if pe[s] else F(1,2)) for s,v in qe.items()}
  z=sum(w.values());ck(z>0);qb={s:v/z for s,v in w.items() if v}
  ck(sum(qb.values())==1);ck(all(qb.get(s,F())>0 for s in pb));out.append((tb,qb));Z.append(z)
 ck(sum(Z)==1);return out,Z,dict(pe),dict(qe)
def invoice(t,j,a):
 p=spectrum(t);old=fresh(t,a);ch,Z,pe,qe=transport(t,old,j)
 new=plus(*(scale(kl(spectrum(tb),fresh(tb,a)),F(1,2)) for tb,_ in ch))
 inherited=plus(*(scale(kl(spectrum(tb),q),F(1,2)) for tb,q in ch))
 outcome=kl({0:F(1,2),1:F(1,2)},dict(enumerate(Z)))
 ck(all((1-a)/2<=z<=(1+a)/2 for z in Z))
 ck(outcome[1]<=a*a/(2*(1-a*a)))
 sigma=plus(new,scale(inherited,-1));res=plus(sigma,scale(outcome,-1))
 cross=plus(new,scale(kl(pe,qe),-1))
 ck(res[0]<=cross[1] and cross[0]<=res[1])
 ii=F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t))
 upper=(2+a/(1-a))*ii
 ck(res[1]<=upper or ii==0)
 # Prove the source-zero rows have not been dropped in the query identity.
 oldleft=plus(kl(pe,qe),scale(outcome,-1))
 ck(inherited[0]<=oldleft[1] and oldleft[0]<=inherited[1])
 return sigma,outcome,res,ii,Z
def activation(t,s):return tuple(s if x%2==0 else t[x//2] for x in range(2*len(t)))
def lift(t,s,a):
 p=spectrum(activation(t,s));q={u:v for u,v in p.items() if u<2}
 for u,v in fresh(t,a).items():
  if u:q[2*u]=q[2*u+1]=v/4
 ck(sum(q.values())==1);return q
def rare(r):
 h=lambda z:1-2*((z>>(1 if not z&1 else 2))&1)
 h0=tuple(h(z)*(-1 if z==1 else 1) for z in range(1<<r))
 h1=tuple(h(z)*(-1 if z in (1,4,5) else 1) for z in range(1<<r))
 return tuple((h1 if x&1 else h0)[x>>1] for x in range(1<<(r+1)))
def enc(v):return [str(x) for x in v]
a=F(1,6);small=0;tables=0;rows=[]
if '--pilot' not in sys.argv:
 for n in (2,3):
  for t in itertools.product((-1,1),repeat=1<<n):
   tables+=1
   if essential(t)!=(1<<n)-1:continue
   for j in range(n):
    ts=[child(t,j,b) for b in (0,1)]
    if any(essential(tb)!=(1<<(n-1))-1 for tb in ts):continue
    sigma,outcome,res,ii,Z=invoice(t,j,a);small+=1
    if sum(ts[0])==sum(ts[1]):ck(res[0]>=-F(1,1<<60))
for r in ([4] if '--pilot' in sys.argv else range(4,9)):
 t=rare(r);delta=F(1,1<<r);ck(essential(t)==(1<<(r+1))-1)
 ts=[child(t,0,b) for b in (0,1)];ps=[spectrum(tb) for tb in ts]
 ck(all(essential(tb)==(1<<r)-1 for tb in ts));ck([sum(tb) for tb in ts]==[-2,-2])
 t0,t1=[p[(1<<r)-1] for p in ps];ck(t0==4*delta*delta and t1==36*delta*delta)
 sigma,outcome,res,ii,Z=invoice(t,0,a);ck(ii==2*delta)
 c=a*(1-4*delta*delta);E=(t0+t1)/2
 gamma=plus(*(scale(ln(((1-a)+c/E)/((1-a)+c/v)),v/2) for v in (t0,t1)))
 ck(res[0]<=gamma[1] and gamma[0]<=res[1]);ck(gamma[0]>0)
 ck(gamma[1]<=8*delta*delta)
 ck(sigma[0]>LN2[1]/128)
 act=[]
 for s in (-1,1):
  jt=activation(t,s);q=lift(t,s,a);ch,zs,pe,qe=transport(jt,q,1)
  avg=plus(*(scale(plus(kl(spectrum(tb),lift(ts[b],s,a)),scale(kl(spectrum(tb),qq),-1)),F(1,2)) for b,(tb,qq) in enumerate(ch)))
  out=kl({0:F(1,2),1:F(1,2)},dict(enumerate(zs)))
  predicted=plus(out,scale(gamma,F(1,2)))
  ck(avg[0]<=predicted[1] and predicted[0]<=avg[1]);ck(avg[0]>LN2[1]/512)
  act.append({'sign':s,'sigma_nats':enc(avg),'outcome_nats':enc(out),'reference_outcomes':[str(z) for z in zs]})
 rows.append({'r':r,'query_influence':str(ii),'sigma_nats':enc(sigma),'outcome_nats':enc(outcome),'remainder_nats':enc(res),'gamma_nats':enc(gamma),'reference_outcomes':[str(z) for z in Z],'activations':act})
result={'status':'PASS','checks':checks,'small_truth_tables':tables,'stable_mask_queries':small,'rare_cases':rows,'seconds':time.perf_counter()-start,'units':'natural logs in certificates; bit claims divide by ln2','external_review':'same-agent code only; A047 statement independently reconstructed by A049'}
name='PILOT.json' if '--pilot' in sys.argv else 'CHECK.json'
(R/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','small_truth_tables','stable_mask_queries','seconds']}))
