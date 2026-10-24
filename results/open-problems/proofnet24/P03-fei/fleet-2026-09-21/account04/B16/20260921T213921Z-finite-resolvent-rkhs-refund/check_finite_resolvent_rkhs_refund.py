from fractions import Fraction
from itertools import product
from math import sin, cos, exp, log1p, sqrt
import random


def vertices(n):
    return list(product((0, 1), repeat=n))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) & 1


def affine_words(n):
    V = vertices(n)
    out = []
    for c in (0, 1):
        for a in V:
            out.append(tuple((c ^ dot(a, x)) for x in V))
    return out


def c0_relations(n):
    V = vertices(n)
    N = len(V)
    out = []
    for mask in range(1 << N):
        inds = [i for i in range(N) if (mask >> i) & 1]
        if len(inds) & 1:
            continue
        xo = [0] * n
        for i in inds:
            for j, b in enumerate(V[i]):
                xo[j] ^= b
        if not any(xo):
            out.append(tuple(1 if i in inds else 0 for i in range(N)))
    return out


def F(T, x):
    if x == 0.0:
        return 0.0
    return x * log1p(T / x)


def K(T, u, v):
    return F(T, (u + v) * (u + v)) - F(T, (u - v) * (u - v))


def w_lt(T, s):
    if abs(s) < 1e-9:
        return (2.0 / 3.0) * T ** 1.5
    a = s * sqrt(T)
    return 4.0 / s**3 * (1.0 - exp(-a) * (1.0 + a + 0.5 * a * a))


def w_gt(T, s):
    a = s * sqrt(T)
    return 4.0 / s**3 * exp(-a) * (1.0 + a + 0.5 * a * a)


def simpson(f, a, b, n=20000):
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i & 1 else 2) * f(a + i * h)
    return total * h / 3


# 1. Exact algebraic low/high Borel multipliers.
for s in (0.03, 0.2, 0.7, 1.3, 4.0, 10.0):
    lhs = w_lt(2.0, s) + w_gt(2.0, s)
    rhs = 4.0 / s**3
    assert abs(lhs - rhs) <= 2e-10 * max(1.0, abs(rhs))


# 2. Scalar finite-window polarization kernel against its positive sine feature.
random.seed(1604)
for _ in range(30):
    T = 10 ** random.uniform(-1.2, 0.4)
    u = random.uniform(-1, 1)
    v = random.uniform(-1, 1)
    integ = 2 * simpson(
        lambda s: w_lt(T, s) * sin(u * s) * sin(v * s),
        0.0,
        180.0,
        36000,
    )
    # The unintegrated tail is O(S^-2); this tolerance is deliberately loose.
    assert abs(integ - K(T, u, v)) < 4e-4


# 3. PSD sanity checks for K_T.
for T in (0.1, 0.5, 2.0, 5.0):
    for _ in range(100):
        us = [random.uniform(-1, 1) for _ in range(6)]
        cs = [random.uniform(-2, 2) for _ in range(6)]
        q = sum(
            cs[i] * cs[j] * K(T, us[i], us[j])
            for i in range(6)
            for j in range(6)
        )
        assert q > -2e-10


quad_checks = 0
quartic_checks = 0
borel_checks = 0

for n in (2, 3):
    V = vertices(n)
    N = len(V)
    M = affine_words(n)
    D = c0_relations(n)

    faces = []
    for c in range(2, n + 1):
        Q = {i for i, x in enumerate(V) if all(x[j] == 1 for j in range(c))}
        faces.append(Q)

    if n == 2:
        f_samples = [
            tuple(-1 if (mask >> i) & 1 else 1 for i in range(N))
            for mask in range(1 << N)
        ]
    else:
        rng = random.Random(303)
        f_samples = [tuple(rng.choice((-1, 1)) for _ in range(N)) for __ in range(80)]

    for Q in faces:
        for f in f_samples:
            M2f = Fraction(0)
            M2o = Fraction(0)
            M4f = Fraction(0)
            M4o = Fraction(0)

            for m in M:
                sb = [f[i] * ((-1) ** m[i]) for i in range(N)]
                so = [((-1) ** m[i]) for i in range(N)]

                uf = Fraction(sum(sb[i] for i in range(N) if i not in Q), N)
                vf = Fraction(sum(sb[i] for i in Q), N)
                uo = Fraction(sum(so[i] for i in range(N) if i not in Q), N)
                vo = Fraction(sum(so[i] for i in Q), N)

                M2f += uf * vf / Fraction(len(M))
                M2o += uo * vo / Fraction(len(M))
                M4f += (uf**3 * vf + uf * vf**3) / Fraction(len(M))
                M4o += (uo**3 * vo + uo * vo**3) / Fraction(len(M))

            assert M2f == 0 and M2o == 0
            quad_checks += 2

            c4 = 0
            for A in D:
                inds = [i for i, b in enumerate(A) if b]
                if len(inds) != 4:
                    continue
                if sum(1 for i in inds if i in Q) % 2 != 1:
                    continue
                fA = 1
                for i in inds:
                    fA *= f[i]
                if fA == -1:
                    c4 += 1

            rhs = Fraction(-12 * c4, N**4)
            assert M4f - M4o == rhs
            quartic_checks += 1

            # Direct all-order Borel relation identity.
            for s in (0.19, 0.73, 1.31):
                avg = 0.0
                for m in M:
                    sb = [f[i] * ((-1) ** m[i]) for i in range(N)]
                    so = [((-1) ** m[i]) for i in range(N)]
                    uf = sum(sb[i] for i in range(N) if i not in Q) / N
                    vf = sum(sb[i] for i in Q) / N
                    uo = sum(so[i] for i in range(N) if i not in Q) / N
                    vo = sum(so[i] for i in Q) / N
                    avg += (
                        sin(s * uf) * sin(s * vf)
                        - sin(s * uo) * sin(s * vo)
                    ) / len(M)

                theta = s / N
                rel = 0.0
                for A in D:
                    inds = [i for i, b in enumerate(A) if b]
                    if sum(1 for i in inds if i in Q) % 2 != 1:
                        continue
                    fA = 1
                    for i in inds:
                        fA *= f[i]
                    if fA == -1:
                        k = len(inds)
                        rel += (
                            2
                            * ((-1) ** (k // 2))
                            * (sin(theta) ** k)
                            * (cos(theta) ** (N - k))
                        )

                assert abs(avg - rel) < 2e-12
                borel_checks += 1


print("PASS")
print("kernel_identity_numeric=30")
print("kernel_psd_random=400")
print("quadratic_cancellation_exact=", quad_checks)
print("quartic_first_separator_exact=", quartic_checks)
print("borel_relation_identity_numeric=", borel_checks)
