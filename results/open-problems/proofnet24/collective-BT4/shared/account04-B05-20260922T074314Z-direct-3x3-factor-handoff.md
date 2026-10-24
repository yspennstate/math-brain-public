# BT4 handoff — account04/B05 direct 3x3 cycle-factor reduction

Source run: `proofnet24/collective-BT4/account04/B05/b05-20260922t074314z-r35/`  
Candidate: `BT4-R4-DIRECT-3X3-CYCLE-FACTOR-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`; BT4 remains open.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Inputs actually consumed

- lead account02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, report blob `713053330313bf5906035c7bfd5841eb4e6b88ef`;
- assigned OTHER-account partner account01/B06 `BT4-X-DELETED-2X2-RANK-COLLAPSE-v1`, report blob `fdd394bc4a6b8f3ca851978c06219c5fe7563881`;
- account04/B06 `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`, report blob `ff7bbac3a8211262bc273f6fa02b102d3ace16dd`;
- newest compatible account03/B05 `BT4-SHORTEST-CROSS-PARITY-TRAP-v1`, report blob `89f2749e556f8e97966eefbc1418adea4cbd4172`.

## New proved step

In the exact four-remainder heavy-triangle cage

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with `p in A`, `p->h0`, and `q in B`, `q->h1`, any trimmed light-to-light connector with nonempty interior in `R` forces a connector whose interior meets `H`: if its last remainder vertex is `r_j`, route through the appropriate directed segment of `H` and `h_j->r_j`; if it is `x`, use `h0->r0->x` in the `A->B` direction or `h1->r1->x` in the reverse direction.

Hence, in the no-H-mediation branch, the three disjoint Menger paths in each ordered light-support direction supplied by 3-vertex-strongness are all **direct arcs**. The residual linkage object is therefore a direct `3 x 3` cross system, not arbitrary remainder paths.

If the six cross endpoints alternate on both light supports, let `pi_A,pi_B in S_3` be the unique support pairings giving three disjoint directed support intervals. The six direct cross arcs plus these intervals decompose into exactly the number of mixed cycles equal to the number of cycles of `pi_A^{-1} pi_B`. In particular, `pi_A=pi_B` yields three pairwise vertex-disjoint mixed directed cycles; together with `H`, this is the desired four-pack and is impossible in a counterexample.

For any compatible `2 x 2` sublinkage in this no-mediation exact cage, all four connectors are direct, so the assigned partner's tax sharpens from `G_A+G_B<=L_X<=7` to `G_A+G_B<=4`; in the four-distinct-port case it is forced to exact equality `G_A+G_B=4`.

## Necessary negative control

Direct rank three alone does not force a legal two-cycle or three-cycle factor. Exact cyclic-order enumeration over 14,400 normalized distinct-port order pairs found 10,548 with no compatible `2 x 2`; the first is the fully grouped signature

`A: A1,A2,A3,D1,D2,D3`,
`B: B1,B2,B3,G1,G2,G3`.

A separate exact check also refutes the shortcut that a fresh source with two fresh targets automatically fixes a `2 x 2` parity mismatch by Hall selection: all 160 normalized extended placements tested retained an unresolved pure-order instance. These are local port-system countermodels only, not BT4 counterexamples.

## First unpaid implication

`BT4-R4-DIRECT-3X3-ORDER-FORCING-v1`: use exact-seven degree, global NO-SIX, chordlessness, shortest-mixed-cycle displacement inequalities and the fixed cage/fan arcs to force either

1. full alternation with `pi_A=pi_B` (immediate four-pack),
2. a productive endpoint collision,
3. same-support bypass,
4. H mediation,
5. SIX / bounded support,
6. strict lexicographic packing decrease or a cyclic exchanged remainder.

The next argument cannot rely on raw connector rank or independent random choice; the exact grouped-port countermodel shows that graph-specific degree/fan geometry is essential.

Canonical report blob: `ab5f354238ef330125494b0afa5c8e4799716534`.
