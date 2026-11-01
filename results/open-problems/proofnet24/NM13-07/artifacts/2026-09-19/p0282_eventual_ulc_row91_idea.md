# P0282 idea before production validation — eventual ULC on every fixed-defect diagonal

Date: 2026-09-19 UTC
Track: `proofnet24/NM13-07`
Canonical claim: `P0282`
Entry frozen metric: `N_exact = 90`
Retained complete Chen fixed-defect frontier: `j=n-k <= 66`
Retained stronger all-n ULC frontier: `j <= 26`

The previous run found coefficientwise-positive shifted ULC-margin polynomials through fixed defect 26. Rather than merely extending that finite strip, this run asks what happens for an arbitrary fixed defect `j` as `n -> infinity`.

For a partition `mu |- j`, write `N=n-j`. The hook formula for the shape `(N,mu)` can be factored as

`f^(N,mu) = C(n,j) f^mu prod_{c=1}^{mu_1} (N-c+1)/(N-c+1+mu'_c)`.

Since `sum_c mu'_c=j`, this gives uniformly for each fixed `mu`

`f^(N,mu) = (f^mu/j!) n^j (1 - j(j+1)/(2n) + O_j(n^-2))`.

Summing squares over `mu |- j` and using the regular-representation identity `sum_mu (f^mu)^2 = j!` should therefore give

`E_j(n)=ell_{n,n-j} = n^(2j)/j! * (1 - j(j+1)/n + O_j(n^-2))`.

Insert this expansion into the binomial-normalized ULC margin

`M_j(n)=j(n-j-1)E_j(n)^2-(j+1)(n-j)E_{j-1}(n)E_{j+1}(n)`.

The apparent `n^(4j+1)` terms cancel exactly. The next coefficient should simplify to

`[n^(4j)] M_j(n) = j/(j!)^2 > 0`.

If correct, this proves a qualitative theorem for every fixed defect: for each `j>=1` there exists `N_j` such that the stronger ULC inequality, hence Chen, holds for every `n>=N_j` on the diagonal `k=n-j`. This is not an all-defect uniform bound, but it extends the structural theorem from finitely many defects to all fixed defects asymptotically.

Section-B routes actually pursued in this run are therefore:
- #7 TAKE THE LIMIT: fixed `j`, `n -> infinity`;
- #25 COUNT THE SAME THING TWICE: hook-formula asymptotics plus `sum (f^mu)^2=j!`;
- #3 PROVE SOMETHING STRONGER: prove eventual binomial-normalized ULC, not merely Chen.

All three labels are RECYCLED because this track has already genuinely used all thirty method numbers; the triple is different from the predecessor's #30/#4/#16.

Only after writing this route down should finite code be used: (i) a small exact self-check of the leading coefficients, and (ii) an exact Gessel low-LIS seam certificate for row 91 to move the frozen metric independently.