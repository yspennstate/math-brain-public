"""Validation on K_{3,3} (must return Numaro's core as the unique optimum, F2's 3^13 enumeration) and the
exhaustive S_5-invariant, complement-anti-invariant search on the edges of K_5 (m = 10)."""
import sys, os, itertools, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orbenum import run_group, close_group, perm_cells
from hc import evaluate

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')


def k33_group():
    # variable 3r+c
    def P(f):
        return tuple(f(i // 3, i % 3) for i in range(9))
    gens = [P(lambda r, c: 3 * ((r + 1) % 3) + c), P(lambda r, c: 3 * (1 - r if r < 2 else 2) + c),
            P(lambda r, c: 3 * r + (c + 1) % 3), P(lambda r, c: 3 * r + (1 - c if c < 2 else 2)),
            P(lambda r, c: 3 * c + r)]
    return close_group(gens, 9)


def find_anti(c0, m):
    N = 1 << m
    for pi in itertools.permutations(range(m)):
        pc = perm_cells(pi, m)
        A = (N - 1) ^ pc
        if np.all(c0[A] == -c0):
            return pi
    return None


def k5_group():
    E = list(itertools.combinations(range(5), 2))
    idx = {e: i for i, e in enumerate(E)}
    G = []
    for s in itertools.permutations(range(5)):
        G.append(tuple(idx[tuple(sorted((s[a], s[b])))] for (a, b) in E))
    return sorted(set(G)), E


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if which in ('k33', 'all'):
        c0 = np.load(os.path.join(LOG, '..', '..', 'F2-new-gates', 'logs', 'numaro_core_c0.npy')).astype(np.int64)
        G = k33_group()
        pi = find_anti(c0, 9)
        print('K33 |G| =', len(G), 'anti perm', pi)
        with open(os.path.join(LOG, 'enum_k33_validation.log'), 'w') as f:
            f.write(f'anti perm {pi}\n')
            run_group('K33', G, 9, pi, topk=12, log=f)
    if which in ('k5', 'all'):
        G, E = k5_group()
        with open(os.path.join(LOG, 'enum_k5_complement.log'), 'w') as f:
            f.write(f'edges {E}\n')
            run_group('K5', G, 10, tuple(range(10)), topk=30, log=f)
