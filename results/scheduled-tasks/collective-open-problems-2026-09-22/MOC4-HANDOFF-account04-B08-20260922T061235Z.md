# MOC4 handoff — account04/B08 — strict Spin(4) sectors

**Run:** `20260922T061235Z-account04-B08-MOC4-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; MOC4 remains OPEN.  
**Scientific report:** `yspennstate/math-open-problems/proofnet24/collective-MOC4/account04/B08/20260922T061235Z-account04-B08-MOC4-r12/REPORT.md`, canonical report commit `c7270aa48ae25bdcda0700d404549862c8a8c68f`, blob `7630170b6cc3b73a5dbe1b0e19c60c0f2529218a`.  
**Verifier:** same run directory, `verify_root_strictness.py`; captured `VERIFY_OUTPUT.txt`.

## Sources applied

- Latest complete team lead: account03/B07 `20260922T060726Z-account03-B07-MOC4-r11`, report blob `c8911d75149115eb15810e4f8fac624cfc5e34f5`, theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`.
- Pair-Haar source theorem: account04/B09 `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`, report blob `1ec092caac4aa78fb3998199849f632387a0c18f`.
- Assigned OTHER-account partner: account01/B09 `b09-20260922T054641Z-moc4-r11`, report blob `b12c5f150c244bcb5c6111233a8dcac845ee07b3`, strict-pair/full-stationary projected-lift no-go and mixed-Hessian saddle certificate.

## New essential step

The latest lead proves that if one scalar Spin(4) sector of the exact pair Hessian saturates, `T=|C|`, then one coordinate row/column embedded `SU(2)` orbit is support-flat. Combining that exact flatness with account04/B09's full exterior-minor Haar-twirl lift gives an immediate target bound on the flat orbit. Therefore a support-violating global maximizer cannot saturate any such sector:

`T^L_{alpha gamma} > |C^L_{alpha gamma}|` for all three left block-plane pairs, and
`T^R_{beta delta} > |C^R_{beta delta}|` for all three right block-plane pairs.

This strictly strengthens the lead's saturation-to-zero-face reduction: the mixed-conformal saturation branch is target-safe directly and needs no separate zero-face inequality merely for that branch.

An exact exterior-square root calculation identifies the six conformal/anticonformal sector planes with the six coordinate `SU(2)` pair root planes:

- 01 -> block planes 1<->2, anticonformal; 23 -> same, conformal;
- 02 -> block planes 0<->2, anticonformal; 13 -> same, conformal;
- 03 -> block planes 0<->1, anticonformal; 12 -> same, conformal.

## Remaining pair-Hessian boundary

With `a=T-C>0`, `b=T+C>0`, a lead pair Hessian is

`[ -2a I  M ; M^T  -2b I ]`.

The only singular boundary left is mixed Schur equality `||M||_op=2 sqrt(ab)`. If `Mv=2 sqrt(ab) u` and `M^T u=2 sqrt(ab) v`, an explicit kernel direction is

`Z*=sqrt(b)(u1 E1+u2 E2)+sqrt(a)(v1 F1+v2 F2)`.

It necessarily has both conformal and anticonformal components. The scientific report derives exact singular-safe polynomial gates on this boundary:

- `MOC4-MIXED-SCHUR-CUBIC-GATE-v1`: the exact third derivative `J3(Z*)` must vanish;
- `MOC4-MIXED-SCHUR-QUARTIC-GATE-v1`: after that, the exact fourth derivative `J4(Z*)` must be nonpositive.

The verifier symbolically checks the determinant- and norm-channel derivative identities and the complete root dictionary.

## Assigned-partner calibration

The account01/B09 adversary is strict on all twelve coordinate pair orbits, so the new strict-sector theorem correctly does not reject it. It is rejected only by its positive mixed second derivative. This confirms that the remaining proof must retain the mixed Hessian and must not replace it by pairwise strictness or a positive coefficient-lift assertion.

## Next exact obligation

`MOC4-STRICT-ROOT-MIXED-SCHUR-RESIDUAL-v1`: exclude a genuine positive-gap global maximizer satisfying the retained endpoint/subgroup roofs, same-unitary P/R/D compatibility, full stationarity, every strict Spin(4) root inequality, every mixed-Hessian inequality, and on any Schur-equality boundary the explicit kernel/cubic/quartic gates. If all pair blocks are negative definite, attack the strict-interior coupling across distinct root blocks and Cartan directions.

No full-proof claim is made.
