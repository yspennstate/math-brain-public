# BT4 proof attempt — account01/B06

Run: `20260922T083534Z-b06-bt4-r11x`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-R4-DIRECT3X3-SWITCH-CLASSIFICATION-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Fresh state actually consumed

Fresh owner controls were read coherently at `bf8cf24101d2e090d6db2c9d9af38959785729c5`, OWNER CONTROL revision `2026-09-22.2`, together with the active ORDER/TARGETS/ASSIGNMENTS package. Installation/benchmark work remains superseded for this slot.

The latest complete campaign-lead report available in the canonical scientific archive remains account02/B04 `20260922T0619Z-b04-bt4-r11`, report blob `713053330313bf5906035c7bfd5841eb4e6b88ef`, handoff blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`. Later lead run directories visible during this invocation had not supplied a later complete canonical report and were not promoted.

Named OTHER-account result actually consumed and applied: account04/B05 run `b05-20260922t074314z-r35`, candidate `BT4-R4-DIRECT-3X3-CYCLE-FACTOR-v1`, canonical report blob `ab5f354238ef330125494b0afa5c8e4799716534`, source-bound handoff blob `7b0ab787c77713fbc54cced778f236a0236468fe`. Its residual no-H-mediation branch is a fully direct `3 x 3` cross-port system. In the fully alternating endpoint case, the mixed-cycle count is the cycle count of `sigma=pi_A^{-1} pi_B`; identity closes BT4 locally, while rank alone does not force identity.

I also apply account03/B04 `BT4-R4-RANK3-SHORT-MIXED-BYPASS-v1`, report blob `df8c2244fb4a13f5a6fd4ef9fac4bc334076a25a`: in the same R4 normal form a shortest mixed cycle forces a fresh-source cross or a same-support bypass (unless third-support mediation already occurs). The bypass is already a productive campaign exit; the fresh-cross alternative is retained below as the next non-port-only input.

The immediately preceding B06 result `BT4-R4-DIRECT3X3-NONTRANSPOSE-v1`, report blob `d09f7c94d56b17ef6ef93b851471a5148fc4db9e`, excludes transposition monodromy by chordlessness of a globally minimum equal-size repacking. Hence the fully alternating direct-rank-three wall has only the two inverse 3-cycle monodromies left.

## Compact conditional end-to-end route

Use the established minimal-counterexample normal form: oriented, exactly seven-outregular, arc-dominated and 3-vertex-strong, with a globally minimum three-cycle packing and acyclic remainder. Existing campaign reductions route the exact four-remainder heavy-triangle branch to SIX / third-support mediation / a same-support bypass / a strict packing improvement / cyclic exchanged remainder / a fourth cycle, or to account04/B05's direct `3 x 3` cross-port wall. Identity monodromy already gives three mixed cycles plus `H`; transposition monodromy is impossible by the preceding B06 lemma. Thus only 3-cycle monodromy survives.

The theorem below completely classifies every spanning refactorization that uses only the six selected support intervals, the six selected direct cross arcs, and the six original support-boundary arcs. It shows that the hoped-for purely six-chord closure is false: one orientation class is switch-rigid, and the only flexible orientation class has exact neutral two-cycle refactorizations with no prescribed internal chord. Therefore the next proof must genuinely use extra graph information. Applying account03/B04 identifies that extra information sharply as a fresh-source CROSS (unless a same-support BYPASS has already exited the branch).

## New theorem: exact switch algebra for the residual 3-cycle monodromy

### Contracted notation

Contract each of the three selected directed support intervals on `A` and `B` to an oriented path-block, without deleting its vertices. Write these blocks as `A_i,B_i` (`i in {1,2,3}`), with entries `A_i^- , B_i^-` and exits `A_i^+ , B_i^+`.

Relabel the selected direct crosses so that the forward crosses are

`F_i : A_i^+ -> B_i^-`,

and the selected reverse crosses are

`G_i^* : B_i^+ -> A_{sigma(i)}^-`.

The residual case has `sigma` a 3-cycle. Let `c_A,c_B in S_3` be the cyclic successor permutations of the interval-blocks on the original support cycles. Thus the original support-boundary arcs are

`A_i^+ -> A_{c_A(i)}^-`,    `B_i^+ -> B_{c_B(i)}^-`.

Both `c_A` and `c_B` are 3-cycles.

A **port-supported spanning transition factor** is a directed 2-factor on all six blocks obtained by retaining every block internally and, at every block exit, choosing exactly one of the two available transition types: original support-boundary or selected direct cross.

### Theorem (`BT4-R4-DIRECT3X3-SWITCH-CLASSIFICATION-v1`)

For such a transition factor, let `x_i=1` when `A_i^+` uses `F_i`, and `x_i=0` when it uses its original A-support boundary. Let `y_i` be the analogous indicator at `B_i^+` for using `G_i^*`.

Then a choice is a directed 2-factor if and only if

`y_i = x_{c_B(i)}`

for all `i`, and

`x_{T(i)}=x_i` for all `i`, where

`T = c_B sigma^{-1} c_A`.

Since `c_A,c_B,sigma` are all even permutations on three letters, `T` is either the identity or a 3-cycle. Consequently:

1. If `T` is a 3-cycle, the only port-supported spanning transition factors are `x=(0,0,0)` and `x=(1,1,1)`, namely the original pair `A union B` and the all-cross mixed cycle `K`. There is **no partial switch at all**.
2. If `T=id`, all eight bit vectors are valid transition factors. The weight-one choices give one mixed spanning cycle; the weight-two choices give two mixed directed cycles covering all of `A union B`; the all-zero factor is `A union B`; the all-one factor is `K`.
3. Because `c_A,c_B` are 3-cycles, `T=id` occurs exactly when `c_A=c_B` and `sigma=c_A^{-1}` (after a common relabeling of the three blocks). Every other 3-cycle-monodromy orientation is switch-rigid as in (1).

### Proof

At the entry `B_j^-`, the only two prescribed incoming transitions are the forward cross from `A_j^+` and the B-support boundary from `B_{c_B^{-1}(j)}^+`. Exact indegree one therefore says

`x_j + (1-y_{c_B^{-1}(j)}) = 1`,

hence `y_i=x_{c_B(i)}`.

At `A_k^-`, the only two prescribed incoming transitions are the A-support boundary from `A_{c_A^{-1}(k)}^+` and the reverse cross from `B_{sigma^{-1}(k)}^+`. Exact indegree one says

`(1-x_{c_A^{-1}(k)}) + y_{sigma^{-1}(k)} = 1`.

Substituting the first relation gives

`x_{c_B sigma^{-1}(k)}=x_{c_A^{-1}(k)}`.

Put `k=c_A(i)`. This is exactly

`x_{c_B sigma^{-1} c_A(i)}=x_i`,

so `x` must be constant on the cycles of `T=c_B sigma^{-1}c_A`. Conversely these equations give indegree one at every block entry, while every block exit has one chosen transition by construction, so they are sufficient.

The product `T` is even. On three letters an even permutation is `id` or a 3-cycle. If `T` is a 3-cycle, a Boolean vector constant on its sole orbit is constant, giving only all-zero and all-one. If `T=id`, every Boolean vector works.

For the last assertion, all 3-cycles lie in the cyclic subgroup of order three, so they commute. The equation `T=id` is `sigma=c_A c_B`. If `c_A` and `c_B` are opposite 3-cycles, their product is `id`, impossible because `sigma` is a 3-cycle. Hence `c_A=c_B=c`, and then `sigma=c^2=c^{-1}`. The converse is immediate.

For `T=id`, use cyclic relabeling to take `c_A=c_B=c=(123)` and `sigma=c^{-1}`. Direct tracing shows a weight-one selection joins the two original support cycles into one mixed cycle, whereas a weight-two selection yields two mixed cycles. Cyclic symmetry covers all three choices of each weight. QED.

## Explicit local countermodel: the six-chord wall does not close by itself

The preceding classification is not merely an absence-of-proof statement. There is a concrete loopless simple directed port graph satisfying the full-alternation / direct-rank-three / 3-cycle-monodromy transition hypotheses in which the nontrivial neutral two-cycle refactorization has no chord coming from any prescribed transition edge.

Take `c=(123)`, `c_A=c_B=c`, `sigma=c^{-1}`. For each `i`, let `A_i` and `B_i` be a nonempty directed path. Add exactly the following transitions:

- A-support boundaries `A_i^+ -> A_{c(i)}^-`;
- B-support boundaries `B_i^+ -> B_{c(i)}^-`;
- forward crosses `A_i^+ -> B_i^-`;
- reverse crosses `B_i^+ -> A_{sigma(i)}^-`.

Choose `x_1=x_2=1,x_3=0`. The factor equations force `y_1=1,y_2=0,y_3=1`. The resulting two directed cycles are, at block level,

`C_1 = A_1 -> B_1 -> A_3 -> A_1`,

`C_2 = A_2 -> B_2 -> B_3 -> A_2`.

They cover every vertex of `A union B`. The six unused prescribed transitions are

- `A_1 -> A_2`, `A_2 -> A_3`, `A_3 -> B_3`;
- `B_1 -> B_2`, `B_2 -> A_1`, `B_3 -> B_1`.

Every one goes **between** `C_1` and `C_2`; none has both endpoints on one of the two cycles. Taking each block itself chordless therefore makes both `C_1,C_2` chordless relative to the entire prescribed port graph. This is a genuine local countermodel to the implication

`3-cycle monodromy + six original support-boundary chords => a chord contradiction or strict smaller packing`

when only the B05 port-system information is used. It is **not** a counterexample to BT4 or to the full exact-seven R4 cage, because the omitted exact-degree / remainder-fan arcs are precisely the information not represented in this local graph.

## Application of account03/B04 and the first unpaid implication

The local countermodel proves that the residual cannot be closed by repeatedly switching only among the twelve prescribed transitions. Account03/B04 supplies the required non-port edge: choose a shortest genuine A/B mixed cycle in the exact R4 cage. Unless third-support mediation or a same-support bypass already occurs, its theorem forces a **fresh-source direct cross**.

Therefore the first missing implication is now narrower than `six-chord circular closure`:

`BT4-R4-DIRECT3X3-FRESH-CROSS-BREAK-v1`:

> In the exact-seven / global-NO-SIX four-remainder heavy-triangle cage, assume the fully alternating direct `3 x 3` system has 3-cycle monodromy. Apply account03/B04 and obtain a fresh-source cross. Use the exact R4 fan arcs and degree deficits to prove that this extra cross cannot remain trapped inside either switch class above. It must force one of: (i) a same-support bypass; (ii) H/third-support mediation; (iii) SIX; (iv) a strict lexicographic packing decrease or cyclic exchanged remainder; or (v) a replacement direct `3 x 3` selection with identity/transposition monodromy, which is already closed by B05 plus the previous B06 lemma.

A single arbitrary fresh cross is not declared sufficient by cyclic order alone; that would contradict the team's existing parity-trap controls. The unpaid work is specifically to exploit exact-seven/global-NO-SIX/R4 structure to make the fresh cross switch-breaking.

## Honest boundary

This run proves the switch-classification theorem and a source-valid local countermodel to the port-only six-chord closure. It does **not** prove BT4. Global debts such as SIX closure and other non-direct-R4 / bounded-support branches remain separate. No edge-disjoint substitute is used.

No authenticated brain retrieval/context was used. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid/remote compute, workflow dispatch, permission change, or protected-control mutation was used.
