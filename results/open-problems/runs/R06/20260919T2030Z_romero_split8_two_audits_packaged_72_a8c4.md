Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. FIXED I0056 NO MOVEMENT / AUXILIARY CLOSURE MOVEMENT: frozen `H_{5,5}` interval width `0 -> 0`; `ROMERO-2025-SPLIT8` mathematical metric `0 -> 0`; Romero distinct-audit gate `1/2 -> 2/2`; required paper package `ABSENT -> CREATED`; successor-admission metric `E_ready: 0 -> 0`; methods #2 ATTACK THE NEGATION FIRST, #10 DERANDOMIZE, #24 FIND THE EXTREMAL OBJECT.**

# R06 CLOSABLE OUTSIDE — Romero finite-layer closure transition, package created, no free successor admitted

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Worker: R06.
Lane: CLOSABLE OUTSIDE.
Date checked: 2026-09-19 UTC.

## 1. Continuity: original R06 source remains frozen and PARTIAL

The controlling predecessor is

`runs/R06/20260919T1921Z_successor_gate_p0434_owned_p0063_closed_no_free_71_b6e4.md`

created at commit

`dbbebd80168f4a6f2f9cd5d8b84ee46e644a6daa`.

I preserve the exact original R06 source and metric:

- source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056;
- exact first-clause class: regular, co-regular plane graphs;
- frozen graph/regime: regular co-regular tessellation `H_{5,5}` / Schlaefli `{5,5}`;
- parameters: vertex degree `d=5`, face degree/codegree `f=5`;
- normalization: outer vertex boundary
  \[
  \Phi_V(G)=\inf_{\varnothing\ne K\subset V,\ K\text{ finite}}\frac{|\partial_VK|}{|K|};
  \]
- retained certified value:
  \[
  \Phi_V(H_{5,5})=\sqrt5,
  \qquad [L,U]=[\sqrt5,\sqrt5],
  \qquad U-L=0.
  \]

The maintained Lyons--Peres edition still states Question 6.20 exactly as:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

Therefore the solved `H_{5,5}` subclass remains **PARTIAL for the full Question 6.20**. The source's current annotation records Haslegrave--Panagiotis only for codegrees `3` and `4`; their paper, DOI `10.1002/rsa.20946`, establishes the exact vertex-isoperimetric constants for triangular and square hyperbolic lattices. Those regimes remain prior art and are not relabelled as R06 results.

Root `POSTED.md` also records *Outer Vertex-Isoperimetry of Regular Plane Tessellations* in the owner's 18 September ResearchGate snapshot, publication ID `414470838`. Posting is not an audit, but it reinforces the exclusion against reopening this frozen predecessor as new research.

Preserved I0056 audits remain:

- `R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`;
- `P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`.

No I0056 theorem is rederived in this invocation.

## 2. Required repository refresh and exact delta

Before the closure transition I refreshed/recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the operative follow-up implementation manifest, the newest own R06 report, current coordinator/task-health state, current canonical claims material to admission, the newest P13 successor screen, P26 audit/reconciliation evidence, and the new R01 neighboring audit.

The append-only intake JSONL corpus is too large to claim that every unchanged row was freshly rendered model-visible. I do not make that claim. Candidate-specific records were reopened where material, and the complete Git comparison below establishes the actual repository delta after the prior R06 report.

Frozen pre-package head:

`e718031a3401ca195076e61def1e3971800b2a04`.

Exact comparison

`dbbebd80168f4a6f2f9cd5d8b84ee46e644a6daa .. e718031a3401ca195076e61def1e3971800b2a04`

returns:

- status: `ahead`;
- commits ahead: **117**;
- commits behind: **0**;
- `too_large = null`.

The decisive changed file is

`runs/R01/20260919T2000Z_romero_split8_second_audit_20_27_30_5c8e2a71.md`.

A second material lifecycle record is P26's late reconciliation sidecar

`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-19/2026-09-19_22-57-43__ledger-sidecar.md`.

The delta also contains a newly admitted finite CLOSABLE target, `SHPECTOROV-ZHAO-2026-SRG69`, but its canonical claim says `CLAIMED / ADMITTED_ACTIVE / CLOSABLE OUTSIDE` and assigns it to native slot `6aa7b46f70a8819184095c277974c256`; it is not free R06 inventory. The newest coordinator and P13 screens continue to report zero newly certified free READY CLOSABLE entries.

## 3. Genuine second audit arrived: Romero gate 1/2 -> 2/2

R01 has now supplied the missing genuinely distinct OTHER-task audit of the complete claimed finite layer:

`R01-AUDIT-R06-ROMERO-SPLIT8-N8-01 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_MATCH_N8_LAYER / INDEPENDENT_EXACT_CORE_PASS / PRIOR_ART_BOUNDED_NEGATIVE / PUBLICATION_PRIORITY_UNVERIFIED`.

Report:

`runs/R01/20260919T2000Z_romero_split8_second_audit_20_27_30_5c8e2a71.md`

creation commit

`9c44bb6e9a3a82242652e025e60669edf7e03b2d`.

R01 is distinct from both owner R06 and auditor P26. It recorded its route before code, wrote fresh independent C code rather than copying the owner checker, and archived output ending

`R01_ROMERO_SPLIT8_INDEPENDENT_EXACT_AUDIT_PASS`.

R01 independently reconstructed the full claim:

### Sparse half, `m=14,...,19`

It recomputed the exact two-forest / Matrix--Tree comparisons

| `m` | balloon `N_6` | competitor `N_6` | gain |
|---:|---:|---:|---:|
| 14 | 840 | 900 | 60 |
| 15 | 1404 | 1440 | 36 |
| 16 | 2160 | 2592 | 432 |
| 17 | 3024 | 3780 | 756 |
| 18 | 5292 | 5880 | 588 |
| 19 | 8232 | 8575 | 343 |

and checked graph size, edge count, connectivity, the appropriate diameter-terminal balloon, and the small-`p` contradiction to Romero's local-optimum characterization.

### Dense half, `m=20,...,26`

It independently reconstructed terminal-fixed complement orbits under `S_6`, verified exact orbit--stabilizer totals, rederived the connected-spanning-subgraph recurrence, and checked coefficientwise domination for every connected representative. It reproduced:

| `m` | connected terminal-fixed orbits | ties with balloon coefficient vector | violations |
|---:|---:|---:|---:|
| 20 | 6852 | 4 | 0 |
| 21 | 3018 | 2 | 0 |
| 22 | 1189 | 2 | 0 |
| 23 | 419 | 2 | 0 |
| 24 | 137 | 2 | 0 |
| 25 | 43 | 2 | 0 |
| 26 | 13 | 2 | 0 |

It explicitly attacked the failure modes most capable of invalidating the finite proof: a wrong two-terminal quotient, omitted complement orbits, disconnected leakage, recurrence error, invalid exchange of graph/probability quantifiers, integer overflow, Matrix--Tree minor/sign error, and scope inflation. No defect survived.

The already-existing first full audit is

`P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64 = PASS_FULL_MATHEMATICAL_PROOF / CLAIM_SCOPED_N8 / EXACT_FINITE_CORE_PASS / SOURCE_PARTIAL_OPEN / PRIOR_ART_BOUNDED_NEGATIVE`.

P26's new late sidecar now explicitly reconciles the pair and records

`P26-RECONCILE-R06-ROMERO-SPLIT8-N8-2OF2-76 = PASS / DISTINCT_AUDITORS_P26_PLUS_R01 / OWNER_R06_EXCLUDED / SOURCE_SCOPE_COMPLETE_N8_LAYER_ONLY / EXACT_FINITE_CORE_BOTH_AUDITS_PASS / PRIOR_ART_BOUNDED_NEGATIVE / PUBLICATION_PRIORITY_UNVERIFIED`.

Thus the finite-layer gate moves rigorously

\[
\boxed{1/2\to2/2.}
\]

This does **not** close the unrestricted all-`n` Romero/Brown--McMullin source problem. The exact closed scope is only

\[
n=8,\qquad m=14,15,\ldots,26.
\]

## 4. Closure theorem retained exactly

The internally closed finite theorem is:

\[
\boxed{
\begin{array}{ll}
14\le m\le19:&\text{no uniformly most split reliable graph exists in }T_{8,m},\\[1mm]
20\le m\le26:&\text{a diameter-terminal balloon is uniformly most split reliable in }T_{8,m}.
\end{array}}
\]

The sparse half uses the all-minors Matrix--Tree theorem to identify the first possible split coefficient `N_6` with a two-root Laplacian minor. In every sparse class an explicit competitor has strictly larger `N_6`; because all lower split coefficients vanish on eight vertices, it beats the balloon for sufficiently small positive `p`. Romero's local characterization then rules out any uniform maximizer.

The dense half writes

\[
\SR_G(p)=\sum_jN_j(G)p^j(1-p)^{m-j}
\]

and proves `N_j(B)>=N_j(H)` for every coefficient and every graph `H` in the complete terminal-fixed orbit list. Since every basis function is nonnegative on `[0,1]`, coefficientwise domination implies uniform split-reliability domination for all `p`.

No sampled-`p` argument is used.

## 5. Required paper package created

Because both independent audit gates now pass, the repository protocol requires a source-matching paper folder. I created

`paper_romero_split8_n8_layer/`

with:

- `README.md` — creation commit `508aff5e5a65474489517cc62d20f77857a92b0c`;
- `main.tex` — creation commit `a9d7483074a4b8ad22c302393b1ed3f04cf6035b`, then a TeX filename-escaping / balloon-definition repair at `e943bf6ea469f530d655c155bec99116667fe240`;
- `check_sparse.py` — commit `5061be550506665e44d01e6f84c7e55244f3ebcb`;
- `check_sparse.out` — commit `934fa81c23786f3b88d3f9c736c44ce61ae012fe`;
- `check_dense.c` — commit `685f2306109c4273bfb69802849334961b4dd011`;
- `check_dense.out` — commit `d7469f6c52b6e1fcbef74f37c50a068e008ac2a1`.

Every file was read back at its returned commit.

The package deliberately reuses the already executed and audited exact finite cores rather than manufacturing a new checker merely because closure occurred. Blob identity confirms byte-for-byte reuse:

- packaged `check_sparse.py` blob = owner sparse checker blob `2da21c8fa13da1652bfb57dc355d38d849ab981d`;
- packaged `check_sparse.out` blob = owner sparse output blob `40f69d65cc1a0848845ce4a4e6762eb83a292b10`;
- packaged `check_dense.c` blob = owner dense checker blob `7b28fc2fc36b298c96d11c745755b95300475ffb`;
- packaged `check_dense.out` blob = owner dense output blob `2124eb4afdd6a4728d9f7294226892299b33c41b`.

`main.tex` contains a theorem-sized proof, not a sketch: source reduction, explicit sparse witnesses and exact determinant table, proof of the connected-spanning-subgraph recurrence, proof of orbit-generation completeness, exact dense table, and the coefficientwise-to-uniform quantifier step. The README states exactly what Romero's source asked, exactly what the finite package proves, the two independent audit IDs, and the bounded prior-art qualification.

Internal lifecycle label for this exact finite package is now

\[
\boxed{\text{PROVED / AUDIT-COMPLETE / PACKAGED}.}
\]

This is not a claim of journal acceptance, external peer review, or resolution of all remaining source cases.

## 6. Dated source and prior-art check

Fresh 2026-09-19 web/source queries included:

- `Pablo Romero "Characterization of locally most split reliable graphs" 2026 split reliability T 8 m`;
- `"2503.15453" split reliability Romero 2026`;
- exact-title/author/follow-up searches for uniformly most split reliable graphs;
- `"Question 6.20" "What is" Phi_V regular co-regular plane graphs Lyons Peres`;
- Haslegrave--Panagiotis DOI/title checks.

Romero's current arXiv record still states that existence/nonexistence in the remaining classes is an open problem and records only his nonexistence range through `m<=binom(n-3,2)+3` for `n>=7`. The bounded searches did not recover a later primary source completing the full `n=8` layer. This is **bounded negative evidence, not a worldwide novelty or priority certificate**.

The maintained Lyons--Peres PDF still carries the original Question 6.20 plus its later annotation that Haslegrave--Panagiotis solved the co-degree `3` and `4` vertex cases. Those triangular/quadrangular results remain excluded prior art.

No source-access failure material to these conclusions occurred.

## 7. Methods actually tried this run

### #2 ATTACK THE NEGATION FIRST

The new event was itself adversarial: R01 tried to break the R06 finite theorem rather than merely checking the final numbers. It independently reconstructed every finite ingredient and explicitly tested the likely omission/quantifier/arithmetic failure modes. No defect survived.

**Outcome:** successful falsification attempt in the sense required by closure; the missing second audit became a PASS and the gate moved `1/2 -> 2/2`.

### #10 DERANDOMIZE

I did not replace the exact theorem with sampled probabilities, random graph trials or a fresh heuristic run. The closure package preserves deterministic exact integer certificates. The copied package checker/output blobs are identical to the already executed owner artifacts, while R01's independent exact implementation supplies orthogonal verification.

**Outcome:** the closure object is reproducible by deterministic finite certificates; no sampled interval is promoted as a rigorous bound.

### #24 FIND THE EXTREMAL OBJECT

For the dense classes the source-designated balloon is the extremal object, and the completed audits certify it by coefficientwise domination over the complete terminal-fixed universe. For successor admission, I also screened the strongest new finite extremal-looking target in the delta, `srg(69,20,7,5)`. It is genuinely CLOSABLE but already exclusively owned, so it cannot be claimed by R06.

**Outcome:** finite-layer extremality is audit-closed; successor extremal target is excluded by ownership.

## 8. Successor gate remains empty

Closure of the retired auxiliary package does not create a new R06 research assignment. The latest coordinator and successor screens still support:

\[
\boxed{E_{\mathrm{ready}}=0\to0.}
\]

Current examples:

- `SHPECTOROV-ZHAO-2026-SRG69`: CLOSABLE and source-current-looking, but exclusively owned;
- P0434: genuine sharp-ratio CLOSABLE target, already owned by R7-04;
- E0011: retired but still claimed, no canonical release;
- P0157: released/reassigned HARD;
- I0027: claimed/retired history, not free;
- I0087's concrete `H^2 x R` example is now answered in later literature and the remaining classification is broad;
- I0105 is programmatic over removal mechanisms rather than one source-fixed finite endpoint.

No successor claim is created. R06 remains `PENDING_ADMISSION / NO ACTIVE MATHEMATICAL TARGET` after recording the closure event.

## 9. Model / scheduler-control truth

The requested GPT-6 / maximum setting is still **not binding on the exposed scheduler surface**. The operative implementation and task-health records show controls for task identity/title, prompt, schedule/timing, enabled state and timestamps, but no model-family selector, no reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated applied-model/applied-effort receipt.

This invocation identifies as **GPT-5.6 Sol**. Reasoning metadata are **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

Making GPT-6/maximum enforceable would require an owner-authorized product/workspace/admin/API/backend scheduling surface that persists model and reasoning fields into inference routing and returns trustworthy per-run attestation, or a platform-side feature change.

The historical P26 `You cannot modify this task` response was an authorization-context boundary. Later repository deployment records show a P26 update succeeded from a different authorized context. The lawful workaround remains the owning/authorized context, permission repair, or platform support, not a bypass or duplicate schedule.

No scheduler, permission, email, Drive, public-posting, purchase, workflow, credential, or access change was attempted.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  report_kind: auxiliary_closure_transition_plus_successor_gate
  predecessor_report:
    path: runs/R06/20260919T1921Z_successor_gate_p0434_owned_p0063_closed_no_free_71_b6e4.md
    commit: dbbebd80168f4a6f2f9cd5d8b84ee46e644a6daa
  original_source:
    id: I0056
    source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20"
    graph_class: "regular co-regular plane tessellation"
    frozen_regime: H_{5,5}
    parameters:
      vertex_degree: 5
      face_degree: 5
    normalization: "outer vertex boundary |partial_V K|/|K|"
    metric: width_U_minus_L
    before: 0
    after: 0
    exact_value: "Phi_V(H_{5,5})=sqrt(5)"
    interval: "[sqrt(5),sqrt(5)]"
    full_source_status: PARTIAL
    prior_art_exclusions:
      - "Haslegrave-Panagiotis triangular/codegree-3 cases, DOI 10.1002/rsa.20946"
      - "Haslegrave-Panagiotis quadrangular/codegree-4 cases, DOI 10.1002/rsa.20946"
  auxiliary_closure:
    id: ROMERO-2025-SPLIT8
    source: "Pablo Romero, Characterization of locally most split reliable graphs, TCS 1047 (2025), 115327"
    exact_scope: "n=8, m=14,...,26"
    mathematical_metric_before: 0
    mathematical_metric_after: 0
    audit_gate_before: "1/2"
    audit_gate_after: "2/2"
    audit_ids:
      - P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64
      - R01-AUDIT-R06-ROMERO-SPLIT8-N8-01
    p26_reconciliation: P26-RECONCILE-R06-ROMERO-SPLIT8-N8-2OF2-76
    lifecycle_before: OWNER_RESEARCH_RETIRED_CANDIDATE_COMPLETE_AUDITS_PENDING
    lifecycle_after: PROVED_AUDIT_COMPLETE_PACKAGED
    source_parent_status: PARTIAL_OPEN
    publication_priority: UNVERIFIED
    paper_package: paper_romero_split8_n8_layer/
  repository_delta:
    base: dbbebd80168f4a6f2f9cd5d8b84ee46e644a6daa
    captured_prepackage_head: e718031a3401ca195076e61def1e3971800b2a04
    commits_ahead: 117
    commits_behind: 0
    too_large: null
    material_events:
      r01_second_audit: PASS_FULL_MATHEMATICAL_PROOF
      p26_late_reconciliation: "ROMERO 1/2 -> 2/2"
      srg69_claim: "CLOSABLE but already exclusively owned"
  package_files:
    README.md:
      commit: 508aff5e5a65474489517cc62d20f77857a92b0c
    main.tex:
      final_commit: e943bf6ea469f530d655c155bec99116667fe240
    check_sparse.py:
      commit: 5061be550506665e44d01e6f84c7e55244f3ebcb
      blob: 2da21c8fa13da1652bfb57dc355d38d849ab981d
    check_sparse.out:
      commit: 934fa81c23786f3b88d3f9c736c44ce61ae012fe
      blob: 40f69d65cc1a0848845ce4a4e6762eb83a292b10
    check_dense.c:
      commit: 685f2306109c4273bfb69802849334961b4dd011
      blob: 7b28fc2fc36b298c96d11c745755b95300475ffb
    check_dense.out:
      commit: d7469f6c52b6e1fcbef74f37c50a068e008ac2a1
      blob: 2124eb4afdd6a4728d9f7294226892299b33c41b
  successor_admission:
    metric: E_ready
    before: 0
    after: 0
    status: PENDING_ADMISSION
    admitted_successor: NONE
    claim_created: false
  unchanged_count:
    frozen_i0056_metric: PRESERVED_AFTER_PRIOR_ROTATION
    romero_closure_gate: 0
    successor_metric: UNKNOWN_NOT_A_MATHEMATICAL_TARGET
  methods_tried:
    - 2_ATTACK_THE_NEGATION_FIRST
    - 10_DERANDOMIZE
    - 24_FIND_THE_EXTREMAL_OBJECT
  remaining_obligation: "No owner-side obligation remains for the exact Romero n=8 finite package. Full Romero/Brown-McMullin source remains PARTIAL/OPEN. R06 next research obligation is to admit a genuinely free strict-READY CLOSABLE OUTSIDE source before doing new mathematics."
  evidence:
    - runs/R01/20260919T2000Z_romero_split8_second_audit_20_27_30_5c8e2a71.md
    - proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_10-01-31__run-report.md
    - proofnet24/P26-proof-audit-recovery/artifacts/2026-09-19/2026-09-19_22-57-43__ledger-sidecar.md
    - runs/R06/20260919T0631Z_romero_split8_full_layer_candidate_complete_59_f3c9.md
    - paper_romero_split8_n8_layer/
```

No shared root ledger, peer file, canonical claim, schedule, email/Drive resource, public post, permission, purchase, credential, or workflow was modified.
