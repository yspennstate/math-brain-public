"""Full mixed-order replay, importing only this run's independently built primitives."""
from pathlib import Path
from fractions import Fraction as F
import json,time
import check_transfer as q
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out'
spec={'helper':'check_mixed.py v1 + own check_transfer.py direct-character primitives','family':'negative-cell edit 1-2A_a+2A_(a+b+r)','domain':{'a':[1,2,3],'b':[0,1],'r':[2,3],'references':['matching','uniform','increasing','singleton-spiked']},'roots':48,'case_count':'376 prefix nodes (deterministic recursion count below asserted)','symmetry':'One specified active label and one control label at each step; no claim of exhaustive asymmetric-reference label permutations','arithmetic':'Fraction spectra, rational logarithm bounds from own primitive checker','memory_estimate_mb':80,'max_runtime_seconds':55,'scope':'all active/control type orders until final active boundary or r=1; all complementary children keep inherited references'}
(OUT/'FROZEN_MIXED_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
nodes=0;control_steps=0;active_steps=0;minimum=None
def scan(a,b,r,R,reach,debit,term,quota,e0,used,Wroot):
 global nodes,control_steps,active_steps,minimum
 nodes+=1
 v,P,Q=q.floor(a,b,r,R)
 total=q.add(debit,term,q.mul(reach,q.CE(P,Q)))
 q.ck(total[1]<=Wroot[1]+8*used*e0)
 q.ck(total[1]<=quota-12*e0)
 margin=(quota-total[1])/e0;minimum=margin if minimum is None else min(minimum,margin)
 Rn,d,k,last=q.active(a,b,r,R)
 dd=q.add(debit,q.mul(reach,d));tt=q.add(term,q.mul(reach/2,k));active_steps+=1
 if a==1:
  terminal=q.add(dd,tt,q.mul(reach/2,last));q.ck(terminal[1]<=quota-12*e0)
 else:scan(a-1,b,r,Rn,reach/2,dd,tt,quota,e0,used,Wroot)
 if r>=2:
  j=a+b;old=q.marginal(Q,j);off=q.child(v,j,1);on=q.child(v,j,0)
  vn,pn,qn=q.floor(a,b,r-1,R);q.ck(on==vn)
  d=q.B(P,j);coff=q.CE(q.spec(off),old);e=F(2,1<<(a+b+r))
  q.ck(reach*e==e0)
  loc=q.add(d,q.mul(F(1,2),coff),q.mul(F(1,2),q.W(a,b,r-1,R)))
  q.ck(loc[1]<q.W(a,b,r,R)[0]+8*e)
  control_steps+=1
  scan(a,b,r-1,R,reach/2,q.add(debit,q.mul(reach,d)),q.add(term,q.mul(reach/2,coff)),quota,e0,used+1,Wroot)
roots=0
for a in [1,2,3]:
 for b in [0,1]:
  for r in [2,3]:
   Pg=q.spec(q.src(a,b));N=len(Pg)
   for raw in [Pg,[F(1,N)]*N,[F(2*(i+1),N*(N+1)) for i in range(N)],[F(1000 if i==1 else 1,1000+N-1) for i in range(N)]]:
    R=q.cal(raw,Pg);c=q.CE(Pg,R);Ig=F(2*a,1<<a);K=2*c[1]/Ig+10
    e0=F(2,1<<(a+b+r));v,P,Q=q.floor(a,b,r,R);quota=K*q.influence(v)
    q.ck(quota-q.W(a,b,r,R)[1]>=5*a*(1<<(b+r))*e0)
    q.ck(5*a*(1<<(b+r))-8*(r-1)>=12)
    scan(a,b,r,R,F(1),(F(0),F(0)),(F(0),F(0)),quota,e0,0,q.W(a,b,r,R));roots+=1
def count(a,r):return 1+(count(a-1,r) if a>1 else 0)+(count(a,r-1) if r>1 else 0)
expected=sum(count(a,r)*8 for a in [1,2,3] for r in [2,3])
q.ck(nodes==expected)
result={'status':'PASS','roots':roots,'prefix_nodes':nodes,'expected_nodes':expected,'active_steps':active_steps,'control_steps':control_steps,'checks':q.checks,'runtime_seconds':time.perf_counter()-q.START,'minimum_observed_margin_over_e_root':str(minimum),'rung':'exact finite validation plus analytic induction; not Lean-checked'}
(OUT/'MIXED_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
