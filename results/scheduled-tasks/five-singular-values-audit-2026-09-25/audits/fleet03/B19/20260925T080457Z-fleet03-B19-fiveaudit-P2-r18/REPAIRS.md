# Repairs / disagreements

No new mandatory repair was found in L173-L285.

Optional clarity edit at L222 only:
- original: “Factors with beta_i=0 are at most one and are dropped.”
- clearer: “Factors with beta_i=0 are bounded by one and are dropped.”

Mathematical status remains PASS under the natural value-bound reading because beta_i=0 implies w_i=0, making that factor z-independent and <=1. Any number of such factors may be removed from an upper bound.

Existing C01-C07 are unchanged. C02 lies above this run and was already independently reproduced in P2 r17. The existing L148/C06b disagreement remains preserved for the later reverse pass.
