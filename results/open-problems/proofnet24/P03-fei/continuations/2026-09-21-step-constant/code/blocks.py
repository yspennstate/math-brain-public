"""The B/I-extremal read-once trees are ANDs of a repeated block. Push that family
to the largest n an exact 2^n spectrum allows, and see where B/I is heading."""
import numpy as np, sys
import ro
from erasure import spectrum, stats
from erasure_ro import truth

def blk_or(w, ctr):       # OR of w fresh variables
    n = None
    for _ in range(w):
        l = ro.lit(ctr[0]); ctr[0] += 1
        n = l if n is None else ro.OR(n, l)
    return n

def blk_motif(ctr):       # ((x|x)&x)|(x&x)  -- the motif the search kept
    a = ro.lit(ctr[0]); ctr[0]+=1; b = ro.lit(ctr[0]); ctr[0]+=1
    c = ro.lit(ctr[0]); ctr[0]+=1; d = ro.lit(ctr[0]); ctr[0]+=1
    e = ro.lit(ctr[0]); ctr[0]+=1
    return ro.OR(ro.AND(ro.OR(a,b), c), ro.AND(d,e))

def blk_motif4(ctr):      # ((x|x)&x)|x
    a = ro.lit(ctr[0]); ctr[0]+=1; b = ro.lit(ctr[0]); ctr[0]+=1
    c = ro.lit(ctr[0]); ctr[0]+=1; d = ro.lit(ctr[0]); ctr[0]+=1
    return ro.OR(ro.AND(ro.OR(a,b), c), d)

def andk(mk, k):
    ctr = [0]; t = None
    for _ in range(k):
        b = mk(ctr)
        t = b if t is None else ro.AND(t, b)
    return t, ctr[0]

def row(name, t, n):
    f = truth(t, n)
    if f.sum() in (0, 1 << n): return None
    mu = spectrum(f, n); I, H, B = stats(mu, n)
    if I <= 1e-12: return None
    print("%-26s n=%-3d Pr=%.5f I=%8.4f H/I=%7.4f B=%8.4f  B/I=%8.5f"
          % (name, n, float(mu[0])**0, I, H/I, B, B/I))
    sys.stdout.flush()
    return B/I

if __name__ == '__main__':
    best = 0.0
    print("=== AND of k copies of ((x|x)&x)|(x&x)  (5 vars per block) ===")
    for k in range(1, 5):
        t, n = andk(blk_motif, k)
        if n > 22: break
        r = row("motif5 x%d" % k, t, n)
        if r: best = max(best, r)
    print("=== AND of k copies of ((x|x)&x)|x  (4 vars per block) ===")
    for k in range(1, 6):
        t, n = andk(blk_motif4, k)
        if n > 22: break
        r = row("motif4 x%d" % k, t, n)
        if r: best = max(best, r)
    print("=== AND of k ORs of width w (tribes, for reference) ===")
    for w in (2, 3):
        for k in range(2, 12):
            if k*w > 22: break
            ctr=[0]; t=None
            for _ in range(k):
                b = blk_or(w, ctr); t = b if t is None else ro.AND(t, b)
            r = row("tribes w=%d x%d" % (w, k), t, ctr[0])
            if r: best = max(best, r)
    print("\nbest B/I over these families: %.6f" % best)
