Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NEW SUCCESSOR ADMITTED, but NO NEW-TARGET METRIC MOVEMENT: `R_TFIK22: 3 -> 3`, supported unchanged count `0 -> 1`; frozen Aldous–Fill I0024 remains `C=1`; status `OPEN / PARTIAL`; methods #11 DUALIZE, #13 FIND WHAT ONLY INCREASES, #15 BREAK THE SYMMETRY ON PURPOSE.**

# R01 — manual admission of the finite 22-edge triangle-free intrinsic-knotting residue

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity first: I0024 remains frozen and is not reopened

I recovered the current R01 state before selecting a successor. The original R01 source remains David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 3.44. The maintained source page was rechecked on 2026-09-19 and still asks literally whether relaxation time admits a characterization **exactly as an infimum over flows**, distinguishing this from the Chapter-4 flow/path inequality that gives only an upper bound.

The frozen R01 solution remains

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

and hence the fixed original metric remains

\[
\boxed{C=1}.
\]

Existing independent source-level mathematical audits remain preserved:

- `R20-AUDIT-R01-I0024-03 = PASS`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

Those audits do not turn bounded prior-art searching into a worldwide priority certificate. I0024 is not reopened. The old R01 FEI assignment remains retired; P03 owns FEI. The later KPS/Nielsen successor reached its six-supported-unchanged terminal handoff and is also not restarted.

The immediately preceding R01 report was

`runs/R01/20260919T0424Z_successor_gate_p0219_owned_p0216_graphon_8_14_19_7d2e1c4a.md`

at commit

`edd7f931ab2d7842822b1894e60de0bb84daf6d1`.

It left R01 in `PENDING_ADMISSION`, with no active successor metric and with methods #8/#14/#19 last used. P0219 had become exclusively owned by native slot `6aa7ebbe26308191a40003a950a2307a`, so R01 correctly stopped mathematical work on it.

## 2. Repository-wide read and lifecycle delta before admission

Before successor research I recovered the current versions of:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the newest own R01 report;
- the current P0219 owner report and claim;
- the newest coordinator/task-health reconciliation;
- material CLOSABLE claim additions, including `ROMERO-2025-SPLIT8` and `VANBERKEL-BOSMA-2026-TS12`;
- intake/source records as needed by exact candidate searches.

The append-only intake corpora are too large for an honest claim that every historical JSONL byte was freshly rendered in this invocation. I make no such claim. Candidate identity, current ownership, source wording, and prior-history exclusions were rechecked directly.

An exact compare from the previous R01 report commit to a captured current head showed more than one hundred intervening commits and no release of a source that R01 could simply inherit. Newly admitted finite CLOSABLE targets in that interval are owner-bound. In particular:

- P0219 is exclusively owned by another native slot;
- `ROMERO-2025-SPLIT8` is exclusively owned by R06;
- `VANBERKEL-BOSMA-2026-TS12` is exclusively owned elsewhere;
- terminal handoffs without explicit release were not treated as free inventory.

I therefore did not duplicate an existing claim.

## 3. Fresh outside-source admission: Kim–Mattman–Oh 2026

The fresh source is:

Hyoungjun Kim, Thomas W. Mattman, and Seungsang Oh, **“Four triangle-free intrinsically knotted graphs with 22 edges”**, arXiv:2609.08891, submitted 2026-09-08.

The source says that the classification of triangle-free intrinsically knotted graphs with 22 edges remains incomplete. Earlier work handles the branches containing a vertex of degree at least five. The remaining source class has all vertex degrees equal to three or four. Kim–Mattman–Oh themselves settle the subcase having eight degree-4 vertices and four degree-3 vertices and obtain exactly four graphs.

Fresh repository searches immediately before claim creation for

- `2609.08891`,
- `intrinsically knotted 22 edges`,
- `KIM-MATTMAN-OH`, and
- the proposed claim ID

returned no earlier repository claim, report, posted package, or owner conflict.

Fresh bounded public/source searches dated 2026-09-19 used the exact title, arXiv ID, author names, `triangle-free intrinsically knotted graphs with 22 edges`, `all vertices degree 3 or 4`, and the remaining degree-profile language. They recovered the 2026 source, earlier degree-at-least-five classification papers, and older spatial-graph surveys, but no later primary source completing the remaining degree-3/4 profiles. Because this source is only eleven days old, that negative search is **not** a worldwide novelty or priority certificate.

I therefore created the canonical create-only claim

`operations/claims/KIM-MATTMAN-OH-2026-TFIK22-D34.md`

at commit

`f118983cb0acf6f734f6450993b1a12cc378e113`.

Status: `CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE`, owner `R01`.

## 4. Exact finite source scope and checker

Let

- `a=n_4` be the number of degree-4 vertices,
- `b=n_3` be the number of degree-3 vertices.

Every graph in the remaining source class has 22 edges, so by the handshake lemma

\[
4a+3b=44.
\tag{4.1}
\]

With `a,b` nonnegative integers, the exact solution set is

\[
\boxed{(a,b)=(2,12),(5,8),(8,4),(11,0)}.
\tag{4.2}
\]

Kim–Mattman–Oh settle `(8,4)`. Thus the exact claimed residue consists of precisely three degree profiles:

\[
\boxed{(n_4,n_3)=(11,0),\ (5,8),\ (2,12).}
\tag{4.3}
\]

I executed an exact integer checker and archived both code and output:

- `artifacts/R01/tfik22_degree_profile_checker_20260919.py`, creation commit `9dbe6df891e7e5bab16c84c6ac332928b3842b73`;
- `artifacts/R01/tfik22_degree_profile_checker_20260919.out`, creation commit `cddf165d30cc8b6611fb48f66e45056f1a83a6f2`.

The archived output is

`[(2, 12, 14), (5, 8, 13), (8, 4, 12), (11, 0, 11)]`

where the third coordinate is total vertex count. This is only a checker for the exact degree-profile reduction, not an intrinsic-knotting classifier.

The new frozen metric is

`R_TFIK22 := number of the three claimed degree profiles whose complete source-valid triangle-free 22-edge IK classification is still unresolved`.

Baseline and current value:

\[
\boxed{R_{\rm TFIK22}:3\longrightarrow3.}
\]

Lower is stronger. A profile counts as resolved only after **all** graphs in that profile are covered by exact positive or negative certificates. Therefore this run is `OPEN / PARTIAL`, unchanged count `0 -> 1` for the new target.

## 5. Method #15 — BREAK THE SYMMETRY ON PURPOSE: the full residue is exactly three finite profiles

The source statement looks like one broad graph-classification problem. Equation (4.1) breaks it into four disjoint degree profiles, and the source removes one of them. No asymptotic or hidden degree case remains inside the all-degree-3/4 branch.

This is useful because the three surviving profiles have different sizes:

\[
(11,0): n=11,\qquad
(5,8): n=13,\qquad
(2,12): n=14.
\]

The smallest profile `(11,0)` is 4-regular and already contains at least one known 22-edge MMIK example, the classical Schwartz graph `G_S`. So the tempting negation “perhaps the three remaining profiles contain no IK graphs” is already false. This is a productive counterexample-first fact: the first task is classification, not emptiness.

**Outcome #15:** the exact source residue is now a three-profile finite problem, and the first profile is known nonempty.

## 6. Method #13 — FIND WHAT ONLY INCREASES: one-step minor frontier at 21 edges

The useful monotone quantity is the number of edges under passage to a proper minor.

Known prior art gives two crucial facts:

1. every intrinsically knotted graph has at least 21 edges;
2. the 21-edge intrinsically knotted graphs are completely classified: they are the fourteen graphs in the `F_triangle(K_7)` family.

This yields the following exact reduction.

### Lemma — one-step minor frontier

Let `G` be a simple 22-edge graph in one of the claimed triangle-free degree-3/4 profiles.

If `G` is intrinsically knotted and is **not** minor-minimal intrinsically knotted, then `G` has a proper intrinsically knotted minor with exactly 21 edges, and that minor belongs to the known fourteen-graph 21-edge IK classification.

Equivalently, if `G` has no 21-edge IK minor, then any proof that `G` is IK automatically proves that `G` is a 22-edge MMIK graph.

### Proof

If `G` is IK and not MMIK, it has a proper IK minor `H`. Proper minor operations cannot increase edge count, so `|E(H)|<=21`. But every IK graph has at least 21 edges. Therefore `|E(H)|=21`. The 21-edge classification then places `H` in the known fourteen-graph family. Conversely, if `G` has no 21-edge IK minor and nevertheless is IK, no proper minor can be IK because every proper minor has at most 21 edges and any 21-edge IK minor would have appeared in the classified family. Hence `G` is MMIK. `QED`

This is a genuine structural compression: **positive classification is one minor step away from a fully known frontier unless the candidate itself is a new 22-edge MMIK graph.**

Older survey literature reported 92 known 22-edge MMIK graphs and computer evidence suggesting no others, but that computational indication is not accepted here as a proof. The 2026 source is precisely evidence that rigorous completion still requires source-valid arguments in the remaining degree-3/4 residue.

**Outcome #13:** all non-minimal positives reduce to a finite known 21-edge minor list; only the 22-edge MMIK survivors need new positive topology.

## 7. Method #11 — DUALIZE: two exact certificate languages

The minor-frontier lemma suggests treating classification as a certificate problem with complementary positive and negative languages.

### Positive certificate language

For a candidate `G`, either:

1. exhibit an explicit deletion/contraction sequence to one of the fourteen known 21-edge IK graphs; because intrinsic knotting is minor-monotone upward, this certifies `G` is IK; or
2. prove directly that `G` is IK. If no 21-edge IK minor exists, the lemma simultaneously identifies `G` as a 22-edge MMIK graph.

### Negative certificate language

A standard sufficient certificate for non-IK is **2-apex**: exhibit vertices `u,v` such that deleting them leaves a planar graph. Planarity can be certified exactly by a planar embedding / Kuratowski-free verification after the source-valid simplifications. Kim–Mattman–Oh also use pair-deletion/restoring arguments: delete two vertices, simplify degree-1/2 structures by restoring edges, and prove the result planar or one of a tightly controlled nonplanar forms.

Thus an exhaustive profile proof does not need one opaque “IK oracle.” It needs a finite ledger in which every candidate is assigned one of:

- known 21-edge IK-minor certificate;
- direct 22-edge MMIK/IK proof;
- 2-apex / planar pair-deletion certificate.

Any survivor lacking all three is precisely where new topology is required.

**Outcome #11:** the classification target is converted into two exact certificate languages plus a sharply isolated 22-edge MMIK residue.

## 8. Counterexample-first pressure test

The first thing I tried to falsify was the easiest possible completion claim: that the remaining three profiles are empty of IK graphs. This fails immediately because the known 4-regular Schwartz graph `G_S` is a 22-edge MMIK graph, lying in profile `(11,0)`.

The second tempting shortcut is to treat the older survey's computer search — which found no 22-edge MMIK graphs beyond 92 known examples — as a complete proof. That also fails the source-valid standard. The survey itself distinguishes computational indication from theorem, and the new 2026 paper supplies rigorous classification work inside one part of the allegedly exhausted degree-3/4 region. Therefore the campaign must not replace the remaining proof obligations by an old computational census receipt.

No source statement has been refuted. The current exact target remains the three-profile classification.

## 9. Prior-art map and what is actually new in this run

The following are **prior art**, not R01 novelty claims:

- the minimum 21-edge theorem for IK graphs;
- the complete fourteen-graph 21-edge IK classification;
- the older degree-at-least-five classification for triangle-free 22-edge IK graphs;
- the Schwartz 4-regular 22-edge MMIK example;
- survey/computer evidence for a 92-graph 22-edge MMIK census;
- Kim–Mattman–Oh's 2026 `(8,4)` classification yielding four graphs.

The new R01 contribution in this run is organizational/structural rather than a solved profile:

1. freeze the exact source remainder as the three profiles `(11,0),(5,8),(2,12)`;
2. establish the one-step 21-edge minor frontier as the natural positive certificate reduction;
3. dualize the future classification into explicit positive-minor/direct-IK versus negative-2-apex certificate languages;
4. create the finite CLOSABLE metric `R_TFIK22` and exact degree-profile checker.

No claim of publication novelty is made for the one-step minor observation; it is elementary once the 21-edge theorem/classification is known.

## 10. What remains and next research triple

The source-valid remaining obligation is exactly:

\[
\boxed{\text{classify every triangle-free 22-edge IK graph in profiles }(11,0),(5,8),(2,12).}
\]

The next run should not write another profile checker. It should begin the actual finite classification, starting from the smallest `(11,0)` 4-regular 11-vertex profile, because that profile is small, known nonempty, and should expose whether the old 92-graph census can be converted into a rigorous exact certificate package.

Fresh next methods:

- **#2 ATTACK THE NEGATION FIRST:** search exact canonical candidates for a graph outside the known 22-edge families; a survivor immediately falsifies “the old known list is complete.”
- **#16 COMPUTE EVERY SMALL CASE:** exact canonical enumeration of triangle-free 4-regular graphs on 11 vertices, followed by exact minor / 2-apex certificates.
- **#20 FIND WHY THE ALGORITHM FAILS:** isolate candidates for which neither a known 21-edge IK minor nor a 2-apex certificate is found; these survivors are the actual topological theorem obligation.

No audit is requested. The package is not complete and the new metric has not moved.

## 11. Model / scheduler-control truth

The current scheduler/runtime situation is unchanged from the operative implementation record. The exposed task-control surface provides task identity/title/prompt, scheduling/timing, enablement and related metadata, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed hour-long execution control**.

Therefore `GPT-6 / maximum` remains a prompt request on this surface. The actual model available to this run identifies as GPT-5.6 Sol; reasoning telemetry is unavailable, hence `UNVERIFIED`.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary. A later authorized context succeeded. The lawful way to bind a model/reasoning setting or modify an inaccessible task is an owning/authorized product/workspace/API/admin surface or platform support that exposes those fields; prompt text, duplicate schedules, and permission bypass are not substitutes. No scheduler or permission mutation was attempted here.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R01
  lane: CLOSABLE_OUTSIDE
  frozen_original:
    id: I0024
    source: Aldous-Fill Open Problem 3.44
    metric: smallest_uniform_flow_characterization_distortion_C
    before: 1
    after: 1
    lifecycle: FROZEN_DO_NOT_REOPEN
    audits:
      - R20-AUDIT-R01-I0024-03
      - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
    prior_art_novelty: UNVERIFIED
  successor:
    id: KIM-MATTMAN-OH-2026-TFIK22-D34
    source: "Kim, Mattman, Oh (2026), Four triangle-free intrinsically knotted graphs with 22 edges, arXiv:2609.08891"
    status_before: PENDING_ADMISSION
    status_after: OPEN_PARTIAL_CLAIMED_MANUALLY_ADMITTED
    claim_path: operations/claims/KIM-MATTMAN-OH-2026-TFIK22-D34.md
    claim_commit: f118983cb0acf6f734f6450993b1a12cc378e113
    exact_profiles:
      - [11, 0]
      - [5, 8]
      - [2, 12]
    metric_name: R_TFIK22
    metric_definition: number_of_the_three_claimed_degree_profiles_not_yet_completely_classified
    metric_before: 3
    metric_after: 3
    moved: false
    unchanged_count_before: 0
    unchanged_count_after: 1
    tried_moves:
      - 11_DUALIZE
      - 13_FIND_WHAT_ONLY_INCREASES
      - 15_BREAK_THE_SYMMETRY_ON_PURPOSE
    remaining_obligation: "complete exact triangle-free 22-edge IK classification in profiles (11,0), (5,8), (2,12)"
    finite_evidence:
      checker: artifacts/R01/tfik22_degree_profile_checker_20260919.py
      checker_commit: 9dbe6df891e7e5bab16c84c6ac332928b3842b73
      output: artifacts/R01/tfik22_degree_profile_checker_20260919.out
      output_commit: cddf165d30cc8b6611fb48f66e45056f1a83a6f2
    theorem_evidence:
      - "one-step minor frontier: a non-MMIK 22-edge IK graph has a classified 21-edge IK minor"
    prior_art_search_date: 2026-09-19
    prior_art_scope: BOUNDED_NOT_WORLDWIDE_CERTIFICATE
    audits: []
    p26_audit: NOT_REQUESTED_PACKAGE_INCOMPLETE
    second_audit: NOT_REQUESTED_PACKAGE_INCOMPLETE
  next_methods:
    - 2_ATTACK_THE_NEGATION_FIRST
    - 16_COMPUTE_EVERY_SMALL_CASE
    - 20_FIND_WHY_THE_ALGORITHM_FAILS
  github_only: true
  shared_root_edits: none
  email_drive_public_scheduler_permission_actions: none
```
