# POS3 account03/B11 — third-distinguisher localization and exact shadow-cover charge

**Run:** `20260922T044349Z-account03-B11-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `a,b` with `1/3 <= Pr(a<b) <= 2/3` under the uniform law on all linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run implements `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact account03/B11 assignment is to use a distinct order-polytope/correlation method to improve the decisive pair-selection statement; the named partner is `account04/B19`. No installation or benchmark work is resumed.

## 1. Exact inherited state used

The required named OTHER-account result consumed and applied is:

- `account04/B19`, `proofnet24/collective-POS3/account04/B19/B19-20260922T041629Z-auto11/REPORT.md`, blob `1dd0349a2fd05e0f0765d3e6db5ebb5a59ca9d7e`.

Its amplified outer-fringe theorem starts from the live crossed singleton configuration

`Pred(y)\Pred(x)={d}`, `Succ(x)\Succ(y)={u}`,

with

`d lessdot y`, `x lessdot u`, `d prec_* x prec_* y prec_* u`, and `d||u`.

For the outer pair `(d,u)` it proves

`Pred(d) subseteq Pred(u)`, `Succ(u) subseteq Succ(d)`,

`x in Pred(u)\Pred(d)`, `y in Succ(d)\Succ(u)`,

and

`Pr(d<u)>5/6`.

It also proves that the outer pair cannot have only the two distinguishers `x,y`: that reciprocal-singleton case would make `{d,x,y,u}` an autonomous induced `2+2`, forbidden in a cardinality-minimal counterexample (or directly balanced if it is the whole poset). Hence at least one further outer distinguisher exists.

The newest team-lead state used is:

- `account04/B10`, `proofnet24/collective-POS3/account04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

It isolates the remaining global problem as a charge/flux upgrade: turn local `>1/6` crossing mass or repeated bridged Hasse forks into a balanced pair, span descent, or an ordinal/autonomous reduction. The present result localizes exactly what the partner's mandatory third distinguisher can do and produces an exact `>1/3` cover-crossing charge in the shadow case.

The immediately preceding account03/B11 report is:

- `proofnet24/collective-POS3/account03/B11/20260922T040957Z-account03-B11-pos3-r11/REPORT.md`, blob `fd48b47637ca81a6c25fa5c52f8898e596662062`.

It proves that the incomparable-fringe exact-two mechanism amplifies bias by more than `1/6`, so it cannot repeat consecutively.

## 2. Outer fringe notation

Keep the partner hypotheses and define the outer discrepancy sets

`D = Pred(u)\Pred(d)`,
`U = Succ(d)\Succ(u)`.

The original singleton covers immediately imply two facts that are useful but were not yet extracted in the partner report:

### Lemma 2.1 — the inherited inner witnesses are already canonical outer fringe points

`x` is a maximal member of `D`, and `y` is a minimal member of `U`.

### Proof

We know `x in D` and `x lessdot u`. If `x<z` for some `z in D`, then `x<z<u`, contradicting the cover `x lessdot u`. Hence `x` is maximal in `D`.

Dually, `y in U` and `d lessdot y`. If some `z in U` had `z<y`, then `d<z<y`, contradicting `d lessdot y`. Hence `y` is minimal in `U`. `square`

Since every maximal member of `D` is incomparable with `d`, `Max(D) union {d}` is an antichain; width at most three gives `|Max(D)|<=2`. Dually `|Min(U)|<=2`. Every `l in Max(D)` is a lower cover of `u`, and every `r in Min(U)` is an upper cover of `d`: an intermediate point would lie in the same discrepancy set and contradict maximality/minimality.

Thus any additional outer distinguisher is either a genuinely second canonical blocker, or it lies behind the inherited canonical point `x` or `y`.

## 3. Lower third-distinguisher dichotomy

Let `z in D\{x}`.

Because `x` is maximal in `D`, `x<z` is impossible. Thus either `z||x`, or `z<x`.

- If some such `z||x`, extend `z` upward inside `D` to a maximal element `l`. Then `l!=x`, so `Max(D)={x,l}` or contains these two, and width three forbids a third. Moreover `l lessdot u`. This is a genuine **second canonical lower blocker**.

- Otherwise every additional lower distinguisher lies below `x`. Choose `z` maximal in `D\{x}`. Then in fact

  `z lessdot x`.                                                (3.1)

  Indeed, if `z<t<x`, then `t<u`. We cannot have `t<d`, since that would force `z<d`, contrary to `z in D`; and we cannot have `d<t`, since `d<t<x<u` would force `d<u`, contrary to `d||u`. Hence `t||d`, so `t in D\{x}`, contradicting maximality of `z`.

Now use the strong-majority order. We already have `d prec_* x`. Since `z<x` in the poset, also `z prec_* x`.

If `d prec_* z prec_* x`, the incomparable pair `(d,z)` is a strict strong-majority span descent inside the flank `(d,x)`. Otherwise, in a no-balanced counterexample the only remaining orientation is

`z prec_* d prec_* x`.                                         (3.2)

This orientation has an exact extension-multiplicity consequence.

### Theorem 3.2 — lower shadow cover carries more than one third of all extensions

Let `N=e(P)` be the total number of linear extensions. Under (3.1)-(3.2),

`#{L : z<d<x in L} = #{L:d<x} + #{L:z<d} - N > N/3`.           (3.3)

Equivalently,

`Pr(z<d<x)>1/3`.                                                (3.4)

### Proof

Since `z<x` is forced by the poset, every extension with `d<x` lies in exactly one of the disjoint events `d<z<x` and `z<d<x`. The first event is exactly `{d<z}`. Therefore

`N(z<d<x)=N(d<x)-N(d<z)=N(d<x)+N(z<d)-N`.

The no-balanced strong orientations `z prec_* d` and `d prec_* x` give

`N(z<d)>2N/3`, `N(d<x)>2N/3`,

so the right side is strictly larger than `N/3`. No induced extension law is used. `square`

This is an order-polytope volume identity as well: normalized counting measure on linear extensions is the chamber decomposition of the order polytope, and (3.3) is simply the exact volume inclusion-exclusion for two nested comparison half-spaces.

## 4. Upper third-distinguisher dichotomy

The dual statement is exact.

Let `w in U\{y}`. Either some such `w||y`, in which case a minimal element `r` below it gives a second canonical upper blocker `r!=y` with `d lessdot r`; or every upper extra lies above `y`. In the latter case choose a minimal such `w`, obtaining

`y lessdot w`.                                                  (4.1)

Because `y prec_* u` and `y prec_* w`, either `y prec_* w prec_* u`, which is a strict span descent inside `(y,u)`, or else no descent forces

`y prec_* u prec_* w`.                                         (4.2)

Then exact multiplicities give

`#{L : y<u<w in L} = #{L:y<u} + #{L:u<w} - N > N/3`,           (4.3)

so

`Pr(y<u<w)>1/3`.                                                (4.4)

## 5. Third-distinguisher localization theorem

Combine Sections 2-4 with the partner's theorem that `(D\{x}) union (U\{y})` is nonempty.

### Theorem 5.1 — amplified outer pair cannot hide its mandatory third distinguisher

In the partner's amplified incomparable-fringe branch of a hypothetical cardinality-minimal width-three counterexample, where `Pr(d<u)>5/6`, at least one of the following occurs:

1. **strict strong-majority span descent** on one of the two flanks `(d,x)` or `(y,u)`;
2. a **second canonical outer blocker**, i.e. `Max(D)` contains a second member besides `x`, or `Min(U)` contains a second member besides `y`; this second blocker is respectively a Hasse predecessor of `u` or Hasse successor of `d`;
3. a **heavy shadow-cover crossing**: there is a Hasse edge `z lessdot x` with `Pr(z<d<x)>1/3`, or a Hasse edge `y lessdot w` with `Pr(y<u<w)>1/3`.

### Proof

The partner guarantees at least one extra element of `D` or `U`. Apply the lower or upper dichotomy above to that side. `square`

This pays the first localization step in the partner's stated “amplified outer-fringe charge” obligation. The previously vague `>=3`-distinguisher residual is now forced into one of two concrete width-three transport objects after span descent is removed: a second canonical Hasse blocker, or an exact Hasse-cover crossing carrying more than one third of all extension mass.

## 6. Exact adversarial calibration

The conclusion is not vacuous. There is an eight-element width-three poset with the transitive relation

`0<2, 0<3, 0<4, 0<5, 0<6, 0<7,`
`1<4, 1<6, 1<7,`
`2<6, 2<7,`
`3<5, 3<6, 3<7,`
`4<6, 4<7, 5<7, 6<7`.

It has exactly `N=60` linear extensions. With

`(x,y,d,u,z,w)=(3,4,1,5,0,6)`,

the exact counts are

`N(x<y)=44`, so `Pr(x<y)=11/15`,
`N(d<u)=55`, so `Pr(d<u)=11/12`,
`N(z<d)=42`, `N(d<x)=41`,
`N(z<d<x)=23`,
`N(y<u)=41`, `N(u<w)=42`,
`N(y<u<w)=23`.

Thus both shadow fringe pairs themselves are extreme (`42/60>2/3`), yet each exact cover-crossing charge is

`23/60 > 1/3`.

So the theorem genuinely improves the residual: one cannot replace the shadow case by the false hope that an extra shadow immediately gives a balanced pair. The correct invariant is the heavy three-point cover-crossing mass.

This eight-point poset is not a POS3 counterexample; it contains balanced incomparable pairs. It is used only to show that the new heavy-charge alternative is a real branch rather than a proof artifact.

## 7. Deterministic verification

`verify_shadow_cover_charge.py`, blob `f54b0e37838ce43f25c63b3f33cd2f59179ecc40`, checks the structural classification and exact sandwich identities. It exhausts every transitively closed naturally labelled width-at-most-three poset through `n=6`, scans the exact crossed-singleton strong configurations, and separately verifies the eight-point calibration above.

Captured output, blob `5396d136f8d7dbf23a09375e0f78046dc09cfc35`, ends

`POS3_SHADOW_COVER_CHARGE_CHECK_PASS`.

The exhaustive small cases contain 14 crossed exact-two strong configurations at `n=6`; their shadow fringe pairs already fall into the balanced regime, so the no-balanced heavy-orientation premise does not activate there. The eight-point calibration is included specifically to exercise the strict heavy-charge branch.

The verifier is regression evidence for the algebraic theorem, not a finite proof of POS3.

## 8. Remaining first obligation

The first missing implication is now narrower and directly aligned with the team lead's global flux programme:

> **Heavy-cover / second-blocker charge propagation.** In a cardinality-minimal width-three counterexample with no span descent, show that a canonical second Hasse blocker or a cover edge carrying `>1/3` sandwich mass cannot propagate through the three-chain corridor without producing a balanced pair, a four-antichain, or a proper autonomous/ordinal reduction.

The new `>1/3` sandwich mass is already at the target threshold; what is missing is a valid conversion from a three-point event such as `z<d<x` to the ordering probability of one incomparable pair. Any next step should preserve exact extension multiplicities rather than replace the induced corridor law by a uniform law.

## 9. Status and integrity

- named partner account04/B19 amplified outer-fringe theorem: **CONSUMED/APPLIED**;
- inherited witnesses `x,y` are canonical outer fringe points: **PROVED**;
- every extra distinguisher localizes to second canonical blocker or shadow behind `x/y`: **PROVED**;
- maximal/minimal shadow becomes an adjacent Hasse edge: **PROVED**;
- no-descent shadow carries exact sandwich mass `>1/3`: **PROVED**;
- mandatory third distinguisher therefore gives span descent, second canonical blocker, or heavy cover crossing: **PROVED**;
- full POS3 target: **OPEN / NOT PROVED**;
- run classification: `ESSENTIAL_STEP_APPLIED`.

Scoped privacy/provenance review: these files contain mathematical statements, repository-relative source references, Git object identifiers, deterministic standard-library verifier code/output, and nonsecret run labels only. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive material, paid model/API/Codex calls, remote workflows, public-posting actions, permission changes, or production-brain mutation are present.
