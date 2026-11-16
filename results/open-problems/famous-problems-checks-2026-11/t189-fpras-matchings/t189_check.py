# T189: brute-force tests on K_n (n = 4, 6, 8) of statements used in the FPRAS for perfect matchings
# (OpenAI, 23 Sep 2026; Liu-Meng, arXiv 2610.26803, whose numbering is used here).
#   A  (4.2), (4.4), (4.5): hole-ratio inequalities
#   B  (4.3) and Lemma 4.2: balanced activities, completion mu = lambda + B/D
#   C  (2.2): 2 Var(f) <= S(f)
#   D  Theorem 2.1: Var(f) <= C_pair E(f(M1) + g(M2)) for a between B and rB, B ultrametric.
#      The constant (10n)^80 r^9 cannot be probed; what is measured is the best constant
#      lam = inf E(f + g) / Var(f) as the spread t of the ultrametric grows, and the same quantity
#      for a weight that is not comparable to an ultrametric (heavy chordless cycle).
# Floating point throughout.
import itertools, math, sys
import numpy as np

def out(*a):
    print(*a, flush=True)

rng = np.random.default_rng(189)

# ---------- matchings and hole sums ----------
def hole_sums(a, n):
    """Zm[mask] = total weight of perfect matchings of the vertex set mask"""
    Zm = np.zeros(1 << n)
    Zm[0] = 1.0
    for mask in range(1, 1 << n):
        if bin(mask).count("1") % 2:
            continue
        i = (mask & -mask).bit_length() - 1
        rest = mask ^ (1 << i)
        s = 0.0
        m = rest
        while m:
            j = (m & -m).bit_length() - 1
            s += a[i, j]*Zm[rest ^ (1 << j)]
            m &= m - 1
        Zm[mask] = s
    return Zm

def g_of(Zm, n, U):
    full = (1 << n) - 1
    mask = full
    for u in U:
        mask ^= (1 << u)
    return Zm[mask]/Zm[full]

def bottleneck(lam, n):
    B = np.maximum(1.0, lam.copy())
    np.fill_diagonal(B, np.inf)
    for k in range(n):
        B = np.maximum(B, np.minimum(B[:, k:k+1], B[k:k+1, :]))
    np.fill_diagonal(B, 0.0)
    return B

def rand_sym(n, spread):
    a = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            a[i, j] = a[j, i] = 10.0**rng.uniform(-spread, spread)
    return a

def graph_like(n, p, eps):
    a = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            a[i, j] = a[j, i] = 1.0 if rng.random() < p else eps
    return a

# ---------- A ----------
out("A. hole-ratio inequalities")
worstA = dict(e42=-1e9, e44=-1e9, e45=-1e9); cnt = 0
eq4 = 0.0
for n in (4, 6, 8):
    for rep in range(150 if n < 8 else 60):
        a = rand_sym(n, [0.5, 2.0, 6.0][rep % 3]) if rep % 5 else graph_like(n, 0.5, 10.0**-rng.integers(1, 9))
        Zm = hole_sums(a, n)
        g = lambda U: g_of(Zm, n, U)
        for (i, j, u, v) in itertools.combinations(range(n), 4):
            lhs = g((i, j, u, v))
            rhs = g((i, j))*g((u, v)) + g((i, u))*g((j, v)) + g((i, v))*g((j, u))
            worstA['e42'] = max(worstA['e42'], lhs/rhs - 1)
            if n == 4:
                eq4 = max(eq4, abs(lhs/rhs - 1))
        for _ in range(40):
            k1 = 2*int(rng.integers(0, n//2 + 1)); k2 = 2*int(rng.integers(0, n//2 + 1))
            U1 = set(rng.choice(n, size=k1, replace=False).tolist()); U2 = set(rng.choice(n, size=k2, replace=False).tolist())
            sd = sorted(U1 ^ U2)
            if not sd:
                continue
            x = sd[int(rng.integers(len(sd)))]
            lhs = g(tuple(U1))*g(tuple(U2))
            rhs = sum(g(tuple(U1 ^ {x, y}))*g(tuple(U2 ^ {x, y})) for y in sd if y != x)
            worstA['e44'] = max(worstA['e44'], lhs/rhs - 1 if rhs > 0 else (0.0 if lhs == 0 else 1e9))
            C = set(rng.choice(n, size=2*int(rng.integers(0, n//2)), replace=False).tolist())
            free = [z for z in range(n) if z not in C]
            if len(free) >= 2:
                x, z = rng.choice(free, size=2, replace=False).tolist()
                worstA['e45'] = max(worstA['e45'], a[x, z]*g(tuple(C | {x, z}))/g(tuple(C)) - 1)
        cnt += 1
out("  %d activity matrices; (4.2) largest lhs/rhs - 1 = %.2e (n = 4 is an identity: deviation %.1e)" % (cnt, worstA['e42'], eq4))
out("  (4.4) largest lhs/rhs - 1 = %.2e ; (4.5) largest lhs/rhs - 1 = %.2e   (claims: <= 0)" % (worstA['e44'], worstA['e45']))

# ---------- B ----------
out("B. balanced activities and the completion")
def balance(a, n):
    Zm = hole_sums(a, n)
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            G[i, j] = G[j, i] = g_of(Zm, n, (i, j))
    s = np.ones(n)
    for sweep in range(2000):
        for i in range(n):
            r = max(G[i, j]/(s[i]*s[j]) for j in range(n) if j != i)
            s[i] *= r/0.5
        R = np.array([max(G[i, j]/(s[i]*s[j]) for j in range(n) if j != i) for i in range(n)])
        if R.min() >= 0.25 and R.max() <= 1.0:
            return s, R
    return None, None

mx2 = 0.0; mx4 = 0.0; mxsum = 0.0; mxZ = 0.0; nb = 0; fail = 0; minreal = 1.0
for n in (4, 6, 8):
    D = 1e8*(n + 1)**4
    for rep in range(120 if n < 8 else 50):
        a = rand_sym(n, [0.5, 2.0, 6.0][rep % 3]) if rep % 4 else graph_like(n, 0.5, 10.0**-rng.integers(1, 9))
        s, R = balance(a, n)
        if s is None:
            fail += 1
            continue
        nb += 1
        lam = a*np.outer(s, s)
        Zm = hole_sums(lam, n)
        B = bottleneck(lam, n)
        for (i, j) in itertools.combinations(range(n), 2):
            mx2 = max(mx2, g_of(Zm, n, (i, j))*B[i, j]/n)
        for U in itertools.combinations(range(n), 4):
            gU = g_of(Zm, n, U)
            for (i, j) in itertools.combinations(U, 2):
                mx4 = max(mx4, gU*B[i, j]/n)
        sm = sum(B[i, j]*g_of(Zm, n, (i, j)) for (i, j) in itertools.combinations(range(n), 2))
        mxsum = max(mxsum, sm/(math.comb(n, 2)*n))
        mu = lam + B/D
        Zmu = hole_sums(mu, n)[(1 << n) - 1]
        Zl = Zm[(1 << n) - 1]
        mxZ = max(mxZ, Zmu/Zl - 1)
        minreal = min(minreal, Zl/Zmu)
out("  balanced instances: %d (scaling did not converge on %d)" % (nb, fail))
out("  (4.3) largest g(U) B_ij / n: two holes %.3f, four holes %.3f   (claim: <= 1e5)" % (mx2, mx4))
out("  largest sum_ij B_ij g(ij) / (C(n,2) n) = %.3f (the proof bounds it by 1e5)" % mxsum)
out("  Lemma 4.2: largest Z_mu/Z_lambda - 1 = %.2e (claim: <= 1.0005e-3); smallest all-real probability %.12f" % (mxZ, minreal))

# ---------- pair chain ----------
def matchings(n):
    res = []
    def rec(vs, cur):
        if not vs:
            res.append(tuple(cur)); return
        i = vs[0]
        for k in range(1, len(vs)):
            j = vs[k]
            rec(vs[1:k] + vs[k+1:], cur + [(i, j)])
    rec(list(range(n)), [])
    return res

def build(n):
    Ms = matchings(n)
    idx = {frozenset(M): k for k, M in enumerate(Ms)}
    m = len(Ms)
    partner = np.zeros((m, n), dtype=int)
    for k, M in enumerate(Ms):
        for (i, j) in M:
            partner[k, i] = j; partner[k, j] = i
    # two-edge switches
    sw = []
    for k, M in enumerate(Ms):
        for e1, e2 in itertools.combinations(M, 2):
            (p, q), (u, v) = e1, e2
            rest = [e for e in M if e != e1 and e != e2]
            for new in ([(p, u), (q, v)], [(p, v), (q, u)]):
                k2 = idx[frozenset(tuple(sorted(e)) for e in new) | frozenset(rest)]
                if k < k2:
                    sw.append((k, k2))
    sw = np.array(sw)
    # cycle exchanges
    ex = []          # (i1, i2, k, j1, j2)
    for i1 in range(m):
        for i2 in range(m):
            if i1 == i2:
                continue
            seen = [False]*n; cycles = []
            for v in range(n):
                if seen[v] or partner[i1, v] == partner[i2, v]:
                    continue
                cyc = []; x = v; use1 = True
                while not seen[x]:
                    seen[x] = True; cyc.append(x)
                    x = partner[i1, x] if use1 else partner[i2, x]
                    use1 = not use1
                cycles.append(cyc)
            k = len(cycles)
            for cyc in cycles:
                S = set(cyc)
                n1 = frozenset(tuple(sorted((v, partner[i2, v] if v in S else partner[i1, v]))) for v in range(n))
                n2 = frozenset(tuple(sorted((v, partner[i1, v] if v in S else partner[i2, v]))) for v in range(n))
                ex.append((i1, i2, k, idx[n1], idx[n2]))
    return Ms, sw, np.array(ex)

def weights(Ms, a):
    w = np.array([math.prod(a[i, j] for (i, j) in M) for M in Ms])
    return w/w.sum()

def pair_gap(n, Ms, sw, ex, a, ridge=1e-13):
    m = len(Ms)
    pi = weights(Ms, a)
    sq = np.sqrt(pi)
    q = (1/3)*(1/math.comb(n//2, 2))*0.5
    Q = np.zeros((2*m, 2*m))
    # switches (first coordinate only), in variables u = sqrt(pi) f
    k1, k2 = sw[:, 0], sw[:, 1]
    mn = q*np.minimum(pi[k1], pi[k2])
    np.add.at(Q, (k1, k1), mn/pi[k1]); np.add.at(Q, (k2, k2), mn/pi[k2])
    c = mn/(sq[k1]*sq[k2])
    np.add.at(Q, (k1, k2), -c); np.add.at(Q, (k2, k1), -c)
    # cycle exchanges
    i1, i2, kk, j1, j2 = ex.T
    wt = (1/6)*pi[i1]*pi[i2]/kk
    cols = [(i1, 1.0/sq[i1]), (j1, -1.0/sq[j1]), (m + i2, 1.0/sq[i2]), (m + j2, -1.0/sq[j2])]
    for (ra, ca) in cols:
        for (rb, cb) in cols:
            np.add.at(Q, (ra, rb), wt*ca*cb)
    Qff, Qfg, Qgg = Q[:m, :m], Q[:m, m:], Q[m:, m:]
    S = Qff - Qfg @ np.linalg.solve(Qgg + ridge*np.eye(m), Qfg.T)
    S = (S + S.T)/2 + 10.0*np.outer(sq, sq)
    ev = np.linalg.eigvalsh(S)
    # switch-only gap for comparison (no second coordinate)
    Lf = Qff.copy()
    return ev[0], pi

def ultra(n, blocks, t):
    """B_ij = t^(depth of the smallest block containing i and j); blocks: nested lists of vertices"""
    B = np.ones((n, n))
    def rec(node, depth):
        vs = flat(node)
        for i in vs:
            for j in vs:
                if i != j:
                    B[i, j] = max(B[i, j], t**depth)
        if isinstance(node, list):
            for ch in node:
                if isinstance(ch, list):
                    rec(ch, depth + 1)
    def flat(node):
        return [node] if not isinstance(node, list) else [x for ch in node for x in flat(ch)]
    rec(blocks, 0)
    np.fill_diagonal(B, 0.0)
    return B

def is_ultra(B, n):
    return all(B[i, j] >= min(B[i, k], B[k, j]) - 1e-12 for i in range(n) for j in range(n) for k in range(n) if len({i, j, k}) == 3)

out("C, D. two-matching chain")
trees = {
    6: {"3+3": [[0, 1, 2], [3, 4, 5]], "2+2+2": [[0, 1], [2, 3], [4, 5]], "nested": [[[[[0, 1], 2], 3], 4], 5], "4+2": [[0, 1, 2, 3], [4, 5]], "5+1": [[0, 1, 2, 3, 4], 5]},
    8: {"4+4": [[0, 1, 2, 3], [4, 5, 6, 7]], "3+3+2": [[0, 1, 2], [3, 4, 5], [6, 7]], "nested": [[[[[[[0, 1], 2], 3], 4], 5], 6], 7], "3+5": [[0, 1, 2], [3, 4, 5, 6, 7]], "(2+2)+(3+1)": [[[0, 1], [2, 3]], [[4, 5, 6], 7]]},
}
for n in (6, 8):
    Ms, sw, ex = build(n)
    m = len(Ms)
    out("  n = %d: %d perfect matchings, %d switch pairs, %d cycle exchanges" % (n, m, len(sw), len(ex)))
    # C: (2.2)
    worst = -1e9
    for rep in range(30):
        a = rand_sym(n, [0.3, 1.5, 4.0][rep % 3])
        pi = weights(Ms, a)
        f = rng.normal(size=m)
        var = pi @ f**2 - (pi @ f)**2
        i1, i2, kk, j1, j2 = ex.T
        Sf = (pi[i1]*pi[i2]*(f[i1] - f[j1])**2).sum()
        worst = max(worst, 2*var/Sf - 1)
    out("    (2.2): largest 2 Var(f)/S(f) - 1 over 30 weights = %.3e (claim: <= 0)" % worst)
    # D
    for name, blocks in trees[n].items():
        row = []
        for r in (1.0, 4.0):
            vals = []
            for t in (1.0, 10.0, 1e2, 1e4, 1e6):
                B = ultra(n, blocks, t)
                assert is_ultra(B, n)
                chi = np.ones((n, n))
                if r > 1:
                    for i in range(n):
                        for j in range(i + 1, n):
                            chi[i, j] = chi[j, i] = rng.uniform(1.0, r)
                a = B*chi
                lam, pi = pair_gap(n, Ms, sw, ex, a)
                lam2, _ = pair_gap(n, Ms, sw, ex, a, ridge=1e-10)
                vals.append((lam, lam2))
            row.append("r=%g: " % r + " ".join("%.4f" % v[0] for v in vals) + "  (ridge check, largest change %.1e)" % max(abs(v[0] - v[1]) for v in vals))
        out("    ultrametric %-12s lam at t = 1, 10, 1e2, 1e4, 1e6:  %s" % (name, " | ".join(row)))
    # not comparable to an ultrametric: a chordless cycle of heavy edges
    vals = []
    for t in (1.0, 10.0, 1e2, 1e3, 1e4):
        a = np.ones((n, n)); np.fill_diagonal(a, 0.0)
        for i in range(6):
            j = (i + 1) % 6
            a[i, j] = a[j, i] = t
        lam, pi = pair_gap(n, Ms, sw, ex, a)
        vals.append(lam)
    out("    heavy 6-cycle, chords 1 (not ultrametric), lam at t = 1, 10, 1e2, 1e3, 1e4:  " + " ".join("%.3e" % v for v in vals))
out("done")
