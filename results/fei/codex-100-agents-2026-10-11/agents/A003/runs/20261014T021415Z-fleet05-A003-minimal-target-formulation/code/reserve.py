import lib as L
from lib import Q,add
from pathlib import Path
import itertools,time,json
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();assertions=0
def ck(b):
 global assertions
 assertions+=1;assert b;assert time.perf_counter()-start<58
def p(t):return [v*v for v in L.fw(t)]
def sl(t,i,s):return tuple(t[(b&((1<<i)-1))|((s<0)<<i)|((b>>i)<<(i+1))] for b in range(len(t)//2))
def erased(t,labels,order):
 if not order:return {}
 i=labels.index(order[0]);rest=labels[:i]+labels[i+1:]
 return add((1,L.edge(p(t),i)),(Q(1,2),erased(sl(t,i,1),rest,order[1:])),(Q(1,2),erased(sl(t,i,-1),rest,order[1:])))
h=tuple(L.majority(3,[]));out=[]
for k in [2,4,6]:
 delta=Q(1,1<<k)
 bent=tuple(1 if sum(((b>>(2*j))&1)*((b>>(2*j+1))&1) for j in range(k//2))%2==0 else -1 for b in range(1<<k))
 g=tuple(bent[y] if s==0 or y else -1 for y in range(1<<k) for s in range(2))
 F=tuple(g[2*y+((hx<0)^u)] for y in range(1<<k) for u in range(2) for hx in h)
 ck(L.edge(p(F),3)=={})
 for order in itertools.permutations(range(3)):ck(erased(h,(0,1,2),order)=={2:Q(1)})
 out.append({'k':k,'physical_unlock_erasure':'0','inherited_encoder_erasure':str(delta),'encoder_orders':6,'terminal_slack_lower_bound':str(2*k*delta),'analytic_reserve_scope':'even k>=4 only'})
(ROOT/'out/TERMINAL_OWNER.json').write_text(json.dumps({'status':'PASS','assertions':assertions,'controls':out,'runtime_seconds':time.perf_counter()-start},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','assertions':assertions,'runtime_seconds':time.perf_counter()-start}))
