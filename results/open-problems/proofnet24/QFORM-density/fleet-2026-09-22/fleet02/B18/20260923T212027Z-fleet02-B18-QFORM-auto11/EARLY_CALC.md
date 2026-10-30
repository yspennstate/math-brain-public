# fleet02/B18 early calculation — moderate-leverage exact-rank-three cut

Programme: `QFORM-DENSITY-3EIG-20260922`. Full QFORM remains OPEN.

First unpaid implication addressed here: improve the newest exact-rank-three diffuse physical-cut threshold without rotating the random source. Let

`A=U Lambda U^T`, `U^T U=I_3`, `kappa=max_i ||u_i||_2^2`, and `|lambda_j|>=1`.

For a Bernoulli half-partition `I sqcup J`, set `G_I=sum_{i in I} u_i u_i^T`. Then

`E ||G_I-I_3/2||_F^2 = (1/4) sum_i ||u_i||^4 <= 3 kappa/4`.

Hence if `kappa<=1/8`, some actual ORIGINAL-coordinate cut satisfies

`||G_I-I_3/2||_op <= sqrt(3/32)=sqrt(6)/8`.

Put

`a0=(4-sqrt(6))/8`, `h0=1/(4-sqrt(6))=(4+sqrt(6))/10 <3/4`.

Then `G_I,G_J >= a0 I_3`. For `M=A[I,J]=U_I Lambda U_J^T`, Cauchy--Binet gives

`Z_3(M)=det(Lambda)^2 det(G_I)det(G_J) >= a0^6`.

Its I-side 3-volume row marginal is exactly

`alpha_i=u_i^T G_I^{-1}u_i <= (1/8)/a0 = h0`.

The completed pinned e5f Theorem D' therefore yields, for arbitrary bank-local measurable phases and hence for the original quadratic form,

`||p_Q||_infinity <= 6 sqrt(e) (2h0)^(-1/2)(3-4h0)^(-1) a0^(-1)`

`= 24 sqrt(2e(4-sqrt(6)))/(8-3sqrt(6))`

`= 106.9487887028395...`.

The D' proof also gives an L1 characteristic function, so this exact-rank-three branch has a continuous C0 density. No continuity claim is made for the full target.

This raises the clean random-cut leverage corollary from the current `1/24` checkpoint to `1/8`; the older correction inbox already records a different direct-cross proof through `1/12`, so no novelty claim is made for the subrange `kappa<=1/12`.

A literal target family at the new range is the 24-row circular Parseval frame

`u_j=(1/sqrt(24), sqrt(2/24) cos(2pi j/24), sqrt(2/24) sin(2pi j/24))`,

for which every row has leverage exactly `1/8`. With `Lambda=diag(1,1,-1)`, the physical matrix has nonzero spectrum `{1,1,-1}`. The new cut theorem gives the whole-line bound above. The owner-pinned e5f ruled one-sheet theorem independently gives `p_Q(t)<=pi sqrt(2)` for a.e. `t>=0` on this same exact target family.
