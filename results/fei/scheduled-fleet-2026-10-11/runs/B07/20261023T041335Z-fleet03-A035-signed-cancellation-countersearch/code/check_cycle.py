from pathlib import Path
import sys,json,time
from itertools import product
from fractions import Fraction as F
sys.dont_write_bytecode=True
import dependency as d
R=Path(__file__).resolve().parents[1]
class Triangle(d.Triangle):
 def labels(self,h=(),erase=0):
  forbidden=erase|sum(1<<i for i,s in h)
  singles=[1<<i for i in list(range(5))+[4+self.L] if not forbidden>>i&1]
  blocks=[(self.private[1]&~16)&~forbidden,(self.private[2]&~(1<<(4+self.L)))&~forbidden]
  for flags in product([0,1],repeat=2):
   if any(v and not m for v,m in zip(flags,blocks)):continue
   mult=1;rep=0
   for v,b in zip(flags,blocks):
    if v:mult*=(1<<b.bit_count())-1;rep|=b&-b
   for pick in range(1<<len(singles)):
    yield mult,rep|sum(b for j,b in enumerate(singles) if pick>>j&1)
def avg(xs):return d.mul(d.add(*xs),F(1,len(xs)))
def case(L):
 T=Triangle(L);z=4+L;parents=[];oldce=[];newbills=[];third=[];fourth=[]
 for s,t in product([0,1],repeat=2):
  h=((3,s),(1,t));By=T.row(h,4)[2]
  ce=T.full_ce(h,lambda S:T.lift(h,0,S))[0];oldce.append(ce)
  fourthnodes=[];after=[];terminal=[];thirdce=[]
  for u in [0,1]:
   hy=h+((4,u),);Bz=T.row(hy,z)[2]
   incoming_ce=T.full_ce(hy,lambda S:T.lift(hy,2,S))[0];thirdce.append(incoming_ce)
   ci=[];cn=[]
   for v in [0,1]:
    leaf=hy+((z,v),)
    incoming=lambda S:T.lift(hy,2,S)+T.lift(hy,2,S|(1<<z))
    a=T.full_ce(leaf,incoming)[0];b=T.full_ce(leaf,lambda S:T.lift(leaf,0,S))[0]
    ci.append(a);cn.append(b)
    for m,S in T.labels(leaf):
     d.ck(T.amp(leaf,S)==T.amp(hy,S)+(1 if v==0 else -1)*T.amp(hy,S|(1<<z)))
    terminal.append(dict(x=s,b=t,y=u,z=v,H=d.saved(T.entropy(leaf)),CE=d.saved(b)))
    if s==t==1:d.zero(d.sub(b,(F(1),F(1))))
   rho=T.cmi(hy,z,2);delta=d.sub(avg(cn),avg(ci));net=d.sub(d.add(Bz,avg(cn)),incoming_ce)
   d.zero(d.sub(net,d.sub(delta,rho)))
   formula=d.sub(d.sub(T.row(hy,2)[2],T.js(hy,z)),avg([T.row(hy+((z,v),),0)[2] for v in [0,1]]))
   d.zero(d.sub(net,formula))
   fourthnodes.append(dict(y=u,rho=d.saved(rho),Delta=d.saved(delta),net=d.saved(net),symmetry_gap_c_minus_a=d.saved(d.sub(T.row(hy,2)[2],T.row(hy,0)[2]))))
   after.append(d.add(Bz,avg(cn)))
  bill=d.add(By,avg(after));newbills.append(bill)
  net=d.sub(bill,ce);oldthird=d.add(By,avg(thirdce));third.append(oldthird);fourth.append(d.sub(bill,oldthird))
  # Independently expanded entropy identity across the two physical levels.
  Ba=T.row(h,0)[2];J=d.add(T.js(h,4),avg([T.js(h+((4,u),),z) for u in [0,1]]))
  Bafin=avg([T.row(h+((4,u),(z,v)),0)[2] for u,v in product([0,1],repeat=2)])
  d.zero(d.sub(net,d.sub(d.sub(Ba,J),Bafin)))
  parents.append(dict(x=s,b=t,cycle_net=d.saved(net),fourth_nodes=fourthnodes,terminals=terminal))
 rootrows=[T.row((),i) for i in [0,1,2,3,4,z]]
 M=d.add(*(d.mul(r[1],1 if i<4 else L) for i,r in enumerate(rootrows)))
 Ip=rootrows[3][0]+L*(rootrows[4][0]+rootrows[5][0])
 prefix=d.add(M,rootrows[3][2],avg([T.row(((3,s),),1)[2] for s in [0,1]]))
 bill=d.add(prefix,avg(newbills));spare=d.sub((17*Ip,17*Ip),bill)
 d.ck(spare[0]>F(1,32))
 record=dict(L=L,I_private=str(Ip),original_debits=d.saved(prefix),old_bill=d.saved(d.add(prefix,avg(oldce))),fourth_bill=d.saved(bill),spare=d.saved(spare),third_bill=d.saved(d.add(prefix,avg(third))),mean_fourth_net=d.saved(avg(fourth)),parents=parents)
 return record
if __name__=='__main__':
 start=time.monotonic();pilot='--pilot' in sys.argv;domain=[1,2,3] if pilot else [1,2,3,4,8,16,32,64];records=[]
 for L in domain:
  records.append(case(L));d.ck(time.monotonic()-start<(55 if pilot else 180))
  (R/'out/CHECKPOINT.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
 ans=dict(cases=records,checks=d.CHECKS,runtime_seconds=time.monotonic()-start)
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(ans,indent=2),encoding='utf-8')
 positive=[(r['L'],p['x'],p['b'],n['y'],n['net']) for r in records for p in r['parents'] for n in p['fourth_nodes'] if F(n['net'][0])>0]
 print(json.dumps(dict(checks=d.CHECKS,seconds=ans['runtime_seconds'],positive_fourth_net=positive)))
