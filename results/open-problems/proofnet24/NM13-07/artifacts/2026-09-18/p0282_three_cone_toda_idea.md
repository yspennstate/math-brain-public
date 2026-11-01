# P0282 idea before code — a three-cone reduction for the Hankel coefficient array

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`

This note is written before the new checker. It continues the already-archived Hankel/Toda reformulation

`A_{k,j} = ell_{k+j,k}/((k+j)!)^2 = [q^j] H_k(q)`

from `p0282_hankel_toda_route.md`, where the source Chen inequality is the diagonal local inequality

`A_{k,j}^2 >= A_{k-1,j+1} A_{k+1,j-1}`.

The key new idea is to stop attacking that diagonal minor directly. There are three coordinate-aligned positivity cones that are much more natural for a Hankel coefficient array:

1. **k-direction log-concavity**

   `A_{k,j}^2 >= A_{k-1,j} A_{k+1,j}`;

2. **j-direction log-concavity**

   `A_{k,j}^2 >= A_{k,j-1} A_{k,j+1}`;

3. **adjacent TP2 / log-supermodularity**

   `A_{k,j} A_{k+1,j+1} >= A_{k+1,j} A_{k,j+1}`.

These three conditions imply Chen locally. Indeed TP2 at `(k-1,j)` and `(k,j-1)` gives

`A_{k-1,j+1} <= A_{k-1,j}A_{k,j+1}/A_{k,j}`

and

`A_{k+1,j-1} <= A_{k+1,j}A_{k,j-1}/A_{k,j}`.

Multiplying and then applying the two coordinate log-concavity inequalities yields

`A_{k-1,j+1}A_{k+1,j-1}`

`<= [A_{k-1,j}A_{k+1,j}][A_{k,j-1}A_{k,j+1}] / A_{k,j}^2`

`<= A_{k,j}^2`.

So Chen is reduced to a package of inequalities aligned with the coefficient axes of the Hankel tau-functions rather than with the anti-diagonal `k+j=n`.

## Why this may be structurally better

- Fixed `k`, the sequence `(A_{k,j})_{j>=0}` is the coefficient sequence of the positive entire function `H_k(q)`. A Laguerre-Pólya / Pólya-frequency mechanism, if available, would attack the j-direction directly.
- Adjacent TP2 is a standard total-positivity shape and is closer to what moment/Hankel matrices and Cauchy-Binet can plausibly preserve.
- Fixed `j`, the k-direction is the previously studied fixed-defect direction but now normalized in a way compatible with the Hankel representation.

The Toda identity

`H_k D^2 H_k - (D H_k)^2 = q H_{k-1}H_{k+1}`

is not itself Chen, but it is evidence that k-neighbor products are naturally controlled inside this coordinate system.

## Falsification-first experiment

Before claiming this route is useful, test all three structural conditions with exact arithmetic on the largest inexpensive complete triangular grid. Any violation kills the package as a universal reduction strategy even though Chen itself might remain true.

The checker should:

- enumerate exact RSK/hook counts for all rows through a moderate cutoff (target `n<=60`);
- form the normalized array exactly (integer cross-multiplication, no floating-point decisions);
- test every source-valid instance of the two coordinate log-concavity inequalities and every adjacent TP2 minor whose four entries lie in the certified grid;
- independently verify partition numbers and Plancherel mass row by row;
- report the first failure, or the exact minimum slack ratio if no failure occurs.

This finite experiment is diagnostic only. Passing it is not an all-n theorem.

## Metric bookkeeping kept separate

The frozen metric remains `N_exact`, the largest complete row cutoff. A separate archived but omitted-from-the-latest-report row-84 certificate is already present on master and must be reconciled honestly before reporting this run. Recovery of that pre-existing certificate is not new mathematical progress. If a new complete row is checked this run, only that new row can move `N_exact`.