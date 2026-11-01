# POS3 fleet04/B20 — canonical two-cover sibling switching forces descent

**Run:** `20260922T101243Z-B20-POS3-r11-ax7m`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and extension counts below are for the original uniform law on the full linear extensions of the original poset. No chain-deletion projection is renamed uniform.

## 1. Exact source-bound state consumed

The latest complete campaign-lead report consumed is:

- fleet04/B10 `20260922T091028Z-fleet04-B10-pos3-r11`,
  `proofnet24/collective-POS3/fleet04/B10/20260922T091028Z-fleet04-B10-pos3-r11/REPORT.md`,
  blob `8a856fa924002567c01a8b70880003fe53b86da3`.

It works in a hypothetical no-balanced width-at-most-three counterexample, where the strong-majority orientation `prec_*` is a strict total order extending the poset order. It chooses the least possible later endpoint `q`, then the leftmost `p||q`, proves the lower Hasse family at that endpoint is empty, and proves that the first canonical heavy bridge cannot be span-exhausted.

The required named OTHER-account result consumed and applied is:

- fleet01/B19 `20260922T094856Z-b19-pos3-r14`,
  `proofnet24/collective-POS3/fleet01/B19/20260922T094856Z-b19-pos3-r14/REPORT.md`,
  blob `6d93d5f0946705f91b7a1e0d70023c5aba8eba64`.

Its Theorem 3.3 proves that, after all immediate strict-subspan exits are removed, the canonical earliest-endpoint export is exactly a two-upper-cover fork. At the canonical left endpoint `p`, there are distinct covers

`p lessdot r_1`, `p lessdot r_2`,

with

`q || r_1,r_2`, `r_1 || r_2`, `q prec_* r_i`,

both exclusive cross packets `r_1<q<r_2` and `r_2<q<r_1` nonempty, and one channel of full-extension mass `>E/6`. Its Theorem 4.1/Corollary 4.2 further proves that, in the span-descent-exhausted branch, each `r_i` has `p` as its **unique lower cover**.

I also use the threshold-free heavy-child theorem:

- fleet01/B10 `20260922T084926Z-b10-pos3-r13`,
  `proofnet24/collective-POS3/fleet01/B10/20260922T084926Z-b10-pos3-r13/REPORT.md`,
  blob `907ef9d19e23c05bc68a13c34ddb5a4aad6e30df`.

For every heavy Hasse bridge with neither balance nor an authorized strict strong-majority span descent, it constructs a heavy child with strictly smaller left `prec_*` rank.

The fleet04/B19 one-sided reset potentials are retained as compatible background:

- `proofnet24/collective-POS3/fleet04/B19/B19-20260922T091459Z-r46/REPORT.md`,
  blob `3ab26879c6f8301fa782a8ee1d2fbd47dca150a7`.

## 2. First unpaid implication attacked

The designated partner left

> `POS3-CANONICAL-TWO-FORK-SWITCH-CHARGE-v1`: show that an excursion alternating between the two sibling covers of the canonical fork, or leaving and re-entering that fork, cannot recycle the two exclusive cross packets indefinitely without balance, strict span descent, a proper reduction, or a genuinely new well-founded charge.

This run pays the **direct sibling-switch / sibling-alternation branch**. The off-fork leave-and-re-enter splice remains open.

## 3. New theorem: the canonical sibling switch cannot survive without descent

Assume for contradiction that `P` is a finite width-at-most-three poset with no balanced pair. Let `(p,q)` be the canonical earliest-ending incomparable pair from the lead: `q` has least possible later `prec_*` rank and `p` is the leftmost predecessor of `q` incomparable with it.

Assume all already-authorized strict strong-majority subspan exits have been removed. By fleet01/B19 r14, the surviving canonical fork has exactly two upper covers

`p lessdot r_1`, `p lessdot r_2`,                                    (3.1)

with

`q || r_1,r_2`, `r_1 || r_2`, `q prec_* r_1,r_2`,                  (3.2)

and each `r_i` has `p` as its unique lower cover.

Relabel the two siblings so that

`r_1 prec_* r_2`.                                                   (3.3)

### Lemma 3.1 — the sibling pair has no lower transposition channel

For the oriented sibling pair `(r_1,r_2)`, its lower Hasse witness family is empty:

`D(r_1,r_2)={z:z lessdot r_2, z||r_1}=emptyset`.                   (3.4)

**Proof.** The unique lower cover of `r_2` is `p`, while `p<r_1` in the poset by (3.1). Thus the only lower cover of `r_2` is comparable with `r_1`, so it is not a member of `D(r_1,r_2)`. `square`

### Lemma 3.2 — absent descent, sibling switching creates exactly two new upper channels

Let

`U(r_1,r_2)={u:r_1 lessdot u, u||r_2}`.                            (3.5)

Then, unless an authorized strict subspan has already occurred,

1. `U(r_1,r_2)={u_1,u_2}` has exactly two vertices;
2. `r_2 prec_* u_i` for both `i`;
3. `u_1||u_2`;
4. the outgoing illegal transposition set of `(r_1,r_2)` has full-extension mass `>E/3`.

**Proof.** Because `(r_1,r_2)` is strongly oriented by (3.3),

`N(r_1<r_2)>2E/3`.

The exact endpoint-transposition identity gives

`|O|-|J| = 2N(r_1<r_2)-E > E/3`,                                 (3.6)

hence `|O|>E/3`.

By Lemma 3.1 every outgoing illegal swap is supported on an upper Hasse channel, and exactly

`O = union_(u in U(r_1,r_2)) {L:u<r_2 in L}`.                     (3.7)

Distinct upper covers of `r_1` are pairwise incomparable, and every member of `U(r_1,r_2)` is also incomparable with `r_2`; width at most three therefore gives

`|U(r_1,r_2)|<=2`.                                               (3.8)

If some `u prec_* r_2`, then `r_1<u` in the poset gives

`r_1 prec_* u prec_* r_2`,

and `(r_1,u)` is an authorized strict subspan of `(r_1,r_2)`. So in the surviving branch every `u` satisfies `r_2 prec_*u`. No-balancedness then gives

`#{L:u<r_2}<E/3`                                                 (3.9)

for each individual channel. Equations (3.6)-(3.9) rule out zero or one channel, proving exactly two. Pairwise incomparability of distinct upper covers gives `u_1||u_2`. `square`

### Lemma 3.3 — width three forces one lifted witness above `q`

At least one of `u_1,u_2` is comparable with `q`; for such a witness `u` one necessarily has

`q<u`.                                                           (3.10)

**Proof.** If `q` were incomparable with both `u_1,u_2`, then

`{q,r_2,u_1,u_2}`

would be a four-element antichain: `q||r_2` by (3.2), `r_2||u_i` by (3.5), and `u_1||u_2` by Lemma 3.2. This contradicts width at most three.

Moreover `q prec_*r_1 prec_*u`, because `r_1<u` in the poset. Hence `q prec_*u`. If `q,u` are comparable, the only compatible poset order is `q<u`. `square`

### Lemma 3.4 — absent descent, the forced relation is actually a cover

For the witness `u` supplied by Lemma 3.3,

`q lessdot u`                                                    (3.11)

unless an authorized strict strong-majority subspan has already occurred.

**Proof.** Choose a saturated chain from `q` to `u`, and let `c lessdot u` be its penultimate vertex. Because `q||r_1` while `r_1 lessdot u`, we have `c!=r_1`.

If `c!=q`, then

`q prec_* c prec_* u`.                                          (3.12)

Also `c` and `r_1` are distinct lower covers of `u`, so `c||r_1`. Compare the `prec_*` rank of `c` with `r_1,r_2`.

- If `q prec_*c prec_*r_1`, then `(c,r_1)` is a strict subspan of the incomparable pair `(q,r_1)`.
- If `r_1 prec_*c prec_*r_2`, then `(r_1,c)` is a strict subspan of `(r_1,r_2)`.
- `c=r_2` is impossible because it would imply `r_2<u`, contrary to `u||r_2`.
- If `r_2 prec_*c prec_*u`, then `c||r_2`: `r_2<c` in the poset would force `r_2<u`, while `c<r_2` would contradict the strong-order placement. Hence `(r_2,c)` is a strict subspan of `(r_2,u)`.

Every case with `c!=q` therefore triggers an authorized strict subspan. In the surviving branch `c=q`, proving (3.11). `square`

### Lemma 3.5 — the lifted witness recreates a heavy bridge anchored at `q`

The triple

`(q,r_2,u)`                                                      (3.13)

is a heavy Hasse bridge:

`q lessdot u`, `r_2||q,u`, `q prec_*r_2 prec_*u`,

and

`Pr(q<r_2<u)>1/3`.                                              (3.14)

**Proof.** The Hasse and incomparability statements are Lemmas 3.3-3.4 and the definition of `U(r_1,r_2)`. The strong-order inequalities follow from (3.2) and Lemma 3.2.

Relative to the forced cover `q<u`, the two endpoint cells have probabilities

`Pr(r_2<q)<1/3`, `Pr(u<r_2)<1/3`

by no-balancedness and `q prec_*r_2 prec_*u`. Their complement is the middle cell `q<r_2<u`, so (3.14) follows. `square`

### Theorem 3.6 — direct canonical sibling recycling is impossible

Starting from the canonical two-cover fork, an attempted direct switch between the sibling covers cannot remain in a no-balance, no-strict-descent branch. It must produce either an actual balanced pair or an authorized strict strong-majority span descent.

**Proof.** Lemmas 3.1-3.5 reduce every surviving sibling-switch branch to the heavy bridge `(q,r_2,u)`. Apply the threshold-free heavy-child theorem of fleet01/B10 r13.

If that theorem returns a Mode-T child `(t,q,r_2)`, then `t||q` and

`t prec_* q`.

By the defining leftmost choice of `p` among the predecessors incomparable with `q`, either:

- `p prec_*t prec_*q`, in which case `(t,q)` is a strict subspan of `(p,q)`; or
- `t=p`, in which case the child is exactly the canonical bridge `(p,q,r_2)`, already proved by the lead report to be incapable of a span-exhausted continuation.

The possibility `t prec_*p` contradicts the leftmost choice of `p`.

If the heavy-child theorem returns a Mode-F child `(c,r_2,u)`, then

`c lessdot u`, `c||r_2`, `c prec_*q`.                            (3.15)

Since `q lessdot u` as well, `c` and `q` are distinct lower covers of `u`, so `c||q`. Thus `c` is another predecessor of `q` in the strong order that is incomparable with `q`. The leftmost choice of `p` rules out `c prec_*p`. Equality `c=p` is impossible because

`p<r_1<u`

would put `r_1` strictly between `p` and `u`, contradicting `p lessdot u`. Hence

`p prec_*c prec_*q`,

and `(c,q)` is a strict subspan of `(p,q)`.

Both heavy-child modes therefore force one of the already-authorized strict-span exits (or the lead's already-paid canonical bridge exit). No span-exhausted direct sibling recycler survives. `square`

## 4. Consequence for the partner's switch-charge residual

The direct sibling-alternation half of `POS3-CANONICAL-TWO-FORK-SWITCH-CHARGE-v1` is now paid.

At the canonical earliest endpoint, once the two-cover saturation has been reached:

- the two sibling covers cannot merely exchange the two cross packets and return neutrally;
- their own transposition has no lower Hasse channel;
- if it does not descend immediately, width three forces two upper sibling channels;
- width three then forces one of those channels to meet `q`;
- in the no-descent branch that relation becomes a cover and hence a heavy bridge;
- the threshold-free heavy-child theorem sends that bridge back to a strict canonical subspan.

Thus **a direct canonical sibling switch is a forced descent mechanism, not an unresolved recycler**.

The remaining unpaid implication is strictly narrower:

> **`POS3-CANONICAL-FORK-REENTRY-SPLICE-v2`.** After the forced strict descent (or another already-authorized external exit) leaves the canonical two-cover fork, prove that a later excursion cannot return to the same canonical fork through a different mechanism without either a globally smaller well-founded state, a balanced pair, or a proper autonomous/ordinal reduction.

This is now an off-fork mixed-mechanism re-entry problem. The sibling-switch branch itself is closed.

## 5. Compact conditional route

Assume a minimal no-balanced width-three candidate.

1. The lead supplies the canonical earliest-ending pair `(p,q)` and rules out a span-exhausted first canonical heavy bridge.
2. fleet01/B19 r14 collapses every still-undescended `q`-anchored export to exactly two upper covers and gives unique lower-cover rigidity.
3. Theorem 3.6 above eliminates direct switching between those two sibling covers: it forces strict span descent or balance.
4. fleet04/B19 already eliminates one-sided same-cover span resets by exact lexicographic potentials.
5. Therefore any remaining recycler must **leave the canonical fork through a genuinely different mechanism and later re-enter it**. Proving that mixed re-entry globally well founded is now the first unpaid splice.

The parent POS3 theorem remains open; no full-proof promotion is made.

## 6. Computation and integrity

No new finite computation was needed for the theorem above. The proof is arbitrary-size and symbolic. The seven-element guard in fleet01/B19 r14 remains a useful warning that bare local fork probabilities alone do not close POS3; this run uses the canonical earliest-endpoint and width-three Hasse structure essentially.

Scoped provenance/privacy review used only the named mathematical repositories, source-bound peer reports, sanitized logical run labels, exact mathematical formulas and nonsecret Git object identifiers. No benchmark gold or sealed answers, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, public posting, paid model/API/Codex execution, remote workflow, permission bypass, production-population mutation, or native verified-brain activation was used or claimed.

## 7. Honest status

- latest complete lead fleet04/B10: **CONSUMED/APPLIED**;
- required OTHER-account fleet01/B19 r14: **CONSUMED/APPLIED**;
- fleet01/B10 threshold-free heavy-child theorem: **CONSUMED/APPLIED**;
- sibling lower Hasse family `D(r_1,r_2)=empty`: **PROVED**;
- no-descent sibling transposition creates exactly two upper channels: **PROVED**;
- width-three forces one lifted witness comparable above `q`: **PROVED**;
- in the no-descent branch that relation sharpens to `q lessdot u`: **PROVED**;
- resulting `(q,r_2,u)` is a heavy Hasse bridge: **PROVED**;
- both heavy-child modes return to a canonical strict-span exit: **PROVED**;
- direct canonical sibling-switch recycler: **ELIMINATED**;
- off-fork mixed-mechanism re-entry splice: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- inherited finite frontier `n_bal=14`: **UNCHANGED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.
