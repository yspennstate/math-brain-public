"""rho_0 on structured read-once families at large n, plus the ceiling
   rho_0(f) <= (1 + h(delta))/delta,  delta = max_i Inf_i
which follows from Delta_i H <= 1 + h(Inf_i) (JS <= 1 bit, concavity)."""
import sys
from math import log2
import ro

def ceiling(delta):
    return (1.0 + ro.h2(delta))/delta if delta > 0 else float('inf')

def balanced(d, top_and=True):
    """alternating AND/OR balanced tree of depth d -> n = 2^d leaves"""
    ctr = [0]
    def go(k, is_and):
        if k == 0:
            i = ctr[0]; ctr[0] += 1
            return ro.lit(i)
        L = go(k-1, not is_and); R = go(k-1, not is_and)
        return ro.AND(L, R) if is_and else ro.OR(L, R)
    return go(d, top_and)

def tribes(s, w, outer_and=True):
    """AND of s ORs of w fresh variables (or the dual)"""
    ctr = [0]
    def chain(k, is_and):
        node = None
        for _ in range(k):
            leaf = ro.lit(ctr[0]); ctr[0] += 1
            node = leaf if node is None else (ro.AND(node, leaf) if is_and else ro.OR(node, leaf))
        return node
    blocks = [chain(w, not outer_and) for _ in range(s)]
    t = blocks[0]
    for b in blocks[1:]:
        t = ro.AND(t, b) if outer_and else ro.OR(t, b)
    return t

def report(name, t):
    r, rows, (p, I, H) = ro.rho0(t)
    if r is None: return None
    delta = max(x[1] for x in rows)
    n = len(set(ro.leaves(t)))
    print("%-26s n=%-5d Pr=%.4f  I=%8.3f  H/I=%7.4f  maxInf=%.5f  ceiling=%8.3f  rho_0=%8.4f"
          % (name, n, p, I, H/I if I else 0, delta, ceiling(delta), r))
    sys.stdout.flush()
    return r

if __name__ == '__main__':
    print("=== balanced alternating AND/OR trees ===")
    best = 0
    for d in range(1, 15):
        for top in (True, False):
            r = report("balanced d=%d %s" % (d, "AND-top" if top else "OR-top"), balanced(d, top))
            if r: best = max(best, r)
    print("\n=== tribes: AND of s ORs of width w ===")
    for w in (2, 3, 4, 5):
        for s in (2, 4, 8, 12, 16, 24, 32, 48, 64):
            if s*w > 4000: continue
            r = report("tribes s=%d w=%d" % (s, w), tribes(s, w, True))
            if r: best = max(best, r)
    print("\nbest rho_0 over these families: %.6f   (target: beta(1/2) = 6.4547837)" % best)
