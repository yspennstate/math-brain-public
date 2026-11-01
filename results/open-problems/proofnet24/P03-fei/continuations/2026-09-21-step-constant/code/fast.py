"""rho_0 with canonical-form memoisation: isomorphic subtrees are computed once,
so symmetric families (balanced trees, tribes) cost O(depth) not O(n^2)."""
import sys
from functools import lru_cache
import ro

def canon(t):
    """canonical hashable form; children sorted so isomorphic trees collide"""
    k = t[0]
    if k == 'const': return ('c', t[1])
    if k == 'lit':   return ('v',)            # variables are interchangeable for H, I
    a = canon(t[1]); b = canon(t[2])
    return (k,) + tuple(sorted((a, b), key=repr))

_memo = {}
def analyse_c(t):
    key = canon(t)
    v = _memo.get(key)
    if v is None:
        v = ro.analyse(t)
        _memo[key] = v
    return v

def rho0_fast(t):
    p, I, H = analyse_c(t)
    seen = {}
    rows = []
    for i in sorted(set(ro.leaves(t))):
        t0 = ro.restrict(t, i, 0); t1 = ro.restrict(t, i, 1)
        key = (canon(t0), canon(t1))
        if key in seen:                      # same orbit: same numbers
            rows.append(seen[key]); continue
        p0, I0, H0 = analyse_c(t0)
        p1, I1, H1 = analyse_c(t1)
        inf_i = abs(p1 - p0)
        if inf_i <= 1e-15: continue
        row = (inf_i, H - (H0+H1)/2.0, (H - (H0+H1)/2.0)/inf_i)
        seen[key] = row; rows.append(row)
    if not rows: return None, rows, (p, I, H)
    return min(r[2] for r in rows), rows, (p, I, H)

def ceiling(d): return (1.0 + ro.h2(d))/d if d > 0 else float('inf')

def report(name, t, out):
    r, rows, (p, I, H) = rho0_fast(t)
    if r is None: return None
    delta = max(x[0] for x in rows)
    n = len(set(ro.leaves(t)))
    line = ("%-24s n=%-6d Pr=%.4f I=%9.3f H/I=%7.4f maxInf=%.6f ceil=%9.3f rho_0=%8.4f"
            % (name, n, p, I, H/I if I else 0, delta, ceiling(delta), r))
    print(line); out.write(line+"\n"); out.flush(); sys.stdout.flush()
    return r

if __name__ == '__main__':
    out = open("fast_results.txt", "w")
    best = (0, "")
    print("=== balanced alternating AND/OR trees ===")
    for d in range(1, 21):
        for top in (True, False):
            r = report("bal d=%d %s" % (d, "AND" if top else "OR"),
                       __import__('bigfam').balanced(d, top), out)
            if r and r > best[0]: best = (r, "balanced d=%d %s" % (d, top))
    print("=== tribes AND of s ORs of width w ===")
    import bigfam
    for w in (2,3,4,5,6):
        for s in (2,4,8,12,16,24,32,48,64,96,128):
            if s*w > 20000: continue
            r = report("tribes s=%d w=%d" % (s,w), bigfam.tribes(s,w,True), out)
            if r and r > best[0]: best = (r, "tribes s=%d w=%d" % (s,w))
    msg = "\nBEST rho_0 = %.6f  at %s   (target beta(1/2) = 6.4547837)" % best
    print(msg); out.write(msg+"\n"); out.close()
