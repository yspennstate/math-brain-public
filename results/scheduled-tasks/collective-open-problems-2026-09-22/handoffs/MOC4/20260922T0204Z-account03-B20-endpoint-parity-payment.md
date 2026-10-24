# MOC4 handoff — account03/B20 — endpoint parity-payment gate

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Brain status: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Inputs consumed

- account03/B07 `MOC4-PARITY-SLACK-v1`, report blob `5e5e58b067d5e546e34a97119893ebe5a7198881`.
- account02/B08 `MOC4-REPEATED-MINIMAL-LIFT-v2`, handoff blob `6d138fe3fff7931c0c6c038d54ca8991e80966d5`.
- account04/B09 structured coefficient/no-common-lift result, handoff blob `94f2370a034a616ea7517f60dfce2b6e0c18f5c6`.

## New result

The existential B07 parity-payment condition should optimize the parity penalty in the opposite direction from the earlier `Psi=min sum lambda F` strong gate. Define

`Q_K(R)=min_{lambda: R=sum lambda R_rho} sum_rho lambda_rho m_rho(K)`.

Then `2 Q_K(R) <= W(D,R,K)` is sufficient for the exact six-fiber MOC4 support inequality for every `X`, where

`W(D,R,K)=sum_ij (R_ij |K_ij| - D_ij K_ij)`.

For every 3x3 doubly stochastic `R`, all Birkhoff decompositions form one explicit interval. Ordering the six permutations as `e,s12,s13,s23,c,cbar` and writing `t=lambda_e`,

`lambda = (t, r33-t, r22-t, r11-t, r12-r33+t, r13-r22+t)`

with

`L=max(0,r33-r12,r22-r13) <= t <= U=min(r11,r22,r33)`.

The parity payment `q(t)=sum lambda_rho(t)m_rho(K)` is affine, hence

`Q_K(R)=min(q(L),q(U))`.

Therefore the B07 existential gate has no hidden LP: it is enough to prove either `2q(L)<=W` or `2q(U)<=W`.

If all nine entries of `K` are nonzero, the six transversal-product signs multiply to +1, so the number of bad fibers is exactly one of `0,2,4,6`; it is never odd. In the two-bad-fiber regime the correct endpoint is determined by their parity class / minimum-entry penalties.

The account02/B08 repeated-spectrum result is used to isolate the simple-spectrum core honestly: `Q=min(q(L),q(U))` is continuous, while repeated-face escape is already localized to the explicit zero-nonrepeated-row or supported-hull-collinearity strata.

## Exact scientific delivery

Repository: `yspennstate/math-open-problems` (private)  
Run: `proofnet24/collective-MOC4/account03/B20/20260922T014851Z-B20-moc4-r11/`  
Final scientific commit: `4d52d56d6a8a1e0ca0a85c639dba70fed5f95810`  
Report blob: `6faf73db3638fb0fe1d5846f8cd4130494b6315f`  
Verifier: `verify_endpoint_gate.py`  
Exact checks: interval reconstruction PASS; endpoint minimization PASS; nonzero bad-fiber counts `[0,2,4,6]` PASS. A separate 200-case numerical LP cross-check agreed to machine precision but is not part of the proof.

## Next universal implication

On the simple-spectrum irreducible strict-compound unique-support-vertex core, prove

`W(D,R,K) >= 2 min(q(L),q(U))`

using the actual unitary blocks and the account04/B09 Bezout/Vandermonde structure of the spectral support coefficient block. If a true-unitary structured datum refutes this sufficient gate, do **not** call it a MOC4 counterexample; return to the exact six-fiber inequality and identify how the `X` term rescues the support bound.

Recommended recipients: account03/B07, account03/B08, account03/B09, account01/B07-B09, account02/B07-B09, account04/B07-B09.
