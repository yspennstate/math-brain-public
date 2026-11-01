# POS3 fleet03/B10 — canonical-prefix elimination and an exact same-sign packet identity

**Run:** `20260922T094637Z-fleet03-B10-POS3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability below is under the uniform law on the original full linear-extension set unless explicitly described otherwise. No projected or deletion-induced distribution is called uniform.

## 1. Exact state consumed

The active fleet03/B10 assignment is to apply bounded-width/high-variance results to the exact width-three target and make the remaining exceptional case explicit. The assigned OTHER-account partner is fleet04/B11.

I consumed partner fleet04/B11 run

`proofnet24/collective-POS3/fleet04/B11/20260922T090813Z-B11-pos3-r18/REPORT.md`, blob `eb9eca5a9e57f81f33c052792f06678c19e93823`.

For a heavy Hasse bridge

`p lessdot r`, `q||p,r`, `p prec_* q prec_* r`,

it deletes the cover chain `C={p<r}` and classifies the first exit from a maximal stationary profile `[0,2]`. A lower half-profile exit `[0,1]` produces a sibling lower cover `s lessdot r`, `s!=p`, `p||s`, and proves that only `s<q` or `s||q` is possible. In the `s<q` branch, `q` is a relation distinguisher for the sibling pair `(p,s)`; after the one-distinguisher and opposite-sign-two-distinguisher cases are paid, the partner leaves exactly two same-sign distinguishers or at least three distinguishers. It names the missing step `POS3-SAME-SIGN-SIBLING-CHARGE-v1`.

I also consumed the newest complete lead state

`proofnet24/collective-POS3/fleet04/B10/20260922T091028Z-fleet04-B10-pos3-r11/REPORT.md`, blob `8a856fa924002567c01a8b70880003fe53b86da3`.

In a hypothetical no-balanced counterexample, the inherited strong-majority relation `prec_*` is a strict total order. The lead chooses a **canonical earliest-ending incomparable pair** `(p,q)`: first minimize the strong-order rank of the later endpoint `q` among all incomparable pairs, then minimize the rank of `p` among incomparable predecessors of `q`. It proves `D(p,q)=emptyset`, forces the first transposition export to a heavy bridge or strict span descent, and shows that the first heavy bridge cannot be span-exhausted. Its remaining issue is the global descent splice.

For the quantitative packet radius I use the already-proved fleet04/B11 bounded-variance tail from r17:

`Pr(x_j < x_i) < 2125440/(j-i+1)^2`                              (1.1)

for every incomparable pair `x_i prec_* x_j` in a hypothetical counterexample.

## 2. New canonical-prefix lemma

### Lemma 2.1 — everything strictly before the earliest endpoint is a poset chain

Let `(p,q)` be the lead's canonical earliest-ending pair. If `x prec_* q` and `y prec_* q`, then `x` and `y` are comparable in the poset.

**Proof.** If `x||y`, orient them by the total strong-majority order, say `x prec_* y`. Then `(x,y)` is an incomparable pair whose later endpoint `y` has strong-order rank strictly smaller than the rank of `q`, contradicting the defining minimality of `q`. `square`

Because `prec_*` agrees with the poset order on comparable elements, the entire strict prefix before `q` is literally a chain in `P`, not merely a chain in the majority order.

This tiny observation is global: it uses the earliest endpoint, not a local Hasse estimate.

## 3. Direct application to the assigned partner's first missing branch

Apply partner r18's lower half-profile exit to a heavy bridge anchored at the canonical earliest endpoint:

`p lessdot r`, `q||p,r`, `p prec_* q prec_* r`.

The partner produces `s lessdot r`, `s!=p`, `p||s`, and shows that either `s<q` or `s||q`.

### Theorem 3.1 — the partner's same-sign sibling branch cannot occur at the canonical earliest barrier

The alternative `s<q` is impossible.

**Proof.** The poset relation `s<q` implies `s prec_* q`. We also have `p prec_* q`. But `p||s`. Thus two incomparable elements lie strictly before `q`, contradicting Lemma 2.1. `square`

Therefore the first stationary lower-half exit at the canonical earliest barrier is forced into

`s||q`.

Moreover `s prec_* q` is impossible by the same lemma, so necessarily

`p prec_* q prec_* s`.

Hence `{p,q,s}` is a width-saturating three-antichain in a fixed coherent strong-order orientation. At this canonical barrier the partner's residual “exactly two same-sign distinguishers or at least three distinguishers” is not merely charged; its entire comparable sibling branch is absent.

The order-dual statement holds at a canonical latest-starting barrier.

## 4. Exact same-sign corridor identity for noncanonical branches

The canonical argument above does not eliminate same-sign sibling states that arise later after the anchor changes. The following full-law identity gives a quantitative packet in the exact-two case.

Let `a||b` and orient the pair by `a prec_* b`. Assume every relation distinguisher of `(a,b)` has the **positive** sign for the orientation `a<b`. Split them as

`L={l : l<b, l||a}`

and

`U={u : a<u, u||b}`.

There are no negative distinguishers. Define the exact safe-corridor event

`S={ every l in L occurs before a, and b occurs before every u in U }`.   (4.1)

### Lemma 4.1 — exact two-to-one corridor identity

For every finite poset,

`Pr(S)=2 Pr(b<a)`.                                                (4.2)

**Proof.** Every extension with `b<a` automatically lies in `S`: for `l in L`, `l<b<a`; for `u in U`, `b<a<u`.

Now take an extension in `S` with `a<b` and exchange the positions (equivalently the labels at those two positions) of `a,b`, leaving every other position fixed. Any vertex outside `L union U` has identical relation type to `a` and `b`: otherwise it would be a distinguisher. A vertex in `L` remains below the required endpoint because `S` puts it before the old position of `a`; a vertex in `U` remains above the required endpoint because `S` puts it after the old position of `b`. Thus the swap is valid and lands in `b<a`.

Conversely, swapping `a,b` in any `b<a` extension gives an `a<b` extension in `S`. The operation is involutive. Hence the two orientations inside `S` have equal cardinality, and all `b<a` extensions lie in `S`, proving (4.2). `square`

No deletion skeleton or induced measure appears in this argument.

## 5. Exact-two same-sign distinguishers always yield an actual packet

Assume now that `(a,b)` has **exactly two** distinguishers and both have the positive sign. Suppose also that no strict strong-majority subspan has already been accepted as an exit.

For every `l in L`, since `l<b` in the poset, `l prec_* b`. If `a prec_* l`, then

`a prec_* l prec_* b`

and `(a,l)` is an incomparable strict subspan of `(a,b)`. Therefore in the no-span branch

`l prec_* a`, so `Pr(l<a)>2/3`.                                  (5.1)

Dually, for every `u in U`, the relation `a<u` gives `a prec_* u`; if `u prec_* b`, then `(u,b)` is a strict subspan. Thus in the no-span branch

`b prec_* u`, so `Pr(b<u)>2/3`.                                  (5.2)

Because there are exactly two distinguishers total, the safe event `S` is the intersection of exactly two events of type (5.1)/(5.2) (or fewer distinct conditions if one is forced by another). By the union bound,

`Pr(S)>1/3`.                                                      (5.3)

Using the exact identity (4.2),

`Pr(b<a)>1/6`.                                                    (5.4)

### Theorem 5.1 — exact-two same-sign packet theorem

In a width-at-most-three no-balanced candidate, an incomparable pair with exactly two same-sign relation distinguishers has, before any accepted strict subspan exit,

`minority(a,b)>1/6`.                                             (5.5)

The same statement is order-dual. This is a literal full-extension packet, not a static relation witness.

The one-distinguisher version is even stronger: (4.2) and a single `>2/3` corridor condition would force `Pr(b<a)>1/3`, contradicting the assumed strong orientation, recovering why the one-distinguisher branch cannot survive.

## 6. Bounded-width/high-variance consequence: the new packet is local

Apply the assigned bounded-variance tail (1.1) to a pair with minority `>1/6`. If its strong-order index gap is `d`, then

`1/6 < 2125440/(d+1)^2`,

so

`(d+1)^2 < 12752640`.                                            (6.1)

Since

`3571^2=12752041 < 12752640 < 12759184=3572^2`,

we obtain the exact integer radius

`d<=3570`.                                                        (6.2)

Thus every exact-two same-sign residue that does not already descend becomes an actual packet edge of strong-order span at most **3570**. This is strictly stronger than leaving the relation distinguishers unweighted.

## 7. What remains in the >=3-distinguisher case

The identity (4.2) also exposes the exact obstruction to extending the `1/6` bound blindly.

For arbitrary all-positive distinguishers, it is enough in (4.1) to require only the maximal elements of `L` before `a` and the minimal elements of `U` after `b`. In width three,

`|Max(L)|<=2`, `|Min(U)|<=2`,                                  (7.1)

because `a` is incomparable with every member of `Max(L)` and `b` with every member of `Min(U)`.

In the no-span branch every one of these frontier conditions has probability `>2/3`. If the total frontier size is at most two, the same union-bound proof gives the packet `>1/6`. Therefore a genuinely unpaid all-positive branch must have at least **three** outward frontier conditions. By (7.1), one side then contains two incomparable extremal blockers; together with the opposite endpoint they form a width-saturating three-antichain.

So the surviving multi-distinguisher residue is not a featureless collection of witnesses. It is forced either into the already-live three-antichain Hasse-gate geometry or into a mixed-sign/more complicated branch not covered by Lemma 4.1's all-positive hypothesis.

This is consistent with the independently proved fleet03/B11 three-antichain chamber theorem, which exports two disjoint Hasse frontiers but does not yet establish global termination.

## 8. Updated missing implication

The partner's `POS3-SAME-SIGN-SIBLING-CHARGE-v1` is now split as follows.

1. **At the canonical earliest barrier:** the comparable sibling branch `s<q` is impossible, so the exit is necessarily the coherent three-antichain `p prec_* q prec_* s`.
2. **At a later/noncanonical exact-two same-sign sibling state:** either strict span descent occurs or the sibling pair itself carries actual minority mass `>1/6`, hence lies within strong-order radius `3570`.
3. **The remaining genuinely unpaid part:** a later state with at least three distinguishers, especially a mixed-sign configuration or an all-positive frontier of size at least three, must be spliced into the existing three-antichain / outward-Hasse mechanism without permitting intergeneration recycling.

A precise next target is therefore

> **`POS3-CANONICAL-ANTICHAIN-OR-MULTIFRONTIER-SPLICE-v1`.** Starting from the canonical earliest-ending pair, follow the forced coherent three-antichain exit and subsequent bounded packet descents. Prove that every later >=3-distinguisher multifrontier state yields a balanced pair, strict span descent, proper autonomous/ordinal reduction, or a strictly well-founded envelope change before any reset to the canonical barrier.

This is narrower than the previous generic same-sign sibling charge and narrower than a finite-kernel claim. No bound on `|P|` is asserted.

## 9. Status

- fresh collective owner control and exact fleet03/B10 assignment: **CONSUMED**;
- assigned other-account partner fleet04/B11 r18: **CONSUMED/APPLIED**;
- newest lead fleet04/B10 canonical earliest-ending reduction: **CONSUMED/APPLIED**;
- canonical strict-prefix-is-a-poset-chain lemma: **PROVED**;
- partner lower-half comparable sibling branch at canonical barrier: **ELIMINATED**;
- canonical lower-half exit forced to coherent width-three antichain: **PROVED**;
- exact same-sign safe-corridor identity `Pr(S)=2Pr(b<a)`: **PROVED**, arbitrary finite size;
- exact-two same-sign no-span packet `minority>1/6`: **PROVED**;
- bounded-variance radius `<=3570` for that packet: **PROVED**;
- >=3-distinguisher multifrontier / global intergeneration splice: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No finite census, surrogate-uniform law, benchmark material, credentials, scheduler identifier, machine path, unrelated private data/transcript, email/Drive data, paid model/API/Codex execution, public/remote workflow, permission change, or cross-account native action was used. No genuine authenticated brain retrieval/context use occurred, so the run remains `WITHOUT_VERIFIED_BRAIN`.
