# P0282 idea before archival production validation — extend the ULC strip, then move the row frontier

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`  
Entry frozen metric: `N_exact = 89`  
Retained complete Chen fixed-defect frontier: `j=n-k <= 66`  
Retained stronger binomial-normalized ULC frontier: `j<=20`

All 30 Section-B methods have already been genuinely used on P0282, so this invocation cannot truthfully supply three previously unused method numbers. The archival report will therefore label its chosen methods as recycled and will not repeat the immediately preceding triple `#2/#1/#5`.

## New route

The preceding run found that for fixed defect `j`, the binomial-normalized ULC margin

`M_j(n) = j(n-j-1) E_j(n)^2 - (j+1)(n-j) E_{j-1}(n)E_{j+1}(n)`,  `E_j(n)=ell_{n,n-j}`,

is an exact polynomial once the first row is long enough, and that after shifting `n=2j+2+m` every coefficient is positive for `j<=20`. Rather than blindly rescan rows or return to the already falsified real-rootedness route, localize one fixed-defect strip at a time.

1. **Recycled #30 — one scale/direction at a time.** Test the exact shifted coefficient cone for the next defects `21<=j<=26`. A single nonpositive coefficient is an immediate obstruction to this certificate route. If all coefficients are positive, the large-`n` regime is proved for those defects.
2. **Recycled #4 — prove something weaker, completely.** The all-defect source is much broader, but an all-`n` theorem for the stronger ULC inequality on `j<=26` is a complete restricted theorem. Close its finite boundary `j+2<=n<=2j+1` independently rather than infer it from the polynomial regime.
3. **Recycled #16 — compute every small case and stare at the sequence.** Use Gessel's Bessel/Toeplitz determinant with exact modular reconstruction for that finite boundary. This is independent of the residual-partition polynomial construction and can expose a sporadic boundary failure.

Only after this structural extension is decided, use the already validated low-LIS seam method to test row 90. Since the retained Chen theorem covers `j<=66`, row 90 needs only the low-LIS seam `k=2,...,23`; if exact positivity holds there, `N_exact` can move from 89 to 90 without recomputing the theorem-covered high-LIS sector.

## Falsification conditions

- Any nonpositive shifted coefficient for `M_j(2j+2+m)`, `21<=j<=26`, blocks the coefficientwise ULC route at that defect.
- Any failed exact boundary ULC cell blocks the claimed all-`n` ULC extension.
- Any failed row-90 Chen seam cell blocks frozen-metric movement.

No source closure, novelty, audit pass, or all-defect theorem is presumed.