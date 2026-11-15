"""The normalised exponential-moment form of containment (FLOW.md 6(a'), statement (N)).

For Boolean g (values +-1) with beta = P[g = -1], mu = ghat^2, up(S) = sum_{U>=S} mu(U):
    W0(g; theta, c) = sum_{S nonempty} mu(S) c^-|S| up(S)^-theta
    (N):  W0(g) <= Psi(beta) := 4^(1-theta) * min( b (1 - b^(1-theta)) : b in {beta, 1-beta} )
(N) for all g  <=>  sum_S mu c^-|S| up^-theta <= K^I for all f and some K  (AND/OR of many copies of g),
and (N) implies sum_S mu c^-|S| up^-theta <= 1, hence A <= (log2 c / theta) I.

For each function the script finds c*(g, theta) = the least c for which (N) holds, and reports the sup over a class,
with log2(c*)/theta (the containment constant that c would give).

Usage: python check_wstar.py census4
       python check_wstar.py sample n count seed
       python check_wstar.py tribes           tribes w x s, all s up to 40 * 2^w, closed form
       python check_wstar.py fam nmax
"""
import sys
import math
import numpy as np
from check_sec5 import wht, zeta_sup, TINY

THETAS = [0.5, 0.25, 0.1, 0.02]


def psi(beta, th):
    a = beta * (1 - beta ** (1 - th))
    b = (1 - beta) * (1 - (1 - beta) ** (1 - th))
    return 4 ** (1 - th) * np.minimum(a, b)


def cstar_from_levels(m, target):
    """m: (batch, n+1) level sums m_k = sum_{|S|=k} mu up^-theta (k >= 1 used); least c with sum_k m_k c^-k <= target."""
    Bt, n1 = m.shape
    ks = np.arange(n1, dtype=np.float64)
    lo = np.zeros(Bt)            # log c
    hi = np.full(Bt, 60.0)
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        val = (m[:, 1:] * np.exp(-mid[:, None] * ks[None, 1:])).sum(axis=1)
        good = val <= target
        hi = np.where(good, mid, hi)
        lo = np.where(good, lo, mid)
    return np.exp(hi)


def cstars(f, n):
    N = 1 << n
    pop = np.array([bin(s).count("1") for s in range(N)])
    fh = wht(f, n)
    mu = fh * fh
    up = zeta_sup(mu, n)
    pos = mu > 1e-15
    beta = (1 - fh[:, 0]) / 2
    I = (mu * pop).sum(axis=1)
    A = -(mu * np.where(pos, np.log2(np.maximum(up, TINY)), 0)).sum(axis=1)
    out = {"I": I, "beta": beta, "A": A}
    onehot = np.zeros((N, n + 1))
    onehot[np.arange(N), pop] = 1.0
    for th in THETAS:
        t = np.where(pos, mu * np.maximum(up, TINY) ** (-th), 0.0)
        m = t @ onehot
        out[th] = cstar_from_levels(m, psi(beta, th))
    return out


def upd(best, o, tag):
    ok = o["I"] > 1e-12
    for th in THETAS:
        v = np.where(ok, o[th], 0.0)
        j = int(np.argmax(v))
        if th not in best or v[j] > best[th][0]:
            best[th] = (float(v[j]), tag(j), float(o["I"][j]), float(o["beta"][j]), float(o["A"][j]))


def report(best):
    for th in THETAS:
        v, tag, I, beta, A = best[th]
        dict_c = 2 ** th / (2 ** (1 - th) - 1)
        print("  theta=%.2f  sup c* = %10.5f  (dictator needs %8.5f)  log2(c*)/theta = %7.4f   at %s  I=%.4f beta=%.4f A/I=%.4f"
              % (th, v, dict_c, math.log2(v) / th, tag, I, beta, A / I))


def census4():
    n, N = 4, 16
    best = {}
    for start in range(0, 1 << N, 8192):
        idx = np.arange(start, start + 8192, dtype=np.uint64)
        f = 1.0 - 2.0 * ((idx[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(np.float64)
        upd(best, cstars(f, n), lambda j: "tt=0x%04x" % int(idx[j]))
    print("n=4 census")
    report(best)


def sample(n, count, seed):
    N = 1 << n
    rng = np.random.default_rng(seed)
    best = {}
    done = 0
    bs = max(64, min(8192, (1 << 22) // N))
    while done < count:
        b = min(bs, count - done)
        dens = rng.choice([0.5, 0.3, 0.15, 0.05], size=(b, 1))
        bits = rng.random((b, N)) < dens
        f = 1.0 - 2.0 * bits.astype(np.float64)
        keep = bits.copy()
        upd(best, cstars(f, n), lambda j: "bits=" + "".join("1" if x else "0" for x in keep[j]))
        done += b
    print("n=%d sample of %d (seed %d)" % (n, count, seed))
    report(best)


def tribes():
    print("tribes w x s (OR of s ANDs of width w), closed form; sup over s of c*, and where")
    for th in THETAS:
        print(" theta=%.2f   dictator c = %.5f" % (th, 2 ** th / (2 ** (1 - th) - 1)))
        for w in range(1, 9):
            d = 2.0 ** (-w)
            bestc, bests = 0.0, 0
            smax = 40 * 2 ** w
            for s in list(range(1, min(smax, 400))) + list(range(400, smax, max(1, smax // 400))):
                q = (1 - d) ** s                 # P[no tribe true]; beta = P[f=-1] = 1-q (or q; psi is symmetric)
                # psi from q directly (1 - q rounds to 1 for large s)
                lq = s * math.log1p(-d)
                ta = q * (-math.expm1((1 - th) * lq))
                tb = (1 - q) * (-math.expm1((1 - th) * math.log1p(-q)))
                target = 4 ** (1 - th) * min(ta, tb)
                # W0(c) = 4^(1-th) [ ((1-d)^(2-th) + d^(2-th) ((1+2^th/c)^w - 1))^s - (1-d)^((2-th) s) ]
                lo, hi = 0.0, 60.0
                for _ in range(70):
                    mid = 0.5 * (lo + hi)
                    c = math.exp(mid)
                    base = (1 - d) ** (2 - th) + d ** (2 - th) * ((1 + 2 ** th / c) ** w - 1)
                    lw = s * math.log(base)
                    val = 4 ** (1 - th) * (math.exp(lw) - math.exp((2 - th) * lq)) if lw < 700 else float("inf")
                    if val <= target:
                        hi = mid
                    else:
                        lo = mid
                c = math.exp(hi)
                if c > bestc:
                    bestc, bests = c, s
            print("   w=%d  sup_s c* = %10.5f at s=%d   log2(c*)/theta = %.4f" % (w, bestc, bests, math.log2(bestc) / th))


def fam(nmax):
    def pts(n):
        return ((np.arange(1 << n)[:, None] >> np.arange(n)[None, :]) & 1)

    rows = []
    for n in range(3, nmax + 1, 2):
        rows.append(("MAJ_%d" % n, n, np.where(pts(n).sum(axis=1) * 2 > n, -1.0, 1.0)))
    for k in (1, 2, 3):
        n = k + (1 << k)
        if n <= nmax:
            b = pts(n)
            addr = (b[:, :k] * (1 << np.arange(k))[None, :]).sum(axis=1)
            rows.append(("ADDR_%d" % k, n, 1.0 - 2.0 * b[np.arange(1 << n), k + addr]))
    for n in range(4, nmax + 1):
        b = pts(n)
        for t in range(1, n // 2 + 1):
            rows.append(("THR_%d_%d" % (n, t), n, np.where(b.sum(axis=1) >= n - t, -1.0, 1.0)))   # Hamming ball radius t
    print("%-12s %7s %7s %6s  " % ("f", "I", "beta", "A/I") + " ".join("c*(th=%.2f)" % th for th in THETAS))
    for name, n, f in rows:
        o = cstars(f[None, :].astype(np.float64), n)
        print("%-12s %7.4f %7.4f %6.3f  " % (name, float(o["I"][0]), float(o["beta"][0]), float(o["A"][0] / o["I"][0]))
              + " ".join("%11.5f" % float(o[th][0]) for th in THETAS), flush=True)


if __name__ == "__main__":
    m = sys.argv[1]
    if m == "census4":
        census4()
    elif m == "sample":
        sample(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif m == "tribes":
        tribes()
    else:
        fam(int(sys.argv[2]) if len(sys.argv) > 2 else 12)
