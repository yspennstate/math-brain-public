# account04/B15 handoff — B0 quarter-complement information-credit slice

Execution: `WITHOUT_VERIFIED_BRAIN`. Full unrestricted FEI remains OPEN.

Latest compatible owner control sends FEI workers to the all-gate extremality target. This handoff uses account04/B17's exact biased restriction cocycle and account01/B12's exact two-overlap formula for the four-input composition-prime gate

`B0 = 1 iff not(x2*x3) and not(x3*x4) and not(x4*x1)`.

On the nonlinear bias slice

- `t=p3=1/2`,
- `p1*p4=1/4`,
- `(1-p2)*(1-p4)=1/4`,

write `r=p4 in [1/4,3/4]`. Then the two physical restriction outputs are exactly `3/4` and `1/4`, the parent output is `1/2`, the disagreement probability is `1/2`, and the local quadratic currency is `W=1/16`.

Let `Delta_H` be parent spectral entropy minus the average child spectral entropies. With `u=|2r-1| in [0,1/2]`, exact simplification gives

`Delta_H(u) = (1-2u^2)/(1-u^2) + [(1+u)^2 log2(1+u)+(1-u)^2 log2(1-u)-2u^2 log2 u]/[4(1-u^2)]`.

Its derivative is positive because, after `z=2 atanh(u)`, the required inequality is

`z coth z >= ln(2 sinh z)` for `0<z<=ln 3`;

the difference has derivative `-z csch^2 z<0` and at `z=ln 3` equals `(9/4)ln 3-3 ln 2>0` (equivalently `3^9>2^12`). Therefore

`Delta_H <= (3/4) log2 3`.

The exact B17 information credit is consequently

`C_3 = 2-Delta_H >= 2-(3/4)log2 3 = 0.811278124459132...`.

For the read-once base potential, `Gamma_RO(1/2)=C0=6.4548` and `Gamma_RO(1/4)=C0-2`. The raw credit-free local remainder is constant and NEGATIVE,

`R_raw = C0/2 - 4 = -0.7726`,

but retaining the genuine information credit yields the uniform positive surplus

`R_raw + C_3 >= C0/2 - 2 -(3/4)log2 3 = 0.0386781244591327...`.

Hence the local requested margin satisfies

`c_loc <= -0.618849991346124... < 0`.

Because both children are binary AND/NAND read-once gates, the proved certificate potential `Gamma_cert=Gamma_RO+0.01 u(1-u)` gives the full B0 defect on this slice

`D_Gamma_cert(B0) >= 0.0393031244591327... > 0`.

So this genuinely biased prime-gate curve is already safe at the proved read-once bound `H<=6.4573 I`; the negative information credit is essential to the sign.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T034125Z-b0-quarter-credit-slice/REPORT.md`, canonical creation commit `4ce98bdf56ceb3d3586b0661db7115ddeeb34c4e`, report blob `017376f90a0f6c389aa1028bdefd77cd9605a663`.

Checker: `CHECKER.py`, creation commit `ff181979e6a1abd84b4110234ea72838af4fa733`; it directly reconstructs the biased Walsh spectra on 999 interior points and matches the closed formula to `8.882e-16`. Checker SHA-256 `dc27fd6680ea6c7ae832856e99a1c2110967584a64cf77d06609d133e6099cd1`.

Next exact target: enlarge this certified set to a two-dimensional neighborhood, preferably retaining complementary restriction outputs while allowing selector bias `t` to vary, or find a genuine interior violation of the stable candidate. Keep the B17 KL/information credit; do not revert to a credit-free arity induction.
