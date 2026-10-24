# QFORM account02/B14 r26 — disjoint multibank localization and the one-bank selection barrier

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T05:07:51Z.

attacking: finite multi-bank localization—compress disjoint aligned bank statistics without normalizing fragments, allow arbitrary aggregate curvature, and quantify the exact bank-count loss before a volume exit is needed.

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Run: `20260923T050751Z-account02-B14-QFORM-r26`.  
Status: **SUPPORTING TARGET-LEVEL THEOREM + PROOF-MECHANISM OBSTRUCTION / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`. Continuity is separate.

## 1. Exact first unpaid implication and sources actually used

The full target is unchanged: independent real coordinates with probability densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and a universal essential density bound for `X^T A X`, or a valid counterexample. No support radius, moments, connected support, log-concavity, centering, identical laws, or independence after spectral rotation may be assumed.

This run attacks the first localization debt left by account03/B14 r26: its completed theorem compresses **one** diffuse product bank when the leakage, bank curvature, and bank-to-outside coupling all factor through the same statistic. The unpaid case is several disjoint product banks with arbitrary quadratic coupling among their aggregate statistics.

Two completed sources are applied at equations.

1. Designated partner account03/B14 r26: `yspennstate/math-open-problems@f89093b26b458e02914d99e7235268aff6ae1e40`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T043707Z-account03-B14-QFORM-r26/REPORT.md`. It supplies (i) the product-safe one-dimensional projection cap `||p_(a^T V)||_infinity <= sqrt(2)/||a||_2`, and (ii) after product-preserving bank compression, a fixed four-independent-variable theorem with constant

   `C4 = 1000(8+log 4) = 9386.294361119892...`,

   uniform in arbitrary affine terms and arbitrary rough/unbounded supports, whenever the resulting physical `4x4` quadratic block has three eigenvalues of modulus at least `sigma`; the density bound is `C4/sigma`.

2. Required newest-Claude source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. `RESULTS.md` proves the mixed hub/Fresnel theorem H; `FOURIER_ROUTE_REPORT.md` proves the relaxed D' and unconditional fifth-volume D5 exits. Theorem H is applied below to an explicit target-valid family and gives the concrete uniform bound `3*4^(2/3)<7.560` where one-bank selection loses `sqrt(d)`.

The live correction boundary is respected: no arbitrary-joint rank-three coarea, no positive moment of a worst conditional projection cap, no post-rotation independence, no universally good physical minor/cross cut, and no interpretation of a small matrix coefficient as a uniformly small random perturbation on unbounded laws.

## 2. Main theorem: disjoint multibank localization

Let the original independent coordinates split as

`X=(U,V^(1),...,V^(d),Z)`, with `U in R^3`,

where the banks `V^(j)` and the outside bank `Z` are pairwise disjoint original-coordinate sets. Let `B=B^T` be `3x3`, let `k` be a unit vector with `Bk=0`, and suppose the two eigenvalues of `B|_(k^perp)` have moduli at least `nu>0`.

For each `j`, fix a nonzero bank vector `a_j`, put

`W_j = a_j^T V^(j)`,

and assume the coefficient matrix factors through these statistics as follows:

* `A_(U,Vj) = gamma_j k a_j^T`;
* `A_(Vj,Vl) = h_jl a_j a_l^T`, where `H=(h_jl)` is an **arbitrary real symmetric d x d matrix**;
* `A_(Vj,Z) = a_j b_j^T`;
* `A_(U,Z)` and `A_(Z,Z)` are arbitrary.

No size or sign assumption is made on `H`; in particular the aggregate bank curvature can be dense and arbitrarily large.

For each `j`, let `eta_j` be any certified density cap for `W_j`,

`||p_(W_j)||_infinity <= eta_j`.

The product-projection theorem permits the universal choice

`eta_j = sqrt(2)/||a_j||_2`.

Set

`Y_j = eta_j W_j`, `r_j = gamma_j/eta_j`.

Then `Y_1,...,Y_d` are mutually independent, independent of `U`, and each has density cap at most one. Define

`r_* = max_j |r_j|`.

### Theorem 2.1 — finite disjoint-bank compiler

Under the hypotheses above,

`boxed: ||p_(X^T A X)||_infinity <= C4 / min(nu,r_*).`       (2.1)

Using only the universal projection caps gives

`r_* >= (1/sqrt(2)) max_j |gamma_j| ||a_j||_2`,

and, if

`R = (sum_j r_j^2)^(1/2)`,

then

`boxed: ||p_(X^T A X)||_infinity <= C4 max(nu^(-1), sqrt(d)/R).`  (2.2)

The constants do not depend on support location/diameter, fragment number/separation, moments, translations, the size of `H`, or any outside affine parameters.

### Proof

Condition first only on the outside **original** coordinates `Z=z`. By the assumed factorisation the conditional form depends on each bank only through `W_j`, hence, after the cap-one rescaling, it has the exact form

`Q_z(U,Y) = U^T B U + 2(k^T U) r^T Y + Y^T H_tilde Y + affine_z(U,Y) + c_z`,  (2.3)

where

`(H_tilde)_jl = h_jl/(eta_j eta_l)`.

No thin fiber has been normalized and no support truncation has occurred.

Choose `j` with `|r_j|=r_*`. Condition on the **other disjoint bank statistics** `(Y_l)_(l != j)`. This conditioning is product-safe: because the original banks are disjoint, the joint law of `(U,Y_j)` is unchanged and remains a product of four cap-one laws. Every cross term `(H_tilde)_jl Y_j Y_l` with `l != j` becomes merely affine in `Y_j`; every leakage term from another bank becomes affine in `U`. Thus the active quadratic block is exactly

`K_j = [[B, r_j k], [r_j k^T, (H_tilde)_jj]].`               (2.4)

Diagonalise `B|_(k^perp)` only as deterministic matrix algebra; no random variables are rotated. The spectrum of `K_j` consists of the two eigenvalues of `B|_(k^perp)` and the two eigenvalues of

`T_j = [[0,r_j],[r_j,(H_tilde)_jj]].`                         (2.5)

Since `||T_j e_1||_2=|r_j|`, the spectral radius of `T_j` is at least `|r_j|`. Hence `K_j` has at least three eigenvalues of modulus at least

`sigma_j = min(nu,|r_j|).`                                    (2.6)

Apply the completed four-variable theorem used in partner r26, uniformly in all affine terms generated by `z` and the conditioned bank statistics. It gives `C4/sigma_j`. Averaging first over the other bank statistics and then over `Z` proves (2.1). Finally `r_* >= R/sqrt(d)` proves (2.2).

The key localization fact is that **conditioning on a statistic of a disjoint bank does not renormalize the active bank**. This is fundamentally different from the conjugate-sum/difference thin-fiber normalizations refuted in preceding B14 runs.

### Translation and rough-support invariance

Translating any original bank translates `W_j`, hence `Y_j`, and changes (2.3) only through affine/scalar terms after expansion of `Y^T H_tilde Y`. The quadratic block (2.4) is unchanged. The partner theorem is uniform in affine terms, and the projection cap has no support or moment hypothesis. Therefore arbitrary distant fragments, unbounded supports and arbitrary shifts pay zero additional localization tax.

## 3. Volume exits in the compressed product basis

The compression above creates a genuine product law in the scalar variables `Y_j`; it does not assert independence of overlapping rotated statistics. Therefore the newest-Claude cross-volume theorems may be applied directly to the aggregate curvature matrix `H_tilde`.

For disjoint bank-index sets `I,J`, let `M=(H_tilde)_(I,J)`.

* If `Z_3=e_3(M^T M)>0` and the row volume marginals obey `alpha_i<=h<3/4`, Claude D' gives

  `boxed: ||p_Q||_infinity <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z_3^(-1/6).`  (3.1)

* If `Z_5=e_5(M^T M)>0`, Claude D5 gives, with no marginal condition,

  `boxed: ||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10).`       (3.2)

All remaining self blocks, the `U` variables, affine terms and outside couplings are permitted by those theorems. Thus large genuinely multidirectional aggregate curvature can exit by volume before any one-bank reciprocal payment.

## 4. Target-valid obstruction to selecting one bank first

The `sqrt(d)` in (2.2) is not intrinsic to the law. A diffuse rank-one aggregate curvature gives an exact family where one-bank selection deteriorates while the completed mixed hub/Fresnel theorem stays uniform.

Let even `d>=4`, and put

`r=(1,...,1)/sqrt(d)`,
`u=(1,...,1,-1,...,-1)/sqrt(d)`,

with `d/2` plus and `d/2` minus signs. Then `r` and `u` are orthonormal. For independent cap-one variables

`U_1,U_2,U_3,Y_1,...,Y_d`,

define

`Q_d = U_1^2 - U_2^2 + 2 U_3 (r^T Y) + (u^T Y)^2.`           (4.1)

Its coefficient matrix has eigenvalues `+1,-1` from `U_1,U_2`; on `span(U_3,r,u)` it is the direct sum of `[[0,1],[1,0]]` and `[1]`, hence has eigenvalues `+1,-1,+1`. Therefore (4.1) is squarely inside the exact QFORM target, with five eigenvalues of modulus one.

The aggregate curvature `u u^T` has rank one, so every third- and fifth-volume certificate internal to that curvature vanishes. Conditioning down to a single bank coordinate leaves leakage `|r_j|=d^(-1/2)`, so the one-bank compiler alone gives only `C4 sqrt(d)`.

However, apply **Claude Theorem H** directly to (4.1): use hub `H={U_3}`, spread rank-one square vector `u` with `lambda=1`, and leaf bank `I={Y_1,...,Y_d}` with hub-coupling vector `r`. The augmented row frame is `(u_j,r_j)`, whose Gram matrix is `I_2`, and every row leverage is

`u_j^2+r_j^2 = 2/d <= 1/2.`                                   (4.2)

The theorem gives

`|phi_(Q_d)(t)| <= 4 pi^(3/2) |t|^(-3/2).`                   (4.3)

Combining with `|phi|<=1`,

`integral_R |phi(t)| dt <= 6 (4 pi^(3/2))^(2/3)`,

and Fourier inversion yields the dimension-free bound

`boxed: ||p_(Q_d)||_infinity <= 3*4^(2/3) = 7.559526299... .` (4.4)

This is an equation-level application of the required newest-Claude result. It proves that the `sqrt(d)` loss from selecting one bank is a proof-order artefact, not a QFORM obstruction.

More generally, if `u` is unit, `r` is orthogonal to `u` with `||r||_2=R`, and

`u_j^2 + r_j^2/R^2 <= 1/2` for all j,

then the same calculation with `det G=R^2` and square coefficient `lambda` gives

`||p_Q||_infinity <= 3*4^(2/3) |lambda|^(-1/3) R^(-2/3).`    (4.5)

## 5. What changed and what remains unpaid

New positive result: `QFORM-DISJOINT-MULTIBANK-LOCALIZATION-v1`, equations (2.1)-(2.2). It extends the partner's single aligned bank to finitely many **disjoint** product banks and permits an arbitrary dense quadratic matrix among their aggregate statistics, with zero support/translation/moment tax.

New mechanism obstruction: `QFORM-ONE-BANK-SELECTION-SQRTd-BARRIER-v1`, equations (4.1)-(4.4). Even in a target-valid family, selecting one weak bank before aggregate Fresnel/volume payment loses `sqrt(d)` while the actual density is uniformly bounded by a proved theorem. This is not a counterexample to QFORM.

The first unpaid implication is now `QFORM-HIGH-LEVERAGE-MULTIBANK-OR-VOLUME-EXIT-v1`: for the reduced product form (2.3) with unbounded `d`, prove an exhaustive branch giving either (i) a D'/D5 volume certificate in `H_tilde`; (ii) a diffuse mixed hub/Fresnel frame certificate such as (4.5); or (iii) a bounded high-leverage active subset whose aggregate leakage can be paid by a fixed-core theorem without a `sqrt(d)` selection loss. The reduction must keep the scalar bank variables product-disjoint; it may not condition on overlapping linear statistics, normalize tiny conjugate fibers before reciprocal payment, or replace a small matrix norm by a small random perturbation on arbitrary unbounded inputs.

Full QFORM remains OPEN. The mixed-hub branch above has an integrable characteristic function and hence a bounded continuous density; the partner fixed-core branch is used only for essential boundedness unless its source states more.
