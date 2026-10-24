import numpy as np, math
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply
# P0288 (Pollett queues/QSD survey, Section 2 Conjecture (ii)): does every finite positive limit
# of t^a e^{lambda t} p_t(i,j) factor as A x_i m_j?
# Candidate counterexample: nearest-neighbour CT walk on Z (rate 1 each side), killed at rate kappa
# everywhere and at extra rate v at 0.  Claim: t^{3/2} e^{kappa t} p_t(i,j) -> [(|i|+2/v)(|j|+2/v)+ij]/(4 sqrt(pi))
# The kappa cancels in e^{kappa t} p_t, so set kappa = 0 and kill only at 0 with rate v.
def kernel(N, v, t, sources):
    n=2*N+1
    L = diags([np.ones(n-1), -2*np.ones(n), np.ones(n-1)], [-1,0,1], format='csc')
    kill = np.zeros(n); kill[N] = v          # index N is site 0
    A = (L - diags([kill],[0])).tocsc()
    out={}
    for i in sources:
        e = np.zeros(n); e[N+i] = 1.0
        u = expm_multiply(A*t, e)
        out[i]=u
    return out
def claimed(i,j,v):
    c = 2.0/v
    return ((abs(i)+c)*(abs(j)+c) + i*j)/(4*math.sqrt(math.pi))
v=2.0
print(f"v={v}: claimed limits  M(0,0)={claimed(0,0,v):.6f}  M(0,1)={claimed(0,1,v):.6f}  M(1,1)={claimed(1,1,v):.6f}  M(1,-1)={claimed(1,-1,v):.6f}")
print(f"{'t':>7} {'N':>6} {'t^1.5 p(0,0)':>13} {'t^1.5 p(0,1)':>13} {'t^1.5 p(1,1)':>13} {'t^1.5 p(1,-1)':>14}")
for t in [100.0, 400.0, 1600.0, 6400.0]:
    N=int(12*math.sqrt(t))+50
    K=kernel(N,v,t,[0,1])
    f=t**1.5
    p00=K[0][N+0]; p01=K[0][N+1]; p11=K[1][N+1]; p1m1=K[1][N-1]
    print(f"{t:>7.0f} {N:>6} {f*p00:>13.6f} {f*p01:>13.6f} {f*p11:>13.6f} {f*p1m1:>14.6f}")
print()
print("2x2 minor of the LIMIT matrix at (0,1): M00*M11 - M01*M10 = c^2/(16 pi) =", (2.0/v)**2/(16*math.pi))
print("(nonzero => the limit is not rank one => no factorisation A x_i m_j)")
