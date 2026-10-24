# account02/B02 — conditional-projection falsifier + third-compound overlap ledger

Run: `20260922T163740Z-account02-B02-dc2fcdd7`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository retrieval was authenticated transport, not verified native learned-memory receiver ingestion.

## 1. Fresh control and first unpaid implication

The control refresh during this run advanced to OWNER CONTROL revision `2026-09-22.8` at brain commit `0c2eba9151d95fa5a29ba1b529bdfd98e9494c16`. The target remains: independent real coordinates with densities at most one, arbitrary real symmetric `A`, at least three eigenvalues of modulus at least one, and a universal essential density bound for `Q=X^TAX`.

The new owner message proposes a rank-three coarea route whose stated gap is a universal bound on the conditional three-dimensional spectral projection density after conditioning the remaining spectral coordinates. I tested that implication before using it. **It is false as stated.** Moreover the proposed auxiliary statement that a rank-three quadratic pushforward is bounded solely by the `L^infinity` norm of an arbitrary three-dimensional input density is also false. These are route corrections, not counterexamples to QFORM.

After recording the falsifiers I continued the assigned integrated-Fourier route. The positive result is a target-wide third-compound overlap ledger: the three-large-eigenvalue hypothesis always puts universal squared-minor mass into one of four original-coordinate overlap geometries. Its disjoint-overlap branch feeds directly into the already-reviewed regularized-determinant Fourier theorem without choosing a tiny individual minor.

## 2. Falsifier A: bounded rank-three input density alone does not control a quadratic pushforward

Fix `R>0` and choose `delta_R>0` so that the spherical shell

`E_R={y in R^3 : R <= |y| <= R+delta_R}`

has Lebesgue volume one:

`(4*pi/3)[(R+delta_R)^3-R^3]=1`.

Let `rho_R=1_{E_R}`. Then `rho_R` is a probability density and `||rho_R||_infinity=1`. For

`S=Y_1^2+Y_2^2+Y_3^2`,

coarea gives, for `R^2<s<(R+delta_R)^2`,

`p_S(s)= integral_{|y|=sqrt(s)} [1/|grad |y|^2|] dH^2(y)
       = 4*pi*s/(2*sqrt(s))
       = 2*pi*sqrt(s)`.

Hence

`||p_S||_infinity >= 2*pi*R -> infinity`.

Therefore there is no universal `C_0` such that every three-dimensional probability density `rho` satisfies

`||p_{sum lambda_i Y_i^2}||_infinity <= C_0 ||rho||_infinity`

merely from `|lambda_i|>=1`. The failure already occurs for the positive definite identity form. Any valid coarea theorem for QFORM must use substantially more than the joint density cap; in particular it must retain projection/product provenance or another quantitative radial/slice constraint.

## 3. Falsifier B: the conditional 3-D spectral projection cap is unbounded inside the exact QFORM class

Take independent

`X_1,X_2,X_3,X_4 ~ Uniform[-1/2,1/2]`,

so every original-coordinate density is exactly one on its support. Define the orthogonal coordinates

`Y_1=(X_1+X_2)/sqrt(2)`,
`Z  =(X_1-X_2)/sqrt(2)`,
`Y_2=X_3`, `Y_3=X_4`.

The joint density of `(Y_1,Z)` is the indicator of the diamond

`|Y_1|+|Z| <= 1/sqrt(2)`.

Thus for `|z|<1/sqrt(2)`,

`f_Z(z)=sqrt(2)-2|z|`,

and the conditional law of `Y_1` given `Z=z` is uniform on an interval of that length. Consequently

`||f_{Y_1|Z=z}||_infinity = 1/(sqrt(2)-2|z|)`.

Since `Y_2,Y_3` remain independent uniforms and independent of `(Y_1,Z)`, the conditional three-dimensional spectral density satisfies exactly

`||f_{(Y_1,Y_2,Y_3)|Z=z}||_infinity
   =1/(sqrt(2)-2|z|) -> infinity`

as `|z|` tends to `1/sqrt(2)`. This divergence occurs on sets of positive `Z`-probability for every finite proposed bound, so its essential supremum in the conditioning variable is infinite.

Now take the target-class matrix whose spectral form is

`Q=Y_1^2+Y_2^2+Y_3^2`.

In original coordinates its first `2x2` block is `[[1/2,1/2],[1/2,1/2]]` and the final two diagonal entries are one. Its eigenvalues are `{1,1,1,0}`. Hence it satisfies the exact three-large-eigenvalue hypothesis. Nevertheless the proposed universal conditional projection cap `M` is infinite.

This is not a counterexample to QFORM: `X_3^2+X_4^2` already has density at most `pi` by the proved two-square beta-integral theorem, and it is independent of `Y_1`; convolving with `Y_1^2` therefore gives `||p_Q||_infinity<=pi`. The example isolates the failure of conditioning in spectral coordinates rather than failure of the target.

This is the target-class lift of the live correction `QFORM-UV-CONDITIONAL-CAP-FALSE` (account02/B03, canonical brain correction source tied to commit `0d99f085f5378d267057cc5b9bcbf8e53ca494b5`).

## 4. New structural theorem: `QFORM-THIRD-COMPOUND-OVERLAP-LEDGER-v1`

For a real symmetric `n x n` matrix `A`, and `j=0,1,2,3`, define

`M_j(A)= sum_{|S|=|T|=3, |S cap T|=j} det(A[S,T])^2`.

### Theorem 4.1

If `A` has at least three eigenvalues of modulus at least one, then

`M_0+M_1+M_2+M_3 >= 1`,

so at least one `M_j>=1/4`. More precisely:

1. There is a bipartition `[n]=I disjoint_union J` with

   `E_3(A[I,J]) := sum_{S subset I, T subset J, |S|=|T|=3} det A[S,T]^2
                  >= M_0/64`.

2. There is a three-color partition `[n]=P disjoint_union I disjoint_union J` with

   `sum_{k in P} sum_{R subset I, T subset J, |R|=|T|=2}
      det A[{k} union R,{k} union T]^2
    >= M_1/3^5`.

3. There is a three-color partition `[n]=P disjoint_union I disjoint_union J` with

   `sum_{K subset P, |K|=2} sum_{i in I, t in J}
      det A[K union {i}, K union {t}]^2
    >= M_2/3^4`.

4. The `j=3` resource is already the principal aggregate

   `M_3=sum_{|S|=3} det A[S,S]^2`.

Thus one of the following dimension-free original-coordinate resources is always present:

`E_3 cross mass >=1/256`,
`one-common-pivot aggregate >=1/972`,
`two-common-pivot aggregate >=1/324`,
or `principal triple aggregate >=1/4`.

### Proof

By Cauchy--Binet,

`sum_{|S|=|T|=3} det A[S,T]^2
 = sum_{|S|=3} det((A A^T)[S,S])
 = e_3(s_1(A)^2,...,s_n(A)^2)`.

Since `A` is symmetric, its singular values are the absolute values of its eigenvalues. Three eigenvalues with modulus at least one contribute a term at least one to this nonnegative elementary symmetric polynomial. Splitting the left side by `|S cap T|` proves the first assertion.

For `j=0`, independently color every coordinate `I` or `J` with probability `1/2`. Each ordered disjoint pair `(S,T)` is captured as `S subset I,T subset J` with probability `2^-6`; taking expectations yields an `I,J` with the asserted `M_0/64` mass.

For `j=1`, independently color every coordinate `P,I,J` with probability `1/3`. For a fixed ordered pair with one common coordinate, the common coordinate must receive color `P`, the two row-only coordinates color `I`, and the two column-only coordinates color `J`. This occurs with probability `3^-5`. Expectation gives the second assertion. The `j=2` proof is identical, now on a four-coordinate union, so the probability is `3^-4`. QED.

This theorem includes **all additional eigendirections of A**. It is not a selected-rank-three-core statement and therefore cannot be invalidated by cancellation from an omitted spectral tail. It also aggregates squared minors before any reciprocal payment, so it does not repeat the refuted fixed-good-minor mechanism.

## 5. Direct integrated-Fourier payment of the disjoint-overlap branch

The previously reviewed theorem `QFORM-EK-INTEGRATED-DETERMINANT-v1` is source-pinned at

`yspennstate/math-open-problems@e3fe4ce35f6aa4a90cca913051886c96c7febfc3`.

For an original-coordinate cross block `B`, if `1<=q<3/2` and the maximum coordinate leverage of `range(B)` on its row side is at most `q/2`, then with `k=3`

`||p_Q||_infinity
 <= [e/(6 sqrt(2q))]
    BETA(1/6,1/(4q)-1/6)
    E_3(B)^(-1/6)`,

and the density is continuous and vanishes at infinity.

Apply Theorem 4.1 when `M_0>=1/4`. A deterministic cut has `E_3(B)>=1/256`. Therefore:

- if its row leverage is at most `1/2`, take `q=1` and obtain

  `||p_Q||_infinity < 14.252`;

- if its row leverage is at most `2/3`, take `q=4/3` and obtain

  `||p_Q||_infinity < 37.562`.

This is a genuine full-matrix QFORM branch: arbitrary self blocks, arbitrary outside couplings, arbitrary dimension, signs and extra eigenvalues are retained. If the disjoint mass branch occurs but this payment fails, the obstruction has now been localized to a **high-leverage row of a cross block carrying universal aggregate third-compound mass** rather than to absence of a coordinate minor.

No counterexample to a target-wide `||phi_Q||_1` bound was found. The stronger Fourier criterion therefore remains open; the result above pays a nontrivial target-wide branch of it.

## 6. Exact-rank-three balanced paving corollary

There is a useful clean consequence when `A=U Lambda U^T` has exact rank three, `U^T U=I_3`, and

`mu=max_i ||u_i||_2^2 <=1/8`.

Let `eps_i` be independent signs and `T=sum eps_i u_i u_i^T`. Then

`E ||T||_F^2 = sum_i ||u_i||^4 <=3mu`.

With `tau=5/8`, `tau^2>3mu`, so some sign choice has `||T||op<tau`. For the induced cut,

`G=U_I^T U_I=(I+T)/2`,

and every eigenvalue of `G` lies between `(1-tau)/2` and `(1+tau)/2`. The cross block `B=A[I,J]` has

`E_3(B)=det(Lambda)^2 det(G)det(I-G)
       > det(Lambda)^2 [(1-tau^2)/4]^3
       = det(Lambda)^2 (39/256)^3`.

Moreover the I-side leverage is at most

`2mu/(1-tau) <=2/3`.

Applying the preceding `q=4/3` determinant theorem and `|det Lambda|>=1` gives

`||p_Q||_infinity <38.191`,

with a continuous density. This widens the explicit direct diffuse exact-rank-three range beyond the archived `mu<=1/12` branch, at the cost of a larger constant. It is auxiliary: arbitrary additional spectral components remain the full-target difficulty.

## 7. Named partner actually applied: widen the localized residual cutoff to `mu<=9/50`

The latest completed named-partner result is account03/B02

`QFORM-RANK2-SCHUR-BALANCED-PAVING-v1`,
canonical report `yspennstate/math-open-problems@16c7d95068defd13bad9f9fe86be6037d046a1ef`,
path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T160323Z-account03-B02-qform-r11/REPORT.md`.

Its general parameter theorem allows more than the two explicit cutoffs printed in the handoff. Apply it with

`mu<=9/50`, `tau=121/200`, `q=183/100`, `r=48/25`.

The hypotheses hold because

`tau^2=0.366025 >2mu=0.36`,

and

`2mu/(1-tau) <=72/79 =0.911392... <q/2=0.915`,

while `q<r<2`. Substitution in the partner's exact formula (4.8) gives

`||p_Q||_infinity
 <72.82810 |d|^(-1/2)|det M|^(-1/4)`

for a genuine physical scalar pivot whose rank-two Schur frame has maximum row leverage at most `9/50`.

For the partner's exact-rank-three localized setting, where `ell>1/2`, `|d|>=1/2`, `|det Lambda|>=1` and `|det M|=|det Lambda| ell/|d|`, this becomes

`||p_Q||_infinity <102.995 <103`.

Thus the explicit localized residual coverage is widened from the partner handoff's `mu<=1/6` numerical branch to `mu<=0.18`. The partner theorem itself notes feasibility up to `(3-sqrt(5))/4`; this run supplies a concrete parameter choice and target inequality inside that range rather than claiming a new feasibility threshold.

## 8. Exact regression

`check_exterior3.py` uses only exact integer 3x3 determinants for the compound identities and exhaustive two-/three-color partitions on three deterministic symmetric `6x6` integer matrices. It verifies

`M_0+M_1+M_2+M_3=e_3(A^2)`,
`64 max R_0 >= M_0`,
`3^5 max R_1 >= M_1`,
`3^4 max R_2 >= M_2`,

and checks the partner parameters above. `CHECK_OUTPUT.txt` ends

`STATUS=ALL_EXACT_COMBINATORIAL_CHECKS_PASS`.

The checker is regression only; Sections 2--7 are analytic.

## 9. What remains unpaid

The full conjecture is still **OPEN**. The immediate proof obligations are now more precise:

1. The revision-2026-09-22.8 conditional-projection route cannot use a uniform conditional 3-D density cap, and the rank-three coarea pushforward cannot depend only on `||rho||infinity`. Any repair must keep stronger product/projection structure and average before taking the damaging conditional supremum.
2. For the integrated-Fourier route, pay the high-leverage disjoint-third-compound branch, or develop Fourier/coarea consumers for the universal overlap-one, overlap-two and principal aggregate resources in Theorem 4.1. This is an exhaustive original-coordinate classification, not a fixed-minor dichotomy.
3. Arbitrary additional eigendirections remain present automatically in the ledger but still obstruct the simpler exact-rank-three paving arguments.

No claim of continuity is made outside branches where `L^1` Fourier inversion was actually established. No full-solution or novelty claim is made.

## 10. Source discipline

Fresh protected control used before publication: `yspennstate/math-research-brain@0c2eba9151d95fa5a29ba1b529bdfd98e9494c16`, OWNER CONTROL revision `2026-09-22.8` (the run began before later control increments and refreshed when they appeared). Live corrections were reread after the increment, including the earlier conditional-cap, fixed-minor, post-rotation-independence, fiber-trace and same-square-absorption falsifiers.

Mathematical dependencies actually used:

- account02/B02 `QFORM-EK-INTEGRATED-DETERMINANT-v1`: `math-open-problems@e3fe4ce35f6aa4a90cca913051886c96c7febfc3`;
- named partner account03/B02 `QFORM-RANK2-SCHUR-BALANCED-PAVING-v1`: `math-open-problems@16c7d95068defd13bad9f9fe86be6037d046a1ef`, report blob `3c0a5d6aabbdfc02cfd56ddbf5593f57ce4bc5e0`;
- live correction `QFORM-UV-CONDITIONAL-CAP-FALSE`: account02/B03 canonical source commit `0d99f085f5378d267057cc5b9bcbf8e53ca494b5`.

No external theorem beyond the already source-reviewed dependencies is needed for the new falsifiers or compound ledger.
