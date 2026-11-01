# Heuristic policy for depth K, evaluated EXACTLY (Fractions) over its reachable states -> rigorous upper bound on D_K.
# Policy: at the root (depth K) with children types c1,c2,c3 of depth K-1 (whose exact optimal values V are known from
# dp_exact for K-1 <= 3), consider queries that are V-optimal inside a child, and pick the child by one-step lookahead
# with the heuristic root value R(t) = value of the 'lottery game' in which child i can be fully learned at cost V(c_i)
# and has posterior q_i = P(c_i = +).
import sys, time
from fractions import Fraction
from functools import lru_cache
from dp_exact import V, queries, full, norm
sys.setrecursionlimit(100000)

@lru_cache(maxsize=None)
def q(t):
    """posterior probability that node type t evaluates to +"""
    if t == '+': return 1.0
    if t == '-': return 0.0
    if t == 'u': return 0.5
    a, b, c = (q(x) for x in t)
    return a*b*c + a*b*(1-c) + a*(1-b)*c + (1-a)*b*c

def lottery(ws, qs):
    """optimal expected cost to determine maj of 3 independent lotteries, lottery i costs ws[i], P(+)=qs[i]."""
    @lru_cache(maxsize=None)
    def g(state):  # state: tuple of 3 entries in {None, 0, 1}
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

@lru_cache(maxsize=None)
def R(t):
    if t in ('+', '-'): return 0.0
    ws = tuple(float(V(c)) for c in t)
    qs = tuple(q(c) for c in t)
    return lottery(ws, qs)

@lru_cache(maxsize=None)
def child_opt_moves(c):
    """V-optimal query outcomes inside child type c (all ties kept)"""
    if c == 'u': return (('+', '-'),)
    opts = [(1 + (V(a)+V(b))/2, a, b) for (a, b) in queries(c)]
    m = min(o[0] for o in opts)
    return tuple((a, b) for v, a, b in opts if v == m)

@lru_cache(maxsize=None)
def policy(t):
    best = None
    for i in range(3):
        c = t[i]
        if c in ('+', '-'): continue
        if i > 0 and t[i] == t[i-1]: continue
        for (cp, cm) in child_opt_moves(c):
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
    e = E(full(K))
    print(f"K={K}: heuristic policy exact cost = {e} = {float(e):.6f}; reachable states = {E.cache_info().currsize}; "
          f"cost^(1/K) = {float(e)**(1/K):.6f}; time {time.time()-t0:.1f}s", flush=True)
    if K <= 3:
        print(f"   optimum D_{K} = {float(V(full(K))):.6f}; composition bound D_{K-1}^(K/(K-1)) = {float(V(full(K-1)))**(K/(K-1)):.6f}")
