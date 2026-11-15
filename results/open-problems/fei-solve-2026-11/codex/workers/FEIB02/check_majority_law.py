from fractions import Fraction as F
from math import comb
from symmetric import integer_data
import json,mpmath as mp
checks=0
for m in range(1,41):
 n=2*m+1;f=[1 if t<=m else -1 for t in range(n+1)];rows=integer_data(f)
 I=F(n*comb(2*m,m),4**m)
 qs=[]
 for j in range(2*m+1):
  actual=F((j+1)*comb(n,j+1)*rows[j+1][0]**2,2**(2*n))/I
  expected=F(comb(j,j//2)*comb(2*m-j,m-j//2),4**m) if j%2==0 else F(0)
  assert actual==expected;(qs.append(actual));checks+=1
 assert sum(qs)==1
mp.mp.dps=80
print(json.dumps({'exact_derivative_level_weights_checked':checks,'m_range':[1,40],'limit_A_AND':'3','limit_B_majority':str(2/mp.log(2)),'limit_Gamma_majority':str(1/mp.log(2)),'Theorem1_uniform_coefficient_floor':str(2+4/mp.log(2))},indent=2))
