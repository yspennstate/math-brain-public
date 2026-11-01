Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. SUCCESSOR-ADMISSION HOLD: `E_ready: 0 -> 0`; I0076 remains RETIRED-HANDOFF at `2/4`, I0124 remains RETIRED-HANDOFF with `H_288=112`. Methods used: #4 PROVE SOMETHING WEAKER COMPLETELY, #6 DEFORM TO A SOLVABLE POINT, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# R15 CLOSABLE OUTSIDE — successor-admission / D0039 spectral-measure screen

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did not reopen Burdzy--Scheutzow Problem 7.2. Its six-run handoff remains controlling: the source-matching positive-route metric is frozen at `2/4`, with the random-time independence hypothesis interpreted literally as independence of the two complete centered half-paths at an arbitrary finite random time; no deterministic-time substitute, no stopping-time strengthening, and no Problem 7.5 work is introduced here.

I also did not reopen I0124. The newest R15 report is

`runs/R15/20260917_1857Z_i0124_sixrun_handoff_games_h38.md`

and it corrects the stagnation history: I0124 had already accumulated six unchanged runs after the metric reached `H_288=112`. Its proved interval is `236 <= c_{7,3} <= 285`, and it is now `PARTIAL / RETIRED-HANDOFF / SUCCESSOR_ADMISSION_REQUIRED`. The Games-graph reduction in that handoff is preserved for a future reassigned owner; this run does not attack it.

Before screening I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the NEW-METHODS implementation area, the newest R15 handoff, current ownership claims, the latest task-health queue/admission update, and neighboring successor-admission reports. The freshest coordinator admission pass still reports no newly established `READY + CLOSABLE + UNASSIGNED` row after source, current-literature, later-author/citing-paper, ownership and finite-route checks. I therefore screened a source-corrected row that is conspicuously absent from the old READY reserve rather than recycling an already rejected queue item.

## 2. Admission metric

There is no active mathematical source, so I do not invent a theorem metric before a lawful claim exists.

For this admission-only run define

`E_ready := number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded screen.`

Before: `E_ready = 0`.  
After: `E_ready = 0`.

No source claim is created.

## 3. Candidate D0039 — Virag Question 1 is genuinely open-looking, but not yet CLOSABLE

### Exact outside source

Bálint Virág, *Operator limits of random matrices*, ICM 2014 / arXiv:1804.06953, Question 1 in Section 4. The source constructs the semi-infinite beta-Hermite Jacobi matrix `J_beta` and its spectral measure `mu_beta` at the first coordinate. Breuer--Forrester--Smilansky give Hausdorff dimension `(1-2/beta)^+`, and Virág asks:

> Does the beta-Hermite measure and the Gaussian multiplicative cascade measure with the same Hausdorff dimension have the same fractal spectrum?

I checked the source page itself rather than relying on the intake summary.

### Why the old exclusion is wrong

The repository's `probability_1000_intake_D_20260908/CORRECTIONS.md` already records the key correction: Chhaibi--Najnudel's theorem is for the **circular** beta ensemble / OPUC spectral measure, while Virág's Question 1 names the **beta-Hermite** measure on the real line. Their 2026 JEMS paper proves an exact circular GMC identification and explicitly says it answers Virág's question for the random measure constructed from CbetaE; it does not identify the beta-Hermite Jacobi spectral measure with GMC. This distinction survives a fresh 2026-09-17 bounded search.

No canonical `operations/claims/D0039.md` exists at the checked master snapshot. Thus D0039 is ownership-clear in the narrow canonical-claim sense, but ownership clearance alone is not enough to dispatch it.

### Fresh current-status / later-literature screen

Queries run 2026-09-17 included exact combinations of `beta-Hermite`, `fractal spectrum`, `spectral measure`, `Gaussian multiplicative chaos`, Virág Question 1, and later work by Virág/Najnudel/Chhaibi/Breuer/Forrester. The search recovered:

- Breuer--Forrester--Smilansky, *Random discrete Schrödinger operators from Random Matrix Theory* (2007): spectral type transition and the Hausdorff-dimension input, not a full multifractal spectrum;
- Alberts--Normand, *Dimension Results for the Spectral Measure of the Circular Beta Ensembles* (Ann. Appl. Probab. 2022): a process-level large-deviation principle for Jitomirskaya--Last norms in the **circular** model;
- Chhaibi--Najnudel, *On the circle, Gaussian multiplicative chaos and Beta ensembles match exactly*, JEMS 28 (2026), 1--77: exact GMC/CbetaE identification on the circle;
- later Hermite-beta work on corners, bead processes and finite-size statistics, but no source-matching beta-Hermite multifractal-spectrum theorem.

This is bounded negative dispatch evidence, not a worldwide novelty certificate.

## 4. #6 DEFORM TO A SOLVABLE POINT — the circular model reveals the missing object

The closest solved deformation is not `beta -> infinity`; it is **Hermite Jacobi -> circular OPUC**. In the circular model, the random Verblunsky coefficients make logarithms of orthogonal-polynomial norms into sums of nearly independent increments. Alberts--Normand prove a process-level LDP for those sums and then pass through the Jitomirskaya--Last norm. Chhaibi--Najnudel go further and identify the resulting random spectral measure with GMC exactly.

The beta-Hermite analogue therefore has a concrete target rather than a vague "transfer the proof": one needs a process-level large-deviation theorem for the real-line transfer matrices / orthogonal-polynomial norm attached to the independent Jacobi coefficients of `J_beta`, at logarithmic scale, strong enough to convert atypical polynomial growth into local spectral-mass exponents.

The source's one-number Hausdorff dimension is exactly what survives if one keeps only the typical growth exponent. The full fractal spectrum requires the atypical-growth rate function.

**Outcome of move #6:** the circular proof supplies the correct missing *type* of theorem, but not a finite/short transfer. The real-line Prüfer/Jitomirskaya--Last conversion and energy-uniform control are genuine analytic obligations. D0039 is therefore not promoted to CLOSABLE on the strength of the circular theorem.

## 5. #28 REPLACE FOR ALL WITH FOR TYPICAL — why the known dimension result is insufficient

For beta > 2, write

`d = 1 - 2/beta`.

The beta-Hermite spectral measure and the comparison lognormal cascade have been matched only at the level encoded by `d`: their typical local dimension / Hausdorff dimension. In standard one-dimensional lognormal-GMC normalization, matching this dimension corresponds to intermittency satisfying `gamma^2/2 = 1-d = 2/beta`; the predicted GMC spectrum is the parabola

`f_d(alpha) = 1 - (alpha - (2-d))^2 / (4(1-d))`

on its nonnegative range. Equivalently, after substituting `d=1-2/beta`,

`f_beta(alpha) = 1 - (beta/8) (alpha - 1 - 2/beta)^2`.

This formula is recorded here as the **comparison target under the standard GMC normalization**, not as a proved beta-Hermite theorem.

At a point sampled from the measure itself the typical exponent is `alpha=d`, and `f_d(d)=d`, so the old Hausdorff-dimension theorem tests only one point on the whole parabola. That explains structurally why reproducing `(1-2/beta)^+` cannot answer Virág's question: the source asks for all exceptional level sets, not merely the typical exponent.

**Outcome of move #28:** the simplest honest restricted theorem is to prove the beta-Hermite local-dimension LDP near its typical exponent with the same quadratic second-order rate as the circular/GMC model. That would be a strong PARTIAL result, but it would still not be source closure unless upgraded to the full level-set spectrum.

## 6. #4 PROVE SOMETHING WEAKER COMPLETELY — the first plausible theorem and why it is still not a dispatch certificate

A clean weaker target suggested by the two moves above is:

> For one fixed bulk energy `E`, prove that the logarithmic growth variable controlling the beta-Hermite Jitomirskaya--Last norm satisfies a speed-`log n` LDP with the same quadratic rate function as the circular beta spectral measure, at least in a neighborhood of its zero.

This is substantially stronger than a CLT and would expose whether the Hermite and circular multifractal mechanisms really coincide before attempting a global energy-uniform theorem.

Breuer--Forrester--Smilansky's setup makes this plausible: the beta-Hermite Jacobi coefficients are independent and their fluctuations are of the critical `n^{-1/2}` type, so logarithmic transfer-matrix growth accumulates on a `log n` scale. But unlike the circular case, the increments of the logarithmic polynomial norm are not independent scalar functions of one coefficient; the Prüfer phase feeds back into the next increment. The missing ingredient is therefore a **joint phase/amplitude LDP or exponential-equivalence reduction** that removes the phase without losing the logarithmic-speed rate function.

I found no source in the bounded search that supplies exactly that reduction for `J_beta`.

**Outcome of move #4:** this is a concrete research theorem worth assigning in a HARD/RMT lane, but it is not a CLOSABLE OUTSIDE target under the owner's current contract. A one-hour finite certificate is not visible, and even success at one energy remains PARTIAL relative to the full fractal-spectrum question.

## 7. Two nearby candidates rejected without recycling old work

### D0034 — Bradley Question 6

Bradley's survey asks whether there exists a strictly stationary psi-mixing (perhaps even 1-dependent) sequence that is not the instantaneous function of any stationary Harris recurrent Markov chain. The canonical claim path is absent at the checked snapshot and a bounded search did not reveal a source-matching later resolution. But a proof must certify non-representability against **every** Harris recurrent Markov chain; no finite witness or short analytic invariant was found. This is open-looking but HARD, not CLOSABLE.

### D0040 — Virag Question 2 / nested beta models

The intake's historical attempt treats independent tridiagonal/CMV parameters as the mechanism for nesting. Current literature contains extensive beta-corners processes, including Laguerre-beta multilevel models and the July 2026 perturbed beta-corners construction. That makes the old source-status boundary nontrivial: part of the broad "any other natural models?" question is now covered by later multilevel constructions, while an exact classification remains broad. A source-clean dispatch would first have to decide precisely which later corners processes satisfy Virág's **same nesting coupling** rather than merely sharing lower-level marginals. That scope reconciliation is not a one-step research closure, so D0040 is not promoted.

## 8. Admission conclusion

The useful new information is not another checker. D0039 is **genuinely open-looking after correcting the circular/Hermite conflation**, and the nearest solved circular work identifies the missing analytic object: a logarithmic-speed, process-level large-deviation principle for the beta-Hermite transfer-matrix/Jitomirskaya--Last norm, followed by a level-set conversion. That is a serious route, but it is theorem-sized and still leaves an energy-uniform multifractal argument. It therefore fails the current CLOSABLE admission gate.

D0034 is also open-looking but has an all-Harris-chain universal obstruction. D0040 needs source-scope reconciliation against later beta-corners literature. None is honestly `READY + CLOSABLE + UNASSIGNED`.

R15 remains `SUCCESSOR_ADMISSION_REQUIRED`. Do not reopen I0076 or I0124 on the next run. Continue beyond the already-screened Bradley/Virág cluster and prefer a source statement whose full logical quantifiers can be closed by one finite construction/counterexample or one short exact analytic argument.

Suggested fresh methods for the next admission pass: **#7 TAKE THE LIMIT, #16 COMPUTE EVERY SMALL CASE, #26 HUNT THE SPORADIC CASE**.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE OUTSIDE
  active_source: NONE
  retired_preserved:
    I0076:
      source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2"
      status: "OPEN / PARTIAL / RETIRED-HANDOFF"
      metric: "source-matching obligations = 2/4"
      unchanged_count: 6
    I0124:
      source: "Thackeray, cap set problem in AG(7,3)"
      status: "PARTIAL / RETIRED-HANDOFF"
      metric: "H_288 = 112"
      source_interval: "236 <= c_{7,3} <= 285"
      unchanged_count: 6
  admission_gate:
    metric: E_ready
    before: 0
    after: 0
  methods: [4, 6, 28]
  screened:
    D0039:
      status: "OPEN-looking after corrected circular/Hermite literature scope"
      ownership: "no canonical operations/claims/D0039.md at checked snapshot"
      disposition: "HARD analytic multifractal/LDP transfer; NOT CLAIMED"
      nearest_solved: "circular beta spectral measure / GMC"
      remaining_obligation: "real-line transfer-matrix process LDP + Jitomirskaya--Last/local-mass conversion + full level-set spectrum"
    D0034:
      status: "OPEN-looking"
      disposition: "universal Harris-chain non-representability; HARD; NOT CLAIMED"
    D0040:
      status: "later beta-corners literature creates scope-reconciliation issue"
      disposition: "NOT CLAIMED"
  evidence:
    repository:
      - "runs/R15/20260917_1857Z_i0124_sixrun_handoff_games_h38.md"
      - "probability_1000_intake_D_20260908/CORRECTIONS.md"
      - "probability_1000_intake_D_20260908/batches/b04.json"
      - "latest task-health successor-admission screen at checked master"
    literature:
      - "Virag, arXiv:1804.06953, Question 1"
      - "Breuer--Forrester--Smilansky, 2007"
      - "Alberts--Normand, Ann. Appl. Probab. 2022"
      - "Chhaibi--Najnudel, JEMS 28 (2026), 1--77"
  audit_ids: []
  new_theorem_claims: 0
  new_finite_claims: 0
  checker: none
  claim_created: false
  successor_status: SUCCESSOR_ADMISSION_REQUIRED
  next_methods: [7, 16, 26]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

## 10. Model / scheduler escalation

The limitation is still present in the actually exposed automation interface: it offers title, prompt, schedule/relative start, timing mode and enabled-state controls, but no model-family selector, no reasoning-effort selector, no authenticated applied-model telemetry and no guaranteed hour-long runtime field. Thus `GPT-6 / maximum` is request text only from this worker and cannot be honestly reported as applied.

Making the requirement enforceable needs an authorized product/backend or owner/admin surface that exposes persistent model and reasoning fields **and** returns authenticated runtime metadata. The historical P26 `You cannot modify this task` response is an authorization-context boundary; the lawful workaround is the owning authorized context, a supported ownership/admin change, or platform support. Do not duplicate the task or bypass permissions.

No scheduler or permission mutation is attempted in this run.

## 11. Delivery discipline

Only this immutable R15 report is written. No checker is manufactured because no finite claim moved. No shared root, queue, claim, peer-track file, email, Drive item, public post, purchase, permission, workflow or scheduler setting is modified.
