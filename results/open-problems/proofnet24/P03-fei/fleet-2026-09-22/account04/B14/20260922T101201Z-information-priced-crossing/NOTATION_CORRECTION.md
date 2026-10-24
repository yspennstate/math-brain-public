# Notation correction — physical restriction values versus spectral support bits

This addendum preserves the theorem and corrects one potentially confusing symbol choice in `REPORT.md`.

In Sections 1–4 of the report, the mutual-information variable written there as `X_A` means the **physical cube restriction values** on the original-coordinate block `A`. To avoid collision with account01/B18 notation, write these physical values as `Z_A` instead. Thus

`U = P(eta_j=1 | Z_A)`

and the theorem is

`I(eta_j; Z_A) >= h2(p_j)-h2(p_j-c_j(A))`.

By contrast, account01/B18's block-Shannon term

`B_A = H(X_A | X_{A^c})`

uses `X` for the **spectral support indicator vector**. These are different random objects and no inequality between `I(eta_j;Z_A)` and `B_A` is asserted in this run.

The stopping theorem `sum_v pi_v B_{A_v} <= K J(root)` is unchanged, because it follows solely from the admission condition `B_A<=K D_A` and exact folded-drift telescoping. The information-price theorem is also unchanged, because it is a direct posterior/Jensen statement on physical restriction values.

Accordingly, the next-arrow comparison between the forced physical posterior information and the spectral curvature/Shannon currencies is an explicitly **unproved bridge problem**, not an already-established payment identity.
