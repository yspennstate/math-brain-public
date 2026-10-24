"""P0292 on three states beyond the star family: random reversible 3-state generators (all six rates positive).
For each: (i) the bivariate criterion  l1(1) l1(3) <= 0  where l1 = pi * v1 is the left eigenvector of the slowest
nonzero eigenvalue (equivalent to the two-point concordance order being monotone in the lag: only H_s(1,2) is
non-trivial, and its slow-mode coefficient has the sign of l1(1) l1(3));  (ii) the LP dual test of >=_sm at n = 3, 4.
Hypothesis: on three states, (2) <=> l1(1) l1(3) <= 0.  Also flags stochastically monotone chains (where (2) is a
theorem) so the interesting rows are the non-monotone ones.
"""
import numpy as np
from p0291_star_sm_lp import fdd, sm_gap, stationary

def random_reversible(rng):
    pi = rng.dirichlet([2, 2, 2])
    S = np.zeros((3, 3))
    for i in range(3):
        for j in range(i+1, 3):
            S[i, j] = S[j, i] = rng.uniform(0.1, 3.0)          # symmetric "conductances"
    Q = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            if i != j: Q[i, j] = S[i, j] / pi[i]
        Q[i, i] = -Q[i].sum()
    return Q

def monotone(Q):
    # 3-state criterion: q13 <= q23 and q31 <= q21
    return Q[0, 2] <= Q[1, 2] + 1e-12 and Q[2, 0] <= Q[1, 0] + 1e-12

def slow_sign(Q):
    pi = stationary(Q)
    lam, V = np.linalg.eig(Q); order = np.argsort(-lam.real); v1 = V.real[:, order[1]]
    l1 = pi * v1
    return l1[0] * l1[2], -lam.real[order[1]], -lam.real[order[2]]

def lp_test(Q):
    worst = -1
    for times in ([0.0, 1.0, 2.0], [0.0, 0.3, 1.0], [0.0, 0.5, 1.0, 1.5]):
        for c1, c2 in ((0.5, 1.0), (1.0, 2.0), (2.0, 4.0)):
            g, _, _ = sm_gap(fdd(Q, times, c1), fdd(Q, times, c2)); worst = max(worst, g)
    return worst

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    rng = np.random.default_rng(20260910)
    agree = disagree = 0
    for k in range(40):
        Q = random_reversible(rng)
        s, mu1, mu2 = slow_sign(Q); w = lp_test(Q); mono = monotone(Q)
        holds = w <= 1e-9; pred = s <= 1e-12
        tag = "agree" if holds == pred else "DISAGREE"
        agree += holds == pred; disagree += holds != pred
        print(f"{k:2d} q=[{Q[0,1]:.2f},{Q[0,2]:.2f},{Q[1,0]:.2f},{Q[1,2]:.2f},{Q[2,0]:.2f},{Q[2,1]:.2f}] mono={int(mono)} "
              f"l1(1)l1(3)={s:+.3f} LPworst={w:+.2e} holds={int(holds)} -> {tag}", flush=True)
    print(f"agree {agree} disagree {disagree}")
