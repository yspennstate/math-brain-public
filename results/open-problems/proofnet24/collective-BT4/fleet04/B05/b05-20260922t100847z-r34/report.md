# BT4 fleet04/B05 — gap-signature invariance and the two-fresh-cross parity gate

Run: `b05-20260922t100847z-r34`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Role: counting / probabilistic-choice / reconstruction with dependencies paid  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Subcandidate refuted: `ONE-FRESH-CROSS-BREAK`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and current literature boundary

The target is the genuine k=4 Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven has four pairwise vertex-disjoint genuinely directed cycles. Digons count.

The current external boundary was rechecked. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (submitted 13 August 2026), states that the genuine conjecture remains unresolved for every k>=4 and proves instead a relaxation allowing one reversed arc per packed cycle. Lichiardopol--Pór--Sereni, SIAM J. Discrete Math. 23 (2009), 979--992, proves the genuine k=3 threshold-five theorem used in the campaign.

No novelty is inferred from a search miss.

## 2. Exact campaign state consumed

### Team lead

The latest complete canonical fleet02/B04 lead report available was

`proofnet24/collective-BT4/fleet02/B04/20260922T0619Z-b04-bt4-r11/report.md`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`, candidate `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`.

I use its inherited hypothetical-counterexample normal form: oriented, exactly seven-outregular, arc-dominated and 3-vertex-strong, with a three-cycle packing chosen first to minimize packed order and then to maximize remainder arcs; the remainder is acyclic and packed cycles are chordless. The live R4 heavy-triangle branch has `H=h0 h1 h2 h0` and old remainder `R={x,r0,r1,r2}`.

### Previous B05 state

The immediately relevant fleet04/B05 result is `BT4-R4-DIRECT-3X3-CYCLE-FACTOR-v1`, report blob `ab5f354238ef330125494b0afa5c8e4799716534`. In the no-H-mediation residual branch, directed Menger plus the exact R4 cage makes three A->B and three B->A connectors direct. When the six endpoint ports alternate on both light supports, the six cross arcs and selected support intervals decompose into a number of mixed directed cycles equal to the cycle count of the monodromy `sigma=pi_A^{-1} pi_B`. Identity gives three mixed cycles and hence, with H, the forbidden four-pack.

### Named OTHER-account result actually applied

I read and apply fleet01/B06 `BT4-R4-DIRECT3X3-NONTRANSPOSE-v1` (report created in run `20260922T080451Z-b06-bt4-r11`) and its strengthening/classification `BT4-R4-DIRECT3X3-SWITCH-CLASSIFICATION-v1` (run `20260922T083534Z-b06-bt4-r11x`). The first eliminates transposition monodromy in a globally minimum three-packing. The second proves that the residual 3-cycle monodromy cannot in general be closed by switching only among the six selected direct crosses and six original support-boundary transitions; extra graph information is genuinely required. Its first unpaid interface is a fresh-source cross supplied by fleet03/B04 unless a productive bypass/third-support exit already occurs.

The transposition proof should be read with the standard direct-splice packing tax made explicit: if the all-cross factor has two mixed cycles, global packing minimality forces the six omitted support gaps to have total edge length exactly six, hence each gap is one edge; only then does the repacking cover the same packed vertex set and the chord argument apply. This supplies the implicit equality step and does not change the partner conclusion.

I also use fleet03/B04 `BT4-R4-RANK3-SHORT-MIXED-BYPASS-v1`: in the exact R4 branch, a shortest A/B mixed cycle forces either a same-support bypass / third-support mediation or a fresh-source direct cross.

## 3. Compact conditional end-to-end route

The campaign reduction is now extremely narrow in this branch. The exact-seven globally minimum normal form reaches the fully direct 3x3 light-cross system. Identity monodromy gives the fourth cycle packing; transposition is excluded by fleet01/B06; therefore only a 3-cycle monodromy survives. Fleet03/B04 supplies an additional fresh-source cross unless an already accepted bypass/third-support exit occurs.

The tempting next step was to replace one old forward cross by this fresh cross and hope that the 3-cycle monodromy changes to identity or transposition. The theorem below proves that this is impossible whenever the replacement still has six distinct alternating ports. The dependence is exact: one-for-one replacement preserving alternation is trapped in the same two gap cells and therefore leaves the monodromy unchanged.

The first mechanism that can change the parity class while keeping full alternation is a **pair** of vertex-disjoint fresh crosses occupying complementary swapped gap cells. Such a pair changes the 3-cycle monodromy into a transposition, which is already excluded. Thus the remaining mathematical debt is no longer vague “use a fresh cross”: it is to force either this two-cross swapped-cell pair or one of the nonalternating/collision/bypass/H/SIX exits from exact-seven/R4 degree-fan data.

## 4. Gap signatures

Fix the three reverse direct crosses

`Gj : gamma_j -> delta_j`  (`B -> A`, j=1,2,3).

On A, delete the three arrival ports `delta_1,delta_2,delta_3`. They cut the directed support cyclically into three source gaps. For any direct forward cross `F:a->b` (`A->B`) whose source is not one of the deltas, define

`a(F)=r`

when `a` lies in the r-th gap, equivalently `delta_r` is the immediately preceding reverse-arrival port among the selected port set.

On B, the three reverse departure ports `gamma_1,gamma_2,gamma_3` cut the support into three target gaps. Define

`b(F)=s`

when `gamma_s` is the immediately following reverse-departure port among the selected port set.

A set of three forward crosses has fully alternating endpoints with the fixed reverse triple if and only if its three `a`-labels are all distinct and its three `b`-labels are all distinct. Identifying each selected forward cross by its unique A-gap label, the monodromy is exactly the permutation

`m : r -> b(F_r)`.

Thus the B05 residual is simply `m` a 3-cycle.

This encoding pays the endpoint-order dependencies rather than treating cross choices as independent.

## 5. New theorem — one fresh cross cannot change 3-cycle monodromy

### Theorem 5.1 (`BT4-R4-ONE-FRESH-GAP-INVARIANCE-v1`)

Assume a fully alternating direct 3x3 system with distinct ports and 3-cycle monodromy `m`. Replace exactly one selected forward cross `F_r` by another direct forward cross `E`, whose source and target are distinct from the retained ports. If the resulting three forward crosses still have fully alternating endpoints with the same reverse triple, then

`a(E)=r` and `b(E)=m(r)`.

Consequently the new monodromy is exactly the same permutation `m`; in particular it is again a 3-cycle.

### Proof

Before replacement, full alternation says that each of the three A-gaps contains exactly one selected forward source. Deleting `F_r` leaves the r-th A-gap empty and the other two occupied. If the new triple is still alternating, the fresh source must occupy the unique empty gap, so `a(E)=r`.

Exactly the same argument on B applies to targets: deleting `F_r` leaves only the target gap `m(r)` empty. Full alternation after insertion therefore forces `b(E)=m(r)`.

The gap permutation is unchanged on the two retained labels and also unchanged at r. Hence the entire monodromy `m` is unchanged. QED.

### Consequence

The subclaim

`one fresh-source cross + residual 3-cycle monodromy => identity/transposition by a one-for-one alternating reselection`

is false. This is not merely a failed search: Theorem 5.1 is an exact obstruction. Fleet03/B04's fresh-source cross can still be productive if it creates a port collision, destroys alternation in a way that yields a paid 2x2/bypass exit, participates in a multi-cross replacement, or invokes exact cage/fan geometry. It cannot change the 3-cycle class by itself while staying inside the distinct-port alternating 3x3 model.

## 6. New theorem — two crossed fresh cells are enough

### Theorem 6.1 (`BT4-R4-TWO-FRESH-PARITY-BREAK-v1`)

Keep the same residual system and let `r!=t`. Suppose there are two **vertex-disjoint** direct forward crosses `E,E'`, disjoint also from the retained selected ports, with gap signatures

`(a(E),b(E)) = (r,m(t))`,

`(a(E'),b(E')) = (t,m(r))`.

Replace `F_r,F_t` by `E,E'` and retain the third old forward cross and all three reverse crosses. Then the six ports alternate on both supports and the new monodromy is

`m' = m o (r t)`.

Since `m` is a 3-cycle, `m'` is a transposition. Therefore this configuration is impossible in the unresolved globally minimum BT4 state by fleet01/B06 `BT4-R4-DIRECT3X3-NONTRANSPOSE-v1`.

### Proof

The two replacement sources occupy exactly the two A-gaps vacated by `F_r,F_t`, so A remains alternating. Their targets occupy exactly the two B-gaps vacated by those same two old crosses, so B remains alternating. The replacement swaps which B-gap is paired to the two A-gap labels, and leaves the third label unchanged; hence `m'=m o (r t)`. A 3-cycle times a transposition is a transposition in `S_3`. Apply the partner theorem. QED.

This is the first true parity-changing mechanism in the direct 3x3 wall. It uses two dependent choices and explicitly requires vertex disjointness; no independence is assumed.

## 7. Counting reformulation of the remaining wall

Project every admissible fresh A->B direct cross to its 3x3 gap cell `(a,b)`. The old three selected crosses occupy the permutation cells `(r,m(r))`.

For each unordered pair `{r,t}`, the two complementary swap cells

`(r,m(t))` and `(t,m(r))`

cannot simultaneously contain **vertex-disjoint usable representatives**, by Theorem 6.1. Thus the residual exact-R4 state has a cross-intersection restriction on each of three complementary cell pairs.

Equivalently, any future collection of three vertex-disjoint fresh forward crosses whose A-gap labels and B-gap labels are both complete defines another permutation `p in S_3`. If `p=id`, B05's cycle-factor theorem closes with four cycles; if `p` is a transposition, fleet01/B06 excludes it; hence every surviving perfect matching of the fresh-cross cell graph must itself be one of the two 3-cycles.

This converts the “fresh cross” debt into a finite matching/diversity problem with dependencies visible. A cell count alone is not enough because many arcs can share endpoints; the next proof must use exact outdegree/global-NO-SIX/cage fan constraints to obtain vertex-disjoint representatives or else turn the forced endpoint concentration into a bypass, third-support mediation, SIX, short support, or a cyclic exchanged remainder.

## 8. Exact finite verification

The analytical proof above is complete; a small exact checker was used only as an adversarial verification. It normalizes the two 3-cycle orientations, the two cyclic block orientations on A, and the two on B (8 classes), inserts one distinct fresh source and one distinct fresh target into all 6x6 port gaps, tries all three one-for-one replacements, and recomputes the monodromy whenever full alternation survives.

Exact output:

```
normalized_3cycle_classes = 8
fresh_source_target_gap_insertions = 288
one_for_one_replacements_preserving_full_alternation = 96
still_3cycle_monodromy = 96
identity_or_transposition_after_one_replacement = 0
```

The source-exact checker is `gap_signature_check.py` beside this report. The enumeration is a verification of Theorem 5.1, not evidence for BT4 itself.

## 9. First essential missing implication

`BT4-R4-TWO-FRESH-CROSS-DIVERSITY-v1`:

> In the exact-seven/global-NO-SIX four-remainder heavy-triangle cage, start from the residual fully alternating direct 3x3 3-cycle monodromy and the fresh-source-cross output of fleet03/B04. Prove that either (a) exact degree/fan constraints force a second vertex-disjoint fresh cross in the complementary swapped cell required by Theorem 6.1; or (b) the fresh cross necessarily creates a productive endpoint collision/nonalternating 2x2 splice; or (c) endpoint concentration forces a same-support bypass, H/third-support mediation, SIX, short support, a strict lexicographic packing decrease, or a cyclic exchanged remainder.

A proof may not assume the second cross is independent of the first. Theorem 6.1 specifies the exact pairwise dependence that must be paid.

## 10. Failure boundaries and honest status

- This report does **not** prove BT4.
- The one-fresh-cross parity-break shortcut is refuted in the distinct-port fully alternating model.
- The two-fresh-cross theorem is conditional on actual vertex-disjoint representatives in the two complementary cells; cell occupancy alone is insufficient.
- Port collisions and nonalternating replacements are not declared contradictions and remain routed to the campaign's splice/bypass machinery.
- SIX, bounded F2/F3 states, and non-R4 campaign branches remain separate global debts.
- No authenticated brain retrieval/context was used: `WITHOUT_VERIFIED_BRAIN`.

Overall outcome: `ESSENTIAL_STEP_APPLIED`, with the explicitly named subcandidate `ONE-FRESH-CROSS-BREAK` refuted and the first unpaid implication sharpened to `BT4-R4-TWO-FRESH-CROSS-DIVERSITY-v1`.
