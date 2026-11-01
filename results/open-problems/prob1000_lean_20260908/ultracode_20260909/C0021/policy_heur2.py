# Generic version of policy_heur.py: exact V for depth <= 3, and for depth d >= 4 the child value is the exact cost
# E_{d}(c) of the heuristic policy itself (recursively), the child move is the policy's move.  Exact rational
# evaluation of the resulting depth-K policy => rigorous upper bound on D_K.
import sys, time
from fractions import Fraction
from functools import lru_cache
from dp_exact import V, queries, full, norm
sys.setrecursionlimit(1000000)
EXACT_DEPTH = 3

@lru_cache(maxsize=None)
def depth(t):
    if t == 'u': return 0
    for c in t:
        if c not in ('+', '-'): return 1 + depth(c)
    raise ValueError

@lru_cache(maxsize=None)
def q(t):
    if t == '+': return 1.0
    if t == '-': return 0.0
    if t == 'u': return 0.5
    a, b, c = (q(x) for x in t)
    return a*b*c + a*b*(1-c) + a*(1-b)*c + (1-a)*b*c

@lru_cache(maxsize=None)
def lottery(ws, qs):
    @lru_cache(maxsize=None)
    def g(state):
        p = sum(1 for s in state if s == 1); m = sum(1 for s in state if s == 0)
        if p >= 2 or m >= 2: return 0.0
        best = float('inf')
        for i in range(3):
            if state[i] is None:
                sp = list(state); sp[i] = 1; sm = list(state); sm[i] = 0
                v = ws[i] + qs[i]*g(tuple(sp)) + (1-qs[i])*g(tuple(sm))
                if v < best: best = v
        return best
    init = tuple(None if 0 < qs[i] < 1 else int(qs[i] > 0.5) for i in range(3))
    return g(init)

def val(c):
    """child value: exact optimum for depth <= EXACT_DEPTH, else the heuristic policy's own exact cost"""
    if c in ('+', '-'): return 0.0
    return float(V(c)) if depth(c) <= EXACT_DEPTH else float(E(c))

@lru_cache(maxsize=None)
def R(t):
    if t in ('+', '-'): return 0.0
    return lottery(tuple(val(c) for c in t), tuple(q(c) for c in t))

@lru_cache(maxsize=None)
def child_moves(c):
    if c == 'u': return (('+', '-'),)
    if depth(c) <= EXACT_DEPTH:
        opts = [(1 + (V(a)+V(b))/2, a, b) for (a, b) in queries(c)]
        m = min(o[0] for o in opts)
        return tuple((a, b) for v, a, b in opts if v == m)
    return (policy(c),)

@lru_cache(maxsize=None)
def policy(t):
    best = None
    for i in range(3):
        c = t[i]
        if c in ('+', '-'): continue
        if i > 0 and t[i] == t[i-1]: continue
        for (cp, cm) in child_moves(c):
            tp = norm(t[:i] + (cp,) + t[i+1:]); tm = norm(t[:i] + (cm,) + t[i+1:])
            h = 1 + (R(tp) + R(tm))/2
            if best is None or h < best[0] - 1e-12: best = (h, tp, tm)
    return best[1], best[2]

@lru_cache(maxsize=None)
def E(t):
    if t in ('+', '-'): return Fraction(0)
    a, b = policy(t)
    return 1 + (E(a) + E(b))/2

if __name__ == '__main__':
    K = int(sys.argv[1])
    t0 = time.time()
    for k in range(1, K+1):
        e = E(full(k))
        print(f"K={k}: policy exact cost = {e} = {float(e):.6f}; cost^(1/K) = {float(e)**(1/k):.6f}; "
              f"E-states = {E.cache_info().currsize}; time {time.time()-t0:.1f}s", flush=True)
