"""Free stable laws, and whether they are freely strongly unimodal.

The reduction in the companion memo leaves Hasebe and Ueda's Problem 3.11 open only for measures attracted
to a free stable law of index other than one and two.  So the question is whether a free alpha-stable law
lambda has some unimodal nu with lambda box+ nu not unimodal.

The symmetric free alpha-stable law has R-transform R(w) = -i (i w)^{alpha-1}, which gives R = -i at
alpha = 1 (the Cauchy, whose R-transform is the constant -i) and R(w) = w at alpha = 2 (the semicircle).
Its Cauchy transform is recovered from K(w) = 1/w + R(w) by solving K(G(z)) = z, and the density follows.

CONTROLS: at alpha = 2 the density must be the semicircle on [-2,2] with peak 1/pi; at alpha = 1 it must
be the standard Cauchy with peak 1/pi.  Both are checked before anything else is believed.
"""
import numpy as np, cmath


def R_stable(alpha):
    def R(w):
        return -1j * cmath.exp((alpha - 1) * cmath.log(1j * w))
    return R


def G_stable(alpha):
    """Cauchy transform of the symmetric free alpha-stable law, by Newton on K(G) = z"""
    R = R_stable(alpha)
    K = lambda w: 1.0 / w + R(w)
    def G(z, guess=None):
        w = guess if guess is not None else 1.0 / z
        for _ in range(300):
            h = 1e-8 * max(1.0, abs(w))
            f = K(w) - z
            d = (K(w + h) - K(w - h)) / (2 * h)
            if d == 0: return None
            step = f / d
            w = w - step
            if w.imag > 0: w = complex(w.real, -abs(w.imag))   # G maps C+ to C-
            if abs(step) < 1e-13 * max(1.0, abs(w)): return w
        return None
    return G


def density(alpha, xs, eps=1e-6):
    G = G_stable(alpha)
    out = []
    guess = None
    for x in xs:
        w = G(complex(x, eps), guess)
        if w is None:
            out.append(np.nan); guess = None
        else:
            out.append(-w.imag / np.pi); guess = w
    return np.array(out)


if __name__ == '__main__':
    print("CONTROLS")
    xs = np.linspace(-3, 3, 1201)
    f = density(2.0, xs)
    ok = np.nanmax(f)
    print(f"  alpha = 2: peak {ok:.5f} (semicircle exact {1/np.pi:.5f}), "
          f"support edge {xs[np.nan_to_num(f) > 1e-4].max():.3f} (exact 2)")
    f1 = density(1.0, xs)
    print(f"  alpha = 1: peak {np.nanmax(f1):.5f} (Cauchy exact {1/np.pi:.5f}), "
          f"value at x=1 {f1[np.argmin(np.abs(xs-1))]:.5f} (exact {1/(2*np.pi):.5f})")
    print("\nmass check, by trapezoid over a wide grid")
    for a in (2.0, 1.5, 1.0, 0.7):
        g = np.linspace(-60, 60, 40001)
        d = density(a, g)
        print(f"  alpha = {a}: integral {np.trapezoid(np.nan_to_num(d), g):.4f}, peak {np.nanmax(d):.4f}")
