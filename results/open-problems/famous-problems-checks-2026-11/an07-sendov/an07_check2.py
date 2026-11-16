"""Steps of the Mazur-Tao proof of Sendov's conjecture, tested from the statements in Tao's exposition of
12 Aug 2026 (numbering of that text).

Part A  Lemma 6, the four identities (7)-(10), on random polynomials with a zero at a in (0, 1).  The identities
        are algebraic: they hold for any polynomial with p(a) = 0 and p'(a) != 0, critical points a - 1/q_j.
Part B  The pointwise inequalities used with points q_j of the closed unit disk (no polynomial needed):
        (24)-(25)  prod |t(1-a^2) q_j + a| <= (a^2 + 2 a t x (1-a^2) + t^2 (1-a^2)^2)^((n-1)/2)
                   <= exp(alpha(-1 + (2 - beta(1)) t));
        the derivative bound |F'(t) + (n-1) a (x+iy) F(t)| <= a^2 t (n-1) beta(t)^((n-2)/2).
Part C  Lemma 13 (defect lemma), and the step after it: for z_j, q_j in the disk satisfying the centroid
        identity, |J sum((n-1)/n 1/z_j + q_j) - a J (n-1)^2/n| <= 1 - |J|^2.
Part D  Scalar steps: (27) log(sinh h / h) <= sqrt(h^2+9) - 3; (17) implies (18) on a grid; (35) for n >= 5;
        the numbers 0.1825 and 1.948 in the proof of alpha <= 17; (19) implies (21) for random (a, x, n).
Part E  Inequality (22) (eta replaced by alpha/(3+alpha)) for 5 <= n <= 200 with Tao's side condition
        c(alpha)^2 <= a^2, and the large-n bound 0.399.
"""
import math
import random

import numpy as np

from an07_check import F as Fscalar

T, W = np.polynomial.legendre.leggauss(120)
T = 0.5 * (T + 1.0)
W = 0.5 * W


def part_a(rng):
    worst = 0.0
    cases = 0
    for n in range(3, 11):
        for _ in range(250):
            a = rng.uniform(0.05, 0.95)
            z = np.array([complex(rng.uniform(-1.2, 1.2), rng.uniform(-1.2, 1.2)) for _ in range(n - 1)])
            p = np.poly(np.concatenate(([a], z)))
            dp = np.polyder(p)
            w = np.roots(dp)
            if abs(np.polyval(dp, a)) < 1e-3 or np.abs(w - a).min() < 0.05 or np.abs(z).min() < 0.05 or np.abs(z - a).min() < 0.05:
                continue
            q = 1.0 / (a - w)
            lhs7 = (a + z.sum()) / n
            rhs7 = (a - 1.0 / q).sum() / (n - 1)
            lhs8 = np.prod((1 - a * z) / (a - z))
            rhs8 = (W * np.prod(T[:, None] * (1 - a * a) * q[None, :] + a, axis=1)).sum()
            Ft = np.prod(1 - a * T[:, None] * q[None, :], axis=1)
            sign = (-1) ** (n - 1)
            lhs9 = sign * np.prod(z)
            rhs9 = n / np.prod(q) * (W * Ft).sum()
            lhs10 = sign * np.prod(z) * (1 + a * (1 / z).sum())
            rhs10 = n / np.prod(q) * np.prod(1 - a * q)
            for l, r in ((lhs7, rhs7), (lhs8, rhs8), (lhs9, rhs9), (lhs10, rhs10)):
                err = abs(l - r) / max(1.0, abs(l), abs(r))
                worst = max(worst, err)
                assert err < 1e-6, ("identity fails", n, err)
            cases += 1
    print("part A: identities (7)-(10) on %d random polynomials of degree 3 to 10; largest relative error %.1e" % (cases, worst), flush=True)


def disk_points(rng, k, rmin=0.0):
    out = []
    for _ in range(k):
        r = math.sqrt(rng.uniform(rmin * rmin, 1.0)) if rng.random() < 0.7 else rng.uniform(0.97, 1.0)
        th = rng.uniform(-math.pi, math.pi) if rng.random() < 0.5 else rng.gauss(0.0, 0.3)
        out.append(r * complex(math.cos(th), math.sin(th)))
    return np.array(out)


def part_b(rng):
    n_cases = 0
    worst = [0.0, 0.0, 0.0]
    for _ in range(4000):
        n = rng.randint(3, 40)
        a = rng.uniform(0.01, 0.999)
        q = disk_points(rng, n - 1)
        x = q.real.mean()
        mean = q.mean()
        alpha = (n - 1) * (1 - a * a) / 2
        beta1 = 1 - 2 * a * x + a * a
        for t in (0.0, 0.03, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0):
            lhs = np.prod(np.abs(t * (1 - a * a) * q + a))
            base = a * a + 2 * a * t * x * (1 - a * a) + t * t * (1 - a * a) ** 2
            mid = base ** ((n - 1) / 2) if base > 0 else 0.0
            top = math.exp(alpha * (-1 + (2 - beta1) * t))
            assert lhs <= mid * (1 + 1e-9) + 1e-12, ("(24)-(25) fails", n, a, t)
            assert mid <= top * (1 + 1e-9), ("exp bound fails", n, a, t)
            worst[0] = max(worst[0], lhs / mid if mid > 0 else 0.0)
            worst[1] = max(worst[1], mid / top)
            fac = 1 - a * t * q
            Fv = np.prod(fac)
            dF = sum(-a * q[j] * np.prod(np.delete(fac, j)) for j in range(n - 1))
            bt = 1 - 2 * a * x * t + a * a * t * t
            bound = a * a * t * (n - 1) * bt ** ((n - 2) / 2)
            dev = abs(dF + (n - 1) * a * mean * Fv)
            assert dev <= bound * (1 + 1e-9) + 1e-12, ("derivative bound fails", n, a, t, dev, bound)
            if bound > 0:
                worst[2] = max(worst[2], dev / bound)
        n_cases += 1
    print("part B: %d point sets in the disk, 8 values of t each: largest ratios (24)-(25) %.4f, exp bound %.4f, derivative bound %.4f" % (n_cases, worst[0], worst[1], worst[2]), flush=True)


def part_c(rng):
    worst = 0.0
    for _ in range(20000):
        N = rng.randint(1, 30)
        w = disk_points(rng, N, rmin=0.05)
        P = np.prod(np.abs(w))
        lhs = P * np.abs(1 / w - np.conj(w)).sum()
        rhs = 1 - P * P
        assert lhs <= rhs + 1e-10, ("defect lemma fails", N)
        if rhs > 1e-9:
            worst = max(worst, lhs / rhs)
    print("part C: defect lemma on 20000 point sets; largest lhs/rhs %.4f" % worst, flush=True)
    done = 0
    tries = 0
    worst2 = 0.0
    while done < 3000 and tries < 400000:
        tries += 1
        n = rng.randint(5, 30)
        a = rng.uniform(0.05, 0.99)
        q = disk_points(rng, n - 1, rmin=0.6)
        S = (n - 1) * a - n / (n - 1) * (1 / np.conj(q)).sum().conjugate()   # required sum of z_j: from (7)
        S = (n - 1) * a - n / (n - 1) * (1 / q).sum()
        c = S / (n - 1)
        if abs(c) > 0.9:
            continue
        d = np.array([complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(n - 1)])
        d -= d.mean()
        d *= rng.uniform(0.0, 1.0) * (1 - abs(c)) / max(1e-12, np.abs(d).max())
        z = c + d
        if np.abs(z).max() > 1 or np.abs(z).min() < 1e-3:
            continue
        assert abs((a + z.sum()) / n - (a - 1 / q).sum() / (n - 1)) < 1e-9
        J = np.prod(z) * np.prod(q)
        lhs = abs(J * ((n - 1) / n * (1 / z).sum() + q.sum()) - a * J * (n - 1) ** 2 / n)
        rhs = 1 - abs(J) ** 2
        assert lhs <= rhs + 1e-9, ("defect step fails", n, lhs, rhs)
        worst2 = max(worst2, lhs / rhs)
        done += 1
    assert done == 3000
    print("part C: the step after the defect lemma on %d configurations satisfying the centroid identity; largest lhs/rhs %.4f" % (done, worst2), flush=True)


def part_d(rng):
    h = np.concatenate((np.linspace(1e-3, 5, 20000), np.linspace(5, 400, 20000)))
    lhs = np.where(h < 300, np.log(np.sinh(np.minimum(h, 300)) / h), h - np.log(2 * h))
    gap = np.sqrt(h * h + 9) - 3 - lhs
    assert gap.min() > -1e-12
    print("part D: (27) on 40000 values of h in (0, 400]; smallest gap %.2e (at h = %.3f)" % (gap.min(), h[int(np.argmin(gap))]), flush=True)

    al = np.linspace(0.01, 40, 2000)[:, None]
    be = np.linspace(0.0005, 0.9995, 2000)[None, :]
    integral = (np.exp(al * (1 - be)) - np.exp(-al)) / (al * (2 - be))
    feasible = integral > 1
    bound = np.minimum(al / (3 + al), np.where(al > 0, 1 - np.log(al) / al, 1.0))
    viol = feasible & (be >= bound)
    print("        (17) implies (18): %d grid points (alpha, beta(1)) satisfy (17); violations of (18) among them: %d" % (int(feasible.sum()), int(viol.sum())), flush=True)
    assert viol.sum() == 0

    worst35 = 1e9
    for n in range(5, 400):
        a = np.linspace(0.0, 1.0, 4001)
        val = (n - 1) ** 2 * a * a - (3 * n - 1) * a + (n - 1)
        worst35 = min(worst35, float(val.min()))
        assert (3 * n - 1) ** 2 - 4 * (n - 1) ** 3 < 0
    assert (3 * 4 - 1) ** 2 - 4 * 3 ** 3 > 0
    print("        (35): the quadratic is positive on [0, 1] for 5 <= n < 400 (smallest value %.3f); its discriminant is negative for n >= 5 and positive for n = 4" % worst35, flush=True)

    u = np.linspace(0, 20, 2000001)
    m = float((u * (1 + u) * 17.0 ** (-u)).max())
    rhs = 1 / (2 * 35 * 17) + 4 * 36 * 35 / (34 ** 2 * math.log(17)) + 2 * 36 / 35 * m * 17 ** (1 / 34)
    print("        alpha <= 17: max of u(1+u)17^(-u) = %.5f (text: at most 0.1825); right-hand side %.4f (text: at most 1.948), below 2" % (m, rhs), flush=True)
    assert m <= 0.1825 and rhs <= 1.948

    worst = -1e9
    cases = 0
    for _ in range(40000):
        n = rng.randint(5, 250)
        a = rng.uniform(0.02, 0.9995) if rng.random() < 0.5 else math.sqrt(max(1e-6, 1 - 2 * rng.uniform(0.01, 17) / (n - 1)))
        x = rng.uniform(a / 2 + 1e-6, 1.0)
        alpha = (n - 1) * (1 - a * a) / 2
        b1 = 1 - 2 * a * x + a * a
        if not (0 < b1 < 1):
            continue
        beta = 1 - 2 * a * x * T + a * a * T * T
        r19 = (1 - x * x) / (2 * (n - 1)) + a * a * n * (n - 1) * (W * T * beta ** ((n - 2) / 2)).sum()
        l19 = 2 * alpha + a * x
        r21 = (b1 / (2 * alpha * (1 - b1)) + b1 / (4 * alpha) + 1 / (2 * (n - 1)) + b1 / (4 * alpha * (n - 1))
               + a ** 4 * n * (n - 1) * (n - 2) * b1 / (4 * alpha) * (W * T ** 3 * beta ** ((n - 4) / 2)).sum())
        slack = 2 * alpha * (r21 - 1) - (r19 - l19)
        assert slack >= -1e-7 * max(1.0, abs(r19)), ("(19) does not imply (21)", n, a, x, slack)
        worst = max(worst, -slack)
        cases += 1
    print("        (19) implies (21): 2 alpha (rhs(21) - 1) >= rhs(19) - lhs(19) in all %d random cases (a, x, n), n up to 250" % cases, flush=True)


def part_e():
    da = 0.005
    best = (-1.0, None)
    rows = {}
    for n in range(5, 201):
        m = n - 1.0
        al = np.arange(da, 17.0 + da / 2, da)
        al = al[al < m / 2]
        eta = al / (3 + al)
        c = 1 - al / m - eta / 2
        ok = (c >= 0) & (c * c <= 1 - 2 * al / m)
        al, eta = al[ok], eta[ok]
        v = Fscalar(eta, al, n)
        i = int(np.argmax(v))
        rows[n] = (float(v[i]), float(al[i]))
        if v[i] > best[0]:
            best = (float(v[i]), n, float(al[i]))
    print("part E: right-hand side of (22) for 5 <= n <= 200, alpha step %.3f, with c(alpha)^2 <= a^2: largest value %.4f at n = %d, alpha = %.3f" % (da, best[0], best[1], best[2]), flush=True)
    for n in (5, 6, 8, 20, 40, 50, 52, 53, 54, 56, 60, 80, 120, 200):
        print("        n = %3d: max %.4f at alpha = %.3f" % (n, rows[n][0], rows[n][1]), flush=True)
    assert best[0] < 1
    n = 201
    tail = 1 / 6 + 1 / 12 + 7 / (12 * 200) + 24 * 201 * 200 * 199 / 197 ** 4 + 201 * 200 * 199 / 48 * (17 / 20) ** ((201 - 4) / 2)
    c17 = 1 - 17 / 200 - 17 / 40
    print("        n > 200: bound %.4f (text: at most 0.399); (3 + 17) c(17)^4 at n = 201 = %.4f (text: 1.1529)" % (tail, 20 * c17 ** 4), flush=True)
    assert tail <= 0.399 and 20 * c17 ** 4 > 1


def main():
    rng = random.Random(11)
    np.random.seed(11)
    part_a(rng)
    part_b(rng)
    part_c(rng)
    part_d(rng)
    part_e()
    print("all assertions passed")


if __name__ == "__main__":
    main()
