SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B09, 2026-09-22T18:46:18Z.
attacking: pay a rank-two bilinear cross block when one physical bank has arbitrary coordinate-separable curvature, without Cauchy--Schwarz or a square-root interval loss.

# fleet01/B09 — one-sided separable cross smoothing

Run: `B09-20260922T184627Z-r15`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The full target remains open. The theorem below proves a new arbitrary-rank ambient branch and, in particular, closes a genuinely curved rank-two cross-bank configuration that is not covered by the latest exact-zero-bank theorem. It proves a bounded **continuous** density in its exact scope and therefore a direct `O(|I|)` interval bound.

## 1. Corrections and source-pinned dependencies

This run does **not** use any of the following refuted interfaces: law-uniform scalar van-der-Corput decay, independence after spectral rotation, the arbitrary-joint rank-three coarea bound, positive moments of normalized conditional spectral densities, a universally good fixed coordinate minor, a universal rank-three cross cut, or the one-heavy-row-plus-its-own-square absorption rule.

Two positive inputs are used exactly in their proved scopes.

1. **Separable-phase Brascamp--Lieb/Hausdorff--Young estimate.** Canonical proof: `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`, claim `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`. If `U` is an `m x r` orthonormal-column frame with row leverages `c_i=||u_i||^2<=1/2`, and

   `h_i(x)=f_i(x) exp(i V_i(x))`,

   where `0<=f_i<=1`, `int f_i=1`, and `V_i` is arbitrary measurable, then

   `int_{R^r} prod_i |hat h_i(<u_i,xi>)| dxi <= (2pi)^r B(U)`,        (1.1)

   where

   `B(U)=prod_{c_i>0}(1-c_i)^(-(1-c_i)/2) <= exp(r/2)`.              (1.2)

   The Fourier convention is `hat h(xi)=int exp(-i xi x)h(x)dx`. The proof uses geometric Brascamp--Lieb and sharp Hausdorff--Young for complex amplitudes.

2. **Livshyts--Paouris--Pivovarov marginal-density bound.** For an `r`-dimensional orthogonal marginal of a product probability density with one-dimensional caps at most one, the marginal density is at most `2^(r/2)`. I use this only for a genuine orthogonal marginal of an original independent coordinate bank. No independence among the projected coordinates is asserted.

The required completed partner result is fleet02/B09 `QFORM-ZEROINTERNAL-BANK-WEDGE-v1`, canonical report `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T181745Z-fleet02-B09-QFORM-r6/REPORT.md` (read-back blob `42ded502289f1feffa051daace8733857fa40e47`). It is applied quantitatively in Section 6.

## 2. Compact conditional end-to-end route

A bilinear route to the full theorem would be complete if the spectral hypothesis `s_3(A)>=1` forced one of the already-paid product-preserving exits: a ridge/diffuse branch, a quantitative indefinite physical pair, a scalar-pivot/half-Riesz branch, an exact one-sided-zero cross bank, or the new one-sided **coordinate-separable** cross bank below. The first unpaid implication for B09 is therefore to isolate and pay the residual in which every useful rank-two cross bank has genuinely nonseparable self-curvature on both sides and simultaneously has heavy cross-frame leverage.

The analytic step attacked here is the separable-curvature branch itself. Crucially, it pays rank two without first Cauchy--Schwarz squaring the characteristic function; that is exactly where the usual rank-two `|t|^{-1}` endpoint becomes nonintegrable.

## 3. Main theorem

### Theorem 3.1 — `QFORM-ONE-SIDED-SEPARABLE-CROSS-DIFFUSE-v1`

Let `X=(X_i)_{i in I}` and `Y=(Y_j)_{j in J}` be disjoint original-coordinate banks. All coordinates are mutually independent and each has a probability density bounded by one. Let `B` be a real `|I| x |J|` matrix of rank `r>=2` with thin SVD

`B=U Sigma V^T`,                                                     (3.1)

where `U^T U=V^T V=I_r` and the positive singular values are `s_1,...,s_r`. Put

`D=prod_{ell=1}^r s_ell`,
`c_i=||U_{i,*}||_2^2`,
`B_U=prod_{c_i>0}(1-c_i)^(-(1-c_i)/2)`.                              (3.2)

Assume

`max_i c_i <= 1/2`.                                                   (3.3)

Let `W_i:R->R` be arbitrary measurable functions, finite almost surely, and let `H:R^{|J|}->R` be arbitrary measurable, finite almost surely. Define

`T = sum_{i in I} W_i(X_i) + 2 X^T B Y + H(Y)`.                       (3.4)

Then `T` has a bounded continuous density vanishing at infinity and

`boxed: ||p_T||_infinity <= sqrt(2) [r/(r-1)] B_U^(1/r) D^(-1/r).`    (3.5)

Using `B_U<=e^(r/2)`, the simpler universal form is

`boxed: ||p_T||_infinity <= sqrt(2e) [r/(r-1)] D^(-1/r).`             (3.6)

Consequently every interval `L` satisfies

`boxed: P{T in L} <= sqrt(2e) [r/(r-1)] D^(-1/r) |L|.`                (3.7)

For rank two this becomes

`boxed: ||p_T||_infinity <= 2 sqrt(2e) / sqrt(s_1 s_2).}`             (3.8)

No moment, support, smoothness, centering, identical-law, log-concavity or sign assumption is used. The `Y`-side term `H` may contain completely arbitrary same-bank quadratic curvature.

### Proof

For each real frequency `t`, set

`h_{i,t}(x)=f_i(x) exp(i t W_i(x)).`                                  (3.9)

Since the `X_i` are independent, conditioning on `Y=y` gives

`E_X exp[i t(sum_i W_i(X_i)+2X^T B y)]`
` = prod_i hat h_{i,t}(-2t(By)_i).`                                  (3.10)

Therefore

`phi_T(t)=E_Y [ exp(i t H(Y)) prod_i hat h_{i,t}(-2t(By)_i) ]`.       (3.11)

Take absolute values only after this product has been formed:

`|phi_T(t)| <= E_Y prod_i |hat h_{i,t}(2t(By)_i)|`.                  (3.12)

This is the step that preserves the entire coordinate-separable `X` curvature as unit-modulus complex amplitudes. No scalar stationary-phase bound is used.

Write

`Z=V^T Y in R^r`.                                                     (3.13)

`Z` is an orthogonal marginal of the original product law on the `Y` bank, so it has a density `rho_Z` with

`||rho_Z||_infinity <= 2^(r/2)`.                                     (3.14)

The coordinates of `Z` are generally dependent; only the joint density cap (3.14) is used. Because `By=U Sigma Z`, equations (3.12)--(3.14) give, for `t!=0`,

`|phi_T(t)|`
` <= 2^(r/2) int_{R^r} prod_i |hat h_{i,t}(2t <U_{i,*},Sigma z>)| dz.` (3.15)

Make the invertible change of variables

`xi=2t Sigma z`.                                                      (3.16)

Its Jacobian is

`dz = [(2|t|)^r D]^(-1) dxi`.                                        (3.17)

Now apply the exact separable-phase estimate (1.1) to the **same** left singular frame `U`. We obtain

`|phi_T(t)|`
` <= [2^(r/2)/(2^r |t|^r D)] (2pi)^r B_U`
` = [(sqrt(2) pi)^r B_U]/[D |t|^r].`                                 (3.18)

Set

`L = sqrt(2) pi B_U^(1/r) D^(-1/r).`                                 (3.19)

Together with the trivial probability bound `|phi_T(t)|<=1`,

`|phi_T(t)| <= min(1,(L/|t|)^r).`                                    (3.20)

Since `r>=2`, this envelope is integrable. Directly,

`int_R |phi_T(t)| dt`
` <= 2[L+L^r int_L^infinity t^(-r)dt]`
` = 2L r/(r-1).`                                                      (3.21)

Fourier inversion now gives a bounded continuous density vanishing at infinity and

`||p_T||_infinity`
` <= (2pi)^(-1) 2L r/(r-1)`
` = sqrt(2) [r/(r-1)] B_U^(1/r) D^(-1/r),`                           (3.22)

which is (3.5). Equation (1.2) yields (3.6), and integrating the density over an interval gives (3.7). QED.

### Why rank two is the natural endpoint here

For `r=1`, the same calculation gives only a `|t|^{-1}` envelope, exactly the logarithmic nonintegrable boundary familiar from a scalar bilinear product. Thus the theorem does not falsely assert a rank-one bilinear density bound. At `r=2`, retaining the product without a Cauchy--Schwarz square root gives `|t|^{-2}`, already integrable. This is the analytic gain over a route that first removes arbitrary self phases by Cauchy--Schwarz.

## 4. Quadratic-form corollary with arbitrary outside spectrum

### Corollary 4.1 — `QFORM-DIAGONALBANK-CROSS-DIFFUSE-v1`

Let the original coordinates be partitioned into disjoint sets `I,J,K`. Suppose the physical principal block `A[I,I]` is diagonal. Put

`B=A[I,J]`,

and suppose `rank(B)=r>=2`. Let `B=U Sigma V^T` be its thin SVD and assume every left row leverage of `U` is at most `1/2`.

There is **no restriction** on `A[J,J]`, `A[K,K]`, `A[I,K]`, `A[J,K]`, the total rank of `A`, the signs of the spectrum, or additional eigenvalues. Then, with `D=prod s_ell(B)`,

`||p_{X^TAX}||_infinity <= sqrt(2e) [r/(r-1)] D^(-1/r),`              (4.1)

and the density is continuous and vanishes at infinity.

#### Proof

Condition on the original coordinates `X_K`. The `I` and `J` banks remain independent product families with the original cap-one marginals. Since `A[I,I]` is diagonal, every conditioned contribution involving only `I` is a sum of one-coordinate functions: diagonal squares plus the induced linear terms from `K`. Every `J`-side self term, all induced `J`-linear terms, and the conditioned constant are absorbed into the arbitrary `H(Y)` of Theorem 3.1. The theorem is uniform in the conditioned value of `X_K`, so averaging the conditional laws preserves the same bound and continuity follows from the common `L^1` characteristic-function envelope (3.20). QED.

Thus exact flatness of the coefficient-side bank is **not** necessary in the diffuse cross-frame regime: arbitrary diagonal quadratic curvature and arbitrary linear translations are free.

## 5. Target-valid curved stress family

Let even `m>=4`. On `R^m` define

`u=m^(-1/2)(1,...,1)`,
`v=m^(-1/2)(1,...,1,-1,...,-1)`,

where `v` has `m/2` plus signs and `m/2` minus signs, and put

`P=uu^T+vv^T`.                                                        (5.1)

`P` is a rank-two orthogonal projection. On two disjoint `m`-coordinate banks set

`A_m = [[(1/2) I_m, 2P], [2P, (1/2) I_m]].`                           (5.2)

The cross block `B=2P` has rank two and

`s_1=s_2=2`, `D=4`.                                                   (5.3)

Its left singular frame is `[u,v]`; every physical row leverage equals

`c_i=2/m <=1/2`.                                                      (5.4)

The exact nontrivial spectrum of (5.2) on each of the two singular directions of `P` is the spectrum of

`[[1/2,2],[2,1/2]]`,

namely `5/2,-3/2`. Hence `A_m` has four eigenvalues of modulus at least one (two `5/2`, two `-3/2`), while all remaining eigenvalues are `1/2`. This is therefore a target-valid full-rank family with nonzero curvature on **both** physical banks.

Theorem 3.1 applies and gives the sharper frame-dependent estimate

`||p_{X^T A_m X}||_infinity <= sqrt(2) B_U^(1/2),`                    (5.5)

where

`B_U=(1-2/m)^(-(m-2)/2) <= e`.                                       (5.6)

Thus uniformly in `m` and in every admissible product input law,

`boxed: ||p_{X^T A_m X}||_infinity <= sqrt(2e).}`                     (5.7)

This stress family is deliberately outside the latest partner theorem's exact hypothesis `A[I,I]=0`: both self blocks are `(1/2)I_m`. The new theorem therefore pays a real curved-self-bank branch rather than merely reproving the flat-bank result.

## 6. Required fleet02/B09 partner result applied quantitatively

The latest completed fleet02/B09 theorem `QFORM-ZEROINTERNAL-BANK-WEDGE-v1` says that if the `I` self block is exactly zero and the cross block has two nonzero singular values `s_1>=s_2>0`, then

`||p_Q||_infinity <= 2 sqrt(pi) / sqrt(s_1 s_2).`                    (6.1)

It permits arbitrary curvature on the opposite bank and arbitrary outside couplings/rank. On the overlap where `A[I,I]=0` **and** the left rank-two singular frame is diffuse, Theorem 3.1 gives

`||p_Q||_infinity <= 2 sqrt(2e)/sqrt(s_1 s_2),`                       (6.2)

whereas the named partner gives the strictly sharper bound (6.1), since `pi<2e`. Therefore the compatible combined endpoint is the actual inequality

`boxed: ||p_Q||_infinity <= 2 sqrt(pi)/sqrt(s_1 s_2)`                 (6.3)

on the flat overlap, while the new result extends the same product-preserving routing to arbitrary coordinate-separable curvature on the diffuse side.

For the partner's canonical diffuse cross geometry `B=2P`, equation (6.3) gives

`||p_Q||_infinity <= sqrt(pi)`.                                      (6.4)

This is an actual application of the completed partner theorem, not a nominal citation.

## 7. What changed mathematically

The newest B09 partner result removed the analytic debt when one entire cross bank is internally flat. The new theorem removes a substantial part of the remaining `curved self-bank` debt:

- the bank need not be flat;
- any diagonal quadratic curvature is allowed;
- arbitrary coordinatewise nonlinear phases are in fact allowed;
- arbitrary linear translations from conditioned outside coordinates are allowed;
- arbitrary nonseparable curvature is allowed on the opposite bank;
- rank two already yields a continuous density and a direct linear interval estimate;
- no scalar square pivot is required;
- no Cauchy--Schwarz decoupling or selected reciprocal minor is paid.

The mechanism is source-valid because the only rotated object on the `Y` side is used through its genuine joint marginal density cap, while the `X` side retains the original product amplitudes throughout the Brascamp--Lieb estimate.

## 8. First remaining implication

The first unpaid B09 implication is now

**`QFORM-NONSEPARABLE-SELF-BANK-OR-HEAVY-ROUTING-v1`.** Starting only from `s_3(A)>=1`, after the already-paid ridge, indefinite-pair, scalar-pivot, exact-zero-bank and grouped-coordinate branches, prove that one can force either

1. a rank-`r>=2` physical cross block whose one side has coordinate-separable self-curvature and whose singular frame there has all row leverages `<=1/2`, so Theorem 3.1 applies; or
2. one of the existing paid branches; or
3. a quantitatively structured residual in which every useful rank-two cross block has genuinely **nonseparable off-diagonal self-curvature on both sides** and a heavy singular-frame row, then pay that residual without conditioning away product structure.

This is narrower than the preceding generic `curved self-bank` residual: diagonal curvature is no longer an obstruction. The structural extraction from the bare three-large-eigenvalue hypothesis remains unsolved.

## 9. Status integrity

- `QFORM-ONE-SIDED-SEPARABLE-CROSS-DIFFUSE-v1`: **proved in the stated scope**.
- `QFORM-DIAGONALBANK-CROSS-DIFFUSE-v1`: **proved in the stated arbitrary-ambient-rank scope**.
- Target-valid curved family (5.2): **uniformly closed**, with a continuous-density bound `sqrt(2e)`.
- fleet02/B09 `QFORM-ZEROINTERNAL-BANK-WEDGE-v1`: **consumed and applied quantitatively** in Section 6.
- Full universal QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuity: **proved for the new theorem/corollary**, still OPEN for the unrestricted target.

Repository synchronization is not native brain ingestion. No new installation work, task creation, scheduler mutation, email, push notification, public release, permission expansion, paid model/API/Codex call, or remote workflow is part of this run.
