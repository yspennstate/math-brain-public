# POS3 account03/B10 — direct full-law export localizes every ray switch to a bounded Hasse-chord walk

**Run:** `20260922T081747Z-B10-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability below is under the original uniform law on the complete set of full linear extensions of the original poset. No deletion, projection, or induced distribution is substituted for that law.

## 1. Exact assignment and sources consumed

The assigned account04/B11 partner result consumed is:

- account04/B11 r17, `proofnet24/collective-POS3/account04/B11/20260922T071403Z-B11-pos3-r17/REPORT.md`, commit `d6c62e8f596a7138756a51d76f63fea08143b308`, blob `bd9d3d0ae19ddc6d4d11a341665c6082ed5976ad`.

It proves, in the actual exceptional no-balanced regime,

`7 <= pi(P) <= K_3`,

and for incomparable `x_i prec_* x_j`, `d=j-i`,

`Pr(x_j < x_i) < 2125440/(d+1)^2`.                 (1.1)

It therefore localizes every pair carrying a fixed positive minority mass to a bounded strong-majority interval, and gives maximum degree at most `K_3` for every positive-threshold packet graph. Its first unpaid implication was `DISTINGUISHER-TO-PACKET EXIT`: a coherent three-antichain gate forces static external relation distinguishers, but that report correctly refuses to assign them packet mass without a proof.

A newer compatible collective result was also consumed:

- account02/B10 r11, `proofnet24/collective-POS3/account02/B10/20260922T075033Z-b10-pos3-r11/REPORT.md`, blob `c82c5309ce2cf74a1c103149b879249eaa1ffce9`.

It proves an exact full-law four-channel transposition theorem: from every strong incomparable pair `p prec_* q`, unless a balanced pair or strict strong-order span descent is already obtained, one gets an outward Hasse-witnessed incomparable pair with actual minority probability strictly greater than `1/12`. The output pair shares one endpoint with the input pair. Applied to the old coherent gate, the Hasse witness cannot be the third antichain vertex, so the gate genuinely exits.

This run applies the assigned B11 bounded-variance/high-comparability machinery to that stronger direct export, and then analyzes the first genuinely global obstruction: left/right ray switching.

## 2. The static-distinguisher bottleneck is bypassed, not silently assumed

The B11 r17 `DISTINGUISHER-TO-PACKET` implication is **not** assumed or claimed proved. Instead the newer transposition theorem makes it unnecessary for the current route.

Starting from either strong endpoint pair of the coherent gate, apply the exact position-swap involution on full linear extensions. If the run does not terminate by balance or strict span descent, the outgoing defect mass exceeds `E/3`; width three gives at most four Hasse witness channels, so one channel carries more than `E/12` full extensions and recodes to an actual outward incomparable pair. This is direct full-law mass and does not pass through the static relation distinguisher at all.

Thus the exact validation/process change from the assigned partner is:

> replace the unproved static-witness-to-probability conversion by the source-bound four-channel full-law transposition export; retain B11's variance/range estimates only after the actual packet has been certified.

No claim is made that an arbitrary relation distinguisher itself carries a universal packet.

## 3. New `1/12` packet-graph localization

Define `Gamma_{1/12}` to be the graph on `P` whose edges are incomparable pairs with minority ordering probability at least `1/12`.

### Theorem 3.1 — exported packets have degree at most `K_3` and bandwidth at most `5049`

In a hypothetical no-balanced width-three counterexample in the B11 exceptional regime,

`Delta(Gamma_{1/12}) <= K_3`,                              (3.1)

and every edge `{x_i,x_j}` of `Gamma_{1/12}`, `i<j`, satisfies

`j-i <= 5049`.                                             (3.2)

**Proof.** Every packet edge is an incomparability edge, hence its degree at a vertex is at most `|Inc(v)| <= pi(P) <= K_3`.

For bandwidth, let `m=Pr(x_j<x_i) >= 1/12`. By (1.1),

`1/12 <= m < 2125440/(j-i+1)^2`,

so

`(j-i+1)^2 < 2125440*12 = 25505280`.

The exact integer comparison is

`5050^2 = 25502500 < 25505280 < 25512601 = 5051^2`.

Hence `j-i+1 <= 5050`, i.e. `j-i <= 5049`. `square`

The account02 export is strict `>1/12`, so every nonterminal exported pair lies in this graph with room to spare.

## 4. New recursive Hasse-chord packet-walk invariant

Orient every current packet edge by the strong-majority order. Suppose the current pair is

`p prec_* q`, `p||q`.

The four-channel theorem has only two outward forms.

- **Right export:** a witness `r` satisfies `p lessdot r`, `r||q`, the new strong order is `q prec_* r`, and the next packet edge is `{q,r}`.
- **Left export:** a witness `r` satisfies `r lessdot q`, `r||p`, the new strong order is `r prec_* p`, and the next packet edge is `{r,p}`.

Thus every nonterminal export shares exactly one endpoint with the preceding packet edge, and the two nonshared vertices are joined by a Hasse cover. After the first export, every edge of the recursive sequence has minority mass `>1/12`; by Theorem 3.1 every such edge has strong-order span at most `5049` and every anchor has at most `K_3` packet neighbors.

This turns the remaining global problem into a concrete **Hasse-chord walk in `Gamma_{1/12}`**, rather than an abstract sequence of static distinguishers.

## 5. New exact classification of a genuine ray switch

The first unpaid account02 implication is ray-switch accounting. A single switch has a rigid width-three form.

### Theorem 5.1 — right-to-left switch is either an immediate backtrack or a width-saturating three-antichain

Assume one recursive step goes right:

`{a,b} -> {b,c}`,

so

`a prec_* b prec_* c`, `a lessdot c`, `a||b`, `b||c`.       (5.1)

Assume the next step goes left from `{b,c}` to `{d,b}`. Then

`d lessdot c`, `d||b`, `d prec_* b prec_* c`.                (5.2)

Exactly one of the following occurs.

1. `d=a`, so the packet walk immediately backtracks to the previous edge `{a,b}`.
2. `d!=a`, in which case `{a,b,d}` is a three-element antichain, hence width-saturating.

**Proof.** If `d!=a`, then `a` and `d` are distinct lower covers of `c`; distinct lower covers are incomparable. Equations (5.1)-(5.2) also give `a||b` and `d||b`. Hence `a,b,d` are pairwise incomparable. Width at most three makes this a saturated antichain. `square`

The left-to-right statement is the order dual.

### Corollary 5.2 — every nonbacktracking turn is `5049`-local

Once the walk is inside `Gamma_{1/12}`, both packet edges `{a,b}` and `{d,b}` have span at most `5049`. Since `a` and `d` lie on the same strong-order side of `b` in a right-to-left turn, the whole turn antichain `{a,b,d}` has strong-order diameter at most `5049`.

Thus a genuine ray switch cannot create an arbitrarily wide fresh local gate. It either exactly backtracks or creates a new bounded-diameter width-saturating antichain.

## 6. Exact actual-law structure of the immediate backtrack

The backtrack case `d=a` is also rigid. Then

`a lessdot c`, `a||b`, `b||c`, `a prec_* b prec_* c`.

Let

`alpha = Pr(b<a)`, `beta = Pr(c<b)`.

Because `a<c` is a poset relation, the relative order of the triple in every full extension is exactly one of

`b<a<c`, `a<b<c`, `a<c<b`.

Consequently

`Pr(a<b<c) = 1-alpha-beta`.                                 (6.1)

If this is a genuine two-way exported backtrack, each selected channel has mass `>E/12`, so

`alpha > 1/12`, `beta > 1/12`.                               (6.2)

No-balancedness gives `alpha,beta<1/3`. Therefore the canonical cover-sandwich event is squeezed by

`1/3 < Pr(a<b<c) < 5/6`.                                    (6.3)

Again (6.1)-(6.3) are statements about the original uniform full-extension law; no conditional law is present.

This does not yet contradict no-balancedness, but it identifies the exact two-cycle obstruction: a Hasse cover with an incomparable middle strong-majority vertex, both adjacent packet minorities in `(1/12,1/3)`, and canonical slot mass in `(1/3,5/6)`.

## 7. Sharpened first missing implication

Combining Sections 3--6, the old generic `DISTINGUISHER-TO-PACKET EXIT` and generic ray-switch statement can be replaced by the narrower target

**`POS3-BOUNDED-HASSE-CHORD-WALK-v1`.**  Rule out a recursive `>1/12` packet walk in `Gamma_{1/12}` which avoids balance and strict span descent, where

- consecutive packet edges share an endpoint;
- the two nonshared vertices are Hasse-comparable;
- every packet edge has strong-order span at most `5049`;
- packet degree is at most `K_3`;
- every nonbacktracking ray switch creates a `5049`-local width-saturating three-antichain; and
- every immediate ray-switch backtrack is the exact Hasse sandwich (6.1)-(6.3).

Same-ray segments already have the inherited strict potential. The genuinely unpaid work is therefore to exclude (a) repeated Hasse-sandwich two-cycles and (b) chains of bounded local three-antichain turns, or to show that one of them forces a balanced pair, strict span descent, a four-antichain, or a proper autonomous/ordinal reduction.

This is not a finite-kernel theorem: bounded bandwidth and bounded degree do not bound `|P|`.

## 8. Status

- assigned partner account04/B11 r17: **CONSUMED/APPLIED**;
- newer account02/B10 r11 direct full-law transposition export: **CONSUMED/APPLIED**;
- unproved static-distinguisher mass transfer: **NOT USED**;
- threshold packet graph `Gamma_{1/12}` degree `<=K_3`: **PROVED**;
- threshold packet graph bandwidth `<=5049`: **PROVED**;
- recursive export is an endpoint-sharing Hasse-chord packet walk: **PROVED**;
- nonbacktracking ray switch gives a width-saturating three-antichain: **PROVED**;
- such turn antichain has strong-order diameter `<=5049`: **PROVED**;
- immediate backtrack gives exact Hasse-sandwich identity and `(1/3,5/6)` slot window: **PROVED**;
- bounded Hasse-chord walk termination: **OPEN / FIRST ESSENTIAL MISSING IMPLICATION**;
- parent POS3 target: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark material, credentials, email/Drive data, paid/remote compute, public workflow dispatch, scheduler mutation, or verified-brain activation was used.
