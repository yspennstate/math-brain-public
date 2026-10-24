"""Multi-scale witnesses for a general Boolean f, by brute force (n <= 16).

For each coordinate i, order the other coordinates by co-occurrence with i in the spectral sample,
c_ij = P(S contains i and j) = sum_{S > {i,j}} fhat(S)^2 (ties by index), and cut the order into nested shells.  A witness
is a function of U = S - i; its cost is H(S_i | W) = sum over the values w of phi(P(U in w, i notin S), P(U in w, i in S)),
and B_i <= H(S_i | W) for every witness.  Witnesses compared:
  level    |U|                                      (the level statistic of section 5, O5)
  first    position of the first ordered coordinate present in U
  geo      geometric shells (sizes 1, 2, 4, ...): the first shell that U meets and U on that shell
  eq       shells of equal co-occurrence (rel. tol 1e-9): the first shell that U meets and U on that shell
           (geo and eq shells are cut into chunks of at most ceil(2 log2(1/eps_i)) coordinates, so no witness sees all of U)
  geo+lev, eq+lev   the pair (shell witness, |U|)
  cell1, cell2      U on the m nearest coordinates, m = ceil(c log2(1/eps_i)), c = 1, 2, and whether U has more outside
On a read-once formula whose co-occurrence classes are the tree distances, eq is the branch witness of section 5b and costs
exactly B_i.  Usage: python general_witness.py OUTJSON
"""
import sys, json, math
import numpy as np

LOG2 = math.log(2)


def phi_vec(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    t = a + b
    out = np.zeros_like(t)
    m = (a > 0) & (b > 0)
    x, y = a[m], b[m]
    out[m] = (x * np.log1p(y / x) + y * np.log1p(x / y)) / LOG2
    return out


def walsh(T):
    a = T.astype(float).copy()
    n = len(a).bit_length() - 1
    for k in range(n):
        a = a.reshape(-1, 2, 1 << k)
        u, w = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :], a[:, 1, :] = u + w, u - w
        a = a.reshape(-1)
    return a / len(a)


def cond_entropy(label, pU, pUi):
    _, inv = np.unique(label, return_inverse=True)
    A = np.bincount(inv, weights=pU)
    Bv = np.bincount(inv, weights=pUi)
    return float(phi_vec(A, Bv).sum())


def popcount(x):
    x = x.astype(np.int64)
    c = np.zeros_like(x)
    while np.any(x):
        c += x & 1
        x >>= 1
    return c


def shell_label(lo, order, shells, r_first):
    """shells: list of (start, end) position ranges covering 0..len(order)-1. Label = (index of first shell hit, pattern)."""
    none = len(order)
    lab = np.full(len(lo), -1, dtype=np.int64)
    width = max(e - s for s, e in shells)
    for k, (s, e) in enumerate(shells):
        hit = (r_first >= s) & (r_first < e)
        if not np.any(hit):
            continue
        pat = np.zeros(int(hit.sum()), dtype=np.int64)
        sub = lo[hit]
        for pos in range(s, e):
            pat |= ((sub >> order[pos]) & 1) << (pos - s)
        lab[hit] = (k + 1) * (1 << width) + pat
    lab[r_first == none] = 0
    return lab


def analyse(T, name):
    n = len(T).bit_length() - 1
    p = walsh(T) ** 2
    idx = np.arange(1 << n, dtype=np.int64)
    pc = popcount(idx)
    H = float(-(p[p > 0] * np.log2(p[p > 0])).sum())
    keys = ["B", "level", "first", "geo", "eq", "geo+lev", "eq+lev", "cell1", "cell2", "geo-count", "eq-count"]
    neq = []
    tot = {k: 0.0 for k in keys}
    I = 0.0
    for i in range(n):
        bit = 1 << i
        lo = idx[(idx & bit) == 0]
        pU, pUi = p[lo], p[lo | bit]
        eps = float(pUi.sum())
        I += eps
        if eps <= 0:
            continue
        tot["B"] += float(phi_vec(pU, pUi).sum())
        lev = pc[lo]
        tot["level"] += cond_entropy(lev, pU, pUi)
        others = [j for j in range(n) if j != i]
        c = {j: float(pUi[((lo >> j) & 1) == 1].sum()) for j in others}
        order = sorted(others, key=lambda j: (-c[j], j))
        none = len(order)
        r = np.full(len(lo), none, dtype=np.int64)
        for k in range(none - 1, -1, -1):
            r[((lo >> order[k]) & 1) == 1] = k
        tot["first"] += cond_entropy(r, pU, pUi)
        geo, s = [], 0
        size = 1
        while s < none:
            geo.append((s, min(none, s + size)))
            s += size
            size *= 2
        eqs, s = [], 0
        while s < none:
            e = s + 1
            while e < none and abs(c[order[e]] - c[order[s]]) <= 1e-9 * max(c[order[s]], 1e-300):
                e += 1
            eqs.append((s, e))
            s = e
        L2 = math.log2(1 / eps) if eps < 1 else 0.0
        cap = max(1, math.ceil(2 * L2))  # a shell never shows more than 2 log2(1/eps_i) coordinates at once

        def capped(sh):
            out = []
            for s0, e0 in sh:
                while e0 - s0 > cap:
                    out.append((s0, s0 + cap))
                    s0 += cap
                out.append((s0, e0))
            return out
        geo_raw, eqs_raw = list(geo), list(eqs)
        geo, eqs = capped(geo), capped(eqs)
        # count profiles: |U cap shell| for every shell (no positions); eq shells uncapped here, since only counts show
        cnt_geo = np.zeros(len(lo), dtype=np.int64)
        for k, (s0, e0) in enumerate(geo_raw):
            cnt = np.zeros(len(lo), dtype=np.int64)
            for pos in range(s0, e0):
                cnt += (lo >> order[pos]) & 1
            cnt_geo = cnt_geo * (n + 1) + cnt
        cnt_eq = np.zeros(len(lo), dtype=np.int64)
        for k, (s0, e0) in enumerate(eqs_raw):
            cnt = np.zeros(len(lo), dtype=np.int64)
            for pos in range(s0, e0):
                cnt += (lo >> order[pos]) & 1
            cnt_eq = cnt_eq * (n + 1) + cnt
        tot["geo-count"] += cond_entropy(cnt_geo, pU, pUi)
        tot["eq-count"] += cond_entropy(cnt_eq, pU, pUi)
        neq.append(len(eqs_raw))
        Lg = shell_label(lo, order, geo, r)
        Le = shell_label(lo, order, eqs, r)
        tot["geo"] += cond_entropy(Lg, pU, pUi)
        tot["eq"] += cond_entropy(Le, pU, pUi)
        tot["geo+lev"] += cond_entropy(Lg * (n + 1) + lev, pU, pUi)
        tot["eq+lev"] += cond_entropy(Le * (n + 1) + lev, pU, pUi)
        for cc, key in ((1, "cell1"), (2, "cell2")):
            m = min(none, max(1, math.ceil(cc * L2)))
            pat = np.zeros(len(lo), dtype=np.int64)
            for pos in range(m):
                pat |= ((lo >> order[pos]) & 1) << pos
            outside = np.zeros(len(lo), dtype=np.int64)
            for pos in range(m, none):
                outside |= (lo >> order[pos]) & 1
            tot[key] += cond_entropy(pat * 2 + outside, pU, pUi)
    row = dict(name=name, n=n, I=I, H_over_I=H / I, log2_inv_mean_eps=math.log2(n / I), max_eq_shells=max(neq) if neq else 0)
    for k in keys:
        row[k + "_over_I"] = tot[k] / I
    return row


# ---------- families (index bit j set <=> x_j = -1 <=> "true") ----------
def table(n, fn):
    idx = np.arange(1 << n, dtype=np.int64)
    bits = ((idx[:, None] >> np.arange(n)) & 1).astype(bool)
    return np.where(fn(bits), -1, 1).astype(np.int8)


def tribes(w, s):
    return table(w * s, lambda b: np.any(np.all(b.reshape(-1, s, w), axis=2), axis=1))


def majority(n):
    return table(n, lambda b: b.sum(1) > n // 2)


def ball(n, r):
    return table(n, lambda b: b.sum(1) <= r)


def x0bent(m):
    def fn(b):
        ip = np.zeros(len(b), dtype=np.int64)
        for k in range(m):
            ip ^= (b[:, 1 + 2 * k] & b[:, 2 + 2 * k]).astype(np.int64)
        return (b[:, 0].astype(np.int64) ^ ip).astype(bool)
    return table(2 * m + 1, fn)


def andor(d, top="AND"):
    def ev(b, lo, depth, typ):
        if depth == 0:
            return b[:, lo]
        half = 1 << (depth - 1)
        nxt = "OR" if typ == "AND" else "AND"
        l, r = ev(b, lo, depth - 1, nxt), ev(b, lo + half, depth - 1, nxt)
        return (l & r) if typ == "AND" else (l | r)
    return table(1 << d, lambda b: ev(b, 0, d, top))


def rmaj33():
    def fn(b):
        m = [b[:, 3 * k:3 * k + 3].sum(1) >= 2 for k in range(3)]
        return (m[0].astype(int) + m[1] + m[2]) >= 2
    return table(9, fn)


def or_of_maj3(s):
    return table(3 * s, lambda b: np.any(b.reshape(-1, s, 3).sum(2) >= 2, axis=1))


def maj3_of_and(w):
    return table(3 * w, lambda b: np.all(b.reshape(-1, 3, w), axis=2).sum(1) >= 2)


def or_of_maj(s, m):
    return table(s * m, lambda b: np.any(b.reshape(-1, s, m).sum(2) > m // 2, axis=1))


def and2_or3_and2():
    def fn(b):
        blocks = b.reshape(-1, 2, 3, 2)          # AND2 of OR3 of AND2
        return np.all(np.any(np.all(blocks, axis=3), axis=2), axis=1)
    return table(12, fn)


def address(k):
    n = k + (1 << k)
    def fn(b):
        a = np.zeros(len(b), dtype=np.int64)
        for t in range(k):
            a |= b[:, t].astype(np.int64) << t
        return b[np.arange(len(b)), k + a]
    return table(n, fn)


def bent_pm(m):
    idx = np.arange(1 << m)
    s = np.zeros(1 << m, dtype=np.int64)
    for k in range(0, m - 1, 2):
        s ^= ((idx >> k) & 1) & ((idx >> (k + 1)) & 1)
    return (1 - 2 * s).astype(np.int8)


def mux(g0, g1):
    """selector = lowest bit: F[z + 2y] = g_z(y) (the layout of SEL-selector-interference/referee_code/check_falsifiers.py)"""
    F = np.empty(2 * len(g0), dtype=np.int8)
    F[0::2], F[1::2] = g0, g1
    return F


def x002(m):
    """X002 parity splice (odd m): g0(y) = bent(y_j xor y_m, j < m), g1 = (-1)^{y_m} g0"""
    idx = np.arange(1 << m)
    ym = (idx >> (m - 1)) & 1
    tt = np.zeros(1 << m, dtype=np.int64)
    for j in range(m - 1):
        tt |= (((idx >> j) & 1) ^ ym) << j
    g0 = bent_pm(m - 1)[tt]
    return mux(g0, np.where(ym == 1, -g0, g0).astype(np.int8))


def x003(k, r):
    """X003 sparse activation splice: children 1 + A(b - 1), 1 + A(b' - 1), A = 1{z = 0} on r fresh bits, b' = b flipped at 0"""
    b = bent_pm(k)
    bp = b.copy()
    bp[0] = -bp[0]
    idx = np.arange(1 << (k + r))
    A = (idx >> k) == 0
    x = idx & ((1 << k) - 1)
    return mux(np.where(A, b[x], 1).astype(np.int8), np.where(A, bp[x], 1).astype(np.int8))


def x009(m):
    """X009 sparse bent perturbation F(y, t) = g(y) (1 - 2 t 1{y = 0}), bent g on m bits, t = bit m"""
    g = bent_pm(m)
    F = np.concatenate([g, g]).astype(np.int8)
    F[1 << m] = -F[1 << m]
    return F


def random_dnf(n, terms, width, seed):
    rng = np.random.default_rng(seed)
    T = [(rng.choice(n, width, replace=False), rng.integers(0, 2, width).astype(bool)) for _ in range(terms)]
    def fn(b):
        out = np.zeros(len(b), dtype=bool)
        for vars_, sg in T:
            out |= np.all(b[:, vars_] == sg, axis=1)
        return out
    return table(n, fn)


def random_table(n, seed):
    rng = np.random.default_rng(seed)
    return np.where(rng.integers(0, 2, 1 << n) == 1, -1, 1).astype(np.int8)


def random_threshold(n, seed):
    rng = np.random.default_rng(seed)
    w = rng.exponential(1.0, n)
    return table(n, lambda b: (b * w).sum(1) > w.sum() / 2)


def main():
    fams = [("tribes 2x4", lambda: tribes(2, 4)), ("tribes 3x3", lambda: tribes(3, 3)), ("tribes 3x4", lambda: tribes(3, 4)),
            ("tribes 4x3", lambda: tribes(4, 3)), ("tribes 4x4", lambda: tribes(4, 4)), ("tribes 3x5", lambda: tribes(3, 5)),
            ("majority 9", lambda: majority(9)), ("majority 13", lambda: majority(13)), ("majority 15", lambda: majority(15)),
            ("ball 12 r1", lambda: ball(12, 1)), ("ball 12 r3", lambda: ball(12, 3)), ("ball 16 r2", lambda: ball(16, 2)),
            ("x0*bent m4", lambda: x0bent(4)), ("x0*bent m7", lambda: x0bent(7)),
            ("andor d3", lambda: andor(3)), ("andor d4", lambda: andor(4)),
            ("rmaj 3o3", rmaj33), ("OR4 of MAJ3", lambda: or_of_maj3(4)), ("OR5 of MAJ3", lambda: or_of_maj3(5)),
            ("MAJ3 of AND4", lambda: maj3_of_and(4)), ("MAJ3 of AND5", lambda: maj3_of_and(5)),
            ("address k3", lambda: address(3)), ("OR3 of MAJ3", lambda: or_of_maj(3, 3)), ("OR3 of MAJ5", lambda: or_of_maj(3, 5)),
            ("OR2 of MAJ7", lambda: or_of_maj(2, 7)), ("AND2-OR3-AND2", and2_or3_and2),
            ("X002 m5", lambda: x002(5)), ("X002 m7", lambda: x002(7)), ("X003 k4 r8", lambda: x003(4, 8)),
            ("X009 m6", lambda: x009(6)), ("X009 m10", lambda: x009(10)), ("X009 m14", lambda: x009(14))]
    fams += [(f"dnf n12 t{t} w{w} s{s}", (lambda t=t, w=w, s=s: random_dnf(12, t, w, s))) for (t, w, s) in
             ((6, 3, 1), (6, 3, 2), (10, 4, 3), (10, 4, 4), (20, 5, 5), (4, 2, 6))]
    fams += [(f"threshold n14 s{s}", (lambda s=s: random_threshold(14, s))) for s in (1, 2)]
    fams += [(f"random n10 s{s}", (lambda s=s: random_table(10, s))) for s in (1, 2, 3)]
    rows = []
    hdr = "family               n   I      H/I    B/I    level  first  geo    eq     geo+l  eq+l   cell1  cell2  gcnt   ecnt  #eq"
    print(hdr, flush=True)
    for name, mk in fams:
        R = analyse(mk(), name)
        rows.append(R)
        print(f"{name:20s} {R['n']:2d} {R['I']:6.3f} {R['H_over_I']:6.3f} {R['B_over_I']:6.3f} {R['level_over_I']:6.3f} "
              f"{R['first_over_I']:6.3f} {R['geo_over_I']:6.3f} {R['eq_over_I']:6.3f} {R['geo+lev_over_I']:6.3f} "
              f"{R['eq+lev_over_I']:6.3f} {R['cell1_over_I']:6.3f} {R['cell2_over_I']:6.3f} {R['geo-count_over_I']:6.3f} "
              f"{R['eq-count_over_I']:6.3f} {R['max_eq_shells']:3d}", flush=True)
    json.dump(dict(rows=rows), open(sys.argv[1], "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
