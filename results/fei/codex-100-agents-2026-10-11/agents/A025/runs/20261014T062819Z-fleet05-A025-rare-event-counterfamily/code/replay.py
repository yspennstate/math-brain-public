from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import json,time
P=Path(__file__).resolve().parents[1];start=time.monotonic();CK=0;S=1<<104
def check(v):
 global CK
 assert v;CK+=1
 if time.monotonic()-start>60:raise TimeoutError('frozen60 cap')
def ln(t):
 z=(t-1)/(t+1);p=z;a=Q(0)
 for j in range(44):a+=2*p/(2*j+1);p*=z*z
 return a,a+2*p/(89*(1-z*z))
L2=ln(Q(2))
@lru_cache(None)
def lg(n):
 k=n.bit_length()-1
 if n==1<<k:return k*S,k*S
 a,b=ln(Q(n,1<<k));lo=(k+a/L2[1])*S;hi=(k+b/L2[0])*S
 return lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)
src=json.loads((P/'out/RESULTS.json').read_text());count=0
for cert in src['certificates']:
 lo=hi=0
 for n,c in cert['terms']:
  n=int(n);c=int(c);a,b=lg(n);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 check(not cert['terms'] or lo>0 or hi<0);sgn=0 if not cert['terms'] else (1 if lo>0 else -1);check(sgn==cert['sign']);count+=1
pis=[(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1)),(Q(1,2),Q(1,4),Q(1,4)),(Q(1,4),Q(1,2),Q(1,4)),(Q(3,4),Q(1,8),Q(1,8))]
profiles=0
for r in product((0,1),repeat=3):
 for p0,p1 in product(pis,repeat=2):
  p=tuple((a+b)/2 for a,b in zip(p0,p1));q=sum(a*b for a,b in zip(p,r));q0=sum(a*b for a,b in zip(p0,r));q1=sum(a*b for a,b in zip(p1,r))
  pair=2*sum(p[i]*p[j]*(r[i]!=r[j]) for i in range(3) for j in range(i+1,3));check(pair==2*q*(1-q));check(pair-(q0*(1-q0)+q1*(1-q1))==(q0-q1)**2/2);profiles+=1
# Annotate activation banks correctly: newly introduced V directions
# remain in both x children and have ZERO release, not zero capacity.
for row in src['rows']:
 m,t=row['m'],row['t'];a=Q(1,1<<t);delta=Q(1,1<<m)
 row['original_root_bank']=row.pop('root_bank');row['original_remaining_expected_bank']=row.pop('remaining_expected_bank')
 row['activated_root_bank']=str(a*(3*m+2+3*t)*delta/4);row['activated_remaining_expected_bank']=str(a*(3*m-1+3*t)*delta/4)
 check(Q(row['activated_root_bank'])-Q(row['activated_remaining_expected_bank'])==a*3*delta/4)
write={'status':'PASS','certificates_replayed':count,'edge_profile_cases':profiles,'assertions':CK,'seconds':time.monotonic()-start,'activation_bank_correction':'explicit V-direction capacity retained; x release unchanged','annotated_rows':src['rows']}
(P/'out/REPLAY_RESULTS.json').write_text(json.dumps(write,indent=2));print(json.dumps({k:v for k,v in write.items() if k!='annotated_rows'}))
