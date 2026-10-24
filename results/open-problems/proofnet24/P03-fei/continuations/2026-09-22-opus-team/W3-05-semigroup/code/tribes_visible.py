"""Tribes: exact spectrum by the composition formula, and the level-uniform measure with the same
level profile and the same per-coordinate level marginals (tribes is transitive).

Spectrum (derived in the report): for S touching exactly m >= 1 tribes (any nonempty subset in each),
  w(S) = 4 (1-p)^{2(t-m)} 4^{-w m},  p = 2^{-w},
and w(empty) = (1 - 2 (1-p)^t)^2.  Level profile W^k = sum_m C(t,m) g_m [z^k] ((1+z)^w - 1)^m.

Reports H/I, H_lev/I where H_lev = H(level profile) + sum_k W^k log C(n,k) is the entropy of the
level-uniform measure (maximal entropy among all laws with the same (level, coordinate) marginal array),
and the growth of H_lev/I with n.  Entropies in nats.
"""
import math
import numpy as np
from fei_core import lowprio

lowprio()


def lgC(a, b):
    return math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)


def tribes_stats(w, t, mmax=60):
    p = 2.0 ** (-w)
    n = w * t
    base = np.array([math.comb(w, j) / 2.0 ** w for j in range(w + 1)])   # ((1+z)^w)/2^w
    base[0] -= 1.0 / 2.0 ** w                                           # ((1+z)^w - 1)/2^w
    poly = np.array([1.0])
    Wk = np.zeros(n + 1)
    H = 0.0; I = 0.0; tot = 0.0
    W0 = (1 - 2 * (1 - p) ** t) ** 2
    ES = w * 2 ** (w - 1) / (2 ** w - 1)
    for m in range(1, min(t, mmax) + 1):
        poly = np.convolve(poly, base)                                  # ((1+z)^w-1)^m / 2^{wm}
        lg = math.log(4) + 2 * (t - m) * math.log1p(-p) - w * m * math.log(4)     # log g_m
        lmass = lgC(t, m) + m * math.log(2 ** w - 1) + lg                        # total weight of m-tribe sets
        mass = math.exp(lmass)
        tot += mass
        H += mass * (-lg)
        I += mass * m * ES
        # level profile: C(t,m) g_m 2^{wm} * poly
        scale = math.exp(lgC(t, m) + lg + w * m * math.log(2))
        Wk[:poly.size] += scale * poly
    Wk[0] += W0
    H += W0 * (-math.log(W0)) if W0 > 0 else 0.0
    Hlevel = -sum(x * math.log(x) for x in Wk if x > 0)
    Hwithin = sum(Wk[k] * lgC(n, k) for k in range(n + 1) if Wk[k] > 0)
    return dict(n=n, H=H, I=I, tot=tot + W0, Hlev=Hlevel + Hwithin, Hlevel=Hlevel)


def main():
    lines = []
    P = lambda s: (lines.append(s), print(s, flush=True))
    P("# tribes w x t with t = round(2^w ln 2); nats")
    P("# w t n mass_check I H/I(bits) H_lev/I(nats) H_lev/(I log2 n)")
    for w in range(2, 17):
        t = max(1, round(2 ** w * math.log(2)))
        s = tribes_stats(w, t)
        P("%2d %6d %8d %.12f %.6f %.6f %.4f %.4f" % (w, t, s['n'], s['tot'], s['I'], s['H'] / s['I'] / math.log(2),
                                                  s['Hlev'] / s['I'], s['Hlev'] / (s['I'] * math.log2(s['n']))))
    with open('../logs/tribes_visible.log', 'w') as fh:
        fh.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
