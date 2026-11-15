# Independent referee log

Task received 2026-11-13 11:17 +04 (Asia/Tbilisi): “You are an independent referee ... Break it if it is wrong.” D0046, Virág Question 8.

## 11:18 +04 — orientation and scope

Read the submitted report and log, brain recall, mesh protocol, and compute state (ok, owner_away_open). No subagents. The task-specific instruction to work only in this directory prevents writing the global mesh, checklist, and memory stores; this log is the local task record. Submitted artifacts remain untouched. Source downloads will be converted in memory to plain text; no PDFs or page images are written. Numerical work will inherit/verify nice 10, use one numerical thread, and stay below 4 GB.

Initial proof audit finds the bounded-covariance extension is explicitly stated and proved as Corollary B, conditional on standard reversible diffusion calculus. Suspected minor error: standard Airy time is s, rather than 2s, for the report's rate-one OU and n^(1/6) edge normalization. Need direct source confirmation. The report correctly distinguishes its obstruction from a solution of the general operator-limit question. Recent primary source 2411.01633v3 (2026) is especially relevant and will be read independently.

## 11:22 +04 — proof and simulations

Re-derived all inequalities in Theorem A. Gaussian/radial OU construction and beta-two invariant law are correct. The forward/backward identity gives the stated constant 20; the entry map is Frobenius-Lipschitz; the delocalization argument yields the claimed n^(-1/4)(log n)^(1/4) bound. Corollary B genuinely follows, provided its full independent Dumitriu–Edelman invariant-law and covariance-operator assumptions are retained.

Independent exact-transition code is in code/independent_simulation.py. It uses one shifted normal square plus a central chi-square to evolve radial OU, rather than the submitted noncentral-chi-square implementation. No submitted code has been read or imported. Tridiagonal simulations through n=4096 (800 paths each, 16 time steps) show decreasing edge MSE. Dense Gaussian matrix OU comparisons are in progress. All processes inherit nice 10; one numerical thread requested and enforced by threadpoolctl. Peak RSS so far <300 MB for simulation.

Source extraction issue caught: pypdf treats some math-font glyphs as embedded control characters, including form feeds. This makes page counts inferred from extracted text wrong. The fetcher has been changed to pdftotext through stdin/stdout and all texts will be regenerated. No PDFs were stored. Source conclusions are being checked against actual page boundaries.

## 11:29 +04 — independent runs complete

Independent experiment completed in 439.5 seconds, peak RSS 759,414,784 bytes (724.2 MiB), nice 10. It used 4,800 tridiagonal paths (n=64,256,512,1024,2048,4096) and 804 dense matrix paths (n=64,256,512,1024,2048). The largest dense batch has only 16 paths and is reported with its large standard error. The grid maximum is only a sampled maximum, never a numerical proof of the continuum-supremum claim.

Independent small-time tests at n=20 give edge MSE/ds = 1.9363 ± 0.0352 for Hermitian OU (prediction 2), and 1.0290 ± 0.0192 for tridiagonal OU (prediction 1.0479). Finite differences match the Gaussian-coordinate eigenvalue gradient to 9.44e-11. The sampled Lanczos orbit identity is accurate to 1e-15. A platform BLAS floating-status warning appeared during a composed matrix multiplication despite finite correct output; explicit einsum independently reconstructed the identity and eliminated the warning on rerun.

All 14 primary sources were regenerated with Poppler. Their form-feed page counts agree with the PDF parser counts; no NUL bytes remain. EJN Problem 4 is on actual PDF p.18 and Remark 5.6 on pp.19–20. The report's correction of the latter's t^(-1) typo to t^(-2) is correct.

Scalar math.fsum recomputation checked all 72 submitted numerical summary rows: maximum MSE discrepancy 2.23e-16 and maximum correlation discrepancy 4.45e-16. All 44 independent summary rows also agree to floating-point precision. No submitted code was used. A plot was generated; Fontconfig reported unavailable global cache directories, while the plot and Matplotlib cache were written locally. A separate native thread-count audit of the same eigensolver kernels is running to check the requested limits, since threadpoolctl recognizes no pools on this Accelerate build.

## Final audit — completed 2026-11-13 +04

Wrote REPORT.md with verdict MINOR. The only mathematical correction is the extra factor two in the stated standard Airy time. Additional revisions clarify the eigenvalue marginal versus matrix law, the full covariance-operator/invariant-law hypotheses, and the measurable Markov quotient. The freezing proof, its qualified extension, and pointwise covariance lower bound survive. The independent quotient argument explicitly supplies the Borel kernel and handles the deterministic-time cyclicity issue.

The separate same-kernel resource audit observed a maximum of two native threads including its monitor, at nice 10, with 25 samples at a requested 5 ms interval. This is not retrospective monitoring of the earlier entire run. Main simulation peak RSS was 724.2 MiB.

Final verification passed: all 14 source hashes and actual page counts match the manifest; sources/ contains .txt files only, without NUL bytes; no PDF files, PDF signatures, scans or page images anywhere in the directory; all 32 claim artifacts retain their recorded hashes; independent plot SVG parses; local report links resolve; math display and inline delimiters balance; all independent Python files compile. The report explicitly distinguishes sampled path maxima from the proved continuous-time supremum. Source searches include primary 2026 papers, with no verified general resolution found and novelty of the precise bound left unestablished.

No publication, push, external message, or subagent was used.

Task: “You are an independent referee ... Break it if it is wrong.” D0046. Received 2026-11-13 11:17 +04 (Asia/Tbilisi).
