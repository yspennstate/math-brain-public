import check as C
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,time

start=time.perf_counter();rows=[]
for m in [1,2,3,4]:
    for k in [8,32,128]:
        e=F(1,k*m);n=m+2;ps=[F(1,2)]*2+[e]*m
        table=[1 if x.bit_count()>=2 else -1 for x in range(1<<n)]
        cs,P,vs=C.spectrum(table,ps)
        C.check(sum(P)==1)
        q0=(1-e)**m;q1=m*e*(1-e)**(m-1)
        C.check(cs[1]==(q0+q1)/2 and cs[3]==(q0-q1)/2)
        delta=sum((F(s.bit_count()-1)*p for s,p in enumerate(P) if s),F(0))
        R=sum((F(s.bit_count()-2)*p for s,p in enumerate(P) if s.bit_count()>=3),F(0))
        j1=F(0);jh=F(0);lo=F(0);hi=F(0)
        for s,c in enumerate(cs):
            if not s or not c:continue
            j,u=C.scale(c)
            if s.bit_count()==1:
                j1+=P[s]*j;a,b=C.log_interval(1/u);lo+=P[s]*a;hi+=P[s]*b
            else:jh+=P[s]*j
        dlo=2*delta-j1-hi;dhi=2*delta-j1-lo
        C.check(dlo>0 and dlo>=R and dhi<=5*m*e)
        C.check(jh>=F(9,64) and jh>=F(9,320*m)/e*dhi)
        C.prime_rows(table,n)
        rows.append({'m':m,'epsilon':str(e),'ratio_lower':str(F(9,320*m)/e)})
        assert time.perf_counter()-start<55
result={'status':'PASS','cases':len(rows),'checks':C.checks,'runtime_seconds':time.perf_counter()-start,'rows':rows}
(C.ROOT/'out/A045_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
