# POS3 account04/B10 — heavy active-blocker charge is forced onto the two outer strong-order rays

**Run:** `20260922T061407Z-B10-POS3-r15`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability and count below is for the original uniform law on all full linear extensions. No deletion-induced law is treated as uniform.

## 1. Exact collective state consumed

The latest complete campaign-lead version inherited by this run is my immediately preceding result

- account04/B10 r14, `proofnet24/collective-POS3/account04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`, blob `50bac494667235f3630991a512438eac42c30521`.

It proves that the surviving bridged majority-late branch contains a saturated bridge

`c=z_0 lessdot ... lessdot x lessdot y lessdot ... lessdot z_k=u`

and an element `a` incomparable with every bridge vertex such that

`Pr(x<a)>2/3`, `Pr(y<a)<1/3`,

hence the literal cover-gap event `H={x<a<y}` has mass `>1/3`.

The assigned partner result actually consumed is

- account01/B11, `proofnet24/collective-POS3/account01/B11/20260922T051731Z-b11-pos3-r11/REPORT.md`, blob `bba2357120a72c7e2d473dd23095240f61e2f266`.

For two consecutive exact-two crossed states it proves the actual-pair selector `>=3/11`, with local-fiber equality ray at `3/11`; thus the exact remaining numerical gap is

`1/3-3/11=2/33`.

Two newer OTHER-account results are used essentially rather than repeated.

- account03/B11, `proofnet24/collective-POS3/account03/B11/20260922T061153Z-account03-B11-pos3-r11/REPORT.md`, report blob `007674a740f490d5c90b2820dadde4d5ee48de52`, proves the exact two-sided heavy-gap swap-defect identity, canonical Hasse realization of every outgoing defect, and width-three compression to the four Hasse families

  `F1={r:x lessdot r, r||a, r!=y}`,
  `F2={r:r lessdot a, r||x}`,
  `F3={r:a lessdot r, r||y}`,
  `F4={r:r lessdot y, r||a, r!=x}`,

  with cardinalities at most `(1,2,2,1)` and total outgoing defect incidence at least `3|H|-E`.

- account03/B10, `proofnet24/collective-POS3/account03/B10/b10-20260922t061504z-r11/REPORT.md`, report blob `85fb81cdcbd72f87bcfca53e30f060a83770a1f6`, proves that the exact-two recurrence reaches the first actual non-exact boundary pair with **zero probability defect**. Its surviving same-polarity boundary satisfies the overload identity `K-B=A_prev+3A-E>0`; the missing step is structural conversion, not an additive correction to the boundary pair count.

I also use the compatible account04/B20 active-blocker result at `proofnet24/collective-POS3/account04/B20/20260922T054301Z-b20-auto11-pos3/REPORT.md` (read at science state containing commit `3be80f0efb709475ab7c81ad18c3f3fd42dd3b0b`). It strengthens the heavy-cover witness statement to two disjoint weighted off-bridge active-blocker families. The present theorem adds the missing **strong-order direction** of that exact weight.

## 2. Conditional end-to-end route

Assume a cardinality-minimal width-at-most-three counterexample and use the inherited transitive strong-majority order `prec_*`. Work in the branch where strong-majority span descent has already been exhausted in each of the two intervals

`x prec_* a prec_* y`.

The current route is now:

1. r14 creates a literal heavy cover gap `Pr(x<a<y)>1/3`;
2. account03/B11 and account04/B20 convert its excess into exact full-extension swap-defect weights on concrete off-bridge Hasse channels;
3. **new here:** every such canonical active channel lies strictly on one of the two strong-order rays outside the whole interval `[x,y]`; no active charge can remain in the interior interval after span descent has been exhausted;
4. if neither endpoint minority has yet reached the partner scale `3/11`, more than `2E/11` marked defect incidence is forced onto one outer ray, and one concrete outward Hasse pair receives more than `2E/33` marked full extensions;
5. the remaining step is therefore a ray-return/reuse exclusion, not an unnamed witness-existence problem or a boundary-probability correction.

Step 3 and its quantitative consequence are proved below.

## 3. Strong-order ray localization

Let

`x lessdot y`, `a||x,y`, `x prec_* a prec_* y`,

and assume there is no strict strong-majority span descent inside either interval `(x,a)` or `(a,y)`.

Use the canonical Hasse families `F1,...,F4` from account03/B11.

### Theorem 3.1 — every canonical active blocker is outside `[x,y]`

Under the hypotheses above,

`r in F2 union F4  =>  r prec_* x`,                         (3.1)

`r in F1 union F3  =>  y prec_* r`.                         (3.2)

Thus all canonical active blockers lie on the two **outer strong-order rays**; none lies in the closed strong-order interval from `x` to `y`.

### Proof

For `F2`, we have `r lessdot a` and `r||x`. Hence `r prec_* a` because a poset relation has probability one. If `x prec_* r prec_* a`, then the incomparable pair `(x,r)` gives a strictly shorter strong-majority span inside `(x,a)`, contrary to the no-span-descent branch. Therefore `r prec_* x`.

For `F3`, `a lessdot r` and `r||y`, so `a prec_* r`. If `a prec_* r prec_* y`, then `(r,y)` is a strict span descent inside `(a,y)`. Hence `y prec_* r`.

Now let `r in F1`. Then `x lessdot r`, `r||a`, and `r!=y`. Since `x lessdot y` also, the two distinct upper covers `r,y` of `x` are incomparable: `r||y`. The relation `x<r` gives `x prec_* r`. No descent inside `(x,a)` therefore forces `a prec_* r`. Since also `r||y`, no descent inside `(a,y)` rules out `a prec_* r prec_* y`; consequently `y prec_* r`.

Finally let `r in F4`. Then `r lessdot y`, `r||a`, and `r!=x`. The distinct lower covers `r,x` of `y` are incomparable: `r||x`. The relation `r<y` gives `r prec_* y`; no descent inside `(a,y)` forces `r prec_* a`. Since `r||x`, no descent inside `(x,a)` then rules out `x prec_* r prec_* a`; hence `r prec_* x`.

This proves (3.1)-(3.2). `square`

### Why the Hasse reduction retains the active mass

Account03/B11 proves that every failed middle-gap swap can be assigned to a canonical Hasse witness by following a saturated chain from the raw blocker toward the relevant endpoint. The witness still lies between the swapped endpoints in that full extension and therefore still marks the same failed-swap incidence. Thus Theorem 3.1 localizes the **actual weighted defect flux**, not merely the static relation-witness set.

## 4. Quantitative two-ray packet theorem

Let

`A = #{L:a<x<y}`,
`H = #{L:x<a<y}`,
`C = #{L:x<y<a}`,
`E=A+H+C`.

Thus `A/E=Pr(a<x)` and `C/E=Pr(y<a)` are the two endpoint minority probabilities in the heavy branch.

Account03/B11 gives canonical outgoing defect incidence at least

`D := 3H-E = 2E-3A-3C`.                                     (4.1)

By Theorem 3.1, after canonical Hasse assignment this incidence splits into

- a left-ray packet supported on `F2 union F4`, containing at most three concrete incomparable-pair channels, all with their witness vertices strictly before `x` in `prec_*`;
- a right-ray packet supported on `F1 union F3`, also containing at most three channels, all with witness vertices strictly after `y`.

Hence one of the two rays receives at least `D/2` marked full-extension incidences.

### Corollary 4.1 — endpoint-or-outward-packet dichotomy at the partner scale

In a hypothetical no-balanced candidate, either

`A/E >= 3/11` or `C/E >= 3/11`,                              (4.2)

in which case one of the actual endpoint pairs `(x,a)` or `(a,y)` already has minority probability in `[3/11,1/3)`,

or else

`A<3E/11` and `C<3E/11`.                                    (4.3)

In the latter case (4.1) gives

`D > 2E-18E/11 = 4E/11`.                                    (4.4)

Therefore one outer strong-order ray receives **strictly more than**

`2E/11`                                                     (4.5)

marked active-defect incidences. Since each ray has at most three canonical Hasse channels, at least one concrete outward incomparable-pair channel receives strictly more than

`2E/33`                                                     (4.6)

marked full extensions.

Every such mark is contained in the minority orientation event of that channel in the inherited no-span branch. Thus the channel's actual minority probability is itself `>2/33`, and its witness vertex is strictly outside `[x,y]` in the strong-majority order.

The value `2/33` is exactly the partner's numerical gap `1/3-3/11`. Equation (4.6) is **not** yet a proof of balance: the marked `2/33` packet belongs to a different outward pair and cannot simply be added to a `3/11` probability. What has now been proved is the missing directional capacity statement: if the two heavy-edge endpoint pairs both stay below the partner scale, a target-sized amount of exact defect incidence is forced onto a single outward ray, with a `2/33` packet visible on one concrete Hasse pair.

## 5. Application to the first non-exact boundary

The account03/B10 first-boundary theorem rules out a tempting but false mechanism: extra distinguishers do not first appear as an additive correction to the actual boundary-pair recurrence. The actual first boundary count is still exactly

`B=E+K-A_prev-3A`,

and a same-polarity no-balanced boundary has the strict overload

`K-B=A_prev+3A-E>0`.

The present ray theorem supplies a structural direction when this overloaded boundary is routed through the lead's heavy-cover/bridge mechanism. The exact full-extension excess cannot be paid by active channels lying inside the already exhausted strong-majority interval. It must leave through vertices strictly before the left endpoint or strictly after the right endpoint; in the low-endpoint branch one of those two rays carries more than `2E/11` active incidence.

Thus the first remaining global statement can be narrowed to:

> **RAY-RETURN EXCLUSION.** Show that an outward packet produced by (4.5), when recycled through subsequent exact-two / crossed / heavy-cover states, cannot return through previously exposed strong-order territory without producing a balanced incomparable pair, strict span descent, a four-antichain, a proper autonomous/ordinal reduction, or a controlled non-crossed/multi-distinguisher exit carrying the conserved charge onward.

This is strictly narrower than generic recycler acyclicity: stationary interior absorption is now impossible, and the packet has a definite left-or-right strong-order direction and an exact quantitative mass.

## 6. Source-valid guard against overclaiming

The account02/B19 exact heavy-cover trap remains a necessary regression guard. Its nine-element width-three core has `E=499`,

`Pr(x<a)=343/499`, `Pr(y<a)=142/499`, `Pr(x<a<y)=201/499`,

and its two displayed off-bridge witness events have

`Pr(x<p)=126/499`, `Pr(z<y)=125/499`,

while `90/499` heavy-gap extensions lie outside the union of those two witness events. The captured output is `proofnet24/collective-POS3/account02/B19/20260922T051105Z-account02-B19-pos3-r12/verify_two_witness_gap_noncover.out`, blob `63f6c3deadeab45e22645f4a102e127320a5217c`.

So relation-witness events are **not** a partition of the heavy gap, and one may not route `H` itself by a naive event-cover argument. The present proof avoids that error: it routes only the exact failed-swap incidences from account03/B11/account04-B20. In the 499-extension guard, both endpoint minorities (`156/499` and `142/499`) already exceed `3/11`, so Corollary 4.1 correctly takes its endpoint branch rather than asserting the low-endpoint ray packet.

## 7. Status

- lead r14 heavy bridge / target-scale cover flux: **CONSUMED**;
- assigned partner account01/B11 `3/11` selector: **CONSUMED/APPLIED**;
- account03/B11 exact weighted Hasse defect export: **CONSUMED/APPLIED**;
- account03/B10 zero first-boundary probability defect / overload identity: **CONSUMED/APPLIED**;
- strong-order ray localization of all canonical active blockers: **PROVED**;
- endpoint-or-`>2E/11` outward-ray packet dichotomy: **PROVED**;
- one concrete outward Hasse channel gets `>2E/33` marked extensions in the low-endpoint branch: **PROVED**;
- ray-return exclusion / global recycler acyclicity: **OPEN**;
- parent POS3 theorem: **OPEN / NOT PROVED**;
- inherited finite frontier: `n_bal=14` unchanged;
- run classification: `ESSENTIAL_STEP_APPLIED`.

No new computation is used as proof in this run. The only finite numerical object quoted is the source-valid account02/B19 regression guard above. No novelty/priority claim is made. No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid model/API/Codex calls, remote workflow, public posting, permission change, or native verified-brain activation is used or claimed.
