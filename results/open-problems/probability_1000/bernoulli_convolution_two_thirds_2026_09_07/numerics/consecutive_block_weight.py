"""How much of the weight sits on the consecutive block?

nu(eps) = sum_{i<=K} eps_i 2^i 3^(K-i),  eps in {-1,0,1}^(K+1),  c(eps) = 2^(-#nonzero eps_i).
The paper says the map is injective, its image contains every |m| <= 2^(K+1)-1 (the "consecutive
block"), the full range is |nu| <= 3^(K+1) - 2^(K+1), and sum_m c(m) = 2^(K+1) - 1.
A verifier says the consecutive block holds only about 1 pct of the weight at K = 12.
Both cannot be right about the same sum.  Measure it.
"""
import numpy as np

for K in (8, 10, 12):
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64)
    c = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    tot_patterns = 3 ** (K + 1)
    uniq = np.unique(nu).size
    block = 2 ** (K + 1) - 1
    inblk = np.abs(nu) <= block
    nonzero = nu != 0
    print(f"K={K:>3}  patterns={tot_patterns:>9}  distinct nu={uniq:>9}  injective={uniq==tot_patterns}")
    print(f"       full range |nu| <= {3**(K+1) - 2**(K+1):>10}   consecutive block |m| <= {block}")
    print(f"       sum c over ALL patterns          = {c.sum():.4f}   (2^(K+1) = {2**(K+1)})")
    print(f"       sum c over nu != 0               = {c[nonzero].sum():.4f}   (paper: 2^(K+1)-1 = {2**(K+1)-1})")
    print(f"       sum c over 0 < |nu| <= block     = {c[inblk & nonzero].sum():.4f}"
          f"   = {100*c[inblk & nonzero].sum()/c[nonzero].sum():.2f} pct of the weight")
    print(f"       block holds {int(inblk.sum())} of {tot_patterns} patterns"
          f" = {100*inblk.sum()/tot_patterns:.3f} pct of the patterns")
    print()
