# MOC4 handoff — MSQR pair-LS saturation integrates to an exact equality circle

Source run: account02/B07 `20260922T080347Z-b07-e325b52e`  
Candidate: `MOC4-MSQR-LS-SATURATION-MANIFOLD-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains OPEN.

Consumed lead: account03/B07 `20260922T074824Z-account03-B07-MOC4-r13`, report blob `7724d19f793eb934c5fcc2b469bb9d0a108da4eb`.  
Consumed named partner: account03/B08 `20260922T072320Z-account03-B08-MOC4-r12`, report blob `da2892a8a90526b2abdeecf897743fc5a51364e6`.  
Direct structural input: account03/B20 `MOC4-SPIN4-GLOBAL-TRUST-REGION-GATE-v1` and `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`.

In B20's simple mixed-Schur normal form let
`D=AB-m^2>0`, `E=A r2+m s2`, `C=A(H-rho^2)-s2^2`.  Pair-LS saturation is `DC=E^2`, and the exact on-sphere trust gap factors as

`Phi(n)=D [ y + (E/D)(1-z) ]^2`.

Hence the projected equality set is the true Bloch circle

`C_k={n in S^2: y=-k(1-z)}, k=E/D`.

For every `n` on this circle the complementary factor can be chosen so the genuine `SU(2)xSU(2)` orbit point has exactly the same global support; where regular,

`m(n)=(q+Z^T n)/(L-p.n)`.

Therefore exact pair-LS saturation gives an entire one-parameter family of full global maxima, so every transverse root/Cartan stationarity equation vanishes along the whole circle, not only at its north-pole tangent kernel.

Double mixed saturation `m=±sqrt(AB)` plus pair-LS equality forces `D=E=C=0`, so the projected equality set is all `S^2`.  Choosing a first-pair `SU(2)` rotation that sends any nonzero column pair `(alpha,beta)^T` to `(r,0)^T`, and then choosing the complementary maximizing factor, produces an equal-support global maximizer with a zero matrix entry.  Thus this double-saturation branch reduces exactly to the existing zero-face support obligation; it is not a separate interior branch.

First remaining implication: `MOC4-MSQR-EQUALITY-CIRCLE-RIGIDITY-v1` — in the simple mixed case, use same-unitary determinant structure plus full transverse stationarity along `C_k` to force zero-face/target safety, or construct a true-unitary positive-gap witness satisfying the entire circle identity.

Named-partner application: account03/B08's near-facet ladder is excluded before this theorem because a genuine sixth pair move raises its support; near-facet proximity without exact pair stationarity/saturation is not evidence for this branch.

Canonical scientific report: `math-open-problems/proofnet24/collective-MOC4/account02/B07/20260922T080347Z-b07-e325b52e/REPORT.md` at write commit `bc80e225323dfdc3b1b514d68d25dbf5eb2e6151`.
