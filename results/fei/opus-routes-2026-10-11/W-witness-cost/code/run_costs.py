"""Evidence runs: queue-law code lengths on random selector trees and on the obstruction family N1.
Usage: python run_costs.py random SEED COUNT | python run_costs.py n1 DMAX
"""
import sys
import json
import random
import math
from rodt import *
from queue_cost import *
from test_spectrum import random_instance


def complete_tree(vars_iter, depth):
    if depth == 0:
        return ('leaf', None)
    v = next(vars_iter)
    return ('node', v, complete_tree(vars_iter, depth - 1), complete_tree(vars_iter, depth - 1))


def renumber(tree, counter):
    if tree[0] == 'leaf':
        i = counter[0]
        counter[0] += 1
        return ('leaf', i)
    return ('node', tree[1], renumber(tree[2], counter), renumber(tree[3], counter))


def n1_family(D, w):
    """x_0 root; plus side: complete read-once depth-D tree with OR_w leaves; minus side: AND_w leaves."""
    it = iter(range(1, 10 ** 6))
    plus = complete_tree(it, D)
    minus = complete_tree(it, D)
    tree = renumber(('node', 0, plus, minus), [0])
    nctrl = 1 + 2 * ((1 << D) - 1)
    leaves = {}
    nxt = nctrl
    nplus = 1 << D
    for i in range(2 * nplus):
        T = or_table(w) if i < nplus else and_table(w)
        leaves[i] = (list(range(nxt, nxt + w)), T)
        nxt += w
    return SelectorTree(tree, leaves)


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'random':
        seed, count = int(sys.argv[2]), int(sys.argv[3])
        rng = random.Random(seed)
        worst = {}
        rows = []
        for t in range(count):
            ro = t % 2 == 0
            st = random_instance(rng, max_vars=16, read_once=ro)
            res = code_lengths(st, lam=1.0)
            own = owner_code_length(st, res, best_owner(res))
            I = res['I']
            if I == 0:
                continue
            row = dict(ro=ro, H_I=res['H'] / I, minW_I=res['minW'] / I, sumW_I=res['sumW'] / I,
                       owner_I=own / I, I=I, n=st.n)
            rows.append(row)
            for k in ('H_I', 'minW_I', 'sumW_I', 'owner_I'):
                key = (ro, k)
                if key not in worst or row[k] > worst[key]:
                    worst[key] = row[k]
        print(json.dumps({f"{'RO' if k[0] else 'DT'}:{k[1]}": round(v, 4) for k, v in worst.items()}, indent=1))
    elif mode == 'n1':
        Dmax = int(sys.argv[2])
        for D in range(1, Dmax + 1):
            w = max(1, math.ceil(math.log2(max(D, 2))))
            st = n1_family(D, w)
            res = code_lengths(st, lam=1.0)
            # optimize the global lambda for minW over a grid (EVIDENCE)
            best = None
            for e in range(-4, 2 * D + 6):
                lam = 2.0 ** e
                r2 = code_lengths(st, lam=lam)
                if best is None or r2['minW'] < best[0]:
                    best = (r2['minW'], lam)
            own = owner_code_length(st, res, best_owner(res))
            print(f"D={D} w={w} I={res['I']:.4f} H/I={res['H']/res['I']:.3f} "
                  f"minW(lam=1)/I={res['minW']/res['I']:.3f} best-lam minW/I={best[0]/res['I']:.3f} (lam={best[1]}) "
                  f"sumW(lam=1)/I={res['sumW']/res['I']:.3f} owner/I={own/res['I']:.3f}", flush=True)
