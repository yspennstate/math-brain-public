"""Exact checks for X088; analytic inequalities are proved in the report."""
import itertools, json
from pathlib import Path
import sympy as s
I=s.I;R=s.Rational
F=s.Matrix(4,4,lambda i,j:I**(i*j)/2)
sets=[tuple(i for i in range(4) if mask>>i&1) for mask in range(16)]
checks=0
def check(q):
 global checks
 assert q
 checks+=1
# Two-stage network: row pairs (0,2),(1,3), column pairs (0,1),(2,3).
# Network column groups correspond to physical opposite pairs (0,2),(1,3).
physical=[0,2,1,3]
net=s.zeros(16)
for mask,T in enumerate(sets):
 for coins in itertools.product((0,1),repeat=4):
  occ=[int(i in T) for i in range(4)]
  for coin,(i,j) in zip(coins,[(0,2),(1,3),(0,1),(2,3)]):
   if coin:occ[i],occ[j]=occ[j],occ[i]
  out=sum((occ[i]<<physical[i]) for i in range(4))
  net[out,mask]+=R(1,16)
for sm,S in enumerate(sets):
 for tm,T in enumerate(sets):
  prob=0 if len(S)!=len(T) else s.expand_complex(F.extract(S,T).det()*s.conjugate(F.extract(S,T).det()))
  check(s.simplify(net[sm,tm]-prob)==0)
# Symbolic orbit masses and complete imbalance.
a,b,x,y,t,z=s.symbols('a b x y t z',real=True)
u=[(1-a)**2-x*x,2*(a*(1-a)+x*x),a*a-x*x]
v=[(1-b)**2-y*y,2*(b*(1-b)+y*y),b*b-y*y]
A=s.expand(u[1]*v[1]);B=s.expand(u[2]*v[0]+u[0]*v[2]);f=s.expand(A+B);Delta=s.expand(A-2*B)
check(s.expand(Delta-2*(x*x+y*y-(a-b)**2))==0)
check(s.expand(f-(6*a*a*b*b-6*a*a*b+a*a-6*a*b*b+4*a*b+b*b+(6*b*(1-b)-1)*x*x+(6*a*(1-a)-1)*y*y+6*x*x*y*y))==0)
fs=s.expand(f.subs({a:t,b:t}));beta=6*t*(1-t)-1
check(s.expand(fs-(6*t*t*(1-t)**2+beta*(x*x+y*y)+6*x*x*y*y))==0)
check(s.simplify(s.hessian(fs,(x,y))-s.Matrix([[2*beta+12*y*y,24*x*y],[24*x*y,2*beta+12*x*x]]))==s.zeros(2))
z=s.symbols('z',real=True)
j=(1+z)*s.log(1+z)/3+2*(1-z/2)*s.log(1-z/2)/3
check(s.simplify(s.diff(j,z,2)-1/(2*(1+z)*(1-z/2)))==0)
check(s.simplify(j-z*s.diff(j,z)-(s.log(1+z)+2*s.log(1-z/2))/3)==0)
check(s.simplify(s.diff(j,z)/2-(s.log(1+z)-s.log(1-z/2))/6)==0)
check(s.simplify(s.diff(5*s.log(1+z)+7*s.log(1-z/2),z)-(R(3,2)-6*z)/((1+z)*(1-z/2)))==0)
check(R(3,2)**5*R(3,4)**7==R(531441,524288))
th=(s.sqrt(69)-3)/12
check(s.simplify(-2+12*th+24*th*th-8)==0)
# Full determinant atom tables at a rational strong nonbalanced example.
lam=[R(79,100),R(63,100),R(1,100),R(17,100)]
K=s.simplify(F*s.diag(*lam)*F.conjugate().T)
q=[]
for T in sets:q.append(s.prod(lam[i] if i in T else 1-lam[i] for i in range(4)))
probs=net*s.Matrix(q)
for sm,S in enumerate(sets):
 M=s.Matrix(4,4,lambda i,j:K[i,j] if j in S else int(i==j)-K[i,j])
 check(s.simplify(M.det()-probs[sm])==0)
check(sum(probs)==1)
for p in probs:check(p>0)
subs={a:R(2,5),b:R(2,5),x:R(39,100),y:R(23,100)}
fv=f.subs(subs);dv=Delta.subs(subs)
for sm,S in enumerate(sets):
 if len(S)==2:
  expected=fv/6+dv/12 if (S[1]-S[0])==2 else fv/6-dv/24
  check(s.simplify(probs[sm]-expected)==0)
check(dv>0)
# An exact obstruction to extending the deficit-convexity argument unaided.
check(4*27**10<32**10)
result={'exact_assertions':checks,'status':'PASS','threshold':str(th),'threshold_decimal':float(th),'strong_example_eigenvalues':[str(q) for q in lam],'strong_example_kernel':str(K),'pair_atom_adjacent':str(fv/6-dv/24),'pair_atom_opposite':str(fv/6+dv/12),'network_projection_entries_checked':256,'comment':'Finite identities supplement the analytic all-parameter proof; no sampled sign is used as a theorem.'}
Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
