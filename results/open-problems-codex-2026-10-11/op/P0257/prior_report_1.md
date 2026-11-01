Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629258051845519310707290096835... -> b_NUV >= 0.629258051894864749286960900927... > 0.629258051894`; actual Section-B methods tried: #14, #16, #24.**

# NM13-11 — P0257 size-5 orbit classification and trivial-automorphism sink movement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0257 / `operations/claims/P0257.md`**  
Canonical dedup key: `law_of_large_numbers_and_constants_for_nuv_lengths`  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 10`  
Status after this invocation: **PARTIAL / SOURCE OPEN**

## 1. Continuity, ownership, and frozen source metric

This invocation continues the already-admitted P0257 source, David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs* (arXiv:1912.13175; *Probability in the Engineering and Informational Sciences* 36 (2022), 851--867, DOI `10.1017/S0269964821000115`). It does **not** reopen intake, create a second claim, switch sources, or change the metric.

Immediately before this report I reread `operations/claims/P0257.md`. It still records:

- status `CLAIMED / ADMITTED / HARD OUTSIDE`;
- owner `proofnet24/NM13-11/`;
- canonical dedup key `law_of_large_numbers_and_constants_for_nuv_lengths`;
- SHA-256 `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`;
- shard residue **10 mod 13**;
- the exact Euclidean iid random-points NUV model.

No P0257 release, handoff, retirement, settlement, competing owner, or canonical-alias collision was recovered. The current neighboring NM13-10 report remains in residue-9 admission-screen mode, and the current designated secondary-auditor NM13-12 report remains in residue-11 successor screening and explicitly treats NM13-11 as active on P0257. Neither releases or duplicates this claim.

The frozen metric remains

`b_NUV = explicit certified endpoint in liminf_{n->infinity} E[L_n]/n >= b_NUV`

for the source's area-`n` Euclidean square scaling.

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T22-02-00Z__p0257-five-d2-sink-topology-movement.md`

created at commit

`10b75027957e0792c45c2d83f2a3340e4310ec80`.

Its exact endpoint is

`B_before =`

`257829989578496350414183523146605335856248997408453788237962025484814476957683136019074638921462335179814079007196663994330380573638384791944133112730116386394080336881706051 /`

`409736496533210395577129470979508748365626015570562389564441613457911228367916571422161933413348402679750261900585439123098992187500000000000000000000000000000000000000000000`

`= 0.62925805184551931070729009683590061627639266285210461589341007849834871417375502...`.

This invocation proves the new additive correction

`Delta_orbit5 >=`

`2314212291015625000 / 46898200879888981540448041041`

`= 4.93454385796708040919848364619699796548928895675556617...e-11`.

Therefore

`B_after =`

`4030587548353407239385594764200229614297797658205062329180415991935634988507131251165427843820794999771597107722461131707733943325633277304301536835785477343473397459589419707534599554139802937648679697 /`

`6405301507412145469471049291078200132062046565450533944155920254596661605498664430441568460794726368748340630284796689323210137382338787704649039451912789062500000000000000000000000000000000000000000000`

`= 0.62925805189486474928696090092788545273836264250699750546096574020861543570053631...`.

In particular,

`b_NUV > 0.629258051894`.

The source remains open. This result does **not** prove existence of Aldous's proposed limit `lim L_n/n`, does not identify that limit, and does not upgrade P0257 to PROVED.

## 2. Authoritative repository continuity and race check

Before substantive work I freshly read or targeted-recovered the required current state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling NM13-11 predecessor and its relevant earlier D2 sink-SCC reports;
- newest neighboring NM13-10 report `proofnet24/NM13-10/runs/2026-09-19/2026-09-19T22-56-30Z__admission-delta-screen-52-hard-releases-no-r9-closable.md`;
- newest completed NM13-12 successor-screen report available to this invocation, `proofnet24/NM13-12/runs/2026-09-19/2026-09-19T21-59-30Z__post-p0214-successor-delta-f0111-projective-p0487-offshard-p0205-ambiguous.md`;
- current `operations/claims/P0257.md`;
- exact repository searches for P0257 / its canonical key / historical attempt `P0257-A001`;
- campaign source/attempt continuity identifying the old pre-NM13 nearest-neighbor lower-bound mechanism; and
- an exact Git comparison from the predecessor report commit to the final prewrite head.

The large append-only intake and attempt corpora cannot honestly be represented as fully model-visible byte-for-byte in one bounded connector response. I preserved the already recovered P0257 canonical identity and reopened the candidate-specific source, attempt, ownership, and lifecycle records instead of treating aggregate truncation as permission to restart history.

The final frozen prewrite master was

`aec330f2beca1351c61176b36fba4b9a04a0e09f`.

The exact comparison

`10b75027957e0792c45c2d83f2a3340e4310ec80 .. aec330f2beca1351c61176b36fba4b9a04a0e09f`

reported:

- status `ahead`;
- **137 commits ahead**;
- **0 behind**;
- `too_large = null`, so the returned changed-file set is complete.

That complete interval contains this run's idea/checker/output, unrelated concurrent research/claim changes, and a current `POSTED.md` bibliographic update. It contains **no mutation of `operations/claims/P0257.md`**, no P0257 handoff or retirement, and no campaign control change settling P0257. I separately reread the claim at the prewrite head and confirmed the same exclusive owner and source identity.

The newest `POSTED.md` change is the owner-supplied 20 September ResearchGate inventory. It explicitly says the update is bibliographic only and changes no schedule, assignment, ownership, audit count, or mathematical closure status. None of the three newly confirmed ResearchGate titles is P0257/NUV.

No private-repository history known to be material to this P0257 continuation was inaccessible.

## 3. Runtime and model-control truth

The prompt requests `Model: GPT-6. Reasoning: maximum`. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, verified maximum reasoning, a binding maximum-effort setting, a guaranteed hour-long execution, or a support escalation.

The exposed scheduled-task control surface still provides task title/prompt, schedule or relative-start configuration, timing mode, enabled state, listing, and ordinary update operations. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-model/applied-effort receipt**. GPT-6/maximum therefore remains prompt text only on this surface.

Making GPT-6/maximum binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists explicit model-family and reasoning-effort routing fields and returns trustworthy per-run attestation of the model and effort actually applied.

Repository continuity preserves the historical P26 `You cannot modify this task` result, while later authorized context successfully updated P26. The denial is therefore authorization/context-specific, not proof that the task can never be changed. If a modification is denied again, the compliant workaround is the **same task's** owning or otherwise authorized context, supported ownership/permission repair or transfer where available, or authorized platform/admin support. Creating a duplicate task, substituting identities, or bypassing access controls is not a workaround.

No scheduler, task configuration, permission, workflow, email/Gmail, Drive resource, public surface, paid-compute resource, shared root ledger, peer namespace, or canonical P0257 claim was modified in this invocation.

## 4. Fresh bounded source/literature check — 2026-09-19 UTC

This is bounded current-status evidence, not proof of worldwide openness, novelty, or priority.

Fresh public checks recovered:

1. Cambridge's current page for Aldous's NUV article, DOI `10.1017/S0269964821000115`, still lists *Probability in the Engineering and Informational Sciences* 36(3), July 2022, pp. 851--867, and its abstract says that establishing sharper results appears challenging.
2. Aldous's currently crawled Berkeley page still lists **The Nearest Unvisited Vertex Walk on Random Graphs** and the challenge of improving beyond order-of-magnitude results for random-graph models.
3. Aldous's current publication list still lists the 2022 NUV paper.
4. Bounded exact-title / `nearest unvisited vertex walk` / Euclidean-random-points / 2023--2026 searches did not surface a checked later primary source resolving the Euclidean first-order constant or superseding the exact source question used here.

Primary/public surfaces checked in this run include:

- `https://www.cambridge.org/core/journals/probability-in-the-engineering-and-informational-sciences/article/nearest-unvisited-vertex-walk-on-random-graphs/`;
- `https://www.stat.berkeley.edu/~aldous/` and its publication/research listings;
- `https://arxiv.org/abs/1912.13175`;
- bounded web indexing for the exact title and 2023--2026 follow-up terms.

Search access was bounded to the publicly indexed sources returned on 2026-09-19 UTC. Failure to find a resolution is not a bibliographic-completeness certificate.

## 5. Section-B methods genuinely attempted — #14 / #16 / #24

All thirty Section-B methods have already appeared at least once in P0257 history. This invocation therefore uses the predecessor's planned **recycled, nonconsecutive** triple #14/#16/#24 and does not misreport them as unused.

The mathematical idea was written **before checker code** at

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T22-50-00Z__p0257_orbit_extremal_route_idea.md`

creation commit

`e6c643cf5ae0cb14a3ee53bec4fba1a11a3f7b1b`.

### #14 FIND THE GROUP ACTING — success

The previous run charged one five-vertex directed two-nearest-neighbor topology and paid an ordered-tuple multiplicity factor equal to the topology's automorphism-group size. The natural group is the full relabeling action of `S_5` on loopless 2-out digraphs.

Instead of searching labeled topologies one by one, quotient the finite strongly connected 2-out digraph space by `S_5`. If an unordered five-point set admits two ordered normalizations lying in one fixed topology chart `A`, the permutation carrying one labeling to the other preserves the directed two-nearest-neighbor adjacency and is therefore in `Aut(A)`. Hence a chart's factorial-moment count needs division by at most `|Aut(A)|`, not by a generic `5!`.

This makes the group action source-relevant: small automorphism groups directly increase the certified Palm/binomial intensity of a geometric sink-SCC family.

### #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE — success

An exact first-principles enumeration of all loopless labeled outdegree-two digraphs on five vertices found:

- strongly connected labeled digraphs: **5346**;
- strongly connected isomorphism classes under `S_5`: **53**;
- automorphism-size histogram among the 53 classes:

`|Aut|=1: 38`, `|Aut|=2: 12`, `|Aut|=4: 1`, `|Aut|=5: 1`, `|Aut|=10: 1`.

The orbit identity checks exactly:

`38*120 + 12*60 + 1*30 + 1*24 + 1*12 = 5346`.

Thus **38/53** isomorphism classes, accounting for exactly `4560/5346 = 760/891` of the labeled strongly connected objects, have trivial automorphism group. The finite census therefore points away from symmetric C5-style shapes and toward asymmetric Euclidean realizations.

### #24 FIND THE EXTREMAL OBJECT — success on the source-relevant intensity functional

For a normalized five-point topology chart with six-dimensional shape volume `V`, uniform internal second-neighbor bound `U`, external exclusion radius `H>U`, guard coefficient `Q`, and automorphism count `a`, the already proved sink-SCC transfer gives the source-valid correction

`Delta = 105*pi^(3/2)/16 * [V*(H-U)/(a*Q^(9/2))]`.

Thus the object to maximize is not geometric prettiness but

`J = V*(H-U)/(a*Q^(9/2))`.

The run deliberately hunted a **trivial-automorphism** class (`a=1`) and found an exact positive-measure Euclidean chart with strict ranking margins. This produces genuine new movement. It is not a subdivision or decimal refinement of the predecessor's `a=2` chart.

## 6. Exact finite orbit census

For each vertex `v` in `{0,1,2,3,4}`, choose an unordered pair of distinct other vertices as its two out-neighbors. There are `C(4,2)^5 = 6^5 = 7776` labeled loopless 2-out digraphs.

The exact checker tests strong connectivity in both the graph and transpose, canonicalizes each survivor over all 120 permutations, and computes its stabilizer exactly. It obtains the 5346/53 census and the automorphism histogram above. No floating point, sampling, graph-isomorphism heuristic, or external table is used.

The identity

`sum_[isomorphism classes A] 120/|Aut(A)| = 5346`

is independently checked and closes the orbit-count bookkeeping.

This finite census is useful research guidance but **is not itself counted as movement of `b_NUV`**. Movement comes only from the Euclidean chart and its source-valid transfer below.

## 7. A new trivial-automorphism five-point Euclidean chart

Normalize an ordered five-tuple by translation, rotation and scale so that

`p0=(0,0)`, `p1=(1,0)`.

Let

`p2=(x2,y2)` with

`53/100 <= x2 <= 63/100`,

`21/125 <= y2 <= 53/250`;

`p3=(x3,y3)` with

`91/250 <= x3 <= 52/125`,

`-13/60 <= y3 <= -7/60`;

and

`p4=(x4,y4)` with

`89/100 <= x4 <= 93/100`,

`-59/125 <= y4 <= -56/125`.

The normalized six-dimensional volume is exactly

`V = 429/19531250000 = 2.19648e-8`.

Exact interval arithmetic proves throughout this whole closed rational box that the internal two-nearest-neighbor sets are

`N2(0)={2,3}`,

`N2(1)={2,4}`,

`N2(2)={1,3}`,

`N2(3)={0,2}`,

`N2(4)={1,3}`.

Equivalently the fixed labeled directed topology is

`A = ((2,3),(2,4),(1,3),(0,2),(1,3))`.

The exact squared-distance ranking gaps, in vertex order, are

`6887/12500`,

`49963/562500`,

`541/12500`,

`74/3125`,

`493/1125000`.

The minimum strict gap is therefore

`493/1125000 > 0`.

The graph `A` is strongly connected. Its canonical `S_5` representative is

`((1,2),(0,2),(0,3),(2,4),(0,3))`.

Its automorphism group is exactly

`Aut(A) = {id}`.

The checker canonicalizes the two previously charged size-5 topology classes and proves that this canonical representative differs from both. Therefore this is a genuinely new size-5 `D_2` sink-SCC class for the additive accounting below.

## 8. Guard and boundary surplus

Across the entire chart the largest possible squared distance from a vertex to one of its designated two internal nearest neighbors is

`100489/225000`.

Take

`U = 669/1000`.

Then

`U^2 - 100489/225000 = 8489/9000000 > 0`,

so every selected vertex has its internal second-neighbor radius strictly below `U r` after rescaling by `r=|p1-p0|`.

Take external exclusion radius

`H = 407/500`.

Then

`H-U = 29/200 > 0`.

If no other source point lies within distance `H r` of any selected vertex, the two global nearest neighbors of each selected vertex are its two chart neighbors. Thus these five selected vertices form a sink strongly connected component of the global directed `D_2` graph.

Every chart point lies in the normalized rectangle

`[0,1] x [-59/125, 53/250]`,

with width `1` and height `171/250`. The union of the five radius-`H r` guard disks is contained in the `H r`-parallel body of this rectangle. By the planar Steiner formula and the classical rational bound `pi < 22/7`, its area is at most

`Q r^2`,

with

`Q <= Qbar := 4819497/875000 = 5.507996571428...`.

The rational square-root upper bound

`sqrt(Qbar) < 2347/1000`

is certified by

`(2347/1000)^2 - Qbar = 2887/7000000 > 0`.

The topology-independent Hamiltonian-boundary theorem from the predecessor applies: a proper sink SCC containing neither endpoint of the NUV Hamiltonian path has at least two path edges crossing its boundary. Each such crossing has length at least `H r`, whereas the degree-two nearest-neighbor baseline charges at most `U r` at the affected component vertex. Summing the two boundary crossings yields an **L-side surplus at least `(H-U)r`** for each non-endpoint qualifying component.

At most two sink SCCs can contain the two global Hamiltonian-path endpoints. Under any fixed scale cutoff `r<=M`, dropping those components loses only `O(M)`, hence `o(n)` after division by `n`.

## 9. No double counting

SCCs of a fixed directed graph partition its vertices. Hence distinct global sink SCCs are vertex-disjoint.

The predecessor's charged size-3, size-4, and size-5 objects are all sink SCCs of the same global `D_2` graph. Different sizes cannot be the same SCC. For size 5, the actual directed adjacency of an SCC is unique; the exact canonicalization proves that the new class is not isomorphic to either previously charged size-5 class.

Therefore the new charge is additive to the existing certified endpoint. No predecessor term is silently counted twice, and no old five-point term is replaced in this run.

## 10. Exact finite-binomial transfer to the source model

I spell out the transfer because finite geometry alone is not the source theorem.

Work in the source's equivalent area-`n` square containing exactly `n` iid uniform points. Fix a scale cutoff `M<infinity`. Count ordered distinct five-tuples satisfying the normalized chart with `r=|x1-x0|<=M`, with the anchor and guard sufficiently far from the square boundary.

For a fixed ordered pair `(x0,x1)`, writing `x1-x0 = r e_theta`, each of `x2,x3,x4` is obtained from a normalized chart coordinate by the same rotation and scale. The six free chart coordinates contribute the Jacobian factor `r^6 V`. Polar coordinates for `x1-x0` contribute `r dr dtheta`. Integrating the orientation gives `2*pi`.

For a tuple of scale `r`, the guard union has area at most `Qbar r^2`. Conditional on the tuple points, the remaining `n-5` iid points avoid the guard with probability at least

`(1-Qbar r^2/n)^(n-5)`

whenever the cutoff makes the expression positive. The ordered distinct-point factorial factor is `(n)_5/n^5 -> 1`. The area of admissible anchors is `n-o(n)` for fixed `M`.

Because an unordered set can have at most `|Aut(A)|=1` chart labeling inducing this fixed topology, there is no further multiplicity loss here. Combining the component surplus `(H-U)r` with the geometric Jacobians gives, after division by `n` and first taking `n->infinity`,

`Delta_M >= 2*pi*V*(H-U) * integral_0^M r^8 exp(-Qbar*r^2) dr`.

All integrands are nonnegative. Sending `M->infinity` after the finite-volume limit gives by monotone convergence

`Delta_orbit5 >= 2*pi*V*(H-U) * integral_0^infinity r^8 exp(-Qbar*r^2) dr`.

The Gaussian integral is exact:

`integral_0^infinity r^8 exp(-Q r^2) dr = 105*sqrt(pi)/(32 Q^(9/2))`.

Hence

`Delta_orbit5 >= (105*pi^(3/2)/16) * V*(H-U)*Qbar^(-9/2)`.

This transfer stays in the **exact finite binomial source model** before taking limits. It does not assume Poissonization as a theorem, stabilization of the NUV functional, existence of `lim L_n/n`, or validity of a finite simulation.

For a completely rational certificate, use

`pi^(3/2) > 51/10`

(from `pi>3` and `sqrt(pi)>17/10`) and

`Qbar^(9/2) < Qbar^4*(2347/1000)`.

Substitution gives exactly

`Delta_orbit5 >=`

`2314212291015625000 / 46898200879888981540448041041`

`= 4.93454385796708040919848...e-11`.

Adding this disjoint correction to `B_before` gives the exact `B_after` stated in Section 1 and the certified decimal threshold

`b_NUV > 0.629258051894`.

## 11. Exact self-check artifacts

Only after the orbit/intensity idea had been written did I create the exact checker:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T22-55-00Z__p0257_n5_orbit_trivial_aut_exact.py`

creation commit

`b28e7dbe09af5b3d8d9434d4a02fb501a59a0ef1`.

I executed the exact-arithmetic program and archived its output at

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T22-56-00Z__p0257_n5_orbit_trivial_aut_exact.out`

creation commit

`a6e6e2f6dbf0c2660fc4ab3e176d6e1e3300f1d7`.

The run independently verifies:

- `STRONG_LABELLED_N5 = 5346`;
- `STRONG_ISOMORPHISM_CLASSES_N5 = 53`;
- `AUTOMORPHISM_HISTOGRAM = {1:38,2:12,4:1,5:1,10:1}`;
- the orbit-size sum `5346`;
- strong connectivity and trivial automorphism group of the new target;
- canonical nonisomorphism from both previously charged size-5 classes;
- every rational ranking gap on the entire coordinate box;
- the exact chart volume, second-neighbor bound, guard coefficient and square-root slack;
- the exact correction and endpoint arithmetic; and
- `B_AFTER_GT_0.629258051894 = True`.

The archived output ends

`ALL_EXACT_FINITE_CHECKS_PASS`.

This is a **SELF-CHECK**, not an independent audit. The proof above, rather than the program alone, is the theorem-sized claim.

## 12. Status, counters, audits, and next route

P0257 remains **PARTIAL / SOURCE OPEN**. The source's proposed limiting constant is neither proved to exist nor identified.

Because the frozen metric moved in this invocation:

- `unchanged_runs = 0`;
- HARD stuck-recovery episodes remain `0/2`;
- no handoff is triggered.

Required independent audits remain:

- P26: **NOT REQUESTED / NOT PRESUMED**;
- NM13-12: **NOT REQUESTED / NOT PRESUMED**.

The next run should not keep enumerating one more five-vertex orbit merely because 53 classes exist. The next planned recycled, nonconsecutive Section-B triple is **#5 / #9 / #30**:

- **#5 ADD A PARAMETER AND DIFFERENTIATE:** replace one common exclusion radius `H` by a one-parameter family tied to vertexwise second-neighbor radii and differentiate the certified intensity functional;
- **#9 RANDOMIZE:** expose the external Palm points relative to the component and seek a positive-probability clearance event weaker than the current uniform rectangle guard while keeping a rigorous finite-binomial transfer;
- **#30 ONE SCALE / ONE DIRECTION AT A TIME:** localize the union-of-disks geometry by scale and angular sector so any gain comes from a genuinely smaller guard measure, not a finer coordinate mesh.

If that route cannot move the tracked endpoint, it should be abandoned rather than followed by another certificate for the same number.

## 13. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  namespace: proofnet24/NM13-11/
  category: HARD_OUTSIDE
  source_id: P0257
  claim_path: operations/claims/P0257.md
  canonical_dedup_key: law_of_large_numbers_and_constants_for_nuv_lengths
  shard_residue_mod_13: 10
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: b_NUV_explicit_liminf_expectation_lower_endpoint
  metric_before_exact: "257829989578496350414183523146605335856248997408453788237962025484814476957683136019074638921462335179814079007196663994330380573638384791944133112730116386394080336881706051/409736496533210395577129470979508748365626015570562389564441613457911228367916571422161933413348402679750261900585439123098992187500000000000000000000000000000000000000000000"
  metric_before_decimal: "0.629258051845519310707290096835900616276392662852104615893410078498348714..."
  new_correction_exact: "2314212291015625000/46898200879888981540448041041"
  new_correction_decimal: "4.934543857967080409198483646196997965e-11"
  metric_after_exact: "4030587548353407239385594764200229614297797658205062329180415991935634988507131251165427843820794999771597107722461131707733943325633277304301536835785477343473397459589419707534599554139802937648679697/6405301507412145469471049291078200132062046565450533944155920254596661605498664430441568460794726368748340630284796689323210137382338787704649039451912789062500000000000000000000000000000000000000000000"
  metric_after_decimal: "0.629258051894864749286960900927885452738362642506997505460965740208615435..."
  movement: true
  section_b_methods_actual:
    - 14
    - 16
    - 24
  method_outcomes:
    14: "SUCCESS: quotient five-vertex strong 2-out digraphs by S5; topology automorphism size is the exact factorial-moment multiplicity penalty."
    16: "SUCCESS: exact census 5346 labeled / 53 isomorphism classes, automorphism histogram {1:38,2:12,4:1,5:1,10:1}."
    24: "SUCCESS: found a new Euclidean positive-measure trivial-automorphism sink-SCC chart and optimized the source-relevant intensity functional enough for a positive additive correction."
  finite_claim_checker: "proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T22-55-00Z__p0257_n5_orbit_trivial_aut_exact.py"
  checker_commit: b28e7dbe09af5b3d8d9434d4a02fb501a59a0ef1
  checker_output: "proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T22-56-00Z__p0257_n5_orbit_trivial_aut_exact.out"
  checker_output_commit: a6e6e2f6dbf0c2660fc4ab3e176d6e1e3300f1d7
  checker_label: SELF_CHECK_ONLY
  checker_result: ALL_EXACT_FINITE_CHECKS_PASS
  idea_before_code: "proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T22-50-00Z__p0257_orbit_extremal_route_idea.md"
  idea_commit: e6c643cf5ae0cb14a3ee53bec4fba1a11a3f7b1b
  unchanged_runs: 0
  hard_recoveries_used: 0
  hard_recoveries_allowed: 2
  p26_audit: NOT_REQUESTED_NOT_PRESUMED
  nm13_12_audit: NOT_REQUESTED_NOT_PRESUMED
  literature_check_date_utc: 2026-09-19
  literature_scope: "Cambridge DOI/source page; Aldous Berkeley research/publication pages; arXiv:1912.13175; bounded exact-title/NUV/Euclidean-random-points 2023-2026 web searches. No checked later primary source resolving the exact Euclidean first-order constant surfaced; bounded negative evidence only."
  ownership_check: "P0257 claim reread prewrite; owner still proofnet24/NM13-11/; no release/handoff/retirement/competing owner; exact predecessor-to-head compare 137 ahead, 0 behind, too_large=null, no P0257 claim mutation."
  next_section_b_methods:
    - 5
    - 9
    - 30
  next_step: "Seek a parametrized/vertexwise Palm clearance event with rigorously smaller guard measure; abandon if it does not move b_NUV rather than enumerate another orbit by default."
```
