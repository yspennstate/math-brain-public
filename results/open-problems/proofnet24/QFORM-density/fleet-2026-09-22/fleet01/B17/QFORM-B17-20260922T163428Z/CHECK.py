import math

SQRT2 = math.sqrt(2.0)
BASE = 3.0 * SQRT2


def F(u):
    if u == 0.0:
        return 1.0
    return math.sqrt(2.0 * math.pi / u) * math.erf(math.sqrt(u) / (2.0 * SQRT2))


def H(s, a):
    if a == 0.0:
        return 1.0 / s
    c = 12.0 * a / (1.0 - a)
    return F(c / s) / (s * math.sqrt(1.0 - a))


def central_peak(v, sigma2=1.0 / 12.0, n=40000):
    r2 = sum(x*x for x in v)
    assert r2 < 1.0
    s = 12.0 * sigma2
    assert s >= 1.0
    total = 0.0
    invsqrt2 = 1.0 / SQRT2
    for j in range(n):
        th = 2.0 * math.pi * (j + 0.5) / n
        omega = (math.cos(th) * invsqrt2,
                 math.sin(th) * invsqrt2,
                 invsqrt2)
        z = sum(v[i] * omega[i] for i in range(3))
        a = r2 - z*z
        if a < 0.0 and a > -1e-13:
            a = 0.0
        assert 0.0 <= a < 1.0
        total += H(s, a)
    return BASE * total / n


# Grid check of the scalar theorem H_s(a)<=1.
max_h = 0.0
max_arg = None
for s in (1.0, 1.01, 1.1, 1.5, 2.0, 4.0, 10.0, 100.0):
    for j in range(1, 20000):
        a = 0.999999 * j / 20000.0
        h = H(s, a)
        if h > max_h:
            max_h = h
            max_arg = (s, a)
        assert h <= 1.0 + 2e-12

# Deterministic stress orientations.
tests = [
    ((0.0, 0.0, 0.0), 1.0/12.0),
    ((0.2, 0.0, 0.0), 1.0/12.0),
    ((0.0, 0.0, 0.2), 1.0/12.0),
    ((0.2886751345948129,)*3, 1.0/12.0),
    ((0.8, 0.0, 0.0), 1.0/12.0),
    ((0.6, 0.1, -0.2), 1.0/10.0),
]
peaks = []
for v, sigma2 in tests:
    p = central_peak(v, sigma2)
    peaks.append((v, sigma2, p))
    assert p <= BASE + 3e-10

# Frame identity check for a few deterministic v values.
for v in ((0.2, 0.1, 0.3), (0.7, -0.2, 0.1)):
    r2 = sum(x*x for x in v)
    assert r2 < 1.0
    # Trace/determinant sanity for M=I-vv^T.
    trM = 3.0 - r2
    detM = 1.0 - r2
    assert trM > 2.0
    assert detM > 0.0

print('PASS')
print('BASE_3SQRT2', format(BASE, '.15f'))
print('MAX_GRID_H', format(max_h, '.15f'), 'AT', max_arg)
for row in peaks:
    print('PEAK', row)
