#!/usr/bin/env python3
"""Small normalization checks for the boundary lemma; no PDE discretization."""
import itertools
import math
import os
import resource
import signal
from decimal import Decimal as D, localcontext
from fractions import Fraction as F

signal.alarm(60)
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

def norm(z):
    return sum(x*x for x in z)

def dot(z, w):
    return sum(x*y for x, y in zip(z, w))

def sub(z, w):
    return tuple(x-y for x, y in zip(z, w))

def cmul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])

def conj(z):
    return (z[0], -z[1])

def cdiv(z, w):
    a = cmul(z, conj(w))
    return tuple(x/norm(w) for x in a)

def phi(p, s):
    return cdiv(sub(s, p), sub((F(1), F(0)), cmul(conj(p), s)))

def inertia(a):
    """Rational symmetric elimination; zero diagonals use a 2 by 2 pivot."""
    if not a:
        return (0, 0, 0)
    n = len(a)
    k = next((i for i in range(n) if a[i][i]), None)
    if k is not None:
        others = [i for i in range(n) if i != k]
        pivot = a[k][k]
        rest = [[a[i][j]-a[i][k]*a[k][j]/pivot for j in others]
                for i in others]
        pos, neg, zero = inertia(rest)
        return (pos+(pivot > 0), neg+(pivot < 0), zero)
    pair = next(((i, j) for i in range(n) for j in range(i+1, n)
                 if a[i][j]), None)
    if pair is None:
        return (0, 0, n)
    i, j = pair
    others = [k for k in range(n) if k not in pair]
    pivot = a[i][j]
    rest = [[a[k][l]-(a[k][i]*a[j][l]+a[k][j]*a[i][l])/pivot
             for l in others] for k in others]
    pos, neg, zero = inertia(rest)
    return (pos+1, neg+1, zero)

# The two independent moment integrations, with pi**(1-j) removed.
for j in (2, 3, 4):
    radial = F(1, 2)
    for k in range(1, j+1):
        radial *= F(k, 2)
    radial *= F(8, 2**j)
    level = F(1, 4)
    for k in range(1, j):
        level *= F(k, 4)
    level *= 4*j
    assert radial == level == F(math.factorial(j), 4**(j-1))
assert F(3, 8)*32 == 12  # H**3 / A**3 = 12/pi**3
print('moments and Holder constant: exact; H**3/A**3 = 12/pi**3')

circle = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(0)),
          (F(0), F(-1)), (F(3, 5), F(4, 5)),
          (F(9999, 10001), F(200, 10001))]
points = [(F(0), F(0)), (F(1, 3), F(-1, 4)),
          (F(89, 100), F(0)), (F(-3, 10), F(7, 10))]
assert all(norm(s) == 1 for s in circle)
assert all(norm(p) < F(81, 100) for p in points)

one_cases = two_cases = 0
with localcontext() as ctx:
    ctx.prec = 180
    tol = D('1e-75')

    def dec(x):
        return D(x.numerator)/D(x.denominator)

    def green4(z, w):
        # Original logarithmic ratio, normalized as 4*pi*G.
        top = 1-2*dot(z, w)+norm(z)*norm(w)
        bottom = norm(sub(z, w))
        original = (top/bottom).ln()
        alternate = (1+(1-norm(z))*(1-norm(w))/bottom).ln()
        assert abs(original-alternate) < tol
        return original

    for s in circle:
        sd = tuple(map(dec, s))
        for p in points:
            pd = tuple(map(dec, p))
            target = 2*(1-norm(pd))/norm(sub(sd, pd))  # 4*pi*P_s(p)
            z = cmul(p, conj(s))
            denominator = norm(sub((F(1), F(0)), z))
            derivative = 2*((1-z[0])+z[0]*(1-z[0])-z[1]*z[1])/denominator
            assert derivative == 2*(1-norm(p))/norm(sub(s, p))
            for exponent in (4, 8, 16, 30, 40):
                e = D(10)**(-exponent)
                r = 1-e
                observed = green4(tuple(r*x for x in sd), pd)/e
                # Uniform analytic bound for |p|<=0.9, r>=0.95.
                assert abs(observed-target) <= D(352400)*e+tol
                one_cases += 1

    for s, t in itertools.combinations(circle, 2):
        sd, td = tuple(map(dec, s)), tuple(map(dec, t))
        delta2 = norm(sub(sd, td))
        target = 4/delta2  # 4*pi*N_0(s,t)
        for exponent in (4, 8, 16, 30, 40):
            e = D(10)**(-exponent)
            r = 1-e
            observed = green4(tuple(r*x for x in sd), tuple(r*x for x in td))/e**2
            q = (1+r)**2/(r*r*delta2)
            bound = 4*e/(r*r*delta2)+e*e*q*q/2
            assert abs(observed-target) <= bound+tol
            two_cases += 1

    # Integrate the angular Fourier series independently of the log primitive.
    for r in (D('0.25'), D('0.5'), D('0.75'), D('0.9')):
        u = r*r
        total = u
        power = u*u
        for n in range(1, 2001):
            total += 2*power/(n+1)
            power *= u
        primitive = -u-2*(1-u).ln()  # 4*pi*integral P_s**2
        assert abs(total-primitive) < D('1e-70')
    diagonal = []
    for exponent in (2, 4, 8, 16, 30):
        r = 1-D(10)**(-exponent)
        value = -r*r-2*(1-r*r).ln()
        diagonal.append(value)
    assert all(x < y for x, y in zip(diagonal, diagonal[1:]))
    print('Poisson squared integral: 4 series/primitive comparisons; 5 growing cutoff values')
    print('normalized cutoff values:', ', '.join(f'{x:.6f}' for x in diagonal))

print(f'radial limits: {one_cases} one-boundary and {two_cases} two-boundary high-precision cases')

families = signs = 0
for p in points:
    for count in (1, 2, 3, 4, 6):
        nodes = circle[:count]
        ell = [2*norm(sub(s, p))/(1-norm(p)) for s in nodes]
        block = [[norm(sub(s, t)) for t in nodes] for s in nodes]
        bordered = [row+[ell[i]] for i, row in enumerate(block)]+[ell+[F(0)]]
        expected = (1, min(3, count), max(0, count-3))
        assert inertia(bordered) == expected
        mapped = [phi(p, s) for s in nodes]
        assert all(norm(u) == 1 for u in mapped)
        normalized = [[block[i][j]/(ell[i]*ell[j]) for j in range(count)]
                      for i in range(count)]
        for i in range(count):
            for j in range(count):
                assert normalized[i][j] == norm(sub(mapped[i], mapped[j]))/4
        for seed in range(7):
            a = [F((i+1)*(seed+2) % 9-4) for i in range(count-1)]
            a += [-sum(a)]
            form = sum(a[i]*a[j]*normalized[i][j]
                       for i in range(count) for j in range(count))
            barycenter = tuple(sum(a[i]*mapped[i][axis] for i in range(count))
                               for axis in range(2))
            assert form == -norm(barycenter)/2 <= 0
            signs += 1
        families += 1
print(f'zero-potential bordered forms: {families} exact inertia checks; {signs} distance/sign identities')
print('PASS (elementary kernel arithmetic only)')
print(f'priority={os.getpriority(os.PRIO_PROCESS, 0)}, '
      f'peak_rss_bytes={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}')
