# D0065 independent referee log

Task received 2026-11-13, 11:16 +04 (Asia/Tbilisi): “You are an independent referee… Break it if it is wrong.”

## 11:20 +04 — orientation and scope

Read the complete claim report and log, startup memory, and compute state (ok). No subagents. The explicit instruction to work only in this directory overrides external checklist/mesh/memory writes; this local log is the task record. Claim files remain unchanged. No publication, pushes, or background services. Numerical work and source extraction will run with nice 10 and one numerical-library thread, using PDF bytes only in memory and retaining plain text with page markers.

The claim is carefully qualified, so the main checks are the source's actual cutoff class, normalization of its conjecture, and whether general literature results have been understated. Initial search also found that the published review renumbers the conjecture as 6.3 and explicitly acknowledges Madaule; will compare versions rather than assume the preprint numbering is current.

## 11:23 +04 — independent calculations and source checks

Retrieved review, Madaule (arXiv and published), DRZ, BDZ, BL (both), Acosta, DRSV (both), JS, JSW, Powell and later papers directly from primary URLs. Extraction uses bytes in memory; no PDF files. The process inherits nice 10; attempts to increase niceness further are sandbox-denied, so code checks the inherited value rather than silently running at normal priority. One process, one numerical thread.

`independent_checks.py` independently recomputed all 8,192 data rows and eight summary groups, refitted the calibration constants, and recalculated both held-out CDF distances. Largest discrepancy 5.56e-16. Gamma integrals checked for d=1,2,3; maximum error 1.46e-13. Counterexample algebra checked in d=1,2,3,10. Fresh 256-tree runs in d=1,2 check the BRW normalization independently. Peak RSS about 81 MB.

Counterexample survives direct algebra. It also appears to satisfy the source's Definition 3.3 (smooth Gaussian approximations), a useful omitted source connection. It does not have independent scale increments or fixed-mollifier form, as the claim already says.

Found omitted Bertacco–Hairer, `Uniqueness of supercritical Gaussian multiplicative chaos`, arXiv:2504.07552v3 (accepted version; published EJP 30, DOI 10.1214/25-EJP1449). Theorem A gives general convolution supercritical-chaos convergence, but Remark 1.14 explicitly leaves extending Madaule's maximum result to convolution approximations for future work. Its companion arXiv:2504.06956v2 is star-scale extremal-cluster/supercritical work. These update the bibliography without establishing an unrestricted maximum theorem.

## 11:30 +04 — published source changes the framing

Retrieved the complete 78-page published Rhodes–Vargas review through the ICM EMIS journal mirror, after the main EMIS URL failed. Its Conjecture 6.3 (printed 369–370 / PDF 55–56) explicitly adds the star-scale invariant hypothesis, records Madaule's result, and already discusses the conformal-radius-squared DGFF weight. The preprint's Conjecture 6.5 transcription in the claim is accurate; the omitted publication changes are nevertheless relevant to the interpretation and value of the claimed partial resolution.

Also retrieved the exact author-final BL manuscript and published JSW, Acosta and Paquette–Zeitouni versions. The theorem/page references in the claim match those versions. Added Schweiger's 2020 four-dimensional membrane-model maximum theorem (arXiv:1903.02522v2, Theorem 1.1, PDF p. 2), a concrete non-star-scale example. Biskup survey Theorem 10.30, PDF p. 145, independently confirms the DGFF radius weight. The latest 2026 Xie preprint has a changed title and treats a cooling variance profile, not the fixed coefficient-one logarithmic class.

Provisional disposition: MINOR. No fatal theorem, normalization, algebra or simulation error found. Main changes needed: describe the published review accurately; connect the cutoff example to Definition 3.3; specify Acosta's square domain; update the literature discussion. The arbitrary-cutoff counterexample is a valid warning about an unqualified reading, not a disproof of the canonical Madaule cutoff theorem.

## 11:33 +04 — final audit complete

Wrote `REPORT.md`, first line exactly `MINOR`. It contains five located corrections/package gaps, the exact arXiv conjecture and published changes, a theorem-by-theorem audit of every substantive cited result, an independent line-by-line proof check of the counterexample, normalization checks, computations and the updated literature conclusion.

Final checks: all 30 retrieved-paper entries in `sources/manifest.txt` have existing text files with matching hashes. `sources/` contains 32 plain `.txt` files: 30 complete paper texts, the manifest, and a browser excerpt retained during mirror troubleshooting. No PDF, page image, scan, DjVu or PostScript file was created or retained. The original claim's SVG is its simulation plot, not a paper image. Source text extraction sometimes loses mathematical glyphs; load-bearing formulas were cross-checked against alternate extraction/browser text and the printed versions. All local source filenames cited in the report exist. No publication, git mutation, pushes, subagents or external task-store updates.

The final numerical audit is `data/independent_checks.json`; the standalone reproducer is `independent_checks.py`. The original run's runtime and historical memory use are not independently certified. Its mathematical computations and all CSV summaries were independently reproduced. The source-fetch process has completed, with no task process left running.

Task: “You are an independent referee… Break it if it is wrong.” Received 2026-11-13, 11:16 +04 (Asia/Tbilisi). Result: MINOR; main mathematics survives, with source-version, scope and literature corrections.
