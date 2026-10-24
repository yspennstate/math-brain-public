"""The gate inequality for named gates of larger fan-in, where enumerating NPN classes is out of reach.

Same statistic as gates6: the margin c_G(p) = -D_G(p) / (I(G;p)/4 - p_out(1-p_out)) that the gate asks of the
potential.  Arity 2's AND is the control.  Gates: majority, parity, AND/OR, tribes of several widths, the
bent (inner-product) function and bent-with-one-point-flipped (the family that breaks the per-coordinate
erasure bound), the iterated 3-majority, and the best functions the R hill climb found.
usage: bigates.py <npz> [nsym] [nrand]"""
import sys, time, json, itertools
import numpy as np
import gam

def spec(vals, ps):
    """biased spectrum of a gate given as +-1 values over 2^k inputs, at bias vector ps"""
    k = len(ps); n = 1 << k
    A = np.ones((1, 1))
    for p in ps:
        s2 = np.sqrt(p * (1 - p))
        M = np.array([[1 - p, p], [s2, -s2]])
        m = A.shape[0]
        A = np.einsum("si,Sx->sSix", M, A).reshape(2 * m, 2 * m)
    C = A @ vals
    return C

def stat(vals, ps, Gm):
    k = len(ps); n = 1 << k
    C = spec(vals, ps); pS = C * C
    Ht = -float((pS * np.log2(np.maximum(pS, 1e-300))).sum())
    SEL = np.array([[(S >> i) & 1 for i in range(k)] for S in range(n)], float)
    It = pS @ SEL
    p_out = float(np.clip((1 - C[0]) * 0.5, 0, 1))
    pa = np.asarray(ps, float); V = 4 * pa * (1 - pa)
    base = (Gm(pa) + gam.h2(V)) / V
    D = float(It @ base) - Ht - float(Gm(np.array([p_out]))[0])
    den = float(It.sum()) / 4.0 - p_out * (1 - p_out)
    return D, den, p_out

def gates():
    out = []
    def bits(k): return np.arange(1 << k)
    pop = lambda x: np.array([bin(int(i)).count("1") for i in x])
    out.append(("AND2", 2, np.where(bits(2) == 3, -1.0, 1.0)))
    for k in (3, 5, 7, 9):
        out.append(("MAJ%d" % k, k, 1.0 - 2.0 * (pop(bits(k)) > k // 2)))
    for k in (3, 4, 5, 6):
        out.append(("PAR%d" % k, k, 1.0 - 2.0 * (pop(bits(k)) & 1)))
    for k in (4, 6, 8):
        out.append(("AND%d" % k, k, np.where(bits(k) == (1 << k) - 1, -1.0, 1.0)))
    for w, s in ((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (4, 2)):
        k = w * s; x = bits(k); hit = np.zeros(1 << k, bool)
        for b in range(s):
            m = ((1 << w) - 1) << (b * w)
            hit |= ((x & m) == m)
        out.append(("TRIBES w%d s%d" % (w, s), k, np.where(hit, -1.0, 1.0)))
    for m in (2, 4, 6):                                  # bent (inner product) and bent + one flip
        M = 1 << m; xs = np.arange(M); half = m // 2
        u = xs & ((1 << half) - 1); v = xs >> half
        ip = np.array([bin(int(a) & int(b)).count("1") & 1 for a, b in zip(u, v)])
        g = 1.0 - 2.0 * ip
        out.append(("BENT%d" % m, m, g.copy()))
        f = np.concatenate([g, g.copy()]); f[M] = -f[M]
        out.append(("BENT%d+flip" % m, m + 1, f))
    k = 9                                                 # iterated 3-majority
    x = bits(k); tri = [(x >> (3 * j)) & 7 for j in range(3)]
    inner = [1 - 2 * (np.array([bin(int(t)).count("1") for t in tt]) > 1) for tt in tri]
    s = sum((1 - v) // 2 for v in inner)
    out.append(("MAJ3oMAJ3", 9, 1.0 - 2.0 * (s > 1)))
    return out

if __name__ == "__main__":
    npz = sys.argv[1]
    nsym = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
    nrand = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
    Gm = gam.Gam(npz, 0.0)
    rng = np.random.default_rng(3)
    xs = np.concatenate([np.linspace(1.0, 12.0, nsym), np.linspace(0.02, 1.0, nsym // 4)[:-1]])
    pv = np.unique(np.concatenate([2.0 ** -xs, 1 - 2.0 ** -xs]))
    print("gate                arity   max margin c (symmetric bias)   max margin c (random bias)   -> constant")
    rows = []
    for name, k, vals in gates():
        bs = -1e9; bsp = None
        for p in pv:
            D, den, po = stat(vals, [p] * k, Gm)
            if den > 1e-8:
                c = -D / den
                if c > bs: bs, bsp = c, p
        br = -1e9; brp = None
        for _ in range(nrand):
            ps = 2.0 ** -rng.uniform(1, 14, k)
            ps = np.where(rng.random(k) < 0.5, 1 - ps, ps)
            D, den, po = stat(vals, ps, Gm)
            if den > 1e-8:
                c = -D / den
                if c > br: br, brp = c, ps.copy()
        worst = max(bs, br)
        print("%-18s %5d   %+.6e                %+.6e            %.7f"
              % (name, k, bs, br, Gm.cap + max(worst, 0) / 4), flush=True)
        rows.append([name, k, bs, br])
    json.dump(rows, open("bigates.json", "w"))
