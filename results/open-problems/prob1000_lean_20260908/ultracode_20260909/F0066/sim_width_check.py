# Independent sanity check for F0066 (Janson Conj 20.6 / 21.6).
import os
KINDS = os.environ.get('KINDS','geometric,zipf2.5,zipf3').split(',')
SIZES = [int(x) for x in os.environ.get('SIZES','1000,4000,16000').split(',')]
# Samples size-conditioned critical Bienayme trees by the cycle lemma
# (Lukasiewicz path + Vervaat rotation) for three offspring laws:
#   geometric (sigma^2 finite), a Zipf law with P(k) ~ k^{-5/2} (alpha=3/2 stable domain),
#   and a law with P(k) ~ k^{-3}, whose variance is infinite only logarithmically.
# For each tree it records the width, the depth of a uniform node, and
# |n_T|_2^2 / n (the quantity ABHK's Corollary 5.3 / Prop 2.3 says tends to infinity).
import numpy as np, sys, time
rng = np.random.default_rng(20260909)

def crit_law(kind, K=2_000_000):
    k = np.arange(K+1, dtype=float)
    if kind == 'geometric':
        p = 0.5**(k+1)
    elif kind == 'zipf2.5':
        p = np.zeros(K+1); p[1:] = k[1:]**-2.5
        p[0] = 1.0  # placeholder, fixed below
    elif kind == 'zipf3':
        p = np.zeros(K+1); p[1:] = k[1:]**-3.0
        p[0] = 1.0
    if kind != 'geometric':
        # choose p0 so that the law is critical: mean = 1
        # p = (p0, c k^-a ...): mean = c*sum k^{1-a}, total = p0 + c*sum k^-a = 1
        s1 = (k[1:]**(1.0)*p[1:]).sum(); s0 = p[1:].sum()
        c = 1.0/s1; p0 = 1 - c*s0
        p[1:] *= c; p[0] = p0
    p /= p.sum()
    return p

def sample_tree_widths(p, n, reps):
    cdf = np.cumsum(p)
    out = []
    tries = 0
    while len(out) < reps:
        tries += 1
        xi = np.searchsorted(cdf, rng.random(n))
        if xi.sum() != n-1:
            continue
        # cycle lemma: rotate so the Lukasiewicz path stays >= 0 until the end
        s = np.cumsum(xi - 1)
        j = int(np.argmin(s)); # rotate to start right after the first minimum
        xi = np.concatenate([xi[j+1:], xi[:j+1]])
        # depths from the Lukasiewicz path via a stack (children of v follow v in DFS order)
        depth = np.empty(n, dtype=np.int64)
        stack = []  # list of remaining child counts
        d = 0
        for i in range(n):
            depth[i] = len(stack)
            stack.append(xi[i])
            while stack and stack[-1] == 0:
                stack.pop()
                if stack: stack[-1] -= 1
        levels = np.bincount(depth)
        W = levels.max(); H = len(levels)-1
        n2 = float((xi.astype(float)**2).sum())
        Vd = depth[rng.integers(n)]
        out.append((W, H, n2/n, Vd, xi.max()))
    return np.array(out, dtype=float), tries

for kind in KINDS:
    p = crit_law(kind)
    mean = (np.arange(len(p))*p).sum(); var = ((np.arange(len(p))**2)*p).sum() - mean**2
    print(f"\n{kind}: mean={mean:.6f} truncated var={var:.3f} p0={p[0]:.4f}")
    for n in SIZES:
        # rejection sampling of sum = n-1 costs ~ sqrt(n) (or n^{1/alpha}) tries; keep reps small
        reps = 24 if n <= 4000 else 8
        t0 = time.time()
        a, tries = sample_tree_widths(p, n, reps)
        W, H, n2, Vd, dmax = a.T
        print(f"  n={n:6d} reps={reps} tries={tries:5d}  W/sqrt n={np.median(W)/np.sqrt(n):6.3f}"
              f"  H/sqrt n={np.median(H)/np.sqrt(n):6.3f}  |n|_2^2/n={np.median(n2):7.2f}"
              f"  depth(V)/sqrt n={np.median(Vd)/np.sqrt(n):6.3f}  maxdeg/sqrt n={np.median(dmax)/np.sqrt(n):6.3f}"
              f"  ({time.time()-t0:.1f}s)")
