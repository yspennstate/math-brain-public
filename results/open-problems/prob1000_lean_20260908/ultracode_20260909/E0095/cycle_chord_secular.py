# Second, independent method for the SRW on C_n plus one chord {0,m}:
# eigenvalues rho = cos(theta) of P solve, in the sector phi(0)=phi(m) (symmetric)
#     tan(theta*m/2) + tan(theta*(n-m)/2) + tan(theta/2) = 0
# and in the sector phi(0) = -phi(m) (antisymmetric)
#     cot(theta*m/2) + cot(theta*(n-m)/2) + cot(theta/2) = 0 ,
# derived from the transfer-matrix ansatz phi = cos/sin(theta(j - l/2)) on each arc.
# We find the smallest positive root of each and compare cos(theta) with the
# second-largest eigenvalue of P computed by dense linear algebra.
import numpy as np
from scipy.optimize import brentq

def srw_lambda2(n, m):
    A = np.zeros((n, n))
    for j in range(n):
        A[j, (j+1) % n] = A[(j+1) % n, j] = 1
    A[0, m] = A[m, 0] = 1
    d = A.sum(1); S = A / np.sqrt(np.outer(d, d))
    mu = np.sort(np.linalg.eigvalsh(S))[::-1]
    return mu[1]

def smallest_root(F, hi, step=1e-4):
    # scan for the first sign change avoiding poles (|F| huge)
    xs = np.arange(step, hi, step)
    v = F(xs)
    for i in range(len(xs)-1):
        if np.isfinite(v[i]) and np.isfinite(v[i+1]) and v[i]*v[i+1] < 0 and abs(v[i]) < 50 and abs(v[i+1]) < 50:
            return brentq(F, xs[i], xs[i+1], xtol=1e-14)
    return None

worst = 0
for n in [8, 9, 12, 13, 20, 21, 40, 41, 80, 81, 200]:
    for m in sorted(set([2, 3, n//3, n//2, (n-1)//2, n//2+1, 2*n//3])):
        if m < 2 or m > n-2: continue
        Fs = lambda t: np.tan(t*m/2) + np.tan(t*(n-m)/2) + np.tan(t/2)
        Fa = lambda t: 1/np.tan(t*m/2) + 1/np.tan(t*(n-m)/2) + 1/np.tan(t/2)
        ts = smallest_root(Fs, 4*np.pi/n)
        ta = smallest_root(Fa, 4*np.pi/n)
        cands = [np.cos(t) for t in (ts, ta) if t is not None]
        # Dirichlet-type eigenvectors vanishing at both chord ends: theta = pi*k/m = pi*k'/(n-m)
        from math import gcd
        g = gcd(m, n-m); tD = np.pi*g/(m*(n-m)) * 1.0  # smallest common value pi*k/m = pi*k'/(n-m)
        # smallest positive theta with theta*m/pi and theta*(n-m)/pi both integers is pi*lcm(m,n-m)/(m(n-m)) = pi/gcd(m,n-m)?? -> theta = pi*L/(m(n-m)), L=lcm
        L = m*(n-m)//g; tD = np.pi*L/(m*(n-m))
        cands.append(np.cos(tD))
        pred = max(cands) if cands else None
        exact = srw_lambda2(n, m)
        err = abs(pred - exact) if pred is not None else float('nan')
        worst = max(worst, err)
        print(f"n={n:4d} m={m:4d}  secular lambda_2(P)={pred:.12f}  dense={exact:.12f}  diff={err:.1e}  cycle={np.cos(2*np.pi/n):.12f}")
print("worst discrepancy:", worst)
