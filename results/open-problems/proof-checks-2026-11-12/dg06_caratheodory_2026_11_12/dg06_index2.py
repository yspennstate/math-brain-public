"""Index of the Hessian eigenline field of H_k at the origin, on circles small enough for the leading term.

H_k(z) = b(z) G(z),  b = exp(-|z|^(-k/4)),  G = F(w),  w = z^(-k/2).  With s = |z|^(-k/4):
    b_z / b  = (k/8) s / z
    b_zz / b = ((k/8) s / z)^2 - (k/8)(1 + k/8) s / z^2
    G_z  = F_w w',   G_zz = F_ww w'^2 + F_w w'',   w' = -(k/2) z^(-k/2-1),  w'' = (k/2)(k/2+1) z^(-k/2-2)
    H_zz / b = (b_zz/b) G + 2 (b_z/b) G_z + G_zz.
The leading term F_ww w'^2 has winding -(k+2) (F_ww never vanishes), which is the claimed index 1 + k/2; it
dominates F_w w'' only when |z|^(-k/2) is large against M1 (k/2+1) / (c k/2), about 50 for k = 1.

Step 1: the closed formula against central differences of H_k at 50 digits, at random points.
Step 2: winding of H_zz / b on the circles |z| = 0.35 and 0.2 of dg06_index.py and on circles with
        |w| = |z|^(-k/2) = 3, 30, 400, 2000, at 40 and 200 samples per unit of the path of w; index = -winding / 2.
"""
import cmath
import math
import random

import mpmath as mp


def F_all(w):
    x, y = w.real, w.imag
    sx, cx, sy, cy = math.sin(x), math.cos(x), math.sin(y), math.cos(y)
    a = lambda s: s ** 4 + 3 * s ** 2
    a1 = lambda s, c: (4 * s ** 3 + 6 * s) * c
    a2 = lambda s: 6 - 16 * s ** 4            # a''(t) = 6 - 16 sin^4 t
    F = a(sx) - a(sy) + sx * sy
    Fx = a1(sx, cx) + cx * sy
    Fy = -a1(sy, cy) + sx * cy
    Fxx = a2(sx) - sx * sy
    Fyy = -a2(sy) - sx * sy
    Fxy = cx * cy
    return F, complex(Fx, -Fy) / 2, complex(Fxx - Fyy, -2 * Fxy) / 4


def Hzz_over_b(k, z):
    s = abs(z) ** (-k / 4)
    w = z ** (-k / 2)
    w1 = -(k / 2) * w / z
    w2 = (k / 2) * (k / 2 + 1) * w / (z * z)
    F, Fw, Fww = F_all(w)
    bz = (k / 8) * s / z
    bzz = bz * bz - (k / 8) * (1 + k / 8) * s / (z * z)
    return bzz * F + 2 * bz * Fw * w1 + Fww * w1 * w1 + Fw * w2


def H_mp(k, x, y):
    z = mp.mpc(x, y)
    w = z ** (-mp.mpf(k) / 2)
    sx, sy = mp.sin(mp.re(w)), mp.sin(mp.im(w))
    return mp.exp(-abs(z) ** (-mp.mpf(k) / 4)) * (sx ** 4 + 3 * sx ** 2 - sy ** 4 - 3 * sy ** 2 + sx * sy)


def main():
    mp.mp.dps = 50
    rng = random.Random(4)
    h = mp.mpf(10) ** (-16)
    worst = 0.0
    for k in (1, 2, 3, 4):
        for _ in range(8):
            r = rng.uniform(0.05, 0.6)
            t = rng.uniform(-3.0, 3.0)        # away from the cut of the principal power only for convenience
            x, y = r * math.cos(t), r * math.sin(t)
            f = lambda a, b: H_mp(k, mp.mpf(x) + a * h, mp.mpf(y) + b * h)
            f0 = f(0, 0)
            hxx = (f(1, 0) - 2 * f0 + f(-1, 0)) / (h * h)
            hyy = (f(0, 1) - 2 * f0 + f(0, -1)) / (h * h)
            hxy = (f(1, 1) - f(1, -1) - f(-1, 1) + f(-1, -1)) / (4 * h * h)
            num = mp.mpc(hxx - hyy, -2 * hxy) / 4 / mp.exp(-mp.mpf(r) ** (-mp.mpf(k) / 4))
            ana = Hzz_over_b(k, complex(x, y))
            worst = max(worst, abs(complex(num) - ana) / abs(ana))
    print("step 1: closed formula for H_zz / b against 50-digit central differences at 32 random points (k = 1..4): largest relative difference %.2e" % worst, flush=True)

    for k in (1, 2, 3, 4):
        for R, dens in ((None, 0.35), (None, 0.2), (3.0, 40), (30.0, 40), (30.0, 200), (400.0, 40), (400.0, 200), (2000.0, 40)):
            if R is None:
                # the two circles of dg06_index.py (50-digit differences), for comparison of the two routes
                r = dens
                R = r ** (-k / 2.0)
                dens = 2000
            else:
                r = R ** (-2.0 / k)
            n = int(dens * k * math.pi * R) + 2000
            prev = None
            total = 0.0
            biggest = 0.0
            smallest = None
            for i in range(n + 1):
                t = 2 * math.pi * i / n
                v = Hzz_over_b(k, cmath.rect(r, t))
                if smallest is None or abs(v) < smallest:
                    smallest = abs(v)
                if prev is not None:
                    d = cmath.phase(v / prev)
                    total += d
                    biggest = max(biggest, abs(d))
                prev = v
            wind = total / (2 * math.pi)
            print("k = %d, |w| = %6.0f (|z| = %.3e), %7d samples: winding of H_zz = %8.4f, index = %7.4f (claimed %.1f); largest step %.3f rad; min |H_zz / b| = %.3e" % (k, R, r, n, wind, -wind / 2, 1 + k / 2, biggest, smallest), flush=True)


if __name__ == "__main__":
    main()
