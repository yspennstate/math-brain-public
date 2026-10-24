# MOC4 handoff — account04/B08 pair-specific endpoint roof

Run: `20260922T031434Z-account04-B08-MOC4-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Candidate: `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`.  
Execution: `WITHOUT_VERIFIED_BRAIN_RESEARCH`.

Scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account04/B08/20260922T031434Z-account04-B08-MOC4-r11/REPORT.md`, creation commit `6cbb25db480704590e30481f161613f0936a0b10`, report blob `0c611698463f4f00abe78c96a10308759d3cb716`. Exact verifier blob `b49a1e730ca9aa1e5c10eb0c2c9d7a262a602488`; captured output blob `ea701f5fa76cee91ed641062c62b4c4b3b430ca7`.

## New exact theorem

Fix a real support direction for the 24 target endpoint values `H_sigma`, with `M=max H_sigma`. For a row transposition `tau`, define

`R_tau^row=max_sigma (H_sigma+H_{sigma o tau})/2`.

For a column transposition define

`R_tau^col=max_sigma (H_sigma+H_{tau o sigma})/2`.

Then every true unitary satisfies

`(h(U)+h(tau U))/2 <= R_tau^row`,

and

`(h(U)+h(U tau))/2 <= R_tau^col`.

Proof: apply B08's preceding `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`, then average the exact lift with its pushforward by the same transposition. The invariant lift decomposes into the twelve two-point permutation orbits, so its support expectation is a convex combination of the corresponding two-endpoint averages.

Consequently every pair roof is at most `(H_(1)+H_(2))/2`, the average of the top two distinct endpoint supports.

## Exact boundary characterization

Let

`g_tau=2M-max_sigma(H_sigma+H_paired_sigma)`.

Then `g_tau=0` iff the maximizing target support face contains an endpoint edge paired by that transposition. Thus nonunique endpoint support alone is not the relevant degeneracy: a tied face with no such transposition edge is still quantitatively strict. A unique maximizing endpoint forces all twelve row/column pair gaps positive.

If a global support maximizer violates the target by `gamma>0`, then

`h(U*)-h(tau U*) >= 2 gamma + g_tau`.

Using account03/B20's exact six-transposition Spin(6) identity, for the six column gaps with sum `G` this strengthens its curvature collar to

`2k+3(x-c) >= 6 gamma + G/2`,

`Tr H_pair <= -48 gamma - 4G`.

If the endpoint support maximum is unique with global gap `delta=H_(1)-H_(2)`, then `G>=6 delta`, hence

`Tr H_pair <= -48 gamma - 24 delta`.

## Named assigned-partner result applied

Applied account01/B09 run `20260922T024937Z-account01-B09-MOC4-r12`, `MOC4-SIMPLE-COMPLEX-EVEN-LIFT-v1` refutation. For its exact dense rational unitary and simple nonreal spectra, in the real-part support direction the top two endpoint values are `256,240`, so `delta=16`. Exact row pair gaps are `186,16,24,168,50,302`; exact column pair gaps are `24,50,412,192,16,168`. The standard-library verifier recomputes the partner determinant and checks all twelve physical pair inequalities exactly. This is a negative control: the partner's universal even-channel lift fails, but the new theorem survives because it only uses the valid pair-symmetrized lift.

## First unpaid implication

`MOC4-GAPPED-STATIONARY-SIX-FIBER-v1`: exclude a global true-unitary support maximizer satisfying the full Spin(6) stationarity system, strict odd-overlap/Cartan conditions, and the positive pair-specific endpoint gaps above, by proving the exact structured six-fiber target support inequality; alternatively construct a genuine target-level counterexample satisfying all of those conditions.

No common-lift shortcut for a single unitary, no benchmark material, no credentials, no scheduler identifiers, no machine paths, no email/Drive data, no paid/remote compute, and no public posting were used.
