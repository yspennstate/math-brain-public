# r36 prepublication scope addendum

1. The phrase in REPORT.md saying that the literal `q_Y=q_Z=1` physical block is "exactly B" is to be read up to diagonal sign conjugation: if `Y=eps_i X_i`, `Z=eps_j X_j` with `eps_i,eps_j in {+1,-1}`, then the original-coordinate principal block is `diag(eps_i,eps_j) B diag(eps_i,eps_j)`. Its determinant magnitude and definiteness are unchanged, so the account04/B05 definite-pair inequality used there is exactly valid.

2. `QFORM-NEAR-DOUBLEZERO-GENERAL-HYPERBOLA-v1` is a homogeneous-packet (or range-affine-removable) theorem. It allows arbitrary dependence of the residual environment inside the pair translations `F(S,E),G(S,E)`, but it does not allow a free additive function `H(E)`. In particular a higher-rank conditioning-generated term `hR` is not declared harmless.

3. The theorem gives interval domination and an essentially bounded density. It does not prove continuity. Full QFORM and full-target continuity remain open.

4. Finite constants in CHECKS.txt are diagnostic arithmetic only. The proof is the deterministic factorization, change-of-variables, derivative bounds, and layer-cake argument in REPORT.md.
