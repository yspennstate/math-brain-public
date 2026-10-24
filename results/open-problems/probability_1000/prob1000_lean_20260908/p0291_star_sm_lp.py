"""P0291 (Leskela, Ross's second conjecture note, Problem 3): is there a stationary ergodic CTMC that is NOT
stochastically monotone but whose speeded-up versions are decreasing in the supermodular order?

Candidate: the symmetric star chain on {1,2,3}: 1 -> 2 and 1 -> 3 at rate a each, 2 -> 1 and 3 -> 1 at rate b.
Not monotone (q13 = a > q23 = 0). Test: for fixed times t_1 < ... < t_n and speeds c1 < c2, is
(X(c1 t_k))_k >=_sm (X(c2 t_k))_k ?  Exact check by LP duality on the finite lattice {1,2,3}^n:
   max over phi supermodular, |phi| <= 1, of  E_{c2} phi - E_{c1} phi.
sm-order holds iff the maximum is <= 0.  Supermodularity on a product of chains is equivalent to
increasing differences in every pair of coordinates (Topkis), so the constraints are
   phi(x + e_i + e_j) - phi(x + e_i) - phi(x + e_j) + phi(x) >= 0  for all x, i < j.
Also runs the same test on a CONTROL (a clockwise 3-cycle, which should fail) and on a reversible
monotone birth-death chain (which must pass, Bauerle-Rolski 1998).
"""
import itertools, sys
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog

def star(a, b):
    return np.array([[-2*a, a, a], [b, -b, 0.0], [b, 0.0, -b]])

def cycle(r):
    return np.array([[-r, r, 0.0], [0.0, -r, r], [r, 0.0, -r]])

def birth_death(u, d):
    return np.array([[-u, u, 0.0], [d, -(u+d), u], [0.0, d, -d]])

def stationary(Q):
    w, v = np.linalg.eig(Q.T)
    k = np.argmin(abs(w)); p = np.real(v[:, k]); return p / p.sum()

def fdd(Q, times, c):
    """joint law of (X(c t_1), ..., X(c t_n)) as an array over {0,1,2}^n"""
    pi = stationary(Q); n = len(times); m = Q.shape[0]
    P = [expm(Q * c * (times[k+1] - times[k])) for k in range(n-1)]
    law = np.zeros([m]*n)
    for x in itertools.product(range(m), repeat=n):
        p = pi[x[0]]
        for k in range(n-1): p *= P[k][x[k], x[k+1]]
        law[x] = p
    return law

def sm_gap(law1, law2):
    """max_{phi supermodular, |phi|<=1} E_2 phi - E_1 phi. <= 0 means law1 >=_sm law2."""
    shape = law1.shape; n = len(shape); m = shape[0]
    idx = {x: i for i, x in enumerate(itertools.product(range(m), repeat=n))}
    N = len(idx)
    rows = []
    for x in idx:
        for i in range(n):
            for j in range(i+1, n):
                if x[i] + 1 < m and x[j] + 1 < m:
                    xi = list(x); xi[i] += 1; xj = list(x); xj[j] += 1; xij = list(x); xij[i] += 1; xij[j] += 1
                    row = np.zeros(N)
                    row[idx[tuple(xij)]] += 1; row[idx[x]] += 1; row[idx[tuple(xi)]] -= 1; row[idx[tuple(xj)]] -= 1
                    rows.append(-row)          # linprog wants A_ub phi <= 0, we need row.phi >= 0
    A = np.array(rows)
    cobj = np.array([law1[x] - law2[x] for x in idx])   # minimize E_1 - E_2  == maximize E_2 - E_1
    res = linprog(cobj, A_ub=A, b_ub=np.zeros(len(rows)), bounds=[(-1, 1)]*N, method="highs")
    assert res.status == 0, res.message
    return -res.fun, res.x, idx

def run(name, Q, times, speeds):
    worst = -1.0
    for c1, c2 in zip(speeds[:-1], speeds[1:]):
        g, phi, idx = sm_gap(fdd(Q, times, c1), fdd(Q, times, c2))
        worst = max(worst, g)
        flag = "OK " if g <= 1e-9 else "VIOLATION"
        print(f"  {name} times={times} c1={c1:g} c2={c2:g}: max(E2-E1)={g:+.3e} {flag}", flush=True)
    return worst

if __name__ == "__main__":
    speeds = [0.25, 0.5, 1.0, 2.0, 4.0, 8.0]
    for times in ([0.0, 1.0, 2.0], [0.0, 0.3, 1.0], [0.0, 1.0, 1.5, 3.0], [0.0, 0.5, 1.0, 1.5]):
        print("== star a=1 b=1"); run("star11", star(1.0, 1.0), times, speeds)
        print("== star a=1 b=3"); run("star13", star(1.0, 3.0), times, speeds)
        print("== star a=3 b=1"); run("star31", star(3.0, 1.0), times, speeds)
        print("== CONTROL cycle (should violate)"); run("cycle", cycle(1.0), times, speeds)
        print("== CONTROL birth-death (must pass)"); run("bd", birth_death(1.0, 2.0), times, speeds)
