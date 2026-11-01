"""H0024: where the factor four in arXiv:2607.27082 comes from, and what the true constant is.

Their Theorem 3.1: extinction a.s. if limsup n P(D* >= n) < 1/(2 E eta), survival with positive
probability if liminf n P(D-> >= n) > 1/(E eta). Since P(D* >= n) ~ 2 P(D-> >= n), the two constants
differ by four.

Model here: sites of Z carry i.i.d. reaches with P(R >= n) = min(1, c/n). Site 0 starts activated; an
activated site at x activates [x - L_x, x + R_x]; the activated set is an interval that grows until it
closes. Only the sites added at the previous step can extend it (the older ones are already known not
to), which is what makes the simulation O(final size).

Three variants:
  one   : L = 0                (the one-sided firework their survival bound uses)
  indep : L an independent copy of R
  same  : L = R                (the bidirectional firework with a single radius, which is what using
                                D* on both sides amounts to)
The one-sided threshold is c = 1: writing g_k for the growth at step k, the growth ratio U = g_{k+1}/g_k
has P(U < u) = (u/(1+u))^c in the limit of large g, so E[log U] = psi(c) + gamma, which is zero exactly
at c = 1 (psi(1) = -gamma).  The question is whether the two-sided variants move that threshold.
"""
import numpy as np, sys
from math import log

def run(c, variant, nmax, trials, rng):
    """returns the fraction of trials whose activated interval reaches size >= nmax"""
    hit = 0
    for _ in range(trials):
        A = B = 0
        new = np.zeros(1, dtype=np.int64)      # positions whose reaches are not yet drawn
        while True:
            k = new.size
            R = np.floor(c / rng.random(k)).astype(np.int64)
            if variant == 'one':
                L = np.zeros(k, dtype=np.int64)
            elif variant == 'indep':
                L = np.floor(c / rng.random(k)).astype(np.int64)
            else:
                L = R
            nB = max(B, int((new + R).max()))
            nA = min(A, int((new - L).min()))
            if nA == A and nB == B:
                break
            new = np.concatenate((np.arange(B + 1, nB + 1, dtype=np.int64),
                                  np.arange(nA, A, dtype=np.int64)))
            A, B = nA, nB
            if B - A + 1 >= nmax:
                hit += 1
                break
    return hit / trials

if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
    trials = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    rng = np.random.default_rng(31)
    print(f"survival proxy: P(interval reaches size {nmax:g}), {trials} trials")
    print(f"{'c':>6} " + " ".join(f"{v:>9}" for v in ('one', 'indep', 'same')))
    for c in (0.25, 0.5, 0.75, 0.9, 1.0, 1.1, 1.25, 1.5, 2.0):
        row = [run(c, v, nmax, trials, rng) for v in ('one', 'indep', 'same')]
        print(f"{c:>6.2f} " + " ".join(f"{r:>9.3f}" for r in row))
