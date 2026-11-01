# fleet03/B07 — Plucker conditioning collar and bounded-depth localization

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Run: `fleet03-B07-20260922T124045Z-qform-minors-v11`  
Assignment: coordinate minor selection / GEOMETRY  
Classification: `ESSENTIAL_STEP_APPLIED / RANK_THREE_REDUCTION`; full conjecture remains `OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Exact target and scope

The full owner target is: for independent real coordinates with scalar densities bounded by one and an arbitrary real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a universal essential-density bound for `X^T A X`.

This report proves a dimension-free aggregate coordinate-selection theorem for the rank-exactly-three spectral core

`A = U Lambda U^T`, `U^T U = I_3`, `|det Lambda| >= 1`,

with no alignment between `U` and the independent coordinates and with arbitrary signs of `Lambda`. It does not remove a general correlated additional spectral remainder. The result uses aggregate Plucker mass rather than selecting one large principal minor.

Current corrections are respected: no law-uniform pointwise one-dimensional Fresnel decay is used; no rotated spectral coordinate is declared independent; no unrestricted fiber supremum is used; and no claim is based on one cross/minor alone.

The designated partner `fleet04/B07` had no completed current-QFORM handoff at the fresh source snapshot. No result was fabricated. A compatible completed other-account theorem actually used below is fleet04/B18's `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, source commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`. I also use the source-pinned fleet03/B06 spectral-row computation, which itself applies that partner theorem.

## 2. Aggregate Plucker mass is exactly the retained spectral volume

Write the row vectors of `U` as `u_i^T in R^3`. For every triple `S` define

`w_S = det(U_S)^2 >= 0`.

By Cauchy-Binet,

`sum_{|S|=3} w_S = det(U^T U)=1`.                                            (2.1)

For any retained original-coordinate set `R subset [n]`, put

`G_R = U_R^T U_R`, `q_R = det G_R`.

Again by Cauchy-Binet,

`q_R = sum_{S subset R, |S|=3} w_S`.                                         (2.2)

Thus `q_R` is an aggregate determinant mass, not one small principal minor. When `q_R>0`, whiten the retained frame by

`W_R = U_R G_R^{-1/2}`, so `W_R^T W_R=I_3`.

For `i in R`, its normalized retained leverage is

`ell_i(R)=u_i^T G_R^{-1}u_i`.                                                (2.3)

The matrix determinant lemma gives the exact decrement identity

`q_{R\{i}} = q_R (1-ell_i(R))`.                                              (2.4)

Combining (2.2) and (2.4),

`ell_i(R)
 = [sum_{S subset R, |S|=3, i in S} w_S] / q_R`.                             (2.5)

So `ell_i(R)` is literally the conditional inclusion probability of coordinate `i` under the size-three volume-sampling law with weights `w_S`, conditioned on the sampled triple lying inside `R`.

This identity is the main source-valid replacement for a “pick one good principal minor” argument.

## 3. Conditioning preserves original-coordinate independence and pays the whole aggregate mass

Let `H=R^c` and condition on the actual original coordinates `X_H`. Put

`z = U_H^T X_H`.

Then

`Q = (U_R^T X_R + z)^T Lambda (U_R^T X_R + z)`.

With `Y=W_R^T X_R` and

`Lambda_R = G_R^{1/2} Lambda G_R^{1/2}`,                                     (3.1)

we have

`U_R^T X_R = G_R^{1/2}Y`,

and the conditional form is

`Y^T Lambda_R Y + beta^T X_R + constant`,                                    (3.2)

for an explicit linear coefficient vector `beta` depending on the conditioned outside coordinates. The retained `X_i`, `i in R`, are still the original independent coordinates.

Moreover

`|det Lambda_R| = q_R |det Lambda|`.                                          (3.3)

Assume now

`max_{i in R} ell_i(R) <= 1/2`.                                               (3.4)

For completeness, the needed diffuse estimate can be derived directly on (3.2). For fixed Fourier frequency `t`, replace each retained scalar density by the complex amplitude

`h_{i,t}(x)=f_i(x) exp(i t beta_i x)`.

Its every `L^p` norm is unchanged. The geometric rank-one Brascamp-Lieb inequality applied to the rows of `W_R`, followed by sharp Hausdorff-Young at exponents `q_i=1/ell_i>=2`, gives

`||hat g_t||_1 <= (2 pi)^3 B(W_R)`,

where

`B(W_R)=prod_i (1-ell_i)^(-(1-ell_i)/2) <= exp(3/2)`.                          (3.5)

Quadratic Gaussian regularization/Fresnel inversion then yields

`|phi_Q(t)| <= min(1, B(W_R) pi^(3/2) |det Lambda_R|^(-1/2)|t|^(-3/2))`.      (3.6)

Integrating the right side and Fourier-inverting gives

`||p_Q||_infinity <= 3 B(W_R)^(2/3)|det Lambda_R|^(-1/3)
                   <= 3e (q_R |det Lambda|)^(-1/3)`.                         (3.7)

The bound is uniform in the outside conditioning value, so averaging the conditional densities preserves it. This is the linear-perturbation specialization of the independently supplied `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`; the calculation is included here to make the exact determinant payment explicit.

### Aggregate collar corollary

If `q_R>=1/8`, `max ell_i(R)<=1/2`, and `|det Lambda|>=1`, then

`boxed( ||p_Q||_infinity <= 6e. )`                                            (3.8)

Thus a retained eighth of total Plucker mass is already enough, provided the whitened retained frame is diffuse.

## 4. Recursive minority-pivot gate using the completed fleet04 theorem

At a retained state `(R,G_R)`, let `w_i^T` be the `i`th row of `W_R`. Its scalar quadratic pivot in the effective matrix `Lambda_R` is

`w_i^T Lambda_R w_i = u_i^T Lambda u_i = A_ii`.                              (4.1)

So the original physical diagonal pivot is invariant under this conditioning/whitening step. Also `Lambda_R` has the same inertia as `Lambda` by congruence.

For a rank-three indefinite form of inertia `(2,1)` or `(1,2)`, suppose `i` is a retained row with leverage `ell_i(R)>0`, and `A_ii` has the minority sign. Then its spectral Schur complement is definite. The source-pinned fleet03/B06 calculation gives the residual two-dimensional product-projection density bound, and applying fleet04/B18's completed dependent-square-smoothing lemma gives

`||p_Q||_infinity
 <= 2 sqrt(2 pi) /
    ( ell_i(R) q_R |det Lambda| |A_ii| )^(1/4).`                             (4.2)

The key use of fleet04/B18 is genuine: after completing the original scalar coordinate, the translated square is not independent of the residual quadratic value, and the dependent version is exactly what permits (4.2).

Hence if

`q_R>=1/8`, `ell_i(R)>1/2`, `|det Lambda|>=1`,

and `A_ii` is minority-sign with `|A_ii|>=tau`, then

`||p_Q||_infinity <= 4 sqrt(2 pi) tau^(-1/4)`.                               (4.3)

For the concrete threshold `tau=1/2`, the right side is approximately `11.924`, below `6e approximately 16.310`.

## 5. Bounded-depth Plucker localization theorem

We now attack the first unpaid coordinate-selection implication directly.

Fix `delta=1/8` and `tau=1/2`. Start from `R_0=[n]`, `H_0=empty`, `q_0=1`. At stage `k`, with `q_k>=delta`:

1. If every normalized leverage is at most `1/2`, apply the aggregate collar (3.8) and stop.
2. Otherwise choose a row `i_{k+1}` with `ell_{i_{k+1}}(R_k)>1/2`.
3. If its pivot has the minority sign and `|A_{i_{k+1}i_{k+1}}|>=1/2`, apply (4.3) and stop.
4. Otherwise set `q_{k+1}=q_k(1-ell_{i_{k+1}}(R_k))`. If `q_{k+1}<1/8`, stop and declare the ordered localized set `J={i_1,...,i_{k+1}}`. If not, delete that coordinate and continue.

Every actual deletion satisfies

`q_{k+1}<q_k/2`.                                                              (5.1)

Therefore after at most three selected heavy coordinates the process must have stopped: if three consecutive heavy deletions were attempted then

`q_3<1/8`.                                                                    (5.2)

This proves the following.

### Theorem `QFORM-PLUCKER-COLLAR-TRICHOTOMY-v1`

For every rank-exactly-three indefinite `A=U Lambda U^T` with all three nonzero eigenvalues of magnitude at least one and every independent input law with scalar densities bounded by one, at least one of the following holds:

**(D) Diffuse aggregate collar.** The output density is bounded by `6e` via a retained original-coordinate set carrying at least `1/8` of the total Plucker mass.

**(P) Minority-pivot payment.** The output density is bounded by

`4 sqrt(2 pi) 2^(1/4) < 11.924 < 6e`

through a heavy conditional row and fleet04/B18 dependent square smoothing.

**(L) Localized exceptional chain.** There is an ordered set `J=(i_1,...,i_m)`, `1<=m<=3`, such that

`det(U_{J^c}^T U_{J^c}) < 1/8`,                                               (5.3)

and every selected coordinate was a strict conditional majority:

`u_{i_k}^T G_{k-1}^{-1}u_{i_k} > 1/2`,                                       (5.4)

where `G_{k-1}=U_{R_{k-1}}^T U_{R_{k-1}}`. Each selected pivot additionally fails the paid gate, so it is either majority-sign or satisfies

`|A_{i_k i_k}|<1/2`.                                                         (5.5)

The localized branch has a further spectral consequence. Since

`U_{J^c}^T U_{J^c}=I-U_J^T U_J`

has determinant below `1/8` and all its eigenvalues lie in `[0,1]`, at least one eigenvalue is below `1/2`. Hence there is a unit spectral direction `e in R^3` with

`boxed( ||U_J e||_2^2 > 1/2. )`                                               (5.6)

So the only rank-three indefinite forms not already paid by the aggregate collar or the minority-pivot gate have more than half of one spectral direction concentrated on at most three original coordinates, together with a nested conditional-majority certificate and majority/near-light-cone pivot restrictions.

This is dimension-free and does not rely on a single principal minor.

## 6. Exact sanity check: rational Hadamard frame

Take the first three normalized columns of the `4 x 4` Hadamard matrix, so the four rows are

`(1,1,1)/2`, `(1,-1,1)/2`, `(1,1,-1)/2`, `(1,-1,-1)/2`.

All four triple Plucker weights are exactly `1/4`; their sum is one. Every original row leverage is `3/4`, so the full frame is not diffuse. Delete the first row: the retained aggregate mass is exactly `1/4`, and because only three rows remain in a rank-three frame, every whitened retained leverage is exactly one. A second heavy deletion drives the retained determinant to zero. Thus the greedy theorem returns a two-coordinate localized set, exactly as predicted.

The accompanying Fraction-only checker verifies these identities without floating-point arithmetic. It is a sanity check of the algebra, not a substitute for the proof.

## 7. What was actually gained and what remains

The previous coordinate-minor obstruction was that no one fixed physical minor need be large; delocalized Hadamard-type frames make that false. The new mechanism never asks for one. It tracks the complete Cauchy-Binet mass through actual original-coordinate conditioning and converts either a constant amount of retained determinant mass into a density bound or, after at most three failures, into a finite-coordinate localization certificate.

The first rank-three unpaid implication is now sharply finite-dimensional:

`QFORM-LOCALIZED-MAJORITY-CHAIN-v1` — control branch (L), where at most three original coordinates form a conditional-majority chain and each selected pivot is majority-sign or within `1/2` of the spectral light cone. This interfaces directly with the existing heavy-row/near-isotropic work of fleet03/B10; its leverage-one isotropic endpoint is already paid, but the dependent leakage branch remains open.

For the **full owner target**, a separate interaction debt remains: if `A` has additional spectral components beyond the chosen three large directions, those terms are generally nonseparable and correlated with the rank-three core. The present theorem does not permit convolving or conditioning them away. Closing that remainder interaction, together with the localized majority-chain branch, is still required.

## 8. Source ledger and status

Fresh control remained owner revision `2026-09-22.5` before publication. Correction inbox retained `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`.

Applied compatible other-account mathematics:

- fleet04/B18, `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, full source `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Additional source-pinned inputs:

- fleet03/B06 spectral-row Schur smoothing, `yspennstate/math-open-problems@6853fe0b03502a11750096e7a21e650bebb4fe6d`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T122731Z-fleet03-B06-qform-curved-trace-v2/REPORT.md`;
- diffuse/separable Fourier mechanism, source report `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, path `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`; only the linear-perturbation specialization needed here is rederived in Section 3.

The designated `fleet04/B07` slot had no completed current-programme handoff at the final prepublication source check. Full QFORM remains `OPEN / NOT PROVED`.
