"""het_record.py - a gate fed inputs of different biases, scored by potentials.

For g on uniform bits put U_V(g) = G(g) - V J(g).  For a gate F with INDEPENDENT inputs g_1..g_k of biases p_j,
    G(F(g)) = G_pvec(F) + sum_j J^(j) G(g_j),   J(F(g)) = sum_j J^(j) J(g_j),   so   U' = G_pvec(F) + sum_j J^(j) U_j,
with w_T the normalised p-vector-biased Fourier weights of F and J^(j) = sum_{T contains j} w_T.  If W is the value
table of homogeneous towers (tower_vi.py --dump), any g with U_V(g) + W(p_g) > 0 gives sup H/I > V.

Step 1 builds a menu of read-once formulas over AND/OR/XOR/NOT with inputs of unequal bias: for each reachable bias
the largest potential U_c at V = c (the record), by dynamic programming over pairs.  It prints max U_c(p) + W(p)
(positive would already be a new bound from a read-once entry function).
Step 2 splits the inputs of the gate in LIB (first line "n hex") into classes by their uniform influence, gives each
class a menu bias, and prints the largest Phi = G_pvec + sum_classes J_class U_c(p_class) + W(p').
usage: python het_record.py W_table.txt GATE.txt [rounds] [npts]
"""
import sys

import numpy as np

C = 6.521845710923


def and_stats(pa, pb):
    """gate fires (-1) iff both inputs are -1; returns p', G, J1, J2 for arrays pa, pb."""
    sa, sb = np.sqrt(pa * (1 - pa)), np.sqrt(pb * (1 - pb))
    q = pa * pb
    var = 4 * q * (1 - q)
    w1 = 4 * pb * pb * sa * sa / var
    w2 = 4 * pa * pa * sb * sb / var
    w12 = 4 * sa * sa * sb * sb / var
    G = -(w1 * np.log2(w1) + w2 * np.log2(w2) + w12 * np.log2(w12))
    return q, G, w1 + w12, w2 + w12


def xor_stats(pa, pb):
    ma, mb = 1 - 2 * pa, 1 - 2 * pb
    var = 1 - ma * ma * mb * mb
    w1 = (1 - ma * ma) * mb * mb / var
    w2 = ma * ma * (1 - mb * mb) / var
    w12 = (1 - ma * ma) * (1 - mb * mb) / var
    with np.errstate(divide="ignore", invalid="ignore"):
        G = -(np.where(w1 > 0, w1 * np.log2(np.where(w1 > 0, w1, 1)), 0) + np.where(w2 > 0, w2 * np.log2(np.where(w2 > 0, w2, 1)), 0)
              + w12 * np.log2(w12))
    return (1 - ma * mb) / 2, G, w1 + w12, w2 + w12


def build_menu(rounds, nbins=1200, span=9.0, use_xor=True):
    """returns arrays p, U (best potential found per bin of log-odds, the exact p of that best kept)."""
    best = {}

    def offer(p, U):
        t = np.log2(p / (1 - p))
        ok = (np.abs(t) < span) & np.isfinite(U)
        b = np.round((t[ok] + span) / (2 * span) * nbins).astype(int)
        for bi, pi, ui in zip(b, p[ok], U[ok]):
            cur = best.get(bi)
            if cur is None or ui > cur[1]:
                best[bi] = (pi, ui)

    offer(np.array([0.5]), np.array([-C]))
    for r in range(rounds):
        items = sorted(best.values())
        p = np.array([x[0] for x in items])
        U = np.array([x[1] for x in items])
        p = np.concatenate([p, 1 - p])          # NOT
        U = np.concatenate([U, U])
        A, B = np.meshgrid(p, p, indexing="ij")
        UA, UB = np.meshgrid(U, U, indexing="ij")
        q, G, J1, J2 = and_stats(A, B)
        offer(q.ravel(), (G + J1 * UA + J2 * UB).ravel())
        if use_xor:
            q, G, J1, J2 = xor_stats(A, B)
            offer(q.ravel(), (G + J1 * UA + J2 * UB).ravel())
        offer(p, U)
        print("menu round %d: %d biases" % (r + 1, len(best)), flush=True)
    items = sorted(best.values())
    p = np.array([x[0] for x in items])
    U = np.array([x[1] for x in items])
    return np.concatenate([p, 1 - p]), np.concatenate([U, U])


def gate_stats(vals, n, pvec):
    """p-vector-biased transform; returns p', G, per-input normalised influences J^(j)."""
    a = vals.copy()
    for i in range(n):
        p = pvec[i]
        s = np.sqrt(p * (1 - p))
        a = a.reshape(-1, 2, 1 << i)
        lo, hi = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = (1 - p) * lo + p * hi
        a[:, 1, :] = s * (hi - lo)
        a = a.reshape(-1)
    mean = a[0]
    var = 1 - mean * mean
    w = a * a / var
    w[0] = 0
    G = float(-(w[w > 1e-300] * np.log2(w[w > 1e-300])).sum())
    idx = np.arange(1 << n)
    Jj = np.array([w[(idx >> i) & 1 == 1].sum() for i in range(n)])
    return (1 - mean) / 2, G, Jj


def main():
    wt = np.loadtxt(sys.argv[1], comments="#")
    t, W = wt[:, 0], wt[:, 1]
    rounds = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    npts = int(sys.argv[4]) if len(sys.argv) > 4 else 41

    def Wof(p):
        p = np.clip(p, 1e-12, 1 - 1e-12)
        return np.interp(np.clip(np.log2(p / (1 - p)), t[0], t[-1]), t, W)

    mp, mU = build_menu(rounds)
    slack = mU + Wof(mp)
    order = np.argsort(-slack)
    print("menu: %d biases; largest U_c(p) + W(p):" % len(mp))
    for i in order[:8]:
        print("   p=%.9f  U_c=%.6f  W=%.6f  sum=%+.6f" % (mp[i], mU[i], Wof(mp[i]), slack[i]))

    with open(sys.argv[2], encoding="utf-8") as fh:
        n, hx = fh.readline().split()
    n = int(n)
    tab = int(hx, 16)
    bits = np.unpackbits(np.frombuffer(tab.to_bytes((1 << n) // 8, "little"), dtype=np.uint8), bitorder="little")
    vals = 1.0 - 2.0 * bits.astype(np.float64)
    p0, G0, J0 = gate_stats(vals, n, [0.5] * n)
    cls = {}
    for i, x in enumerate(J0):
        cls.setdefault(round(float(x), 9), []).append(i)
    groups = list(cls.values())
    print("gate n=%d  uniform: p'=%.9f G=%.9f J=%.9f; %d input classes:" % (n, p0, G0, J0.sum(), len(groups)),
          [(len(g), round(float(J0[g[0]]), 6)) for g in groups])
    if len(groups) != 2:
        print("this scan handles two classes; stopping")
        return
    # candidate biases: menu points nearest to an even spread in (0.06, 0.94)
    targets = np.linspace(0.06, 0.94, npts)
    cand = sorted(set(int(np.argmin(np.abs(mp - x))) for x in targets) | {int(np.argmin(np.abs(mp - 0.5)))})
    rows = []
    for ia in cand:
        for ib in cand:
            pv = np.empty(n)
            pv[groups[0]] = mp[ia]
            pv[groups[1]] = mp[ib]
            pp, G, Jj = gate_stats(vals, n, pv)
            Ja, Jb = Jj[groups[0]].sum(), Jj[groups[1]].sum()
            phi = G + Ja * mU[ia] + Jb * mU[ib] + float(Wof(pp))
            rows.append((phi, mp[ia], mp[ib], pp, G, Ja, Jb, mU[ia], mU[ib]))
    rows.sort(key=lambda r: -r[0])
    print("largest Phi over %d x %d bias pairs (0 at the uniform point by construction):" % (len(cand), len(cand)))
    for r in rows[:25]:
        print("   Phi=%+.6f  p_A=%.6f p_B=%.6f -> p'=%.6f  G=%.5f J_A=%.5f J_B=%.5f  U_A=%.5f U_B=%.5f" % r)


if __name__ == "__main__":
    main()
