# BT4 fleet04/B05 — direct three-linkage collapse and 3x3 cycle-factor criterion

Run: `b05-20260922t074314z-r35`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Role: fleet04/B05 counting / probabilistic-choice / reconstruction  
Candidate: `BT4-R4-DIRECT-3X3-CYCLE-FACTOR-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and literature boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs and hence digons are allowed in the target statement.

The external status was refreshed during this run. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (submitted 13 August 2026), explicitly states that the genuine conjecture remains unresolved for every `k>=4`; its theorem at the same `2k-1` threshold permits one arc reversal per packed cycle and therefore does not settle BT4. The genuine lower-parameter input retained by the campaign is Lichiardopol--Pór--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992: minimum outdegree five gives three vertex-disjoint directed cycles.

No novelty claim is inferred from a search miss.

## 2. Exact mathematical state consumed

### Team lead fleet02/B04

I read the latest complete lead report

`proofnet24/collective-BT4/fleet02/B04/20260922T0619Z-b04-bt4-r11/report.md`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

The inherited normal form is a hypothetical BT4 counterexample `D` that is oriented, exactly 7-outregular, arc-dominated and 3-vertex-strong. A packing of three pairwise disjoint directed cycles is chosen first to minimize total packed order and then to maximize the number of arcs induced by the acyclic remainder. Packed cycles are chordless.

The live aligned four-remainder heavy-triangle cage has

`H = h0 -> h1 -> h2 -> h0`, `R={x,r0,r1,r2}`,

with

`h0->r0`, `h1->r1`, `h2->r2`,
`r0->r1`, `r1->r2`, `r0->x`, `r1->x`, `r2->x`,

and the lead's light-support data

`p in A`, `p->h0,r0,x`,
`q in B`, `q->h1`,
`P : p->x->b` with `b in B`,
`Q : q->a3` with `a3 in A`.

The lead's `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` correctly reduces the long aligned branch to genuine CROSS/BYPASS geometry rather than the earlier invalid direct SC2 invocation.

### Assigned OTHER-account partner fleet01/B06

I read and apply fleet01/B06

`proofnet24/collective-BT4/fleet01/B06/20260922T070201Z-b06-bt4-r12/report.md`, Git blob `fdd394bc4a6b8f3ca851978c06219c5fe7563881`, candidate `BT4-X-DELETED-2X2-RANK-COLLAPSE-v1`.

Its proved content used here is that after deleting the distinguished sink `x`, either one obtains third-support mediation, a same-support bypass, a light support of order at most four, or two vertex-disjoint `A->B` connectors and two vertex-disjoint `B->A` connectors whose interiors are mutually disjoint subsets of `{r0,r1,r2}` and whose total edge length is at most seven. It also gives the exact cyclic-order criterion for a two-cycle splice and the tax `G_A+G_B<=L_X<=7`.

### Current same-campaign linkage input

I also use the source-exact proof in fleet04/B06

`proofnet24/collective-BT4/fleet04/B06/20260922T070806Z-b06-bt4-coll11/report.md`, Git blob `ff7bbac3a8211262bc273f6fa02b102d3ace16dd`, candidate `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`.

Its directed-Menger proof gives **three** pairwise vertex-disjoint `A->B` paths and three pairwise vertex-disjoint `B->A` paths in the 3-vertex-strong normal form; after trimming, their interiors avoid the two endpoint supports. If no trimmed path meets `H`, all of their internal vertices lie in `R`.

### Newest compatible cross-team correction

During this run fleet03/B05 published `BT4-SHORTEST-CROSS-PARITY-TRAP-v1`, canonical report

`proofnet24/collective-BT4/fleet03/B05/20260922T074352Z-fleet03-B05-bt4-r11/report.md`, Git blob `89f2749e556f8e97966eefbc1418adea4cbd4172`.

It proves that in the shortest-mixed-cycle geometry, merely adding one fresh reverse connector to a fresh forward cross can force opposite pairing parity rather than a legal two-cycle splice. I preserve that correction: rank growth by itself is not closure.

## 3. Compact conditional end-to-end route

The inherited campaign route is: reduce to the exact-seven / globally minimum three-packing normal form; split into SIX and global NO-SIX; reduce the four-remainder heavy-triangle NO-SIX branch to cross/bypass/linkage interfaces; then reconstruct enough disjoint genuine cycles or obtain a strict packing improvement / cyclic exchanged remainder / previously paid exit.

This report pays a sharper part of the reconstruction debt. In the exact R4 cage, **if third-support mediation is absent, every remainder-internal light-to-light connector is forced to be direct**. Combining this with the three-linkage Menger theorem produces three pairwise vertex-disjoint direct crosses in *each* light-support direction. Thus the surviving linkage wall is not an arbitrary path-dependence problem at all: it is a finite `3 x 3` direct packed-port order problem.

Moreover, if the six ports alternate on both light supports and the two induced three-way pairings agree, the six direct cross arcs reconstruct **three** pairwise vertex-disjoint mixed directed cycles. Together with `H`, this is already the desired four-cycle packing. The remaining obstruction is therefore an explicit nonalternating / endpoint-collision / nonidentity-permutation port signature. A finite exact check shows that raw rank three alone does not eliminate this signature, so the next proof must use the exact-seven / NO-SIX / shortest-cycle geometry rather than an unjustified Hall-independence step.

## 4. New lemma — every non-direct R-connector is H-mediated

Call an `A->B` or `B->A` connector **H-mediated** if its internal vertices meet the third packed cycle `H`.

### Lemma 4.1

In the exact cage above, let `J` be a trimmed `A->B` connector whose internal vertices lie in `R`. If `J` has a nonempty interior, then there exists an `A->B` connector whose interior meets `H`. Symmetrically, every non-direct remainder-internal `B->A` connector forces a `B->A` connector whose interior meets `H`.

### Proof

Take an `A->B` connector and let `y` be its last internal vertex before its endpoint `w in B`.

If `y=r_j`, then `r_j->w`. The exact cage gives `p->h0`; follow the directed triangle `H` from `h0` to `h_j`, then use `h_j->r_j->w`. Thus

`p -> h0 -> H[h0,h_j] -> r_j -> w`

is a simple directed `A->B` connector meeting `H` internally.

If `y=x`, then `x->w`. Using `p->h0`, `h0->r0` and `r0->x` gives

`p -> h0 -> r0 -> x -> w`,

again an `H`-mediated `A->B` connector.

These are the only possibilities because `R={x,r0,r1,r2}`.

For a `B->A` connector with last internal vertex `y` and endpoint `w in A`, use `q->h1`. If `y=r_j`, follow the directed triangle from `h1` to `h_j` and then `h_j->r_j->w`. If `y=x`, use

`q -> h1 -> r1 -> x -> w`.

All vertices are distinct because `A,B,H,R` are pairwise disjoint and the displayed `H` segment is simple. QED.

### Immediate consequence

In the branch in which **no H-mediated light-to-light connector exists**, every trimmed connector between `A` and `B` whose interior lies in `R` is a direct cross arc.

This strengthens the assigned partner's x-deleted conclusion: its residual `L_X<=7` case actually has `L_X=4` for any selected `2 x 2` sublinkage in this exact cage. In the four-distinct-port compatible case the partner tax then becomes

`4 <= G_A+G_B <= L_X = 4`,

so every legal two-cycle splice is forced to the exact neutral boundary `G_A+G_B=4`; the previous collar values 5,6,7 disappear in this branch.

## 5. New theorem — no H mediation gives a direct 3 x 3 cross system

### Theorem 5.1 (`BT4-R4-DIRECT-3X3`)

In the exact R4 heavy-triangle cage, assume neither light-support direction admits an H-mediated connector. Then there exist

`F_i : alpha_i -> beta_i` (`A->B`, `i=1,2,3`)

and

`G_j : gamma_j -> delta_j` (`B->A`, `j=1,2,3`)

such that all six connectors are **direct arcs**, the three `F_i` are pairwise vertex-disjoint, and the three `G_j` are pairwise vertex-disjoint. Hence `alpha_1,alpha_2,alpha_3` are distinct and `beta_1,beta_2,beta_3` are distinct, and similarly the three `gamma_j` and three `delta_j` are distinct.

### Proof

By 3-vertex-strongness and directed vertex-Menger, there are three pairwise vertex-disjoint directed paths from `A` to `B`: if a separator of size at most two met all such paths, delete it and choose surviving vertices of `A` and `B`; the remaining digraph is strongly connected, contradiction. Trim each path from its last `A` vertex to its first subsequent `B` vertex. The interiors then avoid `A union B`.

Under the present no-H-mediation assumption, none of the three trimmed paths can meet `H`, so every internal vertex lies in `R`. Lemma 4.1 then says that any non-direct one would itself force H mediation. Therefore all three are direct arcs. The reverse direction is identical. QED.

This removes hidden dependence in a way stronger than probabilistic independence: in the residual branch there are no connector interiors to collide at all.

## 6. New reconstruction theorem — the 3-way pairing permutation counts mixed cycles

Assume first that all six endpoints on each support are distinct across directions. On `A`, consider the three endpoint types `delta` (arrivals of `G`) and `alpha` (departures of `F`). If they alternate around the directed cycle, there is a unique permutation `pi_A in S_3` such that the three directed support intervals

`A[delta_{pi_A(i)}, alpha_i]`, `i=1,2,3`,

are pairwise vertex-disjoint. Likewise, if the six `B` endpoints alternate by type, there is a unique `pi_B in S_3` such that

`B[beta_i, gamma_{pi_B(i)}]`, `i=1,2,3`,

are pairwise vertex-disjoint.

### Theorem 6.1 (`BT4-R4-3X3-CYCLE-FACTOR`)

If both supports fully alternate, the union of the six direct cross arcs with those six support intervals decomposes into as many pairwise vertex-disjoint directed mixed cycles as there are cycles of the permutation

`sigma = pi_A^{-1} o pi_B`.

In particular:

- if `pi_A=pi_B`, there are **three** pairwise vertex-disjoint mixed directed cycles; together with the disjoint packed triangle `H` they form four vertex-disjoint directed cycles, contradicting BT4-counterexamplehood;
- if `sigma` is a transposition, the union has two mixed directed cycles;
- if `sigma` is a 3-cycle, the union is one mixed directed cycle.

### Proof

Start at `alpha_i`. Traverse the direct arc `F_i` to `beta_i`, then the selected `B` interval to `gamma_{pi_B(i)}`, then `G_{pi_B(i)}` to `delta_{pi_B(i)}`. The selected `A` interval starting there ends at `alpha_k` where `pi_A(k)=pi_B(i)`, i.e.

`k = pi_A^{-1}(pi_B(i)) = sigma(i)`.

Thus one circuit through the selected directed pieces sends the `F`-index `i` to `sigma(i)`. Pairwise disjointness of the selected support intervals and distinctness of the direct-cross endpoints imply that different permutation orbits give vertex-disjoint directed cycles and every selected piece lies on exactly one such cycle. Hence the number of mixed cycles is exactly the number of cycles of `sigma`.

When `sigma=id`, its three singleton orbits give three mixed cycles, all contained in `A union B` and therefore disjoint from `H`; adjoining `H` gives the prohibited four-pack. QED.

This is the first point in the current order-wall programme where the counting object directly reconstructs the **fourth cycle packing** rather than merely another neutral three-packing.

## 7. A rank-only closure is false: exact finite countermodels

Theorems 5.1--6.1 do **not** imply that every direct `3 x 3` system has an identity cycle factor. The port order must be paid.

I executed an exact finite enumeration over all normalized cyclic orders of six distinct endpoints on each support. Rotations are normalized by fixing `A1` first on `A` and `B1` first on `B`. For every pair of cyclic orders the checker tests every choice of two forward arcs, two reverse arcs, and both pairings, using closed directed support intervals and literal vertex-disjointness.

Exact output from `three_by_three_order_check.py`:

```
cyclic_order_pairs_tested = 14400
no_compatible_2x2 = 10548
first_countermodel = (('A1', 'A2', 'A3', 'D1', 'D2', 'D3'), ('B1', 'B2', 'B3', 'G1', 'G2', 'G3'))
```

So even three direct connectors in each direction do **not** force a compatible `2 x 2` splice from cyclic order alone. The first countermodel is the completely grouped signature: all forward endpoints occur consecutively and all reverse endpoints consecutively on both supports. This is a countermodel only to the local rank-only selection claim, not to BT4 and not to the exact-seven cage.

I also tested a stronger but tempting Hall shortcut suggested by the two-way parity wall: start from a `2 x 2` parity mismatch, add one fresh forward source with **two** fresh targets, and ask whether keeping either old forward arc plus one of the two fresh arcs must resolve the pairing. It does not. Exact output from `order_wall_check.py`:

```
initial_parity_mismatch_orders = 2
extended_fresh_fan_orders = 160
unresolved_by_pure_cyclic_order = 160
first_unresolved = (('D1', 'A1', 'D2', 'A2', 'A3'), ('G1', 'B1', 'G2', 'B2', 'B3', 'B4'))
```

Thus the subclaim

`fresh two-target fan + old parity mismatch => compatible splice by Hall/cyclic order alone`

is `CANDIDATE_REFUTED`. This agrees with, and strengthens the warning supplied by, fleet03/B05's fresh-cross parity trap: the next proof must exploit graph-specific geometry, not independent random choices or raw connector rank.

The scripts are stored source-exactly beside this report:

- `order_wall_check.py`
- `three_by_three_order_check.py`

No numerical census is promoted as proof of the parent conjecture.

## 8. First essential missing implication

The surviving local statement is now sharply formulated as

`BT4-R4-DIRECT-3X3-ORDER-FORCING-v1`:

> In the exact aligned four-remainder heavy-triangle cage, use exact outdegree seven, global NO-SIX, chordlessness, shortest-mixed-cycle constraints and the fixed cage/fan arcs to prove that the direct `3 x 3` cross system of Theorem 5.1 either (i) has three-way alternating port orders with `pi_A=pi_B`, giving the four-pack of Theorem 6.1; (ii) has a productive packed-endpoint collision; (iii) emits a same-support bypass; (iv) forces H mediation; (v) forces SIX / bounded short support; or (vi) yields a strict lexicographic packing improvement / cyclic exchanged remainder.

The purely topological statement with only 3-vertex-strongness and connector rank is false by the explicit grouped-port countermodel above. The missing information must therefore come from the **degree/fan/shortest-cycle constraints of the actual BT4 normal form**.

A useful metric refinement for the next run is this: if `K=F_0+B[beta_0,gamma_0]+G_0+A[delta_0,alpha_0]` is chosen shortest and another direct `A->B` arc has source in the complementary `A` interval but target on the `B` trace of `K`, shortestness imposes a comparison between its forward displacement on `A` and on `B`. The fleet03/B05 parity-trap theorem shows that merely adding a reverse arc cannot pay this comparison; the new `3 x 3` direct system is the first place where those metric inequalities can be summed over several independent crosses without assuming their choices are independent.

Global campaign debts remain separate: SIX closure, bounded F2/F3 states, the support-carried seven-remainder branch, and any H-mediated branch not already closed by other workers.

## 9. Honesty, failures and scope

Classification: **`ESSENTIAL_STEP_APPLIED`**, not `FULL_PROOF_CANDIDATE`.

What is proved here is the exact-cage direct-three-linkage reduction and the three-way cycle-factor reconstruction criterion. What is refuted is the rank-only / fresh-fan Hall shortcut. BT4 itself remains open.

No authenticated brain retrieval or source-bound cognitive firing occurred; status remains `WITHOUT_VERIFIED_BRAIN`. No email, Drive, public posting, paid model/API, Codex, remote workflow, credential use, benchmark gold, unrelated private material, or other-account native action was used. The finite computations are local combinatorial enumerations of cyclic endpoint orders only.
