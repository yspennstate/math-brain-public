"""Referee check of SEL-5 (reuse representation), SEL-5b (effective branches) and SEL-6 (exact H > 4I witness)."""
import numpy as np
from fractions import Fraction
from rlib import wht, popcount_table, I_exact

rng = np.random.default_rng(7)


def chi_table(S, n):
    idx = np.arange(1 << n)
    pc = np.zeros(1 << n, dtype=np.int64)
    for j in range(n):
        if (S >> j) & 1:
            pc += (idx >> j) & 1
    return 1 - 2 * (pc & 1)


# ---------- SEL-5 (i)-(iii) ----------
ok = True
for n in range(1, 8):
    for trial in range(20):
        f = rng.choice([-1, 1], size=1 << n)
        branches = []
        for b in range(1 << n):
            Sb = b                      # S_b = {i : b_i = -1} = bits set in index b
            sgn = -1 if bin(Sb).count("1") % 2 else 1
            Bb = f[b] * sgn * chi_table(Sb, n)
            branches.append(Bb)
            ok &= (Bb[b] == f[b])
        Bm = np.array(branches)
        G = Bm @ Bm.T                   # Gram matrix, integer
        ok &= np.array_equal(G, (1 << n) * np.eye(1 << n, dtype=np.int64))
        # f(x) = B_x(x)
        ok &= np.array_equal(np.array([Bm[x, x] for x in range(1 << n)]), f)
print("SEL-5 one-node representation (n<=7, 140 random f): B_b(b)=f(b), Gram = 2^n I:", ok)


# ---------- SEL-5 one-bit recursion ----------
def decompose(G, S, n):
    """Full function = chi_S * G with G not depending on the variables in S.  Split on a relevant variable v
    of G: chi_S G = Mux_v(chi_S G_+, -v chi_S G_-).  Returns (#leaves, all nodes orthogonal & exact?, leaves
    are signed characters?)."""
    idx = np.arange(1 << n)
    full = chi_table(S, n) * G
    rel = [v for v in range(n) if np.any(G != G[idx ^ (1 << v)])]
    assert not any((S >> v) & 1 for v in rel)
    if not rel:                                   # G constant: signed character leaf
        return 1, True, len(np.flatnonzero(wht(full))) == 1
    v = rel[0]
    xv = 1 - 2 * ((idx >> v) & 1)
    Gp = np.where(xv == 1, G, G[idx ^ (1 << v)])   # G|_{v=+1}, independent of v
    Gm = np.where(xv == -1, G, G[idx ^ (1 << v)])  # G|_{v=-1}, independent of v
    Bp = chi_table(S, n) * Gp
    Bm = -xv * chi_table(S, n) * Gm               # = chi_{S+v} * (-Gm)
    recon = np.where(xv == 1, Bp, Bm)
    good = (int(np.dot(Bp, Bm)) == 0) and np.array_equal(recon, full)
    l1, o1, c1 = decompose(Gp, S, n)
    l2, o2, c2 = decompose(-Gm, S | (1 << v), n)
    return l1 + l2, good and o1 and o2, c1 and c2


ok2 = True
for n in range(1, 7):
    for trial in range(10):
        f = rng.choice([-1, 1], size=1 << n)
        leaves, orth, lv = decompose(f, 0, n)
        ok2 &= orth and lv
print("SEL-5 one-bit recursion: every node exact with full-cube-orthogonal branches, leaves signed characters:", ok2)

# ---------- SEL-6 ----------
# g(x0,x1,x2,x3) = x2 if x2 = x3; x0 if (x2,x3) = (1,-1); x1 if (x2,x3) = (-1,1)
g = np.empty(16, dtype=np.int64)
for i in range(16):
    x = [(-1 if (i >> j) & 1 else 1) for j in range(4)]
    if x[2] == x[3]:
        g[i] = x[2]
    elif (x[2], x[3]) == (1, -1):
        g[i] = x[0]
    else:
        g[i] = x[1]
W = wht(g)
coef = {S: Fraction(int(W[S]), 16) for S in range(16) if W[S] != 0}
print("ghat:", {tuple(j for j in range(4) if (S >> j) & 1): str(c) for S, c in coef.items()})


def H_dyadic(Wv, n):
    """Exact entropy when every nonzero |W| is a power of two: -p log2 p = k 2^-k for p = 2^-k."""
    tot = Fraction(0)
    for v in np.abs(Wv):
        v = int(v)
        if v == 0:
            continue
        assert v & (v - 1) == 0, "non-dyadic coefficient"
        j = v.bit_length() - 1
        k = 2 * n - 2 * j         # p = v^2 / 4^n = 2^(2j - 2n)
        tot += Fraction(k, 1 << k)
    return tot


Hg = H_dyadic(W, 4); Ig = I_exact(g, 4)
print("H(g) =", Hg, " I(g) =", Ig, " E g =", Fraction(int(W[0]), 16))


def compose(outer, n_out, inner, n_in):
    """outer(inner(block_1), ..., inner(block_n_out)) on n_out*n_in variables; block r = bits r*n_in..."""
    N = 1 << (n_out * n_in)
    idx = np.arange(N, dtype=np.int64)
    oidx = np.zeros(N, dtype=np.int64)
    for r in range(n_out):
        blk = (idx >> (r * n_in)) & ((1 << n_in) - 1)
        val = inner[blk]                       # +-1
        oidx |= ((val == -1).astype(np.int64)) << r
    return outer[oidx]


gg = compose(g, 4, g, 4)            # 16 variables
Wgg = wht(gg)
Hgg = H_dyadic(Wgg, 16); Igg = I_exact(gg, 16)
print("H(g o g) =", Hgg, "(claim 15/2)   I(g o g) =", Igg, "(claim 9/4)   E =", Fraction(int(Wgg[0]), 1 << 16))
# composition lemma check on the spectrum (multiset): T ~ ghat^2, S_i ~ ghat^2 for i in T
from collections import Counter
pred = Counter()
outer = {S: c * c for S, c in coef.items()}
inner_masses = [c * c for c in coef.values()]
import itertools
for T, mT in outer.items():
    k = bin(T).count("1")
    for combo in itertools.product(inner_masses, repeat=k):
        m = mT
        for q in combo:
            m *= q
        pred[m] += 1
act = Counter()
for v in Wgg:
    v = int(v)
    if v:
        act[Fraction(v * v, 1 << 32)] += 1
print("composition lemma: predicted spectral multiset == brute force for g o g:", pred == act)
# G = g o (g o g) by the lemma, and also (g o g) o g, exact
H3a = Hg + Ig * Hgg; I3a = Ig * Igg
H3b = Hgg + Igg * Hg; I3b = Igg * Ig
print("H(G) =", H3a, "=", H3b, "  I(G) =", I3a, "  4I(G) =", 4 * I3a, "  H/I =", H3a / I3a,
      "  H > 4I:", H3a > 4 * I3a)
seq = []
Hk, Ik = Hg, Ig
for k in range(1, 6):
    seq.append(str(Hk / Ik))
    Hk, Ik = Hg + Ig * Hk, Ig * Ik
print("H/I along g^(k):", seq, " formula 6(1-(2/3)^k):", [str(6 * (1 - Fraction(2, 3) ** k)) for k in range(1, 6)])
