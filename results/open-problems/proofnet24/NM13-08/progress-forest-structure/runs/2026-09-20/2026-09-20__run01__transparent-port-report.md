Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — transparent two-terminal substitution and an infinite non-series-parallel uniform-forest class

Status: **PARTIAL / theorem candidate pending later independent review**. The arbitrary-finite-graph uniform-forest conjecture remains open.

## 0. Compact transition handoff

The immediately preceding NM13-08 state was the old residue-7 CLOSABLE admission loop, latest report `proofnet24/NM13-08/runs/2026-09-19/2026-09-19T22-40-30Z__admission-delta-screen-35-p0487-r7-hard-releases-hard-row109-no-ready.md` at commit `410cf6305b9e8cacdcb94fa27305923fbf5401f2`. It had **no admitted mathematical target, no claim, and no successor metric**; only the screening cursor `STRICT_DELTA_ONLY_RESIDUE_7` was live. The later owner policy `operations/PROGRESS20_2026-09-20.md` supersedes that intake-only loop and maps NM13-08 to T07 graph-decomposition/generating-polynomial theory under this report root. I preserve the old screening history and do not reinterpret it as T07 progress.

The current companion NM13-04 had not yet produced a T07 theorem when this run began: its newest durable commit was still the pre-transition admission report `442983c57062cb9641435ddbd715400003a8b532`. R13 had just written a transition handoff to PROB10-07 at `42606ada73eec3695907f19ccf80b3e1ad3de1ea`, with no new forest theorem in that handoff. Thus the route below is a complementary generating-polynomial substitution theorem, not a duplicate finite graph-order enumeration and not a takeover of another claim.

`POSTED.md` was checked. I found no posted T07 closure to reopen. The general uniform-forest conjecture is not treated as posted or settled.

## 1. Exact parent problem and recovered prior scope

For a finite simple graph `G=(V,E)`, let

`I_G(y) = sum_{F subset E, F acyclic} prod_{e in F} y_e`.

For distinct edges `e,f`, define the forest Rayleigh difference

`Delta_G(e,f) = I_e I_f - I I_ef`.

At all edge weights `1`, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for the **uniform measure on all acyclic spanning edge subsets** (isolated vertices are allowed). This is not the spanning-tree measure and not a measure with a fixed number of components.

Recovered source scope, rechecked against primary sources in this run:

* Grimmett--Winkler, arXiv `math/0302185`, Conjecture 1.1, asks for pairwise edge negative association for the uniform forest on every finite graph. Their Theorem 1.5 verifies it for every graph with at most 8 vertices and every 9-vertex graph with at most 18 edges. They explicitly distinguish this from the already-known uniform-spanning-tree theorem.
* Erickson, arXiv `1008.3660`, defines the stronger **I-Rayleigh** property: `Delta>=0` for every positive evaluation of all edge weights. Theorem 1.2 gives a sum-of-squares proof for series-parallel graphs. The same paper records that the SOS conjecture was known for `K_7`, the cube, and the 8-vertex Möbius ladder, and Lemma 2.3 gives deletion/contraction inheritance of the SOS identity. It also records that two-sums of I-Rayleigh graphs are I-Rayleigh. This weighted closure is stronger than the source's unit-weight assertion.
* Historical P14/HARD10 work in this repository completed the complementary dense 9-vertex sector: together with Grimmett--Winkler, every simple graph on 9 vertices is exactly certified at unit weights. P14's resulting finite source metric is `n=9`; a counterexample, if any, has at least 10 vertices. P14 also identified the key obstruction to a naive unweighted two-sum induction: collapsing a two-terminal side generally creates a **non-unit virtual edge weight**, so a unit-only core theorem cannot simply invoke weighted two-sum closure.
* Huang, arXiv `2311.00965`, states that negative correlation for arboreal gas remains open in general and proves results for specific graph/parameter regimes, including adjacent edges for sufficiently large beta and complete graphs in certain regimes.
* Tang--Zhang, arXiv `2603.10738`, treats uniform families on the complete graph, including forests with exactly `k` components for fixed `k` and sufficiently large `n`. That is not the measure here, which ranges over **all** forests of an arbitrary finite graph.

Bounded literature queries were run on 2026-09-20 for the exact source, Erickson's weighted closure, later arboreal-gas work, and the 2026 complete-graph paper. I do **not** claim the new lemma below is first in the worldwide literature; novelty/priority is **UNVERIFIED**. The claim made here is narrower: it is a new repository theorem and it yields a graph family not covered by the recovered named theorem scopes above.

## 2. New decomposition theorem: transparent two-terminal replacement

Let `H` be a graph with a distinguished edge `g=xy`; write `B=H-g`. Let `A` be a graph with terminals `x,y`, internally vertex-disjoint from `B`, and containing no edge `xy`. Let `G` be obtained from `H` by deleting `g` and inserting `A` between the same terminals.

For forests of a two-terminal graph `Q`, split its generating polynomial into

* `D_Q`: forests in which `x,y` are disconnected;
* `C_Q`: forests in which `x,y` are connected.

Thus `I_Q=D_Q+C_Q`. For an edge `p` of `Q`, write `D_{Q,p}, C_{Q,p}` for the corresponding derivatives. All quantities below may be evaluated at any fixed positive weights on the real edges; in the application every real edge has weight 1.

### Theorem T07-PORT-SUBSTITUTION-01

Define the terminal activity of `A` by `t_A=C_A/D_A` (`D_A>0` because the empty forest is counted). Then:

1. **Partition identity**

   `I_G = D_A(D_B+C_B) + C_A D_B = D_A * I_H |_{y_g=t_A}`.

2. **Core-core factorization.** For `e,f in E(B)`,

   `Delta_G(e,f) = D_A^2 * Delta_H(e,f)|_{y_g=t_A}`.

3. **Gadget-gadget factorization.** Let `K=A+g` and put `s_B=C_B/D_B`. For `p,q in E(A)`,

   `Delta_G(p,q) = D_B^2 * Delta_K(p,q)|_{y_g=s_B}`.

4. **Cross-edge sign factorization.** For `p in E(A)` and `e in E(B)`,

   `Delta_G(p,e) = J_A(p) J_B(e)`,

   where

   `J_A(p)=D_A C_{A,p}-C_A D_{A,p}`,

   `J_B(e)=D_B C_{B,e}-C_B D_{B,e}`.

   Moreover

   `J_A(p)=Delta_{A+g}(p,g)` and `J_B(e)=Delta_H(e,g)`,

   and each of these expressions is independent of the value assigned to `y_g`.

### Proof

A pair `(F_A,F_B)` of forests has acyclic union in `G` unless **both** `F_A` and `F_B` connect `x` to `y`: if both do, their two `x-y` paths form a cycle; if at least one does not, any cycle in the union would have to cross the two-terminal separator and would force an `x-y` path on each side. Therefore valid pairs have generating sum

`D_A D_B + D_A C_B + C_A D_B`,

which proves (1). Since `t_A` depends only on `A`, differentiation in two `B`-edges immediately gives (2).

Likewise

`I_G = D_B[(D_A+C_A) + (C_B/D_B)D_A] = D_B I_{A+g}|_{y_g=s_B}`,

because forests of `A+g` that use `g` are exactly `g` times forests of `A` disconnecting `x,y`. Differentiating twice in `A` gives (3). If `s_B=0`, the same identity follows by polynomial continuity; in the concrete family below `s_B>0` anyway.

For (4), abbreviate `a=D_A`, `c=C_A`, `b=D_B`, `d=C_B`. For derivatives in `p` and `e`, direct expansion of

`I=ab+ad+cb`

gives

`I_p I_e - I I_pe = (a c_p-c a_p)(b d_e-d b_e)`.

Finally, for `K=A+g`,

`I_K=D_A+C_A+y_g D_A`, `I_{K,g}=D_A`,

so

`Delta_K(p,g)=D_A C_{A,p}-C_A D_{A,p}=J_A(p)`;

the same calculation in `H=B+g` gives `Delta_H(e,g)=J_B(e)`. The `y_g` terms cancel, proving independence of the port weight. QED.

### Corollary T07-UNIT-TRANSPARENT-PORT-02

Call `A` **unit-transparent** when `C_A=D_A` at unit weights. If `K=A+g` is I-Rayleigh, then replacing any edge `g` of any graph `H` that satisfies the **unit-weight** pairwise forest inequality by a unit-weight copy of `A` preserves the unit-weight pairwise forest inequality for every edge pair of the new graph.

Proof: because `C_A=D_A`, the core-core factorization samples `H` at `y_g=1`, exactly the hypothesis available on `H`. For cross pairs, I-Rayleigh of `K` gives `J_A(p)>=0`, while unit p-NC of `H` applied to `(e,g)` gives `J_B(e)>=0`. For two gadget edges, (3) invokes the I-Rayleigh inequality of `K` at the positive port activity `s_B` (or its zero limit). These three cases exhaust the edge pairs. QED.

**This is the mechanism gain.** Generic two-sum closure requires a weighted I-Rayleigh hypothesis on the core. The transparent-port condition removes exactly that obstruction: the core is sampled only at unit port weight. Thus the lemma can transfer a merely unit-p-NC core into arbitrarily large graphs.

## 3. A concrete transparent gadget from the octahedron

Let `O_6` be the octahedral graph `K_6` minus the perfect matching `{05,14,23}` and choose port edge `g=01`. Let

`A = O_6 - g`, terminals `0,1`.

The executed exact checker enumerates every forest and obtains

`Z(O_6)=1083`, `# {forests containing g}=361`,

and, directly in `A`,

`D_A=361`, `C_A=361`.

Hence `A` is unit-transparent: `t_A=1` exactly.

The required weighted gadget hypothesis is not merely computational. Erickson records the SOS identity for `K_7`, and his deletion lemma preserves the identity under edge deletion. Delete all six edges incident to one vertex of `K_7` and delete the matching `{05,14,23}` among the remaining six vertices. The surviving non-isolated graph is exactly `O_6`; isolated vertices do not alter the forest polynomial. Therefore `O_6=A+g` is SOS and hence I-Rayleigh for all positive edge weights. The corollary applies.

The exact checker also finds that `A` has 11 edges, degree sequence `3,3,4,4,4,4`, no bridge, and nonnegative port-interface signs for all 11 real edges (minimum `J_A=3610`). The latter is a finite sanity check; the proof of all-positive port behavior is Erickson's inherited SOS theorem, not this finite sample.

## 4. All-parameter application: arbitrary iterated octahedral-port expansions

Let `C_9^O` be the following class.

Start from **any** simple graph `H_0` with at most 9 vertices. At each step choose an arbitrary current edge and replace it by a fresh copy of `A=O_6-01`, identifying the terminals with the old endpoints and keeping the four other gadget vertices new. Repeat any finite number `k` of times, with the choice of replaced edge allowed to depend arbitrarily on the preceding construction.

### Theorem T07-OCTAHEDRAL-EXPANSION-03

Every graph in `C_9^O` has pairwise negative edge correlation under the uniform measure on **all** forests.

### Proof

P14's recovered exact source-level result says every simple `H_0` on at most 9 vertices satisfies unit p-NC. The octahedral port gadget is unit-transparent and its completed port `O_6` is I-Rayleigh. Therefore Corollary T07-UNIT-TRANSPARENT-PORT-02 applies to the first replacement. The resulting graph again satisfies unit p-NC, so the same corollary applies inductively to every later replacement, regardless of which current edge is chosen. QED.

This is an **all-parameter** theorem: `k` is arbitrary and the replacement sequence is arbitrary. It is not finite enumeration of the expanded graphs.

### A genuinely uncovered explicit subfamily

To make sure the theorem is not merely rephrasing Erickson's series-parallel class, take the 9-vertex core

`H_* = R_{3,3} + {04}`,

where `R_{3,3}` is the 3-by-3 rook graph on vertices `(r,c)` (`0..8` in row-major order), and `04` is a non-rook edge. This simple graph has 19 edges and graph6 string `H{fQXgj`.

The exact checker independently verifies all 171 edge pairs:

`Z(H_*)=81112`, `negative pairs=0`, `min Delta=3607636`.

Thus it is a concrete unit-p-NC core. It also lies just outside Grimmett--Winkler's published 9-vertex/18-edge finite theorem (while being included in P14/HARD10's later repository completion).

After `k` octahedral-port substitutions,

`|V| = 9+4k`, `|E| = 19+10k`.

These graphs are not series-parallel: already `H_*` has `19 > 2*9-3=15` edges, impossible for a simple series-parallel graph, and every expanded graph has `H_*` as a minor by collapsing each inserted two-terminal gadget back to its replaced edge. Series-parallel graphs are minor-closed. The checker also records that `H_*` and the gadget are bridgeless and have minimum degree at least 3/4 as appropriate; in the expanded family the minimum degree stays at least 4. Thus the family is not generated by a trivial bridge/degree-2/parallel-edge simplification.

Nor is this a Tang--Zhang complete-graph/fixed-component theorem: the graphs are non-complete and the probability space is the union of forests of **all** component counts.

Finally, the proof does not secretly invoke weighted I-Rayleigh for `H_*`. That stronger property is **not claimed** here. Only unit p-NC of the core is used; the weighted theorem is confined to the fixed six-vertex port gadget. This is precisely why the result goes beyond what the recovered generic weighted two-sum theorem can certify from the available hypotheses.

## 5. Exact executed certificate

Artifact: `2026-09-20__run01__exact_check.cpp` with executed output `2026-09-20__run01__exact_check.out` in this run directory.

The checker uses integer enumeration of every edge subset for `H_*` (19 edges) and for the octahedral gadget, rejecting cyclic subsets by disjoint-set union. It certifies exact forest counts, every unit Rayleigh numerator on `H_*`, the exact `D_A=C_A=361` activity identity, bridge counts, and the port-interface signs. Terminal line: `ALL_EXACT_CHECKS_PASS`.

Key output:

* `CORE_H0 ... n=9 m=19 Z=81112 pair_count=171 negative=0 min_delta=3607636`
* `O6 ... Z=1083 port_edge_count=361`
* `GADGET_A=O6-g ... D=361 C=361 activity=361/361`
* `GADGET_INTERFACE ... negative_J=0 min_J=3610`
* `ALL_EXACT_CHECKS_PASS`

The finite checker is **not** the proof for arbitrary `k`; the transfer theorem above is.

## 6. Parent theorem vs mechanism progress

**Parent source theorem (arbitrary finite graph, all forests):** `OPEN -> OPEN`. No claim of a general solution or counterexample. The universal graph-order lower bound from P14 stays `counterexample order >=10`; this run does not change it.

**Demonstrated source-scope gain:** before this run the explicit dense core `H_*` was certified only as one finite 9-vertex instance (substitution depth `k=0`). After the theorem, **every** arbitrary substitution depth `k>=0` and every replacement sequence is certified. Thus the demonstrated structural parameter moves

`k_max: 0 -> unbounded`.

More generally, the finite P14 class of all simple graphs on at most 9 vertices gains the infinite closure `C_9^O` under arbitrary repeated octahedral-port replacement.

**Mechanism gain:** a new exact cross-edge factorization plus the unit-transparent port criterion converts a weighted two-sum obstruction into a unit-only core closure rule. This is a proof mechanism with a concrete infinite application, not merely a framework.

## 7. Failed / rejected routes preserved

1. **Generic two-sum induction** was rejected: P14 already isolated the non-unit virtual-weight obstruction, and Erickson/Cocks weighted closure needs the stronger I-Rayleigh hypothesis on the core.
2. **Tiny activity-one gadgets built from series/parallel reductions** were rejected as a target application because they would collapse back into already-covered series-parallel or elementary simplification regimes.
3. **Complete-graph/fixed-component transfer** was rejected because it changes the probability space and would not address the uniform measure over all forests of arbitrary graphs.

The octahedral transparent gadget survives all three filters.

## 8. Residual obstruction and next attack

The exact source remains wide open because most 2-terminal replacements have `t_A != 1`; then core-core pairs demand knowledge of `Delta_H` at a non-unit virtual edge weight. The next nonduplicating attack is to characterize a broader family of **unit-transparent ports** by a local involution or deletion-contraction identity, or to prove an interval version `t_A in J` together with a one-edge Rayleigh interval theorem for a source-level unit core class. A second promising direction is a multi-port version whose Schur-type interface matrix is sign-controlled; that could move from edge substitution to genuine 2-separator decomposition.

No peer file, shared root ledger, schedule, workflow, email/Drive resource, permission, public posting, or paid compute was changed in this run.