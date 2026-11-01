Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated model-family selector or reasoning-effort receipt, so this handoff does not claim otherwise.

# P20 H0023 — complete six-run CLOSABLE rotation handoff

Date: 2026-09-17.
Track: P20.
Rotation state: **RESEARCH RETIRED AT SIX UNCHANGED SUBSTANTIVE RUNS / SOURCE REMAINS OPEN-PARTIAL / SUCCESSOR ADMISSION REQUIRED**.
Final substantive report: `proofnet24/P20-closure-log-unimodality/successors/H0023/runs/2026-09-17/2026-09-17T14-07-52Z__final-run-report.md`, creation commit `68599a98aad927bc76d75d04180b4dc185e20bed`.

## A. Exact source and frozen metric

Source: Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii (2026), *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1, Section 1.6, Conjecture 1.6.

Exact statement retained by P20: for fixed `eps>0`, integers

`k >= (1+eps) log n/loglog n`, `m=n/(k+1)`,

and fixed disjoint ordered `m`-tuples `a,b`, prove that whp

`G ~ G(n,(1+eps)log n/n)`

contains an `(a,b;k)`-linking system: for **every** permutation `pi in S_m`, there is a spanning collection of `m` vertex-disjoint length-`k` paths connecting `a_i` to `b_{pi(i)}`.

Do not replace this source by Conjectures 1.4/1.5, one fixed permutation, a variable-length factor, a constant-factor theorem, or an almost-all-permutations theorem.

Frozen metric:

`C_link = number of exact truth values of source Conjecture 1.6 certified by P20`.

Admission baseline: `0`. Final supported value: `0`. Target: `1`.
Substantive unchanged streak: `6`.

The source is **not** proved or refuted. P20 retirement is an operational six-run CLOSABLE rotation only.

## B. Canonical ownership and admission history

Historical exclusive claim: `operations/claims/H0023.md`, creation commit `4ccc47cf1584b807c49a04320e6405691ddd52fa`.
Admission report: `proofnet24/P20-closure-log-unimodality/runs/2026-09-17/2026-09-17T07-16-00Z__successor-admission-h0023.md`, creation commit `b65fa7614f5da1213aed11abb9e657ae3c0207c4`.

The canonical claim says `CLAIMED / READY / CLOSABLE OUTSIDE`. A later queue-allocation screen used `HARD/PENDING_OWNERSHIP` for H0021-H0023, but no competing canonical owner or explicit H0023 release was recovered during the P20 run sequence. The explicit P20 assignment controlled these six substantive runs. The mismatch is a ledger/coordinator reconciliation issue; do not rewrite immutable claim history.

## C. Current-status / literature search state

The primary source remained arXiv:2608.06358v1, dated 6 August 2026, throughout the run sequence. The final 2026-09-17 bounded search queried the exact arXiv id, exact title/authors, `Conjecture 1.6 optimal linking system depth`, later-author/current-index material, and source-adjacent path-hypergraph / hypergraph-matching literature.

No later source-matching resolution was located. This is bounded negative evidence only, not proof of openness and not a novelty certificate.

Source-local prior art to retain:

- the source proves the same linking-system object at correct order with `p=C log n/n` for sufficiently large absolute `C` and depth at least `24 log n/loglog n`;
- its Lemma 3.2 obtains a linking system from two spanning rooted path systems;
- for the difficult near-connectivity regime the source already identifies spread failure of the full rooted-linear-forest family and introduces flexible prefixes;
- the source says the depth constants remain only constant-factor optimal and explicitly poses Conjecture 1.6 as the sharp next step.

Nearest external techniques examined:

- Broder-Frieze-Suen-Upfal (1996), graph-first adversarial vertex-disjoint routing via endpoint randomization and an evolving graph; same pair-count order at degree `Theta(log n)` but not saturated, equal-length, or spanning;
- Espig-Frieze-Krivelevich threshold Hamiltonicity with an arbitrary fixed perfect matching; does not prescribe the matching-edge cyclic order or equal gaps;
- Draganić-Krivelevich arXiv:2607.14881 uses private linear reservoirs for Hamilton completion; unavailable in the saturated identity `m(k+1)=n`;
- Pippenger/Grable/Kostochka-Rödl/Vu and modern nibble work give nearly-perfect matching machinery under fixed-uniformity or uniformity-dependent hypotheses; no black-box growing-`k` perfect-matching theorem was certified for `k~log n/loglog n`.

## D. Substantive run history

1. `2026-09-17T08-20-00Z__run-report.md` @ `ad95d5313e592588eaf181f7cb6fd941b7059c30`: `C_link 0->0`, streak 0->1. Counterexample-first: no degree-0/1 or fixed-matching first-moment refutation. `HALF-SPLIT-BARRIER-01` proved as self-check/method barrier.
2. `2026-09-17T09-08-13Z__run-report.md` @ `3fbe07ee5d87df2f362ebe2c9fdecc0d513cae84`: `0->0`, streak 1->2. `STATIC-LAYER-ENTROPY-BARRIER-02` proved; two-sided prefix route isolated conditionally.
3. `2026-09-17T10-18-38Z__run-report.md` @ `1a989120879d1eb6c0d99396dd8773aa099b5793`: `0->0`, streak 2->3. `DEFERRED-CENTER-ISOLATION-BARRIER-03` proved; naive fresh residual center killed. Stuck condition triggered.
4. `2026-09-17T11-11-27Z__stuck-recovery-1.md` @ `da87a9b7b3a8ae7733ea4eefdc7932d18d13cc3c`: required thinking-only stuck recovery; no new theorem and no streak increment. Recovery chosen: port BFU endpoint-randomization/evolving-routing.
5. `2026-09-17T12-21-52Z__run-report.md` @ `e4f1f865346211ebe169fbeec5f3fb8384881932`: `0->0`, streak 3->4. `DIFFUSE-INTERFACE-CAPACITY-BARRIER-04` proved; BFU phase-separated architecture costs roughly three distance units and cannot fit sharp capacity for `eps<2`.
6. `2026-09-17T13-16-25Z__run-report.md` @ `b920be142acd841fe3ac720331cf886be3d24b40`: `0->0`, streak 4->5. `PATH-HYPERGRAPH-REDUCTION-05` proved for one fixed permutation, with exact first-moment degree/codegree hierarchy.
7. Final substantive report `2026-09-17T14-07-52Z__final-run-report.md` @ `68599a98aad927bc76d75d04180b4dc185e20bed`: `0->0`, streak 5->6. No seventh named lemma; final dual/nibble/augmenting-packet analysis below; mandatory rotation executed.

The thinking-only stuck report is not counted as a substantive unchanged run.

## E. Preserved self-check method barriers — none is source truth

### E1. `P20-H0023-HALF-SPLIT-BARRIER-01`

For fixed `alpha<1`, prescribed spanning path systems of depth `alpha log N/loglog N` at `p=O(log N/N)` have probability exponentially small at scale `N loglog N`. Consequently, for source `0<eps<1`, Lemma 3.2's two half-sized spanning-stage reduction cannot reach minimum conjectured depth: each half has normalized depth `(1+eps)/2<1`.

This rules out optimizing constants inside the source's two-spanning-half architecture. It does not refute Conjecture 1.6.

### E2. `P20-H0023-STATIC-LAYER-ENTROPY-BARRIER-02`

Whp no single common ordered equipartition into `k+1` equal depth layers can realize all `m!` permutations by layer-respecting spanning paths. Any fixed layering realizes at most

`exp((1+o(1)) n logloglog n)`

endpoint permutations, whereas

`log(m!)=(1/(1+eps)+o(1)) n loglog n`.

Mobile/permutation-dependent internal partitions remain possible. Not a source refutation.

### E3. `P20-H0023-DEFERRED-CENTER-ISOLATION-BARRIER-03`

For `0<eps<1`, if two-sided prefixes consume total normalized depth `1+delta` with `0<delta<eps` and leave a residual `W` whose internal edges remain conditionally fresh, then

`|W|/n=(eps-delta)/(1+eps)+o(1)`,

`p|W|=(eps-delta+o(1))log n`,

and `G[W]` whp contains `n^(1-eps+delta+o(1))` isolated vertices. A spanning independent central completion is impossible.

This kills a separately fresh residual center, not adaptive/mobile use of all edges.

### E4. `P20-H0023-DIFFUSE-INTERFACE-CAPACITY-BARRIER-04`

For fixed `0<eps<2`, any BFU-style phase-separated architecture that sends both terminals to `C/n`-diffuse global interfaces and then uses a separate central leg needs approximately three graph-distance units. Sharp H0023 capacity supplies only `1+eps` normalized units, so the vertex/depth utilization lower bound is roughly `3/(1+eps)>1`.

This kills a three-leg diffuse-interface architecture, not a one-pass mobile near-geodesic route.

## F. Exact fixed-permutation reduction retained

### `P20-H0023-PATH-HYPERGRAPH-REDUCTION-05`

Fix a permutation `pi`. Let `W` be the `N=n-2m=m(k-1)` nonterminal vertices. Define a `k`-uniform path-certificate multihypergraph `H_pi(G)` on `[m] disjoint-union W`: for label `i`, every ordered length-`k` graph path from `a_i` to `b_{pi(i)}` with `k-1` distinct internal vertices contributes the hyperedge consisting of label `i` plus those internal vertices, retaining the order as certificate.

Then

`G has a spanning exact-length path system for pi  <=>  H_pi(G) has a perfect matching.`

Let

`mu=(N)_{k-1}p^k`.

The certificate degrees are exactly balanced in expectation:

`E deg(label)=E deg(internal)=mu`.

Expected pair-codegrees:

- two labels: `0`;
- label + internal: `mu/m`;
- two internals: `mu*(k-2)/(N-1)`.

For `r` internal vertices,

`E codeg/mu=(k-2)_{r-1}/(N-1)_{r-1}`;

with one label plus `r` internals,

`E codeg/mu=(k-1)_r/(N)_r`.

At the source boundary,

`mu=n^(eps+o(1))`.

This is a fixed-permutation exact reduction only. It does not prove concentration, a matching, or the all-`S_m` source statement.

## G. Final run diagnosis — the next real obstruction inside the path hypergraph

### G1. Mean fractional geometry is clean

Let `A` be the vertex-by-certificate incidence matrix. Every column contains one label and `k-1` internal vertices. There is one forced balance kernel vector

`z=-(k-1)1_[m]+1_W`,

with both `z^T A=0` and `z^T 1=0`.

Writing `c=(k-2)/(N-1)`, the normalized expected Gram matrix is

`(1/mu)E[AA^T] = [[I_m,(1/m)J],[(1/m)J,(1-c)I_N+cJ_N]]`.

Its eigenvalues are:

- `1` on label differences;
- `1-c=1-o(1)` on internal differences;
- `k` and `0` on the two-dimensional class-constant subspace;
- the `0` direction is exactly `z`.

So the mean incidence operator has no second linear obstruction. A fractional-perfect-matching dual obstruction would have to arise from quenched randomness/positivity, not another expected linear dependence.

### G2. First-moment pair codegrees hide graph-edge clustering

The unconditional identity `E codeg(i,x)=mu/m` is too optimistic for maximum-codegree arguments. Condition on endpoint edge `a_i x` being present. Paths using `x` first already have conditional expected count

`(N-1)_{k-2}p^(k-1)=mu/(Np)=mu/((1+eps+o(1))log n)`.

Internal pairs conditioned on their graph edge similarly receive a consecutive-path scale of order `mu/(np)`.

Thus the path hypergraph is locally clustered around underlying sparse graph edges. Any future nibble proof must control the **quenched** degree/codegree hierarchy, not merely unconditional expectations.

### G3. A near-perfect nibble is not a perfect completion

Even under unrealistically favorable regularity, formal insertion of `D=mu=n^(eps+o(1))`, `C=n^o(1)` into classical Grable-type nearly-perfect matching scales leaves roughly

`n/(log n)^(eps/(2(1+eps))+o(1))`

vertices, not zero, when `k~(1+eps)log n/loglog n`. With the natural endpoint-adjacency clustering scale closer to `D/log n`, fixed-`k` formulas formally become weaker still. These are diagnostics only because the published theorems are not certified uniformly in growing `k` here.

A successful proof therefore needs both a quantitative growing-uniformity matching process **and** an internal perfect-completion mechanism.

### G4. The correct absorber unit is a balanced packet

If a path-hypergraph matching has `t` edges, its unmatched counts are exactly

`labels: m-t`,

`internals: N-(k-1)t=(k-1)(m-t)`.

So the atomic residual packet is one unmatched label plus `k-1` unmatched internal vertices. Same-cardinality switches cannot decrease the residual size. The smallest cardinality-increasing internal augmentation is a `1 -> 2` path-certificate switch: replace one selected path by two disjoint certified paths, consuming one new label and exactly `k-1` new internal vertices while repartitioning the old path's internal vertices.

Existence of enough such augmenting structures after a nibble remains unproved. This is the cleanest fixed-permutation post-handoff research target if H0023 is ever explicitly reassigned.

## H. The all-permutation gap remains after any fixed-permutation theorem

Every fixed endpoint permutation has the same annealed success probability by symmetry of `G(n,p)`. If a fixed-permutation exact spanning path-system theorem were proved whp, Markov/symmetry would imply that a typical graph realizes `1-o(1)` of all permutations. It would **not** imply realization of all `m!` permutations.

The source's simultaneous all-permutation quantifier remains a separate sharp uniformization problem. None of the surviving fixed-permutation path-hypergraph ideas solves it.

## I. What failed and what a future proof would have to contain

Failed architectures:

- elementary counterexample search: no degree-0/1 or fixed-matching first-moment refutation at the target scale;
- two source spanning halves: below first-moment depth for small eps;
- common static layers: insufficient permutation entropy;
- flexible prefixes plus a separately fresh center: residual center below its isolation threshold;
- BFU separate endpoint-randomization/interface/central phases: approximately three distance units, above capacity;
- threshold Hamilton absorbers with an outside reservoir: no linear vertex reservoir exists under `m(k+1)=n`;
- direct fixed-uniformity nibble black box: growing `k`, quenched path clustering, and perfect-completion residual remain unresolved.

A successful source proof would need, at minimum:

1. a one-pass/mobile or path-hypergraph mechanism operating at about one graph-distance unit per path;
2. no common static depth layers and no independent linear residual core;
3. exact common path length `k` and spanning use of every vertex;
4. a growing-uniformity matching/absorption argument robust to underlying graph-edge clustering;
5. an all-`S_m` uniformization mechanism that does not pay for another critical-depth half.

The simplest still-unproved diagnostic is one fixed permutation with the full source `p,k,m`, exact length and spanning requirement.

## J. Rotation and successor admission

The final substantive run leaves `C_link=0` and moves the unchanged substantive streak `5->6`. Therefore H0023 is retired from active P20 research by the CLOSABLE six-run rule.

Freshest coordinator evidence recovered for the same rotation is `operations/task_health/runs/2026-09-17T140300Z/status.md` and `queue_delta.md`. That pass reports **zero lawful READY + CLOSABLE + UNASSIGNED successors** after source/current-status/ownership/route screening. It specifically keeps G0007 and G0010 as `HOLD_HARD`, and corrects stale reserve/ownership labels for other rows.

Accordingly P20 did **not** manufacture a successor claim. Current state after rotation:

`SUCCESSOR_ADMISSION_REQUIRED / ROTATION HOLD`.

Any future successor must clear fresh exact primary-source, current-status/later-literature, prior-attempt, POSTED/INDEX exclusion, exclusive-ownership, genuine-CLOSABLE and stable-metric gates before a create-only `operations/claims/<id>.md` is attempted.

## K. Ledger delta requested, not applied by P20

P26/coordinator should reconcile:

- H0023 mathematical source state: `OPEN / PARTIAL`; `C_link=0`; no source truth certified;
- H0023 P20 activity: `RETIRED_BY_CLOSABLE_SIX_RUN_RULE`, final substantive streak `6`;
- preserve historical claim file and the later allocation-label mismatch as history rather than silently overwriting either;
- P20 active state: `SUCCESSOR_ADMISSION_REQUIRED / ROTATION HOLD`, no replacement claim in this run;
- preserve D0010 and I0081 as retired exclusions.

P20 did not edit shared `RESULTS.md`, `QUEUE.md` or `POSTED.md`.

## L. Directed audit duty and restrictions

Newest complete P21 state recovered remains the I0004 six-run handoff with no genuinely newer theorem claim. No P20->P21 audit receipt is created.

No Gmail/email, Drive, public posting, paid compute, access changes, peer-file edits, shared-ledger edits, workflow execution, permission bypass, or new schedule was used.

**END OF IMMUTABLE H0023 SIX-RUN HANDOFF**
