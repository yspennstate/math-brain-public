from pathlib import Path
from fractions import Fraction as F
from itertools import product,permutations
from collections import defaultdict
import json,sys,time
R=Path(__file__).resolve().parents[1]; start=time.monotonic(); count=0
def ck(b):
 global count
 count+=1
 assert b,count
 assert time.monotonic()-start<55,'frozen runtime cap'
EDGES=(3,5,6)
def actual_anchor(alpha):
 rho=sum(alpha); q=defaultdict(F); keys=set()
 for j,e in enumerate(EDGES):
  if not alpha[j]:continue
  options=[]
  for k,edge in enumerate(EDGES):
   masks=[s for s in range(8) if s and s&edge==s]
   options.append([(s,F(1,3)) for s in masks] if k==j else [(0,1-alpha[k])]+[(s,alpha[k]/3) for s in masks])
  for draws in product(*options):
   mass=alpha[j]/rho; output=0; tup=[]
   for s,p in draws:mass*=p;output|=s;tup.append(s)
   if mass:
    key=(j,tuple(tup));ck(key not in keys);keys.add(key);q[output]+=mass
 ck(sum(q.values())==1)
 return q,len(keys)
def forest(alpha):
 D=F(1)
 for x in alpha:D*=1+x/4
 D-=1; q=defaultdict(F); events=[]
 for i in range(3):
  for e in range(3):
   if EDGES[e]&(1<<i):events.append(((e,1<<i,()),1<<i,alpha[e]/4*F(1,4)*F(1,2)))
 for e in range(3):events.append(((e,EDGES[e],()),EDGES[e],alpha[e]/4*F(1,6)*F(1,2)))
 for e in range(3):
  for child in range(3):
   if e==child:continue
   shared=EDGES[e]&EDGES[child]; remaining=EDGES[child]&~EDGES[e]
   events.append(((e,EDGES[e],((shared,child,remaining),)),7,alpha[e]/4*F(1,6)*F(1,6)*F(1,2)*alpha[child]*F(1,4)*F(1,2)))
 ck(len(events)==15);ck(len({key for key,_,_ in events})==15)
 for _,a,num in events:q[a]+=num/D
 s1=sum(alpha);s2=sum(alpha[i]*alpha[j] for i in range(3) for j in range(i));s3=alpha[0]*alpha[1]*alpha[2]
 for i in range(3):ck(q[1<<i]==sum(alpha[e] for e in range(3) if EDGES[e]&(1<<i))/32/D)
 ck(q[7]==s2/1152/D);ck(sum(q.values())<=1)
 ck(117*s1-242*s2+48*s3>=0)
 return q,D
def add(*ps):
 out=defaultdict(F)
 for p in ps:
  for a,v in p.items():out[a]+=v
 return {a:v for a,v in out.items() if v}
def mul(p,q):
 out=defaultdict(F)
 for a,x in p.items():
  for b,y in q.items():out[tuple(i+j for i,j in zip(a,b))]+=x*y
 return dict(out)
def scale(p,c):return {a:v*c for a,v in p.items() if v*c}
X=[{tuple(int(i==j) for i in range(4)):F(1)} for j in range(4)]
a,b,c,t=X; L=[add(v,scale(t,F(1,2))) for v in X[:3]]; S=add(*X)
s1=add(*L);s2=add(*(mul(L[i],L[j]) for i in range(3) for j in range(i)));s3=mul(mul(L[0],L[1]),L[2])
hom=add(scale(mul(s1,mul(S,S)),117),scale(mul(s2,S),-242),scale(s3,48))
expected={}
for exp,coef in hom.items():
 deg=exp[3]; abcexp=exp[:3]
 if deg==0: target=117 if 3 in abcexp else (24 if abcexp==(1,1,1) else 109)
 elif deg==1:target=F(335,2) if 2 in abcexp else 117
 elif deg==2:target=F(113,2)
 else:target=0
 ck(coef==target);expected[exp]=target
ck(len(hom)==19);ck((0,0,0,3) not in hom)
values=[2*int(all(x&e for e in EDGES))-1 for x in range(8)]
p={s:F(sum(values[x]*(-1)**((s&x).bit_count()) for x in range(8))**2,64) for s in range(8)}
ck(p=={0:F(0),1:F(1,4),2:F(1,4),3:F(0),4:F(1,4),5:F(0),6:F(0),7:F(1,4)})
ck(sum(s.bit_count()*v for s,v in p.items())==F(3,2))
ck(F(sum(values[x]!=values[x^(1<<i)] for x in range(8) for i in range(3)),8)==F(3,2))
half=(F(1,2),)*3;qh,runs=actual_anchor(half);ck(runs==144)
mixed=defaultdict(F)
for s,q in qh.items():mixed[s]+=F(3,8)*q
for i in range(3):
 q,_=actual_anchor(tuple(F(int(i==j)) for j in range(3)))
 for s,v in q.items():mixed[s]+=F(5,24)*v
ck(mixed=={1:F(1,6),2:F(1,6),4:F(1,6),3:F(1,8),5:F(1,8),6:F(1,8),7:F(1,8)})
cols=[]
for alpha in [(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)),half]:
 q,_=actual_anchor(alpha);cols.append([q.get(s,F()) for s in (1,2,4,7)])
det=F()
for perm in permutations(range(4)):
 term=F((-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4)))
 for i in range(4):term*=cols[perm[i]][i]
 det+=term
ck(det==F(-2,81))
pilot='--pilot' in sys.argv;d=3 if pilot else 12;profiles=0;equality=0
for aa,bb,cc in product(range(d+1),repeat=3):
 if aa+bb>d or aa+cc>d or bb+cc>d or not aa+bb+cc:continue
 alpha=tuple(F(x,d) for x in (aa,bb,cc));q,_=actual_anchor(alpha)
 u=sum(alpha);v=sum(alpha[i]*alpha[j] for i in range(3) for j in range(i));w=alpha[0]*alpha[1]*alpha[2]
 single=sum(q.get(i,F()) for i in (1,2,4));triple=q.get(7,F())
 ck(single==F(2,3)-10*v/(9*u)+4*w/(3*u));ck(triple==2*v/(3*u))
 score=sum(p[s]*q.get(s,F())/mixed[s] for s in mixed)
 ck(score==1-(v-6*w)/(3*u));ck(score<=1)
 ck(v<=u*u/3);ck(2*u<=3);ck(v*v>=3*u*w)
 if score==1:
  equality+=1;ck(v==0 or alpha==half)
 fq,D=forest(alpha);fs=sum(p[s]*fq[s]/(F(16,217) if s in (1,2,4) else F(1,651)) for s in (1,2,4,7))
 ck(fs<=1)
 profiles+=1
for i,j,k,l in product(range(7),repeat=4):
 if i+j+k+l!=6:continue
 bary=tuple(F(x,6) for x in (i,j,k,l))
 for upper in [False,True]:
  alpha=tuple(bary[x]+bary[3]/2 for x in range(3)) if upper else bary[:3]
  if sum(alpha):forest(alpha)
fq,D=forest(half);ck(D==F(217,512));ck(fq[1]==F(16,217));ck(fq[7]==F(1,651))
ck(F(217,96)-1==F(121,96));ck(117*3-242*3+48==-327)
ck(2*F(1,8)*F(217,64)==F(217,256));ck(2*F(1,144)*F(651,4)==F(217,96))
ck(F(1,8)/32768>0) # positive omitted triple event at half weights
def ln_bounds(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 def base(y):
  z=(y-1)/(y+1);lo=sum((2*z**(2*j+1)/F(2*j+1) for j in range(30)),F())
  return lo,lo+2*z**61/(61*(1-z*z))
 lo,hi=base(x);a,b=base(F(2));return lo+k*a,hi+k*b
lo3,hi3=ln_bounds(3);lo2,hi2=ln_bounds(2)
costlo=F(3,2)+F(3,4)*lo3/hi2;costhi=F(3,2)+F(3,4)*hi3/lo2
ck(costlo>2);ck(costhi<3)
out={'status':'PASS','assertions':count,'profiles':profiles,'equality_profiles':equality,'runtime_seconds':time.monotonic()-start,'pilot':pilot,'mixed_law':{str(k):str(v) for k,v in mixed.items()},'cost_interval':[str(costlo),str(costhi)],'upper_simplex_coefficients':{str(k):str(v) for k,v in hom.items()},'full_fei':'OPEN'}
(R/'out').mkdir(exist_ok=True)
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k in ['status','assertions','profiles','equality_profiles','runtime_seconds','pilot','full_fei']}))
