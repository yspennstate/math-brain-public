"""
Decisive O1 check: does the exhaustive two-sided min sit at the FINITE-N first-moment threshold?
If the 2nd moment concentrates, m_N is where E[#{(S,T): sigma_min(A[T,S])<=t}] = 1, i.e.
    C(N,n)^2 * C_F(n) * (sqrt(n) t)^{d_F} = 1.
So predicted rho_N^pred = -(1/N) log t solves that. We:
  1. exhaustively measure rho_N = -(1/N) log min_{|S|=|T|=n} sigma_min(A[T,S]),
  2. calibrate C_F(n) = P(sigma_min(G_n)<=t)/(sqrt(n) t)^{d_F} at small t by simulation,
  3. compare measured rho_N to rho_N^pred and to the asymptotic 2H(alpha)/d_F.
Match ==> constant 2H/d_F correct, 2nd moment concentrates, real-case "lag" is finite-size.
"""
import numpy as np, math
from itertools import combinations
from math import lgamma, log, sqrt, exp

def logC(N, k): return lgamma(N+1)-lgamma(k+1)-lgamma(N-k+1)

def gauss(shape, cplx, rng):
    if cplx: return (rng.standard_normal(shape)+1j*rng.standard_normal(shape))/math.sqrt(2)
    return rng.standard_normal(shape)

def exhaustive_min(A, n):
    N = A.shape[0]; subs = list(combinations(range(N), n)); best = np.inf
    for T in subs:
        RS = A[list(T), :]
        for S in subs:
            s = np.linalg.svd(RS[:, list(S)], compute_uv=False)[-1]
            if s < best: best = s
    return best

def calibrate_CF(n, cplx, rng, reps=200000, t=None):
    # C_F(n) = P(sigma_min(G_n)<=t)/(sqrt(n) t)^{d_F} at small t (near the exp scale it's ~const)
    dF = 2 if cplx else 1
    if t is None: t = 0.05/math.sqrt(n)
    hits = 0
    B = 20000
    done = 0
    while done < reps:
        b = min(B, reps-done); done += b
        # smallest singular value of b independent n x n gaussians
        G = gauss((b, n, n), cplx, rng)
        s = np.linalg.svd(G, compute_uv=False)[:, -1]
        hits += int((s <= t).sum())
    p = hits/reps
    return p/((math.sqrt(n)*t)**dF)

def run(field):
    cplx = (field=='C'); dF = 2 if cplx else 1
    print(f"=== field {field} (d_F={dF}) ===  2H(1/2)/d_F = {2*math.log(2)/dF:.4f}")
    for N in (8, 10, 12, 14):
        n = N//2; alpha = 0.5
        H = -alpha*log(alpha)-(1-alpha)*log(1-alpha)
        reps = 12 if N<=10 else (5 if N==12 else 2)
        rng = np.random.default_rng(1234+N+(100 if cplx else 0))
        CF = calibrate_CF(n, cplx, rng)
        # predicted: C(N,n)^2 * CF * (sqrt(n) t)^{dF} = 1 -> t
        # 2 logC + log CF + dF*(0.5 log n + log t) = 0
        log_t = -(2*logC(N,n) + log(CF) + dF*0.5*log(n))/dF
        rho_pred = -log_t/N
        ms = []
        for _ in range(reps):
            A = gauss((N,N), cplx, rng); ms.append(-log(exhaustive_min(A,n))/N)
        ms = np.array(ms)
        print(f"  N={N:2d} n={n}: rho_meas={ms.mean():.4f}+/-{ms.std()/math.sqrt(reps):.4f}  "
              f"rho_pred(1st-moment)={rho_pred:.4f}  [C_F(n)={CF:.3f}]")

if __name__ == "__main__":
    for field in ('R','C'): run(field)
