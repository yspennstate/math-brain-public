# Verification — B16 arbitrary-residual OR-lift

The committed standard-library checker logic was replayed locally in this invocation.

Results:

- 300 small truth-table parent/child cases checked across `2<=r<=4`, `1<=m<=4` and arbitrary sampled residual events `R`;
- exact-formula comparisons for both `Delta_T H` and `D_T` agreed to maximum floating discrepancy `1.5765166949677223e-14`;
- 7,878 theorem-regime scalar points checked for `2<=r<=79` and `0<=s<=q/[16(1-q)]`;
- every sampled scalar point satisfied `Delta_T H <= 5 D_T`;
- largest unrestricted small truth-table ratio observed was `Delta_T H/D_T = 3.8346950634254178`;
- analytic proof coefficients recorded by the checker are `2369/512 = 4.626953125` on `qr` and `(17/8+1/16+4/47)/ln 2 = 3.278677958616009` on `q`, each strictly below the corresponding coefficient in `5 q[1+47r/48]`.

The finite checks are sanity checks only; the universal coefficient-five statement is proved analytically in `REPORT.md`.
