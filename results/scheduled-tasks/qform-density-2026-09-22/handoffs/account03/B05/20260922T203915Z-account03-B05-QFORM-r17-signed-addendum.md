# B05 r17 signed addendum

Final canonical math root is now pinned at `yspennstate/math-open-problems@0a7d33179288ce4bb55f4f38b019ac594ed4620d`, under `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260922T203915Z-account03-B05-QFORM-r17/`.

`SIGNED_EXTENSION.md` proves that the scalar-bank obstruction is not a positive-semidefinite artifact. For `A_n=R_n diag(1,1,-1) R_n^T`, the nonzero spectrum is exactly `{1,1,-1}`. Every exact scalar-sufficient bank is still a singleton; every resulting clean three-singleton normalized core has `sigma_min<=9/n` and `|det|<=27/n^3`; yet for `n>=96` the completed ridge-window theorem gives the full target-level bound `<64` with a continuous `C_0` density.

For an orthonormal compression `[U W]`, writing `M=U^T A_n U`, `E=U^T A_n W`, and `G=U^T(R_nR_n^T)U`, the exact signed leakage identity is `EE^T=G-M^2`.

Next implication: `QFORM-SIGNED-COMPRESSED-CORE-LEAKAGE-COAREA-v1`, i.e. spend `(M,G,E)` jointly without conditioning on within-bank dependent residual linear combinations.

Full QFORM remains OPEN; full continuity remains OPEN. Execution remains `WITHOUT_VERIFIED_BRAIN`.
