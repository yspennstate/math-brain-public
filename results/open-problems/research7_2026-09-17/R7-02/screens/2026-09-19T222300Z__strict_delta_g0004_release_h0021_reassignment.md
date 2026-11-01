Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-02 strict-delta successor screen — G0004 release / H0021 reassignment

## Purpose

R7-02 is still `PENDING_ADMISSION`. This screen examines only the material canonical-claim changes after the preceding own report rather than recycling the already exhausted P/C/D/E/F/G/H/I candidate corpora. The exact R7-02 partition is the case-sensitive rule

`sum(ord(c) for c in canonical_id) % 7 == 1`.

The slot/native identity remains `R7-02 Finite Certificate Research`, native ID `6aabe797a39081919acc889f29f4c556`, preferred class `CLOSABLE OUTSIDE`.

## Captured repository state and continuity

Run-start master was

`0b614e71b5931f6b3d7e57e1a802e91f07f3798b`.

Previous immutable R7-02 report:

`research7_2026-09-17/R7-02/runs/2026-09-19/2026-09-19T211900Z__report.md`

creation commit:

`84ea1e28117610e40eeb683c02a8bfd829e678c1`.

Required current surfaces were reread/reconciled: owner directive, visible-fleet entrypoint, R7 registry, root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md` and `RANKING.md`, current canonical claims, own path-scoped history, and the relevant R17 handoff/source records.

Path-specific history since the preceding report timestamp shows no new commit to root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`, or campaign `RANKING.md`. Thus the material admission-side delta is in canonical claim ownership/status changes, not a newly ranked queue row.

## Canonical claim changes in the strict delta

The post-report claim-change stream contains these material events:

1. `G0004`: R17 explicitly released Lucas Flammant's finite-graph percolation Conjecture 2.2 after exhausting its HARD lifecycle.
2. `H0021`: the previously released tree-universality conjecture was re-assigned to R17 with a fresh HARD route.
3. `B-WEAK-EVEN-LOGCONCAVE`: released after HARD7-01 Section-I exhaustion.
4. `MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS`: released after HARD7-01 Section-I exhaustion.
5. `AK-KATZIN-C41-EQUALITY`: literal equality clause recorded as exactly refuted and released as a resolved literal target.
6. `LOG-BRUNN-MINKOWSKI-SYMMETRIC`: newly claimed by HARD7-01.

Exact checksum residues are:

| canonical ID | checksum mod 7 | disposition for R7-02 |
|---|---:|---|
| `G0004` | 1 | shard-compatible, newly free, but HARD rather than CLOSABLE |
| `H0021` | 1 | shard-compatible but immediately re-owned by R17 and HARD |
| `B-WEAK-EVEN-LOGCONCAVE` | 3 | off shard |
| `MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS` | 5 | off shard |
| `AK-KATZIN-C41-EQUALITY` | 4 | off shard and resolved literal target |
| `LOG-BRUNN-MINKOWSKI-SYMMETRIC` | 2 | off shard and owned |

Therefore the only newly free shard-1 source requiring a fresh R7-02 source-class gate is `G0004`.

# G0004 source gate

## Exact outside source and statement

Lucas Flammant, *A conjecture implying theta(p_c)=0 for Bernoulli bond percolation on Z^d*, arXiv:2609.03492, Conjecture 2.2.

For Bernoulli bond percolation on an arbitrary finite graph `G=(V,E)`, an origin `o`, a boundary set `B`, and increasing events `(E_b)_{b in B}` satisfying

`P(E_b) >= 1-epsilon`,

prove the existence of a universal function `phi(epsilon) -> 1` as `epsilon -> 0` such that

`P[ union_{b in B} ({o<->b} cap E_b) ] >= phi(epsilon) P[o<->B]`

uniformly over all of the source quantifiers. The source proves the outer-face planar case with `phi(epsilon)=1-2 sqrt(epsilon)`; the unrestricted finite-graph conjecture is what remains.

Current canonical status after the R17 handoff is `SOURCE OPEN / PARTIAL / RELEASED BY R17`, with no current owner. The claim records a bounded source check dated 2026-09-19 finding the Flammant preprint still current and no later primary source claiming the unrestricted theorem. This is bounded negative evidence, not worldwide-open or novelty certification.

## Why “finite graph” does not make the source a finite-certificate CLOSABLE target

R17's exact failure-kernel reduction writes, for decreasing kernels

`q_b = 1-P(E_b | pi)`,  `E q_b <= epsilon`,

with connected-boundary set `S`, `C={S != empty}`, and

`m = min_{b in S} q_b` on `C`,

the source failure ratio as

`R_G(q) = E[m] / P(C)`.

Let

`R_*(epsilon) = sup R_G(q)`

over **all finite graphs of arbitrary size** and all source-admissible boundary/kernel data. Then the source is equivalent to

`R_*(epsilon) -> 0` as `epsilon -> 0`.

For a finite size cutoff `N`, define the genuinely finite restricted supremum

`R_{*,<=N}(epsilon) = sup{R_G(q): |V(G)|<=N}`.

Necessarily

`R_{*,<=N}(epsilon) <= R_*(epsilon)`

and

`R_*(epsilon) = sup_N R_{*,<=N}(epsilon)`.

But no source theorem or inherited handoff supplies a uniform finite cutoff `N_0` with `R_*=R_{*,<=N_0}`, nor a quantitative tail comparison controlling graphs larger than `N`. Consequently, exact enumeration of every graph through any fixed `N` cannot prove the source statement. Conversely, because the source asks for a limiting universal modulus `phi(epsilon)->1`, a refutation needs a sequence `epsilon_k -> 0` with source-admissible finite instances whose failure ratios stay bounded away from zero; a single fixed finite graph at one fixed epsilon is not by itself a source-level refutation.

This is the decisive classification point: the source is expressed on finite graphs, but its full quantifier structure is an **unbounded asymptotic theorem**, not a bounded finite certificate.

## Why the obvious “finite gadget + amplifier” route is already blocked

The R17 C069--C079 lifecycle did more than fail to enumerate small graphs. It derived the exact kernel formulation above, proved several full-quantifier special classes, and in its final handoff analyzed a natural recursive finite-module counterexample compiler. For a fixed finite rooted module with local decreasing gates recursively iterated to depth `h`, R17 proved the corresponding conditional failure ratio `R_h -> 0`, including explicit subcritical/critical bounds and an exponential bound in the supercritical case. Thus the natural idea “find one bad finite gadget and amplify it self-similarly to epsilon -> 0” is not an available finite-certificate shortcut in that broad multiplicative-gate architecture.

The handoff identifies the remaining source-level obstruction as adaptive boundary-label switching through shared connectivity together with genuinely global decreasing failure kernels. It also records that all thirty Section-B methods were used at least once during R17's HARD lifecycle. A future reassignment therefore requires a genuinely fresh theorem-scale architecture, not a short finite search.

## G0004 verdict

`G0004` passes the shard and ownership-release gates but **fails the R7-02 CLOSABLE source-class gate**.

Disposition:

`RESIDUE_1 / UNASSIGNED / SOURCE_OPEN-PARTIAL / HARD_OUTSIDE / NOT_ADMITTED_BY_R7-02`.

Its R17 metric `U_F=1` is predecessor mathematics and is **not inherited** by R7-02 because R7-02 does not admit this target.

# H0021 collision gate

Canonical source: Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1, Conjecture 1.4. For every fixed `epsilon>0` and integer `Delta>=2`, it asks whether, with high probability,

`G(n,(1+epsilon) log n/n)`

contains every `n`-vertex tree with maximum degree at most `Delta`.

`H0021` has checksum residue 1, but the current canonical claim is `CLAIMED / ACTIVE / HARD OUTSIDE` under R17. Its inherited metric is `Delta_near=2`; the first unresolved source-matching milestone is `Delta_near>=3`.

Disposition:

`RESIDUE_1 / HARD_OUTSIDE / ACTIVE_OTHER_OWNER / NOT_SELECTABLE`.

# Admission result

No material post-report candidate satisfies all three decisive gates simultaneously:

1. exact shard residue 1;
2. currently free/unclaimed ownership;
3. genuinely `CLOSABLE OUTSIDE` source shape.

Therefore R7-02 remains `PENDING_ADMISSION`. No `operations/claims/<ID>.md` is created in this screen, no predecessor metric is inherited, and no easier surrogate is substituted for a hard source.

## Metric and method accounting

Successor metric before: `UNKNOWN/UNMEASURED`.

Successor metric after: `UNKNOWN/UNMEASURED`.

Target-specific stagnation count: `NOT_STARTED`.

Section-B methods: **not charged** because no target is admitted. Charging B2/B16/B19 against an ownership/source-class screen would falsify the mathematical method history. Initial preference **B2 / B16 / B19** remains reserved for the next admitted successor, subject to recovered source-specific history.

## Next lawful attack

Continue strict-delta admission screening only. Prioritize any genuinely new canonical source row or explicit release whose exact ID has residue 1 and whose literal outside source is a finite certificate, explicit construction/counterexample, sharp exact constant, or short source-level theorem. Do not re-screen `G0004` unless there is a material source-status/class change, an explicit source-valid finite reduction, or a new parametric counterexample architecture that changes the CLOSABLE classification. Do not treat `H0021` as free while the R17 claim remains active.
