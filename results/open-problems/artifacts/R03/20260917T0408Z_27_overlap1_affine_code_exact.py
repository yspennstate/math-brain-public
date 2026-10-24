from fractions import Fraction
from math import comb
from itertools import product
from collections import Counter


def classes(r):
    if r % 2 == 0:
        a = r // 2
        return [('even', comb(r - 1, a - 1), a - 1, a)]
    a = (r - 1) // 2
    return [
        ('minority', comb(r - 1, a - 1), a - 1, a + 1),
        ('majority', comb(r - 1, a), a, a),
    ]


def projective_vectors(p, d):
    # One representative of each projective nonzero linear functional:
    # first nonzero coefficient normalized to 1.
    for first in range(d):
        for tail in product(range(p), repeat=d - first - 1):
            yield (0,) * first + (1,) + tail


def parameter_slice(r, cls_name, p, z):
    """Boolean residual assignments after fixing the overlap bit z.

    A balanced relation is oriented so the overlap coefficient is +1.
    One residual coordinate is eliminated, leaving r-2 linear parameters.
    """
    row = [c for c in classes(r) if c[0] == cls_name][0]
    plus, minus = row[2], row[3]
    coeff = [1] * plus + [-1] * minus
    last = coeff[-1] % p
    inv = pow(last, -1, p)
    others = coeff[:-1]
    pts = []
    for bits in product((0, 1), repeat=len(others)):
        rhs = (-z - sum(c * b for c, b in zip(others, bits))) % p
        xlast = (rhs * inv) % p
        if xlast in (0, 1):
            pts.append(tuple(bits))
    return pts


def max_projective_fiber(pts, p):
    """Largest affine fiber of a nonzero linear functional on pts."""
    d = len(pts[0]) if pts else 0
    if d == 0:
        return len(pts)
    best = 0
    for a in projective_vectors(p, d):
        cnt = Counter(sum(ai * xi for ai, xi in zip(a, x)) % p for x in pts)
        best = max(best, max(cnt.values()))
    return best


def local_stats(r, cls_name, p):
    out = {}
    for z in (0, 1):
        pts = parameter_slice(r, cls_name, p, z)
        out[z] = (len(pts), max_projective_fiber(pts, p))
    return out


def class_rows(m, p):
    rows = []
    Ntot = 0
    Etot = 0
    for s in (3, 4):
        for t in range(5, m + 1):
            if not (s < t and s + t - 1 <= m):
                continue
            b = m - (s + t - 1)
            support_configs = comb(m, s) * s * comb(m - s, t - 1)
            for cs in classes(s):
                ss = local_stats(s, cs[0], p)
                for ct in classes(t):
                    tt = local_stats(t, ct[0], p)
                    A0, qA0 = ss[0]
                    A1, qA1 = ss[1]
                    B0, qB0 = tt[0]
                    B1, qB1 = tt[1]

                    # The overlap-one Boolean slice is a two-fiber union over z=0,1.
                    h = (A0 * B0 + A1 * B1) * (2 ** b)

                    # Hyperplane cap: condition on every block except one on which
                    # the functional is genuinely nonzero. If only z survives,
                    # one z-fiber is selected. If a free Boolean bit survives,
                    # at most half of the free cube is selected.
                    Qs = (qA0 * B0 + qA1 * B1) * (2 ** b)
                    Qt = (qB0 * A0 + qB1 * A1) * (2 ** b)
                    candidates = [Qs, Qt, max(A0 * B0, A1 * B1) * (2 ** b)]
                    if b > 0:
                        assert h % 2 == 0
                        candidates.append(h // 2)
                    Q = max(candidates)

                    # dim(V^perp)=m-2.  A j-dimensional span contains at most 2^j
                    # Boolean points, and every proper span lies in a hyperplane.
                    factors = [h - min(2 ** j, Q) for j in range(m - 2)]
                    assert min(factors) > 0
                    Basis = 1
                    for f in factors:
                        Basis *= f

                    N = support_configs * cs[1] * ct[1]
                    E = N * Basis * (h - m + 1) * (h - m)
                    rows.append(
                        {
                            's': s,
                            't': t,
                            'cs': cs[0],
                            'ct': ct[0],
                            'b': b,
                            'h': h,
                            'Q': Q,
                            'N': N,
                            'Basis': Basis,
                            'E': E,
                            'factors': factors,
                            'A': ss,
                            'B': tt,
                        }
                    )
                    Ntot += N
                    Etot += E
    return rows, Ntot, Etot


def correction(m, p, D, E):
    c = Fraction(p * (p * p - 1), p ** D - 1)
    slack = Fraction(p, 1) - c
    delta = Fraction(2 ** (m + 1), 2 ** (m * m)) * slack * E
    return delta, c, slack


def show(m, p, D, baseline, expected_planes):
    rows, N, E = class_rows(m, p)
    assert N == expected_planes
    delta, c, slack = correction(m, p, D, E)
    new = baseline - delta
    print(f'CASE m={m} p={p} D={D}')
    print('plane_count', N)
    print('exact_corank2_certified', E)
    print('c', c)
    print('slack', slack)
    for r in rows:
        print(
            'ROW', r['s'], r['t'], r['cs'], r['ct'],
            'b', r['b'], 'h', r['h'], 'Q', r['Q'], 'N', r['N'],
            'Basis', r['Basis'], 'E', r['E'],
            'factors', ','.join(map(str, r['factors'])),
            'A0q', r['A'][0], 'A1q', r['A'][1],
            'B0q', r['B'][0], 'B1q', r['B'][1],
        )
    print('delta', delta)
    print('delta_decimal', float(delta))
    print('baseline', baseline)
    print('new', new)
    print('new_decimal', float(new))
    print()


# Retained run26 replay-certified baselines.
r10 = Fraction(1271019142666434244923, 4611686018427387904)
r11 = Fraction(4087618837251051672826796387925, 7787900129957441143457185792)

show(9, 7, 4, r10, 275940)
show(10, 11, 5, r11, 1524600)

# Independent sanity check: the two overlap-bit fibers partition the balanced
# Boolean solutions on each local support.
for p in (7, 11):
    for r in range(3, 9):
        for cls in classes(r):
            st = local_stats(r, cls[0], p)
            target = comb(r, r // 2 if r % 2 == 0 else (r - 1) // 2)
            assert st[0][0] + st[1][0] == target

print('SELF-CHECK PASS')
