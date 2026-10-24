# BT4 account01/B04 — domination-torus reduction of the remaining light-support port wall

Run: `20260922T0744Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-DOMINATION-TORUS-CYCLE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the target, hence directed digons count.

Current public source boundary checked on 22 September 2026: Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (submitted 13 August 2026), explicitly says the genuine conjecture remains unresolved for every `k>=4`; their theorem permits one reversed arc per cycle and is not a genuine BT4 conclusion. Lichiardopol--Pór--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, proves the genuine `k=3` theorem `delta^+>=5 => 3` disjoint directed cycles and the strengthened `k=2` input used elsewhere by the team.

No search miss is treated as a novelty claim.

## 2. Exact inherited mathematics consumed

### Campaign lead

I read the latest complete account02/B04 lead report available at the start of the mathematical derivation:

`proofnet24/collective-BT4/account02/B04/20260922T0619Z-b04-bt4-r11/report.md`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

Its controlling normal form is a hypothetical BT4 counterexample `D` reduced to an oriented, exactly seven-outregular, arc-dominated, 3-vertex-strong digraph. Three pairwise vertex-disjoint directed cycles `(H,A,B)` are chosen lexicographically: first minimize total packed order and then maximize the number of arcs induced by the acyclic remainder `R`. Packed cycles are chordless.

In the live four-remainder heavy-triangle branch,

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

and the lead's corrected long aligned state supplies a clean opposite pair

`p->x->b` (`A->B`), `q->a3` (`B->A`),

with four distinct packed ports. Its theorem `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` correctly sends the state to a genuine packed CROSS or a distinct-port same-support remainder BYPASS. It also corrects the earlier invalid direct use of a two-packed-port lemma on the four-port mixed cycle.

### Assigned OTHER-account partner account02/B05 — actually applied

I read and use account02/B05 `BT4-R4-ALIGNED-TRIPLE-ABSORPTION-v1`, report

`proofnet24/collective-BT4/account02/B05/20260922T062431Z-b05-bt4-b744a134/report.md`, Git blob `bf6b94983890a99c3c8d2e902bfc94fa3f57e22c`.

It proves that the aligned consecutive-triple lock cannot remain a terminal branch: global minimum forces the light support to be a triangle, and the canonical neutral source pivot then exposes a heavy inport forbidden by the complete F2/F3 survival classification. Hence the present run does **not** reopen that solved local lock. I work only after that partner reduction, on the genuine long-support CROSS/BYPASS/order wall.

### Rank-two input used to identify the first missing inference

I also read account04/B06 `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`, blob `ff7bbac3a8211262bc273f6fa02b102d3ace16dd`, and account01/B06 `BT4-X-DELETED-2X2-RANK-COLLAPSE-v1`, blob `fdd394bc4a6b8f3ca851978c06219c5fe7563881`. They reduce the all-long, no-bypass, no-third-support branch to an explicit packed-port order wall: after deleting the distinguished sink, there are rank-two connector families in both directions; internal cross-direction intersections produce a bypass or short support; the remaining obstruction is cyclic order / endpoint matching on `A,B`.

## 3. Compact conditional end-to-end route

Assume BT4 false and enter the inherited exact-seven normal form. The genuine `k=3` theorem supplies the initial three-packing. The collective deficit and neutral-pivot reductions route the principal four-remainder NO-SIX branch to clean light-support CROSS/BYPASS geometry; the named partner removes the aligned consecutive-triple lock. Rank-two/Menger work then removes connector matching number one and uncontrolled interior intersections.

Thus, locally, a complete proof would follow if the residual packed-port order wall could always be converted into one of: two legal vertex-disjoint replacement cycles, a strictly smaller three-packing, a directed cycle in an exchanged remainder, SIX, short support already covered by bounded analysis, third-support mediation, or a compatible bypass family.

The first unpaid inference was that the residual port pattern could still be essentially arbitrary. The theorem below shows it cannot: **arc domination closes the direct cross pattern under a rigid predecessor rule on the discrete torus `A x B`, and because direct crosses occur in both directions, that rule forces a mixed winding cycle.** Every sign switch of that cycle is an explicit two-edge packed detour replacing one support edge. The arbitrary order wall is thereby reduced to a finite homological/staircase structure.

## 4. Preliminary lemma — every remainder connector directizes unless an existing exit already occurs

Let

`P : a -> ... -> v -> b`, with `a in A`, `b in B`,

be a directed `A->B` connector whose internal vertices lie in the acyclic remainder `R`. Assume there is no same-support remainder bypass, no third-support mediation, and no short-support replacement of order at most `|R|+1`.

Apply arc domination to the final arc `v->b`. A dominator `z` satisfies `z->v,b`. If `z in R`, dominate `z->b` and continue backwards while retaining the same target `b`. The process cannot remain in `R` forever, because the successive domination vertices form a directed chain and `D[R]` is finite and acyclic. Let `c` be the first packed vertex reached.

- If `c in A`, the domination step itself gives the direct cross `c->b`.
- If `c in H`, we have third-support mediation.
- If `c in B`, the full domination chain gives a distinct-port `B`-to-`B` path through `R`; it is a same-support bypass. The endpoint cannot equal `b`, since the terminal domination step would then require a loop `b->b`.

Thus, outside already-useful exits, every remainder-internal `A->B` connector yields a **direct** `A->B` cross. The statement is symmetric for `B->A`.

In particular, the rank-two results consumed above imply that in the pure long-support residual there is at least one direct cross in each direction.

## 5. New theorem — `BT4-DOMINATION-TORUS-CYCLE-v1`

### Statement

Work in the inherited oriented, exact-seven, arc-dominated, globally minimum three-packing normal form. Let `A=(a_i)_{i mod m}` and `B=(b_j)_{j mod n}` be chordless packed directed cycles. Assume:

1. direct crosses exist in both directions between `A` and `B`;
2. there is no third-support mediation;
3. there is no distinct-port same-support path with all internal vertices in `R`;
4. `|A|,|B|>|R|+1` (in the live R4 cage, both are at least six).

Encode a direct cross by an occupied signed cell of the torus `Z_m x Z_n`:

- `+(i,j)` means `a_i->b_j`;
- `-(i,j)` means `b_j->a_i`.

Because the inherited normal form is oriented, a cell cannot carry both signs.

Then every occupied signed cell has an occupied predecessor of one of the following two forms:

`+(i-1,j)` or `-(i,j-1)`.                                  (T)

After choosing one permitted predecessor at every occupied cell, the resulting finite functional digraph contains a directed predecessor cycle that uses **both signs**. If that mixed predecessor cycle contains `N_+` plus states and `N_-` minus states, then

`N_+ = u m`, `N_- = v n`                                   (W)

for some positive integers `u,v`. In particular it winds nontrivially around both torus coordinates and contains at least `m+n` direct cross states.

Moreover every sign switch has an exact graph-theoretic meaning:

- a transition whose current state is `+(i,j)` and whose predecessor is `-(i,j-1)` gives the directed two-edge detour

  `b_{j-1} -> a_i -> b_j`,                                  (B-detour)

  parallel to the support edge `b_{j-1}->b_j`;

- a transition whose current state is `-(i,j)` and whose predecessor is `+(i-1,j)` gives

  `a_{i-1} -> b_j -> a_i`,                                  (A-detour)

  parallel to `a_{i-1}->a_i`.

Every mixed predecessor cycle contains at least one detour of each type.

### Proof of the predecessor rule (T)

Take an occupied `+(i,j)`, i.e. the arc `a_i->b_j`. Arc domination supplies a vertex `z` with

`z->a_i`, `z->b_j`.                                        (1)

There are four possible locations.

**(a) `z in A`.** Chordlessness of the directed support `A` forces `z=a_{i-1}`: the only arc of `A` entering `a_i` from another vertex of `A` is its support predecessor. Equation (1) therefore gives `a_{i-1}->b_j`, namely `+(i-1,j)`.

**(b) `z in B`.** Chordlessness similarly forces `z=b_{j-1}`, and (1) gives `b_{j-1}->a_i`, namely `-(i,j-1)`.

**(c) `z in H`.** This is third-support mediation, excluded by hypothesis.

**(d) `z in R`.** This case cannot survive the hypotheses. Repeatedly dominate the arc from the current remainder dominator to the fixed target `b_j`, exactly as in Section 4, until a first packed apex `c` is reached. The domination chain has internal vertices in `R`, and its last remainder vertex is still `z`, which also has the arc `z->a_i` from (1).

- If `c in A` and `c!=a_i`, concatenate the chain from `c` to `z` with `z->a_i`; this is a distinct-port same-support `A` bypass through `R`.
- If `c=a_i`, the same chain closes into a genuine directed cycle using `a_i` and at most all vertices of `R`. Replacing `A` by that cycle while retaining `H,B` gives another three-cycle packing, so global minimum yields `|A|<=|R|+1`, contrary to hypothesis.
- If `c in B`, the chain ending at `b_j` is a distinct-port same-support `B` bypass; `c!=b_j` because loops are forbidden.
- If `c in H`, this is third-support mediation.

Thus case (d) is impossible in the residual branch. This proves (T) for a plus state. For a minus state `b_j->a_i`, the same domination argument with the roles of `A,B` interchanged gives exactly the same two allowed predecessor cells `+(i-1,j)` or `-(i,j-1)`.

### Proof that a mixed predecessor cycle exists

Choose, for every occupied signed cell, one allowed predecessor given by (T). Iterating this map from any occupied state eventually enters a directed cycle because the occupied-state set is finite.

A predecessor cycle using only plus states keeps `j` fixed and decrements `i` by one at every step. Hence it is exactly the full plus row

`+(0,j), +(1,j), ..., +(m-1,j)`                             (2)

in cyclic order. Likewise a predecessor cycle using only minus states is exactly a full minus column

`-(i,0), -(i,1), ..., -(i,n-1)`.                            (3)

Because direct crosses exist in both orientations, start one predecessor trajectory from a plus state and one from a minus state.

A trajectory beginning outside a full plus row cannot enter that row for the first time. Indeed, if `t=+(i,j)` were the first row state reached from its predecessor-successor state `s` (that is, the chosen predecessor of `s` is `t`), then the only way `t` can be a permitted predecessor is the `+(i-1,j)` alternative; consequently `s` has cell `(i+1,j)`. But the full plus row already contains the plus state at `(i+1,j)`. Orientedness forbids an opposite minus state at that same cell, so `s` is itself a row state, contradicting first entry. Symmetrically, no outside trajectory can enter a full minus column for the first time.

Therefore, if the plus-started trajectory ends in a pure cycle, that cycle is a full plus row; if the minus-started trajectory ends in a pure cycle, it is a full minus column. These two pure cycles cannot both exist: their row and column meet in one torus cell, which would then carry both `a_i->b_j` and `b_j->a_i`, a directed digon, contradicting the oriented normal form.

Hence at least one predecessor trajectory ends in a cycle containing both signs.

### Winding count (W)

Along a predecessor step, the first coordinate decreases by one exactly when the new predecessor state is plus, and the second coordinate decreases by one exactly when it is minus. On a closed predecessor cycle, both coordinates return to their starting values modulo `m,n`. Thus the number `N_+` of plus states on a mixed cycle is a positive multiple of `m`, and the number `N_-` of minus states is a positive multiple of `n`, proving (W).

### Sign-switch detours

If a plus state `+(i,j)` chooses the minus predecessor `-(i,j-1)`, the two encoded arcs are exactly

`b_{j-1}->a_i` and `a_i->b_j`,

which concatenate to the B-detour displayed above. The other sign switch is symmetric. A cyclic word containing both signs has at least one transition `+` to `-` and at least one transition `-` to `+`; hence both detour types occur. QED.

## 6. What this pays

The live long-support wall was previously described only as an arbitrary cyclic-order/parity incompatibility among several direct or remainder-supported connectors. The theorem proves that, after the existing bypass/short-support/third-support exits are removed, the direct cross set cannot be arbitrary. It contains a **mixed monotone winding cycle on `Z_m x Z_n`** whose local sign changes are explicit two-edge packed detours replacing support edges on both `A` and `B`.

This has two concrete consequences for subsequent workers:

1. the obstruction carries at least `|A|+|B|` source-valid direct cross arcs arranged in one predecessor-closed staircase, not merely four unrelated ports;
2. the remaining splice problem can be attacked block-by-block along this single torus cycle. A maximal plus block shares one `B` target and a maximal minus block shares one `A` target; adjacent sign switches give the exact two-edge support detours above. Thus any surviving parity wall must be compatible with the entire winding staircase, not just one chosen 2x2 connector family.

I have **not** claimed that a two-edge detour is a legal same-support remainder bypass: its internal vertex lies on the other packed support. I also have not claimed that the mixed torus cycle itself is a fourth directed cycle in `D`. Those would be invalid promotions.

## 7. First essential missing implication after this run

Define `BT4-TORUS-BLOCK-SPLICE-v1`:

> In the live R4 long-support residual, take the mixed domination predecessor cycle supplied by `BT4-DOMINATION-TORUS-CYCLE-v1`. Decompose it into maximal plus and minus blocks. Using the exact heavy-triangle cage, the x-deleted connector tax, and global minimum of the three-packing, prove that either two block-boundary detours can be paired into two vertex-disjoint mixed replacement cycles, or the block geometry forces a strict smaller packing, a directed cycle in an exchanged remainder, SIX, a support of bounded order, third-support mediation, or a genuine compatible remainder bypass family.

A useful exact reformulation is geometric. Every plus block gives a set of consecutive `A` vertices with a common `B` target; every minus block gives consecutive `B` vertices with a common `A` target. The two boundary switches supply opposite two-edge detours. The unpaid issue is whether the cyclic block intervals can avoid all disjoint pairings while respecting the winding condition (W), exact outdegree seven, and the previously proved `L_X<=7` connector tax. This is substantially narrower than the former arbitrary port-order wall.

Full BT4 still separately requires the global SIX closure, the remaining bounded F2/F3 states, and the support-carried seven-remainder omitted-sink branch. No inference about those debts is made here.

## 8. Exact deletion / contraction accounting retained for the B04 assignment

For any packed directed cycle `C` and any vertex `v` outside it, let

`a_C(v)=|N^+(v) intersect V(C)|`.

In the exact-seven normal form,

`d^+_{D-C}(v)=7-a_C(v)`.                                    (4)

If `C` is contracted to one vertex and quotient parallel arcs are coalesced,

`d^+_{D/C}(v)=7-a_C(v)+1_{a_C(v)>0}`.                       (5)

Thus deletion loses exactly `a_C(v)` outgoing neighbors, while contraction recovers only one and still loses `a_C(v)-1` whenever `v` hits `C`. The contracted cycle vertex has outdegree equal to the number of **distinct external heads** of `C`, which can also be below seven. For two disjoint contracted cycles, the two indicator corrections add. Consequently contraction preserves vertex-disjoint lifting in the obvious quotient sense but does **not** preserve the degree-seven hypothesis needed for a recursive BT4 invocation. This is the exact obstruction, not a heuristic warning.

## 9. Failure checks

- The target permits digons, but the torus theorem is used only after the inherited genuine digon reduction to the oriented minimum-counterexample normal form.
- Arc domination is used on actual arcs of `D`; no missing arc is inserted.
- Repeated domination through `R` terminates because the directed domination chain would otherwise repeat a remainder vertex and create a directed cycle in the acyclic remainder.
- Chordlessness is used only to identify a packed dominator of an arc entering a vertex of the same support with that vertex's support predecessor.
- The short-support conclusion in the self-return case is exactly `|A|<=|R|+1` (or symmetrically for `B`); in the R4 cage this is at most five.
- The mixed-cycle existence argument uses orientedness at the intersection of a hypothetical full plus row and full minus column; it does not apply to the unreduced target before the digon reduction.
- No finite computation is used and no auxiliary count is promoted to a BT4 proof.

## 10. Honest status

`ESSENTIAL_STEP_APPLIED / OPEN_NOT_PROVED / WITHOUT_VERIFIED_BRAIN`.

The assigned partner's aligned-triple absorption is consumed to remove that branch. The new mathematical contribution is the domination predecessor closure (T), directization of remainder connectors, forced mixed torus winding cycle (W), and its two exact sign-switch detours. The first local debt is now the block-splice theorem above rather than arbitrary connector rank or arbitrary cyclic port order.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: maximum actually supported. Configured reasoning effort and provider reasoning usage: `UNKNOWN_NOT_EXPOSED` / not exposed. Elapsed execution is recorded in the operational receipt and is not pure thinking time.
