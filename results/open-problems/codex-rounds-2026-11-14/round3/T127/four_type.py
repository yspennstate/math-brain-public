#!/usr/bin/env python3
"""Four-type exact certificate and a small optional floating-point search."""
import argparse
import json
import time
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from independent_audit import check_resources, enumerate_matrix, matvec, peak


def formula(d,q,t):
    s = d+1
    return [
        [d*(1-q)/s/t, d*q/s/t, t/s, 0*q],
        [d*(2*d*(1-q)+q)/s**2/t, d*(2*d*q+1)/s**2/t, 2*d*t/s**2, t/s**2],
        [(d-(d-1)*q)/s/t, (d-1)*q/s/t, t/s, 0*q],
        [(2*d*d-(d-1)*(2*d-1)*q)/s**2/t,
         (d+2*d*(d-1)*q)/s**2/t, 2*d*t/s**2, t/s**2],
    ]


def approximate(d,q,t):
    m = formula(d,q,t)
    v = [1.,2.,1.,2.]
    for _ in range(120):
        w = [sum(a*b for a,b in zip(row,v)) for row in m]
        rho = w[1]/v[1]
        v = [x*2/w[1] for x in w]
    return rho,v


def search():
    for d in (3,4):
        best = (0.,None,None)
        for k in range(80):
            t = 1.5+k*.02
            lo,hi = 0.,1.
            for _ in range(15):
                q = (lo+hi)/2
                rho,v = approximate(d,q,t)
                if rho < 1:
                    lo = q
                else:
                    hi = q
            if lo > best[0]:
                best = (lo,t,approximate(d,lo,t)[1])
        print(f'exploratory d={d}: q~{best[0]}, t={best[1]}, v={best[2]}')


def bits_matrix(d,q,t):
    """Third derivation: explicit Bernoulli configurations, with total mass."""
    names = ('F','D','B','E')
    matrix = []
    for kind in names:
        row = [Q(0)]*4
        mass = Q(0)
        n = 2 if kind in ('D','E') else 1
        for steps in product(range(-1,d), repeat=n):
            fresh = sorted(set(steps)-{-1})
            if kind in ('B','E') and 0 in fresh:
                fresh.remove(0)
            for bits in product((0,1), repeat=len(fresh)):
                prob = Q(1,(d+1)**n)
                for b in bits:
                    prob *= q if b else 1-q
                mass += prob
                sleepers = dict(zip(fresh,bits))
                for target in set(steps):
                    k = steps.count(target)
                    if target == -1:
                        row[2 if k == 1 else 3] += prob*t
                    else:
                        total = k+sleepers.get(target,0)
                        pairs,singles = divmod(total,2)
                        row[0] += prob*singles/t
                        row[1] += prob*pairs/t
        assert mass == 1
        matrix.append(row)
    return matrix


def certify(d,q,t,v):
    for r in (Q(0),q,Q(1)):
        m = formula(d,r,t)
        assert m == enumerate_matrix(d,r,t,True) == bits_matrix(d,r,t)
        # Frog-slot totals offer a further check independent of packet labels.
        capacities = [Q(1),Q(2),Q(1),Q(2)]
        # Weighted births: each fresh child hit spawns q new slots.
        expected_counts = [
            t/(d+1) + d*(1+r)/(d+1)/t,
            2*t/(d+1) + (Q(2*d,d+1)+r*d*(2*d+1)/(d+1)**2)/t,
            t/(d+1) + (d+(d-1)*r)/(d+1)/t,
            2*t/(d+1) + (Q(2*d,d+1)+r*(d-1)*(2*d+1)/(d+1)**2)/t,
        ]
        assert matvec(m,capacities) == expected_counts
    m = formula(d,q,t)
    mv = matvec(m,v)
    slack = [a-b for a,b in zip(v,mv)]
    c = min(v[2],v[1]/2,v[3]/2)
    g = ((1-q)*v[0]+q*v[1])/t
    assert t > 1 and min(v) > 0 and min(slack) > 0 and g < c
    # Enumerate height-one weights from the bit-derived matrix by replacing
    # B and E backward output by c and 2c, respectively.
    back_terms = [t/(d+1)*v[2],
                  2*d*t/(d+1)**2*v[2]+t/(d+1)**2*v[3],
                  t/(d+1)*v[2],
                  2*d*t/(d+1)**2*v[2]+t/(d+1)**2*v[3]]
    root_terms = [t/(d+1)*c,2*t/(d+1)*c,
                  t/(d+1)*c,2*t/(d+1)*c]
    boundary = [a-b+r for a,b,r in zip(mv,back_terms,root_terms)]
    assert all(a <= b for a,b in zip(boundary,mv))
    rho = max(g/c, *(a/b for a,b in zip(mv,v)))
    epsilon = min(1-g/c, *(a/b for a,b in zip(slack,v)))
    assert 1-rho == epsilon and rho < 1
    full_slack = [a-b for a,b in zip(v,matvec(formula(d,Q(1),t),v))]
    assert max(full_slack) < 0
    previous = Q(41,100) if d == 3 else Q(33,50)
    print(f'd={d}; q={q}; t={t}; v={tuple(map(str,v))}; c={c}')
    print('  v-Mv =',tuple(map(str,slack)))
    print('  root_margin =',c-g)
    print('  root_replacement_margins =',tuple(map(str,[v[2]-c,v[1]-2*c,v[3]-2*c])))
    print('  rho =',rho,'; E[visits] <=',1/epsilon)
    print('  q_improvement =',q-previous)
    print('  q=1 slacks =',tuple(map(str,full_slack)))
    return {'d':d,'q':str(q),'t':str(t),'v':list(map(str,v)),
            'c':str(c),'matrix':[[str(x) for x in row] for row in m],
            'slack':list(map(str,slack)),'root_margin':str(c-g),
            'rho':str(rho),'expected_visits_bound':str(1/epsilon),
            'height_one_weights':list(map(str,boundary)),
            'q_one_slack':list(map(str,full_slack))}


if __name__ == '__main__':
    check_resources()
    started = time.monotonic()
    parser = argparse.ArgumentParser()
    parser.add_argument('--search', action='store_true')
    args = parser.parse_args()
    if args.search:
        search()
    else:
        cases = [
            (3,Q(419,1000),Q(51,25),
             [Q(1022057,1000000),Q(2),Q(971841,1000000),Q(382311,200000)]),
            (4,Q(337,500),Q(127,50),
             [Q(511527,500000),Q(2),Q(971203,1000000),Q(1906179,1000000)]),
        ]
        results = []
        for d,q,t,v in cases:
            results.append(certify(d,q,t,v))
        Path('four_type_data.json').write_text(json.dumps(results,indent=2)+'\n')
        print('PASS: three independent matrices, exact slacks, root, and q=1 failures.')
    peak()
    print(f'elapsed_seconds = {time.monotonic()-started:.3f}')
