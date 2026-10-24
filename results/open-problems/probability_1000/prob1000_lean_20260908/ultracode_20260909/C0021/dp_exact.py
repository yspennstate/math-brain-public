# Exact optimal expected query count D_k of recursive 3-majority on 3^k uniform bits (zero-error).
# State = node type, canonical under S_3 at every node.  Determined nodes collapse to '+'/'-'.
import sys
from fractions import Fraction
from functools import lru_cache
sys.setrecursionlimit(10000)

def norm(children):
    """children: tuple of 3 child types -> node type (collapsed if determined)."""
    p = sum(1 for c in children if c == '+')
    m = sum(1 for c in children if c == '-')
    if p >= 2: return '+'
    if m >= 2: return '-'
    return tuple(sorted(children, key=repr))

@lru_cache(maxsize=None)
def queries(t):
    """all (t_plus, t_minus) outcomes from querying one unknown leaf inside t"""
    if t == 'u': return (('+', '-'),)
    if t in ('+', '-'): return ()
    out = set()
    for i in range(3):
        c = t[i]
        if i > 0 and t[i] == t[i-1]: continue
        for (cp, cm) in queries(c):
            tp = norm(t[:i] + (cp,) + t[i+1:])
            tm = norm(t[:i] + (cm,) + t[i+1:])
            out.add((tp, tm))
    return tuple(sorted(out, key=repr))

@lru_cache(maxsize=None)
def V(t):
    if t in ('+', '-'): return Fraction(0)
    best = None
    for (a, b) in queries(t):
        v = 1 + (V(a) + V(b)) / 2
        if best is None or v < best: best = v
    return best

def full(k):
    return 'u' if k == 0 else norm((full(k-1),)*3)

if __name__ == '__main__':
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    for k in range(1, K+1):
        t = full(k)
        d = V(t)
        print(f"k={k}: D_k = {d} = {float(d):.6f}   D_k^(1/k) = {float(d)**(1/k):.6f}   states memo={V.cache_info().currsize}", flush=True)
