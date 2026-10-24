# LEMMA (proved by hand): sum_{j=0}^K eps_j 2^{K-j} 3^j = 0 with eps_j in {0,+-1} forces eps = 0.
#   Proof: mod 2 kills eps_K (only that term is odd); mod 3 kills eps_0; the rest is 6 x the same form at K-2.
# So the frequencies (3/2)^j carry NO nontrivial {0,+-1} relation.  Dissociateness in the classical Riesz-product
# sense needs {0,+-1,+-2}.  Test both by exhaustive search for small K, and test the full-period average
#   A_K = mean over k mod 3^{K+1} of prod_{i=0}^{K} cos^2(pi k 2^i / 3^{i+1})
# against the independence value 2^{-(K+1)}.
import numpy as np, itertools, math, sys
print("exhaustive relation search: is sum_j eps_j 2^{K-j} 3^j = 0 possible with eps nonzero?")
for K in range(0, 13):
    coeffs = [2**(K-j)*3**j for j in range(K+1)]
    found1 = found2 = None
    for eps in itertools.product((0,1,-1), repeat=K+1):
        if any(eps) and sum(e*c for e, c in zip(eps, coeffs)) == 0: found1 = eps; break
    if K <= 9:
        for eps in itertools.product((0,1,-1,2,-2), repeat=K+1):
            if any(eps) and sum(e*c for e, c in zip(eps, coeffs)) == 0: found2 = eps; break
    print(f"K={K:2d}: {{0,+-1}} relation: {found1 if found1 else 'NONE'} | {{0,+-2}} relation: {found2 if found2 else ('NONE' if K<=9 else 'not searched')}")
print("\nfull-period average A_K vs the independence value 2^{-(K+1)}:")
for K in range(0, 14):
    M = 3**(K+1)
    if M > 30_000_000: break
    k = np.arange(M, dtype=np.float64)
    P = np.ones(M)
    for i in range(K+1):
        P *= np.cos(np.pi*k*(2.0**i)/(3.0**(i+1)))**2
    A = float(P.mean()); ind = 2.0**(-(K+1))
    print(f"K={K:2d}: A_K = {A:.6e}   2^-(K+1) = {ind:.6e}   ratio = {A/ind:.4f}", flush=True)
