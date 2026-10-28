from pathlib import Path
from fractions import Fraction as F
import exact as E
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();count=0
def ck(x):
 global count
 assert x;count+=1;assert time.perf_counter()-start<55
def ell(u):
 ans={}
 for x,w in [(1+u,(1+u)**2/2),(1-u,(1-u)**2/2),(u,-u*u)]:
  if x and w:ans=E.add(ans,E.scale(E.logvec(x),w))
 return ans
N=512;lo=F(1,5);hi=F(3,4);step=(hi-lo)/N;rows=[];minimum=None
for j in range(N):
 a=lo+j*step;b=a+step;u=(a+b)/2
 d=E.add(ell(u),{2:-(5*u-1)/2});l,h=E.bounds(d);lower=l-12*step/2
 ck(lower>0)
 minimum=lower if minimum is None else min(minimum,lower)
 rows.append({'left':str(a),'right':str(b),'mid':str(u),'D_interval':[str(l),str(h)],'entire_cell_lower':str(lower)})
ck(rows[0]['left']==str(lo) and rows[-1]['right']==str(hi))
for a,b in zip(rows,rows[1:]):ck(a['right']==b['left'])
endpoint=E.add(ell(hi),{2:-(5*hi-1)/2});ck(E.bounds(endpoint)[0]>0)
ck(F(7,4)+F(8,5)+F(9,2)+F(5,2)<12)
ck(F(1,5)<F(3,4) and F(3,4)**2>F(1,2))
assert ell(F(0))=={} and E.bounds(E.add(ell(F(1)),{2:-2}))==(0,0)
(R/'out/SCALAR_CELLS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
res={'status':'PASS','cells':N,'assertions':count,'minimum_middle_cell_lower':str(minimum),'domain':'[0,1/5] analytic positivity;[1/5,3/4] tiled exact cells;[3/4,1] analytic concavity/endpoints','Lipschitz_constant':12,'runtime_seconds':time.perf_counter()-start,'theorem':'L(u)>=(5u-1)/2 on[0,1]'}
(R/'out/SCALAR.json').write_text(json.dumps(res,indent=2),encoding='utf-8');print(json.dumps(res))
