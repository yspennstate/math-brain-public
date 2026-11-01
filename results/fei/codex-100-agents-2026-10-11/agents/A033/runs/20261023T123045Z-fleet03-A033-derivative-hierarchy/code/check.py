from fractions import Fraction as F
from pathlib import Path
from itertools import product
from collections import defaultdict
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1];START=time.monotonic();checks=0;cases=0;yes=0;no=0
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
 if time.monotonic()-START>55:raise TimeoutError('frozen55s cap')
def fw(tt):
 w=list(tt);k=1
 while k<len(w):
  for s in range(0,len(w),2*k):
   for j in range(s,s+k):a,b=w[j],w[j+k];w[j],w[j+k]=a+b,a-b
  k*=2
 return tuple(F(x,len(w)) for x in w)
def direct(tt):return tuple(F(sum(x*(-1 if (s&t).bit_count()%2 else 1) for t,x in enumerate(tt)),len(tt)) for s in range(len(tt)))
def law(tt):return tuple(x*x for x in fw(tt))
def parts(xs):
 if not xs:yield ();return
 for p in parts(xs[1:]):
  yield ((xs[0],),)+p
  for j in range(len(p)):yield p[:j]+((xs[0],)+p[j],)+p[j+1:]
partitions=list(parts(tuple(range(4))));ck(len(partitions)==15)
tables=list(product((-1,1),repeat=4))
for tp,tm in product(tables,repeat=2):
 p=[law(tp),law(tm)];q=tuple((x+y)/2 for x,y in zip(*p))
 # Every pair is realized by one full three-bit Boolean physical selector.
 parent=tuple((tp,tm)[x&1][x>>1] for x in range(8));hat=fw(parent);ck(hat==direct(parent))
 pp=tuple(x*x for x in hat);ck(tuple(pp[2*t]+pp[2*t+1] for t in range(4))==q)
 for shift in range(8):ck(sum(hat[s]*hat[s^shift] for s in range(8))==(1 if shift==0 else 0))
 for partition in partitions:
  candidate=[[F(0)]*4 for _ in range(2)];predicted=True
  for w in partition:
   ap=sum(p[0][i] for i in w);am=sum(p[1][i] for i in w);r=(ap+am)/2
   if not r:continue
   if ap and am:
    obstruction=any((r-ap)*(am*p[0][i]-ap*p[1][i]) for i in w)
    predicted=predicted and not obstruction
    # Independent candidate uses normalized child profiles, not the cross-multiplied criterion.
    for i in w:candidate[0][i]=r*p[0][i]/ap;candidate[1][i]=r*p[1][i]/am
   else:
    occupied=0 if ap else 1;mass=ap or am
    for i in w:
     candidate[occupied][i]=r*p[occupied][i]/mass
     candidate[1-occupied][i]=2*q[i]-candidate[occupied][i]
   ck(all(sum(candidate[o][i] for i in w)==r for o in (0,1)))
  ck(all(sum(z)==1 and all(x>=0 for x in z) for z in candidate))
  compatible=all(candidate[0][i]+candidate[1][i]==2*q[i] for i in range(4))
  ck(compatible==predicted)
  if predicted:
   ck(all(not p[o][i] or candidate[o][i]>0 for o in (0,1) for i in range(4)));yes+=1
  else:no+=1
  cases+=1
ck(cases==3840)
def factors(n):
 d=2;out={}
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def logform(q):
 z=defaultdict(F)
 for p,v in factors(q.numerator).items():z[p]+=v
 for p,v in factors(q.denominator).items():z[p]-=v
 return {p:v for p,v in z.items() if v}
def add(*terms):
 z=defaultdict(F)
 for scale,form in terms:
  for p,v in form.items():z[p]+=scale*v
 return {p:v for p,v in z.items() if v}
def CE(p,q):
 z={}
 for x,y in zip(p,q):
  if x:ck(y>0);z=add((1,z),(-x,logform(y)))
 return z
def KL(p,q):return add((1,CE(p,q)),(-1,CE(p,p)))
tp=(-1,1,1,1);tm=(1,-1,1,-1);p=[law(tp),law(tm)];q=tuple((x+y)/2 for x,y in zip(*p))
ck(p==[(F(1,4),)*4,(0,1,0,0)])
R=[(F(1,4),F(1,2),F(1,8),F(1,8)),(0,F(3,4),F(1,8),F(1,8))]
ck(tuple((x+y)/2 for x,y in zip(*R))==q);ck(all(sum(z)==1 for z in R))
ck(all((sum(z[:2]),sum(z[2:]))==(F(3,4),F(1,4)) for z in R))
M=add((F(1,2),KL(p[0],R[0])),(F(1,2),KL(p[1],R[1])))
L=add((F(1,2),KL((F(1,2),F(1,2)),(F(3,4),F(1,4)))),(F(1,2),KL((1,0),(F(3,4),F(1,4)))))
ck(M=={2:F(9,8),3:F(-1,2)});ck(L=={2:F(3,2),3:F(-3,4)})
ck(add((1,M),(-1,L))=={2:F(-3,8),3:F(1,4)})
# Exact strict gap: M-L=1/8-(1/4)log2(4/3)>0 iff16<18.
ck(16<18)
# Rational convex subgradient/KKT certificate: remove the common1/ln2 factor.
gradient=tuple((-p[0][i]/(2*R[0][i]) if p[0][i] else 0)+(p[1][i]/(2*R[1][i]) if p[1][i] else 0) for i in range(4))
ck(gradient==(F(-1,2),F(5,12),-1,-1))
ck(R[0][0]==2*q[0] and gradient[0]-gradient[1]==F(-11,12))
ck(gradient[2]==gradient[3])
# The first block's only feasible direction has deltaRplus(empty)<=0; the other block is tangent-flat.
for numerator in range(9):
 x=F(numerator,32)
 ck(x<=F(1,4))
 ck((gradient[0]-gradient[1])*(x-F(1,4))>=0)
 ck(F(3,8)+F(11,4)*x-6*x*x>=F(3,8)+F(5,4)*x>0)
parent=tuple((tp,tm)[x&1][x>>1] for x in range(8));P=law(parent)
Hpar=CE(P,P);Hq=CE(q,q);Hchild=add((F(1,2),CE(p[0],p[0])),(F(1,2),CE(p[1],p[1])))
B=add((1,Hpar),(-1,Hq));J=add((1,Hq),(-1,Hchild))
increment=add((1,B),(F(1,2),CE(p[0],R[0])),(F(1,2),CE(p[1],R[1])),(-1,Hpar))
ck(increment==add((1,M),(-1,J)))
ck(increment=={2:F(-7,8),3:F(-1,2),5:F(5,8)})
ck(5**5<2**7*3**4)
I=sum(F(s.bit_count())*x for s,x in enumerate(P));edges=sum(parent[x]!=parent[x^(1<<j)] for x in range(8) for j in range(3));ck(I==F(edges,8))
out={'status':'PASS','helper':'A033-compatible-coarse-gap-v1','parent_tables':256,'partition_cases':cases,'coarse_attainable_cases':yes,'strict_fine_gap_cases':no,'exact_assertions':checks,'runtime_seconds':time.monotonic()-START,'witness':{'parent_truth_table':parent,'child_spectra':[[str(z) for z in y] for y in p],'inherited_marginal':[str(z) for z in q],'optimizer':[[str(z) for z in y] for y in R],'coarse_lower_invoice':'(3/4)log2(4/3)','exact_compatible_minimum':'1/8+(1/2)log2(4/3)','strict_gap':'1/8-(1/4)log2(4/3)>0','rational_sign_guard':'16<18','rational_KKT_gradient':[str(z) for z in gradient],'B_prime_log':{str(k):str(v) for k,v in B.items()},'JS_prime_log':{str(k):str(v) for k,v in J.items()},'full_signed_increment_prime_log':{str(k):str(v) for k,v in increment.items()},'full_signed_increment_includes_JS':True,'physical_influence':str(I)},'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out['witness']['net_sign_guard']='5^5 < 2^7*3^4; full net transaction NEGATIVE despite positive fine gap'
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='witness'}))
