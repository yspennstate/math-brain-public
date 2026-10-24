# account02/B15 handoff — fixed-multiplicity audit

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.

Pinned baseline audited end-to-end: `math-open-problems` source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Verdict: mathematical PASS for the stated `s_17(A)>=s` theorem, with one non-fatal notation GAP in the final indefinite-pair paragraph: `||A/B||` is undefined and should be replaced by the already-defined Schur complement `S=D-C^TB^{-1}C`. Gaussian inversion and the Riesz half-potential constant `1/sqrt(2*pi)` were independently rebuilt; the order-three weighted integral is exactly `12 sqrt(u/(2*pi))`. Rough-law scope is correct: only the no-pivot `L^1` characteristic-function branch gets continuity; pivot branches establish essential bounds by measure domination/Tonelli and do not smuggle continuity.

Constants independently rebuilt: quarter-power Gaussian coefficient `3.9952593615<16`; no-pivot nine half-potential `176.959336<200`; no-pivot seventeen density `2174.625463<2400`; pivot-H branches all `<600`; scalar main branch `6010<10000`; indefinite pair main branch `238.998<251`.

Counterexample/method obstruction: order four would yield only a `C/|t|` Fourier envelope. This is insufficient for bounded density: for independent standard Gaussians `G,H`, `Z=GH` has `phi_Z(t)=(1+t^2)^(-1/2)` and logarithmically divergent density at zero. This blocks the naive `k=5 -> k=4` absolute-inversion reduction but does not disprove a lower fixed-multiplicity theorem.

No lower threshold is claimed; unrestricted three-eigenvalue QFORM remains open. Full immutable audit: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account02/B15/20260924T133137Z-account02-B15-fixed-multiplicity-r11/AUDIT.md` at commit `d01f2b13d10ea0759370bca5880634b3a2fb2e85`.
