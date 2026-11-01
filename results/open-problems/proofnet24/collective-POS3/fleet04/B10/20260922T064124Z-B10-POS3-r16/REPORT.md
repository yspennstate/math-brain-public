# POS3 fleet04/B10 — heavy-cover defect flux can be re-anchored to two genuine fully outward boundary pairs

**Run:** `20260922T064124Z-B10-POS3-r16`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability and count below is for the original uniform law on all full linear extensions. No deletion-induced law is treated as uniform.

## 1. Exact collective state consumed

The latest complete campaign-lead version consumed is my immediately preceding report

- fleet04/B10 r15, `proofnet24/collective-POS3/fleet04/B10/20260922T061407Z-B10-POS3-r15/REPORT.md`, blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`.

Its live heavy-cover state is

`x lessdot y`, `a||x,y`, `x prec_* a prec_* y`,

with strong-majority span descent already exhausted in both local intervals. Writing

`A=#{L:a<x<y}`, `H=#{L:x<a<y}`, `C=#{L:x<y<a}`, `E=A+H+C`,

r15 applies the exact Hasse swap-defect decomposition of fleet03/B11 and proves that every canonical active blocker lies on one of the two outer strong-order rays:

- `F2 union F4` lies strictly before `x` in `prec_*`;
- `F1 union F3` lies strictly after `y` in `prec_*`.

It also proves that if both endpoint minorities `A/E,C/E` are below the partner scale `3/11`, then one outer ray receives more than `2E/11` active-defect incidence and one concrete Hasse channel on that ray receives more than `2E/33` marks. The first unpaid statement was `RAY-RETURN EXCLUSION`.

The required named OTHER-account inputs used directly are:

- fleet01/B11, `proofnet24/collective-POS3/fleet01/B11/20260922T051731Z-b11-pos3-r11/REPORT.md`, blob `bba2357120a72c7e2d473dd23095240f61e2f266`, which proves the repeated exact-two actual-pair selector `>=3/11` and identifies the exact numerical gap `1/3-3/11=2/33`;
- fleet03/B11, `proofnet24/collective-POS3/fleet03/B11/20260922T061153Z-fleet03-B11-pos3-r11/REPORT.md`, blob `007674a740f490d5c90b2820dadde4d5ee48de52`, which proves the exact outgoing swap-defect identity, Hasse realization of every defect, and the width-three family bounds

  `|F1|<=1`, `|F2|<=2`, `|F3|<=2`, `|F4|<=1`.

I also use fleet04/B20's two-sided active-blocker theorem,

- `proofnet24/collective-POS3/fleet04/B20/20260922T054301Z-b20-auto11-pos3/REPORT.md`, blob `47c3315fbc0f05e501a9e49c6f305d6711ffed50`.

It gives separate exact lower bounds for the two failed-swap families and proves that the left-swap and right-swap active-blocker vertex sets are disjoint.

## 2. Compact conditional end-to-end route

In the surviving lead branch, r15 leaves an apparent ambiguity: an `F1` mark was naturally recorded on the defect orientation `r<a`, and an `F4` mark on `a<r`. Those charged pairs still use the interior point `a`, so a later iteration can look as if it has already returned through the old interval even though the blocker vertex itself lies on an outer ray.

The first missing structural implication is to decide whether this is a real return phenomenon or merely an artifact of which pair was used to record the failed swap.

The theorem below shows it is an artifact. Every canonical defect mark can be reassigned, with no loss of a single marked full extension, to an incomparable pair whose **whole strong-order interval is on the corresponding outer side of the old heavy edge**:

- every left-ray blocker is charged to `(r,x)`;
- every right-ray blocker is charged to `(y,r)`.

Thus the first export from a heavy edge has no interior return at all. Moreover, in the low-endpoint branch the two separate failed-swap families force **two distinct fully outward actual pairs**, each carrying more than `2E/33` marked extensions. This strengthens the previous one-channel ray statement and aligns the exact `2/33` scale with actual boundary-anchored pairs.

## 3. Boundary-anchor recoding lemma

Use the four canonical Hasse families from fleet03/B11:

`F1={r:x lessdot r, r||a, r!=y}`,
`F2={r:r lessdot a, r||x}`,
`F3={r:a lessdot r, r||y}`,
`F4={r:r lessdot y, r||a, r!=x}`.

For a middle extension `L in H`, a left failed swap `x <-> a` has a canonical witness in `F1 union F2`; a right failed swap `a <-> y` has a canonical witness in `F3 union F4`.

### Theorem 3.1 — every defect mark has a fully outward boundary anchor

Under the r15 no-span hypotheses:

1. if a canonical defect witness `r` lies in `F2 union F4`, then `r||x`, `r prec_* x`, and the marked extension belongs to the minority event

   `{x<r}` for the actual incomparable pair `(r,x)`;

2. if a canonical defect witness `r` lies in `F1 union F3`, then `r||y`, `y prec_* r`, and the marked extension belongs to the minority event

   `{r<y}` for the actual incomparable pair `(y,r)`.

Consequently every marked channel pair is fully outward from the old heavy interval: its strong-order interval is contained in the closed left ray ending at `x`, or the closed right ray beginning at `y`. No charged pair uses the interior point `a`.

### Proof

The strong-order directions are r15's ray-localization theorem. It remains only to prove the common boundary anchoring.

Take `r in F2`. By definition `r||x`. A left-swap defect witnessed by `r` occurs in a middle extension with

`x<r<a<y`,

so that extension belongs to `{x<r}`. Since r15 gives `r prec_* x`, this is the minority orientation of `(r,x)`.

Take `r in F4`. We have `r lessdot y`, while `x lessdot y` and `r!=x`. Distinct lower covers of the same element are incomparable, hence `r||x`. The right-swap witness occurs in an extension with

`x<a<r<y`,

so again that extension belongs to `{x<r}`. R15 gives `r prec_* x`, so it is again a minority mark for `(r,x)`.

Now take `r in F3`. The definition already gives `r||y`; a right-swap witness has

`x<a<r<y`,

hence belongs to `{r<y}`. R15 gives `y prec_* r`, making this the minority orientation of `(y,r)`.

Finally take `r in F1`. Here `x lessdot r`, while also `x lessdot y` and `r!=y`. Distinct upper covers of the same element are incomparable, so `r||y`. A left-swap witness has

`x<r<a<y`,

and therefore also lies in `{r<y}`. R15 gives `y prec_* r`, so it is a minority mark for `(y,r)`.

No injection or probability comparison is used in this recoding: it is a literal containment of each already-marked full extension in a boundary-pair minority event. Hence no marked mass is lost. `square`

### Structural meaning of the four types after recoding

The recoding also makes the outgoing geometry explicit.

- `F1`: the charged pair is `(y,r)` and `x lessdot y`, `x lessdot r`; it is a sibling-upper-fork channel completely to the right of the old interval.
- `F3`: the charged pair is `(y,r)` and `a lessdot r`; it is a right delayed-predecessor/successor-discrepancy channel.
- `F2`: the charged pair is `(r,x)` and `r lessdot a`; it is the dual left delayed-successor/discrepancy channel.
- `F4`: the charged pair is `(r,x)` and `r lessdot y`, `x lessdot y`; it is a sibling-lower-fork channel completely to the left.

Thus the first outward step enters only fork/corridor geometries already present in the collective reduction; it does not create an unclassified interior-return state.

## 4. Two-sided `2/33` boundary-packet theorem

Let

`B_L` be the middle extensions for which swapping the positions of `x` and `a` is invalid, and
`B_R` the middle extensions for which swapping the positions of `a` and `y` is invalid.

Fleet04/B20 proves

`|B_L| >= H-A`,
`|B_R| >= H-C`,                                                 (4.1)

and its active-blocker-capable vertex sets on the two swap sides are disjoint.

Assume now the live low-endpoint branch

`A < 3E/11`, `C < 3E/11`.                                      (4.2)

Since `H=E-A-C`, (4.1) gives

`|B_L| >= E-2A-C > 2E/11`,                                    (4.3)

`|B_R| >= E-A-2C > 2E/11`.                                    (4.4)

Choose a deterministic canonical Hasse witness for every bad swap, using fleet03/B11's Hasse reduction. Width three gives at most three left-swap witness vertices (`F1` plus at most two in `F2`) and at most three right-swap witness vertices (at most two in `F3` plus `F4`). Therefore:

### Theorem 4.1 — two distinct fully outward actual pairs carry the exact local gap scale

Under (4.2), there exist two distinct canonical blocker vertices `r_L` and `r_R`, one from the left-swap family and one from the right-swap family, such that each receives strictly more than

`2E/33`                                                        (4.5)

marked full extensions.

After applying Theorem 3.1, each mark set is contained in the minority orientation event of a fully outward actual incomparable pair of one of the forms

`(r,x)` with `r prec_* x`, or `(y,r)` with `y prec_* r`.        (4.6)

Hence there are two distinct fully outward incomparable pairs, each having actual minority probability strictly greater than `2/33`.

### Proof

The canonical witness assignment partitions `B_L` among at most three `F1/F2` vertices. Equation (4.3) and pigeonhole therefore give one left-swap witness with weight `>2E/33`. Likewise (4.4) and the at-most-three `F3/F4` vertices give one right-swap witness with weight `>2E/33`.

Fleet04/B20 proves the left-swap and right-swap active-blocker vertex sets are disjoint, so the selected witness vertices, and therefore the resulting boundary pairs, are distinct. Theorem 3.1 converts each selected mark set to a fully outward boundary-pair minority event without loss. `square`

The threshold in (4.5) is exactly

`1/3 - 3/11 = 2/33`,

the numerical gap isolated independently by fleet01/B11. No addition of probabilities from different pairs is claimed; the significance is structural: **two distinct actual outward pairs now carry a full local-gap-sized packet**, not merely one abstract ray incidence.

## 5. Exact exception classification when both packets choose the same ray

Theorem 4.1 does not force the two selected pairs onto opposite rays. If they are on opposite rays, the heavy edge has simultaneously produced one leftward and one rightward fully outward packet.

If instead both selected pairs lie on the same strong-order ray, they share the corresponding heavy-edge boundary endpoint:

- on the right, they are `(y,r_1)` and `(y,r_2)` with `y||r_1,r_2` and `y prec_* r_1,r_2`;
- on the left, they are `(r_1,x)` and `(r_2,x)` with `r_1,r_2||x` and `r_1,r_2 prec_* x`.

There is then an exact two-case structural alternative.

### Corollary 5.1 — same-ray packets form either a nested channel or a width-saturating gate

For two distinct same-ray blocker vertices `r_1,r_2`:

1. if `r_1` and `r_2` are comparable, their order agrees with `prec_*`, and the corresponding boundary minority events are nested;
2. if they are incomparable, the boundary endpoint together with `r_1,r_2` is a three-element antichain, saturating width three.

For example, on the right, if `r_1<r_2` then

`{r_2<y} subseteq {r_1<y}`;

while if `r_1||r_2`, then `{y,r_1,r_2}` is a three-antichain. The left-ray statement is dual.

This reduces the same-ray recycling exception to a one-dimensional nested channel or a width-saturating three-antichain gate; no third local geometry is possible.

## 6. Consequence for the r15 ray-return obligation

R15's first unpaid statement was phrased as a possible return of an outward packet through already exposed strong-order territory. Theorem 3.1 pays the **first return implication**:

> the exact heavy-edge defect mark itself never returns through the interior. Every mark can be charged to a pair whose whole strong-order interval lies on an outer ray, with anchor exactly `x` or `y`.

Thus a genuine return can occur only after a new outward fork/corridor state has been entered and another transfer is executed. In particular, the apparent immediate return caused by recording an `F1` mark on `(a,r)` or an `F4` mark on `(r,a)` is eliminated completely.

Theorem 4.1 then strengthens the low-endpoint branch to **two distinct** fully outward packets at the exact `2/33` local-gap scale. Corollary 5.1 identifies the only same-ray local exception: nested outward channels or a saturated three-antichain gate.

The remaining global implication is now narrower:

> **OUTWARD-STATE RECYCLING.** Starting from the two boundary-anchored packets of Theorem 4.1, prove that successive fork/exact-two/crossed/non-crossed transitions cannot cycle among outward states without forcing one of: an actual balanced pair, strict strong-majority span descent, a proper autonomous/ordinal reduction, a four-antichain, or a controlled multi-distinguisher exit carrying the exact charge onward. In the same-ray case it is enough to treat the nested-channel and width-saturating-gate alternatives of Corollary 5.1.

This is strictly more specific than r15's ray-return statement because the old interval and its interior point `a` no longer participate in the charged pair after the first export.

## 7. Status

- latest lead r15 heavy active-defect ray theorem: **CONSUMED/APPLIED**;
- assigned partner fleet01/B11 `3/11` selector and `2/33` gap: **CONSUMED/APPLIED**;
- fleet03/B11 exact Hasse swap-defect decomposition and `(1,2,2,1)` channel bounds: **CONSUMED/APPLIED**;
- fleet04/B20 separate left/right bad-swap lower bounds and disjoint blocker sets: **CONSUMED/APPLIED**;
- lossless boundary-anchor recoding of every canonical defect mark: **PROVED**;
- two distinct fully outward actual pairs, each carrying `>2E/33` marks in the low-endpoint branch: **PROVED**;
- same-ray nested-channel / three-antichain exception classification: **PROVED**;
- global outward-state recycling termination: **OPEN**;
- parent POS3 theorem: **OPEN / NOT PROVED**;
- inherited finite frontier: `n_bal=14`, unchanged;
- run classification: `ESSENTIAL_STEP_APPLIED`.

No computation is used in this run. There is therefore no code/output artifact to report. The proof is symbolic and arbitrary-size. No novelty or priority claim is made.

Scoped provenance/privacy review: this report contains only mathematics, repository-relative source references, nonsecret logical run labels and exact source blob identifiers. It contains no benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive content, paid model/API/Codex execution, remote workflow dispatch, public posting, permission changes, notification enablement or production-brain mutation.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: maximum actually supported. Configured reasoning effort and provider reasoning-token/thinking-time counters: `UNKNOWN / NOT_EXPOSED`, not zero. Elapsed execution is recorded separately in the operational receipt and is not pure thinking time.
