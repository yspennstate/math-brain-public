Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-12 — random signed-affine universality for the negative spherical perceptron

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Applied parent: **T03 negative spherical perceptron, kappa=-1, exact sphere**  
Status: **PARTIAL / NEW FINITE-N PROBABILITY COMPARISON / NEW SIGNED DEPENDENT FULL-RANK APPLICATION / ORIGINAL T03 UNCHANGED**

## 1. Compact handoff: P12 and the immediately preceding universality result

The latest canonical P12 report remains

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its frozen theorem is source-exact as follows. For `F in {R,C}`, let `A_m in F^{N_m x m}` have iid centered variance-one entries with densities `f_m`. Assume one fixed integer `q>=1` and one finite constant `M` satisfy

`sup_m ||f_m^{*q}||_infty <= M`,

and assume

`N_m/m -> gamma>1`, `k_m=r_m+1`, `k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) -> -h(gamma)/d_F` in probability,

with `d_R=1`, `d_C=2`. There is **no fourth-moment assumption and no positive-moment assumption above variance normalization**. Fixed bounded-density laws are covered by `q=1`. P12's still-unresolved mathematical successor is triangular smooth / bounded-fourth-moment universality without a uniform microscopic finite-convolution smoothing hypothesis. P12 is mathematically frozen; its remaining historical obligation is independent protocol review, not another author-side lemma.

I do **not** reopen or repackage the posted row-submatrix, mesoscopic-spike, kernel, ReLU, or zero-margin/Ising results. The theorem below concerns a different object: exact negative-margin spherical feasibility after adding a random signed affine closure of the Gaussian constraint rows.

The immediately preceding NM13-12 report was

`2026-09-20T0658Z__t03-substochastic-barycentric-universality.md`.

It proved the deterministic pathwise identity

`SAT([A;WA],kappa)=SAT(A,kappa)`

when `W>=0` has row sums at most one and `kappa<=0` (exact row-stochastic closure is the zero-loss case). Its explicit next obstruction was **signed barycentric contamination**: once coefficients can be negative, lower bounds on the core projections no longer imply lower bounds on their signed combinations.

This run attacks that obstruction with a genuinely different method: random signed affine coefficients plus conditional Gaussian concentration around the row average. The sign restriction is removed probabilistically rather than repaired by another covariance or singular-value argument.

## 2. Current T03 parent and coordination with NM13-03 / NM13-07

The exact source model is unchanged. In unit-vector normalization, for `m=floor(alpha N)` and iid rows `g_i~N(0,I_N)`, seek `x in S^{N-1}` satisfying

`g_i . x >= -1`, all `i<=m`.

Equivalently, with `sigma=sqrt(N)x`, this is the source radius-`sqrt(N)` system

`<g_i,sigma> >= -sqrt(N)`.

Current companion state on `master` is complementary to the present route:

1. `NM13-03`, latest report `2026-09-20__t03-thirdfull-feasibility-alpha12288.md`, derived the complete third-full objective, algebraically eliminated the `q3,q2,gamma_p` sector, and produced a high-accuracy **CONDITIONAL** exact-sphere upper candidate `alpha=12.288` with positive comparison value. It did not promote this to a directed-interval source endpoint because the five-dimensional root and the two-dimensional Gaussian expectation are not yet outward-enclosed.
2. `NM13-07`, latest report `2026-09-20__t03-thirdfull-score-overlap-reduction.md`, proved exact heat-semigroup/score identities and reduced the third-full capacity system to five derivative-free scalars. It explicitly leaves `12.288` conditional and retains the earlier review-pending complete-second candidate `12.31963485`.

This NM13-12 run does not recompute the lifted objective, stationarity equations, quadrature, or interval boxes. It develops a disorder-universality theorem. Every present or future T03 upper endpoint transfers to the new model by an exact event inclusion; the lower endpoint is transferred using a vanishing explicit margin loss.

For status bookkeeping I keep three levels distinct:

- rigorous LP lower endpoint: `alpha_L=1/Phi(-1)=6.302974375068753...`;
- older conservative rigorous upper endpoint retained by the project: `12.78437096216`;
- current peer review-pending candidate upper endpoint: `12.31963485`;
- newer third-full `12.288`: **CONDITIONAL**, not promoted here.

The original T03 parent is not moved by this worker.

## 3. New mechanism — Gaussian signed-affine closure

For `A in R^{m x N}` and threshold `kappa`, write `SAT(A,kappa)` for existence of `x in S^{N-1}` with

`Ax >= kappa 1_m`.

Let

`P_m = I_m - (1/m) 1_m 1_m^T`

be orthogonal projection onto the mean-zero subspace. Let `xi_1,...,xi_K iid N(0,I_m)`, independent of `A`. For an amplitude `delta>0`, define signed affine weights

`w_j^T = (1/m) 1_m^T + (delta/m) xi_j^T P_m`,

and collect them as `W in R^{K x m}`. Every row satisfies exactly

`w_j^T 1_m = 1`,

but for nonzero `delta` the coefficients are signed with positive probability. Define the added block

`B = W A`.

### Theorem NM12-RSA (finite-N random signed-affine comparison)

For every deterministic `A`, every `tau>0`, every real `kappa`, and every `L>=||A||_op`,

`P_W( SAT([A;WA],kappa) | A )`

is at least

`1 - K exp[-m^2 tau^2/(2 delta^2 L^2)]`

on the event `SAT(A,kappa+tau)`. Equivalently, for random `A` independent of `W`,

`P{SAT([A;WA],kappa)}`
` >= P{SAT(A,kappa+tau), ||A||_op<=L}`
`    - K exp[-m^2 tau^2/(2 delta^2 L^2)]`.                 (3.1)

Always, without probability or sign assumptions,

`SAT([A;WA],kappa) subset SAT(A,kappa)`,                   (3.2)

because the augmented system contains all original rows.

### Proof

Fix `A` and suppose `x in S^{N-1}` is a witness to

`Ax >= (kappa+tau) 1_m`.

Put `y=Ax` and `ybar=m^{-1}1^T y`. Then `ybar>=kappa+tau`. For one added row,

`(WAx)_j = w_j^T y`
`          = ybar + (delta/m) xi_j^T P_m y`.               (3.3)

Conditional on `A` and this fixed witness `x`, the second term in (3.3) is centered Gaussian with variance

`delta^2 ||P_m y||_2^2 / m^2`.

Hence, if `P_m y` is nonzero,

`P_W{(WAx)_j < kappa | A,x}`
` <= exp[-m^2 (ybar-kappa)^2/(2 delta^2 ||P_m y||_2^2)]`
` <= exp[-m^2 tau^2/(2 delta^2 ||A||_op^2)]`.              (3.4)

If `P_m y=0`, the failure probability is zero, so the same bound holds. A union bound over `j<=K` proves that the **same witness** satisfies every added constraint with conditional probability at least

`1-K exp[-m^2 tau^2/(2 delta^2 ||A||_op^2)]`.

This pointwise conditional lower bound holds for every `A` for which a stronger-margin witness exists; no measurable choice of a canonical witness is needed because the conditional probability of the existential augmented event is at least the success probability for any one such witness. Replacing `||A||_op` by `L` and integrating over `A` gives (3.1). Inclusion (3.2) is immediate. QED.

### What changed relative to the predecessor

The preceding barycentric theorem required every weight to be nonnegative. Theorem NM12-RSA allows **arbitrarily many negative coefficients** and controls their aggregate effect only through cancellation in a random mean-zero affine perturbation. The price is no longer zero pathwise loss; it is an explicit stronger-core margin `tau` and a Gaussian failure term.

The theorem is also not another low-rank/singular-value statement. It never bounds the rank or singular values of `WA`; in the concrete application below `WA` is full rank almost surely. The proof uses only one-dimensional concentration along a core witness plus the random-matrix scale `||A||_op`.

## 4. Gaussian-core quantitative rate

Now let `A` be an `m x N` iid standard real Gaussian matrix. The standard Gaussian operator-norm estimate gives, for every `s>=0`,

`P{||A||_op > sqrt(m)+sqrt(N)+s} <= exp(-s^2/2)`.          (4.1)

Take

`L_N = sqrt(m)+sqrt(N)+s_N`,

and choose

`tau_N = (delta_N L_N/m) sqrt(2 log(K_N N^q))`             (4.2)

for any fixed `q>0`. Then the conditional union term in (3.1) is exactly at most `N^{-q}`. Therefore

`P_aug(kappa)`
` >= P_core(kappa+tau_N)`
`    - exp(-s_N^2/2) - N^{-q}`.                            (4.3)

For the linear regime

`m/N -> alpha>0`, `K_N/N -> beta in (0,infinity)`,

choose `s_N=sqrt(4 log N)` and `q=2`. Then

`tau_N`
` = (delta_N (sqrt(alpha)+1)/alpha + o(delta_N))`
`   * sqrt(6 log N/N)`.                                    (4.4)

Consequently

`delta_N = o(sqrt(N/log N))`                               (4.5)

is sufficient for `tau_N -> 0` while `K_N=Theta(N)` signed rows are added.

This is the quantitative universality rate produced by the present mechanism. The allowed signed-affine amplitude can diverge almost as fast as `sqrt(N/log N)` while the feasibility comparison still loses only `o(1)` in margin.

## 5. The signed class is genuinely outside nonnegative barycentric closure

Take the concrete amplitude

`delta_N=N^(1/4)`.

For one weight row write `Z_i` for the iid standard Gaussian coordinates and `Zbar=m^{-1}sum_i Z_i`. Then

`w_i = [1 + delta_N (Z_i-Zbar)]/m`.                        (5.1)

The empirical fraction of negative coefficients is

`m^{-1} # {i: Z_i-Zbar < -1/delta_N}`.

Since `Zbar->0` in probability, `1/delta_N->0`, and the empirical Gaussian cdf converges uniformly, this fraction converges in probability to

`Phi(0)=1/2`.                                               (5.2)

Even more strongly, the total negative coefficient mass diverges. Namely

`sum_i (-w_i)_+ / delta_N`
` = m^{-1} sum_i [-1/delta_N-(Z_i-Zbar)]_+`
` -> E[(-Z)_+] = 1/sqrt(2 pi)` in probability.             (5.3)

Thus

`sum_i (-w_i)_+ ~ delta_N/sqrt(2 pi) -> infinity`.         (5.4)

This is far outside the predecessor hypothesis `W>=0`; the new theorem is not obtaining signedness from a vanishing total negative mass.

At the same time the cancellation scale relevant to a fixed witness is small. The row coefficient l2 norm is of order `delta_N/sqrt(m)`, and (4.4) gives

`tau_N = O(N^(-1/4) sqrt(log N)) -> 0`.                    (5.5)

The mechanism is therefore genuinely directional: the added rows can have large Euclidean norm in ambient space while their random signed fluctuation along the selected core witness is small.

## 6. Concrete unresolved T03 extension

Fix `beta=1` and `delta_N=N^(1/4)`. Let

`m_N=floor(alpha N)`, `K_N=N`.

Generate the Gaussian T03 core

`A_N in R^{m_N x N}`, iid `N(0,1)`.

Independently generate `xi_j iid N(0,I_{m_N})`, form the signed affine matrix `W_N` above, and add

`B_N=W_N A_N`.

The augmented exact-sphere problem asks for `x in S^{N-1}` satisfying

`A_N x >= -1`,
`B_N x >= -1`.                                             (6.1)

It has total constraint density

`lambda = alpha+1+o(1)`.

This model is not iid Gaussian disorder and is not covered by the nonnegative closure theorem.

### 6.1 Full rank almost surely

Assume `m_N>=N`, which holds throughout the T03 density range. Each row of `W_N` has a smooth Gaussian density on the affine hyperplane

`H={w in R^m: 1^T w=1}`.

There exist `N` linearly independent points of `H` (for example the first `N` coordinate vectors), and the rank-deficient set is a proper algebraic subset of `H^N`. Therefore

`rank(W_N)=N` almost surely.

Conditional on such a `W_N`, the columns of `B_N=W_NA_N` are independent Gaussian vectors with covariance `W_NW_N^T`, which is positive definite. Hence

`rank(B_N)=N` almost surely.                                (6.2)

So the added block is genuinely full ambient rank.

### 6.2 Added rows are non-Gaussian

For one coordinate `X` of one added row, conditional on its weight vector `w`,

`X | w ~ N(0,V)`, `V=||w||_2^2`.

Orthogonality of `1` and `P_m xi` gives exactly

`V = 1/m + (delta_N^2/m^2) Q`,
`Q ~ chi-square_{m-1}`.                                    (6.3)

Thus `V` is nonconstant for every `delta_N>0`, so `X` is a nontrivial Gaussian variance mixture. In particular

`E X^4 = 3 E V^2 > 3(EV)^2`,                               (6.4)

and the row marginal is not Gaussian.

### 6.3 Added rows are dependent

Different rows share the same Gaussian core `A_N`. For `j!=k`, one coordinate satisfies

`Cov((B_N)_{j1},(B_N)_{k1})`
` = E[w_j^T w_k]`
` = ||E w_j||_2^2`
` = 1/m_N > 0`.                                             (6.5)

Thus the added constraints are mutually dependent and dependent on the original core. Ordinary iid-row universality does not apply.

## 7. T03 transfer with explicit hypotheses checked

### Lower side

The project uses Montanari--Zhong--Zhou's rigorous LP success theorem in the exact Gaussian spherical normalization:

`alpha < delta_lin(kappa):=1/Phi(kappa)`

implies high-probability feasibility at fixed margin `kappa`.

Fix any

`alpha < 1/Phi(-1)`.

By continuity of `1/Phi(kappa)`, choose a fixed `eps>0` such that

`alpha < 1/Phi(-1+eps)`.

MZZ therefore gives

`P{SAT(A_N,-1+eps)} -> 1`.

Because `delta_N=N^(1/4)` satisfies (4.5), `tau_N->0`; eventually `tau_N<eps`. Hence

`SAT(A_N,-1+eps) subset SAT(A_N,-1+tau_N)`.

Applying (4.3) yields

`P{SAT([A_N;B_N],-1)} -> 1`.                               (7.1)

Therefore the augmented model has the same rigorous lower endpoint in **core-density** coordinates:

`alpha_L=6.302974375068753...`.

Since total density is `lambda=alpha+1+o(1)`, its rigorous total-density lower endpoint is

`lambda_L=7.302974375068753...`.                            (7.2)

No uniform-in-`kappa` version of MZZ is silently assumed: the argument uses one fixed `eps>0` selected after fixing a strict subcritical `alpha`.

### Upper side

For every realization,

`SAT([A_N;B_N],-1) subset SAT(A_N,-1)`.

Therefore every Gaussian-core UNSAT upper endpoint transfers with **zero loss** in core-density coordinates and with `+1` in total-density coordinates.

Using the older conservative rigorous source upper endpoint `12.78437096216`,

`lambda_U,rig = 13.78437096216`.                            (7.3)

Using NM13-07's current review-pending complete-second candidate `12.31963485` transfers the same status to

`lambda_U,cand = 13.31963485`.                              (7.4)

Using the newer companion third-full value `12.288` transfers only **conditionally**:

`lambda_U,third = 13.288`,                                  (7.5)

because the parent `12.288` root is not yet interval-certified. This run does not upgrade that status.

Thus the concrete signed/dependent/full-rank model (6.1) has the rigorous project-supported bracket

`7.302974375068753... <= lambda_c <= 13.78437096216`,       (7.6)

with exact threshold existence still UNKNOWN. The stronger `13.31963485` and `13.288` upper values retain exactly their parent review-pending / conditional statuses.

## 8. Strict theory gain versus original-parent before/after

### Original T03 parent claim

This worker does not move the iid-Gaussian exact-sphere threshold itself.

Before this run:

- rigorous lower: `6.302974375068753...`;
- older conservative rigorous upper: `12.78437096216`;
- review-pending peer candidate: `12.31963485`;
- third-full conditional candidate: `12.288`.

After this run: **the same values with the same statuses**.

So the original parent metric has **NO NM13-12 MOVEMENT**.

### Demonstrated universality gain

Before this run, the pathwise barycentric closure required nonnegative coefficient rows.

After this run:

- coefficients may be signed on asymptotically half of their coordinates;
- total negative coefficient mass may diverge like `delta_N/sqrt(2 pi)`;
- `delta_N` may grow as any `o(sqrt(N/log N))` in the linear-row regime;
- the added block may be full rank;
- added row marginals may be non-Gaussian variance mixtures;
- added rows may be mutually dependent and dependent on the Gaussian core;
- the finite-N comparison error is explicit in (4.3);
- all Gaussian-core UNSAT upper bounds transfer pathwise with zero loss;
- MZZ's lower endpoint transfers asymptotically with no endpoint loss because the required stronger-margin shift is `o(1)`.

This is a strict distributional-class / sign-assumption extension, not a renamed instance of the posted row-submatrix/kernel/ReLU/zero-margin results and not a repetition of the previous covariance/singular-value theorems.

## 9. Essential executed checker

Executed source:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T0751Z__signed_affine_universality_check.py`

Archived output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T0751Z__signed_affine_universality_check.out`

The checker verifies:

1. the chosen Gaussian operator-norm and conditional union error budgets;
2. the explicit `tau_N` rate for `delta_N=N^(1/4)`;
3. the exact Gaussian formulas for negative-coordinate fraction and negative coefficient mass;
4. exact row sums equal to one in a seeded finite realization;
5. presence of negative weights;
6. full row rank of `W` and full rank of `B=WA` in the seeded sanity instance;
7. the one-row Gaussian tail inequality used in the theorem;
8. strictly super-Gaussian fourth moment of a row coordinate due to random variance mixing.

The archived output ends

`ALL_SIGNED_AFFINE_CHECKS_PASS`.

Selected quantitative values for `alpha=6`, `beta=1`, `delta_N=N^(1/4)` are:

- `N=10^4`: `tau_N=0.434903043595`, expected signed negative fraction `0.460171831925`;
- `N=10^6`: `tau_N=0.165881374094`, negative fraction `0.487386438634`;
- `N=10^8`: `tau_N=0.0604561001812`, negative fraction `0.496010643682`.

The negative mass grows from `3.51` to `39.40` across these benchmarks while the margin loss decreases, numerically illustrating the theorem's cancellation mechanism.

## 10. Bounded current-literature sanity check

Dated check: **20 September 2026**.

The exact source remains the negative Gaussian spherical perceptron on radius `sqrt(N)` (El Alaoui--Sellke, arXiv:2010.15811). Stojnic's fully lifted RDT treatment (arXiv:2312.16531) remains the relevant lifted-comparison source; its practical capacity values require substantial numerical work. A fresh search also surfaced the September 2026 exact **online asymmetric binary** perceptron threshold (arXiv:2609.02124), but that is a different binary/online model and does not close T03 or subsume the signed-affine theorem here. No matching rigorous finite-N signed-affine closure theorem for this exact spherical feasibility event surfaced in the bounded search. This is bounded negative evidence, not a worldwide novelty certificate.

## 11. Preserved failures / obstruction and next attack

Preserved obstruction from the predecessor: arbitrary deterministic signed barycentric weights cannot be controlled from one-sided core inequalities alone, because negative coefficients can multiply arbitrarily large positive core projections.

This run succeeds only because the signed component is random, centered in coefficient space, and independent of the core; the fluctuation along a fixed core witness is then one-dimensional Gaussian with variance controlled by `||A||_op`.

The new remaining obstruction is meaningful rather than administrative:

**Can the independence of the signed coefficient noise from the core be weakened?**

A next nonduplicating route is to allow coefficient rows selected from the core through a low-information / leave-one-block-out rule and prove a conditional subgaussian projection bound. That would enlarge the model from independent signed affine perturbations to genuinely adaptive signed closures while retaining an `o(1)` margin loss. A second possible route is to replace Gaussian coefficient noise by a sharp subgaussian Orlicz condition and identify the best tail constant in (4.3).

No peer files, shared root ledgers, schedules, permissions, workflows, email/Drive resources, or public surfaces were modified.

## 12. ledger_delta

- track: `NM13-12 / progress-universality`
- parent: `T03 negative spherical perceptron`
- parent_source_metric: exact-sphere iid-Gaussian threshold bracket
- parent_before_rigorous: `[6.302974375068753..., 12.78437096216]`
- parent_after_rigorous: `[6.302974375068753..., 12.78437096216]`
- parent_before_review_pending_candidate_upper: `12.31963485`
- parent_after_review_pending_candidate_upper: `12.31963485`
- parent_thirdfull_conditional_upper: `12.288` before and after
- parent_movement_by_NM13-12: `NO MOVEMENT`
- theory_quantity: allowable signed-affine coefficient amplitude in linear-row regime with vanishing margin loss
- theory_before: `delta_N=0` for exact nonnegative barycentric closure; signed case not covered by that theorem
- theory_after: `delta_N=o(sqrt(N/log N))` for independent centered Gaussian affine perturbations, with explicit finite-N loss (4.3)
- sign_gain: negative-coordinate fraction may tend `1/2`; total negative mass may diverge
- concrete_application: `K_N=N`, `delta_N=N^(1/4)`, full-rank dependent non-Gaussian added rows
- application_before: `UNKNOWN / UNMEASURED` in this namespace
- application_after_rigorous_total_density_bracket: `[7.302974375068753..., 13.78437096216]`
- application_review_pending_candidate_upper: `13.31963485`
- application_thirdfull_conditional_upper: `13.288`
- exact_threshold_status: `UNKNOWN`
- checker: `PASS / ALL_SIGNED_AFFINE_CHECKS_PASS`
- coordination_NM13_03: consumed third-full conditional `12.288`; did not duplicate lifted calculation
- coordination_NM13_07: consumed score-overlap reduction and `12.31963485` status; did not duplicate interval work
- posted_exclusions_respected: `yes`
- next_obstruction: adaptive/core-dependent signed coefficients or general subgaussian coefficient universality

# END_OF_NM13_12_SIGNED_AFFINE_REPORT
