# D0051 work log

Task received: 2026-11-13, approximately 08:07 Asia/Tbilisi (launcher/file timestamps).

## 2026-11-13 08:11 +04

- Began literature-first investigation of Ding–Dubédat–Gwynne Problem 5.3.
- Read compute governor: status ok, owner_away_open. Computation will use nice 10, one numerical worker, BLAS threads capped at one, well under 4 GB.
- Read brain identity orientation and mesh protocol. The current task explicitly restricts all work/writes to this directory; shared mesh/checklist/memory writes outside it are therefore omitted. This log is the local task checklist. No helpers/subagents, publication, git pushes, or external writes.
- Search leads: Fan–Goswami roughness (2205.00676); Bhatia–Kavvadias zero-one laws (2608.22693). Need inspect primary texts rather than infer an answer from titles.
- Important scope check: Gwynne's boundary result distinguishes circle-average thick points from metric thick points.

Checklist: source conventions [working]; literature [working]; rigorous deductions [pending]; LFPP evidence [pending]; final report/audit [pending].

## 2026-11-13 08:15 +04

- Saved 19 primary-paper extractions in sources/; all PDFs processed in RAM only. Read Section 5 and Problem 5.3, PDF pp. 23–24, exactly.
- Literature findings and exact locations saved in sources/LITERATURE.md. No complete answer found. Bhatia–Kavvadias 2608.22693, Section 1.3, p. 4, explicitly leaves typical thickness unanswered.
- Important corrections: source uses limsup; Pfeffer 2104.04020 Theorem 1.16 uses exact limits; Lemma 2.25 bounds liminf in geodesic interiors. Gwynne boundary Theorem 1.2 is for metric thick points, not automatically the source's set. Source's lower-bound discussion is outdated after Fan–Goswami Theorem 1.1.
- The shell already inherits nice 10. An initial redundant `nice -n 10` emitted a sandbox setpriority denial; direct getpriority confirmed nice=10. Subsequent numerical processes inherit it directly.
- Next: write dyadic-square upper-bound proof, explicitly for limsup sets; then run reproducible DGFF/LFPP evidence.

Checklist: source conventions [done]; literature [done, search limitations recorded]; rigorous deductions [working]; LFPP evidence [pending]; final report/audit [pending].

## 2026-11-13 08:20–08:27 +04

- Saved the complete upper-bound argument in REPORT.md before the numerical experiment. It combines Gaussian band-square first moments with a uniform annular distance lower bound and a path-length budget. A separate crossing-network argument proves the metric upper bound for the source's limsup sets. The maximiser is explicitly a maximiser of a bound, not a solution of the open problem.
- Checked signs and quantifiers against Pfeffer Lemma 3.7 and Theorem 1.16, GP Corollary 1.10, Gwynne Theorem 1.2, GPS Remark 1.12 and Section 6.1. Kept limsup, exact limit, signed liminf, and metric thickness separate. Checked source page numbers again; corrected the confluence theorem to p. 7 and the survey's geodesic section to Section 3.3.
- Ran `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/lfpp_experiment.py > data/run.log 2>&1` (the data directory had been created by the initial run). Final run: 144 paths, N=128/256/512, 12 independent fields per N, xi=0/0.2/1/sqrt(6)/0.8; 11.27 seconds; inherited nice 10; one numerical worker; peak RSS 498,499,584 bytes. The governor was warn/cpu_saturated but owner_away_open, not distress; no extra workers were used.
- Initial run had platform matrix-product floating-point status warnings, although outputs were finite. Replaced the relevant products by explicit elementwise reductions and non-BLAS einsum; reran the full experiment with the same seeds. Final data/run.log has no such warnings.
- Ran `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/analyze.py > data/analysis.log 2>&1`. Analysis peak RSS 496,713,728 bytes. Generated original SVG/PNG figures; visually inspected the bound plot, histograms, and example paths. Figure caches are local to data/.
- Validation: exact zero-field distances and xi=0 straight path; independent heap Dijkstra; every path simple/nearest-neighbour with reconstructed cost equal to the computed distance; 10,000-draw covariance comparison to 2*pi*inverse(L), relative Frobenius error 0.04388; circle averages of a constant; all statistics finite; histogram mass error <=1.5e-14. Re-derived the bound numerically on 200,001 alpha values and algebraically as (4+sqrt(15))/6 at the Brownian-map parameter.
- Saved raw fields/paths, per-replicate statistics, histograms, aggregate tables, paired controls, metadata, numerical audit, and SHA256 field manifest in data/. The stored fields use float32; the simulation and deterministic seed reconstruction use float64.
- Converted 19 paper PDFs in RAM only. Removed 99 extraction NUL control characters from the existing plain-text files; retained original PDF hashes and added data/source_manifest.json with plaintext hashes and page counts. No PDFs, paper page images, or scans were saved.
- Follow-up searches through late 2026 found no exact spectrum or unique-maximiser theorem. Latest directly relevant paper remains Bhatia–Kavvadias 2608.22693; its zero-one laws do not compute the spectrum.

Checklist: source conventions [done]; literature [done]; rigorous upper bounds [done]; LFPP evidence [done]; final report/audit [done]. Open problem itself remains unresolved. Final status: PARTIAL.

Task: “Open problem D0051” — received 13 November 2026, approximately 08:07 Asia/Tbilisi. Work remained local; no subagents, publication, or pushes.
