# POS3 account01/B10 — canonical earliest barrier has a two-out / at-most-one-in exact flux fork

**Run:** `20260922T095221Z-b10-pos3-r14`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below refer to the original uniform distribution on all full linear extensions of the original poset. No chain-deletion or projected law is treated as uniform.

## 1. Exact state consumed

The latest complete campaign-lead result used here is **account04/B10**

`proofnet24/collective-POS3/account04/B10/20260922T091028Z-account04-B10-pos3-r11/REPORT.md`

(blob `8a856fa924002567c01a8b70880003fe53b86da3`). It chooses the canonical earliest-ending strong incomparable pair `(p,q)`: `q` has minimum strong-order rank among right endpoints of incomparable pairs and, for that `q`, `p` has minimum rank among incomparable left endpoints. It proves `D(p,q)=emptyset`, forces the first outgoing exact transposition export into either a strict subspan or a heavy bridge, and proves that the first such heavy bridge cannot be span-exhausted. Its remaining statement is `POS3-EARLIEST-BARRIER-DESCENT-SPLICE-v1`.

The required named OTHER-account partner result used here is **account02/B11 r18**

`proofnet24/collective-POS3/account02/B11/20260922T075311Z-b11-pos3-r18-aa069b32/REPORT.md`.

It proves that, in a cardinality-minimal counterexample, an incomparability cut vertex cannot hide an arbitrarily long ordinal corridor after strict span descent has been exhausted: only a two-boundary interface or a two-boundary-plus-one-leaf interface can remain. Thus a later recycling argument need only treat those interfaces or a 2-connected incomparability block.

I also use account02/B10's exact full-law transposition identity and Hasse localization,

`proofnet24/collective-POS3/account02/B10/20260922T075033Z-b10-pos3-r11/REPORT.md`,

and this slot's exact three-chain TP2 flux theorem,

`proofnet24/collective-POS3/account01/B10/20260922T024151Z-b10-pos3-r11b/REPORT.md`.

## 2. Compact conditional route

Assume for contradiction that `P` is a finite width-at-most-three poset with no balanced pair. The strong-majority orientation `prec_*` is then a strict total order extending the poset order. Choose the campaign lead's canonical earliest-ending incomparable pair

`p || q`, `p prec_* q`.

The lead already shows that an immediate Hasse export either gives a strict strong-order subspan or enters its heavy-bridge state. The missing global issue is whether repeated descents/exports can migrate away and eventually recycle to the original earliest barrier.

The new result below shows that the barrier itself is far more rigid than a generic four-channel state. If no immediate `q`-terminal strict subspan is available, then:

1. `p,q` are consecutive in the strong-majority order;
2. they have exactly the same strict predecessor ideal;
3. the lower outgoing and lower incoming Hasse-defect families both vanish;
4. the union of the remaining outgoing and incoming Hasse families is one antichain;
5. width three and the exact transposition identity force **exactly two outgoing upper Hasse witnesses and at most one incoming upper witness**.

So the earliest barrier is a canonical width-saturating `2-out / <=1-in` fork, not the generic `(2,2)` four-channel configuration.

## 3. The strong-order prefix before the earliest endpoint is a chain

Let `rho` denote rank in `prec_*`.

### Lemma 3.1 — prefix-chain lemma

The set

`Q^-={v: rho(v)<rho(q)}`

is a chain in `P`.

**Proof.** If `u,v in Q^-` were incomparable, orient them by the total order, say `u prec_* v`. Then `(u,v)` would be an incomparable pair whose later endpoint `v` satisfies `rho(v)<rho(q)`, contradicting the defining minimality of `q`. Hence every two elements of `Q^-` are comparable in `P`. `square`

This is a purely structural consequence of the canonical earliest endpoint; it does not use any deletion law.

### Lemma 3.2 — either immediate `q`-terminal descent, or adjacency and equal predecessor ideals

If some `s` satisfies

`p prec_* s prec_* q`,

then `(s,q)` is an incomparable strict subspan of `(p,q)`. Consequently, after excluding this already-authorized immediate descent, `p` and `q` are consecutive in `prec_*` and

`Pred(p)=Pred(q)`.                                             (3.1)

**Proof.** By Lemma 3.1, `p` and `s` are comparable, and their strong-order order forces `p<s` in `P`. If `s<q`, then transitivity gives `p<q`, impossible; `q<s` contradicts `s prec_* q`. Thus `s||q`, giving the strict subspan.

Now assume no such `s`. If `z<p`, then `rho(z)<rho(p)`. By the leftmost choice of `p` among vertices incomparable with `q`, `z` cannot be incomparable with `q`; since `z prec_*q`, it follows that `z<q`. Hence `Pred(p) subseteq Pred(q)`. Conversely, if `z<q`, then `rho(z)<rho(q)`. Because `p,q` are consecutive and `z!=p`, one has `rho(z)<rho(p)`; Lemma 3.1 gives `z<p`. Thus `Pred(q) subseteq Pred(p)`. `square`

## 4. Exact outgoing/incoming Hasse families at the canonical barrier

For the pair `(p,q)` define

`U={r: p lessdot r, r||q}`,

`D={r: r lessdot q, r||p}`,

and for the reverse-direction defective swaps define

`L={s: s lessdot p, s||q}`,

`V={s: q lessdot s, s||p}`.                                  (4.1)

The lead has already proved `D=emptyset`. The canonical leftmost choice gives the matching incoming fact.

### Lemma 4.1 — `L=emptyset`

If `s lessdot p`, then `rho(s)<rho(p)<rho(q)`. Were `s||q`, the pair `(s,q)` would have the same earliest right endpoint `q` but a left endpoint earlier than `p`, contradicting the definition of `p`. Thus `L=emptyset`. `square`

Let `O` be the set of `p<q` extensions for which exchanging the positions of `p,q` is illegal, and `I` the corresponding illegal-swap set among `q<p` extensions. The account02/B10 exact involution gives, with `E=e(P)` and `M=N(p<q)`, 

`|O|-|I| = 2M-E > E/3`.                                      (4.2)

Because `D=L=emptyset`, Hasse localization is exact here:

`O = union_(r in U) {L: r<q in L}`,                            (4.3)

`I = union_(s in V) {L: s<p in L}`.                            (4.4)

Indeed `p<r` is forced for `r in U`, so such an `r` lies between the swapped endpoints exactly when `r<q`; conversely every outgoing illegality has a Hasse witness in `U union D=U`. The incoming statement is the order-dual argument using `L union V=V`.

## 5. Width three couples the outgoing and incoming channel counts

### Lemma 5.1 — `U union V` is an antichain

Distinct elements of `U` are incomparable because they are distinct covers of `p`; a comparison between them would put one strictly between `p` and the other. Distinct elements of `V` are likewise incomparable because they are distinct elements covering `q`.

Now take `r in U`, `s in V`. If `r<s`, then `p<r<s`, contradicting `s||p`. If `s<r`, then `q<s<r`, contradicting `r||q`. Hence `r||s`.

Therefore `U union V` is an antichain. Since `width(P)<=3`,

`|U|+|V| <= 3`.                                               (5.1)

This improves the generic separate bounds `|U|<=2`, `|V|<=2`: at the canonical barrier the two sides share one common width budget.

## 6. New theorem: the no-descent canonical state is exactly two-out / at-most-one-in

### Theorem 6.1 — canonical fork normal form

Assume no balanced pair and suppose the canonical earliest pair `(p,q)` has no immediate strict `q`-terminal subspan. Then

`|U|=2`, `|V|<=1`.                                             (6.1)

Moreover, writing `U={r_1,r_2}`, one has

`{q,r_1,r_2}` is a three-element antichain,                    (6.2)

`p prec_* q prec_* r_i` for `i=1,2`,                           (6.3)

and

`Pred(p)=Pred(q)`.                                             (6.4)

**Proof.** Equations (6.2) and (6.4) follow from the definitions, Lemma 5.1 and Lemma 3.2 once `|U|=2` is established.

For any `r in U`, if `r prec_* q`, then `p<r` in the poset gives

`p prec_* r prec_* q`,

and `(r,q)` is an immediate strict subspan, contrary to hypothesis. Hence `q prec_* r`. Since there is no balanced pair and `q||r`,

`Pr(r<q)<1/3`.                                                (6.5)

By (4.2), `|O|>E/3`, so `U` is nonempty. If `|U|=1`, say `U={r}`, then (4.3) and (6.5) give

`|O|/E = Pr(r<q)<1/3`,

contradicting `|O|>E/3`. Therefore `|U|>=2`. The generic width-three cover argument gives `|U|<=2`, so `|U|=2`. Finally (5.1) yields `|V|<=1`. `square`

This theorem is arbitrary-size and exact. It rules out the generic four-channel `(2,2)` local recycler at the first global incomparable endpoint.

## 7. Exact three-chain interpretation

Take any partition of `P` into at most three chains and add empty chains if necessary. Since `{q,r_1,r_2}` is a three-element antichain, these three vertices occupy three distinct chains in every three-chain cover. Because `p||q`, the vertex `p` cannot lie on `q`'s chain, so it lies on the chain containing one of `r_1,r_2`; relabel so this is `r_1`. Since `p lessdot r_1`, they are consecutive on that chain.

Let that chain be `C_b` and suppose `p=b_s`, `r_1=b_{s+1}`. For the exact full-extension flux of `x=q`,

`S=number of C_b-elements preceding q`,

the row atom `S=s` is exactly the heavy-bridge event

`p<q<r_1`.                                                     (7.1)

The two tails are

`S<=s-1  iff  q<p`,

`S>=s+1  iff  r_1<q`.                                         (7.2)

(The equality of predecessor ideals from (6.4) forces every earlier element of `C_b` below `q`.) Hence, under the actual uniform full-extension law,

`Pr(S<=s-1)<1/3`, `Pr(S>=s+1)<1/3`,                           (7.3)

while

`Pr(S=s) = Pr(p<q<r_1)
         = Pr(p<q)+Pr(q<r_1)-1
         > 1/3`.                                               (7.4)

Thus the campaign's earliest barrier has a **canonical exact heavy flux row with both tails below one third**, not merely an arbitrary heavy slice. This row sits inside the previously proved TP2 two-dimensional flux matrix `W_q(s,t)`. The missing difficulty is therefore not local sign or multiplicity: it is transport of this canonical heavy row when the proof leaves the earliest barrier and changes its active endpoint/ray.

## 8. Applying account02/B11's articulation reduction

The designated partner theorem now removes one entire way a future reset could hide. After strict span descent is exhausted, a cut vertex of the incomparability graph has only a two-boundary interface or a two-boundary-plus-one-leaf interface; an arbitrary multi-level ordinal corridor is impossible.

Combining that with Theorem 6.1 gives the following narrowed first unpaid implication:

> **`POS3-EARLIEST-2OUT-ONEIN-SPLICE-v1`.** Starting from the canonical earliest pair, either take an immediate `q`-terminal strict subspan, or enter the exact equal-predecessor `|U|=2, |V|<=1` fork of Theorem 6.1. Prove that after leaving this fork, a later sequence of Hasse exports cannot recreate the literal earliest barrier without first producing a balanced pair, a further well-founded span descent, or a proper autonomous/ordinal reduction. By account02/B11 r18, an articulation-mediated reset need only be treated through the two-boundary or one-leaf interface; otherwise the attempted reset occurs inside a 2-connected incomparability block.

This is strictly narrower than the lead's preceding generic earliest-barrier descent-splice problem: the initial barrier has a shared width budget of three, a canonical `2-out / <=1-in` shape, equal predecessor ideals, and an exact heavy row in every three-chain cover.

I do **not** prove the remaining 2-connected / residual-interface splice here. POS3 remains open.

## 9. Status

- campaign lead account04/B10 latest complete earliest-barrier theorem: **CONSUMED/APPLIED**;
- designated OTHER-account partner account02/B11 r18 articulation-corridor reduction: **CONSUMED/APPLIED**;
- account02/B10 full-law transposition/Hasse localization: **CONSUMED/APPLIED**;
- strong-order prefix before the earliest incomparable endpoint is a poset chain: **PROVED**;
- no immediate `q`-terminal descent implies strong-order adjacency and `Pred(p)=Pred(q)`: **PROVED**;
- incoming lower Hasse family `L=emptyset`: **PROVED**;
- `U union V` is an antichain and `|U|+|V|<=3`: **PROVED**;
- canonical no-descent state `|U|=2, |V|<=1`: **PROVED**;
- canonical exact three-chain heavy row with both tails `<1/3`: **PROVED**;
- `POS3-EARLIEST-2OUT-ONEIN-SPLICE-v1`: **OPEN**;
- parent POS3 target: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No computation was needed for the proof. Scoped provenance/privacy review: only the named private mathematical repositories, exact peer reports, sanitized logical run labels and mathematical formulas were used. No benchmark gold or sealed answers, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid model/API/Codex execution, remote workflow, permission bypass, public posting, notification enabling, or production-brain mutation was used or claimed.