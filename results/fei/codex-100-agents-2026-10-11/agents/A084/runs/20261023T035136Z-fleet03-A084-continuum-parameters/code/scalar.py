from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,time
r=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=cases=zeroT=zeroA=0
def ck(p):
 global checks
 assert p;checks+=1
for w in [F(0),F(1,8),F(1,2),F(7,8),F(1)]:
 weights=[w,1-w];support=[i for i in range(2) if weights[i]]
 def avg(xs):return sum(weights[i]*xs[i] for i in support)
 for ss in product([-2,0,2],repeat=2):
  for extra in product([0,1],repeat=2):
   R=[max(F(0),-F(s))+x for s,x in zip(ss,extra)];need=avg(R)
   for b in [0,1]:
    a=need+b;D=a;e=avg(ss);credit=[x+a-need for x in R];debit=[F(s)+x for s,x in zip(ss,credit)];T=D+e
    ck(avg(credit)==a and avg(debit)==T and T>=0)
    ck(all(credit[i]>=R[i] and debit[i]>=0 for i in support))
    if T:kernel=[debit[i]/T for i in range(2)]
    else:
     zeroT+=1;ck(all(debit[i]==0 for i in support));kernel=[F(1),F(1)]
    ck(avg(kernel)==1)
    labels=[D+1,F(-1),e];sent=[[L*k for L in labels] for k in kernel]
    for k,L in enumerate(labels):ck(avg([ls[k] for ls in sent])==L)
    for i in support:ck(sum(sent[i])==debit[i])
    if a:
     credit_kernel=[x/a for x in credit]
     for owner in [a/3,2*a/3]:ck(avg([owner*k for k in credit_kernel])==owner)
    else:zeroA+=1;ck(all(credit[i]==0 for i in support))
    # A real extra initial shift remains the SAME shift after allocation.
    shift=F(7,11);ck(all(R[i]+a+shift-need==credit[i]+shift for i in support))
    cases+=1
ck(cases==360)
# Failure controls for hypotheses omitted by a proposed simplification.
ck(F(-1)*2+F(2)*1==0 and 2!=0) # negative weights invalidate zero-mean nonnegative absorption
ck((F(1,4)+F(1,4))*2!=2)       # unnormalized weights do not preserve constant credit
ck(max(0,-F(-1))==1)           # stop option cannot be omitted
out=dict(cases=cases,exact_assertions=checks,zero_total_debit_cases=zeroT,zero_credit_cases=zeroA,runtime_seconds=time.perf_counter()-start,scope='Finite boundary controls; all-real weight/credit coverage is the algebraic proof, not this grid.')
ck(out['runtime_seconds']<55)
(r/'out/SCALAR_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
