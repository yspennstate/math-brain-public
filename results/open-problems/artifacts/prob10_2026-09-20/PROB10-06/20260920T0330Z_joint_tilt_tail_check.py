from fractions import Fraction as F
import itertools
import math
import sympy as sp

lam = sp.symbols('lam')
p = sp.symbols('p')


def bernstein_coeffs(poly, var):
    P = sp.Poly(sp.expand(poly), var, domain=sp.QQ)
    n = P.degree()
    a = [P.nth(k) for k in range(n + 1)]
    out = []
    for j in range(n + 1):
        s = sp.Rational(0)
        for k in range(j + 1):
            s += a[k] * sp.Rational(math.comb(j, k), math.comb(n, k))
        out.append(sp.factor(s))
    return out


def bernstein_interval(poly, var, a, b):
    t = sp.symbols('_t')
    q = sp.expand(poly.subs(var, a + (b - a) * t))
    return bernstein_coeffs(q, t)


def certify_poly_positive(poly, var, a=sp.Rational(0), b=sp.Rational(1), depth=0, maxdepth=16):
    coeffs = bernstein_interval(poly, var, a, b)
    if min(coeffs) > 0:
        return True, depth, min(coeffs)
    if depth >= maxdepth:
        return False, depth, min(coeffs)
    mid = (a + b) / 2
    ok1, d1, m1 = certify_poly_positive(poly, var, a, mid, depth + 1, maxdepth)
    if not ok1:
        return False, d1, m1
    ok2, d2, m2 = certify_poly_positive(poly, var, mid, b, depth + 1, maxdepth)
    return ok2, max(d1, d2), min(m1, m2)


def certify_rational_positive(expr, var, a, b):
    num, den = [sp.factor(x) for x in sp.together(expr).as_numer_denom()]
    mid = (a + b) / 2
    denmid = sp.sign(sp.N(den.subs(var, mid), 80))
    assert denmid in (-1, 1)
    s = sp.Integer(int(denmid))
    okd, dd, md = certify_poly_positive(sp.expand(s * den), var, a, b)
    okn, dn, mn = certify_poly_positive(sp.expand(s * num), var, a, b)
    return okd and okn, max(dd, dn), min(md, mn)


# Type-conditioned escape/log-derivative envelopes inherited from the
# preceding R02 report, valid for the {2,3} offspring family and 1<=lambda<2.
a = lam - 1
b2 = (2 - lam) / 2
b3 = 3 * (2 - lam) / (6 - lam)
u2 = 2 * (3 - lam) / (lam + 6)
u3 = (3 - lam) / 3
q2u = 1 / (2 - lam)
q3u = 4 / ((2 - lam) * (6 - lam))
q2l = 9 / ((3 - lam) * (lam + 6))
q3l = 1 / (3 - lam)


def pattern_expr(n, m, upper):
    smin = (n - m) * b2 + m * b3
    smax = (n - m) * u2 + m * u3
    ymin = sp.factor(smin / (a + smin))
    ymax = sp.factor(smax / (a + smax))
    if upper:
        Q = sp.factor(((n - m) * u2 * q2u + m * b3 * q3u) /
                      ((n - m) * u2 + m * b3))
        r = sp.factor((1 + a * Q) / (a + smin))
    else:
        Q = sp.factor(((n - m) * b2 * q2l + m * u3 * q3l) /
                      ((n - m) * b2 + m * u3))
        r = sp.factor((1 + a * Q) / (a + smax))
    return ymin, ymax, Q, r


def endpoint_constants(n, upper, L0, L1):
    out = []
    for m in range(n + 1):
        ymin, ymax, Q, r = pattern_expr(n, m, upper)
        # On each certified strip ymin,ymax decrease and r increases.
        lo = sp.factor(ymin.subs(lam, L1))
        hi = sp.factor(ymax.subs(lam, L0))
        rr = sp.factor(r.subs(lam, L1 if upper else L0))
        assert lo > 0 and hi > 0 and lo <= hi and rr > 0
        out.append((lo, hi, rr))
    return out


def ratio_corner(n, const, bits):
    num = sp.Rational(0)
    den = sp.Rational(0)
    for m, (lo, hi, r) in enumerate(const):
        x = hi if bits[m] else lo
        prob = sp.binomial(n, m) * p**m * (1 - p)**(n - m)
        num += prob * x * r
        den += prob * x
    return sp.factor(num), sp.factor(den)


def certify_strip(L0, L1, psmall, plarge, R):
    # 1) Exact lambda monotonicity of all pattern-envelope quantities.
    mono = 0
    max_depth = 0
    for n, upper in [(3, True), (4, False)]:
        for m in range(n + 1):
            ymin, ymax, Q, r = pattern_expr(n, m, upper)
            for expr, sgn in [(sp.diff(ymin, lam), -1),
                              (sp.diff(ymax, lam), -1),
                              (sp.diff(r, lam), +1)]:
                ok, d, mb = certify_rational_positive(sgn * expr, lam, L0, L1)
                assert ok
                mono += 1
                max_depth = max(max_depth, d)
    assert mono == 27

    Uconst = endpoint_constants(3, True, L0, L1)
    Lconst = endpoint_constants(4, False, L0, L1)
    Ucorners = [ratio_corner(3, Uconst, bits)
                for bits in itertools.product([0, 1], repeat=4)]
    Lcorners = [ratio_corner(4, Lconst, bits)
                for bits in itertools.product([0, 1], repeat=5)]

    # 2) Keep theta coupled to p using 3/4 <= t=c3/c2 <= 1.
    # Small tail: theta <= p and g(theta)<=g(p)=p(1-p)/(2+p).
    # Large tail: theta >= 3p/(4-p), and on the large-tail side
    # g(theta)<=g(3p/(4-p))=12p(1-p)/((4-p)(8+p)).
    count = 0
    worst = None
    for i, (Nu, Du) in enumerate(Ucorners):
        for j, (Nl, Dl) in enumerate(Lcorners):
            diff_num = sp.expand(Nu * Dl - Nl * Du)

            poly_s = sp.factor(
                R * (2 + p) * Du * Dl
                - L1 * p * (1 - p) * diff_num
            )
            ok, d, mb = certify_poly_positive(poly_s, p, sp.Rational(0), psmall)
            assert ok, ('small', i, j, d, mb)
            max_depth = max(max_depth, d)
            if worst is None or mb < worst[0]:
                worst = (mb, 'small', i, j)
            count += 1

            poly_l = sp.factor(
                R * (4 - p) * (8 + p) * Du * Dl
                - 12 * L1 * p * (1 - p) * diff_num
            )
            ok, d, mb = certify_poly_positive(poly_l, p, plarge, sp.Rational(1))
            assert ok, ('large', i, j, d, mb)
            max_depth = max(max_depth, d)
            if mb < worst[0]:
                worst = (mb, 'large', i, j)
            count += 1

    assert count == 2 * 16 * 32

    # If lambda*g(theta)*Delta <= R<1 then
    # -ell' = 2[(2+theta)-lambda theta(1-theta)Delta]/(2+theta+lambda)^2
    #       >= 4(1-R)/(3+L1)^2.
    margin = sp.factor(4 * (1 - R) / (3 + L1)**2)
    assert margin > 0
    return mono, count, max_depth, worst, margin


strip1 = certify_strip(
    sp.Rational(1851, 1000), sp.Rational(19, 10),
    sp.Rational(31, 200), sp.Rational(41, 50),
    sp.Rational(999, 1000)
)
strip2 = certify_strip(
    sp.Rational(19, 10), sp.Rational(983, 500),
    sp.Rational(1, 27), sp.Rational(22, 23),
    sp.Rational(99, 100)
)

assert strip1[4] == sp.Rational(2, 12005)
assert strip2[4] == sp.Rational(10000, 6165289)

print('PROB10-06 exact joint p-theta tail checker')
print('strip 1: lambda in [1851/1000,19/10]')
print('  p regions: [0,31/200] union [41/50,1]')
print('  target lambda*g(theta)*Delta <= 999/1000')
print('  monotonicity checks:', strip1[0])
print('  corner-tail inequalities:', strip1[1])
print('  max Bernstein subdivision depth:', strip1[2])
print('  derivative margin -ell_prime >=', strip1[4], '~', float(strip1[4]))
print('strip 2: lambda in [19/10,983/500]')
print('  p regions: [0,1/27] union [22/23,1]')
print('  target lambda*g(theta)*Delta <= 99/100')
print('  monotonicity checks:', strip2[0])
print('  corner-tail inequalities:', strip2[1])
print('  max Bernstein subdivision depth:', strip2[2])
print('  derivative margin -ell_prime >=', strip2[4], '~', float(strip2[4]))
print('ALL_EXACT_CHECKS_PASS')
