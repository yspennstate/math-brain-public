# QFORM-PAIRLOG-LP-SCHUR-RESIDUAL-v1

Run: `B09-20260922T224934Z-r18`  
Worker: `account01/B09` — Bilinear block mechanism  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Fresh control at start: `yspennstate/math-research-brain@5dd0b45fa5b2d014b2d87a4a272370d8b6b784cf`, OWNER CONTROL revision `2026-09-22.15`.  
Status: **ESSENTIAL_STEP_APPLIED / NEW_SUPPORTING THEOREM / FULL CONJECTURE OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and purpose

The full target remains: for every dimension, every independent real input coordinates with densities bounded by one, and every real symmetric coefficient matrix having at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound for the quadratic form, or give a valid counterexample.

This report proves a new product-preserving endpoint for a nested bilinear configuration. It combines the exact logarithmic density envelope of an **indefinite physical endpoint pair** with finite-`L^p` smoothing of an arbitrary Schur-center residual. The main application uses account02/B09's rank-two original-coordinate cross-block `L^3` theorem. The mechanism directly yields an `O(|I|)` interval bound and does not square the desired probability.

The result is not a proof of the full conjecture: the remaining structural problem is to force the displayed endpoint-pair plus residual-cross resource, or route the survivor to one of the already-paid branches.

## 2. Source-pinned inputs and corrections

Positive mathematical inputs:

1. account02/B09 `QFORM-PAIRLOG-SCHUR-CENTER-v1`, full proof  
   `yspennstate/math-open-problems@004631a217e4c6b716651d7ac551e035a181cc45`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T204204Z-account02-B09-QFORM-r9/REPORT.md`.
   For an invertible indefinite original-coordinate endpoint pair `E`, with `D=|det E|` and `kappa=sigma_min(E)`, after completing the pair the conditional density has, for every `r>0`,

   `p(t | residual y) <= 2 sqrt(2)/r + D^(-1/2) log_+( 2 r^2 /(kappa |t-R(y)|) )`,

   where `R(y)` is the exact moving Schur-center critical value. The bound is uniform in affine shifts and outside conditioning.

2. account02/B09 `QFORM-RANK2-CROSS-LP-v1`, full proof  
   `yspennstate/math-open-problems@17dec75dc10459933f8bfde30daa86d1c6d90a6a`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T124417Z-account02-B09-QFORM-r2/REPORT.md`.
   For an original-coordinate disjoint split with arbitrary quadratic-affine terms on both sides and rank-two cross block with singular-value product `Theta`,

   `||p_R||_3 <= 6^(2/3) Theta^(-1/3)`.

Corrections explicitly retained: no law-uniform pointwise quadratic Fresnel decay; no post-rotation independence; no dimension-free naive spectral-fiber supremum; no universal single Schur-rank-two extraction; an invertible indefinite pair alone is not sufficient when the third Schur-center resource vanishes. None of those refuted interfaces is used positively below.

## 3. An exact logarithmic-kernel `L^p` lemma

Let `R` be a real random variable with a density `g in L^p(R)`, where `p>1`, and let

`M=||g||_p`, `q=p/(p-1)`.

For every `L>0`,

`sup_t E log_+( L/|t-R| ) <= M [2 L Gamma(q+1)]^(1/q)`.       (3.1)

### Proof

For fixed `t`, apply Holder to `g(s)` and the translated logarithmic kernel:

`E log_+(L/|t-R|)`
` <= ||g||_p [ integral_R log_+^q(L/|u|) du ]^(1/q)`.

The kernel is supported on `|u|<L`, and the integral is exact:

`integral_R log_+^q(L/|u|) du`
` =2 integral_0^L log^q(L/u) du`
` =2 L integral_0^infinity v^q e^(-v) dv`
` =2 L Gamma(q+1)`.

This gives (3.1). QED.

## 4. Main theorem: finite-`L^p` Schur-center smoothing of an indefinite physical pair

### Theorem 4.1 — `QFORM-PAIRLOG-LP-SCHUR-RESIDUAL-v1`

Let two original independent input coordinates form an invertible indefinite physical endpoint block `E`. Condition on all other outside original coordinates except a residual product vector `Y`; arbitrary outside quadratic coefficients and couplings are thereby absorbed into affine terms and constants. Complete the endpoint pair exactly, so that the moving critical value is a real residual random variable `R=R(Y)`.

Put

`D=|det E|`, `kappa=sigma_min(E)>0`.

Assume only that `R` has a density in `L^p`, `p>1`, with `M=||p_R||_p`. Set

`q=p/(p-1)`, `alpha=2/q=2(p-1)/p`.

Then the full quadratic form has an essentially bounded density and

`||p_Q||_infinity`
` <= C_p^(log) D^(-p/[2(3p-2)]) kappa^(-(p-1)/(3p-2)) M^(p/(3p-2)),`   (4.1)

where

`C_p^(log)`
` =(alpha+1) alpha^(-alpha/(alpha+1))`
`  *(2 sqrt(2))^(alpha/(alpha+1))`
`  *[4 Gamma(q+1)]^(1/[q(alpha+1)]).`                              (4.2)

In particular, for `p=3`,

`boxed( ||p_Q||_infinity`
` <= 7 (pi/12)^(1/7) D^(-3/14) kappa^(-2/7) ||p_R||_3^(3/7). )`     (4.3)

Every interval `I` therefore satisfies the same coefficient times `|I|`.

### Proof

The source-pinned account02/B09 pair-log theorem gives, for every `r>0`, uniformly in the outside conditioning,

`p_Q(t)`
` <= 2 sqrt(2)/r`
`    +D^(-1/2) E log_+( 2 r^2 /(kappa |t-R|) ).`                   (4.4)

Apply (3.1) with `L=2r^2/kappa`. Then

`p_Q(t)`
` <= A r^(-1) + B r^alpha`,                                      (4.5)

where

`A=2 sqrt(2)`,
`B=D^(-1/2) M [4 Gamma(q+1)/kappa]^(1/q)`,
`alpha=2/q`.

For positive `A,B,alpha`, the exact minimum is

`min_{r>0} [A/r+B r^alpha]`
` =(alpha+1) alpha^(-alpha/(alpha+1))`
`  *A^(alpha/(alpha+1)) B^(1/(alpha+1)).`                         (4.6)

Since

`1/(alpha+1)=p/(3p-2)`,
`1/[q(alpha+1)]=(p-1)/(3p-2)`,

substitution yields (4.1)-(4.2).

For `p=3`, `q=3/2`, `alpha=4/3`, and `Gamma(5/2)=3 sqrt(pi)/4`. The constant simplifies exactly:

`(7/3)(4/3)^(-4/7)(2sqrt(2))^(4/7)(3sqrt(pi))^(2/7)`
` =7 (pi/12)^(1/7)`,

which is (4.3). The bound is uniform in all outside original-coordinate conditioning; averaging preserves it. QED.

### Structural point

The theorem uses the **marginal** `L^p` law of the exact Schur-center residual. It never takes a worst conditional density along a spectral fiber, never rotates the independent source coordinates, and never replaces a logarithmic saddle by a false pointwise oscillatory estimate.

## 5. Rank-two residual cross block: direct application of the designated partner

### Corollary 5.1 — `QFORM-PAIRLOG-RANK2-SCHUR-CROSS-v1`

Partition the original coordinates as endpoint pair `K` of size two, two disjoint residual banks `I,J`, and an arbitrary outside bank `O`. Condition on `O`.

Write the selected quadratic matrix in blocks

`[ E   L_I    L_J ]`
`[L_I^T B      M  ]`
`[L_J^T M^T    C  ]`,

where `E` is invertible indefinite. After completing the endpoint pair, the exact residual Schur matrix is

`S = [[B,M],[M^T,C]] - [[L_I^T],[L_J^T]] E^(-1) [L_I,L_J]`.

Let its original-coordinate cross block across `I|J` be

`N = M - L_I^T E^(-1) L_J`.                                  (5.1)

Assume `rank N=2`, with nonzero singular values `s1,s2`, and set

`Theta=s1 s2`.

Then, with no restriction on the two residual self blocks, affine terms, outside couplings, signs, supports, or additional spectrum,

`boxed( ||p_Q||_infinity`
` <= 7 (3 pi)^(1/7) D^(-3/14) kappa^(-2/7) Theta^(-1/7). )`     (5.2)

Numerically the universal coefficient is

`7(3pi)^(1/7) = 9.6444980506...`.

Consequently

`P(Q in I0) <= 7(3pi)^(1/7) D^(-3/14) kappa^(-2/7) Theta^(-1/7) |I0|`  (5.3)

for every interval `I0`.

### Proof

The completed-pair critical value is an arbitrary quadratic-affine form of the residual **original** coordinates. Its cross block is exactly `N` in (5.1). Therefore the designated account02/B09 theorem `QFORM-RANK2-CROSS-LP-v1`, at `p=3`, applies without changing coordinates:

`||p_R||_3 <=6^(2/3) Theta^(-1/3)`.                           (5.4)

Insert (5.4) into (4.3):

`||p_Q||_infinity`
` <=7(pi/12)^(1/7) D^(-3/14) kappa^(-2/7)`
`    *[6^(2/3) Theta^(-1/3)]^(3/7)`
` =7(3pi)^(1/7) D^(-3/14) kappa^(-2/7) Theta^(-1/7).`

This is (5.2). QED.

### Scaling audit

Under multiplication of the full coefficient matrix by `lambda`,

`D -> lambda^2 D`, `kappa -> |lambda| kappa`, `Theta -> lambda^2 Theta`.

The right side of (5.2) scales as

`|lambda|^(-3/7) |lambda|^(-2/7) |lambda|^(-2/7)=|lambda|^(-1)`,

which is exactly the required density scaling. Thus no hidden scale loss is present.

## 6. Target-valid stress instance: two individually singular smoothing channels jointly become bounded

Let six independent cap-one input variables be grouped as `(X0,Z0)` and `(X1,X2,Y1,Y2)`, and consider

`Q = X0^2-Z0^2 +(X1+Y1)^2-(X2+Y2)^2`.                         (6.1)

The endpoint block is `E=diag(1,-1)`, so

`D=1`, `kappa=1`.

The residual cross block for `I={X1,X2}`, `J={Y1,Y2}` is `N=diag(1,-1)`, hence `Theta=1`. The full matrix has eigenvalues

`{2,-2,1,-1,0,0}`,

so this is a genuine instance of the owner's target class. Corollary 5.1 gives, for **every** admissible independent input law,

`boxed( ||p_Q||_infinity <=7(3pi)^(1/7)<9.645. )`              (6.2)

This is a useful mechanism stress test. The two-variable saddle `X0^2-Z0^2` may itself have a logarithmically unbounded density, and the residual `(X1+Y1)^2-(X2+Y2)^2` is the source-valid rank-two-cross logarithmic obstruction. The nested argument spends the residual's finite `L^3` regularity to average the endpoint logarithm, producing a genuine bounded-density endpoint without falsely asserting that either rank-two saddle is bounded by itself.

The example is not a full-target obstruction and is not claimed novel; it verifies that the theorem operates exactly at the two logarithmic thresholds that earlier B09 corrections identified.

## 7. Relation to the current fleet survivor

The newest source-bound structural work has already paid a heavy residual physical Schur edge `|S_pz|>1/8` under a heavy first pivot. The still-unpaid survivor is therefore concentrated in pivot-star / balanced aligned-bank configurations whose physical cross geometry is close to rank one.

Corollary 5.1 gives a clean paid exit as soon as such a configuration, after choosing an invertible indefinite endpoint pair, leaves **two** residual original-coordinate cross singular directions with quantitative product `Theta`. Hence the surviving difficult branch can be narrowed further to configurations in which every usable endpoint-pair Schur residual remains effectively rank one at the product-preserving scale, or the endpoint pair itself degenerates/has only a tiny determinant or tiny `kappa`.

This does not yet pay the balanced rank-one aligned-bank survivor. That branch still requires a genuinely one-strong-cross mechanism retaining arbitrary within-bank curvature, or a structural argument forcing a second cross direction / Schur-center determinant / paid pivot packet.

## 8. First unpaid implication

`QFORM-ENDPOINTPAIR-RANK1-RESIDUAL-OR-PAID-EXIT-v1`:

From the current QFORM structural survivor, prove a dimension-free product-preserving routing which either

- produces an invertible physical endpoint pair with controlled `D,kappa` and a residual Schur cross block having controlled rank-two singular product `Theta`, so Corollary 5.1 applies;
- routes to the already-paid heavy-edge, sequential-pivot, grouped-bank, ridge/diffuse, definite-pair, or three-bank Schur-center branches; or
- isolates a genuinely rank-one residual bank operator and proves its density bound while retaining arbitrary self-block curvature.

The third alternative is the remaining analytic obstruction for this B09 mechanism.

## 9. Regularity and integrity

The theorem proves **essential boundedness** and the direct linear interval estimate (5.3). It does not, from these arguments alone, prove a continuous density representative. No numerical histogram or Monte Carlo claim is used as evidence. No moment, compact-support, log-concavity, identical-law, centering, or post-rotation independence assumption is introduced. All conditioning is on original independent coordinates, and all residual cross blocks are original-coordinate blocks of exact Schur complements.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.
