#!/usr/bin/env python3
"""Exact, standard-library checks for PROOF.md; no simulation or external writes."""
import itertools
import math
import os
import resource
import time
from collections import defaultdict
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
started = time.monotonic()
print('priority:', os.getpriority(os.PRIO_PROCESS, 0))
print('OMP_NUM_THREADS:', os.environ.get('OMP_NUM_THREADS'))


def add(a, b):
    out = defaultdict(Q, a)
    for e, c in b.items():
        out[e] += c
    return {e: c for e, c in out.items() if c}


def scale(a, c):
    return {e: c*v for e, v in a.items() if c*v}


def mul(a, b):
    out = defaultdict(Q)
    for e, c in a.items():
        for f, v in b.items():
            out[tuple(x+y for x, y in zip(e, f))] += c*v
    return {e: c for e, c in out.items() if c}


def power(a, n, nv):
    out = {(0,)*nv: Q(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def derivative(a, j):
    out = {}
    for e, c in a.items():
        if e[j]:
            f = list(e)
            f[j] -= 1
            out[tuple(f)] = c*e[j]
    return out


def gm(p):
    return 0 if p % 2 else math.prod(range(1, p, 2))


def mean(a):
    return sum((c*math.prod(gm(p) for p in e) for e, c in a.items()), Q(0))


def mean_product(a, b):
    # Integrate before building the product polynomial, keeping memory small.
    total = Q(0)
    for e, c in a.items():
        for f, v in b.items():
            g = math.prod(gm(x+y) for x, y in zip(e, f))
            if g:
                total += c*v*g
    return total


def variable(nv, j):
    e = [0]*nv
    e[j] = 1
    return {tuple(e): Q(1)}


def radial(d, p):
    return math.prod((Q(d+2*j, d) for j in range(p)), start=Q(1))


def constants(d, k):
    m = [radial(d, p) for p in range(7)]
    rho = m[3]-2*m[2]+m[1]
    eta = m[6]-4*m[5]+6*m[4]-4*m[3]+m[2]
    delta = m[6]/k + Q(k-1, k)*m[3]**2*(
        Q(1, d)+Q(3, d*(d+2))+Q(15, d*(d+2)*(d+4)))
    beta = Q(9, 4)*(eta/k + Q(k-1, k)*(1+Q(2, d))*rho**2)
    ell = Q(3, 2)*rho
    eps2 = 6*float(delta) + 2*(2*math.sqrt(float(delta))
        + 4/math.sqrt(6)*float(delta*beta)**0.25)**2
    return delta, beta, ell, eps2


def direct_contraction_moment(d, k):
    """Expand the raw tensor in independent W coordinates; no row partitions."""
    nv = d*k
    w = [[variable(nv, i*d+j) for j in range(d)] for i in range(k)]
    raw = {}
    for inds in itertools.product(range(d), repeat=3):
        val = {}
        for row in w:
            val = add(val, mul(mul(row[inds[0]], row[inds[1]]), row[inds[2]]))
        raw[inds] = val
    actual = Q(0)
    for i, j in itertools.product(range(d), repeat=2):
        c = {}
        for p, q in itertools.product(range(d), repeat=2):
            c = add(c, mul(raw[i, p, q], raw[j, p, q]))
        actual += mean_product(c, c)
    actual /= k*k*d**6
    expected = constants(d, k)[0]
    assert actual == expected, (d, k, actual, expected)
    print(f'coordinate contraction moment d={d} k={k}: PASS; delta={actual}')


def wick(tensor, d):
    """Coordinate Hermite expansion, independent of the Wick product formula."""
    out = {}
    for inds, value in tensor.items():
        counts = [inds.count(j) for j in range(d)]
        p = {(0,)*d: Q(value)}
        for j, count in enumerate(counts):
            hp = {}
            for a in range(count//2+1):
                e = [0]*d
                e[j] = count-2*a
                hp[tuple(e)] = Q((-1)**a*math.factorial(count),
                    2**a*math.factorial(a)*math.factorial(count-2*a))
            p = mul(p, hp)
        out = add(out, p)
    return out


def deterministic_network(rows):
    d = len(rows[0])
    x = [variable(d, j) for j in range(d)]
    t = {inds: sum(math.prod(row[j] for j in inds) for row in rows)
         for inds in itertools.product(range(d), repeat=3)}
    b = [3*sum((sum(v*v for v in row)-d)*row[j] for row in rows)
         for j in range(d)]
    f = {}
    for row in rows:
        z = {}
        for j in range(d):
            z = add(z, scale(x[j], row[j]))
        f = add(f, add(power(z, 3, d), scale(z, -3*d)))
    cubic = wick(t, d)
    linear = wick({(j,): b[j] for j in range(d)}, d)
    assert f == add(cubic, linear)
    inverse = add(scale(cubic, Q(1, 3)), linear)
    return f, inverse, t, b


def deterministic_check(rows_a, rows_b):
    d = len(rows_a[0])
    fa, ia, ta, ba = deterministic_network(rows_a)
    fb, ib, tb, bb = deterministic_network(rows_b)
    gamma = {}
    for j in range(d):
        gamma = add(gamma, mul(derivative(ia, j), derivative(fb, j)))
    cov = 6*sum(ta[x]*tb[x] for x in ta)+sum(a*b for a, b in zip(ba, bb))
    assert mean_product(fa, fb) == cov == mean(gamma)
    residual = add(gamma, {(0,)*d: -Q(cov)})
    c1 = {}
    for i, j, l, m in itertools.product(range(d), repeat=4):
        c1[i, j, l, m] = 3*sum(ta[i, j, p]*tb[l, m, p] for p in range(d))
    c2 = {}
    for i, j in itertools.product(range(d), repeat=2):
        c2[i, j] = 12*sum(ta[i, p, q]*tb[j, p, q]
            for p, q in itertools.product(range(d), repeat=2))
        c2[i, j] += sum(ta[i, j, p]*bb[p]+3*tb[i, j, p]*ba[p]
                       for p in range(d))
    assert residual == add(wick(c1, d), wick(c2, d))
    # Mixed polynomial test h(fa,fb)=fa^p*fb^q checks the exact Stein identity.
    for p, q in [(0, 1), (1, 0), (2, 1), (1, 2), (3, 0)]:
        test = mul(power(fa, p, d), power(fb, q, d))
        lhs = mean_product(fa, test)
        rhs = Q(0)
        for j in range(d):
            rhs += mean_product(derivative(ia, j), derivative(test, j))
        assert lhs == rhs, (d, p, q, lhs, rhs)
    print(f'deterministic mixed Stein/Wick identities d={d}: PASS; covariance={cov}')

    def contract(a, b, r):
        order = 3-r
        return {left+right: sum(a[left+common]*b[right+common]
                    for common in itertools.product(range(d), repeat=r))
                for left in itertools.product(range(d), repeat=order)
                for right in itertools.product(range(d), repeat=order)}

    def norm2(a):
        return sum(v*v for v in a.values())

    da = norm2(contract(ta, ta, 2))
    db = norm2(contract(tb, tb, 2))
    assert da == norm2(contract(ta, ta, 1))
    assert db == norm2(contract(tb, tb, 1))
    for r in [1, 2]:
        assert norm2(contract(ta, tb, r))**2 <= da*db
    for t, v, dt in [(ta, bb, da), (tb, ba, db)]:
        linear = {(i, j): sum(t[i, j, p]*v[p] for p in range(d))
                  for i, j in itertools.product(range(d), repeat=2)}
        assert norm2(linear)**2 <= dt*sum(x*x for x in v)**2


def direct_stein_variance(d, k):
    """Integrate the actual Stein residual over W and X, without contractions."""
    nw = d*k
    nv = nw+d
    zero = (0,)*nv
    one = {zero: Q(1)}
    w = [[variable(nv, i*d+j) for j in range(d)] for i in range(k)]
    x = [variable(nv, nw+j) for j in range(d)]
    f, inverse = {}, {}
    for row in w:
        z, radius = {}, {}
        for j in range(d):
            z = add(z, mul(row[j], x[j]))
            radius = add(radius, mul(row[j], row[j]))
        cubic_z = power(z, 3, nv)
        f = add(f, add(cubic_z, scale(z, -3*d)))
        # L^{-1} with a minus sign: I3/3 + I1.
        inverse = add(inverse, add(scale(cubic_z, Q(1, 3)),
            mul(add(scale(radius, 2), scale(one, -3*d)), z)))
    gamma = {}
    for j in range(d):
        gamma = add(gamma, mul(derivative(inverse, nw+j), derivative(f, nw+j)))
    kpoly = defaultdict(Q)
    for e, c in mul(f, f).items():
        kpoly[e[:nw]+(0,)*d] += c*math.prod(gm(p) for p in e[nw:])
    kpoly = {e: c for e, c in kpoly.items() if c}
    residual = add(gamma, scale(kpoly, -1))
    actual = mean_product(residual, residual)/Q((6*k*d**3)**2)
    delta, beta, ell, eps2 = constants(d, k)
    assert float(actual) <= eps2
    # A coarser rational/algebraic check avoids relying only on floating point.
    # epsilon^2 <= 30*delta+10*sqrt(delta*beta), by (a+b+c)^2 <= 3 sum squares.
    gap = actual-30*delta
    assert gap <= 0 or gap*gap <= 100*delta*beta
    print(f'direct averaged Stein variance d={d} k={k}: PASS; exact={actual}; '
          f'epsilon^2={eps2:.6f}')


for dims in [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 2)]:
    direct_contraction_moment(*dims)

deterministic_check([[2], [-1]], [[1], [3]])
deterministic_check([[1, 0], [1, 2]], [[-1, 2], [2, 0]])
deterministic_check([[1, 2, -1], [0, 1, 2]], [[2, -1, 0], [1, 1, 1]])
# Identical, opposite, permuted, and zero-row cases catch degenerate covariances.
deterministic_check([[1, 0], [1, 2]], [[1, 0], [1, 2]])
deterministic_check([[1, 0], [1, 2]], [[-1, 0], [-1, -2]])
deterministic_check([[1, 0], [1, 2]], [[1, 2], [1, 0]])
deterministic_check([[0, 0], [0, 0]], [[1, 1], [2, -1]])

for dims in [(1, 1), (1, 2), (2, 1), (2, 2)]:
    direct_stein_variance(*dims)

print('rates: gamma, d, d*delta, d^2*beta, sqrt(d)*epsilon, limiting sqrt(d)*epsilon')
for ratio in [Q(1, 2), Q(1), Q(2)]:
    for d in [64, 1024, 16384, 262144]:
        k = int(d*ratio)
        delta, beta, ell, eps2 = constants(d, k)
        print(ratio, d, f'{float(d*delta):.9f}', f'{float(d*d*beta):.9f}',
              f'{math.sqrt(d*eps2):.9f}', f'{math.sqrt(14*(1+1/float(ratio))):.9f}')

print('elapsed seconds:', round(time.monotonic()-started, 3))
print('peak RSS bytes:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('ALL CHECKS PASSED')
