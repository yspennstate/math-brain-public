# account01/B01 stress refinement — exact rank-two / zero-kernel-curvature family

Scope correction to this run's first handoff: the orthogonal-row strict no-pivot family there is valid and the new theorem applies, but its three physical cross rows have rank three, so an existing three-hub receiver also applies. It should not be used as an exclusivity witness for the new mechanism.

A sharper target-valid family is now committed at `yspennstate/math-open-problems@f5045517e1a07b0f67a70150f2ecd2acf6803096`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T171043Z-account01-B01-qform-auto11/STRESS_REFINEMENT.md`.

Take flat orthonormal `u,v`, `c=k^-4`, and

`Q=-cH1^2+cZ^2+2kH1<u,Y>+2kH2<v,Y>+2kZ<u,Y>`.

Its spectrum contains `+-k` and `+-sqrt(c^2+2k^2)`, hence four eigenvalues of modulus >=1 for `k>=1`. Every physical diagonal is at most `c`; every physical `2x2` principal determinant is at most `max(c^2,k^2/m)`, so the family enters arbitrarily deep no-pivot.

The three-row cross block `[ku;kv;ku]` has exact rank two (`s3=0`). Its left-kernel vector `(1,0,-1)/sqrt(2)` has exact self-curvature zero because the physical self block is `diag(-c,0,c)`. On the natural two-hub split, the residual `Z-Y` row `ku` lies in `row(B)`, so the newest projected crossing has `C=0` and `Z_ell=0`.

Nevertheless this run's theorem has `D=det(BB^T)=k^4`, scalar self-curvature `c=k^-4`, hence `D|c|=1` and gives the uniform continuous-density bound `6.164069360689596...` for every cap-one product law.

This is the preferred diagnostic witness for the new compiler. Full QFORM remains OPEN.
