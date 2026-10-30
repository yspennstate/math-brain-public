# POS3 B19 r46 handoff

Outcome: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains OPEN.

Consume together:

- `REPORT.md`, blob `3ab26879c6f8301fa782a8ee1d2fbd47dca150a7`;
- `CORRECTION_DIRECT_SPLICE_SCOPE.md`, blob `5f693edf2ef6aaa6e9eba33cacb28339e49be671`.

Latest lead consumed: fleet04/B10 r18, blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.
Required OTHER-account partner consumed: fleet01/B10 r13, blob `907ef9d19e23c05bc68a13c34ddb5a4aad6e30df`.

New proved step, with the correction's direct-splice scope: for a heavy bridge `(ell,m,r)`, partner-r13 heavy-child transitions strictly lower either `rho(r)` or `rho(ell)`. A direct same-cover right-boundary span splice changes the middle to `u` with `rho(u)>rho(m)`, so

`Phi_R=(rho(r),rho(ell),-rho(m))`

strictly decreases. A direct same-cover left-boundary span splice has `rho(u)<rho(m)`, so

`Phi_L=(rho(r),rho(ell),rho(m))`

strictly decreases. Hence no cycle can consist only of partner heavy-child transitions plus direct same-cover splices taken always from one fixed boundary side.

Not proved: arbitrary delayed returns to the same cover, alternating-side direct same-cover bounces, or cover-changing span splices.

Next exact target: `POS3-ALTERNATING/COVER-SWITCH-SPLICE-v1`: pay the first side change or Hasse-cover change by forcing balance, a strict smaller span, a proper autonomous/ordinal reduction, or a charged outside-envelope exit already controlled by the fixed-ray machinery.
