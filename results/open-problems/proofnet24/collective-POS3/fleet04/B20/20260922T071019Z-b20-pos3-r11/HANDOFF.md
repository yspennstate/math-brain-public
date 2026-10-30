# POS3 B20 handoff — signed incoming defects cannot return locally

Parent POS3 remains **OPEN / NOT PROVED**. Run classification: `ESSENTIAL_STEP_APPLIED`.

Main report: `proofnet24/collective-POS3/fleet04/B20/20260922T071019Z-b20-pos3-r11/REPORT.md`.

Newest complete lead consumed: fleet04/B10 r16, `proofnet24/collective-POS3/fleet04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md`.

Newest complete designated other-account partner consumed: fleet01/B19 r13, `proofnet24/collective-POS3/fleet01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`. The newer r14 directory was start-only at the source snapshot.

New exact step: the incoming/negative terms `D_A^+` and `D_C^-` in the heavy-cover transposition identities admit canonical Hasse witnesses in four width-three families of size at most two each. Every incoming left mark is losslessly charged to either `(r,a)` with marked minority event `a<r` and `r prec_* x prec_* a`, or `(x,r)` with marked minority event `r<x` and `x prec_* a prec_* r`. The right side is dual: `(a,r)` with `a prec_* y prec_* r`, or `(r,y)` with `r prec_* a prec_* y`.

Therefore every canonical reverse-transposition cancellation moves to a **strict strong-order superinterval**. The directed graph of pure incoming-cancellation steps is acyclic under the integer potential `span_*`; a path beginning at span `s` has at most `n-1-s` further such steps.

At the partner's local threshold, if either incoming side has mass at least `8E/33`, one of at most four strict-superinterval channels carries at least `2E/33` marked minority extensions. In the B10-r16 low-endpoint branch, independently,

`|D_H^-|-|D_A^+|=H-A>2E/11`,

`|D_H^+|-|D_C^-|=H-C>2E/11`.

So negative reverse-swap terms cannot erase the heavy-gap current locally: large cancellation exports a gap-scale superinterval packet; small cancellation leaves a quantitatively positive signed outward current.

Regression: `verify_incoming_superinterval.py`; captured output `verify_incoming_superinterval.out`. It checks every naturally labelled transitively closed width-at-most-three poset through six vertices: 3,699 posets, 24,996 cover/incomparable triples, 63,296 left incoming defects and 63,296 right incoming defects, with zero failures and maximum incoming Hasse-family size two.

**Next exact implication:** MIXED-MECHANISM OUTWARD RECYCLING. Starting from B10 r16's two boundary-anchored outward `>2E/33` packets, prove that alternation among fork/exact-two/crossed/non-crossed/bridge mechanisms cannot evade balance. Any reverse-transposition cancellation strictly increases strong-order span, so a genuine cycle must use another transition type. Combine that fact with width three, the conserved exact-two `K`, and B20's non-crossed staircase half-charge to force balance, strict span descent, a proper autonomous/ordinal reduction, a four-antichain contradiction, or a controlled charge-preserving exit.

Do not promote this to a full proof. No novelty/priority claim is made. `WITHOUT_VERIFIED_BRAIN` remains the correct execution label.
