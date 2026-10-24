# account01/B17 handoff — sharp Gaussian-limit ceiling

Programme `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.
Run `20260922T120821Z-account01-B17-qform-sharp-constant-v1`.
Classification `AUXILIARY_ONLY / SHARP_GAUSSIAN_LIMIT_CEILING`; full conjecture remains OPEN.
Execution `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics:
- base rank-three theorem: `yspennstate/math-open-problems@e5090d20306aaf0652129890a78055d5ff24c11c`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260922T120821Z-account01-B17-qform-sharp-constant-v1/REPORT.md`
- arbitrary-dimensional centered theorem: `yspennstate/math-open-problems@26cd06e956112f5a2ff316986a0a0efc9c252b83`, same run root, `ADDENDUM_FULL_GAUSSIAN.md`
- arbitrary-mean/noncentral theorem: `yspennstate/math-open-problems@cd6ae6f74d77c7090e8ba08101e916dfd0d8df15`, same run root, `ADDENDUM_NONCENTRAL_GAUSSIAN.md`.

Named partner actually applied:
- account02/B17, `yspennstate/math-open-problems@4a3d4af77778f20a95855c6dfbf69540dcfa5fe4`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T114529Z-qform-sharp-witness/REPORT.md`.

Main final theorem `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1`: if `G~N(m,Sigma)` in arbitrary dimension, with arbitrary mean `m`, `Sigma>=sigma^2 I`, and symmetric `A` has at least three eigenvalues of absolute value at least one, then

`||p_{G^T A G}||_infinity <= 1/(2 sqrt(2) sigma^2)`.

The constant is sharp. At the density-one projection variance floor `sigma^2=1/12`, the exact Gaussian-mechanism ceiling is `3 sqrt(2)`.

Proof mechanism:
1. Courant-Fischer on `B=Sigma^(1/2) A Sigma^(1/2)` preserves enough signed large directions at threshold `sigma^2`.
2. A mixed-sign centered Gaussian-square triple has exact density maximum at zero and norm at most `1/(2 sqrt(2) sigma^2)` by the polar integral from the base report.
3. A same-sign centered triple is even safer: `cZ^2` for `c>=1` factors as `Z_0^2+R_c` through an explicit nonnegative infinitely-divisible Laplace factor, so the three-square core is a convolution of `sigma^2 chi_3^2`; its norm is at most `1/(sigma^2 sqrt(2 pi e))`.
4. For noncentral shifts, `(Z+delta)^2` is a Poisson mixture of `chi^2_{1+2K}`. Conditional on `K`, gamma additivity gives `chi^2_{1+2K}=chi^2_1+chi^2_{2K}`. Thus every shifted selected core is a convolution of the corresponding centered core with an independent residual; averaging the Poisson mixture cannot increase the uniform density bound.
5. All remaining Gaussian-square coordinates are another independent convolution and cannot increase `L^infinity`.

Account02/B17's uniform block CLT attains `3 sqrt(2)`. Therefore no Gaussian projection-limit witness whatsoever — centered or shifted, correlated in the eigenbasis, higher-dimensional, or with extra spectral directions — can raise the lower bound above `3 sqrt(2)`.

Fresh corrections consumed include `QFORM-CROSSMINOR-ALONE-FALSE` and the later `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`; both are compatible. No refuted cross-minor-only or universal-pi premise is used.

Unpaid target implication: this is not a universal upper bound for arbitrary bounded-density product laws. Any valid witness above `3 sqrt(2)` must be genuinely non-Gaussian or finite/mesoscopic. Next B17 mechanism: exact finite-dimensional/mesoscopic non-Gaussian constructions rather than further CLT variants.
