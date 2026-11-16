"""Index of the Hessian eigenline field of H_k at the origin (arXiv 2610.34036, formula (0.2), Theorem 1.3).

H_k(z) = exp(-|z|^(-k/4)) F(z^(-k/2)),  F(x + iy) = a(x) - a(y) + sin x sin y,  a(t) = sin^4 t + 3 sin^2 t.
With H_zz = (H_xx - H_yy - 2i H_xy)/4 the eigenline angle theta satisfies 2 theta = -arg(H_zz) (mod 2 pi), so the
index on a circle around 0 is -wind(H_zz)/2.  Claimed: 1 + k/2.
H_zz is taken by central differences at 50 digits (step 1e-14), on circles of two radii, and the winding number
is the sum of the argument increments; the largest single increment is printed so that an undersampled circle
would show.
"""
import mpmath as mp

mp.mp.dps = 50


def F(w):
    x, y = mp.re(w), mp.im(w)
    sx, sy = mp.sin(x), mp.sin(y)
    return sx ** 4 + 3 * sx ** 2 - sy ** 4 - 3 * sy ** 2 + sx * sy


def H(k, x, y):
    z = mp.mpc(x, y)
    r = abs(z)
    return mp.exp(-r ** (-mp.mpf(k) / 4)) * F(z ** (-mp.mpf(k) / 2))


def Hzz(k, x, y, h):
    f = lambda a, b: H(k, x + a * h, y + b * h)
    f0 = f(0, 0)
    hxx = (f(1, 0) - 2 * f0 + f(-1, 0)) / (h * h)
    hyy = (f(0, 1) - 2 * f0 + f(0, -1)) / (h * h)
    hxy = (f(1, 1) - f(1, -1) - f(-1, 1) + f(-1, -1)) / (4 * h * h)
    return mp.mpc(hxx - hyy, -2 * hxy) / 4


def main():
    h = mp.mpf(10) ** (-14)
    for k in (1, 2, 3, 4):
        for r in (mp.mpf("0.35"), mp.mpf("0.2")):
            n = 6000
            prev = None
            total = mp.mpf(0)
            biggest = mp.mpf(0)
            smallest = None
            first = None
            for i in range(n + 1):
                t = 2 * mp.pi * i / n
                v = Hzz(k, r * mp.cos(t), r * mp.sin(t), h)
                a = abs(v)
                if smallest is None or a < smallest:
                    smallest = a
                if prev is not None:
                    d = mp.arg(v / prev)
                    total += d
                    biggest = max(biggest, abs(d))
                prev = v
            wind = total / (2 * mp.pi)
            print("k = %d, circle |z| = %s, %d samples: winding of H_zz = %s, index = %s (claimed %s); largest step in the argument %s rad; min |H_zz| on the circle %s" % (k, mp.nstr(r, 3), n, mp.nstr(wind, 8), mp.nstr(-wind / 2, 8), mp.nstr(1 + mp.mpf(k) / 2, 3), mp.nstr(biggest, 3), mp.nstr(smallest, 3)), flush=True)


if __name__ == "__main__":
    main()
