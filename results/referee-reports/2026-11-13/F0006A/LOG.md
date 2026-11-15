# F0006 research log

Started: 2026-11-13T05:56:07.796095+04:00

Task: literature audit of Vu Conjecture 6.8, then support constructions and determinant atom computations if unresolved. Original task file created 2026-11-13 05:55:20 +04:00.

Scope: all task writes remain in this directory; no subagents, publication, pushes, or global brain/mesh/checklist registration. The later task-specific directory restriction supersedes global state registration. Startup memory and compute state were consulted. Compute governor reported throttle; use one worker at nice >=10. The inherited process priority was subsequently verified as nice 15.

Literature lead: The range of 0-1 determinants is large appears to prove |sigma(n)| > exp(0.5 n log n - 7 n log log n). Primary verification pending. nice launcher reported setpriority not permitted; inspecting inherited priority before compute.

2026-11-13T05:58:32.352096+04:00 — Read Vu Section 6 completely (arXiv PDF pp. 8–11). Confirmed Conjecture 6.8 and weaker support question. Downloaded PDF and extracted full text. Primary author preprint found: Yaroslav Shitov, The range of 0-1 determinants is large, uploaded 2025-11-14, DOI 10.13140/RG.2.2.32216.35842. Read primary PDF through web reader; shell download returned HTTP 403. Theorem 1 covers all integers through floor(exp(0.5 n log n - 7 n log log n)). Publication status: preprint; no journal verified. Auditing elementary slips in intermediate text before final conclusion. Inherited nice is 15 (more polite than requested 10); no heavy computation.

2026-11-13T06:07:27.165182+04:00 — Completed primary-source audit. Verified the unimodularity input in Alon–Vu Section 2.4 and final remark. Independently rederived the sign-border determinant, Schur substitution, digit encoding, dimension slack (3-3/(2 log 2) > 0), and leading support exponent 1/2. Recorded correctable intermediate notation/rounding slips in Shitov rather than silently copying them. All 763 exact identity checks passed with Bareiss plus SymPy; one thread, nice 15, peak RSS 55,820,288 bytes. No distribution enumeration or Monte Carlo was begun because the literature stop condition was reached.

Conclusion: RESOLVED_IN_LITERATURE for the weaker support statement, specifically a public November 2025 author preprint, not a verified journal publication. Full atom conjecture not resolved here; no proof found in bounded searches. REPORT.md states this distinction on line 2, gives the exact reference/theorem, transfer proof, corrected dimension audit, and literature findings. OEIS support values are literature data, not fresh enumerations. PDFs, extracted primary passages, source hashes, code, and data are saved locally.
