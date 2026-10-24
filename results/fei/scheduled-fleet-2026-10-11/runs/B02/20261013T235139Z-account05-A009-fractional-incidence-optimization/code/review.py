import json, math, time
from fractions import Fraction as F
from pathlib import Path
def comps(c,s):
    if s==1: yield (c,); return
    for j in range(c+1):
        for tail in comps(c-j,s-1): yield (j,)+tail
start=time.perf_counter(); count=checks=0
for s in range(1,5):
    for c in range(7):
        for h in comps(c,s):
            count+=1; M=math.prod(math.factorial(j) for j in h)
            Ns=F(M,(c+1)*(c+2)*math.comb(s+c-1,c))
            moments=F(2,(c+1)*(c+2))*math.factorial(c)*F(math.factorial(s-1)*M,math.factorial(s+c-1))
            assert moments/2==Ns; checks+=1
            assert F(M,2**(s+1+c)*3**c)<=Ns<=F(M,2); checks+=1
            assert (c+1)*(c+2)<=2*3**c; checks+=1
            assert math.comb(s+c-1,c)<=2**(s+c); checks+=1
result={'vectors':count,'checks':checks,'all_passed':True,'elapsed_seconds':time.perf_counter()-start,'scope':'operator moments and inequalities; all-finite proof analytic in REVIEW_A008.md'}
(Path(__file__).resolve().parents[1]/'out'/'REVIEW_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
