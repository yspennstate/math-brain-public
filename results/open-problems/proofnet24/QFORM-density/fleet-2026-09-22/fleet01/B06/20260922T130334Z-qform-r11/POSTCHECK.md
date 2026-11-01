# Post-publication correction check — fleet01/B06 `20260922T130334Z-qform-r11`

A later fresh correction snapshot at `yspennstate/math-research-brain@9aa2469bab6499771c82a286203526fc1c042401` added two relevant warnings after the main report was committed.

1. `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS` refutes a **quadratic-phase/difference-variable** route that takes absolute values and then applies coordinatewise Hausdorff--Young/Hölder. It does not affect `QFORM-WEIGHTED-2D-PROJECTION-v1`: the latter applies sharp Hausdorff--Young only to the characteristic functions of the original one-dimensional inputs inside the exact **linear projection** factorization `hat mu(xi)=prod_i hat f_i(u_i dot xi)`, followed by geometric Brascamp--Lieb. No quadratic-phase ambiguity or difference-density majorant is introduced.

2. `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` shows that bounded pair density plus bounded conditional density does not substitute for independence in a hyperbolic coupling. This reinforces, rather than contradicts, the main report's unpaid implication. Any attempt at `QFORM-ORTHOGONAL-CORRELATED-ADDITION-v1` must retain the original product-linear provenance; it cannot simply combine the `pi e` marginal ellipse bound with a conditional cap for the orthogonal remainder.

The mathematical status of the main report is unchanged: the weighted two-dimensional projection and pure same-sign ellipse component bounds remain proved supporting results; the full QFORM target remains open.
