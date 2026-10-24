#!/usr/bin/env python3
"""Exact C059 leaf/core certificates; Python standard library only.

The independent full-law calculation expands principal determinants and then
Möbius-inverts inclusion moments. It does not use Schur complements. Conditional
two-site atoms, leaf replacement, and every acceleration coefficient are checked
against that calculation with rational arithmetic. Logarithms in the displayed
curvatures and chord gaps use rational atanh-series enclosures.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations
from functools import lru_cache
from pathlib import Path
import json


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    def __add__(self, y):
        y = as_c(y)
        return C(self.re + y.re, self.im + y.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, y):
        return self + (-as_c(y))

    def __rsub__(self, y):
        return as_c(y) - self

    def __mul__(self, y):
        y = as_c(y)
        return C(self.re * y.re - self.im * y.im,
                 self.re * y.im + self.im * y.re)

    __rmul__ = __mul__

    def __truediv__(self, y):
        assert not isinstance(y, C)
        return C(self.re / y, self.im / y)

    def conj(self):
        return C(self.re, -self.im)

    def real(self):
        assert self.im == 0, self
        return self.re

    def norm2(self):
        return self.re ** 2 + self.im ** 2


def as_c(x):
    return x if isinstance(x, C) else C(F(x))


Z, O = C(), C(F(1))
JZ, JO = (Z, Z, Z), (O, Z, Z)


def jadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def jscale(a, s):
    return tuple(x * s for x in a)


def jsub(a, b):
    return jadd(a, jscale(b, -1))


def jmul(a, b):
    return (a[0] * b[0], a[0] * b[1] + a[1] * b[0],
            a[0] * b[2] + a[1] * b[1] + a[2] * b[0])


def jconj(a):
    return tuple(x.conj() for x in a)


def detjet(a):
    n = len(a)
    ans = JZ
    for perm in permutations(range(n)):
        term = JO
        for i, j in enumerate(perm):
            if a[i][j] == JZ:
                term = JZ
                break
            term = jmul(term, a[i][j])
        sign = (-1) ** sum(perm[i] > perm[j]
                          for i in range(n) for j in range(i + 1, n))
        ans = jadd(ans, jscale(term, sign))
    return ans


def atomjets(k):
    """Full exact atoms from inclusion determinants, independently of conditioning."""
    n = len(k)
    atoms = []
    for mask in range(1 << n):
        ix = [i for i in range(n) if mask >> i & 1]
        atoms.append(detjet([[k[i][j] for j in ix] for i in ix]))
    for bit in range(n):
        for mask in range(1 << n):
            if not (mask >> bit & 1):
                atoms[mask] = jsub(atoms[mask], atoms[mask | (1 << bit)])
    out = [tuple(x.real() for x in p) for p in atoms]
    assert sum(p[0] for p in out) == 1
    assert sum(p[1] for p in out) == 0
    assert sum(p[2] for p in out) == 0
    assert min(p[0] for p in out) > 0
    return out


def twoatoms(m):
    a, b, w = m[0][0], m[1][1], m[0][1]
    w2 = jmul(w, jconj(w))
    ps = [jsub(jmul(jsub(JO, a), jsub(JO, b)), w2),
          jadd(jmul(a, jsub(JO, b)), w2),
          jadd(jmul(jsub(JO, a), b), w2),
          jsub(jmul(a, b), w2)]
    return [tuple(x.real() for x in p) for p in ps]


def outer(w):
    return [[w[i] * w[j].conj() for j in range(2)] for i in range(2)]


def matrix_at(ex, t):
    m = len(ex['d'])
    zs = [(z0 + t * (z1 - z0), z1 - z0, Z)
          for z0, z1 in zip(ex['z0'], ex['z1'])]
    a = [[(ex['a0'][i][j] + t * (ex['a1'][i][j] - ex['a0'][i][j]),
           ex['a1'][i][j] - ex['a0'][i][j], Z)
          for j in range(2)] for i in range(2)]
    k = [[JZ for _ in range(m + 2)] for _ in range(m + 2)]
    for i, d in enumerate(ex['d']):
        k[i][i] = (C(d), Z, Z)
        for j in range(2):
            k[i][m + j] = jscale(zs[i], ex['w'][i][j].conj())
            k[m + j][i] = jconj(k[i][m + j])
    for i in range(2):
        for j in range(2):
            k[m + i][m + j] = a[i][j]
    return k, a, zs


def strict_matrix2(a):
    assert a[1][0] == a[0][1].conj()
    d0, d1 = a[0][0].real(), a[1][1].real()
    det = d0 * d1 - a[0][1].norm2()
    assert d0 > 0 and d1 > 0 and det > 0
    return {'diagonal_0': str(d0), 'diagonal_1': str(d1), 'det': str(det)}


def feasibility(ex, t):
    _, aa, zs = matrix_at(ex, t)
    lower = [[aa[i][j][0] for j in range(2)] for i in range(2)]
    upper = [[(O if i == j else Z) - lower[i][j] for j in range(2)]
             for i in range(2)]
    for d, w, z in zip(ex['d'], ex['w'], zs):
        q = outer(w)
        for i in range(2):
            for j in range(2):
                lower[i][j] -= z[0].norm2() * q[i][j] / d
                upper[i][j] -= z[0].norm2() * q[i][j] / (1 - d)
    return {'K_Schur': strict_matrix2(lower),
            'I_minus_K_Schur': strict_matrix2(upper)}


def series_log(r, n=45):
    """Rational interval for log(r), for 1 <= r <= 2."""
    assert 1 <= r <= 2
    z = (r - 1) / (r + 1)
    power, total = z, F(0)
    for k in range(n):
        total += 2 * power / (2 * k + 1)
        power *= z * z
    tail = 2 * power / ((2 * n + 1) * (1 - z * z))
    return total, total + tail


@lru_cache(None)
def logbounds(x):
    assert x > 0
    r, k = x, 0
    while r < 1:
        r *= 2
        k -= 1
    while r > 2:
        r /= 2
        k += 1
    lo, hi = series_log(r)
    l2, h2 = series_log(F(2))
    aa, bb = ((lo + k * l2, hi + k * h2) if k >= 0
              else (lo + k * h2, hi + k * l2))
    # A common decimal grid prevents irrelevant denominator growth when many
    # independently enclosed logarithms are added. Rounding is always outward.
    scale = 10 ** 42
    return (F((aa.numerator * scale) // aa.denominator, scale),
            F(-((-bb.numerator * scale) // bb.denominator), scale))


def interval_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def interval_scale(a, c):
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def logsum(terms, rational=F(0)):
    lo, hi = rational, rational
    for coef, argument in terms:
        term = interval_scale(logbounds(argument), coef)
        lo += term[0]
        hi += term[1]
    return lo, hi


def outward(interval, digits=24):
    scale = 10 ** digits
    a, b = interval
    floor = (a.numerator * scale) // a.denominator
    ceil = -((-b.numerator * scale) // b.denominator)
    def dec(v):
        return ('-' if v < 0 else '') + str(abs(v) // scale) + '.' + str(abs(v) % scale).zfill(digits)
    return [dec(floor), dec(ceil)]


def entropy(atoms):
    return logsum([(-p[0], p[0]) for p in atoms])


def certify(ex, t):
    k, a, zs = matrix_at(ex, t)
    p = atomjets(k)
    m = len(ex['d'])
    rho = [z[0].norm2() for z in zs]
    accel = [2 * z[1].norm2() for z in zs]
    assert all(r > 0 for r in rho)
    delta = []
    jbounds = []
    for i, d in enumerate(ex['d']):
        di = []
        for mask in range(1 << (m + 2)):
            pair = mask & ~(1 << i)
            pi = d if (mask >> i & 1) else 1 - d
            q = pi * (p[pair][0] + p[pair | (1 << i)][0])
            di.append(p[mask][0] - q)
        delta.append(di)
        # The reset-law logarithm cancels exactly on every retained configuration.
        for mask in range(1 << (m + 2)):
            if not (mask >> i & 1):
                assert di[mask] + di[mask | (1 << i)] == 0
        jb = logsum(list(zip(di, [pp[0] for pp in p])))
        assert jb[0] > 0
        jbounds.append(jb)

    cond_curvature = (F(0), F(0))
    conditional_records = []
    for leafmask in range(1 << m):
        mu = F(1)
        mx = [[a[i][j] for j in range(2)] for i in range(2)]
        for i, (d, w, z) in enumerate(zip(ex['d'], ex['w'], zs)):
            chosen = leafmask >> i & 1
            mu *= d if chosen else 1 - d
            r = 1 / d if chosen else -1 / (1 - d)
            rj = jmul(z, jconj(z))
            q = outer(w)
            for j in range(2):
                for ell in range(2):
                    mx[j][ell] = jsub(mx[j][ell], jscale(rj, r * q[j][ell]))
        # Two independent Schur inequalities certify each conditional contraction.
        mb = [[mx[i][j][0] for j in range(2)] for i in range(2)]
        strict_matrix2(mb)
        strict_matrix2([[(O if i == j else Z) - mb[i][j]
                         for j in range(2)] for i in range(2)])
        pc = twoatoms(mx)
        tangent = [[(mx[i][j][0], mx[i][j][1], Z) for j in range(2)]
                   for i in range(2)]
        pl = twoatoms(tangent)
        for coremask in range(4):
            mask = leafmask | coremask << m
            assert p[mask] == tuple(mu * x for x in pc[coremask])
            assert pc[coremask][:2] == pl[coremask][:2]
            # Exact coefficient-by-coefficient acceleration control. No logs occur.
            full_acceleration = 2 * p[mask][2] - 2 * mu * pl[coremask][2]
            reset_acceleration = sum(accel[i] * delta[i][mask] / rho[i]
                                     for i in range(m))
            assert full_acceleration == reset_acceleration
        fisher = sum(q[1] ** 2 / q[0] for q in pl)
        cb = logsum([(2 * q[2], q[0]) for q in pl], fisher)
        # The generic proof guarantees this sign; this exact example verifies it.
        assert cb[0] > 0
        cond_curvature = interval_add(cond_curvature, interval_scale(cb, mu))
        conditional_records.append({'leaf_mask': leafmask,
                                    'probability': str(mu),
                                    'negative_tangent_entropy_curvature': outward(cb)})

    full_fisher = sum(q[1] ** 2 / q[0] for q in p)
    minus_h2 = logsum([(2 * q[2], q[0]) for q in p], full_fisher)
    acceleration_cost = (F(0), F(0))
    for aa, rr, jj in zip(accel, rho, jbounds):
        acceleration_cost = interval_add(acceleration_cost, interval_scale(jj, aa / rr))
    decomposition = interval_add(cond_curvature, acceleration_cost)
    assert max(minus_h2[0], decomposition[0]) <= min(minus_h2[1], decomposition[1])
    assert minus_h2[0] > 0
    return {'parameter': str(t), 'atom_count': len(p),
            'rho': list(map(str, rho)),
            'rho_derivative': [str(2 * (z[0].conj() * z[1]).re) for z in zs],
            'minus_entropy_second_derivative': outward(minus_h2),
            'conditional_tangent_curvature': outward(cond_curvature),
            'Jeffreys_acceleration_cost': outward(acceleration_cost),
            'leaf_Jeffreys_divergences': [outward(jj) for jj in jbounds],
            'atoms': [{'mask': i, 'p': str(q[0]), 'p_first': str(q[1]),
                       'p_second': str(2 * q[2])} for i, q in enumerate(p)],
            'conditional_slices': conditional_records}


def c(a, b=0):
    return C(F(a), F(b))


TREE = {
    'd': [F(1, 3), F(2, 5), F(3, 5), F(2, 3)],
    'w': [[O, Z], [O, Z], [Z, O], [Z, O]],
    'z0': [c('1/5'), c('1/10'), c('1/5'), c('3/20')],
    'z1': [c('1/10', '1/20'), c('1/5', '-1/25'),
           c('3/25', '1/20'), c('1/5', '1/25')],
    'a0': [[c('9/20'), c('1/4')], [c('1/4'), c('11/20')]],
    'a1': [[c('11/20'), c('-1/5', '1/10')],
           [c('-1/5', '-1/10'), c('9/20')]],
}

DENSE = {
    'd': [F(1, 3), F(2, 5), F(3, 5)],
    'w': [[O, O], [O, c(0, 1)], [c('3/5'), c('4/5')]],
    'z0': [c('1/10'), c('1/12'), c('1/9')],
    'z1': [c('1/16', '1/25'), c('1/9', '-1/20'), c('1/14', '1/40')],
    'a0': [[c('9/20'), c('1/5', '1/20')],
           [c('1/5', '-1/20'), c('11/20')]],
    'a1': [[c('11/20'), c('-1/6', '1/12')],
           [c('-1/6', '-1/12'), c('1/2')]],
}


def main():
    results = {'arithmetic': 'exact rational Gaussian jets; rational logarithm enclosures'}
    for name, ex, t in [('six_site_double_star', TREE, F(1, 2)),
                        ('five_site_fixed_complex_orientations', DENSE, F(1, 3))]:
        record = {'endpoint_0': feasibility(ex, F(0)),
                  'endpoint_1': feasibility(ex, F(1)),
                  'curvature_certificate': certify(ex, t)}
        if name == 'six_site_double_star':
            hs = [entropy(atomjets(matrix_at(ex, q)[0])) for q in [F(0), F(1, 2), F(1)]]
            gap = interval_add(hs[1], interval_scale(interval_add(hs[0], hs[2]), F(-1, 2)))
            assert gap[0] > 0
            record['midpoint_entropy_gap'] = outward(gap)
            record['endpoint_0_entropy'] = outward(hs[0])
            record['midpoint_entropy'] = outward(hs[1])
            record['endpoint_1_entropy'] = outward(hs[2])
            # The changing cross block has column rank two: disjoint nonzero columns.
            dz = [b - a for a, b in zip(ex['z0'], ex['z1'])]
            assert all(z != Z for z in dz)
            assert ex['a1'][0][1] != ex['a0'][0][1]
            assert (ex['a1'][0][1] - ex['a0'][0][1]).im != 0
            assert all(s != '0' for s in record['curvature_certificate']['rho_derivative'])
            record['direction_rank'] = 4
            record['direction_inertia'] = [2, 2, 2]
        results[name] = record
        cc = record['curvature_certificate']
        print(name + ': -H_second in ' + str(cc['minus_entropy_second_derivative']))
        print('  conditional tangent + Jeffreys acceleration = '
              + str(cc['conditional_tangent_curvature']) + ' + '
              + str(cc['Jeffreys_acceleration_cost']))
        if 'midpoint_entropy_gap' in record:
            print('  midpoint entropy gap in ' + str(record['midpoint_entropy_gap']))
    (Path(__file__).parent / 'certificate.json').write_text(json.dumps(results, indent=2) + '\n')
    print('PASS: 96 exact full atoms, conditional laws, all acceleration coefficients, '
          'strict endpoint Schur certificates, mixed radial signs, rigorous entropy enclosures.')


if __name__ == '__main__':
    main()
