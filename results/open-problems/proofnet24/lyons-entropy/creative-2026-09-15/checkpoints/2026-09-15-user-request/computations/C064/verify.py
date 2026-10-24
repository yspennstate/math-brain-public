#!/usr/bin/env python3
"""Exact rational checks for C064; the report contains the all-parameter proof.

No third-party modules. Gaussian rationals are pairs of Fraction objects.
Natural logarithms are enclosed by a positive atanh series and outward
rounding to a fixed rational grid. No floating-point value is a certificate.
"""
from collections import defaultdict, deque
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def ga(x):
    return x if isinstance(x, tuple) else (F(x), F(0))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def conj(x):
    return (x[0], -x[1])


def abs2(x):
    return x[0]*x[0]+x[1]*x[1]


def div(x, y):
    z = mul(x, conj(y))
    a = abs2(y)
    return (z[0]/a, z[1]/a)


def mm(A, B):
    return [[sum_ga(mul(A[i][k], B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def sum_ga(xs):
    s = ZERO
    for x in xs:
        s = add(s, x)
    return s


def adj(A):
    return [[conj(A[j][i]) for j in range(len(A))]
            for i in range(len(A[0]))]


def det(A):
    A = [row[:] for row in A]
    z = ONE
    for k in range(len(A)):
        pivot = next((i for i in range(k, len(A)) if A[i][k] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            z = neg(z)
        a = A[k][k]
        z = mul(z, a)
        for i in range(k+1, len(A)):
            ratio = div(A[i][k], a)
            for j in range(k+1, len(A)):
                A[i][j] = sub(A[i][j], mul(ratio, A[k][j]))
            A[i][k] = ZERO
    return z


def reflection(xs):
    xs = [ga(x) for x in xs]
    norm = sum(abs2(x) for x in xs)
    n = len(xs)
    return [[sub(ONE if i == j else ZERO,
                 mul(ga(2/norm), mul(xs[i], conj(xs[j]))))
             for j in range(n)] for i in range(n)]


def projection_law(Q, cols):
    law = {}
    for S in combinations(range(len(Q)), len(cols)):
        p = abs2(det([[Q[i][j] for j in cols] for i in S]))
        if p:
            law[S] = p
    assert sum(law.values()) == 1
    return law


def inclusion_flow(left, right):
    """Ordinary inclusion max flow: pairs inside triples, with exact capacities."""
    source, sink = ('s',), ('t',)
    capacity = defaultdict(F)
    graph = defaultdict(list)

    def edge(u, v, c):
        graph[u].append(v)
        graph[v].append(u)
        capacity[u, v] = c

    for B, p in left.items():
        edge(source, ('l', B), p)
    for T, p in right.items():
        edge(('r', T), sink, p)
    for B in left:
        for T in right:
            if set(B) < set(T):
                edge(('l', B), ('r', T), F(2))
    initial = dict(capacity)
    total = F(0)
    while True:
        parent = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            u = queue.popleft()
            for v in graph[u]:
                if v not in parent and capacity[u, v] > 0:
                    parent[v] = u
                    queue.append(v)
        if sink not in parent:
            break
        v, amount = sink, F(2)
        while parent[v] is not None:
            u = parent[v]
            amount = min(amount, capacity[u, v])
            v = u
        v = sink
        while parent[v] is not None:
            u = parent[v]
            capacity[u, v] -= amount
            capacity[v, u] += amount
            v = u
        total += amount
    assert total == 1
    flow = {}
    for B in left:
        for T in right:
            e = (('l', B), ('r', T))
            value = initial.get(e, F(0))-capacity[e]
            if value > 0:
                flow[B, T] = value
    for B, p in left.items():
        assert sum(t for (C, T), t in flow.items() if B == C) == p
    for T, p in right.items():
        assert sum(t for (B, U), t in flow.items() if T == U) == p
    return flow


SCALE = 10**35


def atanh_log_interval(x, terms=45):
    assert F(1) <= x <= F(2)
    t = (x-1)/(x+1)
    partial = F(0)
    power = t
    for k in range(terms):
        partial += 2*power/(2*k+1)
        power *= t*t
    tail = 2*power/((2*terms+1)*(1-t*t))
    return partial, partial+tail


@lru_cache(maxsize=None)
def log_interval(x):
    assert x > 0
    y, exponent = x, 0
    while y < 1:
        y *= 2
        exponent -= 1
    while y >= 2:
        y /= 2
        exponent += 1
    low, high = atanh_log_interval(y)
    l2, h2 = atanh_log_interval(F(2))
    if exponent >= 0:
        low, high = low+exponent*l2, high+exponent*h2
    else:
        low, high = low+exponent*h2, high+exponent*l2
    low = F((low*SCALE).numerator // (low*SCALE).denominator, SCALE)
    high = F(-((-high*SCALE).numerator // (-high*SCALE).denominator), SCALE)
    return low, high


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def times(c, a):
    return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])


def constant(c):
    return F(c), F(c)


def linear(items):
    result = constant(0)
    for c, a in items:
        result = plus(result, times(F(c), a))
    return result


def entropy(law):
    return linear((-p, log_interval(p)) for p in law.values() if p)


def check_zero(interval):
    assert interval[0] <= 0 <= interval[1]
    assert interval[1]-interval[0] < F(1, 10**28)


def interval_json(interval):
    return {'lower': str(interval[0]), 'upper': str(interval[1]),
            'display_midpoint': float((interval[0]+interval[1])/2)}


def check_counts():
    # Square odds ensure sqrt(v*w) is exactly rational for every pair.
    pars = [(F(1, 5), F(2, 5)), (F(1, 2), F(1, 2)),
            (F(4, 5), F(2, 5)), (F(9, 25), F(12, 25))]
    slopes = [(F(1), F(1)), (F(2), F(3)), (F(-2), F(-1))]
    records = []
    l2 = log_interval(F(2))
    cstar = linear([(1, constant(4)), (-2, l2)])
    for p, sqrtv in pars:
        for q, sqrtw in pars:
            a, b, c = (1-p)*(1-q), p+q-2*p*q, p*q
            v, w, d = p*(1-p), q*(1-q), p-q
            z = b/(sqrtv*sqrtw)
            assert z >= 2 and b <= z/(z+2)
            assert a*c == v*w == (sqrtv*sqrtw)**2
            A, B, C = (v+d*d)/(v*b), (w+d*d)/(w*b), 1/b
            assert A == (1-q)**2/a+(1-2*q)**2/b+q*q/c
            assert B == (1-p)**2/a+(1-2*p)**2/b+p*p/c
            assert C == 2+(1-2*p)*(1-2*q)/b
            for alpha, eta in slopes:
                X, Y = alpha*(1-q)+eta*(1-p), alpha*q+eta*p
                info = X*X/a+(X-Y)**2/b+Y*Y/c
                assert info == A*alpha**2+2*C*alpha*eta+B*eta**2
                assert info >= 2*alpha*eta*(z+2)
                curvature = linear([(-1, constant(info)),
                                    (4*alpha*eta, log_interval(z))])
                gap = linear([(-1, curvature), (-2*alpha*eta, cstar)])
                if p == q == F(1, 2) and alpha == eta:
                    check_zero(gap)
                else:
                    assert gap[0] > 0
                records.append({'p': str(p), 'q': str(q),
                                'slopes': [str(alpha), str(eta)],
                                'count_curvature': interval_json(curvature),
                                'sharp_bound_slack': interval_json(gap)})
    return records


def check_flag():
    h = [1, 2, 3, 1, 2, 1]
    k = [1, (F(0), F(1)), 2, (F(0), F(-1)),
         (F(1), F(1)), (F(0), F(2))]
    Q = mm(reflection(k), reflection(h))
    identity = mm(adj(Q), Q)
    assert all(identity[i][j] == (ONE if i == j else ZERO)
               for i in range(6) for j in range(6))
    m0 = projection_law(Q, [0])
    m1 = projection_law(Q, [0, 1])
    m2 = projection_law(Q, [0, 2])
    m3 = projection_law(Q, [0, 1, 2])
    hpair = projection_law(Q, [1, 2])
    # This example's two middle laws both exceed the single-phase maximum
    # of 1+2*(6-2)=9 possible rank-two atoms.
    assert len(m1) > 9 and len(m2) > 9
    flow = inclusion_flow(hpair, m3)
    bottom, top, aggregate, joint_sm = [defaultdict(F) for _ in range(4)]
    diamonds = {}
    for (B, T), t in flow.items():
        S = tuple(sorted(set(T)-set(B)))
        assert len(S) == 1
        diamonds[S, T] = t
        bottom[S] += t
        top[T] += t
        for i in B:
            M = tuple(sorted(S+(i,)))
            aggregate[M] += t
            joint_sm[S, M] += t/2
    assert dict(bottom) == m0 and dict(top) == m3
    for M in set(aggregate) | set(m1) | set(m2):
        assert aggregate[M] == m1.get(M, F(0))+m2.get(M, F(0))
    mbar = {M: p/2 for M, p in aggregate.items() if p}
    H0, H1, H2, H3, Hbar, Hd, Hsm = map(
        entropy, [m0, m1, m2, m3, mbar, diamonds, joint_sm])
    l2 = log_interval(F(2))
    beta = linear([(1, H1), (1, H2), (-1, H0), (-1, H3)])
    js = linear([(1, Hbar), (-F(1, 2), H1), (-F(1, 2), H2)])
    s_given_t = linear([(1, Hd), (-1, H3)])
    s_given_m = linear([(1, Hsm), (-1, Hbar)])
    cmi = linear([(2, Hsm), (-1, H0), (-1, Hd), (-1, l2)])
    rhs = linear([(1, l2), (1, s_given_t), (-2, s_given_m),
                  (1, cmi), (-2, js)])
    check_zero(linear([(1, beta), (-1, rhs)]))
    assert js[0] > 0 and linear([(1, l2), (-1, js)])[0] > 0
    assert s_given_t[0] > 0 and cmi[0] > 0
    assert s_given_m[0] > 0 and linear([(1, l2), (-1, s_given_m)])[0] > 0
    assert linear([(1, beta), (3, l2)])[0] > 0
    # Four actual spectral points, including both same-sign and opposite-sign
    # directions. Exact rational atom derivatives precede logarithm enclosure.
    checks = []
    samples = [(F(1, 2), F(1, 2), F(1), F(1)),
               (F(1, 5), F(4, 5), F(2), F(1)),
               (F(2, 7), F(3, 5), F(1), F(-2)),
               (F(2, 7), F(3, 5), F(1), F(0))]
    support = set(m0) | set(m1) | set(m2) | set(m3)
    for p, q, alpha, eta in samples:
        atoms, first, second = {}, {}, {}
        for S in support:
            a0, a1, a2, a3 = [m.get(S, F(0)) for m in [m0, m1, m2, m3]]
            atoms[S] = ((1-p)*(1-q)*a0+p*(1-q)*a1
                        +q*(1-p)*a2+p*q*a3)
            first[S] = (-(alpha*(1-q)+eta*(1-p))*a0
                        +(alpha*(1-q)-eta*p)*a1
                        +(eta*(1-p)-alpha*q)*a2
                        +(alpha*q+eta*p)*a3)
            second[S] = 2*alpha*eta*(a0-a1-a2+a3)
        assert sum(atoms.values()) == 1
        assert sum(first.values()) == sum(second.values()) == 0
        fisher = sum(first[S]**2/atoms[S] for S in support)
        curvature = linear([(-1, constant(fisher))]+
                           [(-second[S], log_interval(atoms[S])) for S in support])
        assert curvature[1] < 0
        record = {'p': str(p), 'q': str(q),
                  'slopes': [str(alpha), str(eta)],
                  'curvature': interval_json(curvature)}
        if alpha*eta > 0:
            guaranteed = times(-2*alpha*eta,
                               linear([(1, constant(4)), (-5, l2)]))
            assert curvature[1] <= guaranteed[0]
            record['universal_upper_bound'] = interval_json(guaranteed)
        elif alpha*eta < 0:
            for (S, T), t in diamonds.items():
                i, j = sorted(set(T)-set(S))
                M, N = tuple(sorted(S+(i,))), tuple(sorted(S+(j,)))
                assert atoms[S]*atoms[T] <= atoms[M]*atoms[N]
        checks.append(record)
    def encode_law(law):
        return [{'set': list(S), 'p': str(p)} for S, p in sorted(law.items())]
    certificate = {
        'construction': 'Q=H_k H_h, H_x=I-2*x*x^*/||x||^2',
        'h': [[str(a), str(b)] for a, b in map(ga, h)],
        'k': [[str(a), str(b)] for a, b in map(ga, k)],
        'Q': [[[str(a), str(b)] for a, b in row] for row in Q],
        'projection_laws': {name: encode_law(law)
                            for name, law in [('mu0', m0), ('mu1', m1),
                                              ('mu2', m2), ('mu3', m3),
                                              ('added_pair', hpair)]},
        'diamonds': [{'bottom': list(S), 'top': list(T), 'weight': str(t)}
                     for (S, T), t in sorted(diamonds.items())],
        'entropy_information': {name: interval_json(a) for name, a in
                                [('beta', beta), ('JS', js),
                                 ('H_bottom_given_top', s_given_t),
                                 ('H_bottom_given_middle', s_given_m),
                                 ('I_additions_given_bottom', cmi)]},
        'spectral_curvature_checks': checks,
    }
    (HERE/'rational_flag_certificate.json').write_text(json.dumps(certificate, indent=2)+'\n')
    return {'ambient_dimension': 6,
            'projection_support_sizes': [len(m0), len(m1), len(m2), len(m3)],
            'positive_diamonds': len(diamonds),
            'beta': interval_json(beta), 'spectral_checks': len(checks)}


def main():
    l2 = log_interval(F(2))
    gap = linear([(1, constant(4)), (-5, l2)])
    assert gap[0] > 0
    counts = check_counts()
    flag = check_flag()
    output = {'status': 'PASS', 'count_checks': len(counts),
              'count_constant_4_minus_2_log2': interval_json(
                  linear([(1, constant(4)), (-2, l2)])),
              'rank_one_gap_4_minus_5_log2': interval_json(gap),
              'flag': flag, 'count_records': counts}
    (HERE/'verified_output.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: v for k, v in output.items() if k != 'count_records'}, indent=2))


if __name__ == '__main__':
    main()
