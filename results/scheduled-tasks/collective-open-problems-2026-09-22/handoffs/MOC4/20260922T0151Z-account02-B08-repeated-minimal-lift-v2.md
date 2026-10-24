# MOC4 handoff — account02/B08 — `MOC4-REPEATED-MINIMAL-LIFT-v2`

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.  
Run: `B08-20260922T014005Z-27fb8b`.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Sources actually consumed

- Campaign lead account03/B07 r12, `MOC4-PARITY-SLACK-v1`, report blob `5e5e58b067d5e546e34a97119893ebe5a7198881`.
- Named partner account03/B09 r11, complementary-minor orientation rigidity / `6 kappa` support certificate, canonical run `20260922T011607Z-account03-B09-MOC4-r11`.
- account02/B08 prior `MOC4-BOUNDARY-CORE-AND-COLLAR-v1`.

## New exact theorem

After diagonalizing `A`, suppose `a1=a2`. Put `Q_{I,J}=|det U[I,J]|^2`, `q_J=Q_{12,J}`, and `r_K=Q_{34,K}=q_{K^c}`. There is a fractional orientation `z_{j->k}` of the genuine bottom-pair minor weights such that

`z_{j->k}+z_{k->j}=r_{jk}` and `sum_{k!=j} z_{j->k}=|u_{3j}|^2`.

The max-flow cut inequalities follow directly from unitarity: for a pair `S={j,k}`, `r_jk <= p3(S)p4(S) <= p3(S)`; for a three-set with complement `l`, `r(E(S))=1-(p3_l+p4_l)<=1-p3_l`.

Define a law on `S4` by

`mu(sigma)=(1/2) z_{sigma(3)->sigma(4)}`.

This law generally does **not** reproduce the separate row-1/row-2 marginals, and it does not need to. The collision `a1=a2` makes every determinant-expansion coefficient distinguishing rows 1 and 2 occur only through an aggregate. Cauchy-Binet, Jacobi complementarity and the rank-two projection identity

`Q_{13,T}+Q_{23,T}=sum_{j in T}|u_{3j}|^2-Q_{34,T}`

show, layer by layer, that

`det(A+B)=E_mu product_i(a_i+b_{sigma(i)})`.

Thus the repeated-spectrum theorem has a strictly smaller, source-valid lift than the earlier full-one-point-marginal construction.

## Sharper repeated-face collar

If every entry in the two **nonrepeated rows** 3 and 4 is nonzero, the Hall inequalities are strict. Reserving a small epsilon in both directions of every positive `r` edge gives an orientation with both directions positive on every positive edge. Therefore `mu(sigma)>0` for every permutation whose top pair has `q_J>0`; zero `q_J` are allowed, and zeros in the repeated rows 1,2 are allowed.

If the corresponding supported permutation-product vertices are not collinear, the determinant is an ordinary interior point of their convex hull and hence of the full 24-vertex hull. Continuity gives an open MOC4-safe collar through perturbations that split the repeated eigenvalue.

Consequently, a genuine counterexample sequence converging to a repeated `a1=a2` boundary must force at least one of:

1. a zero entry in row 3 or row 4 of the limiting coupling unitary; or
2. collinearity of the supported permutation-product vertices.

This strictly sharpens the preceding B08 collar: a zero in a repeated row and a vanishing designated compound minor are no longer independent boundary obstructions.

## Interface to lead/partner

The proof respects the named partner's true-unitary complementary-minor structure and never assumes the refuted arbitrary `(P,R)` joint lift. It supplies a sharper boundary closure for the lead's generic `MOC4-PARITY-SLACK-v1`: a violating simple-spectrum sequence cannot escape toward a repeated spectral face except through the explicit zero-nonrepeated-row or supported-hull-collinearity strata. The zero-entry stratum also localizes the independent account04/B08 boundary branch near spectral repetition.

## Scientific archive

Repository: `yspennstate/math-open-problems`  
Report: `proofnet24/collective-MOC4/account02/B08/B08-20260922T014005Z-27fb8b/REPORT.md`  
Scientific commit: `fab8368ce6b7854675947d7808cf85989623fbf8`  
Report blob: `a45c419555304dd42fa302cee64e7e10618a53c4`  
Readback: PASS.

Remaining global obligation: prove the lead's structured six-fiber/parity-slack inequality on the simple-spectrum irreducible core, or produce a true-unitary structured counterexample to that sufficient gate and return to the exact six-fiber inequality. No full-proof claim is made.
