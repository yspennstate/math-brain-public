# Source-bound handoff — account04/B19 POS3 r11

**Run:** `B19-20260922T081503Z-r11`  
**Status:** `ESSENTIAL_STEP_APPLIED`; parent POS3 remains **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## Exact artifacts to consume

1. Main run report: `proofnet24/collective-POS3/account04/B19/B19-20260922T081503Z-r11/REPORT.md`.
2. Lead-r18 reconciliation: `proofnet24/collective-POS3/account04/B19/B19-20260922T081503Z-r11/LEAD_R18_RECONCILIATION.md`, Git blob `06983ae01ea38228ca94355cc1c9e2538d49dd78`.
3. New decisive addendum: `proofnet24/collective-POS3/account04/B19/B19-20260922T081503Z-r11/ADDENDUM_GLOBAL_OUTSIDE_BACKTRACK_BYPASS.md`, Git blob `b56486c3c1fcace42c685686ab4897a797758611`, commit `d09d5ece11394c2ed216a56615850009669f0389`.

The addendum consumes:

- campaign lead account04/B10 r18, report blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`;
- assigned partner account01/B10 `20260922T072132Z-b10-pos3-r11`, report blob `85fa62968e584b5db7fe6270260f55f92c071438`;
- newer account02/B10 r12 exact-backtrack double-leak theorem, science commit `57a563af112063929fae35a4aa28c4fe61aa64cf`.

## New theorem to reuse

In a low-endpoint exact-backtrack heavy bridge

`p lessdot r`, `q||p,r`, `p prec_* q prec_* r`,

with `Pr(r<q),Pr(q<p)<3/11`, assume the no-balanced hypothesis and that strict strong-majority span descent is exhausted for both adjacent active pairs `(p,q)` and `(q,r)`.

Then every noncentral Hasse leak channel is globally outside the full bridge interval `[p,r]_*`:

- a channel in `D(p,q)` lies strictly before `p` in `prec_*`;
- a channel in `U(p,q)\{r}` lies strictly after `r`;
- a channel in `D(q,r)\{p}` lies strictly before `p`;
- a channel in `U(q,r)` lies strictly after `r`.

Account02/B10 r12 guarantees a noncentral channel for the *current* pair `(q,r)` carrying `>2E/33` marked full extensions. Select it instead of the central backtrack channel `p`.

- If it is in `U(q,r)`, the alternative step is `(q,r)->(r,z)` with `r prec_* z`; it stays on the right ray and strictly increases account01/B10's `Psi_R`.
- If it is in `D(q,r)\{p}`, the alternative step is `(q,r)->(z,q)` with `z prec_* p`; it is a strict opposite-ray envelope expansion, not an exact return.

The order-dual statement holds for a left-then-right exact backtrack.

**Operational mathematical consequence:** a choice-based recursive export never needs to take a literal low-endpoint exact-backtrack edge. The remaining low-endpoint global obstruction is strict outside-envelope reuse across ray switches, not a locally closed or multi-distinguisher exact return.

## First unpaid implication

`POS3-OUTSIDE-ENVELOPE-REUSE-v1`: rule out a span-descent-exhausted no-balanced width-three export sequence in which fixed-ray segments obey the account01/B10 strict integer potential and every ray switch is a strict envelope expansion through a witness outside the preceding heavy bridge. The first reuse of a previously exposed outer strong-order region must be converted into a balanced pair, strict span descent, width-four contradiction, proper autonomous/ordinal reduction, or an already-controlled exact-two state.

The high-endpoint `[3/11,1/3)` branch remains separate. No global acyclicity claim is made yet.
