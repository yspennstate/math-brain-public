"""FEI coordinate-step numerics, continued from 2026-09-20.

Two statistics of a Boolean f (entropy in bits, normalized Walsh spectrum p(S) = fhat(S)^2):
  min-step   rho0(f)  = min over relevant i of  Delta_i H / Inf_i,   Delta_i H = H(f) - (H(f|x_i=0) + H(f|x_i=1))/2
  total-step tau(f)   = sum_i Delta_i H / I(f)
Either one bounded by C over all f gives FEI with constant C by induction on n
(min-step: pick the best coordinate; total-step: average over all coordinates, since
 I(f) = Inf_i(f) + (I(f0)+I(f1))/2 for every i).

Part A: n = 4 exhaustive, both statistics (reproduces the 09-20 min-step record 4.8677).
Part B: tribes(w, s) = AND of s ORs of w disjoint bits, in closed form (no 2^n), every width 2..6,
        s up to 40; cross-checked against brute force where w*s <= 12. All coordinates of tribes are
        equivalent, so min-step = total-step = the single-coordinate ratio.
"""
import math, sys, json
from math import comb, log2
import numpy as np

def h2(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -p * log2(p) - (1 - p) * log2(1 - p)

def wht(f):
    a = np.asarray(f, dtype=float).copy()
    h = 1
    while h < len(a):
        a = a.reshape(-1, 2 * h)
        x = a[:, :h].copy(); y = a[:, h:].copy()
        a[:, :h] = x + y; a[:, h:] = x - y
        a = a.reshape(-1)
        h *= 2
    return a / len(a)

def popcounts(n):
    return np.array([bin(s).count("1") for s in range(1 << n)])

def stats(f, n, pc=None):
    if pc is None:
        pc = popcounts(n)
    p = wht(f) ** 2
    nz = p > 1e-18
    H = float(-(p[nz] * np.log2(p[nz])).sum())
    I = float((pc * p).sum())
    idx = np.arange(1 << n)
    inf = np.array([float(p[(idx >> i) & 1 == 1].sum()) for i in range(n)])
    return H, I, inf, p

def restrict(f, n, i, b):
    idx = np.arange(1 << n)
    return f[(idx >> i) & 1 == b]

def steps(f, n):
    """returns rho0 (min-step over relevant coords), tau (total-step), per-coordinate ratios, H, I"""
    pc = popcounts(n); pc1 = popcounts(n - 1)
    H, I, inf, _ = stats(f, n, pc)
    d = []
    for i in range(n):
        f0 = restrict(f, n, i, 0); f1 = restrict(f, n, i, 1)
        H0 = stats(f0, n - 1, pc1)[0]; H1 = stats(f1, n - 1, pc1)[0]
        d.append(H - (H0 + H1) / 2)
    d = np.array(d)
    rel = inf > 1e-12
    ratios = np.where(rel, d / np.where(rel, inf, 1), np.nan)
    rho0 = float(np.nanmin(ratios)) if rel.any() else float("nan")
    tau = float(d.sum() / I) if I > 1e-12 else float("nan")
    return rho0, tau, ratios, H, I

def tt_to_f(tt, n):
    bits = np.array([(tt >> x) & 1 for x in range(1 << n)])
    return 1 - 2 * bits

# ---------------------------------------------------------------- Part A
def part_a():
    n = 4
    best_rho = (-1, None); best_tau = (-1, None); best_hi = (-1, None)
    tau_at_rho_argmax = None
    for tt in range(1, (1 << (1 << n)) - 1):
        f = tt_to_f(tt, n)
        rho0, tau, ratios, H, I = steps(f, n)
        if rho0 > best_rho[0]:
            best_rho = (rho0, tt); tau_at_rho_argmax = tau
        if tau > best_tau[0]:
            best_tau = (tau, tt)
        if H / I > best_hi[0]:
            best_hi = (H / I, tt)
    print("PART A  n=4 exhaustive over %d functions" % ((1 << 16) - 2))
    print("  max min-step rho0 = %.4f at tt=%d (its total-step tau = %.4f)" % (best_rho[0], best_rho[1], tau_at_rho_argmax))
    print("  max total-step tau = %.4f at tt=%d" % best_tau)
    print("  max H/I = %.4f at tt=%d" % best_hi)
    f = tt_to_f(best_tau[1], n)
    rho0, tau, ratios, H, I = steps(f, n)
    print("  total-step argmax: ones=%d H=%.4f I=%.4f per-coordinate ratios=%s" % (int((f < 0).sum()), H, I, np.round(ratios, 3)))
    return best_rho, best_tau

# ---------------------------------------------------------------- Part B: tribes in closed form
def block_stats(groups):
    """groups = [(count, width), ...] of an AND of ORs on disjoint blocks. Returns (H, I, Inf_1) where
    Inf_1 is the influence of one bit of the first group's first block (width >= 1). +1 = true."""
    if any(w == 0 for c, w in groups if c > 0):
        return 0.0, 0.0, 0.0          # an OR of zero bits is false, the AND is constant
    s = sum(c for c, w in groups)
    # OR_w spectrum: g(empty) = a = 1 - 2^(1-w); |g(T)| = c = 2^(1-w) for T nonempty; m = 2^w - 1 nonempty T;
    # sum over nonempty T of |T| = w 2^(w-1)
    par = []
    for cnt, w in groups:
        a = 1 - 2.0 ** (1 - w); c = 2.0 ** (1 - w); m = 2 ** w - 1; tsum = w * 2 ** (w - 1)
        par.append((cnt, w, a, c, m, tsum))
    H = 0.0; I = 0.0; mass = 0.0
    # p(empty)
    p0 = (2.0 ** (1 - s) * math.prod((1 + a) ** cnt for cnt, w, a, c, m, tsum in par) - 1) ** 2
    if p0 > 0:
        H -= p0 * log2(p0)
    mass += p0
    # nonempty S: choose b_g touched blocks per group
    ranges = [range(0, cnt + 1) for cnt, *_ in par]
    import itertools
    for bs in itertools.product(*ranges):
        if sum(bs) == 0:
            continue
        pS = 4.0 ** (1 - s)
        N = 1.0
        for (cnt, w, a, c, m, tsum), b in zip(par, bs):
            pS *= c ** (2 * b) * (1 + a) ** (2 * (cnt - b))
            N *= comb(cnt, b) * m ** b
        # sum of |S| over these S: prod_g C(cnt_g,b_g) * sum_g [ b_g tsum_g m_g^(b_g-1) prod_{g' != g} m_g'^b_g' ]
        combs = math.prod(comb(cnt, b) for (cnt, *_), b in zip(par, bs))
        ssum = 0.0
        for gi, ((cnt, w, a, c, m, tsum), b) in enumerate(zip(par, bs)):
            if b == 0:
                continue
            term = b * tsum * m ** (b - 1)
            for gj, ((cnt2, w2, a2, c2, m2, tsum2), b2) in enumerate(zip(par, bs)):
                if gj != gi:
                    term *= m2 ** b2
            ssum += term
        ssum *= combs
        mass += N * pS
        if pS > 0:
            H -= N * pS * log2(pS)
        I += pS * ssum
    cnt1, w1 = groups[0]
    # Inf of one bit in a block of width w1: the other s-1 ORs true, the other w1-1 bits false
    others = 1.0
    for gi, (cnt, w) in enumerate(groups):
        k = cnt - 1 if gi == 0 else cnt
        others *= (1 - 2.0 ** (-w)) ** k
    inf1 = others * 2.0 ** (-(w1 - 1))
    assert abs(mass - 1) < 1e-9, mass
    return H, I, inf1

def tribes_step(w, s):
    H, I, inf1 = block_stats([(s, w)])
    Hb = block_stats([(s - 1, w)])[0] if s - 1 > 0 else 0.0           # x_1 true: that OR is true
    Ha = block_stats([(1, w - 1), (s - 1, w)])[0] if w - 1 > 0 else 0.0  # x_1 false: block 1 loses a bit
    if w - 1 > 0 and s - 1 == 0:
        Ha = block_stats([(1, w - 1)])[0]
    d = H - (Ha + Hb) / 2
    return d / inf1, H / I, H, I, inf1

def brute_tribes(w, s):
    n = w * s
    idx = np.arange(1 << n)
    val = np.ones(1 << n, dtype=int)
    for j in range(s):
        blk = (idx >> (j * w)) & ((1 << w) - 1)
        val &= (blk != 0).astype(int)     # OR of the block's bits (bit 1 = true)
    f = 2 * val - 1
    rho0, tau, ratios, H, I = steps(f, n)
    return rho0, tau, H, I

def part_b():
    print("PART B  tribes(w,s) closed form vs brute force (w*s <= 12):")
    for w in (2, 3, 4):
        for s in (2, 3, 4, 5, 6):
            if w * s > 12:
                continue
            r, hi, H, I, inf1 = tribes_step(w, s)
            br, bt, bH, bI = brute_tribes(w, s)
            print("  w=%d s=%d  closed: step %.4f H %.4f I %.4f | brute: min-step %.4f total-step %.4f H %.4f I %.4f  %s"
                  % (w, s, r, H, I, br, bt, bH, bI, "OK" if abs(r - br) < 1e-6 and abs(H - bH) < 1e-6 and abs(I - bI) < 1e-6 else "MISMATCH"))
    print("PART B  tribes(w,s) step ratio and H/I by width (closed form):")
    for w in (2, 3, 4, 5, 6, 8):
        rows = []
        best = (-1, 0)
        for s in range(2, 41):
            r, hi, H, I, inf1 = tribes_step(w, s)
            rows.append((s, r, hi))
            if r > best[0]:
                best = (r, s)
        show = [x for x in rows if x[0] in (2, 3, 4, 6, 8, 12, 16, 24, 32, 40) or x[0] == best[1]]
        print("  w=%d  max step %.4f at s=%d (n=%d);  " % (w, best[0], best[1], best[1] * w)
              + "  ".join("s%d:%.3f/%.2f" % (s, r, hi) for s, r, hi in show))
    print("  (each entry is step-ratio/H-over-I)")

if __name__ == "__main__":
    part_b()
    part_a()
