"""Referee checks of SEL-7 (orthogonal leaves, arbitrary cells), SEL-14 (sign averaging), SEL-15 (balanced
two-cell cut) and SEL-15c (the class M_4).

Instance: selector cube of a bits, labels L[b] in {0..K-1} (cells), Boolean leaves G_k on n data bits.
F[b + 2^a y] = G_{L[b]}[y].
"""
import itertools
import math
import numpy as np
from fractions import Fraction
from rlib import wht, ent, popcount_table

rng = np.random.default_rng(12345)
TOL = 1e-9
WORST = {}


def rec(name, v, info=None):
    if name not in WORST or v > WORST[name][0]:
        WORST[name] = (v, info)


def build_F(L, leaves, a, n):
    N = 1 << a
    D = 1 << n
    G = np.asarray(leaves)[np.asarray(L)]           # (N, D)
    return G.T.reshape(-1).copy()


def fspec(T, nv):
    W = wht(np.asarray(T, dtype=np.int64))
    P = W.astype(np.float64) ** 2 / float(4 ** nv)
    return W, P


def cell_data(L, a, K):
    N = 1 << a
    pc = popcount_table(a)
    out = []
    for k in range(K):
        ind = (np.asarray(L) == k).astype(np.int64)
        p = ind.sum() / N
        Wa = wht(ind)                                # ahat * N
        ahat2 = Wa.astype(np.float64) ** 2 / float(N * N)
        q = ahat2 / p
        h = 2 * ind - 1
        Wh = wht(h)
        Ph = Wh.astype(np.float64) ** 2 / float(N * N)
        Hh = float(ent(Ph))
        Ih = float((Ph * pc).sum())
        Hplus = float(ent(Ph[1:]))                   # nonempty part, unnormalised
        Var = 1 - Ph[0]
        out.append(dict(p=p, ahat2=ahat2, q=q, Hq=float(ent(q)), Hh=Hh, Ih=Ih, Hplus=Hplus, Var=Var))
    return out


def leaf_data(leaves, n):
    pc = popcount_table(n)
    out = []
    for G in leaves:
        W, P = fspec(G, n)
        out.append(dict(P=P, H=float(ent(P)), I=float((P * pc).sum()), mean=float(np.mean(G))))
    return out


def check_sel7(L, leaves, a, n, label, strong_ok=True):
    """All SEL-7 statements for one instance (leaves must be pairwise orthogonal Boolean)."""
    K = len(leaves)
    N, Dn = 1 << a, 1 << n
    lv = np.asarray(leaves)
    gram = lv @ lv.T
    assert np.array_equal(gram, Dn * np.eye(K, dtype=np.int64)), "leaves not orthonormal"
    F = build_F(L, leaves, a, n)
    W, P = fspec(F, a + n)
    Pm = P.reshape(Dn, N)                            # [T, S]
    mu = Pm.sum(axis=0)
    R = Pm.sum(axis=1)
    cd = cell_data(L, a, K)
    ld = leaf_data(leaves, n)
    p = np.array([c["p"] for c in cd])
    mu_pred = sum(c["ahat2"] for c in cd)
    R_pred = sum(c["p"] * l["P"] for c, l in zip(cd, ld))
    rec("SEL7(i) |mu - sum ahat^2|", float(np.abs(mu - mu_pred).max()), label)
    rec("SEL7(i) |R - sum p G^2|", float(np.abs(R - R_pred).max()), label)
    HF = float(ent(P))
    Hp = float(ent(p))
    sub = float(ent(mu) + ent(R))
    rhs = 2 * Hp + sum(c["p"] * (c["Hq"] + l["H"]) for c, l in zip(cd, ld))
    rec("SEL7(ii) H(F)-H(mu)-H(R)", HF - sub, label)
    rec("SEL7(ii) H(mu)+H(R)-[2H(p)+sum p(Hq+HG)]", sub - rhs, label)
    # (iii) exact influences
    idx = np.arange(1 << (a + n))
    Isel = sum(Fraction(int(np.sum(F != F[idx ^ (1 << i)])), 1 << (a + n)) for i in range(a))
    Idat = sum(Fraction(int(np.sum(F != F[idx ^ (1 << (a + j))])), 1 << (a + n)) for j in range(n))
    D4 = sum(Fraction(int(np.sum(c_ind != c_ind[np.arange(N) ^ (1 << i)])), N)
             for k in range(K) for i in range(a)
             for c_ind in [(np.asarray(L) == k).astype(np.int64)]) / 4
    Ilf = sum(Fraction(int(np.sum(np.asarray(L) == k)), N) *
              sum(Fraction(int(np.sum(lv[k] != lv[k][np.arange(Dn) ^ (1 << j)])), Dn) for j in range(n))
              for k in range(K))
    rec("SEL7(iii) Isel != D (exact)", 0.0 if Isel == D4 else 1.0, label)
    rec("SEL7(iii) Idata != sum p I(G) (exact)", 0.0 if Idat == Ilf else 1.0, label)
    IF = float(Isel + Idat)
    # (iv) ordinary closure with the actual ratios
    Cs = max([c["Hh"] / c["Ih"] if c["Ih"] > 1e-12 else 0.0 for c in cd])
    Cg = max([l["H"] / l["I"] if l["I"] > 1e-12 else 0.0 for l in ld])
    rec("SEL7(iv) H(F)-max(Cs+6,Cg)I(F)", HF - max(Cs + 6, Cg) * IF, label)
    # (v) strong closure if leaves balanced
    if strong_ok and all(abs(l["mean"]) < 1e-12 for l in ld):
        Cs2 = max([c["Hplus"] / (c["Ih"] - c["Var"]) if c["Ih"] - c["Var"] > 1e-12 else 0.0 for c in cd])
        Cg2 = max([l["H"] / (l["I"] - 1) if l["I"] - 1 > 1e-12 else 0.0 for l in ld])
        rec("SEL7(v) H(F)-max(max(Cs,4)+2,Cg)(I-1)", HF - max(max(Cs2, 4) + 2, Cg2) * (IF - 1), label)
    # SEL-8 sharp form excess (diagnostic only)
    sharp = Hp + sum(c["p"] * (c["Hq"] + l["H"]) for c, l in zip(cd, ld))
    rec("diag: H(F) - C010 value (T1-sharp excess)", HF - sharp, label)
    # SEL-15 balanced two-cell
    if K == 2 and abs(cd[0]["p"] - 0.5) < 1e-12:
        h = np.where(np.asarray(L) == 0, 1, -1)
        Wh, Ph = fspec(h, a)
        Hh = float(ent(Ph))
        b15 = 2 + Hh / 2 + (ld[0]["H"] + ld[1]["H"]) / 2
        rec("SEL15(ii) H(F) - [2+H(h)/2+avg H(G)]", HF - b15, label)
        Ih = Fraction(int(np.sum(Wh.astype(object) ** 2 * popcount_table(a).astype(object))), 4 ** a)
        IG = [sum(Fraction(int(np.sum(lv[k] != lv[k][np.arange(Dn) ^ (1 << j)])), Dn) for j in range(n)) for k in range(2)]
        rec("SEL15(ii) I(F) identity fails (exact)", 0.0 if (Isel + Idat) == Ih / 2 + (IG[0] + IG[1]) / 2 else 1.0, label)
    return HF, IF


def check_sel14(L, leaves, a, n, label):
    """E over leaf signs of H(F_eps) <= H(p)+sum p(Hq+HG); E I_sel(F_eps) = D (exact)."""
    K = len(leaves)
    N, Dn = 1 << a, 1 << n
    cd = cell_data(L, a, K)
    ld = leaf_data(leaves, n)
    p = np.array([c["p"] for c in cd])
    sharp = float(ent(p)) + sum(c["p"] * (c["Hq"] + l["H"]) for c, l in zip(cd, ld))
    lv = np.asarray(leaves)
    Hs = []
    Isel_sum = Fraction(0)
    idx = np.arange(1 << (a + n))
    signs = list(itertools.product([1, -1], repeat=K))
    for eps in signs:
        lvs = lv * np.asarray(eps)[:, None]
        F = build_F(L, lvs, a, n)
        W, P = fspec(F, a + n)
        Hs.append(float(ent(P)))
        Isel_sum += sum(Fraction(int(np.sum(F != F[idx ^ (1 << i)])), 1 << (a + n)) for i in range(a))
    EH = float(np.mean(Hs))
    rec("SEL14 E_eps H(F_eps) - C010 value", EH - sharp, label)
    D = Fraction(0)
    for k in range(K):
        ind = (np.asarray(L) == k)
        for i in range(a):
            D += Fraction(int(np.sum(ind != ind[np.arange(N) ^ (1 << i)])), N)
    D = D / 4
    rec("SEL14 E I_sel != D (exact)", 0.0 if Isel_sum / len(signs) == D else 1.0, label)


# ---------------- exhaustive n_total <= 4 ----------------
def all_tables(nv):
    M = 1 << nv
    codes = np.arange(1 << M, dtype=np.int64)
    return 1 - 2 * ((codes[:, None] >> np.arange(M)[None, :]) & 1)


def exhaustive():
    cnt7 = cnt15 = cnt14 = 0
    for ntot in (2, 3, 4):
        T = all_tables(ntot)
        for a in range(1, ntot):
            n = ntot - a
            N, Dn = 1 << a, 1 << n
            for F in T:
                G = F.reshape(Dn, N).T                      # G[b, y]
                uniq, L = np.unique(G, axis=0, return_inverse=True)
                L = np.asarray(L).reshape(-1)
                K = len(uniq)
                # SEL-14 on the equal-branch partition (any leaves), skip big K for time
                if K <= 4 and rng.random() < 0.25:
                    check_sel14(L, uniq, a, n, ("exh14", ntot, a)); cnt14 += 1
                gram = uniq @ uniq.T
                if np.array_equal(gram, Dn * np.eye(K, dtype=np.int64)):
                    check_sel7(L, uniq, a, n, ("exh7", ntot, a)); cnt7 += 1
                    if K == 2 and np.sum(L == 0) * 2 == N:
                        cnt15 += 1
    print("exhaustive: SEL-7 instances", cnt7, " (balanced two-cell SEL-15 instances", cnt15, ")  SEL-14 instances", cnt14, flush=True)


# ---------------- random larger instances ----------------
def random_orthogonal_family(n, K, rng, base=None, tries=4000):
    Dn = 1 << n
    G1 = base if base is not None else rng.choice([-1, 1], size=Dn)
    fam = [np.asarray(G1, dtype=np.int64)]
    t = 0
    while len(fam) < K and t < tries:
        t += 1
        flip = np.zeros(Dn, dtype=bool)
        flip[rng.choice(Dn, size=Dn // 2, replace=False)] = True
        cand = np.where(flip, -fam[0], fam[0])
        if all(int(np.dot(cand, g)) == 0 for g in fam):
            fam.append(cand)
    return fam if len(fam) == K else None


def random_partition(a, K, rng, kind):
    N = 1 << a
    if kind == "random":
        L = rng.integers(0, K, size=N)
        L[rng.permutation(N)[:K]] = np.arange(K)     # nonempty cells
        return L
    if kind == "ball":                                # cells by Hamming weight thresholds
        w = popcount_table(a)
        cuts = np.sort(rng.choice(np.arange(1, a + 1), size=K - 1, replace=False))
        return np.searchsorted(cuts, w, side="right")
    if kind == "point":                               # one point cells + rest
        L = np.zeros(N, dtype=np.int64)
        pts = rng.choice(N, size=K - 1, replace=False)
        L[pts] = np.arange(1, K)
        return L
    if kind == "balanced2":
        L = np.zeros(N, dtype=np.int64)
        L[rng.choice(N, size=N // 2, replace=False)] = 1
        return L


def bent_table(m):
    idx = np.arange(1 << m)
    s = np.zeros(1 << m, dtype=np.int64)
    for k in range(0, m - 1, 2):
        s ^= ((idx >> k) & 1) & ((idx >> (k + 1)) & 1)
    return 1 - 2 * s


def maj3_pair():
    # data y1..y4 (bits 0..3); g+ = Maj(y1,y2,y3), g- = Maj(y1,-y2,y4)
    out = []
    for sgn, last in ((1, 2), (-1, 3)):
        t = np.empty(16, dtype=np.int64)
        for i in range(16):
            y = [(-1 if (i >> j) & 1 else 1) for j in range(4)]
            t[i] = 1 if (y[0] + sgn * y[1] + y[last]) > 0 else -1
        out.append(t)
    return out


def randoms():
    cnt = 0
    for a in (2, 3, 4, 5):
        for n in (3, 4, 5):
            for kind in ("random", "ball", "point", "balanced2"):
                for K in (2, 3, 4):
                    if kind == "balanced2" and K != 2:
                        continue
                    if kind == "ball" and K - 1 > a:
                        continue
                    for rep in range(6):
                        base = None
                        r = rng.random()
                        if r < 0.3:
                            base = bent_table(n) if n % 2 == 0 else np.concatenate([bent_table(n - 1)] * 2)
                        fam = random_orthogonal_family(n, K, rng, base=base)
                        if fam is None:
                            continue
                        if rng.random() < 0.4:            # balanced leaves variant: multiply by a character
                            pass
                        L = random_partition(a, K, rng, kind)
                        check_sel7(L, fam, a, n, ("rand7", a, n, kind, K)); cnt += 1
                        if K <= 3 and a + n <= 8:
                            check_sel14(L, fam, a, n, ("rand14", a, n, kind, K))
    # Maj3 pair with balanced cuts and arbitrary cuts
    mp_ = maj3_pair()
    assert int(np.dot(mp_[0], mp_[1])) == 0
    for a in (1, 2, 3, 4):
        for rep in range(20):
            kind = "balanced2" if rep % 2 == 0 else "random"
            L = random_partition(a, 2, rng, kind)
            check_sel7(L, mp_, a, 4, ("maj3", a, kind)); cnt += 1
    # balanced leaves families: G1 chi_U (bent times characters) are balanced if U nonempty and bent*chi has mean...
    for n in (4, 6):
        b = bent_table(n)
        for a in (2, 3, 4):
            for rep in range(15):
                K = rng.integers(2, 5)
                Us = rng.choice(np.arange(1, 1 << n), size=K, replace=False)
                fam = []
                for U in Us:
                    idx = np.arange(1 << n)
                    pcU = np.zeros(1 << n, dtype=np.int64)
                    for j in range(n):
                        if (U >> j) & 1:
                            pcU += (idx >> j) & 1
                    fam.append(b * (1 - 2 * (pcU & 1)))
                lv = np.asarray(fam)
                if not np.array_equal(lv @ lv.T, (1 << n) * np.eye(K, dtype=np.int64)):
                    continue
                for kind in ("random", "balanced2" if K == 2 else "random", "point"):
                    L = random_partition(a, K, rng, kind)
                    check_sel7(L, fam, a, n, ("bentchi", n, a, kind, K)); cnt += 1
    print("random SEL-7/14/15 instances:", cnt, flush=True)


# ---------------- SEL-15c: random members of M_4 ----------------
def m4_members(maxvars=16, count=300):
    """Each member: (table, nvars).  Base: signed dictators on 1 variable.  Operation: h on fresh variables
    (a member), G1 = X, G2 = orthogonal partner sharing variables (either an independent member on disjoint
    variables, or Mux_h'(A, B)/Mux_h'(A, -B) pairs)."""
    pool = [(np.array([1, -1], dtype=np.int64), 1), (np.array([-1, 1], dtype=np.int64), 1)]
    out = []

    def embed(tab, nv, total, offset):
        idx = np.arange(1 << total)
        return tab[(idx >> offset) & ((1 << nv) - 1)]

    def op(h, nh, G1, G2, nG):
        # F(x,y) = ((1+h(x))/2) G1(y) + ((1-h(x))/2) G2(y), x low nh bits, y high nG bits
        tot = nh + nG
        hx = embed(h, nh, tot, 0)
        g1 = embed(G1, nG, tot, nh)
        g2 = embed(G2, nG, tot, nh)
        return np.where(hx == 1, g1, g2), tot

    attempts = 0

    def pick():
        # prefer small members so that compositions stay under maxvars
        sizes = np.array([nv for _, nv in pool], dtype=np.float64)
        w = 2.0 ** (-sizes)
        return pool[rng.choice(len(pool), p=w / w.sum())]

    while len(out) < count and attempts < 200 * count:
        attempts += 1
        h, nh = pick()
        mode = rng.integers(2)
        if mode == 0:     # G1, G2 on disjoint variable sets (orthogonal since both balanced)
            A, na = pick()
            B, nb = pick()
            nG = na + nb
            if nh + nG > maxvars:
                continue
            G1 = embed(A, na, nG, 0)
            G2 = embed(B, nb, nG, na)
        elif mode == 1:   # Mux_{h'}(A,B) and Mux_{h'}(A,-B): orthogonal, share all variables
            hp, nhp = pick()
            A, na = pick()
            B, nb = pick()
            if nh + nhp + max(na, nb) > maxvars:
                continue
            nd = max(na, nb)
            Ae = embed(A, na, nd, 0); Be = embed(B, nb, nd, 0)
            if int(np.dot(Ae, Be)) != 0:      # the operation needs orthogonal leaves
                continue
            G1, nG = op(hp, nhp, Ae, Be, nd)
            G2, _ = op(hp, nhp, Ae, -Be, nd)
        else:
            continue
        if int(np.dot(G1, G2)) != 0:
            continue
        if nh + nG > maxvars:
            continue
        F, tot = op(h, nh, G1, G2, nG)
        assert int(F.sum()) == 0
        pool.append((F, tot))
        pool.append((-F, tot))
        out.append((F, tot))
    return out


def sel15c():
    mem = m4_members()
    worst = -1e9
    worst2 = -1e9
    pc_cache = {}
    for F, nv in mem:
        W, P = fspec(F, nv)
        if nv not in pc_cache:
            pc_cache[nv] = popcount_table(nv)
        HF = float(ent(P)); IF = float((P * pc_cache[nv]).sum())
        worst = max(worst, HF - 4 * (IF - 1))
    print("SEL-15c: %d random members of M_4 (up to 16 variables): max H - 4(I-1) = %.3e" % (len(mem), worst), flush=True)
    rec("SEL15c H - 4(I-1)", worst, "M4")


if __name__ == "__main__":
    import sys
    if "--m4only" not in sys.argv:
        exhaustive()
        randoms()
        for k, (v, info) in sorted(WORST.items()):
            print("%-48s %.3e   at %s" % (k, v, info), flush=True)
    sel15c()
