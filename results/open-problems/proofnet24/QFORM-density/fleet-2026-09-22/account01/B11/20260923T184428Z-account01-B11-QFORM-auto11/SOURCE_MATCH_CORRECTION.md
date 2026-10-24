# Source-match correction and retained new content

A late read of this slot's immediately preceding run

`yspennstate/math-open-problems@20f5424bcd745844055208675a66bbd270b3fab9`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260923T181636Z-account01-B11-QFORM-auto11/REPORT.md`

shows that the **one-bank exact-graph QFORM application** in Sections 3--4 of the present `REPORT.md` is already subsumed, with a better constant, by the earlier theorem `QFORM-HIDDEN-PROJECTION-CONDITIONABLE-SPAN-v1`: after conditioning the opposite bank, `tau_S=0` means the retained hidden source row lies in the span of the two transverse rows, and `Delta_R=det(W_S)`. The earlier theorem gives

`||p_Q||_infinity <= (192/(c det(W_S)))^(1/3) / s`,

which is sharper than the `3*2^(4/3)[c det(W_S)]^(-1/3)/s` corollary derived in the present report. Accordingly **do not count Sections 3--4 as a new QFORM branch closure**. They remain an independent consistency derivation only.

The genuinely new analytic statement retained from this run is `QFORM-ZEROPIVOT-PLANAR-DENSITY-v1` in Section 2. It assumes only: one cap-one scalar independent of an arbitrary planar vector with joint density cap `M`, an invertible `3x3` quadratic Hessian, and zero scalar pivot. It proves

`||p_Q||_infinity <= 3*2^(2/3) M^(2/3)|det H|^(-1/3)`.

This is not the same premise as the preceding source-span compiler, and it gives a sharper concrete full-line control on the mandatory logarithmic test family. For independent cap-one `X,Y,Z`,

`Q=2XY+Z^2`

has `M=1`, `|det H|=1`, hence

`boxed: ||p_Q||_infinity <= 3*2^(2/3)=4.762203155904598...`.

The rank-two receiver `2XY` itself can still have the logarithmic density `log(1/(2|t|))` for centered unit uniforms. Thus the new estimate is a direct quantitative demonstration that the third square removes the logarithmic singularity. It also improves, on this specific normalized full-line test family, the `5.360042964...` leakage-free pure-hub bound in the later interactive source `a499ab4706b29fa1e864fad1291a9269c22793d5`.

Status after source matching: `NEW_SUPPORTING_ANALYTIC_THEOREM / SHARPER_LOG_PLUS_SQUARE_CONTROL / DUPLICATE_QFORM_APPLICATION_STOPPED / FULL_TARGET_OPEN`.
