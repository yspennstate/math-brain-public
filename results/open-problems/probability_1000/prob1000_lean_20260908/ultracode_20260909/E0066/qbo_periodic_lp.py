"""E0066: which periods can a quadratic bistochastic operator (QBO) on S^{m-1} have?

By the structural theorem every periodic orbit consists of coordinate permutations of one vector y.
So fix y and a cyclic sequence y_0 = y, y_1, ..., y_{p-1} of distinct permutation vectors of y and ask
whether some QBO V satisfies V(y_r) = y_{r+1 mod p}.  V(y) is linear in the cubic matrix P, and the
QBO polytope B_m is cut out by linear constraints (Ganikhodzhaev's condition (c) plus (5)), so this
is a linear-programming feasibility problem.  Every feasible P found is re-checked by direct iteration
and by a random majorisation test.
"""
import itertools, sys, time
import numpy as np
from scipy.optimize import linprog
rng = np.random.default_rng(7)


def var_index(m):
    pairs = [(i, j) for i in range(m) for j in range(i, m)]
    idx = {}
    for a, (i, j) in enumerate(pairs):
        for k in range(m):
            idx[(i, j, k)] = a * m + k
    return pairs, idx


def build_P(m, sol):
    pairs, idx = var_index(m)
    P = np.zeros((m, m, m))
    for (i, j) in pairs:
        for k in range(m):
            P[i, j, k] = sol[idx[(i, j, k)]]
            P[j, i, k] = sol[idx[(i, j, k)]]
    return P


def apply(P, x):
    # V is homogeneous of degree 2, so the mass sum V(x) = (sum x)^2 drifts doubly-exponentially under rounding;
    # renormalising keeps the iterate on the simplex (the same map there).
    v = np.einsum('ijk,i,j->k', P, x, x)
    return v / v.sum()


def sorted_partial(x):
    return np.cumsum(np.sort(x)[::-1])


def polytope_constraints(m):
    pairs, idx = var_index(m)
    nv = len(pairs) * m
    A_eq, b_eq, A_ub, b_ub = [], [], [], []
    for (i, j) in pairs:  # sum_k P_{ij,k} = 1
        row = np.zeros(nv)
        for k in range(m):
            row[idx[(i, j, k)]] = 1
        A_eq.append(row); b_eq.append(1.0)
    for t in range(1, m + 1):  # condition (c): sum_{i,j in I} P_{ij,k} <= t   (i,j ordered, so off-diagonal pairs count twice)
        for I in itertools.combinations(range(m), t):
            for k in range(m):
                row = np.zeros(nv)
                for i in I:
                    for j in I:
                        a, b = min(i, j), max(i, j)
                        row[idx[(a, b, k)]] += 1
                A_ub.append(row); b_ub.append(float(t))
    return np.array(A_eq), np.array(b_eq), np.array(A_ub), np.array(b_ub), nv


def orbit_rows(m, cycle):
    pairs, idx = var_index(m)
    nv = len(pairs) * m
    rows, rhs = [], []
    p = len(cycle)
    for r in range(p):
        x, target = cycle[r], cycle[(r + 1) % p]
        for k in range(m):
            row = np.zeros(nv)
            for (i, j) in pairs:
                row[idx[(i, j, k)]] = x[i] * x[j] * (1 if i == j else 2)
            rows.append(row); rhs.append(target[k])
    return np.array(rows), np.array(rhs)


def feasible(m, cycle, base):
    A_eq, b_eq, A_ub, b_ub, nv = base
    R, rhs = orbit_rows(m, cycle)
    # a random objective, then its negative: if the feasible polytope is more than one point the two
    # vertices differ, and a non-permutation operator (if any) is found unless both vertices are permutations
    c = rng.standard_normal(nv)
    out = None
    for cc in (c, -c):
        res = linprog(cc, A_ub=A_ub, b_ub=b_ub, A_eq=np.vstack([A_eq, R]), b_eq=np.concatenate([b_eq, rhs]),
                      bounds=[(0, 1)] * nv, method='highs')
        if res.status != 0:
            return None
        P = build_P(m, res.x)
        if out is None or not is_permutation_operator(P):
            out = P
    return out


def verify(P, cycle, n_maj=400):
    """direct check: iterate and compare with the cycle; random majorisation test."""
    m = P.shape[0]
    x = cycle[0].copy(); p = len(cycle)
    err = 0.0
    for r in range(3 * p):
        x = apply(P, x)
        err = max(err, float(np.max(np.abs(x - cycle[(r + 1) % p]))))
    maj_fail = 0
    for _ in range(n_maj):
        z = rng.exponential(size=m); z /= z.sum()
        if np.any(sorted_partial(apply(P, z)) > sorted_partial(z) + 1e-9):
            maj_fail += 1
    return err, maj_fail


def is_permutation_operator(P, tol=1e-7):
    m = P.shape[0]
    for sigma in itertools.permutations(range(m)):
        Q = np.zeros((m, m, m))
        for k in range(m):
            for j in range(m):
                Q[sigma[k], j, k] += 0.5; Q[j, sigma[k], k] += 0.5
        if np.max(np.abs(P - Q)) < tol:
            return True
    return False


def perm_vectors(y):
    m = len(y)
    out = []
    for s in itertools.permutations(range(m)):
        v = np.array([y[s[i]] for i in range(m)])
        if not any(np.allclose(v, w) for w in out):
            out.append(v)
    return out


def scan(m, y, max_cycles_per_p=None, periods=None, label=''):
    base = polytope_constraints(m)
    pv = perm_vectors(y)
    n = len(pv)
    periods = periods or range(1, n + 1)
    print('--- m=%d y=%s (%d distinct permutation vectors) %s' % (m, np.round(y, 3), n, label))
    found = {}
    for p in periods:
        if p > n:
            break
        cnt = 0; feas = 0; feas_nonperm = 0; example = None
        # cyclic sequences of p distinct permutation vectors starting at pv[0]
        others = list(range(1, n))
        import math
        total = math.perm(len(others), p - 1)
        if max_cycles_per_p is None or total <= max_cycles_per_p:
            seqs = itertools.permutations(others, p - 1)
        else:
            seqs = [tuple(rng.permutation(others)[:p - 1]) for _ in range(max_cycles_per_p)]
        for rest in seqs:
            cycle = [pv[0]] + [pv[i] for i in rest]
            cnt += 1
            P = feasible(m, cycle, base)
            if P is not None:
                err, mf = verify(P, cycle)
                if err > 1e-6 or mf > 0:
                    print('   !! LP solution failed direct check', p, err, mf)
                    continue
                feas += 1
                if not is_permutation_operator(P):
                    feas_nonperm += 1
                    if example is None:
                        example = (cycle, P)
        found[p] = (cnt, feas, feas_nonperm)
        print('   period %d: %d cyclic orders tried, %d realisable by a QBO, %d of them by a NON-permutation QBO' % (p, cnt, feas, feas_nonperm))
        if example is not None:
            cycle, P = example
            print('      example cycle:', [tuple(np.round(c, 3)) for c in cycle])
            np.save('example_P_m%d_p%d_%s.npy' % (m, p, label.replace(' ', '_')), P)
    return found


if __name__ == '__main__':
    t0 = time.time()
    # m = 3: generic interior point (6 distinct permutation vectors) and a boundary point (a,b,0)
    scan(3, np.array([0.5, 0.3, 0.2]), label='interior')
    scan(3, np.array([0.6, 0.4, 0.0]), label='boundary')
    scan(3, np.array([0.5, 0.25, 0.25]), label='interior two equal')
    # m = 4: generic interior point has 24 permutation vectors; sample cyclic orders for p up to 8, all for p<=3
    scan(4, np.array([0.4, 0.3, 0.2, 0.1]), max_cycles_per_p=150, periods=range(1, 9), label='interior')
    scan(4, np.array([0.4, 0.3, 0.2, 0.1]), max_cycles_per_p=150, periods=[12, 24], label='interior long')
    scan(4, np.array([0.5, 0.3, 0.2, 0.0]), max_cycles_per_p=150, periods=range(2, 9), label='boundary')
    print('done %.0fs' % (time.time() - t0))
