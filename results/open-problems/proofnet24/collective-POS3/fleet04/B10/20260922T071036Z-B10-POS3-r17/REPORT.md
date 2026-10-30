# POS3 fleet04/B10 — typed same-ray gates have strict packet order; only a coherent three-antichain gate remains

**Run:** `20260922T071036Z-B10-POS3-r17`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14`, unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below are under the original uniform law on the full linear extensions of the original finite poset. No deletion-induced law is treated as uniform.

## 1. Exact state consumed

The latest complete campaign-lead report is

- fleet04/B10 r16, `proofnet24/collective-POS3/fleet04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md`, Git blob `78e86dcdaef62417888ef6d8b66bf3b6d062f2c9`.

Its live low-endpoint heavy-cover state is

`x lessdot y`, `a||x,y`, `x prec_* a prec_* y`,

with

`A=#{L:a<x<y}`, `H=#{L:x<a<y}`, `C=#{L:x<y<a}`, `E=A+H+C`,

and `A,C<3E/11`. It uses the four canonical Hasse blocker families

`F1={r:x lessdot r, r||a, r!=y}`,
`F2={r:r lessdot a, r||x}`,
`F3={r:a lessdot r, r||y}`,
`F4={r:r lessdot y, r||a, r!=x}`.

The left-swap defect uses `F1 union F2`; the right-swap defect uses `F3 union F4`. Under the no-span hypotheses, `F2 union F4` lies on the left strong-order ray before `x`, while `F1 union F3` lies on the right ray after `y`. R16 proves that one selected left-swap witness and one selected right-swap witness each carry more than `2E/33` canonical marks and can be losslessly recoded to genuine boundary pairs `(r,x)` or `(y,r)`. Its remaining same-ray exception was only classified abstractly as comparable/nested versus an incomparable three-antichain gate.

The required named OTHER-account result used here is

- fleet01/B11, `proofnet24/collective-POS3/fleet01/B11/20260922T064118Z-b11-pos3-r11/REPORT.md`, Git blob `3e01610994266bc6f9e77ba3101389183106cb16`.

For a repeated exact-two crossed block it proves the exact identity

`2(delta_R+delta_L)=11H-5E+s_R+s_L`,

with `s_R,s_L>=0`. Hence in the same low-endpoint regime `H>5E/11`, at least one repeated-exact-two continuation has a strict positive pair-minority gain. That rules out a neutral return cycle *inside* the repeated exact-two regime and makes the first adjacent unresolved local mechanism the lead's same-ray two-packet gate.

The inherited source claim `operations/claims/I0122.md` retains the all-posets finite frontier `n_bal=14`; this width-three campaign does not reset or re-report that frontier as new.

## 2. First missing implication attacked

R16 leaves two selected outward packet vertices, one from each swap side. If both land on the same strong-order ray, the generic statement "comparable implies nested" does not yet identify which swap packet dominates, and the incomparable gate has not been reduced to a single orientation.

The key extra observation is that the two selected vertices have **different Hasse types**. On the right ray they must be one `F1` vertex and one `F3` vertex; on the left ray they must be one `F2` vertex and one `F4` vertex. Those Hasse types force an order whenever the vertices are comparable and force one complete canonical mark family into a definite blocker-versus-blocker orientation whenever they are incomparable.

This yields a strict pair-minority potential in the comparable branch and an anchor-free `>2/33` pair in one orientation of the incomparable branch. The sole same-ray branch not paid by this argument is a coherent width-saturating three-antichain gate whose strong-majority order agrees with that forced mark orientation.

## 3. Elementary order-extension fact

We use the following standard finite-poset fact explicitly.

**Lemma 3.1.** If `u<v` in a finite poset and `z` is incomparable with both `u` and `v`, then there is a linear extension in which

`u<z<v`.

**Proof.** Add the two relations `u<z` and `z<v`. Neither alone creates a directed cycle because `z||u,v`; a cycle using both new relations would require an old path `v<=u`, contradicting `u<v`. The augmented relation is therefore a finite partial order and has a linear extension. `square`

Thus every event of the form `{u<z<v}` occurring below has positive integer count, at least one full linear extension.

## 4. Typed same-ray strict-gain theorem

Let `r_L` be the selected left-swap witness and `r_R` the selected right-swap witness supplied by r16, each carrying more than `2E/33` canonical marks.

### Theorem 4.1 — right-ray comparable gate has a forced strict packet order

Assume both selected blockers lie on the right ray. Then necessarily

`r_L in F1`, `r_R in F3`.

If they are comparable, then

`r_L < r_R`.                                                   (4.1)

Moreover the two actual boundary-pair minority counts satisfy the exact identity

`#{L:r_L<y} - #{L:r_R<y} = #{L:r_L<y<r_R} > 0`.               (4.2)

Equivalently,

`Pr(r_L<y) > Pr(r_R<y)`                                       (4.3)

by at least `1/E`.

**Proof.** Right-ray localization excludes `F2,F4`, so the left-swap witness is in `F1` and the right-swap witness is in `F3`. By definition,

`x lessdot r_L`, `r_L||a,y`, and `a lessdot r_R`, `r_R||y`.

If comparability had the direction `r_R<r_L`, then `a<r_R<r_L`, contradicting `r_L||a`. Hence (4.1).

Because `y||r_L,r_R` and `r_L<r_R`, the event `{r_R<y}` is contained in `{r_L<y}` and their set-theoretic difference is exactly `{r_L<y<r_R}`. Lemma 3.1 shows this difference is nonempty. This proves (4.2)-(4.3). `square`

Thus the comparable right-ray gate is not a neutral two-packet return: the `F1` boundary packet has strictly larger actual minority probability than the `F3` boundary packet.

### Theorem 4.2 — left-ray comparable gate has the dual forced strict packet order

Assume both selected blockers lie on the left ray. Then necessarily

`r_L in F2`, `r_R in F4`.

If they are comparable, then again

`r_L < r_R`,                                                   (4.4)

and now

`#{L:x<r_R} - #{L:x<r_L} = #{L:r_L<x<r_R} > 0`.               (4.5)

Equivalently,

`Pr(x<r_R) > Pr(x<r_L)`                                       (4.6)

by at least `1/E`.

**Proof.** Left-ray localization forces the stated types. We have `r_L<a` from `F2`, while `r_R||a` from `F4`. The direction `r_R<r_L` would give `r_R<r_L<a`, contradicting `r_R||a`; hence `r_L<r_R`. Since `x||r_L,r_R`, `{x<r_L}` is contained in `{x<r_R}`, with exact difference `{r_L<x<r_R}`. Lemma 3.1 makes that difference nonempty. `square`

So the comparable left-ray gate also has a canonical strict higher-potential packet, here the `F4` boundary pair.

### Consequence

R16's same-ray comparable exception is now paid in the sense needed for pair selection: the Hasse types determine a unique direction of strict actual pair-minority gain. In particular, the two same-ray packets can never have equal minority count, and an immediate two-state same-ray return between them is impossible if the selector keeps the larger packet.

This is compatible with and extends fleet01/B11's exact-two anti-return mechanism: the repeated exact-two block supplies a strict-gain side by its fiber identity, while a comparable same-ray gate supplies a strict-gain side by the literal positive strip (4.2) or (4.5). No claim is made yet that an arbitrary mixed sequence of all possible exit types has a single global monotone potential.

## 5. Incomparable same-ray gate: one orientation exports an anchor-free packet

The remaining same-ray alternative has the selected blockers incomparable. The Hasse types then still force one entire selected mark family into a definite blocker-versus-blocker ordering event.

### Theorem 5.1 — right-ray incomparable gate

Assume both selected blockers lie on the right ray and `r_L||r_R`. Then `{y,r_L,r_R}` is a three-element antichain, with

`r_L in F1`, `r_R in F3`.

Every canonical `F1` mark assigned to `r_L` lies in the event

`{r_L<r_R}`.                                                  (5.1)

Since the selected `F1` witness carries more than `2E/33` marks, if the strong-majority order of the blocker pair is

`r_R prec_* r_L`,                                             (5.2)

then the actual anchor-free incomparable pair `(r_R,r_L)` has minority probability

`Pr(r_L<r_R) > 2/33`.                                         (5.3)

If instead `r_L prec_* r_R`, the only unresolved right-ray same-ray state is the coherent width-saturating gate

`y prec_* r_L prec_* r_R`,                                   (5.4)

with `{y,r_L,r_R}` a three-antichain.

**Proof.** An `F1` canonical left-swap mark has the relative order

`x<r_L<a<y`.

Because `r_R in F3`, the poset relation `a<r_R` holds in every extension. Hence each such mark has `r_L<a<r_R`, proving (5.1). R16 gives more than `2E/33` such marks for the selected `F1` witness. Under (5.2), `{r_L<r_R}` is exactly the minority orientation of the blocker pair, proving (5.3). If (5.2) fails, no-balancedness makes the opposite strict strong-majority orientation hold, giving (5.4) together with r16's right-ray orientations `y prec_* r_L,r_R`. `square`

### Theorem 5.2 — left-ray incomparable gate

Assume both selected blockers lie on the left ray and `r_L||r_R`. Then `{r_L,r_R,x}` is a three-element antichain, with

`r_L in F2`, `r_R in F4`.

Every canonical `F4` mark assigned to `r_R` lies in

`{r_L<r_R}`.                                                  (5.5)

Indeed an `F4` right-swap mark has `x<a<r_R<y`, while `r_L<a` is a poset relation from `F2`. Since the selected `F4` witness carries more than `2E/33` marks, if

`r_R prec_* r_L`,                                             (5.6)

then the anchor-free blocker pair has

`Pr(r_L<r_R) > 2/33`.                                         (5.7)

Otherwise the sole unresolved left-ray same-ray state is the coherent width-saturating gate

`r_L prec_* r_R prec_* x`,                                   (5.8)

with `{r_L,r_R,x}` a three-antichain. `square`

The significance is not the constant `2/33` by itself. The new point is that one orientation of the incomparable gate removes the old boundary anchor entirely and exports a genuine blocker-blocker pair at the full local-gap scale. The only incomparable same-ray state that does not do so is the aligned/coherent three-antichain orientation (5.4) or (5.8).

## 6. New reduced recycling obligation

Combining r16 with Theorems 4.1-5.2 reduces the same-ray portion of `OUTWARD-STATE RECYCLING` as follows.

A low-endpoint heavy edge produces two typed outward packets. If they occupy the same ray, exactly one of the following occurs:

1. **Comparable typed gate:** a literal positive strip gives a strict direction of actual pair-minority gain; the neutral same-ray two-packet return is excluded.
2. **Incomparable, anti-aligned gate:** the blocker pair itself is a new anchor-free actual incomparable pair with minority probability `>2/33`.
3. **Coherent three-antichain gate:** the common boundary endpoint and the two blockers form a width-saturating three-antichain whose strong-majority order agrees with the Hasse-forced mark orientation. This is the only same-ray gate left unpaid by the present argument.

The first essential next implication is therefore no longer generic same-ray recycling. It is:

> **COHERENT-GATE EXIT.** Starting from (5.4) or (5.8), prove that width-three Hasse constraints force either a balanced pair, strict strong-majority span descent, a proper autonomous/ordinal reduction, an opposite-ray split, or a transition into the already controlled exact-two/non-crossed charge mechanisms without decreasing the certified pair-minority potential.

Fleet04/B20's separately proved successor-staircase theorem already controls one non-crossed successor-nesting failure by converting at least half of the incoming minority mass into pairwise-disjoint literal cover-gap charge. Thus the coherent three-antichain gate and crossed multi-distinguisher recycling are now the sharp local exceptions, rather than the generic same-ray comparable case.

## 7. Status and integrity

- B10 r16 boundary-anchor recoding and two `>2E/33` outward packets: **CONSUMED/APPLIED**;
- fleet01/B11 heavy-gap exact-two anti-return identity: **CONSUMED/APPLIED**;
- typed same-ray comparable strict packet order: **PROVED**;
- exact positive strip identity and strictness: **PROVED**;
- anti-aligned incomparable gate exports anchor-free `>2/33` blocker pair: **PROVED**;
- coherent width-saturating three-antichain gate: **OPEN / SHARPENED EXCEPTION**;
- parent POS3 target: **OPEN / NOT PROVED**;
- inherited `n_bal=14`: **UNCHANGED**;
- run classification: `ESSENTIAL_STEP_APPLIED`.

No computation was needed for these arbitrary-size implications, so there is no code/output artifact for this run. The argument uses only full-extension event containments, Hasse relations already established in r16, the standard finite-poset extension fact, and the named exact-two partner result. No novelty or publication-priority claim is made.

Scoped privacy/provenance review: this report contains only mathematical statements, logical account/slot/run labels, repository-relative source references, and nonsecret Git object identifiers. It contains no credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, benchmark gold, email or Drive data.
