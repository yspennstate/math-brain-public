# C0097: finite coefficients and factorial upper bounds cannot establish divergence

2026-10-10. Label: proof of an information obstruction, awaiting w346 KEEP. The SAW connective-constant expansion is not solved here.

Given any finite coefficient prefix a_0,...,a_m, the polynomial P(z)=sum_{j<=m}a_j z^j is entire and matches it. The formal series P(z)+sum_{n>m}n! z^n matches the same prefix and has radius zero. Indeed n! >= (floor(n/2))^{ceil(n/2)}, so (n!)^(1/n) tends to infinity and Cauchy-Hadamard gives zero radius. If alternating signs are demanded, use (-1)^n n!, with the same radius. Thus any number of exact low-order coefficients, and ratios observed on them, are compatible with both alternatives.

A factorial upper bound alone is also insufficient: polynomial tails and factorial tails both satisfy |a_n|<=C K^n n! after adjusting C,K for the fixed prefix. A lower bound |a_n|>=c K^n n! along an unbounded subsequence would suffice. The missing step identified in the earlier attempt is signed non-cancellation of the actual lace-diagram coefficients; this note supplies neither that bound nor an analytic continuation for the connective constant.

The experiment uses a deliberately artificial four-term prefix only as a control. It never labels those numbers as connective-constant coefficients. The asymptotic problem's current global status remains unverified from the local cached corpus.
