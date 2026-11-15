# E0082 work log

Started 2026-11-13 10:34 Asia/Tbilisi. Task: Open problem E0082.

Constraints: all artifacts in this directory; no subagents, publication, or pushes; computations nice 10, at most four threads and under 4 GB. Paper PDFs are read from memory and only extracted plain text is saved.

Orientation: read startup memory, compute state (ok, owner_away_open), mesh protocol, and the full internal E0081 memory. The latter is prior internal work only; its claims must be re-derived here. Global mesh/checklist/brain writes are outside both the sandbox and the task's explicit directory restriction; no private substitute mesh is being presented as shared coordination. Progress is recorded here instead.

Literature finding: arXiv 1411.0041v3, Pitman and Tang, Patterns in random walks and Brownian motion (2015 final revision). Theorem 1.8(4) gives n <= ET(FP) <= n^(5/4), not the n upper bound stated in the task. Open problem 2.3 is still printed in this version. Internal E0081 reports order n log n for the very same FP family.

Literature pass update: retrieved published chapter from the author's Columbia site using ?download=1; pdftotext now supplies readable text (some original font mappings remain imperfect). Published numbering: Theorem 6, pp. 56-57; Open Problem 1, p. 65. OpenAlex DOI record W1851725789 returns four citers, saved in data/. Semantic Scholar returned HTTP 429. Searches through 2026 found general formulas and Slepian boundary crossing formulas, but no printed exact solution to both parts. Several primary texts remain inaccessible; the literature claim will be bounded accordingly.

Acquisition correction: an unverified guessed arXiv identifier 1509.08808 fetched an unrelated physics paper. This was noticed immediately on checking its title; the mislabeled text is being replaced by the verified spans paper arXiv 1506.02021. No mathematical claim relied on the wrong paper.

Mathematical setup: first-hit probability vector pi satisfies M pi = ET/2^n times the all-one vector. Thus ET = 2^n/(1^T M^{-1}1), and weighted column sums give p_family ET = E_pi column_sum. The source's formula for standalone individual waiting times is not generally valid as printed; the family formula is valid. Exact computations check the correct first-hit system and an independent window-state Markov chain.

Proof plan: bridge column sums scale by sqrt(n), with a uniform small-shift bound C sqrt(delta). First-hit bridge laws converge by a lattice crossing/Donsker argument, and uniformly geometric tails prove convergence of means. Shepp determinant integrals provide an explicit constant. For first passage, record-time return potential G_m ~ (log m)/(2 pi); the internal E0081 range argument yields two-sided n log n bounds. A finite n-normalized FP constant is impossible.

2026-11-13T10:57:19.826548+04:00: Proof and computations completed. Bridge equivalent proved with explicit Shepp integral series; correctly weighted matching sums shown to converge. Internal E0081 record-range argument reconstructed to prove FP order n log n and divergence on the requested n scale. Sharp FP coefficient remains unproved; REPORT status is PARTIAL.

Exact finite-family calculations: 27 rows, 21 rational; all agree with independent Markov-chain solves (max difference 2.14e-14). Matrix-column identities checked on 2317 words, zero discrepancy. Single-thread Monte Carlo reaches n=65536. Continuous Shepp quadrature gives c_BR(0) about 1.543879 and c_BR(1) about 2.413513, with numerical uncertainty and analytic truncation bounds separated. The alpha=0 first-slab exact integral check is within 1.02 scramble standard errors. Three small Monte Carlo checks agree within 0.49 sampling standard errors.

Numerical implementation correction: Apple Accelerate emitted spurious matmul FPE warnings on finite vector contractions. Replaced validation vector products with explicit einsum; reran exact finite systems without warnings. No mathematical conclusions relied on unchecked values.

Resource and artifact checks: nice=10 confirmed, native numerical threads limited to one, one sequential C++ simulation, no subagents. No PDFs, paper images, scans, publication, or pushes. All task writes remain here. Global coordination/memory stores were not written because of directory/sandbox constraints.

Final mathematical audit: checked the lattice span-2 factors independently in the bridge local limit and record return potential. Checked the Shepp kernel's duration/sign by reconstructing its Brownian path-ordering proof. Verified that replacing the true first-hit bridge law by an ordinary uniform bridge would instead give pi/2 at alpha=0, confirming the need to keep the matching weights. Exact source-table lower bound at n=100 is 206.2948964 versus the printed 179.805.

DONE: Report, literature record, ten plain-text source files, reproducible code, data, and validation saved. Status PARTIAL: bridge leading constant proved as an explicit convergent integral series; FP order n log n re-derived; finite FP n-scale limit disproved; sharp FP leading coefficient not established.
