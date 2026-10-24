# account01/B11 — deletion-normalized diffuse closure for indefinite exact rank three

Run: `QFORM-B11-20260922T201417Z`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: indefinite signatures `(+,+,-)` / `(+,-,-)`  
Outcome: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and conditional end-to-end position

The full target remains open: for arbitrary independent real inputs with one-dimensional densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X` (and separately continuity), or produce a valid counterexample.

This run attacks the exact-rank-three heavy-coordinate indefinite chamber left after the physical-pair/ray-atom mechanisms. The compact conditional route in this chamber is:

1. If an exact projective ray carries quantitative saddle energy, apply completed partner `account02/B11` theorem `QFORM-HEAVY-NULL-RAY-ATOM-v1`.
2. If, after deleting the heavy original coordinate and renormalizing the residual rank-three frame, every residual leverage is at most `1/2`, apply the new theorem below. It is product preserving because the conditioning is on one ORIGINAL independent coordinate.
3. The residual unpaid chamber is therefore simultaneous failure of these two certificates: no quantitative exact-ray atom, and either near-total heavy leverage or a leverage-heavy normalized residual frame. No post-rotation conditional cap is introduced.

The theorem below is sign-free, hence covers both `(+,+,-)` and `(+,-,-)` exact-rank-three signatures.

## 2. Sources actually used

### 2.1 Diffuse separable-phase theorem

Canonical source:

`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`

`proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

Its exact rank-`r` statement used here is: if `U^T U=I_r`, every row leverage `c_i=||u_i||^2<=1/2`, `Lambda` is invertible symmetric, and the independent cap-one original coordinates carry arbitrary coordinate-separable measurable real phases, then

`T=(U^T X)^T Lambda(U^T X)+sum_i V_i(X_i)`

has a bounded continuous density and

`||p_T||_infinity <= [e r/(r-2)] |det Lambda|^(-1/r)`.

For `r=3` this is `3e |det Lambda|^(-1/3)`. The proof supplies a characteristic-function envelope uniform in the separable terms, which is important for averaging over the conditioned heavy coordinate below.

### 2.2 Assigned partner result actually applied

Latest completed assigned-partner result read in this run:

`account02/B11`, run `20260922T192814Z-b11-qform-70f57503`, canonical proof

`yspennstate/math-open-problems@2c065b1bb6a45a479bd2ac5d3405cd59e7bafe8f`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T192814Z-b11-qform-70f57503/REPORT.md`.

In its heavy-null exact-rank-three normal form, with smallest nonzero singular value at least `s` and largest exact-ray saddle coefficient `alpha`, it proves

`||p_Q||_infinity <= s^(-1) max(C1 alpha^(-3/4), C2 alpha^(-5/6))`,

where

`C1=128*2^(1/8)*e^(9/8)<429.953`,
`C2=3*400^(1/3)*2^(7/12)*e^(7/12)<59.350`.

It also constructs the harmonic Parseval family used in Section 5 below to show that `alpha` can tend to zero.

## 3. New theorem: delete one physical coordinate, then renormalize the residual frame

### Theorem 3.1 — `QFORM-HEAVY-DELETE-DIFFUSE-v1`

Let `R` be an `n x 3` real matrix with orthonormal columns, `R^T R=I_3`. Let `M` be an invertible real symmetric `3 x 3` matrix, and put

`A=R M R^T`.

Let `X_0,...,X_(n-1)` be independent real random variables with densities bounded by one. Pick one ORIGINAL coordinate, called `0`, and write its spectral row as `r_0^T`. Put

`h=||r_0||^2 <1`,
`I={1,...,n-1}`,
`G=R_I^T R_I=I_3-r_0 r_0^T`,
`U=R_I G^(-1/2)`.

Assume the normalized residual frame is diffuse:

`max_(i in I) ||u_i||^2 <=1/2`,

where `u_i^T` is row `i` of `U`.

Then `Q=X^T A X` has a bounded continuous density and

`||p_Q||_infinity <=3e [(1-h)|det M|]^(-1/3)`.                  (3.1)

If every singular value of `M` is at least `s>0`, then

`||p_Q||_infinity <=3e s^(-1)(1-h)^(-1/3)`.                     (3.2)

The result is independent of the inertia of `M`; in particular it applies to both indefinite rank-three signatures.

### Proof

Because `R^T R=I_3`, deleting row `r_0` gives

`G=R_I^T R_I=I_3-r_0 r_0^T`.

Since `h<1`, `G` is positive definite: it has eigenvalue `1-h` in the direction of `r_0` and eigenvalue `1` on the orthogonal two-plane. Hence

`det G=1-h`.                                                     (3.3)

By construction,

`U^T U=G^(-1/2) R_I^T R_I G^(-1/2)=I_3`.                       (3.4)

Condition on the ORIGINAL coordinate `X_0=x`. This preserves independence and the cap-one densities of every `X_i`, `i in I`. Expanding the quadratic form gives

`Q | (X_0=x) = X_I^T (R_I M R_I^T) X_I + 2x A_(0,I) X_I + x^2 A_00`.

Using `R_I=U G^(1/2)`, the quadratic part is

`R_I M R_I^T = U Lambda U^T`,
`Lambda=G^(1/2) M G^(1/2)`.                                     (3.5)

The term `2x A_(0,I)X_I` is a sum of one-coordinate linear functions of the independent residual variables, and the final term is a constant. Thus, for each fixed `x`, the completed diffuse separable-phase theorem applies to (3.5), with the SAME normalized frame `U` and the same `Lambda`. Its bound is uniform in `x`:

`||p_(Q | X_0=x)||_infinity <=3e |det Lambda|^(-1/3)`.          (3.6)

Now

`|det Lambda| = det(G) |det M| = (1-h)|det M|`.                 (3.7)

Averaging (3.6) in `x` proves (3.1). Since `|det M|>=s^3`, (3.2) follows.

For continuity one should not rely merely on pointwise mixtures of conditional densities. Instead use the actual Fourier estimate supplied by the separable-phase theorem: for every fixed `x`, the characteristic function has a common integrable envelope depending only on `U` and `Lambda`, not on the induced linear terms. Averaging the conditional characteristic functions over `X_0` preserves that common `L^1(dt)` envelope. Fourier inversion therefore gives a bounded continuous unconditional density vanishing at infinity. QED.

## 4. Why this is a genuinely indefinite third-direction mechanism

The rank-two opposite-sign obstruction remains: even for cap-one independent uniforms, a product such as `UV` has a logarithmically divergent density at zero. The present theorem does not erase that control example.

For the residual rank-three frame, the diffuse complex-amplitude/Fresnel theorem supplies a joint `|t|^(-3/2)` characteristic envelope after product aggregation. This is integrable in time. In rank two the analogous exponent is only `|t|^(-1)`, which is exactly the borderline logarithmic failure. Thus, in this branch, the third direction removes the saddle singularity by contributing the third half-power only after the ORIGINAL product structure has been aggregated through the normalized residual frame; no false one-dimensional pointwise van-der-Corput estimate is used.

The price `(1-h)^(-1/3)` in (3.1) is honest. It records the determinant lost when the heavy physical row is deleted. The theorem therefore does not by itself close the near-total-heavy case `h ->1`.

## 5. Apply the assigned partner theorem to its angularly diffuse obstruction family

The partner's source-valid obstruction takes `h=3/4`, `m>=5`, angles `theta_j=2 pi j/m`, heavy row

`r_0=(sqrt(3)/2,0,0)`,

residual rows

`r_j=(1/(2 sqrt(m)), sqrt(2/m) cos(theta_j), sqrt(2/m) sin(theta_j))`,

and

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`.

Then `R^T R=I_3`, the nonzero spectrum of `A=R M_0 R^T` is exactly `{-1,1,1}`, and the partner proves all residual projective rays are distinct with

`alpha=sqrt(2/m)`.

This family defeats any proof demanding a fixed exact ray atom or a fixed physical local pair. It is nevertheless uniformly controlled as follows.

First,

`G=I-r_0 r_0^T=diag(1/4,1,1)`,
`G^(-1/2)=diag(2,1,1)`.

Hence the normalized residual rows are

`u_j=(1/sqrt(m), sqrt(2/m) cos(theta_j), sqrt(2/m) sin(theta_j))`,

and every normalized residual leverage is exactly

`||u_j||^2 = 1/m + 2/m = 3/m`.                                  (5.1)

Therefore for every `m>=6`, (5.1) is at most `1/2` and Theorem 3.1 gives the uniform continuous-density estimate

`||p_Q||_infinity <=3e (1/4)^(-1/3)=3e 4^(1/3)<12.946`.          (5.2)

The single remaining size `m=5` is where I apply the assigned partner theorem to an actual inequality. Here `s=1` and `alpha=sqrt(2/5)`. Therefore

`C1 alpha^(-3/4)
 =128*2^(1/8)*e^(9/8)*(2/5)^(-3/8)
 <606.245`,

while the partner's second branch is `<86.941`. Thus

`||p_Q||_infinity <607`                                          (5.3)

for `m=5`.

Combining (5.2) and (5.3), the ENTIRE harmonic angularly diffuse obstruction family of the latest assigned partner, for every `m>=5`, has a dimension-free density bound `<607`; for all `m>=6` it has the much sharper continuous bound `<12.946`.

This is not a proof of the full conjecture: it pays the specific family that falsified the fixed-ray-atom shortcut and identifies the next structural chamber.

## 6. First remaining implication

The exact-rank-three heavy-null branch now has a concrete two-certificate cover:

- a quantitative exact projective ray is paid by the partner's ray-atom theorem;
- a diffuse deletion-normalized residual frame is paid by Theorem 3.1.

The first unpaid local implication is therefore:

`QFORM-HEAVY-RESIDUAL-LEVERAGE-COMPILER-v1`.

Given an exact-rank-three heavy-null indefinite frame for which the strongest exact-ray saddle energy tends to zero, prove a universal bound in the remaining case where either

`max_i r_i^T (I-r_0 r_0^T)^(-1) r_i >1/2`

or the deletion determinant `1-h` is arbitrarily small. The mechanism must preserve the original product coordinates and must not replace exact zero by a merely small Schur diagonal, invoke a conditional-density cap as independence, or discard small spectral coefficients using moments/support assumptions.

A plausible next move is a product-preserving high-residual-leverage peel: select the leverage-heavy residual ORIGINAL coordinate and combine its exact two-coordinate geometry with the full-matrix indefinite-pair theorem; if this fails because the associated saddle coefficient is small, use the remaining residual diffuse mass before paying the reciprocal minor. The present run does not claim this compiler is proved.

For the full arbitrary-rank target, an additional aggregation step is still required to pass from this exact-rank-three chamber to arbitrary extra spectrum. Existing full-matrix physical-pair and ridge/separable results cover important exits but do not establish an exhaustive structural dichotomy.

## 7. Corrections explicitly respected

The argument does NOT use any of the following refuted interfaces:

- law-uniform pointwise van-der-Corput decay for one-dimensional quadratic phases;
- arbitrary-joint three-dimensional coarea density control;
- a positive moment of worst conditional projection density;
- bounded conditional density as a substitute for independence;
- a single uniformly conditioned physical minor forced by three large eigenvalues;
- extension of an exact-zero half-Riesz mechanism to a merely small diagonal.

Conditioning occurs only on an ORIGINAL independent coordinate, so the residual variables remain genuinely independent. The harmonic-family computation is exact algebra, not Monte Carlo evidence.

## 8. Verification scope

A finite algebraic sanity check was run for the harmonic family for `m=5,...,12`: it verified `R^T R=I_3`, `G=diag(1/4,1,1)` up to floating error, `U^T U=I_3`, and the exact leverage formula `3/m`; it also evaluated the displayed constants. This check is not a universal proof certificate. The proof of Theorem 3.1 is the analytic argument in Section 3.

Continuity status: PROVED for Theorem 3.1 and hence for the harmonic family when `m>=6`; the partner bound used for `m=5` is only used here as an essential-density bound, so continuity is not asserted from that branch. Full-target continuity remains open with the full target.
