# Addendum — domination slides source ports and collapses the clean order wall

Parent addendum: `BT4-P3-KSIDE-MENGER-v1`  
Candidate: `BT4-DOMINATION-SOURCE-SLIDE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Purpose

The previous addendum reduced the long-support clean branch to K-side connectors

`P*: c -> ... -> e` (`A->B`),
`Q*: f -> ... -> d` (`B->A`),

with `c,d` on the used segment `A[a3,p]`. In the distinct-port / no-internal-intersection residual, the old connectors

`F0: p -> x -> b`,
`G0: q -> a3`

yield two legal mixed replacement cycles when

- `c` occurs before `d` on `A[a3,p]`, and
- the cyclic `B` order is `b,f,e,q`.

This addendum directly attacks failures of those order conditions using the inherited arc-domination property and chordlessness of the packed cycles.

## 2. Source-slide lemma

### Statement

Let `T` be a chordless packed directed cycle and let

`P: c -> t -> ... -> y`

be a directed connector whose source is `c in T`, whose remaining packed endpoint is off `T`, and whose internal vertices (if any) lie in the old acyclic remainder `R`. Here `t` is simply the next vertex of `P`; it may already be the other packed endpoint when `P` is direct.

Dominate the first arc `c->t`. Then one of the following occurs:

1. **one-step source slide:** the dominator is `c^- in T`, and `c^- -> t -> ... -> y` is a connector with exactly the same tail and remainder interior;
2. **packed cross / H exit:** the dominator is packed off `T`, giving a direct packed-to-packed cross into `c` (with an `H` source counted as explicit third-support mediation);
3. **remainder lift:** the dominator lies in `R`; repeated domination of the resulting arc into `c`, using acyclicity of `R`, reaches a packed apex and yields either a distinct-port same-support `T`-bypass, a packed cross / `H` mediation, or a one-support replacement cycle forcing `|T|<=|R|+1`.

### Proof

Let `z` dominate `c->t`, so `z->c,t`.

If `z in T`, then `z->c` is an arc with both endpoints on the chordless directed cycle `T`. Hence `z=c^-`. The additional arc `z->t` gives the same connector tail beginning one support vertex earlier, proving (1).

If `z` is packed but not on `T`, the arc `z->c` is already a cross into `T`; if `z` is on the heavy support this is explicit third-support mediation. This is (2).

Suppose `z in R`. Use arc domination on `z->c`. If its dominator is again in `R`, continue dominating the new remainder-to-`c` arc. The resulting backwards chain inside `R` cannot repeat because each step gives a directed edge from the new remainder vertex to the previous one, and a repetition would create a directed cycle in `D[R]`. Since `R` is finite and acyclic, the chain reaches a packed apex `s`, producing

`s -> ... -> z -> c`

with all internal vertices in `R`.

If `s` is packed off `T`, this is a cross / `H`-mediation output. If `s in T` and `s!=c`, it is a genuine same-support bypass with the standard minimum-packing distance tax. If `s=c`, the path closes to a directed cycle meeting the old packing only at `c` and using at most all vertices of `R`; replacing `T` by that cycle gives `|T|<=|R|+1`. This proves (3). QED.

The lemma is entirely local and uses the inherited arc-domination and chordlessness hypotheses, not an average degree surrogate.

## 3. Collapse of the bad A-port order

Return to the clean heavy-triangle state. Assume the all-long branch and exclude, only for the purpose of identifying the irreducible residual, the outputs already listed in the source-slide lemma and packed endpoint collisions.

Suppose the K-side connectors satisfy the **bad** `A` order: traversing `A[a3,p]`, the reverse target `d` occurs before the forward source `c`.

Apply the source-slide lemma to the first arc of `P*`. In the residual under consideration only alternative (1) may occur, so the source of `P*` moves from `c` to `c^-` with the same connector tail. Repeat.

Moving by predecessors walks backward along `A[a3,p]` from `c` toward `d`. Before the source can pass from the `d`-after region to the `d`-before region, it must equal `d`. Thus repetition forces a packed endpoint collision at `d`, unless an earlier iteration emits a cross, `H` mediation, bypass, or bounded-short-support output.

Therefore, in the clean distinct-port / no-output residual, the bad order `d before c` is impossible. One may assume

`c before d on A[a3,p]`.

This pays the `A`-side nonalternation wall for the K-side quartet.

## 4. Collapse of the movable B-source order

Now the `A` support forces the transposed pairing

`F0 with Q*`, `P* with G0`.

For this pairing to be disjoint on `B`, the required cyclic order is

`b, f, e, q`.

Assume first that the forward target `e` lies on the open directed segment `B(b,q)`.

If `f` does not lie on `B(b,e)`, apply the source-slide lemma on support `B` to the first arc of `Q*` and repeatedly move its source backward while no structural exit occurs.

- If `f` starts on `B(e,q)`, predecessor sliding reaches `e` before it can enter `B(b,e)`, producing the packed endpoint collision `f=e`.
- If `f` starts on the complementary segment `B[q,b]`, predecessor sliding reaches `q` (or an old boundary collision) before it can enter `B(b,e)`.

Hence, after excluding endpoint collisions and the lemma's cross/bypass/`H`/short-support outputs, the only surviving possibility with `e in B(b,q)` is exactly

`f in B(b,e)`,

which gives cyclic order `b,f,e,q` and therefore the legal two-cycle reconstruction

`Z0 = F0 + B[b,f] + Q* + A[d,p]`,

`Z1 = P* + B[e,q] + G0 + A[a3,c]`.

The existing minimum-packing tax then applies to `Z0,Z1`.

## 5. New exact irreducible port wall

Sections 3--4 show that in the all-long, no-bypass, no-`H`-mediation, distinct-packed-port residual, the generic two-support cyclic-order debt collapses to a single target-location obstruction:

`e in B(q,b)`.

That is, the K-side `A->B` connector `P*` forced by the `p+++` short-gap Menger argument must land on the **complementary B arc** rather than the old mixed-cycle trace `B[b,q]`; otherwise source sliding forces the compatible two-cycle splice or an earlier structural exit.

Call this surviving wall

`BT4-KSIDE-WRONG-B-TARGET-v1`.

This is strictly narrower than `BT4-RANK2-PORT-ORDER-SPLICE-v1`: connector rank, remainder intersection, the A-side order, and the movable B-source order are all paid. Only the forward connector's B target location is not movable by source domination.

## 6. Next implication

Directly attack `BT4-KSIDE-WRONG-B-TARGET-v1`:

> In the aligned four-remainder heavy-triangle long-support state, use the other members of the three-path `A->B` Menger linkage, exact-seven fan/arc-domination constraints, and the two sink-fan targets on `B` to prove that some K-side forward connector lands on `B(b,q)`; or else force packed endpoint collision, an opposite-intersection bypass, third-support mediation, SIX, or a bounded support.

Averages do not enter. No claim is made that the wrong-target wall is already impossible.

Global SIX/H5, bounded F2/F3, and seven-remainder support-carried debts remain separate. BT4 remains open.

No authenticated brain use, computation, scheduler mutation, or prohibited external action occurred.
