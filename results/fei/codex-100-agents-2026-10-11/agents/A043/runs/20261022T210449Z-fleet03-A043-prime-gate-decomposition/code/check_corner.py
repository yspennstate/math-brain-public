"""One predeclared exact prime56067 law; no logarithms or subprocesses."""
from fractions import Fraction as Q
from pathlib import Path
import json,time,hashlib
from itertools import combinations
R=Path(__file__).resolve().parents[1];o=R/'out'
spec={'helper':'A043-fixed-order-corner-v1','family':'reflected actual Boolean prime56067','domain':'t=1/1024; (alpha,e,d,q)=(t,t^2,t^4,t); m=0,1,2,4,8,16,32',
 'case_count':1,'symmetry':'none','arithmetic':'exact Fraction derivatives and polynomial reserves, no logarithms','memory_estimate_mb':30,'max_runtime_seconds':55}
(o/'corner_frozen_spec.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.perf_counter();t=Q(1,1024);p=[t,t*t,t**4,t];v=[4*x*(1-x) for x in p]
values=[]
for i in range(16):
 a,x,y,z=[(i>>j)&1 for j in range(4)]
 values.append(-1+2*z+2*x*y-2*z*(a*x+(1-a)*y))
assert all(x in (-1,1) for x in values)
assert all(values[i]==(1 if (56067>>(i^6))&1 else -1) for i in range(16))
prime_rows=[]
for size in (2,3):
 for B in combinations(range(4),size):
  C=[j for j in range(4) if j not in B]
  rows={tuple(values[sum(((x>>j)&1)<<B[j] for j in range(size))+sum(((z>>j)&1)<<C[j] for j in range(len(C)))] for z in range(1<<len(C))) for x in range(1<<size)}
  assert len(rows)>2
  prime_rows.append({'block':list(B),'rows':len(rows)})
def prod(xs):
 a=Q(1)
 for x in xs:a*=x
 return a
c=[];d=[];checks=2+len(prime_rows)
for j in range(4):
 mean=second=Q(0)
 for x in range(16):
  if x>>j&1:continue
  wt=prod(p[k] if x>>k&1 else 1-p[k] for k in range(4) if k!=j)
  diff=Q(values[x|(1<<j)]-values[x],2)
  mean+=wt*diff;second+=wt*diff*diff
 c.append(abs(mean));d.append(second)
expected_c=[t**3*(1-t*t),t*t*(1-t*t),t*(1-2*t),1-t**3-t**4+t**5]
expected_d=[t**3+t**5-2*t**7,t*t+t**4-2*t**6,t-2*t**3+2*t**4,expected_c[3]]
assert c==expected_c and d==expected_d;checks+=2
T=v[0]*v[3]*(v[1]+v[2])/16
assert T==4*t**4*(1-t)**2*(1-t**6)>0;checks+=1
gaps={}
for m in (0,1,2,4,8,16,32):
 S=sum((v[j]*(2*(d[j]-c[j])+c[j]*(1-c[j])*sum((Q(2,k*(k+1))*(1-c[j])**k for k in range(1,m+1)),Q(0))) for j in range(4)),Q(0))
 gap=(S-4*T)/T
 assert gap<0;checks+=1;gaps[str(m)]=str(gap)
assert time.perf_counter()-start<55
result={'status':'PASS','assertions':checks,'case_count':1,'gaps_over_T':gaps,'T':str(T),'prime_block_rows':prime_rows,'runtime_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'one exact interior fixture for seven fixed orders; all-fixed-m obstruction is the analytic limit in PROOF.md'}
(o/'corner_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='gaps_over_T'}))
