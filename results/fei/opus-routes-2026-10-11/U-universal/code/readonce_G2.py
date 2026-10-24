"""Read-once AND/OR formulas: beam search for large H/I storing the tree, then compute G = sum_i Delta_i U exactly
via the composition recursion (restriction of a leaf simplifies the formula).  EVIDENCE (float logs)."""
import math, sys, itertools
from compose_rec import compose_step, X, AND, OR
sys.setrecursionlimit(10000)
GATES = {'A': AND, 'O': OR}
LEAF = ('x',)

def stats(tree, restr=None, path=()):
    """restr: (path_tuple, value) restricting one leaf.  Returns dict or ('const', v)."""
    if tree[0] == 'x':
        if restr is not None and restr[0] == path: return ('const', restr[1])
        return dict(X, H=0.0, U=0.0, I=1.0, Var=1.0)
    g, a, b = tree
    on_a = restr is not None and restr[0][:len(path) + 1] == path + (0,)
    on_b = restr is not None and restr[0][:len(path) + 1] == path + (1,)
    sa = stats(a, restr if on_a else None, path + (0,)) if on_a else cache_stats(a)
    sb = stats(b, restr if on_b else None, path + (1,)) if on_b else cache_stats(b)
    for s, other in ((sa, sb), (sb, sa)):
        if isinstance(s, tuple):
            v = s[1]
            if g == 'A': return ('const', 1) if v == 1 else other
            else: return ('const', -1) if v == -1 else other
    return compose_step(GATES[g], [sa, sb])

_cache = {}
def cache_stats(tree):
    k = id(tree)
    if k not in _cache: _cache[k] = (tree, stats(tree))
    return _cache[k][1]

def leaves(tree, path=()):
    if tree[0] == 'x': yield path; return
    yield from leaves(tree[1], path + (0,)); yield from leaves(tree[2], path + (1,))

def Gratio(tree):
    s = cache_stats(tree); U = s['U']; I = s['I']; G = 0.0; locs = []
    for lp in leaves(tree):
        vals = []
        for v in (1, -1):
            r = stats(tree, (lp, v))
            vals.append(0.0 if isinstance(r, tuple) else r['U'])
        d = U - 0.5 * sum(vals); G += d
    return G / I, s

if __name__ == "__main__":
    NB = 80
    def bin_of(mu): return min(NB - 1, int((mu + 1) / 2 * NB))
    pop = {bin_of(0.0): (LEAF, dict(X, H=0.0, U=0.0, I=1.0, Var=1.0), 1)}
    for rnd in range(11):
        items = list(pop.values()); new = dict(pop)
        for (ta, sa, na), (tb, sb, nb) in itertools.product(items, items):
            if na + nb > 2100: continue
            for gname in 'AO':
                try: r = compose_step(GATES[gname], [sa, sb])
                except ZeroDivisionError: continue
                if r['Var'] < 1e-6: continue
                k = bin_of(r['mu']); ratio = r['H'] / r['I']
                if k not in new or ratio > new[k][1]['H'] / new[k][1]['I']: new[k] = ((gname, ta, tb), r, na + nb)
        pop = new
        tree, s, size = max(pop.values(), key=lambda e: e[1]['H'] / e[1]['I'])
        _cache.clear()
        gi, s2 = Gratio(tree)
        print('round', rnd, 'size', size, 'H/I=%.4f U/I=%.4f G/I=%.4f' % (s['H'] / s['I'], s['U'] / s['I'], gi), flush=True)
