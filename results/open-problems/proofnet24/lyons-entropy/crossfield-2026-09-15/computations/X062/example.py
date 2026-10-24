import sympy as S
from itertools import combinations
om=(-1+S.sqrt(3)*S.I)/2
u=S.Matrix([0,1,-1])/S.sqrt(2)
X=S.Matrix([[0,0,1],[1,0,0],[0,1,0]]); Z=S.diag(1,om,om**2)
base=[S.simplify(Z**a*X**b*u) for a in range(3) for b in range(3)]
R=S.diag(1,1,S.I)
ns=base+[S.simplify(R*v) for v in base]
g={}; W=S.zeros(3)
for i,j in combinations(range(18),2):
 lam=S.simplify((ns[i].conjugate().T*ns[j])[0]*S.conjugate((ns[i].conjugate().T*ns[j])[0]))
 if lam==1: continue
 w=S.conjugate(ns[i].cross(ns[j]))/6
 z=S.simplify(w*w.conjugate().T)
 c=-S.log(1-lam)
 W+=c*z
 g[lam]=S.simplify(g.get(lam,0)+z[2,2]-z[0,0])
print('delta group',g)
print('W diagonals',[S.simplify(W[k,k]) for k in range(3)])
print('W numeric',W.evalf(16))
# operator second moment exact via complete Hermitian real basis
bs=[S.diag(*[int(i==j) for i in range(3)]) for j in range(3)]
for i,j in combinations(range(3),2):
 B=S.zeros(3);B[i,j]=B[j,i]=1;bs.append(B)
 B=S.zeros(3);B[i,j]=S.I;B[j,i]=-S.I;bs.append(B)
for A in bs:
 for B in bs:
  lhs=S.simplify(sum((v.conjugate().T*A*v)[0]*(v.conjugate().T*B*v)[0]/6 for v in ns))
  assert S.simplify(lhs-(S.trace(A)*S.trace(B)+S.trace(A*B))/4)==0
print('81 exact 2-design equalities passed')
