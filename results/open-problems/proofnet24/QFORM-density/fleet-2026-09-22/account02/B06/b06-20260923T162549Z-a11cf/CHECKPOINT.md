# B06 substantive checkpoint — aggregate Fresnel/cross-volume fusion

Full QFORM remains open. The current unpaid partner branch is the recursive near-rank-two physical cross tube with its small nonzero tail retained and arbitrary same-bank curvature.

A new product-weighted subbranch is now available. Split untouched original coordinates into product banks I,J. Suppose, after conditioning only outside I∪J,

Q = X_I^T (D + V Λ V^T) X_I + 2 X_I^T M X_J + R(X_J) + linear terms,

where D is diagonal in the ORIGINAL I-coordinates, V has r orthonormal columns, Λ is invertible diagonal, and R is arbitrary. For an integer k≥0 define

Z_{r,k}(V,M) = Σ_{|S|=r+k, |T|=k} det([V_S, M_{S,T}])^2.

Equivalently by Cauchy–Binet and the Schur determinant identity,

Z_{r,k}(V,M)=e_k(M^T (I-VV^T) M).

Normalize these squared minors and let α_i be the row-inclusion marginals. If max_i α_i≤1/2 and a:=k+r/2>1, then the planned proof gives

|φ_Q(t)| ≤ (4π)^{r/2}(2π)^k e^{k/2} |det Λ|^{-1/2} Z_{r,k}^{-1/2} |t|^{-a},

hence

||p_Q||_∞ ≤ [a/(π(a-1))] [(4π)^{r/2}(2π)^k e^{k/2}]^{1/a}
             |det Λ|^{-1/(2a)} Z_{r,k}^{-1/(2a)}.

The proof combines the pinned newest-Claude Fresnel linearisation and its uniform L^p Fourier lemma with the determinant-weighted Brascamp–Lieb expansion, summing the complete physical minor law before inversion. It does not rotate the input law and does not take a fiber supremum.

Two key special cases:

1. r=0,k=2 (one bank physically diagonal):
   ||p_Q||_∞ ≤ 4√e · e_2(M^TM)^(-1/4).
   On partner account03/B06 r37's live true-near-rank-two cut, e_2(M^TM)>0.007994596888..., so this gives <22.056 whenever the corresponding two-volume row marginals are ≤1/2.

2. r=1,k=1 (rank-one-plus-diagonal bank): with V=v and λ the rank-one coefficient,
   ||p_Q||_∞ ≤ 3·2^(4/3)e^(1/3)|λ|^(-1/3)
                  ||(I-vv^T)M||_F^(-2/3).
   In the partner true-near-rank-two chamber, ||(I-vv^T)M||_F^2≥s_2(M)^2≥E/64 for every unit v, so if |λ|≥1 and the fused row marginals are ≤1/2, the branch is <46.939.

The remaining gap is not a small-tail estimate: arbitrary non-diagonal same-bank curvature destroys the coordinatewise twisted-product factorisation. The next step is either to fuse more same-bank curvature without multiplying tiny spectral coefficients, or to route a fused-volume heavy row marginal to an existing mixed-hub/physical-pair receiver.
