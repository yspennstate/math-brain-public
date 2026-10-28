SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-23T11:28:58Z.
attacking: fixed-heat coefficient stability at the near-null endpoint, and the exact boundary between fixed-law regularity and law-uniform perturbation.

# account03/B15 auto17 — fixed-heat rough-law compiler and no uniform matrix-modulus theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** account03/B15  
**Run:** `20260923T112858Z-account03-B15-qform-auto17`  
**Status:** `ESSENTIAL_STEP_APPLIED / FIXED-HEAT-ROUGH-LAW-COMPILER / UNIFORM-MATRIX-MODULUS-REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This run supplies the precise finite-heat rough-law passage requested by the newest B15 assignment and proves a target-level obstruction showing that this passage cannot be upgraded to a law-uniform coefficient perturbation estimate, even if both compared matrices are full rank and have third singular value exactly one.

## 1. Fresh controls and exact dependencies

At prepublication refresh, `yspennstate/math-research-brain` main was observed at commit

`2379f69200ac1a510020a5924d743adbc28cc42b`,


The designated completed partner result actually applied is account04/B15's Gaussian heat-height theorem:

- repository/commit: `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

For every Borel probability law `mu` on `R`, with

`H_epsilon(mu;y)=(mu*gamma_epsilon)(y)` and `M_epsilon(mu)=sup_y H_epsilon(mu;y)`, it proves

`sup_{epsilon>0} M_epsilon(mu)=||p_mu||_infinity`,

with value `+infinity` if no bounded density exists; and if `p_mu in C_0`, then `M_epsilon(mu)->max p_mu` as `epsilon downarrow0`.

The newest owner-required mathematical result actually applied is the volume-stability theorem:

- repository/commit: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`;
- path: `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

On its certified original-coordinate cross-block branch `M=M0+E`, `s3(M0)>=a`, `max diag(P_range(M0))<=1/2`, `||E||op<=a/16`, it proves a continuous density with

`||p_Q||_infinity <= 24 sqrt(3)e/(5a) <23/a`,                         (1.1)

for the full ambient quadratic-plus-affine output, with all self blocks and outside couplings retained.

The immediately preceding B15 run was

`yspennstate/math-open-problems@ac5676953c28ec64bc907924b20ef9a24542c914`,

which proved lower semicontinuity of density height under weak convergence. The present result is a strict finite-scale refinement: at every fixed positive Gaussian heat scale, the entire smoothed density converges **uniformly in the output center**, not merely through a liminf inequality for its eventual height.

## 2. Uniform convolution closure under weak convergence

### Theorem 2.1 — fixed-kernel uniform closure

Let `mu_m=>mu` weakly be probability measures on `R`. For every `K in C_0(R)`,

`boxed: ||mu_m*K-mu*K||_infinity ->0.`                             (2.1)

No density, moment or support assumption is imposed.

### Proof

Because `K in C_0(R)`, it is bounded and uniformly continuous. Put `B=||K||infinity`.

Fix `eta>0`. Weak convergence makes `{mu_m}` uniformly tight. Choose `R>0` so that, for all sufficiently large `m`,

`mu([-R,R]^c)<eta`,  `mu_m([-R,R]^c)<eta`.                         (2.2)

Choose `S>0` such that

`|K(u)|<eta` whenever `|u|>S`.                                      (2.3)

If `|y|>R+S`, then for `|x|<=R`, `|y-x|>S`, hence

`|(mu_m*K)(y)| <= eta + B eta`,
`|(mu*K)(y)|   <= eta + B eta`.                                    (2.4)

Thus the difference is uniformly small outside the compact y-window `[-R-S,R+S]`.

On that compact window, uniform continuity gives a finite grid `y_1,...,y_N` such that for each y in the window some `y_j` satisfies

`sup_x |K(y-x)-K(y_j-x)|<eta`.                                      (2.5)

For each fixed `j`, the function `x -> K(y_j-x)` is bounded and continuous, so weak convergence gives

`int K(y_j-x)dmu_m(x) -> int K(y_j-x)dmu(x)`.                       (2.6)

Since there are finitely many grid points, the convergence is uniform in j. Equation (2.5) then gives, uniformly over the entire compact y-window,

`|(mu_m*K)(y)-(mu*K)(y)| <= o(1)+2eta`.                             (2.7)

Combine (2.4) and (2.7), then send `eta downarrow0`. This proves (2.1). QED.

### Corollary 2.2 — Gaussian heat profiles

For every fixed `epsilon>0`,

`boxed:
  sup_y |H_epsilon(mu_m;y)-H_epsilon(mu;y)| ->0,
  M_epsilon(mu_m)->M_epsilon(mu).
`                                                                         (2.8)

The second conclusion follows from `|sup f-sup g|<=||f-g||infinity`.

## 3. Rough-law / varying-quadratic compiler at fixed heat scale

Let `nu_m=>nu` be probability laws on `R^n`, and let continuous maps `q_m:R^n->R` converge to `q` uniformly on compact sets. Standard tightness plus local-uniform convergence gives

`(q_m)_#nu_m => q_#nu`.                                                (3.1)

Applying Theorem 2.1 to these pushforwards yields, for every fixed `epsilon>0`,

`boxed:
 sup_y |
   int gamma_epsilon(q_m(x)-y)dnu_m(x)
  -int gamma_epsilon(q(x)-y)dnu(x)
 | ->0.
`                                                                         (3.2)

In particular, if the dimension is fixed, `A_m->A`, `b_m->b`, `c_m->c`, and the cap-one product laws `nu_m=>nu`, then

`q_m(x)=x^T A_m x+b_m^T x+c_m`

converges uniformly to `q` on compacts, and (3.2) applies. No moments are needed. The cap-one product class is weakly closed in fixed dimension, so the limiting law remains admissible.

This is a precise rough-law trace justification for positive heat estimates: a bound at a fixed positive heat scale passes to a weak coefficient/input limit with no loss and with uniformity in the output center.

## 4. Main obstruction — no law-uniform fixed-heat modulus in the matrix

The previous theorem is necessarily **fixed-sequence/fixed-law compactness**, not a uniform perturbation estimate over the owner target class. The failure persists even if both matrices are full rank.

### Theorem 4.1 — `QFORM-NO-LAW-UNIFORM-FIXED-HEAT-MATRIX-MODULUS-v1`

There exist one fixed heat scale `epsilon_0>0`, a sequence `delta downarrow0`, full-rank target matrices `A_delta^-`, `A_delta^+` with

`||A_delta^+-A_delta^-||op=delta`,
`s3(A_delta^-)=s3(A_delta^+)=1`,                                      (4.1)

and, for each delta, one common admissible cap-one product law `X^(delta)` such that

`boxed:
 M_epsilon0(X^T A_delta^- X)
 -M_epsilon0(X^T A_delta^+ X)>1/4.
`                                                                          (4.2)

Hence no modulus `omega(r)->0` can control the fixed-positive-scale Gaussian heat maximum uniformly in the coefficient matrix over all admissible product laws, even on full-rank matrices with normalized third singular value one.

### Proof

Let

`X_1,X_2,X_3 iid Uniform[-1/2,1/2]`,                               (4.3)

and put

`Q_0=X_1^2+X_2^2+X_3^2`.                                           (4.4)

For one square, the density is

`h(u)=u^(-1/2) 1_(0,1/4)(u)`.                                     (4.5)

Thus `p_0=h*h*h`. Since `h in L^1`, the threefold convolution is in `C_0`; moreover `h*h<=pi` by the beta integral, so it is bounded. Its support lies in `[0,3/4]`, and therefore

`||p_0||infinity >= 1/(3/4)=4/3`.                                  (4.6)

Apply the completed account04/B15 heat-height theorem. Since `p_0 in C_0`,

`M_epsilon(Q_0)->max p_0>=4/3` as `epsilon downarrow0`.             (4.7)

Choose **one fixed** `epsilon_0>0` so that

`M_epsilon0(Q_0)>1`.                                                (4.8)

Let

`L_0=||gamma_epsilon0'||infinity
    =1/(sqrt(2 pi e) epsilon_0^2)`.                                (4.9)

For small `delta>0`, let the fourth coordinate be independent with

`X_4=delta^(-1)+U`, `U Uniform[0,1]`,                              (4.10)

and define the two full-rank matrices

`A_delta^- =diag(1,1,1,delta^2)`,
`A_delta^+ =diag(1,1,1,delta^2+delta)`.                             (4.11)

Every marginal density is at most one. For `0<delta<1/2`, both matrices have at least three eigenvalues of modulus at least one, are full rank, have third singular value exactly one, and satisfy (4.1).

For the minus matrix,

`delta^2 X_4^2 = 1+V_delta`,
`V_delta=2delta U+delta^2 U^2`,
`0<=V_delta<=2delta+delta^2`.                                      (4.12)

Let `y_0` maximize the `epsilon_0` heat profile of `Q_0`. Evaluating the minus heat profile at the translated center `y_0+1` and using the Lipschitz constant (4.9),

`M_epsilon0(Q_delta^-)
 >= E H_0(y_0-V_delta)
 >= M_epsilon0(Q_0)-L_0(2delta+delta^2),`                           (4.13)

where `H_0(y)=E gamma_epsilon0(Q_0-y)`.

Choose delta sufficiently small that

`L_0(2delta+delta^2)<1/4`.                                          (4.14)

Then (4.8) gives

`M_epsilon0(Q_delta^-)>3/4`.                                        (4.15)

For the plus matrix, put `c_delta=delta+delta^2`. Conditional on U,

`c_delta X_4^2=c_delta(delta^(-1)+U)^2`.                            (4.16)

As a function of U, its derivative is

`2c_delta(delta^(-1)+U)>=2(1+delta)`.                              (4.17)

Therefore the random variable `c_delta X_4^2` has a density bounded by

`1/[2(1+delta)]<1/2`.                                               (4.18)

It is independent of `Q_0`, so convolution gives

`||p_(Q_delta^+)||infinity <=1/[2(1+delta)]<1/2`.                  (4.19)

Applying the partner heat theorem (or simply convolution contraction),

`M_epsilon0(Q_delta^+)<=1/[2(1+delta)]<1/2`.                       (4.20)

Equations (4.15) and (4.20) imply (4.2). QED.

### Interpretation

This is stronger than the elementary observation that a small operator-norm coefficient can create a large random value on far-away supports. The heat maximum is invariant under deterministic output translation, so the diverging constant term in (4.12)/(4.16) is irrelevant. What changes discontinuously in the law-uniform sense is the **amount of smoothing** induced by the remote cap-one coordinate.

Thus neither continuity of each individual output density nor positive Gaussian smoothing creates a law-uniform matrix perturbation theory under the owner hypotheses.

This theorem is an obstruction to an intermediate proof mechanism only. Both outputs above have bounded densities; it is not a counterexample to the QFORM conjecture.

## 5. Actual application of the newest volume theorem and partner result

On the volume-stability branch (1.1), the completed account04/B15 heat-height theorem gives the exact positive-regularization inequality

`boxed:
 sup_{epsilon>0,y}
 E gamma_epsilon(X^T A X+b^T X+c-y)
 <= 24 sqrt(3)e/(5a).
`                                                                          (5.1)

This is an actual equation combining the newest owner-required theorem and the designated partner result. Conversely, by the partner theorem, (5.1) is equivalent to the density cap on that branch; there is no additional regularity cost.

Now let a sequence of certified branch instances with the same parameter `a` converge weakly in the precise sense of Section 3. For every fixed epsilon, (3.2) passes (5.1) to the limit uniformly in y. Since this holds for every positive epsilon, the partner theorem recovers the same density bound at the limiting instance. This supplies a direct heat-level rough-law trace passage for that density estimate.

Theorem 4.1 marks the exact boundary of this compiler: one may pass a **uniformly proved** estimate along a convergent sequence, but one cannot create the uniform estimate merely from closeness of the coefficient matrices to a paid null endpoint. The near-null/high-leverage branch therefore still needs product geometry, not perturbative regularity.

## 6. Continuity ledger

The central statement proved here is finite-scale regularity/closure, not a new raw-density continuity theorem. The source-reported completed B15 chain gives `C_0` densities for individual rank-at-least-three instances, but shared `CLAIMS.json` still records the full-target continuous-representative item separately pending consolidation. Nothing in Theorem 2.1 requires that issue to be settled.

For the explicit base law in Section 4, continuity is elementary from the convolution representation `p_0=h*h*h`, so the counterexample to a uniform matrix modulus does not depend on the unsettled shared continuity ledger.

A universal `L^infinity` proof can therefore use weak-limit/heat closure safely, but must not invoke a uniform raw-density modulus, a uniform heat desmoothing rate, or a uniform coefficient modulus. The missing theorem remains the universal height bound in the near-null/high-leverage/product-coupled survivors.

## 7. What changed and the first unpaid implication

This run sharpens the regularity map in two directions:

1. **Positive:** weak convergence plus locally uniform convergence of the quadratic maps implies **uniform-in-center convergence of every fixed Gaussian heat profile**. This is the precise rough-law trace compiler requested by the newest B15 assignment.
2. **Negative:** no coefficient modulus for those fixed heat maxima can be uniform over all admissible cap-one product laws, even with full-rank matrices and fixed `s3=1`.

Therefore the first unpaid implication is not a limiting/continuity defect. It is genuinely quantitative geometry: obtain a universal heat/density estimate in the near-null/high-leverage branch before taking the limit. Once such estimates are available uniformly along approximants, Sections 2–3 pass them to rough and algebraically degenerate endpoints with zero loss.

No task, schedule, enablement, notification, email, permission, cross-account, public-release, or paid-model/API/Codex setting was changed in this run. Repository transport did not establish native receiver ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
