Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but no authenticated applied-model / reasoning-effort receipt is available to this run, so I do not claim otherwise.

# NM13-12 progress-universality — defect-tolerant / quantile radial universality for negative spherical perceptrons

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12`  
Progress root: `proofnet24/NM13-12/progress-universality/`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
Parent: T03 negative spherical perceptron at `kappa=-1`  
Status: **PARTIAL / NEW THEOREM PROVED / STRICT UNIVERSALITY-CLASS AND RATE GAIN / ORIGINAL T03 BRACKET UNCHANGED**

## 1. Compact handoff, latest P12 correction, and exact source hypotheses

The previous NM13-12 run proved a pathwise all-row radial-margin sandwich. For `X=SY`, `S=diag(s_a)`, and `1-delta <= s_a <= 1+delta`, it showed for `kappa<0`

`SAT(Y,kappa/(1+delta)) subset SAT(X,kappa) subset SAT(Y,kappa/(1-delta))`,

then used Gaussian radius concentration to transfer the current rigorous T03 bracket to iid fixed-radius spherical rows with an all-row margin distortion `O(sqrt(log N/N))`. It also gave an exact Rademacher obstruction showing that blanket centered variance-one iid-entry universality is false at `kappa=-1`.

This run does **not** repeat that theorem. It removes the all-row lower-radius hypothesis on the UNSAT side: only a sufficiently large quantile of rows must have radius above a threshold. Consequently an `o(N)` set of rows may have order-one or even zero radius, something the previous `max_a |s_a-1| -> 0` theorem cannot tolerate.

A continuity correction is also needed. The latest retained P12 report is not the earlier `06-25-12Z` checkpoint but

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T07-17-16Z__run-report.md`.

Its mathematics is frozen exactly as follows. For `F in {R,C}`, `d_R=1`, `d_C=2`, let `A_m` have iid centered variance-one entries with density `f_m`. Assume one fixed `q>=1` and one fixed `M<infinity` such that

`sup_m ||f_m^{*q}||_infinity <= M`,

`N_m/m -> gamma>1`,

`k_m=r_m+1`,

`k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`.

There is **no fourth-moment assumption** and no positive-moment assumption beyond variance normalization. The latest P12 report explicitly leaves arbitrary triangular smooth/bounded-fourth-moment laws **without a uniform microscopic finite-convolution smoothing condition** outside scope; noncentered universality and complex phase-retrieval stability are also not claimed. P12's remaining frozen obligations are protocol/final-package items, not missing author-side lemmas.

Because `POSTED.md` excludes rediscovery of the row-submatrix papers, kernels, ReLU work and zero-margin/Ising perceptron results, I do not turn that P12 successor into another row-submatrix theorem here. The new theorem below concerns hard feasibility under row-radius defects and is genuinely different from least-singular-value minima.

## 2. Exact T03 parent state and peer coordination

Freeze the source model exactly:

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- seek `sigma` with `||sigma||_2=sqrt(N)`;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`.

Equivalently, with `x=sigma/sqrt(N)`, seek `x in S^{N-1}` satisfying `Gx >= -1`.

The fully certified repository bracket entering and leaving this run is

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`width = 6.48139658710`.

The lower endpoint is the Montanari--Zhong--Zhou LP success threshold after exact normalization. The upper endpoint is the rigorously certified Stojnic-2013 partial-lift/Gordon bound retained by the project.

### NM13-07

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-full2-two-scalar-reduction.md`

reduces complete second-full stationarity to two scalars `(p,B)` and numerically locates an `alpha=12.75` point with positive comparison value, but correctly does not move the source bracket until the required continuum/root enclosure is rigorous.

### NM13-03

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-closed-kernel-miranda-alpha12p75.md`

has now removed the nested conditional-Gaussian/automatic-differentiation obstruction: it derives closed one-dimensional formulas for the needed kernel derivatives and exhibits a robust Poincare--Miranda rectangle at `alpha=12.75`. It labels the endpoint **CANDIDATE_FULL / review-pending finite enclosure**, not certified, because the mesh-to-continuum interval/Taylor step is still missing.

The present route is nonduplicating. I do not touch their second-full stationarity equations or certify their rectangle. Instead I prove a distributional transfer theorem which will consume any future certified T03 upper endpoint automatically.

## 3. New deterministic mechanism: one-sided quantile / trimming comparison

For an `M x N` matrix `A` and `kappa<0`, write

`SAT(A,kappa) := {exists x in S^{N-1}: (Ax)_a >= kappa for every a}`.

Let rows of `Y` be `y_a`, let positive scalars `s_a` be arbitrary, and set `X=SY`, `S=diag(s_1,...,s_M)`.

### Theorem NM12-QRT-1 (defect-tolerant radial comparison)

Fix `kappa<0`.

**Lower/SAT direction.** If `s_a <= u` for every row, where `u>0`, then pathwise

`SAT(Y,kappa/u) subset SAT(X,kappa)`.

**Upper/UNSAT direction.** For any `ell>0`, define

`I_ell={a: s_a >= ell}`.

Then pathwise

`SAT(X,kappa) subset SAT(Y_{I_ell}, kappa/ell)`.

In particular, UNSAT of the selected high-radius subsystem `Y_{I_ell}` at the easier margin `kappa/ell` forces UNSAT of the full scaled system, irrespective of how small the omitted radii are and irrespective of how large any radii are outside the selected lower-radius condition.

### Proof

For the SAT direction, let `x` satisfy `y_a.x >= kappa/u` for all `a`. If `y_a.x>=0`, then `s_a y_a.x>=0>kappa`. If `y_a.x<0`, the inequality `s_a<=u` reverses under multiplication by this negative number, giving

`s_a y_a.x >= u y_a.x >= kappa`.

Thus the same `x` witnesses `SAT(X,kappa)`.

For the UNSAT direction, let `x` witness `SAT(X,kappa)`. For each `a in I_ell`,

`s_a y_a.x >= kappa`, hence `y_a.x >= kappa/s_a`.

Because `kappa<0` and `s_a>=ell`,

`kappa/s_a >= kappa/ell`.

Therefore `x` witnesses `SAT(Y_{I_ell},kappa/ell)`. Contraposition gives the UNSAT implication. QED.

### Exact difference from the predecessor

The predecessor required the **minimum radius over all rows** to satisfy `min_a s_a >= 1-delta` in order to obtain its right-hand inclusion. QRT-1 needs no such minimum. One may discard every row below `ell` and retain only a large enough high-radius subset. This is an assumption-level gain, not a restatement: order-one lower-radius defects are allowed on `o(N)` rows, or on a fixed positive fraction if the remaining density is still above the angular UNSAT threshold.

## 4. Finite-N probabilistic theorem and a quantile capacity formula

Let `theta_a` be iid uniform on `S^{N-1}` and define fixed-radius angular rows

`Y_a=sqrt(N) theta_a`.

Let `S_a>0` be iid and independent of the directions, and set

`X_a=S_a Y_a`.

Fix `ell>0` and write

`p_ell=P(S_a>=ell)`.

Let `K_ell=#{a<=M:S_a>=ell}`. Then `K_ell~Bin(M,p_ell)`.

### Theorem NM12-QRT-2 (finite-N quantile transfer)

For every deterministic integer `m<=M`,

`P[SAT(X,kappa)]`
` <= P[Bin(M,p_ell)<m] + P[SAT(Y^{(m)},kappa/ell)]`,

where `Y^{(m)}` denotes an independent `m x N` fixed-radius spherical matrix.

If `r=m/M < p_ell`, then the first term has the exact Chernoff/KL bound

`P[Bin(M,p_ell)<m] <= exp(-M D(r||p_ell))`,

with

`D(r||p)=r log(r/p)+(1-r)log((1-r)/(1-p))`.

### Proof

On `{K_ell>=m}`, select the first `m` indices satisfying `S_a>=ell`. Their indices are measurable with respect to the radii alone. Since radii and directions are independent, the selected directions remain iid uniform on the sphere. QRT-1 shows that `SAT(X,kappa)` implies SAT of those selected angular rows at `kappa/ell`. Hence

`P[SAT(X,kappa),K_ell>=m] <= P[SAT(Y^{(m)},kappa/ell)]`.

Adding `P(K_ell<m)` proves the first claim. The second is the standard binomial Chernoff bound. QED.

### Asymptotic capacity consequence

Let `U_sph(t)` denote any rigorous fixed-radius spherical UNSAT upper threshold at margin `t`: for every `beta>U_sph(t)`, the `floor(beta N) x N` fixed-radius model is UNSAT with probability tending to one.

Then for any iid radial law independent of direction,

`U_rad(kappa) <= inf_{ell: p_ell>0} U_sph(kappa/ell)/p_ell`.

Indeed, if `alpha > U_sph(kappa/ell)/p_ell`, choose `beta` strictly between `U_sph(kappa/ell)` and `alpha p_ell`, put `m=floor(beta N)`, apply QRT-2, and use the law of large numbers/Chernoff bound for `K_ell`.

Similarly, if `S_a<=u` almost surely and `L_sph(t)` is a rigorous fixed-radius SAT lower threshold, then

`L_rad(kappa) >= L_sph(kappa/u)`

by the pathwise SAT half of QRT-1.

This is a genuine quantitative radial-universality formula: an upper threshold is controlled by an optimizable **radius quantile** rather than the minimum radius.

## 5. Strict rate gain for Gaussian radii: `sqrt(log log N/N)` instead of `sqrt(log N/N)` on the trimmed UNSAT side

For Gaussian rows `g_a=R_a theta_a`, `R_a^2~chi_N^2`, set `S_a=R_a/sqrt(N)`.

The predecessor all-row theorem used

`delta_old = sqrt(12 log N/N)`

to make `max_a |S_a-1|<=delta_old` with polynomially small failure probability for `M=O(N)`.

For QRT-2 we need only that the **fraction** of rows below `1-delta_N` is small. Laurent--Massart gives, for `0<delta<=1`,

`q_N:=P(S_a<1-delta) <= exp(-N delta^2/4)`.

Choose

`delta_new = sqrt(8 log log N/N)`.

Then

`q_N <= (log N)^(-2)`.

Let `B_N` be the number of rows with `S_a<1-delta_new`, and choose

`epsilon_N=1/log N`.

For `M=O(N)`, the binomial Chernoff bound gives

`P(B_N >= epsilon_N M)`
` <= (e q_N/epsilon_N)^(epsilon_N M)`
` <= exp[-(M/log N)(log log N-1)]`.

Thus, with overwhelmingly high probability, at least a `(1-1/log N)` fraction of Gaussian rows have radius at least `1-delta_new`, while the selected-subsystem margin shift is only

`|kappa/(1-delta_new)-kappa|`
` = |kappa| delta_new/(1-delta_new)`
` = O(sqrt(log log N/N))`.

This is a strict quantitative rate improvement over the predecessor's `O(sqrt(log N/N))` all-row distortion, at the explicit cost of discarding at most `M/log N=o(N)` low-radius rows. It is deliberately stated as a **trimmed UNSAT-side** gain; it is not misreported as a new two-sided full-row coupling.

More generally, taking `delta_N=L_N/sqrt(N)` with any `L_N->infinity` and `L_N=o(sqrt(N))` gives

`q_N <= exp(-L_N^2/4) -> 0`.

Hence the quantile mechanism operates at essentially the `omega(1)/sqrt(N)` radius scale.

### Near-optimality of the scale

If instead `delta_N=c/sqrt(N)` for a fixed `c>0`, then the chi-square CLT and delta method give

`sqrt(2)(R_a-sqrt(N)) => N(0,1)`.

Therefore

`P(S_a<1-c/sqrt(N)) -> Phi(-sqrt(2)c)>0`.

So a fixed `c/sqrt(N)` window leaves a positive asymptotic fraction below the cutoff. The `omega(1)/sqrt(N)` scale is therefore the natural threshold for the bad fraction to vanish; the old all-row maximum scale `sqrt(log N/N)` is genuinely stronger than necessary for UNSAT transfer.

## 6. Concrete unresolved probability application: half-radius contamination

Define a triangular, non-Gaussian hard-feasibility model at the exact T03 margin and sphere radius. Let

`theta_a iid Unif(S^{N-1})`, `Y_a=sqrt(N) theta_a`,

and independently

`S_{a,N}=1` with probability `1-rho_N`,

`S_{a,N}=1/2` with probability `rho_N`.

Set `X_a=S_{a,N}Y_a`, and seek `x in S^{N-1}` satisfying

`X_a.x >= -1` for every `a<=floor(alpha N)`.

This is a concrete negative spherical perceptron with lower-radius contamination. Its exact capacity is unresolved.

### Theorem NM12-T03-CONTAM (vanishing order-one defects preserve the current full bracket)

Take

`rho_N = 1/log N`.

Then the model satisfies the same currently rigorous lower/upper threshold statements as the uncontaminated fixed-radius model:

- for every `alpha < 6.30297437506`, SAT probability tends to one;
- for every `alpha > 12.78437096216`, UNSAT probability tends to one.

Thus its current rigorous bracket is

`[6.30297437506, 12.78437096216]`.

### Proof of the lower bound

All scales satisfy `S_{a,N}<=1`. By the SAT half of QRT-1 with `u=1`, every fixed-radius witness at margin `-1` is also a witness for the contaminated matrix at margin `-1`. The predecessor NM13-12 theorem already established the fixed-radius SAT statement for every `alpha<6.30297437506`. Hence the contaminated model is SAT whp throughout the same lower range. QED.

### Proof of the upper bound

Fix `alpha>12.78437096216`. Choose a constant `beta` with

`12.78437096216 < beta < alpha`.

Let `K_N` be the number of unshrunk rows (`S_{a,N}=1`). Since `rho_N->0`,

`K_N/N -> alpha`

in probability, so `P(K_N>=floor(beta N))->1` (Chernoff gives exponentially small failure). Conditional on the radial variables, the directions attached to the unshrunk rows are still iid uniform. Select the first `floor(beta N)` unshrunk rows. If the full contaminated matrix were SAT at `-1`, this selected fixed-radius subsystem would also be SAT at `-1` (here `ell=1`, so there is no margin loss). But the predecessor fixed-radius theorem is UNSAT whp at every `beta>12.78437096216`. Therefore the full contaminated system is UNSAT whp. QED.

### Why the predecessor cannot prove this application

With `M=floor(alpha N)` and `rho_N=1/log N`,

`P(no half-radius row)=(1-rho_N)^M <= exp(-M/log N) -> 0`.

Hence with probability tending to one,

`max_a |S_{a,N}-1| = 1/2`.

The predecessor hypothesis `max_a|S_a-1|->0` therefore fails as strongly as possible. QRT-1/QRT-2 nevertheless recover the same full certified bracket. This is the promised strict distributional-class extension.

## 7. Constant contamination: explicit quantitative bracket

The same mechanism gives a non-vanishing-defect theorem. Fix `rho in [0,1)` and let

`S_a=1` with probability `1-rho`,

`S_a=c` with probability `rho`, for any fixed `0<=c<1`,

independently of iid spherical directions.

Then at `kappa=-1`:

- because `S_a<=1`, the SAT lower endpoint remains at least `6.30297437506`;
- because the unshrunk rows have asymptotic density `(1-rho)alpha`, the UNSAT upper endpoint is at most

`12.78437096216/(1-rho)`.

For the concrete ten-percent contamination case `rho=0.10`, `c=1/2`, this gives

`6.30297437506 <= alpha_c^(10% half-radius) <= 14.204856624622222...`.

No claim of a sharp threshold or equality is made.

## 8. Applied parent claim before/after versus theory gain

### Original T03 Gaussian source claim

Certified before:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

Certified after:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**No source-level T03 movement is claimed.** NM13-03's `12.75` endpoint remains a review-pending candidate until its continuous face/objective enclosure is completed.

### Demonstrated theory gain

Before this run, NM13-12's hard-margin radial transfer required all rows to have relative radius error `o(1)`; for Gaussian rows, an explicit polynomial all-row guarantee used distortion `sqrt(12 log N/N)`.

After this run:

1. UNSAT transfer needs only an angularly unbiased high-radius **quantile**, not a minimum radius;
2. the finite-N error is controlled by an exact binomial/KL term plus the base angular SAT probability;
3. Gaussian radii can be trimmed at distortion `sqrt(8 log log N/N)`, with only `o(N)` rows discarded and exponentially small probability of exceeding the discard budget;
4. the natural trimmed scale is `omega(1)/sqrt(N)`, shown near-optimal by the chi-square CLT;
5. a concrete triangular model with `N/log N` order-one half-radius defects inherits the full current fixed-radius bracket even though `max_a|S_a-1|` stays equal to `1/2` whp.

That is a strict assumption, distributional-class and quantitative-rate improvement.

## 9. Coordination consequence for the `alpha=12.75` candidate

Nothing in QRT-1/QRT-2 depends on the particular numerical upper endpoint. If NM13-03/NM13-07 later complete the missing finite enclosure and rigorously certify `alpha_U=12.75` for the Gaussian source, the predecessor radial theorem transfers that endpoint to fixed-radius disorder under its already-recorded margin-stability step, and the present quantile theorem then gives immediately:

- vanishing half-radius contamination `rho_N->0`: upper endpoint `12.75`;
- constant contamination fraction `rho`: upper endpoint `12.75/(1-rho)`.

This is a future logical consequence only. I do **not** count it as current source movement.

## 10. Essential executed artifact and arithmetic

Executed checker:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_quantile_radial_check.py`

creation commit `2e141b2ff3b290f3e65bbe56360614cb8198e622`.

Archived actual output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_quantile_radial_check.out`

creation commit `df100abb1021b925e64d71d4947470d13eab1963`.

The checker verifies the exact inherited bracket arithmetic, constant-contamination upper bounds, and representative old/new Gaussian radius scales. It ends `ALL_CHECKS_PASS`.

For example, at `N=10^6` it records

`delta_old = 0.01287579615773608`,

`delta_new = 0.004583266882454925`,

ratio `0.3559598821...`,

with `q_N <= 0.0052392138...` and an extremely small Chernoff bound for exceeding the `1/log N` discard budget. These numerics illustrate the proved formulas; they are not substitutes for the analytic theorem.

## 11. Bounded literature check — 20 September 2026

Fresh primary-source search reconfirmed:

- El Alaoui--Sellke, arXiv:2010.15811, studies the exact Gaussian-disorder spherical perceptron on radius `sqrt(N)`; its negative-margin algorithmic result does not give the exact full-radius threshold.
- Stojnic, arXiv:2312.16531, develops fully lifted RDT for the negative spherical perceptron and states that practical operation requires substantial numerical work.
- A bounded search for non-Gaussian/radial-disorder negative spherical-perceptron universality did not recover a theorem matching the defect-tolerant quantile statement above. This is bounded negative evidence only, not a worldwide novelty certificate.

No posted row-submatrix, kernel, ReLU, or zero-margin Ising claim is reused as new mathematics.

## 12. Residual obstruction and next attack

The original Gaussian T03 bracket remains blocked by certification of a stronger Gaussian upper comparison (currently the `12.75` candidate). The present worker should not duplicate NM13-03/NM13-07's interval-enclosure job unless their route stalls.

The next nonduplicating universality attack is to remove **independence between radii and directions** in QRT-2 by replacing exact angular preservation under radial selection with a quantified conditional angular-bias hypothesis, for example a total-variation or likelihood-ratio bound on `Law(theta | S>=ell)` versus uniform sphere. A successful theorem would turn radial/angular dependence into an explicit additive error and enlarge the universality class beyond elliptical radial mixtures.

No historical/peer file, root ledger, schedule, permission, workflow, email/Drive object, public surface, or paid-compute resource was modified.

```yaml
ledger_delta:
  worker: NM13-12
  parent: T03
  target: "negative spherical perceptron hard-feasibility universality"
  status: "PARTIAL / NEW QUANTILE-RADIAL THEOREM PROVED / ORIGINAL T03 OPEN"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
  source_metric:
    quantity: "certified Gaussian T03 threshold bracket"
    before:
      alpha_L: "6.30297437506"
      alpha_U: "12.78437096216"
      width: "6.48139658710"
    after:
      alpha_L: "6.30297437506"
      alpha_U: "12.78437096216"
      width: "6.48139658710"
    movement: "none"
  theory_gain:
    predecessor_assumption: "all-row min/max radial control; max_a |S_a-1| -> 0"
    new_assumption: "UNSAT transfer through any angularly unbiased high-radius quantile; low-radius defects may be omitted"
    finite_N_bound: "P[SAT(X,kappa)] <= P[Bin(M,p_ell)<m] + P[SAT(Y^m,kappa/ell)]"
    gaussian_old_margin_scale: "sqrt(12 log N/N) for all-row control"
    gaussian_new_trimmed_scale: "sqrt(8 log log N/N), more generally omega(1)/sqrt(N)"
    dropped_rows: "at most M/log N in explicit specialization with exponentially small overflow probability"
  concrete_application:
    model: "iid spherical directions, row scale 1 w.p. 1-1/log N and 1/2 w.p. 1/log N, kappa=-1"
    prior_max_radius_theorem_applies: false
    proved_lower: "6.30297437506"
    proved_upper: "12.78437096216"
    status: "same current bracket despite order-one defects on N/log N rows"
  constant_contamination_example:
    rho: "0.10"
    c: "0.5"
    lower: "6.30297437506"
    upper: "14.2048566246222222222222222222"
  p12_recovery:
    latest_report: "2026-09-17T07-17-16Z__run-report.md"
    frozen_hypotheses: "centered variance-one iid densities; fixed q,M with sup ||f_m^{*q}||_inf<=M; N_m/m->gamma>1; k_m log m=o(m)"
    fourth_moment_required: false
    unresolved_successor: "triangular smooth/B4 iid-entry universality without uniform microscopic finite-convolution smoothing"
  coordination:
    NM13-03: "closed one-dimensional kernel; alpha=12.75 Miranda candidate remains continuum-enclosure pending"
    NM13-07: "exact two-scalar second-full reconstruction retained; no duplication"
    consequence_if_12p75_certified: "quantile theorem propagates it to vanishing contamination and to constant rho with upper 12.75/(1-rho)"
  artifacts:
    checker: "artifacts/t03_quantile_radial_check.py"
    output: "artifacts/t03_quantile_radial_check.out"
    output_status: "ALL_CHECKS_PASS"
  next_attack: "dependent radius-direction quantile transfer via quantified conditional angular bias"
```
