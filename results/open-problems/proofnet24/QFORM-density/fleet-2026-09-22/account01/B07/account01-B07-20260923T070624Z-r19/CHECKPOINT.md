SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T07:06:24Z.
attacking: the partner edge-plus-E2 survivor via exact scalar-anchored Schur compound identities; force anchored fifth volume or a quantitative rank-2/3/4 residual tube without selecting one tiny minor.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: supporting structural calculation; full QFORM remains OPEN.
Execution: `WITHOUT_VERIFIED_BRAIN`.

Immediate partner input actually used: account02/B07 checkpoint `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/account02-B07-20260923T063044Z-r11/CHECKPOINT.md`, which receives from account03/B07 r26 a residual physical cross block `N` with

`E2(N) >= 3 ||N||_F^4/16`

inside an actual scalar-edge augmentation

`B = [[b,u^T],[v,N]]`, `b != 0`.

Write the exact scalar Schur complement

`S = N - v u^T/b`.

For `q>=2`, let `H_q` be the sum of squared determinants of all physical `q x q` minors of `B` containing the distinguished anchor row and distinguished anchor column. Exact block determinant expansion gives

`H_q = b^2 E_{q-1}(S)`,

where `E_k(S)=e_k(SS^T)` is the full aggregate squared `k x k` minor mass. In particular

`H_3=b^2 E_2(S)`, `H_4=b^2 E_3(S)`, `H_5=b^2 E_4(S)`.

For singular-square values `mu_1>=mu_2>=...` of `S`, let `T_k(S)=sum_{j>k} mu_j`. The compound-tail ladder gives

`T_k(S) E_k(S) <= (k+1) E_{k+1}(S)`,

hence the sharp anchored recursion

`T_k(S) H_{k+1} <= (k+1) H_{k+2}`.

Also `N=vu^T/b+S`, so approximating `S` by rank `k` gives

`dist_F(N,{rank<=k+1})^2 <= T_k(S)`.

This yields a clean threshold-1/4 quadrichotomy from the partner E2 branch. Put `G=||N||_F`.

1. If `E2(S)<E2(N)/256`, then using `T_1(S)^2<=2E2(S)` and `E2(N)<=G^4/2`,

`dist_F(N,{rank<=2}) < G/4`.

2. Otherwise

`H_3=b^2E2(S) >= b^2 E2(N)/256 >= 3 b^2 G^4/4096`.

If `T_2(S)<=G^2/16`, then `dist_F(N,{rank<=3})<=G/4`.

3. If instead `T_2(S)>G^2/16`, then

`H_4 >= (G^2/48) H_3`.

If `T_3(S)<=G^2/16`, then `dist_F(N,{rank<=4})<=G/4`.

4. If also `T_3(S)>G^2/16`, then

`H_5 >= (G^2/64)H_4 >= b^2 G^8/2^22`.

Since `E5(B)>=H5`, the completed fifth-volume receiver from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, gives in branch 4

`||p_Q||_infinity <= 5 sqrt(2e) E5(B)^(-1/10)
 <= 5 sqrt(2e) 2^(11/5) |b|^(-1/5) G^(-4/5)`.

Thus the exact cancellation geometry seen by account02/B07 is not an unstructured obstruction: either it pushes the residual core into a quantitative rank-2/3/4 Frobenius tube, or the same fixed physical anchor generates enough fifth-volume mass to pay the full ambient density directly. No individual coordinate minor is reciprocated.

Next: write the complete proof carefully, propagate the inherited parent-scale edge/star bounds into the D5 inequality, and identify the first unpaid receiver among the three rank-tube branches.