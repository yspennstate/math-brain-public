SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T20:15:58Z.
attacking: the critical two-selector endpoint with a random-center physical square; keep the whole independent-copy difference and recover an L1 time bound by dyadic square-energy averaging.

# QFORM B03 r32 — random-center square closes the critical two-selector time endpoint

Status: **new supporting theorem proved; full unrestricted QFORM remains OPEN.**

Execution state: `WITHOUT_VERIFIED_BRAIN`. This report uses repository retrieval, not native learned-memory ingestion.

## 1. Scope and source discipline

Target: independent real coordinates with one-dimensional densities bounded by 1; arbitrary real symmetric quadratic form with at least three eigenvalues of absolute value at least 1. No moments, log-concavity, compact support, connected support, Gaussianity, or post-rotation independence are assumed.

The current live corrections are respected. In particular, no conditional density cap is asserted for a difference variable after conditioning on its conjugate sum; no law-uniform pointwise van-der-Corput estimate is used; no arbitrary-joint coarea lemma is used.

The designated partner input is account02/B03's completed theorem `QFORM-JOINT-PROJECTION-COEFFICIENT-PLANCHEREL-v1` (canonical report `math-open-problems@1cf28b1faa4ca92850b551bd1cc23457164639d6`). The theorem below refines its actual Cauchy--Schwarz/Plancherel inequality by retaining, rather than discarding, an extra genuine physical square factor.

## 2. The theorem

### Theorem (critical two-selector packet plus a random-center physical square)

Let

- `Z=(Z_1,Z_2)` be an R^2-valued random vector with density `p_Z` satisfying `||p_Z||_infty <= M_Z`;
- `X` be a real random variable, independent of `(Z,W)`, with density `f_X <= 1`;
- `Z` be independent of the background `W`;
- `C(W) in R^2` have a joint density `p_C` satisfying `||p_C||_infty <= M_C`;
- `B` be an invertible real 2x2 matrix;
- `d != 0`;
- `h(W), R(W)` be arbitrary measurable real functions and `P(Z)` an arbitrary measurable real function.

Set

`Q = P(Z) + R(W) + d (X-h(W))^2 + 2 Z^T B C(W)`.

Define

`K := pi sqrt(M_Z M_C / |det B|)`, `D:=|d|`, and `T_0:=max{K,D^{-1}}`.

Then `Q` has a continuous density vanishing at infinity and

`||p_Q||_infty < 10 T_0`

and therefore, for every interval `I`,

`P(Q in I) < 10 max{ pi sqrt(M_Z M_C/|det B|), |d|^{-1} } |I|`.

The theorem is shift-uniform in the random center `h(W)`: no size, moment, or regularity assumption on `h(W)` occurs.

In addition, the whole independent-copy collision integral obeys

`integral_R |t|^{-1/2} |phi_Q(t)|^2 dt <= (16/3) K^{1/2}`.

The latter identity is a dependence-safe estimate for `phi_{Q-Q'}(t)=|phi_Q(t)|^2`; no coordinatewise sum/difference decomposition is used.

## 3. Refined partner inequality

For a fixed shift `a`, write

`G_a(t) := E_X exp(i t d (X-a)^2)`.

For `t != 0`, define the complex measure on coefficient space R^2 by its density

`mu_t(c) := p_C(c) E[ exp(i t R(W)) G_{h(W)}(t) | C(W)=c ]`.

Then

`phi_Q(t) = integral p_Z(z) exp(i t P(z)) hat(mu_t)(2 t B^T z) dz`.

Weighted Cauchy--Schwarz first gives

`|phi_Q(t)|^2 <= M_Z integral_R2 |hat(mu_t)(2t B^T z)|^2 dz`.

Under the Fourier convention `hat g(xi)=integral exp(i xi.c) g(c) dc`, the change of variables `xi=2t B^Tz` and Plancherel yield

`integral |hat(mu_t)(2tB^Tz)|^2 dz
 = pi^2 |det B|^{-1} |t|^{-2} ||mu_t||_2^2`.

Conditional Jensen and `p_C<=M_C` give

`||mu_t||_2^2
 <= integral p_C(c)^2 E[|G_{h(W)}(t)|^2 | C=c] dc
 <= M_C E |G_{h(W)}(t)|^2`.

Hence the actual strengthened partner inequality is

`|phi_Q(t)|^2 <= min{1, K^2 |t|^{-2} E |G_{h(W)}(t)|^2}.`   (3.1)

If the square factor is simply bounded by 1, (3.1) reduces exactly to the partner's k=2 critical Plancherel envelope. The point of this run is that the square factor has enough **dyadic L2 time energy** to make the one-copy characteristic function integrable even though it has no uniform pointwise decay.

## 4. Uniform dyadic square-energy lemma

### Lemma

Let `X` have any density `f<=1`, let `a in R`, and

`G_a(t)=E exp(i t d (X-a)^2)`, `D=|d|`.

For every `T>0` with `DT>=1`,

`integral_T^{2T} |G_a(t)|^2 dt <= D^{-1} L(DT)`,   (4.1)

where

`L(u):=8+8 pi log(1+sqrt(u)/2)` for `u>=1`.

The bound is uniform in both `a` and the admissible density `f`.

### Proof

Let `Y=(X-a)^2`. Its probability density on `(0,infty)` is

`p_a(y)=[f(a+sqrt(y))+f(a-sqrt(y))]/(2 sqrt(y))`,

so

`0<=p_a(y)<=y^{-1/2}`, `integral p_a=1`.   (4.2)

Fix `tau>=1` and put `delta=tau^{-1}`. Split `p_a=p_0+p_1`, where `p_0` is supported on `(0,delta)` and `p_1` on `[delta,infty)`.

By (4.2),

`m_0:=||p_0||_1 <= integral_0^delta y^{-1/2}dy = 2/sqrt(tau)`.

Therefore

`integral_tau^{2tau} |hat p_0(s)|^2 ds <= tau m_0^2 <=4`.   (4.3)

For the tail, `p_1^2 <= y^{-1/2}p_1`. Among all `0<=p<=y^{-1/2}` supported on `[delta,infty)` with mass at most one, the decreasing-weight functional `integral y^{-1/2}p(y)dy` is maximized by filling the cap nearest `delta`. The endpoint `R` is fixed by

`2(sqrt(R)-sqrt(delta))=1`,

and hence

`||p_1||_2^2 <= integral_delta^R y^{-1}dy
 =2 log(1+sqrt(tau)/2)`.   (4.4)

Plancherel gives

`integral_R |hat p_1(s)|^2 ds <=4 pi log(1+sqrt(tau)/2)`.   (4.5)

Using `|u+v|^2<=2|u|^2+2|v|^2`, (4.3)--(4.5) imply

`integral_tau^{2tau} |hat p_a(s)|^2 ds
 <=8+8pi log(1+sqrt(tau)/2)=L(tau)`.   (4.6)

Finally `G_a(t)=hat p_a(dt)` up to the harmless sign convention, and `|hat p_a(-s)|=|hat p_a(s)|`. Changing variables proves (4.1). QED.

Averaging (4.1) over the random center `a=h(W)` preserves exactly the same bound:

`integral_T^{2T} E|G_{h(W)}(t)|^2 dt <= D^{-1} L(DT)`.   (4.7)

This is the essential missing implication: the arbitrary random shear/center costs nothing because only the translation-uniform cap (4.2) is used.

## 5. L1 time closure and linear small-ball scaling

On a dyadic block `[T,2T]` with `DT>=1`, (3.1), Cauchy--Schwarz in time, and (4.7) give

`integral_T^{2T} |phi_Q(t)|dt
 <= K T^{-1/2} [D^{-1}L(DT)]^{1/2}
 = K sqrt( L(DT)/(DT) ).`   (5.1)

The function `u -> L(u)/u` decreases on `[1,infty)`. Indeed

`u L'(u)=4pi sqrt(u)/(2+sqrt(u)) <4pi`,

whereas

`L(u)>=L(1)=8+8pi log(3/2)>4pi`.

Let `T_j=2^j T_0`. Since `DT_0>=1` and `K<=T_0`, (5.1) yields

`integral_{T_j}^{2T_j}|phi_Q(t)|dt
 <= T_0 sqrt(L(2^j)/2^j)`.   (5.2)

For `r=2^{-1/2}`,

`log(1+2^{j/2}/2) <= log(3/2)+(j/2)log2`,

so with

`A_0=8+8pi log(3/2)`, `B_0=4pi log2`,

we have `L(2^j)<=A_0+B_0 j`. Hence

`sum_{j>=0} sqrt(L(2^j)/2^j)
 <= sqrt(A_0)/(1-r)
    +sqrt(B_0) sqrt( r/(1-r)^3 )
 =30.218265050697436...`.   (5.3)

The low-frequency interval `[0,T_0]` contributes at most `T_0`. Therefore

`integral_0^infty |phi_Q(t)|dt
 <31.218265050697436 T_0`,

and by symmetry

`integral_R |phi_Q(t)|dt
 <62.43653010139487 T_0`.   (5.4)

Fourier inversion now gives a continuous `C_0` density and

`||p_Q||_infty
 <=(2pi)^{-1} integral_R |phi_Q(t)|dt
 <9.93708239514291 T_0
 <10T_0`.   (5.5)

This proves the theorem and the stated linear small-ball estimate.

## 6. Whole-copy independent-copy integral

Equation (3.1) implies the weaker but assignment-specific dependence-safe bound

`|phi_Q(t)|^2 <= min{1,K^2 |t|^{-2}}`.

Since `|phi_Q(t)|^2=phi_{Q-Q'}(t)` for an independent copy of the **whole scalar Q**, one obtains directly

`integral_R |t|^{-1/2}|phi_Q(t)|^2dt
 <=2[ integral_0^K t^{-1/2}dt
       +K^2 integral_K^infty t^{-5/2}dt ]
 =(16/3)K^{1/2}`.   (6.1)

No pair `(X_i-X_i',X_i+X_i')` is separated or conditionally re-capped anywhere in (6.1). This retains exactly the dependence required by the live correction inbox.

The key distinction is now explicit: the collision integral (6.1) alone is not an L-infinity criterion, but the same coupled Plancherel representation, with the genuine physical square retained and averaged dyadically, upgrades the critical endpoint to the L1 estimate (5.4), which *does* recover linear small-ball scaling.

## 7. Target-valid control family with arbitrarily large shear

For independent cap-one variables `X,Y_1,Y_2,Z_1,Z_2` and arbitrary real `c`, consider

`Q_c=(X-cY_1)^2+2Z_1Y_1+2Z_2Y_2`.   (7.1)

Apply the theorem with

`Z=(Z_1,Z_2)`, `W=(Y_1,Y_2)`, `C(W)=W`, `B=I_2`, `d=1`, `h(W)=cY_1`.

Because the two-dimensional product densities of `Z` and `W` are bounded by one, `M_Z=M_C=1`. Therefore

`||p_{Q_c}||_infty <10pi`   (7.2)

and the density is continuous `C_0`, **uniformly in the shear c**.

This is a genuine instance of the full target. In the coordinate order `(X,Y_1,Z_1,Y_2,Z_2)`, the matrix is the direct sum of

`[[1,-c,0],[-c,c^2,1],[0,1,0]]`

and

`[[0,1],[1,0]]`.

The second block has eigenvalues `+1,-1`. The first block has largest eigenvalue at least the Rayleigh quotient at `e_X`, which equals 1. Hence the full matrix has at least three eigenvalues of absolute value at least one for every `c`.

This control is useful because a proposed arbitrary-shear *pointwise/tube* estimate is false in the live corrections; (7.2) instead survives by a dyadic integrated-time argument.

## 8. What remains open

This theorem does **not** solve unrestricted QFORM. The unresolved structural step is to route every matrix satisfying `s_3(A)>=1` into a product-preserving packet that supplies, at universal scale, either

1. a genuine physical square plus a critical two-selector joint coefficient packet as above,
2. an already-paid three-volume crossing packet,
3. an already-paid diagonal/pivot/grouped-hub/ridge/semidefinite branch,

without assuming a uniformly good single minor and without making small matrix coefficients into probabilistically small perturbations.

The new result specifically removes one analytic obstruction: once the critical two-selector Plancherel packet and a genuine physical square coexist, **an arbitrary background-dependent square center no longer causes a loss**. The remaining issue is matrix/product-structure extraction.

Full universal essential boundedness: OPEN.
Full universal continuity: OPEN.
This theorem's branch: continuous `C_0` density with explicit linear small-ball constant.

## 9. Partner application and provenance

Partner account02/B03 result applied at the exact inequality in Section 3: its whole-background Cauchy--Schwarz / whole-selector Plancherel calculation gives the `K^2 |t|^{-2}` critical factor; this run retains the physical-square multiplier through the same calculation and proves the new dyadic energy lemma. The designated partner's latest handoff is `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B03/b03-20260923T191657Z-4d3b23.md`; its canonical theorem report is `math-open-problems@1cf28b1faa4ca92850b551bd1cc23457164639d6`.

No Monte Carlo or histogram is used. All estimates above are analytic and uniform over the stated rough input laws.
