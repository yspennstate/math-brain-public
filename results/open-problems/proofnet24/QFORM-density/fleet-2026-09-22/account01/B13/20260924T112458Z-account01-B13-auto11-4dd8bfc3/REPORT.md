SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-24T11:24:58.245005Z.
attacking: pay the account02/B13 translation-gradient misalignment endpoint by an aggregate original-coordinate Fourier receiver for a rank-one quadratic plus a transverse affine bank, and route the remaining product geometry without selecting a tiny physical minor.

# account01/B13 — aggregate affine-wedge receiver and product-set routing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws / analytic derivation and exact structural identities  
Run: `20260924T112458Z-account01-B13-auto11-4dd8bfc3`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING THEOREMS / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN / CONTINUITY OPEN**.

The unrestricted target remains OPEN / NOT PROVED / NOT DISPROVED. No statement below assumes connected supports, moments, log-concavity, a single interval extremizer, centered uniforms, post-rotation independence, or law-uniform pointwise quadratic-phase decay.

## 1. Source boundary and exact product-law reduction retained

Fresh control was read from `yspennstate/math-research-brain/main`; OWNER CONTROL is revision `2026-09-22.15`. The live correction inbox still rules out the pointwise Fresnel shortcut, rotation-preserves-independence, arbitrary-joint coarea, bounded-diameter localization, and a uniform fragment-count reduction.

The extremal-law reduction proved in the preceding account01/B13 report is retained at its exact scope:

`QFORM-GLOBAL-FINITE-CERTIFICATE-PRODUCT-PURIFICATION-v1`:
for arbitrary cap-one probability densities and any finite bounded measurable certificate family, there are measurable unit sets in the original coordinates preserving all certificate expectations exactly. In particular every individual slab witness transfers with zero loss, for the same `A` and the same interval `J`, to a unit-measure product-indicator witness. Its canonical source is

`yspennstate/math-open-problems@ceb97940391426cb7914cfa180429566be831379`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260924T093120Z-account01-B13-qform-auto11/REPORT.md`.

When the shell-defect quantity below is needed, one may approximate a strict measurable unit-product witness in product measure by bounded finite-union unit sets with arbitrarily small loss. No uniform diameter or fragment count is inferred.

## 2. Completed designated partner actually applied

The newest completed account02/B13 result consumed in this run is its corrected r13 compatible-affine theorem:

- canonical report: `yspennstate/math-open-problems@ade0b364b2afd0a7049b1491e78e2e020ce86810`,
  `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260924T105434Z-account02-B13-QFORM-r13/FINAL_REPORT.md`;
- correction that wins over the initial same-run report: `yspennstate/math-open-problems@53dfa26f9fbe756959fd08ae76a0560b8307390d`, same run `CORRECTION.md`.

It explicitly withdraws the old use of a rank-one grouping theorem for an arbitrary physical affine vector. I do not revive that error.

In the forced ultracollapsed chamber it gives

`A=M_C+F`,
`M_C=D_C+lambda v v^T`, `|C|<=4`, `s_3(M_C)>=s_*`,
`F=D_(C^c)+mu w w^T`,

with

`s_*=0.7336078268845...`,
`||D_(C^c)||op <= C_D/rho`, `C_D=2sqrt(30 pi)=19.41625912555699...`,
`|mu| <= C_u/rho^2`, `C_u=32sqrt(6)e=213.06891061773865...`.

Its compatible affine core constant is

`K_core=e C_5^aff/s_* < infinity`,

valid only for outside affine vectors parallel to `v_(C^c)`.

Let a bounded finite-union unit-product witness have slab interval `J` of length `ell`, slab mass

`p=rho ell`.

Take a partner trimming `G=prod_i G_i` with total omitted marginal mass at most `p/2`. Put

`kappa_i := inf_(alpha,beta) esssup_(x in G_i) |x^2-alpha x-beta|`,
`S_kappa := sum_i kappa_i^2`.

The partner shell-radius lemma supplies centers `m_i` with physical radii `r_i<=8 kappa_i`. Write `m=(m_i)` and, on `H=C^c`,

`g_i := 2 d_i m_i + 2 mu w_i (w^T m) = 2(Fm)_i`.

Define the exact compatible-gradient mismatch

`Gamma := inf_alpha sum_(i in H) kappa_i |g_i-alpha v_i|`.

The partner theorem gives the actual inequality

`boxed:
8 Gamma + 64 A_rho S_kappa >= p/(8 K_core),`                 (2.1)

where

`A_rho := C_D/rho + C_u/rho^2
        = (C_D+C_u/rho)/rho`.                                 (2.2)

This is the partner result used below at equation level.

## 3. First new deterministic split: pay the centered quadratic remainder at the slab scale

The Taylor expansion of the retained tail at the partner centers is exact:

`x^T F x = 2(Fm)^T x - m^T Fm + (x-m)^T F(x-m)`.             (3.1)

On `G`, the shell radii and the coefficient bounds imply

`|(x-m)^T F(x-m)|
 <=64(C_D/rho+C_u/rho^2) S_kappa
 =: R_0`.                                                       (3.2)

There are now two alternatives.

### Quadratic-defect branch

If `R_0>=ell/2`, then

`boxed:
S_kappa >= p/[128(C_D+C_u/rho)].`                              (3.3)

This is a genuine product-set curvature bill: it uses `kappa`, not convex-hull diameter, so an empty remote gap does not by itself pay it.

### Small-centered-remainder branch

Assume instead

`R_0<ell/2`.                                                     (3.4)

Define the full Taylor-affine core

`Q_aff(x):=x^T M_C x + 2(Fm)^T x - m^T Fm`.                    (3.5)

The trimming removes at most `p/2` total product mass. Hence at least `p/2` of the original bad slab lies in `G`. By (3.1)-(3.4), every such point has `Q_aff(x)` in `J+[-R_0,R_0]`, an interval of length `<2ell`. Therefore

`boxed:
Q_aff has an interval ratio at least rho/4.`                    (3.6)

If also `rho>=8K_core`, then (2.1) and `R_0<ell/2=p/(2rho)` give

`8 Gamma
 > p/(8K_core)-p/(2rho)
 >= p/(16K_core)`,

so

`boxed:
Gamma > p/(128 K_core).`                                       (3.7)

The point of the next theorem is to pay this arbitrary outside affine direction without pretending it is group-compatible.

## 4. New Fourier theorem: a diffuse rank-one affine wedge is a bounded-density receiver

Let `X_1,...,X_m` be independent real variables with densities `0<=f_i<=1`. Let `v,g in R^m` be linearly independent, let `lambda!=0`, and let `s,c in R`. Put

`T=lambda(v^T X+s)^2+g^T X+c`.                                 (4.1)

Define the `2x2` coefficient Gram matrix

`G = sum_i b_i b_i^T`, `b_i=(v_i,g_i)^T`,                      (4.2)

and the affine-wedge volume

`W:=sqrt(det G)
   =sqrt(sum_(i<j)(v_i g_j-v_j g_i)^2)>0`.                     (4.3)

Whiten the physical coefficient rows:

`u_i=G^(-1/2)b_i`, `ell_i=||u_i||_2^2`.                        (4.4)

Then `sum_i u_i u_i^T=I_2` and `sum_i ell_i=2`.

### Theorem 4.1 — `QFORM-RANK1-AFFINE-WEDGE-DIFFUSE-v1`

If

`max_i ell_i <=1/2`,                                            (4.5)

then `T` has an essentially bounded density and

`boxed:
||p_T||_infinity
 <= C_A |lambda|^(-1/3) W^(-2/3),`                             (4.6)

where

`C_A=3*2^(-2/3)*e^(2/3)=3.6809866768823865...`.                (4.7)

The estimate is uniform in the square translation `s` and constant `c`.

### Proof

Use the Fourier convention

`hat f(xi)=int exp(i xi x)f(x)dx`.

The Fresnel representation gives, for `t!=0`,

`|phi_T(t)|
 <= [4 pi |lambda t|]^(-1/2) H(t)`,                            (4.8)

where

`H(t)=int_R prod_i |hat f_i(y v_i+t g_i)| dy`.                 (4.9)

The translation `s` contributes only a unit-modulus factor in the Fresnel variable.

The central estimate is

`boxed:
int_R H(t)dt <= (2pi)^2 e/W.`                                  (4.10)

To prove it, change variables in `(y,t)` by the positive matrix `G^(1/2)`. The Jacobian contributes `W^(-1)`, and the scalar arguments become `u_i^T z`. For every nonzero row write

`u_i=sqrt(ell_i) theta_i`, `||theta_i||=1`.

The frame identity becomes

`sum_i ell_i theta_i theta_i^T=I_2`.                           (4.11)

Apply the geometric Brascamp-Lieb inequality with weights `ell_i` to

`F_i(r):=|hat f_i(sqrt(ell_i) r)|^(1/ell_i)`.

Rows with `ell_i=0` contribute the harmless factor `hat f_i(0)=1`. Since (4.5) gives `q_i=1/ell_i>=2`, Beckner's sharp Hausdorff-Young inequality with

`p_i=1/(1-ell_i)`, `q_i=1/ell_i`

and `||f_i||_(p_i)<=1` yields

`int |hat f_i(xi)|^(1/ell_i) dxi
 <= 2pi ell_i^(1/2)
    (1-ell_i)^(-(1-ell_i)/(2ell_i)).`                           (4.12)

After the `sqrt(ell_i)` rescaling in `F_i`, the `ell_i^(1/2)` cancels. Therefore

`int_R2 prod_i |hat f_i(u_i^T z)| dz
 <=(2pi)^2 prod_i(1-ell_i)^(-(1-ell_i)/2).`                    (4.13)

For `0<=x<=1/2`,

`-(1-x)log(1-x)<=x`.

Since `sum ell_i=2`, the product in (4.13) is at most `e`. This proves (4.10).

Now let

`M=(2pi)^2 e/W`,
`A=M/[2 sqrt(pi)|lambda|^(1/2)]`.

Using `|phi_T(t)|<=1`, for every `R>0`,

`int_R |phi_T(t)|dt
 <=2R + A R^(-1/2)`.                                           (4.14)

The optimizer is `R=(A/4)^(2/3)`, giving

`int |phi_T|
 <=3*2^(-1/3) A^(2/3)
 <=3*2^(1/3) pi e^(2/3)
   |lambda|^(-1/3)W^(-2/3).`                                  (4.15)

Fourier inversion divides by `2pi`, yielding (4.6)-(4.7). Since the characteristic function is integrable, the density exists and is bounded. QED.

### Exact physical interpretation of the leverage gate

Put

`D_ij:=v_i g_j-v_j g_i`.                                      (4.16)

For the whitened Parseval two-frame,

`boxed:
ell_i = [sum_(j!=i) D_ij^2]/[sum_(r<s)D_rs^2].}`        (4.17)

Indeed `det(u_i,u_j)=D_ij/W`, and for a Parseval two-frame
`sum_j det(u_i,u_j)^2=||u_i||^2`.

Thus (4.5) says exactly that no one physical coordinate carries more than half of the total affine-wedge square volume. It is an original-coordinate diffuse condition, not a spectral rotation of the random vector.

## 5. Companion heavy-star receiver

The same rank-one-plus-affine model has a complementary exact physical-star estimate.

For an index `k` with `v_k!=0`, define

`S_k := [sum_(j!=k)D_kj^2]^(1/2)`.                              (5.1)

### Theorem 5.1 — `QFORM-RANK1-AFFINE-WEDGE-STAR-v1`

If `S_k>0`, then

`boxed:
||p_T||_infinity
 <=2^(7/4)|lambda|^(-1/2)|v_k|^(-1/2)S_k^(-1/2).`              (5.2)

If the leverage `ell_k=S_k^2/W^2>1/2`, this simplifies to

`boxed:
||p_T||_infinity
 <4 |lambda|^(-1/2)(|v_k|W)^(-1/2).`                           (5.3)

If `v_k=0` and `S_k>0`, conditioning all other coordinates makes `T` an affine image of `X_k`, and

`boxed:
||p_T||_infinity <= |g_k|^(-1)=||v||_2/S_k.`                   (5.4)

#### Proof of (5.2)

Let

`Z=s+sum_(j!=k)v_j X_j`.

Completing the literal original coordinate `X_k` gives

`T=lambda v_k^2 (X_k+theta(X_(not k)))^2
  + sum_(j!=k) h_j X_j + constant`,                             (5.5)

where

`h_j=g_j-(g_k/v_k)v_j=D_kj/v_k`.                               (5.6)

The usual one-coordinate square peel, uniform in the random translation `theta`, gives

`||p_T||infinity
 <= |lambda|^(-1/2)|v_k|^(-1)
    sup_t E|sum_(j!=k)h_jX_j-t|^(-1/2).`                       (5.7)

The Rogozin-Ball scalar projection bound gives density at most

`sqrt(2)/||h||_2`

for the residual linear form. The decreasing-kernel bathtub bound gives

`sup_t E|L-t|^(-1/2)
 <=2sqrt(2*sqrt(2)/||h||_2)
 =2^(7/4)||h||_2^(-1/2).`                                     (5.8)

Since `||h||_2=S_k/|v_k|`, (5.2) follows. If `S_k>W/sqrt(2)`, (5.3) follows. QED.

This star theorem is not needed to prove the diffuse theorem; it records the exact complementary physical mechanism for the next routing step.

## 6. Apply the new receiver to the designated partner inequality

Return to the partner small-centered-remainder branch (3.4), and write

`H=C^c`,
`q:=||v_H||_2`,
`D_ij:=v_i g_j-v_j g_i`,
`W^2:=sum_(i<j, i,j in H)D_ij^2`.                               (6.1)

Assume first `q>0`. The exact exterior identity is

`boxed:
W^2
 =q^2||g_H||_2^2-(v_H^Tg_H)^2
 =q^2 dist_2(g_H,span(v_H))^2.`                                (6.2)

Take the Euclidean projection coefficient

`alpha_2=(v_H^Tg_H)/q^2`.

Then Cauchy-Schwarz and the definition of `Gamma` give

`Gamma
 <=sum_(i in H)kappa_i|g_i-alpha_2v_i|
 <=sqrt(S_kappa) dist_2(g_H,span(v_H))
 =sqrt(S_kappa) W/q.`                                          (6.3)

Under (3.4),

`S_kappa < ell/[128 A_rho]
 =p/[128(C_D+C_u/rho)].`                                      (6.4)

Combine (3.7), (6.3), (6.4):

`boxed:
W^2
 > q^2 p(C_D+C_u/rho)/(128 K_core^2).`                         (6.5)

So the translation-gradient branch necessarily contains a positive amount of **aggregate original-coordinate affine-wedge volume**.

### Diffuse affine-wedge subbranch

For each outside row define its two-dimensional leverage using `(v_H,g_H)` as in (4.4). If

`max_(i in H) ell_i<=1/2`,                                     (6.6)

condition on all center coordinates `X_C`. The conditional affine core has the exact form

`lambda(v_H^T X_H+s)^2+g_H^T X_H+constant`,                    (6.7)

with the same `W`; all `D_C` terms and inside affine terms are frozen constants. Theorem 4.1 applies uniformly in the conditioning. Hence

`||p_Qaff||infinity
 <=C_A |lambda|^(-1/3)W^(-2/3).`                              (6.8)

But (3.6) says `Q_aff` has an interval ratio at least `rho/4`. Therefore

`rho/4
 <=C_A |lambda|^(-1/3)W^(-2/3)`,

or, using the exact constant `(4C_A)^3=432e^2`,

`boxed:
W^2 <=432e^2 |lambda|^(-1) rho^(-3).`                          (6.9)

Combining (6.5) and (6.9) gives the explicit mass collapse

`boxed:
p
 < [55296 e^2 K_core^2]
   /[|lambda| q^2 (C_D+C_u/rho)] * rho^(-3).`                  (6.10)

Equivalently the interval length in this diffuse affine-wedge endpoint obeys the stronger

`ell=p/rho
 < [55296 e^2 K_core^2]
   /[|lambda| q^2 (C_D+C_u/rho)] * rho^(-4).`                  (6.11)

This is not yet a contradiction—an essential-density witness may live on arbitrarily short intervals—but it is a genuine analytic payment of the diffuse translation-gradient geometry. The unpaid geometry is now the heavy affine-wedge star, not an arbitrary affine vector.

### Heavy affine-wedge subbranch

If (6.6) fails, (4.17) gives a literal physical coordinate `k in H` with

`sum_(j!=k)D_kj^2 > W^2/2`.                                   (6.12)

If `v_k!=0`, Theorem 5.1 and the ratio lower bound (3.6) imply

`boxed:
|v_k| W <256 |lambda|^(-1)rho^(-2).`                          (6.13)

If `v_k=0`, then (5.4) and (3.6) imply

`boxed:
W <4sqrt(2) q/rho.`                                            (6.14)

Thus every small-centered-remainder survivor is routed into one of two sharply stated physical configurations:

1. a diffuse two-dimensional affine coefficient frame, already paid by the aggregate Fourier theorem and forced into (6.10)-(6.11); or
2. a single heavy original coordinate carrying more than half of the exterior affine-gradient currency, with the star constraint (6.13) or (6.14).

No reciprocal individual `D_ij` is paid in this routing.

## 7. Independent pair cap and an effective-packet count

For comparison, the source-pinned theorem `QFORM-RANK1-PAIR-TRANSVERSE-AFFINE-v1` from account01/B16 (`math-open-problems@ef871949f7fbaa8e75adc9206b0eba88c7952dd7`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260922T190433Z-account01-B16-QFORM-auto11/REPORT.md`) gives, after conditioning all coordinates except an outside physical pair `{i,j}`,

`||p_Qaff||infinity
 <=6 |lambda|^(-1/3)|D_ij|^(-2/3).`                            (7.1)

The conditioned rank-one-core cross term is parallel to `v_{ij}`, so its transverse component cancels exactly; no post-rotation independence is used.

Together with (3.6), every pair obeys

`boxed:
|D_ij| <=(24/rho)^(3/2)|lambda|^(-1/2)
 =117.5755076536... |lambda|^(-1/2)rho^(-3/2).`                (7.2)

Combining (7.2) with (6.5) shows that if `lambda q!=0`, the affine-wedge packet has effective pair count

`N_eff:=W^2/[max_(i<j)|D_ij|^2]`

satisfying

`boxed:
N_eff
 > |lambda|q^2 p rho^3(C_D+C_u/rho)
   /[1,769,472 K_core^2].`                                     (7.3)

Thus even before the diffuse/star split, high density cannot put the partner's entire translation-gradient debt into one moderate physical pair: individual pair areas are forced down at the `rho^(-3/2)` scale while their aggregate exterior square mass is bounded from below by (6.5).

## 8. Degenerate carrier cases

The exterior compiler above is only invoked when `q=||v_H||>0` and `lambda!=0`.

If `lambda=0` or `q=0`, the dominant quadratic core is supported on the at-most-four center coordinates. Since `s_3(M_C)>=s_*`, the completed fixed-dimensional affine theorem used by the partner bounds the center quadratic-plus-affine density uniformly; any outside affine linear form is independent additive noise and convolution cannot increase the `L^infinity` norm. Hence the small-remainder affine-core ratio (3.6) is already impossible once `rho` exceeds the corresponding universal fixed-dimensional constant. No wedge argument is needed there.

## 9. Exact scope and first unpaid implication

What is now proved in the partner ultracollapse chamber is the following product-set trichotomy for sufficiently large `rho`:

- **quadratic-defect payment:** (3.3), a genuine fragmentation-sensitive `kappa` lower bound;
- **diffuse affine-wedge payment:** (6.5)+(6.9), via a new aggregate Fourier/BL receiver with no selected minor;
- **heavy physical affine-wedge star:** one literal coordinate satisfies (6.12) together with (6.13) or (6.14).

The first unpaid implication is therefore

`QFORM-HEAVY-AFFINE-WEDGE-STAR-TO-ROUGH-PRODUCT-RECEIVER-v1`:

> In the partner ultracollapsed normal form, consume the single-heavy-coordinate branch while retaining the centered diagonal remainder and the secondary rank-one remainder on the actual product set; or show that the all-budget trimming can always be chosen to force the quadratic-defect branch. A valid closure must remain uniform as `v_k->0` and must not replace coefficient-small quadratic tails by small random variables without a support/moment payment.

The full arbitrary-matrix conjecture remains OPEN. The general non-exact-rank-two skeleton and dependent small spectral tails remain separate assembly obligations.

## 10. Finite algebra checks

A direct random finite-dimensional check of the identities used above gave

`max |det(B^T B)-sum_(i<j)D_ij^2| <4.0e-13`,

`max_i |ell_i-[sum_(j!=i)D_ij^2]/W^2| <6.7e-16`

over 1000 random ten-row coefficient frames.

Constants checked exactly/numerically:

`C_A=3*2^(-2/3)e^(2/3)=3.6809866768823865...`,
`(4C_A)^3=432e^2=3192.07223473804...`,
`24^(3/2)=117.57550765359255...`,
`128*24^3=1,769,472`.

Model self-report: `GPT-5.6 Sol`. Configured thinking level: `UNKNOWN_NOT_EXPOSED`. Provider reasoning tokens and provider thinking seconds: `null / not exposed`.
