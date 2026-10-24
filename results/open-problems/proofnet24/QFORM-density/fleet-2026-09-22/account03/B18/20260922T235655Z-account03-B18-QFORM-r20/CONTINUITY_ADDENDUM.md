# account03/B18 r20 — continuity proof addendum

This addendum corrects one sentence in `REPORT.md` without changing the theorem or its constants.

The report says that the convolution of two `L^1(R)` functions is continuous and vanishes at infinity. That statement is too broad as written and is **not** the justification used here.

For every nonzero coefficient `a_j`, the density of `a_j X_j` is a probability density with finite `L^infinity` norm `<=1/|a_j|`. Hence it lies in `L^1 cap L^infinity subset L^2`. Under `sum a_j^2=1` and `max_j a_j^2<=4/9`, there are at least three nonzero coefficients, so choose any two. If their scaled densities are `f,g in L^2(R)`, Plancherel gives `hat f,hat g in L^2`, and Cauchy--Schwarz gives `hat f hat g in L^1`. Therefore

`f*g = inverse_Fourier(hat f hat g)`

has a continuous representative vanishing at infinity. Convolution with each remaining probability measure/density preserves continuity and the `C_0` property by dominated convergence / translation averaging. Thus the linear aggregate in `QFORM-DIFFUSE-BANK-KK-ROGOZIN-v1` indeed has a continuous density.

All `L^infinity` estimates, the Juškevičius--Lee reduction, the König--Koldobsky sinc/Hölder calculation, the account04/B18 splice, and the strict-N3 application are unchanged.

**Status after correction:** theorem and constants unchanged; continuity conclusion remains proved. Full N3 and full QFORM remain open.
