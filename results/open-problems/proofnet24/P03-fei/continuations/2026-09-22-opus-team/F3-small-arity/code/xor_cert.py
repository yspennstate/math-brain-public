"""Interval certificate for the XOR gate inequality of a stored potential:

    D_XOR(p, q) = Gamma(p) + Gamma(q) - Gamma(p + q - 2pq) >= 0      for all p, q in (0, 1),

Gamma(z) = s Gnum(log2(1/s)) (+ c z(1-z)), s = min(z, 1-z).  D_XOR is exactly the gate defect of XOR (It_i = V_i,
Htilde = h(V_p) + h(V_q)).  Reductions (proved in the report): negating an input maps p to 1-p and the output measure to
its complement, and Gamma is symmetric, so p, q <= 1/2; D is symmetric, so p <= q; the margin c z(1-z) adds
c V_p V_q / 4 >= 0, so c = 0 suffices.

Coverage of 0 < p <= q <= 1/2 (x = log2(1/p) >= y = log2(1/q) >= 1):
  (T) q <= 2^-(K+1): all of p, q, z = p+q-2pq lie in the linear tail, where Gamma(u) = sigma u log2(1/u) + b u with
      sigma = (G_J - b*)/K > 0 and b = G_J - K sigma; u log(1/u) is concave with value 0 at 0, so subadditive and
      increasing on (0, 1/e): D >= sigma[(p log 1/p + q log 1/q) - z log 1/z] + b (p + q - z) >= 0 since z <= p + q and
      b(p + q - z) = 2 b p q >= 0 (b = b* > 0).
  (L) for each q-cell [q_lo, q_hi] and 0 < p <= p*: Gamma is absolutely continuous with Gamma' <= Lc on [q_lo, 2 q_hi],
      so D >= Gamma(p) - p(1-2q) Lc >= p [G(x) - (1-2q_lo) Lc] >= 0 once min_{x' >= x} G(x') >= (1-2q_lo) Lc.
  (C) the rest, p* <= p <= q, by direct enclosures on (x, y) cells, subdivided until verified:
      D >= Gamma_lo(p-cell) + Gamma_lo(q-cell) - Gamma_hi(z-range),  z increasing in p and q on [0, 1/2]^2.
Arithmetic: numpy float64; every log2 padded by 8 ulp relative plus 1e-300, every product and sum rounded outward with
nextafter (as in fei_cert.py).  usage: xor_cert.py <npz> [h]"""
import sys, os, time, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()

npz = sys.argv[1]; h0 = float(sys.argv[2]) if len(sys.argv) > 2 else 1 / 32
d = np.load(npz); xs = np.asarray(d["xs"], float); G = np.asarray(d["G"], float)
K = float(xs[-1]); J = len(xs) - 1
LN2_HI = np.nextafter(math.log(2.0), 2.0)
BSTAR_HI = np.nextafter(8 - 4 / np.nextafter(LN2_HI, 2.0), 99.0)
sigma_lo = np.nextafter((G[-1] - BSTAR_HI) / K, -1.0)
assert sigma_lo > 0
up = lambda a: np.nextafter(a, np.inf)
dn = lambda a: np.nextafter(a, -np.inf)


def log2_iv(z):
    """enclosure of log2(1/z) for float z > 0 (z itself exact)"""
    v = -np.log2(z)
    pad = 8 * np.spacing(np.abs(v)) + 1e-300
    return v - pad, v + pad


# piecewise data: slopes s_j on [x_j, x_{j+1}], per-piece max of G and of Gamma' = G - s/ln2
s = np.diff(G) / np.diff(xs)
seg_gmax = np.maximum(G[:-1], G[1:]); seg_gmin = np.minimum(G[:-1], G[1:])
seg_dmax = seg_gmax - s / math.log(2.0)
# sparse tables for range max / min over piece indices
def sparse(a, fn):
    t = [a.copy()]
    k = 1
    while (1 << k) <= len(a):
        prev = t[-1]; w = 1 << (k - 1)
        t.append(fn(prev[:-w], prev[w:]) if len(prev) > w else prev.copy())
        k += 1
    return t
TMAXG, TMING, TMAXD = sparse(seg_gmax, np.maximum), sparse(seg_gmin, np.minimum), sparse(seg_dmax, np.maximum)
def rq(tab, fn, i0, i1):
    """fn over pieces i0..i1 inclusive (vectorized)"""
    ln = np.maximum(i1 - i0 + 1, 1); k = np.floor(np.log2(ln)).astype(int)
    out = np.empty(len(i0))
    for kk in np.unique(k):
        m = k == kk
        a = tab[kk][i0[m]]; b = tab[kk][i1[m] - (1 << kk) + 1]
        out[m] = fn(a, b)
    return out


def piece(x):
    return np.clip(np.searchsorted(xs, x, side="right") - 1, 0, J - 1)


def G_range(xlo, xhi):
    """[min, max] of Gnum over [xlo, xhi], inside [1, K] (the tail is treated by the caller)"""
    xlo = np.maximum(xlo, 1.0); xhi = np.minimum(xhi, K)
    i0 = piece(xlo); i1 = piece(xhi)
    lo = rq(TMING, np.minimum, i0, i1); hi = rq(TMAXG, np.maximum, i0, i1)
    return lo, hi


def G_range_tail(xlo, xhi):
    """same, allowing x > K (linear tail with slope sigma > 0, so increasing there)"""
    lo = np.empty(len(xlo)); hi = np.empty(len(xlo))
    a = xhi <= K
    if a.any():
        lo[a], hi[a] = G_range(xlo[a], xhi[a])
    b = ~a
    if b.any():
        sig_hi = up((G[-1] - np.nextafter(8 - 4 / np.nextafter(math.log(2.0), 0.0), -99.0)) / K)
        glo_in, ghi_in = G_range(np.minimum(xlo[b], K), np.full(b.sum(), K))
        tl = G[-1] + np.maximum(xlo[b] - K, 0) * sigma_lo
        th = up(G[-1] + (xhi[b] - K) * sig_hi)
        inside = xlo[b] < K
        lo[b] = np.where(inside, np.minimum(glo_in, tl), tl)
        hi[b] = np.where(inside, np.maximum(ghi_in, th), th)
    return lo, hi


def Gamma_range(zlo, zhi):
    """enclosure of Gamma over [zlo, zhi] subset (0, 1/2]: z * G(log2(1/z)), both factors positive"""
    xa, _ = log2_iv(zhi); _, xb = log2_iv(zlo)
    glo, ghi = G_range_tail(np.maximum(xa, 1.0), np.maximum(xb, 1.0))
    return dn(zlo * glo), up(zhi * ghi)


t0 = time.time()
# suffix minimum of G over nodes (and the increasing tail): Smin[j] = min_{i >= j} G_i
Smin = np.minimum.accumulate(G[::-1])[::-1]
def G_suffix_min(x):
    """min of Gnum over [x, infinity) (piecewise linear: the min over x' >= x is min(G(x), node minima after x))"""
    j = np.clip(np.searchsorted(xs, x, side="right"), 0, J)
    xi = np.minimum(x, K)
    i = piece(xi)
    gx = G[i] + s[i] * (xi - xs[i])
    gx = gx - 1e-12 * np.abs(gx)
    after = np.where(j <= J, Smin[np.minimum(j, J)], np.inf)
    return np.minimum(gx, after)

# (L) + (C) over q-cells in y = log2(1/q) in [1, K+1]
ys = np.arange(1.0, K + 1.0 + 1e-12, h0)
ylo, yhi = ys[:-1], ys[1:]
qlo, qhi = 2.0 ** -yhi, 2.0 ** -ylo
qlo = dn(qlo); qhi = np.minimum(up(qhi), 0.5)
zc_hi = np.minimum(2 * qhi, 0.5)
# Gamma' bound on [q_lo, zc_hi]: pieces covering x in [log2(1/zc_hi), log2(1/q_lo)]
xa, _ = log2_iv(zc_hi); _, xb = log2_iv(qlo)
xa = np.maximum(xa, 1.0)
inK = xb <= K
Lc = np.full(len(qlo), np.inf)
Lc[inK] = rq(TMAXD, np.maximum, piece(xa[inK]), piece(np.minimum(xb[inK], K)))
if (~inK).any():                                  # q-cells reaching into the tail: add the tail's Gamma' = G - sigma/ln2
    sig_hi = up((G[-1] - np.nextafter(8 - 4 / np.nextafter(math.log(2.0), 0.0), -99.0)) / K)
    tail_d = G[-1] + (xb[~inK] - K) * sig_hi
    Lc[~inK] = np.maximum(rq(TMAXD, np.maximum, piece(xa[~inK]), np.full((~inK).sum(), J - 1)), tail_d)
Lc = up(Lc * (1 + 1e-12))
need = up((1 - 2 * qlo) * Lc)
# smallest x* with G_suffix_min(x*) >= need: search on a fine x grid
xgrid = np.arange(1.0, K + 60.0, 1 / 256)
gs = G_suffix_min(np.minimum(xgrid, K))
tailx = xgrid > K
gs[tailx] = G[-1] + (xgrid[tailx] - K) * sigma_lo          # the tail is increasing: its suffix minimum is itself
# suffix min along the grid including the tail region
gs_suf = np.minimum.accumulate(gs[::-1])[::-1]
idx = np.searchsorted(-gs_suf[::-1], -need)  # not used; do it directly below
xstar = np.empty(len(qlo))
for i in range(len(qlo)):
    ok = np.nonzero(gs_suf >= need[i])[0]
    xstar[i] = xgrid[ok[0]] if len(ok) else np.inf
print("(L) q-cells: %d ; max x* - y over cells = %.3f ; cells with x* = inf: %d  (%.1f s)"
      % (len(qlo), float(np.max(np.where(np.isfinite(xstar), xstar - ylo, 0))), int(np.isinf(xstar).sum()), time.time() - t0), flush=True)
if not np.all(np.isfinite(xstar)):
    print("XOR certificate for %s: NOT VERIFIED (the Lipschitz stage cannot close %d q-cells: Gamma' exceeds every G)"
          % (os.path.basename(npz), int(np.isinf(xstar).sum())))
    sys.exit(0)

# (C) direct cells: x in [ylo, x*] (p between p* and q; p <= q means x >= y)
cells = []
for i in range(len(qlo)):
    xe = max(xstar[i], ylo[i])
    if xe <= ylo[i]:
        continue
    xg = np.arange(ylo[i], xe + h0, h0)
    for a, b in zip(xg[:-1], xg[1:]):
        cells.append((a, b, ylo[i], yhi[i]))
cells = np.array(cells)
print("(C) initial cells: %d" % len(cells), flush=True)
total = 0; depth = 0; worst = np.inf
while len(cells):
    xl, xh, yl, yh = cells.T
    plo, phi_ = dn(2.0 ** -xh), up(2.0 ** -xl)
    ql, qh = dn(2.0 ** -yh), np.minimum(up(2.0 ** -yl), 0.5)
    plo = np.minimum(plo, qh); phi_ = np.minimum(phi_, qh)
    zl = dn(dn(ql + plo) - up(2 * up(plo * ql)))
    # z = p + q - 2pq is increasing in both on [0,1/2]^2: extremes at the corners
    zh = np.minimum(up(up(qh + phi_) - dn(2 * dn(phi_ * qh))), 0.5)
    gpl, _ = Gamma_range(plo, phi_)
    gql, _ = Gamma_range(ql, qh)
    _, gzh = Gamma_range(np.maximum(zl, 1e-300), zh)
    D_lo = dn(dn(gpl + gql) - gzh)
    total += len(cells)
    ok = D_lo >= 0
    worst = min(worst, float(D_lo[ok].min()) if ok.any() else worst)
    bad = cells[~ok]
    print("  depth %d: %d cells, %d not yet verified (%.1f s)" % (depth, len(cells), len(bad), time.time() - t0), flush=True)
    if len(bad) == 0:
        break
    if depth >= 14 or 4 * len(bad) > 3_000_000:
        print("  FAILED: unverified cells remain (depth %d, %d cells), e.g." % (depth, len(bad)), bad[:3]); break
    xm = 0.5 * (bad[:, 0] + bad[:, 1]); ym = 0.5 * (bad[:, 2] + bad[:, 3])
    cells = np.concatenate([np.column_stack([bad[:, 0], xm, bad[:, 2], ym]), np.column_stack([xm, bad[:, 1], bad[:, 2], ym]),
                            np.column_stack([bad[:, 0], xm, ym, bad[:, 3]]), np.column_stack([xm, bad[:, 1], ym, bad[:, 3]])])
    # keep only the part with x >= y (p <= q); cells entirely below the diagonal are outside the domain
    cells = cells[cells[:, 1] >= cells[:, 2]]
    depth += 1
print("XOR certificate for %s: %s ; cells evaluated %d ; smallest verified cell lower bound %.3e ; (%.1f s)"
      % (os.path.basename(npz), "VERIFIED" if len(cells) == 0 or (len(bad) == 0) else "NOT VERIFIED", total, worst, time.time() - t0))

if os.environ.get("XOR_SELFCHECK") == "1":
    # sampled check of the Lipschitz stage: numerical Gamma' on each q-cell's z-range never exceeds Lc, and at sampled
    # (p, q) with x >= x* the bound p [G(x) - (1-2q) Lc] is below the true D and nonnegative
    pot = F.Pot(npz, 0.0)
    rng = np.random.default_rng(1)
    worst_slope = -np.inf; worst_D = np.inf; viol = 0
    for i in rng.choice(len(qlo), 300, replace=False):
        z = np.exp(rng.uniform(np.log(qlo[i]), np.log(zc_hi[i]), 2000))
        hstep = 1e-7 * z
        der = (pot(z + hstep) - pot(z - hstep)) / (2 * hstep)
        worst_slope = max(worst_slope, float(np.max(der - Lc[i])))
        q = np.exp(rng.uniform(np.log(qlo[i]), np.log(qhi[i]), 200))
        x = xstar[i] + rng.exponential(3.0, 200)
        p = np.minimum(2.0 ** -x, q)
        Dt = pot(p) + pot(q) - pot(p + q - 2 * p * q)
        bound = p * (pot(p) / p - (1 - 2 * q) * Lc[i])
        viol += int(np.sum(Dt < bound - 1e-12 * np.abs(Dt)))
        worst_D = min(worst_D, float(np.min(bound / p)))
    print("selfcheck: max over samples of (numerical Gamma' - Lc) = %.3e (must be <= 0 up to difference noise); "
          "bound above true D at %d samples; min bound/p = %.4f (must be >= 0)" % (worst_slope, viol, worst_D))
