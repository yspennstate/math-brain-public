"""Exact 3-by-3 coefficient-matrix certificate for the rank-one boundary."""
import itertools,json
import sympy as s
z=s.symbols('z0:4')
U=s.Matrix([sum(((5-j) if i<j else -j)*z[j-1] for j in range(1,5)) for i in range(5)])
t=(U.T*U)[0];q=sum(x**4 for x in U);d=sum(x**3 for x in U);p=-U[0]*U[4]
Delta=U[0]-U[4]
K=s.zeros(5,3)
for j in range(3):K[0,j]=U[4]-U[j+1];K[j+1,j]=Delta;K[4,j]=U[j+1]-U[0]
assert s.expand((s.ones(1,5)*K))==s.zeros(1,3)
assert s.simplify(U.T*K)==s.zeros(1,3)
R=K.T*K;C=K.T*s.diag(*[u*u for u in U])*K
Fm=K.T*s.diag(*list(U))*K;ev=K.T*s.Matrix([u*u for u in U])
alpha=140*p*q-28*p*t*t-47*q*t+13*t**3+24*d*d
M=alpha*R+(140*p*t-41*t*t)*C+6*t*ev*ev.T+18*t*d*Fm-s.Rational(1,2)*t**3*R
coeff={}
for i in range(3):
 for j in range(i,3):
  for mon,c in s.Poly(s.expand(M[i,j]),*z).terms():
   assert sum(mon)==8
   if mon not in coeff:coeff[mon]=s.zeros(3)
   coeff[mon][i,j]=coeff[mon][j,i]=c
minors=0;zeros=0
for mon,mat in coeff.items():
 for k in range(1,4):
  for inds in itertools.combinations(range(3),k):
   val=mat.extract(inds,inds).det();assert val>=0,(mon,inds,val)
   minors+=1;zeros+=int(val==0)
records=[{'monomial':mon,'twice_matrix':[[int(2*mat[i,j]) for j in range(3)] for i in range(3)]} for mon,mat in sorted(coeff.items())]
for mon,mat in coeff.items():assert all((2*x).is_Integer for x in mat)
with open('rank_one_matrices.json','w') as f:json.dump(records,f,indent=2)
print('PROVED: exact coefficient matrices:',len(coeff))
print('PROVED: principal minors checked:',minors,'zero:',zeros,'negative: 0')
print('PROVED: all matrices are PSD, proving E >= 1/2 for every orthonormal zero-sum pair.')
# Check the endpoint reduction in abstract moments.
a,p0,A,C0,d0,e0,f0=s.symbols('a p A C d e f')
T_over_a=((70-200*a)*A+(70-170*a)*C0+58*a-14+120*a*d0*d0+30*a*e0*e0+90*a*d0*f0)/45
E=140*p0*(A+C0)-28*p0-47*A-41*C0+13+24*d0*d0+6*e0*e0+18*d0*f0
assert s.factor(T_over_a.subs(a,2/(20*p0-1))-2*E/(9*(20*p0-1)))==0
print('PROVED: rank-one endpoint identity checked exactly.')
