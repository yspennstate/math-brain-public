# account01/B13 auto21 addendum — sharp projection-leverage factor

Source-pinned mathematics: `yspennstate/math-open-problems@a7ccd87c95953d17337fa35a4f32f98862c20c7b`, directory `proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T110212Z-account01-B13-qform-auto21/`, with `REPORT.md` and `ADDENDUM_SHARP_LEVERAGE.md`.

The dual rectangular theorem has the sharper exact factor

`||p_Q||inf <= K_r Phi(B)^(1/r) det(BB^T)^(-1/(2r))`,

where `K_r=[r/(sqrt(2)(r-1))]omega_r^(1/r)` and, for `R=B^T(BB^T)^(-1/2)` with row leverages `ell_j`,

`Phi(B)=prod_{ell_j<1}(1-ell_j)^(-(1-ell_j)/2) <= exp(r/2)`.

Thus the universal `sqrt(e)` loss in the main report is only the relaxation `Phi(B)^(1/r)<=sqrt(e)`. If the opposite curved bank is square (`m=r`), `R` is orthogonal, every row leverage is one, `Phi(B)=1`, and there is **no loss at all**:

`||p_Q||inf <= K_r |det B|^(-1/r)`

with arbitrary opposite-side curvature. For `r=2`, this is

`||p_Q||inf <= sqrt(2pi)|det B|^(-1/2)`.

For a rectangular two-hub bank,

`||p_Q||inf <=sqrt(2pi)Phi(B)^(1/2)e2(B^TB)^(-1/4)`,

so an actual slab ratio `rho` forces

`e2(B^TB)<=4pi^2 Phi(B)^2 rho^(-4)<=4pi^2 e^2 rho^(-4)`.

Full QFORM remains OPEN. This addendum changes only the constant/structural sharpness; the first unpaid implication remains `QFORM-BOTH-SIDES-NONNULL-TWOHUB-CURVATURE-GLUE-v1`. Execution remains `WITHOUT_VERIFIED_BRAIN`; no task/scheduler/notification/public-release change was made.
