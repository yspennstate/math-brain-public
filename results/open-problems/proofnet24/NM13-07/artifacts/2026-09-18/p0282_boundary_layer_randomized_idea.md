# P0282 idea before code — Plancherel tail truncation and fixed-depth boundary layers

Date: 2026-09-18 UTC
Track: NM13-07
Target: P0282, Chen fixed-size LIS log-concavity

This note is intentionally written before the new checker. It records the mathematical route rather than a certificate.

## Runtime/method-history constraint

The recovered P0282 history has genuinely used 28 of the 30 Section-B moves. The only unused moves are #9 RANDOMIZE and #22 READ THE FAILURES, NOT THE SUCCESSES. Therefore this run cannot honestly claim three previously unused moves. It will use those two unused moves and, if needed, explicitly recycle #30 DO ONE SCALE / ONE DIRECTION AT A TIME; the recycled method will be labeled recycled rather than falsely called untried.

## #9 RANDOMIZE — completion as a Plancherel tail expectation

For defect `q`, put `N=n-q`. The residual-partition formula already established on this track is

`E_q(n)=ell_{n,n-q}=1/(q!)^2 * sum_{mu|-q, mu_1<=N} (f^mu)^2 R_mu(N)^2`,

where

`R_mu(N)=prod_{i=1}^q (N+i-mu_i)`

with `mu` padded by zeroes. The polynomial completion drops the event `mu_1<=N`:

`Etilde_q(n)=1/(q!)^2 * sum_{mu|-q} (f^mu)^2 R_mu(N)^2`.

Under Plancherel measure `P_q(mu)=(f^mu)^2/q!`, this is an exact truncated-expectation identity:

`E_q(n)=(1/q!) E_q^Pl[ R_mu(N)^2 1_{mu_1<=N} ]`,

`Etilde_q(n)=(1/q!) E_q^Pl[ R_mu(N)^2 ]`.

So the completion error is not an uncontrolled algebraic artifact: it is an explicit positive tail expectation over `mu_1>N`. Near the boundary `n=2j-s`, that tail has only finitely many possible *deficits from the one-row partition*, independent of `j` when `s` is fixed.

Let the neighboring defect be `q=j+t` with `t in {-1,0,1}` and set `n=2j-s`. Write an invalid residual partition as

`mu=(q-r, lambda)`, where `lambda|-r`.

Then `N=n-q=j-s-t`, and the first residual factor is

`N+1-mu_1 = r-(s+2t)+1`.

Invalidity is `r < s+2t`; the endpoint `r=s+2t-1` has zero residual factor. Therefore the *nonzero* completion error is exactly supported on

`0 <= r <= s+2t-2`.

For fixed depth `s`, this gives a finite tail-correction formula involving only partitions of integers up to `s` (for `t=1`). This is the randomized route's useful deterministic output.

## #22 READ THE FAILURES, NOT THE SUCCESSES — what the literature leaves missing

Fresh 2026-09-18 searches recovered three relevant lines:

1. Bóna–Lackner–Sagan, arXiv:1511.08653, state Chen's fixed-size conjecture and prove only analogues/restricted shape families plus a limiting log-concavity statement.
2. Gao–Xie–Yang, arXiv:1703.06382, obtain Schur-positive restricted families and explicitly present them as an approach to Chen's original conjecture, not a resolution.
3. Baslingker–Krishnapur–Madiman, arXiv:2412.15116, prove the Poissonized Plancherel top-row law log-concave and call it the first positive result toward Chen's conjecture. Kauers–Wang, arXiv:2609.02220, supply long-LIS recurrences but do not claim fixed-size log-concavity.

The recurring failure is the fixed-size/de-Poissonization boundary: positive statements in Poissonized or specially restricted models do not automatically preserve the fixed-`n` Turan inequalities. The track's completion method has the same failure in miniature: at `j=4,n=6` the completion Turan quantity is negative while the true source margin is positive. The new route therefore corrects the truncation exactly rather than trying to prove a false surrogate.

## recycled #30 — one boundary depth at a time

The predecessor solved depth `s=2`, i.e. `n=2j-2`, by classifying the completion tail exactly. The next target is `s=3`, i.e. `n=2j-3`. The formula above predicts:

- for `E_{j-1}` (`t=-1`): no nonzero offenders;
- for `E_j` (`t=0`): only tail sizes `r=0,1`, i.e. residual shapes `(j)` and `(j-1,1)`;
- for `E_{j+1}` (`t=1`): only tail sizes `r=0,1,2,3`, i.e. seven shapes total for sufficiently large `j`.

Instead of hard-coding those seven formulas, write an exact finite-tail evaluator generated from the partition tails. If depth 3 works, use the same theorem to test several fixed depths `s` in one checker. Any promoted theorem must be source-valued: subtract the exact completion tails first and then test

`E_j(n)^2-E_{j-1}(n)E_{j+1}(n)>0`.

A successful depth scan for every `s=3,...,S` and every `4<=j<=100` (only source-valid pairs `n>=j+2`) would combine with the predecessor `n>=2j-2` result to improve the restricted theorem from `n>=2j-2` to `n>=2j-S`. The frozen metric `N_exact` remains separate and only moves if a new complete row is independently certified.
