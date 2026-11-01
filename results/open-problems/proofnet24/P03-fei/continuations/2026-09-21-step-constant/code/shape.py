"""What does the B/I-extremal read-once tree look like?  Print its shape per n."""
import sys
import ro
from erasure import spectrum, stats
from erasure_ro import truth
from fast import canon
from beam import grow

def show(t):
    k = t[0]
    if k == 'lit': return 'x'
    if k == 'const': return str(t[1])
    op = '&' if k == 'and' else '|'
    return '(' + show(t[1]) + op + show(t[2]) + ')'

def profile(t):
    """multiset of leaf depths, and the gate pattern by level"""
    out = []
    def go(node, d):
        if node[0] == 'lit': out.append(d); return
        go(node[1], d+1); go(node[2], d+1)
    go(t, 0)
    from collections import Counter
    return sorted(Counter(out).items())

def run(nmax=16, beam=25):
    frontier = [ro.lit(0)]
    for n in range(2, nmax+1):
        cand = {}
        for t in frontier:
            for c in grow(t, n-1):
                k = canon(c)
                if k in cand: continue
                f = truth(c, n)
                if f.sum() in (0, 1 << n): continue
                mu = spectrum(f, n); I, H, B = stats(mu, n)
                if I <= 1e-12: continue
                cand[k] = (B/I, c)
        if not cand: break
        ranked = sorted(cand.values(), key=lambda z: -z[0])
        frontier = [z[1] for z in ranked[:beam]]
        r, t = ranked[0]
        if n >= 10:
            print("n=%-3d B/I=%.6f  depths=%s" % (n, r, profile(t)))
            print("     %s" % show(t))
            sys.stdout.flush()

if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 16)
