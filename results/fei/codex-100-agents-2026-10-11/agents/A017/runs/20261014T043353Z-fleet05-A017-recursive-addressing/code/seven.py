"""A017-seven-edit-fixture-v1: exact bad-pivot and adaptive repair."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util,json,time
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('utility',R.parent/'20261011T234546Z-fleet05-A017-recursive-addressing/code/check.py');U=importlib.util.module_from_spec(sp);sp.loader.exec_module(U)
checks=0
def req(ok):
 global checks
 checks+=1
 if not ok:raise AssertionError(checks)
def cut(v,n,i,bit):return [v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(1<<(n-1))]
def tree(g,b,ids,Q,first=None):
 n=len(ids);sp=U.spectrum(g,[0]*(1<<n));inf,_,C,_=U.spectral_metrics(sp,n);H=U.entropy(sp,n)
 polar=[i for i in range(n) if Q[ids[i]]&sum(1<<j for j in ids)]
 if g==b or not polar:
  req(U.LF((4+U.log_interval(7)[0])*sum(inf)).add(H,-1).interval()[0]>=0)
  return F(0),F(0),sum(inf),0
 i=ids.index(first) if first is not None else polar[0];B=U.erasure(sp,n,i)
 margin=U.LF().add(B).add(U.LF(4*inf[i]),-1);lo,hi=margin.interval();req(lo>0 or hi<=0)
 bad=int(lo>0);charge=C[i] if bad else F(0)
 children=[tree(cut(g,n,i,t),cut(b,n,i,t),ids[:i]+ids[i+1:],Q) for t in [0,1]]
 bill=charge+sum(v[0] for v in children)/2;spent=inf[i]+sum(v[1] for v in children)/2;terminal=sum(v[2] for v in children)/2
 req(spent+terminal==sum(inf))
 return bill,spent,terminal,bad+sum(v[3] for v in children)
start=time.perf_counter();n=5;edges=[(0,1),(1,2),(3,4)];code=U.poly_code(n,edges);ell,_,Q=U.parameters(n,code);base=U.signs(n,ell,edges)
E=[x for x in range(32) if x&3==3 and x!=3];req(len(E)==7)
g=base.copy()
for x in E:g[x]*=-1
sp=U.spectrum(g,[0]*32);inf,pairs,C,dc=U.spectral_metrics(sp,5);physical=U.physical(g,[0]*32,5);req((inf,pairs,dc)==physical)
B=U.erasure(sp,5,0);expected=U.LF(1).log(3,-F(45,64)).log(5,-F(25,32)).log(13,F(39,64))
req(B==expected and inf[0]==F(1,16) and C[0]==F(3,8))
req(2**192*13**156>3**180*5**200)
bad=tree(g,base,list(range(5)),Q,first=0);repair=tree(g,base,list(range(5)),Q,first=1)
req(bad[0]==F(3,8) and bad[3]==1 and repair[0]==0 and repair[3]==0)
H=U.entropy(sp,5);req(U.LF((4+2/U.LN2[1])*repair[1]+(4+U.log_interval(7)[0])*repair[2]).add(H,-1).interval()[0]>=0)
out=dict(status='PASS',helper='A017-seven-edit-fixture-v1',q_edges=edges,edits=E,influence=[str(x) for x in inf],I_phase=str(sum(inf)),B_root_x0=B.json(),C_root_x0=str(C[0]),integer_badness='2^192*13^156 > 3^180*5^200',integer_positive_slack=str(2**192*13**156-3**180*5**200),bad_minimum_polar_order=dict(first=0,bill=str(bad[0]),bad_nodes=bad[3]),repaired_order=dict(first=1,bill=str(repair[0]),bad_nodes=repair[3],spent=str(repair[1]),terminal_phase=str(repair[2])),assertions=checks,elapsed_seconds=time.perf_counter()-start)
(R/'out/SEVEN_EDIT_FIXTURE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print(json.dumps({k:v for k,v in out.items() if k not in ['B_root_x0','integer_positive_slack']}))
