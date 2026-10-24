"""Hasebe and Ueda, ALEA 15 (2018), Conjecture 3.5: is the free convolution of two symmetric unimodal
measures unimodal?  (Its classical analogue is Wintner's theorem, which follows from Khinchin's
representation plus linearity of ordinary convolution; free convolution is not linear, so that route is
closed.)

Densities are computed by the Belinschi and Bercovici subordination iteration.  With F_i = 1/G_i, the
subordination functions satisfy

    omega_1 = F_2(omega_2) - omega_2 + z,      omega_2 = F_1(omega_1) - omega_1 + z,

and iterating from omega_1 = z converges for z in the upper half plane; then G_{mu box+ nu}(z) =
G_1(omega_1(z)) and the density at x is -Im G(x + i eps)/pi.

By Khinchin a symmetric unimodal law is a mixture of uniform laws on symmetric intervals, so mixtures
sum_i w_i U_{a_i} are the test family, with G(z) = sum_i (w_i/a_i) arctanh(a_i/z).

Controls: the semicircle law free-convolved with itself must be a semicircle of twice the variance, and
U_1 box+ U_1 must be unimodal with support edge near 1.5457 and peak density near 0.3710, the peak being
where tan(v) = 2v.
"""
import numpy as np, cmath


def atanh(z):
    return 0.5 * (cmath.log(1 + z) - cmath.log(1 - z))


def G_mix(ws, as_):
    ws = np.asarray(ws, float); ws = ws / ws.sum()
    def G(z):
        return sum(w / a * atanh(a / z) for w, a in zip(ws, as_))
    return G


def G_semicircle(t):
    """semicircle of variance t, support [-2 sqrt t, 2 sqrt t]"""
    def G(z):
        return (z - cmath.sqrt(z * z - 4 * t)) / (2 * t)
    return G


def density(G1, G2, xs, eps=1e-5, iters=4000):
    F1 = lambda w: 1.0 / G1(w)
    F2 = lambda w: 1.0 / G2(w)
    out = []
    for x in xs:
        z = complex(x, eps)
        w1 = z
        for _ in range(iters):
            w2 = F1(w1) - w1 + z
            if w2.imag < eps: w2 = complex(w2.real, eps)
            nw1 = F2(w2) - w2 + z
            if nw1.imag < eps: nw1 = complex(nw1.real, eps)
            if abs(nw1 - w1) < 1e-13 * max(1.0, abs(nw1)):
                w1 = nw1; break
            w1 = nw1
        out.append(-G1(w1).imag / np.pi)
    return np.array(out)


def modes(xs, f, tol=1e-9):
    up = np.diff(f) > tol
    return int(np.sum(up[:-1] & ~up[1:]))


if __name__ == '__main__':
    print("CONTROLS")
    xs = np.linspace(-4, 4, 4001)
    f = density(G_semicircle(1.0), G_semicircle(1.0), xs)
    peak = f.max(); edge = xs[f > 1e-6].max()
    print(f"  semicircle(1) box+ semicircle(1): edge {edge:.4f} (exact 2*sqrt2 = {2*np.sqrt(2):.4f}), "
          f"peak {peak:.4f} (exact {1/(np.pi*np.sqrt(2)):.4f}), modes {modes(xs,f)}")
    xs = np.linspace(-2.5, 2.5, 5001)
    f = density(G_mix([1],[1.0]), G_mix([1],[1.0]), xs)
    print(f"  U_1 box+ U_1: edge {xs[f>1e-6].max():.4f} (expected 1.5457), "
          f"peak {f.max():.4f} (expected 0.3710), modes {modes(xs,f)}")

    print("\nCONJECTURE 3.5, symmetric unimodal pairs (mixtures of uniforms)")
    CASES = [
        ("U_1 with U_1",                  ([1],[1.0]),                ([1],[1.0])),
        ("U_1 with U_3",                  ([1],[1.0]),                ([1],[3.0])),
        ("U_1 with U_0.05",               ([1],[1.0]),                ([1],[0.05])),
        ("spike+slab 0.5/0.5, itself",    ([0.5,0.5],[0.02,1.0]),     ([0.5,0.5],[0.02,1.0])),
        ("spike+slab 0.8/0.2, itself",    ([0.8,0.2],[0.02,1.0]),     ([0.8,0.2],[0.02,1.0])),
        ("spike+slab 0.95/0.05, itself",  ([0.95,0.05],[0.01,1.0]),   ([0.95,0.05],[0.01,1.0])),
        ("three scales, itself",          ([0.4,0.3,0.3],[0.02,0.3,1.0]), ([0.4,0.3,0.3],[0.02,0.3,1.0])),
        ("spike+slab with a wide slab",   ([0.9,0.1],[0.01,1.0]),     ([1],[2.0])),
        ("two-scale vs two-scale",        ([0.7,0.3],[0.05,1.0]),     ([0.3,0.7],[0.05,1.0])),
    ]
    for name, (w1,a1), (w2,a2) in CASES:
        span = (max(a1) + max(a2)) * 1.3 + 0.5
        xs = np.linspace(-span, span, 6001)
        f = density(G_mix(w1,a1), G_mix(w2,a2), xs)
        m = modes(xs, f)
        print(f"  {name:>32}: modes {m}   peak {f.max():.4f}   edge {xs[f>1e-6].max():.4f}"
              + ("   <-- NOT UNIMODAL" if m > 1 else ""))
