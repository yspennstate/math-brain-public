# BT4 proof attempt — fleet01/B06

Run: `20260922T080451Z-b06-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Fresh state consumed


The newest complete team dependency actually consumed is fleet04/B05 run `b05-20260922t074314z-r35`, handoff commit `5da7fbeac3f200fd228058be8662a8ccfad1bf00`, handoff blob `7b0ab787c77713fbc54cced778f236a0236468fe`. Its theorem is the direct-rank-three reduction: in the exact four-remainder heavy-triangle cage, excluding H-mediated connectors forces all three light-to-light Menger paths in each direction to be direct cross arcs. In the alternating-endpoint case these six arcs plus the three support intervals on each light cycle define permutations `pi_A,pi_B`; the all-cross decomposition has a number of mixed directed cycles equal to the number of cycles of `tau=pi_A^{-1}pi_B`. Identity `tau` gives three mixed cycles and hence, together with the packed heavy triangle `H`, four vertex-disjoint directed cycles. The live first debt in that handoff is `BT4-R4-DIRECT-3X3-ORDER-FORCING-v1`.

That handoff in turn pins the campaign-lead fleet02/B04 dependency `BT4-HANDOFF-fleet02-B04-20260922T0619Z.md`, blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`, and lead report blob `713053330313bf5906035c7bfd5841eb4e6b88ef`. The current fleet02/B04 run observed during this invocation had started but had not yet produced a later complete candidate, so no incomplete lead state was promoted.

A second OTHER-account dependency actually applied is fleet03/B04 `BT4-R4-RANK3-SHORT-MIXED-BYPASS-v1`, commit `20483023af7b8b798e6ee47d5a73269bedd42cee`, report blob `df8c2244fb4a13f5a6fd4ef9fac4bc334076a25a`. It confirms that the four-remainder cage should be attacked through genuine packed support rerouting and fresh-source crossings, not by a local connector-existence shortcut.

## Compact conditional end-to-end route

In a minimal BT4 counterexample, dispose of a digon by deleting its two vertices, applying the known k=3 threshold-five result in the remainder, and restoring the digon as the fourth cycle. In the oriented branch, use the established exact-seven, 3-vertex-strong, arc-dominated, globally minimum three-cycle packing with acyclic remainder. Existing campaign reductions route the unresolved exact-R4 heavy-triangle branch either to SIX / third-support mediation / a productive bypass / a cyclic exchanged remainder / an immediate fourth cycle, or to fleet04/B05's direct `3 x 3` light-support cross-port system. In the alternating-endpoint subcase, write `tau=pi_A^{-1}pi_B`. Identity closes immediately. The new lemma below eliminates every transposition. Thus the only surviving alternating direct-rank-three monodromy is a 3-cycle. Closing that sole monodromy class (or routing it to an accepted output) would remove the latest complete candidate's direct-3x3 order wall.

## New lemma — transposition monodromy is impossible in a globally minimum three-packing

### Statement (`BT4-R4-DIRECT3X3-NONTRANSPOSE-v1`)

Assume the fleet04/B05 direct-rank-three alternating-endpoint state. Let the three pairwise disjoint forward support intervals on `A` be `A_1,A_2,A_3` in cyclic order, and similarly let the three intervals on `B` be `B_1,B_2,B_3`. Every interval begins at an incoming cross port and ends at an outgoing cross port; the original support edge from the terminal port of one interval to the initial port of the next interval is not among the selected cross arcs. The six selected direct cross arcs and the six support intervals decompose according to the cycle structure of `tau=pi_A^{-1}pi_B`.

Then `tau` cannot be a transposition.

### Proof

Suppose `tau` is a transposition. The all-cross decomposition therefore consists of exactly two vertex-disjoint genuine directed mixed cycles, say `M` and `N`: one corresponds to the two-element orbit of `tau`, the other to the singleton orbit. Their union is exactly `A union B`; no packed vertex is lost or gained.

Consequently `(H,M,N)` is a three-cycle packing covering exactly the same vertices as the globally minimum packing `(H,A,B)`. Hence `(H,M,N)` is itself globally minimum.

A cycle occurring in a globally minimum three-cycle packing cannot have a directed chord. Indeed, if `C` is one of the three cycles and `u->v` is an arc between two vertices of `C` which is not the successor edge of `u` on `C`, then

`u -> v -> C[v,u]`

is a genuine directed cycle strictly shorter than `C`. Replacing `C` by this shorter cycle while keeping the other two disjoint packed cycles gives a strictly smaller three-cycle packing, contradicting global minimality. Thus every member of `(H,M,N)` is chordless.

Now inspect the two-element `tau`-orbit. It contains two of the three `A`-intervals. Among three intervals arranged cyclically on `A`, every two-element subset contains the endpoints of one original support-boundary edge: for some two orbit intervals `A_i,A_j`, the original directed successor edge `e_A` leaves the terminal outgoing cross port of `A_i` and enters the initial incoming cross port of `A_j` (indices cyclically relabeled if needed).

Both endpoints of `e_A` lie on the same mixed cycle `M`, because `A_i,A_j` belong to the same `tau`-orbit. But `e_A` is not the successor edge of its tail on `M`: the mixed cycle leaves that terminal port through its selected direct `A->B` cross arc. Therefore `e_A` is a directed chord of `M`, contradicting the chordlessness forced above.

Hence transposition monodromy is impossible. QED.

## Consequence: exact residual order wall

In the alternating direct `3 x 3` state there are now only three permutation types:

- `tau = id`: three mixed directed cycles, so together with `H` there are four vertex-disjoint directed cycles — closed;
- `tau` a transposition: impossible by the new lemma;
- `tau` a 3-cycle: the sole surviving order type.

Thus the 3x3 order problem is reduced from arbitrary port-order compatibility to the two inverse 3-cycle monodromies.

There is also a useful structural description of this final class. When `tau` is a 3-cycle, the all-cross decomposition is one mixed cycle `K` containing all vertices of `A union B`. Every original boundary edge between consecutive support intervals of `A` or `B` is then an unused directed chord of `K`. A single such chord cannot by itself contradict three-packing minimality because `(H,K)` contains only two cycles. However, if two of these boundary chords yield vertex-disjoint shortcut cycles whose union omits any vertex of `K`, then those two shortcut cycles together with `H` form a strictly smaller three-cycle packing. Therefore any two disjoint shortcut cycles generated by the six support-boundary chords must partition all of `K` exactly. This is the next exact rerouting constraint; it converts the residual order problem into a six-chord circular-intersection/equality problem rather than another Menger-existence problem.

## First unpaid implication

`BT4-R4-DIRECT3X3-3CYCLE-CLOSE-v1`: in the sole surviving `tau`-3-cycle monodromy, combine the six unused support-boundary chords of `K`, exact-seven/global-NO-SIX fan data from the four-vertex remainder, and the fresh-source-cross/bypass mechanism from fleet03/B04 to force one of:

1. two vertex-disjoint shortcut cycles in `K` with a strict packing decrease;
2. a neutral two-cycle refactorization with cyclic exchanged remainder;
3. third-support mediation / same-support bypass;
4. SIX;
5. four vertex-disjoint genuinely directed cycles.

No edge-disjoint substitute is used. This report does not claim BT4 proved.

## Provenance / safeguards

No authenticated brain retrieval/context was used; execution remains `WITHOUT_VERIFIED_BRAIN`. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, e-mail, Drive, public posting, paid/remote compute, workflows, permission changes, or protected-control mutations were used.
