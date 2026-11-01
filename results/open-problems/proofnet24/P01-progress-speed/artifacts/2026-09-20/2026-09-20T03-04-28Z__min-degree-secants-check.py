from fractions import Fraction as F


def b(n, d, lam):
    n, d, lam = F(n), F(d), F(lam)
    return (d - 1) / ((d - lam) * (n + lam * (d - n - 1) / d))


def a(n, d, D, lam):
    n, d, D, lam = F(n), F(d), F(D), F(lam)
    return (D - 1) / ((D - lam) * (n + lam * (D - n - 1) / D))


def g(n, d, D, lam):
    return F(n) * a(n, d, D, lam)


def chord_coeff(x0, x1, y0, y1):
    x0, x1 = F(x0), F(x1)
    s = (y1 - y0) / (x1 - x0)
    c = y0 - s * x0
    return c, s


def max_concave_quadratic(A, B, C, lo, hi):
    lo, hi = F(lo), F(hi)
    cand = [(A * lo * lo + B * lo + C, lo),
            (A * hi * hi + B * hi + C, hi)]
    if A < 0:
        rv = -B / (2 * A)
        if lo <= rv <= hi:
            cand.append((A * rv * rv + B * rv + C, rv))
    return max(cand, key=lambda z: z[0])


def certificate(d, D, L):
    d, D, L = int(d), int(D), F(L)
    bd = b(d, d, L)
    bD = b(D, d, L)
    gd = g(d, d, D, L)
    gD = g(D, d, D, F(1))
    b0, bs = chord_coeff(d, D, bd, bD)
    g0, gs = chord_coeff(d, D, gd, gD)
    # H(r)=r*(b0+bs*r)-(g0+gs*r), Psi=L*H-r.
    A = L * bs
    B = L * b0 - L * gs - 1
    C = -L * g0
    mx, rv = max_concave_quadratic(A, B, C, d, D)
    delta = -mx
    margin = 2 * delta / (F(D) + L) ** 2 if delta > 0 else None
    # Positivity at L makes the denominator of g_d increasing on [1,L], hence g_d decreasing.
    gd_den_derivative_at_L = F(D - 2 * d - 1) - 2 * L * F(D - d - 1, D)
    return dict(d=d, D=D, L=L, bd=bd, bD=bD, gd=gd, gD=gD,
                A=A, B=B, C=C, maxpsi=mx, rstar=rv,
                delta=delta, margin=margin,
                gd_den_derivative_at_L=gd_den_derivative_at_L)


def verify_secants(cert):
    d, D, L = cert['d'], cert['D'], cert['L']
    b0, bs = chord_coeff(d, D, cert['bd'], cert['bD'])
    g0, gs = chord_coeff(d, D, cert['gd'], cert['gD'])
    # Analytic convexity/concavity proves this for all real x; integer checks are sanity checks.
    for n in range(d, D + 1):
        assert b(n, d, L) <= b0 + bs * n
        assert g(n, d, D, L) >= g0 + gs * n


cases = [
    ('deep_d3_D163_L7/4', 3, 163, F(7, 4), F(1, 3_000_000)),
    ('broad_d3_D760_L17/10', 3, 760, F(17, 10), F(1, 10_000_000_000)),
    ('very_broad_d3_D8264_L5/3', 3, 8264, F(5, 3), F(1, 500_000_000_000)),
]

print('P01 T06 general-minimum-degree conditional secant exact checker')
for name, d, D, L, clean_margin in cases:
    c = certificate(d, D, L)
    verify_secants(c)
    assert c['gd_den_derivative_at_L'] > 0
    assert c['maxpsi'] < 0
    assert c['delta'] < d
    assert c['margin'] > clean_margin
    fail = certificate(d, D + 1, L)
    assert fail['maxpsi'] > 0
    print(name)
    for k in ['bd','bD','gd','gD','A','B','C','rstar','maxpsi','delta','margin','gd_den_derivative_at_L']:
        print(' ', k, '=', c[k], '~', float(c[k]))
    print(' clean_margin >', clean_margin, '~', float(clean_margin))
    print(' next_D', D + 1, 'maxpsi =', fail['maxpsi'], '~', float(fail['maxpsi']))

# theta_3=3/(1+sqrt(2/3)) is below all three chosen endpoints.
assert F(2,3) > F(25,49)   # theta_3 < 7/4
assert F(2,3) > F(169,289) # theta_3 < 17/10
assert F(2,3) > F(16,25)   # theta_3 < 5/3

print('published theta_3 is strictly below all three chosen L endpoints')
print('ALL_EXACT_CHECKS_PASS')
