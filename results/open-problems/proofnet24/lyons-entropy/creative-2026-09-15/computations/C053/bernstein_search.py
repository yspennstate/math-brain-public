import json,numpy as np
from math import comb
from fractions import Fraction as F
from scipy.linalg import eigvalsh
raw=json.load(open('computations/C053/polynomial_data.json'));cc=np.array([[[float(F(v)) for v in row] for row in C] for C in raw['polynomial_coefficients']]);d=len(cc)-1
for count in [1,2,4,8,16,32,64]:
 worst=1e100;who=None
 for k in range(count):
  a=.25+.75*k/count;b=.25+.75*(k+1)/count
  dc=[sum(comb(k,j)*a**(k-j)*(b-a)**j*cc[k] for k in range(j,d+1)) for j in range(d+1)]
  for i in range(d+1):
   B=sum(comb(i,j)/comb(d,j)*dc[j] for j in range(i+1))
   ev=eigvalsh(B)[0]
   if ev<worst:worst=ev;who=(k,i)
 print(count,worst,who,flush=True)
 if worst>0:break
