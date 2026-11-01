"""Exact counterexample to R(U)>=0, not to Sidorenko (standard library)."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

p=[F(1,3),F(2,3)]
W=[[F(4,5),F(11,10)],[F(11,10),F(19,20)]]
lam=-F(1,10); z=F(1,2)
assert all(sum(p[j]*W[i][j] for j in range(2))==1 for i in range(2))
assert all(W[i][j]==W[j][i]>0 for i,j in product(range(2),repeat=2))
assert max(abs(x-1) for row in W for x in row)==F(1,5)
# f=(2,-1)/sqrt(2), E f=0, E f^2=1, (E f^3)^2=1/2.
f=[F(2),F(-1)]
assert sum(p[i]*f[i] for i in range(2))==0
assert sum(p[i]*f[i]**2 for i in range(2))==2
assert sum(p[i]*f[i]**3 for i in range(2))**2/8==z
assert all(W[i][j]==1+lam*f[i]*f[j]/2 for i,j in product(range(2),repeat=2))
C={(i,j,k):sum(p[u]*W[u][i]*W[u][j]*W[u][k] for u in range(2))
   for i,j,k in product(range(2),repeat=3)}
t=F(0)
for x in product(range(2),repeat=5):
    term=F(1)
    for i in range(5):term*=p[x[i]]*C[x[i],x[(i+1)%5],x[(i+2)%5]]
    t+=term
A=lam**6+z*lam**7
Pplus=(5*A+10*z*(lam**8+lam**9)+25*lam**8+8*lam**10
       +5*lam**8+5*lam**4*A+70*z*lam**10)
R=t-1-5*lam**4-10*lam**6-Pplus
Rpoly=(50*z*lam**9+15*z*z*lam**10+(90*z+60*z*z)*lam**11
       +(145*z*z+10*z**3)*lam**12+75*z**3*lam**13
       +15*z**4*lam**14+z**5*lam**15)
assert R==Rpoly==F(-806029701,32000000000000000)<0
assert t==F(32016482386770299,32000000000000000)>1
assert Pplus==F(203991,40000000000)>0
assert Pplus+R>0
out={'status':'ALL_EXACT_CHECKS_PASS','refuted_claim':'R(U)>=0 for every nonnegative regular W',
     'weights':list(map(str,p)),'W':[[str(v) for v in row] for row in W],
     'nonconstant_eigenvalue':str(lam),'squared_third_moment':str(z),
     'R':str(R),'P_plus':str(Pplus),'P_plus_plus_R':str(Pplus+R),'density':str(t),
     'Sidorenko_counterexample':False,'full_proof':False}
text=json.dumps(out,indent=2)+'\n'
Path(__file__).with_name('residual_checks.json').write_text(text)
print(text,end='')
