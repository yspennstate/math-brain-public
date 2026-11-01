"""Validate termdl.py on small term decision lists against the exact generic machinery:
the unfolded tree is built as a SelectorTree (leaves sharing an output block), the Walsh spectrum is
computed from the truth table (integers), and the witness-sum code length is computed exactly over all
single-root witnesses with natural (path) order. termdl.py's Monte Carlo (Jensen over owners) must be >= it
up to sampling error, and its v and I must match exactly."""
import random
import math
from fractions import Fraction
import fei_core as fc
from rodt import SelectorTree, and_table, or_table
from queue_cost import code_lengths
from termdl import TermDL


def build_unfolded(widths, outputs):
    """Return SelectorTree for the term DL with blocks of the given widths, outputs list of (kind,u)."""
    m = len(widths)
    var = 0
    blocks = []
    for w in widths:
        blocks.append(list(range(var, var + w)))
        var += w
    out_blocks = []
    tables = []
    for kind, u in outputs:
        if kind == 'dict':
            out_blocks.append([var]); tables.append([1, -1]); var += 1
        elif kind == 'and':
            out_blocks.append(list(range(var, var + u))); tables.append(and_table(u)); var += u
        elif kind == 'or':
            out_blocks.append(list(range(var, var + u))); tables.append(or_table(u)); var += u
        elif kind == 'const+1':
            out_blocks.append([var]); tables.append([1, 1]); var += 1
        elif kind == 'const-1':
            out_blocks.append([var]); tables.append([-1, -1]); var += 1
    leaves = {}
    counter = [0]

    def make_leaf(j):
        i = counter[0]; counter[0] += 1
        leaves[i] = (out_blocks[j], tables[j])
        return ('leaf', i)

    def build(k, pos):
        # testing literal pos of block k; literal true means x = +1
        if k == m:
            return make_leaf(m)
        v = blocks[k][pos]
        if pos == len(blocks[k]) - 1:
            plus = make_leaf(k)
        else:
            plus = build(k, pos + 1)
        minus = build(k + 1, 0)
        return ('node', v, plus, minus)

    return SelectorTree(build(0, 0), leaves)


if __name__ == '__main__':
    rng = random.Random(4)
    cases = [((2, 2, 2), [('dict', 1)] * 3 + [('const-1', 0)]),
             ((1, 2, 3), [('dict', 1), ('and', 2), ('or', 1), ('dict', 1)]),
             ((3, 1, 2), [('or', 2), ('dict', 1), ('const+1', 0), ('and', 1)])]
    for widths, outs in cases:
        st = build_unfolded(widths, outs)
        T = st.truth_table()
        H, I, v, masses = fc.entropy_influence_exact(T)
        res = code_lengths(st, lam=1.0)
        dl = TermDL(list(widths), outs)
        I_dl = dl.influence()
        mc = [dl.code_length_mc(random.Random(s), 'natural', 4000, exactZ=True)['total'] for s in range(3)]
        print(f"widths={widths}: exact v={float(v):.6f} termdl v={dl.v:.6f} | exact I={float(I):.6f} termdl I={I_dl:.6f}"
              f" | exact sumW={res['sumW']:.4f} minW={res['minW']:.4f} | MC (Jensen) runs {[round(x,4) for x in mc]}")
