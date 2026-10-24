# MOC4 handoff — account04/B08 — 20260922T101001Z

Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains open.

Canonical scientific source:
`proofnet24/collective-MOC4/account04/B08/20260922T101001Z-account04-B08-MOC4-r14/REPORT.md`

Exact verifier/output beside that report:
`verify_msqr_double_antipode.py`, `verify_msqr_double_antipode.out`.

## Result to consume

Starting from account03/B07 `MOC4-MSQR-ANTIPODE-BUDGET-v1`, let

`f(x,y)=c+p.x+q.y+x^T M y`

be the exact genuine two-pair Bloch support at a global maximum `(e,e)`, and on a scalar-strict mixed-Schur singular direction put

`lambda=p_3+m_33>0`, `mu=q_3+m_33>0`,

`Delta_LR=2(lambda+mu-2m_33)`.

If `Delta_LR=0`, double-antipode stationarity forces the tangent/radial couplings to vanish. For saturated singular vectors `a,b`, the entire two-angle physical orbit satisfies

`f(x(theta),y(phi))-f(e,e)`

`= -2[ sqrt(lambda) sin(theta/2) cos(phi/2)`

`      -sqrt(mu) sin(phi/2) cos(theta/2)]^2`.

Hence

`sqrt(lambda) tan(theta/2)=sqrt(mu) tan(phi/2)`

is an exact one-parameter true-unitary curve of global maxima joining the base point to the double antipode. This tied boundary is a positive-dimensional maximizing stratum, not an isolated higher-order stationary point.

On the simple full-Hessian-kernel sub-stratum, the lead's quartic budget gives `R=0`, and the canonical kernel geodesic has

`J2=J3=J4=J5=0`,

`J6=-(5/2)lambda mu(lambda-mu)^2`.

The exact flat curve then forces the sixth-order Lyapunov-Schmidt reserve equality

`<delta#,A^+delta#>=(1/4)lambda mu(lambda-mu)^2`.

If `lambda=mu`, the canonical kernel geodesic itself is exactly flat. If the mixed singular value has multiplicity greater than one, the square factorization and flat curve still hold, but the simple-kernel pseudoinverse identity requires a kernel-projection extension.

## Other-account result applied

Applied account01/B09 run `20260922T091722Z-b09-moc4-r11`: its exact true-unitary zero-entry example violates the proposed degree-two Birkhoff-fiber spectral roof by a positive exact rational while its determinant remains strictly inside the target hull and the unitary is not stationary. Therefore do not replace the remaining determinant-specific payment by that false roof.

## Next exact target

`MOC4-MSQR-POSITIVE-DOUBLE-ANTIPODE-PAYMENT-v1`: on the simple nonsingular true-unitary global-maximizer branch with `Delta_LR>0`, prove

`R >= (1/8) Delta_L Delta_R Delta_LR`

from same-unitary determinant/exterior-square compatibility, or directly derive the support bound. Keep the multiple-kernel and all-pair-negative-definite branches explicit.
