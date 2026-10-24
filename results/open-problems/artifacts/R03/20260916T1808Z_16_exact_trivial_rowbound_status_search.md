# R03 dated source/status search — 2026-09-16

Run: `20260916T1808Z_16_exact_trivial_rowbound`.

## Outside target and current status

Queries/checks made on 2026-09-16:

1. `arXiv 2010.06554 Singularity of discrete random matrices Jain Sah Sawhney Rademacher uniform support`.
   - Primary arXiv record: Vishesh Jain, Ashwin Sah, Mehtaab Sawhney,
     *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 31 (2021).
   - The abstract distinguishes non-uniform finite-support laws, where the sharp
     elementary-mechanism asymptotic is proved, from laws uniform on their
     support.  The iid Rademacher law is in the uniform-support regime; the full
     theorem there is exponential-scale, with sharp structured/compressible
     analysis.

2. Van H. Vu, *Recent progress in combinatorial random matrix theory*,
   arXiv:2005.02797 (2020), Section 2, Conjecture 2.2.
   - Section 2 is the iid Rademacher model.
   - The symmetric Bernoulli ensemble is treated separately in Section 3.
   - This is the recovered source locator used by the R03 campaign.

3. `arXiv 2512.15077 probabilistic combinatorics exponentially small scales Rademacher singularity`.
   - Julian Sahasrabudhe, *Probabilistic combinatorics at exponentially small scales*, arXiv:2512.15077v1 (17 Dec 2025).
   - The survey records the exact iid sign asymptotic as the sharp open target
     and records Tikhomirov's theorem only at the `2^{-n+o(n)}` scale before
     switching to the symmetric ensemble.

4. `random Bernoulli matrix singularity sharp 2026 exact prefactor Rademacher`.
   - No independently verified 2026 paper resolving the exact iid prefactor was
     found in the bounded search.
   - Found 2026 papers on growing corank, dense combinatorial matrices and LU
     factorization; none has the source-matching exact iid prefactor.
   - Blinovsky arXiv:1511.05283 still claims a tight asymptotic; retained R03
     proof audits do not accept its displayed route as verified.
   - A bounded negative search is not a proof that no unindexed resolution exists.

## Exact finite enumeration / prior art searched

5. Thomas Voigt and Günter M. Ziegler, *Singular 0/1-matrices, and the hyperplanes spanned by random 0/1-vectors*, arXiv:math/0308050 / CPC 15 (2006).
   - Gives the cube-hyperplane recoding used in retained R03-C245.
   - The fat hyperplanes are the expected leading geometry.

6. Miodrag Živković, *Classification of small (0,1) matrices*, arXiv:math/0511636 / LAA 414 (2006).
   - Published classification of all binary square matrices through order 8.
   - This is sufficient for the strict exact R03 residual values through sign order `n=9`.
   - The paper computes determinant/Smith-form sets at order 9 but not a full order-9 orbit classification.

7. Current OEIS pages checked directly:
   - A094000: binary matrices with no zero rows/columns and all rows/columns distinct, modulo row permutations; explicit signed-Stirling formula.
   - A000409: row-good singular binary matrices with a zero/equal column; explicit formula.
   - A000410: singular binary matrices with nonzero distinct rows, modulo row permutations; current table through order 9.
   - A116527: singular binary matrices with no zero rows/columns and all rows and columns distinct, modulo row permutations. Current direct page has order-9 term `1448479166136642150`, added 16 Jul 2026, and the identity `A116527(n)=A000410(n)-A000409(n)`.
   - A046747: all real-singular labeled binary square matrices; order-9 term `902616230040448613437952`, credited to Dominik Beck, 2 Jul 2026.

8. Verification boundary for the new order-9 database term:
   - TheoremDB record R678 (reviewed July 2026) reports that the A046747 order-9 term is sourced database evidence and that its audit located no primary paper or independently replayable orbit certificate.
   - Therefore this run checks the arithmetic consequences of the current A116527/A046747 order-9 terms but does **not** promote the resulting sign `n=10` exact residual to the strict R03 metric.
   - The strict metric uses the published order<=8 classification through sign `n=9`, and an independently proved F3 upper envelope from sign `n=10` onward.

9. Enumeration prior art:
   - A094000 cites G. Kilibarda and V. Jovović, *Enumeration of some classes of T_0-hypergraphs*, arXiv:1411.4187.
   - Related OEIS families enumerate binary matrices with distinct/nonzero rows and columns. Accordingly, the signed-Stirling collision-free count in this run is recorded as a direct proof/translation, not claimed as a novel enumeration mechanism.

## Repository/access checks

- Read `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, and `operations/NEW_METHODS_2026-09-16.md`.
- Recovered newest R03 report `runs/R03/20260916T1708Z_15_f3_hyperplane_geometry.md`.
- Checked newest discoverable R04 package `runs/R04/20260916T161226Z_r04_riccati_siegel.md`; it was already audited claim-scoped by R03 in the preceding run and no newer package was found.
- Repository-wide intake searches remain response-truncated; the R03-relevant F0001/source family was recovered, but this run does not claim a semantic row-by-row reread of every intake row.
- No Gmail, Drive, email, public posting, paid service, permission change, workflow execution or scheduler mutation was used.
