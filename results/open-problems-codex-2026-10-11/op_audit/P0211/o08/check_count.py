from fractions import Fraction as F
import json, math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
identities=0
for n in range(2,31):
 for beta in (F(1,n),F(1,n*n),F(7,3)):
  Q=[[F(0) for j in range(n)] for i in range(n)]
  A=[[F(0) for j in range(n-1)] for i in range(n-1)]
  D=[[F(int(j==i+1)-int(j==i)) for j in range(n)] for i in range(n-1)]
  for i in range(n):
   k=i+1
   if i<n-1: Q[i][i+1]=beta*(n-k)
   if i: Q[i][i-1]=F(k*(k-1),n)
   Q[i][i]=-sum(Q[i])
  for i in range(n-1):
   k=i+1
   if i<n-2: A[i][i+1]=beta*(n-k-1)
   if i: A[i][i-1]=F(k*(k-1),n)
   A[i][i]=-sum(A[i])-beta-F(2*k,n)
  # DQ has row Q[i+1]-Q[i]; AD uses the two nonzero entries per D row.
  for i in range(n-1):
   for j in range(n):
    rhs=(A[i][j-1] if j>0 else F(0))-(A[i][j] if j<n-1 else F(0))
    assert Q[i+1][j]-Q[i][j]==rhs
  identities+=1
upper_cases=0; combination_cases=0
for n in (2,3,7,8,9,16,100,1000,10000):
 for beta in np.geomspace(1e-16,1e8,49):
  a=max(1,n*math.sqrt(beta)); k=np.arange(1,n,dtype=float)
  cert=2*beta*(n-k-1)/(k+a+2)+beta+2*k*a/(n*(k+a-1))
  bound=beta+4*max(math.sqrt(beta),1/n)
  assert np.all(cert<=bound*(1+1e-13)); upper_cases+=len(k)
  s=beta+math.sqrt(beta)+1/n
  lower=beta+2/n
  if n>=8 and 4/n**2<=beta<=1/16: lower=max(lower,math.sqrt(beta)/5)
  assert lower>=s/6*(1-1e-13); combination_cases+=1
report={'exact_gradient_matrix_identities':identities,'upper_pointwise_certificate_cases':upper_cases,'combination_parameter_cases':combination_cases,'all_passed':True}
(ROOT/'count_results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
