# fleet02/B07 — Pluecker flag decomposition for three large spectral directions

**Status:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / FULL_TARGET_OPEN`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** coordinate-minor selection  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Target, corrections, and source pins

Target: for independent real coordinates `X_i` with densities `0<=f_i<=1` and real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^TAX` has a universally bounded density, or produce a genuine counterexample.

The current correction set is applied. In particular, law-uniform pointwise one-dimensional Fresnel decay is false; naive spectral-fiber suprema can lose dimension; rotations do not preserve coordinate independence; a nonsingular cross block alone does not imply bounded density; and the diagonal `pi` constant is not a universal constant for all rotated forms. None of those challenged premises is used below.

Source pins actually used:

1. fleet01/B08, `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, `yspennstate/math-open-problems@fce159beaecf924a3e500dc7865ae61f8b35c932`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260922T114116Z-fleet01-B08-qform-r11/REPORT.md`. It proves a `3e` density bound for a `k>=3` diffuse orthonormal frame with row leverage at most `1/2`, even after arbitrary coordinate-separable phases.
2. fleet03/B05, `yspennstate/math-open-problems@c828d2ee2f8acef5eb96892bc8a9a25594db0f51`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260922T113800Z-fleet03-B05-qform-r11/REPORT.md`. It independently supplies the small-leverage Fresnel--Brascamp--Lieb mechanism and explicitly uses the previous B07 Walsh stress family.
3. Previous own B07 result, `yspennstate/math-open-problems@7ba557b8854ea86dcdc22a342d6fdd73d6882c6a`, established the exterior-power determinant-mass identities and the failure of fixed-size principal-block extraction on a rank-three Walsh projection.

The assigned partner is `fleet03/B07`. No completed current-programme handoff from that slot was visible at the fresh partner checks, so no partner result is fabricated or awaited.

## 2. Exact Pluecker accounting

Select three orthonormal eigenvectors corresponding to three eigenvalues of magnitude at least one. Write

`B = U Lambda U^T`, `U^T U=I_3`, `min_j |lambda_j|>=1`,

where the `i`th row of `U` is `u_i^T` and `c_i=||u_i||^2`. Thus

`sum_i c_i = 3`.

Fix

`theta=1/16`,

and split the original coordinates into

`H={i:c_i>theta}`, `L=H^c`.

Then `|H|<48`, hence `|H|<=47`. Define the light covariance in the three-dimensional spectral coordinate space

`S = sum_{i in L} u_i u_i^T = I_3 - sum_{i in H} u_i u_i^T`.

Cauchy--Binet gives the exact identity

`sum_{I subset L, |I|=3} det(U_I)^2 = det S`.                 (2.1)

For every three-coordinate principal compression of the selected rank-three form,

`det B[I,I] = det(Lambda) det(U_I)^2`,

so

`sum_{I subset L, |I|=3} |det B[I,I]| = |det Lambda| det S`.   (2.2)

Thus `det S` is not merely a leverage proxy: it is exactly the fraction of the rank-three principal-determinant `L^1` mass that lies wholly among light original coordinates.

## 3. Diffuse determinant-mass branch: a quantitative density theorem

### Theorem 3.1

Assume

`det S >= 1/8`.                                               (3.1)

Let the full matrix have the form

`A = C + U Lambda U^T`,

where the light-light compression `C[L,L]` is diagonal in the original coordinates. No restriction is imposed on `C[H,H]` or `C[H,L]`.

Then for every independent input vector with coordinate densities bounded by `1`, the law of `X^TAX` has a continuous density satisfying

`||p||_infinity <= 24 e`.                                     (3.2)

In particular, (3.2) holds for every `A=D+U Lambda U^T` with arbitrary diagonal `D`.

### Proof

Let `s_1<=s_2<=s_3<=1` be the eigenvalues of `S`. Since `det S=s_1s_2s_3<=s_1`, (3.1) implies

`S >= (1/8) I_3`.                                             (3.3)

Condition on all heavy coordinates `X_H`. In the remaining light variables, all heavy-light terms are linear coordinate-separable phases and `C[L,L]` is diagonal, so the conditional quadratic polynomial is

`x_L^T U_L Lambda U_L^T x_L + sum_{i in L} V_i(x_i) + const`,  (3.4)

with arbitrary measurable quadratic/linear one-coordinate functions `V_i` depending parametrically on the conditioned heavy values.

Whiten the light spectral frame:

`v_i = S^{-1/2} u_i`, `i in L`.

Then

`sum_{i in L} v_i v_i^T=I_3`,

and by (3.3),

`||v_i||^2 <= ||S^{-1}|| c_i <= 8/16 = 1/2`.                  (3.5)

The transformed three-dimensional quadratic matrix is

`M=S^{1/2} Lambda S^{1/2}`.

It is invertible and

`||M^{-1}|| = ||S^{-1/2} Lambda^{-1} S^{-1/2}|| <= 8`,

so every eigenvalue of `M` has absolute value at least `1/8`. Factor out `1/8` from the entire conditional polynomial (absorbing the correspondingly rescaled one-coordinate terms into the arbitrary `V_i`). The fleet01/B08 separable-phase theorem applies to the whitened frame and gives conditional density at most `3e` for the scaled variable. Scaling back multiplies the density bound by `8`, proving the uniform conditional bound `24e`. Averaging the conditional densities over `X_H` preserves this bound; dominated convergence also preserves continuity. QED.

This result is singular-safe in the probabilistic sense needed here: it never divides by a value of the random quadratic form and it does not assume a nonsingular realization of `A` outside the selected three-dimensional spectral part.

## 4. What failure of the diffuse branch really gives: a spectral flag

Suppose now

`det S < 1/8`.                                               (4.1)

Because all eigenvalues of `S` lie in `[0,1]`, (4.1) implies that at least one eigenvalue is below `1/2`. Let

`q = #{j : s_j < 1/2}`, so `q in {1,2,3}`.

Let `F` be the `q`-dimensional span of the corresponding eigenvectors of `S`, and `E=F^perp`. Put

`G=I-S=sum_{i in H}u_i u_i^T`.

On `F`, all eigenvalues of `G` exceed `1/2`. Therefore the covariance of the projected heavy rows `P_F u_i` has determinant greater than `2^{-q}`. By Cauchy--Binet in dimension `q`,

`sum_{J subset H, |J|=q} Vol_q(P_F u_J)^2 > 2^{-q}`.          (4.2)

Since `|H|<=47`, some heavy `q`-tuple obeys the explicit lower bound

`Vol_q(P_F u_J)^2 > 2^{-q} / binom(47,q)`.                    (4.3)

Numerically/exactly this yields

- `q=1`: one heavy row has squared projection on the localized line greater than `1/94`;
- `q=2`: one heavy pair has projected area squared greater than `1/4324`;
- `q=3`: one heavy triple has spectral volume squared greater than `1/129720`.

At the same time, on the complementary light spectral subspace `E`, every eigenvalue of the light covariance is at least `1/2`. Whitening the projected light rows therefore produces an orthonormal `(3-q)`-frame with normalized row leverage at most

`2 theta = 1/8`.                                             (4.4)

So failure of the three-dimensional diffuse determinant branch does **not** mean that all three spectral directions become localized. It yields an exact rank-adaptive decomposition:

`q localized spectral directions carried quantitatively by <=47 heavy coordinates`

plus

`3-q genuinely diffuse spectral directions carried by the light coordinates`.  (4.5)

This is the correct geometric successor to fixed-principal-minor selection. The remaining analytic debt is to combine the two pieces without destroying independence or losing the arbitrary nonseparable residual phase.

## 5. Exact falsifier for the tempting bounded-block strengthening

The following source-valid family refutes the stronger claim

> if the three-dimensional light determinant mass collapses, then some bounded number of original coordinates captures a fixed positive fraction of the rank-three determinant mass.

For an integer square `m`, take an `n=(2m+1)` by `3` orthonormal-column frame with rows

`e_1`,

`m` copies of `e_2/sqrt(m)`,

`m` copies of `e_3/sqrt(m)`.

For `m>16` and threshold `1/16`, the heavy set consists only of the first row. The light covariance is

`S=diag(0,1,1)`, so `det S=0`.

Every nonzero three-row determinant must use the heavy `e_1` row, one `e_2` row, and one `e_3` row. Each squared determinant equals `1/m^2`, and there are `m^2` of them, so the total Pluecker mass is exactly one.

For any subset of at most `K` original coordinates, the determinant mass it can capture is at most

`floor((K-1)^2/4) / m^2`,                                   (5.1)

which tends to zero for every fixed `K` as `m` tends to infinity. Thus a bounded-size `3x3` principal-minor search is genuinely invalid even after the diffuse branch fails. One direction can be perfectly localized while the complementary two-dimensional area mass remains arbitrarily diffuse.

This is a counterexample to an intermediate coordinate-selection shortcut, **not** to the quadratic-form density conjecture.

The exact rational instance `m=64` was checked by `check_plucker_flag.py`. It has 129 rows, Gram matrix exactly `I_3`, heavy set of size one, `S=diag(0,1,1)`, exactly 4096 nonzero Pluecker weights each equal to `1/4096`, and total mass exactly one. The captured masses for `K=3,5,9,17` are respectively `1/4096, 1/1024, 1/256, 1/64`. The checker ends `PASS`.

## 6. Conditional end-to-end route and first unpaid implication

A compact route consistent with all current corrections is now:

1. choose three large spectral directions and form the original-coordinate row frame `U`;
2. apply the exact heavy/light Pluecker decomposition above;
3. if `det S>=1/8`, use whitening plus the fleet01/B08 separable-phase Fourier--Brascamp--Lieb theorem; this already closes rank-three-plus-coordinate-separable residuals with constant `24e`;
4. if `det S<1/8`, use the rank-adaptive flag `(F,E)`: `q` localized directions have an explicit finite-coordinate exterior-volume witness, while `3-q` light directions remain quantitatively diffuse;
5. combine the localized physical smoothing and diffuse Fourier/curved smoothing in a way that retains the original product law and tolerates the arbitrary spectral residual.

The first B07-specific unpaid implication is therefore

`QFORM-PLUCKER-FLAG-HYBRID-v1`:

> Prove a dimension-free small-ball/density estimate on the `q=1` and `q=2` flag branches by combining the explicit heavy-coordinate `q`-volume witness (4.3) with the whitened diffuse `(3-q)`-frame (4.4), without conditioning away a singular factor and without assuming the residual quadratic phase is coordinate-separable. The family in Section 5 is a mandatory stress test.

A separate global interface, already isolated by fleet01/B08 and fleet03/B05, is `QFORM-DIFFUSE-RESIDUAL-COUPLING-v1`: arbitrary spectral complements are generally nonseparable in the original coordinates. The present report does not solve that debt.

## 7. Classification

`ESSENTIAL_STEP_APPLIED`: exact Pluecker mass is converted into a quantitative heavy/light spectral-flag dichotomy, and a genuine density theorem with explicit constant `24e` is proved on the diffuse determinant branch with coordinate-separable light residual.

`CANDIDATE_REFUTED`: the stronger bounded-coordinate-set determinant-mass extraction shortcut is false by the exact family in Section 5.

`FULL_TARGET_OPEN`: arbitrary residual coupling and the localized/diffuse hybrid branches remain unpaid. No full proof or target-level counterexample is claimed.
