"""A074: direct truth-table Fourier and FORWARD min-plus admission audit."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util,itertools,json,sys,time,hashlib
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
helper=R.parent/'20261021T152214Z-fleet03-A074-independent-reproducer/code/reproduce.py'
sp=importlib.util.spec_from_file_location('a074_logs',helper);c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
START=time.perf_counter();COUNT=0
def ck(v):
 global COUNT
 COUNT+=1
 if not v:raise AssertionError(COUNT)
def dump(name,z):(R/'out'/name).write_text(json.dumps(z,indent=2,default=str)+'\n',encoding='utf-8')
def clean(p):return {k:v for k,v in p.items() if v}
def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,F(0))+v
 return clean(d)
def mul(p,v):return clean({k:x*v for k,x in p.items()})
def sub(p,q):return add(p,mul(q,-1))
def const(v):return {None:F(v)} if v else {}
def mean(p,q):return mul(add(p,q),F(1,2))
def pack(p):return {('constant' if k is None else str(k)):str(v) for k,v in p.items()}
@lru_cache(None)
def factors(x):
 out=[];q=2
 while q*q<=x:
  e=0
  while x%q==0:e+=1;x//=q
  if e:out.append((q,e))
  q=3 if q==2 else q+2
 if x>1:out.append((x,1))
 return out
def logint(x):
 ck(x>0)
 return {None if p==2 else p:F(e) for p,e in factors(x)}
def entropy_integer_walsh(W):
 N=len(W);n=N.bit_length()-1
 p=const(2*n)
 for w in W:
  if w:p=sub(p,mul(logint(abs(w)),F(2*w*w,N*N)))
 return p
@lru_cache(None)
def ev_key(key):return c.add(*(c.scale(c.point(1) if k is None else c.log2(F(k)),v) for k,v in key))
def ev(p):return ev_key(tuple(sorted(p.items(),key=lambda z:0 if z[0] is None else z[0])))
def compare(p,q):
 d=sub(p,q)
 if not d:return 0
 lo,hi=ev(d)
 if lo>0:return 1
 if hi<0:return -1
 raise ArithmeticError('unresolved sign '+str(pack(d)))
def maximum(ps):
 best=ps[0]
 for p in ps[1:]:
  if compare(p,best)>0:best=p
 return best
@lru_cache(None)
def spectrum(t):
 N=len(t);n=N.bit_length()-1
 W=[sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(t)) for s in range(N)]
 ck(sum(w*w for w in W)==N*N)
 for x,y in enumerate(t):ck(sum(w*(-1 if (x&s).bit_count()%2 else 1) for s,w in enumerate(W))==N*y)
 ds=[]
 for i in range(n):
  d=F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N)
  ck(d==sum(F(w*w,N*N) for s,w in enumerate(W) if s>>i&1));ds.append(d)
 H=entropy_integer_walsh(W)
 return H,sum(ds),ds,W
def truth_restrict(t,tag):
 free=[i for i,b in enumerate(tag) if b==-1];fixed=sum((b==1)<<i for i,b in enumerate(tag))
 return tuple(t[fixed|sum(((x>>k)&1)<<i for k,i in enumerate(free))] for x in range(1<<len(free)))
def family(d):
 n=d+3;P=((1<<3)-1)<<d
 return tuple((-1 if (x&P).bit_count()%2 else 1)*(-1 if x==0 else 1) for x in range(1<<n))
def account(t,K,timeout):
 n=len(t).bit_length()-1;root=(-1,)*n;terminal_checks=0;edges=0
 @lru_cache(None)
 def state(tag):
  tt=truth_restrict(t,tag);H,I,ds,W=spectrum(tt);S=sub(const(K*I),H)
  return dict(S=S,b=maximum([{},mul(S,-1)]),I=I,H=H,ds=ds)
 @lru_cache(None)
 def hull(tag,mask):
  p=state(tag);cs=[p['b']]
  for i in range(n):
   if mask>>i&1:
    ck(tag[i]==-1)
    kids=[tag[:i]+(b,)+tag[i+1:] for b in (0,1)];m=mask^(1<<i)
    cs.append(mean(hull(kids[0],m),hull(kids[1],m)))
  return maximum(cs)
 # Rank increases by exactly one on each admission or physical query.
 # A node stores the least accumulated credit increment among ALL arrivals.
 buckets=[{} for _ in range(2*n+1)];buckets[0][root,0]={}
 parents={};values={};capital={};badnode=(root,0)
 for rank,bucket in enumerate(buckets):
  for (tag,mask),offset in bucket.items():
   values[tag,mask]=offset;p=state(tag);candidate=sub(p['b'],offset)
   if compare(candidate,capital)>0:capital=candidate;badnode=(tag,mask)
   terminal_checks+=1
   def offer(target,inc,kind):
    nonlocal edges
    edges+=1;nextoff=add(offset,inc);nextrank=2*sum(b!=-1 for b in target[0])+target[1].bit_count()
    ck(nextrank==rank+1)
    old=buckets[nextrank].get(target)
    if old is None or compare(nextoff,old)<0:
     buckets[nextrank][target]=nextoff;parents[target]=((tag,mask),inc,kind)
   for i,b in enumerate(tag):
    if b!=-1:continue
    if not mask>>i&1:offer((tag,mask|(1<<i)),{},['admit',i]);continue
    kids=[tag[:i]+(v,)+tag[i+1:] for v in (0,1)];m=mask^(1<<i)
    childrho=[hull(k,m) for k in kids];av=mean(*childrho)
    index=[j for j,v in enumerate(tag) if v==-1].index(i)
    ck(p['I']-sum(state(k)['I'] for k in kids)/2==p['ds'][index])
    for v,k in enumerate(kids):offer((k,m),sub(childrho[v],av),['query',i,v])
  ck(time.perf_counter()-START<timeout)
 ck(len(values)==4**n)
 full=hull(root,(1<<n)-1);ck(compare(capital,full)>=0)
 path=[];node=badnode
 while node!=(root,0):
  prev,inc,kind=parents[node];path.append(dict(action=kind,increment=pack(inc),arrival_tag=node[0],arrival_mask=node[1]));node=prev
 path.reverse();total={}
 for z in path:
  total=add(total,{None if k=='constant' else int(k):F(v) for k,v in z['increment'].items()})
 ck(not sub(capital,sub(state(badnode[0])['b'],total)))
 return dict(n=n,K=K,global_hull=pack(full),robust_capital=pack(capital),global_interval=ev(full),capital_interval=ev(capital),augmented_states=len(values),physical_states=state.cache_info().currsize,edges=edges,extremal_path=path,extremal_need=pack(state(badnode[0])['b']))
def hm(m):
 if m==0:return {}
 N=1<<m
 # Direct integer multiplicities, without building a size-N spectrum.
 return sub(sub(const(2*m),mul(logint(N-2),F(2*(N-2)**2,N*N))) if N>2 else const(2*m),const(F(8*(N-1),N*N)))
def formula(d):
 ps=[]
 for r in range(4):
  for s in range(d+1):
   m=r+s;I=F(r)+F(2*(m-2*r),1<<m) if m else F(0)
   ps.append(mul(maximum([{},sub(hm(m),const(I))]),F(1,1<<(d+3-m))))
 return maximum(ps)
def main():
 mode=sys.argv[1] if len(sys.argv)>1 else '--constructed';name=mode.removeprefix('--').upper();journal=R/'out'/(name+'_CASES.jsonl')
 if journal.exists():raise RuntimeError('existing journal; reconcile before rerun')
 results=[]
 if mode in ('--pilot','--census'):
  n=2 if mode=='--pilot' else 3;cap=55 if mode=='--pilot' else 180
  cases=((tuple(-1 if bits>>x&1 else 1 for x in range(1<<n)),K,bits) for bits in range(1<<(1<<n)) for K in (0,1,4))
  for t,K,bits in cases:
   z=account(t,F(K),cap);ck(z['global_hull']==z['robust_capital']);z['truth_mask']=bits
   with journal.open('a',encoding='utf-8') as f:f.write(json.dumps(z,default=str)+'\n')
   results.append(z)
 elif mode=='--constructed':
  for d in (0,1,2,3):
   t=family(d);z=account(t,F(1),180);z['d']=d
   H,I,ds,W=spectrum(t);n=d+3;P=7<<d;N=1<<n
   ck(W==[N*(s==P)-2 for s in range(N)])
   ck(I==3+F(2*(d-3),N));ck(not sub(H,hm(n)))
   ck(z['global_hull']==pack(formula(d)))
   capz={None if k=='constant' else int(k):F(v) for k,v in z['robust_capital'].items()}
   ck(compare(capz,const(F(1,2)))>=0)
   if d==1:ck(z['global_hull']==pack(const(F(1,4))));ck(z['robust_capital']==pack(const(F(1,2))))
   dump('CONSTRUCTED_d'+str(d)+'.json',z)
   with journal.open('a',encoding='utf-8') as f:f.write(json.dumps(z,default=str)+'\n')
   results.append(z)
 elif mode=='--formula':
  for d in range(17):
   R0=formula(d);ri=ev(R0);bound=F(8*(d+4),1<<(d+3))
   ck(ri[0]>0 and ri[1]<=bound)
   for s in range(d+1):
    m=s+3;I=3+F(2*(s-3),1<<m);ck(compare(const(I),hm(m))>0)
   z=dict(d=d,R=pack(R0),R_interval=ri,upper_bound=bound,T_lower=F(1,2),ratio_lower=F(1<<(d+3),16*(d+4)))
   with journal.open('a',encoding='utf-8') as f:f.write(json.dumps(z,default=str)+'\n')
   results.append(z);ck(time.perf_counter()-START<55)
 else:raise ValueError(mode)
 result=dict(passed=True,mode=mode,cases=len(results),checks=COUNT,log_primitive_checks=c.COUNT-64,runtime_seconds=time.perf_counter()-START,peer_executable_imports=False,forward_minimum_offset=True,canonical_prime_log_equalities=True,log_bits=112,spectrum_tables=spectrum.cache_info().currsize,full_FEI='OPEN')
 dump(name+'_VALIDATION.json',result);print(json.dumps(result))
if __name__=='__main__':main()
