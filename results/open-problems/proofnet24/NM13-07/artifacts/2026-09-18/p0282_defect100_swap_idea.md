# P0282 idea before code — fixed-defect cone as a uniform-in-n certificate

Date: 2026-09-18 UTC
Track: `proofnet24/NM13-07`
Canonical claim: `P0282`
Frozen metric on entry: `N_exact = 77`

The preceding run proved Chen's fixed-size LIS log-concavity for every source-valid `n` at defects `1 <= j <= 20` by combining Kauers–Wang's long-LIS recurrence with the integer polynomials

`P_0(n)=1`, `P_1(n)=(n-1)^2`,

`P_{j+1}(n)=n^2(P_j(n-1)+jP_{j-1}(n-1))-(2n-j-1)P_j(n)`,

and the Turán polynomial

`D_j(n)=(j+1)P_j(n)^2-jP_{j-1}(n)P_{j+1}(n)`.

The new route is not to push another row first. It asks whether the shifted positive-coefficient cone

`D_j(m+2j+1)`

persists far beyond `j=20`, and then swaps the quantifiers: instead of proving a statement for one `n` at a time, certify **all source-valid n at once** for every defect in a much wider finite set. The infinite tail `n>=2j+1` is decided by coefficient positivity; the finite bridge `j+2<=n<=2j` can be checked from the exact residual-partition hook formula without enumerating all partitions of the ambient `n`.

The three genuinely new Section-B moves for this run are:

- **#7 TAKE THE LIMIT.** Inspect the top degree / shifted-coefficient structure of `D_j` as `n` grows, looking for a stable cone rather than isolated rows.
- **#10 DERANDOMIZE.** Replace the shape-level Plancherel sum by a deterministic exact polynomial certificate plus a residual-partition bridge checker.
- **#27 SWAP THE QUANTIFIERS.** Prove `for every n` simultaneously after fixing a whole defect range `1<=j<=J`, rather than `for one n, every k`.

A successful run should either locate the first defect where shifted coefficient positivity fails, or rigorously widen the complete fixed-defect strip beyond 20. Only after this idea is archived should code be written. The frozen metric `N_exact` is not redefined by this theorem; if it moves, that must come from an independent exact full-row certificate.