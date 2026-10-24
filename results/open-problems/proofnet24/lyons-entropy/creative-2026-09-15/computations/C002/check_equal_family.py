"""Reproducible arithmetic/finite diagnostics for C002; not a proof.
The mathematical proof in agents/C002.md covers every 0<t<1.
Run with the CODEX_PRIMARY_RUNTIME_PYTHON environment's Python.
"""
from fractions import Fraction as F
from math import log, sqrt
import numpy as np

# Exact rational checks of the displayed coefficient identities on rational t.
# The identities are also verified as polynomial identities below using only
# a tiny standard-library polynomial implementation.
def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 while len(c)>1 and not c[-1]:c.pop()
 return c
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 while len(c)>1 and not c[-1]:c.pop()
 return c
def scale(a,c):return [c*x for x in a]
D=[3,-2,-1]
na=add(mul(mul([3,-1],[3,-1]),[3,1]),scale(mul(mul([1,1],[1,1]),[1,-1]),9))
nb=add(scale(mul([0,1],mul([3,-1],[3,1])),-2),scale(mul([0,1],mul([1,1],[1,-1])),18))
nc=add(scale(mul([0,0,1],[3,1]),4),scale(mul([0,0,1],[1,-1]),36))
assert na==[36,0,-12,-8]
assert nb==[0,0,0,-16]
assert nc==[0,0,48,-32]
assert add(na,scale(nc,-1))==scale(mul([1,-1],[3,3,-2]),12)
assert add(mul(na,nc),scale(mul(nb,nb),-1))==scale(mul([0,0,1],D),576)
print('PASS exact polynomial identities')

# Independently assemble the full 9-real-coordinate entropy Hessian from
# determinant atoms and Jacobi derivatives, then compare the 2x2 restriction.
def hermitian_basis():
 out=[]
 for i in range(3):
  A=np.zeros((3,3),complex);A[i,i]=1;out.append(A)
 for i,j in [(1,2),(2,0),(0,1)]:
  A=np.zeros((3,3),complex);A[i,j]=A[j,i]=1/sqrt(2);out.append(A)
 for i,j in [(1,2),(2,0),(0,1)]:
  A=np.zeros((3,3),complex);A[i,j]=1j/sqrt(2);A[j,i]=-1j/sqrt(2);out.append(A)
 return out
basis=hermitian_basis()
def independent_hessian(K):
 result=np.zeros((9,9));atoms=[]
 for mask in range(8):
  absent=[i for i in range(3) if not (mask>>i)&1]
  Q=K.copy()
  for i in absent:Q[i,i]-=1
  p=float(((-1)**len(absent)*np.linalg.det(Q)).real)
  R=np.linalg.inv(Q)
  score=np.array([np.trace(R@A).real for A in basis])
  # D^2 p(A,B) = p [tr(R A) tr(R B)-tr(R A R B)].
  dd=np.array([[p*(score[i]*score[j]-np.trace(R@A@R@B).real) for j,B in enumerate(basis)] for i,A in enumerate(basis)])
  result-=p*np.outer(score,score)+log(p)*dd
  atoms.append(p)
 return result,np.array(atoms)

rows=[]
for t in [1e-5,.001,.01,.1,.5,.9,.99,.9999,1-1e-6]:
 r=sqrt(t/12);K=np.eye(3,dtype=complex)/2
 for i,j in [(0,1),(1,2),(2,0)]:K[i,j]=1j*r;K[j,i]=-1j*r
 H,p=independent_hessian(K)
 q0=(1-t)/8;q=(3+t)/24;m=log(q/q0)
 den=(1-t)*(3+t)
 alpha=(36-12*t*t-8*t*t*t)/den
 beta=-16*t*t*t/den
 gamma=16*t*t*(3-2*t)/den
 T=np.array([[alpha-6*m,beta],[beta,gamma+6*m]])
 # Coordinates of a I + u(J-I) in the orthonormal basis.
 X=np.zeros((9,2));X[:3,0]=1;X[3:6,1]=sqrt(2)
 discrepancy=float(np.max(np.abs(-X.T@H@X-T)))/(1+float(np.max(np.abs(T))))
 assert discrepancy<1e-8,(t,discrepancy)
 assert np.linalg.eigvalsh(H).max()<0,(t,np.linalg.eigvalsh(H))
 assert m*m<=16*t*t/(3*den)*(1+1e-10)
 rows.append((t,np.linalg.eigvalsh(H).max(),discrepancy))
print('PASS independent finite Hessian checks')
for t,e,d in rows:print(f't={t:.9g} max_Hessian_eigenvalue={e:.12g} relative_restriction_error={d:.3g}')
