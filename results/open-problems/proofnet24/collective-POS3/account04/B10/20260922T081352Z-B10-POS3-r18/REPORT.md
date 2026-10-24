# POS3 account04/B10 r18 — every four-channel ray switch re-enters a heavy Hasse bridge; two-step switches have only descent, expansion, or exact backtrack

**Run:** `20260922T081352Z-B10-POS3-r18`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14`, unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and counts below are for the original uniform law on the full linear extensions of the original finite poset. No deletion-induced law is substituted for it.

## 1. Exact state and external results consumed

The latest complete campaign-lead state is account04/B10 r17,

- `proofnet24/collective-POS3/account04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, blob `61c94984acd303d2fbed96f2f3bb77664a51297b`.

R17 paid the comparable same-ray typed gate and the anti-aligned incomparable same-ray gate. Its only same-ray local exception was the coherent width-saturating three-antichain gate.

The decisive OTHER-account result consumed and applied is account02/B10,

- `proofnet24/collective-POS3/account02/B10/20260922T075033Z-b10-pos3-r11/REPORT.md`, blob `c82c5309ce2cf74a1c103149b879249eaa1ffce9`.

For any strong incomparable pair `p prec_* q`, it proves the exact transposition-defect identity

`|D_M|-|D_N| = 2M-E`,

so the outgoing defect has more than `E/3` extensions. Width at most three gives at most four Hasse witness channels. Hence one channel carries more than `E/12` marked extensions and exports either strict strong-majority span descent or a genuine outward incomparable pair whose minority orientation has probability `>1/12`. Applying this to r17's coherent gate shows that the gate cannot be a closed local recycler.

A second OTHER-account result used below is account01/B10,

- `proofnet24/collective-POS3/account01/B10/20260922T072132Z-b10-pos3-r11/REPORT.md`, blob `85fa62968e584b5db7fe6270260f55f92c071438`.

It proves that, under the no-balanced-pair hypothesis, `prec_*` is a strict total order, and supplies strict integer potentials on fixed left and right rays. Therefore the newly unpaid issue is genuinely a ray switch / crossed transition, not fixed-ray recycling.

I also use account01/B11's exact repeated-two anti-return identity,

- `proofnet24/collective-POS3/account01/B11/20260922T064118Z-b11-pos3-r11/REPORT.md`, blob `3e01610994266bc6f9e77ba3101389183106cb16`,

which gives, in its stated repeated-exact-two low-endpoint geometry,

`2(delta_R+delta_L)=11H-5E+s_R+s_L`.

Thus `H>5E/11` forces at least one strict outward pair-minority gain. This is invoked only when those exact-two hypotheses hold.

Finally, account02/B11 r18 supplies the articulation-corridor reduction:

- `proofnet24/collective-POS3/account02/B11/20260922T075311Z-b11-pos3-r18-aa069b32/REPORT.md`.

After strict span descent is exhausted, an incomparability cut vertex has only a two-boundary interface or a two-boundary-plus-one-leaf interface; a multi-level ordinal corridor is impossible.

The inherited source claim `operations/claims/I0122.md` retains the all-posets finite frontier `n_bal=14`. This width-three campaign does not reset that metric.

## 2. Compact conditional route and first missing implication

Assume for contradiction a finite width-at-most-three nonchain poset with no balanced pair. Then `prec_*` is a strict total order. The lead heavy-cover machinery produces outward charged incomparable pairs. Account02/B10 now says every strong pair exports either span descent or another outward pair carrying minority mass `>1/12`. Account01/B10 prevents indefinite recycling while the export stays on one strong-order ray.

The missing point is what happens when the export changes ray. The first result below shows that such an outward export does not enter an arbitrary new geometry: it **automatically recreates the lead's heavy Hasse-cover bridge**, with an exact three-cell partition. The second result classifies a two-step opposite-ray switch. After span descent is excluded, it is either a strict enlargement of the active strong-order envelope or an exact backtrack through that heavy bridge. There is no third local two-step ray-switch geometry.

This does not yet prove POS3. What remains is to exclude global cross-envelope reuse and the non-exact/multi-distinguisher exact-backtrack branch.

## 3. Every outward transposition export is a heavy Hasse bridge

Let `p||q` and assume `p prec_* q`, so `Pr(p<q)>2/3` in a no-balanced candidate.

### Theorem 3.1 — right export gives an exact heavy-cover state

Suppose account02/B10's selected outgoing Hasse channel is

`r in U(p,q)={r:p lessdot r, r||q}`

and that the marked orientation does not produce strict span descent. Then no-balancedness forces

`p prec_* q prec_* r`.                                      (3.1)

Put

`B = #{L:q<p<r}`,
`H = #{L:p<q<r}`,
`A = #{L:p<r<q}`,
`E=e(P)`.

Then

`E=A+H+B`,                                                   (3.2)

and

`B/E = Pr(q<p)`,
`A/E = Pr(r<q)`,                                             (3.3)

while

`H/E = Pr(p<q)+Pr(q<r)-1`
`    = Pr(p<q)-Pr(r<q)`
`    = Pr(q<r)-Pr(q<p)`.                                    (3.4)

In particular,

`H>E/3`.                                                     (3.5)

If moreover both endpoint minorities satisfy

`A<3E/11`, `B<3E/11`,                                       (3.6)

then

`H>5E/11`.                                                   (3.7)

**Proof.** Since `p lessdot r`, every full extension has `p<r`. The incomparable vertex `q` therefore has exactly three possible positions relative to this ordered pair: before `p`, between `p,r`, or after `r`; these are precisely the three disjoint cells in (3.2).

Account02/B10's right-channel marks lie in `p<r<q`, so `Pr(r<q)>1/12`. If `Pr(r<q)>2/3`, the exported pair `(r,q)` is the already-authorized strict inner-span exit. In the surviving no-descent branch, no-balancedness therefore gives `Pr(r<q)<1/3`, equivalently `Pr(q<r)>2/3`, which proves (3.1).

Equations (3.3) are immediate from the three-cell partition. Since `Pr(p<q)=(A+H)/E` and `Pr(q<r)=(B+H)/E`, each equality in (3.4) follows by subtraction and (3.2). Both probabilities on the first line of (3.4) exceed `2/3`, so their sum minus one exceeds `1/3`; this is (3.5). Finally (3.6) and (3.2) imply `H=E-A-B>5E/11`. `square`

Thus every surviving right export produces exactly the same kind of object used by the lead: a Hasse cover `p lessdot r`, a vertex `q` incomparable with both endpoints, and strong-majority order `p prec_* q prec_* r`.

### Theorem 3.2 — left export is the exact dual

Suppose the selected channel is

`r in D(p,q)={r:r lessdot q, r||p}`

and there is no strict span descent. Then

`r prec_* p prec_* q`.                                      (3.8)

The three positions of `p` relative to the cover `r lessdot q` give the dual exact partition. The middle-cell probability is again strictly greater than `1/3`, and if the old and new endpoint minorities are both below `3/11`, the middle cell is strictly greater than `5/11`.

The proof is the order-dual of Theorem 3.1. `square`

### Consequence 3.3 — high endpoint or low-endpoint heavy branch

Every outward four-channel transition therefore has a sharp dichotomy:

1. one of the old/new endpoint minority probabilities is at least `3/11` (and still below `1/3` in a no-balanced candidate), giving a near-balance/high-endpoint exit; or
2. both are below `3/11`, and the recreated Hasse bridge satisfies the lead low-endpoint inequality `H>5E/11`.

This is not merely a new constant. It closes the structural gap between the general four-channel transposition export and the lead's heavy-cover normal form.

## 4. Two-step ray-switch normal form

Write `[u,v]_*` for the interval between `u prec_* v` in the total strong-majority order.

### Theorem 4.1 — right then left switch: descent, strict envelope expansion, or exact backtrack

Start with a strong incomparable pair

`I_0=(p,q)`, `p prec_* q`.

Assume a surviving right export through `r`:

`p lessdot r`, `p prec_* q prec_* r`,

so the new active pair is

`I_1=(q,r)`.

Now assume the next surviving export changes direction, using a left Hasse channel `s in D(q,r)`. Thus

`s lessdot r`, `s||q`,

and no-balancedness/no-descent gives

`s prec_* q prec_* r`,

with new active pair

`I_2=(s,q)`.

Then exactly one of the following holds.

1. **Strict span descent:** `p prec_* s prec_* q`, so
   `[s,q]_* proper_subset [p,q]_*`.
2. **Strict two-step envelope expansion:** `s prec_* p`, so
   `[p,q]_* proper_subset [s,q]_*`.
3. **Exact backtrack:** `s=p`, hence `I_2=I_0`. The intermediate configuration is the heavy Hasse bridge
   `p lessdot r`, `q||p,r`, `p prec_* q prec_* r`,
   with the exact cell partition of Theorem 3.1 and middle mass `H>E/3`; in the low-endpoint subbranch it has `H>5E/11`.

**Proof.** The total order `prec_*` compares `s` and `p`. Both are strictly before `q`. Hence there are exactly three possibilities: `p prec_* s`, `s prec_* p`, or `s=p`. The first gives strict interval containment in direction (1), the second gives strict interval containment in direction (2), and the equality case is literal return to `(p,q)`. The heavy-bridge assertions in case (3) are exactly Theorem 3.1 applied to the first right export. `square`

### Theorem 4.2 — left then right switch

The order-dual statement holds. A surviving left export followed by a right export has exactly the same three possibilities: strict span descent, strict two-step envelope expansion, or exact backtrack through the corresponding heavy Hasse bridge.

### Corollary 4.3 — no unclassified local ray switch remains

After the accepted strict-span-descent exit is removed, every two-step genuine ray switch is either

- a strict strong-order envelope enlargement, or
- an exact backtrack through a lead-type heavy Hasse bridge.

In particular, the account02/B10 `>1/12` export cannot execute a locally neutral ray change that is neither enlargement nor literal return.

## 5. Integration with existing anti-return mechanisms

The exact-backtrack case is not automatically solved, but it is now placed inside a previously developed normal form.

If its endpoint minorities are both `<3/11`, Theorem 3.1 gives `H>5E/11`. Whenever the repeated-exact-two hypotheses of account01/B11 hold, its exact identity

`2(delta_R+delta_L)=11H-5E+s_R+s_L`

therefore forces a strictly positive outward-gain side. Thus a low-endpoint exact backtrack cannot be a neutral return **inside that exact-two corridor**.

If the endpoint minority is `>=3/11`, the state exits to the already isolated high-endpoint near-balance regime. What remains genuinely unpaid in the exact-backtrack case is therefore the non-exact / multi-distinguisher heavy-cover branch, not an arbitrary ray switch.

Separately, account01/B10's fixed-ray potentials control any maximal run of same-ray exports before or after a switch. Thus any hypothetical global recycler must alternate finite monotone same-ray stretches with strict envelope expansions or with the exact-backtrack heavy bridges above.

## 6. Articulation-mediated reuse is also narrowed

Account02/B11 r18 proves that, after strict span descent is exhausted, an incomparability articulation cannot hide an arbitrarily long ordinal corridor: only a two-boundary interface or a two-boundary-plus-one-leaf interface remains. Therefore if a strict envelope expansion or exact heavy-backtrack is mediated through a cut vertex of the incomparability graph, multi-level corridor reuse is already excluded. A surviving global recycler must use one of those residual interfaces or operate inside a 2-connected incomparability block.

This is a direct application of that theorem; it is not a claim that the two residual cut shapes are solved.

## 7. New first essential remaining implication

The first unpaid global statement is now sharper than `POS3-RAY-SWITCH-CHARGE-ACCOUNTING-v1`:

> **`POS3-CROSS-ENVELOPE-BACKTRACK-EXIT-v1`.** In a span-descent-exhausted no-balanced width-three candidate, prove that a sequence of outward four-channel exports cannot recycle by combining strict strong-order envelope expansions with non-exact/multi-distinguisher exact-backtrack heavy bridges. Equivalently, show that either an expansion cannot later reuse a previously exposed envelope, or the first such reuse transfers enough exact charge to produce a balanced pair, a proper autonomous/ordinal reduction, or one of the already controlled exact-two/non-crossed exits.

The articulation-corridor theorem reduces any cut-mediated instance of this statement to the two residual boundary interfaces; otherwise the obstruction lies in a 2-connected incomparability block.

This is a genuine remaining implication. The present run does **not** establish a global monotone potential across arbitrary envelope expansions, so POS3 remains open.

## 8. Status and integrity

- account04/B10 r17 typed same-ray reduction: **CONSUMED/APPLIED**;
- account02/B10 four-channel transposition export `>1/12`: **CONSUMED/APPLIED**;
- account01/B10 fixed-ray total-order potential: **CONSUMED/APPLIED**;
- account01/B11 repeated exact-two heavy-gap anti-return: **CONSUMED/APPLIED under its exact hypotheses**;
- account02/B11 articulation-corridor reduction: **CONSUMED/APPLIED**;
- every surviving outward export recreates a lead-type heavy Hasse bridge: **PROVED**;
- exact three-cell formulas (3.2)-(3.4) and `H>E/3`: **PROVED**;
- low-endpoint export gives `H>5E/11`: **PROVED**;
- two-step opposite-ray switch trichotomy: **PROVED**;
- generic locally neutral ray switch: **ELIMINATED**;
- global cross-envelope reuse / non-exact exact-backtrack exit: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- inherited `n_bal=14`: **UNCHANGED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No computation was needed for these arbitrary-size implications. No benchmark material, held-out answers, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive data, paid or remote model/API/Codex execution, workflow dispatch, permission change, or public posting was used.
