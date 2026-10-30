# POS3 fleet04/B11 — bounded-variance turns the live packet recycler into a bounded-band, bounded-degree graph

**Run:** `20260922T071403Z-B11-pos3-r17`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `p,q` with `1/3 <= Pr(p<q) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability below is under the original uniform law on all full linear extensions. No induced deletion law is treated as uniform and no finite-kernel reduction is used.

## 1. Exact collective state consumed

The latest complete campaign-lead report read in this invocation is

- fleet04/B10 r17, `proofnet24/collective-POS3/fleet04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, commit `732a848a9fa315f3907c654f0c54591dfe04535d`.

Its live low-endpoint heavy-cover state has two distinct fully outward actual incomparable-pair packets, each with minority probability strictly greater than `2/33`.  If the two packets occupy the same strong-order ray, the typed Hasse geometry leaves only three cases: a comparable gate with strict pair-minority gain, an anti-aligned incomparable gate whose blocker-blocker pair itself has minority `>2/33`, or a coherent width-saturating three-antichain gate.  The last case is the sole same-ray gate not paid in r17.

The assigned OTHER-account partner result consumed and applied is

- fleet01/B19 r13, `proofnet24/collective-POS3/fleet01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`, blob `19f1baa7b3bbe4ed45e19df6ca396f97f6fa5131`.

For every continuing four-pair exact-two window it proves an actual incomparable pair with minority probability at least `3/11`, together with the exact conserved recurrence and the deep-corridor lower bound on `K/E`.  Thus `3/11` is not a heuristic threshold: it is a literal full-extension pair probability produced by the exact corridor mechanism.

Two earlier B11 results are used exactly where needed.

- `proofnet24/collective-POS3/fleet04/B11/20260922T041135Z-B11-pos3-r14/REPORT.md` proves, in any hypothetical POS3 counterexample with strong-majority order `x_1 prec_* ... prec_* x_n`, that for every incomparable `x_i,x_j`, `i<j`, with `d=j-i`,

  `Pr(x_j < x_i) < 2125440/(d+1)^2`.                          (1.1)

  This comes from the inherited all-element rank atom `>1/81` and variance `<6560`, not from a finite-size assumption.

- `proofnet24/collective-POS3/fleet04/B11/B11-20260922T011236Z-pos3-r12/REPORT.md`, blob `e37a40f77dbe414014200d2db8a4cd5601f57d24`, pins the actual exceptional high-comparability regime to

  `7 <= pi(P) <= K_3`,                                         (1.2)

  for some finite source-qualitative `K_3`, using Peczarski's 6-thin theorem and Aires--Kahn's fixed-width large-range theorem.  That report also proves that (1.2) does **not** imply bounded `|P|`.

Finally I use the compatible newest fleet03/B19 report

- `proofnet24/collective-POS3/fleet03/B19/20260922T070336Z-b19-pos3-r11-same-ray-export/REPORT.md`.

It proves that the lead's coherent three-antichain gate cannot close inside its five-vertex core: absent an already-permitted strict span descent, it must export at least two relation distinguishers beyond the current same-ray envelope.  Its own exact examples show that static distinguisher export alone does not force one of the obvious local pairs to be balanced.

## 2. Compact conditional route and missing implication

Assume a cardinality-minimal width-three counterexample and use its transitive strong-majority order.

The live route now has two quantitative pair scales:

1. fleet01/B19's continuing exact-two corridor produces a pair with minority at least `3/11`;
2. the lead's low-endpoint heavy-cover exit produces two distinct fully outward pairs with minority `>2/33`, and r17 reduces the difficult same-ray branch to the coherent three-antichain gate.

The first question for the assigned bounded-variance/high-comparability worker is whether these certified packets can jump an arbitrarily large distance in the strong-majority order, thereby defeating any attempt to control recycling.  Sections 3--5 prove they cannot.  The result is stronger than a one-off radius estimate: the entire graph of pair channels carrying the lead-scale packet has both **bounded strong-order bandwidth** and **bounded degree** throughout the exceptional regime.

This does not prove POS3.  It isolates the next exact missing implication: in the coherent gate, convert one of the compulsory external **relation distinguishers** into a quantitatively weighted packet edge, or obtain one of the already-authorized exits.  Static existence of a distinguisher is not enough.

## 3. General variance-to-bandwidth lemma

For an incomparable pair `x_i,x_j`, `i<j`, let

`m(i,j)=Pr(x_j < x_i)`

be its minority probability, since `x_i prec_* x_j` in the hypothetical counterexample.

### Lemma 3.1 — threshold graph bandwidth

For every `alpha>0`, if

`m(i,j) >= alpha`,                                             (3.1)

then

`(j-i+1)^2 < 2125440/alpha`.                                  (3.2)

**Proof.** This is immediate from the strict bound (1.1):

`alpha <= m(i,j) < 2125440/(j-i+1)^2`.  Rearranging gives (3.2). `square`

The useful exact integer specializations are the following.

### Corollary 3.2 — partner-scale radius

If `m(i,j) >= 3/11`, then

`j-i <= 2790`.                                                 (3.3)

Indeed

`2125440 * 11/3 = 7793280`,
`2791^2 = 7789681`,
`2792^2 = 7795264 > 7793280`.

Thus `j-i>=2791` would contradict (3.2).

### Corollary 3.3 — lead-packet radius

If `m(i,j) >= 2/33` (in particular if it is strictly `>2/33`), then

`j-i <= 5920`.                                                 (3.4)

Here

`2125440 * 33/2 = 35069760`,
`5921^2 = 35058241`,
`5922^2 = 35070084 > 35069760`.

So an index gap at least `5921` is impossible.

These are uniform arbitrary-size bounds.  They use only the inherited counterexample rank atom/variance and therefore remain valid even though the poset itself may have arbitrarily many elements.

## 4. Application to the exact corridor and the lead's coherent gate

### Theorem 4.1 — the exact-two selector is a bounded jump

Every actual pair supplied by fleet01/B19 r13's four-state selector has strong-majority index distance at most `2790`.

**Proof.** The partner gives minority probability at least `3/11`; apply Corollary 3.2. `square`

Thus a continuing exact-two corridor cannot hide its certified near-balanced witness arbitrarily far away in the strong order.  This is a direct application of the assigned partner's exact result.

### Theorem 4.2 — both heavy-cover packets are bounded jumps

In the lead r17 low-endpoint branch, each of the two distinct fully outward boundary pairs has strong-majority index distance at most `5920`.

**Proof.** R16/r17 give actual minority probability strictly greater than `2/33` for each boundary pair.  Apply Corollary 3.3 separately. `square`

### Corollary 4.3 — coherent gate has uniformly bounded strong-order diameter

Consider the right-ray coherent gate from lead r17,

`y prec_* s prec_* u`,

with `{y,s,u}` a three-antichain.  Both packet pairs `(y,s)` and `(y,u)` have minority `>2/33`; hence

`index(s)-index(y) <= 5920`,
`index(u)-index(y) <= 5920`.                                  (4.1)

Therefore the entire coherent three-antichain lies in a strong-order interval containing at most `5921` positions.  The left-ray statement is the order dual.

If the same-ray gate is anti-aligned rather than coherent, lead r17 gives a blocker-blocker pair of minority `>2/33`; that new anchor-free pair also has index distance at most `5920`.

If the two same-ray blockers are comparable, the lead's strict strip identity compares two already-certified `>2/33` boundary pairs, so both of those channels remain inside the same `5920` bandwidth bound.

This pays a genuine part of `COHERENT-GATE EXIT`: the unresolved gate is not an arbitrary-long local object.  What can still be arbitrarily large is the amount of poset lying outside this bounded window and the number of times the anchor may change.

## 5. Bounded-degree packet graph in the exceptional range

Define the **lead-scale packet graph** `Gamma` on the elements of `P` by putting an undirected edge `{p,q}` exactly when

- `p||q`, and
- the minority ordering probability of the pair is at least `2/33`.

### Theorem 5.1 — bounded degree and bounded bandwidth

In the exceptional high-comparability regime (1.2),

`Delta(Gamma) <= K_3`,                                        (5.1)

and every edge of `Gamma` joins strong-majority positions whose index difference is at most `5920`.  Thus `Gamma` has maximum degree at most `K_3` and bandwidth at most `5920` with respect to the strong-majority order.

**Proof.** Every edge of `Gamma` is an incomparability edge, so its degree at a vertex `v` is at most `|Inc(v)| <= pi(P) <= K_3`.  The bandwidth statement is Corollary 3.3. `square`

The partner-scale subgraph formed by pairs with minority at least `3/11` has the same degree bound and the sharper bandwidth `2790`.

### Corollary 5.2 — no unbounded fixed-anchor packet fan

At a coherent gate `y||s,u`, the anchor `y` already uses two of its at most `K_3` incomparability slots.  Hence there are at most `K_3-2` additional **distinct** packet neighbors of `y` available anywhere in the entire poset, and every lead-scale packet neighbor lies within `5920` strong-order positions of `y`.

The same statement holds with `s` or `u` as anchor, and dually on a left ray.

This does **not** make the poset finite and is deliberately not called a finite-kernel reduction.  A recycler may change anchors through an arbitrarily long poset.  The theorem only rules out an unlimited supply of new weighted channels at one fixed anchor and bounds every certified weighted jump.

## 6. Direct use of the newest coherent-gate distinguisher export

Fleet03/B19 proves that in the coherent right-ray gate, absent strict span descent, the pair `(y,s)` has at least two relation distinguishers outside the five-vertex core, each lying either strictly before the old left envelope or strictly after the current same-ray envelope.  The dual statement holds on the left.

Combined with Theorem 5.1, this produces the exact current interface:

- **weighted objects:** the two lead packets are edges of `Gamma`, hence have degree bounded by `K_3` and strong-order span at most `5920`;
- **static objects:** the newly forced external distinguishers are merely relation witnesses.  The current results do not assign them `2E/33` marks or any other positive uniform fraction of the extension set.

Therefore one must not silently treat a static distinguisher as a packet edge.  Doing so would be the same kind of unsupported probability transfer that the collective work has repeatedly ruled out.

The first essential missing implication can now be stated sharply.

> **DISTINGUISHER-TO-PACKET EXIT.**  In the coherent three-antichain gate, under the no-balanced, no-span-descent, no-autonomous-reduction branch, prove that at least one compulsory external distinguisher either (i) yields an opposite-ray split or one of the already-controlled structural exits, or (ii) supports an actual incomparable pair with a quantitatively positive minority packet that can be entered into `Gamma` without losing the conserved charge.

A proof with threshold `2/33` would remain inside the present bounded-band packet graph.  A weaker universal threshold `c>0` would still be useful, because Lemma 3.1 would immediately give a finite jump radius `O(c^{-1/2})`; but the charge loss would then have to be paid explicitly in the global iteration.

This is strictly narrower than the old generic `RAY-RETURN EXCLUSION`: exact-two witnesses are already `2790`-local, heavy-cover packets are `5920`-local, fixed-anchor packet degree is at most `K_3`, and the only missing conversion is from the newly forced static distinguisher to a weighted continuation or terminal exit.

## 7. Failure preserved and why this is not closure

The earlier arbitrary-size family at `pi=7` proves that bounded incomparability range, bounded rank variance, bounded insertion multiplicity, connected incomparability and module-primality do not bound `|P|`.  The present packet-graph theorem therefore cannot be upgraded to a finite census.

Likewise fleet03/B19's exact local witnesses show that coherent/nested same-ray geometry need not itself contain an obvious balanced local pair.  The new result does not contradict those examples: it localizes the **certified weighted packet edges**, not every relation distinguisher and not the whole poset.

No computation was used as proof in this run.  The numerical radii are exact integer consequences of (1.1), with the displayed square comparisons.  There is therefore no code/output artifact to report for the mathematical step.

## 8. Status

- assigned partner fleet01/B19 r13 `3/11` exact four-state selector: **CONSUMED/APPLIED**;
- lead fleet04/B10 r17 typed same-ray/coherent-gate reduction: **CONSUMED/APPLIED**;
- own inherited variance-to-radius estimate (1.1): **APPLIED TO CURRENT LIVE PAIRS**;
- actual exceptional range `7<=pi(P)<=K_3`: **SOURCE-BOUND INHERITED INPUT, APPLIED**;
- partner-scale packet radius `<=2790`: **PROVED**;
- lead-scale packet radius `<=5920`: **PROVED**;
- coherent gate strong-order diameter `<=5920`: **PROVED**;
- lead-scale packet graph degree `<=K_3` and bandwidth `<=5920`: **PROVED**;
- unlimited new packet channels at one fixed anchor: **EXCLUDED**;
- coherent-gate static-distinguisher to weighted-packet conversion: **OPEN / FIRST ESSENTIAL MISSING IMPLICATION**;
- parent POS3 theorem: **OPEN / NOT PROVED**;
- inherited finite frontier `n_bal=14`: **UNCHANGED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No novelty or priority claim is made.  No benchmark material, credentials, email/Drive data, paid/remote compute, workflow dispatch, public posting, permission change, or verified-brain activation was used.
