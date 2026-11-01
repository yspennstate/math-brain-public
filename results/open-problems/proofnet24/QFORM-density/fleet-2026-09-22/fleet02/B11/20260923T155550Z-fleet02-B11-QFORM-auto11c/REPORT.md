SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-23T15:55:50Z.
attacking: the finite-heavy-spike null-ruling survivor; replace the absolute tiny-row requirement by a relative atom split and isolate a single dominant near-null source coordinate.

# fleet02/B11 — relative-atom null-ruling crosscut and single-spike reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved in the new cross-volume branch only; continuity remains separate from the unrestricted target.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 1. First unpaid implication and outcome

The preceding fleet02/B11 refinement left

`QFORM-NULL-RULING-FINITE-SPIKE-INTERPOLATION-v2`:

> in the exact-rank-three two-plane indefinite chamber, if the three essential null-ruling directions do not all retain enough absolutely low-leverage source mass, use the finitely many heavy ORIGINAL coordinates jointly with the residual product banks, or force a paid scalar/pair/volume exit.

This run closes a substantial part of that implication. The absolute light-row cutoff is not needed provided no single projected atom carries more than one third of its essential null-line cluster. In that case a deliberately asymmetric original-coordinate cut has volume-sampling row marginal `<17/25`, so the completed Jensen extension D' of Claude's three-volume theorem applies to the **actual** cross block.

Consequently, inside the predecessor near-null-ruling chamber, failure of the new crosscut no longer means an unspecified finite heavy set: it forces **one original coordinate** to carry more than one third of one essential projected null-line mass, hence actual spectral leverage `>tau/36`. Combining the newest designated partner fleet03/B11 r35 further confines every unpaid exact-rank-three state to its collision collar `3/4<C2<5/4`.

The new first unpaid implication is therefore

`QFORM-NULL-RULING-SINGLE-SPIKE-INTERPOLATION-v1`:

> treat one dominant ORIGINAL near-null spike carrying `c_h>tau/36` together with the two residual transverse product banks, or force a paid minority-Schur / pair / disjoint-volume exit. The majority-sign one-sheet half-line is already paid by the ruled theorem; the hard output side is the opposite two-sheet side. Near-zero nonzero pivots may not be replaced by exact zero.

Arbitrary additional nonseparable spectrum remains a separate full-target bridge unless an already-completed full-matrix cross-volume stability hypothesis is available.

## 2. Source-pinned completed inputs actually used

### 2.1 Required Claude package at `e5f71d79...`

Read in full scope before this proof:

- `RESULTS.md`;
- `FOURIER_ROUTE_REPORT.md`;
- `COUNTEREXAMPLE_SEARCH.md`

from `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The result applied below is the proved Jensen extension D' of the three-volume theorem. If `I,J` are disjoint original-coordinate sets, `C=A[I,J]`,

`Z=e_3(C^T C)`,

and the squared-minor volume-sampling row marginals on `I` satisfy

`alpha_i<=h<3/4`,

then

`||p_Q||_infinity
 <=6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z^(-1/6)`.                    (2.1)

This theorem keeps all same-side quadratic terms and affine terms; it is an original-coordinate decoupling theorem and does not assert spectral-coordinate independence.

The same required package proves the sign-specific ruled theorem: for exact rank-three signature `(2,1)` with minimum spectral magnitude `s`,

`p_Q(t)<=pi sqrt(2)/s,  t>=0`,                                      (2.2)

with reflection giving the majority-sign half-line for `(1,2)`. It also records the exact rank-two saddle logarithm.

### 2.2 Predecessor fleet02/B11 null-ruling geometry

The immediate predecessor is

`yspennstate/math-open-problems@ec304ed03ea21d1ff58ee9e901915610446fb80a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T145222Z-fleet02-B11-QFORM-auto11b/REFINEMENT.md`.

It works in the exact-rank-three two-plane setup

`A=R M R^T`, `R^T R=I_3`, `s=min |eig(M)|`,

`R_S^T R_S=diag(1,rho,0)`,
`R_T^T R_T=diag(0,1-rho,1)`,
`m_22=0`,                                                             (2.3)

with

`tau=min(rho,1-rho)`.

The three essential projected null directions are

`S1: s=(a,b,0)`,
`E:  e=(0,1,0)`,
`T1: t=(0,c,d)`,                                                       (2.4)

where the predecessor proves

`a^2>=rho/9`, `d^2>=(1-rho)/9`.                                      (2.5)

Let `r_i^*` be the nearest-null projection of the physical row `r_i`. Put the projected squared cluster masses

`M_s=sum_(i in S1)||r_i^*||^2`,
`M_e=sum_(i in E )||r_i^*||^2`,
`M_t=sum_(i in T1)||r_i^*||^2`.

Under the predecessor error hypothesis

`eta=eta_S+eta_T<=tau^2/3600`,                                        (2.6)

one has

`M_s>=rho/12`, `M_e>=1/12`, `M_t>=(1-rho)/12`.                       (2.7)

Moreover, for every original-coordinate subset `U`, if

`K_U=sum_(i in U) r_i^* (r_i^*)^T`,
`G_U=sum_(i in U) r_i r_i^T`,

then

`||G_U-K_U||op<=eta`.                                                  (2.8)

The nearest-line displacement of each row in its physical plane is at most the corresponding `eps_S` or `eps_T`, and

`eps_S<=eta_S/(2sqrt(2))`, `eps_T<=eta_T/(2sqrt(2))`.                 (2.9)

### 2.3 Latest designated partner fleet03/B11 r35

Latest completed partner read and applied:

`yspennstate/math-open-problems@32a96eb18f2b23de67a15d846a56ccb3d998d889`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T152023Z-fleet03-B11-QFORM-r35/REPORT.md`.

For every exact-rank-three Parseval factorization it defines

`c_i=||r_i||^2`, `C2=sum_i c_i^2`,

and proves two quantitative wings. With `delta=1/4`,

`C2<=3/4  => ||p_Q||infinity <20.549/s`,                              (2.10)

`C2>=5/4  => ||p_Q||infinity <627.070/s`.                             (2.11)

Thus only

`3/4<C2<5/4`                                                          (2.12)

survives these newest partner exits. This is used as an actual case reduction in Section 7.

## 3. New theorem: relative-atom crosscut

### Theorem 3.1 — `QFORM-NULL-RULING-ONE-THIRD-ATOM-CROSSCUT-v1`

Assume the exact-rank-three two-plane hypotheses (2.3)--(2.9). In each of the three essential projected null-line clusters define

`w_i=||r_i^*||^2`.

Suppose that no single projected atom carries more than one third of its cluster:

`w_i<=M_s/3` for every `i in S1`,
`w_i<=M_e/3` for every `i in E`,
`w_i<=M_t/3` for every `i in T1`.                                     (3.1)

Then there exists an original-coordinate partition `I sqcup J` such that

`G_I>=gamma I_3`, `G_J>=gamma I_3`,
`gamma=tau^2/4400`,                                                   (3.2)

and every three-volume row marginal on the constrained side satisfies

`alpha_i<=17/25<3/4`.                                                 (3.3)

Consequently the required completed theorem D' gives a continuous density and

`boxed:
 ||p_(X^T A X)||infinity
 <= [3300000 sqrt(e)/(7 sqrt(34))] /(s tau^2)
 <133299/(s tau^2).`                                                  (3.4)

The statement is symmetric under `A -> -A`, hence applies to both signatures `(2,1)` and `(1,2)`.

### Proof

#### Step 1: greedily split each essential source cluster

For one cluster with total projected squared mass `M`, assume every atom has weight at most `M/3`. Starting from the empty set, add original coordinates until the selected mass first reaches `5M/9`.

Because the last added atom has weight at most `M/3`, the selected mass `mu` satisfies

`5M/9 <= mu <= 8M/9`,                                                 (3.5)

and the unselected complement retains at least

`M-mu>=M/9`.                                                          (3.6)

Also every selected projected atom has relative share

`w_i/mu <= (M/3)/(5M/9)=3/5`.                                        (3.7)

Do this separately on `S1`, `E`, and `T1`; let `I` be the union of the three selected sets and put every other original coordinate in `J`. Denote the selected masses by `mu_s,mu_e,mu_t` and the complementary masses by `nu_s,nu_e,nu_t`.

Using (2.7),

`mu_s>=5rho/108`,
`mu_e>=5/108`,
`mu_t>=5(1-rho)/108`,                                                (3.8)

whereas

`nu_s>=rho/108`,
`nu_e>=1/108`,
`nu_t>=(1-rho)/108`.                                                  (3.9)

#### Step 2: projected Gram lower bound on the constrained side

The projected Gram on `I` is exactly

`K_I=mu_s ss^T+mu_e ee^T+mu_t tt^T`.                                 (3.10)

For arbitrary `x=(x_1,x_2,x_3)`, let

`y_1=sqrt(mu_s)(a x_1+b x_2)`,
`y_2=sqrt(mu_e)x_2`,
`y_3=sqrt(mu_t)(c x_2+d x_3)`.

Then `x^T K_I x=|y|^2` and

`x_2=y_2/sqrt(mu_e)`,
`x_1=[y_1/sqrt(mu_s)-b x_2]/a`,
`x_3=[y_3/sqrt(mu_t)-c x_2]/d`.

Hence

`|x|^2<=A1 y_1^2+A2 y_2^2+A3 y_3^2`,                               (3.11)

where

`A1<=2/(mu_s a^2)`,
`A3<=2/(mu_t d^2)`,
`A2<=(1+2/a^2+2/d^2)/mu_e`.                                         (3.12)

By (2.5), (3.8), and `rho(1-rho)>=tau/2`,

`A1,A3<=1944/(5 tau^2)`,                                             (3.13)

and

`A2<=(108/5)[1+18/rho+18/(1-rho)]`
`   <=(108/5)(1+36/tau)`
`   <=1971/(5 tau^2)`,                                                (3.14)

because `0<tau<=1/2` implies `tau^2+36tau<=73/4`.

Therefore

`K_I >= [5 tau^2/1971] I_3 > [tau^2/395] I_3`.                       (3.15)

#### Step 3: projected Gram lower bound on the free side

Exactly the same calculation with (3.9) gives

`K_J=nu_s ss^T+nu_e ee^T+nu_t tt^T`

and

`K_J >= [tau^2/1971] I_3`.                                          (3.16)

Applying the actual/projected error bound (2.8) and (2.6),

`G_I >= (1/395-1/3600) tau^2 I_3`,
`G_J >= (1/1971-1/3600) tau^2 I_3`.                                 (3.17)

The second coefficient is the smaller one, and

`[1/1971-1/3600]^(-1)=4355.8011...<4400`,                            (3.18)

so (3.2) follows.

#### Step 4: the selected-side volume marginal is below `17/25`

For a projected row on one of the three basis directions, (3.10) gives an exact leverage identity:

`(r_i^*)^T K_I^(-1) r_i^* = w_i/mu_k`,                               (3.19)

where `k` is its line cluster. By (3.7), this is at most `3/5`.

Let `e_i=r_i-r_i^*`. From (2.9) and (2.6),

`||e_i|| <= tau^2/(7200 sqrt(2))`.                                   (3.20)

Put `kappa=tau^2/395`. By (3.15) and (2.8),

`||K_I^(-1/2)(G_I-K_I)K_I^(-1/2)||op <=395/3600`.                    (3.21)

Hence

`G_I^(-1) <= [1-395/3600]^(-1) K_I^(-1)`.                            (3.22)

Moreover, since `tau<=1/2`,

`||K_I^(-1/2)e_i||
 <= ||e_i||/sqrt(kappa)
 <= sqrt(395)/(14400 sqrt(2))
 <0.001`.                                                            (3.23)

Therefore

`alpha_i=r_i^T G_I^(-1)r_i`
` <= [1-395/3600]^(-1) [sqrt(3/5)+0.001]^2`
` <0.6757<17/25`.                                                     (3.24)

This is precisely the marginal gate needed by theorem D'. Notice that no absolute bound such as `||r_i||^2<=tau^2/7200` is imposed.

#### Step 5: actual cross volume and application of Claude D'

Let

`C=A[I,J]=R_I M R_J^T`.                                               (3.25)

Since both actual Grams are positive definite, `C` has exact rank three. Its three-volume is

`Z=e_3(C^T C)
  =det(M)^2 det(G_I) det(G_J)`.                                      (3.26)

Also, for exact rank three, the squared-minor volume-sampling row marginal is exactly

`alpha_i=r_i^T G_I^(-1)r_i`,                                        (3.27)

so (3.24) applies to the actual physical cross block.

Because `|det M|>=s^3` and both Grams are at least `gamma I_3`,

`Z>=s^6 gamma^6`.                                                     (3.28)

Use theorem D' with

`h=17/25`.

Then

`(2h)^(-1/2)=5/sqrt(34)`,
`(3-4h)^(-1)=25/7`,                                                  (3.29)

and therefore

`||p_Q||infinity
 <= [750 sqrt(e)/(7 sqrt(34))] Z^(-1/6)`
` <= [750 sqrt(e)/(7 sqrt(34))] [4400/(s tau^2)]`
` = [3300000 sqrt(e)/(7 sqrt(34))]/(s tau^2)`
` <133299/(s tau^2)`.                                                (3.30)

This proves (3.4). Since theorem D' gives Fourier decay exponent strictly larger than one, this branch has a continuous density. QED.

## 4. Sharp structural consequence: finite spikes collapse to one dominant atom

The contrapositive of Theorem 3.1 is immediate and useful.

### Corollary 4.1 — `QFORM-NULL-RULING-SINGLE-DOMINANT-ATOM-v1`

Under (2.3)--(2.9), if the new cross-volume branch does not apply, then some essential null-line cluster contains one original coordinate `h` with

`||r_h^*||^2 > M_k/3`.                                                (4.1)

By (2.7), regardless of which of the three essential directions fails,

`boxed: ||r_h||^2 >=||r_h^*||^2 > tau/36.`                           (4.2)

Thus the predecessor residual is not merely a finite set of heavy coordinates of cardinality `O(tau^-2)`: it contains a single quantitatively dominant source atom.

This is the main structural gain of the run.

## 5. Sign-specific Schur and ruled splice after the new reduction

The dominant atom `h` in Corollary 4.1 is an ORIGINAL coordinate, so the already-completed sign-sensitive scalar pivots remain legal.

For signature `(2,1)`, if its physical diagonal `a_h=A_hh` has the minority sign and `|a_h|>=xi`, the earlier fleet02/B11 theorem `QFORM-MINORITY-SCHUR-DEFINITE-v1` gives

`||p_Q||infinity <=2 sqrt(2 pi) xi^(-1/2)`.                           (5.1)

The proof there uses inertia: a minority negative scalar pivot leaves a rank-two PSD Schur complement, whose two-dimensional density is paid before the independent scalar square is reintroduced. It does not erase the rank-two opposite-sign singularity in the majority-pivot case.

For the majority-sign half-line, the required pinned ruled theorem gives (2.2) with no pivot hypothesis. Therefore, after Theorem 3.1 and the fixed-scale minority-Schur exit, the genuinely hard sign-specific state is:

- one dominant original coordinate with `c_h>tau/36`;
- its fixed-scale minority pivot absent (or its pivot is genuinely near zero);
- output on the opposite two-sheet side.

Reflection gives the `(1,2)` statement.

This is exactly the single-spike interpolation problem named in Section 1.

## 6. Rank-two logarithm retained; exact third-direction gain

The rank-two opposite-sign failure remains genuine. For independent centered unit uniforms,

`T=2XY`

has

`p_T(u)=log(1/(2|u|)),  0<|u|<1/2`.                                  (6.1)

Thus the rank-two saddle itself is not bounded.

The new theorem identifies the third-direction repair quantitatively without rotating the random variables. The cut (3.25) has three genuine singular directions carried by disjoint sets of ORIGINAL coordinates. Because the constrained volume marginals are only bounded by `h=17/25`, the Jensen version of the decoupling argument uses

`q=2h=34/25`.

Its large-`|t|` characteristic-function exponent is

`3/(2q)=75/68>1`.                                                     (6.2)

So the third physical cross direction changes the non-integrable rank-two endpoint `|t|^-1` into the integrable decay

`|phi_Q(t)|=O(|t|^(-75/68))`.                                        (6.3)

This is the precise analytic sense in which the third direction removes the logarithmic singularity in the relative-atom branch. No spectral projection is declared independent.

## 7. Latest partner r35 applied: collision collar plus dominant atom

Apply fleet03/B11 r35 with `delta=1/4` to the same exact-rank-three matrix. Equations (2.10)--(2.11) pay the two exterior collision wings. Therefore any state still unpaid after the present theorem must satisfy simultaneously

`3/4<C2=sum_i||r_i||^4<5/4`,                                         (7.1)

and

`there exists h with ||r_h||^2>tau/36`                               (7.2)

whose projected row carries more than one third of one essential null-line cluster.

This is a real use of the designated partner result: the new single-spike branch is intersected with the partner's collision collar before any further local analysis.

The partner's exact-coloop regular-polygon stress family explains why a dominant-atom alternative is structurally necessary. There one leverage-one original row lies outside a diffuse transverse plane, `D=0`, and all pair-area scales vanish as the planar bank grows. Any volume-sampling cut that puts that coloop on the constrained side gives row marginal one; putting it on the free side leaves the constrained spectral span rank two. Thus a theorem with a strict `<3/4` marginal gate cannot simply delete the dominant-atom branch. That family is not a QFORM counterexample; it points to the separate coloop/near-coloop receiver.

## 8. Scope and remaining debt

The theorem is exact-rank-three and belongs only to the predecessor two-plane near-null-ruling chamber. It does not prove the unrestricted QFORM conjecture and does not remove arbitrary additional nonseparable spectrum.

What is newly closed is the whole portion of the finite-heavy-spike branch in which every essential projected null-line cluster is atom-diffuse at relative scale `1/3`. No absolute row-leverage threshold is required there.

What remains is sharply smaller:

`QFORM-NULL-RULING-SINGLE-SPIKE-INTERPOLATION-v1`.

One must exploit the single dominant original coordinate from (4.2), together with the two transverse original-product banks and the collision-collar information (7.1), to force one of:

1. the minority-sign Schur exit;
2. a product-preserving hub/pair or near-coloop receiver on the two-sheet side;
3. an actual disjoint-volume/cross-block exit.

A small nonzero scalar pivot cannot be replaced by zero, and no matrix-small perturbation is treated as a small random quadratic error on arbitrary unbounded inputs.

No hidden moments, support bounds, log-concavity, identical-law assumption, diagonal-basis assumption, post-rotation independence, arbitrary-joint coarea, FEI/installation/benchmark work, task mutation, notification/email, cross-account authentication, paid call, permission change, public release, unrelated data, or benchmark gold is used.