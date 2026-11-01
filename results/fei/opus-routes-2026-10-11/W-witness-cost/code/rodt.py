"""Selector trees with regular leaves (class K of NOTES.md) and the exact queue-law witness costs.

Tree encoding: ('leaf', i) or ('node', var, plus_subtree, minus_subtree), where var is a global
coordinate index (a control variable); 'plus' is followed when x_var = +1.
Leaf i carries (block_vars, local_truth_table) with local index bit k <-> block_vars[k] = -1.
"""
import math
import random
import itertools
import numpy as np
from fractions import Fraction

import fei_core as fc

A_EXP = 6.0 / 5.0  # the paper's a


# ---------- tree utilities ----------
def leaves_with_paths(tree, path=()):
    """Yield (leaf_id, path) where path = tuple of (var, sign) from root."""
    if tree[0] == 'leaf':
        yield tree[1], path
    else:
        _, var, plus, minus = tree
        yield from leaves_with_paths(plus, path + ((var, 1),))
        yield from leaves_with_paths(minus, path + ((var, -1),))


def internal_nodes(tree, anc=()):
    """Yield (var, anc_path, plus_subtree, minus_subtree); anc_path = tuple of (var, sign) above."""
    if tree[0] == 'leaf':
        return
    _, var, plus, minus = tree
    yield var, anc, plus, minus
    yield from internal_nodes(plus, anc + ((var, 1),))
    yield from internal_nodes(minus, anc + ((var, -1),))


def subtree_mean(tree, mu):
    """E[leaf mean] under uniform control bits below this node."""
    if tree[0] == 'leaf':
        return mu[tree[1]]
    _, var, plus, minus = tree
    return (subtree_mean(plus, mu) + subtree_mean(minus, mu)) / 2


def subtree_leaves(tree):
    return [i for i, _ in leaves_with_paths(tree)]


def is_read_once(tree):
    vs = [v for v, _, _, _ in internal_nodes(tree)]
    return len(vs) == len(set(vs))


# ---------- leaf library ----------
def ltf_table(w, weights, theta):
    """LTF sgn(sum w_k x_k - theta) on w local vars (sgn(0)=+1)."""
    T = []
    for x in range(1 << w):
        s = 0
        for k in range(w):
            xk = -1 if (x >> k) & 1 else 1
            s += weights[k] * xk
        T.append(1 if s - theta >= 0 else -1)
    return T


def random_ltf(w, rng):
    while True:
        weights = [rng.choice([-3, -2, -1, 1, 2, 3, 4]) for _ in range(w)]
        theta = rng.choice([-5, -3, -2, -1, 0, 1, 2, 3, 5]) + 0.5
        T = ltf_table(w, weights, theta)
        return T


def and_table(w):
    return [1 if x == 0 else -1 for x in range(1 << w)]  # true iff all x_k = +1


def or_table(w):
    return [-1 if x == (1 << w) - 1 else 1 for x in range(1 << w)]  # false iff all x_k = -1


# ---------- global function ----------
class SelectorTree:
    def __init__(self, tree, leaves):
        """leaves: dict leaf_id -> (block_vars list, local table)."""
        self.tree = tree
        self.leaves = leaves
        self.paths = dict(leaves_with_paths(tree))
        ctrl = set(v for v, _, _, _ in internal_nodes(tree))
        data = set()
        for i, (bv, _) in leaves.items():
            data |= set(bv)
        assert not (ctrl & data), "control and data variables must be disjoint"
        self.ctrl = sorted(ctrl)
        self.data = sorted(data)
        self.n = max(ctrl | data | {-1}) + 1
        # leaf spectra (exact)
        self.leaf_spec = {}
        self.mu = {}
        for i, (bv, T) in leaves.items():
            w = len(bv)
            W = fc.fwht_int(T)
            spec = {}
            for Sloc, c in enumerate(W):
                if c != 0:
                    Sg = 0
                    for k in range(w):
                        if (Sloc >> k) & 1:
                            Sg |= 1 << bv[k]
                    spec[Sg] = Fraction(c, 1 << w)
            self.leaf_spec[i] = spec
            self.mu[i] = spec.get(0, Fraction(0))

    def leaf_of(self, x):
        t = self.tree
        while t[0] == 'node':
            _, var, plus, minus = t
            t = minus if (x >> var) & 1 else plus
        return t[1]

    def eval(self, x):
        i = self.leaf_of(x)
        bv, T = self.leaves[i]
        loc = 0
        for k, v in enumerate(bv):
            if (x >> v) & 1:
                loc |= 1 << k
        return T[loc]

    def truth_table(self):
        assert self.n <= 22
        return [self.eval(x) for x in range(1 << self.n)]

    # ---- predicted exact spectrum (NOTES section 4) ----
    def predicted_spectrum(self):
        """Return dict S -> Fraction coefficient fhat(S) predicted by the selector formula
        fhat(T u B) = sum_i 1hat_{C_i}(T) ghat_i(B) (valid for ANY decision tree)."""
        coef = {}
        for i, path in self.paths.items():
            c = len(path)
            pv = [v for v, _ in path]
            sg = {v: s for v, s in path}
            for r in range(c + 1):
                for Tsub in itertools.combinations(pv, r):
                    Tm = 0
                    sign = 1
                    for v in Tsub:
                        Tm |= 1 << v
                        sign *= sg[v]
                    cell = Fraction(sign, 1 << c)
                    for B, gb in self.leaf_spec[i].items():
                        key = Tm | B
                        coef[key] = coef.get(key, Fraction(0)) + cell * gb
        return {k: v for k, v in coef.items() if v != 0}


def masses_from_coef(coef):
    return {S: c * c for S, c in coef.items()}


def H_I_from_masses(masses):
    H = 0.0
    I = Fraction(0)
    v = Fraction(0)
    for S, m in masses.items():
        if m == 0:
            continue
        H += float(m) * math.log2(1.0 / float(m))
        I += fc.popcount(S) * m
        if S:
            v += m
    return H, I, v
