"""Referee recomputation of the SEL-8 witnesses (T1-sharp refutation) with exact Walsh integers and mpmath
interval arithmetic, plus the SVD-lemma witness and the real-leaf witness.

Boolean witness, built from the verbal description (0-based data coordinates y_0..y_3):
  G2 = 1 - 2*1[y = (+1,+1,-1,+1)],  G1 = -y_2 * (1 - 2*1[y = (+1,-1,+1,-1)]);
  selector of r bits, A_2 = {x = (+1,...,+1)} (one point), A_1 = rest.
T1-sharp value: H(p) + sum_k p_k [H(q_k) + H(G_k)], q_k = ahat_k^2 / p_k.
"""
import numpy as np
import mpmath as mp
from fractions import Fraction
from rlib import wht

iv = mp.iv
iv.dps = 60
LN2 = iv.log(iv.mpf(2))


def ilog2(x):
    return iv.log(x) / LN2


def H_from_W_interval(W, nvars):
    vals, cnt = np.unique(np.abs(np.asarray(W, dtype=np.int64)), return_counts=True)
    tot = iv.mpf(0)
    four_n = iv.mpf(4) ** nvars
    for v, c in zip(vals, cnt):
        v = int(v)
        if v == 0:
            continue
        p = iv.mpf(v * v) / four_n
        tot += int(c) * (-p * ilog2(p))
    return tot


def H_fracs_interval(masses_counts):
    tot = iv.mpf(0)
    for m, c in masses_counts:
        if m == 0:
            continue
        p = iv.mpf(m.numerator) / iv.mpf(m.denominator)
        tot += c * (-p * ilog2(p))
    return tot


def leaf(pt, base):
    t = np.empty(16, dtype=np.int64)
    for i in range(16):
        y = tuple(-1 if (i >> j) & 1 else 1 for j in range(4))
        t[i] = base(y) * (-1 if y == pt else 1)
    return t


G2 = leaf((1, 1, -1, 1), lambda y: 1)
G1 = leaf((1, -1, 1, -1), lambda y: -y[2])
print("E[G1] =", Fraction(int(G1.sum()), 16), " E[G2] =", Fraction(int(G2.sum()), 16),
      " E[G1 G2] =", Fraction(int(np.dot(G1, G2)), 16))
W1 = wht(G1); W2 = wht(G2)
print("supports: |supp G1hat| =", int(np.count_nonzero(W1)), " |supp G2hat| =", int(np.count_nonzero(W2)))
HG1 = H_from_W_interval(W1, 4); HG2 = H_from_W_interval(W2, 4)


def omega(G1, G2):
    """Omega(G1,G2) = 4H(V) - 4 sum_T G1hat V hat log2(1/G1hat^2) + H(G1) - H(G2) - 4, V=(G1-G2)/2,
    H(V) unnormalised.  Derived independently by the referee (see REFEREE.md, SEL-8)."""
    g1 = wht(G1).astype(np.float64) / 16
    g2 = wht(G2).astype(np.float64) / 16
    v = (g1 - g2) / 2
    def Hu(c):
        c2 = c * c
        m = c2 > 0
        return float(np.sum(c2[m] * np.log2(1 / c2[m])))
    m = g1 != 0
    cross = float(np.sum(g1[m] * v[m] * np.log2(1 / (g1[m] ** 2))))
    return 4 * Hu(v) - 4 * cross + Hu(g1) - Hu(g2) - 4


Om = omega(G1, G2)
print("Omega(G1,G2) from the formula = %.10f" % Om)

for r in list(range(1, 19)):
    N = 1 << r
    lab = np.zeros(N, dtype=np.int64); lab[0] = 1
    Bm = np.where(lab[:, None] == 1, G2[None, :], G1[None, :])     # (N, 16)
    F = Bm.T.reshape(-1)
    WF = wht(F)
    HF = H_from_W_interval(WF, r + 4)
    p2 = Fraction(1, N); p1 = 1 - p2
    # a_2 = 1_{x = all +1}: ahat_2(S) = 1/N for every S; a_1 = 1 - a_2: ahat_1(0) = 1 - 1/N, ahat_1(S) = -1/N
    Hq2 = iv.mpf(r)
    Hq1 = H_fracs_interval([(p1 * p1 / p1, 1), (Fraction(1, N * N) / p1, N - 1)])
    Hp = H_fracs_interval([(p1, 1), (p2, 1)])
    rhs = Hp + iv.mpf(p1.numerator) / p1.denominator * (Hq1 + HG1) + iv.mpf(1) / N * (Hq2 + HG2)
    gap = HF - rhs
    print("r=%2d  excess in [%s, %s]   excess/p2 = %.8f   (Omega %.8f)" % (
        r, mp.nstr(gap.a, 14), mp.nstr(gap.b, 14), float(gap.a) * N, Om), flush=True)

# ---------------- SVD lemma witness ----------------
mp.mp.dps = 40
M = mp.matrix([[2, -1], [-1, -1]]) / mp.sqrt(7)
U, S, V = mp.svd_r(M)
s = [S[i] ** 2 for i in range(2)]
def Hmp(ps):
    return -sum(p * mp.log(p, 2) for p in ps if p > 0)
lhs = Hmp([M[i, j] ** 2 for i in range(2) for j in range(2)])
rhs = Hmp(s) + sum(s[k] * (Hmp([U[i, k] ** 2 for i in range(2)]) + Hmp([V[k, j] ** 2 for j in range(2)])) for k in range(2))
print("SVD lemma witness M=[[2,-1],[-1,-1]]/sqrt7: singular values^2 =", [mp.nstr(x, 12) for x in s],
      " gap = H(|M|^2) - RHS =", mp.nstr(lhs - rhs, 15))
# reconstruct check
Mr = U * mp.diag(S) * V
print("   SVD reconstruction error:", mp.nstr(mp.mnorm(Mr - M, 1), 5))

# ---------------- real-leaf witness ----------------
e = mp.mpf("0.05")
# x in {+-1}^2 (bits 0,1), y one bit (bit 2); A_1 = {x = (1,1)} = index 0
Fv = []
for i in range(8):
    xi = i & 3
    y = -1 if (i >> 2) & 1 else 1
    if xi == 0:
        Fv.append(mp.cos(e) - mp.sin(e) * y)
    else:
        Fv.append(mp.sin(e) + mp.cos(e) * y)
coef = []
for S in range(8):
    c = mp.mpf(0)
    for i in range(8):
        sg = -1 if bin(S & i).count("1") % 2 else 1
        c += Fv[i] * sg
    coef.append(c / 8)
norm = sum(c * c for c in coef)
HF = Hmp([c * c for c in coef])
p1, p2 = mp.mpf(1) / 4, mp.mpf(3) / 4
Hq1 = mp.mpf(2)                                         # point cell: uniform on 4 sets
Hq2 = Hmp([mp.mpf(3) / 4] + [mp.mpf(1) / 12] * 3)       # complement: ahat(0)=3/4, ahat(S)=-1/4
HG = Hmp([mp.cos(e) ** 2, mp.sin(e) ** 2])
bound = Hmp([p1, p2]) + p1 * (Hq1 + HG) + p2 * (Hq2 + HG)
print("real-leaf witness: ||F||^2 =", mp.nstr(norm, 15), " H(F) - T1sharp value =", mp.nstr(HF - bound, 12))
