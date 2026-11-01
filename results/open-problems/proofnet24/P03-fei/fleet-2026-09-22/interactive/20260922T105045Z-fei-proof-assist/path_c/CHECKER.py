#!/usr/bin/env python3
"""Independent exact combinatorial checks for robust trigger clusters.

No finite check is used as a proof of FEI or of universal ratio criticality.
The displayed entropy/slack values use binary64; all graph/support/mass
checks use integer counts or Fraction arithmetic.
"""
from fractions import Fraction
from itertools import product
from math import log2, log1p, log, sqrt
import json
import numpy as np

ETA = Fraction(1, 16)


def derivative(b, coordinate):
    return b ^ b[np.arange(len(b)) ^ (1 << coordinate)]


def center(b, n):
    b = b.copy()
    indices = np.arange(len(b))
    for i in range(n):
        if int(derivative(b, i).sum()) > len(b) // 2:
            b ^= ((indices >> i) & 1).astype(np.uint8)
    return b


def subcube(n, assignments):
    indices = np.arange(1 << n)
    mask = np.ones(1 << n, dtype=np.uint8)
    for i, a in assignments.items():
        mask &= (((indices >> i) & 1) == a).astype(np.uint8)
    return mask


def find_robust_rows(b, n):
    rows = {}
    N = len(b)
    for i in range(n):
        E = derivative(b, i)
        count = int(E.sum())
        if count == 0:
            continue
        others = [j for j in range(n) if j != i]
        matches = []
        for spec in product((-1, 0, 1), repeat=n - 1):
            assignments = {j: a for j, a in zip(others, spec) if a >= 0}
            Q = subcube(n, assignments)
            error = int(np.count_nonzero(E ^ Q))
            if Fraction(error, count) <= ETA:
                matches.append((assignments, Q, error))
        assert len(matches) <= 1
        if matches:
            assignments, Q, error = matches[0]
            rows[i] = dict(E=E, Q=Q, F=set(assignments), a=assignments,
                           q=Fraction(count, N), s=Fraction(int(Q.sum()), N),
                           eps=Fraction(error, N))
    return rows


def validate_rows(b, n, rows):
    N = len(b)
    for i, ri in rows.items():
        assert ri['q'] <= Fraction(1, 2)
        assert ri['eps'] <= ETA * ri['q']
        assert derivative(b, i).tolist() == ri['E'].tolist()
        assert ri['F']
        for j, rj in rows.items():
            if i == j:
                continue
            actual = derivative(ri['E'], j)
            assert np.array_equal(actual, derivative(rj['E'], i))
            if j not in ri['F']:
                continue
            if i not in rj['F']:
                assert rj['q'] >= 14 * ri['q']
            else:
                assert np.array_equal(derivative(ri['Q'], j),
                                      derivative(rj['Q'], i))
                assert ri['F'] | {i} == rj['F'] | {j}
    components = []
    pending = set(rows)
    while pending:
        seed = min(pending)
        C = {seed}
        while True:
            expanded = C | {j for i in C for j in pending
                            if j in rows[i]['F'] and i in rows[j]['F']}
            if expanded == C:
                break
            C = expanded
        pending -= C
        components.append(C)
        for i in C:
            assert C - {i} <= rows[i]['F']
            for j in C:
                assert rows[i]['F'] | {i} == rows[j]['F'] | {j}
    owner = {i: c for c, C in enumerate(components) for i in C}
    arrows = set()
    for i, ri in rows.items():
        for j in ri['F'] & set(rows):
            if owner[i] != owner[j]:
                assert rows[j]['s'] >= 16 * ri['s']
                arrows.add((owner[i], owner[j]))
    return components, arrows


def phase(q):
    if q <= 0:
        return 0.0
    if q == 0.5:
        return 1.0
    if q < 1e-7:
        u2 = 4 * q * (1 - q)
        term = u2
        answer = 0.0
        for k in range(1, 20):
            answer += term / ((2*k) * (2*k - 1) * log(2))
            term *= u2
        return answer
    t = 0.5 + sqrt(q * (1 - q))
    return 1 + t * log2(t) + (1-t) * log2(1-t)


def FJ(b, n):
    N = len(b)
    W = 1 - 2 * b.astype(np.int64)
    for i in range(n):
        a = W.reshape(-1, 2, 1 << i)
        lo, hi = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :], a[:, 1, :] = lo + hi, lo - hi
    p = W.astype(float)**2 / (N*N)
    p = p[p != 0]
    H = float(-np.dot(p, np.log2(p)))
    q = [Fraction(min(int(derivative(b, i).sum()),
                          N-int(derivative(b, i).sum())), N) for i in range(n)]
    J = sum(q)
    return H - sum(phase(float(x)) for x in q), J


def check_fibers(b, n, rows, C, rho=10.0):
    C = sorted(C)
    m = len(C)
    assert m >= 2
    Ncore = rows[C[0]]['F'] | {C[0]}
    T = Ncore - set(C)
    assignments = {}
    for i in C:
        for j, a in rows[i]['a'].items():
            if j in assignments:
                assert assignments[j] == a
            assignments[j] = a
    assert set(assignments) == Ncore
    Mbit = subcube(n, assignments)
    hbit = b ^ Mbit
    eps_sum = sum(rows[i]['eps'] for i in C)
    assert sum(Fraction(int(derivative(hbit, i).sum()), len(b)) for i in C) == eps_sum
    outside = [i for i in range(n) if i not in C]
    mpoint = np.array([int(all(((x >> k) & 1) == assignments[i]
                              for k, i in enumerate(C))) for x in range(1 << m)],
                     dtype=np.uint8)
    Fpoint, Jpoint = FJ(mpoint, m)
    assert Jpoint == Fraction(m, 1 << (m-1))
    rm = Fpoint / float(Jpoint)
    assert rm < 2
    bad = good_active = 0
    total_error_influence = Fraction(0)
    child_slack = 0.0
    for z in range(1 << len(outside)):
        fixed = sum(((z >> k) & 1) << i for k, i in enumerate(outside))
        indices = [fixed | sum(((x >> k) & 1) << i for k, i in enumerate(C))
                   for x in range(1 << m)]
        hz = hbit[indices]
        fz = b[indices]
        active = all(((fixed >> i) & 1) == assignments[i] for i in T)
        nonconstant = bool(np.any(hz != hz[0]))
        Ifiber = sum(Fraction(int(derivative(hz, i).sum()), 1 << m) for i in range(m))
        total_error_influence += Ifiber
        if nonconstant:
            bad += 1
            assert Ifiber >= Jpoint
        elif active:
            good_active += 1
            assert np.array_equal(fz, mpoint) or np.array_equal(fz, 1-mpoint)
        else:
            assert np.all(fz == fz[0])
        Fchild, Jchild = FJ(fz, m)
        slack = rho * float(Jchild) - Fchild
        assert slack >= -1e-12
        child_slack += slack
    denom = 1 << len(outside)
    bad_prob = Fraction(bad, denom)
    good_prob = Fraction(good_active, denom)
    Jcore = sum(rows[i]['q'] for i in C)
    assert total_error_influence / denom == eps_sum
    assert bad_prob <= eps_sum / Jpoint
    assert good_prob >= Fraction(1, 1 << len(T)) - eps_sum / Jpoint
    assert good_prob >= (1-2*ETA)/(1-ETA) / (1 << len(T))
    assert child_slack / denom + 1e-12 >= float((1-2*ETA)*Jcore) * (rho-rm)
    return {'clique':C,'core':sorted(Ncore),'outside_triggers':sorted(T),
            'bad_probability':str(bad_prob),'good_active_probability':str(good_prob),
            'parent_clique_influence':str(Jcore),'point_defect_ratio':rm,
            'rho_for_regression':rho,'mean_child_slack':child_slack/denom,
            'proved_lower_bound':float((1-2*ETA)*Jcore)*(rho-rm)}


def main():
    gates = robust_rows = reciprocal_components = 0
    for n in range(1, 4):
        for mask in range(1 << (1 << n)):
            b = np.array([(mask >> x) & 1 for x in range(1 << n)], dtype=np.uint8)
            b = center(b, n)
            rows = find_robust_rows(b, n)
            comps, arrows = validate_rows(b, n, rows)
            assert not arrows  # exact supports at these finite resolutions
            gates += 1
            robust_rows += len(rows)
            reciprocal_components += len(comps)
    n = 11
    big, small = {0,1,2,3}, {0,4,5,6,7,8,9,10}
    b = subcube(n, dict.fromkeys(big, 1)) ^ subcube(n, dict.fromkeys(small, 1))
    rows = {}
    for i in range(n):
        core = big if i in big else small
        assignments = dict.fromkeys(core-{i}, 1)
        Q = subcube(n, assignments)
        E = derivative(b, i)
        rows[i] = dict(E=E,Q=Q,F=set(assignments),a=assignments,
                       q=Fraction(int(E.sum()),1<<n),s=Fraction(int(Q.sum()),1<<n),
                       eps=Fraction(int(np.count_nonzero(E^Q)),1<<n))
    comps, arrows = validate_rows(b, n, rows)
    assert {frozenset(C) for C in comps} == {frozenset(big), frozenset(small-{0})}
    assert rows[0]['q'] == Fraction(67,512)
    assert rows[0]['eps'] == Fraction(1,128)
    fibers = [check_fibers(b,n,rows,C) for C in comps]
    max_rm = -1.0
    for m in range(2, 129):
        q = 2.0**(1-m)
        v = q*(2-q)
        H = -(1-q)**2 * (2*log1p(-q)/log(2)) + v*(2*m-2)
        rm = H/(m*q) - phase(q)/q
        assert rm < 2
        max_rm = max(max_rm,rm)
    print(json.dumps({'exhaustive_gates_n_le_3':gates,
                      'robust_rows_checked':robust_rows,
                      'reciprocal_components_checked':reciprocal_components,
                      'hierarchy_influences':{str(i):str(r['q']) for i,r in rows.items()},
                      'hierarchy_components':[sorted(C) for C in comps],
                      'hierarchy_arrows':sorted(arrows),
                      'fiber_checks':fibers,
                      'max_point_defect_F_over_J_m_2_through_128':max_rm,
                      'result':'PASS'},indent=2))


if __name__ == '__main__':
    main()
