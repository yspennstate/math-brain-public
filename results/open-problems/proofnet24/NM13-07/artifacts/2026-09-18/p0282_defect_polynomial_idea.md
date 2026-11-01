# P0282 idea before archival code — fixed-defect Plancherel polynomial route

Date: 2026-09-18 UTC
Track: `proofnet24/NM13-07`
Canonical claim: `P0282`
Frozen metric: `N_exact`, the largest N with an archived exact-arithmetic certificate verifying every Chen LIS log-concavity inequality for `1 <= n <= N`.

The previous run found no counterexample through n=60 and proved the top two interior inequalities uniformly. Its tightest finite ratio was at defect `j=n-k=23`, so another run devoted only to a larger finite cutoff would not respect the new-methods-first instruction.

This run will instead try three new Section-B moves that were reserved by the previous report:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY.** Extend the uniform boundary theorem to at least the next interior position `k=n-3` by deriving the exact defect-4 RSK count and proving the resulting polynomial margin positive on its full valid range, with the finitely many pre-stable values handled exactly.
- **#18 SAY IT IN ANOTHER LANGUAGE.** Replace partitions of n with first row `n-j` by a fixed residual partition `mu |- j`. For `n >= 2j`, every such shape is `(n-j,mu)`. Derive a fixed-defect hook formula and use the Plancherel identity `sum_{mu |- j}(f^mu)^2=j!` to read off `ell_{n,n-j} ~ n^(2j)/j!` directly.
- **#24 FIND THE EXTREMAL OBJECT.** Use that asymptotic language to determine the limiting fixed-defect log-concavity ratio. If it is `(j+1)/j`, then the dangerous boundary is not any fixed j but the regime `j -> infinity`; this would explain why the exact minimum through n=60 had already moved to defect 23 and would redirect future work toward growing-defect recurrences rather than ever deeper fixed-j algebra.

Only after this note is committed should any archival checker be written or executed. If the theorem route succeeds, extend the existing exact RSK certificate modestly beyond 60 so the frozen metric moves without turning the run back into a computation-only exercise. No finite cutoff will be called closure, and any fixed-defect asymptotic already present in the literature will be labeled as recovered/elementary rather than novel.

Process note: before persisting this note, private symbolic scratch was used to test whether the defect-4 algebra appears tractable. No repository checker or certificate was written or executed from that scratch. This is a minor ordering miss relative to the owner preference that the idea precede all code; the persisted idea does precede every archival program and certificate in this run.