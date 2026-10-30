from pathlib import Path
from fractions import Fraction as F
import math,json,time
import exact_arithmetic as a
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();rows=[];checks=0
for m in [4,8,12,16,24,32]:
 M=math.comb(2*m,m);t=F(1,1<<m)
 assert M*(2*m+1)>=4**m;checks+=1
 def scale(iv,c):return tuple(sorted((iv[0]*c,iv[1]*c)))
 def add(*ivs):return sum(x[0] for x in ivs),sum(x[1] for x in ivs)
 U=scale(a.logiv(1+M*t/(1-t)),1-t)
 lower=scale(add((F(m),F(m)),scale(a.logiv(F(2*m+1)),-1)),1-t)
 iv=add(U,scale(lower,-1));assert iv[0]>0;checks+=1
 def eta(q):return scale(a.logiv(q),-q) if q else (F(0),F(0))
 Hdiff=add(eta(t),eta(1-t),scale(a.logiv(F(M)),-t))
 assert M*(1-t)>1;checks+=1
 lo,hi=U;eh=Hdiff
 scale=1<<160
 pack=lambda v:[v[0].numerator*scale//v[0].denominator,-((-v[1].numerator*scale)//v[1].denominator)]
 rows.append({'m':m,'N':2*m,'M':M,'tau':str(t),'U_interval_2pow160':pack((lo,hi)),'entropy_difference_interval_2pow160':pack(eh),'U_display_only':[float(lo),float(hi)]})
out={'status':'PASS','assertions':checks,'normalization':'exact probability laws; REAL functions, not Boolean','all_real_tau_domain':'[0,1/16] by closed formula and continuous zero face','cases':rows,'runtime_seconds':time.perf_counter()-start}
(R/'out/GU_GUARD.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
