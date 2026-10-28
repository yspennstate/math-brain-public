from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import time,json,hashlib
ROOT=Path(__file__).resolve().parents[1];START=time.monotonic();checks=0;cases=0;eligible=0
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
 return tuple(F(z,len(w)) for z in w)
def law(tt):return tuple(z*z for z in fw(tt))
def child(tt,j,o):
 return tuple(tt[(x&((1<<j)-1))|((x>>j)<<(j+1))|(o<<j)] for x in range(len(tt)//2))
controllers=((0,),(1,),(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1))
for n in (1,2,3):
 for tt in product((-1,1),repeat=1<<n):
  h=fw(tt)
  if h[1]:continue
  eligible+=1;m=h[0];H=len(h)//2
  p=[law(child(tt,0,o)) for o in (0,1)]
  bins=tuple(w for w in (tuple(t for t in range(1,H) if h[2*t]*h[2*t+1]>=0),tuple(t for t in range(1,H) if h[2*t]*h[2*t+1]<0)) if w)
  r=[(z[0],)+tuple(sum(z[t] for t in w) for w in bins) for z in p]
  V=sum(abs(x-y) for x,y in zip(*p))/2
  ck(sum(abs(x-y) for x,y in zip(*r))/2==V)
  ck(sum(abs(h[2*t]*h[2*t+1]) for t in range(1,H))*2==V)
  for a in controllers:
   b=tuple(1-z*z for z in a);A=fw(a);B=fw(b);beta=sum(z*z for z in B);E=sum(z**4 for z in B)
   for sig in (1,-1):
    q=[tuple((x+sig*m*y)**2 for x,y in zip(A,B))+tuple(y*y*z[l] for y in B for l in range(1,len(z))) for z in r]
    ck(all(sum(z)==1 for z in q));ck(q[0][:len(A)]==q[1][:len(A)])
    ck(sum(abs(x-y) for x,y in zip(*q))/2==beta*V)
    # Every nonempty component/midpoint has the same B_U^2 scale; this certifies exact JS cancellation.
    for U,y0 in enumerate(B):
     for l in range(1,len(r[0])):
      idx=len(A)+U*(len(r[0])-1)+l-1
      ck(q[0][idx]+q[1][idx]==y0*y0*(r[0][l]+r[1][l]))
    y=beta*V*V/4;x=E*V*V/8
    ck(y>=x)
    if E and x:ck(y/x==2*beta/E)
    cases+=1
ck((eligible,cases)==(78,468))
# Exact complete CE identity, represented as rational coefficients of log2 primes.
def factors(n):
 d=2;out={}
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def logform(q):
 out=defaultdict(F)
 for p,z in factors(q.numerator).items():out[p]+=z
 for p,z in factors(q.denominator).items():out[p]-=z
 return out
def add(*terms):
 out=defaultdict(F)
 for scale,form in terms:
  for p,z in form.items():out[p]+=scale*z
 return {p:z for p,z in out.items() if z}
def CE(p,q):
 out={}
 for x,y in zip(p,q):
  if x:ck(y>0);out=add((1,out),(-x,logform(y)))
 return out
a=controllers[-1];b=tuple(1-z*z for z in a);A=fw(a);B=fw(b);beta=F(3,8)
h=tuple(((-1 if (s&3)==0 else 1)*(-1 if s&4 else 1)) for s in range(8))
fixture=[]
for sig in (1,-1):
 tt=tuple(a[U]+sig*b[U]*h[s] for s in range(8) for U in range(16));P=law(tt)
 pc=[law(child(tt,4,o)) for o in (0,1)];seed=[law(child(h,0,o)) for o in (0,1)]
 pm=tuple(P[(z&15)|((z>>4)<<5)]+P[(z&15)|((z>>4)<<5)|16] for z in range(64))
 erasure=add((1,CE(P,P)),(-1,CE(pm,pm)))
 ck(erasure=={2:beta})
 changes=[]
 for o in (0,1):
  M=seed[o];S=seed[1-o];N=tuple(F(4,5)*x+F(1,5)*y for x,y in zip(M,S))
  q=tuple(A[U]**2 if T==0 else B[U]**2*N[T] for T in range(4) for U in range(16))
  ck(sum(q)==1 and pc[o][:16]==q[:16])
  delta=add((1,CE(pc[o],q)),(-1,CE(pc[o],pc[o])))
  ck(delta=={5:beta,2:-2*beta})
  changes.append(CE(pc[o],q));fixture.append({'sign':sig,'child':o,'new_reference_sha256':hashlib.sha256('|'.join(map(str,q)).encode()).hexdigest()})
 total=add((1,erasure),(F(1,2),changes[0]),(F(1,2),changes[1]),(-1,CE(P,P)))
 ck(total=={5:beta,2:-3*beta})
out={'status':'PASS','helper':'A033-independent-JS-v1','eligible_zero_singleton_seeds':eligible,'controller_sign_cases':cases,'exact_assertions':checks,'runtime_seconds':time.monotonic()-START,'full_fixture_terminals':fixture,'exact_full_increment':'(3/8) log2(5/8)<0','epsilon':'1/5','y':'3/32','old_x':'21/4096','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out/js_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='full_fixture_terminals'}))
