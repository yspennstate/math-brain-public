SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T23:07:27Z.
attacking: the exact-match high-rank same-bank third-curvature survivor by solving the simultaneous physical-cut problem before any near-singular hub inversion.

# Early calculation: a compound identity for simultaneous arm area and projected third curvature

Let `M in R^{2 x m}` have row rank two, let `S=S^T in R^{m x m}`, and for a physical subset `K` let `P_K` be the orthogonal projection onto `row(M_K)`. Put

`A_K^2 = det(M_K M_K^T)`,
`C_K = S[K^c,K](I-P_K)`,
`F_K=||C_K||_F`.

For each `i in K^c`, the Gram Schur-complement identity followed by Cauchy--Binet gives

`A_K^2 ||(S[i,K](I-P_K))||_2^2
 = det([M_K;S[i,K]][M_K;S[i,K]]^T)
 = sum_{T subset K, |T|=3} det([M_T;S[i,T]])^2`.

Therefore

`A_K^2 F_K^2
 = sum_{i in K^c} sum_{T subset K, |T|=3} det([M_T;S[i,T]])^2`.        (E1)

If every coordinate is put in `K` independently with probability `p`, then each ordered pair `(i,T)`, `i notin T`, survives with probability `(1-p)p^3`, so

`E[A_K^2 F_K^2] = p^3(1-p) Xi(M,S)`,                              (E2)

where

`Xi(M,S)=sum_i sum_{T subset [m]\{i}, |T|=3} det([M_T;S[i,T]])^2`.

At `p=3/4`, `p^3(1-p)=27/256`. Hence some literal original-coordinate cut has

`A_K F_K >= sqrt(27/256) Xi(M,S)^(1/2)`.                          (E3)

This is exactly the simultaneous-selection currency missing in the newest fleet03/B08 high-rank exact-match router. If the projected rows of `C_K` have marginals at most `1/2`, the reviewed grouped projected-crossing theorem gives immediately

`||p_Q||_infinity <= 3*2^(5/6)(A_KF_K)^(-1/3)
                  <= 2^(13/6)*sqrt(3) Xi(M,S)^(-1/6)`.            (E4)

No hub inverse, moment assumption, rotated independence, support assumption, or deletion of same-bank curvature appears in (E1)--(E4). A heavy projected row is the complementary localized certificate.

The remaining work in this run is to rewrite `Xi` as an intrinsic arm/alignment energy, derive the actual `619/L` gate inherited from the previous B08 run, and stress the zero-alignment endpoint against a target-valid product-source family.
