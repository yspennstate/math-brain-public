# fleet02/B20 — higher-window annular compiler and physical-star bridge

Run: `20260923T131224Z-fleet02-B20-QFORM-auto11`

Status: **ESSENTIAL_STEP_APPLIED / N3-R14-HIGHER-ANNULUS / PHYSICAL-STAR-VARIANCE-BRIDGE / SINGLE-PAIR-ROUTE-REFUTED / FULL-QFORM-OPEN**.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source discipline

Target: for arbitrary finite `n`, independent real original-coordinate variables `X_i` with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite bound for the density of `Q=X^T A X`, or give a valid counterexample. Continuity is tracked separately.

No Gaussianity, log-concavity, moment, compact/connected-support, iid, diagonal-basis, or post-rotation-independence hypothesis is introduced. The known false law-uniform pointwise quadratic-phase decay, worst-fiber supremum, arbitrary-joint coarea shortcut, and deletion of small dense spectral tails are not used.

Fresh owner control: revision `2026-09-22.15`, QFORM-only. Fresh native fleet02 inventory contains exactly the same twenty B01--B20 QFORM tasks, all enabled, hourly-valid and quiet; no native mutation was needed.

## 2. Sources actually consumed

1. **Designated partner fleet03/B20 r31**, canonical `yspennstate/math-open-problems@c6e058c3d4aa36e89ad433c1f4d41b6f82739bf`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T121606Z-fleet03-B20-QFORM-r31/REPORT.md`. Its exact-rank-three compiler gives: either

   `||p_Q||_infinity <= 192 e < 522`,

   or there is a set `S` of at most eighteen original physical coordinates and a spectral unit vector `v` with

   `sum_(i in S) <r_i,v>^2 > 63/64`.

   At a diffuse deletion stop its exact expression is

   `||p_(Q | X_S)||_infinity <= 3e (|det M| det G_S)^(-1/3) <=192e`,

   with all conditioning on literal original coordinates. I retain this as the exact-rank-three side of the end-to-end proof graph; the new theorem below attacks the arbitrary-extra-spectrum N3 frontier which r31 explicitly leaves open.

2. **Fresh compatible fleet01/B20 compiler**, canonical `yspennstate/math-open-problems@5593a06e6c0d8a346375176fc18181171fdc7ed9`. It proves in `N3(1/64)` that the high-spectrum leverage threshold `P_0=1_{|A|>=1}` at `1/60` either pays by the fifth-volume receiver or leaves a fixed physical star/four-direction packet. It also proves a spectral-window payment at cutoff `1/16`, leverage `1/50`.

3. **Completed ridge receiver**, canonical `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`. For an original-coordinate cross block `B`, ridge scale `gamma`,

   `K=B B^T (gamma^2 I+B B^T)^(-1)`, `theta=tr K`.

   If `max_i K_ii<=1/2` and `theta>2`, then the full ambient form has a continuous `C_0` density and

   `||p_Q||_infinity <= sqrt(e)/(sqrt(2) gamma) * theta/(theta-2)`.

4. **Pinned interactive source** `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. Its Theorem F pays an exact physical rank-three frame whose row leverages are at most `1/2` by `||p_Q||_infinity<=12` when `|lambda_1 lambda_2 lambda_3|>=1` and the complementary block is diagonal on the selected physical bank. I apply it below to the explicit stress family, proving that family is a route counterexample but not a QFORM counterexample.

## 3. N3 setup

Let `tau=1/64` and suppose the global no-pivot reduction has reached `N3(tau)`:

- `s_3(A)>=1`;
- `|A_ii|<1/64` for every original coordinate;
- `|A_ii A_jj-A_ij^2|<1/64` for every physical pair.

Put

`P_0=1_{|A|>=1}`.

The fresh fleet01/B20 theorem pays or structurally compiles every state with some `(P_0)_hh>=1/60`. Hence the complementary arbitrary-rank branch may be assumed to satisfy

`max_h (P_0)_hh <1/60`.                                             (3.1)

The previous compiler then used the annulus `[1/16,1)`. We now push this to `[1/14,1)`.

## 4. New theorem — a `[1/14,infinity)` spectral window is paid at leverage `1/56`

### Theorem 4.1 — `QFORM-SPECTRAL-WINDOW-1OVER14-1OVER56-v1`

Let `A` be any real symmetric matrix with at least three eigenvalues of modulus at least one, and let

`P_14 := 1_{|A|>=1/14}`.

If

`max_i (P_14)_ii <=1/56`,                                           (4.1)

then for arbitrary independent cap-one original-coordinate densities the law of `Q=X^TAX` has a continuous `C_0` density and

`||p_Q||_infinity <1127`.                                           (4.2)

### Proof

Write `A=A_H+E`, where `A_H=U Lambda U^T` is the spectral truncation to `|lambda|>=eta`, with

`eta=1/14`, `epsilon=1/56`, `||E||_op<eta`,

and every physical row `u_i` of `U` obeys `||u_i||^2<=epsilon`.

Apply the same completed two-part MSS frame partition used in fleet01/B20. There are original-coordinate banks `I,J` for which both high-frame partial Gram matrices are bounded below by

`delta I`,

where

`delta = 1/2-sqrt(2 epsilon)-epsilon`
`      = 1/2-1/sqrt(28)-1/56`
`      = 0.293160620638243529...`.                                 (4.3)

For the high spectral cross block

`B_0=A_H[I,J]=U_I Lambda U_J^T`,

both `U_I,U_J` have least singular value at least `sqrt(delta)`. Since `Lambda` contains at least three singular values at least one,

`s_3(B_0)>=delta`.                                                   (4.4)

Because every eigenvalue retained in `A_H` is nonzero, the same argument as in the completed fleet01 proof gives

`max_i (P_range(B_0))_ii <= epsilon/delta`.                         (4.5)

Restore the full tail `F=E[I,J]`, retaining it in the random quadratic form. Weyl gives for the actual physical cross block `B=A[I,J]`

`s_3(B)>=sigma:=delta-eta`
` =0.221732049209672100...`.                                        (4.6)

Choose

`gamma=(7/10)sigma=0.155212434446770470...`.                       (4.7)

The completed ridge-stability inequality then gives

`sqrt(max_i K_gamma,ii)`
` <= sqrt(epsilon/delta)+eta/gamma`
` =0.707003324787831947...`
` <1/sqrt(2)`.                                                       (4.8)

Thus `max_i K_gamma,ii<1/2`.

The three singular values in (4.6) give

`theta=tr K_gamma`
` >=3/(1+(7/10)^2)`
` =300/149>2`.                                                       (4.9)

Apply the completed ridge theorem with `q=1`. Since `theta/(theta-2)` decreases on `(2,infinity)` and `(300/149)/(300/149-2)=150`,

`||p_Q||_infinity`
` <= 150 sqrt(e)/(sqrt(2) gamma)`
` = 1500 sqrt(e)/(7 sqrt(2) sigma)`
` =1126.6706771470456... <1127`.                                   (4.10)

The ridge receiver supplies continuity and vanishing at infinity. All random variables remain original coordinates; the spectral decomposition is used only to construct deterministic matrices. QED.

The numerical inequalities in (4.3)--(4.10) are independently reproduced by the run's committed `checks.py`; they are not Monte Carlo evidence.

## 5. New deterministic bridge — higher annular leverage forces literal physical star energy

Assume (3.1) and that the paid condition (4.1) fails. Then there is an original physical coordinate `h` with

`(P_14)_hh>1/56`, `(P_0)_hh<1/60`.

Let

`R_14:=1_{1/14<=|A|<1}=P_14-P_0`.

At that same coordinate,

`(R_14)_hh > 1/56-1/60 =1/840`.                                   (5.1)

The previous compiler only recorded a spectral-energy lower bound. The key source-preserving bridge is the following exact variance identity.

### Theorem 5.1 — `QFORM-ANNULUS-TO-PHYSICAL-STAR-VARIANCE-v1`

For every real symmetric `A` and every original coordinate `h`, if `a=A_hh`, then

`sum_(j!=h) A_hj^2`
` = (A^2)_hh-a^2`
` = sum_alpha w_alpha (lambda_alpha-a)^2`,                          (5.2)

where `{lambda_alpha}` are the eigenvalues of `A` with an orthonormal eigenbasis and `w_alpha=|u_alpha(h)|^2`, so `sum_alpha w_alpha=1`.

Consequently, in `N3(1/64)`, the annular state (5.1) satisfies the **literal source-coordinate** lower bound

`sum_(j!=h) A_hj^2`
` > (1/840)(1/14-1/64)^2`
` = (1/840)(25/448)^2`
` = 125/33718272`
` = 0.000003707188790694849...`.                                   (5.3)

### Proof

The first equality is the definition of the squared Euclidean norm of physical row `h` with its diagonal removed. For the second, spectral decomposition gives

`a=sum_alpha w_alpha lambda_alpha`,

`(A^2)_hh=sum_alpha w_alpha lambda_alpha^2`,

and the weights sum to one, so their variance is exactly `(A^2)_hh-a^2`.

For every spectral value in `R_14`, `|lambda_alpha|>=1/14`, while the N3 diagonal bound gives `|a|<1/64`; hence

`|lambda_alpha-a|>=1/14-1/64=25/448`.

Restrict the nonnegative sum (5.2) to the `R_14` spectral mass and use (5.1). QED.

This is the desired bridge from a spectral annulus to a physical product-source object. It does **not** claim that `R_14 X` is independent, and it does not select a worst fiber.

## 6. Source-valid route counterexample — no uniformly good pair follows from the annular packet

A natural next shortcut would be to infer from (5.1) or (5.3) one robust original physical pair. That implication is false even inside the exact target and inside `N3(1/64)`.

For each integer `N>=5`, construct a block diagonal matrix

`A_N = P_256 direct_sum (1/14) u_N u_N^T`.

### Large rank-three block

Index 256 coordinates by `x in {0,1}^8` and define a `256 x 3` matrix `R` by

`r_x=(1,(-1)^{x_1},(-1)^{x_2})/16`.

Then `R^T R=I_3`; set `P_256=RR^T`. Thus its three nonzero eigenvalues are exactly `1,1,1`. Every diagonal is `3/256<1/64`. For distinct rows the off-diagonal entry is one of `3/256, 1/256, -1/256`, so every physical `2 x 2` principal determinant is either `0` or

`(3/256)^2-(1/256)^2=1/8192<1/64`.                                (6.1)

### Annular rank-one block

Take `N+1` coordinates with a distinguished hub `h` and let

`u_h^2=1/50`,

`u_j^2=49/(50N)` for each of the `N` leaves.

Then `u_N` is unit. The annular block has its only nonzero eigenvalue exactly `1/14`; all of its `2 x 2` principal determinants are zero. Its hub diagonal is `1/700<1/64`, and for `N>=5` each leaf diagonal is `7/(100N)<1/64`. Cross-block principal determinants are just products of these small diagonals with `3/256`, hence are also `<1/64`.

Therefore `A_N in N3(1/64)` and has at least three eigenvalues of modulus one.

At the annular hub,

`(P_0)_hh=0`,

`(P_14)_hh=1/50>1/56`.                                             (6.2)

Yet each physical hub-leaf coefficient is exactly

`A_hj=(1/14) u_h u_j = 1/(100 sqrt(N))`,                           (6.3)

so every such coefficient tends to zero as `N->infinity`, and every hub-leaf `2 x 2` principal determinant is identically zero because the annular block has rank one. Thus no dimension-free single-edge or robust-pair extraction can follow from the annular leverage packet.

This is a **route counterexample**, not a QFORM counterexample. Indeed the pinned interactive Theorem F applies to the 256-coordinate physical rank-three block: its physical frame leverages are all `3/256<1/2`, its three coefficients are `1,1,1`, and the complementary annular block vanishes on that selected bank. Hence the full form satisfies

`||p_Q||_infinity <=12`.                                            (6.4)

The stress family therefore says exactly what the next proof mechanism must do: spend aggregate star/grouped-square/ridge information before attempting reciprocal local-minor selection.

## 7. Strongest conditional proof graph after this run

The current source-pinned graph is now:

1. Global no-pivot reduction: it suffices to pay `N3(1/64)` plus already-paid pivot branches.
2. If some high-spectrum physical leverage `(P_0)_hh>=1/60`, the fresh fleet01 compiler either pays by D5 below `201.787` or leaves its explicit physical star/four-direction packet.
3. If all `(P_0)_hh<1/60` and `max_i(P_14)_ii<=1/56`, Theorem 4.1 pays the full form continuously below `1127`.
4. Otherwise a literal original-coordinate hub `h` satisfies the physical star-energy lower bound (5.3), while the target-valid family in Section 6 proves that this aggregate mass need not contain any robust single pair.
5. In the exact-rank-three subproblem, the newest designated partner r31 additionally pays every diffuse heavy-deletion stop below `522`, or compresses the survivor to at most eighteen original coordinates carrying `>63/64` of one spectral direction.

Thus the arbitrary-extra-spectrum frontier has been pushed from the prior `[1/16,1)` annulus to the strictly higher `[1/14,1)` annulus and, more importantly, converted from a spectral statement into a physical star-energy statement.

## 8. First unpaid universal implication

The first unpaid arbitrary-rank implication is now

**`QFORM-N3-R14-PHYSICAL-STAR-OR-STAR4DIR-PAYMENT-v1`.**

Under the full original product-source hypotheses and `A in N3(1/64)`, after the paid ridge/D5 branches fail, prove one universal linear small-ball/density estimate for either:

- the existing fleet01 physical star/four-direction packet; or
- an original physical hub `h` with

  `sum_(j!=h) A_hj^2 >125/33718272`,

  arising from the `[1/14,1)` annular packet,

while retaining arbitrary same-side and ambient couplings.

The stress family proves that a valid solution cannot simply demand one fixed-size hub edge or one robust physical pair. The next mechanism should be aggregate grouped-square/multi-hub/volume/ridge smoothing in original coordinate banks. A second Cauchy--Schwarz that only reproduces a square-root collar is not enough for the density target.

The full QFORM theorem remains open, as does full-target continuity. No full candidate exists yet and therefore the required two independent end-to-end reviews have not been triggered.

## 9. Telemetry and provenance

Model self-report: GPT-5.6 Sol. Requested effort: maximum actually supported by the current runtime. Configured effort: `UNKNOWN`. Known actual effort: `UNKNOWN`. Provider reasoning-token count: `null`/unexposed. Pure-thinking-time counter: `null`/unexposed. Wall-clock elapsed execution is not pure thinking.

Authenticated repository retrieval/writeback occurred. No actual learned-memory receiver ingestion was exposed, so execution remains `WITHOUT_VERIFIED_BRAIN`.
