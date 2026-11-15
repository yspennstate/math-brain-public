from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
ncell=[3,5,7,9]; n=sum(ncell); sigma=F(1,2)
z=[-1,-1,1,1]; C=[[F(2*int(i==j)+1+z[i]*z[j],32) for j in range(4)] for i in range(4)]
D=[F(4*v,n) for v in ncell]; gamma=F(1,2); delta=max(abs(v-1) for v in D)
I=[[F(i==j) for j in range(4)] for i in range(4)]
matvec=lambda A,x:[sum((a*b for a,b in zip(row,x)),F(0)) for row in A]
matmul=lambda A,B:[[sum((A[i][l]*B[l][j] for l in range(4)),F(0)) for j in range(4)] for i in range(4)]
add=lambda x,y:[a+b for a,b in zip(x,y)]
sub=lambda x,y:[a-b for a,b in zip(x,y)]
scale=lambda a,x:[a*v for v in x]
norm2=lambda x:sum((v*v for v in x),F(0))
A=[[I[i][j]-gamma*C[i][j] for j in range(4)] for i in range(4)]
AD=[[I[i][j]-gamma*C[i][j]*D[j] for j in range(4)] for i in range(4)]
assert any(C[i][j]*D[j]!=D[i]*C[i][j] for i in range(4) for j in range(4))
labels=[[F(i-1,8)+sigma*(1 if j%2==0 else -1) for j in range(v)] for i,v in enumerate(ncell)]
y=[sum(row,F(0))/len(row) for row in labels]
rI=scale(-1,y); rD=scale(-1,y); history=[]; H=F(0); identity_cases=0
for k in range(1,13):
 history.append(rD[:]); rI=matvec(A,rI);rD=matvec(AD,rD);d=sub(rD,rI)
 rhs=[F(0)]*4;power=I
 for prev in reversed(history):
  forcing=matvec(C,[(D[i]-1)*prev[i] for i in range(4)])
  rhs=sub(rhs,scale(gamma,matvec(power,forcing)))
  power=matmul(power,A)
 assert d==rhs
 H+=F(1,k)
 assert norm2(d)<=4*delta*delta*H*H*norm2(y)
 for i in range(4):
  empirical=sum((rD[i]+y[i]-v for v in labels[i]),F(0))/n
  collapsed=F(ncell[i],n)*rD[i]
  assert empirical==collapsed
 assert sum(D[i]*rD[i]**2 for i in range(4))<=sum(D[i]*y[i]**2 for i in range(4))
 identity_cases+=1
spectral_cases=0
for a in [F(1,32),F(3,32)]:
 for l in range(32):
  assert a*(1-a)**l<=F(1,l+1)
  spectral_cases+=1
patterns=0
for count in ncell:
 values=[sigma*sum(signs)/count for signs in product([-1,1],repeat=count)]
 assert sum(values,F(0))==0
 assert sum((x*x for x in values),F(0))/len(values)==sigma*sigma/count
 patterns+=len(values)
out={'noncommuting_duhamel_identity_steps':identity_cases,'cell_gradient_entries':48,'harmonic_spectral_cases':spectral_cases,'cell_noise_patterns':patterns,'max_cell_count':9,'scope':'Exact finite rational identities only. Does not certify general operator inequalities, count concentration, weighted nonlinear transfer, peak limits or novelty.'}
with (Path(__file__).resolve().parent.parent/'logs/iid_fixed_noise_algebra_checks.json').open('w',encoding='utf-8',newline='') as f:json.dump(out,f,indent=2)
print(json.dumps(out))
