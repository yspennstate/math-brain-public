from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import time,json
import kernel as k
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();k.CAP=50;checks=0;records=[]
for w,t in ((1,3),(2,2),(2,3),(3,2)):
 n=w*t;N=1<<n;vals=[1 if all(((x>>(w*j))&((1<<w)-1))!=0 for j in range(t)) else -1 for x in range(N)]
 f=k.fwht(vals);q=Q(1,1<<w);s=1-q;e=2*q*s**(t-1);c=2*s**t-1
 for i in range(n):
  group=defaultdict(lambda:[Q(0),Q(0)]);ratios={};block=i//w;mask=((1<<w)-1)<<(block*w);mask^=1<<i
  for T in range(N):
   if T&(1<<i):continue
   z=0 if not T else 2 if T&mask else 1
   u=Q(f[T^(1<<i)]**2,N*N)/e;r=Q(f[T]**2+f[T^(1<<i)]**2,N*N)
   group[z][0]+=u;group[z][1]+=r
   if u:
    if z in ratios:assert ratios[z]==u/r
    ratios[z]=u/r;checks+=1
  mu=[e,2*q-e,1-2*q];rr=[c*c+e*e,e*(2*q-e)*(s*s+q*q)/(q*q),2*e*(1-2*q)]
  assert all(group[z]==[mu[z],rr[z]] for z in range(3));checks+=3
  assert sum(mu)==sum(rr)==1;checks+=2
 records.append(dict(w=w,t=t,n=n,coordinate_rows=n,mu=[str(x) for x in mu],r=[str(x) for x in rr]))
assert Q(1)+Q(6*4,16)==Q(5,2) and Q(5,2)<6;checks+=2
out=dict(helper_version='A035-tribes-interface-review-v1',runtime_seconds=time.perf_counter()-start,roots=4,coordinate_rows=19,checks=checks,records=records,normalized_non_Boolean_control=dict(d='1/64',full_row_KL='0',Lambda_over_I='6',violates_claimed_5_over_2=True),status='PASS at reviewed scope')
(ROOT/'out'/'tribes_review.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps({a:b for a,b in out.items() if a!='records'}))
