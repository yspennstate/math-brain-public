SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-24T03:33:04.990943Z.
attacking: combine account02/B13 finite-center conditioning with the all-pair tau identity to force quantitative transverse-diagonal trace collapse in the two-strip survivor, while retaining the rough hub strip.

# account01/B13 — optimizer-free product reduction and transverse-diagonal collapse in the two-strip survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T033304Z-account01-B13-QFORM-auto11`  
Role: Extremal product laws / analytic structural identities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREMS PROVED**  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Unrestricted continuity: **OPEN**.

No moment, compact-support, connected-support, log-concavity, Gaussian-mixture, diagonal-basis, post-rotation independence, interval extremality, common support diameter, uniform fragment count, or probabilistic deletion of a coefficient-small quadratic tail is used.

The current live corrections are respected: no law-uniform pointwise quadratic oscillatory decay, no independence after rotating the physical variables, no projection-density-only solution of an indefinite pushforward, and no use of the diagonal `pi` estimate outside its proved control scope.

## 1. Correct optimizer-free extremal-product reduction

This section replaces the earlier unneeded threshold-attainment argument by a completely finite approximation/mixture argument on the noncompact line.

### Theorem 1.1 — `QFORM-FINITE-MIXTURE-PRODUCT-INDICATOR-REDUCTION-v1`

Let `K:R^n->[0,1]` be measurable. Let `f_i` be probability densities with

`0<=f_i<=1`, `int_R f_i=1`.

For every `epsilon>0` there exist bounded finite unions of intervals `E_i subset R`, each of Lebesgue measure one, such that

`int K(x) prod_i 1_{E_i}(x_i) dx`
` >= int K(x) prod_i f_i(x_i) dx - epsilon`.                       (1.1)

Consequently

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i`
` =sup_{E_i bounded finite unions, |E_i|=1} int_{prod_i E_i} K`.  (1.2)

Equation (1.2) is equality of suprema, not an optimizer-attainment claim.

#### Proof

It suffices first to treat one marginal. Fix `f`, `0<=f<=1`, `int f=1`, and `eta>0`.

Choose a bounded interval `I` so that

`tau:=int_{I^c} f < eta/8`.                                       (1.3)

Choose an integer `M` large enough that `I` can be replaced, at a change of tail mass smaller than `eta/8`, by an interval whose endpoints lie on the grid `(1/M)Z`, and so that cell averaging on the grid cells of length `1/M` approximates `f 1_I` in `L^1` within `eta/4`. This is the standard `L^1` convergence of local conditional expectations / step approximations.

For each grid cell `I_j subset I`, put

`p_j=M int_{I_j} f`.                                               (1.4)

Because `f<=1` and `|I_j|=1/M`, one has `0<=p_j<=1`. The cell-average function

`g_in=sum_j p_j 1_{I_j}`                                          (1.5)

has total mass `int_I f=1-tau`.

Add finitely many further disjoint grid cells of the same length outside `I` and choose coefficients in `[0,1]` on them whose sum is exactly `M tau`. This is possible using `ceil(M tau)` cells. Call the resulting function `g`. Then

`0<=g<=1`, `int g=1`,                                              (1.6)

`g` is boundedly supported and constant on finitely many pairwise disjoint cells of length `1/M`, and

`||f-g||_1<eta`.                                                   (1.7)

Indeed, inside `I` use the step approximation; outside `I` the error is at most the tail mass of `f` plus the added mass of `g`, namely `2 tau`.

Write the finitely many cell coefficients as a vector `p=(p_1,...,p_N)`. Since every cell has measure `1/M` and `int g=1`,

`p in [0,1]^N`, `sum_j p_j=M`.                                    (1.8)

The finite hypersimplex

`P={p in [0,1]^N: sum_j p_j=M}`                                   (1.9)

is the convex hull of the `0/1` vectors having exactly `M` ones. To see this directly, an extreme point cannot have two fractional coordinates, because one may perturb those two coordinates by opposite small amounts while staying in `P`; it also cannot have exactly one fractional coordinate because the coordinate sum is the integer `M`. Thus every extreme point is such a `0/1` vector, and finite-dimensional convexity gives

`p=sum_r theta_r v^(r)`, `theta_r>=0`, `sum_r theta_r=1`.          (1.10)

If `E_r` is the union of the `M` cells selected by `v^(r)`, then `E_r` is a bounded finite union with `|E_r|=1`, and

`g=sum_r theta_r 1_{E_r}`.                                        (1.11)

Apply this construction independently to each `f_i`, with `eta_i>0` and `sum_i eta_i<epsilon`. Let the resulting finite mixtures be `g_i`. The tensor-product telescoping inequality gives

`||prod_i f_i-prod_i g_i||_1 <=sum_i ||f_i-g_i||_1<epsilon`.       (1.12)

Since `0<=K<=1`,

`int K prod_i g_i >= int K prod_i f_i-epsilon`.                   (1.13)

But `prod_i g_i` is a finite convex combination of densities of product sets `prod_i E_i^(r_i)`. At least one component is no smaller than the average in (1.13), proving (1.1). Since every product indicator is itself an admissible cap-one product density, (1.2) follows. `QED`

### QFORM slab consequence

For `K=1_{x^T A x in J}` and every `delta>0`, choose the marginal approximation errors so that their sum is `<delta |J|`. If

`rho=P{X^T A X in J}/|J|`,                                        (1.14)

then a bounded finite-union unit-product-set witness exists with slab ratio at least

`rho-delta`.                                                       (1.15)

Thus every strict universal-bound violation transfers with arbitrarily small prescribed loss to bounded finite-union product indicators. There is no single-interval, centered-uniform, common-diameter, or uniform-fragment-count assertion.

**Scope correction.** The exact finite-measure quantile-threshold step written in account01/B13 run `20260924T023111Z-account01-B13-qform-auto11` is not used here and should not be used as a premise. The finite-mixture theorem above is sufficient and is valid on the noncompact line.

## 2. Source-pinned designated-partner input applied in this run

The newest compatible designated-partner report read at source refresh is account02/B13 r40:

- `yspennstate/math-open-problems@2af615c6d649e207191127733fc6dd180db14944`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260924T025738Z-account02-B13-QFORM-auto11/REPORT.md`.

Two proved pieces are used.

### 2.1 Partner finite-center conditioning

For any original-coordinate center set `E` and `B=E^c`, if a slab witness has ratio `rho`, then for almost some center value `y` the conditional polynomial

`Q_y(x_B)=x_B^T A_BB x_B+2(A_BE y)^T x_B+c(y)`                   (2.1)

under the unchanged product law on `X_B` has slab ratio at least `rho`. Conversely a bound uniform in the induced affine term may be averaged back. This is account02/B13 theorem `QFORM-FINITE-CENTER-CONDITIONING-v1`.

### 2.2 Partner two-strip algebra

In the hard exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`,          (2.2)

account02/B13 r40, consuming account03/B13 r41 at source commit

`37177f7694c9aab73604b36c452e2a92c612aad4`,

reduces high-ratio witnesses to two original-coordinate projective strips after finitely many physical centers, while retaining the exact strip matrix rather than deleting it.

The quantitative input from account03/B13 r41 that will be used below is stronger than choosing one good pair. There is a physical pivot `k` with

`|d_k|>=1`.                                                        (2.3)

In the hard non-rank-one branch, for `rho>sqrt(H0)` with

`H0=sqrt(1536 e^2)=106.534455308869...`,                           (2.4)

one has `c:=||u_k||^2>0`. Rotate **only the deterministic latent two-frame**, never the independent variables, so

`u_k=(sqrt(c),0)`, `u_i=(x_i,y_i)`, `s_i=y_i^2`.                 (2.5)

If `c_i=||u_i||^2<=1/4`, `c_j<=1/4`, and `s_i s_j>0`, then

`|tau_ij|<C_* rho^-1`,                                             (2.6)

where

`tau_ij=d_k q_ij+d_i q_kj+d_j q_ki`,
`q_ab=det(u_a,u_b)^2`,                                             (2.7)

and

`C_*=2278125/(256e^2)=1204.338641107064...`.                       (2.8)

There are at most seven indices `i!=k` with `c_i>1/4`.

These equations are the source-pinned premises; the full unrestricted QFORM theorem remains open.

## 3. New exact identity after partner finite-center conditioning

There is a useful structural fact about the affine term created by the partner's center conditioning which removes an unnecessary ambiguity.

### Lemma 3.1 — `QFORM-CENTER-INDUCED-AFFINE-ALIGNMENT-v1`

Assume `A=D+U Lambda U^T` with `D` diagonal. Condition original coordinates `E` at a value `y` and put `B=E^c`. Then exactly

`Q_y(x_B)`
`=x_B^T(D_B+U_B Lambda U_B^T)x_B`
` +2 x_B^T U_B Lambda U_E^T y +c(y)`.                              (3.1)

In particular the induced affine coefficient is

`b_B(y)=2U_B h_y`, `h_y=Lambda U_E^T y`.                           (3.2)

Hence if an exact physical direction class `G subset B` has rows

`u_i=a_i v`, `i in G`,                                             (3.3)

then both the latent quadratic dependence and the center-induced affine dependence on that class use the same scalar

`L_G(x)=sum_{i in G} a_i x_i`.                                    (3.4)

#### Proof

Because `D` is diagonal and `B cap E=empty`, `D_BE=0`. Expanding `X^T A X` at `X_E=y` gives (3.1)-(3.2). Substituting (3.3) gives

`sum_{i in G} b_i(y)x_i=2(v^T h_y)L_G(x)`,                         (3.5)

while `U_G^T x_G=v L_G(x)`. `QED`

This is the exact affine scope actually needed when account02/B13 groups direction classes after conditioning named physical centers. It does **not** claim that an arbitrary externally supplied affine vector is aligned.

## 4. New theorem: the transverse strip cannot carry arbitrary distributed diagonal curvature

Set

`alpha=rho^-1/3`.                                                   (4.1)

Let `H={i!=k:c_i>1/4}`, so `|H|<=7`, and let

`T={i notin H union {k}: s_i>=alpha}`.                             (4.2)

Rows outside `T union H union {k}` already lie in the pivot-line strip because

`dist(u_i,span u_k)=|y_i|<rho^-1/6`.                              (4.3)

For every `i in T` define the slope and normalized diagonal curvature

`t_i=x_i/y_i`,
`a_i=c d_i/s_i`.                                                    (4.4)

Then the normalized tau identity is exact:

`G_ij:=tau_ij/(s_i s_j)`
`=d_k(t_i-t_j)^2+a_i+a_j`.                                        (4.5)

By (2.6) and `s_i s_j>=rho^-2/3`,

`|G_ij|<epsilon_rho:=C_* rho^-1/3`                                (4.6)

for every distinct pair in `T`.

The exact four-point cancellation is

`G_ij+G_lm-G_il-G_jm`
`=-2 d_k(t_i-t_m)(t_j-t_l)`.                                      (4.7)

All one-vertex diagonal terms cancel.

### Theorem 4.1 — `QFORM-TWOSTRIP-TRANSVERSE-DIAGONAL-TRACE-v1`

Assume `|T|>=4`. Then after removing at most one index `o from T`, there is a transverse latent line `ell_1` such that, with `T'=T\{o}`,

`dist(u_i,ell_1)`
` <=sqrt(C_*/(2|d_k|)) rho^-1/6`
` =24.53913854547 |d_k|^-1/2 rho^-1/6`                            (4.8)

for every `i in T'`, and the actual physical diagonal coefficients on this whole bank satisfy

`boxed: |c d_i| <=(9/2) C_* s_i rho^-1/3}`                         (4.9)

and therefore

`boxed: c sum_{i in T'} |d_i| <=(9/2)C_* rho^-1/3`
`       =5419.523884982 rho^-1/3.}`                               (4.10)

Equivalently, since the residual is diagonal,

`boxed: ||c D_{T'}||_{S_1} <=5419.523884982 rho^-1/3.}`            (4.11)

No random quadratic term represented by `D_{T'}` is deleted.

#### Proof

Order the slopes in `T`:

`t_1<=...<=t_M`, `M=|T|>=4`.                                      (4.12)

Use (4.7) on the four distinct ordered positions

`i=1`, `m=M-1`, `j=M`, `l=2`.                                    (4.13)

The left side has modulus at most `4 epsilon_rho`, so

`2|d_k|(t_{M-1}-t_1)(t_M-t_2)<=4 epsilon_rho`.                   (4.14)

Thus

`(t_{M-1}-t_1)(t_M-t_2)`
` <=2C_* |d_k|^-1 rho^-1/3`.                                     (4.15)

One factor is at most

`w_k:=sqrt(2C_*/|d_k|) rho^-1/6`.                                (4.16)

Delete the opposite extreme row. The remaining `M-1>=3` slopes lie in an interval of length `w_k`. Pick `t_0` in that interval and put

`ell_1=span((t_0,1))`.                                             (4.17)

Because every surviving row has `c_i<=1/4`,

`dist(u_i,ell_1)`
`=|y_i||t_i-t_0|/sqrt(1+t_0^2)`
`<=sqrt(c_i) w_k<=w_k/2`,                                         (4.18)

which is (4.8).

For any distinct `i,j in T'`, (4.5)-(4.6) and `|t_i-t_j|<=w_k` give

`|a_i+a_j|`
`<=|G_ij|+|d_k||t_i-t_j|^2`
`<=C_*rho^-1/3+2C_*rho^-1/3`
`=3C_*rho^-1/3`.                                                   (4.19)

Since `|T'|>=3`, for each `i` choose distinct `j,l` in `T'`. The identity

`2a_i=(a_i+a_j)+(a_i+a_l)-(a_j+a_l)`                              (4.20)

gives

`|a_i|<=(9/2)C_*rho^-1/3`.                                        (4.21)

Because `a_i=c d_i/s_i`, this is (4.9). Finally the second column of `U` has Euclidean norm one, so

`sum_i s_i<=1`; hence summing (4.9) proves (4.10)-(4.11). `QED`

### Small transverse cardinality

If `|T|<=3`, all those coordinates may simply be added to the physical center set. Together with the at most seven high-leverage rows and the pivot this uses at most eleven original-coordinate centers. Account02/B13 finite-center conditioning then removes them without decreasing the slab ratio; no distributed transverse bank remains.

### One-sixth leverage/trace dichotomy

In the `|T|>=4` branch, (4.10) immediately gives

`boxed: c<rho^-1/6`

or

`boxed: ||D_{T'}||_{S_1} <=5419.523884982 rho^-1/6.}`             (4.22)

This is only a coefficient-matrix statement. The second alternative is **not** used as a probabilistic perturbation under arbitrary unbounded/fragmented product laws.

## 5. Actual application of account02/B13 finite-center conditioning

This is where the designated partner theorem enters an actual slab inequality.

In the `|T|>=4` branch choose

`E=H union {k,o}`,                                                  (5.1)

where `o` is the one transverse outlier selected in Theorem 4.1. Thus

`|E|<=9`.                                                          (5.2)

In the `|T|<=3` branch take

`E=H union {k} union T`,                                           (5.3)

so `|E|<=11`.

Apply account02/B13 theorem `QFORM-FINITE-CENTER-CONDITIONING-v1` to the actual witness inequality

`P{X^T A X in J}=rho |J|`.                                        (5.4)

There exists a center value `y` for which the remaining original coordinates retain their product law and

`P{Q_y(X_B) in J}>=rho |J|`.                                      (5.5)

In the large-transverse branch the conditional quadratic coefficient matrix is exactly

`A_BB=D_B+U_B Lambda U_B^T`,                                      (5.6)

with a partition `B=B_0 disjoint_union B_1` such that

`dist(u_i,span u_k)<rho^-1/6`, `i in B_0`,                         (5.7)

and

`dist(u_i,ell_1)`
`<24.540 |d_k|^-1/2 rho^-1/6`, `i in B_1`,                         (5.8)

while

`c ||D_{B_1}||_{S_1}<5419.524 rho^-1/3.`                          (5.9)

The induced affine term is not arbitrary hidden noise; by Lemma 3.1 it is exactly

`2 x_B^T U_B Lambda U_E^T y`.                                     (5.10)

Thus account02/B13's previous two-strip normal form is sharpened as follows:

> after finitely many product-preserving physical centers, **arbitrary distributed diagonal curvature may remain freely on the near-pivot strip, but the entire transverse strip carries only the quantitatively constrained diagonal trace currency (5.9), unless the pivot leverage itself is smaller than `rho^-1/6`.**

This is a strict narrowing of `QFORM-CENTERFREE-TWOSTRIP-DIAGONAL-BANK-RECEIVER-v1`: both strips no longer carry unconstrained distributed diagonal curvature.

## 6. Exact zero-width endpoint

The finite-ratio estimate also has a clean exact structural limit.

Suppose a transverse direction class consists of at least three rows with the same slope `t_0` and satisfies exact tau cancellation

`tau_ij=0`                                                         (6.1)

for every pair in the class. Since `t_i=t_j`, (4.5) becomes

`a_i+a_j=0`.                                                       (6.2)

For three distinct indices,

`2a_i=(a_i+a_j)+(a_i+a_l)-(a_j+a_l)=0`,                            (6.3)

so `a_i=0` for every row. As `c>0` and `s_i>0`,

`boxed: d_i=0`                                                     (6.4)

throughout that transverse class.

Therefore in the exact two-line / exact-cancellation endpoint, after at most two exceptional transverse coordinates are put among the named centers, all distributed diagonal curvature is confined to the pivot-line bank. On the zero-diagonal transverse line, Lemma 3.1 shows that both the latent quadratic term and every center-induced affine term depend on the whole bank through one physical grouped scalar. That scalar may be normalized and its density is bounded by the proved weighted affine-fiber Brascamp--Lieb theorem. The remaining unresolved exact endpoint is therefore a **single rough diagonal bank on the pivot line coupled to one grouped transverse scalar**, not two arbitrary diagonal banks.

This does not yet prove the full density bound for that one-bank configuration.

## 7. Geometric product-set formulation

Combine Theorem 1.1 with Section 5. Given any strict arbitrary-law slab witness, for every `delta>0` first pass to bounded finite-union unit sets with ratio at least `rho-delta`. Fubini on the finite center coordinates then gives a literal slice of the product set with the same remaining unit sets and conditional slab ratio at least `rho-delta`.

Thus a hypothetical sequence `rho_m->infinity` may be represented, after arbitrarily small ratio loss, by bounded finite-union unit-product sets whose hard exact-rank-two coefficient geometry satisfies one of the following:

1. **small transverse cardinality:** at most eleven named original-coordinate centers remove the entire transverse bank;
2. **small pivot leverage:** `c_m<rho_m^-1/6`;
3. **one rough diagonal strip plus constrained transverse strip:** after at most nine centers,
   `B_0` lies within `rho_m^-1/6` of the pivot line, `B_1` lies within `24.540 |d_k|^-1/2 rho_m^-1/6` of a second line, and
   `c_m ||D_{B_1}||_{S_1}<=5419.524 rho_m^-1/3`.

All strip errors, diagonal terms and induced affine terms remain in the actual polynomial.

## 8. First unpaid implication

The first unpaid implication is now

`QFORM-ONE-DIAGONAL-STRIP-ROUGH-PRODUCT-RECEIVER-v1`:

> In the hard exact-rank-two survivor, after the finite-center slice above, prove a uniform product-law density/small-ball receiver when arbitrary diagonal curvature is confined to the near-pivot strip, the transverse strip obeys the trace constraint (5.9), and the complete rank-two strip matrix plus center-induced affine term are retained. Separately pay the low-pivot-leverage branch `c<rho^-1/6`. Otherwise construct a genuine bounded-finite-union product-indicator counterexample in this normal form.

The trace-small transverse diagonal is not to be discarded: under arbitrary separated supports, small coefficients need not give a small random quadratic perturbation. A valid receiver must keep it in the phase or use product-preserving averaging.

## 9. Numerical/algebra checks

The constants were checked independently in the run:

`C_*=1204.3386411070637`,
`3C_*=3613.015923321191`,
`(9/2)C_*=5419.523884981787`,
`sqrt(2C_*)=49.078277090930236`,
`0.5 sqrt(2C_*)=24.539138545465118`.

The exact four-point identity (4.7) was evaluated on 10,000 random coefficient tuples with machine-tolerance equality. The checker and its output are saved beside this report as `CHECK.py` and `CHECK_OUTPUT.txt`. The proof itself is algebraic and does not rely on the numerical test.

## 10. Scope summary

Proved this run:

- optimizer-free finite-mixture reduction from arbitrary cap-one product densities to bounded finite-union unit-product indicators with arbitrarily small witness loss, and equality of the corresponding suprema;
- exact center-induced affine alignment under physical-coordinate conditioning;
- quantitative transverse projective narrowing with the sharper `|d_k|^-1/2` factor;
- aggregate transverse diagonal trace collapse `c||D_{B_1}||_{S_1}=O(rho^-1/3)`;
- exact zero-width consequence that a transverse line of at least three tau-cancelling rows has zero physical diagonal curvature.

Not proved:

- a universal QFORM density constant for all rough cap-one laws;
- a probabilistic perturbation theorem for the trace-small transverse diagonal;
- the low-pivot-leverage branch;
- the remaining one-diagonal-strip rough product receiver;
- unrestricted continuity.

Full QFORM remains OPEN.
