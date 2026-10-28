from pathlib import Path
from fractions import Fraction as Q
import json,time,hashlib
import exact as e
import check as c
ROOT=Path(__file__).resolve().parents[1]
spec={'helper_version':'boundary.py v1 and inherited exact.py P180','actual_Boolean_family':'AND_n, n2..64; product of256 AND4 factors in m4 source, no huge truth table','domain':'63 compressed exact Fourier laws; direct Fourier/character controls n2,3,4; fixed N256 tensor certificate','case_count':63,'symmetry':'compressed equal nonempty Fourier masses proved by direct summation; no sampling','arithmetic':'Fraction, exact outward log intervals2^-180; factor identities proved in PROOF Section5','memory_estimate_MB':30,'max_runtime_seconds':55,'automatic_dimension_escalation':False}
(ROOT/'BOUNDARY_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8',newline='')
start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x;checks+=1
def ah(n):
 p=Q(1,1<<n)
 return e.add(e.eta((1-2*p)**2),c.rational(8*p*(1-p)*(n-1)))
rows=[]
for n in range(2,65):
 p=Q(1,1<<n);iv=ah(n);inf=2*n*p
 ck(iv[0]>=c.rational(8*p*(1-p)*(n-1))[0])
 if n<=4:
  g=tuple(-1 if x==0 else 1 for x in range(1<<n));ck(c.overlap(iv,e.H(g)));ck(e.direct(g)==e.fwht(g));ck(c.I(g)==inf)
 rows.append({'n':n,'H_over_I':e.serial(e.times(iv,1/inf))})
full=e.times(ah(4),16)
budget_hi=e.add(c.rational(7),e.times(c.rational(c.kap()[1]),8))
deficit=e.add(full,e.neg(budget_hi));ck(deficit[0]>0)
old=e.times(e.add(ah(4),e.neg(e.times(ah(3),Q(1,2)))),Q(1,16));ck(old[0]>0)
ck(e.bits(deficit)[0]>Q(12,5))
result={'status':'PASS','checks':checks,'elapsed_s':time.perf_counter()-start,'complete_core_factors':256,'core_dimension':1024,'full_core_debit':e.serial(full),'entire_original_two_owner_budget_upper':e.serial(budget_hi),'deficit':e.serial(deficit),'first_actual_old_debit':e.serial(old),'AND_ratios':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
ck(result['elapsed_s']<55);result['checks']=checks
(ROOT/'out/CHECK_boundary.json').write_text(json.dumps(result,indent=2),encoding='utf-8',newline='')
print(json.dumps({k:result[k] for k in ['status','checks','elapsed_s','deficit','first_actual_old_debit']}))
