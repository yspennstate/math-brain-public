# F0085 work log

Task: “Open problem F0085”, received 2026-11-13, work started 08:07 +04 (Asia/Tbilisi).

## 2026-11-13 08:09 +04 — orientation and literature first

Read startup memory and attempted the requested brain recall. Shared mesh digest failed with “attempt to write a readonly database”. This task's explicit directory-only restriction and filesystem permissions prevent shared checklist/mesh/memory writes; all task records are kept here. No agents, publication, pushes, or outside-directory artifacts. Shell work uses the existing nice-10 launch; numerical code will explicitly cap library threads and use one worker.

Initial primary-source reading: HHP arXiv:math/0505668v4 has 33 PDF pages; the open percolation question is on PDF p.31. FPV arXiv:math/0511186 states Theorem 1.1(i) small-appetite claimed nonpercolation, (ii) small-appetite vacant percolation, both d>=2; Theorem 1.2 gives limsup 2^d alpha_p(d)<=1. It explicitly leaves alpha_p(2)<1 open. Must inspect later literature before drawing a present-status conclusion.

Important correction to the proposed proof tool: the deterministic ball of volume alpha is contained in the claimed set; it does not contain each territory. Upper radius bounds are random, with dependence between centres.

## 08:13 +04 — source verification

Saved HHP original, FPV, HHP tail-bounds preprint, Poisson matching, and Stable Poisson Graphs in One Dimension as page-delimited extracted text. Downloads are decoded in RAM; no PDF is written. One guessed Gouéré arXiv identifier (0709.4417) was wrong, detected immediately by reading its title; that unrelated text is removed and replaced using verified identifier 0712.3638. Subsequent identifiers are verified before fetch. Extraction warnings concern rotated text, generally headers; theorem statements are inspected directly in text.

HHP noncritical bound is a Palm territory-radius exponential moment, with a constant depending on appetite, not a uniform critical estimate. HHP continuity gives replete boxes for intensity <=1 and decisive boxes for intensity >=1 (at fixed appetite 1); these statements cannot be swapped or converted to finite-range independence without another argument.

## 08:16 +04 — literature gate complete

The named paper families and subsequent small-appetite papers have been checked; source files and SEARCH_NOTES.txt preserve the search scope. No complete resolution located. Proceeding with the low-dimensional claimed-near-one and all-dimensional vacant-near-one questions. The all-four-resolved stop condition is not met. Exact theorem locations use saved-version PDF pages when journal pagination is unavailable.

Proof attack will use finite-window allocations as genuine local lower certificates for the claimed set. This yields an explicit finite-dependence comparison, but its success requires a block failure probability small relative to dependence range; density tending to one alone does not establish it. Numerical work starts only after this literature gate.

## 08:17 +04 — numerical implementation and proof deductions

Implemented actual centre-proposing Gale–Shapley with periodic Euclidean preferences and on-demand list expansion; no spatial cutoff. An independent all-pairs global-distance greedy solver agreed on 16 small instances, including exhausted-site/unsated-centre cases. Periodic component sizes and two winding flags agreed with independent lifted-grid BFS on 618 masks, including both 4 and 8 adjacency. A second geometric ball enumeration checks blocking pairs for every production allocation.

The shell's inherited nice level is exactly 10; attempts to add nice produced harmless permission warnings, so subsequent processes inherit nice 10 and Python catches unsuccessful adjustments. Numerical libraries are set to one thread and cKDTree workers=1. Initial L=32, resolution=8 pilot underway.

Proof deductions to write out: in a fixed subcritical model C equals the union of closed stopping balls, whose local finiteness follows from the Palm exponential-radius bound. At criticality infinite demand covers every compact by finitely many open stopping balls. Monotone finite-window and appetite approximations preserve such a cover eventually. This gives local near-one coverage, but no rate relating its failure probability to the required window size.

## 08:24 +04 — proofs saved and coarse runs

REPORT.md now contains the exact four-question literature table, page references, a correction and proof disproving the uniform-radius shortcut, a dependent radius envelope with an explicit Poisson Chernoff bound, local near-one coverage with the order of limits proved, and a fully quantified finite-window contour criterion. The probability hypothesis of that criterion is not established; the open parts have not been claimed solved.

Finished 192 runs at L=32 and 144 at L=64, both h=1/8; L=96 is running next, with one numerical process at a time. Finer-grid runs will follow. Peak RSS in the first completed batch was about 538 MiB, below the 4 GB cap. Every completed allocation has passed the blocking-pair and quota checks.

Caught 31 NUL/control characters from font extraction in the newly added 2024 dependence source. Removed those controls from the plain text and updated the extractor to sanitize them. No PDFs or paper images exist in sources/.

## 08:28 +04 — all three torus sizes completed

The coarse sweep now has 432 completed allocations: L=32 (16 Poisson seeds), L=64 (12 seeds), and L=96 (8 seeds), at 12 appetites each. All geometric stability checks passed. L=64 at h=1/16 is running at 13 appetites for 8 of the same seeds, giving paired resolution comparisons. Its audit streams one centre's ball at a time to reduce peak memory; the independent small-instance checks passed again after that change.

Checked the contour-series constant two ways: direct summation gives 8.222712792654635e-7, and a geometric majorant gives 8.22283494172202e-7, both below 1e-6. Checked the Chernoff threshold algebra on nine dimension/appetite choices; details in data/proof_constant_checks.json. These arithmetic checks support the stated criterion; they do not verify its missing block-probability hypothesis.

## 08:35 +04 — computation complete

All 536 sweep allocations are complete (plus three pilot runs). Independent geometric audits checked 780,192,050 candidate blocking pairs, finding zero violations above the 1e-10 tolerance. Maximum density-balance error was 1.11e-16. Claimed and vacant winding and largest-component sizes were monotone across appetites for every seed. Maximum recorded RSS was 1544.109375 MiB (about 1.62 decimal GB), under the cap. All numerical processes used one worker, one-thread library settings, and nice 10.

The fine-grid L=64 crossover estimates differ from the coarse grid: claimed winding reaches 50% near 0.665–0.676 for 8/4 adjacency, vacant winding falls to 50% near 0.688–0.699. These are finite-grid indicators from eight seeds; no continuum confidence interval is claimed. Data tables and original SVG figures are saved.

Renamed raw field max_radius to max_audit_radius: it is the geometric audit search radius, inflated to search the whole torus for unsated centres. This prevents confusing it with a territory radius. The raw values are unchanged.

An additional 2020 Boolean/vacant sharpness paper was saved. Its initial pypdf extraction collapsed some inequality glyphs; re-extracted from RAM with pdftotext, which preserves those glyphs. The printed vacant-theorem parameter inequalities still appear reversed relative to its decreasing connectivity function; no such inequalities are used in this investigation. Matplotlib's first font-cache attempt was denied outside this directory; final plots set both MPLCONFIGDIR and XDG_CACHE_HOME here.

## 08:39 +04 — final audit and task result

REPORT.md is complete with first line PARTIAL. It distinguishes FPV's two all-dimensional small-appetite conclusions and sufficiently-high-dimensional claimed result from the near-one questions not proved here. It contains the structural proofs, explicit conditional criterion, precise missing estimate, simulation tables, limitations, exact source-version theorem/page references, and reproduction instructions.

The independent numerical checks passed again after the final audit-code change. Python AST and shell syntax checks passed. The filesystem audit found 13 UTF-8 plain-text source files (including search notes), no forbidden PDF/PostScript/DjVu files, and all 536 expected sweep records without duplicates. The original plots were visually inspected. The manifest hashes all code, source text, numerical data, REPORT.md and this log, excluding generated caches and the manifest/audit files themselves. Resource and package details are recorded in data/artifact_audit.json. No numerical worker remains running; no subagents, pushes, publication, or outside-directory deliverables were used.

Task completed as an explicitly partial mathematical investigation: “Open problem F0085” — started 2026-11-13 08:07 +04 (Asia/Tbilisi).

Final hash verification caught an audit-output redirection hashing its own still-changing output file. Removed that transient output and reran the audit without redirection; no research result or source changed.
