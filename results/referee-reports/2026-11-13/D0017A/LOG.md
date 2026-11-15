# D0017 work log

Task received: 2026-11-13 09:25 +04 (Asia/Tbilisi), “Open problem D0017.”

## 2026-11-13 — orientation and source identification

- Workspace is dedicated to D0017A. All deliverables and downloaded source texts stay here. No PDFs or page images are written to disk; PDF responses will be piped directly to pdftotext.
- Read startup memory and compute state. Host status warn/cpu_saturated, mode owner_away_open. Use one process/thread for numerical work, nice 10, far below 4 GB.
- Consulted brain recall. It surfaced an earlier private D0018 argument for finiteness in dimension 5; this is a hint requiring independent verification, not a published result. No subagents.
- The task-specific “work only in this directory” restriction supersedes writes to global mesh/checklist/memory stores. Coordination and durable findings are recorded locally instead. No global state intentionally changed.
- Source identified: D. Khoshnevisan, Slices of Brownian Sheet: New Results, and Open Problems, arXiv:math/0510518 (24 October 2005); later published in Progress in Probability 59 (2008), pp. 135–174.
- Open Problem 2 is indeed in Section 8.2, PDF page 33. Its displayed definition includes the diagonal and the question includes s=0. Both must be reported explicitly; the intended mathematical question requires off-diagonal times and s>0.
- Source Theorem 1.4 / equation (1.12) gives dim_H D_d = min(1,(3-d/2)_+), citing Mountford for the earlier dimension computation.

Next: acquire plain text sources, read all of Section 8 and the cited results, then complete the later-literature search before proof work.

## Literature search completed before proof work

- Retained source preprint and final author version as text, each with explicit PDF-page separators. Read all Section 8 (pp. 33–35), introduction pp. 2–4, Section 5 pp. 20–21, and Appendix A.3 p. 36. Definition (8.2) does not exclude the diagonal; the all-s statement really prints s>=0. Appendix A.3 defines dimension by an infimum over positive exponents, giving dimension(empty)=0.
- Read Dalang–Khoshnevisan–Nualart–Wu–Xiao (2012), Theorem 1.1, Corollary 1.3, and discussion of same-coordinate pairs. The d=8 critical result for a two-parameter sheet does not answer the slice-fiber question at d=4,5.
- Read Khoshnevisan–Wu–Xiao (2006), Lemma 1.1, Lemma 3.1, Theorem 1.3, and Section 4/Theorem 4.1. Uniform image dimensions and full-sheet multiple-point dimensions do not themselves settle the question.
- Read Dalang–Mueller (2015), Theorems 1.1–1.3. The critical condition (k-1)d=2kN is for multiple occurrences of ONE common spatial value, and does not apply to many distinct double pairs on the same slice.
- Found and read the directly relevant part of Keming Chen's April 2026 EPFL thesis 11211: introduction p. 7 (PDF p. 19), Chapter 4.4, pp. 106–109 (PDF pp. 118–121). Theorem 1.3.3 states uniform finiteness for d=5; Theorem 1.3.4 states existence of infinite fibers for d=4. Neither proves the dimension-zero claim for d=4. Infinite and zero-dimensional are compatible. The thesis repeats diagonal/boundary omissions, so its intended meaning must likewise be understood. No reliance on its proof is needed below.
- Also searched Chen–Xiao (2012), Khoshnevisan–Xiao (Images of the Brownian Sheet), Khoshnevisan–Shi hitting probabilities, Lee–Xiao (2025) thermal-capacity paper, Rosen (1984), Kahane, Mountford (1990), and broad/exact-title queries for exceptional slices and double points of slices. The supplied putative Dalang–Mueller title about random walks, Wiener sheets and a lattice was not located; their actual critical-multiple-points paper was located and read instead.
- Mountford's primary full text is blocked by a publisher challenge; its dimension result is independently located in the survey, equation (1.12), p. 4. Rosen's author-hosted PDF was fetched only in memory, but has no pdftotext text layer. No scans/images/PDFs retained, and its original theorem numbering was not verified.
- OpenAlex citation index for the published source returned three citing works (2013 limsup fractals; 2013 packing dimensions; 2025 Chen–Woessner zero-set projections). Snapshot in sources/citation_search.txt. Broad searches additionally found the 2026 thesis. This is not a claim that the index or the literature search is exhaustive.
- Search result: no verified reference settling the intended statement in BOTH d=4 and d=5. The d=5 finiteness statement is already in a publicly deposited thesis. Proceeding to an independent proof of dimension zero for both dimensions, with novelty unclaimed.

## Candidate proof and audit plan

Use Brownian bridges in two disjoint time intervals to get a conditional-variance lower bound even when pairs reuse endpoints. At critical dimension 4, the lattice kernel sum grows logarithmically. Arbitrarily high moments absorb the one-dimensional union over s. Then a uniform Holder modulus passes from grid slices to every positive slice. Prove d=4 directly and deduce d=5 by projection to the first four coordinates. Check the covariance lower bound by a separate Schur-complement computation, then run modest, single-thread simulations as evidence only.

Priority setup: inherited nice value is already 10. Attempts to set priority (including to its current value) were denied by the sandbox; scripts now change priority only if the inherited value is below 10. No heavy computation ran at a higher priority.

## Proof completed and saved

- REPORT.md now begins PROVED for the intended off-diagonal, positive-s statement, with the literal-source counterexamples separately stated.
- Full proof: Brownian bridges give conditional variance >=a/2 times the sum of distances to previous endpoint sets. Conditional small-ball probabilities at d=4 lead to a two-dimensional harmonic lattice sum. Fixed arbitrary moments yield a summable union bound over all s-grid positions. The Holder estimate transfers to all s; a countable exhaustion gives one null set.
- Repeated coordinates and identical pairs are included, with capped small-ball bounds at zero conditional variance. The random Holder constant is handled through countably many deterministic bounds M, not a conditional Gaussian estimate given the modulus event.
- Independent Schur-complement audit: 960 configurations, with repeated endpoints, no lower-bound violation beyond rounding (~1.34e-14). Numerical lattice-sum normalization remained bounded across tested grids. Saved data/proof_audit.json.
- Started code/simulate.py with n=2048, four fixed seeds, one numerical thread, nice 10, streaming rows and small memory footprint. Domains: s in [1,2], u in [0.25,1.25], v in [1.5,2.5]. This excludes diagonal contamination. Tests near coincidences only; outputs are not evidence of exact hits at deterministic grid slices.

## Final computation and audit

- All four n=2048 simulations completed in 73.1 seconds, peak RSS 579.8 MiB, nice 10, one numerical thread. Saved all 216 multiscale count rows, per-seed minima, individual fits and aggregates.
- Simulation finding: no stable dimension estimate. With coefficient 1 at the finest mesh, near-pairs appeared in two of four d=4 runs and one of four d=5 runs in the chosen separated compact time intervals. Across thresholds, fitted slopes vary and can be negative because shrinking cutoffs remove sampled candidates. REPORT.md reports these failures rather than treating them as confirmation. The theorem does not depend on simulation.
- Replaced the continuity-theorem citation in the proof by an explicit dyadic-edge/Borel–Cantelli/chaining argument. Rechecked the exponent in the union bound: 3*p*eta/4-1, positive for a fixed sufficiently large p. Rechecked the harmonic lattice sum directly, including the zero-distance grid terms.
- Checked original page anchors from the saved texts and saved data/citation_page_audit.json. Corrected the Images of the Brownian Sheet manuscript page references. Read the 2004 quasi-sure survey's OU identification and fixed-versus-simultaneous warning as additional context.
- Final artifact audit passed: four Python sources parse; JSON and count CSV files read; 216 count rows; four completed replicates; source files are UTF-8 text; no PDF/image extensions or PDF/image file signatures anywhere in this workspace. Recorded data/final_audit.json.
- Final result: proved the intended dimension-zero statement for every positive slice in d=4 and d=5. Literal printed diagonal-included/s=0 statement is false and is separately documented. Literature novelty remains unclaimed. No publication or push.

Task completed: “Open problem D0017” — asked 2026-11-13 09:25 +04 (Asia/Tbilisi).
