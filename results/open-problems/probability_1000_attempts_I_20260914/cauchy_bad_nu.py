"""An explicit unimodal measure whose Cauchy convolution is not unimodal.

Hasebe and Ueda's Lemma 3.9 needs one: the Cauchy density is not log-concave, so by Ibragimov's theorem
such a measure exists, and they invoke it without exhibiting one.  Making it explicit is worth doing
because the same measure is the test object for asking whether other laws are freely strongly unimodal,
and because for the Cauchy free and classical convolution agree, so it also shows directly that no Cauchy
law is freely strongly unimodal.

A measure whose density is nonincreasing on [0, infinity) and zero to the left of the origin is unimodal
with mode at 0.  Mixtures sum_i w_i U_[0,a_i] of uniform laws anchored at the origin are exactly the such
measures (Khinchin, one-sided form), and their Cauchy convolutions are elementary:

    (nu * C_t)(x) = sum_i (w_i/(pi a_i)) [ arctan((x)/t) - arctan((x-a_i)/t) ].

Each term is unimodal with its mode at a_i/2, so a mixture of widely separated scales can put two bumps in
the result while the mixture itself stays nonincreasing.
"""
import numpy as np


def dens(x, ws, as_, t=1.0):
    out = np.zeros_like(x)
    for w, a in zip(ws, as_):
        out += (w / (np.pi * a)) * (np.arctan(x / t) - np.arctan((x - a) / t))
    return out


def modes(ws, as_, t=1.0, lo=-40, hi=None, n=400001):
    hi = hi if hi is not None else max(as_) + 40
    x = np.linspace(lo, hi, n)
    f = dens(x, ws, as_, t)
    up = np.diff(f) > 0
    return int(np.sum(up[:-1] & ~up[1:])), x, f


if __name__ == '__main__':
    print("searching mixtures of two one-sided uniforms for a bimodal Cauchy convolution")
    best = None
    for a in (0.05, 0.1, 0.2, 0.4):
        for b in (4, 8, 16, 32, 64):
            for w in np.arange(0.05, 0.96, 0.05):
                m, x, f = modes([w, 1 - w], [a, b])
                if m > 1:
                    if best is None: best = (w, a, b)
                    print(f"  FOUND: nu = {w:.2f} U[0,{a}] + {1-w:.2f} U[0,{b}]  gives {m} modes", flush=True)
                    break
            if best: break
        if best: break
    if best is None:
        print("  none found in this family")
    else:
        w, a, b = best
        m, x, f = modes([w, 1 - w], [a, b])
        pk = [(x[i], f[i]) for i in range(1, len(x) - 1) if f[i] > f[i - 1] and f[i] >= f[i + 1]]
        print(f"\n  the measure: nu = {w:.2f} * U[0,{a}] + {1-w:.2f} * U[0,{b}], nonincreasing on [0,inf),")
        print(f"  so unimodal with mode 0. Its Cauchy convolution at t=1 has {m} local maxima:")
        for xx, ff in pk: print(f"     mode at x = {xx:9.4f}, density {ff:.6f}")
        i = np.argmin(np.abs(x - pk[0][0]))
        j = np.argmin(np.abs(x - pk[1][0]))
        dip = f[i:j].min()
        print(f"  the dip between them: {dip:.6f}")
        print("\n  Since mu box+ C_t = mu * C_t for every mu, the same measure shows that no Cauchy law is")
        print("  freely strongly unimodal.")
