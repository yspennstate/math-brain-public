"""Checks of the two lemmas in arXiv 2611.12795 (Huffstutler, Miloschewsky, Podder), written from the statements.

Lemma 4.  G : {0,1}^n -> {0,1} total, U_b a nonempty subset of G^{-1}(b) of density delta_b, FC(G, x) <= gamma_b
          on U_b.  Then some coordinate has influence I_i(G) >= delta_0 delta_1 / (gamma_0 gamma_1).
Lemma 3.  A partial f with a feasible classical-adversary family lambda of cost at most A has completions
          G_t = 1[g < t], g(z) = min(1, min_{a in A1} d_a(z)), with 4 lambda^x a fractional certificate of G_t at
          every x of the domain for 1/4 <= t <= 3/4, and I(G_t) <= 4A for some such t.

Part A  Lemma 4 as stated: FC by linear programming, every pair of thresholds (gamma_0, gamma_1).
Part B  Inequality (4) inside the proof, N_C <= sum_i w_i b_i on every subcube, with the weights, the sets H_y
        and the marked pairs built as in the proof.
Part C  The determinant argument on n = 3: det(M) is not zero, and every monomial m of least degree has
        exponent beta_i <= b_i and weight at least N_C.
Part D  Lemma 3, with lambda from the classical-adversary linear programme.
"""
import itertools
import random
import sys

import numpy as np
from scipy.optimize import linprog

TOL = 1e-7


def bits(n):
    return range(1 << n)


def fc_all(G, n):
    """FC(G, x) and an optimal certificate for every x."""
    N = 1 << n
    val = [0.0] * N
    cert = [None] * N
    cache = {}
    for x in bits(n):
        diffs = tuple(sorted({x ^ y for y in bits(n) if G[y] != G[x]}))
        if diffs not in cache:
            # keep only minimal difference sets
            mins = [d for d in diffs if not any((e & d) == e and e != d for e in diffs)]
            A = np.zeros((len(mins), n))
            for r, d in enumerate(mins):
                for i in range(n):
                    if d >> i & 1:
                        A[r, i] = -1.0
            res = linprog(np.ones(n), A_ub=A, b_ub=-np.ones(len(mins)), bounds=[(0, None)] * n, method="highs")
            assert res.status == 0
            cache[diffs] = (float(res.fun), np.round(res.x, 10))
        val[x], cert[x] = cache[diffs]
    return val, cert


def influences(G, n):
    N = 1 << n
    return [sum(1 for x in bits(n) if G[x] != G[x ^ (1 << i)]) / N for i in range(n)]


def part_a(G, n, stats):
    N = 1 << n
    val, _ = fc_all(G, n)
    imax = max(influences(G, n))
    side = [sorted(set(round(val[x], 9) for x in bits(n) if G[x] == b)) for b in (0, 1)]
    for g0 in side[0]:
        d0 = sum(1 for x in bits(n) if G[x] == 0 and val[x] <= g0 + 1e-9) / N
        for g1 in side[1]:
            d1 = sum(1 for x in bits(n) if G[x] == 1 and val[x] <= g1 + 1e-9) / N
            bound = d0 * d1 / (g0 * g1)
            stats["a_cases"] += 1
            ratio = imax / bound
            if ratio < stats["a_min"]:
                stats["a_min"] = ratio
                stats["a_arg"] = (n, "".join(map(str, G)), g0, g1)
            assert imax >= bound - TOL, ("Lemma 4 fails", n, G, g0, g1, imax, bound)


def subcubes(n):
    full = (1 << n) - 1
    for J in range(1, 1 << n):
        fixed = full ^ J
        base = fixed
        while True:
            yield J, base
            if base == 0:
                break
            base = (base - 1) & fixed


def points(J, base):
    sub = J
    while True:
        yield base | sub
        if sub == 0:
            break
        sub = (sub - 1) & J


def build_marks(G, n):
    val, cert = fc_all(G, n)
    U = [[x for x in bits(n) if G[x] == b] for b in (0, 1)]
    gam = [max(val[x] for x in U[b]) for b in (0, 1)]
    w = 2 * gam[0] / len(U[1]) * sum(cert[x] for x in U[1])
    assert w.sum() <= 2 * gam[0] * gam[1] + TOL
    H = {}
    marked = set()
    for y in U[0]:
        Hy = [i for i in range(n) if cert[y][i] > w[i] + 1e-9]
        H[y] = Hy
        good = [x for x in U[1] if sum(cert[x][i] for i in Hy) < 1 - 1e-9]
        assert 2 * len(good) >= len(U[1]), ("fewer than half marked", G, y)
        for x in good:
            marked.add((x, y))
            # a marked x keeps its value when any subset of H_y is flipped
            for r in range(1, len(Hy) + 1):
                for S in itertools.combinations(Hy, r):
                    m = sum(1 << i for i in S)
                    assert G[x ^ m] == 1
    return w, H, marked, U


def part_b(G, n, stats):
    w, H, marked, U = build_marks(G, n)
    assert 2 * len(marked) >= len(U[0]) * len(U[1])
    counted = 0
    for J, base in subcubes(n):
        NC = sum(1 for x in points(J, base) if G[x] == 1 and (x, x ^ J) in marked)
        rhs = 0.0
        for i in range(n):
            if J >> i & 1:
                bi = sum(1 for x in points(J, base) if G[x] == 1 and G[x ^ (1 << i)] == 0)
                rhs += w[i] * bi
        stats["b_cubes"] += 1
        if NC:
            stats["b_nonzero"] += 1
            stats["b_minslack"] = min(stats["b_minslack"], rhs - NC)
        assert NC <= rhs + TOL, ("inequality (4) fails", n, G, J, base, NC, rhs)
        counted += NC
    assert counted == len(marked)


def part_c(G, n, stats):
    import sympy as sp
    w, H, marked, U = build_marks(G, n)
    t = sp.symbols("t0:%d" % n)
    for J, base in subcubes(n):
        X1 = [x for x in points(J, base) if G[x] == 1]
        if not X1:
            continue
        Jl = [i for i in range(n) if J >> i & 1]
        M = sp.Matrix(len(X1), len(X1), lambda a, b: sp.Mul(*[t[i] for i in Jl if (X1[a] >> i & 1) == (X1[b] >> i & 1)]))
        d = sp.expand(M.det(method="berkowitz"))
        assert d != 0, ("det(M) = 0", G, J, base)
        P = sp.Poly(d, *t)
        low = min(sum(mon) for mon in P.monoms())
        NC = sum(1 for x in X1 if (x, x ^ J) in marked)
        b = [sum(1 for x in X1 if G[x ^ (1 << i)] == 0) if J >> i & 1 else 0 for i in range(n)]
        for mon in P.monoms():
            if sum(mon) == low:
                stats["c_monomials"] += 1
                assert all(mon[i] <= b[i] for i in range(n)), ("beta_i > b_i", G, J, base, mon, b)
                assert sum(w[i] * mon[i] for i in range(n)) >= NC - TOL, ("wt(m) < N_C", G, J, base, mon, NC)
        stats["c_dets"] += 1


def cadv_lp(f, n):
    """Classical adversary: minimise T with |lambda^x|_1 <= T and sum_{i in D(x,y)} min(lambda^x_i, lambda^y_i) >= 1."""
    dom = sorted(f)
    A1 = [x for x in dom if f[x] == 1]
    A0 = [x for x in dom if f[x] == 0]
    idx = {x: k for k, x in enumerate(dom)}
    pairs = [(a, b) for a in A1 for b in A0]
    nl = len(dom) * n
    nm = len(pairs) * n
    nv = nl + nm + 1
    c = np.zeros(nv)
    c[-1] = 1.0
    rows, rhs = [], []
    for x in dom:
        r = np.zeros(nv)
        r[idx[x] * n: idx[x] * n + n] = 1.0
        r[-1] = -1.0
        rows.append(r)
        rhs.append(0.0)
    for k, (a, b) in enumerate(pairs):
        tot = np.zeros(nv)
        for i in range(n):
            mv = nl + k * n + i
            if (a ^ b) >> i & 1:
                for x in (a, b):
                    r = np.zeros(nv)
                    r[mv] = 1.0
                    r[idx[x] * n + i] = -1.0
                    rows.append(r)
                    rhs.append(0.0)
                tot[mv] = -1.0
        rows.append(tot)
        rhs.append(-1.0)
    res = linprog(c, A_ub=np.array(rows), b_ub=np.array(rhs), bounds=[(0, None)] * nv, method="highs")
    assert res.status == 0
    lam = {x: np.round(res.x[idx[x] * n: idx[x] * n + n], 10) for x in dom}
    return float(res.fun), lam, A1, A0


def part_d(f, n, stats):
    A, lam, A1, A0 = cadv_lp(f, n)
    N = 1 << n

    def d(a, z):
        return sum(lam[a][i] for i in range(n) if (a ^ z) >> i & 1)

    g = [min(1.0, min(d(a, z) for a in A1)) for z in bits(n)]
    assert all(abs(g[a]) < TOL for a in A1) and all(abs(g[b] - 1) < TOL for b in A0)
    for z in bits(n):
        assert sum(max(0.0, g[z ^ (1 << i)] - g[z]) for i in range(n)) <= A + TOL, ("upward variation above CAdv", f, z)
    L = sum(abs(g[z] - g[z ^ (1 << i)]) for z in bits(n) for i in range(n)) / N
    assert L <= 2 * A + TOL
    cuts = sorted(set([0.25, 0.75] + [v for v in g if 0.25 < v < 0.75]))
    best = None
    for lo, hi in zip(cuts, cuts[1:]):
        tt = (lo + hi) / 2
        G = [1 if g[z] < tt else 0 for z in bits(n)]
        assert all(G[x] == f[x] for x in f)
        for x in f:
            for y in bits(n):
                if G[y] != G[x]:
                    assert 4 * d(x, y) >= 1 - TOL, ("4 lambda is not a certificate", f, x, y, tt)
        I = sum(influences(G, n))
        best = I if best is None else min(best, I)
    assert best <= 2 * L + TOL and best <= 4 * A + TOL
    stats["d_cases"] += 1
    stats["d_maxratio"] = max(stats["d_maxratio"], best / A)


def named(n):
    N = 1 << n
    out = {}
    out["AND"] = [1 if x == N - 1 else 0 for x in range(N)]
    out["OR"] = [1 if x else 0 for x in range(N)]
    out["PARITY"] = [bin(x).count("1") & 1 for x in range(N)]
    out["MAJ"] = [1 if 2 * bin(x).count("1") > n else 0 for x in range(N)]
    out["DICT"] = [x & 1 for x in range(N)]
    out["THR2"] = [1 if bin(x).count("1") >= 2 else 0 for x in range(N)]
    if n == 6:
        out["TRIBES2x3"] = [1 if any((x >> (2 * k)) & 3 == 3 for k in range(3)) else 0 for x in range(N)]
        out["TRIBES3x2"] = [1 if any((x >> (3 * k)) & 7 == 7 for k in range(2)) else 0 for x in range(N)]
        out["ADDR2"] = [(x >> (2 + (x & 3))) & 1 for x in range(N)]
    return out


def main():
    rng = random.Random(42)
    stats = dict(a_cases=0, a_min=1e9, a_arg=None, b_cubes=0, b_nonzero=0, b_minslack=1e9, c_dets=0, c_monomials=0, d_cases=0, d_maxratio=0.0)

    nf = 0
    for n in (2, 3):
        for code in range(1, (1 << (1 << n)) - 1):
            G = [(code >> x) & 1 for x in range(1 << n)]
            part_a(G, n, stats)
            part_b(G, n, stats)
            nf += 1
    print("parts A, B: all %d nonconstant functions on 2 and 3 bits" % nf, flush=True)
    for n in (3, 4, 5, 6, 7):
        for name, G in named(n).items():
            if len(set(G)) == 2:
                part_a(G, n, stats)
                if n <= 6:
                    part_b(G, n, stats)
    print("parts A, B: named functions (AND, OR, parity, majority, dictator, threshold-2, tribes, address) on 3 to 7 bits", flush=True)
    for n, count in ((4, 1500), (5, 300), (6, 60)):
        done = 0
        while done < count:
            p = rng.choice((0.1, 0.25, 0.5, 0.5, 0.75, 0.9))
            G = [1 if rng.random() < p else 0 for _ in range(1 << n)]
            if len(set(G)) < 2:
                continue
            part_a(G, n, stats)
            part_b(G, n, stats)
            done += 1
        print("parts A, B: %d random functions on %d bits (densities 0.1 to 0.9)" % (count, n), flush=True)
    print("part A: %d threshold pairs, Lemma 4 never fails; smallest max_i I_i * gamma_0 gamma_1 / (delta_0 delta_1) = %.4f at n = %d, G = %s, (gamma_0, gamma_1) = (%g, %g)" % (stats["a_cases"], stats["a_min"], stats["a_arg"][0], stats["a_arg"][1], stats["a_arg"][2], stats["a_arg"][3]), flush=True)
    print("part B: inequality (4) on %d subcubes (%d with N_C > 0), never fails; smallest slack where N_C > 0: %.4f" % (stats["b_cubes"], stats["b_nonzero"], stats["b_minslack"]), flush=True)

    for code in range(1, 255):
        G = [(code >> x) & 1 for x in range(8)]
        part_c(G, 3, stats)
    print("part C: all 254 nonconstant functions on 3 bits: %d determinants, none zero; %d least-degree monomials, each with beta_i <= b_i and weight >= N_C" % (stats["c_dets"], stats["c_monomials"]), flush=True)

    for n, count in ((3, 150), (4, 150), (5, 40)):
        done = 0
        while done < count:
            q = rng.choice((0.3, 0.5, 0.8, 1.0))
            f = {x: rng.randint(0, 1) for x in range(1 << n) if rng.random() < q}
            if len(set(f.values())) < 2 or len(f) > 20:
                continue
            part_d(f, n, stats)
            done += 1
    print("part D: Lemma 3 on %d random partial functions on 3 to 5 bits; largest min_t I(G_t) / CAdv(f) = %.4f (bound 4)" % (stats["d_cases"], stats["d_maxratio"]), flush=True)
    print("all assertions passed")


if __name__ == "__main__":
    main()
