# account02/B09 — substantive checkpoint

Status: supporting implication proved below; unrestricted QFORM remains open. Execution status WITHOUT_VERIFIED_BRAIN.

## First unpaid implication attacked

`QFORM-RANK2-HUBSTAR-HIGH-HUBLEVERAGE-OR-SCALE-ROUTING-v1`: for a physical rank-two hub/star `A[H,I]=P C^T`, `P^T P=I_2`, with completely arbitrary within-leaf curvature `D=A[I,I]`, extend the aggregate singleton-volume compiler beyond the old hub-row leverage gate `max_h (PP^T)_{hh}<=1/2` without rotating the random variables or discarding `D`.

## New lemma: selected-family fractional three-volume BL

Let `M` be an actual original-coordinate cross matrix and let `Omega` be any nonempty selected family of its physical `3x3` minors. Put

`Z_Omega=sum_{(R,C) in Omega} det(M[R,C])^2`,

and normalize those squared minors to a probability measure. Let `alpha_i`, `beta_j` be its physical row/column inclusion marginals. For `1<=q<3/2`, if `max_i alpha_i<=q/2`, then every quadratic-plus-affine form with this cross matrix and arbitrary same-side measurable phases obeys

`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] Z_Omega^(-1/6)`,

with continuous density and the same coefficient times `|L|` for every interval `L`.

Proof: in the Gaussian BL determinant expansion, discard every minor outside `Omega`, then weighted AM-GM with weights `det^2/Z_Omega` gives

`det(D_J+M^T D_I M)>=Z_Omega prod_i d_i^{alpha_i} prod_j e_j^{1-beta_j}`.

The sharp Hausdorff--Young/Jensen calculation thereafter uses only `sum alpha=sum beta=3`, `alpha_i<=q/2`, and `0<=alpha,beta<=1`; it is therefore literally the q-dependent proof of the completed fractional-volume theorem with `Z` replaced by `Z_Omega`. No random-variable rotation occurs.

## Consequence for rank-two hub/stars up to leverage <3/4

Use account03/B09 r32 notation. For each leaf `k`, let `Gamma_k^2=e_3(M_k^T M_k)` and `G_*=sum_k Gamma_k^2`. Bernoulli leaf partitioning supplies a literal selected physical-minor family with mass `W>=cG_*`, `c=27/256`. In the diffuse-singleton branch `Gamma_k^2<(c/2)G_*` for every k, its moved-leaf row marginals are `<1/2`, while each hub-row marginal is exactly `ell_h=(PP^T)_{hh}`.

Therefore if `eta=max_h ell_h<3/4`, put `q_eta=max(1,2eta)`. The selected-family lemma pays the diffuse branch, while the r32 concentrated-singleton branch remains unchanged. Hence

`||p_Q||_inf <= C(eta) G_*^(-1/6)`,

where

`C(eta)=max{3e(512/27)^(1/6), [3e/((3-2q_eta)sqrt(q_eta))](256/27)^(1/6)}`.

This strictly extends the completed r32 gate from `eta<=1/2` to every `eta<3/4`, retaining arbitrary `A[H,H]`, arbitrary dense `D=A[I,I]`, outside couplings, and affine terms.

A genuine target-valid test beyond the old gate: take the 3-row equal-norm Parseval frame
`p1=(sqrt(2/3),0)`, `p2=(-1/sqrt(6),1/sqrt(2))`, `p3=(-1/sqrt(6),-1/sqrt(2))`, so `eta=2/3`. On an m-coordinate leaf bank take a flat orthonormal Walsh triple `c1,c2,v`, set `C=[c1,c2]`, `D=vv^T`, and all hub self-curvature zero. The active spectrum is exactly `{1,-1,1,-1,1}`. Moreover `Gamma_k^2=m^{-1}(1-3/m)`, so `G_*=1-3/m`. With `q=4/3`,

`||p_Q||_inf <= 30.824 (1-3/m)^(-1/6)`.

This is a dimension-free linear-small-ball bound in a genuine leverage-2/3 case not covered by the r32 `<=1/2` gate.

Remaining debt after this checkpoint: leverage `eta>=3/4` (the Fourier exponent reaches the nonintegrable endpoint at eta=3/4) and the separate structural task of forcing a universal-scale `G_*` or another already-paid exit from the bare three-large-eigenvalue hypothesis.
