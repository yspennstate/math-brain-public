2026-10-11: Candidate fixed-law lower-bound construction, not yet refereed.

For 0<eps<2/3 and delta>2eps/(2+eps), choose b in
(max(eps/delta,2eps),(2+eps)/2) and beta in (eps/b,1/2).
Let G be standard real Gaussian and independent Y_j take values +/-R_j
with total probability p_j=2^{-j(2+eps)}R_j^{-(2+eps)}, and zero otherwise.
Choose R_j inductively very large. The sum has finite (2+eps)-moment by
Minkowski. At n_j=floor(R_j^b), the whole matrix misses all Y_k, k>=j,
with probability tending to one. Its entries then agree exactly with the
fixed all-moments law G+sum_{k<j}Y_k. Apply Jalowy Theorem 1 to that law
at n_j, and compare its variance with the total variance. Missing variance
is at least 2^{-j(2+eps)}R_j^{-eps}. This dominates n_j^{-beta} and
its product with n_j^delta can be made >j. Use f(z)=min(|z|,1) to see
a circular-law discrepancy. Need complete induction, metric conversion,
and hostile checks before recording a proved claim.
