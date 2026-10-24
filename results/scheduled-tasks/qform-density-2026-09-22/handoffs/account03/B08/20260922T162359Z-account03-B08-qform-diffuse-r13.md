# account03/B08 handoff — ridge-Lp plus physical-square closure

Run `20260922T162359Z-account03-B08-qform-diffuse-r13`. Pre-publication owner control advanced from initial revision `2026-09-22.5` to live revision `2026-09-22.6`; both keep the same sole QFORM target, so the later control was honored. Execution status: `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@f0a31a05a227ca671ffb22f6d7ed62954ce48c73`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T162359Z-account03-B08-qform-diffuse-r13/REPORT.md`. Arithmetic checker and passing output are beside the report.

New proved theorem `QFORM-PIVOT-PLUS-RIDGE-LP-v1`: after completing one ORIGINAL coordinate with pivot `a!=0`, let the Schur residual have an original-coordinate cross block with ridge parameters `K,theta,D,gamma`. If `max diag K<=q/2` and `theta>q`, then choose `s<2` with `theta s>2q`; fractional inverse Hausdorff--Young gives the residual an `L^p`, `p=s/(s-1)>2`, density, and a dependent-square Abel estimate upgrades it to an essentially bounded density. This strictly lowers the direct ridge endpoint requirement from `theta>2q` to `theta>q` when one physical square is available.

Clean corollary `QFORM-PIVOT-PLUS-TWO-RIDGE-DIRECTIONS-v1`: if the residual cross block has two singular values at least `sigma`, take `gamma=sigma/sqrt(6)` and assume `max diag K<=1/2`; then

`||p_Q||_infinity < 14.34 / sqrt(|a| sigma)`.

Concrete hybrid branch: if the Schur residual has two selected eigen-directions with row leverage `<=1/32`, complementary operator norm `<=1/64`, and the pivot has `|a|>=1/312`, then `sigma>=23/64`, the ridge diagonal is `<(397/1000)^2<1/2`, and `||p_Q||_infinity<423` (safe rational bound `<434`). This connects directly to account03/B12's spectral-window failure certificate `|A_ii|>1/312 OR ||A_{-i,i}||_2>1/312`: the scalar-pivot subbranch is now closed when its Schur residual retains two diffuse large directions.

Completed account04 mathematics actually applied: account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, gives on the stronger residual `theta>2q` branch `||p_Q||_infinity<=2 sqrt(M/|a|)`; for the standard three-ridge certificate this is `<7.17/sqrt(|a|sigma)`. The designated account04/B08 has no completed current-QFORM scientific directory/handoff visible at refresh, so no result was fabricated.

Continuity status: the new hybrid theorem proves essential boundedness / absolute continuity, not a continuous representative. The source direct ridge theorem remains continuous in its own `theta>2q` scope.

Full QFORM remains OPEN. Next B08 mechanism: `QFORM-HEAVY-ROW-TO-PIVOT-OR-RIDGE-v1` — from the fixed-scale heavy physical row forced by spectral-window failure, prove an exhaustive original-coordinate inequality that either extracts a scalar pivot with admissible residual `theta>1`, or pays the off-diagonal-heavy alternative by a grouped-coordinate bilinear/bank mechanism. Preserve the singleton-plus-two-banks correction; no naive one-good-minor/rank-three-cut dichotomy.
