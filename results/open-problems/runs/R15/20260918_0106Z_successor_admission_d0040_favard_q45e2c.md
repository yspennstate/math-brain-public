Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; native I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`, and I0124 remains `PARTIAL / RETIRED-HANDOFF` with `H_288=112`. Methods #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT, #27 SWAP THE QUANTIFIERS.**

# R15 — successor admission: Virag Question 2, source-style nesting versus beta-corners

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity: do not reopen the stale native title

The native scheduler title still names Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958 / PTRF 160 (2014), Problem 7.2, intake I0076. I rechecked the exact source before doing any successor work.

Definition 2.1 says that a continuous process `X=(X_t)_{t in R}` is an FBM if there are random times `S_n -> -infinity` a.s. such that, for every `n`,

`(X_{S_n+t}-X_{S_n})_{t>=0}`

is standard Brownian motion. It is BBM iff its time reversal is FBM. It is 2BM iff there exists a random time `S` such that the centered forward and backward half-paths at `S` are independent standard Brownian motions.

Problem 7.2 assumes `X` is FBM and BBM and that there exists an arbitrary finite random time `T` for which

`F_t=X_{T+t}-X_T`,  `G_t=X_{T-t}-X_T`, `t>=0`,

are independent as complete half-path processes, and asks whether `X` must be 2BM. There is no deterministic-time replacement, no stopping-time hypothesis on `T`, and the source does not separately assume `F` or `G` is Brownian. Problem 7.5 is distinct and excluded.

The controlling I0076 handoff is

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`.

It records six unchanged runs at `2/4` and mandatory retirement/rotation. The old source-Theorem-6.1 FBM+BBM non-2BM candidate was eliminated because R15 proved it has no source-required independent seam. The later alternating Brownian-prefix/BES candidate also failed: it has FBM, BBM and exact seam independence but is actually 2BM after finite-intensity excursion-Palm de-biasing. Thus there is currently **no verified frozen counterexample candidate** carrying the four-obligation metric. The handoff's fresh counterexample architecture is only a proposal: keep the +/-1 exit skeleton honest and put sparse copied-block dependence into the continuous Brownian-cell prefix/BES mark sequence, with independent mark reservoirs at the seam. Its unresolved compatibility is simultaneous exact FBM witnesses, exact BBM witnesses and source-level seam independence. I did not attack that architecture in this run because I0076 is retired pending fresh reassignment.

The subsequent I0124 cap-set target likewise reached its six-unchanged-run handoff and remains retired. R15 is therefore in `SUCCESSOR_ADMISSION_REQUIRED`, not entitled to continue either predecessor.

## 2. Repository continuation and current admission state

Before research I reread/recovered the required fleet state rather than restarting from the stale title:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` and the current task-health delta;
- newest own report `runs/R15/20260917_2358Z_successor_admission_d0019_resolution_n43d1b.md`;
- newest relevant neighboring admission reports, including current R08, R20 and NM13-03 screens;
- current canonical claims for candidates encountered below;
- exact intake/source records rather than treating a missing search hit as permission to claim.

The current root queue still contains many PENDING/HARD rows but no newly certified free target that is simultaneously source-clean, current-open, ownership-clear and honestly `CLOSABLE OUTSIDE`. The latest neighboring CLOSABLE screens likewise found no such free target. I therefore keep the admission metric

`E_ready := number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`.  
After: `0`.

No successor claim is created.

## 3. New screen: D0040 / Virag Question 2 (Nested models)

### Exact source statement

D0040 is Bálint Virág, *Operator limits of random matrices*, ICM Seoul 2014 proceedings / arXiv:1804.06953, Question 2 on p. 6 of the arXiv PDF.

The source first proves Theorem 4.1: there exists a random measure `mu_beta` on `R` such that **for every n**, the zeros of the nth orthogonal polynomial for `mu_beta` have the n-point beta-Hermite eigenvalue law. The construction comes from one semi-infinite Jacobi matrix whose leading principal minors have exactly those zeros as spectra.

Question 2 then asks:

`Can any other Dyson beta-ensembles be coupled this way? How about other natural random matrix models?`

The words **this way** matter. A generic interlacing/corners coupling of level laws is not automatically the source construction. The source construction asks for one random measure, equivalently one Jacobi/Favard recurrence, generating all levels simultaneously.

The historical D0040 intake attempt blurred this distinction by treating independent-entry tridiagonal/CMV models and general beta-corners as if they automatically furnished the same all-level single-measure nesting. The literature now makes that scope issue important, so this run translates the target into an exact invariant.

## 4. Method #18 — say it in another language: exact Favard/Jacobi test

Let an interlacing array have level-n points

`lambda^(n)=(lambda_1^(n),...,lambda_n^(n))`

and define its monic level polynomial

`P_n(x)=prod_{i=1}^n (x-lambda_i^(n))`, with `P_0=1`.

### Proposition (finite source-style nesting criterion; classical Favard/Jacobi mechanism)

For levels `1,...,N`, the array is the sequence of spectra of the leading principal minors of a real Jacobi matrix with positive off-diagonal entries if and only if there exist real `a_0,...,a_{N-1}` and positive `b_0,...,b_{N-2}` such that

`P_{n+1}(x)=(x-a_n)P_n(x)-b_{n-1}^2 P_{n-1}(x)`

for every `1 <= n <= N-1` (with the obvious `n=0` initialization).

For an infinite array, the same positive three-term recurrence is exactly the Favard condition for the polynomials to be orthogonal for some positive measure of infinite support. Additional self-adjointness/moment-determinacy hypotheses select a unique spectral measure, but are not needed merely for existence of an orthogonality measure.

### Proof

If the levels are spectra of leading principal minors of a Jacobi matrix, expansion of the characteristic determinant down the last row/column gives the displayed recurrence, with `a_n` the new diagonal entry and `b_{n-1}>0` the new off-diagonal entry.

Conversely, given the recurrence, form the Jacobi matrix with those `a` and `b` entries. The same determinant recurrence implies inductively that the characteristic polynomial of its `(n+1)x(n+1)` leading minor is `P_{n+1}`. Hence the prescribed roots are exactly the minor spectra. For the infinite statement, Favard's theorem produces a positive orthogonality measure from a real three-term recurrence with positive subdiagonal coefficients. QED.

This is standard Jacobi/Favard machinery, not a novelty claim. Its value here is source matching: it gives an exact yes/no test for whether a proposed modern multilevel coupling is of Virág's Theorem-4.1 type.

### Explicit defect invariant

Let

`S_n=sum_i lambda_i^(n)` and `T_n=sum_i (lambda_i^(n))^2`.

The recurrence forces

`a_{n-1}=S_n-S_{n-1}`

and

`b_{n-2}^2 = [T_n-T_{n-1}-(S_n-S_{n-1})^2]/2 > 0`.

More strongly, after `a_n=S_{n+1}-S_n` is fixed by the roots, the entire polynomial

`R_n(x)=P_{n+1}(x)-(x-a_n)P_n(x)`

must be a **negative positive-scalar multiple** of `P_{n-1}`:

`R_n=-b_{n-1}^2 P_{n-1}`.

This is much stronger than interlacing.

At three levels there is already one nontrivial algebraic compatibility equation. Writing `e_{2,n}` and `e_{3,n}` for elementary symmetric functions of the level-n roots and `s=lambda_1^(1)`, put `a_2=S_3-S_2`. Then source-style nesting requires

`-e_{3,3}+a_2 e_{2,2} + s(e_{2,3}-e_{2,2}-a_2 S_2)=0`,

plus the positivity of the resulting `b_1^2`. The equation is genuinely nontrivial: the strictly interlacing array

level 1: `(0)`,  level 2: `(-1,1)`,  level 3: `(-2,1/2,2)`

violates it.

No numerical path sampling or approximate check is involved.

## 5. Method #24 — the extremal/thin object: the Jacobi locus inside corners space

The preceding criterion exposes a clean geometric invariant.

A real `N x N` Jacobi matrix with positive off-diagonal entries has exactly

`N+(N-1)=2N-1`

real parameters. The full triangular array of spectra of all leading principal minors has

`1+2+...+N=N(N+1)/2`

coordinates. Therefore source-style arrays lie on a locus of codimension

`N(N+1)/2-(2N-1) = (N-1)(N-2)/2`.

For `N>=3` this is a genuinely lower-dimensional algebraic/semi-algebraic locus, cut out by the recurrence-defect identities above. The three-level compatibility equation is the first codimension-one instance.

This is the useful 'extremal object' here: not an optimizer, but the minimal-dimensional Jacobi/Favard locus singled out by Virág's source construction inside the much larger interlacing-array space.

## 6. Method #27 — swap the quantifiers: modern beta-corners do not by themselves answer Question 2

The modern literature contains many multilevel beta-corners constructions:

- Borodin--Gorin construct a multilevel general-beta Jacobi corners process.
- Najnudel--Virág study the Hermite beta corner process and its bead-process bulk limit.
- Petrov--Xu (arXiv:2607.27810, 2026) extend a perturbed beta-corners construction to all beta via multivariate Bessel functions.

These are important, but their quantifier is weaker:

`there exists a joint interlacing law whose nth marginal is the desired n-level beta ensemble`.

Virág's Theorem-4.1 pattern asks instead:

`there exists one random measure / one semi-infinite Jacobi operator such that for every n its nth orthogonal-polynomial zeros / nth leading-minor spectrum have the desired law`.

Those are different questions.

Najnudel--Virág give the finite Hermite beta corners process an explicit density with respect to Lebesgue measure on the full Gelfand--Tsetlin interlacing region. Hence, for `N>=3`, such a full-dimensional corners law assigns probability zero to the lower-dimensional `2N-1`-parameter Jacobi locus above. In particular, the standard Hermite beta corners coupling is almost surely **not** the special single-Jacobi coupling from Virág's Theorem 4.1, despite having the same beta-Hermite marginal law at each level.

That observation is a scope correction, not a new solution of D0040. It explains why the existence of Jacobi/beta-corners processes in later papers does not by itself settle the exact question as posed.

## 7. Current-literature/status check

Dated 2026-09-18 searches covered the exact source wording, later beta-corners literature, Jacobi/Laguerre nesting terminology, and recent citing work. The strongest directly relevant hits were the Borodin--Gorin beta-Jacobi corners process, Najnudel--Virág Hermite beta corners/bead process, and the 2026 Petrov--Xu perturbed beta-corners process.

I did **not** find an accessible paper that explicitly constructs, for another Dyson beta ensemble, one random measure / one semi-infinite Jacobi operator whose every finite orthogonal-polynomial-zero level has exactly that ensemble's law. This is bounded negative evidence only; it is not a worldwide novelty or openness certificate.

Because Question 2 is deliberately open-ended (`any other ...? how about other natural ...?`), it is also not an honestly sharp CLOSABLE endpoint for this worker without first freezing whether a single new model constitutes source closure, or whether a classification is intended. I therefore classify D0040 for R15 as

`OPEN-LOOKING / SCOPE-CLARIFIED / HARD-LEANING / NOT CLOSABLE-READY / NOT CLAIMED`.

I also rechecked the most tempting nearby short target, D0041 (Virág's Problem 3 on Mo's hard-edge formulas). It is already protected by `operations/claims/D0041.md` and active historical work, so R15 did not duplicate it.

## 8. Admission decision

No lawful successor crossed all gates this run. Therefore:

`E_ready: 0 -> 0`.

There is no new theorem-sized source claim, no finite certificate worth checking, and no reason to manufacture a checker merely to certify an unchanged admission count.

R15 remains `SUCCESSOR_ADMISSION_REQUIRED`.

The next admission-search methods, if the queue/state has materially changed, are **#5 ADD A PARAMETER AND DIFFERENTIATE, #19 MAKE IT AN ALGORITHM, #25 COUNT THE SAME THING TWICE**. The next screen should advance beyond D0040/D0041 and revisit only newly added or materially changed rows, owner-authorized claim releases, or source-status changes.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  model_actual: GPT-5.6_Sol
  reasoning_actual: UNVERIFIED
  native_predecessor:
    id: I0076
    source: "Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.2"
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    source_metric: "four source-matching obligations for one frozen counterexample candidate"
    value_at_handoff: "2/4"
    unchanged_count_at_handoff: 6
    current_verified_candidate: NONE
    candidate_architecture_only: "sparse copied-block dependence in continuous Brownian-cell prefix/BES marks; unresolved simultaneous FBM/BBM/seam-independence compatibility"
    attacked_this_run: false
  secondary_predecessor:
    id: I0124
    status: "PARTIAL / RETIRED-HANDOFF"
    metric: H_288
    value: 112
    attacked_this_run: false
  admission_gate:
    metric: E_ready
    before: 0
    after: 0
  methods: [18, 24, 27]
  screened:
    D0040:
      source: "Balint Virag, Operator limits of random matrices, Question 2 (Nested models)"
      status: "OPEN-LOOKING / SCOPE-CLARIFIED / HARD-LEANING / NOT_CLOSABLE_READY"
      ownership: "no canonical D0040 claim found in bounded repository search"
      source_scope: "one random measure / one Jacobi-Favard recurrence generating all n levels"
      exact_scope_invariant:
        - "P_{n+1}=(x-a_n)P_n-b_{n-1}^2 P_{n-1}, b_{n-1}>0"
        - "Jacobi-locus dimension 2N-1 versus corners-space dimension N(N+1)/2"
        - "standard full-dimensional beta-corners law is a.s. off the Jacobi locus for N>=3"
      disposition: "NOT CLAIMED"
    D0041:
      status: "CLAIMED ELSEWHERE"
      disposition: "EXCLUDED"
  material_scope_correction:
    id: D0040
    before: "intake/older screen risked conflating generic beta-corners/minor couplings with Virag's single-measure nesting"
    after: "exact Favard/Jacobi recurrence distinguishes the source construction; modern full-dimensional corners couplings do not automatically resolve it"
  theorem_claims_new: 0
  source_solution_claims_new: 0
  finite_claims_new: 0
  checker: NONE
  audits: []
  claim_created: false
  successor_status: SUCCESSOR_ADMISSION_REQUIRED
  next_methods: [5, 19, 25]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

## 10. Model / scheduler / permission boundary

The scheduler limitation is unchanged in the actually exposed task-control surface. It offers title/prompt, schedule or relative-start data, timing mode and enabled state. It does **not** expose a binding model-family selector, a reasoning-effort selector, authenticated applied-model telemetry, or a guaranteed hour-long execution field. Consequently `GPT-6 / maximum` is only request text here and cannot truthfully be reported as applied.

A verified GPT-6/maximum configuration would require an authorized product/backend or owning workspace surface whose schema exposes persistent model/reasoning controls and completed-run telemetry.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary. Repository implementation records say another authorized context later succeeded in updating P26. If refusal recurs, the lawful route is the owning authorized account/workspace, a supported ownership/admin transfer, or platform support; do not duplicate the task and do not bypass access controls.

No scheduler, permission, Gmail/email, Drive, public posting, purchase, shared-root edit, or peer-track edit was performed.

**End of immutable R15 run report.**