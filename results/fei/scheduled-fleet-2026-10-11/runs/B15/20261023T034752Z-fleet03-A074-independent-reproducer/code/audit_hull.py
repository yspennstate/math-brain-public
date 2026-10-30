"""A074 raw labelled stopping DAG; no peer executable imports."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util, json, sys, time, itertools, hashlib
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
helper=R.parent/'20261021T152214Z-fleet03-A074-independent-reproducer/code/reproduce.py'
spec=importlib.util.spec_from_file_location('a074_binary',helper)
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);c.K=F(4)
START=time.perf_counter();COUNT=0
def ck(b):
 global COUNT
 COUNT+=1
 if not b:raise AssertionError(COUNT)
def save(name,z):(R/'out'/name).write_text(json.dumps(z,indent=2,default=str)+'\n',encoding='utf-8')
def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,F(0))+v
 return {k:v for k,v in d.items() if v}
def mul(p,x):return {k:v*x for k,v in p.items() if v*x}
def sub(p,q):return add(p,mul(q,-1))
def mean(ps):return mul(add(*ps),F(1,len(ps)))
def const(x):return {None:F(x)} if x else {}
def ent(ps):
 d={}
 for p in ps:
  if p and p!=1:d[p]=d.get(p,F(0))-p
 return d
def ev(p):return c.add(*(c.scale(c.point(1) if k is None else c.log2(k),v) for k,v in p.items()))
def pack(p):return {('constant' if k is None else str(k)):str(v) for k,v in p.items()}
def nonnegative(p):ck(not p or ev(p)[0]>=0)
def overlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
@lru_cache(None)
def physical(t,j):
 ts=[(-1,),(1,),c.G,c.G,c.G,c.G];ts[j]=t
 P=c.packet(tuple(ts));hp=ent(P['masses'])
 for core,q in zip(P['cs'],P['q']):
  if core['v']:
   hp=add(hp,mul(ent([F(w*w,len(core['t'])**2)/core['v'] for w in core['W'][1:] if w]),q*core['v']))
 S=sub(const(4*P['I']),hp)
 overlap(ev(hp),P['H']);overlap(ev(S),P['S'])
 return P,S
def raw(tag):
 free=[i for i,b in enumerate(tag) if b==-1]
 fixed=sum((b==1)<<i for i,b in enumerate(tag))
 return tuple(c.G[fixed|sum(((x>>k)&1)<<i for k,i in enumerate(free))] for x in range(1<<len(free)))
def choose(candidates):
 winner=candidates[0]
 for z in candidates[1:]:
  d=sub(z[1],winner[1])
  if not d:continue
  iv=ev(d)
  if iv[0]>0:winner=z
  elif iv[1]<0:pass
  else:raise ArithmeticError('unresolved exact Bellman comparison '+str(pack(d)))
 return winner
def main():
 pilot='--pilot' in sys.argv
 outfile='PILOT_CASES.jsonl' if pilot else 'CASES.jsonl'
 journal=R/'out'/outfile
 if journal.exists():raise RuntimeError('refusing journal overwrite')
 peers=Path(r'~\brain_workers\FEI100_20261011\agents\A072\runs\20261023T015130Z-fleet03-A072-exact-walsh-engine')
 source=None;comparisons=0;rows=0;records=[];gaps=0
 # No quotient: all four original core labels, all 729 labelled restrictions.
 for j in ([2] if pilot else [2,3,4,5]):
  @lru_cache(None)
  def solve(tag):
   nonlocal rows,gaps
   t=raw(tag);P,S=physical(t,j);si=ev(S)
   ck(si[0]>0 or si[1]<0 or not S)
   stop=mul(S,-1) if si[1]<0 else {}
   actions=[]
   for i,b in enumerate(tag):
    if b!=-1:continue
    kids=[tag[:i]+(v,)+tag[i+1:] for v in (0,1)]
    z=[solve(k) for k in kids];av=mean([p['R'] for p in z])
    axis=[k for k,v in enumerate(tag) if v==-1].index(i)
    d=P['q'][j]*P['cs'][j]['inf'][axis]
    ck(P['I']-sum(p['I'] for p in z)/2==d)
    for k,child in enumerate(kids):ck(raw(child)==c.restrict(t,axis,k))
    actions.append((i,av,kids,z,d));rows+=1
   win=choose([('stop',stop)]+[(i,av) for i,av,_,_,_ in actions]);R=win[1]
   nonnegative(sub(R,stop))
   if sub(R,stop):gaps+=1
   for i,av,kids,z,d in actions:
    extra=sub(R,av);nonnegative(extra)
    credits=[add(p['R'],extra) for p in z]
    debits=[add(p['S'],a) for p,a in zip(z,credits)]
    ck(mean(credits)==R)
    for a,b in zip(credits,debits):nonnegative(a);nonnegative(b)
    e=sub(mean([p['S'] for p in z]),S)
    ck(mean(debits)==add(S,R,e))
   value=dict(S=S,R=R,I=P['I'],winner=win[0])
   with journal.open('a',encoding='utf-8') as f:
    f.write(json.dumps(dict(core=j,tag=tag,S=pack(S),R=pack(R),I=str(P['I']),winner=win[0]),default=str)+'\n')
   ck(time.perf_counter()-START<(55 if pilot else 180))
   return value
  root=solve((-1,)*6);ck(solve.cache_info().currsize==729)
  ck(not sub(root['R'],mul(root['S'],-1)))
  iv=ev(root['R']);ck(F(2857328,100000000)<iv[0]<=iv[1]<F(2857329,100000000))
  # Peer numerical outputs are opened only after independent root/DAG evaluation.
  if source is None:source=json.loads((peers/'out/HULL_CASES.json').read_text(encoding='utf-8'))
  other=next(x for x in source['orbits'] if x['core_orbit']==(2 if j in (2,4) else 3))
  overlap(iv,tuple(F(x,1<<192) for x in other['required_credit']));comparisons+=1
  rec=dict(core=j,states=729,query_rows=1458,root_S=ev(root['S']),required_credit=iv,exact_root_R=pack(root['R']),root_gap={},winner=root['winner'])
  records.append(rec);save('PILOT_ROOTS.json' if pilot else 'ROOTS.json',records)
  solve.cache_clear()
 ck(rows==1458*(1 if pilot else 4))
 result=dict(passed=True,checks=COUNT,helper_checks=c.COUNT,total_checks=COUNT+c.COUNT,cores=[x['core'] for x in records],states=729*len(records),query_rows=rows,states_with_strict_future_credit_need=gaps,independent_packet_tables=physical.cache_info().currsize,inner_tables=c.core.cache_info().currsize,source_root_comparisons=comparisons,runtime_seconds=time.perf_counter()-START,peer_executable_imports=False,quotient_used=False,log_bits=112,full_FEI='OPEN')
 save('PILOT.json' if pilot else 'VALIDATION.json',result);print(json.dumps(result))
if __name__=='__main__':main()
