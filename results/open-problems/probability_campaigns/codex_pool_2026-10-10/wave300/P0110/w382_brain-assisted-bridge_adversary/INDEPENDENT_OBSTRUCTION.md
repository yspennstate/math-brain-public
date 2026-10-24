# Independent derivation, saved before reading the paired prover

2026-10-10. Worker w382. Only the target ranking and Chatterjee Theorem 1.1 have been used here; no w381 or w383 proof has been read. This is an obstruction to an abstract implication, not an iid FPP construction and not a solution of P0110.

For n >= 2, let B_n be Bernoulli(n^(-1/2)) and let C_n be Bernoulli(n^(-1/4)). No independence across n or between these two families is needed. Define centered X_n = n^(1/2)(B_n - n^(-1/2)) and nonnegative D_n = n^(3/4) C_n.

Define chi_a as the infimum of s for which some alpha > 0 makes sup_n E exp(alpha |X_n|/n^s) finite, and chi_b as the supremum of s for which inf_{n>N} Var(X_n)/n^(2s) > 0 for some N. Define xi_a with D_n in place of |X_n| in the exponential bound and xi_b with E D_n/n^s in the lower bound.

Then chi_a = 1/2, chi_b = 1/4, xi_a = 3/4, xi_b = 1/2.

Proof: |X_n| <= n^(1/2) and D_n <= n^(3/4), which give the upper exponential bounds at their stated endpoints. For s < 1/2 the event B_n=1 contributes at least n^(-1/2) exp(alpha n^(1/2-s)/2) to the X exponential moment for n >= 4; this tends to infinity for every alpha > 0. Likewise C_n=1 contributes n^(-1/4) exp(alpha n^(3/4-s)), which diverges for every s < 3/4 and every alpha > 0. Finally Var(X_n) = n^(1/2)(1-n^(-1/2)) and E D_n = n^(1/2), so the two lower endpoints are exactly 1/4 and 1/2.

Thus a polynomial variance exponent, a polynomial expected-deviation exponent, boundedness at the generic allowed scales, and even chi_a = 2 xi_a - 1 do not imply equality of the two definitions for either exponent. Strong uniform exponential-tail information at the claimed smaller scale is missing. This scalar example is not FPP; it refutes only the inference from moment data to matching exponential-moment exponents without further structure.

The hardest open bridge for the Chatterjee route is to find one genuine iid nearest-neighbor FPP law on Z^d, d >= 2, for which both equalities of upper and lower exponents hold. Known-law admissibility alone does not supply that bridge. Full target record and survey question still to be recovered.

Independent check required from w383. The arguments above do not multiply conditional bounds or assume independent geodesic increments.
