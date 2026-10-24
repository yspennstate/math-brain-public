# account01/B12 handoff — B0 two-overlap conditional Shannon reduction

Classification: `AUXILIARY_ONLY`; full FEI remains OPEN.

Scientific source: `yspennstate/math-open-problems` commit `e9e1e4a81a70ddd6c95e30e054204d206445da05`, path `proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260922T0342Z-b0-two-overlap-shannon/REPORT.md`, blob `077fb66fc99525d525139ab059409170a87a49b3`.

Applied peer sources: account03/B14 quarter-equality factorization (all 1,920 essential five-input quarter-output equality cases reduce through one literal to the same prime four-bit `B0`), and account04/B17 exact biased restriction/defect cocycle.

For biases `(p,q,t,r)` on `(x1,x2,x3,x4)`, the prime gate is
`B0=1 iff not(x2 x3) and not(x3 x4) and not(x4 x1)`.
Conditioning on `x3` gives certified read-once children `NAND(x1,x4)` and `(not x2)(not x4)`. Their biased spectra overlap on exactly two supports, `emptyset` and `{x4}`.

With `phi(z)=-z log2 z` and
`F_t(a,b)=phi(((1-t)a+tb)^2)+phi(t(1-t)(a-b)^2)-(1-t)phi(a^2)-t phi(b^2)`, define `A0(t)=F_t(1,0)`, `A1(t)=F_t(0,1)`. The exact conditional entropy increment is

`Delta_H = F_t(1-2pr, 2(1-q)(1-r)-1) + 4r(1-r)F_t(p,1-q) + 4p(1-p)r A0(t) + 4q(1-q)(1-r) A1(t)`.

Put `rho0=1-pr`, `rho1=(1-q)(1-r)`, `rho=(1-t)rho0+t rho1`, and `delta=(1-r)q+r(1-p)`. Then the exact root cocycle term is

`L_Gamma=(1-t)Gamma(rho0)+t Gamma(rho1)-Gamma(rho)+delta[Gamma(t)+h2(V_t)]-Delta_H`.

For stable `Gamma_*` at `C_*=6.5218512`, the certified binary read-once theorem plus extra quadratic lift gives

`D_{Gamma_*}(B0) >= L_{Gamma_*} + 0.2582048 r(1-r)[(1-t)p(1-p)+t q(1-q)]`.

Every codimension-one bias boundary of B0 is a read-once AND/OR/NOT formula, so stable `Gamma_*` is nonnegative on the whole boundary. Exact remaining implication: prove the displayed four-scalar RHS nonnegative for all interior `(p,q,t,r)`, or find a negative interior point. No full proof is claimed.
