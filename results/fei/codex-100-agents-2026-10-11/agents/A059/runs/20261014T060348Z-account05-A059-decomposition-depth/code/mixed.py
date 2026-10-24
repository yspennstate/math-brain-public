import sys
sys.dont_write_bytecode=True
import check as c
import exact as e
from fractions import Fraction as Q
import json,time
def data(status,cores,j,i):
 ct=c.select(status);st=c.state(ct,cores);children=[]
 for b in [0,1]:
  cs=list(cores);cs[j]=e.slice_table(cs[j],i,b);children.append(c.state(ct,tuple(cs)))
 D=e.add(st['H'],e.add(children[0]['H'],children[1]['H']),-Q(1,2))
 du=e.add(st['U'],e.add(children[0]['U'],children[1]['U']),-Q(1,2))
 dr=e.add(st['R'],e.add(children[0]['R'],children[1]['R']),-Q(1,2))
 q=st['q'][j];core=e.walsh(cores[j]);t=core[1<<i]**2
 e.ok(dr==e.add({},e.cost(q),t),'same fine reserve data loss')
 e.leconst(e.add(e.add(D,du,-1),dr,-1),3*q*t,'signed data price3/ln2')
 offset=st['ns'][0]+sum(st['ns'][1:j+1])+i
 inf=e.influence(st['a'],offset)
 e.ok(inf==q*e.influence(core,i),'actual data influence')
 e.ok(st['I']==inf+(children[0]['I']+children[1]['I'])/2,'data influence conservation')
 return children
def tree(status,cores,policy):
 st=c.state(c.select(status),cores)
 # Stop when all controller coordinates have been physically exposed.
 def rec(ct,cs,remaining,w):
  z=c.state(ct,cs)
  if not remaining:
   # An actual selector is constant once all physical controls are exposed.
   e.ok(len(set(ct))==1,'controller-resolved leaf')
   label=ct[0];mean=Q(1) if label==0 else Q(sum(cs[label-1]),len(cs[label-1]))
   terminal=e.add(e.add(z['H'],z['U'],-1),z['R'],-1)
   e.ok(terminal==e.cost(mean*mean),'actual biased terminal')
   e.leconst(terminal,z['I'],'terminal<=I/ln2')
   return terminal,Q(0),Q(0),z['I']
  # Query later private controller first, with one genuine data insertion.
  token=remaining[0]
  if token[0]=='c':
   orig=token[1];ids=[x[1] for x in remaining if x[0]=='c'];idx=sorted(ids).index(orig)
   child=[(e.slice_table(ct,idx,b),cs) for b in [0,1]];inf=e.influence(z['a'],idx)
   spent_ctrl=inf;spent_data=Q(0)
  else:
   j=token[1];child=[]
   for b in [0,1]:
    qq=list(cs);qq[j]=e.slice_table(cs[j],0,b);child.append((ct,tuple(qq)))
   inf=e.influence(z['a'],z['ns'][0]+sum(z['ns'][1:j+1]))
   spent_ctrl=Q(0);spent_data=z['q'][j]*e.walsh(cs[j])[1]**2
  term={};pc=spent_ctrl;td=spent_data;il=Q(0)
  for cc,qq in child:
   a,b,d,i=rec(cc,qq,remaining[1:],w/2);term=e.add(term,a,Q(1,2));pc+=b/2;td+=d/2;il+=i/2
  # Every actual subtree uses SAME root fine U/R and literal terminal.
  rhs=e.add(e.add(z['U'],z['R']),term);rhs=e.add(rhs,c.L(17*pc))
  e.leconst(e.add(z['H'],rhs,-1),3*td,'all-order stopped physical ledger')
  # Full spent DATA influence differs from singleton td; exact tree
  # influence conservation is checked per query above for this tree too.
  e.ok(z['I']==inf+sum(c.state(cc,qq)['I'] for cc,qq in child)/2,'tree edge influence')
  return term,pc,td,il
 n=sum(status);ctrl=list(range(n));ctrl=ctrl[::-1] if policy else [1,2,0]
 order=[('c',ctrl[0]),('d',1)]+[('c',x) for x in ctrl[1:]]
 rec(c.select(status),cores,order,Q(1))
def main(pilot):
 start=time.perf_counter();nodes=queries=trees=roots=0
 for sign in ([1] if pilot else [1,-1]):
  seed=tuple(sign*x for x in (1,1,1,-1));base=(seed,seed,seed)
  fixtures=[base]
  for j in range(3):
   for b in [0,1]:
    cs=list(base);cs[j]=e.slice_table(cs[j],0,b);fixtures.append(tuple(cs))
  for status in ([(1,1,1)] if pilot else [(1,1,1),(1,2,1)]):
   for cores in fixtures:
    for j in range(3):c.node(status,cores,j);nodes+=1
    roots+=1
    c.state.cache_clear();e.walsh.cache_clear()
   for j in range(3):
    for i in range(2):data(status,base,j,i);queries+=1
  if not pilot:
   for p in [0,1]:tree((1,1,1),base,p);trees+=1
 out={'status':'PASS','roots':roots,'controller_query_types':nodes,'actual_data_queries':queries,'actual_stopped_trees':trees,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-start,'pilot':pilot}
 (c.ROOT/'out'/('mixed_pilot.json' if pilot else 'mixed_validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main('--pilot' in sys.argv)
