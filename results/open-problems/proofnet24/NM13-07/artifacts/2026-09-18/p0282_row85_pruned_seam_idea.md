# P0282 idea before code — certify row 85 by stitching the all-defect theorem to a low-LIS partition seam

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`  
Frozen metric on entry: `N_exact = 84`  
Retained complete source-valid defect theorem: `1 <= j <= 66`  
Source status: `OPEN`; worker status: `PARTIAL`

## Why the failed full row-85 attempt was solving far too much

The previous exact row certificates enumerated every partition of `n` and reconstructed the entire Plancherel/LIS row. But the retained theorem already proves every Chen inequality at fixed defect

`j = n-k <= 66`

for every source-valid `n`. On row `n=85` this already covers every interior position `k >= 19`. Therefore the only still-uncovered inequalities are `k=2,...,18`, and those require source counts only through `ell_{85,19}`.

This gives a general stitch lemma.

### Low-LIS seam lemma

Assume that, independently of the row computation, Chen's source inequality is already proved for every source-valid fixed defect `1 <= j <= J`. To certify the entire row `n`, it is enough to compute exact values

`ell_{n,k}` for `1 <= k <= n-J`.

Indeed, every inequality with `k >= n-J` has defect `j=n-k <= J` and is already covered. Every remaining inequality has `2 <= k <= n-J-1`, and its three terms use only indices `k-1,k,k+1 <= n-J`.

For the current state `(n,J)=(85,66)`, the exact row-85 obligation therefore collapses to the finite low-LIS seam

`ell_{85,k}, 1 <= k <= 19`,

followed by the 17 explicit Turan checks at `k=2,...,18`. There is no mathematical reason to enumerate shapes with first row greater than 19.

## Exact finite route

By RSK,

`ell_{85,k} = sum_{lambda |- 85, lambda_1=k} (f^lambda)^2`.

So enumerate only partitions of 85 with largest part at most 19, compute each irreducible dimension exactly by the hook-length formula, and accumulate the squared dimensions by first-row length. Independently count partitions of 85 with largest part at most 19 using the standard coin-change partition DP. Equality of the recursion enumeration count with the independent DP guards against omission of a partition shape; all Turan comparisons themselves use arbitrary-precision integers.

A quick complexity calculation gives 17,240,952 relevant partitions, versus 30,167,357 partitions in the complete row. This is still substantial finite work but removes about 43% of the shapes and, more importantly, uses the theorem already proved instead of re-certifying its region by brute force.

## Section-B moves actually being tried

All 30 numbered methods have already genuinely appeared on P0282, so these labels are explicitly **RECYCLED**, not represented as unused.

- **#4 PROVE SOMETHING WEAKER, COMPLETELY (RECYCLED):** prove/certify exactly the missing low-LIS seam, not a redundant full row.
- **#19 MAKE IT AN ALGORITHM (RECYCLED):** turn the seam lemma into a pruned exact enumerator whose cutoff `K=n-J` is derived from the retained theorem.
- **#25 COUNT THE SAME THING TWICE (RECYCLED):** compare recursive enumeration of the admissible partition shapes against an independent bounded-part partition DP before trusting the finite certificate.

If the exact 17 source margins are positive, chaining this seam certificate to archived `N_exact=84` and the complete-defect theorem through 66 legitimately moves the frozen metric to `N_exact=85`; it is not a change of metric. If any margin is nonpositive, the exact witness is a source counterexample and must be reported as such.