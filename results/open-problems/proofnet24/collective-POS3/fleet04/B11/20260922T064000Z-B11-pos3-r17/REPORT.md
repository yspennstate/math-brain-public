# POS3 fleet04/B11 — first non-exact boundary overload exports to four outer-ray Hasse channels

**Run:** `20260922T064000Z-B11-pos3-r17`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every count below is a literal count of full linear extensions of the original poset. No induced deletion law is renamed uniform, no finite-kernel reduction is used, and no bounded-size hypothesis is introduced.

## 1. Exact collective state consumed

The latest complete campaign-lead version used is

- fleet04/B10, `proofnet24/collective-POS3/fleet04/B10/20260922T061407Z-B10-POS3-r15/REPORT.md`, blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`.

It proves, in the surviving no-span-descent branch, that the exact failed-swap charge of a heavy cover is forced onto the two outer rays of the transitive strong-majority order. If both heavy-edge endpoint minorities are below `3/11`, one ray carries more than `2E/11` marked incidences and one concrete outward Hasse channel carries more than `2E/33`. Its first unpaid statement is a ray-return/reuse exclusion.

The assigned OTHER-account partner result consumed directly is

- fleet01/B19, `proofnet24/collective-POS3/fleet01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`, blob `19f1baa7b3bbe4ed45e19df6ca396f97f6fa5131`.

For two consecutive exact-two crossed states it proves the exact four-pair selector `>=3/11`, the conserved corridor integer `K`, the recurrence

`A_(i-1)+3A_i+A_(i+1)=E+K`,

and the deep-corridor bound

`K/E >= 4/11 - eps_s`,

where

`rho=(3-sqrt(5))/2`,
`eps_s=[10/(3(1-rho^2))] rho^s`.

The boundary algebra used below is the newest complete fleet03/B10 result

- `proofnet24/collective-POS3/fleet03/B10/b10-20260922t061504z-r11/REPORT.md`, blob `85fb81cdcbd72f87bcfca53e30f060a83770a1f6`.

It proves that the exact-two recurrence reaches the **actual first non-exact boundary pair with zero additive probability defect**. In its notation, for the last exact-two state and the first boundary pair,

`A_prev+3A+B=E+K`,

so a same-polarity no-balanced boundary has the strict overload

`K-B=A_prev+3A-E>0`.

I also use fleet03/B11's exact Hasse-canonicalization principle from

- `proofnet24/collective-POS3/fleet03/B11/20260922T061153Z-fleet03-B11-pos3-r11/REPORT.md`, blob `007674a740f490d5c90b2820dadde4d5ee48de52`.

That report shows how a failed relabelling/swap can be pushed along a saturated chain to a Hasse witness while preserving the marked full extension. The theorem here derives a different boundary relabelling identity and needs only the same elementary Hasse-pushing idea.

## 2. Conditional route and the exact missing implication attacked

Assume a cardinality-minimal hypothetical POS3 counterexample and follow a maximal exact-two crossed corridor to its first non-exact lower-fringe boundary. Let the last exact-two state have distinguished labels `d,x,y,u` with

`Pred(y)=Pred(x) union {d}`,                                  (2.1)
`Succ(x)=Succ(y) union {u}`.                                  (2.2)

Thus `d<y`, `x<u`, `d||x`, `x||y`, and `u||y`.

Use the six literal four-label word counts

`A = N(d y x u)`,
`C = N(d x y u)`,
`X = N(d x u y)`,
`Y = N(x d y u)`,
`Z = N(x d u y)`,
`W = N(x u d y)`.

The inherited exact-two identities give `C=A` and `Z=K-A`. The actual first boundary pair is `(d,x)`, with

`B=N(x<d)=Y+Z+W`.

Therefore the fleet03/B10 overload has the much more concrete form

`delta := K-B = A-Y-W`.                                      (2.3)

In the surviving same-polarity no-balanced boundary, `delta>0`.

The first missing implication was to convert this purely numerical overload into actual structural channels. Sections 3--5 do exactly that: `delta` full extensions cannot be accounted for by two exact injective relabellings, and every resulting failed inverse relabelling has a Hasse blocker in one of only four width-three channels. Under no span descent those channels lie strictly outside the boundary interval in the strong-majority order.

## 3. Two exact relabelling injections into the A-class

All relabellings below leave every nondisplayed element in the same position. Hence they preserve the exact residual skeleton and all of its multiplicity.

### Lemma 3.1 — `Y -> A`

For every full extension in the `Y` class, whose displayed order is

`x ... d ... y ... u`,

replace the labels occupying the three displayed positions of `x,d,y` by `d,y,x`, respectively. The result is a full linear extension in class `A`. The map is injective.

#### Proof

Call the new order `Phi_Y(L)`.

- `d` moves left to the old position of `x`. Every predecessor of `d` is a predecessor of `y`; by (2.1), because it is not `d` itself, it is a predecessor of `x`. Hence every predecessor of `d` was already before the old `x` position.
- `y` moves left to the old position of `d`. Its predecessors are `Pred(x) union {d}`. The `Pred(x)` elements remain before the old `x` position, and `d` has just been placed at that old `x` position.
- `x` moves right to the old position of `y`. By (2.2), every successor of `x` is either `u` or a successor of `y`. The label `u` remains after the old `y` position, and every successor of `y` was already after it.

All other movements are in the order-preserving direction. The displayed result is `d ... y ... x ... u`. Because the relabelling is a fixed permutation of the labels occupying fixed positions, it is injective. `square`

### Lemma 3.2 — `W -> A`

For every full extension in the `W` class,

`x ... u ... d ... y`,

replace the labels at the four displayed positions by `d,y,x,u`, respectively. The result is a full linear extension in class `A`. This map is injective.

#### Proof

The only additional facts needed beyond (2.1)--(2.2) are their transitive consequences

`Pred(d) subseteq Pred(x)`,                                   (3.1)
`Succ(u) subseteq Succ(y)`.                                   (3.2)

Indeed, if `p<d`, then `p<y`, so (2.1) puts `p` in `Pred(x)`. If `u<s`, then `x<u<s`, so `s` is a successor of `x` different from `u`; (2.2) puts `s` in `Succ(y)`.

Now `d` moves left to the old `x` position, which is safe by (3.1). `y` moves left to the old `u` position; all `Pred(x)` elements lie before old `x`, while the required predecessor `d` is placed at old `x`. The label `x` moves right to the old `d` position; its successors are `u` or successors of `y`, all of which remain to its right. Finally `u` moves right to the old `y` position; (3.2) says every successor of `u` was already after old `y`. Thus the new order is valid and has word `d y x u`. Again this is a fixed-position label permutation, hence injective. `square`

Let `I_Y` and `I_W` denote the two images inside the `A` class. They may overlap; no disjointness is claimed or needed. Therefore

`|A \ (I_Y union I_W)|`
` >= A-|I_Y|-|I_W|`
` = A-Y-W`
` = delta`.                                                   (3.3)

So at least `delta` literal `A`-extensions are missed by **both** exact incoming relabellings.

This is the first key conversion: the boundary overload is exactly a deficit of relabelling coverage, not an abstract recurrence remainder.

## 4. Every missed A-extension has a canonical blocker in four Hasse channels

Take an `A`-extension `L` outside `I_Y union I_W`. In particular `L` is not in `I_Y`. Apply the inverse `Y` relabelling to its displayed positions

`d ... y ... x ... u  ->  x ... d ... y ... u`.              (4.1)

If (4.1) were a linear extension, applying Lemma 3.1 would return `L`, contradicting `L notin I_Y`. Hence (4.1) fails.

Only two kinds of order relation can fail.

### Type G1

The label `x` is moved left. If it crosses a predecessor `q<x`, then (2.1) also gives `q<y`, so `q` lies between the displayed `d` and `y` positions in `L`. It cannot satisfy `q<d`, because it occurs after `d`, and it cannot satisfy `d<q`, because then `d<q<x` would contradict `d||x`. Thus `q||d`.

Follow a saturated chain from `q` to `x` and let `r` be its last vertex before `x`. Then

`r lessdot x`, `r||d`,                                      (4.2)

and in the marked extension `L` one has `d<r`.

### Type G2

The label `d` is moved right. If it crosses a successor `d<q`, then `q` lies between the displayed `d` and `y` positions in `L`. It cannot satisfy `q<x`, because that would give `d<x`, and it cannot satisfy `x<q`, because `q` occurs before the displayed `x`. Hence `q||x`.

Follow a saturated chain from `d` to `q` and let `r` be its first vertex after `d`. Then

`d lessdot r`, `r||x`,                                      (4.3)

and in `L` one has `r<x`.

There is no third failure type. The label `y` moves right only from its displayed position to the displayed position of `x`. If it crossed a successor `y<q`, then (2.2) would imply `x<q`; but `q` would occur before the old `x` position, impossible in a linear extension.

Define

`G1={r: r lessdot x, r||d}`,
`G2={r: d lessdot r, r||x}`.                                 (4.4)

Every missed `A`-extension therefore receives at least one canonical marked incidence in one of these two families.

### Width-three compression

Distinct lower covers of `x` are pairwise incomparable. If `G1` had three elements, those three together with `d` would form a four-antichain. Therefore

`|G1|<=2`.                                                    (4.5)

Dually, distinct upper covers of `d` are pairwise incomparable. Three elements of `G2` together with `x` would form a four-antichain, so

`|G2|<=2`.                                                    (4.6)

Combining (3.3)--(4.6) proves the main quantitative statement.

### Theorem 4.1 — first-boundary overload-to-four-channel export

At the first non-exact boundary of a maximal exact-two crossed corridor, if

`delta=K-B=A-Y-W>0`,

then at least `delta` marked full-extension incidences are carried by at most four concrete incomparable-pair Hasse channels:

- for `r in G1`, the event `d<r` of the pair `d||r`;
- for `r in G2`, the event `r<x` of the pair `r||x`.

Consequently one concrete channel receives at least

`ceil(delta/4)`                                                (4.7)

marked full extensions.

No probability mass has been created or projected. The marked extensions are a subset of the original uniform extension set.

## 5. Strong-majority direction: the overload cannot be absorbed inside the boundary interval

Now add the surviving lead hypotheses: the boundary pair has the same no-balanced polarity

`d prec_* x`,                                                  (5.1)

and there is no strict strong-majority span descent inside the interval `(d,x)`.

### Theorem 5.1 — all four possible boundary channels are outward minority channels

Under (5.1) and no internal span descent,

`r in G1  =>  r prec_* d`,                                    (5.2)
`r in G2  =>  x prec_* r`.                                    (5.3)

Moreover the marked event in Theorem 4.1 is the **minority orientation** of its pair.

#### Proof

If `r in G1`, then the poset relation `r<x` gives `r prec_* x`. If instead `d prec_* r prec_* x`, the incomparable pair `d||r` would be a strict span descent inside `(d,x)`. Therefore `r prec_* d`. Hence the marked event `d<r` is the minority orientation of `r||d` in a hypothetical no-balanced poset.

If `r in G2`, the poset relation `d<r` gives `d prec_* r`. If `d prec_* r prec_* x`, then `r||x` would be a strict internal span descent. Therefore `x prec_* r`. The marked event `r<x` is then the minority orientation of `x||r`. `square`

Thus the **first non-exact boundary itself cannot absorb the strict overload inside the exhausted interval**. It must export it to one of the two outer strong-order rays, through at most four Hasse channels.

This pays a concrete part of the lead's `RAY-RETURN EXCLUSION`: an exact-two corridor reaching its first structural boundary does not lose its overload there and cannot recycle it through a stationary interior blocker. Any remaining recycling must cross into new strong-order territory on the left or right, or enter a later mechanism where the hypotheses genuinely change.

## 6. Direct application of the assigned partner's deep-corridor bound

If the conserved `K` has a continuing four-pair window at strong corridor depth `s`, fleet01/B19 r13 gives

`K/E >= 4/11-eps_s`,
`eps_s=[10/(3(1-rho^2))]rho^s`, `rho=(3-sqrt(5))/2`.

At a same-polarity no-balanced boundary, `B<E/3`. Hence

`delta/E=(K-B)/E > 1/33-eps_s`.                              (6.1)

Combining with Theorem 4.1, one concrete outward Hasse minority channel carries marked mass strictly greater than

`(1/132 - eps_s/4) E`.                                       (6.2)

For `s=6`, the partner constant is

`eps_6 ~= 0.0121204108`,

so (6.2) is already more than `0.00454565 E`. As the exact-two corridor becomes deeper, the guaranteed one-channel packet approaches `E/132` from below.

This is not itself a balanced-pair bound; the packet is a subset of a minority event and need not occupy one third of all extensions. Its significance is structural: a deep corridor arrives at its first non-exact boundary with a quantitatively nonvanishing packet that must immediately leave the exhausted strong-order interval on a concrete Hasse pair.

## 7. Deterministic source-model regression

I wrote a standard-library verifier

`verify_boundary_overload_export.py`, blob `3d7031cbcbdc860ceb9c0e2acd76791c90f7906f`.

It generates every naturally labelled poset through `n=6`, retains width at most three, finds every exact-two crossed state satisfying (2.1)--(2.2), enumerates all full linear extensions, and checks:

1. the `Y -> A` fixed-position relabelling is a valid injection;
2. the `W -> A` fixed-position relabelling is a valid injection;
3. the number of `A`-extensions missed by their union is at least `A-Y-W`;
4. every missed `A`-extension has an invalid inverse `Y` relabelling;
5. every such failure has a canonical `G1` or `G2` Hasse witness;
6. the width-three bounds `|G1|,|G2|<=2` hold.

Captured output, blob `1d9baa8040084c34fba64b6c2aff44b1607e0e76`, is

```text
POS3_BOUNDARY_OVERLOAD_EXPORT_CHECK_PASS
width_at_most_3_n3 7
width_at_most_3_n4 39
width_at_most_3_n5 314
width_at_most_3_n6 3339
states 2811
extensions_examined 106811
positive_delta_states 1006
total_positive_delta 2788
unmatched_total 4311
```

The finite computation is regression evidence only. The arbitrary-size theorem is the symbolic relabelling/Hasse argument in Sections 3--5.

## 8. Compact end-to-end implication now available

The live proof route can now be stated more sharply.

1. The lead's heavy bridge creates a target-scale exact swap-defect packet and forces it onto an outer strong-order ray.
2. The partner's exact-two recurrence transports a balanced-sized latent integer `K`, with a `3/11` local selector and a stronger deep-corridor lower bound on `K/E`.
3. fleet03/B10 shows there is no additive probability defect at the first non-exact boundary; instead a same-polarity escape has strict overload `delta=K-B`.
4. **New here:** that exact overload equals `A-Y-W`, hence is the deficit of two valid incoming relabelling injections. At least `delta` full extensions have no such incoming lift; each has a canonical boundary Hasse blocker. Width three compresses them to at most four channels, and no-span descent forces all four channels onto the two outer rays with the marked orientation minority.

The first essential unpaid implication is therefore no longer “convert the first boundary overload into a channel.” That conversion is proved. What remains is a genuinely global **OUTER-RAY REUSE EXCLUSION**:

> Following the successive outward Hasse packets produced by heavy gaps and first non-exact boundaries, prove that a finite width-three no-balanced minimal core cannot reuse or reverse previously exposed outer-ray territory indefinitely without producing a balanced pair, strict strong-majority span descent, a proper autonomous/ordinal reduction, a four-antichain, or a separately controlled multi-distinguisher exit carrying the conserved charge onward.

The earlier B11 interval-order family remains an essential guard: arbitrary long sequences of short local exact-two/heavy-cover states exist even with bounded incomparability range and bounded rank variance, so the required global reuse exclusion cannot be replaced by a bounded corridor-length argument.

## 9. Status and integrity

- latest lead r15 ray localization: **CONSUMED/APPLIED**;
- assigned partner fleet01/B19 r13 `3/11` selector and deep `K` bound: **CONSUMED/APPLIED**;
- fleet03/B10 first-boundary zero-defect/overload identity: **CONSUMED/APPLIED**;
- exact boundary identity `delta=K-B=A-Y-W`: **DERIVED**;
- exact injections `Y -> A` and `W -> A`: **PROVED**;
- overload deficit becomes at least `delta` missed `A`-extensions: **PROVED**;
- every missed extension has a `G1/G2` Hasse blocker: **PROVED**;
- width-three compression to at most four actual incomparable-pair channels: **PROVED**;
- no-span branch forces those channels strictly onto the two outer strong-order rays and marks minority orientations: **PROVED**;
- global outer-ray reuse/reversal exclusion: **OPEN**;
- parent POS3 target: **OPEN / NOT PROVED**;
- run classification: `ESSENTIAL_STEP_APPLIED`.

No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid model/API/Codex execution, remote workflows, permission changes, or public release were used. The repository artifact is a private source-bound research checkpoint, not a publication or truth promotion.
