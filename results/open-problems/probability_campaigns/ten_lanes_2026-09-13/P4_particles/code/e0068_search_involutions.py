# E0068 / Problem 21: QSOs with V^r = V.  Reduction: minimal r = d+1 where d=ord(V|_ImV).
# Here: search numerically for QSOs on S^2 (m=3) with V o V = id  (d=2, r=3),
# i.e. V(V(x)) = (sum x)^3 x  as a homogeneous polynomial identity.
# Are there any besides the three transpositions?
import numpy as np, itertools
from scipy.optimize import least_squares
PAIRS=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
MULT=[1,2,1,2,1,1]  # multiplicity of x_i x_j in (sum x)^2 expansion: (0,0)->1,(0,1)->2,(0,2)->2,(1,1)->1,(1,2)->2,(2,2)->1
MULT=[1,2,2,1,2,1]
def V(P,x):
    y=np.zeros(3,dtype=x.dtype)
    for idx,(i,j) in enumerate(PAIRS):
        y=y+MULT[idx]*x[i]*x[j]*P[idx]
    return y
# monomials of degree 4 in 3 vars
MON4=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
def residual(p):
    P=p.reshape(6,3)
    res=[]
    # row-sum constraints
    for idx in range(6): res.append(P[idx].sum()-1.0)
    # polynomial identity V(V(x)) - (sum x)^3 x == 0 : sample at enough points (exact via random rational-ish pts)
    rng=np.random.default_rng(0)
    pts=residual.pts
    for x in pts:
        w=V(P,V(P,x))
        res.extend(list(w-(x.sum()**3)*x))
    return np.array(res)
rng=np.random.default_rng(5)
residual.pts=[rng.normal(size=3) for _ in range(40)]   # 40*3=120 eqs, > 45 needed
sols=[]
for trial in range(600):
    p0=rng.dirichlet(np.ones(3),size=6).ravel()
    r=least_squares(residual,p0,bounds=(0,1),xtol=1e-15,ftol=1e-15,gtol=1e-15)
    if np.max(np.abs(r.fun))<1e-9:
        P=r.x.reshape(6,3)
        if not any(np.max(np.abs(P-S))<1e-6 for S in sols):
            sols.append(P.copy())
print("distinct solutions found:",len(sols))
for P in sols:
    print(np.array2string(np.round(P,6)))
    print("  -> images of vertices:", [np.round(V(P,np.eye(3)[i]),4).tolist() for i in range(3)])
