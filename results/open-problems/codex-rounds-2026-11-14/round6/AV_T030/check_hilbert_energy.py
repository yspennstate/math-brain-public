#!/usr/bin/env python3
"""Exact finite and Fourier checks for the final multiplier implication."""
import itertools
import os
import resource
import signal
from fractions import Fraction as F

signal.alarm(60)
# All matrices have order at most eight and use standard-library arithmetic.
# Keep the inherited resource limits; measure actual peak RSS below.
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def distance(x, y):
    return sum((a-b)**2 for a, b in zip(x, y))


def form(b, x, y):
    return sum(x[i]*b[i][j]*y[j] for i in range(len(x))
               for j in range(len(y)))


def inertia(a):
    """Exact symmetric elimination; 2x2 blocks handle zero diagonals."""
    n = len(a)
    if n == 0:
        return (0, 0, 0)
    p = next((i for i in range(n) if a[i][i] != 0), None)
    if p is not None:
        other = [i for i in range(n) if i != p]
        pivot = a[p][p]
        rest = [[a[i][j]-a[i][p]*a[p][j]/pivot for j in other]
                for i in other]
        pos, neg, zero = inertia(rest)
        return (pos+(pivot > 0), neg+(pivot < 0), zero)
    pair = next(((i, j) for i in range(n) for j in range(i+1, n)
                 if a[i][j] != 0), None)
    if pair is None:
        return (0, 0, n)
    i, j = pair
    other = [k for k in range(n) if k not in pair]
    t = a[i][j]
    rest = [[a[k][l]-(a[k][i]*a[j][l]+a[k][j]*a[i][l])/t
             for l in other] for k in other]
    pos, neg, zero = inertia(rest)
    return (pos+1, neg+1, zero)


border_checks = 0
for n in range(1, 8):
    for seed in range(9):
        b = [[F(((i+1)*(j+1)+seed*(i+j+2)) % 11-5, 3)
              for j in range(n)] for i in range(n)]
        ell = [F((i+seed) % 5-2) for i in range(n)]
        if not any(ell):
            ell[0] = F(1)
        k = next(i for i in range(n) if ell[i])
        u = []
        for i in range(n):
            if i == k:
                continue
            v = [F(0)]*n
            v[i], v[k] = F(1), -ell[i]/ell[k]
            assert dot(ell, v) == 0
            u.append(v)
        c = [[form(b, x, y) for y in u] for x in u]
        h = [row+[ell[i]] for i, row in enumerate(b)] + [ell+[F(0)]]
        pos, neg, zero = inertia(c)
        assert inertia(h) == (pos+1, neg+1, zero)
        border_checks += 1
assert border_checks == 63
print(f'bordered inertia identity: {border_checks} exact arbitrary symmetric cases')

# The last zero is a necessary hypothesis for the implication used here.
bad = [[F(-2), F(0), F(1)], [F(0), F(1), F(0)],
       [F(1), F(0), F(-2)]]
assert inertia(bad) == (1, 2, 0)
assert bad[1][1] > 0  # positive on ker((1,0)) despite one positive eigenvalue
print('nonzero last diagonal stress: implication fails at last entry -2')

gram_checks = cnd_checks = 0
all_points = [(F(0), F(0), F(0)), (F(1), F(0), F(0)),
              (F(0), F(1), F(0)), (F(1), F(1), F(0)),
              (F(1, 3), F(-1, 2), F(2)),
              (F(1), F(0), F(0)),  # deliberately repeated location
              (F(-2), F(1, 4), F(1, 2))]
for n in range(1, 8):
    points = all_points[:n]
    k = [F(i+2, 3) for i in range(n)]
    d = [[distance(x, y) for y in points] for x in points]
    b = [[d[i][j]/(k[i]*k[j]) for j in range(n)] for i in range(n)]
    ell = [1/v for v in k]
    h = [row+[ell[i]] for i, row in enumerate(b)]+[ell+[F(0)]]
    assert inertia(h)[0] == 1
    for anchor in range(n):
        gamma = [[(d[i][anchor]+d[j][anchor]-d[i][j])/2
                  for j in range(n)] for i in range(n)]
        anchored = [tuple(a-b for a, b in zip(x, points[anchor]))
                    for x in points]
        assert gamma == [[dot(x, y) for y in anchored] for x in anchored]
        assert inertia(gamma)[1] == 0
        gram_checks += 1
    for seed in range(7):
        a = [F((i+seed) % 5-2) for i in range(n-1)]
        a.append(-sum(a))
        x = [k[i]*a[i] for i in range(n)]
        bary = [sum(a[i]*points[i][axis] for i in range(n))
                for axis in range(3)]
        assert dot(ell, x) == 0
        assert form(d, a, a) == form(b, x, x) == -2*dot(bary, bary)
        cnd_checks += 1
print(f'anchored Gram: {gram_checks} exact cases; CND/barycenter: {cnd_checks}')

# Check the multiplier subtraction itself without assuming variational PSD.
multiplier_checks = diagonal_checks = 0
for n in (2, 3, 5):
    for seed in range(5):
        n0 = [[F(0) if i == j else F(1, i+j+1)
               for j in range(n)] for i in range(n)]
        r = [[F((i+1)*(j+1), 7) for j in range(n)] for i in range(n)]
        curv = [F(i-seed, 3) for i in range(n)]
        g = [(F((i+seed) % 3-1), F(i+1, seed+1)) for i in range(n)]
        scalar = [F(i-seed, i+1) for i in range(n)]

        def energy(h, k):
            first = sum(n0[i][j]*dot(tuple(a-b for a, b in zip(h[i], h[j])),
                                    tuple(a-b for a, b in zip(k[i], k[j])))
                        for i in range(n) for j in range(n))/2
            second = -sum(r[i][j]*dot(h[i], k[j])
                          for i in range(n) for j in range(n))
            return first+second+sum(curv[i]*dot(h[i], k[i]) for i in range(n))

        bg = [tuple(scalar[i]*a for a in g[i]) for i in range(n)]
        bbg = [tuple(scalar[i]**2*a for a in g[i]) for i in range(n)]
        target = sum((n0[i][j]+r[i][j])*(scalar[i]-scalar[j])**2
                     *dot(g[i], g[j]) for i in range(n) for j in range(n))/2
        assert energy(bg, bg)-energy(g, bbg) == target
        multiplier_checks += 1
        weights = [F(i+1, n+1) for i in range(n)]
        k = [F(i+seed+1, 5) for i in range(n)]
        mean = [sum(weights[i]*k[i]*g[i][a] for i in range(n)) for a in (0, 1)]
        cross = sum(weights[i]*weights[j]*k[i]*k[j]*dot(g[i], g[j])
                    for i in range(n) for j in range(n) if i != j)/2
        diagonal = sum(weights[i]**2*k[i]**2*dot(g[i], g[i]) for i in range(n))
        assert cross == (dot(mean, mean)-diagonal)/2
        assert diagonal > 0
        diagonal_checks += 1
print(f'multiplier subtraction: {multiplier_checks}; atomic diagonal corrections: {diagonal_checks}')

# A genuine infinite-coordinate Fourier embedding; all sampled inputs rational.
r = F(1, 4)
c = r*(1+r)/(1-r)
assert c == F(5, 12)
assert r*(1+r)/(1-r)**3 == F(20, 27)
circle = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(0)),
          (F(3, 5), F(4, 5)), (F(9999, 10001), F(200, 10001))]


def multiply(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def tail_moment(m):
    return r**(m+1)*((m+1)**2/(1-r)+2*(m+1)*r/(1-r)**2
                     +r*(1+r)/(1-r)**3)


tail_checks = 0
for s, t in itertools.combinations(circle, 2):
    chord = distance(s, t)
    d = c*chord/(1-2*r*dot(s, t)+r*r)
    assert r*chord <= d <= F(20, 27)*chord
    sn = tn = (F(1), F(0))
    partial = moment = F(0)
    for n in range(1, 25):
        sn, tn = multiply(sn, s), multiply(tn, t)
        partial += r**n*distance(sn, tn)
        moment += n*n*r**n
        tail = tail_moment(n)
        assert tail == F(20, 27)-moment
        assert 0 <= (d-partial)/d <= 4*tail
        tail_checks += 1
print(f'infinite-coordinate distances and uniform tails: {tail_checks} exact checks')


def fejer(n, k):
    return max(n-abs(k), 0)


def pair_energy(n, ell):
    coeff = r**n/c*((1+r*r)*fejer(n, ell)
                    -r*fejer(n, ell-1)-r*fejer(n, ell+1))
    return coeff/(2 if ell == 0 else 4)


signed_checks = constant_checks = 0
for ell in range(1, 9):
    assert pair_energy(ell, ell) == -r**(ell+1)/(4*c)
    assert all(pair_energy(n, ell) == 0 for n in range(1, ell))
    for m in range(ell, ell+12):
        partial = sum(pair_energy(n, ell) for n in range(1, m+1))
        tail = (1-r)**2/(4*c)*r**(m+1)*((m+1-ell)/(1-r)+r/(1-r)**2)
        assert partial+tail == 0
        assert tail > 0 and partial < 0
        signed_checks += 1
for m in range(25):
    partial = sum(pair_energy(n, 0) for n in range(1, m+1))
    tail = r**(m+1)/(2*c)*((1-r)**2*((m+1)/(1-r)+r/(1-r)**2)
                          +2*r/(1-r))
    assert partial+tail == F(1, 2)
    constant_checks += 1
assert pair_energy(1, 1) == F(-3, 80)
print(f'signed Fourier cancellations: {signed_checks}; nonzero-mean sums: {constant_checks}')
print('stress: first Fourier-pair energy=-3/80, remaining tail=3/80; PSD is required')
print('PASS (algebra and explicit Fourier models; no PDE certification)')
print(f'priority={os.getpriority(os.PRIO_PROCESS, 0)}, '
      f'peak_rss_bytes={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}')
