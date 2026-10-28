SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T22:52:25Z.
attacking: the generic ultra-coloop shared-hub gluing obstruction; replace the previous three independent scalar-bank receiver by a one-scalar-bank plus one arbitrary two-dimensional transverse-bank receiver, and audit the orientation-free rank-two affine half-Riesz compiler.

# account01/B10 — a two-bank shared-hub receiver and an independent audit of the rank-two affine compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Status: `NEW_ANALYTIC_RECEIVER / NEW_CONTINUITY_BRANCH / PARTNER_RESULT_APPLIED / INDEPENDENT_REVIEW_PASS / GENERIC_RANK3_OPEN / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source and correction boundary


The immediate account01/B10 predecessor is

`yspennstate/math-open-problems@a267ad08c9b713a974a31759ff8bb4da63c69fd4`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260923T222440Z-account01-B10-QFORM-auto11/REPORT.md`.

It proved a three-*scalar*-bank receiver for

`Q=2sZY+bY^2+2cYW+dW^2`

when `Z,Y,W` are genuinely independent original-bank aggregates. The current run removes the requirement that `Y` and `W` be independent: they may have an arbitrary joint density, provided the entire two-dimensional vector `(Y,W)` is source-disjoint from `Z`.

The designated partner actually used is account02/B10:

`yspennstate/math-open-problems@ca0549ef8c582478415aba1a953bdc6115fe84c6`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T214702Z-account02-B10-QFORM-auto11/REPORT.md`.

Its target-valid near-coloop family has the exact ORIGINAL-bank factorization

`Q_rho=2ZY+W^2`,                                                     (1.1)

with a hub/longitudinal bank carrying `Z` and a transverse collection carrying `(Y,W)`.

A classical external input used below is the sharp fixed-dimensional marginal theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949: if `X_i` are independent with densities bounded by one, then the density of every `k`-dimensional orthogonal projection is bounded by `2^(k/2)`. Only the case `k=2`, hence bound `2`, is used.

## 2. Elementary half-potential input

If `S` has probability density bounded by `K`, then

`sup_a E |S-a|^(-1/2) <= 2 sqrt(2K)`.                                (2.1)

This is the bathtub bound: among densities of mass one and height at most `K`, the symmetric decreasing kernel `|x-a|^(-1/2)` is maximized by `K 1_{|x-a|<=1/(2K)}`.

A useful quadratic pullback consequence is the following. If `f` is a probability density with `||f||_infinity<=K`, `A!=0`, `d!=0`, then for every `u`,

`int_R f((u-dw^2)/A) dw
 <= 2 sqrt(2K) sqrt(|A|/|d|).`                                      (2.2)

Indeed the substitution `z=(u-dw^2)/A`, summing both real roots when they exist, gives

`int f((u-dw^2)/A)dw
 =sqrt(|A|/|d|) int_domain f(z)|u/A-z|^(-1/2)dz`,

and (2.1) proves (2.2). No support or regularity is assumed.

## 3. Main theorem: one scalar bank plus one dependent two-dimensional bank

### Theorem 3.1 — `QFORM-TWO-BANK-HYPERBOLIC-SQUARE-RECEIVER-v1`

Let `Z` be independent of the random vector `(Y,W)`. Assume

`||p_Z||_infinity <= K_Z`,
`||(p_(Y,W))||_infinity <= K_2`,                                    (3.1)

where no independence between `Y` and `W` is assumed. Let `s,d` be nonzero real numbers and `b,c` arbitrary. Put

`Q=2sZY+bY^2+2cYW+dW^2`.                                             (3.2)

Then `Q` has a **continuous** density and

`boxed: ||p_Q||_infinity
 <= 6 (K_Z K_2)^(2/3) (|s|^2 |d|)^(-1/3).`                           (3.3)

The bound is insensitive to arbitrary fragmentation of the source densities.

### Proof

Shear only the two-dimensional output coordinates:

`W_1=W+(c/d)Y`,
`kappa=b-c^2/d`.                                                      (3.4)

The map `(Y,W)->(Y,W_1)` has Jacobian one, so its joint density still has cap `K_2`; it remains independent of `Z`. Equation (3.2) becomes

`Q=2sZY+kappa Y^2+dW_1^2`.                                           (3.5)

Write `rho(y,w)` for the joint density of `(Y,W_1)` and

`m(y)=int rho(y,w)dw`.                                                (3.6)

For `y!=0`, conditioning on `(Y,W_1)=(y,w)` and changing the independent scalar variable `Z` gives the density contribution

`p_Q(q)=int_R [A_y(q)/(2|s||y|)]dy`,                                 (3.7)

where

`A_y(q)=int_R rho(y,w)
 p_Z((q-kappa y^2-dw^2)/(2sy))dw`.                                  (3.8)

The set `Y=0` has probability zero because `(Y,W_1)` has a joint density.

There are two complementary bounds for `A_y(q)`. First, using `p_Z<=K_Z`,

`A_y(q)<=K_Z m(y)`.                                                   (3.9)

Second, using `rho<=K_2` followed by (2.2) with `A=2sy`,

`A_y(q)
 <=K_2 int p_Z((q-kappa y^2-dw^2)/(2sy))dw
 <=4 K_2 sqrt(K_Z |s|/|d|) sqrt(|y|).`                              (3.10)

Fix `R>0`. On `|y|<=R`, insert (3.10) into (3.7):

`int_|y|<=R A_y(q)/(2|s||y|)dy
 <=8 K_2 sqrt(K_Z/(|s d|)) sqrt(R).`                                 (3.11)

On `|y|>R`, use (3.9), `int m=1`, and `1/|y|<=1/R`:

`int_|y|>R A_y(q)/(2|s||y|)dy
 <=K_Z/(2|s|R).`                                                     (3.12)

Thus, uniformly in `q`,

`p_Q(q)<= A sqrt(R)+B/R`,                                             (3.13)

with

`A=8 K_2 sqrt(K_Z/(|s d|))`,
`B=K_Z/(2|s|)`.                                                       (3.14)

The minimum over `R>0` occurs at `R=(2B/A)^(2/3)` and equals

`3*2^(-2/3) A^(2/3) B^(1/3)
 =6 (K_Z K_2)^(2/3)(|s|^2|d|)^(-1/3)`,                              (3.15)

which is (3.3).

It remains to justify the stated continuity, rather than merely essential boundedness. For almost every fixed `y!=0`, the finite slice measure `rho(y,w)dw` is absolutely continuous; its pushforward under `w -> kappa y^2+d w^2` has an `L^1` density. The function in `q` appearing in (3.8)/(3.7) is therefore the convolution of two `L^1` functions: that pushforward density and the scaled density of `2syZ`. Hence it is continuous in `q` for almost every fixed `y!=0`.

For `0<delta<R<infinity`, the integral over `delta<=|y|<=R` is continuous by dominated convergence, using (3.9) and the integrable majorant `K_Z m(y)/(2|s|delta)`. The omitted near-zero part is uniformly at most

`8 K_2 sqrt(K_Z/(|sd|)) sqrt(delta)`,                                (3.16)

by (3.11), and the omitted far tail is uniformly at most

`K_Z/(2|s|R)`,                                                       (3.17)

by (3.12). Letting `delta downarrow0` and `R to infinity` shows that `p_Q` is a uniform limit of continuous middle truncations. Thus the density has a continuous representative. QED.

### Why this is genuinely stronger than the previous receiver

The preceding account01/B10 theorem required **three independent scalar banks** `Z`, `Y`, `W`. Theorem 3.1 only requires a **two-bank split**:

- one scalar bank furnishing `Z`;
- one disjoint bank furnishing the entire two-dimensional vector `(Y,W)`.

The two transverse coordinates may be arbitrarily dependent. This is exactly the dependence pattern produced by a mixed original-coordinate transverse frame and therefore removes one complete source-separation requirement from the ultra-coloop gluing problem.

## 4. Exact rank-three null-axis geometry

Let

`A=RMR^T`, `R^TR=I_3`,                                               (4.1)

where `M` is symmetric, invertible and every eigenvalue has magnitude at least one. Let `r` be a unit null-Rayleigh direction,

`r^TMr=0`,                                                           (4.2)

and set

`s=||Mr||`, `v=Mr/s`.                                                 (4.3)

Complete `(r,v)` to an orthonormal basis `(r,v,q)`. In this basis

`M=[[0,s,0],[s,b,c],[0,c,d]]`,                                       (4.4)

so

`det M=-s^2 d`,
`D:=|det M|=s^2|d|`.                                                  (4.5)

Because every singular value of `M` is at least one,

`s>=1`, `D>=1`.                                                       (4.6)

Suppose the ORIGINAL coordinates admit a source-disjoint split in which one bank produces the full scalar projection `Z` in the `r` direction, while a disjoint bank produces the full transverse vector `(Y,W)` in the `(v,q)` plane. Spectral shears (4.4)->(3.5) do not alter source variables and have determinant one in the transverse plane. Therefore Theorem 3.1 gives

`||p_Q||_infinity
 <=6 (K_Z K_2)^(2/3) D^(-1/3).`                                     (4.7)

If the scalar bank contains a physical hub coefficient `sqrt(h)` on one original cap-one variable, then convolution with every other independent scalar-bank contribution cannot increase the cap, so

`K_Z<=h^(-1/2)`.                                                     (4.8)

If the transverse bank is an orthogonal two-dimensional projection of independent cap-one originals, the Livshyts--Paouris--Pivovarov theorem gives

`K_2<=2`.                                                            (4.9)

Hence

`boxed: ||p_Q||_infinity
 <=6*2^(2/3) h^(-1/3) D^(-1/3).`                                    (4.10)

In the live near-coloop numerical chamber `h>63/64` and `D>=1`, this is

`||p_Q||_infinity < 6*2^(2/3)*(64/63)^(1/3) < 9.575`.                (4.11)

The density is continuous by Theorem 3.1.

At a **true physical coloop** (`h=1`, so every other physical row lies in `r^perp`), no further bank construction is needed: the hub itself is the scalar bank and all remaining originals form the two-dimensional transverse bank. Thus every exact-rank-three null-Rayleigh true-coloop form in this scope has a continuous density with

`boxed: ||p_Q||_infinity <=6*2^(2/3)D^(-1/3)<=9.525.`                (4.12)

No independence is asserted between the two transverse spectral coordinates.

## 5. Designated account02/B10 partner applied to an actual inequality

The newest completed account02/B10 source used here is

`yspennstate/math-open-problems@ca0549ef8c582478415aba1a953bdc6115fe84c6`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T214702Z-account02-B10-QFORM-auto11/REPORT.md`.

For `0<=rho<1/64`, `c_0=1-rho`, it supplies the exact target-valid family with spectrum `{-1,1,1}` and ORIGINAL-bank identity

`Q_rho=2ZY+W^2`,                                                     (5.1)

where

`Z=sqrt(c_0)H+sqrt(rho)P`,
`Y=(1/8)sum_(1..64) U_i`,
`W=(1/8)sum_(1..64) V_i`.                                            (5.2)

The scalar bank in `Z` is disjoint from the entire transverse bank carrying `(Y,W)`. For **arbitrary** cap-one laws on every original coordinate,

`K_Z<=c_0^(-1/2)`                                                    (5.3)

by the physical hub plus convolution. Independently, the two-dimensional projection theorem gives

`K_2<=2`                                                             (5.4)

for `(Y,W)`; this use deliberately does **not** use the stronger fact that the partner's displayed `Y` and `W` happen to be source-disjoint.

Theorem 3.1, with `s=d=1`, therefore gives the actual inequality

`||p_(Q_rho)||_infinity
 <=6*2^(2/3)c_0^(-1/3)
 <6*2^(2/3)(64/63)^(1/3)
 <9.575`,                                                           (5.5)

and gives a continuous density. The numerical constant is slightly weaker than the preceding three-scalar-bank payment `<9.552`, but the hypothesis is strictly weaker: the proof survives arbitrary dependence between the two transverse projected coordinates so long as their whole two-dimensional bank remains source-disjoint from `Z`.

This is the required actual application of a completed designated-partner result.

## 6. A source-valid barrier to peeling the hub too early

Theorem 3.1 also makes the remaining generic obstruction precise. In the generic near-coloop representation

`u_0=sqrt(h)r`,
`u_i=t_i r+p_i`,
`sum_i t_i^2=1-h`,
`sum_i t_i p_i=0`,
`sum_i p_i p_i^T=I_2`,                                               (6.1)

the same original leaf can contribute to the longitudinal aggregate and to both transverse projections. The physical hub gives, after conditioning on all leaves, a scalar conditional density cap `h^(-1/2)` for the longitudinal coordinate, but that fact alone does not create the source-disjoint scalar bank required by Theorem 3.1.

Indeed, even in the partner's easier target-valid family (5.1), if one integrates the hyperbolic variable `Z` first and then discards the square curvature, the resulting envelope is proportional to

`E |Y|^(-1)`.                                                        (6.2)

For the partner's sum-of-uniform control law, `Y` has a continuous density strictly positive at zero, hence

`E |Y|^(-1)=infinity`.                                               (6.3)

Nevertheless the true output is bounded by (5.5) (and by the sharper prior three-bank estimate). Thus the logarithmic divergence is an artifact of a **hub-first scalar peel**; the `W^2` curvature must be spent before or jointly with the hyperbolic singularity. This is a target-valid demonstration of why a conditional-cap argument alone cannot finish the mixed-row collar, consistent with the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`.

The new receiver does exactly this when the scalar bank is genuinely source-disjoint: the quadratic pullback (2.2) spends the whole two-dimensional transverse density before the `1/|Y|` singularity is integrated.

## 7. Independent audit of `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`

I independently checked the immutable source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

Result: **PASS for the stated scope**. This is not a review of the full QFORM conjecture.

The points checked were:

1. **Diffuse Fourier branch.** The geometric Brascamp--Lieb exponents are used only when every row leverage is at most `1/2`, putting the Hausdorff--Young conjugates in the valid range. The complex affine phases have modulus one and do not change the `L^p` norms. The resulting `|t|^-1` rank-two envelope is used only inside the half-Riesz integral, not misreported as an `L^1` characteristic-function bound.

2. **Heavy-coordinate branch.** The two-dimensional spectral basis change is a deterministic change of coefficient representation; it does not rotate the independent original random variables. The heavy original coordinate remains independent of all remaining coordinates. The residual linear term is retained rather than silently projected away.

3. **Nonzero residual Rayleigh coefficient.** With the source notation `k=h^(-1/2)`, `D=|det Lambda|`, the rank-one residual coefficient is

`lambda_0=k^2 D/beta^2`.

The source's product

`k |beta|^(-1/2) lambda_0^(-1/4)
 =sqrt(k) D^(-1/4)`                                                   (7.1)

is exact, so the apparent reciprocal `beta` loss really cancels.

4. **Zero residual Rayleigh coefficient.** When `beta=0`, invertibility gives `D=gamma^2`; the remaining affine-in-heavy-coordinate argument uses only the scalar projection density cap on the normalized residual coordinate. No missing division by `beta` remains.

5. **Rank-three Schur identity.** For physical pivot row `v` with `|v|^2=c_i` and `a=A_ii`, writing `v=sqrt(c_i)e_1` in spectral space gives `a=c_i alpha` and

`det N=det M/alpha=c_i det M/a`,                                     (7.2)

exactly as used. The orthonormal residual frame `W=V_-T` satisfies `W^TW=I_2` because `V_-^TV_-=I-vv^T` and `T^Tv=0`.

6. **Scope.** The theorem proves essential boundedness for the stated rank-two affine half-potential and its exact-rank-three scalar-Schur consequence. It does not prove continuity there and does not apply automatically to arbitrary higher-rank Schur remainders. Those limitations are correctly stated in the source.

I found no mathematical defect in the checked Sections 3--8. Therefore this account supplies the requested existing-worker independent review as **PASS/STATED-SCOPE-ONLY**.

## 8. What changed and the first unpaid implication

Before this run, the shared-hub route required a three-way source separation into scalar `Z`, scalar `Y`, scalar `W`. Theorem 3.1 reduces that to a **one-plus-two bank split**: only the longitudinal/hub scalar must be source-disjoint from the entire transverse plane; the two transverse coordinates may remain fully dependent.

The generic punctured near-coloop state still fails that exact source split because the same mixed leaves carry `t_i`, `p_i^(1)`, and `p_i^(2)`. Smallness of `sum t_i^2=1-h` is not enough to delete that leakage for arbitrary unbounded fragmented inputs.

The first unpaid implication is therefore sharpened to

`QFORM-SHARED-HUB-ONE-PLUS-TWO-BANK-GLUING-v1`:

> In the generic diffuse near-coloop collar, either extract/triangularize one genuine original-coordinate scalar bank carrying the hub plus longitudinal leakage and a disjoint original-coordinate bank carrying the full two-dimensional transverse projection, with order-one canonical `s^2|d|=D`; or prove a grouped product-measure analogue of Theorem 3.1 that allows the longitudinal leakage to share sources with the transverse bank without reverting to a conditional-density supremum or a small-random-perturbation deletion.

The account04/B10 three-way curvature certificate and account03/B10 projected-crossing packets remain compatible structural inputs, but neither presently removes same-bank longitudinal/transverse contamination.

## 9. Status

- `QFORM-TWO-BANK-HYPERBOLIC-SQUARE-RECEIVER-v1`: **PROVED**, continuous density, explicit constant (3.3).
- Exact-rank-three true-coloop/null-axis branch with arbitrary mixed transverse coordinates: **PROVED in the stated source-disjoint endpoint scope**, continuous density, bound (4.12).
- account02/B10 exact near-coloop family: **PAID again under the weaker one-plus-two-bank hypothesis**, continuous density, `<9.575` for arbitrary cap-one originals.
- `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` and rank-three Schur consequence: **INDEPENDENT REVIEW PASS FOR STATED SCOPE**.
- Generic mixed-row punctured near-coloop exact rank three: **OPEN**.
- Arbitrary exact rank three: **OPEN**.
- Full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.

No scheduler state, task identity, cadence, email/push notification, public release, paid model/API call, cross-account authentication, or permissions were changed.
