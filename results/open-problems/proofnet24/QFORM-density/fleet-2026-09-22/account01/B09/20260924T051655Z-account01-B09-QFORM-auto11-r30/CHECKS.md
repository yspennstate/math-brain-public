# Deterministic checks — account01/B09 r30

These computations are regression checks only; the report proofs are algebraic.

## Constants

`C3=3*2^(4/3)*exp(1/3)=10.550168831164775`.

At `Omega_0=13/48`,

`2*C3*(13/48)^(-1/6)=26.232462019716287 < 26.233`.

Partner rough-star/pair-log constant:

`C_RS=4*sqrt(2)*exp(1/4)*sqrt(Gamma(1/4))=13.830540321993613`.

For `D_B*kappa*||m||=8`,

`C_RS*8^(-1/4)=8.223688477623414 < 8.224`.

## Edge-frame gap regression

For flat `u=(1,...,1)/sqrt(17)`, hence `q=1/17`, a fixed-seed random symmetric operator on `u^perp` was projected to the Frobenius-orthogonal complement of

`K_u={P diag(d)P}`.

The residual satisfied

`||Fu||_2 < 6e-16`, `max_i |F_ii| < 1.4e-15`.

The direct ordered disjoint currency and residual norm were

`D_u(F)=121.11541735830438`,
`||F||_F^2=145.84314840229106`,

so

`D_u(F)/||F||_F^2=0.830449826989622`,

while

`1-3q=14/17=0.8235294117647058`.

The full edge-frame matrix obeyed Parseval to floating error:

`sum_(I,J)|v_I^T F v_J|^2 / ||F||_F^2 = 1.000000000000000`.

## Physical determinant regression

A ten-leaf exact singular-pair instance was generated with a non-axis-aligned physical pair basis. For every ordered pair of disjoint leaf edges `I,J`, the direct grouped determinant was compared with

`-s^2 v_I^T E v_J`.

Maximum absolute discrepancy: `4.44e-16`.

Summing only over disjoint `I,J` gave

`s^4 D_u(E)=52.596448494609035`.

The Frobenius sum of the corresponding literal physical `2x2` determinant matrices was

`88.0484527074766`,

so the physical subset inequality in Report (3.2) held with ratio

`88.0484527074766 / 52.596448494609035 = 1.6740379859773475`.

## Partner target example

For

`Q_*=4UV+3X^2+2XZ_1+Z_2^2`,

the coefficient matrix is

`[[0,2],[2,0]] direct_sum [[3,1],[1,0]] direct_sum [1]`.

Its eigenvalues are

`{-2,-0.3027756377319946,1,2,3.302775637731995}`,

so at least four have absolute value at least one. The partner parameters are

`D_B=4`, `kappa=2`, `||m||=1`,

and the completed partner theorem gives `8.223688477623414`.
