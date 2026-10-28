"""Exact referee: every physical policy on three-bit sources; no source code imports."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,json,time
sys.dont_write_bytecode=True
import audit as a
ROOT=Path(__file__).resolve().parents[1]
NODES=0
def add(*v):return a.lin(*[(1,x) for x in v])
def mean(v):return a.lin(*[(F(1,len(v)),x) for x in v])
def prod(t):
 ds=a.stats(t)[1]
 return tuple(__import__('math').prod(d if (s>>j)&1 else 1-d for j,d in enumerate(ds)) for s in range(len(t)))
def choose(x,y):
 d=a.lin((1,x[0]),(-1,y[0]))
 if not d:return x
 lo,hi=a.box(d);a.ck(lo>0 or hi<0,'policy maximum rigorously separated')
 return x if lo>0 else y
@lru_cache(None)
def post(t,R):
 """Max KL+sum outcome cost; accompanying FULL entropy of maximizing leaves."""
 p,ds,H,M,TC=a.stats(t);K=a.kl(p,R)
 best=choose((K,H),(TC,H))
 for i in range(len(ds)):
  cs,rr,reach,O,E,Kc,z=a.move(t,i,R)
  v=[post(cs[b],rr[b]) for b in [0,1]]
  best=choose(best,(add(O,mean([x[0] for x in v])),mean([x[1] for x in v])))
 a.ge(a.lin((1,K),(1,M),(-1,best[0])),'post-reset full continuation envelope')
 return best
def pre(t,R,pivot):
 global NODES
 NODES+=1
 p,ds,H,M,TC=a.stats(t);K=a.kl(p,R)
 pair=[a.child(t,pivot,b) for b in [0,1]]
 W=add(*[a.stats(c)[3] for c in pair])
 best=(K,H)
 for i in range(len(ds)):
  cs,rr,reach,O,E,Kc,z=a.move(t,i,R)
  if i==pivot:
   vals=[]
   for b in [0,1]:
    pr=prod(cs[b]);a.eq(a.kl(a.stats(cs[b])[0],pr),a.stats(cs[b])[4],'actual product reset KL')
    vals.append(choose(post(cs[b],rr[b]),post(cs[b],pr)))
   # Sum, rather than average, is the original allocation of two post-pivot M banks.
   a.eq(W,a.lin((2,mean([a.stats(c)[3] for c in cs]))),'same original reserve at pivot')
  else:
   vals=[pre(cs[b],rr[b],pivot-(i<pivot)) for b in [0,1]]
   childW=[add(*[a.stats(a.child(cs[b],pivot-(i<pivot),v))[3] for v in [0,1]]) for b in [0,1]]
   a.ge(a.lin((1,W),(-1,mean(childW))),'child-marginal bank decreases before pivot')
  best=choose(best,(add(O,mean([x[0] for x in vals])),mean([x[1] for x in vals])))
 a.ge(a.lin((1,K),(1,W),(-1,best[0])),'arbitrary phase protected-pivot bound')
 a.ge(a.lin((2,M),(-2,a.ent((ds[pivot],1-ds[pivot]))),(-1,W)),'parent marginal bound excluding pivot')
 return best
def run(pilot):
 rows=[];affine=0
 for mask in ([0,1,42,127] if pilot else range(128)):
  t=(1,)+tuple(-1 if (mask>>i)&1 else 1 for i in range(7))
  c=[a.child(t,0,b) for b in [0,1]];phase=tuple(x*y for x,y in zip(*c))
  isaff=any(all(phase[x]==phase[0]*(-1 if (L&x).bit_count()%2 else 1) for x in range(4)) for L in range(4))
  a.ge(a.lin((1,a.stats(c[0])[3]),(1,a.stats(phase)[3]),(-1,a.stats(c[1])[3])),'phase marginal triangle inequality')
  if isaff:
   affine+=1;a.eq(a.stats(c[0])[3],a.stats(c[1])[3],'affine phase translates marginal entropy')
  refs=[tuple([F(1,8)]*8),tuple(F(j+1,36) for j in range(8)),a.stats(t)[0]]
  W=add(*[a.stats(v)[3] for v in c])
  # Signed splice: only positive M1-M0 requires topping up the old 2M0 bank.
  delta=a.lin((1,a.stats(c[1])[3]),(-1,a.stats(c[0])[3]))
  a.eq(W,a.lin((2,a.stats(c[0])[3]),(1,delta)),'exact signed non-affine liability')
  for R in refs:
   val=pre(t,R,0)
   rows.append({'mask':mask,'affine':isaff,'W':W,'max_terminal_K_plus_O':val[0],'full_terminal_H':val[1]})
 # Source non-lifted witness, reference-only rows preserved after querying u.
 t=tuple(-1 if ((z>>1)&1)*((z&1)^((z>>2)&1)) else 1 for z in range(16))
 R=tuple(F(j+1,136) for j in range(16));cs,rr,*_=a.move(t,0,R)
 witness=[]
 for b in [0,1]:
  q=a.move(cs[b],0,rr[b]);a.ck(q[2]==[F(15,34),F(19,34)],'source asymmetric pivot prediction')
  a.gt(q[3],'nonzero actual pivot outcome cost');witness.append(q[2])
 # Actual non-affine four-bit counterexample; sign, not numerical evidence.
 t=tuple(-1 if (z&1) and ((z>>1)==7) else 1 for z in range(16))
 p=a.stats(t)[0];v=a.move(t,0,p);a.eq(a.kl(p,p),{},'zero original KL')
 for k in v[5]:a.eq(k,{},'zero inherited child KL')
 expected=a.lin((1,a.const(1)),(F(-9,16),a.log(3)))
 actual=mean([a.stats(c)[4] for c in v[0]])
 a.eq(actual,expected,'point-phase exact old-zero-bank debt');a.gt(actual,'strict phase liability')
 a.ck(2**16>3**9,'independent integer sign certificate')
 return {'fixtures':len(rows),'affine_sources':affine,'ordinary_history_nodes':NODES,'rows':rows,'nonlifted_predictions':witness,'nonaffine_expected_reset_K':actual,'post_cache':str(post.cache_info())}
if __name__=='__main__':
 start=time.perf_counter();pilot='--pilot' in sys.argv
 out=run(pilot);out.update(status='PASS',assertions=a.COUNT,seconds=time.perf_counter()-start)
 a.ck(out['seconds']<(60 if pilot else 180),'frozen runtime')
 (ROOT/'out'/('PILOT.json' if pilot else 'EXACT.json')).write_text(json.dumps(a.serial(out),indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps(a.serial({k:v for k,v in out.items() if k!='rows'})))
