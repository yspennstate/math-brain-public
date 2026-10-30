import check as C
from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
def run(n):
 d=F(1,2**n);N=n+1;e=(1-d)**2/4;z=1-e
 def g(c):return 1-c-(1-c/(2*z))**2*(1-c*d/(2*z))**N
 lo,hi=F(0),F(1)
 for _ in range(60):
  mid=(lo+hi)/2
  if g(mid)>0:lo=mid
  else:hi=mid
 C.ck(lo>0 and g(lo)>0 and g(hi)<0)
 c=(lo,hi);u=C.div(c,C.iv(2*z));t=C.scale(d,u)
 one=C.iv(1);w=one;wm=one
 for _ in range(N):w=C.mul(w,C.sub(one,t))
 for _ in range(N-1):wm=C.mul(wm,C.sub(one,t))
 E=C.add(C.iv(e),C.scale(F(1,2),C.mul(C.sub(one,u),w)));X=C.scale(F(1,2),w)
 k=(1-d/2)**2/((1-d/2)**2+d*d/4)
 out0=C.add(C.iv(F(1,2)),C.scale(k-F(1,2),C.sub(E,X)));out1=C.sub(one,out0)
 B0=C.scale(d/2,C.mul(C.sub(one,u),wm));B1=C.scale(F(1,2),C.mul(t,wm))
 heavies=[C.div(C.add(C.scale(k,E),C.scale(F(1,2),B0)),out0),C.div(C.add(C.scale(k,X),C.scale(F(1,2),B1)),out1)]
 ka=(1-d)**2/(1+(1-d)**2)
 active=[C.sub(one,C.scale(1-ka,x)) for x in heavies]
 def O(p):return C.scale(F(-1,2),C.log(C.scale(4,C.mul(p,C.sub(one,p)))))
 outcome=C.add(O(out0),C.scale(F(1,2),C.total(O(a) for a in active)))
 HM=C.add(C.h(C.iv(z)),C.mul(C.div(C.iv(z),c),C.sub(C.add(C.scale(2,C.h(u)),C.scale(N,C.h(t))),C.h(c))))
 D=C.sub(C.add(C.add(outcome,C.scale(F(N,2),C.h(C.iv(d)))),C.iv(2)),HM)
 C.ck(D[1]<0)
 return {'n':n,'c':C.enc(c),'outcome_normalizers':[C.enc(out0),C.enc(out1)]+[C.enc(x) for x in active],'O_total':C.enc(outcome),'HM':C.enc(HM),'D_end':C.enc(D)}
start=time.perf_counter();table=json.loads((R/'out/CHECK.json').read_text())['results'];out=[]
for n in range(2,16):
 r=run(n);out.append(r)
 if n<=7:
  q=table[n-2]
  for a,b in [(r['D_end'],q['D_end']),(r['O_total'],q['outcome_KL_total'])]:
   C.ck(F(a[0])<=F(b[1]) and F(b[0])<=F(a[1]))
 C.logpoint.cache_clear()
 (R/'out/FORMULA_CHECK.json').write_text(json.dumps({'results':out,'checks':C.checks,'runtime_seconds':time.perf_counter()-start},indent=2),encoding='utf-8')
C.ck(1200*17<2**16);C.ck(6*17*10<2**16);C.ck(9>8)
C.ck(-F(3,10)+F(9,25)*F(17,2**16)<-F(1,4))
C.ck(F(1,25)-F(2,5)*F(1,2**16)>0)
C.ck(C.LN2[0]>F(2,3));C.ck(time.perf_counter()-start<60)
(R/'out/FORMULA_CHECK.json').write_text(json.dumps({'results':out,'checks':C.checks,'runtime_seconds':time.perf_counter()-start,'all_negative':True,'analytic_constant_checks':'PASS'},indent=2),encoding='utf-8')
print(json.dumps({'all_D_negative':True,'finite_bases':14,'checks':C.checks,'runtime_seconds':time.perf_counter()-start}))
