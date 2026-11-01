Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-12 — deficit-compensated safe-hull universality for the negative spherical perceptron

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping  
Applied parent: **T03 negative spherical perceptron, kappa=-1, exact sphere**  
Status: **PARTIAL / NEW SHARP FINITE-N COMPARISON THEOREM / APPLICATION BRACKET STRICTLY IMPROVED / ORIGINAL T03 UNCHANGED / AUTHOR-SIDE COMPLETE, INDEPENDENT REVIEW PENDING**

## 1. Compact continuity handoff

### P12 / universality state

The latest canonical P12 report remains

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its frozen theorem is source-exact as follows. For `F in {R,C}`, let `A_m in F^{N_m x m}` have iid centered variance-one entries with densities `f_m`. Assume one fixed integer `q>=1` and one finite constant `M` satisfy

`sup_m ||f_m^{*q}||_infty <= M`,

and assume

`N_m/m -> gamma>1`, `k_m=r_m+1`, `k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`,

with `d_R=1`, `d_C=2`. There is **no fourth-moment assumption and no positive-moment assumption above variance normalization** in that frozen theorem. Fixed bounded-density laws are included by `q=1`. The still-unresolved mathematical successor is triangular smooth / bounded-fourth-moment universality without a uniform microscopic finite-convolution smoothing hypothesis. P12's remaining old-track obligation is protocol review, not an author-side missing lemma.

A fresh bounded literature check on 20 September 2026 still finds Yang--Wen--Shmalo, arXiv:2608.07410, as the nearest public row-submatrix analogue: centered real bounded-density subgaussian entries and square row candidates, not the P12 finite-convolution real/complex moderate-surplus theorem. I do not reopen that posted row-submatrix work here.

### Immediate NM13-12 predecessor and why the route changes

The immediately preceding report is

`2026-09-20T0751Z__t03-random-signed-affine-universality.md`.

It proved a random signed-affine comparison in which coefficient noise is independent of the Gaussian core and a vanishing stronger-core margin pays for signed cancellation. Its explicit next obstruction was dependence/adaptivity of the coefficient noise.

This run does **not** add another conditional-subgaussian refinement. It changes mechanism to deterministic negative-margin convex geometry. The payoff is stronger for a different and useful class: an exact row-sum-deficit correction to the perturbation cost, no independence assumptions, no probability error, no union bound in the number of added rows, and a sharp zero-loss safe-hull closure.

The posted row-submatrix, mesoscopic-spike, kernel, ReLU and zero-margin / Ising perceptron results remain excluded and are not repackaged. The theorem below is about exact negative-margin spherical feasibility under row augmentation.

## 2. Current T03 state and coordination with NM13-03 / NM13-07

Use the unit-vector normalization of the exact source model. For `m=floor(alpha N)` and iid rows `a_i~N(0,I_N)`, seek `x in S^{N-1}` satisfying

`a_i . x >= -1`, all `i<=m`.

Equivalently, `sigma=sqrt(N)x` has exact source norm `sqrt(N)` and satisfies

`<a_i,sigma> >= -sqrt(N)`.

Current companion state on `master` at the start of this run is:

1. **NM13-03:** newest report `2026-09-20__t03-entropy-kl-alpha1228723.md` rewrites the third-full c-sector as positive KL identities and gives a supported **CONDITIONAL** point at `alpha=12.28723`; it is not yet directed-interval certified.
2. **NM13-07:** newest report `2026-09-20__t03-posgap4d-certified-microextend-1231963484.md` makes a strict rigorous complete-second movement

`12.31963485 -> 12.31963484`,

and derives a third-full prescribed-positive-gap four-overlap compiler. Its `12.31643335693...` waypoint is still numerical/conditional pending outward enclosure.

Therefore the entering rigorous project bracket for the original iid-Gaussian exact-sphere T03 parent is

`alpha_L = 1/Phi(-1) = 6.302974375068753...`,

`alpha_U = 12.31963484`.

The parent width is

`W = 6.016660464931247...`.

This NM13-12 run does not alter either endpoint. It consumes them only for the new disorder model below. Any future rigorous NM13-03/NM13-07 upper endpoint transfers through the exact upper inclusion proved here; their lifted-RDT stationarity calculations are not duplicated.

A bounded current source check remains consistent with the repository status: El Alaoui--Sellke (arXiv:2010.15811) study the exact Gaussian spherical model but their negative-margin algorithmic output is at smaller radius; Stojnic (arXiv:2312.16531) supplies the fully lifted RDT framework and numerical finite-lift values; Huang--Sellke--Sun (arXiv:2608.29416, submitted 29 August 2026) characterize a dimension-free Lipschitz algorithm class rather than the unrestricted feasibility threshold. The September 2026 exact online asymmetric **binary** perceptron result is a different model. This is bounded dated evidence, not a worldwide openness certificate.

## 3. New theorem — deficit-compensated perturbation cost

For a real matrix `A in R^{m x N}` and `kappa<0`, write

`SAT(A,kappa)`

for the existence of `x in S^{N-1}` with

`Ax >= kappa 1_m`.

Let `W in R^{K x m}` have nonnegative entries and row sums

`s_j := sum_i W_{ji} in [0,1]`.

Let `E in R^{K x N}` have rows `e_j`, and define the added block

`B = W A + E`.

For each row define the **free negative-margin budget**

`f_j := (-kappa)(1-s_j)`.

If `s_j>0`, define

`tau_j := ( ||e_j||_2 - f_j )_+ / s_j`.

If `s_j=0`, define `tau_j=0` when `||e_j||_2<=-kappa`, and `tau_j=+infinity` otherwise. Finally put

`tau_* := max_j tau_j`.

### Theorem NM12-DC (sharp deficit-compensated comparison)

For every deterministic `A,W,E` satisfying the hypotheses above and every finite `tau>=tau_*`,

`SAT(A,kappa+tau) subset SAT([A;WA+E],kappa) subset SAT(A,kappa)`.       (3.1)

The right inclusion is exact and pathwise because the augmented system contains the original rows.

The left inclusion has **no probability term** and no dependence on `K`.

### Proof

Let `x in S^{N-1}` satisfy

`Ax >= (kappa+tau) 1_m`.

Because each row of `W` is nonnegative,

`(WAx)_j >= s_j(kappa+tau)`.

Cauchy--Schwarz gives

`e_j . x >= -||e_j||_2`.

Therefore

`b_j . x - kappa`
` >= s_j(kappa+tau) - ||e_j||_2 - kappa`
` = s_j tau - [ ||e_j||_2 - (-kappa)(1-s_j) ]`.             (3.2)

If `s_j>0`, the definition of `tau_j` makes the final line nonnegative whenever `tau>=tau_j`. If `s_j=0`, the same conclusion is exactly the condition `||e_j||_2<=-kappa`. Hence every added row is satisfied. This proves the left inclusion. QED.

### Exact improvement over the earlier project theorem

The earlier deterministic row-augmentation theorem used the cruder sufficient condition

`SAT(A,kappa+epsilon) -> SAT([A;WA+E],kappa)`

with a uniform row bound `||e_j||<=epsilon`, independent of the row-sum deficit `1-s_j`.

The new theorem subtracts the exact free budget already supplied by the negative margin:

`effective row loss = ( ||e_j|| - (-kappa)(1-s_j) )_+ / s_j`.

For `s_j=1` it recovers the old cost `||e_j||`. For `s_j<1` it can be dramatically smaller and can vanish even when `||e_j||` is order one. This is the new quantitative statement; it is not the preceding random signed-affine concentration theorem and uses neither independence nor Gaussian coefficient noise.

## 4. Zero-loss safe hull and idempotent semirandom closure

Setting `tau_*=0` in Theorem NM12-DC gives an exact geometric closure.

For `kappa<0` define

`H_kappa(A) := conv( {a_1,...,a_m} union (-kappa) B_2^N )`,            (4.1)

where `a_i` are the rows of `A` and `B_2^N` is the Euclidean unit ball.

### Corollary NM12-SAFE-HULL

If every added row `b_j` belongs to `H_kappa(A)`, then

`SAT([A;B],kappa) = SAT(A,kappa)`                                  (4.2)

**pathwise, for every finite N and every number K of added rows.**

Indeed, each such row can be written

`b_j = s_j sum_i q_{ji} a_i + (1-s_j) u_j`,

where `q_j` is a probability vector, `s_j in [0,1]`, and `||u_j||<=-kappa`. This is Theorem NM12-DC with

`e_j=(1-s_j)u_j`,

so `||e_j||<=(-kappa)(1-s_j)` and `tau_j=0`.

There is also a direct geometric proof. A core witness `x` has `a_i.x>=kappa` for every core row, while every `u` in `(-kappa)B_2` obeys

`u.x >= -||u|| >= kappa`.

A linear functional preserves the lower bound under convex combinations, so every row in the hull also obeys it.

The closure is **idempotent**:

if `rows(B) subset H_kappa(A)`, then

`H_kappa([A;B]) = H_kappa(A)`.                                      (4.3)

Thus an adaptive semirandom adversary may inspect `A`, add a first batch from the hull, inspect the result, add another batch, and continue for arbitrarily many finite rounds; the feasible set at margin `kappa` never changes. There is no independence assumption and no accumulation of error.

The ball radius is not an arbitrary convenience. It is exactly the set of rows automatically satisfied by every unit vector:

`{u : inf_{||x||=1} u.x >= kappa}`
` = {u : -||u|| >= kappa}`
` = (-kappa) B_2^N`.                                               (4.4)

So the safe-ball component is quantitatively maximal.

## 5. Sharpness of the margin-loss formula

The rowwise loss in Theorem NM12-DC is not merely sufficient; it is optimal for a universal theorem based only on `s_j` and `||e_j||`.

Fix `s in (0,1]`, an error magnitude `E>0`, and a candidate stronger-core margin `kappa+tau`. Suppose

`tau < [E-(-kappa)(1-s)]/s`                                       (5.1)

with positive right side.

Take `N=1`, so the sphere is `{+1,-1}`. Let the core contain two scalar rows

`a_1 = kappa+tau`,

`a_2 = R`,

where `R>|kappa+tau|+1`. At threshold `kappa+tau`, the unique core witness is `x=+1`: row 1 is tight and `x=-1` fails row 2. Choose the added row using weight mass `s` on `a_1` and scalar perturbation `e=-E`. At the unique witness,

`b x = s(kappa+tau)-E`.

Condition (5.1) is exactly

`s(kappa+tau)-E < kappa`,

so the added row kills the only witness. Hence no smaller universal rowwise loss can replace `tau_j`.

For `s=0`, the condition `E<=-kappa` is likewise sharp: if `E>-kappa`, a core forcing `x=+1` and the row `e=-E` destroys feasibility.

This sharpness matters for the application below: the gain is not an artifact of a loose inequality. It comes from spending the exact amount of negative-margin slack that was ignored in the predecessor comparison.

## 6. Concrete unresolved T03 extension with order-one ambient contamination

Consider the following triangular random matrix model at `kappa=-1`.

Let

`m_N=floor(alpha N)`, `K_N=N`,

and let

`A_N in R^{m_N x N}`

have iid standard Gaussian entries. For `j<=N` (which is valid in the T03 density regime `alpha>1`) let `U_j` be iid uniform on the Euclidean unit ball in `R^N`, independent of `A_N`, and define

`r_N := 1/2 + N^{-1/3}`,

`b_j := (1/2) a_j + r_N U_j`.                                    (6.1)

Let `B_N` be the `N x N` matrix with rows `b_j`. The augmented exact-sphere problem is

`A_N x >= -1`,

`B_N x >= -1`,

`||x||_2=1`.                                                     (6.2)

The total number of constraints is `(alpha+1+o(1))N`.

### 6.1 New comparison rate

For every row in (6.1), the coefficient row sum is

`s=1/2`,

and the ambient perturbation satisfies

`||e_j|| <= r_N = 1/2 + N^{-1/3}`.

At `kappa=-1`, the free budget is

`(-kappa)(1-s)=1/2`.

Therefore Theorem NM12-DC gives the **deterministic finite-N sandwich**

`SAT(A_N,-1+2 N^{-1/3})`
` subset SAT([A_N;B_N],-1)`
` subset SAT(A_N,-1)`.                                           (6.3)

There is no exceptional event and no union penalty for the `N` added rows.

The effective margin loss is therefore

`tau_new(N)=2 N^{-1/3}`.                                         (6.4)

By contrast, the predecessor rowwise-error theorem, applied to the **same decomposition**, pays the full error norm

`tau_old(N)=1/2+N^{-1/3}`.                                      (6.5)

Thus this run changes the comparison loss from

`Theta(1)`

to

`O(N^{-1/3})`

while the physical ambient perturbation remains order one.

This is the tracked quantitative theory gain for the run.

### 6.2 The disorder class is genuinely non-Gaussian and the added block is full rank

Conditional on `A_N`, each row `b_j` has an absolutely continuous density on the open ball of radius `r_N/2?` after the affine scaling in (6.1); more directly, because `r_N U_j` has a density on the open ball of radius `r_N`, the row `b_j=(1/2)a_j+r_NU_j` has a translated density on an open set. Hence the joint law of the `N x N` added block has a density conditional on `A_N`, and the determinant-zero hypersurface has Lebesgue measure zero. Therefore

`rank(B_N)=N` almost surely.                                      (6.6)

The added rows are not Gaussian. For one coordinate, write

`X=(1/2)G+r_N U`,

where `G~N(0,1)` and `U` is one coordinate of a uniform unit-ball vector. The exact unit-ball moments are

`E U^2 = 1/(N+2)`,

`E U^4 = 3/[(N+2)(N+4)]`.

Because fourth cumulants add for independent summands and a Gaussian has zero fourth cumulant,

`cum_4(X)`
` = -6 r_N^4 / [(N+2)^2 (N+4)] < 0`.                            (6.7)

So each added row is genuinely non-Gaussian. The augmented collection is also not iid: for the paired Gaussian core row,

`Cov(a_j,b_j) = (1/2) I_N`.                                     (6.8)

The new comparison therefore applies to a dependent Gaussian-plus-bounded-noise random matrix, not an iid Gaussian restatement.

### 6.3 T03 lower endpoint transfers with no asymptotic loss

The project uses the rigorous Montanari--Zhong--Zhou LP-success threshold

`delta_lin(kappa)=1/Phi(kappa)`

for each fixed negative margin in the exact Gaussian normalization.

Fix any

`alpha < 1/Phi(-1)`.

By continuity, choose a fixed `eta>0` such that

`alpha < 1/Phi(-1+eta)`.

For all sufficiently large `N`,

`2N^{-1/3}<eta`.

MZZ gives Gaussian-core feasibility with high probability at the harder fixed margin `-1+eta`; by monotonicity this implies feasibility at `-1+2N^{-1/3}`. The left inclusion in (6.3) then proves augmented feasibility with high probability. Hence the new model inherits the full rigorous T03 lower endpoint

`alpha_L = 1/Phi(-1)=6.302974375068753...`                    (6.9)

in **core density**.

For the upper side, the augmented system contains the full Gaussian core, so every rigorous T03 UNSAT endpoint transfers without loss. Using NM13-07's newest certified source endpoint gives

`alpha_U = 12.31963484`.                                        (6.10)

Therefore the new unresolved model has the core-density bracket

`[6.302974375068753..., 12.31963484]`.                          (6.11)

In total constraint density `lambda=alpha+1`, this is

`boxed: [7.302974375068753..., 13.31963484]`.                  (6.12)

The exact threshold of this dependent non-Gaussian model remains **UNKNOWN**. No continuity of the unknown exact spherical threshold in `kappa` is assumed.

## 7. Quantified application gain relative to the predecessor theorem

This section separates theory/application movement from the original T03 parent.

For the same model (6.1), the predecessor deterministic perturbation comparison would require the Gaussian core at margin

`-1 + (1/2+N^{-1/3})`
` = -1/2 + N^{-1/3}`.

Using the same fixed-margin continuity argument with the MZZ LP theorem, that old route only gives the asymptotic core-density lower endpoint

`1/Phi(-1/2) = 3.241096704566970...`.                         (7.1)

Thus before this run the project theory yields, in total density,

`[4.241096704566970..., 13.31963484]`,

with width

`9.07853813543303...`.

After Theorem NM12-DC, the same concrete model has

`[7.302974375068753..., 13.31963484]`,

with width

`6.016660464931248...`.

The demonstrated application-width gain is therefore

`boxed: 3.061877670501782...`.                                (7.2)

This is a real bound improvement for one fixed unresolved probability model; it is not a checker metric or a renamed auxiliary constant.

Finite-N comparison rates from the executed checker illustrate the convergence:

- `N=10^3`: old loss `0.6`, new loss `0.2`, shifted LP lower `4.72020069673302`;
- `N=10^6`: old loss `0.51`, new loss `0.02`, shifted LP lower `6.11459761185152`;
- `N=10^9`: old loss `0.501`, new loss `0.002`, shifted LP lower `6.28378795447362`;

while the limit is `6.302974375068753...`.

## 8. Original T03 parent before / after — kept separate

**Before this NM13-12 run:**

`[6.302974375068753..., 12.31963484]`.

**After this NM13-12 run:**

exactly the same bracket.

So the original iid-Gaussian T03 source quantity has **NO NM13-12 MOVEMENT** in this invocation. T03 remains OPEN / PARTIAL.

The demonstrated gain is instead:

1. a sharp finite-N universality/comparison theorem with an exact row-sum-deficit correction;
2. a zero-loss idempotent safe-hull closure valid under fully adaptive semirandom row additions;
3. a concrete dependent non-Gaussian full-rank T03 extension whose provable total-density lower endpoint improves from `4.24109670456...` to `7.30297437506...` while its upper endpoint remains `13.31963484`.

NM13-03's `12.28723` and NM13-07's `12.31643335693...` third-full values remain conditional and are not promoted here. If either becomes rigorous, the right inclusion in (6.3) transfers it immediately to the new model with the same status and a `+1` total-density shift.

## 9. Essential executed checks

Executed artifact:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_deficit_compensated_safe_hull_check.py`

Archived output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_deficit_compensated_safe_hull_check.out`

The checker verifies:

- a planted finite-dimensional instance of the full deficit-compensated theorem;
- zero-loss order-one safe-hull perturbations;
- a one-dimensional sharpness witness below `tau_*`;
- the `Theta(1) -> O(N^{-1/3})` comparison-rate change;
- the MZZ lower-endpoint convergence arithmetic;
- a seeded full-rank added-block realization;
- the strictly negative fourth cumulant proving non-Gaussianity;
- the parent and application bracket arithmetic.

The archived output ends

`ALL_DEFICIT_COMPENSATED_CHECKS_PASS`.

These numerical checks are sanity checks only; the theorem proof is the deterministic argument in Sections 3--5.

## 10. Residual obstruction and next nonduplicating attack

The new theorem fully resolves the row-sum-deficit perturbation mechanism itself. The unresolved issue is the **exact threshold** of the excess-noise model (6.1): (6.3) squeezes it between Gaussian problems at margins separated by `2N^{-1/3}`, but the exact T03 threshold is itself unknown.

A genuinely new next attack should not re-run covariance, singular-value, barycentric, or signed-affine variants. The strongest nonduplicating direction is to prove a quantitative continuity modulus in the margin for a rigorous T03 UNSAT certificate (or for the third-full directed-interval certificate once NM13-03/NM13-07 close it). Such a modulus would convert the vanishing `2N^{-1/3}` sandwich into a two-sided finite-N robustness statement for *replacement* rather than augmentation disorder.

No historical or peer file, shared ledger, schedule, permission, workflow, email, Drive resource, public post, or paid-compute resource was modified by this worker.

## ledger_delta

- track: `NM13-12 / progress-universality`
- parent: `T03 negative spherical perceptron, iid Gaussian, kappa=-1, exact sphere`
- parent_metric: `rigorous threshold bracket`
- parent_before: `[6.302974375068753..., 12.31963484]`
- parent_after: `[6.302974375068753..., 12.31963484]`
- parent_movement: `NO MOVEMENT BY NM13-12`
- theory_metric: `effective stronger-core margin loss for s=1/2, ||e||<=1/2+N^(-1/3)`
- theory_before: `1/2+N^(-1/3) = Theta(1)`
- theory_after: `2N^(-1/3) = o(1)`
- theory_status: `COMPLETE AUTHOR-SIDE THEOREM / independent review pending`
- application: `Gaussian T03 core + N dependent non-Gaussian full-rank rows b_j=(1/2)a_j+(1/2+N^(-1/3))U_j`
- application_metric: `rigorous total-density bracket`
- application_before: `[4.241096704566970..., 13.31963484]`
- application_after: `[7.302974375068753..., 13.31963484]`
- application_width_gain: `3.061877670501782...`
- P12_state: `frozen finite-convolution theorem; triangular smooth/B4 without uniform microscopic smoothing remains outside`
- NM13_03_coordination: `12.28723 third-full endpoint CONDITIONAL; entropy/KL compiler consumed only as status`
- NM13_07_coordination: `rigorous T03 upper 12.31963484 consumed; 12.31643335693... waypoint CONDITIONAL`
- posted_exclusions_respected: `yes`
- substantive_artifact: `t03_deficit_compensated_safe_hull_check.py`
- executed_output: `t03_deficit_compensated_safe_hull_check.out; ALL_DEFICIT_COMPENSATED_CHECKS_PASS`
- next_step: `margin-continuity modulus for rigorous UNSAT certificate / two-sided replacement robustness`

# END_NM13_12_2026-09-20T0904Z
