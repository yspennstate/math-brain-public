from itertools import combinations
import numpy as np

# 1. Exact star exception: every disjoint cut has rank <=1, whole offdiag rank is 2.
n=5
S=np.zeros((n,n),float)
for j in range(1,n):
    S[0,j]=S[j,0]=1.0
for r in range(1,n):
    for L in combinations(range(n),r):
        R=[j for j in range(n) if j not in L]
        if not R: continue
        C=S[np.ix_(L,R)]
        assert np.linalg.matrix_rank(C,tol=1e-10)<=1
assert np.linalg.matrix_rank(S,tol=1e-10)==2

# 2. Robust-anchor constants at the worst M=1 threshold.
M=1.0
m0=M/4-1/32
assert abs(m0-7/32)<1e-15
err=M/(8*M-1)
assert abs(err-1/7)<1e-15

# 3. Clique-factor target stress family.
G=np.array([[2,1,1,1],[1,-2,1,1],[1,1,2,1],[1,1,1,0]],float)
ev=np.linalg.eigvalsh(G)
assert sum(abs(x)>=1-1e-10 for x in ev)>=3
E=G[:2,:2]
D=abs(np.linalg.det(E))
kappa=min(abs(np.linalg.eigvalsh(E)))
Delta=abs(np.linalg.det(G[:3,:3]))
bound=8*np.sqrt(2)*np.sqrt(D/(kappa*Delta))+2/np.sqrt(D)
assert D>4.999999 and kappa>np.sqrt(5)-1e-10 and abs(Delta-8)<1e-10
assert bound<6.876

# 4. Pair-routing benchmark constants from the report.
kappa0=3/32
D0=33/1024
eta=1/4
route=8*np.sqrt(2)/np.sqrt(kappa0*eta)+2/np.sqrt(D0)
assert route<85.05

print('QFORM_B09_R18_CHECK_PASS')
print('stress_eigenvalues=',ev.tolist())
print('partner_bound=',bound)
print('route_bound=',route)
