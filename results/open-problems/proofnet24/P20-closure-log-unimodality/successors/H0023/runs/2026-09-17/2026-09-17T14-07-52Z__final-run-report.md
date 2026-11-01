Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated model-family selector or reasoning-effort receipt, so this report does not claim otherwise. **NO SOURCE MOVEMENT: `C_link = 0 -> 0`; substantive unchanged H0023 streak `5 -> 6`. The mandatory CLOSABLE six-run rotation triggers in this run. Fresh Section-B moves: #11 DUALIZE, #19 MAKE IT AN ALGORITHM, #24 FIND THE EXTREMAL OBJECT.**

# P20 CLOSABLE OUTSIDE — H0023 final substantive run and rotation

Date: 2026-09-17.
Track: P20.
Source: Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (2026), Section 1.6, Conjecture 1.6.
Canonical historical claim: `operations/claims/H0023.md`.
Frozen metric: `C_link`, the number of exact truth values of source Conjecture 1.6 certified by P20. Before: `0`. After: `0`. Target: `1`.
Source status after this run: **OPEN / PARTIAL METHOD PROGRESS / NO SOURCE TRUTH VALUE CERTIFIED**.
Research status after this run: **RETIRED FROM ACTIVE P20 RESEARCH BY THE SIX-UNCHANGED-RUN CLOSABLE RULE**.

## 1. Required continuity and current-state refresh

I continued from

`proofnet24/P20-closure-log-unimodality/successors/H0023/runs/2026-09-17/2026-09-17T13-16-25Z__run-report.md`

rather than restarting H0023 or reopening retired D0010/I0081.

Before mathematics I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FLEET_2026-09-16.md`, canonical `operations/claims/H0023.md`, the newest own report, the newest complete P21 state, the newest recovered P26 activity, and the freshest coordinator/task-health state available to this run.

The freshest coordinator state recovered is `operations/task_health/runs/2026-09-17T140300Z/status.md` with `queue_delta.md`. Its fresh admission pass found **zero new lawful READY + CLOSABLE + UNASSIGNED successors**. It specifically keeps G0007 and G0010 as sourced but `HOLD_HARD`, not CLOSABLE, and records several stale/occupied queue rows that must not be treated as unassigned. This matters below when the six-run rotation fires.

The newest complete P21 mathematical state recovered remains the I0004 six-run handoff and contains no genuinely newer theorem claim. I therefore do not manufacture a directed P20->P21 audit receipt.

The operational classification mismatch remains preserved rather than silently rewritten: `operations/claims/H0023.md` says `CLAIMED / READY / CLOSABLE OUTSIDE`, whereas an older queue-allocation screen labeled H0021-H0023 `HARD/PENDING_OWNERSHIP`. No newer release or competing canonical owner was recovered. The explicit P20 assignment governed this final run; after the six-run trigger I request ledger reconciliation rather than editing shared ledgers or overwriting the historical claim.

## 2. Fresh source and literature check — 2026-09-17

Queries included the exact arXiv id `2608.06358`, exact title/authors, exact phrase `Conjecture 1.6 optimal linking system depth`, and combinations of `path hypergraph`, `prescribed endpoints`, `perfect matching`, `growing uniformity`, `Rödl nibble`, `Pippenger`, `Kostochka Rödl`, `Grable`, and `Vu`.

The primary source remains arXiv:2608.06358v1, dated 6 August 2026. The source text still states Conjecture 1.6 exactly as assigned: for each fixed `eps>0`, admissible integer `k >= (1+eps) log n/loglog n`, `m=n/(k+1)`, and fixed disjoint ordered endpoint tuples `a,b`, whp `G(n,(1+eps)log n/n)` contains an `(a,b;k)`-linking system, meaning every endpoint permutation is realized by a spanning collection of vertex-disjoint length-`k` paths. The same source says its proved linking-depth bounds are only optimal up to a constant factor and presents Conjecture 1.6 as the sharp intermediate problem.

No later source-matching resolution was located in this bounded search. That is bounded negative evidence only, not proof of openness and not a novelty certificate.

The nearest matching literature recovered still consists of fixed-uniformity or uniformity-dependent nibble results. Kostochka-Rödl (1998), summarizing Grable, gives quantitative nearly-perfect matching bounds for regular `k`-uniform hypergraphs under codegree hypotheses; Vu (2000) refines such bounds using higher codegrees. The available statements are not a certified growing-`k` perfect-matching theorem at `k ~ log n/loglog n`, and even their formal leftover scales do not supply the perfect completion H0023 needs.

## 3. Final research attack — idea before calculation

The preceding run gave the exact fixed-permutation reduction to the `k`-uniform path-certificate multihypergraph `H_pi(G)`. Its first moments look extraordinarily regular, but that calculation averaged over the underlying random graph edges. The final attack asks three sharper questions:

1. **#11 DUALIZE:** what does the fractional/perfect-matching obstruction look like after quotienting out the one deterministic balance relation?
2. **#19 MAKE IT AN ALGORITHM:** if one nevertheless runs a nibble on path certificates, what quantitative leftover is compatible with growing `k` and the *quenched* codegree scale?
3. **#24 FIND THE EXTREMAL OBJECT:** what is the smallest internal augmenting move that could remove the leftover without an external reservoir?

The conclusion is diagnostic rather than source-closing: the path-hypergraph route remains the cleanest surviving fixed-permutation formulation, but its real obstacle is now sharply localized to quenched local clustering plus a perfect-completion problem at growing uniformity.

## 4. #11 DUALIZE — the mean incidence operator has only the forced balance kernel

Fix one endpoint permutation `pi`. Let `W` be the `N=m(k-1)` internal vertices, and let `A` be the vertex-by-certificate incidence matrix of the path-certificate multihypergraph `H_pi(G)`. Every column contains exactly one label vertex and exactly `k-1` internal vertices.

There is a deterministic left-kernel vector

`z = -(k-1) * 1_[m]  +  1_W`,

because every path certificate has dot product `-(k-1)+(k-1)=0` with `z`. The source balance `N=m(k-1)` also gives `z^T 1=0`, so this relation is compatible with a fractional perfect matching and is not itself an obstruction.

Let

`mu=(N)_{k-1} p^k`,  `c=(k-2)/(N-1)`.

Using the exact first-moment degree/codegree identities from the preceding run, the normalized mean Gram matrix is

`B := (1/mu) E[A A^T]`

with block form

`B = [[ I_m, (1/m) J_{m,N} ], [ (1/m) J_{N,m}, (1-c) I_N + c J_N ]]`.

This matrix can be diagonalized exactly:

- on label differences (sum zero within `[m]`) the eigenvalue is `1`;
- on internal differences (sum zero within `W`) the eigenvalue is `1-c = 1-o(1)`;
- on vectors constant on each class, `(a,b)`, the induced map is `(a,b) -> (a+(k-1)b, a+(k-1)b)`, with eigenvalues `k` and `0`;
- the zero direction is exactly the deterministic balance vector `z` above.

Thus **at the level of the mean incidence operator there is no second linear obstruction**: modulo the forced class-balance relation, the expected Gram matrix is uniformly well conditioned from below (smallest positive eigenvalue `1-o(1)`).

Equivalently, the Farkas dual for a fractional perfect matching, `A x = 1`, `x>=0`, would have to exploit *quenched* path-certificate irregularity rather than an additional mean linear dependence. This identifies the concentration statement a successful route would need, but does not prove a nonnegative fractional solution for the actual random hypergraph.

### The hidden problem: unconditional codegrees understate quenched local clustering

The preceding report recorded

`E codeg(i,x) = mu/m = n^{-1+o(1)} mu`

for a label `i` and internal vertex `x`. That average is misleading for maximum-codegree purposes because it mixes the event that `x` is adjacent to an endpoint with the much more numerous non-neighbours.

Condition on the graph edge `a_i x` being present. Certificates in which `x` is the first internal vertex already contribute conditional mean

`(N-1)_{k-2} p^{k-1} = mu/(N p)`.

At the source boundary `Np=(1+eps+o(1)) log n`, this is

`mu / ((1+eps+o(1)) log n)`,

which is larger than the unconditional `mu/m` scale by a factor `m/(Np)=n^{1-o(1)}`. The same phenomenon occurs for internal pairs conditioned on their graph edge being present: consecutive appearances create a conditional certificate scale of order `mu/(np)`.

This is an exact conditional first-moment diagnosis, not a uniform high-probability max-codegree theorem. It nevertheless shows why the naive slogan "expected pair codegrees are n^{-1+o(1)} times the degree" is insufficient for a nibble: the actual path hypergraph is naturally clustered around the sparse graph edges that generate its certificates.

## 5. #19 MAKE IT AN ALGORITHM — known nibble scales do not reach perfectness here

Suppose optimistically that one could regularize the path hypergraph at degree scale

`D = mu = n^{eps+o(1)}`

and control the relevant codegrees strongly enough to invoke a classical nearly-perfect matching estimate. Two independent difficulties remain.

First, the available Pippenger/Grable/Kostochka-Rödl/Vu statements are formulated for fixed `k` or with constants depending on `k`; P20 has not certified a theorem uniform for

`k=(1+eps+o(1)) log n/loglog n`.

Second, even a formal favorable extrapolation gives only a near-perfect matching. For example, inserting the unrealistically favorable scale `C=n^{o(1)}` into the Grable-type leftover expression

`N_hyp * ((k C log N_hyp)/D)^{1/(2k-1+o(1))}`

with `D=n^{eps+o(1)}` and `k=(1+eps+o(1))log n/loglog n` yields a leftover of order

`n / (log n)^{eps/(2(1+eps))+o(1)}`,

not zero. If instead one respects the endpoint-adjacency clustering scale `C ~ D/log n` suggested by the exact conditional calculation above, the usual fixed-`k` improvement factors become still weaker when formally evaluated at growing `k`.

Therefore the final attack does **not** certify an actual growing-uniformity nibble theorem, and it certainly does not certify a perfect matching. What it does certify as a route diagnosis is that even an ideal near-perfect nibble is only the first half of the missing argument; a no-reservoir perfect-completion mechanism is essential.

## 6. #24 FIND THE EXTREMAL OBJECT — the residual is forced to come in balanced packets

There is one exact accounting fact that sharply specifies what an internal absorber would have to do.

If a matching in `H_pi(G)` contains `t` path certificates, then it leaves

- `m-t` unmatched label vertices, and
- `N-(k-1)t = (k-1)(m-t)` unmatched internal vertices.

So every leftover automatically has the same `1 : (k-1)` class ratio as a path certificate. An absorber should not be designed to "absorb one internal vertex" in isolation. Its atomic deficit is a **balanced packet consisting of one unmatched label and `k-1` unmatched internal vertices**.

A same-cardinality switch cannot reduce the unmatched count. The smallest cardinality-increasing internal augmentation is therefore a `1 -> 2` switch: replace one currently selected certified path by two disjoint certified paths, thereby consuming one previously unmatched label and exactly `k-1` previously unmatched internal vertices while repartitioning the old path's internal vertices. More generally, an `r -> r+1` alternating path-certificate switch consumes one balanced packet.

This gives a concrete post-handoff target: prove that after a quantitative nibble the random path-certificate hypergraph contains enough such balanced augmenting structures to eliminate every residual packet. P20 did not prove that existence statement in this run. In particular, the graph-edge dependencies that inflate local codegrees also create dependencies among these candidate augmenting switches.

## 7. Why this does not move `C_link`

Even if the fixed-permutation path hypergraph were shown to have a perfect matching whp, the source requires **every** permutation on the same graph. Earlier symmetry shows that a fixed-permutation whp theorem would imply that a typical graph realizes `1-o(1)` of all permutations, but not all `m!`. The sharp all-permutation uniformization problem therefore remains after the fixed-permutation matching problem.

No theorem in this run proves or refutes the full source Conjecture 1.6. The frozen metric remains

`C_link: 0 -> 0`.

Because the preceding substantive unchanged count was `5`, this is the sixth unchanged substantive H0023 run:

`unchanged substantive streak: 5 -> 6`.

Per the CLOSABLE rule, H0023 research is retired in this run. I do not manufacture a seventh H0023 lemma or checker.

## 8. Mandatory six-run handoff and rotation

A complete immutable H0023 handoff is being written alongside this report. It preserves:

- exact source statement and status;
- current-status search and limitations;
- every prior P20 method barrier and the fixed-permutation path-hypergraph reduction;
- the final dual/nibble/augmenting-packet diagnosis above;
- report/commit history;
- the unresolved all-permutation gap;
- the operational H0023 classification mismatch.

The source remains **OPEN / PARTIAL**, not PROVED or REFUTED. H0023 is retired only as an active P20 CLOSABLE assignment under the six-run rotation rule.

## 9. Successor-admission outcome in the same run

I executed the CLOSABLE rotation rule rather than continuing H0023.

The freshest coordinator admission screen available here, `operations/task_health/runs/2026-09-17T140300Z/status.md` plus `queue_delta.md`, found **zero lawful READY + CLOSABLE + UNASSIGNED successors** after fresh source/current-status/ownership/route screening. In particular it classifies G0007 and G0010 as `HOLD_HARD`, and it records existing attempt/claim exclusions for stale reserve rows such as I0004, I0075 and G0002. Root `QUEUE.md` itself says newly certified READY entries are zero and warns that listed PENDING candidates are not dispatchable.

Therefore I create **no replacement canonical claim** in this run. P20 enters

`SUCCESSOR_ADMISSION_REQUIRED / ROTATION HOLD`.

This is the lawful outcome; taking a HARD, occupied, or incompletely screened item merely to keep a source attached would violate the admission rule.

## 10. Ledger delta requested from P26/coordinator

P20 does not edit shared `RESULTS.md`, `QUEUE.md` or `POSTED.md`.

Requested reconciliation:

- H0023: source status `OPEN / PARTIAL`, `C_link=0`, substantive unchanged streak reached `6`, P20 research activity `RETIRED_BY_CLOSABLE_SIX_RUN_RULE`; do **not** mark the source solved/refuted.
- Preserve historical canonical claim ownership as evidence; reconcile the old `CLAIMED/READY/CLOSABLE` claim text with the later queue-allocation `HARD/PENDING_OWNERSHIP` label without rewriting immutable history.
- P20 current state after this run: `SUCCESSOR_ADMISSION_REQUIRED / ROTATION HOLD`; no successor claim created because the fresh 14:03Z screen found zero lawful READY+CLOSABLE+UNASSIGNED targets.
- Preserve D0010 and I0081 as retired exclusions exactly as already recorded.

## 11. Directed audit duty

The newest complete P21 state recovered still ends at the I0004 six-run retirement/handoff and contains no concrete new theorem claim. No P20->P21 audit receipt is created.

## 12. Verification / artifacts

No checker was appropriate: the final attack is analytic and produces no finite source-level certificate. The theorem-sized calculations used here are written explicitly above; no black-box growing-uniformity matching theorem is claimed.

A separate immutable six-run handoff records the durable state for any future authorized reassignment.

**END OF CANONICAL H0023 FINAL RUN REPORT**
