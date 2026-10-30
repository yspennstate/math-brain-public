# Fresh-correction addendum — local collision obstruction is paid by the aggregate spectral-coloop theorem

A later same-programme handoff arrived after REPORT.md was committed: fleet02/B03, run `20260923T001512Z-fleet02-B03-QFORM-auto11`, canonical mathematics `yspennstate/math-open-problems@90b9e0b5438b950fd2a0ed054833c055fdb92967`. It proves `QFORM-N3-LOCAL-COLLISION-BEFORE-AGGREGATION-FALSE-v1`: in a no-pivot star-plus-rank-one family, every single physical pair has a fractional collision cost diverging like a positive power of the bank size even though the full mixed-hub output has a universal density bound. Therefore the next step must aggregate the physical hub/bank before taking the fractional endpoint; one-pair localization is not a valid general reduction.

This correction does **not** affect any proof in REPORT.md. In fact the B03 witness is exactly an instance of REPORT Theorem 5.1 and gives a useful regression/application of it.

Let

    A_m(a,b) = [[0, (a/sqrt(m)) 1_m^T, 0],
                [(a/sqrt(m)) 1_m, 0_{m x m}, 0],
                [0, 0, (b/m) J_m]],

with |a|,|b|>=1 and m>=2. Its nonzero spectral space has orthonormal physical basis

    e_h,  v=m^(-1/2)1_V,  e=m^(-1/2)1_E,

and in this basis the exact rank-three matrix is

    Lambda' = [[0,a,0],[a,0,0],[0,0,b]].

The hub row e_h has spectral leverage one. Compressing Lambda' to e_h^perp gives `M=diag(0,b)`, which has rank one. The residual two-dimensional frame consists of the V-bank rows `(1/sqrt(m),0)` and E-bank rows `(0,1/sqrt(m))`; hence every residual row leverage is exactly `1/m<=1/2`. REPORT Theorem 5.1 therefore applies directly and gives

    |phi_Q(t)| <= ((4*pi)^(3/2)/2) |a|^(-1) |b|^(-1/2) |t|^(-3/2),

and

    boxed(||p_Q||_infinity <= (12/2^(2/3)) |a|^(-2/3)|b|^(-1/3)
                               <= 7.559526300).

This is exactly the aggregate mixed-hub scaling reported independently by B03, while B03's local physical-pair collision endpoints diverge. Thus the fresh correction sharpens, rather than invalidates, B02's next step: spend the joint D' row-column star concentration through an **augmented aggregate mixed-hub/bank frame** before any fractional collision endpoint. Do not localize to one physical pair first.

The full QFORM conjecture and the global unweighted `integral |phi_Q|` criterion remain open.
