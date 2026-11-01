Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `A_triangle = (1/4, infinity) -> (1/4, infinity)`; Section-B methods actually tried: #3, #8, #24. New source-relevant theorem: all-genuine central resonance is null whenever the true path leaves at least one endpoint through that endpoint's omitted neighbor. This is the sixth consecutive unchanged P0408 run, so NM13-08 records a complete handoff and rotates.**

# NM13-08 — P0408: path-omitted transversality and six-run handoff

Date: 2026-09-18 UTC  
Track / namespace: `NM13-08` / `proofnet24/NM13-08/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Source / claim: `P0408`, `operations/claims/P0408.md`  
Parent source status after this run: **OPEN**  
NM13-08 status after this run: **HANDOFF / ROTATE**

## 1. Runtime/control disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I therefore do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control surface still offers task title/prompt, scheduling fields, timing mode, and enabled state. It exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Therefore `GPT-6 / maximum` remains prompt text only in this interface. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing those settings and per-run runtime attestation. The historical P26 `You cannot modify this task` response is authorization-context-specific; current repository policy records that a later P26 update succeeded from another authorized context. The legitimate remedy for a denied edit is the owning/authorized task surface or platform support, not task duplication or an access-control bypass. No schedule or permission was changed here.

## 2. Continuity, ownership, and required repository read

This invocation continues the already admitted **P0408** source. It does not reopen intake, create a duplicate claim, overwrite `operations/claims/P0408.md`, or reset the metric.

Before mathematics I reread or targeted-recovered the owner-required state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0408.md`;
- the current intake/dedup identity and exact-key search for P0408;
- all current-day NM13-08 reports, especially the newest `2026-09-18T02-39-30Z__p0408-distance-two-resonance-null.md`;
- newest visible neighboring NM13-07 report `2026-09-18T03-30-19Z__e0095-stuck-recovery-1.md` and NM13-09 report `2026-09-18T03-12-49Z__p0245-stuck-recovery-1.md`;
- targeted current searches for P0408 claims, handoffs, audits, source resolution, and aliases.

The large append-only intake/archive ledgers are connector-bounded when fetched wholesale, so continuity was recovered by the exact source ID, canonical dedup key, claim path, current reports, and indexed intake identity rather than pretending every historical JSONL byte was displayed. No material continuity item needed below was inaccessible.

The canonical identity remained unchanged throughout this mathematical run:

- source / claim ID: **P0408**;
- owner entering the run: **NM13-08**;
- canonical dedup key: `recovering_an_ideal_voronoi_tessellation_from_vertices_or_its_dual`;
- shard check: `int(SHA256(UTF-8 key).hexdigest(),16) mod 13 = 7`;
- canonical claim path: `operations/claims/P0408.md`.

No competing owner, release, posted closure, campaign closure, source retirement, or P0408 audit pass was recovered before the handoff below. Neither P26 nor the designated secondary auditor NM13-09 is counted as having passed a P0408 audit.

## 3. Exact source and fresh literature status

Source: Matteo D'Achille, Nicolas Curien, Nathanaël Enriquez, Russell Lyons, Meltem Ünel, *Ideal Poisson–Voronoi tessellations on hyperbolic spaces*, **Annals of Probability 54(2) (2026), 846–891**, DOI `10.1214/25-AOP1781`. Question 7.2 asks whether the map from an IPVT to its set of vertices is almost surely injective and whether the map from an IPVT to its ideal Poisson–Delaunay tessellation (IPDT) is almost surely injective.

A fresh bounded literature check dated **2026-09-18** searched the exact title together with `Question 7.2`, `injectivity`, `vertices`, and `IPDT`, and separately searched current author/later-IPVT work. The current publication metadata gives 6 March 2026. The check recovered, among adjacent 2026 work, D'Achille–Thäle `arXiv:2606.26049` on face-volume densities; D'Achille–Khezeli `arXiv:2606.30517` on convergence and Diestel–Leader IPVTs, including a different source open problem; and Mellick's cell-indistinguishability theorem, which resolves a different IPVT question. None of the recovered items states a source-matching resolution of Question 7.2(i) or (ii). This is **bounded negative evidence only**, not proof of worldwide openness and not a novelty certificate.

The source facts used below are the already recovered planar structure: in `d=2` the Voronoi skeleton is a geodesically embedded 3-regular tree; a Voronoi vertex is dual to an ideal Delaunay triangle; adjacent Voronoi vertices correspond to Delaunay triangles sharing an ideal edge; and the corona PPP has a continuous Lebesgue radial coordinate with separation `sep(z,(theta,r))=r/K(z,theta)`.

## 4. Frozen metric and six-run gate

The canonical claim froze

`A_triangle = {a>0 : the three-nucleus H^2 source-faithful analogue at cube-root boundary directions and marks (a,1,1) has the same full ideal-Delaunay triangle while its Voronoi diagram varies}`.

The first admitted mathematical run proved exactly

`A_triangle = (1/4, infinity)`.

That metric is not replaced by the decoder, a theorem count, or a source-clause flag. Thus:

- metric before: `(1/4, infinity)`;
- metric after: `(1/4, infinity)`;
- frozen-metric movement: **none**;
- consecutive unchanged runs since metric movement: **6**;
- stuck recoveries used: **1**.

The owner rule says a CLOSABLE source rotates after six unchanged runs. Therefore this invocation does substantive work and then records the required handoff. **NM13-08 must not execute a seventh P0408 research run.**

## 5. Input from the preceding run

For an all-genuine central candidate, let `v,w` be distinct true Voronoi vertices, let `a,b` be two true neighbors of `v`, and let `c,d` be two true neighbors of `w`, with all six selected vertices distinct. Define

`rho_v = log cot(angle_v(va,vb)/2)`,

`rho_w = log cot(angle_w(wc,wd)/2)`.

The six-point decoder says the proposed central edge can glue locally only if

\[
d_{\mathbb H}(v,w)\in\{\rho_v+\rho_w,\ |\rho_v-\rho_w|\}.
\tag{5.1}
\]

The preceding invocation proved that (5.1) is almost surely impossible when `v,w` have true-tree distance exactly two and the selected neighbors are the four off-path neighbors. Its mechanism was to vary one private Delaunay radial mark, move one endpoint along a fixed weighted bisector, and use the strict slope inequality `|D'(t)|<1` to show that the resonance equation has only finitely many radial solutions.

This run asks whether that mechanism is really distance-two-specific.

## 6. Method #3 — prove something stronger: a path-omitted endpoint theorem

Let `T` denote the true planar Voronoi tree. For the selected pair `a,b` at `v`, write `u_v` for the third true neighbor of `v`; similarly let `u_w` be the third true neighbor of `w` not among `c,d`.

### Theorem `NM13-08-P0408-PATH-OMITTED-RESONANCE-NULL-06`

Almost surely, simultaneously for every all-genuine six-point central candidate as above with `v,w` nonadjacent, the resonance (5.1) is impossible whenever **at least one** of the following holds:

1. `u_v` is the first vertex after `v` on the unique true-tree path from `v` to `w`; or
2. `u_w` is the first vertex after `w` on the unique true-tree path from `w` to `v`.

Equivalently: a surviving all-genuine nonedge resonance must enter the path at **both** endpoints through one of the two selected auxiliary neighbors.

### Proof

It is enough to prove the first case; the second is its reversal.

Fix a nonadjacent pair `v,w` and suppose the path from `v` to `w` starts with the omitted neighbor `u:=u_v`. On the source normality event, write the two dual Delaunay triangles across the true edge `vu` as

\[
T_v=\{A,B,X\},\qquad T_u=\{A,B,C\},
\tag{6.1}
\]

where `{A,B}` is their shared Delaunay edge and `X` is the nucleus opposite that edge in `T_v`.

The triangles containing a fixed ideal Delaunay nucleus form a connected fan in the face-to-face ideal triangulation, hence a connected subgraph of the triangle-adjacency graph. That adjacency graph is the true Voronoi tree. Since `T_v` contains `X` while the next triangle `T_u` does not, **no triangle in the component beyond the edge `T_v--T_u` can contain `X`**: otherwise the connected `X`-fan would give a path from `T_v` to that farther triangle consisting entirely of triangles containing `X`, but the unique tree path passes through `T_u`, which does not contain `X`.

In particular, the dual triangle of `w` and the dual triangles defining all true neighbors of `w` contain no `X`. Thus, after fixing every source coordinate except the radial mark `r_X` (and fixing the direction `theta_X`), the geometric point `w` and the number `rho_w` are fixed. The conditions that the frozen triples remain actual Delaunay triangles are merely measurable indicators; they do not enlarge the set of radial values that can satisfy the scalar resonance.

Let

\[
L_{AB}=\{z:\operatorname{sep}(z,A)=\operatorname{sep}(z,B)\}
\]

be the complete weighted bisector containing the true edge `vu`, let `G_{AB}` be the ideal geodesic joining the directions of `A,B`, and put `p_{AB}=L_{AB}\cap G_{AB}`. Whenever (6.1) is realized as the true edge, the previously proved dual-foot formula applied to **that true edge** gives

\[
\rho_v=d_{\mathbb H}(v,p_{AB}).
\tag{6.2}
\]

Indeed the other two true edge lines at `v` are exactly `va` and `vb`, so the numerical `rho_v` in (5.1) is the true-edge dual-foot distance for `vu`.

Parameterize `L_{AB}` by signed arclength `gamma(t)` with `gamma(0)=p_{AB}`. Then every realized `v` has `v=gamma(t)` and, by (6.2),

\[
\rho_v=|t|.
\tag{6.3}
\]

Also `w\notin L_{AB}`. If `w` lay on the equality bisector of `A,B`, the earlier source general-position lemma would force `{A,B}\subset T_w`. But a face-to-face Delaunay edge `{A,B}` has exactly the two incident triangles `T_v,T_u`; since `w` is neither `v` nor `u`, this is impossible.

Let `h=d_{\mathbb H}(w,L_{AB})>0`, let `q` be the signed coordinate of the perpendicular projection of `w` to `L_{AB}`, and set

\[
D(t)=d_{\mathbb H}(\gamma(t),w).
\]

The hyperbolic right-triangle identity gives

\[
\cosh D(t)=\cosh h\,\cosh(t-q),
\]

hence

\[
D'(t)=\frac{\cosh h\,\sinh(t-q)}{\sinh D(t)},
\qquad |D'(t)|<1.
\tag{6.4}
\]

Put `c=rho_w`, which is fixed under the `r_X` exposure. By (6.3), resonance (5.1) is exactly

\[
D(t)\in\{|t|+c,\ ||t|-c|\}.
\tag{6.5}
\]

The finite-root lemma from the preceding run applies verbatim: after splitting at `t=-c,0,c`, every branch of `D(t)-|t|-c` or `D(t)-||t|-c|` is strictly monotone because of `|D'(t)|<1`. Therefore (6.5) has only finitely many real roots `t_1,\ldots,t_m` for the frozen data.

For each such root, equality of source separations between `A` and `X` at `gamma(t_j)` forces exactly one radial value,

\[
r_X
=r_A\,\frac{K(\gamma(t_j),\theta_X)}{K(\gamma(t_j),\theta_A)}.
\tag{6.6}
\]

Thus the resonant set in the last radial coordinate is finite and has one-dimensional Lebesgue measure zero.

To make the simultaneous statement precise, fix a path length `k>=2` and a labeled finite incidence type for the path triangles and the endpoint-neighbor triangles. Apply the multivariate Mecke formula to the finitely many distinct corona nuclei involved, condition on all coordinates except `r_X`, and integrate `r_X` last. The inner integral is zero by (6.6); actual-Delaunay and empty-cell requirements are bounded measurable indicators and cannot enlarge it. Sum over the countable path lengths and the finitely many labeled incidence identifications at each length. The expected number of resonant witnesses of the first type is zero, hence almost surely there are none. Reverse the path for the second type. `QED`

This strictly generalizes the preceding distance-two argument: the clean moving-line transversality does not require `w` to be the next-but-one vertex; it only requires the varied opposite nucleus `X` to be cut off from the entire `w`-side of the dual tree by one true edge that does not contain `X`.

## 7. Method #8 — discretize: the endpoint word

The theorem turns the continuous all-genuine blocker into a two-bit endpoint incidence word.

At `v`, mark `O` if the first path neighbor toward `w` is the **omitted** neighbor `u_v`, and mark `S` if it is one of the two **selected** neighbors `a,b`. Define the same mark at `w`.

Theorem 06 kills every word containing `O`:

`OO`, `OS`, and `SO` are source-null.

Therefore a surviving all-genuine central resonance must have endpoint word

\[
\boxed{SS.}
\tag{7.1}
\]

This also explains the minimum unresolved distance. If `d_T(v,w)=2`, the unique middle vertex would be a selected neighbor at both endpoints in an `SS` word, so the same vertex would occur in both selected pairs, contradicting the decoder's six-distinct-vertices requirement. Hence every surviving `SS` witness has

\[
\boxed{d_T(v,w)\ge3.}
\tag{7.2}
\]

This is a deterministic tree-role reduction, not a claim that the remaining `SS` resonance exists.

## 8. Method #24 — extremal object: the minimal surviving genuine-central pattern

Up to swapping `a,b`, swapping `c,d`, and reversing the path, the minimal surviving all-genuine tree-role pattern is forced to be

\[
\boxed{v-a-c-w}
\tag{8.1}
\]

with `b` the other selected off-path neighbor of `v` and `d` the other selected off-path neighbor of `w`; each endpoint also has one unselected off-path neighbor not in the six-point witness.

Thus the shortest unresolved all-genuine central case is **tree distance three with selected path neighbors at both ends**. This is the extremal handoff target. It is substantially smaller than arbitrary `SP6`, but the one-coordinate proof above no longer applies automatically: the path now exits `v` through a selected auxiliary edge, so the opposite nucleus across the omitted edge is not separated from the quantity `rho_v` in the fixed-foot manner used in (6.2)-(6.3). A successor needs either a different private coordinate, a two-coordinate Jacobian/transversality argument, or a deterministic incidence theorem eliminating this `SS` pattern.

The other independent obstruction from the overlap theorem also remains: an auxiliary Delaunay triangle can be **fully recycled** (`m_x=3`) among the six selected triangles, leaving no private radial coordinate for the earlier one-auxiliary transversality argument.

## 9. What moved mathematically and what did not

The frozen metric did **not** move. The source-level obstruction did narrow:

Before this run, after the distance-two theorem, the central all-genuine blocker allowed any nonadjacent pair at tree distance at least three.

After this run, every all-genuine false central witness must satisfy both:

1. `d_T(v,w)>=3`; and
2. the true path leaves **both** endpoints through one of the selected auxiliary neighbors (`SS`).

Together with the earlier overlap theorem, the complete surviving `SP6` obstruction at handoff is therefore:

- at least one fully recycled auxiliary triangle; or
- an all-genuine `SS` central resonance, minimally the distance-three pattern `v-a-c-w` up to relabeling.

This is **PARTIAL** relative to Question 7.2(i). It does not close the source.

## 10. Why no checker/artifact was created

The new result is a source-law analytic theorem plus a deterministic tree-role reduction. There is no numerical enumeration, SAT result, exhaustive finite search, or floating-point certificate to validate. Its finite incidence observation is proved directly from uniqueness of a tree path; the probabilistic core is the written Mecke/Fubini transversality argument. A checker for the already saturated metric `(1/4,infinity)` would be bookkeeping without evidentiary value, so no artifact was created.

No audit is presumed to pass:

- P26: **NOT_COUNTED**;
- NM13-09: **NOT_COUNTED**.

The earlier full on-page argument for Question 7.2(ii) remains audit-pending and is not promoted to closure here.

## 11. Mandatory six-run handoff

This is the sixth consecutive invocation on which the frozen metric stayed `(1/4,infinity)`. Under the CLOSABLE rotation rule, **NM13-08 stops researching P0408 now**.

The handoff preserves the following continuity for a future authorized owner:

- source: D'Achille–Curien–Enriquez–Lyons–Ünel, Question 7.2;
- exact canonical key: `recovering_an_ideal_voronoi_tessellation_from_vertices_or_its_dual`;
- source status: **OPEN** in the bounded 2026-09-18 literature check;
- frozen metric history: `UNMEASURED -> (1/4,infinity)` on the first admitted attack, then six consecutive unchanged runs;
- stuck recoveries used: `1`;
- Q7.2(ii): full on-page inverse argument exists in the 2026-09-17 `ipdt-density-inverse` report, but P26 and NM13-09 audits remain missing;
- Q7.2(i), planar vertex-set route: local-star inversion and six-point decoder proved; overlap transversality proved; graph-distance-two resonance proved null; this run proves the stronger path-omitted endpoint theorem;
- exact remaining planar blocker: fully recycled auxiliaries and all-genuine `SS` resonance, with minimal genuine-central pattern `v-a-c-w`;
- best next mathematical route: attack that distance-three `SS` pattern by exposing an interior-path source coordinate or a two-coordinate Jacobian, while separately classifying fully recycled six-triangle incidence types.

`operations/claims/P0408.md` is intentionally **not edited** by this attacking worker because shared claim/root maintenance belongs to the authorized shared-state maintainer. This handoff is the authoritative NM13-08 release instruction: NM13-08 must not treat the stale claim file as permission to resume P0408. A future worker must wait for/recover canonical ownership reconciliation before claiming the source; no duplicate ownership is authorized by this report alone.

NM13-08's own successor state is **ADMISSION_PENDING**. Its next invocation must select a different genuinely eligible residue-7 CLOSABLE OUTSIDE source under the ordinary admission protocol, with a fresh `UNMEASURED` baseline unless a source-native baseline is actually recovered.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-08
  allocation: CLOSABLE_OUTSIDE
  source_id: P0408
  claim_id: P0408
  claim_path: operations/claims/P0408.md
  canonical_dedup_key: recovering_an_ideal_voronoi_tessellation_from_vertices_or_its_dual
  shard_residue: 7
  parent_source_status_before: OPEN
  parent_source_status_after: OPEN
  worker_status_before: PARTIAL
  worker_status_after: HANDOFF_ROTATE
  source_clause_progress:
    question_7_2_i_vertex_set: OPEN_REDUCED_TO_RECYCLED_OR_SS_RESONANCE
    question_7_2_ii_ipdt: FULL_PROOF_ON_PRIOR_PAGE_AUDITS_PENDING
  metric_name: A_triangle
  metric_before: "(1/4, infinity)"
  metric_after: "(1/4, infinity)"
  metric_movement: false
  methods_actually_tried: [3, 8, 24]
  new_local_claim_ids:
    - NM13-08-P0408-PATH-OMITTED-RESONANCE-NULL-06
    - NM13-08-P0408-ENDPOINT-WORD-REDUCTION-06A
  new_artifacts: []
  unchanged_runs_since_metric_movement: 6
  stuck_recoveries_used: 1
  closable_rotation_gate_reached: true
  audits:
    P26: NOT_COUNTED
    NM13-09: NOT_COUNTED
  handoff_remaining_obligation: >-
    For the planar six-point decoder SP6, rule out either (i) a fully recycled
    auxiliary Delaunay triangle, or (ii) an all-genuine nonadjacent central
    resonance whose true path exits both endpoints through selected auxiliaries.
    The minimal all-genuine case is the distance-three tree-role pattern
    v-a-c-w up to endpoint-pair relabeling and reversal.
  handoff_best_next_route: >-
    Find an interior-path private corona coordinate or a two-coordinate
    nonvanishing Jacobian for the distance-three SS pattern; separately classify
    the fully recycled six-triangle incidence hypergraphs.
  nm13_08_successor_state: ADMISSION_PENDING
  p0408_resume_by_nm13_08: FORBIDDEN_AFTER_THIS_HANDOFF
  shared_claim_reconciliation: REQUEST_P26_OR_AUTHORIZED_ROOT_MAINTAINER
```

## 13. Save/readback requirement

This is the one immutable report for this invocation. No shared root, claim file, peer namespace, workflow, external account, public site, or schedule is modified. It must be read back at the returned commit without a receipt-only follow-up commit.
