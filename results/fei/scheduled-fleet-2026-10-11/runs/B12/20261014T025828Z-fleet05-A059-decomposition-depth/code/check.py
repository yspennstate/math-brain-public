import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools,json,time
import exact as e
ROOT=Path(__file__).resolve().parents[1]
count=0;outerchecks=0;conversions=0
def ok(b,msg=''):
 global count
 count+=1
 if not b:raise AssertionError(msg)
def add(*args):return e.add(*args)
def ln2coef(x):return add({},e.cost(Q(1,2)),2*x)
def assert_le(a,b={},constant=Q(0),msg=''):
 global count
 count+=1
 dif=add(a,b,-1)
 if dif and e.bounds(dif)[1]>constant:raise AssertionError(msg)
 if not dif and constant<0:raise AssertionError(msg)
def table(n):return [tuple(1-2*((mask>>x)&1) for x in range(1<<n)) for mask in range(1<<(1<<n))]
def gated(internal,r):
 return tuple(internal[x>>r] if x&((1<<r)-1)==0 else 0 for x in range(len(internal)<<r))
def erasure(a,index):
 out={}
 for s in range(len(a)):
  if not s&(1<<index):out=add(out,e.phi(a[s]**2,a[s|(1<<index)]**2))
 return out
@lru_cache(None)
def profile(c,u,v,s):
 global conversions
 parent=e.state(c,u,v)
 if not s or any(c[x]!=0 for x in range(len(c)) if x&((1<<s)-1)):return None
 internal=tuple(c[x<<s] for x in range(len(c)>>s));p=e.state(internal,u,v)
 q=Q(1,1<<s);M=p['a'][0];var=1-M*M
 vbar=sum(prob*V for prob,V in zip(p['q'],p['V']))
 L=var-vbar;ok(L>=0,'total variance of means')
 ok(parent['U']==add({},p['U'],q),'fine U grouping')
 ok(parent['R']==add(ln2coef(q*s*vbar),p['R'],q),'fine R grouping')
 coarseU=add({},add(p['H'],e.cost(M*M),-1),q)
 coarseR=ln2coef(q*s*var)
 transfer=add(add(p['H'],p['U'],-1),p['R'],-1)
 transfer=add(transfer,e.cost(M*M),-1);transfer=add(transfer,ln2coef(s*L));transfer=add({},transfer,q)
 ok(add(add(coarseU,coarseR),add(parent['U'],parent['R']),-1)==transfer,'exact terminal grouping conversion')
 assert_le({},transfer,msg='nonnegative terminal grouping transfer')
 conversions+=1
 return q,M,var,vbar,L
@lru_cache(None)
def node(c,u,v,g,i,s):
 global outerchecks
 D,kappa,cap,t,dataI=e.node_check(c,u,v,g,i)
 st=e.state(c,u,v);inf=e.influence(st['a'],sum(st['n'][:g])+i)
 if g==0 and i<s:
  params=profile(c,u,v,s)
  if params:
   q,M,V,Vbar,L=params;a=1-M;z=q*a
   ok(inf==z,'actual outer physical influence')
   ok(kappa==ln2coef(q*Vbar),'fine-state outer release')
   B=erasure(st['a'],i);packet=e.phi((1-z)**2,z*z)
   expected=add(ln2coef((q-2*q*q)*a*a+q*L),packet)
   ok(add(B,kappa,-1)==expected,'mixed erasure pair identity')
   ok(add(ln2coef(q*V),kappa,-1)==ln2coef(q*L),'coarse-fine release discrepancy')
   residual=add(D,kappa,-1)
   assert_le({},residual,msg='mixed residual nonnegative')
   assert_le(residual,ln2coef(3*z),2*z,'unchanged mixed residual price')
   # Independent single-core A091 source price on same actual F.
   coarseB=add(B,ln2coef(q*V),-1)
   ok(coarseB==add(ln2coef((q-2*q*q)*a*a),packet),'source point-pair review')
   assert_le(add(D,ln2coef(q*V),-1),ln2coef(3*z),2*z,'source point residual review')
  else:
   ok(st['I']==0 and D=={} and kappa=={},'failed gate endpoint')
  outerchecks+=1
 return D,kappa,t,dataI,inf
def run_tree(c,u,v,r,policy):
 st=e.state(c,u,v);sizes=st['n'];N=sum(sizes)
 ids=tuple((g,i) for g,n in enumerate(sizes) for i in range(n))
 if policy==0:order=ids
 elif policy==1:order=tuple(x for x in ids if x[0])+tuple(x for x in ids if not x[0])
 else:order=tuple(sorted(ids,key=lambda x:(x[1],x[0])))
 front=[{'H':{},'U':{},'R':{},'resinner':{},'resouter':{},'release':{},'loss':{},'T':Q(0),'Piouter':Q(0),'spent':Q(0),'I':Q(0)} for _ in range(N+1)]
 def visit(c,u,v,remaining,dep,w,ri,ro,release,loss,T,Piouter,spent):
  state=e.state(c,u,v);z=front[dep]
  for name in ['H','U','R']:z[name]=add(z[name],state[name],w)
  for name,vec in [('resinner',ri),('resouter',ro),('release',release),('loss',loss)]:z[name]=add(z[name],vec,w)
  z['T']+=w*T;z['Piouter']+=w*Piouter;z['spent']+=w*spent;z['I']+=w*state['I']
  s=sum(x<r for x in remaining[0]);profile(c,u,v,s)
  if not any(remaining):return
  if policy==3:
   choices=[(g,i) for g in range(3) for i in range(len(remaining[g]))]
   g,i=max(choices,key=lambda x:(e.influence(state['a'],sum(state['n'][:x[0]])+x[1]),(-1 if state['a'][0]<0 else 1)*(x[0]*8+x[1])))
  else:
   target=next(x for x in order if x[1] in remaining[x[0]])
   g=target[0];i=remaining[g].index(target[1])
  D,kappa,t,dataI,inf=node(c,u,v,g,i,s)
  isouter=g==0 and remaining[0][i]<r
  residual=add(D,kappa,-1)
  rr=list(remaining);rr[g]=rr[g][:i]+rr[g][i+1:];rr=tuple(rr)
  for b in [0,1]:
   pp=[c,u,v];pp[g]=e.slice_table(pp[g],i,b)
   visit(*pp,rr,dep+1,w/2,add(ri,residual if g==0 and not isouter else {}),add(ro,residual if isouter else {}),add(release,kappa if g==0 else {}),add(loss,kappa if g else {}),T+t,Piouter+(inf if isouter else 0),spent+inf)
 visit(c,u,v,tuple(tuple(range(n)) for n in sizes),0,Q(1),{},{},{},{},Q(0),Q(0),Q(0))
 for f in front:
  ok(st['R']==add(add(f['R'],f['release']),f['loss']),'stopped fine reserve conservation')
  ok(st['I']==f['spent']+f['I'],'same-tree influence conservation')
  assert_le(f['resouter'],ln2coef(3*f['Piouter']),2*f['Piouter'],'stopped outer residual price')
  terminal=add(add(f['H'],f['U'],-1),f['R'],-1)
  rhs=add(add(add(st['U'],st['R']),terminal),f['resinner'])
  rhs=add(rhs,ln2coef(3*f['Piouter']))
  assert_le(st['H'],rhs,3*f['T']+2*f['Piouter'],'actual stopped mixed ledger')
 return N+1
def main(pilot):
 start=time.perf_counter();roots=trees=frontiers=0
 maps=list(itertools.product(range(3),repeat=2))
 for internal in (maps[:1] if pilot else maps):
  for u,v in itertools.product(table(1),repeat=2):
   for r in ([1] if pilot else [1,2,3]):
    c=gated(internal,r)
    for policy in range(4):frontiers+=run_tree(c,u,v,r,policy);trees+=1
    roots+=1
    if time.perf_counter()-start>290:raise RuntimeError('frozen main budget exceeded')
 if not pilot:
  for internal in [(1,2,1,0),(1,0,2,0),(1,2,2,0),(0,1,2,0)]:
   for u,v in itertools.product(table(1),repeat=2):
    for r in [1,2]:
     for policy in [2,3]:frontiers+=run_tree(gated(internal,r),u,v,r,policy);trees+=1
     roots+=1
 counter=[]
 for s in ([] if pilot else range(1,65)):
  q=Q(1,1<<s);increase=s*q/4;physical=q/2
  ok(increase/physical==Q(s,2),'exact mean-migration witness')
  counter.append({'outer_width':s,'increase_over_data_influence':str(increase/physical)})
 out={'status':'PASS','roots':roots,'trees':trees,'frontiers':frontiers,'new_assertions':count,'kernel_assertions':e.checks,'assertions':count+e.checks,'outer_node_checks':outerchecks,'terminal_conversions':conversions,'counterfamily':counter,'elapsed_seconds':time.perf_counter()-start,'pilot':pilot,'node_cache':str(node.cache_info())}
 (ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k!='counterfamily'}))
if __name__=='__main__':main('--pilot' in sys.argv)
