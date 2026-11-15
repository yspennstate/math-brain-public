"""Cross-Stay inequality for the slab of a threshold function, at large n, by dynamic programming.

f = sgn(w1 x_1 + w'.y - theta), integer weights 0 < w'_j <= w1, theta a half-integer (no ties).
S = {y : |w'.y - theta| < w1}, delta = P[S].  For y, z rho-correlated uniform points:
  Stay  = P[y in S, z in S]
  Cross = P[y above S, z below S] + P[y below S, z above S]
  R(rho) = Cross * Stay / delta^2            (FLOW section 11(e): FEI for threshold functions follows if R <= M)
The joint law of (w'.y, w'.z) is built coordinate by coordinate on a (W+1) x (W+1) grid, W = sum of w'.

usage: python ltf_cross.py family n param theta_in_sd [seed]
families: maj (all 1), rand (uniform ints 1..param), two (param heavy weights of size ~sqrt(n), rest 1),
          geom (ratio param, rounded, capped), lin (1..n), sq (j^2 scaled to max 40), head (param copies of w1=20, rest 1)
prints one line per rho and the maximum of R.
"""
import sys
import numpy as np

RHOS = np.array([0.0, 0.5, 0.75, 0.875, 0.9375, 0.96875, 0.984375, 0.9921875, 0.99609375, 0.998046875,
                 0.9990234375, 0.99951171875])


def joint(wp, rhos):
    """P[r, a, b] = law of ((v_y + W)/2, (v_z + W)/2) at correlation rhos[r]."""
    W = int(wp.sum())
    R = len(rhos)
    P = np.zeros((R, W + 1, W + 1))
    P[:, 0, 0] = 1.0
    cs = ((1 + rhos) / 4)[:, None, None]
    cd = ((1 - rhos) / 4)[:, None, None]
    top = 0
    for w in wp:
        w = int(w)
        Q = np.zeros_like(P[:, :top + w + 1, :top + w + 1])
        old = P[:, :top + 1, :top + 1]
        Q[:, :top + 1, :top + 1] += cs * old            # (-,-)
        Q[:, w:top + w + 1, w:top + w + 1] += cs * old  # (+,+)
        Q[:, w:top + w + 1, :top + 1] += cd * old       # (+,-)
        Q[:, :top + 1, w:top + w + 1] += cd * old       # (-,+)
        P[:, :top + w + 1, :top + w + 1] = Q
        top += w
    return P, W


def cross_stay(wp, w1, theta, rhos=RHOS):
    P, W = joint(np.asarray(wp), rhos)
    v = 2 * np.arange(W + 1) - W - theta
    inS = np.abs(v) < w1
    up = v >= w1
    dn = v <= -w1
    marg = P[0].sum(axis=1)
    delta = float(marg[inS].sum())
    stay = P[:, inS][:, :, inS].sum(axis=(1, 2))
    cross = P[:, up][:, :, dn].sum(axis=(1, 2)) + P[:, dn][:, :, up].sum(axis=(1, 2))
    return delta, stay, cross, float(marg[up].sum()), float(marg[dn].sum())


def family(fam, n, param, rng):
    m = n - 1
    if fam == 'maj':
        return np.ones(m, dtype=np.int64), 1
    if fam == 'rand':
        wp = rng.integers(1, int(param) + 1, m)
        return wp, int(wp.max())
    if fam == 'two':
        h = int(round(np.sqrt(n)))
        wp = np.ones(m, dtype=np.int64)
        wp[:int(param)] = h
        return wp, h
    if fam == 'geom':
        wp = np.minimum(np.round(param ** np.arange(m)), 60).astype(np.int64)
        return wp, int(wp.max())
    if fam == 'lin':
        wp = np.arange(1, m + 1)
        return wp, m + 1
    if fam == 'sq':
        wp = np.maximum(1, np.round(40.0 * (np.arange(1, m + 1) / m) ** 2)).astype(np.int64)
        return wp, 40
    if fam == 'head':
        wp = np.ones(m, dtype=np.int64)
        wp[:int(param)] = 20
        return wp, 20
    raise SystemExit('family?')


def main():
    fam = sys.argv[1]
    n = int(sys.argv[2])
    param = float(sys.argv[3])
    tsd = float(sys.argv[4])
    seed = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    rng = np.random.default_rng(seed)
    wp, w1 = family(fam, n, param, rng)
    sd = float(np.sqrt((wp.astype(float) ** 2).sum()))
    theta = np.floor(tsd * sd) + 0.5
    delta, stay, cross, pu, pd = cross_stay(wp, w1, theta)
    if delta <= 0:
        print('delta = 0')
        return
    R = cross * stay / delta ** 2
    print('%s n=%d p=%g W=%d w1=%d theta=%.1f (%.2f sd) delta=%.3e P[up]=%.3e P[down]=%.3e'
          % (fam, n, param, int(wp.sum()), w1, theta, theta / sd, delta, pu, pd))
    for r, s, c, x in zip(RHOS, stay, cross, R):
        print('  rho=%.6f  Stay/delta=%.4e  Cross/delta=%.4e  R=%.4f' % (r, s / delta, c / delta, x))
    print('  max R = %.4f at rho=%.6f' % (float(R.max()), float(RHOS[int(R.argmax())])))


if __name__ == '__main__':
    main()
