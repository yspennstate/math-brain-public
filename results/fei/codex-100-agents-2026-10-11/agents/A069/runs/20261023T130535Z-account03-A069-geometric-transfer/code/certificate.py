from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json, time, sys, hashlib

RUN=Path(__file__).resolve().parents[1]
BASE=RUN.parents[1]
OLD=BASE/'runs/20261023T105842Z-account03-A069-geometric-transfer'
# Preserve the exact, previously checked helper in this run before importing it.
helper=(OLD/'code/rational.py').read_bytes()
(RUN/'code/rational.py').write_bytes(helper)
from rational import fw, log, add, interval

start=time.perf_counter();checks=0
def check(v):
 global checks
 checks+=1
 assert v,checks
def expr(x):return {str(p):str(v) for p,v in x.items()}
def sub(a,b):return add((1,a),(-1,b))
def const(q):return log(F(2)**q) if F(q).denominator==1 else {2:F(q)}
def positive(e):
 if not e:return {}
 lo,hi=interval(e)
 check(lo>0 or hi<0)
 return e if lo>0 else {}
def nn(e):
 if e:check(interval(e)[0]>=0)
 else:check(True)
def insert(t,i,bit):return (t&((1<<i)-1))|((t>>i)<<(i+1))|(bit<<i)
def restrict(a,i,bit):return tuple(a[insert(t,i,bit)] for t in range(len(a)//2))
def erase(r,i):return tuple(r[insert(t,i,0)]+r[insert(t,i,1)] for t in range(len(r)//2))
@lru_cache(None)
def spectrum(a):return tuple(F(x*x,len(a)**2) for x in fw(a))
@lru_cache(None)
def state(a,b,r):
 p=tuple((x+y)/2 for x,y in zip(spectrum(a),spectrum(b)))
 ce=add(*[(-x,log(q)) for x,q in zip(p,r) if x])
 influence=sum((x*t.bit_count() for t,x in enumerate(p)),F(0))
 return p,ce,influence
@lru_cache(None)
def trees(n):
 if not n:return (None,)
 return tuple((i,l,r) for i in range(n) for l in trees(n-1) for r in trees(n-1))
@lru_cache(None)
def node(a,b,r,i):
 p,ce,j=state(a,b,r)
 rr=erase(r,i)
 children=tuple((restrict(a,i,e),restrict(b,i,e),rr) for e in (0,1))
 childce=add(*[(F(1,2),state(*v)[1]) for v in children])
 d=sub(ce,childce)
 ji=sum((x for t,x in enumerate(p) if t>>i&1),F(0))
 likelihood=add(*[(x,log(rr[(t&((1<<i)-1))|((t>>(i+1))<<i)]/r[t])) for t,x in enumerate(p) if x])
 check(d==likelihood);nn(d)
 check(j==ji+sum((state(*v)[2] for v in children),F(0))/2)
 debit=positive(sub(d,const(4*ji)))
 paid=sub(d,debit);nn(paid);nn(sub(const(4*ji),paid))
 return children,d,ji,debit,paid
def account(a,b,r,t):
 if t is None:
  check(len(a)==1 and len(r)==1 and r[0]==1)
  check(state(a,b,r)[1]=={} and state(a,b,r)[2]==0)
  return {},F(0),{},{}
 i,tl,tr=t
 children,d,j,v,paid=node(a,b,r,i)
 cl=account(*children[0],tl);cr=account(*children[1],tr)
 return (add((1,d),(F(1,2),cl[0]),(F(1,2),cr[0])),
         j+(cl[1]+cr[1])/2,
         add((1,v),(F(1,2),cl[2]),(F(1,2),cr[2])),
         add((1,paid),(F(1,2),cl[3]),(F(1,2),cr[3])))
def verify(a,b,r):
 p,ce,j=state(a,b,r);results=[]
 for t in trees((len(a)-1).bit_length()):
  ds,js,v,paid=account(a,b,r,t)
  check(ds==ce);check(js==j);check(add((1,v),(1,paid))==ce)
  nn(v);nn(paid);nn(sub(const(4*j),paid));nn(sub(ce,v))
  results.append(v)
 for v,w in product(results,repeat=2):nn(sub(const(4*j),sub(v,w)))
 return results

pilot='--pilot' in sys.argv
all2=[tuple(1 if mask>>x&1 else -1 for x in range(4)) for mask in range(16)]
r2=tuple(F(v,16) for v in (1,2,4,9))
cases=list(product(all2,repeat=2))
if pilot:cases=cases[:4]
count=0
for a,b in cases:
 verify(a,b,r2);count+=2
 if not pilot:
  source=tuple((x+y)/2 for x,y in zip(spectrum(a),spectrum(b)))
  verify(a,b,source);count+=2
if not pilot:
 vals=[tuple(1 for x in range(8)),tuple(-1 if x==0 else 1 for x in range(8)),
       tuple((-1)**(x&1) for x in range(8)),tuple((-1)**((x>>1)&1) for x in range(8)),
       tuple(1 if x.bit_count()>=2 else -1 for x in range(8)),
       tuple((-1)**x.bit_count() for x in range(8))]
 r3=tuple(F(v,256) for v in (1,2,4,8,16,32,64,129))
 for a,b in product(vals,repeat=2):verify(a,b,r3);count+=12

sharp=[]
for k in ([2] if pilot else [1,2,3,4,8,16,32]):
 e=F(1,2**k);rr=(e/16,F(1,16),(15-2*e)/16,e/16)
 a=(1,-1,1,-1);check(sum(rr)==1 and min(rr)>0)
 out=verify(a,a,rr);ell=log(1+e)
 check(out[0]==sub(const(4),ell));check(out[1]==ell)
 if k>=2:nn(sub(const(F(1,2)),ell));nn(sub(out[0],const(F(7,2))))
 sharp.append({'k':k,'R':[str(v) for v in rr],'B':'4','J':'1',
               'invoice_x_then_z':expr(out[0]),'invoice_z_then_x':expr(out[1]),
               'ell_interval':[str(v) for v in interval(ell)]})
# Independently reconstruct A070's normalized-real guard; not a Boolean FEI witness.
ar=(F(7,5),F(-1,5));br=(F(1),F(1))
check((ar[0]**2+1)/2==F(37,25));check((ar[1]**2+1)/2==F(13,25))
check(((ar[0]-ar[1])/2)**2/2==F(8,25));check(F(ar[0]!=ar[1],2)==F(1,2))
result={'status':'PASS','pilot':pilot,'checks':checks,'full_core_trees':count,
 'sharpness_profiles':sharp,'arithmetic':'exact Fraction Walsh, prime-log expressions and rational 24-term atanh intervals',
 'helper_sha256':hashlib.sha256(helper).hexdigest(),'elapsed_seconds':time.perf_counter()-start,
 'scope':'finite validation only; all-dimensional and sharp-limit proofs in DERIVATION.md',
 'A070_real_guard':{'child_norms':['37/25','13/25'],'core_energy':'8/25','pivotal_probability':'1/2'}}
(RUN/'out').mkdir(exist_ok=True)
target=RUN/'out'/('PILOT.json' if pilot else 'CERTIFICATE.json')
target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='sharpness_profiles'}))
