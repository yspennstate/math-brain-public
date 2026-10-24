# B09 substantive checkpoint — Pluecker-balanced mixed hub with dense same-side curvature

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN. This checkpoint records the first useful calculation of the run, before the final report.

## Candidate theorem

Let one original-coordinate hub be `h`, let `I` be a disjoint leaf bank, and condition only further disjoint coordinates. Write the exact leaf block as

`A_II = D + sum_{k=1}^r lambda_k v_k v_k^T`,

with `D` diagonal, `lambda_k != 0`, and put `c=A[I,h]`. Define the mixed physical frame

`W=[v_1,...,v_r,c]`, `G=W^T W`, `d=r+1`.

Assume `G>0`. Whiten `U=W G^{-1/2}`. For `d`-subsets `S` of leaf coordinates put `w_S=det(U_S)^2`; Cauchy--Binet gives `sum_S w_S=1`. Let

`rho = P(S cap T = empty)`

for iid `S,T` drawn from `w`. If `rho>0`, then conditioning the pair on disjointness yields a basis law whose one-coordinate inclusion marginals are all at most `1/2` and whose relative entropy with respect to `w` is at most `log(1/rho)`. Applying the completed determinant-weighted entropy Brascamp--Lieb lemma to the exact mixed-hub Fourier integral in Theorem H gives

`|phi_Q(t)| <= A |t|^{-(r+2)/2}`,

where

`A = pi^((r+2)/2) e^((r+1)/2) [rho det(G) prod_k |lambda_k|]^(-1/2)`.

Indeed Theorem H contributes the exact hub Jacobian `(2|t|)^(-1)`, the `r` Fresnel factors `prod(4 pi |t lambda_k|)^(-1/2)`, and after whitening the entropy-BL integral is at most

`det(G)^(-1/2) (2 pi)^(r+1) e^((r+1)/2) rho^(-1/2)`.

The powers of 2 cancel. Since `alpha=(r+2)/2>1`, direct Fourier integration gives

`||p_Q||_infinity <= ((r+2)/r) e^((r+1)/(r+2)) [rho det(G) prod_k |lambda_k|]^(-1/(r+2))`.

Thus every interval `L` obeys the same coefficient times `|L|`; there is no probability squaring or square-root small-ball loss. The blocks `A_hh,A_hJ,A_IJ,A_JJ` and conditioning-generated affine terms remain arbitrary exactly as in Theorem H.

Source equations actually used: e5f71d79eff325201dd0274053d20268ce65b837, `RESULTS.md`, Theorem H; and 32c257209b588141fb60af698f478f1d0ad20b8a, account02/B07 `QFORM-PLUCKER-ENTROPY-BL-v1`, Sections 3 and 5 (valid for general frame dimension `k`).

## Strict-N3 star where the old leverage gate fails

Take three pairwise disjoint leaf supports. On the first, let `v_1` have squared coordinate weights `0.6` and one hundred copies of `0.004`. On the second, let `v_2` be flat on 256 coordinates. On the third, let `c` be flat on 256 coordinates. They are orthonormal. Let

`B_1=v_1 v_1^T-diag(v_{1i}^2)`, `mu_1=lambda_max(B_1)>0`, `lambda_1=1/mu_1`,

and

`B_2=v_2 v_2^T-diag(v_{2i}^2)`, `lambda_2=256/255`,

so `lambda_max(lambda_1 B_1)=lambda_max(lambda_2 B_2)=1`. Define the full source-coordinate star by

`A_hh=0`, `A[I,h]=c`, `A_II=lambda_1 B_1+lambda_2 B_2`,

with no other blocks. Its spectrum contains `+1,-1` from the star and `+1,+1` from the two same-side blocks, hence it satisfies the target spectral hypothesis.

Every physical diagonal is zero. Since `v_1^T B_1 v_1=1-sum_i v_{1i}^4=0.6384`, `mu_1>=0.6384` and hence `lambda_1<=1/0.6384<1.567`. The largest first-block off-diagonal magnitude is at most `lambda_1 sqrt(0.6*0.004)<0.077`, whose square is `<1/128`. The second-block and hub-star off-diagonal squares are also `<1/128` (the latter equal `1/256`). Thus this is a literal strict-N3(1/128) family.

The old Theorem-H leverage gate fails because the heavy `v_1` row has mixed leverage `0.6>1/2`. But the frame is already orthonormal and its exact disjoint-basis mass is

`rho=(1-(0.6^2+100*0.004^2)) (255/256)^2 = 0.6334222412109375`.

For `r=2`, `det G=1`, and `lambda_1 lambda_2>=1`, the new estimate gives

`||p_Q||_infinity <= 2 e^(3/4) rho^(-1/4) < 4.746`.

This is a genuine strict-no-pivot source-coordinate star with dense same-side couplings, paid by aggregate determinant mass rather than any fixed physical minor.

Independent review: not yet performed. Remaining task for this run: write the full proof carefully, apply the newest account03/B09 result to a separate real inequality, and isolate the quantitative small-disjointness/high-localization survivor.
