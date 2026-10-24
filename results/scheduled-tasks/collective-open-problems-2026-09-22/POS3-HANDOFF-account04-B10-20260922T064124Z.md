# POS3 source-bound handoff — account04/B10 r16

Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent POS3 status: `OPEN / NOT PROVED`  
Inherited finite frontier: `n_bal=14` unchanged  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## Source-bound scientific artifact

- Repository: `yspennstate/math-open-problems`
- Report: `proofnet24/collective-POS3/account04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md`
- Science commit: `f168b1f11b4b5d2d7fce0e1bc977d28cbb654c48`
- Report blob: `78e86dcdaef62417888ef6d8b66bf3b6d062f2c9`

## New theorem

At the lead heavy cover `x lessdot y`, with `a||x,y`, `x prec_* a prec_* y`, and no strict strong-majority span descent inside `(x,a)` or `(a,y)`, every canonical Hasse swap-defect mark from the account03/B11 decomposition can be re-anchored without losing a marked full extension to a fully outward boundary pair:

- every left-ray blocker in `F2 union F4` is charged to the minority event `{x<r}` of the incomparable pair `(r,x)`, with `r prec_* x`;
- every right-ray blocker in `F1 union F3` is charged to the minority event `{r<y}` of the incomparable pair `(y,r)`, with `y prec_* r`.

Thus the first heavy-edge export never uses the interior point `a`; the charged pair's entire strong-order interval lies on an outer ray.

In the low-endpoint branch `A,C<3E/11`, account04/B20's separate exact bad-swap bounds give

`|B_L| >= H-A = E-2A-C > 2E/11`,
`|B_R| >= H-C = E-A-2C > 2E/11`.

Account03/B11 compresses each side to at most three Hasse witness vertices. Hence one left-swap witness and one right-swap witness each receive `>2E/33` marked full extensions. Account04/B20 proves the two active-blocker vertex sets are disjoint, so these give two distinct fully outward actual incomparable pairs, each with minority probability `>2/33`. The scale `2/33` is exactly the partner account01/B11 gap `1/3-3/11`.

If both selected packets lie on the same strong-order ray, their blocker vertices are either comparable, giving nested boundary-minority events, or incomparable, in which case the common boundary endpoint and the two blockers form a width-saturating three-antichain. This exhausts the immediate same-ray local geometry.

## Exact peer results consumed

- account01/B11 `20260922T051731Z-b11-pos3-r11`, blob `bba2357120a72c7e2d473dd23095240f61e2f266`: repeated exact-two actual-pair selector `>=3/11` and exact remaining gap `2/33`.
- account03/B11 `20260922T061153Z-account03-B11-pos3-r11`, blob `007674a740f490d5c90b2820dadde4d5ee48de52`: exact heavy-gap swap-defect identity, Hasse realization and width-three `(1,2,2,1)` channel compression.
- account04/B20 `20260922T054301Z-b20-auto11-pos3`, blob `47c3315fbc0f05e501a9e49c6f305d6711ffed50`: separate left/right bad-swap lower bounds and disjoint active-blocker vertex sets.

## First remaining implication

`OUTWARD-STATE RECYCLING`: starting from the two boundary-anchored `>2E/33` packets, prove that successive fork/exact-two/crossed/non-crossed transitions cannot cycle among outward states without producing a balanced pair, strict strong-majority span descent, a proper autonomous/ordinal reduction, a four-antichain, or a controlled multi-distinguisher exit carrying the exact charge onward. In the same-ray case it suffices to treat the nested-channel and width-saturating-three-antichain alternatives above.

No computation was used in this run. No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid model/API/Codex calls, remote workflows, public posting, permission changes, notification enablement or production-brain mutation were used or claimed.
