SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T06:09:33Z.
attacking: the punctured near-null transverse-square gate in the aggregate rank-two cross-bank branch, retaining the full shear geometry instead of deleting a small quadratic coefficient.

# account02/B19 auto11 — scale-aware near-null interpolation for the rank-two aggregate cross receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Universal proof assembly / SYNTHESIS / complementary constructions and source-valid counterexamples  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

No full-target claim is made. All random variables below are original-coordinate product inputs or linear projections of such inputs used only through source-valid marginal density bounds. No moment, compact-support, log-concavity, Gaussian, post-rotation independence, arbitrary-joint coarea, uniform pointwise stationary-phase, or law-uniform coefficient-perturbation premise is used.

## 1. Source-pinned proof graph and exact first gap

The current owner synthesis leaves the no-pivot class `N3(tau)` open after the scalar/pair exits. The newest-Claude package at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

supplies the product-safe Fresnel/decoupling exits F/H/D/D'/D5. The later current file retains those theorems. In particular D' states, for a physical cross block `M=A[I,J]`, three-volume `Z=e3(M^T M)`, and volume-sampling row marginals bounded by `h<3/4`,

`||p_Q||_infinity <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z^(-1/6)`.   (1.1)

This run applies (1.1) below to an actual quantitative N3 exit.

The designated partner is account03/B19 r26, canonical report commit

`yspennstate/math-open-problems@903a525be3cb74e514e5f402b6fcca404bb5bfc5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T043056Z-account03-B19-QFORM-r26/REPORT.md`.

Its theorem `QFORM-RANK2-CROSS-TRANSVERSE-3D-CURVATURE-v1` considers disjoint original-coordinate product banks `U,V`,

`Q=U^T B U+2U^T C V+V^T D V+a^T U+b^T V+c`,                    (1.2)

where `C` has exact rank two with nonzero singular values `s1>=s2>0`, all `U`-side self curvature and the allowed `U`-affine term lie in a three-dimensional physical projection `E` containing `P=range(C)`, and `r` is a unit vector spanning `E cap P^perp`. Put

`lambda=r^T B r`, `d=PBr`, `delta=||d||`, `rho=s1 s2`.           (1.3)

For `lambda != 0` the partner proves

`||p_Q||_infinity <12.01 |lambda|^(-1/4) rho^(-3/8)`.            (1.4)

The preceding account02/B19 run proves the exact endpoint `lambda=0, delta>0` by an independent hyperbolic receiver:

`||p_Q||_infinity <7.50 delta^(-1/4) rho^(-3/8)`.                (1.5)

Thus the first analytic gap inside this branch is not the endpoint but the punctured interval `0<|lambda|<<delta`: (1.4) diverges although (1.5) is finite, and the live correction set forbids treating `lambda y^2` as a uniformly small random perturbation.

## 2. The missing scale in the partner proof

Choose orthonormal coordinates `z=(x,z_2)` on `P` so that the first axis is parallel to `d`, and put `y=r^T U`. The partner's deterministic completion is

`y' = y + lambda^(-1) d^T z = y+(delta/lambda)x`,                (2.1)

up to an irrelevant deterministic affine shift. The joint projection `(z,y')` has row Gram matrix

`[[I_2,c],[c^T,1+|c|^2]]`, `c=(delta/lambda,0)`,                 (2.2)

whose determinant is exactly one. Therefore the source-valid product-marginal theorem gives the same three-dimensional cap used by the partner,

`K3:=||p_(z,y')||_infinity <=2 sqrt(2)`.                         (2.3)

But the one-dimensional row producing `y'` has Euclidean norm

`L=sqrt(1+delta^2/lambda^2)`,                                    (2.4)

so its marginal density satisfies the strictly stronger scale-aware bound

`K1:=||p_(y')||_infinity
 <=sqrt(2)/L
 =sqrt(2)|lambda|/sqrt(lambda^2+delta^2)`.                        (2.5)

The partner proof replaced (2.5) by the coarse `K1<=sqrt(2)`. Retaining (2.5) recovers part of the hyperbolic endpoint geometry without any perturbation argument.

## 3. General interpolation theorem

### Theorem 3.1 — `QFORM-RANK2-CROSS-NEARNULL-INTERPOLATION-v1`

Under the hypotheses (1.2)-(1.3) of the designated partner, assume `lambda != 0`. For every fixed

`2<r0<4`,                                                          (3.1)

put

`p=r0/(r0-1) in (4/3,2)`,
`C_p=1/(2-p)+((2-p)/(3p-4))^((2-p)/2)`,                           (3.2)

and define

`a=(r0-2)/(2(r0+1))`,
`b=(4-r0)/(2(r0+1))`,
`c=r0/(2(r0+1))`.                                                  (3.3)

Then `Q` has a continuous density and

`||p_Q||_infinity
 <= Gamma_r0 rho^(-c) |lambda|^(-a)
      [sqrt(lambda^2+delta^2)]^(-b)`,                             (3.4)

where `Gamma_r0<infinity` is explicit:

`M_r=(2pi)^(1/r0) 2^(1/p) (sqrt(2))^(1/2) C_p^(1/p)
       (2sqrt(2))^(2/r0-1/2)`,                                   (3.5)

`D_r=pi sqrt(2) [2(r0-1)]^((r0-1)/r0) M_r`,                      (3.6)

`Gamma_r=(r0+1)/pi [D_r/(2r0)]^(r0/(r0+1))`.                     (3.7)

In particular, for every fixed `epsilon>0` one may choose `r0>2` sufficiently close to two so that the power of `|lambda|` in (3.4) is below `epsilon`. The theorem does **not** remove the punctured loss uniformly as `lambda->0`; its value is that the partner's quarter-power blow-up is not intrinsic to the same proof architecture.

### Proof

After (2.1), write the source-bank phase as

`lambda (y')^2 + F(z)`                                           (3.8)

and let `p0(z,y)` be the joint density of `(z,y')`. Define the square pushforward, for `q>0`,

`H(q,z)=[p0(z,sqrt(q))+p0(z,-sqrt(q))]/[2sqrt(q)]`.               (3.9)

Let

`g(y)=int_R2 p0(z,y) dz`, `G(y)=g(y)+g(-y)` for `y>0`.            (3.10)

Then `int_0^infinity G=1` and, by (2.5),

`0<=G<=M:=2K1
 <=2sqrt(2)|lambda|/R`, `R:=sqrt(lambda^2+delta^2)`.              (3.11)

Using `(a+b)^2<=2(a^2+b^2)` and `p0^2<=K3 p0`,

`||H(q,.)||_2^2 <= K3 G(sqrt(q))/(2q)`.                           (3.12)

Hence

`||H||_(L_q^p(L_z^2))^p
 <=2(K3/2)^(p/2) I_p`,                                           (3.13)

where

`I_p=int_0^infinity y^(1-p)G(y)^(p/2)dy`.                        (3.14)

The point is to optimize the singular integral at the actual cap `M`, not at scale one. Split at `R_*=M^(-1)`. On `(0,R_*)`,

`I_p^(near)<=M^(p/2) R_*^(2-p)/(2-p)
             =M^(3p/2-2)/(2-p)`.                                (3.15)

On `(R_*,infinity)`, Holder with exponents `2/p` and `2/(2-p)` gives

`I_p^(far)
 <=[(2-p)/(3p-4)]^((2-p)/2) R_*^((4-3p)/2)
 =[(2-p)/(3p-4)]^((2-p)/2) M^(3p/2-2)`.                          (3.16)

The restriction `p>4/3`, equivalently `r0<4`, is exactly the integrability condition in (3.16). Therefore

`I_p<=C_p M^(3p/2-2)`.                                           (3.17)

Combining (3.13), (3.17), and (3.11),

`||H||_(L_q^p(L_z^2))
 <=2^(1/p)(K3/2)^(1/2) C_p^(1/p)
    (2sqrt(2))^(2/r0-1/2)
    |lambda|^(2/r0-1/2) R^(-(2/r0-1/2))`.                       (3.18)

The Hilbert-valued Hausdorff--Young estimate follows by Riesz--Thorin between the `L^1->L^infinity` norm one and Plancherel norm `sqrt(2pi)`. Since `p'=r0`, scaling `q` by `lambda` yields, for

`F_t(z)=exp(itF(z)) int p0(z,y)exp(it lambda y^2)dy`,             (3.19)

`|| ||F_t||_2 ||_(L_t^r0)
 <= M_r |lambda|^(-(1/2-1/r0))
       R^(-(2/r0-1/2))`.                                         (3.20)

On the opposite bank, the same disintegration as in the partner theorem leaves an amplitude `b_t(w)` with `||b_t||_2<=sqrt(2)`. Two-dimensional bilinear Plancherel therefore gives

`|phi_Q(t)|
 <=pi sqrt(2) rho^(-1/2)|t|^(-1)||F_t||_2`.                     (3.21)

Let `p=r0/(r0-1)`. For `T>0`, Holder on `|t|>T` gives

`|| |t|^(-1) 1_(|t|>T)||_p
 =[2(r0-1)]^((r0-1)/r0) T^(-1/r0)`.                             (3.22)

Thus

`int_R |phi_Q(t)|dt
 <=2T + K T^(-1/r0)`,                                            (3.23)

with

`K=D_r rho^(-1/2)|lambda|^(-(1/2-1/r0))
        R^(-(2/r0-1/2))`.                                        (3.24)

Optimizing at `T=[K/(2r0)]^(r0/(r0+1))` makes the second term `2r0 T`, so Fourier inversion gives exactly (3.4)-(3.7). In particular `phi_Q` is integrable and the density is continuous. QED.

## 4. Clean quantitative corollaries

### 4.1 The `r0=3` sharpening

For `r0=3`, `p=3/2`, `C_p=3`, and the exact constants reduce to

`Gamma_3=10.22308966794036...`.                                  (4.1)

Hence

`||p_Q||_infinity
 <=10.224 [|lambda| sqrt(lambda^2+delta^2)]^(-1/8)
          rho^(-3/8)`.                                           (4.2)

For `|lambda|<<delta`, this is `O(|lambda|^(-1/8)delta^(-1/8))`, improving the designated partner's `|lambda|^(-1/4)` divergence while keeping every self block and product-provenance hypothesis.

### 4.2 A much flatter fixed exponent

Take `r0=11/5`, so `p=11/6`. Then

`C_p=6+3^(-1/6)=6.832683177655602...`,
`Gamma_(11/5)=10.174215991413659...`,                             (4.3)

and

`boxed(
 ||p_Q||_infinity
 <=10.175 rho^(-11/32)|lambda|^(-1/32)
          (lambda^2+delta^2)^(-9/64).
)`                                                               (4.4)

For the current aggregate branch

`rho>=rho0:=sqrt(29/3072)=0.097160198469675...`,
`delta>=1/64`,                                                    (4.5)

(4.4) yields the concrete punctured estimate

`||p_Q||_infinity <73.04 |lambda|^(-1/32)`.                      (4.6)

Compare the current graph: at `lambda=0`, the preceding B19 hyperbolic theorem gives `<50.86`; at `|lambda|>=1/64`, the designated partner gives `<81.43`. The only unboundedness in this receiver is now the very weak punctured factor `|lambda|^(-1/32)`, and Theorem 3.1 lets that exponent be made arbitrarily small at the expense of a larger fixed constant.

## 5. Required newest-Claude result applied at equation level

The newest-Claude D' theorem (1.1) gives a separate actual N3 exit with all self blocks and outside couplings retained. If a physical cross block `M` satisfies

`s3(M)>=1/64`, `max_i alpha_i<=2/3`,                              (5.1)

then

`Z=e3(M^TM)>=s1(M)^2s2(M)^2s3(M)^2>=64^(-6)`.                   (5.2)

Putting `h=2/3` in (1.1),

`||p_Q||_infinity
 <=9sqrt(3e) Z^(-1/6)
 <=576sqrt(3e)
 =1644.865348822354...`.                                         (5.3)

Thus any surviving branch may assume the negation of (5.1) for every candidate cross block: either its third singular value is below `1/64` or its three-volume is concentrated in a row marginal exceeding `2/3`. This is a real quantitative obstruction, not a copied source label.

## 6. Updated noncircular proof graph and first unpaid implication

The strongest current source-pinned graph is:

- physical scalar/pair completion exits reduce the unrestricted theorem to the fixed no-pivot class `N3(tau)` in the current Claude synthesis;
- F/H/D/D'/D5 plus ridge/volume-stability pay diffuse, high-volume, low-rank-plus-diagonal hub and collective-tail packets at their exact hypotheses;
- pure bipartite target matrices and several star/grouped-bank obstructions are paid by completed product-safe Fourier arguments;
- in the exact-rank-three co-heavy aggregate branch, a full physical partition can supply `rho=s1(C)s2(C)>=rho0`;
- account03/B19 r26 pays the quantitative transverse-square state by (1.4);
- account02/B19 r27 pays the exact-null hyperbolic state by (1.5);
- Theorem 3.1 here narrows the punctured near-null blow-up from quarter power to an arbitrarily small fixed power while preserving the exact source assumptions;
- newest-Claude D' separately removes any cross block satisfying (5.1).

The **first unpaid analytic implication in this receiver** is therefore:

`QFORM-RANK2-CROSS-PUNCTURED-NEARNULL-UNIFORM-v2`.

Fix universal constants `rho_0,delta_0>0`. For every finite dimension, every pair of disjoint original-coordinate product banks with scalar densities at most one, every symmetric `B,D`, every exact-rank-two `C` with `s1(C)s2(C)>=rho_0`, every three-dimensional source projection `E` with `range(C),range(B),a subset E`, and unit `r` spanning `E cap range(C)^perp`, if

`0<|lambda|=|r^TBr|<1/64`,
`delta=||PBr||>=delta_0`,                                        (6.1)

prove a density bound independent of `lambda`, the dimension, all input laws, `B,D,a,b,c`, or prove a product-preserving structural descent to an already-paid branch.

Theorem 3.1 gives for every fixed `epsilon>0` a bound `C_epsilon |lambda|^(-epsilon)` on this state, and the exact point `lambda=0` is paid, but neither fact justifies a uniform limit. A law-uniform coefficient-continuity argument is explicitly disallowed by the correction set. Arbitrary-extra-spectrum descent from global `N3` to this three-dimensional-source receiver remains a separate structural debt, so this result is not a proof of the full target.

## 7. Checks and review status

`CHECK.py` evaluates the constants directly. Its saved output records

`Gamma_3=10.22308966794036`,
`Gamma_(11/5)=10.174215991413659`,
`rho0=0.09716019846967515`,
`fixed_branch_coefficient=73.03649706738199`,
`Dprime_s3_1_64_h_2_3=1644.865348822354`,

and status `QFORM_B19_NEARNULL_INTERPOLATION_CONSTANTS_PASS`.

This theorem has **not** received an independent end-to-end review. The full QFORM theorem remains OPEN and does not have the two independent complete reviews required for a full candidate.
