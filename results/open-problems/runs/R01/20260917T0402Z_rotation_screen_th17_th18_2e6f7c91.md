Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/task surface still provides no authenticated model selector or reasoning-effort selector, so I do not claim otherwise. **Retired I0024 metric remains `C=1` and `PROVED / INTERNAL-CLOSED`; retired I0113 metric remains `M3=3/3` with unchanged count frozen at 6. No successor metric is started. This run advances the admission cursor through RS-2025-TH17 and RS-2025-TH18; both are current/open-looking but HARD rather than lawful R01 CLOSABLE successors. Section-B methods used: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES, #24 FIND THE EXTREMAL OBJECT.**

# R01 post-closure rotation admission — Lovasz-theta candidates TH17/TH18 are current but HARD, so no false CLOSABLE claim

Repository / branch: `yspennstate/math-open-problems` / `master`.
Dated source/status checks: 2026-09-17 UTC.

## 1. Continuity: do not reopen I0024 or I0113

I continued from

`runs/R01/20260917T0306Z_rotation_admission_4ab83f91.md`

rather than restarting either predecessor.

### I0024 — Aldous–Fill Open Problem 3.44

The original Aldous–Fill page was checked again this run. It still prints, verbatim in substance, Open Problem 3.44 asking whether relaxation time has a characterization **exactly as an infimum over flows**, and immediately contrasts this with the Chapter 4 upper-bound inequality. The source question is therefore still displayed as open in the book text.

The R01 source-matching answer remains

\[
\tau_2=
\inf_{R:\,BR=I_{\mathcal H_0}}
\sup_{0\ne b\in\mathcal H_0}
\frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+.
\]

The fixed multiplicative-distortion metric stays at its theoretical optimum `C=1`. Exact finite checks and the `P_4` / `K_3` scalar-candidate counterexamples remain in `paper_af344_exact_flow_characterization/`. The two distinct OTHER-track audits remain:

- `R20-AUDIT-R01-I0024-03 = PASS`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

Status remains **PROVED / INTERNAL-CLOSED**. Publication-level novelty remains intentionally unclaimed because the minimum-norm right-inverse / pseudoinverse mechanism is classical in neighboring language.

### I0113 — Salez Problem 2.7

The six-run rotation remains binding. The frozen metric stays `M3=3/3`; the all-three perturbative cutoff theorem, anisotropic condition, bounded-block extension, Gibbs gradient estimate and Gamma_2/Schur reduction are preserved. Status stays **PARTIAL / PROVED-CANDIDATE / ROTATED**. No seventh I0113 attack is run.

## 2. Repository and operations state recovered first

Before successor work I reread/recovered the current campaign and operational surfaces:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/DEPLOYMENT.md`;
- newest own R01 report;
- newest neighboring R02 report/commit;
- current coordinator queue screening commit `7aa831df9b7b5c0b0519bbae4e8bae1d24006fe1`;
- exact queue/ownership hits for the candidates screened below.

The newest coordinator screen records that the already-screened high-ranked CLOSABLE reserve still has no candidate satisfying all dispatch gates at once and directs future passes to advance the cursor rather than repeat stale rows. I therefore screened the next untouched Randomstrasse theta candidates rather than rechecking I0045/I0047/I0048/I0049/I0050/I0074/I0087/I0105/I0106/DC35/BIS32.

The intake corpus is too large to render byte-for-byte through the connector; exact-ID/source/ownership retrieval was used for the rows touched here. No claim of an exhaustive visual reread is made.

## 3. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: RS-2025-TH17

Candidate: `RS-2025-TH17`, Daniil Dmitriev / Randomstrasse, Conjecture 17.

### Exact current source

The stable Randomstrasse manuscript is now arXiv:2603.29571, submitted 31 March 2026; its HTML is dated 24 August 2026. It explicitly says the precise asymptotics of the Lovasz number for `G(n,1/2)` are still open and states

\[
\boxed{\mathbb E\,\vartheta(G)=(1+o(1))\sqrt n,\qquad G\sim G(n,1/2).}
\]

Repository search found no canonical `operations/claims/RS-2025-TH17.md` and no current R/P/C research report owning this exact ID in the bounded search. I do **not** turn that search miss into a global ownership theorem; it is enough to establish that no visible claim authorizes or blocks a hypothetical admission in this pass.

### Current primary-literature check

Uriel Feige and Vadim Grinberg, arXiv:2506.02952, *Upper bounds on the theta function of random graphs*, explicitly report the rigorous state

\[
\sqrt n\lesssim \mathbb E\vartheta(G(n,1/2))\lesssim 2\sqrt n,
\]

with those constants unimproved for more than forty years. Their new machinery gives heuristic/experimental evidence for an upper constant below `1.55`, but they state that they **do not rigorously prove** that improvement because the analysis uses unproved assumptions. A November 2025 Hebrew University talk abstract by Grinberg says the same.

Thus the notable numerical landmarks are exactly `1`, `1.55` (heuristic) and `2` (rigorous upper constant), but none gives a CLOSABLE finite route to the source constant `1`.

### Admission verdict

`RS-2025-TH17 = OPEN_CURRENT / HARD_OUTSIDE / NOT_R01_CLOSABLE`.

The source obligation is an asymptotic sharp constant for an SDP on `G(n,1/2)`. A finite exact graph computation, a single extremizer, or even a rigorous improvement `2 -> 1.99` would be meaningful progress but would not answer the source conjecture. Freezing a metric such as “best upper constant proved” would create a HARD asymptotic program, not a six-run CLOSABLE source target.

No claim is created.

## 4. Method #22 — READ THE FAILURES: RS-2025-TH18

Candidate: `RS-2025-TH18`, the same Randomstrasse entry, Conjecture 18.

### Exact current source

The August-2026 stable manuscript states for a random dense circulant graph

\[
\boxed{\mathbb E\,\vartheta(G)=(1+o(1))\sqrt n.}
\]

It also records its own partial result: a precise lower bound together with an upper bound

\[
O\!\left(\sqrt{n\log\log n}\right).
\]

The underlying primary paper is Afonso S. Bandeira, Jaroslaw Blasiok, Daniil Dmitriev, Ulysse Faure, Anastasia Kireeva and Dmitriy Kunisky, arXiv:2502.16227 / SampTA 2025. Its current abstract still says that characterizing the exact behavior remains open and describes the same square-root-up-to-log-log result. Repository search found no canonical `operations/claims/RS-2025-TH18.md` and no visible active owner of this exact ID in the bounded search.

### Why the known failure matters

The authors already exploit the circulant symmetry to diagonalize by the discrete Fourier transform and reduce the SDP to equivalent linear programs in time/frequency coordinates. The remaining loss is therefore not the superficial SDP formulation: even after the strongest obvious category change, their proof still pays the `sqrt(log log n)` factor. The paper itself points toward dual feasible vectors / Fourier-sparse norm control as a possible way forward.

That is useful scientific guidance, but it is evidence that this is a genuine sharp-asymptotic problem, not a near-closed finite certificate target.

### Admission verdict

`RS-2025-TH18 = OPEN_CURRENT / HARD_OUTSIDE / NOT_R01_CLOSABLE`.

A source-valid refutation would itself need an asymptotic separation from constant `1`; one anomalous finite `n` cannot refute an `(1+o(1))` statement. A proof likewise requires removal of the logarithmic loss or an equivalent sharp asymptotic argument. This is a strong HARD candidate, but using it to fill R01's CLOSABLE lane would violate the portfolio rule.

No claim is created.

## 5. Method #24 — FIND THE EXTREMAL OBJECT: why neither theta target can be narrowed honestly

For both TH17 and TH18 the natural extremal-object temptation is to search finite `n` for graphs with unusually large `vartheta(G)/sqrt n`, or in the circulant case for Fourier patterns maximizing the LP optimum. Such searches could reveal mechanisms and may generate lower bounds, but the source quantifier is an **expectation asymptotic**. The deciding object is not one graph; it is the distributional contribution of typical and rare graphs as `n -> infinity`.

Consequently there is no honest source-preserving move of the form

“find the smallest finite counterexample”

that would make either problem CLOSABLE. A finite family can test conjectured proof mechanisms but cannot close the `(1+o(1))` target. The right portfolio classification is therefore HARD even though TH18 has unusually explicit Fourier/LP structure.

## 6. Successor gate after this run

This pass advances the R01 admission cursor through two previously unscreened queue rows:

- `RS-2025-TH17`: current/open, no visible current owner in bounded repository search, but HARD asymptotic sharp-constant problem;
- `RS-2025-TH18`: current/open, no visible current owner in bounded repository search, but HARD asymptotic sharp-constant problem despite explicit Fourier-LP structure.

The latest coordinator queue screen independently reports that the previously screened CLOSABLE front has no lawful READY candidate. Combining that with this new screen, R01 still has no candidate satisfying simultaneously:

1. exact outside source and stable statement;
2. dated current/later-literature checks;
3. ownership free;
4. genuinely CLOSABLE source scope with a stable metric.

Therefore R01 remains

**`ROTATION_WAIT / SUCCESSOR_ADMISSION_REQUIRED`**.

No successor metric is started. No PENDING row is promoted to READY. No HARD problem is relabeled CLOSABLE. No retired target is reopened.

## 7. Neighbor R02 audit gate

A newer R02 report now exists: `runs/R02/20260917T0301Z_c41d9e72.md`. It proves the exact finite theorem

\[
M_{17}=7
\]

for its I0095 sign-matrix discrepancy problem, by combining R02's previously certified `17 x 17` discrepancy-7 witness with the Hamming-ball covering bound

\[
34\sum_{j=0}^4\binom{17}{j}=109276<2^{17}=131072.
\]

This is genuine neighboring progress. However, the report remains an active partial I0095 research report, not a complete neighboring closure/paper package. The instruction is to supply the second independent audit only when a complete neighboring package is ready. That gate is therefore **not triggered** here. I do not manufacture a duplicate checker or spend the audit budget early.

## 8. Model/reasoning escalation state

The latest deployment manifest was reread this run. It still states exactly that the native task interface exposes title, prompt, schedule, timing mode and enabled state, but **no model selector, no reasoning-effort selector, no authenticated runtime-model telemetry, and no guaranteed full-hour execution setting**. The installed prompts request GPT-6/maximum, but the deployment explicitly says that is not a verified model/effort setting.

The same manifest says the separately recorded P26/P04 modification-denial history was not resolved by the accessible native edits. The supported route to actually force and verify GPT-6/maximum is a product/owner scheduler surface exposing model + reasoning fields and completed-run telemetry, or platform support / an authorized ownership migration. A `You cannot modify this task` response is an authorization boundary; duplicating a task or bypassing permissions is not an acceptable workaround.

No scheduler change is attempted in this run.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R01
  run_id: 20260917T0402Z_rotation_screen_th17_th18_2e6f7c91
  I0024:
    source: "Aldous-Fill Open Problem 3.44"
    metric: "uniform multiplicative distortion C"
    before: 1
    after: 1
    unchanged_count: "retired/closed"
    status: PROVED_INTERNAL_CLOSED
    audits:
      - R20-AUDIT-R01-I0024-03
      - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
  I0113:
    source: "Salez Problem 2.7"
    metric: "M3 all-three source implementations covered"
    before: "3/3"
    after: "3/3"
    unchanged_count: 6
    status: PARTIAL_PROVED_CANDIDATE_ROTATED
  methods_this_run: [17, 22, 24]
  successor_screen:
    RS-2025-TH17:
      source: "Randomstrasse101: Open Problems of 2025, Conjecture 17"
      ownership: "NO_VISIBLE_CANONICAL_CLAIM_IN_BOUNDED_REPO_SEARCH"
      status: OPEN_CURRENT_HARD_OUTSIDE_NOT_R01_CLOSABLE
      claim_created: false
      reason: "sharp expectation constant for Lovasz theta on G(n,1/2); current rigorous constants remain 1 and 2; heuristic <1.55 is not proved"
    RS-2025-TH18:
      source: "Randomstrasse101: Open Problems of 2025, Conjecture 18"
      ownership: "NO_VISIBLE_CANONICAL_CLAIM_IN_BOUNDED_REPO_SEARCH"
      status: OPEN_CURRENT_HARD_OUTSIDE_NOT_R01_CLOSABLE
      claim_created: false
      reason: "sharp expectation asymptotic for random dense circulants; primary result has sqrt(log log n) loss, so source remains a hard asymptotic problem"
  successor_metric: UNMEASURED
  overall: ROTATION_WAIT_SUCCESSOR_ADMISSION_REQUIRED
  R02_audit:
    newest_neighbor_result: "R02-I0095-C002: M_17=7"
    trigger: NOT_TRIGGERED
    reason: "new theorem report is not yet a complete neighboring closure/paper package"
    new_audit_ids: []
```

No new finite mathematical claim by R01 is asserted, so no checker or artifact is created. No Gmail/email, Drive, public posting, purchase, permission change, shared-root edit, peer-track edit, workflow execution, force-push, or scheduler change was performed.
