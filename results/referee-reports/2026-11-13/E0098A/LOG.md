# E0098 work log

Task received: 2026-11-13, approximately 11:10 Asia/Tbilisi (07:10 UTC).
Request: “Open problem E0098” — minimum absolute coordinate of a Wigner eigenvector.

## 2026-11-13 — orientation and literature first

- Read the startup memory, recalled relevant prior work, and checked the compute governor: status ok, owner_away_open. No helpers or language-model workers started.
- The task explicitly confines work to this directory; global mesh/checklist/memory writes would leave it and are therefore not performed. This log serves as the local task record. No publishing, pushes, or git mutations are authorized.
- Found the original survey, arXiv:1601.03678, and its published version. The open question follows Corollary 4.8. The corollary is a lower-tail estimate, uniform in one eigenvector index, and is not a matching two-sided limit theorem.
- Located a potentially relevant June 2026 preprint, arXiv:2606.06419. It must be checked alongside the requested earlier work before deciding whether the problem is resolved.
- Sources will be fetched into memory and converted directly to plain text. No PDF files, scans, or paper screenshots will be written.

Next: save source texts; inspect exact theorem statements, quantifiers, and error estimates.

## Literature checkpoint

- Saved 14 requested/core papers as extracted text, including the survey and Benigni–Lopatto arXiv:2606.06419v2 (14 September 2026). PDF page boundaries are retained as form feeds; each file begins with URL, retrieval time, and SHA-256 of the in-memory PDF stream.
- Survey exact location: arXiv PDF p. 13, published journal p. 377. The real symmetric, centered, unit-off-diagonal-variance, subgaussian setting is the relevant one. Unit eigenvectors are normalized in Euclidean norm; scaling the matrix by n^{-1/2} does not change them.
- Bourgade–Yau Theorem 1.2 / Corollary 1.3 (PDF pp. 5–6) concern fixed-dimensional marginals. Benigni–Lopatto 2022 Theorem 1.2 (QUE CLT, PDF p. 2) concerns a sum of squared coordinates on sets up to n^{1-epsilon}, not joint entrywise normality of that many coordinates.
- Benigni–Lopatto 2026 Theorem 1.3 (PDF pp. 3–4) is a Poisson limit for the upper extreme, centered at 2 log n - log log n - log pi. Theorem 1.6 (pp. 4–5) allows n^{1/4-epsilon} coordinates of one eigenvector for smooth entries; Theorem 1.7 gives additive Kolmogorov errors. These do not directly resolve the lower extreme.
- Followed the 2026 references to Bao–Bucht–Schnelli arXiv:2606.17425 and Osman arXiv:2609.11630. Their upper-extreme results must be distinguished from the minimum. Bao–Bucht–Schnelli Theorem 1.9 compares arbitrary order statistics but with derivatives bounded at a coarse scale; the minimum requires a much finer scale.
- A further search found arXiv:2611.12858 on Rosenzweig–Porter minima. Checking the model and symmetry class before treating it as relevant.
- The launcher already starts Codex at nice 10. A redundant attempt to add nice 10 inside the sandbox was denied; it did not prevent source retrieval. Numerical work will inherit the launcher's priority and explicitly restrict BLAS to one thread.

## Literature decision and proof work

- No directly resolving printed theorem located in the searched material. This is a bounded literature audit, not a certification that no theorem exists anywhere.
- Fyodorov–Shcherbina–Shcherbina arXiv:2611.12858 is a complex GUE Rosenzweig–Porter model with 1 < gamma < 2, dominant diagonal disorder, and a fixed-energy eigenpair law. Its lower-extreme result does not resolve the real, fixed-index Wigner question.
- Main gap: for each fixed r one needs relative asymptotics of r simultaneous events of probability order n^{-r}, not merely ordinary fixed-dimensional weak convergence. Joint normality of order n coordinates is not necessary if these rare-event factorial moments can be controlled.
- Plan for complete partial results: prove GOE exponential/Poisson limit; prove a factorial-moment criterion; construct exchangeable unit vectors with an exact zero but Gaussian marginals in total variation for every o(n) coordinate subset; deduce negligible exact-zero probability from survey Theorem 4.7; verify finite-dimensional Bernoulli examples exactly.
- Pilot computation: 9 matrices (GOE, Rademacher, centered Bernoulli p=0.1, n=128 and 512), 27 eigenvectors. Maximum residual 2.05e-15, RSS 112.3 MB. NumPy/Accelerate emitted spurious arithmetic-status warnings for matmul even though all residuals were finite and tiny; changed residual verification to an independent einsum contraction and added finite/residual/memory assertions before the main run.

## 11:20 Asia/Tbilisi — exact arithmetic checkpoint

- Exhaustively checked Rademacher matrices with Rademacher diagonal for n=2,3,4, and with zero diagonal for n=2,3,4,5. Used exact characteristic-polynomial gcds, excluding repeated-spectrum cases from eigenvector-specific counts.
- Independently reproduced the matrix counts after diagonal sign conjugation fixing the first off-diagonal row to +1. This audit uses determinants and resultants instead of characteristic-polynomial gcds. All seven rows match exactly.
- A simple-spectrum 3-by-3 witness is [[1,1,1],[1,1,1],[1,1,-1]], with eigenvector (1,-1,0)/sqrt(2), eigenvalue 0, and other eigenvalues (1 +/- sqrt(17))/2.
- Corrected the initial clock conversion in this log after explicitly checking the host: local time is Asia/Tbilisi, UTC+4. The launch record gives 11:10 local, not 15:10.
- Main numerical run: 4,830 independent matrices, three chosen eigenvectors per matrix; sequential computation and one numerical thread requested. Samples are flushed after every matrix.

## 11:28 Asia/Tbilisi — main numerical run completed

- Completed all 4,830 matrices / 14,490 selected eigenvectors, n=128,512,1024,2048. Main run took 588.84 seconds; peak process RSS 418,922,496 bytes. Maximum residual 5.0412e-15; maximum norm error 6.662e-16; no nonfinite statistics or exactly zero floating-point minima.
- Independent eigensolver audit: narrow MRRR (`evr`) versus full divide-and-conquer (`evd`) on fresh matrices of each ensemble at n=128 and 512. Maximum discrepancy in the scaled minimum was 2.980e-11.
- Independently re-derived c=sqrt(2/pi) from the Gaussian CDF derivative (agreement within 2e-15) and evaluated exact spherical small-box density bounds for r=1,2,3,4 and n through 8192. See data/math_audit.json.
- Main-law comparisons: five of 36 pointwise KS tests reject the limiting exponential at 0.05; one remains below the Bonferroni threshold 0.05/36. That group is centered Bernoulli p=0.1 at n=128, upper edge (KS 0.07553, p=2.082e-5). This is a finite-size discrepancy, not a counterexample to an asymptotic claim. All n>=1024 groups have p>=0.1355, with much lower power at the largest n.
- Started an independent-seed validation run for centered Bernoulli at n=128 and 512 because of the observed discrepancy. This is an adaptive check and will be reported separately, without silently combining or treating it as a preregistered test.
- Figure generation initially found no writable global fontconfig cache. The SVG was still generated; local cache paths will be set explicitly for a clean reproduction.

## Final evidence checkpoint

- Independent validation completed: 3,000 additional Bernoulli matrices / 9,000 eigenvectors, seed 980014. At n=128 the lower/bulk/upper KS p-values were 0.00984, 0.03196, 0.09748; at n=512 they were 0.37050, 0.40116, 0.50880. The original upper-edge pointwise rejection did not replicate, and none passes the six-group Bonferroni threshold. The report preserves the initial discrepancy and treats this follow-up as adaptive.
- Wrote the full REPORT.md with status PARTIAL, exact source question, index/normalization scope, a literature table, complete GOE/Poisson and sufficient-condition proofs, a total-variation counterexample to the sublinear-marginal inference (including a no-zero version), and exact-zero bounds and examples.
- Saved numerical summaries, raw CSV data, metadata, exact-arithmetic audits, and our own SVG/PNG CDF figures. Viewed the generated plot to check axes, legend, and empirical curves.
- Added the Tao–Vu simple-spectrum paper to sources, checking Theorem 1.3 (p. 2) and Proposition 2.2 (p. 3). The report distinguishes its direct statement from the survey's stated nonvanishing theorem.
- Pinned the source manifest to all 20 arXiv versions actually read. Sources remain plain text only. No external writes, memory/checklist/mesh mutations, publication, or pushes were made; startup recall itself uses the brain's normal internal logging.
- Final artifact audit passed: REPORT.md begins exactly PARTIAL; all 30 report links resolve locally or identify the intended arXiv version; all 43 theorem/page anchors match the saved source text; sample keys, index choices, scaling, residuals, and counts agree. Theorem 1.6's PDF text-extraction heading required a numeral/body anchor because its word “Theorem” was displaced onto a separate line; the page reference itself was correct.
- Twenty paper texts plus SEARCH_LOG.txt are the only files in sources/. No PDFs, source page images, or scans are present. The PNG/SVG files in data/ are our simulation plots.
- DONE: E0098 delivered as PARTIAL. Proved the GOE exponential law with rate sqrt(2/pi) and its lower-extreme Poisson process; gave a precise rare-event criterion and a complete obstruction to inference from sublinear Gaussian marginals; checked exact zeros in theory and small cases; retained all main/validation numerical evidence. The Wigner universality/dependence question is unresolved by this work. Task clock: 13 November 2026, approximately 11:10 Asia/Tbilisi.
