# Mathbrain store: sharp Rademacher singularity dossier objects

```
=====================================================================
  VERDICT: OPEN PROGRAM.  The sharp Rademacher singularity
  conjecture  Pr(det B_n = 0) = (1+o(1)) * 2 * n^2 * 2^(-n)
  is NOT proved.  Nothing in this store claims otherwise, and the
  store must never be read or cited as claiming the conjecture
  proved.  The dossier's own words (p.1): "It must not be cited as
  a proof of the full conjecture."  Statuses below separate proved
  theorems, exact finite certificates, audited computations,
  conditional results, heuristics, disproved routes, and open gaps.
=====================================================================
```

Built 2026-08-18 by the mathbrain ingester lane of the sharp-Rademacher campaign.

## Files

| file | contents |
|---|---|
| `dossier_objects.jsonl` | 97 merged typed objects (one JSON object per line) |
| `edges.jsonl` | 176 dependency edges between store objects |
| `quarantine.jsonl` | invalid digest lines (empty: 0 lines quarantined) |
| `digest_p01-18.jsonl`, `digest_p19-36.jsonl`, `digest_p37-54.jsonl` | raw per-chunk digests (inputs, kept as-is) |

## Provenance

- Source of all content: `~\<private-repo>\06_math_research\sharp_rademacher_campaign_2026_08_18\rademacher_dossier.txt`
  (UTF-8 extraction of the 200-page research dossier of the 2026-08-15 agent packet;
  pages 1-54 synthesis, pages 55-200 verbatim sources S1-S14).
- SHA-256 (PowerShell `Get-FileHash -Algorithm SHA256`, computed 2026-08-18):
  `C4BBBB039C5EC5A655D7E85DE5F3A42BB17A4202392B8356B9EE54EF2C8BBB63`
- Size 326,105 bytes; 13,358 lines measured by `wc -l` (file is newline-terminated; the
  campaign brief quoted 13,359 - the measured value is recorded here).
- The three digest chunks were produced by digester lanes reading dossier pages 1-18,
  19-36, 37-54 respectively. Every object carries a `source` field citing dossier pages.
- Extraction caveat inherited from the dossier text: superscripts/subscripts are
  flattened by PDF extraction (e.g. `9 4l` means `9*4^l`, `2n22-n` means `2*n^2*2^(-n)`).
  Reconstructed readings that are not fully certain are tagged `[EXTRACTION-UNCERTAIN]`
  inside the objects' own statement/notes fields.

## Validation

All 108 non-empty input lines (39 + 27 + 42) parsed as JSON with the required keys
`kind, name, statement, status, source` present and non-empty; `dependencies`, where
present, is a list. 0 lines quarantined; `quarantine.jsonl` exists and is empty to show
the step ran. No literal duplicate names within or across chunks.

## Schema

Each line of `dossier_objects.jsonl`:

| key | meaning |
|---|---|
| `kind` | `conjecture`, `definition`, `theorem`, `lemma`, `certificate`, `counterexample`, `failed_route`, `method`, `open_gap` |
| `name` | canonical unique id (chunk naming styles preserved; see aliases) |
| `statement` | the fullest statement among merged variants, verbatim from its digest |
| `status` | `proved`, `audited-pass`, `exact-certificate`, `conditional`, `heuristic`, `disproved`, `open` |
| `source` | dossier page cites, ` \| `-joined when merged from several chunks |
| `dependencies` | canonical names of store objects this one depends on (resolved) |
| `dependencies_unresolved` | dependency strings pointing outside the store (external literature / earlier-project theorems); present only when non-empty - nothing was silently dropped |
| `notes` | digest notes, ` \|\| `-joined; notes from merged variants are tagged `[from merged variant <name>]` |
| `aliases` | names of merged-away variants (present only on merged objects) |
| `chunks` | which digest file(s) the object came from |
| (in notes) `MERGED-IN variant ...` | full verbatim statement, kind, status, source of each merged-away variant, so no content is lost by keeping only the fullest statement |

Status vocabulary (as the digests use it): `proved` = proved in the packet per the
synthesis; `audited-pass` = proved and passed the dossier's independent audit;
`exact-certificate` = exact finite computation/certificate (integer/rational arithmetic,
exhaustive in its stated range - a certificate about a FINITE claim, never a proof of an
asymptotic statement); `conditional` = proved under stated unproved hypotheses;
`heuristic` = methodology/evidence, no proof claim; `disproved` = shown FALSE by
counterexample; `open` = not proved. A simulation or harness PASS is evidence about its
stated finite range only.

Counts by kind (97 objects): theorem 22, definition 19, lemma 15, certificate 12,
failed_route 11, method 7, open_gap 5, counterexample 5, conjecture 1.

Counts by status: audited-pass 40, exact-certificate 16, proved 15, disproved 11,
open 7, heuristic 5, conditional 3.

Updated 2026-08-20. `explicit_dual_of_linear_system` moved audited-pass -> disproved: `|D| = r + k`
is false for linear systems, refuted by the Pasch configuration, and the counting bound built on
it falls by an unbounded factor. Eight objects were added to `campaign_objects_v2.jsonl` with 13
edges - the bipartite hub construction, the Pasch theorem, the colourability theorem, the r=8
enumeration, the tightness limit, and the replacement open gap `which_linear_systems_have_dual_
exactly_r_plus_k`. `how_far_dense_linear_systems_erode_the_counting_bound` moved open -> resolved:
it named the exact test that settled it, and its self-limiting guess was wrong.

The 7 `open` objects: `sharp_rademacher_singularity_conjecture`,
`first_uncovered_homogeneous_block`, `linear-entropy-rigidity-theorem-needed`,
`centered_moment_jss_transfer`, `connector-absorption-gap`,
`triangular_witness_attack_plan` (an unexecuted plan), `final_status_packet_vs_conjecture`.

## Dedup decisions

108 objects -> 97 after merging 10 groups (21 objects -> 10). Rule: within a group the
variant with the longest statement supplies name/kind/statement/status; sources are
unioned; dependencies are unioned after canonicalization; every merged-away variant's
full statement, kind, status, and source are preserved verbatim in the canonical
object's notes (`MERGED-IN variant ...`). Groups (canonical <- merged-away):

1. `sharp_rademacher_singularity_conjecture` <- `sharp_rademacher_singularity` (p.1-2 = p.54, same conjecture).
2. `entropy-sharpened-residual-rank-theorem` <- `global_bridge_dcb_exponential` (p.2-3/p.9 executive quote of the p.34 theorem `dcb(A) <= 9*4^ell + ell`; the dossier itself says the p.34 theorem is "also quoted p.2").
3. `bounded_congestion_linear_quotient` <- `bounded_congestion_quotient` (p.2-3 quote of the p.39 theorem `dim((R+span W)/span W) <= (2*kappa+1)*L_{Q|W}`).
4. `connector_absorption_criterion` <- `absorption_kernel_criterion` (p.8 summary of the p.41 kernel criterion `ker P0 subseteq ker Bbar`).
5. `three_arm_NAE_star_absorption_failure` <- `nae_star_absorption_failure` (p.8 summary of the p.42 counterexample). Merged status `exact-certificate` (the counterexample is exactly certified); the killed route carries `disproved` separately (`bounded_support_or_degree_implies_absorption`).
6. `three_connectivity_ceiling_false` <- `three_connected_ceiling_falsified` (p.3 ledger verdict of the p.51 falsification, n=13, L_13=521). Same convention: counterexample object `exact-certificate`, route object `constant_one_ceiling_from_three_connectivity` carries `disproved`.
7. `intrinsic-cube-model` <- `shared_h_integration_bridge` (p.6 statement of the p.20 construction; the p.6 consequence sentence about the m<=7 enumeration is preserved in notes).
8. `first_uncovered_homogeneous_block` <- `surviving_core_localization` (p.10 and p.53 describe the SAME surviving block; the dossier's p.53 header is literally "OPEN GAP", so the merged object is kind `open_gap`, status `open`; the localization claim ITSELF - that the survivor has exactly this form - is audited, recorded at p.10 with status audited-pass in the merged-in variant note. What is open is the block class, not the localization).
9. `linear-entropy-rigidity-theorem-needed` <- `connector_compatible_linear_rigidity`, `rooted_linear_rigidity_target` (pp.2/4/8-10, p.28, p.53 all state the one missing deterministic bridge: `dim((R+R_<)/R_<) <= C*L_{Q|W}` plus connector absorption, absolute C >= 1/log2(4/3) = 2.40942...).
10. `centered_moment_jss_transfer` <- `probabilistic_endpoint_transfer_JSS` (pp.2/4 and p.53: the remaining probabilistic Layer-III step; neither written nor audited).

Deliberately NOT merged (recorded so the decision is visible):
`nonsummable_survivor_profile` (p.9, joint coverage profile of both theorems) vs
`endpoint-range-of-exponential-theorem` (p.36, endpoint range of the exponential theorem
alone) - overlapping but different scope; `rooted_nae_cycles_solved` and
`shared_homogenizer_m8_m7` are ledger summary nodes kept distinct from the detailed
theorems/certificates they summarize (linked by edges instead); `connector-absorption-gap`
(absorption for the exponential conditional theorem specifically) is narrower than the
full linear target of group 9.

## Edges

`edges.jsonl`: 176 edges `{"src", "dst", "kind"}`, kinds `uses` (169), `refutes` (5),
`generalizes` (1), `instance_of` (1). Derivation:

- Every entry of an object's `dependencies` field yields `src=object -uses-> dst=dependency`,
  after alias/descriptive-string canonicalization, except the overrides below. Descriptive
  dependency strings (e.g. "dgeo geometric residual distance (p.7)") were resolved to the
  store object defined at the cited page; strings resolving to two definitions (e.g.
  "full dual, closure, coordinate-full (p.6)") yield one edge per target.
- `refutes` (emitted as counterexample -refutes-> failed_route, replacing the uses edge):
  `three_arm_NAE_star_absorption_failure -> bounded_support_or_degree_implies_absorption`;
  `walsh_crosspolytope_single_batch -> single_dense_batch_pays_remainder`;
  `walsh_crosspolytope_single_batch -> ear_or_witness_charging_ignoring_unused_defect`;
  `three_connectivity_ceiling_false -> constant_one_ceiling_from_three_connectivity`;
  `three_connectivity_ceiling_false -> fixed_q_evaluation_rado`.
- `generalizes`: `conditional-exponential-cyclic-block-theorem -> entropy-sharpened-residual-rank-theorem`
  (p.35: "the target-uniform batching proof can be run conditionally on the boundary").
- `instance_of`: `bounded_support_linear_rigidity_coefficient -> bounded_congestion_linear_quotient`
  (p.39: the coefficient is the theorem instantiated at kappa <= (s-1)/log2(4/3)).
- 7 explicit-statement edges beyond the dependencies fields, from ledger summary nodes to
  the results they summarize (dossier p.2-3 "solves rooted NAE cycles exactly, including
  activation-cell and connector-compatible certificates" = pp.46-49; p.3 m=8 / m<=7 ledger
  verdict = pp.23-25): `rooted_nae_cycles_solved -uses-> cycle_{geometric_distance_exact,
  optimal_selector_basis, activation_cell_inequality, connector_transversality}` and
  `shared_homogenizer_m8_m7 -uses-> {m8-support3-and-distinct5-normal-forms,
  m8-repeated-AAB-family, m-le-7-intrinsic-enumeration}`.
- The four failed_route objects whose witness the dossier does not restate on pp.37-54
  (`universal_pair_branching`, `optimizer_monotonicity_under_row_deletion`,
  `geometric_optimizer_saturation`, `matroid_2sum_across_nonbinary_separator`) have no
  refutes edge: p.52 attributes witnesses only collectively, and inventing the specific
  witness would be guessing (UNKNOWN).

Unresolved external dependencies (kept per-object in `dependencies_unresolved`, no store
node, no edge): "finite-group one-point Littlewood-Offord theorem (external)" /
"finite-group-one-point-LO-theorem" (classical literature result invoked at p.31/p.37);
"homogeneous relation-corank-three density theorem (external, pp.10-17)" (earlier-project
theorem the shared-h analysis descends from, reproduced in the packet sources, no digest
object in the pp.1-54 synthesis range).

## Spot-checks against the dossier text

5 objects drawn with Python `random.Random(20260818).sample(sorted(names), 5)`, each
compared against the cited dossier pages (page N = text above the footer line `N / 200`).

1. `first_uncovered_homogeneous_block` (p.10, p.53): PASS. p.53 ("OPEN GAP") matches the
   canonical statement clause-by-clause (singleton-layer cyclic strongly connected,
   relation corank >= 5, not rooted-NAE/stable-set/median/paired-Gale/bounded-congestion,
   congestion of order log n or common-lift failure); p.10 matches the merged-in variant
   ("first homogeneous survivor... no useful low-congestion batching or it fails
   connector absorption"). The merge and the open_gap typing are both confirmed by the
   dossier's own headers.
2. `collision-forest-classification` (p.22): PASS. Forest shapes 3K2, P3+K2, P4, K1,3 and
   the survivor table 16/16/4/4, 16/8/2/2, 16/1/1/1, 16/3/3/3 match exactly; "balanced on
   support four or six and contains the homogenizer", h=1 leaving old support three or
   five, and the fractions.Fraction/no-floating-tolerance sentence all match.
3. `sharp_rademacher_singularity_conjecture` (p.1-2, p.54): PASS. p.2 gives
   `Pr(det Bn = 0) = (1 + o(1)) 2n22-n` (flattened `2*n^2*2^(-n)`), verdict "OPEN PROGRAM -
   SUBSTANTIAL AUDITED PROGRESS"; p.1 "must not be cited as a proof of the full
   conjecture"; p.54 "It does not yet prove the sharp iid Rademacher singularity
   conjecture." Status `open` is correct.
4. `m8-support3-and-distinct5-normal-forms` (p.23): PASS. Flag bounds closing m = 9,10,11;
   support-three planar spectrum (1,2,2) with eight target multisets, rank <= 2
   certificates in all eight; support-five A, B, A+B reducing to twelve projectively
   simple configurations with rank-two certificates and r = 8-3 = 5 classes; "exhaustive
   normal forms, not random samples" - all match.
5. `cycle_rigidity_ratio_limit` (p.51): PASS. `dcb(An)/ell(An) -> 1/(3(1 - log2 phi)) =
   1.090186...` printed on the page; the digest's reconstruction of the flattened fraction
   is confirmed by the printed decimal. Independent re-derivation here: log2(phi) =
   0.6942419, 1/(3*0.3057581) = 1.0901868. The same page confirms the merged
   `three_connectivity_ceiling_false` (dcb(A13) = 5 > ceil(13 - log2 521) = 4, L_13 = 521
   re-checked against the Lucas sequence, infinite family n = 0 mod 6, n >= 42) and the
   `fixed_q_evaluation_rado` failure.

Incidental to the checks, p.2 also matched the merged statements of groups 2, 3, 9, 10
and the ledger sentence justifying the rooted-NAE summary edges.

## Post-build verification

A separate process reloaded the three written files and confirmed: 97 objects with
unique names; no alias collides with a live name; all 176 edges reference existing
objects, use only the four allowed kinds, and contain no self-loops; every object has
the required keys; unresolved externals preserved. Counts above are from that reload,
not from the builder's own report.


---

## SECOND PASS: source files S1-S14 merged (2026-08-19, main agent claude-c53c1d50)

The three source digests over dossier pp.55-200 (the verbatim agent reports carrying the actual
proofs, constants, checker outputs and counterexamples behind the synthesis) are now merged into
this store. The ingester agent assigned to this died on a usage limit; the merge was done by the
main session with `scratchpad/merge_sources.py` (backups: `dossier_objects.jsonl.bak_premerge`,
`edges.jsonl.bak_premerge`).

**Counts now: 325 objects, 602 edges, 0 quarantined lines, 0 unresolved dependency names.**

By kind: {'certificate': 37, 'conjecture': 2, 'corollary': 5, 'counterexample': 16, 'definition': 39, 'failed_route': 27, 'lemma': 49, 'method': 21, 'numeric': 27, 'open_gap': 24, 'proposition': 1, 'theorem': 77}

By status: {'audited-pass': 79, 'conditional': 9, 'disproved': 26, 'exact-certificate': 60, 'heuristic': 5, 'numerical': 10, 'open': 27, 'proved': 109}

Edge kinds: {'generalizes': 1, 'instance_of': 1, 'refutes': 5, 'restates': 18, 'uses': 577}

### Merge ledger (honest)

- 231 source objects read from `sources_S1-S5.jsonl` (98), `sources_S6-S9.jsonl` (75),
  `sources_S10-S14.jsonl` (58). All parsed; all carried the required keys; nothing quarantined.
- **228 added, 3 merged into existing objects by normalized-name match.** Where a merge happened the
  fuller statement was kept and the displaced variant preserved verbatim in `notes` with its source,
  so no text was lost; sources and dependencies were unioned; a status disagreement between the two
  digests is recorded in `notes` as a STATUS VARIANT rather than silently resolved.
- **A name-based dedup is weak here and I checked rather than assumed:** the synthesis digesters and
  the source digesters used different naming conventions, so a content-similarity sweep
  (Jaccard over statement tokens) was run afterwards. It found **9 cross-origin pairs above 0.45**
  and **0 intra-source pairs above 0.55**. The 9 were NOT merged: in each case one object is the
  synthesis-level summary and the other the source-level statement with its proof detail, and
  collapsing them would lose the page-level distinction the store exists to preserve. They are
  cross-linked instead with `restates` edges in both directions (18 edges).
- 408 new `uses` edges were derived from dependency fields, appended only where both endpoints
  resolve to objects present in the store; every dependency name resolved.
- Objects added in this pass carry `"origin": "source-digest <file>"` so the two passes stay
  separable.

### Spot-checks of merged objects (3, done by reading the dossier, not by token search)

A first attempt used a "does a distinctive number appear anywhere in the dossier" test; that test
cannot fail on a 318KB file and was discarded as worthless. The real checks:

1. `conditionally_free_coordinate_dichotomy` (cited S6 p.118) - statement matches the S6 Theorem-2
   proof text at extraction lines ~6538-6590 (conditionally-free definition, q_a(c)=0, lambda_a=+-1,
   assignment to the signed coordinate, residual supported on C). PASS.
2. `rooted_nae_cycle_fibre_An` (cited S10 p.157) - matches extraction lines ~9796-9826 verbatim in
   content (the fibre, the excluded local pattern, independent sets of C_n, the antipodal half). PASS.
3. `target_uniform_interval_cells_m2_and_m_ge_4` (cited S14 pp.197-198) - the "except at m=1,3"
   matching claim matches extraction line 13094, and the coefficient 1/log2(4/3) < 2.410 matches the
   synthesis statement at line 1239. PASS.

### The banner is unchanged and still governs

The sharp Rademacher singularity conjecture Pr(det B_n = 0) = (1+o(1))*2n^2*2^(-n) is **OPEN**. This
store must never be cited as claiming otherwise. Objects of kind `failed_route` and `counterexample`
(now 27 and 16 respectively) are first-class: check them before re-attempting any route.

## Campaign layer (added 2026-08-19)

| file | contents |
|---|---|
| `campaign_objects.jsonl` | 13 typed objects produced by this campaign, not by the dossier |
| `campaign_edges.jsonl` | 32 edges, 15 of them into the dossier layer |

Everything above this section came from the 200-page dossier. Nothing the campaign itself proved
or measured was in the store, so the store could not answer a question about our own work. These
objects close that gap. They use the same schema (`kind`, `name`, `statement`, `status`, `source`,
`dependencies`, `notes`) and the same status vocabulary, with `origin: campaign-2026-08-19`.

What the layer records, by status:

- **proved** — `ker Φ = span{ρ_t}` (dimension exactly `k`); the transversal/Rado condition is
  equivalent to the missed set blocking every nonzero triangle relation; the definition of a
  linear triangle system.
- **audited-pass** — the dual of a linear system is exactly the coordinate forms plus one form per
  triangle, `|D| = r + k`; excess `≤ 2d` per dimension; the excess-2 directions are exactly the
  `3k` pair-sums.
- **conditional** — `d_cb ≥ ⌈k/2⌉` (rests on the unproved `E_t ≤ d`); `d_cb ≥ max(⌈k/2⌉, k − h)`
  (rests additionally on the `d ≥ 2` composition of the unit-constraint bound).
- **exact-certificate** — `d_cb((3,2) at k=6) = 4`; the `k=6` tree sweep.
- **disproved** — `d_cb = max(largest attachment group, ⌈k/2⌉)`, refuted by `(3,2)` at `k=6`.
- **heuristic** — `d_cb = max(⌈k/2⌉, k − h)`, which fits every exact value held and passed a
  registered discriminating test at `k=7`, but whose upper-bound direction has no argument.

The verdict banner at the top of this file applies unchanged: the conjecture is open, and every
object in this layer concerns finite systems that are known non-members of the class.
