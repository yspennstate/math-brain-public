"""P0245 = Aldous-Fill Open Problem 6.30: is E_pi C >= (n-1) H_{n-1} for every irreducible reversible chain on n states?
Reversible chain = random walk on a weighted graph (symmetric w >= 0, self-loops allowed): P(i,j) = w_ij / w_i, pi_i = w_i / W.
E_pi C computed exactly on the absorbing chain over (position, covered set).  Minimise over w by random restarts + Nelder-Mead."""
import numpy as np, itertools, sys
from scipy.optimize import minimize
def cover_time(P):
    n = P.shape[0]; w = None
    # states: (i, S) with S a bitmask containing i; absorbing when S == full
    full = (1<<n)-1
    idx = {}
    for S in range(1<<n):
        for i in range(n):
            if S>>i & 1: idx[(i,S)] = len(idx)
    m = len(idx); A = np.zeros((m,m)); b = np.ones(m)
    for (i,S),k in idx.items():
        if S == full: A[k,k]=1; b[k]=0; continue
        A[k,k] = 1
        for j in range(n):
            if P[i,j] > 0: A[k, idx[(j, S | (1<<j))]] -= P[i,j]
    h = np.linalg.solve(A, b)          # expected remaining time to cover
    pi = np.linalg.eig(P.T)[1][:, np.argmin(np.abs(np.linalg.eigvals(P.T)-1))].real; pi = pi/pi.sum()
    return sum(pi[i]*h[idx[(i, 1<<i)]] for i in range(n))
def P_from(x, n):
    W = np.zeros((n,n)); k=0
    for i in range(n):
        for j in range(i, n):
            W[i,j] = W[j,i] = np.exp(x[k]); k+=1
    return W / W.sum(1, keepdims=True)
def obj(x, n): return cover_time(P_from(x, n))
for n in (3, 4, 5):
    H = sum(1.0/k for k in range(1, n))      # H_{n-1}
    target = (n-1)*H
    Kn = np.ones((n,n)) - np.eye(n); Kn = Kn/(n-1)
    print(f"n={n}: conjectured bound (n-1)H_(n-1) = {target:.6f};  K_n walk (no self loops): {cover_time(Kn):.6f};  uniform incl. self-loops: {cover_time(np.ones((n,n))/n):.6f}")
    rng = np.random.default_rng(245); best = (np.inf, None); m = n*(n+1)//2
    for trial in range(60 if n<5 else 25):
        x0 = rng.normal(size=m)*2
        res = minimize(obj, x0, args=(n,), method='Nelder-Mead', options={'maxfev': 1500 if n<5 else 800, 'xatol':1e-6, 'fatol':1e-9})
        if res.fun < best[0]: best = (res.fun, res.x)
    P = P_from(best[1], n)
    print(f"   min over reversible chains found: {best[0]:.6f}   (bound {target:.6f}, ratio {best[0]/target:.5f})")
    print("   argmin P =\n", np.round(P, 4))
    sys.stdout.flush()
