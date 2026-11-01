"""Read-once AND/OR formulas through their short-circuit decision trees (gates = 1-leaf paths, M = 1 or 2).
Exact spectrum from the truth table; exact queue-law code lengths (path order) via queue_cost.code_lengths.
EVIDENCE for where the witness route stands on read-once formulas (a target example of C020)."""
import random
import math
import sys
import fei_core as fc
from rodt import SelectorTree
from queue_cost import code_lengths


def sc_tree(node, on_true, on_false):
    kind = node[0]
    if kind == 'lit':
        _, var, pos = node
        # literal true when x_var == +1 (pos) or -1 (neg)
        return ('node', var, on_true, on_false) if pos else ('node', var, on_false, on_true)
    ch = node[1]
    if len(ch) == 1:
        return sc_tree(ch[0], on_true, on_false)
    rest = (kind, ch[1:])
    if kind == 'and':
        return sc_tree(ch[0], sc_tree(rest, on_true, on_false), on_false)
    else:
        return sc_tree(ch[0], on_true, sc_tree(rest, on_true, on_false))


def number(tree, leaves, consts):
    if tree[0] == 'leaf':
        i = len(leaves)
        leaves[i] = ([], [tree[1]])
        return ('leaf', i)
    return ('node', tree[1], number(tree[2], leaves, consts), number(tree[3], leaves, consts))


def formula_selector(formula):
    t = sc_tree(formula, ('leaf', 1), ('leaf', -1))
    leaves = {}
    t = number(t, leaves, None)
    return SelectorTree(t, leaves)


def and_or_tree(depth, var=[0], top='and'):
    if depth == 0:
        v = var[0]; var[0] += 1
        return ('lit', v, True)
    sub = 'or' if top == 'and' else 'and'
    return (top, [and_or_tree(depth - 1, var, sub), and_or_tree(depth - 1, var, sub)])


def random_formula(rng, nlits):
    lits = [('lit', i, rng.random() < 0.5) for i in range(nlits)]
    items = lits[:]
    while len(items) > 1:
        k = rng.randint(2, min(3, len(items)))
        rng.shuffle(items)
        grp, items = items[:k], items[k:]
        items.append((rng.choice(['and', 'or']), grp))
    return items[0]


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'andor':
        for d in range(1, 5):
            f = and_or_tree(d, [0], 'and')
            st = formula_selector(f)
            res = code_lengths(st, lam=1.0)
            print(f"AND-OR tree depth {d} (n={2**d}): leaves={len(st.leaves)} H/I={res['H']/res['I']:.3f} "
                  f"minW/I={res['minW']/res['I']:.3f} sumW/I={res['sumW']/res['I']:.3f} I={res['I']:.4f}", flush=True)
    else:
        rng = random.Random(int(sys.argv[2]))
        worst = {}
        for t in range(int(sys.argv[3])):
            nl = rng.randint(4, 12)
            f = random_formula(rng, nl)
            st = formula_selector(f)
            if len(st.leaves) > 400:
                continue
            res = code_lengths(st, lam=1.0)
            if res['I'] == 0:
                continue
            for k in ('H', 'minW', 'sumW'):
                r = res[k] / res['I']
                if r > worst.get(k, (0,))[0]:
                    worst[k] = (r, nl, len(st.leaves))
        print({k: (round(v[0], 3), v[1], v[2]) for k, v in worst.items()})
