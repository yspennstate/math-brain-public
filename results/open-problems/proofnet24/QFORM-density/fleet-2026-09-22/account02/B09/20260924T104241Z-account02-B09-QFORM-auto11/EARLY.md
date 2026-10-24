# Early substantive implication: scalar-pivot grouped-crossing currency is not forced

Programme `QFORM-DENSITY-3EIG-20260922`. Full QFORM remains OPEN.

First unpaid implication after this calculation:

`QFORM-SMALL-SCALARPIVOT-CURRENCY-TO-MIXEDFRAME-OR-CROSSVOLUME-v1`:
from `s_3(A)>=1`, after already-paid physical-pair/core exits, convert the survivor in which every scalar-pivot grouped-rank-two Schur currency is small into a pre-pivot literal source-coordinate mixed frame, projected-crossing volume, or bounded physical core. Do this without deleting small quadratic terms, taking worst conditional projection-density suprema, or asserting post-rotation independence.

## Construction

Let `m=2^k>=8`, and choose three distinct flat orthonormal Sylvester-Walsh vectors `c,w1,w2 in R^m`. With original independent cap-one variables `U,Y_1,...,Y_m`, define

`Q_m = 2 U <c,Y> + <w1,Y>^2 + 2 <w2,Y>^2`.

Thus

`A_m = [[0,c^T],[c,L]]`,  `L=w1 w1^T+2 w2 w2^T`.

The same-side leaf block is physically dense: writing `w_{r,i}=sigma_{r,i}/sqrt(m)`,

`L_ij=(sigma_{1,i}sigma_{1,j}+2 sigma_{2,i}sigma_{2,j})/m in {+-1/m,+-3/m}`,

so no leaf-leaf coefficient vanishes.

In the orthonormal coefficient basis `(U,c,w1,w2)`, the active operator is

`[[0,1],[1,0]] direct_sum [1] direct_sum [2]`,

hence

`spec_nonzero(A_m)={-1,1,1,2}`.

So every member is target-valid.

## Every scalar-pivot grouped-crossing currency collapses

The hub has `A_UU=0`, so account03/B09 r48's scalar-pivot theorem cannot use it. Every leaf pivot `j` has

`a_j=A_jj=3/m`.

Let `u_j=A_{-j,j}` and let

`S_j=A_{-j,-j}-u_j u_j^T/a_j`

be the exact scalar Schur complement. Since `c,w1,w2` are orthonormal,

`(A_m^2)_{jj}=c_j^2+w1_j^2+4w2_j^2=6/m`,

therefore

`||u_j||_2^2=6/m-9/m^2`

and

`||u_j u_j^T/a_j|| = 2-3/m`.

Also `||A_m||=2`, so

`||S_j|| <= ||A_{-j,-j}|| + ||u_j u_j^T/a_j|| <= 4-3/m`.

For ANY literal two-row set `I` and ANY disjoint original-coordinate bank `J`, the Schur crossing `C=S_j[I,J]` obeys

`sigma_1(C)sigma_2(C) <= ||C||^2 <= (4-3/m)^2`.

Consequently every r48 scalar-pivot currency satisfies

`|a_j|^2 sigma_1(C)sigma_2(C)
 <= (9/m^2)(4-3/m)^2 < 144/m^2 ->0`.

Even the naive aggregate over all possible nonzero scalar pivots collapses:

`sum_j sup_{I,J} |a_j|^2 sigma_1(C)sigma_2(C)
 <= (9/m)(4-3/m)^2 < 144/m ->0`.

Thus the bare three-large-eigenvalue hypothesis cannot force a universal r48 scalar-pivot currency, nor can a simple l1 aggregation of those same post-pivot currencies repair the implication.

At `m=1024`, the maximum possible currency is at most `0.0001371280095554539`, and the sum of the maxima over all nonzero pivots is at most `0.1404190817847848`.

## Pinned mixed-hub theorem pays the same law before pivot selection

Apply Theorem H from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` with literal hub `H={U}`, leaf bank `I={Y_i}`, two Fresnel directions `w1,w2`, coefficients `1,2`, and `D=0`. The physical mixed rows are

`rho_i=(w1_i,w2_i,c_i)`.

Their Gram is exactly `G=I_3`, and every leverage is `3/m<=3/8<1/2`. Hence

`|phi_{Q_m}(t)| <= 4 sqrt(2) pi^2 |t|^{-2}`.

Integrating `min(1,4 sqrt(2) pi^2 |t|^{-2})` gives

`||p_{Q_m}||_infinity <= 4*2^(1/4) = 4.756828460010884...`,

and therefore

`P{Q_m in E} <= 4*2^(1/4)|E|`

for every interval `E`. This branch has a continuous density. No probability squaring or square-root small-ball loss occurs, and the dense same-side leaf matrix `L` is retained exactly.

By contrast, account03/B09 r48's scalar-pivot theorem has right-hand side

`2^(11/4) [|a|^2 Delta_2]^(-1/4)`.

Since every admissible currency above is at most `(9/m^2)(4-3/m)^2`, even the numerically best such certificate is at least `62.165716713999...` when `m=1024`, versus the pre-pivot mixed-frame bound `4.756829` for the same full law.

This is a source-valid counterexample to the scalar-pivot-currency forcing mechanism, not to QFORM itself.
