# fleet03/B19 r48 finite diagnostics

These computations are sanity checks only; the inequalities in `REPORT.md` have exact proofs.

## Check A — promoted-row exterior-volume inequality

For 3,000 fixed-seed random noncommuting rectangular matrices `M` and independent random symmetric same-bank coefficient blocks, a physical row `d` was appended to `M`. For the actual top-two right singular space `V2(M)`, the checker compared

`lhs = E3([M;d])`

with

`rhs = [s1(M)s2(M)]^2 dist(d,V2(M))^2`.

Results:

- trials: `3000`
- violations: `0`
- minimum observed `lhs/rhs` over non-negligible `rhs`: `0.9999999999999941`
- maximum normalized numerical deficit: `1.95e-15`

This checks the Cauchy--Binet/exterior-product identity used in Theorem 2.1.

## Check B — light-coordinate deletion stability

For 5,000 fixed-seed random matrices constructed with

`s2(N)>=1/64`,

`dist_F(N,rank<=2)<=2^-16`,

and arbitrary leading singular scale, the checker formed the exact top-two right singular leverage

`ell_j=v1(j)^2+v2(j)^2`.

For every coordinate with `ell_j<=1/2`, it deleted that physical column and checked the lower bound derived from the rank-two Gram determinant and Weyl:

`s1(N_j)s2(N_j)
 >= [s1(N)s2(N)/sqrt(2)] (1-64sqrt(2)2^-16)^2`.

Results:

- constructed matrices: `5000`
- violations: `0`
- minimum observed actual product / claimed lower bound: `1.0003054`

## Constants

`gamma0 = 28159/(4194304 sqrt(2)) = 0.00474725242887306...`

`tau = 2^-16`

`delta = 64sqrt(2) tau = 0.0013810679320049757...`

`Gamma0 = (gamma0/sqrt(2))(1-delta)^2 = 0.0033475488096756326...`

With `f0=2^-12` and the completed physical-E3 receiver constant

`C_E3=8.4530212255281768747...`,

`C_E3 (Gamma0^2 f0^2)^(-1/6) = 904.1135320... <905`.

For the designated fleet04/B19 exact-null-coloop theorem, the gate `D_res>=2^-24` gives

`34 sqrt(log(e 2^24)) = 142.7819154... <143`.

Terminal marker: `QFORM_B19_R48_PROMOTED_ROW_CHECK_PASS`.
