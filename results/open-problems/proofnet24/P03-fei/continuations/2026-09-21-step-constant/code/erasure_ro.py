"""B/I over read-once AND/OR trees, by explicit spectrum (n <= 20).
Does the class that must contain rho_0 >= 6.4548 also push the erasure ratio up?
Uses B = n H(S) - sum_i H(S_{-i}), which is the same quantity computed a second way."""
import numpy as np, itertools, sys
import ro, control
from erasure import spectrum, stats
from fast import canon
from beam import grow

def truth(t, n):
    idx = np.arange(1 << n)
    def ev(node):
        k = node[0]
        if k == 'const': return np.full(1 << n, node[1], dtype=np.int8)
        if k == 'lit':
            v = ((idx >> node[1]) & 1).astype(np.int8)
            return (1 - v) if node[2] else v
        a = ev(node[1]); b = ev(node[2])
        return (a & b) if k == 'and' else (a | b)
    return ev(t)

def B_two_ways(mu, n):
    """B as sum_i H(S_i|S_-i), and again as n H - sum_i H(S_-i)"""
    I, H, B1 = stats(mu, n)
    idx = np.arange(len(mu))
    B2 = n*H
    for i in range(n):
        bit = (idx >> i) & 1
        m = mu[bit == 0] + mu[bit == 1]
        nz = m > 0
        B2 -= float(-(m[nz]*np.log2(m[nz])).sum())
    return I, H, B1, B2

def beam_maxBI(nmax=18, beam=25):
    frontier = [ro.lit(0)]; best = (0.0, None, 0, 0, 0)
    for n in range(2, nmax+1):
        cand = {}
        for t in frontier:
            for c in grow(t, n-1):
                k = canon(c)
                if k in cand: continue
                f = truth(c, n)
                if f.sum() in (0, 1 << n): continue
                mu = spectrum(f, n)
                I, H, B1, B2 = B_two_ways(mu, n)
                if I <= 1e-12: continue
                cand[k] = (B1/I, c, I, H, B1, abs(B1-B2))
        if not cand: break
        ranked = sorted(cand.values(), key=lambda z: -z[0])
        frontier = [z[1] for z in ranked[:beam]]
        b = ranked[0]
        if b[0] > best[0]: best = (b[0], b[1], b[2], b[3], b[4])
        print("n=%-3d trees=%-6d max B/I = %.6f   (I=%.4f H=%.4f H/I=%.4f B=%.4f)  two-way gap %.2e"
              % (n, len(cand), b[0], b[2], b[3], b[3]/b[2], b[4], b[5]))
        sys.stdout.flush()
    return best

if __name__ == '__main__':
    print("=== read-once trees, beam search on B/I ===")
    beam_maxBI(int(sys.argv[1]) if len(sys.argv) > 1 else 18)
