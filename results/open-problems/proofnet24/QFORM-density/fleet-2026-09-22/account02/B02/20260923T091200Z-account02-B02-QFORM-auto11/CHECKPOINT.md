SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-23T09:12:00Z.
attacking: the first unpaid near-coloop/four-anchor E2 collar by conditioning the mixed (incident-E3,residual-E2) determinant laws on physical row/column cross-disjointness.

# Early mathematical checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

Let `B=A[I,J]` be a physical original-coordinate cross block. Fix physical anchors `x in I`, `y in J`. Let

- `J3` be the total squared `3x3`-minor mass of minors containing both `x,y`;
- `N=B[I\{x},J\{y}]` and `E2=e2(N^T N)>0`;
- `mu3` be the normalized determinant-squared law on the residual row/column pairs `(R3,T3)` of the incident `3x3` minors;
- `mu2` be the normalized determinant-squared law on residual `2x2` minors `(R2,T2)` of `N`.

For independent samples define

`delta_r=P(R3 cap R2=empty)`, `delta_c=P(T3 cap T2=empty)`.

## New implication under proof

Conditioning the product law `mu3 tensor mu2` on `R3 cap R2=empty` forces every equal-mixture row marginal to be at most `1/2`: the outer anchor has marginal `1/2`, and each residual row has `(1_{i in R3}+1_{i in R2})/2<=1/2` pointwise. The KL cost satisfies

`D(mu3'||mu3)+D(mu2'||mu2)<=log(1/delta_r)`.

Insert these two conditioned determinant laws into the exact diagonal-plus-PSD Gaussian determinant expansion, retain the incident-3 and residual-2 basis families, and take their geometric mean. Applying the reviewed sharp Hausdorff--Young inequality at `q=1` gives the candidate exact bound

`||p_Q||_infinity <= (5e/2^(1/5)) delta_r^(-1/10) (J3 E2)^(-1/10)`.

The transpose gives the same bound with `delta_c`. The high-frequency envelope is `|phi_Q(t)|<=K|t|^(-5/4)`, hence this is a genuine unweighted `L1_t` characteristic-function branch and gives continuity.

This removes the nonzero physical cross-edge hypothesis from account02/B02's preceding edge/E2 disjointness theorem: the determinant family uses the actual incident third-volume directly, not a cross-only Schur identity.

## Failure certificate and designated-partner splice

If `delta_r<eta`, some residual row pair `H` from the incident-three support satisfies `P_mu2(R2 cap H !=empty)>1-eta`; similarly `delta_c<eta` supplies a residual column pair `L`. Hence if both are `<eta`, more than `(1-2eta)E2` of the residual second-compound mass uses a row from `H` and a column from `L`.

Pigeonholing the four physical pairs `(i,j) in H x L` gives one common-anchor packet

`H2^(i,j)(N) >= (1-2eta)E2/4`.

Now apply the completed designated partner `account03/B02` r25 exact identity (`math-open-problems@ff8ec2ee90d4846f39e728e1ca20d50c717cc894`). Writing the residual block around this physical anchor as

`N=[[a,r^T],[c,M]]`,

partner r25 gives exactly

`H2^(i,j)(N)=||aM-cr^T||_F^2`.

Therefore the four-anchor failure is not merely combinatorial: it forces the quantitative physical obstruction

`||aM-cr^T||_F^2 >= (1-2eta)E2/4`.

At `eta=1/16`,

`||aM-cr^T||_F^2 >= 7E2/32`.

Thus if `a!=0`, the true cross-Schur Frobenius packet obeys

`||M-cr^T/a||_F^2 >= 7E2/(32a^2)`,

while if `a=0` the exact two-star product obeys

`||c||_2^2 ||r||_2^2 >= 7E2/32`.

The remaining work is to finish the determinant/HY constant derivation carefully and then decide whether the forced edge-Schur/two-star packet can be paid by an existing receiver without introducing a false cross-Schur/true-Schur identification. No such payment is asserted in this checkpoint.
