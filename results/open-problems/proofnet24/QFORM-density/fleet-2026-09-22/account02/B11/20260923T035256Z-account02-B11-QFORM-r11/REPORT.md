# B11 report — heavy near-null angular clustering on the two-sheet branch

Programme: `QFORM-DENSITY-3EIG-20260922`.  Worker: account02/B11.  Status: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_REDUCTION / SOURCE-VALID STRUCTURAL FALSIFIER / FULL TARGET OPEN**.  Execution remains `WITHOUT_VERIFIED_BRAIN`.

The target throughout is the universal essential-density bound for `X^T A X` under arbitrary independent one-dimensional density caps `<=1` and at least three eigenvalues of `A` of magnitude at least one.  No moment, support, log-concavity, diagonal-basis, or post-rotation independence hypothesis is used.  Continuity is separate.

## 1. Sources actually used

1. Required Claude package, pinned source
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, Theorem F.  I also read its `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md`.  The current compatible `RESULTS.md` still contains the same Theorem F.  The actual inequality used below is

   `max_i ||r_i||^2 <=1/2  ==>  ||p_Q||_infinity <=12 |det Lambda|^(-1/3)`

   for an exact rank-three spectral frame.  The `COUNTEREXAMPLE_SEARCH.md` ruled theorem is also used to identify the already-paid one-sheet side: for signature `(2,1)`, `p_Q(s)<=pi sqrt(2)` for every `s>=0`.

2. Orientation-free rank-three scalar-pivot theorem,
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, equation (1.2):

   `||p_Q||_infinity <=128 [c_i |A_ii| |det Lambda|]^(-1/4)`

   for an original physical row of leverage `c_i` in an exact-rank-three block, with arbitrary outside affine terms/couplings.

3. Determinant-only physical-pair theorem,
   `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,
   `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, Theorem 3.1.  If an ORIGINAL indefinite physical `2x2` block has `D=|det B|` and the ambient `s_3(A)>=s`, then

   `||p_Q||_infinity <= D^(-1/2)[9.2+log_+(10000 sqrt(D)/s)]`.

   Its proof explicitly retains the logarithmic hyperbolic pair density and uses the third-direction Schur remainder to integrate the logarithm.

4. Designated partner account03/B11 r22,
   `yspennstate/math-open-problems@3a8e3494dac898f3b7180d5b80a8c5eb974a8412`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T021243Z-account03-B11-QFORM-r22/REPORT.md`.  Its full-matrix opposite-diagonal exit is applied in Section 5 below.

No source above is promoted to a full-QFORM result.

## 2. New theorem: heavy-null angular pair reduction

Let

`A=R Lambda R^T`, `R^T R=I_3`, `Lambda=diag(lambda_1,lambda_2,-mu)`,

with `lambda_1,lambda_2,mu>=1`.  Put `r_i` for row `i`, `c_i=||r_i||^2`, and `a_i=A_ii`.  Fix

`tau=1/64`.

Then at least one of the following occurs.

**(F) Diffuse frame.**  `max_i c_i<=1/2`, and

`||p_Q||_infinity <=12`.

**(P) Heavy fixed scalar pivot.**  Some `i` has `c_i>1/2` and `|a_i|>=tau`, and

`||p_Q||_infinity <431`.

**(H) Heavy separated near-null pair.**  Every heavy row has `|a_i|<tau`, but two heavy rows have associated Lorentz-null angles separated by at least `pi/3`; then their ORIGINAL physical `2x2` block is indefinite with

`|det A[{i,j},{i,j}]| >35/4096 >1/120`,

and hence

`||p_Q||_infinity <176`.

**(C) Single-cluster residual.**  Every heavy row has `|a_i|<tau`; after the deterministic spectral rescaling by `|Lambda|^(1/2)`, each heavy row lies within Euclidean distance `1/32` of the unit Lorentz null cone, and all corresponding projective null angles have circular diameter `<pi/3`.

Thus, modulo already-proved branches with constants `<431`, the exact-rank-three indefinite problem is reduced to a **single angular cluster of at most five heavy near-null ORIGINAL rows**.  The number five is immediate from `sum_i c_i=3` and `c_i>1/2`.

Reflection `A -> -A` gives the `(1,2)` version.  On the `(2,1)` side, Claude's ruled theorem already gives `p_Q(s)<=pi sqrt(2)` for `s>=0`, so the genuinely unpaid part of (C) is the two-sheet side `s<0`.

### Proof of (F) and (P)

(F) is the required Claude Theorem F with `G=I_3` and `|det Lambda|>=1`.

For (P), the rank-three scalar-pivot estimate gives

`||p_Q||_infinity <=128[c_i |a_i| |det Lambda|]^(-1/4)`

and the bracket is `>(1/2)(1/64)=1/128`.  Hence

`||p_Q||_infinity <128*128^(1/4)=430.538965...<431`.

### Lorentz normalization of a heavy near-null row

Assume now `c_i>1/2` and `|a_i|<tau`.  Put

`u_i=r_i/sqrt(c_i)`, `z_i=|Lambda|^(1/2)u_i`, `s_i=||z_i||`,
`y_i=z_i/s_i`, `J=diag(1,1,-1)`.

Since every absolute eigenvalue of `Lambda` is at least one, `s_i>=1`.  Also

`q_i:=u_i^T Lambda u_i=a_i/c_i`, so `|q_i|<2tau=1/32`,

and therefore

`delta_i:=y_i^T J y_i=q_i/s_i^2`, `|delta_i|<1/32`.

Orient `y_i` so its third coordinate is positive; this only chooses the sign of the projective row.  Write its spatial angle as `theta_i`.  A unit vector with Lorentz value `delta` has spatial radius `sqrt((1+delta)/2)` and time coordinate `sqrt((1-delta)/2)`.  The unit null vector with the same angle,

`n(theta)=(cos theta,sin theta,1)/sqrt(2)`,

therefore satisfies

`||y_i-n(theta_i)|| <= |delta_i| <1/32`.

Indeed each of the two radial errors is at most `|delta|/sqrt(2)`, by rationalizing the two square roots.  This proves the null-cone part of (C).

### Proof of the separated-pair exit (H)

Suppose two heavy rows `i,j` have null angles with circular separation `Delta>=pi/3`.  For future unit null vectors,

`n(theta_i)^T J n(theta_j)=-sin^2(Delta/2)`,

so its absolute value is at least `1/4`.  Since `||J||op=1`, the preceding `1/32` approximations give

`|y_i^T J y_j| >=1/4-1/32-1/32=3/16`.

Now

`b_ij:=u_i^T Lambda u_j=s_i s_j y_i^T J y_j`,

and `s_i,s_j>=1`, hence `|b_ij|>=3/16`.  The normalized `2x2` Lorentz Gram determinant obeys

`q_i q_j-b_ij^2 <= |q_i q_j|-b_ij^2`
`< 1/1024-9/256=-35/1024`.

Consequently the ORIGINAL physical principal pair has negative determinant and

`D=|a_i a_j-A_ij^2|`
`=c_i c_j |q_i q_j-b_ij^2|`
`> (1/4)(35/1024)=35/4096>1/120`.

This is an actual physical indefinite pair, not a rotated pair.  The determinant-only pair theorem with `s_3(A)>=1` now gives

`||p_Q||_infinity`
`<=sqrt(120)[9.2+log(10000/sqrt(120))]`
`=175.453002...<176`.

If this exit does not occur, every pair of heavy null angles has circular separation `<pi/3`, which is exactly the cluster statement (C).

## 3. The logarithmic rank-two singularity is retained

The separated-pair proof does **not** assert a bounded density for the rank-two saddle.  The source pair theorem first gives the translated hyperbolic envelope

`D^(-1/2)[5.2+log_+(16 sqrt(D)/|t-kappa|)]`.

After completing this ORIGINAL pair, the remaining Schur matrix has operator norm at least `s_3(A)>=1`.  The unrestricted one-eigenvalue small-ball estimate bounds the expected logarithm of the residual critical-value distance, yielding the finite `<176` number above.  Thus the third direction removes the rank-two logarithm precisely by integrating it against a quantitatively nontrivial Schur remainder.  The logarithmic singularity itself is not hidden or falsely declared bounded.

In the diffuse branch, the mechanism is different but equally explicit: Theorem F gives `|phi_Q(t)|=O(|t|^(-3/2))`, so all three quadratic directions jointly cross the Fourier integrability threshold.

## 4. Source-valid falsifier: small one-sign physical diagonals do not imply near-null rays

The previous reduction needs the leverage gate.  Without it, the tempting structural statement

> `max_i |A_ii| ->0` forces the normalized spectral rows toward the Lorentz null cone

is false even inside the exact target.

For any `m>=6`, let `theta_j=2pi j/m` and define the `m x3` frame rows

`r_j=(sqrt(2/m) cos theta_j, sqrt(2/m) sin theta_j, 1/sqrt(m))`,

and take `Lambda=diag(1,1,-1)`, `A_m=R Lambda R^T`.  The root-of-unity identities give

`R^T R=I_3`,

so `A_m` has exactly the nonzero eigenvalues `{-1,1,1}`.  Every physical leverage and diagonal are

`c_j=3/m`, `A_jj=1/m>0`.

Hence all physical diagonals have the **same sign** and tend uniformly to zero.  But the normalized spectral row is

`u_j=(sqrt(2/3) cos theta_j, sqrt(2/3) sin theta_j,1/sqrt(3))`,

whose Lorentz value is identically `1/3`; its Euclidean distance from the unit null cone is the fixed number

`sqrt(2-sqrt(4/3)-sqrt(2/3))=0.169714...`.

So absolute near-zero diagonals alone do not create near-null spectral geometry.  This is a counterexample only to that proposed intermediate implication, not to QFORM.  Since `c_j=3/m<=1/2`, the required Claude Theorem F applies to the actual family and gives

`boxed: ||p_{X^T A_m X}||_infinity <=12`

for every admissible cap-one product law, uniformly in `m`.  Thus the correct proof map is: **diffuse small diagonals are already paid; only high-leverage small diagonals force near-null geometry.**

The checker at `m=12` verifies Parseval error `2.22e-16`, nonzero spectrum `{-1,1,1}`, leverage `1/4`, diagonal `1/12`, and null-cone distance `0.169714...`.

## 5. Designated partner applied to the ambient full-matrix interface

Account03/B11 r22 proves for arbitrary rank that if two ORIGINAL physical diagonals obey

`A_ii>=eta`, `A_jj<=-eta`,

then

`||p_Q||_infinity <=eta^(-1)[9.2+log_+(10000 eta)]`.

At the same threshold `eta=tau=1/64`, this gives the actual bound

`||p_Q||_infinity <912.094`.

Therefore, after the designated-partner exit, any still-unpaid full-matrix indefinite branch has at most one physical diagonal sign at scale `1/64`.  This is compatible with the exact-rank-three reduction above: the latter then says that a genuinely difficult small-diagonal exact-rank-three survivor must contain a heavy near-null row and cannot be explained by the diffuse one-sign construction of Section 4.

## 6. What changed and what remains

The previous B11 endpoint was the broad “near-null one-sign physical-diagonal compiler.”  This run splits that chamber sharply:

* absolute-small diagonals with diffuse spectral leverage are closed by the required Claude Fresnel--Brascamp--Lieb theorem (`<=12`);
* a heavy row with a fixed nonzero pivot is closed by the orientation-free Schur/fractional theorem (`<431`);
* two heavy near-null rows on separated Lorentz rays force an ORIGINAL indefinite physical pair and are closed by the determinant-only logarithmic pair theorem (`<176`);
* the only exact-rank-three residual from these mechanisms is a **single cluster of at most five heavy near-null rows**, and Claude's ruled theorem already removes its one-sheet levels.

The first unpaid B11 implication is therefore

`QFORM-HEAVY-NULL-SINGLE-ARC-TWOSHEET-v1`:

> In exact rank three, control the two-sheet side when every heavy original row has `|A_ii|<1/64` and all heavy Lorentz-null directions lie in one arc of width `<pi/3`, while retaining the light rows nonperturbatively.  Use product-preserving hub/tangent averaging or force an existing physical-pair/ridge/volume exit.  Do not take a worst conditional slice and do not discard a small coefficient matrix as a small random quadratic perturbation.

Arbitrary additional nonseparable spectrum remains a separate interface to the full target.

## 7. Verification

`VERIFY.py` is an exact/numerical regression check, not a proof certificate.  It verifies the rational determinant lower bound `35/4096>1/120`, the pair constant `<176`, the fixed-pivot constant `<431`, the diffuse Parseval family, and existence of a compatible separated pair of heavy exact null rows.  Captured output ends

`QFORM_B11_HEAVY_NULL_CLUSTER_CHECK_PASS`.

Independent end-to-end review of this new reduction was not performed in this run.  Full QFORM remains OPEN.
