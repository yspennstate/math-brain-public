# P0282 idea before validation — long-LIS recurrence and two-count exact extension

Date: 2026-09-18 UTC
Track: `proofnet24/NM13-07`
Canonical claim: `P0282`
Frozen metric: `N_exact`, largest `N` with an archived exact-arithmetic certificate for every Chen inequality for every `n<=N`.

This note is intentionally written before new checker code. It records the route to test; it is not a certificate.

## Fresh Section-B routes for this invocation

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The observed weakest log-concavity ratios for `61<=n<=70` occur near `k≈0.61n`, hence inside the `k>=n/2` sector. Kauers--Wang (arXiv:2609.02220, 2026-09-02) prove in exactly that sector the bivariate recurrence

`(n+1)^2(a_{n,k}+a_{n,k+1})=(n-k+1)a_{n+1,k}+(n+k+1)a_{n+1,k+1}`,

where `a_{n,k}=ell_{n,k}`. This gives an independent exact arithmetic route for the empirically dangerous sector and can be checked against Robinson--Schensted hook sums.

### #25 COUNT THE SAME THING TWICE

For each newly certified row, compute `ell_{n,k}` once as

`sum_{lambda|-n, lambda_1=k} (f^lambda)^2`

using the hook-length formula, and independently check every admissible `k>=n/2` value against the Kauers--Wang recurrence from the previous row. Also check `sum_k ell_{n,k}=n!` and the partition count against an Euler-pentagonal recurrence. A mismatch kills the certificate; agreement gives three independent exact identities around the same integers.

The immediate finite goal is to extend the full source certificate beyond `N_exact=70`, not merely recheck 70.

### #28 REPLACE FOR ALL WITH FOR TYPICAL

Treat the minimum-ratio location as a diagnostic, not as a proof shortcut. Split every row into the long-LIS sector `k>=ceil(n/2)` and the complementary sector, and record the exact minimum ratio in each. If the global minimum continues to lie in the recurrence sector, that identifies the right place for future analytic curvature work while the full finite certificate still checks every `k`.

## Validation plan

1. Enumerate partitions and compute exact hook dimensions with arbitrary-precision integers for consecutive new rows.
2. Check Euler-pentagonal partition counts independently.
3. Check the Plancherel identity `sum_k ell_{n,k}=n!`.
4. Check all Chen margins `ell_{n,k}^2-ell_{n,k-1}ell_{n,k+1}>=0` exactly.
5. Check the Kauers--Wang recurrence exactly throughout its proved `k>=n/2` range wherever both consecutive rows are available.
6. Archive the checker and its complete output only if this moves `N_exact`.

No claim of all-`n` log-concavity, recurrence novelty, or publication novelty is made here.