# P0282 idea before validation — Kauers–Wang as a Riccati/Turán transfer

Date: 2026-09-18 UTC

This note is written before new checker code. The frozen metric remains `N_exact=75` until an exact all-k extension is actually executed and archived. The source remains Chen's fixed-size LIS log-concavity conjecture.

Fresh Section-B methods for P0282 in this run are:

- **#1 CHANGE THE CATEGORY.** Treat Kauers–Wang recurrence (2) as a one-dimensional positive-sequence transfer from row `n` to row `n+1`, rather than as a permutation recurrence. Write `b_k=a_{n+1,k}` and `d_k=(n+1)^2(a_{n,k}+a_{n,k+1})`. Then
  `(n-k+1)b_k+(n+k+1)b_{k+1}=d_k`.
  This is a backward first-order linear/Riccati system in the long-LIS sector.
- **#13 FIND WHAT ONLY INCREASES.** Derive an exact local Turán-slack criterion from that system and test whether its normalized slack has a monotone direction from the solved boundary `k=n` toward `k=ceil(n/2)`. A genuine monotone slack would be an invariant-region route to long-sector log-concavity; failure must be recorded explicitly.
- **#19 MAKE IT AN ALGORITHM.** Use recurrence (2), seeded by one exact row and the exact boundary `a_{n+1,n+1}=1`, to reconstruct the next long-LIS half-row with integer arithmetic. Validate every reconstructed value independently against hook-length/RSK counts before using the recurrence as a route selector.

Exact identity to test. Put
`alpha=n-k+1`, `beta=n+k+1`, `alpha_prev=n-k+2`, `beta_prev=n+k`.
Eliminating `b_{k-1}` and `b_{k+1}` from two adjacent recurrence equations gives

`alpha_prev*beta*(b_k^2-b_{k-1}b_{k+1})`
` = 2(n+1)b_k^2 + (alpha*d_{k-1}+beta_prev*d_k)b_k - d_{k-1}d_k`.

Thus with `x_k=b_k/d_k` and `q_k=d_{k-1}/d_k`, Chen's Turán sign at `(n+1,k)` is equivalent to

`F_{n,k}(x_k,q_k):=2(n+1)x_k^2 + (alpha*q_k+beta_prev)x_k - q_k >= 0`.

Because `F` is strictly increasing in `x>=0`, there is a unique positive threshold `theta_{n,k}(q)`. Also recurrence (2) yields the exact backward normalized update

`x_k = (1 - beta*(d_{k+1}/d_k)*x_{k+1})/alpha`.

The concrete research questions for this run are:

1. Does the exact Turán slack or normalized threshold slack become monotone in `k` on actual long-LIS rows?
2. Can the recurrence reconstruct the long half exactly from a certified seed row and boundary without partition enumeration?
3. If the route survives those tests, perform a modest exact all-k extension beyond `N_exact=75`; this is validation of movement after the idea, not the idea itself.

No theorem, monotonicity, or metric movement is claimed in this note.