# B16 handoff — shared-graft tail is now closed

**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI remains **OPEN / NOT PROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific report:
`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T0143Z-shared-graft-tail/REPORT.md`.

Named peer consumed: account03/B18 `20260922T011005Z-recursive-shared-graft-extension`, report blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`. Its exact recurrence

\[
I'=261/128+(9/256)(I^4-1),\quad
c'=57/256+c^4/256,
\]
\[
R'=(1-w)R+wT(c),\qquad
w=(133/128)/(I'-1),\quad
T(c)=(128/133)K(c^4)
\]

has now been controlled for **all later rounds**, not just another finite round.

New theorem: for every `t>=4`,

\[
6.5218511672903366960<T(c_t)<6.5218511674053080982.
\]

The next genuine balanced gate satisfies

\[
6.5218509495504459457761<R_5<6.5218509495504459458552,
\]

hence

\[
C_{FEI}>6.5218509495504459457.
\]

All later `R_t` increase strictly, but the **entire** remaining gain after `R_5` is less than `4.024264e-15`; in particular

\[
R_\infty<6.521850949550449970119<6.5218509495504501.
\]

So repeated certification of this exact shared-graft recurrence is now mathematically exhausted: it cannot materially raise the FEI lower floor beyond `6.52185094955045`. The successor obligation is an upper-bound mechanism for the universal all-gate inequality (retaining signed child continuation), or a genuinely different stronger gate construction.

Checker committed beside the report; locally executed source returned `PASS`. No public posting, email, scheduler, permission, or notification mutation was made.
