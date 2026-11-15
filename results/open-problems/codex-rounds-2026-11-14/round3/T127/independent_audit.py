#!/usr/bin/env python3
"""Recheck the earlier certificate without importing its code or data."""
import os
import resource
import signal
import sys
from fractions import Fraction as Q
from itertools import product

TYPES = ('F', 'D', 'B', 'E')


def enumerate_matrix(d, q, t, retain_pair=False):
    """Sum over walk directions; integrate each sleeper analytically."""
    names = TYPES if retain_pair else TYPES[:3]
    matrix = []
    for kind in names:
        n = 2 if kind in ('D', 'E') else 1
        row = [Q(0) for _ in names]
        for steps in product(range(d+1), repeat=n):
            # 0 = parent, 1 = remembered empty child for B and E.
            p = Q(1, (d+1)**n)
            backward = steps.count(0)
            if backward:
                target_type = 'B' if backward == 1 else ('E' if retain_pair else 'D')
                row[names.index(target_type)] += p*t
            for child in set(steps) - {0}:
                k = steps.count(child)
                r = Q(0) if child == 1 and kind in ('B', 'E') else q
                # k=1: F without a sleeper, D with one.
                # k=2: D always, plus F if a sleeper is present.
                row[0] += p/t*((1-r) if k == 1 else r)
                row[1] += p/t*(r if k == 1 else 1)
        matrix.append(row)
    return matrix


def matvec(matrix, v):
    return [sum((a*b for a, b in zip(row, v)), Q(0)) for row in matrix]


def check_resources():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    signal.alarm(60)


def peak():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    size = rss if sys.platform == 'darwin' else rss*1024
    assert size < 1024**3
    print('peak_RSS_bytes =', size)


def main():
    check_resources()
    cases = [
        (3, Q(41,100), Q(41,20), [Q(203,200),Q(2),Q(483,500)],
         [Q(1367,1640000),Q(1239,820000),Q(1777,1640000)], Q(1640000,1239)),
        (4, Q(33,50), Q(51,20), [Q(1017,1000),Q(2),Q(483,500)],
         [Q(1481,850000),Q(3173,796875),Q(1383,850000)], Q(273700,461)),
    ]
    for d,q,t,v,expected_slack,expected_bound in cases:
        mv = matvec(enumerate_matrix(d,q,t), v)
        slack = [a-b for a,b in zip(v,mv)]
        assert slack == expected_slack and min(slack) > 0
        c = min(v[2],v[1]/2)
        root_ratio = ((1-q)*v[0]+q*v[1])/t/c
        rho = max(root_ratio, *(a/b for a,b in zip(mv,v)))
        assert root_ratio < 1 and 1/(1-rho) == expected_bound
        # Alternate computation from normalized slack, including the root.
        epsilon = min(1-root_ratio, *(a/b for a,b in zip(slack,v)))
        assert 1/epsilon == expected_bound
        print(f'd={d}: slack={tuple(map(str,slack))}')
        print(f'  rho={rho}; E[visits]<={expected_bound}; root_ratio={root_ratio}')
    print('PASS: earlier two exact certificates independently recovered.')
    peak()


if __name__ == '__main__':
    main()
