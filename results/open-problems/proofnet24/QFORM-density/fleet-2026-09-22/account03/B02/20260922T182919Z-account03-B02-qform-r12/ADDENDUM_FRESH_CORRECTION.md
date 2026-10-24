# Fresh-correction compatibility addendum

After the main proof was written I refreshed the live correction inbox and explicitly checked `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` (brain event source, canonical math report `yspennstate/math-open-problems@77d71ed8bbd7f8a3fd40958e54b5bf658163c27a`). That correction shows that a square plus one heavy off-diagonal coefficient does **not** control arbitrary quadratic curvature on the same coefficient-side bank: `U^2+X^2+2UX=(U+X)^2` is unbounded at zero.

The theorem in this run does not make the refuted inference. Its residual is required to have the exact product-preserving form

`R=2a XU+H(X,V)`,

with `V` independent of `(X,U)` and with no extra `U`-dependent curvature hidden inside `H`. This is precisely why the proof can condition on `V` and then use the affine map in `U`. The correction therefore sharpens, rather than invalidates, the theorem's interface: a structural application must isolate a genuinely affine hyperbolic variable on its own bank, or use a different completed branch.

No status change: `ESSENTIAL_STEP_APPLIED / FULL QFORM TARGET OPEN`.
