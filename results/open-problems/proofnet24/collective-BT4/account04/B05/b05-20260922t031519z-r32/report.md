# BT4 account04/B05 — five-remainder exclusion and the exact six-remainder collar core

Run: `b05-20260922t031519z-r32`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-COUNT-v4-FIVE-R-EXCLUSION`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the target, so directed digons count.

The current exact-status source is Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract states that the genuine conjecture remains unresolved for every `k>=4`; its theorem at the same threshold `2k-1` allows each cycle either to be directed or to become directed after reversing one arc. No such relaxed cycle is promoted here.

The lower-`k` input remains Lichiardopol--Pór--Sereni, SIAM J. Discrete Math. 23 (2009), 979--992, DOI `10.1137/080715792`: minimum outdegree five gives three disjoint directed cycles, and the paper's strengthened `k=2` theorem says that outdegree at least three except for at most two vertices of outdegree two forces two disjoint directed cycles.

## Exact inherited state consumed

Newest complete campaign-lead package actually read:

- account02/B04, `proofnet24/collective-BT4/account02/B04/20260922T022208Z-b04-bt4-r11/report.md`, blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`;
- its controlling correction, blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`.

The correction is controlling. It closes the invalid `A not->z` branch for a cycle-supported heavy witness by a heavy-fan domination escape: in a no-cross state every cycle-supported witness heavy on `A` has a genuine inport `b->z` with `b in A`.

Named OTHER-account partner result actually consumed and applied:

- account01/B06, `BT4-GATE-ESCAPE-v1`, `proofnet24/collective-BT4/account01/B06/20260922T023613Z-b06-bt4-r11/report.md`, blob `adb2dcf7289ec7290cfc75ad760355ff540dff3d`.

That result strengthens the same-heavy support saturation state: two same-heavy witnesses have a common gate on their heavy-cycle return intervals, and 3-vertex-strongness forces either a cross-packed transition, a neutral heavy-cycle exchange, or a strict transverse `R`-bypass across that gate. I use this below to identify the extra structure of the first surviving six-remainder state.

I also use the partner's preceding fixed-pair/collar theorem, account01/B06 run `20260922T013522Z-b06-bt4-r11`: an `R`-supported five-witness heavy with fan `m>=3` gives either a cross-packed transition, a neutral equality exchange, or three strict pure-`R` collars and `|R|>=3m-2>=7`.

The support-correct segment tax used below is account03/B05 `BT4-TCEX-v2.1-linkage`, linkage blob `f1545c2e4a546d17150bb20bbc59650a29eb2672`.

## Normal form

Assume BT4 false and work in the inherited minimum-counterexample normal form:

1. `D` is oriented and every vertex has outdegree exactly seven;
2. `(A,B,C)` is a globally minimum-total packing of three directed cycles;
3. `R=V(D)\(A union B union C)` is nonempty and acyclic;
4. `A,B,C` are chordless;
5. every arc is dominated;
6. `D` is 3-vertex-strong.

For every deleted packed pair, the strengthened `k=2` theorem gives either a residual vertex of outdegree at most one (the `SIX` branch) or at least three residual vertices of outdegree exactly two (five-cross witnesses). `NO-SIX` means the latter alternative holds for all three packed pairs.

## Lemma 1 — equality-free cycle-supported witnesses consume at least six remainder vertices

Assume `NO-SIX`, no genuine cross-packed transition, and no size-neutral globally minimum packing exchange.

Fix one packed pair, say `{A,C}`, and let `z in B` be a cycle-supported five-witness for that pair. Let `A` be a heavy target of `z` and put

`m=|N+(z) intersect A|>=3`.

Because cross-packed transitions are excluded, the lead's corrected heavy-fan domination lemma forces a genuine inport

`b -> z`, with `b in A`.

By 3-vertex-strongness and directed Menger there are three internally vertex-disjoint directed paths from `z^-` to `z^+`. At most one can contain `z`, so choose two internally vertex-disjoint paths `P1,P2` avoiding `z`.

If either path internally meets `A union C`, take the first such hit after the last preceding visit to `B`. The intervening subpath has all internal vertices in `R`, producing a genuine cross-packed transition. This is excluded. Hence both `P1,P2` avoid `A union C`.

Apply account03/B05 Lemma B to each `Pj`. It extracts an `R`-internal bypass

`Qj : pj -> ... -> qj`

of a nonempty proper forward segment `Sj=B[pj^+,qj^-]` containing `z`. Write

`sj=|Sj|`, `ell_j=|Qj|` in edges.

Because `P1,P2` are internally vertex-disjoint, the internal `R`-vertex sets of `Q1,Q2` are disjoint.

Account03/B05 Lemma A, using the inport `b->z` and the `m` heavy fan targets, gives

`ell_j >= m+sj-1`.                                                (1)

There is a useful strict improvement in the present no-neutral branch. If equality held in (1), then

`ell_j+1-sj=m`.

For every fan target `a in N+(z) intersect A`, the marked-segment exchange inequality gives

`d_A(b,a) <= ell_j+1-sj=m`.

These are `m` distinct positive integer distances, so they must be exactly `1,...,m`. Choosing the target at distance `m` makes the total covered-size change

`ell_j+1-sj-m=0`,

which is precisely a size-neutral three-cycle packing exchange. This is excluded. Therefore integrality strengthens (1) to

`ell_j >= m+sj`.                                                  (2)

Each `Qj` consequently has

`ell_j-1 >= m+sj-1 >= m >=3`

internal remainder vertices. The two internal sets are disjoint, so

`|R| >= (ell_1-1)+(ell_2-1) >= 2m >=6`.                          (3)

This proves the lemma. The two collars are simultaneous outputs of one Menger linkage; no independence assumption is made.

## Lemma 2 — five-remainder NO-SIX states cannot be featureless

Assume `NO-SIX` and `|R|<=5`.

Suppose, for contradiction, that there is neither a genuine cross-packed transition nor a size-neutral globally minimum packing exchange.

Choose any packed pair. It has at least three five-witnesses.

If one witness lies in `R`, choose a heavy target with fan `m>=3`. The account01/B06 fixed-pair/collar theorem gives cross, neutral equality, or

`|R|>=3m-2>=7`,

all impossible under the current assumptions.

Hence every five-witness for the chosen pair is cycle-supported on the complementary packed cycle. Pick one such witness. Lemma 1 then gives `|R|>=6`, contradicting `|R|<=5`.

Therefore:

> **BT4-COUNT-v4-FIVE-R-EXCLUSION.** In the inherited exact-seven, oriented, globally minimum three-cycle-packing normal form, every global `NO-SIX` state with `|R|<=5` has either a genuine cross-packed transition or a size-neutral globally minimum packing exchange.

This extends the previous B05 four-remainder escape by one full remainder size, and removes the former strict-bypass endpoint in sizes at most five.

## Lemma 3 — exact structure of the first surviving size, |R|=6

Continue in global `NO-SIX`, exclude cross transitions and neutral exchanges, and assume `|R|=6`.

First, no five-witness can lie in `R`, because the account01/B06 strict `R`-supported collar branch requires at least seven remainder vertices. Thus all five-witnesses for every packed pair are cycle-supported.

Take any such witness `z in B`, heavy on `A` with fan `m>=3`. Apply Lemma 1. Since `|R|=6`, every inequality used there is forced to equality at the strict lower bound:

- `m=3`;
- both extracted bypassed segments have size `s1=s2=1`;
- both bypass lengths are `ell_1=ell_2=4`;
- each bypass has exactly three internal remainder vertices;
- the two internal sets are disjoint and partition all six vertices of `R`.

Because `Sj={z}`, its bypass endpoints are exactly `z^-` and `z^+`. Hence the two Menger detours themselves are

`z^- -> r_{j,1} -> r_{j,2} -> r_{j,3} -> z^+`, `j=1,2`,

and their six internal vertices partition `R`.

The witness's five pair-fan arcs consequently split exactly `3+2` between the two deleted packed cycles. In particular, no `4+1` or `5+0` cycle-supported five-witness survives in this six-remainder no-cross/no-neutral core.

Since each fixed pair has at least three such witnesses on its complementary support cycle, two are heavy on the same target by pigeonhole. Apply the newest account01/B06 `BT4-GATE-ESCAPE-v1` to that same-heavy pair. In the present no-cross/no-neutral branch its first two outputs are excluded, so it supplies a **strict transverse `R`-bypass across a common gate on the heavy packed cycle**.

Thus the first possible finite hard state is not an amorphous six-vertex remainder. It simultaneously has:

1. for every cycle-supported five-witness, two length-four support bypasses whose three-vertex `R` interiors partition the remainder into two directed chains;
2. exact `3+2` pair-fan splitting;
3. for a same-heavy witness pair, a common heavy-cycle gate and a strict transverse `R`-bypass across that gate.

This is the exact six-remainder collar core.

## Compact conditional end-to-end route after this step

The lead's honest universal obligations remain `H6` (exact-six closure), `HX` (cross-linkage/two-cycle-splice closure), and `HS` (strict-collar/neutral-dynamics closure).

The present result pays a genuine finite part of `HS`:

- `NO-SIX` with `|R|<=5` cannot remain in the no-cross/no-neutral strict-collar branch at all;
- the first possible such state is `|R|=6`, where every cycle-supported witness forces an exact two-chain partition of `R`, and the newest partner theorem simultaneously forces a strict transverse heavy-cycle bypass through the same six vertices.

The first essential missing implication is now:

> **Six-remainder two-axis closure.** In the exact six-remainder collar core above, use the coexistence of the witness-specific two-chain partitions of `R` and the same-heavy transverse gate bypass to obtain a legal two-cycle reconstruction, a neutral exchange, a cross-packed transition, a directed cycle in an exchanged remainder, or a SIX configuration.

A mere count of partitions is not claimed to close this step. Different witness-specific partitions can reuse arcs of the same acyclic six-vertex remainder, so the next argument must exploit their directed endpoint attachments and the transverse gate, not pretend the collars are independent.

The separate `SIX` branch and all `|R|>=7` strict-collar states remain open.

## Failure checks and nonclaims

- The two support bypasses in Lemma 1 are not assumed independent; their disjointness comes from one directed-Menger family.
- Equality in the segment tax is converted to a neutral exchange by an explicit integer-distance argument, not by an unsupported equality slogan.
- The `R`-supported witness theorem is used only for genuine remainder vertices; cycle-supported witnesses are routed through the support-correct account03/B05 lemma.
- No claim is made that a strict bypass alone produces a fourth cycle.
- No claim is made that different witnesses induce distinct partitions of `R`.
- Digons are allowed in the original target; orientation is used only in the inherited counterexample reduction.
- No finite-order restriction, tournament assumption, edge-disjoint substitute, or one-reversed-arc cycle is used.
- No computation was used in this run.
- Full BT4 remains OPEN / NOT PROVED.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

New proved step: every global `NO-SIX` state with at most five remainder vertices exports cross geometry or a neutral minimum-packing exchange. The first equality-free/no-cross remainder size is six, and at that size every cycle-supported witness forces an exact pair of length-four, three-internal-vertex support bypasses partitioning `R`, while the newest account01/B06 common-gate theorem adds a transverse heavy-cycle bypass. This is the next source-valid finite core to attack.
