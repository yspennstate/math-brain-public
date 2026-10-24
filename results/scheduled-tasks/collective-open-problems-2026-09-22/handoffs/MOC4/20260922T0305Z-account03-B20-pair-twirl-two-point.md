# MOC4 handoff — account03/B20 pair-twirl two-point bound

Run: `20260922T025001Z-B20-moc4`  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Candidate: `MOC4-PAIR-TWIRL-TWO-POINT-v1` + quantitative pair-curvature collar.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report: `proofnet24/collective-MOC4/account03/B20/20260922T025001Z-B20-moc4-r12/REPORT.md` in `yspennstate/math-open-problems`; creation commit `c83299dfda42613c5b66374e71dff792cee8d115`, report blob `e0dfc532a2c4f9c8eedf8520f6f449f39f4a385b`. Arithmetic verifier blob `88a9ce1d9c0f779a28ff0a4324043c707e98ba43`; verification-output blob `67520a2d70da96e4083a588ce0c507462243020e`.

## Named cross-account result consumed

Assigned partner **account04/B09**, `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`, report blob `1ec092caac4aa78fb3998199849f632387a0c18f`: Haar-averaging the complete exterior-minor data along any genuine row-pair `SU(2)` orbit gives an exact probability lift to the 24 `S4` endpoint data. I combine this with account04/B08's exact affine Bloch-sphere formula for pair orbits and account02/B07's transposition class sum / pair-Hessian trace.

## New exact theorem

For every true unitary `U`, every row transposition `tau`, every column transposition `tau`, every spectra and every support direction, if `M` is the maximum of the 24 target endpoint support values, then

`h(U)+h(tau U) <= 2M`,
`h(U)+h(U tau) <= 2M`.

Proof: on the pair sphere `h=alpha+c.n`; antipodal identity/transposition values sum to `2 alpha`; Haar average is `alpha`; the assigned partner's exact Haar lift places that average in the target endpoint hull.

This is unconditional in `U`: no maximizer, stationarity, simple spectrum, nonsingularity or arbitrary bistochastic surrogate is used.

## Quantitative target consequence

If a global true-unitary maximizer violates support by gap `gamma=h(U*)-M>0`, then for each of all twelve row/column pair swaps

`h(U* tau) <= M-gamma`, hence `h(U*)-h(U* tau) >= 2 gamma`.

Thus every pair sphere is quantitatively strict, not merely nonflat.

In exact Spin(6) nonconstant notation `s=k+x`, `c=<1,X>/6`, account02/B07 gives

`sum_{tau transposition} s(U P_tau)=2k+6c`.

Summing the six new two-point inequalities gives the universal true-unitary bound

`4k+3x+3c <= 6 M_even`, equivalently

`s(U)-M_even <= [2k+3(x-c)]/6`.

At a pair-stationary point, using `Tr H_pair=-8[2k+3(x-c)]`,

`s(U)-M_even <= -Tr H_pair/48`.

Therefore a gap-positive global maximizer satisfies exactly

`2k+3(x-c) >= 6 gamma`,
`Tr H_pair <= -48 gamma`.

This strengthens the previous necessary inequality `2k+3(x-c)>=0` and directly couples target violation size to true-unitary pair curvature.

## Combined surviving branch

Combine with account02/B07's odd-overlap collar and account02/B09's Cartan polarization:
- all 12 pair-swap gaps are >= `2 gamma`;
- every odd-Weyl deficit is >= `gamma^2/(24 W^2)`;
- on the zero-endpoint-safe Cartan branch, every entry obeys `sqrt(gamma/(4W)) <= |u_ij| <= 1-sqrt(gamma/(4W))`;
- flat pair orbits are already target-safe by the assigned partner.

The surviving hypothetical counterexample is therefore a quantitatively compact strict interior global maximizer satisfying full Spin(6) stationarity, not merely a generic pair-strict point.

## First unpaid implication / next recipients

`MOC4-STRICT-COMPACT-INTERIOR-v1`: exclude a structured-support global maximizer satisfying the exact Spin(6) stationarity equations together with all three quantitative collars above. If a Cartan zero endpoint is itself violating, the genuine zero-entry support branch remains instead; do not attempt another unconditional common-minor positive lift.

Primary recipients: account03/B07 campaign lead and assigned partner account04/B09. Also directly useful to account02/B07 (curvature/odd collar), account02/B09 (Cartan collar), and account01/B07 (stationarity equations).

No benchmark material, credentials, scheduler identifiers, machine-local data, email/Drive data, public posting, paid model/API, Codex or remote workflow was used.
