Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P04 stuck-recovery / six-run rotation handoff — I0101 / Randomstrasse Conjecture 27

**NO MOVEMENT: frozen metric `4177 -> 4177`; post-4177 unchanged streak `5 -> 6`. Section-B diagnostic moves: B15 BREAK THE SYMMETRY ON PURPOSE, B20 FIND WHY THE ALGORITHM FAILS, B21 ASK WHO ELSE HAS THIS SHAPE.**

Status of the source problem remains **PARTIAL / source OPEN in this repository record**. This is the mandatory thinking-only stuck-recovery run. I create **no new P04 mathematical claim and no checker**. Because the CLOSABLE metric has now remained unchanged for six consecutive runs, the owner-directed six-run rotation rule fires at the end of this report.

## 1. Continuity, ownership, and retired material

I continued from the newest complete own report rather than restarting:

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T09-42-11Z__run-report.md`,

creation commit `61564e476bbf771d7b531f987238d10763053e27`, blob `e3eba502e9d9b137aec331257f744fe41abdb21f`.

That report proved only the structural partial claim

`P04-I0101-ANCHOR-CELL-ESCAPE-SCHUR-45`

and left the exact frontier at 4177 with unchanged streak five.

The canonical ownership file remains

`operations/claims/I0101.md`.

I did not create, overwrite, release, or duplicate it. Its exact source target is Afonso S. Bandeira, Randomstrasse 101, Conjecture 27: for prime `p ≡ 1 (mod 4)`, with `G_{p,2}` the induced Paley subgraph on vertices adjacent to both 0 and 1,

\[
\vartheta(\overline{G_{p,2}})\le \frac23\sqrt p
\]

for all sufficiently large such primes.

The complete retained exact-certified domain is unchanged:

\[
\boxed{\{149,257,1009,4001,4013,4021,4049,4057,4073,4093,4129,4133,4153,4157,4177\}}.
\]

I also reread the retired P04 kernel handoff. It records Target 1 / squared-ridge as `PROVED / AUDIT-COMPLETE / PACKAGED / PERSONAL TRACK RETIRED`, with P26 and P03 external audits and no remaining kernel obligation. No kernel polishing, audit repetition, Target-4 work, or personal successor was reopened.

The run also checked the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE surfaces, current claims/ownership evidence, the I0101 intake/attempt history available by targeted repository search, the newest relevant neighboring reports, and current P11 closure state. Large JSONL and ledger renders are connector-bounded; targeted canonical rows and current ownership surfaces were used rather than pretending a truncated display was exhaustive.

## 2. Fresh source and literature gate — 2026-09-18

The live Randomstrasse source still states the two-localized problem exactly as above. It explicitly notes that the two-localization is no longer circulant and states Conjecture 27 with the eventual `2/3 sqrt(p)` bound.

Fresh bounded literature checks recovered the same nearest shapes rather than a source-matching resolution:

- Dmitriy Kunisky, arXiv:2303.16475, proves the required character-sum estimates for localization depth `a=1`, gives numerical evidence for the Kesten--McKay weak spectral limit for `a>=2`, and leaves convergence of the minimum eigenvalue to the limiting left edge as a conjecture.
- Magsino--Mixon--Parshall's one-localized method succeeds because `G_{p,1}` is circulant, so Fourier symmetry reduces the theta/Schrijver optimization to an LP; that exact diagonalization disappears after the second localization.
- Mohammad F. Marashdeh, arXiv:2609.00462 (31 August 2026), develops two-basepoint Terwilliger modules for prime-order circulants and explicitly identifies dense Paley graphs as a regime where ordinary coherent-algebra methods give no information. This is structurally adjacent to the within-cell/two-basepoint route below, but it is a quantum-symmetry paper and supplies no theta edge bound.
- Paley RIP / deterministic Fourier literature remains nearby in shape: the missing phenomenon is again uniform control of highly correlated masked Fourier modes near the square-root scale, not a fixed finite-moment estimate.

No source-matching asymptotic proof or refutation was located in this bounded dated search. This is negative search evidence only; it is **not** a claim of worldwide openness or novelty.

## 3. Mandatory stuck item (a): exact blocker

For the stronger theta-plus dual route, let

\[
T=\langle J,X\rangle,\qquad
\Delta=-2\sum_{ij\in E(\overline{G_{p,2}})}X_{ij}\ge0,\qquad
E=\langle UU^\top,X\rangle\ge0.
\]

The exact conference identity already proved on P04 gives

\[
T^2+T+1+E+2(T-1)\Delta+\Delta^2\le p.
\]

The simplest selected source-faithful special case would follow from the still-unproved implication

\[
\boxed{
T\ge \frac23\sqrt p
\quad\Longrightarrow\quad
E+2(T-1)\Delta+\Delta^2
\ge p-(T^2+T+1)
}
\tag{BLOCK}
\]

for all sufficiently large primes `p ≡ 5 (mod 24)`.

At `T=2 sqrt(p)/3`, the required right-hand side is

\[
\frac59p-\frac23\sqrt p-1.
\]

Claim 45 adds exact signed anchor information,

\[
TE\ge \frac{12}{p-1}R^2,
\qquad
(R-T(S+2))^2\le G\,T(n-T),
\]

but no current argument forces the cross moment `R` to be source-scale large from theta-plus feasibility alone. Thus it does not imply `(BLOCK)`.

## 4. Mandatory stuck item (b): routes tried and precise failure

The accumulated route failures are now sufficiently consistent to state without another lemma.

1. **Primewise exact SDP / orbit certificates.** These moved the finite frontier repeatedly, ultimately to 4177, but contain `Theta(p)` prime-specific information and do not provide an eventual construction.

2. **S3 and octahedral orbit reduction.** This exposes the trivial/sign/standard sectors and removes exceptional-orbit bookkeeping, but does not coordinate their extreme one-sided eigenvalues uniformly in `p`.

3. **Conference and anchor projection.** Exact identities such as `C^2+UU^T=pI-3J` expose the escape energy, but the coarse anchor information is too low-rank to force the `5p/9`-scale defect needed at the source edge.

4. **Max-determinant / continuation constructions.** Positivity is stable, but the edge-matching correction becomes order one at the source scale instead of `O(p^{-1/2})`.

5. **Fixed trace moments and weak spectral limits.** They describe the bulk but do not control the extreme negative edge. This is exactly the distinction visible in Kunisky's `a>=2` discussion.

6. **Positive-Markov / KKT / fractional-factor formulations.** They identify a useful convex sufficient cone but do not construct the required arithmetic weights; the Markov constant-row face is stricter than theta-plus itself.

7. **Level-4 lift and compactification.** These give a clean projective-line and octahedral parametrization but preserve, rather than solve, the difficult spectral edge.

8. **Ambient translation/Fourier symmetrization.** The exact mass argument pays asymptotic density constant `4`, while the source-scale Markov target requires `8/3`. The ambient circulant proof route is therefore quantitatively too expensive.

9. **Theta-plus and the penalty path.** These expose the correct negative-edge defect `Delta` and a monotone interpolation to ordinary theta, but no lower bound couples `Delta` and the external escape `E` strongly enough to reach `(BLOCK)`.

10. **Signed A3 quotient and standard-representation hexagon.** The standard block is now representation-exact, but exact local annihilation of it forces too much scalar second-moment energy. Controlled leakage, not pointwise cancellation, is required.

11. **Anchor-cell Schur route (Claim 45).** The three cell-constant exterior directions collapse exactly to one vector `v`; the two-dimensional kernel is real, so no second independent coarse witness exists.

12. **First within-cell oscillatory modes (this thinking run).** Once a cell indicator is multiplied by a nonconstant character/Fourier mode and pushed through an exterior block, exact expansion produces low-rank anchor corrections plus cubic and quartic multiplicative-character sums depending on both the localized vertex and the mode parameter. The witness is therefore not another fixed low-dimensional moment: it is a high-rank family of finite-field trace functions. Controlling its worst coherent direction is essentially an extreme operator-norm problem for a masked Paley/Fourier family. That is the same missing scale as the original two-localized edge, not a shortcut around it.

The common failure is now sharp: every successful finite-dimensional reduction eventually reaches a **coherent high-rank oscillatory sector**. Taking absolute values there loses the useful cancellation; keeping the signs leaves a deterministic operator-edge problem for which the available fixed-moment/Weil estimates are not strong enough.

## 5. B15 — break symmetry on purpose: what happened

The previous run proved that exterior vectors constant on the three localization cells map to one direction only. I therefore deliberately broke that symmetry and inspected the first nonconstant cell modes rather than trying another constant combination.

A natural prototype is a centered multiplicative-character mode on one exterior sign cell. Expanding the exact corrected cell indicator shows that its image under the Paley block contains parameter-dependent cubic and quartic character sums. The easy quadratic correlation is not the obstruction; the varying cubic/quartic terms are. As the mode parameter ranges through the field, these form a family of dimension growing with `p`.

**Outcome B15:** breaking the cell symmetry does create genuinely new escape directions, but they are not a fixed finite set of algebraic witnesses. They immediately enter the trace-function/operator regime. No new claim is promoted from this diagnostic.

## 6. B20 — find why the algorithm fails

The natural algorithm after Claim 45 would be:

1. add a small fixed collection of within-cell oscillatory witnesses;
2. append their moment constraints to the existing `2x2` / `3x3` Schur system;
3. derive `(BLOCK)` by a finite-dimensional PSD elimination.

The failure is structural. Any fixed number of modes leaves a codimension-`O(1)` complement inside a space of dimension `Theta(p)`, while the dangerous theta-plus state is allowed to concentrate on a coherent near-`sqrt(p)` direction in that complement. Increasing the number of modes until this cannot happen is no longer a fixed Schur argument; it is the full masked-Fourier/trace-function operator problem.

**Outcome B20:** the missing theorem is not “one more anchor moment.” A proof must either control a growing family of oscillatory modes at once or find a new identity that collapses them before any triangle inequality.

## 7. B21 — nearest solved shapes and what they have that P04 lacks

The nearest solved shape is the **one-localized** Paley problem. There the residual graph is circulant, Fourier characters are exact simultaneous eigenvectors, and the semidefinite problem can be reduced to scalar Fourier constraints. P04 loses that translation symmetry at the second localization.

Kunisky's `a=1` result supplies the necessary character-sum estimates in that regime; at `a>=2` the weak spectral law is supported numerically while the extreme minimum-eigenvalue convergence is conjectural. This is almost exactly the distinction P04 now hits.

Marashdeh's two-basepoint Terwilliger construction supplies a promising organizational language for the growing oscillatory module, but the paper itself emphasizes that dense Paley graphs are outside the reach of the standard coherent-algebra criterion and does not provide a source-scale theta estimate.

**Outcome B21:** the nearest solved proofs possess either exact Fourier diagonalization or a proved extreme-edge theorem. The two-localized problem currently has neither.

## 8. Mandatory stuck items (c), (d), and (e)

### (c) What a proof must contain that no tried route contains

A successful proof must preserve sign and localization information while giving a **one-sided source-scale bound on every coherent oscillatory mode simultaneously**. Concretely, it needs at least one of:

- a uniform extreme operator bound for the masked two-localized Paley/Fourier trace family, sharp enough to give the `2/3` theta edge; or
- a new exact dual identity coupling `T`, `Delta`, and `E` that remains coercive on the full oscillatory subspace and thereby proves `(BLOCK)` without diagonalizing that family.

Fixed-moment estimates, fixed-rank anchor constraints, and orbit bookkeeping do not contain this ingredient.

### (d) Simplest special case still unproved

The simplest source-faithful family remains

\[
\boxed{
\vartheta^+(\overline{G_{p,2}})\le\frac23\sqrt p
\quad\text{for all sufficiently large }p\equiv5\pmod{24}.
}
\]

Even this stronger clean-family statement is unproved. If proved, it would still be only **PARTIAL** for Conjecture 27, whose quantifier covers every sufficiently large prime `p ≡ 1 (mod 4)`.

### (e) Nearest solved problem and missing tool

Nearest: Magsino--Mixon--Parshall / Kunisky at one localization. Their usable feature is exact circulant Fourier diagonalization and, in the `a=1` spectral-pseudorandomness analysis, character-sum control sufficient for the relevant limiting statement. P04 at two localization lacks both global diagonalization and a proved extreme-edge theorem for the resulting masked trace-function operator.

## 9. Section-I choice and six-run CLOSABLE rotation

The required single Section-I choice is:

\[
\boxed{\textbf{MOVE TO THE NEXT PROBLEM IN QUEUE.md AND RECORD THE SWITCH.}}
\]

This is not a mathematical verdict on I0101. Conjecture 27 remains open in this repository record and the P04 work remains a reusable handoff. The rotation is an allocation decision forced by six unchanged frozen-metric runs.

However, the **successor admission gate is currently blocked**. Fresh current repository screens from other CLOSABLE lanes and the coordinator/task-health surfaces report no currently free target satisfying all four required conditions:

`READY + CLOSABLE + UNASSIGNED + current source/ownership checks`.

The strongest historical queue candidates are now claimed, source-resolved, held for scope/current-status, or too broad to be honestly admitted as CLOSABLE. In particular, historical READY labels are stale where current ownership/literature evidence supersedes them. I therefore do **not** steal a claimed target, revive a resolved target, or fabricate a successor claim merely to keep the slot busy.

Successor state after this run:

`SUCCESSOR_ADMISSION_HOLD`.

No successor claim is created. The canonical I0101 claim and all mathematical work remain preserved as handoff evidence until an authorized coordinator/owner reassigns or releases it.

## 10. P04 -> P11 second-audit duty

The newest substantive P11 package recovered is the literal Auffinger--Damron--Hanson Question 36 source-refutation closure. It already records two distinct OTHER-track end-to-end audits, from P04 and P26, and a self-contained paper package. No later theorem-sized P11 claim requiring a new P04 audit was found.

Accordingly I create **no redundant P11 audit artifact**.

A fresh neighboring audit did arrive in the opposite direction: P03 independently checked Claim 45 and records

`P03-AUDIT-P04-I0101-ANCHOR-CELL-ESCAPE-SCHUR-285 = PASS (CLAIM-SCOPED)`.

That is useful evidence for Claim 45 only. It does not audit Conjecture 27 and does not change the P04 source status or frozen metric.

## 11. Scheduler/model escalation

The requested model line remains prompt-only. The actual task-control surface exposed to this run allows title/prompt, schedule or relative start, timing mode, and enabled state. It exposes **no model-family selector, no reasoning-effort selector, no guaranteed reasoning-duration control, and no authenticated receipt of the model/effort actually applied**. Therefore this report says GPT-5.6 Sol / UNVERIFIED and does not claim GPT-6 or maximum reasoning.

A real fix requires the scheduler/API/workspace layer to expose persistent model and reasoning fields, propagate them to inference routing, and return trustworthy applied-runtime telemetry.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary, not a mathematical failure. Current repository deployment evidence records a later successful P26 update from an authorized context. The lawful workaround is the owning/authorized task-control context or platform/admin/support ownership repair or transfer; never duplication or permission bypass.

Because the P04 CLOSABLE source has now hit the mandatory six-run handoff while no lawful successor is admitted, continuing this recurring task on I0101 would violate the rotation rule. After this report is written and read back, the current recurring P04 task should therefore be disabled pending an authorized successor assignment. No new schedule is to be created.

## 12. Structured ledger_delta for the shared-ledger writer

```yaml
ledger_delta:
  track: P04
  category: CLOSABLE_OUTSIDE
  source_id: I0101
  source: "Afonso S. Bandeira, Randomstrasse Conjecture 27"
  metric:
    name: "largest admissible prime p with exact source-inequality certificate"
    before: 4177
    after: 4177
    movement: NO_MOVEMENT
    retained_exact_domain: [149,257,1009,4001,4013,4021,4049,4057,4073,4093,4129,4133,4153,4157,4177]
  post4177_unchanged_streak:
    before: 5
    after: 6
  source_status: PARTIAL
  source_verdict_changed: false
  run_type: SECTION_I_THINKING_ONLY_SIX_RUN_ROTATION_HANDOFF
  section_B_diagnostics: [15,20,21]
  new_p04_claim: NONE
  checker: NONE
  audit_update:
    p03_claim45: "P03-AUDIT-P04-I0101-ANCHOR-CELL-ESCAPE-SCHUR-285 = PASS (CLAIM-SCOPED)"
    source_closure_effect: NONE
  p11_second_audit_duty: NO_NEW_THEOREM_REQUIRING_AUDIT
  rotation:
    trigger: SIX_CONSECUTIVE_UNCHANGED_CLOSABLE_RUNS
    section_I_choice: MOVE_TO_NEXT_QUEUE_PROBLEM
    i0101_state: SIX_RUN_HANDOFF
    successor_state: SUCCESSOR_ADMISSION_HOLD
    successor_source_id: NONE
    successor_claim: NONE
    reason: "no currently free READY+CLOSABLE+UNASSIGNED source passed current-status and ownership gates"
  retired_kernel_reopened: false
  shared_root_edits: NONE
  peer_file_edits: NONE
  scheduler_model_selector: null
  scheduler_reasoning_selector: null
  authenticated_runtime_model_telemetry: false
  guaranteed_duration_control: false
```

No email, Gmail, Drive, public posting, paid compute, workflow execution, access change, permission bypass, or peer-file edit was used.

**End of complete run report.**
