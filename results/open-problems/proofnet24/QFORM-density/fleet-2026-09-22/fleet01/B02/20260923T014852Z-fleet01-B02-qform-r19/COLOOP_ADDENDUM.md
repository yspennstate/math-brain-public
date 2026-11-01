# Exact natural-e2 coloop identity

This addendum records the endpoint structure left by `QFORM-E2-LR-FOURIER-v1`.

Let `M` have physical rows `r_1,...,r_m`, let

`Z_2=e_2(M^T M)=sum_{j<k} ||r_j wedge r_k||^2>0`,

and let `alpha_i` be the inclusion probability of row `i` under the natural squared-two-volume law. Let `N=M[-i,:]`.

Then Cauchy--Binet gives the two exact identities

`alpha_i Z_2 = sum_{j != i} ||r_i wedge r_j||^2`,                (A.1)

`(1-alpha_i) Z_2 = e_2(N^T N)
                    = sum_{j<k; j,k != i} ||r_j wedge r_k||^2`. (A.2)

Hence an **exact e2 coloop** `alpha_i=1` is equivalent to

`e_2(N^T N)=0`,

and therefore

`rank(N)<=1`.                                                    (A.3)

Thus the excluded rows are all collinear. Equivalently there exist a physical row vector `v` and scalars `c_j`, `j!=i`, such that

`r_j=c_j v` for every `j!=i`,                                  (A.4)

while `r_i` supplies the second row-space direction because `Z_2>0`. In matrix form the cross block is an exact **hub plus rank-one bank**,

`M = e_i r_i^T + c v^T`, with `c_i=0`.                           (A.5)

More generally, if `alpha_i>=1-epsilon`, then the total squared two-volume carried entirely by rows away from `i` is at most

`e_2(N^T N) <= epsilon Z_2`.                                    (A.6)

So the only endpoint missed by the aggregate `L^r_t` theorem is not an arbitrary rank-two packet: it is an exact/near hub-plus-rank-one-bank geometry. This is the correct object for the next mixed-hub/product-preserving closure step. No claim is made here that small `e_2(N^TN)` alone permits discarding `N` or perturbing coefficients under arbitrary fragmented input laws; the live no-uniform-perturbation corrections remain binding.
