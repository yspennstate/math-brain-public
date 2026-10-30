import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import itertools,time,json
import exact as e
ROOT=Path(__file__).resolve().parents[1]
def L(x):return e.add({},e.cost(Q(1,2)),2*x)
def tables():return [(1,),(-1,),(1,-1),(-1,1)]
def prob(s):return Q(s) if s<=0 else Q(1,1<<s)
# -1 is passed (probability1); 0 is failed; positive means live width.
def pp(s):return Q(1) if s==-1 else prob(s)
def select(status):
 widths=[max(s,0) for s in status];n=sum(widths);out=[]
 for x in range(1<<n):
  off=0;label=0
  for j,(s,w) in enumerate(zip(status,widths),1):
   yes=(s==-1 or s>0 and not ((x>>off)&((1<<w)-1)))
   off+=w
   if yes:label=j;break
  out.append(label)
 return tuple(out)
@lru_cache(maxsize=256)
def state(c,cores):
 nc=len(c).bit_length()-1;ns=[len(t).bit_length()-1 for t in cores]
 full=[]
 for ys in itertools.product(*[range(len(t)) for t in reversed(cores)]):
  ys=tuple(reversed(ys))
  for label in c:full.append(1 if not label else cores[label-1][ys[label-1]])
 a=e.walsh(tuple(full));U={};R={};qs=[];vs=[];ms=[]
 for j,t in enumerate(cores,1):
  q=Q(c.count(j),len(c));m=Q(sum(t),len(t));v=1-m*m
  qs.append(q);vs.append(v);ms.append(m)
  U=e.add(U,e.add(e.entropy(e.walsh(t)),e.cost(m*m),-1),q)
  R=e.add(R,e.cost(q),v)
 return {'a':a,'H':e.entropy(a),'I':e.influence(a),'U':U,'R':R,'q':qs,'V':vs,'m':ms,'ns':[nc]+ns}
def erasure(a,i):
 out={}
 for s in range(len(a)):
  if not (s>>i)&1:out=e.add(out,e.phi(a[s]**2,a[s|(1<<i)]**2))
 return out
def params(status,means,start):
 weight=Q(1);n=Q(0);z=Q(0)
 for j in range(start,len(status)):
  p=pp(status[j]);n+=weight*p*means[j];z+=weight*p*(1-means[j]**2);weight*=1-p
 return n+weight,z
def prefix(status,means,j):
 widths=[max(s,0) for s in status[:j]];n=sum(widths);Et=[];Kt=[]
 for x in range(1<<n):
  offset=0;alive=True;k=Q(0)
  for h,w in enumerate(widths):
   yes=(status[h]==-1 or status[h]>0 and not((x>>offset)&((1<<w)-1)))
   offset+=w
   if alive and yes:k=means[h];alive=False
  Et.append(int(alive));Kt.append(k)
 return e.walsh(tuple(Et)),e.walsh(tuple(Kt)),widths
def node(status,cores,j):
 c=select(status);st=state(c,cores);offset=sum(max(s,0) for s in status[:j]);q=pp(status[j])
 children=[state(e.slice_table(c,offset,b),cores) for b in [0,1]]
 D=e.add(st['H'],e.add(children[0]['H'],children[1]['H']),-Q(1,2))
 k=e.add(st['R'],e.add(children[0]['R'],children[1]['R']),-Q(1,2))
 e.ok(e.add(st['U'],e.add(children[0]['U'],children[1]['U']),-Q(1,2))=={},'control U martingale')
 e.le({},k,'fine reserve reset nonnegative')
 inf=e.influence(st['a'],offset)
 e.ok(st['I']==inf+(children[0]['I']+children[1]['I'])/2,'same-tree influence')
 ep=Q(1)
 for s in status[:j]:ep*=1-pp(s)
 if not ep:
  e.ok(not D and not k and not inf,'earlier passed irrelevant query');return
 m=st['m'][j];n,Z=params(status,st['m'],j+1);delta=m-n;M=n+q*delta;V=1-n*n
 e.ok(inf==ep*q*(1-m*n),'actual mismatch influence')
 kq=e.add(e.cost(1-q),e.cost(1-2*q),-Q(1,2))
 expectedk=e.add(L(ep*q*(1-m*m)),kq,ep*Z)
 e.ok(k==expectedk,'exact fine release arbitrary earlier guard')
 ea,ka,widths=prefix(status,st['m'],j);S={};moment={};mass=Q(0)
 for T,(et,kt) in enumerate(zip(ea,ka)):
  S=e.add(S,e.phi((kt+M*et)**2,q*q*delta*delta*et*et))
  if not et:continue
  mass+=et*et/ep;last=-1;off=0
  for h,w in enumerate(widths):
   if ((T>>off)&((1<<w)-1)):last=h
   off+=w
  tail=Q(1)
  for h in range(last+1,j):tail*=1-pp(status[h])
  e.ok(abs(kt/et+M)<=3/tail,'row amplitude tail bound')
  moment=e.add(moment,e.cost(tail),(et*et/ep)/tail)
 e.ok(mass==1,'guard squared spectrum normalized')
 e.leconst(moment,1-ep,'last-frequency log moment')
 expected=e.add(L(ep*(q-2*q*q)*(V+delta*delta)),e.phi((1-q)**2,q*q),ep*V)
 expected=e.add(expected,kq,-ep*Z);expected=e.add(expected,S)
 B=erasure(st['a'],offset)
 e.ok(e.add(B,k,-1)==expected,'full guarded reused-fallback erasure')
 # Rational17 exceeds analytic K_ctrl; check direct residual and erasure.
 e.le(e.add(D,k,-1),L(17*inf),'all-order controller payment17')
 e.le(e.add(B,k,-1),L(14*inf),'erasure payment14')
 e.leconst(e.add(D,B,-1),2*inf,'full physical JS bound')

def main(pilot):
 start=time.perf_counter();roots=nodes=0
 for widths in ([(1,1,1)] if pilot else [(1,1,1),(1,2,1),(2,1,2)]):
  statuses=list(itertools.product(*[[-1,0]+list(range(1,w+1)) for w in widths]))
  coretriples=list(itertools.product(tables(),repeat=3))
  if pilot:statuses=statuses[-3:];coretriples=coretriples[:8]
  for status in statuses:
   for cores in coretriples:
    for j,s in enumerate(status):
     if s>0:node(status,cores,j);nodes+=1
    roots+=1
    if roots%32==0:state.cache_clear();e.walsh.cache_clear()
    if time.perf_counter()-start>230:raise RuntimeError('frozen runtime exhausted')
 # Exact rational exponent certificate used for Kctrl<17.
 exp=sum(Q(7,3)**k/Q(__import__('math').factorial(k)) for k in range(9))
 e.ok(exp>10,'ln10<7/3 rational Taylor certificate')
 out={'status':'PASS','roots':roots,'query_types':nodes,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-start,'pilot':pilot,'symmetry':'within each live point-test block query its first remaining bit; permutation symmetry'}
 (ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main('--pilot' in sys.argv)
