#!/usr/bin/env python3
"""Exact checks for the cubic self-covariance lemma; standard library only."""
import math
import os
import resource
from collections import defaultdict
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
print('priority:', os.getpriority(os.PRIO_PROCESS, 0))
print('thread env:', os.environ.get('OMP_NUM_THREADS'))


def add(a, b):
    out = defaultdict(Q, a)
    for e, c in b.items():
        out[e] += c
    return {e: c for e, c in out.items() if c}


def scale(a, s):
    return {e: c * s for e, c in a.items() if c * s}


def mul(a, b):
    out = defaultdict(Q)
    for e, c in a.items():
        for f, h in b.items():
            out[tuple(x + y for x, y in zip(e, f))] += c * h
    return {e: c for e, c in out.items() if c}


def power(a, n, nv):
    out = {(0,) * nv: Q(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def gm(p):
    return 0 if p % 2 else math.prod(range(1, p, 2))


def gaussian_mean(a):
    return sum((c * math.prod(gm(p) for p in e) for e, c in a.items()), Q(0))


def radial(d, p):
    return math.prod((Q(d + 2*j, d) for j in range(p)), start=Q(1))


def formulas(d, k):
    m = [radial(d, p) for p in range(7)]
    b = m[3] - 2*m[2] + m[1]
    h = m[6] - 4*m[5] + 6*m[4] - 4*m[3] + m[2]
    a = (m[3]-1)**2 + (m[6]-m[3]**2)/k + Q(30*(k-1), k*d**3)*m[3]
    eb = Q(3, 2)*b
    eb2 = Q(9, 4)*(h/k + Q(k-1, k)*(1+Q(2, d))*b*b)
    return m[3], a, eb, eb2


def exact_v_mse(d, k):
    m = [radial(d, p) for p in range(7)]
    ec, a, eb, eb2 = formulas(d, k)
    b = m[3] - 2*m[2] + m[1]
    # Diagonal and identical-edge contributions to Cov(C,B).
    cov = Q(3, 2*k)*(m[6]-2*m[5]+m[4]-m[3]*b)
    cov += Q(9*(k-1), k*d*(d+2))*(m[3]-m[2])**2
    return a+eb2+2*((ec-1)*eb+cov)


def check_small(d, k):
    # Build the network polynomial directly in independent W and X coordinates.
    # Its numerator is sum_i [(w_i.X)^3 - 3*d*(w_i.X)].
    nv = k*d + d
    zero = (0,)*nv
    one = {zero: Q(1)}
    w, x = [], []
    for i in range(k):
        row = []
        for j in range(d):
            e = list(zero)
            e[i*d+j] = 1
            row.append({tuple(e): Q(1)})
        w.append(row)
    for j in range(d):
        e = list(zero)
        e[k*d+j] = 1
        x.append({tuple(e): Q(1)})

    def dot(a, b):
        out = {}
        for u, v in zip(a, b):
            out = add(out, mul(u, v))
        return out

    num = {}
    for row in w:
        z = dot(row, x)
        num = add(num, add(power(z, 3, nv), scale(z, -3*d)))
    vx = defaultdict(Q)
    for e, c in mul(num, num).items():
        ex = e[k*d:]
        ew = e[:k*d] + (0,)*d
        vx[ew] += c*math.prod(gm(p) for p in ex)*Q(1, 6*k*d**3)
    vx = {e: c for e, c in vx.items() if c}

    cpoly, bpoly = {}, {}
    for i in range(k):
        ri = add(dot(w[i], w[i]), scale(one, -d))
        for j in range(k):
            rj = add(dot(w[j], w[j]), scale(one, -d))
            dij = dot(w[i], w[j])
            cpoly = add(cpoly, scale(power(dij, 3, nv), Q(1, k*d**3)))
            bpoly = add(bpoly, scale(mul(mul(ri, rj), dij), Q(3, 2*k*d**3)))
    assert vx == add(cpoly, bpoly), (d, k, 'conditional covariance')
    ec, a, eb, eb2 = formulas(d, k)
    cm1 = add(cpoly, scale(one, -1))
    assert gaussian_mean(cpoly) == ec
    assert gaussian_mean(mul(cm1, cm1)) == a
    assert gaussian_mean(bpoly) == eb
    assert gaussian_mean(mul(bpoly, bpoly)) == eb2
    ev = gaussian_mean(vx)
    assert ev == 1 + Q(9, d) + Q(20, d*d)
    vm1 = add(vx, scale(one, -1))
    actual = gaussian_mean(mul(vm1, vm1))
    # Algebraic Cauchy-Schwarz avoids any floating-point comparison.
    cross = gaussian_mean(mul(cm1, bpoly))
    assert cross*cross <= a*eb2
    assert actual == a + eb2 + 2*cross
    assert actual == exact_v_mse(d, k)
    print(f'exact Wick check d={d} k={k}: PASS; E[V]={ev}; E[(V-1)^2]={actual}')


# Expand moments symbolically in t=1/d independently of numeric substitutions.
mom = [{(0,): Q(1)}]
for p in range(1, 7):
    mom.append(mul(mom[-1], {(0,): Q(1), (1,): Q(2*(p-1))}))
var = add(mom[6], scale(mul(mom[3], mom[3]), -1))
hpoly = add(add(add(add(mom[6], scale(mom[5], -4)), scale(mom[4], 6)), scale(mom[3], -4)), mom[2])
print('M6-M3^2 coefficients in t=1/d:', sorted(var.items()))
print('h coefficients in t=1/d:', sorted(hpoly.items()))
assert var == {(1,): Q(18), (2,): Q(288), (3,): Q(1704), (4,): Q(4320), (5,): Q(3840)}
assert hpoly == {(2,): Q(12), (3,): Q(488), (4,): Q(2848), (5,): Q(3840)}

for dims in [(1, 1), (1, 3), (2, 1), (2, 2), (3, 2)]:
    check_small(*dims)

print('rate checks k=d; columns: d, d^2*A, d^2*D, d^2*upper bound, d^2*true MSE')
for d in [16, 64, 256, 1024, 4096, 16384]:
    _, a, _, b2 = formulas(d, d)
    bound = (math.sqrt(float(a)) + math.sqrt(float(b2)))**2
    print(d, f'{d*d*float(a):.9f}', f'{d*d*float(b2):.9f}', f'{d*d*bound:.9f}', f'{d*d*float(exact_v_mse(d,d)):.9f}')
print('limits:', 54, 9, f'{(math.sqrt(54)+3)**2:.9f}', 99)
for gamma in [Q(1, 2), Q(2)]:
    d = 16384
    k = int(gamma*d)
    _, a, _, _ = formulas(d, k)
    print('other ratio:', gamma, 'd=', d,
          'd^2*A=', f'{d*d*float(a):.9f}', 'limit=', float(36+18/gamma),
          'd^2*true MSE=', f'{d*d*float(exact_v_mse(d,k)):.9f}',
          'limit=', float(81+18/gamma))
print('peak RSS bytes:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('ALL CHECKS PASSED')
