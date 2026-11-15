# C0113 work log

Task received: 2026-11-13, approximately 10:27 +04 (Asia/Tbilisi).
Request: Open problem C0113: Poisson Euclidean minimal spanning forest connectivity.

## 2026-11-13 10:29 +04 — orientation and literature first

Read the available startup memory index and compute governor. Governor: warn / owner_away_open, CPU saturated; use one computational worker, nice 10, numerical libraries restricted to one thread. No subagents. All work and output confined to this directory; do not run global brain/mesh/checklist commands that mutate outside it. No pushes or publication. Initial directory contained only launcher/prompt/session logs.

Plan: acquire public sources as extracted plain text (PDF responses only in memory); distinguish FMSF/WMSF and connectivity/ends; search named authors and recent work; write a complete conditional result or reduction; then bounded Poisson experiments with free and periodic boundaries and an explicit warning that a complete finite MST is always connected.

Early literature signals: Aldous–Steele public preprint at stat.berkeley.edu/~aldous/Papers/me101.pdf; Alexander at stat.berkeley.edu/~aldous/206-SNET/Papers/alexander.pdf; Lyons–Peres–Schramm arXiv math/0412263. Hirsch–Neuhäuser–Schmidt (2013) explicitly calls Poisson connectivity open for d>2.

## 2026-11-13 10:32 +04 — exact source and main pitfalls

Saved Aldous–Steele, Alexander, Lyons–Peres–Schramm, Newman–Stein, Jackson–Read I/II, Heydenreich–van der Hofstad–Last–Matzke, and Chatterjee–Sen as extracted text. PDF bytes existed only in Python memory. The initial `nice -n 10` wrapper warned because inherited nice is already 10; Python confirmed getpriority=10. Future processes inherit nice 10 without attempting to reduce it.

Aldous–Steele Definition 4.2, preprint p.33, uses distinct strict sublevel components and excludes the case where both are infinite: wired definition. Section 6.3, preprint pp.63–64, only conjectures nonconnectivity in sufficiently high d, without a numerical cutoff. Alexander Theorem 2.6 / Example 2.8, pp.93–94, uses planar dual vacant critical nonpercolation. Theorem 2.5(ii), pp.92–93, is about ends, not connectivity. Newman–Stein's unnumbered square-summability theorem is preprint pp.9–11; its function is invasion membership, not critical percolation two-point connectivity. Jackson–Read I explicitly replaces the old d=8 prediction by a d=6 mean-field prediction; this is not a rigorous Euclidean lattice/Poisson disconnection theorem.

Candidate rigorous output: deterministic free/wired and invasion equivalences; exact finite-box path-confinement reduction; and a conditional Poisson theorem using square-summability of the cells revealed by an explicit independent-cell exploration. This last assumption deliberately controls the exploration's information, not just its visited vertices, so the independence argument has a checkable basis.

## 2026-11-13 10:38 +04 — literature and proofs saved before computation

Saved REPORT.md with PARTIAL first line, exact source interpretation, literature gap, full proof of a conditional revealed-cell square-summability criterion, finite-cut/invasion equivalences for the complete Euclidean graph, direct Poisson Mecke proof of FMSF=WMSF, exact finite-box confinement reduction, and finite wired lower certificates. No unconditional d>=3 Poisson resolution found. Book Question 11.35 is printed p.406; journal LPS Question 6.8 and component-count Question 6.10 are p.1689. Public book is corrected 8 November 2020 version. HVHLM has 2026 publication but public preprint version v4, theorem locations p.5. Publisher article direct fetch returned access-challenge HTML, renamed *_access_failed.txt; it is not a source theorem.

Upcoming numerical design: nested Poisson boxes in d=3,4,5; complete-metric MSTs certified using connected radius graphs; free and periodic boundaries on the same samples. Record whole-tree connectivity (tautological), interior forest connectivity for distant pairs, fixed-root/fixed-inner-window brackets using the exterior-distance wire, and resource/check metadata. One worker, inherited nice 10, one numerical thread.

## 2026-11-13 10:54 +04 — numerical evidence and independent audit

Completed the initial 16,384-point pilot and a separate final 65,536-point run. Final: 48 independent nested Poisson realizations (16 each for d=3,4,5), four sizes, paired free/periodic boundaries, 384 finite MSTs and 24,576 far-pair observations. Wall time 137.77 seconds, one worker, nice 10, numerical thread variables one, peak RSS 1,112,948,736 bytes (~1.113 decimal GB). Raw data, seeds/hashes, root coordinates, summaries, runtime metadata and pilot are saved. No failed simulation assertions.

Verified sparse radius-graph Kruskal against independent full-metric Prim on small samples for both boundary metrics; checked all finite wired cut witnesses there. Every large finite graph has a complete-metric radius certificate. Independent stdlib audit rederived every pair fraction and Student-t interval, checked fixed roots, nested monotonicity, boundary inclusions and resource records: PASS. The far-pair observations within a realization are dependent; intervals use only 16 independent replicate fractions. Numerical trends are evidence about interior paths, not a proof of infinite disconnection.

At the final size the wired whole-box certificates connect the fixed pair in 6/16, 3/16 and 0/16 realizations for d=3,4,5. Missing certificates are inconclusive. The fixed-small-window events and the moving-separation measurements are explicitly distinguished from the iterated-limit connectivity criterion in REPORT.md.

## 2026-11-13 10:59 +04 — final proof and artifact audit

Rechecked the conditional proof's adaptive-query coupling at finite horizons, the finite-cut/invasion argument on the infinite-degree Euclidean complete graph, the random-distance Mecke step, and both finite-box monotonicity assertions. Added an explicit regular-tree example showing why critical nonpercolation is not a general wired-connectivity criterion; it is not a counterexample to C0113. Made the optional critical two-point transfer hypothesis fully explicit via an integral over unit cells. Checked LPS's September 2024 erratum. Exact source locations and the known/unproved-input table are in REPORT.md.

The resource audit caught that macOS rejected the attempted RLIMIT_DATA hard limit; the original script had caught that error silently. Corrected the code to expose the failure and corrected REPORT.md/run metadata. The actual measured peak remains 1.113 GB, so the requested memory bound was respected. Re-ran the independent data audit after this metadata/code correction: PASS. Numerical data were not rerun or changed by the diagnostic fix.

Final sources audit: all paper/book files are extracted text, response hashes and source URLs retained; no PDFs or paper/page images anywhere in this directory. Saved source inventory and search record. No subagents, pushes, external publication, global brain mutations or other work outside the authorized directory. Final status PARTIAL: full conditional theorem and reductions, checked finite evidence, original Poisson d>=3 question left unresolved.

DONE — “Open problem C0113”, received approximately 2026-11-13 10:27 +04: REPORT.md, LOG.md, code/, data/ and plain-text sources/ completed.
