from pathlib import Path
from fractions import Fraction as F
from itertools import product
import sys,json,time
sys.dont_write_bytecode=True
import math_kernel as d
R=Path(__file__).resolve().parents[1]
def avg(v):return d.mul(d.add(*v),F(1,len(v)))
class Triangle(d.Triangle):
 def __init__(self,L):super().__init__(L);self.keep=4 if L==1 else 5
 def labels(self,h=(),erase=0):
  forbidden=erase|sum(1<<i for i,s in h)
  explicit=set(range(5))|{4+self.L,self.keep}
  singles=[1<<i for i in sorted(explicit) if not forbidden>>i&1]
  strip=sum(1<<i for i in explicit)
  blocks=[b&~strip&~forbidden for b in self.private[1:]]
  for flags in product([0,1],repeat=2):
   if any(v and not b for v,b in zip(flags,blocks)):continue
   count=1;rep=0
   for v,b in zip(flags,blocks):
    if v:count*=(1<<b.bit_count())-1;rep|=b&-b
   for pick in range(1<<len(singles)):
    yield count,rep|sum(b for j,b in enumerate(singles) if pick>>j&1)
def subtree(t,h,query,marker):
 if not query:return t.full_ce(h,lambda S:t.lift(h,marker,S))[0],[]
 i=query[0];children=[];leaves=[]
 for u in [0,1]:
  hh=h+((i,u),);v,ls=subtree(t,hh,query[1:],marker);children.append(v);leaves+=ls if ls else [hh]
 return d.add(t.row(h,i)[2],avg(children)),leaves
def case(L):
 t=Triangle(L);j=t.keep;z=4+L
 rows=[t.row((),i) for i in [0,1,2,3,4,z]]
 M=d.add(*(d.mul(r[1],1 if k<4 else L) for k,r in enumerate(rows)))
 I=rows[3][0]+L*(rows[4][0]+rows[5][0]);D=d.add(M,rows[3][2],avg([t.row(((3,s),),1)[2] for s in [0,1]]))
 old=[];final=[];intermediate=[];nodes=[]
 for s,b in product([0,1],repeat=2):
  h=((3,s),(1,b));ce=t.full_ce(h,lambda S:t.lift(h,0,S))[0];old.append(ce)
  queries=([4] if L>1 else [])+[z,0,2]
  bill,leaves=subtree(t,h,queries,j);final.append(bill)
  budget=d.add(t.entropy(h),(F(1),F(1)))
  d.ck(bill[0]<=budget[1]);d.ck(d.sub(bill,ce)[0]<=t.row(h,0)[2][1])
  if s==b==1:d.zero(d.sub(bill,(F(1),F(1))))
  prefix,als=subtree(t,h,queries[:-1],2);intermediate.append(prefix)
  # Exact local sixth-reset accounting at every retained c-parent.
  for hh in als:
   incoming=t.full_ce(hh,lambda S:t.lift(hh,2,S))[0];Bc=t.row(hh,2)[2]
   fresh=[];inc=[];terminal=[]
   for u in [0,1]:
    child=hh+((2,u),);new=t.full_ce(child,lambda S:t.lift(child,j,S))[0]
    inherited=t.full_ce(child,lambda S:t.p(hh,S)+t.p(hh,S|4))[0]
    fresh.append(new);inc.append(inherited)
    H=t.entropy(child);KL=d.sub(new,H);Bj=t.row(child,j)[2]
    d.zero(d.sub(KL,d.sub((F(1),F(1)),Bj)));d.ck(KL[0]<=1 and KL[1]>=0)
    for count,S in t.labels(child):d.ck(t.amp(child,S)==t.amp(hh,S)+(-1)**u*t.amp(hh,S|4))
    terminal.append(dict(c=u,CE=d.saved(new),H=d.saved(H),KL=d.saved(KL)))
   rho=d.sub((F(1),F(1)),Bc);Delta=d.sub(avg(fresh),avg(inc));net=d.sub(d.add(Bc,avg(fresh)),incoming)
   d.zero(d.sub(net,d.sub(Delta,rho)))
   d.zero(d.sub(net,d.sub(d.sub(Bc,t.js(hh,2)),avg([t.row(hh+((2,u),),j)[2] for u in [0,1]]))))
   nodes.append(dict(history=hh,net=d.saved(net),Delta=d.saved(Delta),rho=d.saved(rho),terminals=terminal))
 C2=d.add(D,avg(old));bill=d.add(D,avg(final));before=d.add(D,avg(intermediate));spare=d.sub((17*I,17*I),bill)
 d.ck(d.sub((17*I,17*I),C2)[0]>F(7,8));d.ck(spare[0]>F(1,8))
 return dict(L=L,j=j,source_C2=d.saved(C2),source_spare=d.saved(d.sub((17*I,17*I),C2)),D=d.saved(D),I_private=str(I),pre_c_bill=d.saved(before),final_bill=d.saved(bill),final_spare=d.saved(spare),nodes=nodes)
def tail():
 C=d.add((F(39,16),F(39,16)),d.logs([(F(1,4),F(10)),(F(9,16),F(10,9))]))
 endpoint=d.sub((F(17,4),F(17,4)),d.add(C,(F(26217,4194304),)*2))
 d.ck(endpoint[0]>F(7,8));d.ck(2*6550-(2*21*21+124*21+3270)==2*20*20+120*20+3144)
 return dict(C_infinity=d.saved(C),L20_spare=d.saved(endpoint),polynomial='2L^2+124L+3270',analytic_error='Five entropy errors plus original oriented M; reviewed source DERIVATION section2')
if __name__=='__main__':
 start=time.monotonic();pilot='--pilot' in sys.argv;domain=[1,2,3] if pilot else list(range(1,21))+[32,64];records=[]
 for L in domain:
  records.append(case(L));d.ck(time.monotonic()-start<(55 if pilot else 180))
  (R/'out/CHECKPOINT.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
 ans=dict(cases=records,tail=tail(),checks=d.CHECKS,seconds=time.monotonic()-start)
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(ans,indent=2),encoding='utf-8')
 pos=[(r['L'],n['history']) for r in records for n in r['nodes'] if F(n['net'][0])>0]
 print(json.dumps(dict(checks=d.CHECKS,seconds=ans['seconds'],widths=len(records),positive_local_sixth_count=len(pos),first_positive=pos[:2])))
