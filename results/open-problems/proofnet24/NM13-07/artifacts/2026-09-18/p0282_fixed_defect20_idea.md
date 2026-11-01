# P0282 idea before code — fixed-defect polynomial cone from the Kauers–Wang transfer

Date: 2026-09-18 UTC

This note is written before the new checker. It continues the admitted P0282 source and does not alter the frozen metric or claim closure.

Fresh Section-B methods for this run:

- **#3 PROVE SOMETHING STRONGER.** Instead of only testing the empirical normalized slack `S_{n,k}`, try to turn the long-LIS recurrence into exact polynomial Turán certificates for an entire fixed-width boundary strip, for all `n`.
- **#6 DEFORM TO A POINT YOU CAN SOLVE.** Move to defect coordinates `j=n-k`, where the long-LIS recurrence becomes a recursion in `j` for exact fixed-defect polynomials.
- **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE.** Use exact RSK only for the finite pre-polynomial bridge, and independently inspect the shifted coefficient cones before deciding what theorem is actually certified.

Write `E_j(n)=ell_{n,n-j}`. Define integer polynomials `P_j(n)=j! E_j(n)` on the recurrence-valid fixed-defect range. Kauers–Wang recurrence (2), after putting `k=n-j` and shifting the row index, suggests the exact polynomial recursion

`P_0(n)=1`, `P_1(n)=(n-1)^2`,

`P_{j+1}(n) = n^2 [P_j(n-1)+j P_{j-1}(n-1)] - (2n-j-1)P_j(n)`.      (A)

For a Chen margin at defect `j`,

`E_j(n)^2-E_{j-1}(n)E_{j+1}(n)`

has the same sign as the integer polynomial

`D_j(n) := (j+1)P_j(n)^2 - j P_{j-1}(n)P_{j+1}(n)`.                 (B)

The planned theorem test is deliberately finite and source-faithful: for `1<=j<=20`, generate `(A)` exactly and test whether every coefficient of

`D_j(m+2j+1)`

is strictly positive. If so, then once `(A)` is justified from the proved Kauers–Wang recurrence, it gives strict Chen log-concavity for every `n>=2j+1` at those defects. The remaining finite source-valid range `j+2<=n<=2j` will be checked independently by exact RSK/hook arithmetic, not by evaluating a polynomial outside the range where the recurrence has been identified with the source counts.

Only after this theorem route is worth checking will code be written. As an independent frozen-metric movement, a full exact RSK enumeration of row `n=77` will be attempted; it moves `N_exact` only if every source inequality and the factorial/partition-count checks pass. The fixed-defect theorem does not silently redefine `N_exact`.

Scope guard: even a successful `j<=20` theorem is PARTIAL relative to Chen's all-`n`, all-`k` conjecture. A finite coefficient cone is a certificate for this bounded defect strip, not evidence that the same cone holds for arbitrary `j`.