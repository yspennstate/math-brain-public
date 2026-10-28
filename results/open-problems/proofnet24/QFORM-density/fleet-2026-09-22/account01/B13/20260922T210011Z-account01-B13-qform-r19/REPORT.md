SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B13, 2026-09-22T21:00:11Z.
attacking: QFORM-RANK3-ONEHEAVY-LONGITUDINAL-RESIDUAL-v1 by keeping the heavy original coordinate inside the normalized rank-three product block instead of conditioning it away.

# Combined-block whitening pays a large part of the longitudinal-residual branch

**Run:** `20260922T210011Z-account01-B13-qform-r19`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_BRANCH / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full quadratic-form bounded-density conjecture remains OPEN. This report proves a new universal branch inside the exact-rank-three mixed geometry left after the designated partner `account02/B13` trichotomy and the preceding account01/B13 reductions. It does not use arbitrary-joint rank-three coarea, a positive conditional projection-density moment, post-rotation independence, law-uniform pointwise Fresnel decay, a fixed good minor, bounded support, bounded diameter, or a fixed fragment count.

## 1. Fresh source state and exact dependencies


The live `CORRECTION_INBOX.json` was reread at the prepublication source. In particular this argument does not use the refuted arbitrary-joint coarea estimate, the divergent conditional positive-moment bridge, conditional-cap-as-independence, bounded-diameter localization, fixed-fragment localization, or any law-uniform pointwise quadratic oscillatory decay.

The designated partner result actually applied is **account02/B13** run `20260922T182158Z-account02-B13-qform-4ebdd821`, canonical report

`yspennstate/math-open-problems@d511859edaa636cdc00fcd64155ab07506875c3d`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T182158Z-account02-B13-qform-4ebdd821/REPORT.md`.

It proves the exact-rank-three heavy/light trichotomy. For

`A=R Lambda R^T`, `R^T R=I_3`, `min |eig(Lambda)|>=1`,

put `c_j=||r_j||^2`, `H={j:c_j>3/10}`, `L=H^c`, and let the light Gram have eigenvalues `s_1>=s_2>=s_3`. The branches `s_3>=3/5` and `s_2<=3/5` are already universally paid; the only surviving Gram regime is

`boxed(s_3<3/5<s_2)`.

The same slot's earlier exact bang-bang theorem is

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b/REPORT.md`.

For every fixed quadratic slab it identifies the supremum over all independent cap-one mass-one densities with the supremum over arbitrary unit-measure product indicators, with zero loss. No interval extremality is inferred.

The preceding own geometric reduction is

`yspennstate/math-open-problems@01c524aa389abf1b9b58c852bfa11fc747ec5b59`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260922T190849Z-account01-B13-qform-r17/REPORT.md`.

Inside the mixed branch it chooses a heavy original coordinate `i` with

`r_i=sqrt(c) u`, `c>3/10`, `||u||=1`,

and writes every light row as

`r_j=q_j u+p_j`, `p_j in u^perp`.

With

`G=sum_(j in L) p_j p_j^T`,

it proves

`boxed((1/25) I_(u^perp) <= G <= I_(u^perp),   det G>=1/25).`       (1.1)

It also proves that if some normalized transverse leverage

`a_j:=p_j^T G^(-1)p_j`

is at least `1/32`, then the whole form already has a universal density bound `<8228`. Thus throughout the branch attacked below we may and do assume

`boxed(a_j<1/32 for every j in L).`                                  (1.2)

The analytic theorem used below is `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, canonical proof

`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`,
`proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

If a rank-three product projection has orthonormal columns and every physical-row leverage is at most `1/2`, then for arbitrary cap-one independent inputs, arbitrary coordinate-separable real perturbations, and invertible rank-three quadratic coefficient `M`,

`||p_T||_infinity <= 3e |det M|^(-1/3)`.                            (1.3)

Its physical-principal-block conditioning corollary permits arbitrary coefficients and cross-couplings outside the retained original-coordinate block.

## 2. Longitudinal regression coordinates

In the orthogonal decomposition `R u direct_sum u^perp`, write the light Gram as

`S=sum_(j in L) r_j r_j^T = [[s,h^T],[h,G]]`,                       (2.1)

where

`s=sum q_j^2`, `h=sum q_j p_j`.

Set

`ell=G^(-1)h`,
`w_j=q_j-ell^T p_j`,
`tau=s-h^T G^(-1)h`.                                                  (2.2)

Then the normal-equation identities are exact:

`sum_(j in L) w_j p_j=0`,
`sum_(j in L) w_j^2=tau>=0`.                                         (2.3)

The preceding run closed the endpoint `tau=0` when the selected heavy physical pivot is zero. Here we attack `tau>0` without conditioning away the heavy scalar.

The key observation is that the source-coordinate shear

`(q_j,p_j) -> (w_j,p_j)`                                             (2.4)

is only a change of basis in the three-dimensional spectral target; it does not rotate or mix the independent physical coordinates. Under this invertible target-space shear, the Gram of the retained original-coordinate block

`B={i} union L`

becomes exactly

`K_B ~ diag(c+tau,G)`.                                                (2.5)

Indeed the heavy row becomes `(sqrt(c),0)` and (2.3) kills the residual/transverse cross Gram. Hence

`boxed(det K_B=(c+tau) det G).`                                      (2.6)

## 3. Exact row-leverage formula for the combined block

Let `R_B` be the matrix of spectral rows indexed by `B`, and let

`U_B=R_B K_B^(-1/2)`                                                  (3.1)

be its Parseval normalization. The leverage of a physical row `r` in this normalized block is the invariant quantity

`r^T K_B^(-1) r`; it is unchanged by the invertible spectral shear (2.4). Therefore (2.5) gives the exact formulas

`boxed(lambda_i = c/(c+tau))`                                        (3.2)

for the heavy original coordinate and, for every light coordinate,

`boxed(lambda_j = w_j^2/(c+tau) + p_j^T G^(-1)p_j).`                 (3.3)

As a consistency check,

`lambda_i + sum_(j in L) lambda_j
 = c/(c+tau)+tau/(c+tau)+tr(I_2)=3`,                                 (3.4)

as required for a rank-three Parseval frame.

This identity is the structural gain of the run: the longitudinal regression residual can be charged directly as a row leverage while the transverse part retains the already-proved `1/32` cap.

## 4. New universal branch

### Theorem 4.1 — `QFORM-RANK3-COMBINED-BLOCK-DIFFUSE-CLOSURE-v1`

Assume the mixed exact-rank-three geometry above, (1.1)--(1.2), and suppose

`tau>=c`                                                             (4.1)

and

`w_j^2/(c+tau) <= 15/32` for every `j in L`.                         (4.2)

Then for every independent input law with one-dimensional densities bounded by one,

`boxed(||p_Q||_infinity < 28.272).`                                  (4.3)

The conclusion allows arbitrary conditioned heavy coordinates and their induced affine terms. No heavy-pivot sign or nonzero-pivot assumption is needed.

#### Proof

From (4.1),

`lambda_i=c/(c+tau)<=1/2`.                                           (4.4)

For every light coordinate, (1.2), (3.3), and (4.2) give

`lambda_j < 1/32+15/32=1/2`.                                        (4.5)

Thus every row of the normalized rank-three product block `U_B` has leverage at most one half.

Condition on the finitely many remaining heavy **original** coordinates `H\{i}`. The coordinates in `B` remain independent with their original density caps. The conditioned full quadratic form has the form

`X_B^T R_B Lambda R_B^T X_B + linear(X_B)+constant`.                 (4.6)

Write

`M=K_B^(1/2) Lambda K_B^(1/2)`.                                      (4.7)

Then

`R_B Lambda R_B^T=U_B M U_B^T`,

and the conditioned linear term is an allowed coordinate-separable perturbation in (1.3). Hence

`||p_(Q | X_(H\{i}))||_infinity <=3e |det M|^(-1/3)`.                (4.8)

By (2.6),

`|det M|=(c+tau) det G |det Lambda|`.                                (4.9)

Using `tau>=c`, `c>3/10`, `det G>=1/25`, and `|det Lambda|>=1`,

`|det M| > (3/5)(1/25)=3/125`.                                      (4.10)

Therefore

`||p_(Q | X_(H\{i}))||_infinity
 < 3e (125/3)^(1/3)
 = 28.27127028936805...`.                                            (4.11)

The bound is uniform in the conditioned values, so averaging the conditional laws gives the same unconditional estimate. QED.

### Geometric product-set form

Apply the designated partner's exact bang-bang theorem. For every interval `J` and arbitrary measurable sets `E_k` with `|E_k|=1`, hypotheses (4.1)--(4.2) imply

`boxed(|{x in product_k E_k : x^T A x in J}| < 28.272 |J|).`          (4.12)

Thus the new result is an actual geometric sublevel/slab inequality after the correct extremal reduction; it does not assume that any `E_k` is an interval, centered, bounded, or has a uniformly bounded number of components.

## 5. Residual-atom consequence

Theorem 4.1 has a useful contrapositive inside the still-unpaid part of the `tau>=c` branch. Since

`sum_(j in L) w_j^2/(c+tau)=tau/(c+tau)<1`,                          (5.1)

there can be at most two light indices satisfying

`w_j^2/(c+tau)>15/32`.                                                (5.2)

Indeed three such terms would sum to more than `45/32>1`.

Consequently, after the partner trichotomy, the preceding transverse-leverage payment, and Theorem 4.1, every still-unpaid exact-rank-three mixed instance must fall into one of the following sharply localized configurations:

1. `tau<c`, so the selected heavy original coordinate has combined-block leverage `c/(c+tau)>1/2`; or
2. `tau>=c` and at most two light original coordinates carry longitudinal-residual leverage exceeding `15/32`.

This is `QFORM-RANK3-LONGITUDINAL-RESIDUAL-ATOM-DICHOTOMY-v1`. It replaces the previous unrestricted `tau>0` debt by a finite high-leverage obstruction attached to actual original coordinates.

## 6. What changed and what remains unpaid

At the start of the run, the exact-zero graph endpoint `tau=0` was paid, but every `tau>0` longitudinal residual was still open. The new mechanism does **not** perturb from `tau=0`. Instead it keeps the heavy original coordinate in the same rank-three product block, orthogonalizes the longitudinal residual only in spectral target space, computes the exact normalized row leverages, and invokes the completed diffuse separable-phase theorem when the combined block is genuinely diffuse.

The first unpaid implication is now

`QFORM-RANK3-COMBINED-BLOCK-HIGH-LEVERAGE-CLOSURE-v1`:

> In the mixed exact-rank-three branch, close the configurations `tau<c` or the `tau>=c` branch with one or two light residual atoms satisfying (5.2), while retaining original-coordinate product provenance. The natural next move is to isolate only those finitely many high-leverage original coordinates and aggregate the remaining transverse/residual product bank before any reciprocal coefficient is paid.

The full arbitrary-matrix theorem also still requires a bridge from exact rank three to arbitrary additional spectral directions. Therefore **FULL-QFORM remains OPEN**.

## 7. Integrity

The report contains only private mathematical material in the authorized QFORM root. No credential, scheduler identifier, personal archive, email, public release, paid/remote model call, remote workflow, permission expansion, or cross-account authentication is used. Repository synchronization is not native learned-memory ingestion; execution status remains `WITHOUT_VERIFIED_BRAIN`.
