# POS3 account03/B10 — opposite-handed outer-ray reuse forces an actual heavy Hasse sandwich

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent status:** **OPEN / NOT PROVED**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

All probabilities and counts below are under the uniform law on the **full** set `L(P)` of linear extensions of the original poset. No deletion-induced law is replaced by a uniform surrogate.

## 1. Exact assignment and partner result consumed

The account03/B10 assignment is to apply bounded-width/high-variance results to the exact width-three target and make the exceptional residue explicit. The assigned partner is account04/B11.

I consume account04/B11 r17, `proofnet24/collective-POS3/account04/B11/20260922T064000Z-B11-pos3-r17/REPORT.md` (report commit `6a046ab4e6cb33a1311fbf7de41a3391d09999da`; shared handoff blob `b21683e4bf4bb77c3bbf6657b6e5dc4b6935f8d2`). At the first non-exact boundary it proves that the overload

`delta = K-B = A-Y-W > 0`

is exported to at most four concrete outer-ray Hasse minority channels. Its unpaid implication is `OUTER-RAY REUSE EXCLUSION`.

I also use the current lead account04/B10 r16, `proofnet24/collective-POS3/account04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md` (shared handoff blob `3f18184de42d52df865a9395f6a3c132f71fd52c`). Its low-endpoint heavy-cover branch says: for a cover `p lessdot q` and a bridge `a||p,q` with `p prec_* a prec_* q`, if there is no strict internal span descent and both endpoint minority counts are `<3E/11`, then there are two distinct fully outward actual incomparable-pair channels, one on each side, each receiving `>2E/33` marked full extensions.

Finally I use the assigned-partner's earlier bounded-variance theorem, account04/B11 r14, `proofnet24/collective-POS3/account04/B11/20260922T041135Z-B11-pos3-r14/REPORT.md`. In a hypothetical counterexample, if `x_i prec_* x_j`, `d=j-i`, and `x_i||x_j`, then

`Pr(x_j<x_i) < 2125440/(d+1)^2`.                              (1.1)

## 2. Canonical outer transitions

Work in a hypothetical no-balanced width-at-most-three counterexample and its transitive strong-majority order `prec_*`.

For a strong incomparable pair `a prec_* b`, call a canonical outer transition **left-handed** if the account04/B11 Hasse export replaces `(a,b)` by `(r,a)` with

`r prec_* a prec_* b`, `r||a`, and `r lessdot b`.             (2.1)

Call it **right-handed** if it replaces `(a,b)` by `(b,s)` with

`a prec_* b prec_* s`, `b||s`, and `a lessdot s`.             (2.2)

These are exactly the two Hasse forms `G1` and `G2` from the partner theorem, just written without committing to one boundary's labels.

The global unpaid question allows such packets to move outward and perhaps later reverse/reuse old territory. The first missing actual-law implication is what a change of handedness costs.

## 3. Turning lemma: a handedness change is a heavy cover, exactly

### Theorem 3.1 — actual-law turning identity

Suppose two consecutive canonical outer transitions have opposite handedness. Then there exist three elements

`u prec_* v prec_* w`

such that

`u lessdot w`, `u||v`, `v||w`.                               (3.1)

Let

`alpha = Pr(v<u)`, `beta = Pr(w<v)`.                          (3.2)

Then, under the uniform law on `L(P)`,

`Pr(u<v<w) = 1-alpha-beta`.                                  (3.3)

In a no-balanced counterexample, `alpha,beta<1/3`, hence

`Pr(u<v<w)>1/3`.                                              (3.4)

Thus **every reversal of canonical outer-ray direction creates an actual heavy Hasse sandwich**. No probability projection or induced law occurs.

#### Proof

Consider first a left transition followed by a right transition. The first transition lands at `(r,a)` with `r prec_* a` and with a Hasse chord from the old configuration. A right transition from `(r,a)` to `(a,t)` has, by the canonical `G2` form, `r lessdot t`, `a||t`, and `r prec_* a prec_* t`. Set `(u,v,w)=(r,a,t)`.

The reverse strong-order events are

`M_L={v<u}`, `M_R={w<v}`.

They are disjoint because `u<w` holds in the poset. Since every full linear extension has `u<w`, if neither reverse event occurs then necessarily `u<v<w`. Conversely `u<v<w` excludes both reverse events. Therefore the full extension set is the disjoint union

`{v<u} dotcup {u<v<w} dotcup {w<v}`,

which proves (3.3) by literal full-extension counting. The right-then-left case is the order-dual relabelling of the same argument. In a hypothetical no-balanced poset both incomparable pairs have their reverse strong-order probabilities `<1/3`, proving (3.4). `square`

### Corollary 3.2 — quantitative turn dichotomy

At a turn, either

`max(alpha,beta) >= 3/11`,                                    (3.5)

or

`Pr(u<v<w)>5/11`.                                             (3.6)

Indeed, if both `alpha,beta<3/11`, then (3.3) gives `1-alpha-beta>5/11`.

The first branch already gives an actual pair whose minority probability lies in

`[3/11,1/3)`.                                                 (3.7)

In the second branch the turning triple is exactly the low-endpoint heavy-cover configuration required by the current lead. Assuming the inherited no-internal-span-descent branch, account04/B10 r16 therefore exports **two distinct** outward actual incomparable pairs, one left of `u` and one right of `w`, each with minority probability `>2/33`.

This pays a concrete part of `OUTER-RAY REUSE EXCLUSION`: a reversal cannot be a silent return through already exposed territory. It must pass through either a `3/11`-near-balanced pair or a `>5/11` Hasse-sandwich state that immediately emits two fresh outward probability packets.

## 4. Bounded-variance localization of every turning consequence

The earlier account04/B11 actual-law radius estimate (1.1) now makes the exceptional residue explicit.

### Corollary 4.1 — near-balanced turn radius

If a turn falls in branch (3.5), then the relevant pair has minority `m>=3/11`. Combining with (1.1),

`3/11 < 2125440/(d+1)^2`,

so

`(d+1)^2 < 7793280`.

Since

`2791^2=7789681 < 7793280 < 2792^2=7795264`,

we obtain

`d <= 2790`.                                                  (4.1)

### Corollary 4.2 — low-endpoint turn export radius

In the low-endpoint branch, each lead-exported pair has actual minority `m>2/33`. Hence

`2/33 < 2125440/(d+1)^2`,

so

`(d+1)^2 < 35069760`.

Since

`5921^2=35058241 < 35069760 < 5922^2=35070084`,

we obtain

`d <= 5920`.                                                  (4.2)

Therefore every opposite-handed reuse event in a hypothetical counterexample is forced into the following **actual-law bounded-turn residue**:

1. a `[3/11,1/3)` minority pair at strong-order distance at most `2790`; or
2. after the lead's no-span-descent reduction, two opposite-side outward pairs, each with minority in `(2/33,1/3)` and strong-order distance at most `5920`.

These constants are independent of `|P|`.

## 5. What this rules out, and what it does not

A finite outer-channel walk that never changes handedness is monotone in the strong-majority order and therefore cannot itself be periodic. The only way to reuse/reverse strong-order territory is to change handedness. Theorem 3.1 shows that every such change necessarily re-enters the campaign's heavy-cover mechanism with **more than one third of all original full extensions** in the sandwich event. Thus there is no separate probability-defect mechanism at a reversal: the turn is an exact full-law heavy bridge.

This does **not** prove global recycler acyclicity. The lead's two `>2E/33` outward packets are actual subsets of minority events, but current results do not yet prove that each such packet is automatically eligible to restart an exact-two corridor or that packets from different turning generations are disjoint. The account04/B11 `R_N` family already warns that bounded local radius/variance does not bound total corridor length.

The remaining exceptional case is therefore narrower than `OUTER-RAY REUSE EXCLUSION` as previously stated:

**BOUNDED-TURN ACTIVATION.** In a cardinality-minimal no-balanced width-three core, take the two outward pairs produced at a low-endpoint turn. Prove that repeated reuse of those pairs either (i) activates a new canonical outer transition/corridor while preserving a nonvanishing portion of the `>2E/33` charge, (ii) gives strict span descent, (iii) creates a four-antichain, (iv) yields a proper autonomous/ordinal reduction, or (v) reaches a `[3/11,1/3)` pair. The only surviving recycling can use bounded-span (`<=5920`) turn gadgets; a silent uncharged direction reversal is impossible.

This is still an arbitrary-size requirement, not a finite-kernel claim.

## 6. Status

**Proved this run:** the exact turning identity (3.3), the `>1/3` heavy-turn consequence, the `3/11` versus `>5/11` dichotomy, and the explicit strong-order radii `2790` and `5920` after applying the partner's bounded-variance theorem and the lead's outward export theorem.

**Assigned partner directly consumed:** account04/B11 r17 boundary-overload export.

**Not proved:** bounded-turn activation, global recycler acyclicity, or POS3.

**No claim made:** novelty/priority, finite-kernel closure, uniformity of any deletion-induced law, or verified brain use.
