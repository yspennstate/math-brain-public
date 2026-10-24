# MOC4 handoff — account04/B07 spinor determinant hexagons

**Run:** `20260922T044421Z-account04-B07-MOC4-r12`  
**Status:** `ESSENTIAL_STEP_APPLIED`; MOC4 remains OPEN.  
**Audience:** team lead account03/B07 and assigned partner account01/B08.  
**Source report:** `proofnet24/collective-MOC4/account04/B07/20260922T044421Z-account04-B07-MOC4-r12/REPORT.md` at scientific commit `4a259f7799c91179ecf5b2bab7c0d99cc6f794cb`, blob `edef226995227fc0bff482cf97b6ec722abc8efc`.

For the exterior-square Bogoliubov form `T(z)=Mz+N zbar`, every even input/output conjugation gauge `(r,c)` satisfies the exact identities

`det N_rc = 0`,

`|det M_rc| + ||N_rc||_F^2/2 = 1`,

`||adj N_rc||_F^2 = (||N_rc||_F^2/2)^2`.

Combining this with account03/B09's exact `D=(1/4)E^T P E` gives

`L_rc := ||N_rc||_F^2 = 2(1-P_{iota(r),iota(c)})`.

Hence the old 16 parity-mask **mass** inequalities are exactly `P_ij>=0` once same-unitary `P` compatibility is imposed; do not double-count them as extra payment. The new information is phase-sensitive: for all 16 gauges,

`sum_{rho in S3} sgn(rho) product_alpha (N_rc)_{alpha,rho(alpha)} = 0`.

Thus the six term moduli form a polygon, giving 96 inequalities `w_rho <= sum_{sigma != rho} w_sigma`. If a selected odd signed matching is relabelled to the diagonal with masses `x1,x2,x3` and off-matching anti-linear mass `Eoff`, then

`sqrt(x1*x2*x3) <= Eoff/2 + Eoff^(3/2)/(3*sqrt(3))`,

with

`Eoff = 2(1-P_ij) - (x1+x2+x3)`.

This is an explicit nonlinear same-unitary P/R payment, not a positivity lift.

The exact Fraction verifier and captured output are in the same scientific run directory. On the assigned partner's exact rational true unitary, all 16 determinant closures, P reconstructions and adjugate identities hold with exact zero error; for gauge `011,011`, `L=60830802/30525625` and `1-L/2=110224/30525625=|u_22|^2`.

**Partner application:** account01/B08 latest `MOC4-CHAIN-CUBE-FACE-PROPAGATION-v1` plus its stability addendum closes the exact 11-vertex face via the common-circle theorem and controls five transverse spectral cross-ratio phases. A residual generic maximizer must now satisfy those spectral phase controls simultaneously with the 16 unitary spinor determinant closures above, the lead V4/pair ceiling, and the same-P standard-channel ceiling.

**First next implication:** use the determinant-hexagon leakage to prove that support-favored concentration of the symmetric quotient `R` pays enough off-matching mass to cancel the remaining `Kstd-Delta` / V4-pair reserve. If false, the counterexample must use actual spectra, a support direction and one true unitary; an independent `(P,R)` or arbitrary coefficient normal is insufficient.

No benchmark material, credentials, machine paths, scheduler identifiers, email/Drive data, paid/remote compute, public posting or permission changes are included.
