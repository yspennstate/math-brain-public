"""For a reversible 3-state chain, gap-monotonicity of E phi is equivalent to (for every two-point conditional Phi):
  [E1]  F'(0) <= 0  <=>  sum_{x<y} pi(x) q(x,y) D_Phi(x,y) >= 0,  D_Phi(x,y) = Phi(x,x)+Phi(y,y)-Phi(x,y)-Phi(y,x)
  [E2]  slow-mode coefficient alpha >= 0  <=>  <Phi, l1 (x) l1> >= 0,  l1 = pi v1 (slowest nonzero mode)
(F(g) = C + alpha e^{-mu1 g} + beta e^{-mu2 g}; F' <= 0 on (0,inf) iff alpha >= 0 and mu1 alpha + mu2 beta >= 0,
and mu1 alpha + mu2 beta = -<Phi, pi Q> = -F'(0)).  This script computes Phi from phi directly (prefix via the
reversed chain = Q, suffix via Q) for n = 3, 4 and minimises [E1] and [E2] separately over supermodular phi (LP),
for stars that hold / fail and for random chains that hold / fail.  Question: does [E1] ever fail?
"""
import itertools
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog
from p0291_star_sm_lp import stationary
from p0292_star_family_map import star4
from p0292_random_3state_map import random_reversible, slow_sign, monotone

def conds(Q, gaps_before, gaps_after):
    m = 3; pi = stationary(Q)
    lam, V = np.linalg.eig(Q); order = np.argsort(-lam.real); v1 = V.real[:, order[1]]; l1 = pi * v1
    kb, ka = len(gaps_before), len(gaps_after); n = kb + ka + 2
    Pb = [expm(Q * g) for g in gaps_before]; Pa = [expm(Q * g) for g in gaps_after]
    pts = list(itertools.product(range(m), repeat=n)); idx = {x: i for i, x in enumerate(pts)}; N = len(pts)
    def phi_vec(x, y):
        c = np.zeros(N)
        for pre in itertools.product(range(m), repeat=kb):
            p = 1.0; cur = x
            for j in range(kb - 1, -1, -1): p *= Pb[j][cur, pre[j]]; cur = pre[j]
            for suf in itertools.product(range(m), repeat=ka):
                q = 1.0; cur2 = y
                for j in range(ka): q *= Pa[j][cur2, suf[j]]; cur2 = suf[j]
                c[idx[pre + (x, y) + suf]] += p * q
        return c
    Phi = {(x, y): phi_vec(x, y) for x in range(m) for y in range(m)}
    rows = []
    for x in pts:
        for i in range(n):
            for j in range(i+1, n):
                if x[i] + 1 < m and x[j] + 1 < m:
                    xi = list(x); xi[i] += 1; xj = list(x); xj[j] += 1; xij = list(x); xij[i] += 1; xij[j] += 1
                    r = np.zeros(N); r[idx[tuple(xij)]] += 1; r[idx[x]] += 1; r[idx[tuple(xi)]] -= 1; r[idx[tuple(xj)]] -= 1
                    rows.append(-r)
    A = np.array(rows)
    E1 = sum(pi[x] * Q[x, y] * (Phi[(x, x)] + Phi[(y, y)] - Phi[(x, y)] - Phi[(y, x)]) for x in range(m) for y in range(m) if x < y)
    E2 = sum(l1[x] * l1[y] * Phi[(x, y)] for x in range(m) for y in range(m))
    out = {}
    for name, vec in (("E1", E1), ("E2", E2)):
        res = linprog(vec, A_ub=A, b_ub=np.zeros(len(rows)), bounds=[(-1, 1)]*N, method="highs")
        out[name] = res.fun
    return out

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    cases = [("star 1,1,1,1 (holds)", star4(1,1,1,1)), ("star 1,1,2,1 (holds)", star4(1,1,2,1)),
             ("star 1,1,1,2 (FAILS)", star4(1,1,1,2)), ("star 1,1,1,4 (FAILS)", star4(1,1,1,4)), ("star 3,0.3,1.1,1 (holds?)", star4(3,0.3,1.1,1))]
    rng = np.random.default_rng(20260910)
    for k in range(40):
        Q = random_reversible(rng)
        if k in (2, 5, 9, 13, 21, 38):
            s, _, _ = slow_sign(Q); cases.append((f"random #{k} mono={int(monotone(Q))} sign={s:+.3f}", Q))
    for name, Q in cases:
        res = []
        for gb, ga in (([0.4], []), ([], [0.7]), ([0.3], [1.5]), ([1.0, 0.5], [0.2])):
            r = conds(Q, gb, ga); res.append(f"[{gb}|{ga}] E1min={r['E1']:+.2e} E2min={r['E2']:+.2e}")
        print(name); [print("    " + x) for x in res]
        print(flush=True)
