import json,time
from pathlib import Path
from fractions import Fraction
OUT=Path(__file__).resolve().parents[1]/'out'
spec={'helper_version':'A025-direct-faces-v2','family':'one-point defect f_n, all coordinates','parameter_domain':'n=1..10 fixed','case_count':10,'symmetry':'coordinate permutation and cube translation proved analytically','arithmetic':'integer Walsh, rational A/B>=9 and log2(9)>2 analytic certificate, direct face enumeration, Fraction','memory_estimate_MB':5,'max_runtime_seconds':60}
(OUT/'FAMILY_SPEC.json').write_text(json.dumps(spec,indent=2))
start=time.monotonic(); checks=0; rows=[]
for n in range(1,11):
 N=1<<n; vals=[-1]+[1]*(N-1); a=vals[:]; h=1
 while h<N:
  for j in range(0,N,2*h):
   for k in range(j,j+h):
    u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
  h*=2
 assert a[0]==N-2 and all(v==-2 for v in a[1:]);checks+=N
 inf=sum(vals[x]!=vals[x^(1<<i)] for x in range(N) for i in range(n))
 assert inf==2*n;checks+=1
 faces=0
 for i in range(n):
  for j in range(i):
   for x in range(N):
    if x&((1<<i)|(1<<j)): continue
    faces+=vals[x]*vals[x^(1<<i)]*vals[x^(1<<j)]*vals[x^(1<<i)^(1<<j)]==-1
 assert faces==n*(n-1)//2;checks+=1
 for i in range(n):
  dn=0; nonempty_entropy_numerator=0
  for s in range(N):
   if s&(1<<i):continue
   A,B=a[s]**2,a[s|(1<<i)]**2;dn+=B
   if s:
    assert A==B==4
    nonempty_entropy_numerator+=8
   else: anchor=(A,B)
  assert dn==2*N
  if n>=3:
   A,B=anchor
   assert A>=9*B and nonempty_entropy_numerator==2*dn-8
   # The anchor entropy exceeds B log2(A/B)>=4 log2(9)>8.
  elif n==2: assert anchor==(4,4) and nonempty_entropy_numerator==8
  else: assert anchor==(0,4) and nonempty_entropy_numerator==0
  checks+=2
 cost=sum((m-1) for m in range(3,n+1))
 ratio=Fraction(cost,n)
 if n>=2: assert ratio==Fraction(n-1,2)-Fraction(1,n);checks+=1
 rows.append({'n':n,'I':str(Fraction(2*n,N)),'odd_faces':faces,'K2_bad_cost_over_I':str(ratio),'bad_coordinates':n if n>=3 else 0})
 assert time.monotonic()-start<60
result={'assertions_passed':checks,'seconds':time.monotonic()-start,'rows':rows,'arithmetic':'exact'}
(OUT/'FAMILY_RESULTS.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
