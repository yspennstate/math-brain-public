# account01/B05 — qform late dependency closure

Final status: `ESSENTIAL_STEP_APPLIED`; target `OPEN_NOT_PROVED`; `WITHOUT_VERIFIED_BRAIN`.

Primary immutable report: `yspennstate/math-open-problems@e3e8754ab0cd1ae93bbe74f9fdbf0df8947fc6c8`, `qform/fleet-2026-09-22/account01/B05/20260922T1136Z-qform-principal2d-B05-r1/REPORT.md`.

Late dependency closure: `yspennstate/math-open-problems@a0732b537acc63ab8ed61312852f4afee64fb46a`, same run directory, `DEPENDENCY_CLOSURE.md`.

Newly consumed peer: account04/B15 `yspennstate/math-open-problems@15a15f2495abe0d4de12c3562246d55c7a63980d`. It independently proves the physical definite 2x2 principal-block bound and gives a stronger exact hard family with spectrum `(1,1,-1,0,...)` and no definite physical principal pair. Its Cauchy-Binet reserve `sum_J(det R_J)^2=1` was applied to the concrete four-type Walsh system.

New B05 derivation from that peer result: for the three flat Walsh rows, exactly `n^3/16` coordinate triples have `|det R_J|=4/n^(3/2)`. Thus `sum_J(det R_J)^2=1` but `sum_J|det R_J|=n^(3/2)/4`. Therefore simply weighting a local reciprocal-Jacobian chart bound `1/|det R_J|` by Cauchy-Binet square weights still loses `n^(3/2)`. Together with B05's independent cube two-plane calculation giving fiber-supremum loss `n/2`, this rules out best-chart selection, naive square-weight summation of reciprocal-Jacobian bounds, and fiberwise amplitude supremum.

Live unpaid implication: a nonreusing averaged nonlinear level-set/coarea inequality that keeps the product amplitude inside the integral and aggregates charts before reciprocal determinant loss. No full proof claimed.
