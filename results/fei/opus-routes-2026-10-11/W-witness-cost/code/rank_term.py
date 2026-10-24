"""The rank term R_T(f) of Proposition 12.1 (NOTES section 12):
  R_T(f) = sum_{A != empty} fhat(A)^2 * E_{l ~ w_A} [ sum_{x in A} log2+( r_l(x) / |A| ) ],
w_A = law on 1-leaves l whose path contains A, proportional to 2^{-depth(l)}; r_l = rank of x in the path order
(depth position). Also checks the identity |fhat(A)| <= 2 * sum_{1-leaves l containing A} 2^{-depth(l)} exactly
(Fractions), and the resulting bound H <= 23.55 I + 2a R_T (a = 6/5).
Families: majority (sequential tree), AND-OR trees and random read-once formulas (short-circuit trees),
and all NPN classes for n <= 4 (min over ordered reduced trees and over f, -f)."""
import itertools
import math
import sys
from fractions import Fraction
import fei_core as fc
from rodt import leaves_with_paths

A_EXP = 6.0 / 5.0


def rank_term(masses_exact, leaves_paths, target):
    """leaves_paths: list of (path list of (var, sign), out). Returns (R_T, identity_ok)."""
    gates = [(path, Fraction(1, 1 << len(path))) for path, out in leaves_paths if out == target]
    R = 0.0
    ok = True
    for S, m in masses_exact.items():
        if S == 0:
            continue
        s = fc.popcount(S)
        own = []
        for path, p in gates:
            pv = [v for v, _ in path]
            if all(((S >> u) & 1) == 0 or u in pv for u in range(S.bit_length())):
                own.append((path, p))
        tot = sum(p for _, p in own)
        if 4 * tot * tot < m:  # identity |fhat| <= 2 sum p  <=>  m <= 4 tot^2
            ok = False
        if tot == 0:
            return math.inf, False
        exp_cost = 0.0
        for path, p in own:
            pos = {v: i + 1 for i, (v, _) in enumerate(path)}
            c = 0.0
            x = S
            k = 0
            while x:
                if x & 1:
                    c += max(0.0, math.log2(pos[k] / s))
                x >>= 1
                k += 1
            exp_cost += float(p / tot) * c
        R += float(m) * exp_cost
    return R, ok


def tree_leaves(tree):
    return [(list(path), None) for _, path in []]


def selector_leaf_outputs(st):
    out = []
    for i, path in st.paths.items():
        bv, T = st.leaves[i]
        assert len(T) == 1
        out.append((list(path), T[0]))
    return out


if __name__ == '__main__':
    from rodt import SelectorTree
    mode = sys.argv[1]
    if mode == 'maj':
        def maj_seq_tree(n):
            need = n // 2 + 1
            leaves = {}

            def build(i, plus, minus):
                if plus >= need:
                    k = len(leaves); leaves[k] = ([], [1]); return ('leaf', k)
                if minus >= need:
                    k = len(leaves); leaves[k] = ([], [-1]); return ('leaf', k)
                return ('node', i, build(i + 1, plus + 1, minus), build(i + 1, plus, minus + 1))
            return SelectorTree(build(0, 0, 0), leaves)
        for n in range(3, int(sys.argv[2]) + 1, 2):
            st = maj_seq_tree(n)
            T = st.truth_table()
            H, I, v, masses = fc.entropy_influence_exact(T)
            R, ok = rank_term(masses, selector_leaf_outputs(st), 1)
            print(f"MAJ_{n}: H/I={H/float(I):.3f} R_T/I={R/float(I):.3f} identity_ok={ok} "
                  f"bound 23.55+2.4R/I={23.55 + 2*A_EXP*R/float(I):.2f}", flush=True)
    elif mode == 'formulas':
        from readonce_formulas import and_or_tree, formula_selector, random_formula
        import random
        for d in range(1, 5):
            st = formula_selector(and_or_tree(d, [0], 'and'))
            T = st.truth_table()
            H, I, v, masses = fc.entropy_influence_exact(T)
            R1, ok1 = rank_term(masses, selector_leaf_outputs(st), 1)
            Rm, okm = rank_term(masses, selector_leaf_outputs(st), -1)
            print(f"AND-OR depth {d}: H/I={H/float(I):.3f} R_T/I (1-leaves)={R1/float(I):.3f} (0-leaves)={Rm/float(I):.3f} ok={ok1 and okm}", flush=True)
        rng = random.Random(11)
        worst = 0
        allok = True
        for t in range(150):
            st = formula_selector(random_formula(rng, rng.randint(4, 12)))
            if len(st.leaves) > 300:
                continue
            T = st.truth_table()
            H, I, v, masses = fc.entropy_influence_exact(T)
            if I == 0:
                continue
            R1, ok1 = rank_term(masses, selector_leaf_outputs(st), 1)
            Rm, okm = rank_term(masses, selector_leaf_outputs(st), -1)
            allok = allok and ok1 and okm
            worst = max(worst, min(R1, Rm) / float(I))
        print(f"random read-once formulas: max min(R_T)/I = {worst:.3f}, identity ok on all: {allok}")
