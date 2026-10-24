# POS3 handoff — account01/B11

**Run:** `20260922T081324Z-b11-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent POS3:** OPEN / NOT PROVED  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

Canonical report: `proofnet24/collective-POS3/account01/B11/20260922T081324Z-b11-pos3-r11/REPORT.md` in `yspennstate/math-open-problems`, report blob `369bdbc02461f4a6a1c8b67d026f159766b20443`, report-write commit `41a9570d95f99b83ee088bf05bbde33b764dc05c`.

Latest lead consumed: account04/B10 r18, blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`. Assigned partner consumed/applied: account02/B19 r11 main blob `3dda5f9df837b64f7cf7fc6103eb353284ca60dd` plus addendum blob `d0eba0343a375499b460fd29336064c81d16cfc0`.

## New arbitrary-size lemma

At a low-endpoint heavy bridge `x lessdot y`, `a||x,y`, `x prec_* a prec_* y`, with `A,C<3E/11`, deterministically assign every bad left swap to the canonical families `F1 union F2` and every bad right swap to `F3 union F4`. After balance and strict strong-majority span descent are excluded, the **entire positive assigned support** purifies into exactly one of two modes:

1. **through-a:** only `F2/F3` are positive;
2. **fork-fork:** only `F1/F4` are positive.

Reason: positive `F1` together with positive `F3` gives two actual right-ray boundary pairs sharing `y`, hence balance or a strict subspan; positive `F2` together with positive `F4` gives the dual left-ray exit. Since both bad-swap sides have positive mass, no third support pattern survives.

## Quantitative consequences

- Through-a mode: `|F2|,|F3|<=2` and `|B_L|,|B_R|>2E/11`, hence one actual boundary pair on each side has minority `>1/11`; all cross blockers satisfy `t<a<u` in the poset. Using the inherited variance bound, selected packet strong-order radius is at most `4834`.
- Fork-fork mode: `|F1|,|F4|<=1`, so the unique blockers carry the full side defects, each `>2E/11`. Four actual pair minorities (`b<a`, `b<y`, `x<c`, `a<c`) are all `>2/11`. Also `A,C>13E/66` and `5E/11 < H < 5E/9`; packet radii are at most `3418`.
- In fork-fork mode, if `D=B_L cap B_R`, then `|D|>=2H-E`, and every `D` extension has `x<b<a<c<y`. Thus if `H>E/2`, the fork blockers must be incomparable and `Pr(b<c)>=2H/E-1`; if `H<=E/2`, then `A,C>5E/22`.

## Assigned-partner check

The exact account02/B19 108-extension core reconstructs as `F1=[]`, `F2=[6]`, `F3=[7]`, `F4=[3]`, with `lambda_6=23`, `rho_7=19`, `rho_3=6`. Its forbidden same-left-ray `F2/F4` mixing is resolved exactly by the balanced cross-pair `Pr(3<6)=60/108=5/9`. Verifier marker: `POS3_ACTIVE_SUPPORT_PARTNER_CHECK_PASS`.

## First unpaid implication

`POS3-PURE-MODE-CROSS-ENVELOPE-EXIT-v1`: rule out r18 cross-envelope recycling separately in (i) through-a reciprocal cover-pivot mode with packet floor `>1/11` and comparable cross blockers, and (ii) unique fork-fork mode with full-side floor `>2/11` and the double-bad lower bound above. A successful closure must yield balance, strict span descent, a proper autonomous/ordinal reduction, or an already controlled exact-two/non-crossed exit.
