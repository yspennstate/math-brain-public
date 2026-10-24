Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but no authenticated model/reasoning selector or per-run routing receipt is exposed, so I do not claim otherwise. **NO MOVEMENT: successor-admission metric `E_ready: 0 -> 0`; R19 remains `SUCCESSOR_ADMISSION_REQUIRED`; methods #2, #18, #21.**

# R19 CLOSABLE OUTSIDE — successor screen through D0029

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: preserve I0084 and the later R19 rotations

I did not restart the Hasebe--Ueda target named in the stale scheduler prompt. The controlling I0084 handoff remains

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

Its frozen source-version convention is preserved exactly:

- source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084;
- `S_t` may be the law of a classical or a free alpha-stable process;
- the initial measure has the source's exact `(2+alpha)` moment assumption;
- **the conclusion uses ordinary classical convolution `mu * S_t` in both branches**, including when `S_t` is a free-stable law;
- the retained alpha=1/2 metric is frozen at `2/2`, meaning both universal source branches were decided negatively by source-admissible counterexamples; it does not mean all input measures were classified.

I also preserved the later R19 rotations. I0120 was handed off after its six-unchanged limit. F0057/Janson Problem 19.10 was then taken, moved its fixed source metric to `M_TV=1`, and was itself rotated after six unchanged runs. Its newest durable handoff is

`artifacts/R19/2026-09-17_23-36-18_UTC__f0057_source_only_rotation_handoff_b742.md`.

F0057 remains `ROTATED / PROVED_CANDIDATE / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED`; it is not reopened here.

Thus the current R19 state is successor admission, not active I0084/F0057 research.

## 2. Required repository read and current gate

Before mathematical screening I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` and the current NEW-METHODS implementation records;
- the newest complete R19 report and both frozen R19 handoffs above;
- the newest neighboring successor screens, including R08, R15, R20, task-health reconciliation, and NM13 admission work;
- the relevant D-intake rows and prior attempts reached in this pass.

The current task-health reconciliation still has no certified free `READY + CLOSABLE + UNASSIGNED` successor on its screened front. Historical READY rows are stale because they are now claimed, resolved, or held. I therefore continued the source cursor rather than stealing a claim or relabeling a HARD/PENDING item.

For this admission-only run I use

`E_ready := number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors admitted in this bounded pass.`

Before: `0`. After: `0`.

I do not invent an unchanged-count baseline for pre-admission screening; it remains `UNKNOWN / NOT APPLICABLE`.

## 3. Screened source front

### D0028 — KCM stationary-measure decomposition

D0028 is Conjecture 3 from the 2025 KCM source: every stationary measure of a kinetically constrained model should be a mixture over bootstrap-percolation-stable configurations. The literal source is a broad infinite-volume classification theorem. It is not a finite certificate, sharp constant, or short source-wide parametric endpoint, so it remains `HARD / NOT CLOSABLE` for this lane. No claim was created.

### D0029 — Bradley Question 1

The next potentially cleaner candidate is `D0029`, Richard C. Bradley (2005), Question 1, Section 1.2:

> for a real Banach space `B`, is the dependence coefficient `R^B_{infinity,infinity}` always equivalent, in the vanishing sense, to either `alpha` or `beta`?

The source records Hilbert spaces on the alpha side and `l_1`, `l_infinity`, `c_0` on the beta side. The intake already contains substantive attempt `D0029-A001`, which proposed B-convexity / uniform `l_1^n` containment as the natural geometric split and identified the B-convex side as the wall.

A fresh canonical ownership read at delivery time returned 404 for `operations/claims/D0029.md`; no current ownership file was found. However, **absence of a claim is not READY admission**. I found no current queue/admission record promoting D0029 to `READY + CLOSABLE + UNASSIGNED`, and the remaining full-source branch is substantial. Therefore I did not auto-promote or claim it.

### D0030 — Bradley Question 2

D0030 asks whether phi-mixing implies rho-star-mixing. The intake's existing attempt already reduces the issue to interlaced dependence and identifies the missing uniform control over arbitrarily many alternations. Fresh bounded status searching did not recover a source-matching resolution, but the target remains a qualitative infinite-process theorem rather than an honest CLOSABLE endpoint. It is not admitted here.

## 4. Method #2 — attack the negation first on D0029

I first tried to make Bradley's proposed dichotomy fail by looking for a third equivalence class arising from intermediate Banach geometry. No source-valid counterexample was obtained. Instead the beta side rigidified much more strongly than the intake attempt had recorded.

Let `B` contain `l_1^n` uniformly with distortion at most `C` for every `n`. Then for every pair of sigma-fields,

\[
\boxed{
\frac{2}{C}\,\beta(\mathcal A,\mathcal C)
\le R^B_{\infty,\infty}(\mathcal A,\mathcal C)
\le 2\,\beta(\mathcal A,\mathcal C).
}
\]

The proof is short and complete. The upper bound is the entrywise absolute-value bound on every centered contingency table. For the lower bound, take a finite partition nearly attaining beta, embed its `l_1` row-coordinate space into `B`, and for each column use the sign vector of that column to define a functional on the embedded subspace. Hahn--Banach extends those functionals to `B^*`, and the resulting covariance equals the entrywise `l_1` mass divided by the embedding distortion. The full proof is saved in the run artifact.

Since non-B-convexity is characterized by uniform containment of `l_1^n`, this proves the entire non-B-convex class lies on Bradley's beta side. I make **no novelty claim**: this may be folklore or implicit in the Banach-space geometry behind Bradley's examples.

## 5. Method #18 — say D0029 in another language

For finite partitions with centered contingency matrix

\[
d_{ij}=P(A_i\cap C_j)-P(A_i)P(C_j),
\]

Bradley's coefficient becomes

\[
R_B(D)
=\sup_{\|x_i\|_B,\|y_j\|_{B^*}\le1}
\left|\sum_{i,j}d_{ij}\langle x_i,y_j\rangle\right|
=\|D\otimes I_{B^*}\|_{\ell_\infty^J(B^*)\to\ell_1^I(B^*)}.
\]

So the source question is an operator-amplification dichotomy for centered contingency matrices. The scalar cut/sign norm is the alpha endpoint (up to the standard convention factor), while the entrywise `l_1` norm is the `2 beta` endpoint.

This translation makes the remaining obstruction precise rather than rhetorical.

## 6. Method #21 — ask who else has this shape

The natural adjacent machinery is local Banach-space geometry: B-convexity, type/cotype, uniform `l_1^n` containment, regular operators, and uniformly curved spaces.

The uniform-`l_1^n` side gives the exact beta theorem above. The tempting alpha-side route is to show that for B-convex spaces, small scalar cut norm forces the amplified norm to be small. A direct regular-operator interpolation attempt fails on **rare atoms**: alpha can be tiny while dependence is concentrated on events of tiny probability, so the normalized scalar `L_2` operator need not be small without additional density / likelihood-ratio control. This explains why restricted results with stronger regularity do not automatically solve Bradley's unrestricted Question 1.

Thus the current honest source-level state is:

- non-B-convex `B`: beta-equivalence established by the artifact theorem;
- B-convex `B`: unresolved by this route;
- an intermediate third equivalence class is not excluded;
- D0029 as a whole remains open-looking and is **not** promoted to READY/CLOSABLE.

This is real mathematical progress in screening a candidate, but it does not move `E_ready`.

## 7. Prior-art / current-status log

Dated 2026-09-18 UTC, I checked the original Bradley survey, the intake's exact D0029 row and prior attempt, and bounded searches for later work on Bradley Question 1 / the Banach-space dependence coefficient. The searches recovered Bradley's source and restricted dichotomy literature, but no later primary theorem explicitly resolving the unrestricted question. This is bounded negative evidence only, not a novelty or eternal-openness certificate.

For the new non-B-convex lemma I explicitly record that the mechanism may be folklore: the proof is a direct uniform-`l_1^n` embedding plus Hahn--Banach argument, and this run did not establish publication priority.

## 8. Validation / delivery

The substantive artifact is

`artifacts/R19/2026-09-18_01-22-17_UTC__d0029_nonbconvex_beta_screen_d29b.md`.

It contains the full theorem proof and the matrix-amplification reformulation. No exact-arithmetic checker was created because there is no finite computational core.

Artifact creation commit: `72a84849110e532f4ce82b15aff027febcf60cc2`. The artifact was read back from that exact commit before this report was written.

No ownership claim was created. No shared root or peer-track file was edited.

## 9. Model / scheduler status

The model-control limitation remains current. The task-management surface available to this worker exposes title/prompt, schedule or start offset, timing mode, and enabled state, but no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated applied-run model receipt. Making GPT-6/maximum enforceable requires product/backend support exposing those fields and runtime attestation; prompt text cannot make it binding.

The historical P26 `You cannot modify this task` event is not a global immutability result. Current P26 history records that a later authorized context successfully updated the task. The demonstrated lawful workaround is the owning/authorized context (or supported product/admin assistance), not cloning the task or bypassing permissions.

No scheduler change was attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  preserved_retired_source:
    id: I0084
    source: "Hasebe-Ueda arXiv:1710.08240v2, Conjecture 5.5"
    source_version_scope: "ordinary classical convolution mu*S_t in both classical-stable and free-stable branches"
    frozen_metric: "2/2 alpha=1/2 universal source branches decided negatively"
    reopened: false
  preserved_rotated_source:
    id: F0057
    metric: "M_TV=1"
    status: "ROTATED / PROVED_CANDIDATE / AUDIT_PENDING / NOVELTY_UNVERIFIED"
    reopened: false
  active_source: null
  run_status: SUCCESSOR_ADMISSION_REQUIRED
  metric_name: E_ready
  metric_definition: "newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors admitted in this bounded pass"
  metric_before: 0
  metric_after: 0
  movement: false
  unchanged_count: UNKNOWN_NOT_APPLICABLE_PRE_ADMISSION
  tried_moves: [2, 18, 21]
  screened:
    - id: D0028
      disposition: HARD_NOT_CLOSABLE
      action: NO_CLAIM
    - id: D0029
      disposition: HOLD_SCOPE_NOT_READY
      action: NO_CLAIM
      ownership_check: "operations/claims/D0029.md absent at delivery-time read"
      progress: "proved beta-equivalence for every Banach space containing l_1^n uniformly; full B-convex/source branch remains"
    - id: D0030
      disposition: HARD_NOT_CLOSABLE
      action: NO_CLAIM
  remaining_obligation: "Continue beyond D0030 and admit only a literal source-wide target that is current-open, ownership-clean, and actually READY+CLOSABLE; do not auto-promote D0029."
  evidence:
    - "artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md"
    - "artifacts/R19/2026-09-17_23-36-18_UTC__f0057_source_only_rotation_handoff_b742.md"
    - "probability_1000_intake_D_20260908/batches/b03.json"
    - "probability_1000_intake_D_20260908/attempts.jsonl"
    - "artifacts/R19/2026-09-18_01-22-17_UTC__d0029_nonbconvex_beta_screen_d29b.md"
  audit_ids: []
```

No Gmail/email, Drive, public posting, purchase, permission change, workflow execution, shared-root edit, peer-file edit, or scheduler modification was performed.
