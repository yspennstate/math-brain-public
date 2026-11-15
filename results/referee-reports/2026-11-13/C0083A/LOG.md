# C0083 work log

Task received: 2026-11-13, approximately 06:23 Asia/Tbilisi (UTC+04).
Request: investigate Open Problem C0083, literature first, then proofs and CPU checks.

## 2026-11-13 06:25 +04 — orientation and source identification

- Read startup memory, ran the brain recall for Hamming critical-point expansions,
  read the mesh protocol and inspected live mesh claims read-only. No overlapping
  directory claim was found. The specific instruction to work only in this directory
  excludes writes to the global brain, mesh, and task checklist; this log is the
  task-local record. No subagents, publications, pushes, or background services.
- Governor: owner_away_open, status warn (CPU saturation). Computation will use
  one worker at nice 10, with numerical libraries restricted to one thread.
- arXiv:1510.03221 is an unrelated CR geometry paper. arXiv:1512.00807 is an
  unrelated string theory paper. Locate intended sources by title and author.
- arXiv:1701.02099 is correct. Its abstract gives the second-order expansion
  with error O(m^-3)+O(m^-1 V^-1/3), m=d(n-1), V=n^d.
- No PDF, page image, or scan has been saved. Only textual source material will
  be retained.

Status: working; no conclusion yet.

## 2026-11-13 06:29 +04 — primary-source findings

- Obtained and read the TeX of arXiv:1701.02099, retaining only .tex/.bbl.
  Theorem 1.1 is the second-order Hamming expansion. Its Section 1.4 explicitly
  leaves higher coefficients conjectural and does not claim their rationality.
- Read the author's lecture-notes text through the web text extractor, without
  downloading a local PDF or requesting any screenshot. Open Problem 15.10,
  equation (15.5.7), has upper summation index d/3. The surrounding prose says
  two terms settle d=4,5,6, three become necessary at d=7. Consequently the
  intended summation range is integer i<1+d/3, equivalently i<=ceil(d/3).
  Literal floor(d/3) would be false at d=4,5. Do not sell this typographical
  issue as resolving the intended problem.
- The notes give (2d^2-1)/(2(d-1)^2) next to n^-2; the research paper attaches
  that number to m^-2. Conversion is necessary and will be derived independently.
- Correct hypercube sources: arXiv:math/0401073 (all orders, 2005) and
  math/0401072 (first three terms, 2006). Text sources retained.
- The proposed companion scaling-limit paper is listed as 'In preparation'
  (2016) in the expansion paper; no arXiv ID or published theorem located yet.
- Resource audit: commands inherit nice 15. The attempted extra `nice -n 10`
  reported an OS priority error; the inherited nice 15 already exceeds the
  requested politeness floor. Subsequent commands do not try to reset priority.
- Source-reader audit: raw arXiv TeX contains a plus sign in the displayed
  finite-susceptibility critical-point identity. Direct algebra from the lace
  identity gives a minus sign. The report will use the algebraically correct
  identity, without depending on that display.

## 2026-11-13 06:36 +04 — proof and computation setup

- Completed the literature-first stage; recorded references and theorem numbers
  in data/literature/findings.md. No full fixed-d solution located.
- Independent algebra gives a2(d)=(2d^3-2d^2+2d-1)/(2d^2(d-1)^2), in powers of n^-1.
  Values d=4,5,6: 103/288, 209/800, 371/1800.
- Proved the cycle-count obstruction and derived a two-term expansion for the
  expected weighted count of open simple cycles lying in a coordinate line.
  This count is not the lace coefficient; cycle overlaps prevent identifying a3
  from it alone. Details will appear in REPORT.md.
- Added a single-thread C++ root-cluster sampler, exact edge-configuration
  enumeration, and a sequential Python driver. Sampler storage is capped at
  V<=2^24 and exact enumeration at 22 edges; all selected jobs are far smaller.
- Latest governor state was throttle, so numerical work uses just one CPU worker,
  inherited nice 15; library threads are capped at one. No concurrent simulations.
- Audit of later citation: Eslava–Penington–Skerman's source prose refers to
  'first three terms' for Hamming graphs, citing the same 2020 paper. Its cited
  Theorem 1.1 contains only two nonzero coefficients. This wording is not evidence
  for a proved third coefficient. Their own Theorem 1.1 concerns an auxiliary process.

## 2026-11-13 06:42 +04 — first numerical results

- Exact enumeration completed for (n,d)=(3,1),(2,2),(2,3),(3,2), up to
  262144 configurations. Configuration counts match binomial coefficients.
  For every edge count, the root-cluster sum agrees with the independent
  sum-of-component-squares estimator by transitivity. Triangle susceptibility
  also agrees with its hand-derived polynomial.
- Sampler validation used 200000 independent root explorations at each of
  p=0.1,0.2,0.3 on each exact graph. All 12 discrepancies were within 1.60
  estimated standard errors. No sample truncation.
- Monte Carlo d=3 and d=4 completed; d=5 in progress. Both lambda=1 and
  lambda=0.5 are used. Roots use 13 pilot bisection stages followed by seven
  fixed p values with 20000 fresh samples each, interpolating inverse chi.
  Data retain each mean, standard error, maximum observed cluster, and
  interpolation diagnostics. All jobs sequential, one worker, nice 15.
- Descriptive fits retain known a1,a2 and allow a lambda-dependent window
  correction. Omitting the smallest n changes fitted next-order terms, so
  these fits are not evidence for a proved or accurately measured a3.

## 2026-11-13 06:48 +04 — completed and audited

- REPORT.md first line is PARTIAL. The intended statement is settled by
  published results for d<=6; no higher fixed-d expansion or general rationality
  theorem was found. The literal floor(d/3) reading has a counterexample at
  d=4,5, but does not dispose of the intended problem.
- Added complete proofs of the local cycle expectation expansion, the failure
  of a fixed length cutoff, the lambda-separation lower bound, and the
  conditional reduction of a3 to an unresolved next-order lace coefficient.
  No value of a3 or proof of the general expansion is claimed.
- Completed 38 roots over d=3,4,5,6 and lambda=1,0.5: 5320000 final-grid and
  1976000 pilot root explorations. Raw curves, root diagnostics, fitted
  corrections, exact polynomials, and run resources are saved in data/.
- Exact enumeration / sampler checks passed. Recomputed coefficient
  conversions symbolically and checked the local cycle expansion by direct
  finite-n summation. All observed lambda differences also have the sign and
  magnitude required by the rigorous lower bound.
- Final audit checked code syntax, all exact counts and transitivity sums,
  38 data records, normalization, sampler errors, parameter ordering, resource
  metadata, report status, and prohibited artifact formats. Results and code
  hashes are in data/audit.json. No PDF, image, scan, publication, or push.
- All simulations used one worker, nice 15, with one library thread; largest
  graph 331776 vertices. No numerical process remains running.

Task completed as a partial research result: “Open problem C0083”, received
2026-11-13 approximately 06:23 Asia/Tbilisi (UTC+04).
