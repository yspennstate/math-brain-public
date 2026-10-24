"""High-precision verification of tau_1 > tau_0 (Aldous-Fill Open Problem 4.48(a)) on explicit chains.
Family P_k(eps): states 0..k on a path; rate 1 from i to i-1 (toward 0) for i>=1; rate eps from i to i+1 for i<k.
Birth-death, hence reversible. Continuous time. tau_0 = Kemeny constant = trace Z = sum_{lambda>0} 1/lambda,
tau_1 = inf{t : max_{i,j} TV(P_i(X_t), P_j(X_t)) <= 1/e}.
"""
from mpmath import mp, mpf, matrix, eye, exp, findroot, e
mp.dps = 30

def chain(k, eps):
    n = k + 1
    Q = matrix(n, n)
    for i in range(n):
        if i >= 1: Q[i, i-1] = 1
        if i < k: Q[i, i+1] = eps
        Q[i, i] = -(Q[i, i-1] if i >= 1 else 0) - (Q[i, i+1] if i < k else 0)
    # pi: birth-death detailed balance pi_{i+1} = pi_i * eps / 1
    pi = [mpf(1)]
    for i in range(1, n): pi.append(pi[-1] * eps)
    s = sum(pi); pi = [p / s for p in pi]
    return Q, pi

def kemeny(Q, pi):
    n = Q.rows
    Pi = matrix(n, n)
    for i in range(n):
        for j in range(n): Pi[i, j] = pi[j]
    Z = (Pi - Q) ** -1 - Pi
    return sum(Z[j, j] for j in range(n)), Z

def Pt(Q, t):
    return (t * Q).__class__.__name__ and mp.expm(t * Q)

def dbar(Q, t):
    n = Q.rows; P = mp.expm(t * Q); m = mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            m = max(m, sum(abs(P[i, l] - P[j, l]) for l in range(n)) / 2)
    return m

def tau1(Q):
    f = lambda t: dbar(Q, t) - 1 / e
    lo, hi = mpf('0.01'), mpf(1)
    while f(hi) > 0: hi *= 2
    return findroot(f, (lo, hi), solver='bisect', tol=mpf(10) ** -20)

for k in [2, 3, 4, 5, 6]:
    for eps in [mpf('0.1'), mpf('0.01'), mpf('0.001'), mpf('1e-5')]:
        Q, pi = chain(k, eps)
        t0, Z = kemeny(Q, pi)
        t1 = tau1(Q)
        # tau_1^(2) and tau_2 for (b)
        n = k + 1
        t12 = max(-Z[i, j] / pi[j] for i in range(n) for j in range(n))
        ev = mp.eig(-Q)[0]
        lam = sorted([mp.re(v) for v in ev])
        t2 = 1 / lam[1]
        print(f"k={k} eps={mp.nstr(eps,3)}: tau0={mp.nstr(t0,10)} tau1={mp.nstr(t1,10)} ratio tau1/tau0={mp.nstr(t1/t0,8)} | tau2={mp.nstr(t2,8)} tau1^(2)={mp.nstr(t12,8)} ratio={mp.nstr(t2/t12,8)}")
# the random-search witness, exactly as printed (rounded weights), with q_ij = W_ij / w_i
import numpy as np
W = [[1188.3494, 15.0507, 0.0], [15.0507, 0.1821, 0.1013], [0.0, 0.1013, 0.003]]
n = 3; w = [sum(row) for row in W]
Q = matrix(n, n)
for i in range(n):
    for j in range(n):
        if i != j: Q[i, j] = mpf(W[i][j]) / mpf(w[i])
    Q[i, i] = -sum(Q[i, j] for j in range(n) if j != i)
pi = [mpf(w[i]) / mpf(sum(w)) for i in range(n)]
t0, Z = kemeny(Q, pi); t1 = tau1(Q)
print("random-search witness: tau0=", mp.nstr(t0, 12), "tau1=", mp.nstr(t1, 12), "ratio=", mp.nstr(t1 / t0, 10), "pi=", [mp.nstr(p, 6) for p in pi])
