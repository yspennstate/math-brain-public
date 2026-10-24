# account02/B18 — full invertible three-bank compression via LPP + product-transversality

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Worker:** account02/B18  
**Run:** `account02-B18-20260922T153407Z-qform-lit`  
**Assignment:** Literature-to-proof transfer  
**Method:** complementary constructions and source-valid counterexamples  
**Status:** SUPPORTING THEOREM PROVED IN STATED SCOPE / FULL CONJECTURE OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The sole target remains: for every dimension `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove

`P(X^T A X in I) <= C |I|`

for one finite universal `C`, independent of dimension, the laws and `A`, or give a valid counterexample.

The live corrections rule out replacing this by one uniformly good physical minor, one rank-three cross cut, a generic bounded spectral marginal, or post-rotation independence. The first unpaid implication for the bank route is therefore structural:

> **`QFORM-BANK-EXTRACTION-WITH-REMAINDER-v1`.** From the bare three-large-eigenvalue hypothesis, either enter an existing diffuse/ridge-window branch, or construct a bounded number of disjoint original-coordinate one-dimensional aggregates with an invertible compressed quadratic matrix bounded away from singularity, while arranging that all remaining bank dependence enters only through affine couplings to those aggregates (or proving a source-valid stability theorem for the non-bank remainder).

This report closes the exact three-bank analytic branch once such a representation exists. It does not prove the structural extraction.

## 2. Source-matching theorem transferred exactly

Primary source:

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877–889, arXiv:1507.07949, Theorem 1.1.

For a product probability density `f(x)=prod_i f_i(x_i)` with each `||f_i||_infinity<=1`, every one-dimensional orthogonal marginal has density at most `sqrt(2)`. This is the `k=1` case of their theorem; no moment, centering, support, smoothness, log-concavity, or identical-law hypothesis is present.

Hence if `I` is a physical coordinate bank, `u` is a unit vector supported on `I`, and

`Y=<u,X_I>`,

then

`||p_Y||_infinity <= sqrt(2)`.                                      (2.1)

A singleton bank has the sharper cap `1` directly from the owner hypothesis.

This transfer is source-valid because the aggregation occurs within disjoint original-coordinate banks before any rotation. It does **not** assert that arbitrary eigen-coordinates remain independent.

## 3. Completed in-fleet theorem used

A fresh completed account02/B15 theorem is source-pinned at

`yspennstate/math-open-problems@4b2e6a36bcffeb767998c43d27cee1d8f5eaa07e`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T150242Z-account02-B15-qform-r3/REPORT.md`.

Its quantitative 3-variable statement is:

> If `Z_1,Z_2,Z_3` are independent real variables with densities at most `1`, `G` is an invertible real symmetric `3x3` matrix, and `d in R^3`, `c in R`, then
> 
> `Z^T G Z + 2 d^T Z + c`
> 
> has a bounded continuous density with
> 
> `||p||_infinity <= C_3 / sigma_min(G)`,                           (3.1)
> 
> where `C_3=2*pi+3*sqrt(3)`.

The theorem allows arbitrary affine terms. The same report proves that, after conditioning on outside product coordinates, averaging the conditional continuous densities preserves continuity when the height bound is uniform.

## 4. New theorem: all invertible exact three-bank matrices

### Theorem `QFORM-LPP-FULL-THREE-BANK-v1`

Partition the original physical coordinates into four disjoint sets

`I_1, I_2, I_3, K`.

For `r=1,2,3`, let `u_r` be a unit vector supported on `I_r` and set

`Y_r=<u_r,X_{I_r}>`,  `Y=(Y_1,Y_2,Y_3)^T`.

Assume the full quadratic form has the exact original-coordinate factorization

`Q = Y^T B Y + 2 Y^T L X_K + X_K^T D X_K`,                       (4.1)

where `B` is an **arbitrary invertible real symmetric `3x3` matrix**, `L` is arbitrary, and `D` is arbitrary symmetric. Then `Q` has a bounded continuous density.

More generally, if `K_r` is any density cap for `Y_r` and

`D_K=diag(K_1,K_2,K_3)`,

then

`||p_Q||_infinity <= C_3 / sigma_min(D_K^{-1} B D_K^{-1})`.        (4.2)

In particular, by the LPP transfer (2.1), `K_r<=sqrt(2)` and therefore

`boxed( ||p_Q||_infinity
      <= 2(2*pi+3*sqrt(3)) / sigma_min(B) )`.                      (4.3)

Numerically the numerator in (4.3) is

`4*pi+6*sqrt(3) = 22.9586754597724...`.

A singleton bank may use `K_r=1` in the sharper anisotropic formula (4.2).

### Proof

Condition on `X_K=w`. Because the physical banks are disjoint from one another and from `K`, the variables `Y_1,Y_2,Y_3` remain independent under this conditioning, with exactly the same one-dimensional laws and density caps. Equation (4.1) becomes

`Q_w = Y^T B Y + 2 ell_w^T Y + c_w`,                              (4.4)

where `ell_w,c_w` are deterministic for the conditional problem.

Let

`Z_r=K_r Y_r`,  `Z=D_K Y`.

Then

`p_{Z_r}(z)=K_r^{-1}p_{Y_r}(z/K_r)<=1`,

and the three `Z_r` remain independent. Rewriting (4.4),

`Q_w = Z^T G Z + 2 d_w^T Z + c_w`,                               (4.5)

with

`G=D_K^{-1} B D_K^{-1}`.                                          (4.6)

Since `B` and `D_K` are invertible, so is `G`. Apply the source-pinned account02/B15 theorem (3.1): for every `w`,

`||p_{Q|X_K=w}||_infinity <= C_3/sigma_min(G)`,                   (4.7)

and the conditional density is continuous. The right side is independent of `w`; averaging over `X_K` gives (4.2), and dominated convergence gives a continuous representative for the unconditional density.

For (4.3), let `K_max=max_r K_r<=sqrt(2)`. For every vector `x`,

`||D_K^{-1} B D_K^{-1}x||
 >= sigma_min(D_K^{-1}) sigma_min(B) ||D_K^{-1}x||
 >= sigma_min(B) ||x||/K_max^2`.

Thus

`sigma_min(D_K^{-1}BD_K^{-1}) >= sigma_min(B)/K_max^2
 >= sigma_min(B)/2`,                                               (4.8)

and (4.3) follows.

No rotated independence is used anywhere: LPP is applied separately inside each disjoint physical bank, after which the three scalar bank variables are genuinely independent.

## 5. Application of the designated partner result

The fresh completed designated partner report is account03/B18:

`yspennstate/math-open-problems@fed3c111191d2d5cf938405d03acf91ceb7d62ad`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/B18-20260922T145749Z-r12/REPORT.md`.

It proves `QFORM-THREE-BANK-SCHUR-SMOOTHING-v1`: under exactly the same physical-bank factorization (4.1), a scalar pivot whose two-bank Schur complement is definite gives

`||p_Q||_infinity <= 4sqrt(pi)/(|a det B|)^(1/4)`,                (5.1)

with a sharper cap-sensitive formula. That theorem retains dependence in the completed square correctly by using a conditional mixture-of-translations argument.

The new theorem (4.2) **strictly broadens the admissible compressed matrices**: it requires only invertibility of `B`, with no Schur-sign condition. It does not dominate (5.1) numerically; the partner bound can be much sharper where its hypothesis holds. Thus the two results should be used as follows:

- use account03/B18 when a definite Schur pivot is available, to obtain its determinant-sensitive constant;
- otherwise use (4.2) for any exact invertible three-bank compression.

For the partner's explicit matrix

`B_0=[[31/16,-1/16,1/4],[-1/16,31/16,1/4],[1/4,1/4,-1]]`,

its theorem gives `2sqrt(2pi)=5.013...`; (4.2) independently supplies a finite continuous-density bound because `B_0` is invertible. This is a consistency check, not a claim that the new constant is sharper.

## 6. Strict-extension target family: no definite Schur pivot

To show that (4.2) genuinely adds scope beyond the partner's definite-Schur branch, put

`M=[[1,2,1],[2,1,1],[1,1,1]]`,

`s=2+sqrt(3)`, and `B_*=s M`.                                      (6.1)

The characteristic polynomial of `M` is

`(lambda+1)(lambda^2-4lambda+1)`,

so its eigenvalues are

`-1, 2-sqrt(3), 2+sqrt(3)`.

Therefore the eigenvalues of `B_*` are exactly

`-(2+sqrt(3)), 1, 7+4sqrt(3)`,                                    (6.2)

and hence

`sigma_min(B_*)=1`.                                                (6.3)

Every scalar pivot fails the definite-Schur hypothesis. For the unscaled `M`:

- pivot `3` has Schur complement `[[0,1],[1,0]]`, determinant `-1`;
- pivots `1` and `2` each have Schur complement `[[-3,-1],[-1,0]]`, determinant `-1`.

Thus all three Schur complements are indefinite. Moreover the three physical `2x2` principal determinants of `M` are `-3,0,0`, so there is no definite physical pair either.

Now, for every `m>=1`, split `3m` original coordinates into three size-`m` banks and let `c_r` be the normalized all-ones vector on bank `r`. Let `C_m` have columns `c_1,c_2,c_3`, so `C_m^T C_m=I_3`, and set

`A_m=C_m B_* C_m^T`.                                               (6.4)

The nonzero spectrum of `A_m` is exactly (6.2), so every `A_m` satisfies the owner's three-large-eigenvalue hypothesis. All physical entries are `O(1/m)`, yet for every admissible cap-one product source the three bank aggregates are independent with density caps at most `sqrt(2)`. Applying (4.3) and (6.3) gives the dimension-free bound

`boxed( ||p_{X^T A_m X}||_infinity
      <= 4*pi+6*sqrt(3)
      =22.9586754597724... )`.                                    (6.5)

The density is continuous as well.

This family lies outside the definite-Schur condition for every pivot, so (6.5) is a strict scope extension of the designated partner theorem. It also exhibits the same aggregation-before-minor phenomenon emphasized by the live correction inbox: useful curvature may be invisible in every fixed physical minor while remaining nondegenerate after a product-valid bank compression.

## 7. Source/correction reconciliation

The proof respects the live correction set.

- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`: no spectral rotation is used; only disjoint physical-bank functions are aggregated.
- `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`: no claim is made that a useful local pivot or cut is forced.
- `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`: no reciprocal single-triple determinant is paid before aggregation.
- `QFORM-FIBER-SUP-DIMENSION-LOSS` and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`: no generic projected-density or X-ray bound is substituted for product provenance.
- `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`: no absolute Fourier `L1` criterion is used.

The new theorem is an exact-factorization theorem, not a universal extraction theorem. In particular, an approximate bank decomposition cannot be perturbed naively: residual dependence inside a bank can destroy the independence/cap structure of the aggregate after conditioning.

## 8. Full-problem status and next attempt

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.

**MATHEMATICAL CHANGE:** the three-bank analytic payment is no longer restricted to definite Schur pivots. Any exact product-valid three-bank factorization with invertible compressed `B` is now sufficient, with a continuous-density estimate depending only on `sigma_min(B)` and the one-dimensional bank caps.

The first remaining implication is `QFORM-BANK-EXTRACTION-WITH-REMAINDER-v1` from Section 1. The ridge-window theorem on current control gives a complementary full-density branch when the spectral-window projection has small coordinate leverage. The hard regime is therefore high-leverage and nonseparable: convert that structure into a product-valid bank compression with controlled remainder, rather than extracting one local minor.

No counterexample to the owner conjecture was found in this run; no full solution is claimed.
