from fractions import Fraction as F
from math import isqrt
import json,pathlib
raw=json.loads(pathlib.Path('second_counterexample_search.json').read_text())['found']
for den in [100,1000,10000,100000,1000000]:
 a=[[F(round(x*den),den) for x in row] for row in raw['source']];b=[[F(round(x*den),den) for x in row] for row in raw['target']]
 d=[[b[j][0]-a[i][0] for j in range(2)] for i in range(2)];h=[[b[j][1]-a[i][1] for j in range(2)] for i in range(2)]
 q=[[h[i][j]**2/(2*d[i][j]) for j in range(2)] for i in range(2)];dq=q[0][0]+q[1][1]-q[0][1]-q[1][0]
 sq=[[d[i][j]**2+h[i][j]**2 for j in range(2)] for i in range(2)]
 K=10**9;bounds=[]
 for i,j in [(0,0),(1,1),(0,1),(1,0)]:
  v=sq[i][j];k=isqrt(v.numerator*K*K//v.denominator);assert k*k*v.denominator<=v.numerator*K*K<(k+1)*(k+1)*v.denominator;bounds.append((k,k+1))
 diagupper=F(bounds[0][1]+bounds[1][1],K);offlower=F(bounds[2][0]+bounds[3][0],K)
 if dq>0 and diagupper<offlower:
  result={'denominator':den,'source':[[str(x) for x in row] for row in a],'target':[[str(x) for x in row] for row in b],'squared_distances_diag_then_off':[str(sq[i][j]) for i,j in [(0,0),(1,1),(0,1),(1,0)]],'sqrt_bounds_numerators':bounds,'scale':K,'quadratic_diagonal_minus_off':str(dq),'euclidean_diagonal_upper':str(diagupper),'euclidean_off_lower':str(offlower)}
  pathlib.Path('second_exact_counterexample.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));break
else:raise RuntimeError('No rational certificate')
