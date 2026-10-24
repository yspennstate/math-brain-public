import json
from fractions import Fraction as F
from math import comb
from pathlib import Path
raw=json.load(open('computations/C053/polynomial_data.json'));cc=[[[F(v) for v in row] for row in C] for C in raw['polynomial_coefficients']];d=len(cc)-1;n=10
# Prove the quantitative -H'' >= ||A||_F^2 (complex Hermitian).
for k,z in enumerate(raw['Z_coefficients']):
 for i in range(n):cc[k+2][i][i]-=F(z)*(1 if i<4 else 2)
a=F(1,4);b=F(1);width=b-a
weights=[]
for i in range(d+1):
 weights.append([sum(F(comb(i,j),comb(d,j))*comb(k,j)*a**(k-j)*width**j for j in range(min(i,k)+1)) for k in range(d+1)])
def ldl(M):
 N=len(M);L=[[F(int(i==j)) for j in range(N)] for i in range(N)];D=[]
 for i in range(N):
  pivot=M[i][i]-sum(L[i][k]**2*D[k] for k in range(i));assert pivot>0,(i,str(pivot));D.append(pivot)
  for j in range(i+1,N):L[j][i]=(M[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/pivot
 return L,D
saved=[]
for i in range(d+1):
 B=[[sum(weights[i][k]*cc[k][r][c] for k in range(d+1)) for c in range(n)] for r in range(n)]
 L,D=ldl(B)
 # Readable integer lower bounds, all comparisons exact.
 floors=[q.numerator//q.denominator for q in D]
 assert min(floors)>0
 print(i,'pivot floors',floors,flush=True)
 saved.append({'index':i,'matrix':[[str(v) for v in row] for row in B],'L':[[str(v) for v in row] for row in L],'D':list(map(str,D)),'integer_lower_bounds':floors})
Path('computations/C053/bernstein_certificate.json').write_text(json.dumps({'interval':['1/4','1'],'degree':d,'strong_hessian_constant':'1','coefficients':saved},indent=2))
print('PASS: all 11 rational Bernstein matrices positive definite; uniform full-Hermitian bound',flush=True)
