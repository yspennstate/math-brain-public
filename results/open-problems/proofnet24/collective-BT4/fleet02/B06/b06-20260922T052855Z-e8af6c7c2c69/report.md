# BT4 fleet02/B06 — arc-maximal heavy-triangle slide and clean mixed witness

Run: `b06-20260922T052855Z-e8af6c7c2c69`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-ARCMAX-TRANSITIVE-SLIDE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Local false candidate: `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Scope and exact sources consumed

The exact target is the genuine `k=4` Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed, so a digon is a directed cycle.


Latest complete campaign-lead version actually consumed: fleet02/B04 run `20260922T041847Z-b04-bt4-r11`, primary scientific commit `71ff185ec9b372cc24c02c4630cd7c202d13eee7`, blob `596929efe56393d3ab515544fa33ec6a19e75c83`, with controlling strengthening commit `1277bd8435045651114cb6500f47674603f3f522`, blob `8bfc5b33fb232c8543856d6d9ad3b0e8fdc3432c`. The lead's exact-two-predecessor heavy-triangle cage and exact five-witness conclusions are used below.

Named OTHER-account partner actually consumed and applied: fleet03/B04 `BT4-R4-F3-TWOFAN-COLLAPSE-v1`, run `20260922T035106Z-fleet03-B04-bt4-r11`, current report blob `47230bd4d097b62aa8acdb74f4d0f747b3a0fe2d`. I use its source-valid minimum-packing inport localization lemma: if a remainder vertex `q` has an inport `t->q` from a packed cycle `T`, then all `q`-targets on `T` lie in `{t+,t++}`. In particular a remainder witness with at least three outneighbors on `T` cannot receive any arc from `T`.

Compatible OTHER-account mechanism also applied: fleet01/B04 `BT4-R4-MAX-REMAINDER-ARC-COLLAPSE-v1`, run `20260922T044536Z-b04-bt4-r11`, report blob `b9b700749e5723c819b6643aa16c67c38db6c569`. It legitimizes the lexicographic choice: among globally minimum-total three-cycle packings, maximize the number `Phi(P)` of arcs induced by the acyclic remainder. Every size-neutral pivot then satisfies `Phi(P')<=Phi(P)`.

No peer outcome label is used as proof.

## Compact conditional end-to-end route

After the current team reductions, a complete proof would follow from the following remaining closures.

1. Delete a digon if one exists. The survivor has minimum outdegree at least five, so the genuine `k=3` theorem gives three disjoint cycles; restoring the digon gives the fourth. Hence a counterexample may be assumed oriented.
2. Enter the inherited exact-outdegree-seven, 3-vertex-strong, arc-dominated minimum-counterexample normal form with a globally minimum-total packing `(H,S,U)` and nonempty acyclic remainder `R`.
3. Subject to minimum total packed order, maximize `Phi(P)=|A(D[R])|`.
4. Use the pair-deletion `SIX/NO-SIX` system. In the four-remainder NO-SIX heavy-triangle branch, use the lead's predecessor-splice theorem.
5. The theorem below shows that the lead's exact-two-predecessor cage cannot remain an arbitrary neutral-equality state. It collapses either to the existing cycle-supported same-heavy five-witness interface or to one sharply specified **transitive-slide / mixed-clean-witness** state.
6. In that exceptional state the old and exchanged four-vertex remainders are both transitive tournaments, the exchanged sink regenerates the exact `(3,2,2)` heavy-triangle profile, and a remainder-supported exact-five witness shares a heavy light target with a cycle-supported exact-five witness while receiving no inarc from that target.
7. The first unpaid implication is therefore to splice this mixed clean pair, or to prove that applying the heavy-triangle saturation theorem to the regenerated transitive state cannot yield another equal-`Phi` slide. The separate SIX/common-port closures remain independent obligations.

This is not a full proof candidate.

## Inherited exact-two-predecessor cage

Use the lead's notation. The heavy cycle is the directed triangle

`H = h0 -> h1 -> h2 -> h0`

and the four-vertex remainder is

`R = {x,r0,r1,r2}`.

For `i=0,1,2`, the saturation triangles are

`Ti = hi -> ri -> x -> hi`.

In the exact-two-predecessor branch, rotate indices so the missing predecessor relation belongs to `T0`. Then

`r0 -> r1, h1, x`,  
`r1 -> r2, h2, x`,

and the lead proves the exact residual neighborhoods in

`G = D[V(H) union R]`:

`N_G^+(h1) = {h2,r1}`,  
`N_G^+(h2) = {h0,r2}`,  
`N_G^+(r2) = {x,h0}`.                                      (1)

Thus `h1,h2,r2` each send exactly five arcs into `S union U`. The first two are cycle-supported exact five-witnesses; `r2` is a remainder-supported exact five-witness.

The old remainder contains

`r0->r1`, `r1->r2`, and `ri->x` for all `i`.                 (2)

Acyclicity forbids `r2->r0`. Therefore the only undecided unordered pair of the old remainder is `{r0,r2}`. Put

`epsilon = 1` if `r0->r2`, and `epsilon = 0` if `r0,r2` are nonadjacent.

Then

`Phi(P) = 5 + epsilon`.                                       (3)

## The neutral `T2` pivot

Replace the heavy triangle `H` by the equal-size triangle

`T2 = h2 -> r2 -> x -> h2`.

The new remainder is

`R2 = {h0,r0,h1,r1}`.

Five of its six unordered pairs have forced orientations:

`h0->r0`, `r0->h1`, `h1->r1`, `h0->h1`, `r0->r1`.           (4)

The only undecided pair is `{h0,r1}`.

If `r1->h0`, then (4) gives the directed four-cycle

`h0 -> r0 -> h1 -> r1 -> h0`

inside the exchanged remainder. Together with `T2,S,U` this is already a four-pack. Hence a counterexample cannot have `r1->h0`.

If `h0->r1`, then the exchanged remainder has all six possible arcs and

`Phi(P2)=6`.

If the pair is nonadjacent, then

`Phi(P2)=5`.

Because `P` was chosen to maximize `Phi` among globally minimum-total packings, the neutral pivot satisfies

`Phi(P2) <= Phi(P)`.                                         (5)

Equations (3)--(5) give the exact case split.

### Case A: `epsilon=0`

Then `Phi(P)=5`. The orientation `h0->r1` would give `Phi(P2)=6`, contradicting (5); the opposite orientation was just shown to make the exchanged remainder cyclic. Therefore `h0,r1` are nonadjacent.

All other possible `G`-outneighbors of `h0` are already oriented toward `h0`: `h2->h0`, `r2->h0`, `x->h0`; and the displayed cage has `h0->h1,r0`. Consequently

`N_G^+(h0)={h1,r0}`.

Exact outdegree seven therefore makes `h0` a third cycle-supported exact five-witness into `S union U`.

### Case B: `epsilon=1`

Now the old remainder is the complete transitive tournament

`r0 -> r1 -> r2 -> x`,                                      (6)

so `Phi(P)=6`.

If `h0,r1` are nonadjacent, the same argument as Case A makes `h0` a third exact five-witness.

If `r1->h0`, the exchanged remainder is cyclic and BT4 closes.

The sole unresolved equality case is therefore

`h0->r1`.                                                     (7)

Then the new remainder is also a complete transitive tournament, with order

`h0 -> r0 -> h1 -> r1`.                                      (8)

This is the **transitive slide**.

## Theorem — BT4-HT-ARCMAX-TRANSITIVE-SLIDE-v1

Choose the inherited globally minimum-total three-cycle packing lexicographically to maximize the number of arcs in its acyclic remainder. In the lead's exact-two-predecessor four-remainder heavy-triangle cage, at least one of the following occurs.

1. **Fourth-cycle exit:** the `T2` pivot makes the exchanged remainder cyclic.
2. **Cycle-supported same-heavy output:** `h0,h1,h2` are all exact five-witnesses into `S union U`. Hence each is heavy on `S` or `U`, and by pigeonhole two are heavy on the same light cycle.
3. **Transitive-slide / mixed-clean output:** both the old and `T2`-exchanged remainders are transitive tournaments as in (6),(8). The vertices `h1,h2,r2` are exact five-witnesses into `S union U`. If `h1,h2` share a heavy light target, output 2 already occurs. Otherwise their heavy targets are different, and the remainder witness `r2` shares a heavy target `A in {S,U}` with one of them. Moreover

`A not-> r2`.                                                 (9)

### Proof of the clean-inport conclusion

By (1), `r2` has exactly five outneighbors in `S union U`; hence some `A in {S,U}` receives at least three of them.

Suppose `t->r2` for some `t in A`. Apply the named fleet03/B04 inport-localization lemma to the current globally minimum packing, the remainder vertex `r2`, and packed cycle `A`. It says every `r2`-target on `A` lies among the two successors `{t+,t++}`. But `r2` has at least three distinct targets on `A`, contradiction. Thus no vertex of `A` points to `r2`, proving (9).

If `h1,h2` have different heavy targets, the heavy target of `r2` must equal one of those two targets, so the mixed same-heavy pair follows.

QED.

## A useful regeneration fact in the exceptional slide

The transitive slide is not merely an arbitrary equality case. Relative to the new packing `(T2,S,U)`, the new remainder sink is `r1`.

The old cage gives

`r1 -> h2`, `r1 -> r2`, `r1 -> x`.

These are exactly the three vertices of `T2`. Every other old `G`-vertex points toward `r1` in the slide. Hence `r1` has exactly three outneighbors on the new heavy triangle `T2` and four on `S union U`.

If global NO-SIX persists, the two light fans must each have size at least two, and hence exactly two. Thus the new sink profile is again

`(3,2,2)`,

heavy on the triangle `T2`. Orientation also gives

`T2 not-> r1`.

Therefore the exceptional equality state **regenerates the canonical heavy-triangle sink profile after one equal-`Phi` neutral slide**. The next proof step should compare the saturation/predecessor structure forced at this regenerated state with the transitive order (8), rather than treating the slide as generic neutral noise.

## Exact local adversary: equality of the potential does not itself close the branch

The tempting stronger statement

> `BT4-HT-ARCMAX-EQUALITY-v0`: the aligned exact-two-predecessor geometry cannot have both the old and `T2`-exchanged remainders transitive with the same maximum arc count.

is false as a purely local inference.

The deterministic checker archives a 16-vertex oriented 7-outregular digraph with 112 arcs. It remains strongly connected after deletion of any at most two vertices, every arc has a common in-neighbor in the inherited domination sense, and the chosen cycles

`H=(h0,h1,h2)`,  
`S=(s0,s1,s2,s3)`,  
`U=(u0,u1,u2,u3,u4)`

are pairwise disjoint chordless directed cycles.

It realizes the exact aligned cage, with both

`R=(r0,r1,r2,x)`

and the `T2`-exchanged remainder

`R2=(h0,r0,h1,r1)`

being complete transitive tournaments with six induced arcs. It also realizes a clean remainder witness: `r2` has five light-support outneighbors, four on `S`, and no vertex of `S` points to `r2`.

This graph is deliberately **not** a BT4 counterexample and the chosen packing is not claimed globally minimum. The checker exhibits the explicit four-pack

`(h0,h1,h2)`,  
`(r0,r1,u0)`,  
`(r2,s0,u2)`,  
`(s1,x,u3)`.

Its role is exact: it proves that degree seven, orientation, 3-vertex-strongness, chordless chosen supports, arc domination, the aligned predecessor cage, and equality `Phi=6` before and after the neutral pivot do not by themselves contradict one another. The global no-four-pack/minimum-packing machinery is genuinely needed to eliminate the transitive slide.

## Digon boundary with a highly asymmetric degree pattern

A second exact adversary keeps the digon reduction honest.

Take ten vertices `{a,b,d0,...,d7}`. Include every ordered arc between distinct vertices except the two arcs

`d0->d6`, `d0->d7`.

Then

- `a<->b` is a digon;
- `d^+(d0)=7`;
- every other vertex has outdegree `9`.

Thus the degree vector is highly asymmetric: one vertex has degree seven and the other nine vertices have degree nine.

Delete the digon vertices `a,b`. The surviving vertex `d0` has outdegree exactly five, while every other survivor has outdegree seven. Hence

`delta^+(D-{a,b}) = 5`.

This refutes any intermediate claim that digon deletion preserves minimum outdegree at least six in the original `delta^+>=7` problem. The valid reduction is exactly the sharp one: delete the digon, invoke the genuine `k=3` threshold-five theorem, then restore the digon as the fourth cycle.

## Exact computation and reproducibility

The checker was executed in this invocation and returned `PASS`.

- checker creation commit: `247f36840aab62973e201eb7c64311cbbf6bff93`
- checker Git blob after readback: `dd4dd484f8cec19f858587f5da2423524e3c9d04`
- checker byte SHA-256: `996455d97717f4055d2677ca87d1f09cd6b3ef3157035c3c32172d5333138dc7`
- output creation commit: `96dae5e6892a512f0cb9a3fff761d4459a23786c`
- output Git blob after readback: `dbdb84f1146acd969a3b31b1e1179407f9a7fb9d`
- output byte SHA-256: `cbf371e6a3ec1f68991af72fa3fa955730cea5ed6d5caf912a0b8c48c3b412ed`

The checker contains the complete adjacency list, verifies exact outdegree seven, orientation, all at-most-two-vertex deletion strong-connectivity tests, arc domination, chordlessness of the chosen supports, both six-arc transitive remainders, the exact terminal-witness fan, the explicit four-pack, the symbolic `Phi` case split, and the asymmetric digon threshold-five example.

## Honest boundary / first essential missing implication

The current reduction does **not** prove BT4.

The first essential missing implication is now the following tightly specified one.

> In the transitive-slide state (6)--(9), apply the heavy-triangle saturation theorem to the regenerated sink `r1` and new heavy triangle `T2`. Prove that the resulting predecessor/support structure either (i) creates two vertex-disjoint replacement cycles, (ii) decreases the globally minimum packing, (iii) creates a directed cycle in the exchanged remainder, (iv) enters the already-recognized cycle-supported same-heavy interface, or (v) forces a second equal-`Phi` slide whose transitive orders cannot be mutually compatible.

Equivalently, a proof must use the **global no-four-pack condition** to orient the equality orbit; the remainder-arc potential alone can plateau at six, as the exact local adversary demonstrates.

The mixed clean pair `{r2, hi}` on a common light target `A`, with `A not->r2`, is additional exploitable structure in that plateau state and should be combined with the lead's no-inport heavy-fan cross from the cycle-supported witness.

Separate obligations remain for the campaign's SIX/common-packed-port interfaces. No full proof or novelty claim is made.

## Privacy / execution boundary

Only scoped BT4 mathematics, control provenance, and exact research artifacts are recorded. No benchmark gold, sealed answers, credentials, scheduler identifiers, machine paths, unrelated private data, raw transcripts, email/Drive data, public posting, paid API/model/Codex substitution, remote workflow dispatch, or permission changes were used.
