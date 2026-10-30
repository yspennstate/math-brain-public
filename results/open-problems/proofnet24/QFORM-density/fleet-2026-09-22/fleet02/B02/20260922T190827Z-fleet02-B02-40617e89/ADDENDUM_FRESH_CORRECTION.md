# Fresh-correction compatibility addendum

After `REPORT.md` was archived, fresh event `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` appeared at brain commit `6f841c38ee2ac5d6456851e23e01f574bb2ba5b8`, with canonical math source `yspennstate/math-open-problems@b74210c7e963a11c1f0532f98f5d705278967cd1`. It shows that a merely small nonzero scalar Schur diagonal plus a fixed cross-row norm does not give a uniform endpoint half-Riesz bound: the rank-one quadratic form

`epsilon X^2+2XY+epsilon^(-1)Y^2 = epsilon (X+Y/epsilon)^2`

has infinite `H_(1/2)` for centered unit uniforms.

This does not invalidate `QFORM-SUBCRITICAL-PAIR-TRACE-v1`; it is an exact reason for using `alpha<1/2`. Lemma 4.1 applied to the same correction family gives, for every `0<alpha<1/2`,

`H_alpha <= [2^(3alpha)/(1-2alpha)] |epsilon|^(-alpha)`.

In particular

`H_(1/4) <= 2^(7/4)|epsilon|^(-1/4)`.

Thus the endpoint can diverge while the quarter-trace used by the new pair theorem remains finite. The price necessarily deteriorates as `epsilon ->0`; this run makes no false near-zero uniformity claim. The structural first unpaid implication therefore remains quantitative: it must force a lower bound on the product resource `D*kappa*|d|` or route the near-zero case to a different already-proved zero-diagonal/bank mechanism.

Status remains `ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN`.
