from fractions import Fraction as F
from collections import defaultdict, Counter
from functools import lru_cache
from pathlib import Path
import sys,json,time

ROOT=Path(__file__).resolve().parents[1]
MODE=sys.argv[1]; START=time.perf_counter(); ASSERTS=0
CAP=60 if MODE=='pilot' else 300
def check(v,context=''):
 global ASSERTS
 assert v,context
 ASSERTS+=1
 assert time.perf_counter()-START<CAP,'frozen deadline'
def equal(a,b,context=''):check(a==b,(context,a,b))
@lru_cache(None)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def combine(*terms):
 d=defaultdict(F)
 for c,e in terms:
  for p,v in e.items():d[p]+=c*v
 return {p:v for p,v in d.items() if v}
@lru_cache(None)
def logexpr(q):
 return combine((1,factors(q.numerator)),(-1,factors(q.denominator)))
@lru_cache(None)
def masslog(q):return combine((q,logexpr(q))) if q else {}
def entropy(ps):
 counts=Counter(ps)
 return combine(*[(-c,masslog(p)) for p,c in counts.items() if p])
@lru_cache(None)
def lnseries(q):
 z=(q-1)/(q+1);z2=z*z;power=z;s=F()
 for k in range(48):s+=2*power/(2*k+1);power*=z2
 return s,s+2*power/(97*(1-z2))
LN2=lnseries(F(2));SCALE=1<<160
@lru_cache(None)
def loginterval(p):
 q=F(p);k=0
 while q>=2:q/=2;k+=1
 a,b=lnseries(q);lo=k+a/LN2[1];hi=k+b/LN2[0]
 return F((lo*SCALE).numerator//(lo*SCALE).denominator,SCALE),F(-((-hi*SCALE).numerator//(-hi*SCALE).denominator),SCALE)
def interval(e):
 lo=hi=F()
 for p,c in e.items():
  a,b=loginterval(p)
  if c>=0:lo+=c*a;hi+=c*b
  else:lo+=c*b;hi+=c*a
 return lo,hi
def constant(x):return {2:F(x)} if x else {}
def shifted(e,x):return combine((1,e),(1,constant(x)))
def fwht(t):
 a=list(t);h=1
 while h<len(a):
  for block in range(0,len(a),2*h):
   for j in range(block,block+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return [F(x,len(t)) for x in a]
def insert(x,i,b):return (x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)
def total(a):return sum((a[s]**2*s.bit_count() for s in range(len(a))),F())
def vertex_influence(t,i):
 return F(sum(t[insert(x,i,0)]!=t[insert(x,i,1)] for x in range(len(t)//2)),len(t)//2)
def metrics(t,i,a=None):
 if a is None:a=fwht(t)
 n=len(t).bit_length()-1
 childt=[[t[insert(x,i,b)] for x in range(len(t)//2)] for b in (0,1)]
 ca=[fwht(c) for c in childt]
 for b in (0,1):equal(ca[b],[a[insert(x,i,0)]+(-1)**b*a[insert(x,i,1)] for x in range(len(t)//2)],'actual child Walsh')
 ps=[x*x for x in a];hh=entropy(ps)
 d=sum((ps[s] for s in range(len(a)) if s&(1<<i)),F())
 equal(d,vertex_influence(t,i),'physical influence')
 ii=total(a);childI=[total(c) for c in ca];childH=[entropy([x*x for x in c]) for c in ca]
 equal(ii,d+sum(childI,F())/2,'influence removal')
 rem=[ps[insert(x,i,0)]+ps[insert(x,i,1)] for x in range(len(t)//2)]
 B=combine((1,hh),(-1,entropy(rem)))
 D=combine((1,hh),(-F(1,2),childH[0]),(-F(1,2),childH[1]))
 return {'d':d,'B':B,'D':D,'H':hh,'I':ii,'childH':childH,'childI':childI,'childt':childt,'n':n}
def sigma(m,C):return shifted(combine((-F(1,2),m['childH'][0]),(-F(1,2),m['childH'][1])),C*sum(m['childI'],F())/2)

rows=[];roots=splits=0
if MODE in ('pilot','full'):
 for r in range(2 if MODE=='pilot' else 3):
  for mask in range(1<<(1<<r)):
   seed=[1 if mask&(1<<x) else -1 for x in range(1<<r)]
   for q in ((2,) if MODE=='pilot' else (2,3)):
    n=r+q;t=[seed[x&((1<<r)-1)] for x in range(1<<n)];t[0]*=-1
    a=fwht(t);roots+=1;equal(sum(x*x for x in a),1);check(all(a),'full support')
    for i in range(n):
     m=metrics(t,i,a);splits+=1
     if i>=r:
      clean=[seed[x&((1<<r)-1)] for x in range(1<<(n-1))]
      edited=clean.copy();edited[0]*=-1
      equal(m['childt'][0],edited);equal(m['childt'][1],clean);equal(m['d'],F(1,1<<(n-1)))
     for C in (F(0),F(8,3),F(6)):
      delta=shifted(m['H'],-C*m['I']);sig=sigma(m,C)
      equal(combine((1,delta),(1,sig)),shifted(m['D'],-C*m['d']),'signed-child identity')
else:
 equal(MODE,'witness')
 n=12;r=3;C=F(8,3);K=F(5,2)
 t=[-1 if (x&7)==0 and x!=0 else 1 for x in range(1<<n)]
 a=fwht(t);roots=1
 equal(Counter(a),Counter({F(1537,2048):1,F(-511,2048):7,F(1,2048):4088}),'coefficient classes')
 equal(sum(x*x for x in a),1);check(all(a));equal(total(a),F(771,1024))
 oldrow=newrow=None
 for i in range(n):
  m=metrics(t,i,a);splits+=1;old=i<3
  equal(m['d'],F(511,2048) if old else F(1,2048));check(m['d']<F(1,4))
  delta=shifted(m['H'],-C*m['I']);sig=sigma(m,C)
  equal(combine((1,delta),(1,sig)),shifted(m['D'],-C*m['d']))
  check(interval(delta)[0]>0,'violating root')
  sigiv=interval(sig);check(sigiv[0]>0 if old else sigiv[1]<0,'average child signs')
  cheap=interval(shifted(m['B'],-K*m['d']));check(cheap[0]>0 if old else cheap[1]<0,'erasure price threshold')
  childsign=[]
  for h,ii in zip(m['childH'],m['childI']):
   slack=shifted(combine((-1,h)),C*ii)
   if not slack:childsign.append(0)
   else:
    iv=interval(slack);check(iv[0]>0 if old else iv[1]<0,'individual child signs');childsign.append(1 if old else -1)
  equal(sorted(childsign),[0,1] if old else [-1,-1])
  deficit=interval(delta);Biv=interval(m['B']);qnum=m['B'] if old else combine((1,m['B']),(-1,sig))
  qiv=interval(qnum);equal(qnum,combine((1,m['B']),(-1,sig)) if not old else m['B'])
  # Verify the max formula using the exact, certified sign of sigma.
  J=combine((1,m['D']),(-1,m['B']))
  second=shifted(combine((1,delta),(-1,J)),C*m['d'])
  equal(second,combine((1,m['B']),(-1,sig)))
  row={'coordinate':i,'class':'old' if old else 'fresh','influence':str(m['d']),'root_deficit':[str(x) for x in deficit],'average_child_slack':[str(x) for x in sigiv],'child_slack_signs':childsign,'B_over_d':[str(x/m['d']) for x in Biv],'corrected_price':[str(x/m['d']) for x in qiv]}
  rows.append(row)
  if old:oldrow=qiv[1]/m['d']
  else:newrow=qiv[0]/m['d']
 check(newrow>oldrow,'corrected price excludes cheap fresh directions')
 check(oldrow<3,'retained old corrected price below three')
 check(newrow>400,'finite unpaid fresh debt exceeds 400 per queried influence')

out=ROOT/'out';out.mkdir(exist_ok=True)
result={'status':'PASS','mode':MODE,'roots':roots,'physical_coordinates':splits,'exact_assertions':ASSERTS,'seconds':time.perf_counter()-START,'log_terms':48,'outward_rounding_bits':160,'rows':rows}
(out/(MODE.upper()+'_REVIEW.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
