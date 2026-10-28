from pathlib import Path
from fractions import Fraction as F
import sys,time,json
sys.dont_write_bytecode=True
import audit as a
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();rows=[]
for n in [7,8,16,32]:
 m=n-1;d=F(1,2**(n-1));b=2*d;ep=2*b-b*b
 H=a.lin((-2*(1-b)**2,a.log(1-b)),(-2*(2**m-1)*b*b,a.log(b)))
 H2=a.lin((1,a.ent((ep,1-ep))),(ep,a.log(2**m-1)))
 a.eq(H,H2,'two independent exact entropy decompositions')
 M=a.lin((m,a.ent((b,1-b))))
 a.ge(a.lin((1,M),(-1,a.const(m*b*(m-1)))),'point marginal lower bound')
 a.ge(a.lin((1,a.const(2*b*(2*m+1))),(-1,H)),'point entropy upper bound')
 debt=a.lin((F(1,2),M),(F(-1,2),H))
 ratio=a.lin((1/(n*d),debt));lower=F(n-7)+F(4,n)
 a.ge(a.lin((1,ratio),(-1,a.const(lower))),'actual minimal reset payment ratio diverges')
 if n==7:
  t=(-1,)+(1,)*127;p=a.stats(t)[0];c,R,pr,O,E,K,z=a.move(t,0,p)
  a.ck(pr==[F(1,2),F(1,2)],'source spectrum predicts fair')
  a.eq(O,{},'zero outcome cost');a.eq(E,{},'zero erasure credit')
  for k in K:a.eq(k,{},'actual inherited KL zero')
  a.eq(debt,a.lin(*[(F(1,2),a.stats(v)[4]) for v in c]),'direct physical children match closed reset formula')
 rows.append({'n':n,'expected_actual_reset_K':debt,'I':n*d,'ratio':ratio,'proved_lower_ratio':lower})
a.ck(time.perf_counter()-start<30,'frozen cap')
out={'status':'PASS','assertions':a.COUNT,'seconds':time.perf_counter()-start,'rows':rows,'all_n_proof':'PROOF.md section3; no finite inference to infinity'}
(ROOT/'out'/'POINT.json').write_text(json.dumps(a.serial(out),indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(a.serial(out)))
