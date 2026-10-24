"""Independent final checks for the P0291 theorem (symmetric star chain satisfies the supermodular time ordering).
(1) n = 5 LP test of (X(c1 t_k)) >=_sm (X(c2 t_k)) at several configurations and rate pairs (3^5 = 243 lattice points).
(2) Condition (C2) checked DIRECTLY: for n = 3 and n = 4, Phi computed from phi by conditional expectation
    (prefix via the reversed chain, suffix via the forward chain), then min over supermodular phi of
    2Phi11 + Phi22 + Phi33 - Phi12 - Phi13 - Phi21 - Phi31 and of Phi22 + Phi33 - Phi23 - Phi32.
    This does not go through the block reduction, so it is an independent check of the spectral step + (C1),(C2).
"""
import itertools
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog
from p0291_star_sm_lp import star, fdd, sm_gap, stationary

def check_n5():
    print("== (1) n=5 LP test")
    for (a, b) in ((1.0, 1.0), (3.0, 1.0), (1.0, 4.0)):
        Q = star(a, b); worst = -1
        for times in ([0, 0.5, 1, 1.5, 2], [0, 0.2, 1.0, 1.3, 3.0], [0, 1, 2, 4, 8]):
            for c1, c2 in ((0.5, 1.0), (1.0, 2.0), (2.0, 4.0)):
                g, _, _ = sm_gap(fdd(Q, [float(t) for t in times], c1), fdd(Q, [float(t) for t in times], c2)); worst = max(worst, g)
        print(f"   star a={a} b={b}: worst max(E2-E1) = {worst:+.3e} {'VIOLATION' if worst > 1e-9 else 'ok'}", flush=True)

def check_c2_direct(a, b, gaps_before, gaps_after):
    """gaps_before: gaps among prefix times ending at s_k; gaps_after: gaps among suffix times starting at s_{k+1}."""
    Q = star(a, b); m = 3; pi = stationary(Q)
    kb = len(gaps_before); ka = len(gaps_after); n = kb + ka + 2
    # reversed chain = Q (reversible); prefix law given X_{s_k}=x: product of P_{gap} backwards
    Pb = [expm(Q * g) for g in gaps_before]; Pa = [expm(Q * g) for g in gaps_after]
    pts = list(itertools.product(range(m), repeat=n)); idx = {x: i for i, x in enumerate(pts)}; N = len(pts)
    # Phi(x,y) = sum over prefix/suffix of prob * phi(prefix, x, y, suffix) -> linear functional in phi
    def phi_vec(x, y):
        c = np.zeros(N)
        for pre in itertools.product(range(m), repeat=kb):
            p = 1.0; cur = x
            for j in range(kb - 1, -1, -1):        # walk backwards from x through the prefix
                p *= Pb[j][cur, pre[j]]; cur = pre[j]
            for suf in itertools.product(range(m), repeat=ka):
                q = 1.0; cur2 = y
                for j in range(ka):
                    q *= Pa[j][cur2, suf[j]]; cur2 = suf[j]
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
    C1 = Phi[(1,1)] + Phi[(2,2)] - Phi[(1,2)] - Phi[(2,1)]                       # states 0,1,2 = values 1,2,3
    C2 = 2*Phi[(0,0)] + Phi[(1,1)] + Phi[(2,2)] - Phi[(0,1)] - Phi[(0,2)] - Phi[(1,0)] - Phi[(2,0)]
    out = []
    for name, vec in (("C1", C1), ("C2", C2)):
        res = linprog(vec, A_ub=A, b_ub=np.zeros(len(rows)), bounds=[(-1, 1)]*N, method="highs")
        out.append(f"{name} min={res.fun:+.3e}")
    print(f"   a={a} b={b} prefix gaps {gaps_before} suffix gaps {gaps_after}: " + ", ".join(out), flush=True)

if __name__ == "__main__":
    print("== (2) direct (C1),(C2) checks (must be >= 0)")
    for (a, b) in ((1.0, 1.0), (3.0, 1.0), (1.0, 4.0)):
        check_c2_direct(a, b, [0.4], [])
        check_c2_direct(a, b, [], [0.7])
        check_c2_direct(a, b, [0.3], [1.5])
        check_c2_direct(a, b, [2.0, 0.5], [0.2])
    check_n5()
