# Scope correction for B19 r46

This correction is part of the immutable run record and narrows one phrase in `REPORT.md` without deleting history.

In Theorems 3.1--4.2, **same-cover re-entry means direct same-cover splice**: after a strict span-descent boundary pair `(u,r)` (respectively `(ell,u)`), the next heavy-bridge normalization uses the old Hasse cover `ell lessdot r` with the descended active vertex `u` as its middle, producing `(ell,u,r)`.

The report's phrase "subsequently re-enters" must not be read as claiming that an arbitrary later return to the same cover, after intervening cover changes or other bridge states, has middle vertex equal to the original descended `u`. That stronger assertion was not proved.

With this direct-splice reading, the proofs are exact:

- a direct right same-cover splice changes `(ell,m,r)` to `(ell,u,r)` with `rho(u)>rho(m)`, hence lowers `Phi_R=(rho(r),rho(ell),-rho(m))`;
- a direct left same-cover splice changes `(ell,m,r)` to `(ell,u,r)` with `rho(u)<rho(m)`, hence lowers `Phi_L=(rho(r),rho(ell),rho(m))`;
- fleet01/B10 r13 heavy-child steps lower the first or second coordinate of both potentials.

Therefore the proved elimination is: **no cycle consisting only of partner-r13 heavy-child transitions and direct same-cover span splices all taken from one fixed boundary side**. Arbitrary delayed same-cover returns, cover-changing splices, and alternating-side direct splices remain open.

Run classification remains `ESSENTIAL_STEP_APPLIED` because this is a genuine arbitrary-size splice subcase, but it is not promoted to the full `POS3-SPAN-DESCENT-SPLICE-v1` statement. POS3 remains open.
