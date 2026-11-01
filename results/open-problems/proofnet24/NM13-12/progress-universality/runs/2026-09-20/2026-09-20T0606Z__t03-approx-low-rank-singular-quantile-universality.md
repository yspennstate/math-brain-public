Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-12 — singular-quantile universality for full-rank heavy-tailed constraint contamination

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Owner policy: `operations/PROGRESS20_2026-09-20.md` and current LIVE20 mapping  
Worker: `NM13-12` / `progress-universality`  
Applied parent: **T03 negative spherical perceptron, kappa=-1, exact unit sphere**  
Status: **PARTIAL / NEW FINITE-N THEOREM / NEW FULL-RANK CONTAMINATION APPLICATION / ORIGINAL T03 REMAINS OPEN**

## 1. Compact predecessor and P12 handoff

The latest canonical P12 report is

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its frozen mathematical theorem is unchanged. For `F in {R,C}`, centered variance-one iid entries with densities `f_m`, one fixed integer `q>=1` and one finite constant `M` such that

`sup_m || f_m^{*q} ||_infty <= M`,

with

`N_m/m -> gamma > 1`, `k_m=r_m+1`, and `k_m log m=o(m)`,

one has

`(k_m/m) log M^F_{m,r_m}(A_m) -> -h(gamma)/d_F` in probability,

where `d_R=1`, `d_C=2`.

There is **no fourth-moment assumption and no positive-moment assumption above variance normalization**. Fixed bounded-density laws are included by `q=1`. The explicit mathematical successor still outside that theorem is triangular smooth / bounded-fourth-moment universality **without** a uniform microscopic finite-convolution smoothing condition. P12 itself is mathematically frozen and protocol-open only because an independent audit remains missing.

This run does not reopen or repackage the posted row-submatrix theorem, mesoscopic-spike work, kernel result, ReLU work, or zero-margin/Ising perceptron work.

The immediate NM13-12 predecessor proved a finite-N theorem for an arbitrary extra constraint block `B` satisfying the **exact** structural condition `rank(B)<=r`: intersect the Gaussian-core favorable spectral subspace with `ker(B)`, losing at most `r` dimensions. The concrete predecessor application allowed very heavy-tailed rows but only because their total row span was exactly low rank.

The new theorem below replaces the exact-nullspace requirement by a **singular-value quantile**. It allows `B` to have full ambient rank and permits a fixed nonvanishing residual singular scale all the way up to the hard negative-margin budget.

## 2. Current T03 parent state and peer coordination

The source model remains exact:

`M=floor(alpha N)`, independent standard Gaussian row vectors, `x in S^{N-1}`, and `Gx >= -1` coordinatewise.

The latest relevant peer state on current master is:

1. `NM13-07` has a directed whole-box interval-contraction certificate for the complete second-full lift at `alpha=12.75`, with positive comparison value on the entire certified box. Its report promotes the exact-sphere source upper endpoint to `12.75`, pending later independent full-scope review.
2. `NM13-03` proves a stationary-branch comparison-value transport theorem and supports a much stronger `12.33` candidate, but correctly leaves the outward continuum enclosure pending; `12.33` is not consumed here as a rigorous endpoint.
3. The newest `PROB10-03` / R14 run then uses the already-certified NM13-07 box without recomputing Gaussian integrals. Because shifting the target density changes only the constant second residual while leaving the Jacobian unchanged, an exact rational contraction calculation moves the worker-rigorous source endpoint to

`alpha_U = 12.749999921749`.

It records source width `6.447025546689` against the repository lower endpoint `6.30297437506`, with independent full-scope validation still pending.

This NM13-12 route does **not** duplicate the two-scalar stationarity, interval quadrature, or stationary transport work. It consumes the best currently recorded source endpoint only after proving a separate singular-quantile comparison theorem.

## 3. New theorem — approximate-low-rank singular-quantile contamination

For `kappa<0`, let `G` be an `m x N` standard Gaussian matrix. Let `Sigma` be deterministic positive definite, and let `B` be a `K x N` matrix independent of `G` (deterministic is allowed). Define the joint spherical feasibility event

`SAT(G Sigma^{1/2}, B; kappa)`

by existence of `x in S^{N-1}` such that simultaneously

`G Sigma^{1/2} x >= kappa * 1_m`,

`B x >= kappa * 1_K`.

Write singular values of `B` as

`s_1(B) >= ... >= s_N(B) >= 0`,

padding by zeros if necessary. Let `E` be a `d_0`-dimensional spectral subspace of `Sigma` on which

`Sigma|_E <= u I_E`.

Equivalently it suffices that the `d_0`-th smallest eigenvalue satisfies `lambda_{d_0}(Sigma)<=u`. Fix `0<=r<d_0`.

### Theorem NM12-SQ

If

`s_{r+1}(B) <= beta <= -kappa`,

then, conditional on every such `B`,

`P_G{ SAT(G Sigma^{1/2}, B; kappa) }`

`    >= p_iso(m, d_0-r, kappa/sqrt(u))`,                                  (3.1)

where `p_iso(m,d,t)` is the exact spherical feasibility probability for an `m x d` standard Gaussian matrix at margin `t`.

If additionally `lambda_min(Sigma)>=ell>0`, then

`P_G{ SAT(G Sigma^{1/2}, B; kappa) }`

`    <= p_iso(m,N,kappa/sqrt(ell))`.                                      (3.2)

If `B` is random, independent of `G`, and

`P{s_{r+1}(B)<=beta} >= 1-eta`,

then the right side of (3.1) is multiplied by `1-eta`.

### Proof of the lower comparison

Take a singular value decomposition of `B`. The span `K_B` of the right singular vectors corresponding to indices `r+1,...,N` has dimension at least `N-r`, and for every `x in K_B`,

`||Bx||_2 <= s_{r+1}(B) ||x||_2 <= beta ||x||_2`.                         (3.3)

Intersect with the favorable covariance subspace:

`F := E intersect K_B`.

The dimension inequality gives

`dim F >= d_0-r`.

Choose an `N x d` orthonormal matrix `Q`, `d=d_0-r`, whose columns lie in `F`. Put

`C := Q^T Sigma Q`.

Since `Q` lies in `E`,

`0 < C <= u I_d`.                                                         (3.4)

For every unit `v in R^d`, `x=Qv` is unit and (3.3) implies

`(Bx)_j >= -||(Bx)||_infty >= -||Bx||_2 >= -beta >= kappa`                (3.5)

for every contaminant constraint. Thus **all contaminant inequalities are automatic** on this `d`-dimensional sphere.

Conditional on `B`, Gaussian rotational invariance gives

`G Sigma^{1/2} Q  =_law  H C^{1/2}`,                                     (3.6)

where `H` is an `m x d` standard Gaussian matrix.

Now suppose a unit vector `y` satisfies

`H y >= (kappa/sqrt(u)) 1_m`.                                             (3.7)

Set

`t=||C^{-1/2} y||_2`, `v=C^{-1/2}y/t`.

Then `||v||=1`. From `C<=uI`,

`t >= 1/sqrt(u)`.                                                         (3.8)

Because `kappa<0`, (3.8) reverses the useful sign:

`kappa t <= kappa/sqrt(u)`.

Hence (3.7) implies `Hy >= kappa t`, and therefore

`H C^{1/2} v = Hy/t >= kappa 1_m`.                                        (3.9)

Combining (3.5), (3.6), and (3.9) proves (3.1).

### Proof of the upper comparison

Joint feasibility implies feasibility of the Gaussian core after discarding the `B` constraints. If `x` is a core witness, let

`y=Sigma^{1/2}x`, `t=||y||_2`, `z=y/t`.

The lower spectral floor gives `t>=sqrt(ell)`. Therefore

`Gz = G Sigma^{1/2}x/t >= (kappa/t)1_m >= (kappa/sqrt(ell))1_m`,

where the last inequality again uses `kappa<0`. This yields (3.2).

For random `B`, condition on `B`, use (3.1) on the singular-quantile event, and average. QED.

## 4. Exact assumption gain and why it is strict

The predecessor theorem required

`s_{r+1}(B)=0`.

The new theorem permits

`s_{r+1}(B) <= -kappa`.

Thus the allowable residual singular scale improves from exactly zero to the **entire negative-margin budget**. At T03's `kappa=-1`, the theorem accepts `s_{r+1}(B)<=1`, a fixed order-one error that need not vanish with dimension.

This is not a cosmetic closure of the rank condition. A matrix can have `rank(B)=N` while `s_{r+1}(B)<=1`, and the theorem then gives the same asymptotic dimension loss `r` as if `B` had an exact `N-r` dimensional kernel.

The margin budget is sharp for a universal theorem of this form. Take `N=1`, `kappa=-1`, `r=0`, and the one-row contaminant `B=[beta]` with `beta>1`. The contaminant forces the only feasible spherical sign to be `x=+1`. With one Gaussian core row `g`, the core alone is always feasible on `S^0={-1,+1}`, but the joint system is feasible only when `g>=-1`, an event of probability `Phi(1)=0.841344746...<1`. Hence no universal same-margin lower comparison can replace the condition `beta<=1` by an arbitrary larger constant.

## 5. Concrete unresolved application — full-rank Cauchy contamination of T03

This application is deliberately chosen so that the predecessor exact-rank theorem **cannot** apply.

Let

`r_N=floor(N^{2/3})`.

Let `R_N` be an `N x r_N` matrix with orthonormal columns. Let `C_N` be an `N x r_N` matrix with iid standard Cauchy entries, independent of the Gaussian core, and define an `N x N` contaminant block

`B_N := C_N R_N^T + I_N`.                                                 (5.1)

The low-rank part has rank at most `r_N`. By the min-max characterization / Eckart--Young inequality,

`s_{r_N+1}(B_N) <= ||B_N-C_NR_N^T||_op = ||I_N||_op = 1`.                 (5.2)

At `kappa=-1`, (5.2) is exactly the maximal admissible singular-quantile budget in Theorem NM12-SQ.

At the same time `B_N` is **full rank almost surely**. Indeed `det(I_N+C_NR_N^T)` is a nonzero polynomial in the entries of `C_N`: at `C_N=0` it equals `1`. Since the Cauchy law has a product density, the zero set of this nonzero polynomial has probability zero. Therefore

`rank(B_N)=N` almost surely.                                               (5.3)

The rows are heavy tailed and no finite first or second moment is assumed or used for the contaminant block.

Now define the mixed perceptron with total constraint density `alpha` as follows:

- Gaussian core: `m_N=floor((alpha-1)N)` independent standard Gaussian constraints;
- contaminant block: the `N` inequalities `B_N x >= -1`;
- witness: exact unit sphere `x in S^{N-1}`.

The exact threshold of this mixed model is **UNKNOWN**.

### SAT side

By (5.2), Theorem NM12-SQ with `Sigma=I`, `u=1`, and `d_0=N` yields

`P{mixed SAT} >= p_iso(m_N,N-r_N,-1)`.

Because `(N-r_N)/N -> 1`,

`m_N/(N-r_N) -> alpha-1`.

The rigorous Gaussian lower endpoint used by the project is

`alpha_L = 1/Phi(-1) = 6.302974375068753...`.

Therefore, for every fixed

`alpha < 1 + alpha_L = 7.302974375068753...`,

the mixed full-rank heavy-tailed system is SAT with probability tending to one.

### UNSAT side

Discarding the contaminant constraints can only make feasibility easier. Hence if the Gaussian core alone is UNSAT, the mixed system is UNSAT.

The newest current worker-rigorous T03 source endpoint on master is

`alpha_U = 12.749999921749`,

obtained by the exact R14 parametric contraction shift of the NM13-07 certified box. Consequently, for every fixed

`alpha > 1 + alpha_U = 13.749999921749`,

the mixed system is UNSAT with probability tending to one, subject to the same later independent-review caveat as that inherited source endpoint.

Thus the new concrete unresolved model has the rigorous project-supported transition window

`7.302974375068753... <= alpha_c^mix <= 13.749999921749`.                 (5.4)

Its exact threshold remains unknown. Equation (5.4) is a theorem-level application of the new singular-quantile mechanism, not a claim that the mixed threshold equals either endpoint.

## 6. Demonstrated theory gain versus original-parent movement

### Original T03 parent quantity

This NM13-12 run does **not** move the pure Gaussian source threshold.

Current repository worker-rigorous bracket entering this report:

`[6.30297437506, 12.749999921749]`,

repository-rounded width `6.447025546689`.

After this NM13-12 run: **unchanged**.

The strict `12.75 -> 12.749999921749` source movement belongs to the contemporaneous R14 / PROB10-03 parametric contraction run, not to NM13-12.

### New universality / random-matrix quantity

Tracked theory quantity: largest universal residual singular scale allowed beyond rank `r` while retaining the same hard-margin comparison.

Before this run (exact-rank predecessor):

`beta_max = 0`.

After this run:

`beta_max = -kappa`.

For T03, `beta_max: 0 -> 1`.

The corresponding dimension regime also improves strictly: `B` may now have full ambient rank `N`; only the `(r+1)`-st singular value is controlled. For `r_N=o(N)`, this full-rank defect costs asymptotically zero dimension even at a fixed order-one residual scale.

### Applied mixed-model quantity

Before: no theorem in this namespace supplied a T03 bracket for a full-rank Cauchy-plus-identity contaminant block of the form (5.1); status **UNKNOWN / UNMEASURED**.

After: proved project-supported window (5.4). Unknown was not treated as zero.

## 7. Sanity checker and finite witness

The executed checker

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T0556Z__t03_approx_lowrank_singular_quantile_check.py`

with archived output

`.../2026-09-20T0556Z__t03_approx_lowrank_singular_quantile_check.out`

checks three independent facts:

1. a deterministic `N=5`, `r=2`, `beta=0.9` example has `rank(B)=5` but `s_3(B)=0.9` and restricted operator norm `0.9`, so the new hypothesis is genuinely full rank;
2. the `N=1`, `beta=1.1` sharpness example has joint feasibility probability `Phi(1)=0.841344746068543<1` while the core-alone probability is `1`;
3. the `r_N=N^{2/3}` dimension-loss lower comparison converges to the inherited Gaussian lower endpoint.

The archived output ends `ALL_CHECKS_PASS`.

That first checker was created moments before the newer R14 `12.749999921749` endpoint landed on master and therefore prints the then-current `12.75` upper endpoint. It is preserved immutably rather than overwritten. A second executed arithmetic reconciliation,

`.../artifacts/2026-09-20T0602Z__t03_singular_quantile_endpoint_reconcile.py`

with output

`.../artifacts/2026-09-20T0602Z__t03_singular_quantile_endpoint_reconcile.out`,

uses the current inherited endpoint and records

`MIXED_ALPHA_L 7.302974375068753`,

`MIXED_ALPHA_U 13.749999921749`,

`MIXED_WIDTH 6.447025546680247`,

ending `ALL_ENDPOINT_RECONCILE_CHECKS_PASS`. The small width difference from the repository-rounded pure-source width is solely the extra digits retained in `1/Phi(-1)`.

## 8. Literature boundary and source-exactness

Fresh 20 September 2026 source checks preserve the distinction between the source problem and this extension.

- Montanari--Zhong--Zhou, arXiv:2110.15824, studies the proportional negative perceptron and proves upper/lower bounds on the spherical threshold together with the linear-programming threshold. This is the rigorous Gaussian baseline consumed on the SAT side.
- El Alaoui--Sellke, arXiv:2010.15811, defines the exact Gaussian spherical model on radius `sqrt(N)` and emphasizes the unresolved negative-margin SAT geometry; its algorithmic output uses a smaller `sqrt(qbar N)` sphere and therefore does not replace the exact-radius threshold.
- Stojnic, arXiv:2312.16531, fits the negative spherical perceptron into fully lifted RDT and explicitly notes that practical operation requires substantial numerical work.

A bounded fresh search for negative spherical perceptron results with correlated / low-rank / singular-value contamination did not surface a primary theorem matching (3.1)--(3.2). This is bounded negative evidence only, not a novelty certificate.

## 9. What this is not

This report does not claim:

- a solution of the exact T03 threshold;
- that the mixed-model threshold in (5.4) equals either endpoint;
- that the P12 finite-convolution hypothesis has been removed;
- any new row-submatrix least-singular-value theorem;
- any kernel, ReLU, zero-margin Ising, or posted mesoscopic-spike result;
- an independent audit of NM13-03, NM13-07, or R14.

The new result is the finite-N singular-quantile comparison itself and its full-rank heavy-tailed T03 application.

## 10. Next nonduplicating route

The singular-quantile theorem identifies a sharp next boundary. Its lower comparison spends the entire residual operator budget by the crude coordinatewise implication

`||Bx||_infty <= ||Bx||_2 <= beta`.

A genuinely stronger route would replace the spectral `l2 -> l_infty` worst-case step by a **rowwise delocalized almost-kernel theorem**: prove that a large subspace simultaneously has much smaller `||Bx||_infty` than `||Bx||_2`, permitting `s_{r+1}(B)>-kappa` when the right singular vectors or residual rows are delocalized. That would move the quantitative residual threshold beyond `1` for T03 without touching NM13-03/NM13-07's stationarity calculations.

## 11. Immutable artifact provenance

- main singular-quantile checker creation commit: `47c2315580cc1eb6b7ef6b242db11c1f07c32126`;
- archived main checker output creation commit: `731b779530442ebb746a904b1b6f3dd18d3081ed`;
- current-endpoint reconcile checker creation commit: `0dcb9cc3f4a0095975dcc175b49251a46e091291`;
- archived reconcile output creation commit: `46e3f6e81c92419287052ccf525496649d75ad1d`.

No historical report, peer file, shared root ledger, POSTED item, scheduler, permission, workflow, email, Drive object, paid resource, or public surface was modified.

```yaml
ledger_delta:
  worker: NM13-12
  parent: T03
  status: "PARTIAL / NEW SINGULAR-QUANTILE UNIVERSALITY THEOREM / FULL-RANK CONTAMINATION APPLICATION"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
  p12_state:
    theorem_changed: false
    exact_hypothesis: "centered variance-one iid entries; fixed q; uniform finite-convolution L-infinity ceiling; N_m/m->gamma>1; k_m log m=o(m)"
    fourth_moment_assumption: false
    unresolved_successor: "triangular smooth/bounded-fourth-moment universality without uniform microscopic finite-convolution smoothing"
  parent_source_metric:
    quantity: "pure Gaussian T03 threshold bracket"
    before: "[6.30297437506, 12.749999921749]"
    after: "[6.30297437506, 12.749999921749]"
    movement_by_NM13_12: "none"
    note: "the strict 12.75 -> 12.749999921749 movement belongs to contemporaneous R14/PROB10-03"
  theory_metric:
    quantity: "universal residual singular budget beta_max under rank-r approximation"
    before: "0 (exact rank only)"
    after: "-kappa"
    t03_value: "0 -> 1"
  theorem:
    name: "NM12-SQ"
    finite_N_lower: "p_full >= p_iso(m,d0-r,kappa/sqrt(u)) when s_{r+1}(B)<=beta<=-kappa"
    finite_N_upper: "p_full <= p_iso(m,N,kappa/sqrt(ell)) when lambda_min(Sigma)>=ell"
    random_B_extension: "multiply lower bound by P{s_{r+1}(B)<=beta} under independence from G"
  application:
    model: "Gaussian negative spherical core plus N full-rank Cauchy-low-rank + identity constraints"
    exact_threshold: "UNKNOWN"
    before: "UNMEASURED in this namespace"
    after_lower: "7.302974375068753..."
    after_upper: "13.749999921749"
    contaminant_rank: "N almost surely"
    singular_quantile: "s_{floor(N^(2/3))+1}(B_N)<=1"
  coordination:
    NM13_03: "stationary transport supports 12.33 but outward enclosure remains pending"
    NM13_07: "whole-box interval contraction certifies 12.75 source upper, review pending"
    PROB10_03: "exact parametric contraction shift inherits NM13-07 box and moves worker-rigorous upper to 12.749999921749"
  artifacts:
    checker_commit: "47c2315580cc1eb6b7ef6b242db11c1f07c32126"
    checker_output_commit: "731b779530442ebb746a904b1b6f3dd18d3081ed"
    reconcile_checker_commit: "0dcb9cc3f4a0095975dcc175b49251a46e091291"
    reconcile_output_commit: "46e3f6e81c92419287052ccf525496649d75ad1d"
  residual_obstruction: "replace worst-case l2-to-linfinity control by a delocalized almost-kernel theorem to permit residual singular scale exceeding -kappa"
  next_attack: "rowwise delocalized approximate kernel / restricted l2-to-linfinity comparison, without duplicating T03 stationarity work"
```
