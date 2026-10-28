SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T11:55:32.050078Z.
attacking: rebalance the rank-three Fresnel product estimate over physical coordinate bases, replacing the canonical leverage law by an arbitrary half-capped determinant-entropy basis law.

# account01/B04 r36 — rebalanced physical-basis Fresnel estimate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / STRICT EXTENSION OF THE CANONICAL-LEVERAGE FRESNEL BRANCH / FULL QFORM OPEN**  
Regularity: the new branch has an integrable characteristic-function envelope and therefore a continuous `C_0(R)` density.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and dependencies


The analytic inputs used here are already completed source-pinned results:

1. **Separable-phase rank-three Fresnel theorem**, `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, repository/commit
   `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, path
   `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.
   In particular it proves the complex-amplitude Hausdorff--Young estimate and the Gaussian-cutoff quadratic inversion for coordinate-separable phase twists.

2. **Arbitrary-weight Gaussian Brascamp--Lieb determinant mechanism** from the audited Theorem D route, repository/commit
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, path
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.
   Its Lieb normalization is
   `BL = sup_{lambda_i>0} [prod lambda_i^{c_i}/det(sum c_i lambda_i r_i r_i^T)]^(1/2)`
   for one-dimensional maps, and its arbitrary-weight AM--GM step is used below.

3. The designated partner `account02/B04` result actually applied in Section 7 is
   `QFORM-ZEROPIVOT-J1-WEIGHTED-MIXED-HUB-v1`, repository/commit
   `yspennstate/math-open-problems@2311fa678098f3ac7b96e5eb3795d9def07cc2fd`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260924T091038Z-account02-B04-QFORM-auto11-r22/REPORT.md`.

No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, compact support, moments, log-concavity, or connected-support assumption is used.

## 2. The new currency

Let `R` be an `m x 3` real matrix of rank three, with physical rows `r_i^T`. Let `Lambda` be an invertible real symmetric `3 x 3` matrix. A **physical basis law** is a probability law `w=(w_S)` on three-element sets `S subset {1,...,m}` for which `det R_S != 0` whenever `w_S>0`.

Write

`alpha_i = P_w(i in S),`                                         (2.1)

so `sum_i alpha_i=3`, and define the determinant-entropy currency

`G_R(w) = exp( H(w) + sum_S w_S log det(R_S)^2 ).`                (2.2)

Define also

`B(alpha) = prod_{alpha_i>0} (1-alpha_i)^(-(1-alpha_i)/2).`       (2.3)

The relevant feasible set is

`alpha_i <= 1/2` for every physical coordinate `i`.               (2.4)

This is **not** the canonical squared-volume law. The point of the theorem is that one may deliberately rebalance physical bases to satisfy (2.4), paying only the explicit entropy/determinant currency loss in (2.2).

## 3. Main theorem — `QFORM-REBALANCED-BASIS-FRESNEL-v1`

Let `X_1,...,X_m` be independent real random variables with densities `0<=f_i<=1`. Let `V_i:R->R` be arbitrary measurable functions finite almost surely. Put

`T = (R^T X)^T Lambda (R^T X) + sum_i V_i(X_i).`                  (3.1)

Suppose a physical basis law `w` obeying (2.4) exists. Then `T` has a continuous density vanishing at infinity and

`boxed:`
`||p_T||_infinity`
` <= 3 B(alpha)^(2/3) [ |det Lambda| G_R(w) ]^(-1/3).`            (3.2)

Since

`-(1-a) log(1-a) <= a`, `0<=a<1`,                                (3.3)

and `sum alpha_i=3`, one has `B(alpha)<=e^(3/2)`. Hence the simpler universal branch estimate is

`boxed:`
`||p_T||_infinity <= 3e [ |det Lambda| G_R(w) ]^(-1/3).`         (3.4)

The same conclusion holds for a full ambient quadratic form whenever an ORIGINAL-coordinate principal block has the form

`A_II = D + R Lambda R^T`                                        (3.5)

with `D` diagonal and the above basis law: condition on the outside ORIGINAL coordinates; their effect on `X_I` is only a coordinate-separable linear phase, so it is absorbed into the `V_i` without changing any constant.

### Why this is strictly stronger than the canonical-leverage theorem

If `G=R^T R` and one chooses the canonical squared-volume law

`w_S^vol = det(R_S)^2/det(G)`,                                   (3.6)

then Cauchy--Binet gives

`G_R(w^vol)=det(G)`,                                              (3.7)

and its marginals are exactly the leverage scores

`alpha_i^vol = r_i^T G^(-1) r_i`.                                (3.8)

Thus (3.2) reduces exactly to the earlier rank-three separable-phase theorem after normalizing `U=R G^(-1/2)`. The new theorem allows a **different** basis law with all marginals at most `1/2` even when the canonical leverage law violates the half-cap. Section 6 gives an exact example where the old hypothesis fails maximally while (3.2) gives an explicit strong bound.

## 4. Proof

Fix `t in R`. Put

`h_{i,t}(x)=f_i(x) exp(i t V_i(x)).`                               (4.1)

Then for every `1<=p<=infinity`,

`||h_{i,t}||_p <= 1`,                                             (4.2)

using `f_i<=1` and `int f_i=1`.

Push the complex product measure with density `prod_i h_{i,t}` forward by `x -> R^T x`. Since `R` has rank three, the pushforward has an `L^1(R^3)` density `g_t` with `||g_t||_1<=1`. Its Fourier transform is exactly

`hat g_t(xi)=prod_i hat h_{i,t}(r_i dot xi).`                     (4.3)

The next estimate is the new step.

### 4.1 Arbitrary-basis Brascamp--Lieb estimate

For every `i` with `alpha_i>0`, use the one-dimensional linear map

`B_i xi = r_i dot xi`

with exponent `alpha_i`. By Lieb's Gaussian formula, its Brascamp--Lieb constant is

`BL = sup_{lambda_i>0}`
` [ prod_i lambda_i^(alpha_i) / det(sum_i alpha_i lambda_i r_i r_i^T) ]^(1/2).` (4.4)

Cauchy--Binet expands the denominator as

`det(sum_i alpha_i lambda_i r_i r_i^T)`
` = sum_{|S|=3} det(R_S)^2 prod_{i in S}(alpha_i lambda_i).`       (4.5)

Restrict the sum to the support of `w` and apply weighted AM--GM:

`det(...)`
` >= prod_S [ det(R_S)^2 prod_{i in S}(alpha_i lambda_i) / w_S ]^(w_S)`
` = G_R(w) prod_i (alpha_i lambda_i)^(alpha_i).`                  (4.6)

Therefore

`BL <= G_R(w)^(-1/2) prod_i alpha_i^(-alpha_i/2).`                (4.7)

Rows with `alpha_i=0` do not occur in any supported basis and may be dropped from the product estimate.

Now apply Brascamp--Lieb to

`F_i(s)=|hat h_{i,t}(s)|^(1/alpha_i).`

This gives

`||hat g_t||_1`
` <= G_R(w)^(-1/2) prod_i alpha_i^(-alpha_i/2)`
`       prod_i ||hat h_{i,t}||_(1/alpha_i).`                      (4.8)

Because `alpha_i<=1/2`, the conjugate Hausdorff--Young exponent `q_i=1/alpha_i` lies in `[2,infinity]`. The sharp complex Hausdorff--Young bound used in the separable-phase source gives

`||hat h_{i,t}||_(1/alpha_i)`
` <= (2pi)^(alpha_i)`
`    (1-alpha_i)^(-(1-alpha_i)/2) alpha_i^(alpha_i/2).`           (4.9)

The `alpha_i` powers cancel exactly with (4.7). Since `sum alpha_i=3`,

`boxed:`
`||hat g_t||_1 <= (2pi)^3 B(alpha) G_R(w)^(-1/2).`               (4.10)

This is the product-space rearrangement step. It is uniform in `t` and in every coordinate-separable phase `V_i`.

### 4.2 Quadratic Fresnel inversion

The characteristic function is

`phi_T(t)=int_R3 exp(i t y^T Lambda y) g_t(y) dy.`                 (4.11)

Insert a Gaussian cutoff `exp(-epsilon |y|^2)`, Fourier-invert `g_t`, and use Fubini as in the source separable-phase proof. The three-dimensional Gaussian integral gives, uniformly in the dual frequency,

`|K_(epsilon,t)(xi)|`
` <= pi^(3/2) |t|^(-3/2) |det Lambda|^(-1/2).`                   (4.12)

Letting `epsilon downarrow0` yields, from (4.10),

`|phi_T(t)|`
` <= min{1, K |t|^(-3/2)},`                                      (4.13)

where

`K = pi^(3/2) B(alpha) G_R(w)^(-1/2) |det Lambda|^(-1/2).`       (4.14)

The pointwise `1` is only the trivial characteristic-function bound of the actual probability law. No scalar law-uniform stationary-phase estimate is asserted.

### 4.3 Exact time integration

For every `K>0`,

`int_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3).`                       (4.15)

Hence `phi_T in L^1`, Fourier inversion gives a continuous `C_0` density, and

`||p_T||_infinity`
` <= (1/(2pi)) 6 K^(2/3)`
` = 3 B(alpha)^(2/3) [|det Lambda|G_R(w)]^(-1/3).`               (4.16)

This is (3.2). Equation (3.4) follows from (3.3). QED.

## 5. Exact capped-basis optimization dual

The determinant-entropy currency itself has a useful finite-dimensional dual. Define

`G_* = max { G_R(w) : w basis law, alpha_i(w)<=1/2 for every i }`.(5.1)

Whenever the feasible set is nonempty,

`boxed:`
`G_* = inf_(0<x_i<=1) det(R^T D_x R) prod_i x_i^(-1/2),`         (5.2)

where `D_x=diag(x_i)`.

Indeed, Lagrange multipliers `theta_i>=0` for the half-cap constraints give

`sup_w [ H(w)+sum_S w_S log det(R_S)^2 - sum_i theta_i alpha_i ]`
` = log sum_S det(R_S)^2 exp(-sum_{i in S}theta_i).`              (5.3)

Adding `(1/2)sum theta_i` and putting `x_i=e^(-theta_i)` gives (5.2) by Cauchy--Binet. This is exact finite-dimensional entropy duality, not a probabilistic approximation.

A useful corollary is therefore

`||p_T||_infinity <= 3e [ |det Lambda| G_* ]^(-1/3).`            (5.4)

The sharper (3.2) should be used when the optimizing marginals are known because it retains `B(alpha)` rather than replacing it by `e^(3/2)`.

## 6. Fully dense rotated indefinite example outside the canonical half-leverage gate

Take

`R =`
`[[8,0,0],`
` [0,1,0],`
` [0,0,1],`
` [1,0,0],`
` [0,1,0],`
` [0,0,1]]`                                                      (6.1)

and

`Lambda =`
`[[ 2,-4,-4],`
` [-4, 2,-4],`
` [-4,-4, 2]].`                                                   (6.2)

The eigenvalues of `Lambda` are `6,6,-6`, so `|det Lambda|=216`. Put `A=R Lambda R^T`. Explicitly,

`A =`
`[[128,-32,-32, 16,-32,-32],`
` [-32,  2, -4, -4,  2, -4],`
` [-32, -4,  2, -4, -4,  2],`
` [ 16, -4, -4,  2, -4, -4],`
` [-32,  2, -4, -4,  2, -4],`
` [-32, -4,  2, -4, -4,  2]].`                                  (6.3)

Every physical entry is nonzero, so no coordinate axis is an eigenvector; the form is genuinely nonseparable in the independent coordinates. Exact symbolic calculation gives

`spec(A)={156,12,-30,0,0,0}.`                                    (6.4)

Thus it is indefinite and has exactly three nonzero eigenvalues, all of absolute value at least `12`, well inside the owner target.

The canonical Gram matrix is

`R^T R = diag(65,2,2).`                                          (6.5)

Hence the canonical leverage of physical row 1 is

`c_1=64/65>1/2.`                                                  (6.6)

So the earlier canonical-leverage Theorem F does **not** apply.

On the other hand, the nonzero physical bases are exactly the eight triples that choose one row from each parallel pair `{1,4}`, `{2,5}`, `{3,6}`. Put the uniform law on those eight bases. Every physical marginal is then exactly

`alpha_i=1/2.`                                                    (6.7)

Four bases contain row 1 and have squared determinant `64`; four contain row 4 and have squared determinant `1`. Therefore

`H(w)=log 8,`
`sum_S w_S log det(R_S)^2 = (1/2)log64=log8,`

and hence

`boxed: G_R(w)=64.`                                               (6.8)

Because every feasible basis law must choose exactly one row from each parallel pair, the half-cap forces both rows in every pair to have marginal exactly `1/2`. Entropy is then maximized by the uniform eight-basis law, while the determinant-energy expectation is fixed; hence in fact `G_*=64` exactly.

For six marginals equal to `1/2`,

`B(alpha)=2^(3/2),   B(alpha)^(2/3)=2.`                           (6.9)

The new theorem gives the exact numerical certificate

`boxed:`
`||p_(X^T A X)||_infinity`
` <= 3*2*(64*216)^(-1/3)`
` = 1/4.`                                                         (6.10)

Moreover `p_(X^TAX) in C_0(R)`.

This is a genuinely rotated indefinite target matrix on which the canonical leverage hypothesis fails, while a rebalanced physical-basis law restores the product-Fourier estimate with an explicit constant.

## 7. Designated partner applied to an actual inequality

The freshest completed designated `account02/B04` theorem is r22, `QFORM-ZEROPIVOT-J1-WEIGHTED-MIXED-HUB-v1`, source pinned above. On its own fully dense target-valid matrix

`A_*=`
`[[0,4,4,4,4,4],`
` [4,3,2,3,4,5],`
` [4,2,6,6,8,10],`
` [4,3,6,11,12,15],`
` [4,4,8,12,18,20],`
` [4,5,10,15,20,27]],`                                          (7.1)

its exact one-anchor packet is

`J_h=158720.`                                                     (7.2)

Therefore the partner theorem gives the literal full-law inequality

`boxed:`
`||p_(X^T A_* X)||_infinity`
` <= 3*2^(4/3)*158720^(-1/6)`
` = 1.027359969793547... ,`                                      (7.3)

with `p in C_0(R)`. This is a positive application of the designated partner result, not merely a citation.

## 8. Preserved failed mechanism from the beginning of this run

I first tried to enlarge r22 by replacing its literal residual `D+lambda vv^T` with

`D+lambda vv^T+a b^T+b a^T`

and shifting the hub variable `x_h -> x_h+b dot x`. Algebraically this removes the hub-aligned quadratic term, but probabilistically the transformed hub factor becomes

`f_h(z-b dot x)`,                                                 (8.1)

which is no longer a product factor independent of the bank variables. Replacing it by its pointwise cap before the bank Fourier factorization destroys exactly the cancellation needed for the r22 Brascamp--Lieb bound. Therefore **no hub-gauge extension is claimed** from that change of variables. The false start is preserved here to prevent future workers from silently using it.

The valid theorem above instead changes the mechanism: it keeps every original coordinate product factor and rebalances the physical basis law inside the same rank-three Fresnel representation.

## 9. What remains unpaid

The new theorem solves the following branch:

> a physical principal block can be written as diagonal plus a rank-three core `R Lambda R^T`, and the row-vector matroid admits a half-capped physical basis law with target-scale determinant-entropy currency.

The first structural implication still missing for the full target is

`QFORM-BASIS-CAP-OR-LOCALIZED-EXIT-v1`:

starting only from three eigenvalues of `A` with absolute value at least one, either produce an ORIGINAL-coordinate principal block and rank-three representation with

`|det Lambda| G_*(R) >= c>0`,

or show that failure of the half-capped basis polytope / collapse of its determinant-entropy currency forces one of the already-paid localized pair, J1/J2, principal-curvature, ridge, grouped-hub, square-bank, or low-rank endpoints. Exact infeasibility of the half-cap means every basis law has a physical coordinate of marginal `>1/2`; that is a matroid/base-packing concentration witness, but converting it into a universally quantitative paid exit remains open.

The unrestricted conjecture and unrestricted continuity conclusion remain OPEN.
