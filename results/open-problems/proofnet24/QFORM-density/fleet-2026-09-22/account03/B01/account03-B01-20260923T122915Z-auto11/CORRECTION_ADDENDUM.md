# Correction addendum — continuity scope

This addendum corrects one overclaim in `REPORT.md` while preserving the proved density-height theorem.

## Correct status

The proof of `QFORM-INDEFINITE-PAIR-PLUS-SQUARE-LOG-v1` rigorously proves **absolute continuity and the stated essential-supremum bound**

`||p_Q||_infinity <= 2 D_B^(-1/2) Psi(8 sqrt(D_B/(kappa rho)))`,

with `Psi(R)=2sqrt(R)` for `R<=1` and `Psi(R)=2+log R` for `R>=1`.

However, the final continuity sentence in Section 4 of `REPORT.md` is too strong in the theorem's full stated scope. When the completed-pair translation `m_c(X_D)` depends on the same `D`-bank that generates the square remainder, the unconditional density is a mixture

`p_Q(t)=E_D p_pair,D(t-S(D))`,

not a fixed convolution of two independent densities. The pair densities have logarithmic critical singularities, so their individual `C_0` property plus the final averaged `L^infinity` bound does not by itself provide a valid dominated-convergence proof of continuity in `t`.

Therefore:

- **essential boundedness / absolute continuity:** PROVED in the full scope of Theorem 4.1;
- **continuous `C_0` representative:** NOT PROVED in that full scope by this argument;
- if `m_c` is independent of `X_D` (in particular, there is no pair--D coupling after the outside conditioning), then the pair term and grouped square are independent and their `L^1` densities convolve, so the `C_0` conclusion is valid in that narrower subcase.

All numerical constants, layer-cake estimates, the signed-Fejer density-height consequence, and the account04/B01 partner application remain unchanged.

This correction is intentionally additive rather than rewriting the immutable original report.
