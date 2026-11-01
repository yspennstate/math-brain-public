"""Independent of exact.py/validate.py: literal Walsh; rational prime-log cancellation."""
from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();C=0
def ck(x):
 global C
 C+=1;assert x,C;assert time.perf_counter()-start<55
def law(t):
 n=len(t);return [F(sum(v*(-1)**((s&z).bit_count()%2) for z,v in enumerate(t))**2,n*n) for s in range(n)]
def restrict(t,j,y):return [v for z,v in enumerate(t) if (z>>j)&1==y]
def primes(k):
 out={};d=2
 while d*d<=k:
  while k%d==0:out[d]=out.get(d,0)+1;k//=d
  d+=1
 if k>1:out[k]=out.get(k,0)+1
 return out
def logs(x):
 out={}
 for p,a in primes(x.numerator).items():out[p]=F(a)
 for p,a in primes(x.denominator).items():out[p]=out.get(p,F(0))-a
 return {p:a for p,a in out.items() if a}
def plus(a,b,c=F(1)):
 out=a.copy()
 for p,v in b.items():out[p]=out.get(p,F(0))+c*v
 return {p:v for p,v in out.items() if v}
def kl(p,q):
 out={}
 for x,y in zip(p,q):
  if x:out=plus(out,logs(x/y),x)
 return out
def qfactor(t,beta):
 p=law(t)
 if len(t)<=2 or abs(sum(t))==len(t):return p
 q=[p[0]]+[beta*x for x in p[1:]];q[-1]+=(1-beta)*(1-p[0]);return q
def tensor(a,b):return [x*y for y in b for x in a]
def lift(v,u,eps,bv,bu):
 core=tensor(v,u);t=[eps if z%2==0 else core[z//2] for z in range(2*len(core))];p=law(t);q=[F(0)]*len(p);q[:2]=p[:2];qq=tensor(qfactor(v,bv),qfactor(u,bu))
 for s in range(1,len(qq)):q[2*s]=q[2*s+1]=qq[s]/4
 ck(sum(q)==1);return t,p,q
def step(t,q):
 p=law(t);tt=[restrict(t,1,y) for y in [0,1]];ps=[law(t) for t in tt];pp=[p[k]+p[k|2] for k in range(len(p)) if not k&2];qq=[q[k]+q[k|2] for k in range(len(q)) if not k&2];joint=[[qq[k]*ps[y][k]/(2*pp[k]) if pp[k] else qq[k]/2 for k in range(len(pp))] for y in [0,1]];r=[sum(x) for x in joint];old=[[a/r[y] for a in joint[y]] for y in [0,1]];ck(sum(r)==1);return tt,ps,old,r
rows=[]
for w in [2,3,4]:
 for u in [[1],[-1],[1,-1],[-1,1,1,1]]:
  for eps in [1,-1]:
   v=[-1]+[1]*((1<<w)-1);b=F(5,6);bn=F(4,5);t,p,q=lift(v,u,eps,b,F(7,8));ts,ps,old,rr=step(t,q);change={};same={};inc={}
   for y in [0,1]:
    vy=restrict(v,0,y);tt,py,mid=lift(vy,u,eps,b,F(7,8));_,_,new=lift(vy,u,eps,bn,F(7,8));ck(tt==ts[y]);ck(py==ps[y]);change=plus(change,plus(kl(py,new),kl(py,old[y]),-1),F(1,2));same=plus(same,plus(kl(py,mid),kl(py,old[y]),-1),F(1,2));inc=plus(inc,plus(kl(law(vy),qfactor(vy,bn)),kl(law(vy),qfactor(vy,b)),-1),F(1,4))
   ck(change==plus(same,inc));rows.append({'w':w,'spectator':u,'epsilon':eps,'actual_outcomes':list(map(str,rr)),'exact_prime_log_profile_difference':{str(p):str(v) for p,v in inc.items()}})
# A completely separate exact martingale audit: profiles have rational levels,
# i.e. beta=(5/6)(99/100)^level, level<=3. Child-adapted schedules.
mart=[]
for policy in range(27):
 original=[-1]+[1]*7;V0=1-F(sum(original),8)**2;front=[(F(1),original,0)];cost=F(0);cross=[F(0)]*3
 for depth in range(3):
  nxt=[]
  for weight,t,level in front:
   local_charge=F(0);local_residual=F(0);vp=1-F(sum(t),len(t))**2
   for y in [0,1]:
    child=restrict(t,0,y);newlevel=min(3,level+((policy//(3**depth)+y)%3));vv=1-F(sum(child),len(child))**2;cost+=weight*vv*(newlevel-level)/2
    for ell in range(level,newlevel):cross[ell]+=weight*vv/2
    local_charge+=vv*(newlevel-level)/2;local_residual+=vv*(3-newlevel)/2
    nxt.append((weight/2,child,newlevel))
   ev=sum((1-F(sum(restrict(t,0,y)),len(t)//2)**2 for y in [0,1]),F(0))/2
   ck(vp*(3-level)-local_charge-local_residual==(3-level)*(vp-ev));ck(vp*(3-level)>=local_charge+local_residual)
  front=nxt
 ck(cost==sum(cross));ck(all(x<=V0 for x in cross));ck(cost<=3*V0);mart.append({'policy':policy,'cost_in_log_units':str(cost),'initial_variance':str(V0),'crossing_bills':list(map(str,cross))})
# Choosing the increment only in the active child disproves naive factorization.
lhs=F(1,2)*F(3,4);wrong=F(1,2)*F(7,16);ck(lhs>wrong);ck(lhs<=F(7,16))
ck(2*(F(1,3)+F(1,81)+F(1,1215))>F(9,13));ck(10**15<2**8*7**15)
o={'status':'PASS','local_cases':len(rows),'martingale_cases':len(mart),'assertions':C,'seconds':time.perf_counter()-start,'local_rows':rows,'martingale_rows':mart,'adversarial_child_adaptation':{'correct_cost':str(lhs),'false_parent_variance_times_mean_increment':str(wrong),'original_variance':str(F(7,16))}};(R/'out/AUDIT.json').write_text(json.dumps(o,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in o.items() if k not in ['local_rows','martingale_rows']}))
