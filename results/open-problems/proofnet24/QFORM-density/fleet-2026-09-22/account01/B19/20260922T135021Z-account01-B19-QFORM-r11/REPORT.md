# account01/B19 — universal proof assembly: balanced-cut self/cross resource theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T135021Z-account01-B19-QFORM-r11`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Outcome:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Target and corrections retained

The target is the unrestricted statement: for every dimension, every independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the essential supremum of the density of `Q=X^T A X`. Continuity is a separate stronger conclusion.

This report does not use law-uniform pointwise Fresnel decay, post-rotation independence, a fiber supremum, one selected coordinate minor, bounded-diameter localization, or a conditional-density surrogate. Those mechanisms have current source-valid corrections. Signs of the three selected eigenvalues are arbitrary, eigenvalue coincidences are allowed, and all additional eigenvalues of `A` may be arbitrary in number, magnitude and sign.

The first global obstruction in the current assembly is not a local smoothing estimate: it is converting the existence of three large spectral directions into product-coordinate resources without allowing the rest of the spectrum to cancel the selected three directions. This run proves an exact cancellation-resistant inequality for that conversion.

## 2. Spectral-square domination

Choose any three orthonormal eigenvectors of `A` whose eigenvalues satisfy `|lambda_j|>=1`. Put them into an `n x 3` matrix `U` with `U^T U=I_3`, and let

`P=U U^T`

be their orthogonal projection. Then

`A^2 >= P`                                                     (2.1)

in Loewner order.

Indeed, in a complete orthonormal eigenbasis,

`A^2-P = sum_selected (lambda_j^2-1) r_j r_j^T + sum_other lambda_j^2 r_j r_j^T`,

which is positive semidefinite. This is the key point: arbitrary extra eigendirections can cancel entries of `A`, but they cannot cancel the selected spectral mass in `A^2`.

Now split the ORIGINAL coordinates into a set `H` and its complement `L`, and write

`A = [[C,B],[B^T,D]]`,

where `C=A[H,H]`, `D=A[L,L]`, and `B=A[H,L]`. Compressing (2.1) to the two coordinate sides gives

`C^2+B B^T >= U_H U_H^T`,                                      (2.2)

`D^2+B^T B >= U_L U_L^T`.                                      (2.3)

No density argument and no sign assumption has entered.

## 3. Balanced-cut singular-resource theorem

Let

`G_H=U_H^T U_H`, `G_L=U_L^T U_L=I_3-G_H`.

Assume for some `delta>0`

`G_H >= delta I_3`,   `G_L >= delta I_3`.                       (3.1)

The three nonzero eigenvalues of `U_H U_H^T` equal those of `G_H`, so (2.2) implies

`lambda_3(C^2+B B^T)>=delta`.

For positive semidefinite matrices, Weyl's inequality

`lambda_{i+j-1}(S+T) <= lambda_i(S)+lambda_j(T)`

applied with `i+j=4` now gives the exact three inequalities

`delta <= s_1(C)^2+s_3(B)^2`,                                  (3.2)

`delta <= s_2(C)^2+s_2(B)^2`,                                  (3.3)

`delta <= s_3(C)^2+s_1(B)^2`.                                  (3.4)

The same argument on `L` gives

`delta <= s_1(D)^2+s_3(B)^2`,                                  (3.5)

`delta <= s_2(D)^2+s_2(B)^2`,                                  (3.6)

`delta <= s_3(D)^2+s_1(B)^2`.                                  (3.7)

Here singular values are nonincreasing, with missing values interpreted as zero.

Set

`alpha=sqrt(delta/2)`.

Let `r_C` be the number of the first three singular values of `C` that are at least `alpha`, and let `r_B` be the number of the first three singular values of `B` that are at least `alpha`. Then

`r_C+r_B>=3`,   `r_D+r_B>=3`.                                  (3.8)

Proof: if `r_C=0`, then `s_1(C)<alpha`, and (3.2) forces `s_3(B)>=alpha`; if `r_C=1`, (3.3) forces `s_2(B)>=alpha`; if `r_C=2`, (3.4) forces `s_1(B)>=alpha`; `r_C=3` is immediate. The `D` statement is identical.

This is a dimension-free self/cross rank budget. It is stronger than a Hilbert--Schmidt energy estimate: the three selected directions cannot all collapse into one large singular direction after an arbitrary extra-spectrum completion.

Useful sharper endpoint consequences are

* `C=0  => s_3(B)>=sqrt(delta)`;
* `rank(C)<=1 => s_2(B)>=sqrt(delta)`;
* `rank(C)<=2 => s_1(B)>=sqrt(delta)`;
* `||C||op<=sqrt(delta/2) => s_3(B)>=sqrt(delta/2)`.

All four statements remain true with `C` replaced by `D`.

## 4. Diffuse selected eigenspace: an unconditional balanced cut

The fresh regularized-determinant proof package records the two-part Marcus--Spielman--Srivastava partition consequence: if a Parseval frame has row leverage at most `1/32`, its rows can be partitioned into `H,L` with both partial Gram matrices between `7I/32` and `25I/32`.

Apply this only to the selected three-frame `U`; no assumption is made on the rest of the range of `A`. Thus if

`max_i ||U^T e_i||^2 <= 1/32`,                                  (4.1)

there is an original-coordinate cut satisfying (3.1) with

`delta=7/32`,   `alpha=sqrt(7)/8`.                              (4.2)

This is strictly different from the existing full-spectrum diffuse-range theorem. The latter assumes the ENTIRE range projection is diffuse. Here arbitrary extra spectral directions may be completely localized; their only effect is through the actual blocks `C,D,B`, and inequalities (3.2)--(3.7) remain valid.

## 5. Completed peer mathematics applied to actual density inequalities

### 5.1 Exact zero-self endpoint — designated partner account02/B19

The completed partner theorem `QFORM-RECTANGULAR-MULTIPIVOT-SINGULAR-v1` states that for disjoint original-coordinate packets `I,J`, if `A[I,I]=0` and `A[I,J]` has two nonzero singular values `s_1,s_2`, then

`||p_Q||_infinity <= 2 sqrt(pi)/sqrt(s_1 s_2)`                  (5.1)

for arbitrary independent input densities bounded by one and arbitrary completion on the other side.

Use the balanced-cut theorem with `I=H,J=L`. If `C=0`, then (3.2) gives `s_3(B)>=sqrt(delta)`, hence in particular `s_1(B),s_2(B)>=sqrt(delta)`. Substitution into the partner's actual inequality gives

`||p_Q||_infinity <= 2 sqrt(pi)/sqrt(delta)`.                  (5.2)

For the MSS selected-frame cut `delta=7/32`,

`||p_Q||_infinity <= 8 sqrt(2 pi/7) < 7.58`.                   (5.3)

This is a target-level full-matrix branch: all extra eigenvalues, all signs, all outside/self terms on `L`, and all admissible input laws are retained.

### 5.2 Small self block plus diffuse cross range — regularized determinant theorem

The completed regularized-determinant theorem gives, when a cross block has three singular values at least `sigma` and the coordinate leverage of its range on one physical side is at most `1/2`,

`||p_Q||_infinity <= 3e/(sqrt(2) sigma)`,                       (5.4)

with a continuous representative vanishing at infinity; arbitrary self blocks and arbitrary extra spectrum are permitted.

If `||C||op<=sqrt(delta/2)`, (3.2) gives `s_3(B)>=sqrt(delta/2)`. Therefore, whenever the stated cross-range leverage condition holds,

`||p_Q||_infinity <= 3e/sqrt(delta)`.                           (5.5)

At `delta=7/32` this is

`||p_Q||_infinity <= 24e/sqrt(14) < 17.44`.                    (5.6)

Thus the new algebraic inequality converts selected-eigenspace diffuseness plus one checkable mixed-block condition into an actual universal full-matrix density estimate. No small additional eigenvalue is discarded or paid reciprocally.

## 6. Mixed profiles are genuinely necessary: exact target family

A tempting strengthening would say that a balanced selected eigenspace forces either three strong self singular directions or three strong cross singular directions. That is false even in a six-dimensional target matrix.

Let

`U=2^(-1/2) [ I_3 ; I_3 ]`,
`V=2^(-1/2) [ I_3 ; -I_3 ]`.

For `r=0,1,2,3`, let

`M_r=diag(1,...,1,-1,...,-1)`

with `r` plus signs, and set

`A_r=U I_3 U^T + V M_r V^T`.

Then the `U` columns are three eigenvectors of eigenvalue `+1`, while the `V` columns have eigenvalues `+/-1`. Hence every eigenvalue of `A_r` has modulus one. For the cut into the first and last three coordinates,

`G_H=G_L=(1/2)I_3`,

and direct block multiplication gives

`C=D=(I_3+M_r)/2`,
`B=(I_3-M_r)/2`.

Consequently

`rank(C)=rank(D)=r`,   `rank(B)=3-r`.                            (6.1)

For `r=1` and `r=2`, neither the self block nor the cross block has rank three. Therefore any claimed universal reduction to only a rank-three principal block or only a rank-three cross block is false. The mixed `1 self + 2 cross` and `2 self + 1 cross` profiles are source-valid target configurations, not proof artifacts.

The family is not a counterexample to QFORM. It only proves that the mixed profiles cannot be omitted from a structural proof.

## 7. Compact conditional end-to-end assembly

The current source-valid proof architecture can now be stated without a cancellation gap.

1. Diagonal / near-diagonal physical forms are already paid by the previous account01/B19 theorem.
2. Rank-three diffuse and localized-diffuse-residual basins are paid by account03/B08 and account03/B19; finite projective-bank rank-three forms are also paid.
3. Entire-range diffuse matrices, including arbitrary tiny extra eigenvalues, are paid by the regularized-determinant/MSS theorem.
4. For a matrix whose SELECTED three-eigenspace is diffuse but whose extra range is not, the present theorem supplies an MSS cut and the exact self/cross rank budget (3.8), immune to cancellation by the extra spectrum.
5. Pure/near-pure cross endpoints satisfying the peer hypotheses are paid by (5.2) or (5.5).

Thus the first essential missing implication is no longer 'show extra eigendirections do not cancel the selected three'. They can cancel entries of `A`, but (2.1)--(3.8) show exactly where the resource goes.

The remaining analytic bridge is:

**`QFORM-BALANCED-MIXED-PROFILE-SMOOTHING-v1` (OPEN).** For a balanced cut with fixed `delta>0` and the rank budget (3.8), prove a dimension-free density estimate in the two genuinely mixed regimes `2 self + 1 cross` and `1 self + 2 cross`, and in the cross-rank-three heavy-range regime not covered by the fractional regularized determinant theorem. The proof must aggregate the singular directions before choosing physical minors and must preserve original-coordinate product structure. The six-dimensional family in Section 6 shows the mixed regimes cannot be deleted by a stronger linear-algebra dichotomy.

Closing this mixed-profile smoothing statement together with the already completed heavy-row/localized rank-three branches would produce the next credible full-proof assembly. Arbitrary additional spectrum is already present in the inequalities here; it is not a later perturbation debt for this branch.

## 8. Auxiliary affine-tilt closure lemma

For assembly under conditioning, note a useful general fact. Suppose a homogeneous density theorem with constant `M` is known for a spectral class stable under adding arbitrarily small eigenvalues in the kernel. Then the same essential-density bound holds after adding an arbitrary deterministic linear term.

Indeed write `K=ker A`, let `P_K` be its orthogonal projection, and set `A_e=A+e P_K`. Then `A_e` is invertible and preserves every pre-existing large eigenvalue. Choose `h_e=(1/2)A_e^{-1}b`. Coordinatewise translation `X+h_e` preserves independence and every density cap, while, up to a deterministic constant,

`(X+h_e)^T A_e (X+h_e)=X^T A X+b^T X+e X^T P_K X`.

As `e->0` the right side converges almost surely to `X^TAX+b^TX`. If the approximants have densities at most `M`, then for every nonnegative compactly supported continuous test function `g`, weak convergence gives

`int g dmu = lim int g p_e <= M int g`,

so the limit measure also has a density bounded by `M`. This passage does not by itself preserve continuity, which is why continuity remains tracked separately.

## 9. Source pins and status

Completed designated partner actually applied:

- account02/B19, `QFORM-RECTANGULAR-MULTIPIVOT-SINGULAR-v1`, canonical package `yspennstate/math-open-problems@23b520c19dd0e43cbff0fc0514a4dbfcd637b0f4`, report path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260922T123814Z-account02-B19-qform-r11/REPORT.md`.

Other completed mathematics actually applied:

- regularized determinant and MSS full-spectrum diffuse theorem, canonical `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, path `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`;
- account03/B19 critical rank-two `L^3` / localized residual theorem, canonical `yspennstate/math-open-problems@f600d39b2e88b14acf5af050076e1062cc33f1f6`, used in the conditional assembly status but not re-proved here;
- account03/B13 finite projective-bank theorem, canonical handoff records report commit `5c37d1ea814c481c8a6c0230a871f6d59b448cda`.

Fresh control at run start: `yspennstate/math-research-brain@0c0c57ad0f1454ca3ba708eaa2f8a42743d94608`; before publication main advanced through unrelated QFORM worker records, with owner revision still `2026-09-22.5` and the same exclusive target.

**Proved this run:** spectral-square domination (2.1); balanced-cut block inequalities (3.2)--(3.7); threshold rank budget (3.8); selected-frame MSS corollary; target-level peer applications (5.2)--(5.6); exact six-dimensional mixed-profile obstruction; affine-tilt weak-closure lemma.

**Not proved:** the mixed-profile smoothing implication; the unrestricted full QFORM conjecture; universal continuity. No full-proof claim is made.
