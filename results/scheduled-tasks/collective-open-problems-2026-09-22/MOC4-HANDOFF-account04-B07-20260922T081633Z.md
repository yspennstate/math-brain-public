# MOC4 handoff — account04/B07 — 20260922T081633Z

Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains OPEN.

Scientific report:
`proofnet24/collective-MOC4/account04/B07/20260922T081633Z-account04-B07-MOC4-r12/REPORT.md`

Exact verifier/output:
- `proofnet24/collective-MOC4/account04/B07/20260922T081633Z-account04-B07-MOC4-r12/verify_cofactor_deficit.py`
- `proofnet24/collective-MOC4/account04/B07/20260922T081633Z-account04-B07-MOC4-r12/verify_cofactor_deficit.out`

Named OTHER-account source consumed:
- account03/B07 `20260922T060726Z-account03-B07-MOC4-r11`
- theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`
- source path `proofnet24/collective-MOC4/account03/B07/20260922T060726Z-account03-B07-MOC4-r11/REPORT.md`
- source blob `3c11567e275d39376f217a9b9e3c10693efa3127`
- read at main `86ebffd8566c6594c03aeb66f5a209e076098aee`.

New theorem: `MOC4-SPIN6-COFACTOR-DEFICIT-v1`.

For every real exterior-square point `O=Lambda^2 U in SO(6)`, write `T(z)=Mz+N conjugate(z)`. Then `N` has singular values `(sqrt(lambda),sqrt(lambda),0)`. If `r_alpha=sum_beta |n_{alpha beta}|^2` and `c_beta=sum_alpha |n_{alpha beta}|^2`, then for all nine complementary minors

`|cof_{alpha beta}(N)|^2=(lambda-r_alpha)(lambda-c_beta)`.

Hence the anti-conformal mass matrix obeys nine nonlinear phase-free cofactor-deficit interval constraints. These are exact same-unitary constraints and strictly strengthen mass/two-rook conditions.

Strict-cut witness: `S=diag(1,1/2,1/2)` is a convex combination of two two-rook vertices and satisfies total/row/column mass constraints, but total mass gives `lambda=1`, while its `(1,1)` cofactor deficit is `0` and the complementary-minor squared modulus is forced to `1/4`. Therefore no genuine Spin(6) point has `q^-=S`. This refutes only the weaker relaxation, not MOC4.

Immediate collar: if `r_alpha=lambda` or `c_beta=lambda`, the opposite `2 x 2` minor of `N` vanishes exactly; quantitatively the mismatch of the two complementary product magnitudes is bounded by `sqrt((lambda-r_alpha)(lambda-c_beta))`.

First unpaid implication: `MOC4-STRICT-CURVATURE-COFACTOR-PAYMENT-v1`. Combine all genuine strict Spin(4) curvature reserves with the gauge-conjugate cofactor-deficit identities and same-unitary exterior-minor relations to pay any positive support excess. On a saturated mixed Spin(4) gate, the team-lead theorem reduces to the still-unpaid zero-face support problem; this handoff does not call that face solved.

Execution/provenance: `WITHOUT_VERIFIED_BRAIN`; no benchmark gold, answer-bearing benchmark metadata, credentials, email/Drive, paid or remote compute, public posting, scheduler mutation, or other-account authentication used.
