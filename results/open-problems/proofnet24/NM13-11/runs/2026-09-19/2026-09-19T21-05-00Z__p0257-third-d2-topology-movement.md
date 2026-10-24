Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629258030552741666144008725369... -> b_NUV >= 0.629258046438982198074857419668... > 0.629258046`; actual Section-B methods tried: #3, #15, #25.**

# NM13-11 — P0257 third directed-2NN sink-topology movement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0257 / `operations/claims/P0257.md`**  
Canonical dedup key: `law_of_large_numbers_and_constants_for_nuv_lengths`  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 10`  
Status after this invocation: **PARTIAL / SOURCE OPEN**

## 1. Result and frozen metric

This invocation continues the already-admitted source P0257, David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs* (arXiv:1912.13175; *Probability in the Engineering and Informational Sciences* 36 (2022), 851–867, DOI 10.1017/S0269964821000115). It does **not** reopen intake, create a second claim, or select a replacement source.

The frozen metric remains exactly

`b_NUV = explicit certified endpoint in liminf_{n->infinity} E[L_n]/n >= b_NUV`

for Aldous's exact Euclidean random-points NUV model in the area-`n` scaling.

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T20-00-00Z__p0257-capsule-guard-movement.md`

created at commit

`58152c22f04afccfec2d31050300918ff073627d`.

Metric before this run:

`b_NUV >=`

`12234885369899315774910192590367613149468633559630832101342942986342507415367247043258638762394714330725215296855853141419683832042798882673372297 /`

`19443351973040638050987304673433346221975007518723198189172396736647229533566751930247359385542476562500000000000000000000000000000000000000000000`

`= 0.629258030552741666144008725369464071345769637757593902876157849635807123655699627949012263...`.

This run proves an **additive, topology-disjoint** four-point sink-component correction

`Delta_new >= 34478703 / 2170350054230822`

`= 1.5886240531930848694299457760505767...e-8 > 1.5e-8`.

Therefore

`b_NUV >=`

`428290077362103688393910556289374260624427851669128955928061085239297514491295131572164454010069801964500982465126129692695841537835318496791550852459470618357 /`

`680627096921253366568966735604927531896699764460645393329189347179240150914086801287321056287307690561375724195312500000000000000000000000000000000000000000000`

`= 0.629258046438982198074857419668921831851536676941650725297605646247807750117971133667474381...`.

In particular,

`b_NUV > 0.629258046`.

The source problem is still open. This run does **not** prove existence of Aldous's proposed limit `lim L_n/n`, does not identify that limit, and does not upgrade the source to PROVED.

## 2. Runtime / model-control truth

The task prompt requests `Model: GPT-6. Reasoning: maximum`. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, a binding maximum-effort setting, an hour-long execution, or a support escalation.

The exposed scheduled-task control surface still provides task title/prompt, schedule or relative-start data, timing mode, enabled state, listing, and ordinary updates. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-model/applied-effort receipt**. GPT-6/maximum is therefore prompt text only on this surface.

Making the requested setting binding would require an owner-authorized product/workspace/API/admin scheduling surface that actually persists model-family and reasoning-effort fields into inference routing and returns trustworthy per-run attestation.

Repository continuity also preserves the P26 permission history accurately: one earlier context returned `You cannot modify this task`, while a later authorized context successfully updated P26. Thus the historical denial was authorization/context-specific, not evidence of global immutability. If such a denial recurs, the compliant route is the same task's owning or otherwise authorized product/workspace/API/admin context, supported ownership/permission repair where available, or authorized platform support. It is **not** duplication, identity substitution, or permission bypass.

No scheduler, task configuration, permission, workflow, email/Gmail, Drive resource, public surface, paid-compute resource, shared root ledger, peer namespace, or canonical P0257 claim was modified in this invocation.

## 3. Authoritative continuity, required reads, and ownership race check

Before substantive work I freshly read or directly recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling NM13-11 predecessor above;
- the preceding four-point chain and C4/sink-SCC reports needed for disjointness bookkeeping;
- newest neighboring NM13-10 report `2026-09-19T20-52-30Z__admission-delta-screen-50-e0011-released-r6-no-r9-closable.md`;
- newest neighboring / designated-secondary-auditor NM13-12 report at commit `9caafdf1a51064e50672c9082d92ae85f87941a1` (`F0111` still pending; `P0205` source-ambiguous; no successor admission);
- current canonical `operations/claims/P0257.md` after substantive artifacts were written;
- repository-wide exact-ID / canonical-key / P0257-attempt searches; and
- the exact predecessor-creation-commit to final frozen-prewrite `master` comparison.

The append-only intake/source/attempt corpora are too large for an honest assertion that every unchanged historical byte was freshly rendered model-visible in one connector response. I make no such claim. The exact complete Git delta below is used for unchanged continuity, while P0257's canonical claim, aliases, attempt history, latest own state, and neighboring state were reopened directly.

Final frozen pre-report `master`:

`e327ce1698354e19d62c90f8ddad7091e442df96`.

Exact comparison

`58152c22f04afccfec2d31050300918ff073627d .. e327ce1698354e19d62c90f8ddad7091e442df96`

returned:

- status `ahead`;
- commits ahead **155**;
- commits behind **0**;
- total commits **155**;
- `too_large = null`.

Because `too_large=null`, the returned changed-file set is complete for that interval. It contains one unrelated claim-history addition, `operations/claims/E0011-REASSIGNED-2026-09-19.md`, but **no mutation of `operations/claims/P0257.md`, no P0257 release/handoff/retirement, no second P0257 owner, no root QUEUE/POSTED/RESULTS mutation, no campaign INDEX/RANKING mutation, no screened probability-intake `problems.jsonl` mutation, and no controlling owner/new-method/NM13 policy mutation**.

A final direct read of `operations/claims/P0257.md` at the frozen pre-report commit still records:

- status `CLAIMED / ADMITTED / HARD OUTSIDE`;
- owner `proofnet24/NM13-11/`;
- canonical dedup key `law_of_large_numbers_and_constants_for_nuv_lengths`;
- SHA-256 `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`;
- shard residue **10 mod 13**;
- campaign status `attempted_unsolved` and the historical nearest-neighbor-floor route.

No private-repository history known to be material to this continuation was inaccessible.

## 4. Actual Section-B methods and outcomes

All thirty Section-B methods have already appeared at least once in P0257's history. This invocation therefore uses the planned **recycled, nonconsecutive** triple #3/#15/#25 and does not misreport any of them as first-ever attempts.

### #3 PROVE SOMETHING STRONGER — success at the right abstraction level

Do not prove another statement tied to one named C4 or chain gadget. Strengthen the local mechanism to the following topology-independent form:

> Any finite **sink strongly connected component of the directed two-nearest-neighbor graph** with internal second-neighbor radius at most `Us` and all external distances at least `Hs>Us` forces at least `(H-U)s` of `L`-side surplus whenever it contains neither global Hamiltonian-path endpoint.

The proof uses only Hamiltonian-path boundary crossings, not consecutive NUV consumption. This is stronger than a gadget-specific trap statement. The theorem alone does not move the metric; movement comes from finding a genuinely new positive-density sink topology to which it applies.

### #15 BREAK THE SYMMETRY ON PURPOSE — success

The preceding charged four-point classes are the bidirected C4 family and a near-collinear chain family. Deliberately search for a third **non-isomorphic** strongly connected directed-2NN topology rather than refining either old geometry.

A positive-measure asymmetric four-point family below realizes exactly such a topology. Its canonical adjacency tuple under all 24 relabelings is

`((1,2),(0,2),(0,3),(1,2))`,

while the already charged chain and C4 classes canonicalize respectively to

`((1,2),(0,2),(0,3),(0,2))`

and

`((1,2),(0,3),(0,3),(1,2))`.

The exact checker verifies all 24 relabelings and certifies that the three topology classes are distinct.

### #25 COUNT THE SAME THING TWICE — success

Count the same local object in two compatible ways:

1. as an **ordered geometric quadruple** in the exact finite binomial process, which gives its expected asymptotic density after dividing by `4!`; and
2. as a **global sink SCC** of the directed-2NN graph, which gives vertex-disjoint Hamiltonian boundary charging.

The ordered count supplies the intensity; SCC uniqueness supplies the no-overlap certificate. This avoids an auxiliary packing lemma.

## 5. Research path before certification

The idea was written down before checker code, as required by the 90/10 policy.

The first probe used a narrow asymmetric box and already realized the missing topology. Its exact checker certified a small correction `>4.5e-10`. Rather than stop and file that tiny movement, the route was widened before final certification. A second idea note derived a much larger exact rational box from the topology inequalities themselves. The final metric below uses **only** the widened family; the narrow-family correction is not added and therefore cannot be double-counted.

This matters operationally: the finite checker followed the research idea, rather than the run being organized around manufacturing a checker for an unchanged number.

## 6. The general guarded sink-SCC boundary lemma

Work in a finite tie-free Euclidean configuration. Let `D_2` be the directed graph putting arcs from each point `v` to its first and second nearest neighbors. Let `P` be any Hamiltonian path through all points; the NUV visitation order is such a path.

For each vertex `v`, let

`r_1(v) <= r_2(v)`

be its first and second nearest-neighbor distances in the full configuration.

If `v` is not a global path endpoint, let its two incident path-edge lengths be `a_v <= b_v`. Since the path uses two distinct neighboring vertices,

`a_v + b_v >= r_1(v)+r_2(v)`.

This is the degree-two nearest-neighbor baseline already underlying the prior lower-bound package.

Now let `S` be a proper sink SCC of `D_2` and suppose, for some scale `s>0`,

`r_2(v) <= U s` for every `v in S`,

while every point outside `S` is at distance at least `H s` from every `v in S`, with `H>U`.

For an inside vertex `v`, let `m(v)` be the number of incident Hamiltonian-path edges crossing the cut `(S,S^c)`.

- If `m(v)=0`, no extra charge is claimed.
- If `m(v)=1` and `v` is not a global path endpoint, the crossing edge has length at least `Hs`, while the other incident edge is at least `r_1(v)`. Hence the local incident-length sum exceeds `r_1(v)+r_2(v)` by at least `(H-U)s`.
- If `m(v)=2`, both incident edges have length at least `Hs`, while `r_1(v)+r_2(v) <= 2Us`; hence the local surplus is at least `2(H-U)s`.

Therefore the contribution to the **`2L` side** above the degree-two baseline is at least

`cross_P(S) (H-U)s`,

where `cross_P(S)` is the number of path edges crossing the component boundary.

If `S` contains neither global path endpoint, then a Hamiltonian path must enter and leave it, so

`cross_P(S) >= 2`.

Thus every such component contributes at least

`2(H-U)s`

on the `2L` side, equivalently

`(H-U)s`

on the `L` side.

Distinct SCCs of one directed graph are vertex-disjoint. At most two sink SCCs can contain the two global path endpoints. Under a fixed scale cutoff `s<=M`, discarding those at most two exceptional components costs only `O(M)` total length, hence `o(n)` after division by `n`. This proves the asymptotic charge without assuming that NUV consumes a component consecutively and without assuming existence of the source limit.

## 7. A third robust four-point directed-2NN topology

Normalize an ordered quadruple by translation, rotation and scale:

`p1=(0,0), p2=(1,0), p3=(x,-r), p4=(z,-s)`.

Take the rational shape box

`13/100 <= x <= 49/100`,

`29/25 <= r <= 7/5`,

`51/100 <= z <= 81/100`,

`33/50 <= s <= 21/25`.

Its normalized four-dimensional volume is

`V = (36/100)*(6/25)*(30/100)*(9/50)`

`  = 729/156250`

`  = 0.0046656`.

Write `d_ij^2=|p_i-p_j|^2`. The exact inequalities are as follows.

First,

`d13^2 = x^2+r^2 >= (13/100)^2 + (29/25)^2 = 109/80`,

while

`d14^2 = z^2+s^2 <= (81/100)^2 + (21/25)^2 = 13617/10000`.

Since

`109/80 - 13617/10000 = 1/1250 > 0`,

we have `d13>d14>1` uniformly.

Second,

`d23^2-d13^2 = 1-2x >= 1/50 > 0`

because `x<=49/100`.

Third,

`d14^2-d24^2 = 2z-1 >= 1/50 > 0`

because `z>=51/100`.

Fourth,

`d14^2-d34^2 = x(2z-x)+r(2s-r)`.

On this box `z>x`, so the first term increases with both `x` and `z`; also `r>s`, so the second term increases with `s` and decreases with `r`. Therefore its exact minimum occurs at

`x=13/100, z=51/100, r=7/5, s=33/50`,

and equals

`37/10000 > 0`.

Finally,

`d24^2 <= (49/100)^2 + (21/25)^2 = 9457/10000 < 1`.

These strict inequalities imply, throughout the whole shape box,

`N2(p1)={p2,p4}`,

`N2(p2)={p1,p4}`,

`N2(p3)={p1,p4}`,

`N2(p4)={p2,p3}`.

Indeed:

- from `p1`, `p2` has squared distance `1`, `p4` has smaller distance than `p3`, and `p3` has distance `>1`;
- from `p2`, `p4` has distance `<1`, `p1` has distance `1`, and `p3` is farther than `p1` because `d23>d13>1`;
- from `p3`, both `p1` and `p4` beat `p2`, since `d23>d13>d14>d34` where needed; and
- from `p4`, both `p2` and `p3` beat `p1`, since `d14>d24` and `d14>d34`.

The resulting directed graph is strongly connected: for example `p1 <-> p2`, `p1 -> p4 -> p3 -> p1`, and every vertex reaches every other.

The exact checker canonicalizes this topology over all 24 label permutations and obtains

`CAN_NEW   = ((1,2),(0,2),(0,3),(1,2))`.

For comparison, the already charged non-C4 chain topology from the 19:00Z predecessor and the earlier C4 topology canonicalize to

`CAN_CHAIN = ((1,2),(0,2),(0,3),(0,2))`,

`CAN_C4    = ((1,2),(0,3),(0,3),(1,2))`.

Thus this is a genuinely new four-point `D_2` sink topology, not a coordinate re-description of an old charged class.

## 8. Internal radius and source-valid external guard

The largest possible squared internal second-neighbor radius in the new family is bounded by

`d13^2 <= (49/100)^2 + (7/5)^2 = 22001/10000`.

All other internal second-neighbor distances are smaller by the topology inequalities above. Choose

`U = 297/200`.

Then

`U^2 - 22001/10000 = 41/8000 > 0`.

Choose the external guard radius

`H = 37/20`.

The Hamiltonian-boundary surplus parameter is therefore

`delta = H-U = 73/200`.

Require that no source point outside the selected quadruple lies within distance `Hs` of any of its four vertices. Since every selected vertex already has two internal neighbors within `<Us<Hs`, the guard forces its two **global** nearest neighbors to stay inside the quadruple. Combined with strong connectivity, the selected four-set is a global sink SCC of `D_2`.

All normalized centers lie inside the rectangle

`K=[0,1] x [-7/5,0]`.

Hence the union of four radius-`H` guard disks is contained in the parallel body `K+B_H`. By the exact rectangle Steiner formula,

`|K+B_H| = 7/5 + 2H(1+7/5) + pi H^2`.

Using only `pi<22/7`,

`|K+B_H| <= Q := 29451/1400 = 21.0364285714...`.

For the later `Q^(7/2)` denominator, the checker certifies

`(1147/250)^2 - Q = 11651/875000 > 0`,

so

`sqrt(Q) < 1147/250`.

No finite plot or simulation is used anywhere in this argument.

## 9. Exact finite-binomial to infinite-volume transfer

Return to the **exact source model** in the area-`n` square: `n` iid uniform points, intensity one after scaling, and the NUV Hamiltonian path.

Fix a scale cutoff `M`. Restrict the anchor point to an interior sub-square far enough from the boundary that the full guard of every accepted shape with `s<=M` is contained in the source square. The lost anchor area is `O(sqrt(n))`, so divided by `n` it vanishes for fixed `M`.

Parameterize an ordered accepted quadruple by

- anchor `a in R^2`;
- scale `s`;
- rotation `theta`;
- shape coordinates `(x,r,z,sigma)` in the box above.

The relative-coordinate Jacobian is

`s^5 ds dtheta dx dr dz dsigma`.

For four distinct labeled source points, the exact binomial factorial density contributes

`(n)_4 / n^4`.

Conditional on the quadruple, let `A_guard` be the actual guard area. Since

`A_guard <= Q s^2`,

the exact probability that all remaining `n-4` source points avoid the guard is

`(1-A_guard/n)^(n-4)`.

For fixed accepted shape and fixed scale, as `n->infinity` this tends to

`exp(-A_guard) >= exp(-Q s^2)`.

The accepted family has finite cutoff and finite guard, so dominated convergence applies for fixed `M`.

Each non-endpoint sink component contributes at least `delta*s` to the `L`-side surplus by Section 6. Count ordered quadruples and divide by `4!`. An unordered four-set has at most 24 labelings, so this cannot overcount components even if more than one ordering lands in the accepted normalized family.

Thus for fixed `M`, after dividing by `n` and taking `n->infinity`, the new contribution is at least

`(1/4!)*(2*pi)*V*delta * integral_0^M s^6 exp(-Q s^2) ds`.

Discarding the at most two endpoint-containing sink SCCs loses only `O(M)/n` after normalization. Then let `M->infinity`. Monotone convergence gives

`Delta_new >= (1/24)*(2*pi)*V*delta * integral_0^infinity s^6 exp(-Q s^2) ds`.

The Gaussian integral is exact:

`integral_0^infinity s^6 exp(-Q s^2) ds = 15 sqrt(pi)/(16 Q^(7/2))`.

Therefore

`Delta_new >= (5*pi^(3/2)/64) * V * delta * Q^(-7/2)`.

For an exact rational lower certificate use only

`pi > 3`, `sqrt(pi)>17/10`, hence `pi^(3/2)>51/10`,

and

`sqrt(Q)<1147/250`.

The resulting exact bound is

`Delta_new >= 34478703/2170350054230822`

`= 1.5886240531930848694299457760505767039184056822421...e-8`.

This transfer takes `n->infinity` **before** removing the fixed scale cutoff. It does not assume Poissonization of the source, NUV stabilization, local weak convergence of the NUV path, or existence of `lim L_n/n`.

## 10. Additivity and no-double-counting proof

The previous endpoint already contains the baseline and earlier topology-disjoint sink-SCC improvements. The present correction is **added**, not substituted, for the following exact reason.

In any tie-free realization the global directed-2NN graph is uniquely determined. A sink SCC has one intrinsic isomorphism type. The new four-point component has canonical topology

`((1,2),(0,2),(0,3),(1,2))`,

which is distinct from both previously charged four-point topology classes. Hence one size-4 sink SCC cannot be counted both as a new component and as an old C4/chain component.

Moreover, distinct SCCs of a directed graph are vertex-disjoint. Thus the already charged size-3, size-4, and size-5 `D_2` sink components and the present new size-4 topology can all be charged without sharing a vertex in the degree-two baseline accounting.

The first narrow exploratory box from this invocation is **not** included in the final arithmetic. Only the widened box in Sections 7–9 contributes `Delta_new`, so there is also no within-run overlap issue.

This establishes the additive movement from the predecessor endpoint to the endpoint in Section 1.

## 11. Exact self-check artifacts

The research idea was written before checker code.

Initial missing-topology idea:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T20-55-00Z__p0257_missing_d2_topology_idea.md`

creation commit `f517eac48900e725a62e568548da6756b1fa8050`.

Initial narrow-box viability checker and output:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T20-57-00Z__p0257_missing_d2_topology_exact.py`

creation commit `091105847a5014d480cef6b88143fc6bcfe4563b`,

and

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T20-57-00Z__p0257_missing_d2_topology_exact.out`

creation commit `91bf350a108213dcb49add65b81f839f12b7f474`.

That probe established the new topology but its smaller correction is superseded and **not counted**.

Widened-family idea before final checker:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T20-59-00Z__p0257_asymmetric_topology_box_idea.md`

creation commit `b659a16a0118d36631fafcf2b9bdb2e9811a4c85`.

Final exact checker:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T21-02-00Z__p0257_widened_missing_d2_topology_exact.py`

creation commit `75c9d1f5ac5fa02bfd6bc7eaf20241154a4eb87e`.

Archived execution output:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T21-02-00Z__p0257_widened_missing_d2_topology_exact.out`

creation commit `e327ce1698354e19d62c90f8ddad7091e442df96`.

The final output certifies, among other statements:

- `D13_GT_1_SLACK = 29/80`;
- `D13_GT_D14_SLACK = 1/1250`;
- `X_HALF_SLACK = 1/100`;
- `Z_HALF_SLACK = 1/100`;
- `D14_GT_D34_SLACK = 37/10000`;
- `D24_LT_1_SLACK = 543/10000`;
- the three canonical four-point topology tuples are pairwise distinct;
- `SHAPE_VOLUME = 729/156250`;
- `U2_SLACK = 41/8000`;
- `DELTA = 73/200`;
- `Q = 29451/1400`;
- `SQRTQ_SQUARE_SLACK = 11651/875000`;
- `DELTA_NEW = 34478703/2170350054230822`;
- `DELTA_NEW_GT_1.5E-8 = True`;
- the exact new endpoint fraction;
- `B_NEW_GT_0.629258046 = True`; and
- terminal line **`ALL_EXACT_FINITE_CHECKS_PASS`**.

This is a self-check, not an independent audit.

## 12. Fresh original-source and literature check — 2026-09-19

I freshly reopened the original Aldous paper through Cambridge Core / UC Berkeley eScholarship. The paper defines the Euclidean random-points model and at Equation (4) proposes

`c := lim n^{-1} L_n`,

with small-scale simulation near `c≈0.9`; immediately afterward it says the only rigorous information there is the order upper bound `E[L_n] <= A n`. Section 5 says further progress needs a technique beyond the paper's ball-covering argument, explicitly mentions the Poisson-plane local weak limit, and separately suggests finding restrictions on local NUV path behavior. That is directly aligned with, but does not prove, the present local sink-SCC route.

Primary-source locations checked:

- Cambridge article / DOI: `https://doi.org/10.1017/S0269964821000115`;
- eScholarship PDF: `https://escholarship.org/uc/item/90j8z5bk`;
- Aldous's maintained home/research page: `https://www.stat.berkeley.edu/~aldous/`.

Aldous's page, crawled on 2026-09-19, still lists *The Nearest Unvisited Vertex Walk on Random Graphs* and states the challenge as improving beyond order of magnitude for models of random graphs.

Bounded current searches on 2026-09-19 included:

- exact title `"The Nearest Unvisited Vertex Walk on Random Graphs"`;
- `"nearest unvisited vertex" Euclidean random points` with 2023–2026 terms;
- `NUV walk` / first-order constant variants;
- recent directed / `k`-nearest-neighbor graph component and percolation literature.

The adjacent literature includes Jahnel–Köppl–Lodewijks–Tóbiás, *Percolation in lattice k-neighbor graphs*, *Journal of Applied Probability* 62 (2025), which studies directed `k`-neighbor graphs on lattices and their percolation. It does **not** establish the Euclidean NUV-length lower bound or Equation-(4) limit. Recent nearest-neighbor-graph algorithmic papers are likewise different problems.

No checked later primary source in this bounded search resolved Aldous's Euclidean first-order constant or supplied the present explicit endpoint. This is **bounded negative evidence only**. It is not a proof of worldwide openness, novelty, priority, or correctness of this run's theorem.

## 13. Status, counters, audit gate, and next route

Status after this invocation: **PARTIAL / SOURCE OPEN**.

The frozen metric moved, so:

- `unchanged_runs = 0`;
- HARD stuck/recovery episodes remain `0/2`;
- no Section-I stuck report is triggered;
- no handoff or rotation is triggered.

P26 audit status: **NOT REQUESTED / NOT PRESUMED**.  
NM13-12 secondary audit status: **NOT REQUESTED / NOT PRESUMED**.

Closure is not claimed. The source-level limit still lacks an existence/identification proof, and the present metric theorem has only its own exact self-check.

Next substantive triple, deliberately different from #3/#15/#25:

- **#1 CHANGE THE CATEGORY:** recast finite `D_2` sink components as a finite-type geometric hypergraph / mass-transport object rather than a list of coordinate boxes;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** inspect component-intensity constants and exact small-component formulas in continuum nearest-neighbor / stochastic-geometry literature for a transferable Palm identity;
- **#26 HUNT THE SPORADIC CASE:** test whether a size-4 or size-5 sink topology outside all presently charged classes admits a much larger positive-measure family, with exact topology certification before any new checker is built.

The next run must not merely tighten `Q`, subdivide this same box, or file another certificate for the same endpoint. It should seek a new component class or a topology-level intensity theorem that moves `b_NUV` by a genuinely new mechanism.

## 14. Structured ledger_delta for P26

```json
{
  "worker": "NM13-11",
  "namespace": "proofnet24/NM13-11/",
  "category": "HARD OUTSIDE",
  "source_id": "P0257",
  "claim_id": "P0257",
  "canonical_dedup_key": "law_of_large_numbers_and_constants_for_nuv_lengths",
  "shard_residue_mod_13": 10,
  "metric": "b_NUV: certified endpoint in liminf E[L_n]/n >= b_NUV",
  "metric_before": "0.629258030552741666144008725369464071345769637757593902876157849635807123655699627949012263...",
  "metric_after": "0.629258046438982198074857419668921831851536676941650725297605646247807750117971133667474381...",
  "metric_delta_exact": "34478703/2170350054230822",
  "metric_delta_decimal": "1.5886240531930848694299457760505767e-8",
  "status": "PARTIAL",
  "source_status": "OPEN",
  "methods_actual": [3, 15, 25],
  "method_outcomes": {
    "3": "success: topology-independent guarded D2 sink-SCC Hamiltonian boundary theorem",
    "15": "success: third non-isomorphic positive-measure four-point D2 sink topology",
    "25": "success: ordered factorial-moment count plus SCC uniqueness/disjointness"
  },
  "unchanged_runs": 0,
  "hard_recoveries_used": 0,
  "hard_recoveries_cap": 2,
  "p26_audit": "NOT_REQUESTED_NOT_PRESUMED",
  "nm13_12_audit": "NOT_REQUESTED_NOT_PRESUMED",
  "next_methods": [1, 17, 26],
  "next_step": "seek a new sink-component class or topology-level Palm/mass-transport intensity theorem; do not refine this box merely for constants"
}
```
