"""Selector trees with regular leaves (class K of NOTES section 4), written independently.

A tree is a nested tuple:  ('leaf', leaf_dict)  or  ('node', var, plus_subtree, minus_subtree)
(plus subtree taken when x_var = +1).  A leaf dict: {'kind': 'const'|'ltf', 'val': +-1 (const),
'vars': [data vars], 'w': [positive int weights], 'sig': [+-1 orientations], 'th': int threshold}.
LTF leaf: g(y) = +1 iff sum_j w_j sig_j y_j >= th.  Desirability order = decreasing w (ties by position).
"""
import random
from fractions import Fraction
import numpy as np
from rc_common import coords, spectrum, stats_exact, popcount, bits_of


def eval_leaf(leaf, X):
    if leaf['kind'] == 'const':
        return np.full(X[0].shape, leaf['val'], dtype=np.int8)
    tot = np.zeros(X[0].shape, dtype=np.int64)
    for v, w, s in zip(leaf['vars'], leaf['w'], leaf['sig']):
        tot += w * s * X[v].astype(np.int64)
    return np.where(tot >= leaf['th'], 1, -1).astype(np.int8)


def eval_tree(tree, X):
    if tree[0] == 'leaf':
        return eval_leaf(tree[1], X)
    _, var, tp, tm = tree
    a = eval_tree(tp, X)
    b = eval_tree(tm, X)
    return np.where(X[var] == 1, a, b).astype(np.int8)


def leaves_with_paths(tree, path=()):
    """List of (leaf_dict, path) with path = tuple of (var, sign) root first."""
    if tree[0] == 'leaf':
        return [(tree[1], path)]
    _, var, tp, tm = tree
    return leaves_with_paths(tp, path + ((var, 1),)) + leaves_with_paths(tm, path + ((var, -1),))


def internal_nodes(tree, anc=()):
    """List of (var, anc_path, plus_subtree, minus_subtree) for every internal node."""
    if tree[0] == 'leaf':
        return []
    _, var, tp, tm = tree
    out = [(var, anc, tp, tm)]
    out += internal_nodes(tp, anc + ((var, 1),))
    out += internal_nodes(tm, anc + ((var, -1),))
    return out


def leaf_table(leaf):
    """Exact (P(g=1) as Fraction, relevant vars, desirability-ordered relevant vars, local spectrum dict)."""
    if leaf['kind'] == 'const':
        P = Fraction(1) if leaf['val'] == 1 else Fraction(0)
        return P, [], [], {0: leaf['val']}, 0
    vs = leaf['vars']
    k = len(vs)
    Xl = coords(k)
    tot = np.zeros(1 << k, dtype=np.int64)
    for i, (w, s) in enumerate(zip(leaf['w'], leaf['sig'])):
        tot += w * s * Xl[i].astype(np.int64)
    g = np.where(tot >= leaf['th'], 1, -1).astype(np.int8)
    P = Fraction(int(np.count_nonzero(g == 1)), 1 << k)
    idx = np.arange(1 << k)
    rel = [i for i in range(k) if np.any(g[idx ^ (1 << i)] != g)]
    order = sorted(rel, key=lambda i: (-leaf['w'][i], i))
    nloc, spec = spectrum(g)
    return P, [vs[i] for i in rel], [vs[i] for i in order], spec, k


def mean_of(tree):
    """Exact E[f] of a subtree (uniform inputs)."""
    if tree[0] == 'leaf':
        P = leaf_table(tree[1])[0]
        return 2 * P - 1
    _, var, tp, tm = tree
    return (mean_of(tp) + mean_of(tm)) / 2


# ---------------- random instance generators ----------------

def rand_ltf(rng, vars_):
    k = len(vars_)
    w = [rng.randint(1, 5) for _ in range(k)]
    sig = [rng.choice([1, -1]) for _ in range(k)]
    tot = sum(w)
    th = rng.randint(-tot + 1, tot)
    return {'kind': 'ltf', 'vars': list(vars_), 'w': w, 'sig': sig, 'th': th}


def rand_leaf(rng, next_var, max_data):
    r = rng.random()
    if r < 0.2:
        return {'kind': 'const', 'val': rng.choice([1, -1])}, next_var
    k = rng.randint(1, max_data)
    vars_ = list(range(next_var, next_var + k))
    if r < 0.45:
        # AND / OR of k literals (regular)
        sig = [rng.choice([1, -1]) for _ in range(k)]
        if rng.random() < 0.5:
            return {'kind': 'ltf', 'vars': vars_, 'w': [1] * k, 'sig': sig, 'th': k}, next_var + k
        return {'kind': 'ltf', 'vars': vars_, 'w': [1] * k, 'sig': sig, 'th': 2 - k}, next_var + k
    return rand_ltf(rng, vars_), next_var + k


def rand_readonce_tree(rng, depth_budget, n_budget, max_data, next_var=0, p_stop=0.3):
    """Random read-once control tree (fresh control variable per internal node), random regular leaves
    on fresh data blocks. Returns (tree, next_var)."""
    if depth_budget == 0 or rng.random() < p_stop or next_var >= n_budget:
        leaf, nv = rand_leaf(rng, next_var, max_data)
        return ('leaf', leaf), nv
    var = next_var
    tp, nv = rand_readonce_tree(rng, depth_budget - 1, n_budget, max_data, next_var + 1, p_stop)
    tm, nv = rand_readonce_tree(rng, depth_budget - 1, n_budget, max_data, nv, p_stop)
    return ('node', var, tp, tm), nv


def rand_general_tree_equal_means(rng, n_ctrl, depth, mean_kind):
    """Random (non-read-once) decision tree on control vars 0..n_ctrl-1 (no repeat along a path), all leaves
    regular with ONE common mean. mean_kind: 'dict' (mean 0), 'and2' (mean -1/2), 'mix' (mean -1/2 with
    AND2 / 4-var LTF 2x1+x2+x3+x4>=4 / OR? no). Leaves on fresh blocks after the control vars."""
    nv = [n_ctrl]

    def leaf():
        if mean_kind == 'dict':
            v = nv[0]; nv[0] += 1
            # dictator or anti-dictator, or majority of 3 (mean 0)
            if rng.random() < 0.6:
                return {'kind': 'ltf', 'vars': [v], 'w': [1], 'sig': [rng.choice([1, -1])], 'th': 0}
            nv[0] += 2
            return {'kind': 'ltf', 'vars': [v, v + 1, v + 2], 'w': [1, 1, 1],
                    'sig': [rng.choice([1, -1]) for _ in range(3)], 'th': 0}
        # mean -1/2: AND_2 (P = 1/4) or the 4-var LTF 2y1+y2+y3+y4 >= 4 (P = 1/4)
        if mean_kind == 'and2' or rng.random() < 0.5:
            v = nv[0]; nv[0] += 2
            return {'kind': 'ltf', 'vars': [v, v + 1], 'w': [1, 1],
                    'sig': [rng.choice([1, -1]) for _ in range(2)], 'th': 2}
        v = nv[0]; nv[0] += 4
        return {'kind': 'ltf', 'vars': [v, v + 1, v + 2, v + 3], 'w': [2, 1, 1, 1],
                'sig': [rng.choice([1, -1]) for _ in range(4)], 'th': 3}

    def build(avail, d):
        if d == 0 or not avail or rng.random() < 0.25:
            return ('leaf', leaf())
        var = rng.choice(sorted(avail))
        rest = avail - {var}
        return ('node', var, build(rest, d - 1), build(rest, d - 1))

    t = build(set(range(n_ctrl)), depth)
    return t, nv[0]


def tree_n(tree):
    m = -1
    for leaf, path in leaves_with_paths(tree):
        for v, _ in path:
            m = max(m, v)
        if leaf['kind'] == 'ltf':
            m = max(m, max(leaf['vars']))
    return m + 1
