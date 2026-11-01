"""E0063 / Rozikov Problem 10: xi-QSO on E_0 = {0,1,..,m}, partition of E into q blocks; same-block pairs and any pair
with 0 produce the empty body 0 (P=1 at k=0); cross-block pairs arbitrary.  Claim: 1 - x0' <= (1 - 1/q)(1 - x0)^2,
hence unique fixed point e_0 and convergence.  Random operators, random points, worst ratio."""
import numpy as np
rng=np.random.default_rng(63)
worst=0.0; worst_conv=0; worst_ratio_seq=0
for trial in range(300):
    m=int(rng.integers(3,9)); q=int(rng.integers(2,min(m,5)+1))
    blocks=rng.integers(0,q,m)
    while len(set(blocks))<q: blocks=rng.integers(0,q,m)
    P=np.zeros((m+1,m+1,m+1))
    for i in range(m+1):
        for j in range(i,m+1):
            if i==0 or j==0 or blocks[i-1]==blocks[j-1]:
                P[i,j,0]=P[j,i,0]=1.0
            else:
                row=rng.dirichlet(np.ones(m+1)*rng.choice([0.3,1,3]))
                P[i,j]=row; P[j,i]=row
    def V(x):
        y=np.einsum('i,j,ijk->k',x,x,P); return y/y.sum()   # V is homogeneous of degree 2: renormalise or a rounding error in the mass squares every step
    for _ in range(20):
        x=rng.dirichlet(np.ones(m+1)*rng.choice([0.2,1,5]))
        y=V(x); lhs=1-y[0]; rhs=(1-1/q)*(1-x[0])**2
        if rhs>0: worst=max(worst,lhs/rhs)
        # convergence
        z=x.copy()
        for k in range(60):
            y0=z[1:].sum(); z=V(z); y1=z[1:].sum()          # 1 - x0 computed as the mass off 0: exact down to underflow
            if y0>1e-150: worst_ratio_seq=max(worst_ratio_seq, y1/((1-1/q)*y0*y0))
        worst_conv=max(worst_conv,z[1:].sum())
print("max over trials of (1-x0')/((1-1/q)(1-x0)^2):", worst, " (claim: <= 1)")
print("max of 1-x0 after 60 iterations:", worst_conv); print("max along trajectories of y_{n+1}/((1-1/q) y_n^2):", worst_ratio_seq)
