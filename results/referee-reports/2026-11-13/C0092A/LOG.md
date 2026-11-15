# C0092 work log

Task: “Open problem C0092”, received 2026-11-13 at 09:30 +04 (launch record; seconds unavailable).

## 09:33 +04 — orientation and scope
Read startup memory, recalled random-cluster correlation work as an unverified hint, and checked the compute governor (status ok). No subagents. All new files stay in this directory; no publication or pushes. Global mesh/checklist/brain writes are outside the explicit task scope and sandbox, so this log is the local task record. Shared mesh protocol read; no shared files are edited. Numerical jobs will use one thread at nice 10 and well below 4 GB.

Literature comes first. Found the authors’ March 17, 2017 book manuscript, Grimmett’s author-hosted book, DRT 2019, and two 2026 preprints concerning wired trees / negative correlation. Their relevance remains to be checked in full text. PDFs will be downloaded into memory and piped directly to pdftotext; only text will be saved.

## 09:39 +04 — literature and proof plan
Saved the complete author-hosted book manuscript and read Chapter 16, especially Section 16.4. Open Problem 16.10 explicitly says q > 0; manuscript p. 242 corresponds to the published p. 254 citation. Saved DRT (published text), Grimmett, both Hutchcroft papers, Duminil-Copin lectures, Lyons–Peres, Pemantle, Kahn, Dubédat, the forest papers, and 2025–2026 negative-correlation papers. No all-q<1/all-d sharpness theorem found. The recent tree result is Park, arXiv:2608.08565, and concerns wired DLR uniqueness and separated branches; the other new results are pairwise correlation estimates in restricted regimes. They do not settle C0092.

Derived exact triangle covariance and a two-coordinate decision-tree obstruction. Plan: prove Bernoulli sandwich and an O(1-q) interval bound; prove free regular-tree sharpness directly; give a fully specified conditional sharpness reduction with a bound on negative event-edge covariance. Ordinary edge negative correlation alone will not be asserted to imply sharpness. No claim of perturbative or large-d equality has been obtained.

Priority check: inherited nice value is 10. The sandbox rejects changing process priority even to a lower one, so child jobs inherit the launcher’s existing nice 10; no priority escalation is attempted.

## 09:42–09:44 +04 — exact checks and simulations
Completed exact enumeration on 2D tori L=2,3 and the 3D torus L=2 (parallel bonds retained at side 2). Integer histogram totals agree with 2^m and every fixed-edge-count slice with binomial(m,a). At q=1 all checked partition functions equal 1. An independent Python DFS/lift calculation reproduces the entire 2D L=2 histogram including winding observables. Heat-bath detailed balance error is below 8e-16. Nine exact rational triangle checks verify both the negative covariance formula and the OSSS deficit.

Monte Carlo uses exact single-edge conditional probabilities, not the usual q>=1 Chayes–Machta activation rule. Scans: q=.25,.5,.75; 2D L=8,12,16; 3D L=4,6,8; two independent empty/full starts, 400 burn-in sweeps, 1600 measurement sweeps, every fourth sweep retained. Raw samples and seeds saved. These short runs require explicit autocorrelation/start diagnostics; they are evidence only.

## 09:45–09:52 +04 — numerical audit and report
The original numerical scan finished in 155.69 s; its C++ child peak RSS was 3,604,480 bytes. Added 102 lower-p chains because some susceptibility proxies peaked at scan boundaries. Combined main scan: 294 parameter points, 235,200 retained samples.

One initial exact-vs-MC comparison, nonwrapping susceptibility on the 3D side-2 torus at q=.25,p=.6, was 12.64 nominal standard errors from the exact value. Inspection identified rare connected nonwrapping configurations that the short validation hardly sampled. Kept the initial summary and increased this parameter to one million measured sweeps per chain, stride 10. Final validation has 268,000 retained samples, 108 comparisons; maximum standardized discrepancy 2.775. FFT autocovariance avoids quadratic work in the long validation chains. No result is treated as a mixing certificate.

The finite-size proxies differ substantially, especially in 2D; no agreement of infinite-volume thresholds is inferred. Saved raw data, all seeds, block-bootstrap intervals, R-hat/ESS diagnostics and an SVG generated from our own data. REPORT.md contains complete proofs of the limited unconditional results and a conditional theorem with explicit unproved covariance hypotheses.

## 09:59–10:01 +04 — additional literature and mathematical audit
A final targeted search located Beffara–Faipeur–Oke, arXiv:2512.16486v1 (2025), the closest lattice result found. Saved its full text and read the introduction/main statements, specifications discussion, and open questions. Theorems 1.4 (p. 6), 1.10 and 1.11 (p. 11) strictly extend comparison/uniqueness regions, but §1.4 (p. 10) still leaves existence of a below-one critical point open. Updated REPORT.md and LITERATURE.md; the elementary interval estimate here is explicitly conservative.

Rechecked the conditional theorem without assuming infinite-volume differentiability: integrate the finite-torus inequalities first, then use bounded convergence and the analytic argument. Checked the separate roles of absolute-covariance revealment and the bound on negative covariance mass; neither is claimed to follow from ordinary negative association. Rechecked manuscript versus published theorem pages. A report patch failed because delete/add targeted the same file; the report was then written successfully in sequential sections.

## 2026-11-13 10:02:56 +0400 — completed
Final status PARTIAL. REPORT.md, LITERATURE.md, code/, data/, and 19 full plain-text source conversions are saved. Audit verifies all source text hashes, local document links, Python syntax, the exact PARTIAL first line, no saved PDFs, 294 parameter points, 588 main chains and 235,200 main samples. Final analysis peak RSS: 220,200,960 bytes. No subagents, publication, commits or pushes. General lattice sharpness and general p-monotonicity below one remain unproved here; the conditional hypotheses are explicitly identified.
