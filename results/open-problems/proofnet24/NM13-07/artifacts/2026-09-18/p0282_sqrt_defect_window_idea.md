# P0282 idea before validation — Plancherel hook correction and a growing-defect window

Date: 2026-09-18 UTC
Track: `proofnet24/NM13-07`
Source: P0282, Chen fixed-size LIS log-concavity

The previous run showed that grinding fixed defects is strategically weak: if `E_j(n)=ell_{n,n-j}`, then for each fixed `j`, `E_j(n)^2/(E_{j-1}(n)E_{j+1}(n)) -> (j+1)/j`, while the finite near-minimizer moves to growing `j`.

This run therefore tries the reserved methods #11, #20 and #30 without extending the finite cutoff merely for its own sake.

## #11 DUALIZE

Use the exact hook formula from the preceding report. For `mu |- j` and `n>=2j`, put

`R_mu(n,j) = prod_{c=1}^{mu_1} (n-j-c+1)/(n-j-c+1+mu'_c)`.

With Plancherel measure `P_j(mu)=(f^mu)^2/j!`, the exact boundary count factors as

`E_j(n) = ((n)_j^2/j!) A_j(n)`,

where

`A_j(n)=E_{mu~P_j}[R_mu(n,j)^2]`.

Thus the Chen margin at defect `j` is dualized to an adjacent-ratio correction:

`E_j(n)^2/(E_{j-1}(n)E_{j+1}(n))`

`= ((j+1)/j) ((n-j+1)/(n-j))^2 * A_j(n)^2/(A_{j-1}(n)A_{j+1}(n))`.

The factorial/falling-factorial factor is explicitly log-concave. The only obstruction is the curvature of the shape-correction sequence `A_j`.

## #30 ONE SCALE / ONE DIRECTION

A shape-uniform lower bound already yields a nontrivial growing-defect theorem. Since `sum_c mu'_c=j` and `n-j-c+1 >= n-2j+1`,

`log R_mu(n,j) = -sum_c log(1 + mu'_c/(n-j-c+1)) >= -j/(n-2j+1)`.

Hence

`exp(-2j/(n-2j+1)) <= A_j(n) <= 1`.

Using only `A_j` below and `A_{j-1},A_{j+1}` above gives

`Q_j(n):=E_j(n)^2/(E_{j-1}(n)E_{j+1}(n))`

`>= ((j+1)/j) ((n-j+1)/(n-j))^2 exp(-4j/(n-2j+1))`.

Since `log(1+1/j) > 1/(j+1)`, it is enough that

`1/(j+1) >= 4j/(n-2j+1)`,

i.e.

`n >= 4j^2 + 6j - 1`.

So the candidate theorem is: Chen's inequality is strict at `k=n-j` whenever `j>=1` and `n>=4j^2+6j-1`. Equivalently, for every `n`, all defects

`1 <= j <= floor((sqrt(4n+13)-3)/4)`

are certified. This is a uniform `j = O(sqrt n)` boundary window, not merely fixed-defect eventual positivity.

## #20 FIND WHY THE ALGORITHM FAILS

The same inequality diagnoses the limitation of this crude route. Its positive factorial margin is `log(1+1/j) ~ 1/j`, while the worst-shape correction loss is `4j/n`. They balance at `j ~ sqrt n`. Thus any attempt that uses only the shape-uniform bound on `R_mu` cannot enter `j >> sqrt n`: the estimate, not necessarily the conjecture, fails there.

To go farther one needs genuinely distributional information under Plancherel measure — for example concentration or curvature control for `log R_mu` — or an exact recurrence with a proved TP2/sign-preserving kernel. The Kauers--Wang 2026 paper advertises bivariate recurrences, but this invocation must inspect exact coefficients before claiming they preserve adjacent-ratio positivity.

This note records the mathematical route before any archival checker/certificate for it.