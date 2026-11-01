"""An independent computation of free convolutions, to check the constants found by subordination.

From G = G_mu(omega_1) = G_lambda(omega_2) and omega_1 + omega_2 = z + 1/G, and from
omega_2 = K_lambda(G) = 1/G + R_lambda(G), the second subordination function drops out and

    omega_1(z) = z - R_lambda(G),        so        G = G_mu(z - R_lambda(G)),

one implicit equation for G with no iteration between two maps.  For the semicircle, R(w) = tw, this is
G = G_mu(z - tG), the free heat equation, and writing G = a - i pi f recovers exactly Hasebe and Ueda's
Lemma 3.1, the condition int dmu/((u-y)^2+v^2) = 1/t with v = pi t f, in which the density has cancelled.
That cancellation is special to the semicircle and is why only it has a clean level-set criterion.

Here the equation is solved directly by Newton in the complex plane, continued along the grid in x.  It
shares no code path with the Belinschi and Bercovici iteration used elsewhere, so agreement between them
is a real check.
"""
import numpy as np, cmath


def R_stable(alpha):
    return lambda w: -1j * cmath.exp((alpha - 1) * cmath.log(1j * w))


def G_two(D):
    return lambda z: 0.5 / (z + D / 2) + 0.5 / (z - D / 2)


def density(alpha, D, xs, eps=1e-6):
    R = R_stable(alpha); Gm = G_two(D)
    out = []
    g = None
    for x in xs:
        z = complex(x, eps)
        w = g if g is not None else Gm(z)
        for _ in range(300):
            h = 1e-8 * max(1.0, abs(w))
            f = Gm(z - R(w)) - w
            d = ((Gm(z - R(w + h)) - (w + h)) - (Gm(z - R(w - h)) - (w - h))) / (2 * h)
            if d == 0: break
            step = f / d
            w = w - step
            if w.imag > 0: w = complex(w.real, -abs(w.imag))
            if abs(step) < 1e-13 * max(1.0, abs(w)): break
        g = w
        out.append(-w.imag / np.pi)
    return np.array(out)


def interior_maxima(xs, f):
    d = np.diff(f)
    return [i + 1 for i in range(len(d) - 1) if d[i] > 0 and d[i + 1] <= 0]


def c_free(alpha, lo=0.2, hi=4.0, steps=12, n=400):
    def uni(D):
        span = D / 2 + 8.0
        xs = np.linspace(-span, span, n)
        return len(interior_maxima(xs, density(alpha, D, xs))) <= 1
    if not uni(lo): return float('nan')
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        if uni(mid): lo = mid
        else: hi = mid
    return lo


if __name__ == '__main__':
    print("independent recomputation of the free stable constants, by the implicit equation")
    print(f"{'alpha':>7} {'c_free (implicit)':>18} {'by subordination':>17}")
    prev = {2.0: 1.0015, 1.8: 1.0241, 1.4: 1.0779, 1.0: 1.1601, 0.8: 1.2280, 0.5: 1.4348}
    for a in (2.0, 1.8, 1.4, 1.0, 0.8, 0.5):
        print(f"{a:>7.2f} {c_free(a):>18.4f} {prev[a]:>17.4f}", flush=True)
