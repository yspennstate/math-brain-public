# MOC4 source-bound handoff — account04/B09

Run: `20260922T051510Z-b09-moc4-r35`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Canonical scientific report: `proofnet24/collective-MOC4/account04/B09/20260922T051510Z-b09-moc4-r35/REPORT.md` in `yspennstate/math-open-problems`, report creation commit `126eef8c1843137b4e827a013b9ae6667000e420`. Exact verifier: `verify_continuous_biorientation.py`, blob `d3bf01cbb430fd4cb13e7c0ccd732541f85333f0`. Captured exact output: `VERIFY_OUTPUT.txt`, blob `72cd7cb5d035a53a19fff956e6fffb6886539e86`.

Named OTHER-account partner consumed and applied: account01/B07 `MOC4-BIORIENTATION-PAIR-GATE-v1`, canonical report `proofnet24/collective-MOC4/account01/B07/20260922T040155Z-a01-b07-moc4-r12/REPORT.md`. Lead consumed: account03/B07 `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`, report `proofnet24/collective-MOC4/account03/B07/20260922T043708Z-account03-B07-MOC4-r11/REPORT.md`. Also integrated account04/B08 `MOC4-CUBATURE-ROOF-RIGIDITY-v1` published during this invocation, and used account03/B09 `MOC4-CYCLE-SEPARATOR-NOGO-v1` only as an exact negative-control datum.

## New theorem: `MOC4-CONTINUOUS-BIORIENTATION-STATIONARITY-v1`

Write a genuine exterior-square point `O=Lambda^2 U in SO(6)` as real `2 x 2` blocks `B_{alpha beta}`, with

`D_ab=det B_ab`, `R_ab=||B_ab||_F^2/2`, and support

`s(O)=sum_ab [K_ab D_ab + (1/2) X_ab R_ab]`.

At every local/global support maximizer, for each row-plane pair `alpha<gamma` and every real `2 x 2` matrix `Z`, with `A_beta=B_{alpha beta}`, `G_beta=B_{gamma beta}`, one has the exact stationarity identity

`sum_beta [ K_ab q(A_beta,Z G_beta) - K_gb q(G_beta,Z^T A_beta) + (X_ab-X_gb)/2 <A_beta,Z G_beta>_F ] = 0`,

where `q` is determinant polarization. It is enough to impose this for the four orthogonal basis matrices `I,J,S,T`, giving 12 exact scalar equations. These 12 equations are the full first-order `SO(6)` stationarity system modulo the exact three-dimensional block-rotation gauge.

For orthogonal `Z`, `epsilon=det Z`, the whole pair circle satisfies the exact identity

`s(W_Z(theta)O)-s(O) = -sin(theta)^2 (T^L_{alpha gamma}-epsilon C^L_{alpha gamma}) + sin(theta)cos(theta) B^{L,epsilon}_{alpha gamma}(Z)`.

Thus, once stationarity sets the cross term to zero, account01/B07's discrete gate `T^L>=|C^L|` controls the **entire** continuous row-pair circle, not merely the swap endpoint.

## Decisive exact negative control

The genuine `SO(6)` point from account03/B09's cycle-separator no-go passes all three row discrete gates (slacks `4446471/1051250`, `44037/42050`, `818424/525625`) but fails the new stationarity equations: for row pair `(0,1)` and `Z=I`, the derivative is exactly `-27216/18125`.

An exact rational genuine `SO(6)` row-plane rotation with half-angle parameter `t=-1/100`, hence `c=9999/10001`, `s=-200/10001`, raises its separating support by

`59577629088/2102920521025 > 0`.

Therefore that current coefficientwise cycle-separator witness is **not even a local maximizer** for its own separating functional. It remains a valid refutation of the universal coefficientwise endpoint-hull strengthening, but it cannot occur in the global-maximizer residual relevant to MOC4.

## First remaining implication

`MOC4-STRUCTURED-SPIN6-STATIONARY-RIGIDITY-v1`: for structured spectral coefficients `(K,X)`, exclude every genuine positive-gap `O in SO(6)` simultaneously satisfying (i) the 12 exact stationarity equations above, (ii) the six account01/B07 bi-orientation gates, (iii) same-unitary `(P,D,R)` identities, and (iv) the lead subgroup/V4 positive-reserve ceilings, with account04/B08's all-roofs-tied cubature-boundary degeneracy handled separately. A target-level disproof must produce actual spectra/support direction and a true unitary satisfying all these conditions.

The theorem itself uses no simple-spectrum, invertibility, nonzero-minor, or nonsingularity assumption; it creates no new limit-case debt. No target-level closure is claimed.
