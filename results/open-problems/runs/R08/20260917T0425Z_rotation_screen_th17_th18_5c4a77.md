Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or completed-run model telemetry, so I do not claim otherwise. **Retired I0082 metric remains frozen at `2/3` with retirement count `6`; successor-admission movement: `RS-2025-TH17: UNSCREENED_IN_R08 -> OPEN_CURRENT_HARD_NOT_CLOSABLE`, `RS-2025-TH18: UNSCREENED_IN_R08 -> OPEN_CURRENT_HARD_NOT_CLOSABLE`. Methods actually used: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #20 FIND WHY THE ALGORITHM FAILS, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R08 CLOSABLE OUTSIDE — rotation admission: Lovasz-theta Conjectures 17 and 18

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: I0082 stays retired

I did not reopen Hasebe--Ueda Problem 3.11. The controlling R08 handoff is `runs/R08/20260916T2327Z_i0082_sixrun_handoff_rotation_hold_4f8c2d.md`: the frozen explicit-candidate metric is `2/3`, the supported unchanged count reached `6`, and the CLOSABLE policy retired this source from further R08 research.

The strongest preserved mathematical package remains:

- `R08-I0082-C005`: candidate classification theorem, every freely strongly unimodal probability law is Dirac;
- `R08-I0082-C006`: actual-branch / first-order continuation hardening used by C005.

A fresh exact repository search for `R08-I0082-C005` recovered only R08's own proof/handoff reports and no independent end-to-end PASS. I therefore preserve the status **PARTIAL / PROVED-ON-PAGE / AUDIT_PENDING / RETIRED-FROM-R08-SLOT**. I do not create a paper folder and I do not reset the metric.

The shared `operations/claims/I0082.md` still carries older active wording; under the owner instruction, the later immutable six-run R08 handoff controls this track. I do not edit the shared claim file.

## 2. Required repository recovery and neighbor reconciliation

Before successor screening I read or exact-searched the required current state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0082.md`;
- newest own R08 report `runs/R08/20260917T0325Z_rotation_screen_i0115_sirsn_8c2f41.md`;
- newest neighboring R09 report `runs/R09/20260917T0332Z_rotation_screen_cla_clc.md`;
- newest coordinator queue screen `operations/task_health/runs/2026-09-17T034510Z/queue_screening.md`;
- intake-I README / touched problem records and exact ownership searches for the candidates below.

The coordinator screen says the CLOSABLE successor gates are intentionally left empty unless a candidate passes all four gates: exact source, dated current/later-literature check, no owner, and genuinely CLOSABLE source scope. It also instructs the cursor to advance beyond already-screened candidates rather than recycle a HARD problem.

R09's newest report screens `RS-2026-CL-A` and `RS-2026-CL-C` as current but HARD/not CLOSABLE. I therefore did not duplicate those screens.

## 3. Ownership check for the next unscreened Randomstrasse rows

Exact repository searches immediately before this screen found:

- no canonical `operations/claims/RS-2025-TH17.md` and no prior R/P/C research package under that exact ID;
- no canonical `operations/claims/RS-2025-TH18.md` and no prior R/P/C research package under that exact ID;
- only their queue entries among exact-ID matches.

Thus ownership does not itself block either row. The decisive issue is lane fit.

## 4. Exact source and current status

### RS-2025-TH17 — Erdos--Renyi Lovasz theta leading constant

Primary source: Daniil Dmitriev, Randomstrasse 101, *The Lovasz number for random graphs (problems 17 and 18)*, posted 21 May 2025, updated 22 May 2025:

`https://randomstrasse101.math.ethz.ch/posts/lovasz-circulant/`

Its Conjecture 17 is exactly

\[
G\sim G(n,1/2),\qquad \mathbb E\,\vartheta(G)=(1+o(1))\sqrt n.
\]

The 2026 stable source record is A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac and A. Rodder, *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571v1 (31 March 2026). It still records Conjecture 17 as an open problem.

The most relevant later primary paper found in the dated search is Uriel Feige and Vadim Grinberg, *Upper bounds on the theta function of random graphs*, arXiv:2506.02952 (3 June 2025). It states that for `G(n,1/2)` the rigorous expected-value bounds are still between `sqrt(n)` and `2 sqrt(n)`, says these bounds had not been improved in over forty years, and offers heuristic/experimental evidence for an upper constant below `1.55` while explicitly saying the paper does not rigorously prove such a bound. A November 2025 Hebrew University seminar abstract for the same work repeats that the sub-1.55 conclusion remains heuristic.

A bounded 2026-09-17 search for later papers/results under the exact theta/random-graph phrases did not surface a primary theorem resolving the constant-1 asymptotic. This is bounded evidence only; it is not a claim of exhaustive worldwide novelty.

**Current-status judgment:** source-current/open-looking, with serious later partial/heuristic work but no source-level resolution found.

### RS-2025-TH18 — random dense circulant Lovasz theta leading constant

The same Randomstrasse source states Conjecture 18:

\[
G\text{ random dense circulant},\qquad \mathbb E\,\vartheta(G)=(1+o(1))\sqrt n.
\]

The source itself cites the primary partial result A. S. Bandeira, J. Blasiok, D. Dmitriev, U. Faure, A. Kireeva and D. Kunisky, *The Lovasz number of random circulant graphs*, arXiv:2502.16227 (22 February 2025), subsequently published at SampTA 2025. That paper gives a sharp/precise lower bound and an upper bound of order `sqrt(n log log n)` (the exact typography differs across summaries), and explicitly says the exact behavior remains open.

The March 2026 stable Randomstrasse record arXiv:2603.29571 still includes this conjecture. A bounded 2026-09-17 search for a later sharp random-circulant theta asymptotic did not surface a source-matching primary resolution. Current public status summaries also still list the conjecture as open, but those secondary summaries are not used as closure evidence.

**Current-status judgment:** source-current/open-looking; best source-linked theorem remains partial.

## 5. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

For TH17 the number that matters is the leading constant multiplying `sqrt(n)`. Looking for that constant in the closest later work does not collapse the problem into a CLOSABLE residue: Feige--Grinberg's later approach does not even give a rigorous constant strictly below `2`; it gives a heuristic value below about `1.55`. The source asks for the exact asymptotic constant `1`.

For TH18 the same constant `1` appears in a Fourier-structured ensemble. The published partial theorem still loses a `log log n` factor on the upper side. Thus the neighboring numerical constants do not reveal a small finite obstruction or a one-parameter endpoint that R08 could honestly freeze and close.

**Outcome of #17:** both rows remain genuine asymptotic-leading-constant problems, not finite certificate problems.

## 6. Method #20 — FIND WHY THE ALGORITHM FAILS

For TH17, the obvious spectral certificate gives the classical `2 sqrt(n)` scale. The later Feige--Grinberg program tries to optimize over a richer class of polynomial-time computable upper bounds, but its sharper numerical constant relies on unproved assumptions. The precise obstruction is therefore theorem-sized control of an optimized random-matrix/SDP object, not a missing finite verification.

For TH18, circulant symmetry reduces the SDP to a random Fourier linear program. Bandeira et al. control it through sparse-Fourier/RIP estimates, but the source-level target requires removing the residual logarithmic loss and identifying the exact leading constant. Again the obstruction is asymptotic random-optimization control, not a finite case count.

A CLOSABLE worker could certainly prove a new finite-size inequality or improve a constant/factor, but unless it reaches the exact asymptotic requested by the source that result is only **PARTIAL**. Freezing an easier finite `n`, a restricted ansatz, or a weaker `O(sqrt(n log log n))` target would change the source obligation.

**Outcome of #20:** both targets are HARD OUTSIDE in their exact source scope.

## 7. Method #30 — ONE SCALE / ONE DIRECTION AT A TIME

I kept the two ensembles separate instead of treating `sqrt(n)` as permission to merge them.

- TH17 uses independent edges in `G(n,1/2)` and asks for a constant-1 asymptotic.
- TH18 uses the dependent Fourier/circulant ensemble and asks for the same-looking constant-1 asymptotic, but its proof technology and current gap are different.

The complement identity and the shared lower `sqrt(n)` scale do not transfer the missing upper bound from one ensemble to the other. In particular, finite numerics on either ensemble cannot settle the asymptotic source statement.

**Outcome of #30:** neither row is a lawful CLOSABLE replacement, and one should not use progress on one as evidence of closure of the other.

## 8. Admission dispositions

This run advances the R08 successor-admission cursor past two additional unclaimed queue rows:

- `RS-2025-TH17`: **OPEN_CURRENT / HARD_OUTSIDE / NOT_CLOSABLE_FOR_R08**;
- `RS-2025-TH18`: **OPEN_CURRENT / HARD_OUTSIDE / NOT_CLOSABLE_FOR_R08**.

No claim is created and no successor metric is started.

The result is still

`R08 = ROTATION_HOLD / SUCCESSOR_ADMISSION_REQUIRED`.

That is preferable to seizing a HARD asymptotic problem, narrowing its quantifiers, or inventing a finite surrogate simply to keep the slot busy.

## 9. No new neighboring theorem audit

The newest R09 report is itself a successor-admission screen (`RS-2026-CL-A` / `RS-2026-CL-C`), not a new theorem/certificate package. There is therefore no legitimate new R09 mathematical audit to manufacture this run.

## 10. Model / scheduler / denied-task escalation status

The runtime situation is unchanged. The exposed task-management surface provides prompt/title/schedule/timing/enabled controls but **no model-family selector, no reasoning-effort selector, no authenticated applied-run model telemetry, and no guaranteed hour-long execution control**. GPT-6 / maximum therefore remains prompt text rather than a verifiable runtime setting.

Actually enforcing it requires a product/API surface that exposes model and reasoning fields plus completed-run telemetry, or management from the authorized task-owning workspace/UI if that surface provides those controls. Historical `You cannot modify this task` responses, including the earlier P26 case, are authorization/ownership boundaries. The lawful workaround is the owning context, ownership/admin transfer, or platform support — not duplicate tasks and not repository text pretending to configure runtime.

No scheduler modification, email/Gmail, Drive operation, public posting, purchase, permission change, workflow execution, shared-root rewrite, peer-track edit, or force-push was performed.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  run_id: 20260917T0425Z_rotation_screen_th17_th18_5c4a77
  predecessor:
    source: "Hasebe-Ueda arXiv:1710.08240v2, Problem 3.11 / I0082"
    metric: "number of three frozen obligations proved for one explicit candidate"
    before: 2/3
    after: 2/3
    unchanged_count: 6
    state: RETIRED_FROZEN
    strongest_package: "R08-I0082-C005/C006; PROVED_ON_PAGE_SELF_CHECKED_AUDIT_PENDING"
  methods_this_run: [17, 20, 30]
  neighbor_reconciliation:
    R09: "latest report is 20260917T0332Z successor-admission screen; no new theorem package to audit"
  successor_screen:
    RS-2025-TH17:
      ownership: "no canonical claim recovered under exact ID"
      source_status: "Conjecture 17 retained in March 2026 Randomstrasse stable record; Feige-Grinberg 2025 is heuristic/partial, not a source-level resolution"
      disposition: OPEN_CURRENT_HARD_OUTSIDE_NOT_CLOSABLE_FOR_R08
      claim_created: false
    RS-2025-TH18:
      ownership: "no canonical claim recovered under exact ID"
      source_status: "Conjecture 18 retained in March 2026 stable record; Bandeira et al. 2025 proves only partial sqrt(n)-scale bounds with logarithmic upper loss"
      disposition: OPEN_CURRENT_HARD_OUTSIDE_NOT_CLOSABLE_FOR_R08
      claim_created: false
  successor_metric: UNMEASURED
  overall: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  new_exact_artifact: NONE_SOURCE_ADMISSION_RUN
```