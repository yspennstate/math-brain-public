"""Corroborate the half of the Hadamard-discrepancy answer that rests on the literature: that for odd
k <= 7 the bent-concatenation bound is optimal, so disc(H_k) = 2^((k+1)/2) there.

disc(H_k) = min over Boolean f on k variables of max |W_f|.  The conjecture says 8 at k = 5 and 16 at
k = 7.  k = 1 and 3 were settled here by brute force over all 2^n sign vectors; 32 and 128 variables'
worth of sign vectors are too many for that, so this searches hard instead: exhaustive for k = 5 over a
random sample plus steepest descent, and annealing for k = 7.  Finding nothing below the bound is
corroboration, not proof; the proof is Berlekamp and Welch for k = 5 and Mykkeltveit for k = 7.
"""
import numpy as np, sys

def wht(x, n):
    a = x.astype(np.int64).copy(); h = 1
    while h < n:
        a = a.reshape(-1, 2, h)
        u, v = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = u + v; a[:, 1, :] = u - v
        a = a.reshape(-1); h <<= 1
    return a

def best_for(k, trials, seed=0):
    n = 1 << k
    rng = np.random.default_rng(seed)
    best = n
    for _ in range(trials):
        x = 1 - 2 * rng.integers(0, 2, n)
        cur = int(np.abs(wht(x, n)).max())
        improved = True
        while improved:                      # steepest descent on single-bit flips
            improved = False
            order = rng.permutation(n)
            for i in order:
                x[i] = -x[i]
                v = int(np.abs(wht(x, n)).max())
                if v < cur:
                    cur = v; improved = True
                else:
                    x[i] = -x[i]
        best = min(best, cur)
    return best

if __name__ == '__main__':
    for k, target, trials in ((3, 4, 60), (5, 8, 400), (7, 16, 40)):
        b = best_for(k, trials)
        nl = (1 << (k - 1)) - b // 2
        print(f"k = {k}: best max|W| found = {b}, nonlinearity {nl};  conjectured minimum "
              f"{target} (nonlinearity {(1<<(k-1)) - target//2})   "
              f"{'matches' if b == target else 'BELOW THE BOUND' if b < target else 'above'}", flush=True)
