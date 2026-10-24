"""Exact finite checks of X027's algebra; no universal numerical inference."""
import json
import sympy as s
from itertools import product
I=s.I
checks=0

def check(value):
 global checks
 assert value
 checks+=1

def zero(X):
 if isinstance(X,s.MatrixBase):
  return all(s.simplify(z)==0 for z in X)
 return s.simplify(X)==0

# Symbolic moving-pivot compression, including the changing denominator.
r,t,d=s.symbols('r t d',real=True,nonzero=True)
v1,v2,w1,w2=s.symbols('v1 v2 w1 w2',complex=True)
b11,b22=s.symbols('b11 b22',real=True)
b12=s.symbols('b12',complex=True)
v=s.Matrix([v1,v2]);w=s.Matrix([w1,w2])
B=s.Matrix([[b11,b12],[s.conjugate(b12),b22]])
A=s.Matrix.vstack(s.Matrix([[d,w1.conjugate(),w2.conjugate()]]),s.Matrix.hstack(w,B))
V=s.Matrix.vstack(-v.conjugate().T/r,s.eye(2))
E=B-(w*v.conjugate().T+v*w.conjugate().T)/r+d*v*v.conjugate().T/r**2
check(zero(V.conjugate().T*A*V-E))
Jpath=t*B-(v+t*w)*(v+t*w).conjugate().T/(r+t*d)
check(zero(Jpath.diff(t).subs(t,0)-E))

# Exact rational unequal-phase example outside the balanced locus.
K=s.Matrix([[s.Rational(1,5),s.Rational(1,10),I/20],[s.Rational(1,10),s.Rational(3,5),s.Rational(1,10)],[-I/20,s.Rational(1,10),s.Rational(4,5)]])
D=s.diag(0,10,20); U=I*(D*K-K*D); B=s.eye(3); A=B+U
for J in [K,s.eye(3)-K]:
 for n in [1,2,3]:check(J[:n,:n].det()>0)
check(A==s.Matrix([[1,-I,1],[I,1,-I],[1,I,1]]))
check(A.charpoly().as_expr().factor()==(s.Symbol('lambda')+1)*(s.Symbol('lambda')-2)**2)
c1,c2,c3,tau=s.symbols('c1 c2 c3 tau',real=True)
M=s.diag(c1,c2,c3)+tau*K; Adj=M.adjugate()
check(zero(s.trace(Adj*U)))
check(zero(s.trace(Adj*B*Adj*U)))
check(zero(s.trace(M*A.adjugate())-s.trace(M*B.adjugate())-s.trace(M*U.adjugate())))

# Every atom derivative is unchanged by the gauge tangent.
def probs(J):
 out=[]
 for bits in product([0,1],repeat=3):
  absent=[1-x for x in bits]
  out.append(s.expand((-1)**sum(absent)*(J-s.diag(*absent)).det()))
 return s.Matrix(out)
pA=probs(K+t*A);pB=probs(K+t*B)
check(zero(pA.diff(t).subs(t,0)-pB.diff(t).subs(t,0)))

# D and the six conditional endpoint Fisher sums are computed directly.
def endpoint_form(Vel):
 total=0
 for k in range(3):
  R=[j for j in range(3) if j!=k]
  a=K[k,k]
  v=K[R,[k]];wv=Vel[R,[k]];F=Vel.extract(R,R)
  for state in [0,1]:
   rr=a-(1-state);pi=a if state else 1-a
   J=K.extract(R,R)-v*v.conjugate().T/rr
   EV=F-(wv*v.conjugate().T+v*wv.conjugate().T)/rr+Vel[k,k]*v*v.conjugate().T/rr**2
   T=s.eye(3)[:,R];T[k,:]=-v.conjugate().T/rr
   check(zero(EV-T.conjugate().T*Vel*T))
   for FJ in [J,s.eye(2)-J]:
    P=T*FJ.adjugate()*T.conjugate().T
    check(P.rank()==2)
    score=s.trace(FJ.adjugate()*EV)
    check(zero(score-s.trace(P*Vel)))
    total+=pi*score**2/FJ.det()
 return s.factor(total)
EA=endpoint_form(A); EB=endpoint_form(B)
check(EA==EB)

# Horizontal projection is not positive, even for scalar M.
K0=s.eye(3)/2+I*s.Matrix([[0,1,-1],[-1,0,1],[1,-1,0]])/4
U0=[]
for k in [0,1]:
 d0=s.diag(*[int(j==k) for j in range(3)])
 U0.append(I*(d0*K0-K0*d0))
G=s.Matrix(2,2,lambda i,j:s.trace(U0[i]*U0[j]))
v=s.Matrix([1,1,0]); P=v*v.T
coeff=G.inv()*s.Matrix([s.trace(Z*P) for Z in U0])
Ph=P-sum((coeff[i]*U0[i] for i in range(2)),s.zeros(3))
expected=s.Matrix([[1,s.Rational(1,3),s.Rational(1,3)],[s.Rational(1,3),1,s.Rational(1,3)],[s.Rational(1,3),s.Rational(1,3),0]])
check(Ph==expected)
for Z in U0:check(s.trace(Z*Ph)==0)
check(Ph.extract([0,2],[0,2]).det()==-s.Rational(1,9))
check(Ph.det()==-s.Rational(4,27))
check(probs(K0)==s.Matrix([s.Rational(1,32)]+[s.Rational(5,32)]*6+[s.Rational(1,32)]))
report={'status':'PASS','exact_assertions':checks,'indefinite_direction_spectrum':[-1,2,2],'endpoint_A_equals_endpoint_I':str(EA),'nonpositive_projection_principal_minor':'-1/9','nonpositive_projection_determinant':'-4/27'}
print(json.dumps(report,indent=2))
