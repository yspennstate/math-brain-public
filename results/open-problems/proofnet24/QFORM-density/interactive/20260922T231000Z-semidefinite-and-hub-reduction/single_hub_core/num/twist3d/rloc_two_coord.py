# The local maximal functional of Proposition 5.4 when q^ shares only two coordinates with w:
# w = (e1 + e2)/sqrt2, q^ = (e1 - e2)/sqrt2 (v = (e3 + e4)/sqrt2 satisfies the leverage condition of (0.1)).
# X1, X2 are combs of N teeth of width 1/N at spacings a, b of order N^{-1/2} with irrational ratio; then (L, P) is the
# rotated product f1 x f2, of density 1 on disjoint squares, and int dp sup_{|l - l0| <= 1} rho_{L,P}(l, p) is the length
# of the union of the P-projections of the squares whose centres lie in the window. Computed exactly (interval union).
import sys, math
import numpy as np

def rloc(N, c1=1.0, c2=math.sqrt(2) * 0.7):
    a, b, h = c1 / math.sqrt(N), c2 / math.sqrt(N), 1.0 / N
    j = np.arange(N)[:, None]; k = np.arange(N)[None, :]
    lc = (j * a + k * b + h) / math.sqrt(2)                   # centre of each square in L
    l0 = 0.5 * (lc.min() + lc.max())
    sel = np.abs(lc - l0) <= 1.0
    pc = ((j * a - k * b) / math.sqrt(2))[sel]                 # centre of each square in P (the centre offset cancels)
    half = h / math.sqrt(2)                                    # a square of side h at 45 degrees projects to length sqrt2 h
    iv = np.sort(pc)
    lo, hi = iv - half, iv + half
    tot = 0.0; cur_lo, cur_hi = lo[0], hi[0]
    for x, y in zip(lo[1:], hi[1:]):
        if x > cur_hi:
            tot += cur_hi - cur_lo; cur_lo, cur_hi = x, y
        else:
            cur_hi = max(cur_hi, y)
    tot += cur_hi - cur_lo
    return tot, int(sel.sum()), pc.max() - pc.min()

if __name__ == "__main__":
    for N in (64, 256, 1024, 4096):
        tot, cnt, rng = rloc(N)
        print("N=%5d  squares in the window %7d  P-range %.2f  local functional %.3f  ratio to sqrt(N) %.3f"
              % (N, cnt, rng, tot, tot / math.sqrt(N)), flush=True)
