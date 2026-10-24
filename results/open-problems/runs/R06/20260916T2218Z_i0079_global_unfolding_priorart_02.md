Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED by runtime metadata — GPT-6 maximum was requested, but the exposed scheduler/runtime surface has no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **NO MOVEMENT: active I0079 metric `R_unique = +infinity -> +infinity`; Section-B moves tried: #22 READ THE FAILURES / CLOSE PRIOR ART, #18 SAY IT IN ANOTHER LANGUAGE, #3 PROVE SOMETHING STRONGER.**

Problem/source: Héctor Jardón-Sánchez, Sam Mellick, Antoine Poulin, Konrad Wróbel, *Exactness and the topology of the space of invariant random equivalence relations*, Question 2 (accepted 2026 version): “In what generality can one say that there is a unique ideal Bernoulli Voronoi tessellation on a group?” Intake I0079. **Status: PARTIAL; the full source question is not claimed closed.**

# R06 CLOSABLE OUTSIDE — I0079 run 2: global phase unfolding, close-prior-art correction, and IRE-cylinder hardening

Run date: 2026-09-17 Asia/Jerusalem / 2026-09-16 UTC.
Repository / branch: `yspennstate/math-open-problems` / `master`.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Repository continuity and why I0056 is not restarted

The scheduler title/prompt still names Lyons--Peres Question 6.20 / I0056, but current repository state is later than that assignment. R06 reached the six-unchanged-run rotation threshold on I0056 and preserved the complete handoff in

`runs/R06/20260916T2020Z_i0056_rotation_i0079.md`.

The canonical successor is

`operations/claims/I0079.md`,

and the newest own report before this run is

`runs/R06/20260916T2121Z_i0079_phase_cancellation_01.md`.

Therefore this run continues I0079 instead of silently restarting a rotated problem. I0056 remains preserved as PARTIAL / audit-gated; its `H_{5,5}` frozen interval remains collapsed to `[sqrt(5),sqrt(5)]`.

Before new mathematics I rechecked current `master` through the connector:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md` and `QUEUE.md`;
- canonical `operations/claims/I0079.md`;
- newest own R06 report;
- newest R07 report `runs/R07/20260916T2124Z_i0077_positive_seam_gauges_05.md`;
- targeted repository searches for I0079, R06-I0079 audits, P26 audit records, and current model/deployment manifests.

The large intake JSONL files cannot be exhaustively rendered row-by-row through the connector in one response; the I0079 intake/source/ownership record was checked by targeted repository search. No other track's file was edited.

## 2. Fixed metric and continuity

Frozen class from the canonical claim:

\[
\Gamma=F_2\times F_2,
\]

with the standard product word metric, equivalently the graph product `T_4 x T_4` with the `l^1` graph metric.

Frozen tie refinement: each Bernoulli nucleus receives an iid continuous `Unif[0,1]` label and a distance tie is won by the smallest label. This is an equivariant genuine-partition refinement of the type allowed by the source and is the exact marked convention used in the product-tree convergence paper. No refinement-independent theorem is claimed.

Metric:

\[
R_{\rm unique}
=
\sup\{R\ge1:\hbox{ all subsequential refined BVT limits agree on every IRE cylinder supported in }B_R(e)\}.
\]

Previous run proved `R_unique=+infinity` for this frozen marked model, subject to the explicit audit gate on the finite-cylinder handoff. Therefore the metric cannot increase:

\[
\boxed{+\infty\longrightarrow+\infty.}
\]

This is the first unchanged run after the previous movement, so `unchanged_count = 1`.

## 3. Primary source rechecked

Current source checked directly again:

`https://antoinegpoulin.github.io/pdf/exac.pdf`

Section 6 defines BVT for a left-invariant proper metric. The unrefined Voronoi cells can overlap on distance ties; the source explicitly says one may refine equivariantly to a genuine partition, gives random tie choice as an example, says other methods are possible, and fixes one. Question 2 remains:

> In what generality can one say that there is a unique ideal Bernoulli Voronoi tessellation on a group?

Thus the source problem remains open-ended and the present iid-nucleus-label theorem is only one source-admissible partial answer.

## 4. Move #22 — READ THE FAILURES / CLOSE PRIOR ART: a much closer 2026 paper

Fresh searches on 2026-09-17 found a highly relevant paper that the preceding I0079 run did not adequately separate from the Bernoulli-IRE claim:

Matteo D'Achille and Ali Khezeli,
*Convergence towards Ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs*, arXiv:2606.30517 (June 2026; current arXiv v2 surfaced in the dated search).

Important scope facts from the paper:

1. **Vertex-measured graphs.** Their Theorem 1.3 gives phase-parametrized graph IPVT limits. Their Remark 4.8 explicitly warns that in vertex-measured graph IPVTs the fractional phase can be observable; for regular trees this is known in their unrefined IPVT sense.

2. **Poisson versus Bernoulli on the same vertex measure.** Their Lemma 4.9 says low-intensity Poisson and Bernoulli nuclei on a vertex-measured graph have the same subsequential Voronoi limits under the stated square-mass condition.

3. **Edge-measured phase independence.** Their Theorem 1.5 / Theorem 4.14 proves phase independence after restricting an **edge-measured** IPVT to vertices (or vertices and midpoints) under diagonal boundary hypotheses.

4. **Equal two-tree product.** Their Corollary 1.6 applies this edge-measured independence theorem to `T(p) x T(p)`; unequal `T(p) x T(q)` can fail the diagonal condition.

5. **Known cancellation mechanism.** Their Lemma 4.15 proves phase cancellation by a “magic telescopic sum” after introducing the within-edge continuous coordinate.

This is materially closer prior art than was recorded in run 1. It changes the novelty assessment:

- The **abstract cancellation mechanism is not new**. A publication claim must cite D'Achille--Khezeli 2026 and distinguish the model precisely.
- Corollary 1.6 is **not, from the checked text, the same theorem as R06-T1**. It is an edge-measured-nuclei statement restricted to graph vertices; the source I0079 model has Bernoulli nuclei on vertices, with a separate equivariant refinement of distance ties. Lemma 4.9 compares Poisson and Bernoulli for a fixed vertex measure; it does not identify vertex-nucleus BVT with edge-measured PVT.
- Therefore I do **not** reclassify the frozen Bernoulli-IRE result as KNOWN on the evidence checked. I do downgrade novelty to `OVERLAPPING_CLOSE_PRIOR_ART / NOVELTY_UNVERIFIED`.

This distinction also resolves an apparent contradiction: D'Achille--Khezeli can have phase dependence for an unrefined vertex-measured graph IPVT while a particular random genuine-partition refinement can erase the phase at the level of the induced equivalence relation.

Dated query set included:

- `"Convergence towards Ideal Poisson--Voronoi tessellations" products regular trees independence xi`;
- `2606.30517 Bernoulli labels vertices tie breaking`;
- exact source-question phrase `unique ideal Bernoulli Voronoi tessellation`;
- `2511.23317 Theorem 20 theta(0) product regular trees`;
- author/later-paper searches for D'Achille, Khezeli, Jardón-Sánchez, Mellick, Poulin, Wróbel.

No checked source states the exact frozen iid-nucleus-label Bernoulli-IRE theorem. This is bounded negative evidence, not a novelty certificate.

## 5. Move #18 — SAY IT IN ANOTHER LANGUAGE: unfold the geometric delay ladder into Lebesgue measure

The preceding proof used finite-radius boundary signatures. There is a cleaner global coordinate that makes phase cancellation exact before any finite-radius projection.

Let

\[
G=(T_d)^k,\qquad q=d-1,
\]

and suppose a subsequential product-tree boundary intensity has the form supplied by D'Achille--Grebík--Khezeli--Recke--Wilkens (arXiv:2511.23317, Theorem 20):

\[
\mu_c(d\psi,m)
=
\beta^k(d\psi)\,c q^m,
\qquad
\psi\in(\partial T_d)^k,\quad m\in\mathbb Z,
\tag{5.1}
\]

for some phase constant `c>0`. Attach the iid continuous nucleus mark `u in [0,1]`. The marked intensity is

\[
\widehat\mu_c(d\psi,m,du)
=
\beta^k(d\psi)\,c q^m\,du.
\tag{5.2}
\]

Define

\[
\boxed{
 t
 =
 \frac{c}{q-1}
 q^m\bigl(1+(q-1)u\bigr).
}
\tag{5.3}
\]

For fixed `m`, as `u` runs through `[0,1)`, `t` runs through

\[
I_m(c)
=
\left[
\frac{cq^m}{q-1},
\frac{cq^{m+1}}{q-1}
\right),
\]

and

\[
dt=cq^m\,du.
\tag{5.4}
\]

The intervals `I_m(c)`, `m in Z`, partition `(0,infinity)`. Consequently the map

\[
(\psi,m,u)\mapsto(\psi,t)
\]

pushes (5.2) **exactly** to

\[
\boxed{
\beta^k(d\psi)\,dt,
}
\tag{5.5}
\]

which contains no phase `c`.

Thus a marked PPP with any phase `c` can be represented by one and the same phase-free PPP

\[
\Pi\sim\operatorname{PPP}
\left(
\beta^k\otimes\operatorname{Leb}_{(0,\infty)}
\right).
\tag{5.6}
\]

This is the marked-Maharam / exponential-ladder coordinate hidden inside the finite-radius proof and is a coupling version of the telescopic cancellation mechanism in D'Achille--Khezeli Lemma 4.15.

## 6. Move #3 — PROVE SOMETHING STRONGER: the entire winner field is phase-free pathwise

Let `h_psi(v)` be the integer-valued Busemann part of the ideal candidate at vertex `v`. In the original marked representation, a candidate is ranked at `v` lexicographically by

\[
\bigl(m+h_\psi(v),u\bigr).
\tag{6.1}
\]

Multiplying (5.3) by `q^{h_psi(v)}` gives

\[
tq^{h_\psi(v)}
=
\frac{c}{q-1}
q^{m+h_\psi(v)}
\bigl(1+(q-1)u\bigr).
\tag{6.2}
\]

For any integer `r`, the factor

\[
q^r(1+(q-1)u)
\]

runs strictly increasingly through `[q^r,q^{r+1})` as `u` runs through `[0,1)`. Therefore ordinary order of the positive numbers in (6.2) is exactly lexicographic order of `(m+h_psi(v),u)`.

Hence the winning boundary signature at every vertex is

\[
\boxed{
W(v)
=
\arg\min_{(\psi,t)\in\Pi}
 t q^{h_\psi(v)}.
}
\tag{6.3}
\]

The right-hand side contains no phase `c`. The same realization of `Pi` couples **all** phases simultaneously and makes the entire winner field `(W(v))_{v in G}` identical, not merely equal in distribution on one fixed ball.

Local finiteness / existence of the minimum is not asserted from (5.6) alone; it is inherited from the product-tree subsequential-limit theorem, which proves the corresponding finite-competitor property at each vertex. Under that established hypothesis, (6.3) is a pathwise global phase-removal theorem.

### Status of this strengthening

For the frozen two-factor Bernoulli-IRE theorem, (6.3) is a shorter and stronger proof device than run 1's finite-signature calculation.

I do **not** count it as a new source metric point. It is conceptually adjacent to the known 2026 telescopic-cancellation lemma and therefore publication novelty remains unverified.

The same algebra applies to the `k>=2` equal-tree intensity family of arXiv:2511.23317. Whether the resulting `k>=3` Bernoulli-IRE corollary is already implicit in the June-2026 general graph theorem is left for a dedicated source-scope check; I do not promote that extension to a new source theorem in this run.

## 7. I0079-R06-L2 — finite IRE-cylinder continuity of the marked winner map

**Status: PROVED as a deterministic continuity lemma under the hypotheses below.**

Let `S` be a finite vertex set. Let marked candidate configurations `Xi_n` converge locally/vaguely to a marked candidate configuration `Xi` in the product-tree horofunction/delay space. Assume:

1. for every `v in S`, the minimum candidate score is finite;
2. only finitely many candidates have score at most the first nonwinning score cutoff relevant to `S`;
3. whenever two distinct candidates tie in distance score at a vertex of `S`, their continuous marks are distinct.

Then the induced winner identity map on `S`, and hence the equivalence relation

\[
v\sim w\iff W(v)=W(w),
\]

is locally constant at `Xi`.

### Proof

By (1)--(2), there is a finite set `F` of candidates containing every winner at every `v in S` and every candidate capable of replacing a winner under a sufficiently small perturbation. All remaining candidates have a positive score gap from the winners on the finite set `S`.

Within `F`, candidate distance scores on `S` are integer-valued in the graph model. Thus a perturbation sufficiently small in the horofunction/delay topology preserves every strict distance inequality. At a distance tie, condition (3) gives a strictly positive minimum mark gap because there are only finitely many tied competitors in `F`. A sufficiently small perturbation of the marks preserves that order as well.

Therefore every winner identity on `S` is unchanged in a neighborhood of `Xi`. Equality of winner identities is then unchanged, proving local constancy. `QED`

For the ideal marked product-tree process, the finite-competitor property is precisely the local-finiteness input used in the product-tree convergence paper, and iid continuous marks give (3) almost surely. Hence the marked finite IRE cylinder is an a.s. continuity functional of the subsequential marked point process.

This closes the explicit gap recorded in run 1 between Theorem 25's partition encoding and source-level finite IRE cylinders: one can work directly with the marked winner identities on a finite ball instead of trying to reconstruct a cell identity from an edge encoding outside that ball.

## 8. Consequence for the frozen class

Combine:

- product-tree subsequential intensity classification (arXiv:2511.23317, Theorem 20);
- marked point-process convergence / the same marked finite-core used in its Theorem 25;
- global phase unfolding (Sections 5--6 above);
- finite IRE-cylinder continuity L2.

Then every subsequence of Bernoulli intensities tending to zero has a further subsequence whose refined IRE cylinders converge, and every such limit is the same phase-free law (6.3). By compactness of the IRE space, this implies full convergence of the refined BVT IRE for the frozen `T_4 x T_4` class.

Thus the mathematical status remains

\[
\boxed{R_{\rm unique}=+\infty.}
\]

The result is still **audit-gated** and only for the frozen iid-nucleus-label refinement. It does not answer source Question 2 in full and does not assert uniqueness across different equivariant tie-refinement rules.

## 9. Exact-check policy this run

No new finite checker was manufactured because:

- the fixed metric did not move;
- the new statements are global measure-theoretic / deterministic continuity arguments, not finite exhaustive claims;
- the existing exact checker from run 1 already verifies finite-radius phase cancellation for the frozen product-tree model:
  `artifacts/R06/20260916T2121Z_i0079_phase_cancellation_exact.py` and its archived output.

This follows the owner's 90/10 rule: idea first, validation only where it bears on a finite core.

## 10. Independent audit of newest R07 package

Newest R07 package read in full:

`runs/R07/20260916T2124Z_i0077_positive_seam_gauges_05.md`.

Audited theorem: `I0077-R07-T6`, the positive-seam superdiffusive gauge theorem.

### Audit

The theorem assumes continuous nondecreasing `f`, `f(0)=a>0`, and

\[
f(u)/\sqrt{u\log\log u}\to\infty.
\]

The proof has four essential points.

1. **Positive-probability whole-tube Brownian event.** The split at a large deterministic `R` is valid. On `[0,R]` a compact Brownian small-ball event has positive probability. For future increments, the reflection estimate on `[0,R]` plus LIL control on `[R,infinity)` gives the required shifted-tail event with positive probability. The past and future pieces used there are independent.

2. **Recurrence of good reversed terminal times.** Integer re-rooting of two-sided Wiener increments is an ergodic Bernoulli shift. Birkhoff therefore supplies infinitely many whole-past good integer terminal times. The endpoint condition follows eventually from the LIL and the super-LIL growth of `f`. The first qualifying integer is a stopping time; the continuum tube condition is measurable by continuity/rational-time approximation.

3. **Backward concatenation.** Independent Brownian pieces with their own a.s.-finite stopping rules give independent `(B^k,T_k)` pairs. Each `T_k>=1`, so the cumulative splice times diverge in both directions once unit pieces are used on the positive side, matching the decomposable-FBM construction.

4. **Amplitude budget.** With `c=C/2` and `delta_m=C2^{-m-1}`, the accumulated completed-piece displacement is at most `(sum_{j<m}delta_j)f(|t|)` and the within-piece displacement is at most `c f(|t|)`. Monotonicity is sufficient because every earlier completed duration and the current backward time are bounded by `|t|`. The total is at most `Cf(|t|)`.

The `C=0` impossibility argument is immediate from the FBM witness-time definition.

I found no mathematical gap in T6 at its stated scope. There are two harmless markdown typos (`\nrac` where `\frac` is intended) in the displayed inequalities, but they do not alter the proof.

**Verdict:**

`R06-AUDIT-R07-I0077-T6-20260916T2218Z: PASS_SCOPED / NOVELTY_UNVERIFIED`.

Scope: mathematical proof of T6 only. This is not a full audit of Problem 7.8, the five-family metric, or publication novelty.

## 11. Audit/closure state for I0079

Repository search this run found no P26 audit of `I0079-R06-T1` and no second independent OTHER-track audit of the frozen theorem.

Therefore closure is **not** declared. No paper folder is created.

Current proof package now consists of:

- run 1 phase-cancellation theorem and exact finite checker;
- this run's global phase-free PPP coupling;
- this run's finite IRE-cylinder continuity lemma;
- a substantially improved and properly scoped prior-art discussion.

The strongest remaining non-novelty obligation is to determine whether D'Achille--Khezeli 2026 plus their general graph theorem already implies the exact iid-nucleus-label Bernoulli-IRE corollary by a route not stated in their Corollary 1.6. Until that is resolved, novelty remains **UNVERIFIED / CLOSE PRIOR ART**.

## 12. Model / scheduler / permission escalation

The model-control limitation remains unchanged.

The exposed task-control surface provides title, prompt, schedule, enablement, and timing mode, but no model-family selector, no reasoning-effort selector, and no authenticated runtime-model telemetry. Prompt text therefore cannot force or verify GPT-6 / maximum reasoning. Actual runtime for this report is GPT-5.6 Sol; reasoning level is UNVERIFIED.

To change this for real requires either:

1. product/API support for task-level model and reasoning fields plus runtime telemetry;
2. an authorized owner/admin context controlling the task's runtime policy; or
3. platform support.

A `You cannot modify this task` response is an ownership/context boundary. The permitted workaround is the authorized owning context or platform support, not duplication or bypass. No scheduler mutation was attempted.

## 13. Status and next attack

**Source status:** PARTIAL / open-ended.

**Frozen metric:** `+infinity -> +infinity` (no movement).

**Unchanged count:** `1`.

**Mathematical frozen-subclass status:** PROVED / AUDIT_PENDING under the iid-nucleus-label refinement.

**Novelty status:** `UNVERIFIED / CLOSE OVERLAPPING PRIOR ART`; the cancellation mechanism itself is known in D'Achille--Khezeli 2026 for the edge-measured setting.

Next high-value attack is not another checker. It is a scope-separation run:

- determine whether Theorem 1.5 / 4.14 of arXiv:2606.30517 can be functorially transferred from edge-measured nuclei to the source's vertex-Bernoulli nuclei with iid nucleus-label tie refinement;
- if yes, reclassify the frozen theorem as KNOWN and rotate immediately;
- if no, isolate the exact obstruction and then test the equal three-tree product `T_4^3` as a source-unresolved regime using the global unfolding coordinate, but do not refreeze or claim novelty until that status check is complete.

Suggested unused methods for the next run: **#1 CHANGE THE CATEGORY**, **#14 FIND THE GROUP ACTING**, **#30 DO ONE SCALE / ONE DIRECTION AT A TIME**.

## Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  active_source:
    authors: [Hector Jardon-Sanchez, Sam Mellick, Antoine Poulin, Konrad Wrobel]
    work: Exactness and the topology of the space of invariant random equivalence relations
    year: 2026
    locator: Question 2
    intake: I0079
  predecessor:
    intake: I0056
    status: PARTIAL_PRESERVED_ROTATED
  frozen_class: "F_2 x F_2 = T_4 x T_4, l1 product metric; iid continuous nucleus-label tie refinement"
  metric: R_unique
  before: +infinity
  after: +infinity
  movement: NO
  unchanged_count: 1
  methods_this_run: [22, 18, 3]
  status: PARTIAL
  exact_evidence:
    - "I0079-R06-T1 retained: all finite IRE cylinders phase-independent in frozen marked model"
    - "I0079-R06-L2 NEW: finite marked-winner IRE-cylinder continuity lemma"
    - "global marked-ladder unfolding: (m,u) -> t pushes c q^m du exactly to dt"
    - "existing exact checker: artifacts/R06/20260916T2121Z_i0079_phase_cancellation_exact.py"
  prior_art:
    - "D'Achille--Khezeli arXiv:2606.30517 Theorem 1.5 / 4.14 / Corollary 1.6: close edge-measured phase-independence result"
    - "D'Achille--Khezeli Lemma 4.15: known telescopic cancellation mechanism"
    - "not yet found: exact vertex-Bernoulli iid-nucleus-label IRE corollary"
  novelty: UNVERIFIED_CLOSE_OVERLAPPING_PRIOR_ART
  audits:
    own_target_p26: PENDING_NOT_FOUND
    own_target_second_other_track: PENDING_NOT_FOUND
    peer_new: "R06-AUDIT-R07-I0077-T6-20260916T2218Z: PASS_SCOPED / NOVELTY_UNVERIFIED"
  closure: false
  remaining_obligation: "Resolve whether 2606.30517 already implies the exact marked Bernoulli-IRE theorem; obtain P26 and distinct other-track audits if still source-new."
  next_methods: [1, 14, 30]
```
