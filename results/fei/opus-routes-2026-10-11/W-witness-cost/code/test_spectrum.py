"""Exact checks of the selector-tree spectrum (NOTES section 4):
 (a) fhat = predicted selector formula, for random decision trees (read-once or not) with regular leaves
     on fresh blocks;
 (b) read-once trees: phi-sets with deepest node v are exactly S u {v}, S subset of anc(v), each with
     |fhat| = 2^{-d_v} |m_+ - m_-|;
 (c) Inf_{x_v}(f) = P(reach v) (1 - m_+ m_-)/2 for read-once trees;
 (d) I(f) = sum_v w_v (d_v+1)/2 + sum_i p_i [Var_i c_i/2 + I(g_i)].
All arithmetic exact (Fractions / integers).
"""
import random
import sys
from fractions import Fraction
import fei_core as fc
from rodt import *


def random_tree(rng, ctrl_pool, depth, read_once=True, used=None, p_stop=0.3):
    """Random decision tree; returns tree and list of leaf ids (assigned later)."""
    if used is None:
        used = set()
    if depth == 0 or (rng.random() < p_stop and depth < 3):
        return ('leaf', None)
    choices = [v for v in ctrl_pool if v not in used]
    if not choices:
        return ('leaf', None)
    var = rng.choice(choices)
    if read_once:
        used.add(var)
        plus = random_tree(rng, ctrl_pool, depth - 1, True, used, p_stop)
        minus = random_tree(rng, ctrl_pool, depth - 1, True, used, p_stop)
    else:
        u2 = set(used) | {var}
        plus = random_tree(rng, ctrl_pool, depth - 1, False, set(u2), p_stop)
        minus = random_tree(rng, ctrl_pool, depth - 1, False, set(u2), p_stop)
    return ('node', var, plus, minus)


def number_leaves(tree, counter):
    if tree[0] == 'leaf':
        i = counter[0]
        counter[0] += 1
        return ('leaf', i)
    _, var, p, m = tree
    return ('node', var, number_leaves(p, counter), number_leaves(m, counter))


def random_instance(rng, max_vars=16, read_once=True):
    while True:
        nctrl = rng.randint(1, 5)
        ctrl = list(range(nctrl))
        tree = random_tree(rng, ctrl, depth=rng.randint(1, 4), read_once=read_once)
        tree = number_leaves(tree, [0])
        L = len(subtree_leaves(tree))
        nxt = nctrl
        leaves = {}
        for i in range(L):
            kind = rng.random()
            w = rng.randint(1, 3)
            if kind < 0.15:
                T = [rng.choice([-1, 1])] * 2  # constant on one var (irrelevant var)
                w = 1
            elif kind < 0.3:
                T = and_table(w)
            elif kind < 0.45:
                T = or_table(w)
            else:
                T = random_ltf(w, rng)
            leaves[i] = (list(range(nxt, nxt + w)), T)
            nxt += w
        if nxt <= max_vars:
            return SelectorTree(tree, leaves)


def check_instance(st, read_once):
    T = st.truth_table()
    n, W = fc.spectrum(T)
    actual = {S: Fraction(w, 1 << n) for S, w in enumerate(W) if w != 0}
    pred = st.predicted_spectrum()
    assert actual == pred, "selector formula mismatch"
    if not read_once:
        return
    # (b) phi-sets
    ctrlmask = 0
    for v in st.ctrl:
        ctrlmask |= 1 << v
    phi_sets = {S: c for S, c in actual.items() if S and (S & ~ctrlmask) == 0}
    predicted_phi = {}
    wsum = Fraction(0)
    Iphi = Fraction(0)
    for var, anc, plus, minus in internal_nodes(st.tree):
        mp = subtree_mean(plus, st.mu)
        mm = subtree_mean(minus, st.mu)
        d = len(anc) + 1
        mag = Fraction(1, 1 << d) * abs(mp - mm)
        if mag == 0:
            continue
        av = [a for a, _ in anc]
        sg = {a: s for a, s in anc}
        for r in range(len(av) + 1):
            for Ssub in itertools.combinations(av, r):
                Sm = 1 << var
                for a in Ssub:
                    Sm |= 1 << a
                predicted_phi[Sm] = mag
        wv = Fraction(1, 1 << (d - 1)) * ((mp - mm) / 2) ** 2
        wsum += wv
        Iphi += wv * Fraction(d + 1, 2)
        # (c) influence of x_var
        infl = fc.influences(T)[var]
        assert infl == Fraction(1, 1 << (d - 1)) * (1 - mp * mm) / 2, "Inf formula"
    assert {S: abs(c) for S, c in phi_sets.items()} == predicted_phi, "phi-set structure"
    # (d) influence decomposition
    H, I, v = H_I_from_masses({S: c * c for S, c in actual.items()})
    Iblk = Fraction(0)
    for i, path in st.paths.items():
        c = len(path)
        spec = st.leaf_spec[i]
        var_i = sum(m * m for S, m in spec.items() if S)
        Ig = sum(fc.popcount(S) * m * m for S, m in spec.items())
        Iblk += Fraction(1, 1 << c) * (var_i * Fraction(c, 2) + Ig)
    assert I == Iphi + Iblk, "I decomposition"


if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
    cnt = {True: 0, False: 0}
    for trial in range(400):
        ro = trial % 2 == 0
        st = random_instance(rng, max_vars=15, read_once=ro)
        if ro:
            assert is_read_once(st.tree)
        check_instance(st, ro)
        cnt[ro] += 1
    print("all checks passed:", cnt)
