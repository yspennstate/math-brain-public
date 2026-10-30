"""Own Walsh-subset reconstruction of A084, independent of its profile engine.
No peer executable is imported. The log enclosure primitive is A075's prior code.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,time,hashlib,shutil
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261022T234728Z-fleet03-A075-search-to-theorem-bridge'
shutil.copyfile(OLD/'code/arithmetic.py',ROOT/'code/review_log.py')
import review_log as ar
SOURCE=ROOT.parent.parent.parent.parent/'agents/A084/runs/20261023T035136Z-fleet03-A084-continuum-parameters'
def write(n,o):(ROOT/'out'/n).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
spec={'version':'A075-independent-A084-v1','domain':'all432 pair-profile instances in the3 source orbit representatives; all72 original one-core prefix cuts; all729 restrictions/1458 query rows of the six-bit core','symmetry':'literal supplied3 pair representatives only; original outer swaps verified in primary job','case_count':432,'arithmetic':'own direct Walsh-subset expansion, exact prime logs and192-bit rational sign bounds','memory_estimate_mb':150,'maximum_runtime_seconds':120,'source_report_sha256':hashlib.sha256((SOURCE/'REPORT.md').read_bytes()).hexdigest(),'peer_code_execution':False}
write('INDEPENDENT_REVIEW_SPEC.json',spec)
start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x;checks+=1
def add(a,b,c=F(1)):return ar.add(a,b,c)
def scale(a,c):return ar.scale(a,c)
def cmp(a,b):
 d=add(a,b,F(-1))
 if not d:return 0
 lo,hi=ar.enclose(d)
 ck(lo>0 or hi<0)
 return 1 if lo>0 else -1
def positive(x):return x if cmp(x,{})>0 else {}
def avg(a,b):return scale(add(a,b),F(1,2))
@lru_cache(None)
def factor(n):
 out={};k=2
 while k*k<=n:
  while n%k==0:out[k]=out.get(k,F(0))+1;n//=k
  k=3 if k==2 else k+2
 if n>1:out[n]=out.get(n,F(0))+1
 return out
def lq(x):return add(factor(x.numerator),factor(x.denominator),F(-1))
def hm(x):return scale(lq(x),-x) if x else {}
def truth(name):
 if name=='P':return (1,)
 k=name[0];m=int(name[1:]);return tuple(-1 if x in ({0} if k=='A' else {0,1,2}) else 1 for x in range(1<<m))
def name(t):
 if t==(1,):return 'P'
 return ('A' if t.count(-1)==1 else 'L')+str((len(t)-1).bit_length())
NAMES=['P']+['A'+str(m) for m in range(6)]+['L'+str(m) for m in range(2,7)]
def rows(n):
 if n in ['P','A0']:return []
 m=int(n[1:])
 if n[0]=='A':return [('A'+str(m-1),'P')]
 return [('A'+str(m-2),'A'+str(m-1))]+([('L'+str(m-1),'P')] if m>=3 else [])
def reduce(t):
 while len(t)>1:
  d=next((j for j in range((len(t)-1).bit_length()) if all(t[x]==t[x^(1<<j)] for x in range(len(t)))),None)
  if d is None:break
  t=tuple(t[x] for x in range(len(t)) if not(x>>d&1))
 ck(t in [truth(n) for n in NAMES]);return name(t)
G=truth('L6')
for ass in product([-1,0,1],repeat=6):
 raw=tuple(G[x] for x in range(64) if all(b<0 or x>>i&1==b for i,b in enumerate(ass)));typ=reduce(raw)
 for i in range((len(raw)-1).bit_length()):
  kids=tuple(reduce(tuple(raw[x] for x in range(len(raw)) if x>>i&1==b)) for b in range(2))
  ck(kids==(typ,typ) or kids in rows(typ))
H=tuple(-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64))
K=tuple(-H[x<<2] for x in range(16));WK=ar.fwht(K)
@lru_cache(None)
def core(n):
 t=truth(n);N=len(t);w=ar.fwht(t);ent={}
 for z in w:
  if z:ent=add(ent,scale(lq(F(abs(z),N)),-2*F(z*z,N*N)))
 I=sum(F(sum(t[x]!=t[x^(1<<j)] for x in range(N)),N) for j in range((N-1).bit_length()))
 ck(I==sum(F(z*z,N*N)*i.bit_count() for i,z in enumerate(w)))
 return F(t.count(-1),N),I,ent
def prod(xs):
 v=F(1)
 for x in xs:v*=x
 return v
@lru_cache(None)
def full(ns):
 cs=[core(n) for n in ns];ps=[c[0] for c in cs];mus=[1-2*p for p in ps];vs=[4*p*(1-p) for p in ps];entropy={};masses=[]
 for T in range(16):
  coef=sum(F(w,16)*prod(mus[j] for j in range(4) if (U^T)>>j&1) for U,w in enumerate(WK) if U&T==T)
  mass=coef*coef*prod(vs[j] for j in range(4) if T>>j&1);masses.append(mass)
  if mass:
   logs=scale(lq(abs(coef)),F(2))
   for j in range(4):
    if T>>j&1:logs=add(logs,lq(vs[j]))
   entropy=add(entropy,logs,-mass)
 ck(sum(masses)==1);I=F(0)
 for j,c in enumerate(cs):
  q=sum(prod(ps[k] if x>>k&1 else 1-ps[k] for k in range(4) if k!=j) for x in range(16) if not(x>>j&1) and K[x]!=K[x^(1<<j)])
  ck(sum(masses[T] for T in range(16) if T>>j&1)==q*vs[j]);I+=q*c[1]
  entropy=add(add(entropy,c[2],q),add(hm(vs[j]),hm(1-vs[j])),-q)
 return add({2:4*I},entropy,F(-1))
def unpack(d):return {int(k):F(v) for k,v in d.items()}
raw=json.loads((SOURCE/'out/JOINT_CASES.json').read_text(encoding='utf-8'));cuts=json.loads((SOURCE/'out/PREFIX_CUTS.json').read_text(encoding='utf-8'));count=0;prefixes=0
for case in raw:
 pair=case['pair_original'];Ss={};expected={}
 for row in case['states_certificate']:
  names=tuple(name(tuple(t)) for t in row['truths']);ns=['L6']*4
  for j,n in zip(pair,names):ns[j-2]=n
  s=full(tuple(ns));target=unpack(row['S'])
  if s!=target:
   clean={k:v for k,v in s.items() if v}
   write('REVIEW_FIRST_FAILURE.json',{'profile':ns,'own':{str(k):str(v) for k,v in s.items()},'source':row['S'],'difference':{str(k):str(v) for k,v in add(s,target,F(-1)).items()},'zero_coefficient_normalization_only':clean==target,'failed_first_run':'strict dictionary equality before removing explicit zero log coefficients'})
   s=clean
  ck(s==target);Ss[names]=s;expected[names]=unpack(row['R']);count+=1
 Rs={}
 for key in sorted(Ss,key=lambda k:sum(len(truth(n)) for n in k)):
  r=positive(scale(Ss[key],F(-1)))
  for side,n in enumerate(key):
   for kids in rows(n):
    args=[]
    for c in kids:
     arg=list(key);arg[side]=c;args.append(tuple(arg))
    v=avg(Rs[args[0]],Rs[args[1]])
    if cmp(v,r)>0:r=v
  Rs[key]=r;ck(r==expected[key])
 A=scale(Ss[('L6','L6')],F(-1));ck(Rs[('L6','L6')]==A)
 for side in [0,1]:
  def key(n):return (n,'L6') if side==0 else ('L6',n)
  single={}
  for n in sorted(NAMES,key=lambda n:len(truth(n))):
   r=positive(scale(Ss[key(n)],F(-1)))
   for a,b in rows(n):
    v=avg(single[a],single[b])
    if cmp(v,r)>0:r=v
   single[n]=r
  incoming={'L6':A}
  for n in sorted(NAMES,key=lambda n:len(truth(n)),reverse=True):
   for a,b in rows(n):
    reserve=add(incoming[n],avg(single[a],single[b]),F(-1))
    for c in [a,b]:
     val=add(single[c],reserve)
     if c not in incoming or cmp(val,incoming[c])<0:incoming[c]=val
  for n in NAMES:
   src=next(z for z in cuts if z['pair']==pair and z['first_core']==pair[side] and tuple(z['truth'])==truth(n))
   ck(incoming[n]==unpack(src['source_incoming_credit']));ck(cmp(incoming[n],Rs[key(n)])>=0);prefixes+=1
 ck(time.perf_counter()-start<120)
out={'verdict':'HOLDS_UNCHANGED_FINITE_AND_ALL_REAL_SUPPLIED_DEBIT_SCOPE','state_instances':count,'unique_spectra':full.cache_info().currsize,'actual_source_prefix_cuts':prefixes,'exact_checks':checks,'runtime_seconds':time.perf_counter()-start,'source':'A084-SAME-CREDIT-TWO-CORE-CONTINUATION@1','method':'own direct Walsh subset masses; exact prime-log equality for all S and hull R; bottom-up rather than recursive Bellman; source credit independently propagated','independent_reviewer':'A075','universal_fei':'OPEN'}
write('INDEPENDENT_REVIEW.json',out);print(json.dumps(out))
