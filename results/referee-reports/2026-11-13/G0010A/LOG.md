# G0010 work log

Task: “Open problem G0010” — received 2026-11-13, first local clock reading 08:49:07 +04 (Asia/Tbilisi).

## 2026-11-13 08:49 +04 — orientation and source identification

- Work is confined to this directory. No subagents, publications, pushes, or shared brain/mesh/checklist mutations. The task-specific directory-only order supersedes the global shared-store write routines. Read the memory index, mesh protocol and compute state without altering them.
- Compute governor snapshot: status warn, mode owner_away_open. Computation will use nice 10, one worker and one numerical library thread, with a memory limit below 4 GB.
- Identified Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1, submitted 19 August 2026, 22 PDF pages. Official abstract and HTML checked.
- Initial status: literature review in progress; no claim that the open question has been resolved.

## Source read and first mathematical checks

- Saved the 22-page source as `sources/CMW_2608.19145v1.txt`, using PDF bytes only in memory and piping to pdftotext. No PDF was saved.
- Read Theorem 1.4 (PDF pp. 4–5), all of its proof (Section 4.1, pp. 14–16), Lemmas 2.4, 2.5, 3.1 and the exploration argument (pp. 9–13), and Section 5 in full (pp. 19–20).
- Important distinction: the direct global path count proves Theorem 1.3(II); Theorem 1.4(II) uses a resolvent weight and an exponential weighted exploration tail. The factor sqrt(n Delta)/lambda is the maximum-to-minimum weight bound in Lemma 2.4.
- Elementary logarithmic regime: (1-epsilon)(1+delta)<1. Beyond that condition a calibrated clique plus a finite branching tree is a candidate polynomial counterexample, including a connected version. Verification in progress; not yet claimed.
- The shell already inherits priority 10. Running `nice -n 10` attempted to increase its numerical nice value again and was refused; verified with os.getpriority that the actual priority is 10. Subsequent processes inherit 10 directly.

## Literature pass completed, before writing results

- Saved and inspected the relevant theorem statements of the named literature; exact references, theorem numbers, PDF pages and non-applicability checks are in `sources/LITERATURE_REVIEW.txt`.
- Forward citations were checked through web search, Semantic Scholar and OpenAlex. Semantic Scholar returned one citing preprint: Anastos–Frieze–Krueger, *Perfect matchings in a random k-out subgraph of the hypercube*, dated 27 August 2026. Retrieved its original author text; CMW is background on p. 2 and reference [7] on p. 10. It does not answer Question 5.2. OpenAlex returned zero forward citations. Search incompleteness recorded.
- No located printed/preprint solution of the general Question 5.2; continue with partial theoretical results.
- Correction to prompt locator: Question 5.2 itself is on PDF p. 20 of v1, while its discussion starts on p. 19.

## Proofs saved before simulation

- Wrote REPORT.md with a complete connected near-regular polynomial counterexample for every fixed (1-epsilon)(1+delta)>1.
- Strengthened the construction by independent vertex replacement: lambda and Delta may both grow like n^a for any fixed a<1, while the polynomial obstruction persists. Proved all spectral, independence and probability estimates directly.
- Included the existing tight logarithmic worst-case regime for (1-epsilon)(1+delta)<1 with a proof and reference (DEKK Theorem 2), and a self-contained O_epsilon(log^3 n) upper bound at equality via an exponential moment for a multitype branching process.
- Included a refined walk-resolvent upper bound, using min(Delta^j, lambda^{j-1} sqrt(n Delta)), and stated the remaining exponent gap explicitly.
- REPORT.md status is COUNTEREXAMPLE for the requested near-regular alternative; the report explicitly says the full Question 5.2 remains open in this work.

## Simulation implementation and checks

- Implemented exact Bernoulli-edge sampling by geometric waiting times; complete bipartite, complete-core-plus-star and vertex-replacement hosts remain implicit, avoiding materializing dense host edges.
- Sparse planted-hub hosts use a seeded G(n,6/(n-1)) base plus four planted hubs; repeats condition on one host per n. Largest eigenvalues are computed numerically with recorded residuals; analytic spectra are used for the other families.
- Independent checks passed: 58 complete upper-triangle decoders, 30,000 sampler trials, 120 SciPy-components versus separate union-find comparisons, full-matrix versus quotient/Kronecker spectra (maximum difference below 4e-14), and 59 second-moment recurrence steps.
- Managed macOS rejects RLIMIT_AS, RLIMIT_DATA and RLIMIT_RSS changes with “current limit exceeds maximum limit.” No OS hard-limit claim is made. The simulation uses bounded sparse arrays and a 50 ms watchdog stopping at 3 GiB peak RSS, leaving margin below 4 GB; actual peak will be reported. One numerical thread plus the watchdog, one process, inherited nice 10.

## Computation completed and final audit

- Completed 1,200 percolation realizations on 30 hosts in seven families, 40 trials per host, maximum n=1,118,688. Actual simulation peak RSS: 1,008,943,104 bytes; nice 10; one numerical thread plus one RSS watchdog. No worker processes or subagents were spawned.
- Saved raw trials, per-host summaries, exact host seeds/hashes, spectral residuals, conditional-bootstrap fits and a standalone SVG plot in data/. The largest eigenpair residual for planted hosts was 8.90e-10.
- Finite power fits were explicitly separated from asymptotic claims. In particular the logarithmic balanced-bipartite control has an apparent power slope 0.269, illustrating why a fit alone cannot establish a polynomial theorem.
- Finished REPORT.md computational section and added the dense logarithmic regime and a calibrated clique/star construction with its family-specific matching bound and full proof.
- Re-derived the load-bearing proof steps and recorded the audit in data/proof_audit.txt. Verified independent small-graph samplers/components/spectra, the explicit counterexample constants by two routes, all 1,200 p*lambda values, and resource usage.
- Repaired inline mathematical delimiter formatting during document review. Final artifact audit: PASS; all 23 files in sources/ are plain UTF-8 text; no PDF, DjVu, TIFF, paper image or scan was retained. The SVG is an original simulation plot.
- Done: REPORT.md begins exactly COUNTEREXAMPLE. It proves the requested near-regular polynomial alternative in the strict regime, includes logarithmic and boundary upper bounds, and states the remaining general problem and nonmatching exponents. No publication or push was made.

Task: “Open problem G0010” — first local clock reading 2026-11-13 08:49:07 +04.
