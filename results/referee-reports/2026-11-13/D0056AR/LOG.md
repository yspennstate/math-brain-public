# Independent referee log

Task received: 13 November 2026, approximately 02:21 local shell time. Audit CLAIM.md and claim_files; deliver REPORT.md. No publication. All audit artifacts stay in this directory. No subagents; numerical workers will use at most four threads and less than 4 GB.

## Initial inspection

- Read the submitted statements and proofs independently. The sparse construction appears internally consistent; its moment statement is per fixed rho (orders up to rho), not a single sparse law with all orders below two.
- Began fetching the four principal arXiv references directly, rather than trusting the submitted literature summary.
- Read the compute governor (status ok). Attempted the requested mesh registration/digest; both fail because the coordination database is read-only in this sandbox. No bypass or external writes will be attempted. Checklist and durable-memory writes outside this directory are also excluded by the task's directory restriction.
- Initial source location issue: CLAIM.md references literature/, code/, and data/ as if it were inside claim_files; actual packaging has CLAIM.md at the root and code/data below claim_files. Will distinguish packaging defects from mathematical defects.

## Proof and source checks, approximately 02:24

- Independently derived equations (8)–(12), including the factor (m-1)/m multiplying 1-(1-q)^m. The comparison lemma uses an unstable forward recurrence and convergence to zero; its contradiction argument is valid in both directions.
- Downloaded fresh PDFs and extracted text for arXiv:2006.06140, 1705.04787v2, 2005.10208, and 2108.05610 into audit_sources/. Chen–Shi Theorem 1.1 has exactly the product, tail exponent range, and criticality used. The 2019 Theorem 2 supplies G_n(m) to 1. The 2021 sustainability theorem requires an exponential moment beyond m, so it is not contradicted by Theorem A.
- The 2019 Section 9 contains weaker harmonic bounds, not the claimed precise liminf/limsup bracket. Derrida–Shi Section 2.1 explicitly conjectures the two binary constants; it does not prove their survival asymptotics.
- Installed separate numerical dependencies under audit_vendor/; no submitted code or vendored packages imported. Planning exact Fraction checks on small supports and a separate FLINT integer-polynomial implementation for long certified runs.

## Independent computations, approximately 02:28

- audit_independent.py passed 120 exact generating-function/criticality identities, 28 exact truncated-law enclosure comparisons, 180 transport inequalities, and 8 comparisons of exact truncated and untruncated trajectories. Fractions, not floating point, were used in these checks.
- The first 10,000-generation run (m=2, two-point {0,2}) independently gives n^2 q_n = 4.0079637107992774, inside the submitted twelve-decimal certified interval. This uses FLINT polynomial powers rather than the submitted packed GMP code, a different precision (128 bits), and decreasing supports with a separately derived bound.
- A serialization limit on huge rational denominators stopped the first m=3 launch before any iteration. Disabled Python's decimal-string digit limit and restarted; no mathematical algorithm changed.
- Obtained the full 1983 Collet et al. proceedings scan. Appendix III assumes a smooth expansion; Appendix IV proves/describes product growth for singular tilted generating functions. Checking the scanned formulas visually because extraction loses exponents.
- Recent primary sources checked include Li–Zhang v3 (geometric offspring), Alsmeyer–Hu–Mallein v2 (geometric Galton–Watson offspring), the 2023 dual-conjecture paper (subcritical decay), Chen's smoothness paper, and Duquesne–Shi September 2026 (continuous branching). None of their stated results supplies a deterministic-offspring critical survival constant.

## Certificate wording and table audit, approximately 02:33

- The lower certificate columns are (ceil(S*q_numeric)-1)/S. This is a valid lower bound for the original untruncated process, because every numerical update is dominated by its untruncated exact update. However, CLAIM.md line 414 says these intervals enclose the exact repeatedly deleted process, while line 409 correctly says that process and the numerical process need not be ordered. The displayed transport estimate by itself gives a two-sided error for the deleted process. Required repair: subtract E_n/(m-1) for its lower endpoint, or relabel/prove the existing lower endpoint specifically for the original process. This does not invalidate the final original-process enclosures. A coarse rational search did not find a failing endpoint; the issue is the missing argument, not an observed failure of the reported data.
- Reconstructed every submitted numerical table from the saved data, independently recomputed all 46 regressions, and independently evaluated all 24 sparse leaf bounds. All those comparisons pass. The leaf CSV prints more digits than its 70-digit initialization supports, but agrees to that precision.
- Visually read Appendix IV in the Collet scan, including (AIV.5), (AIV.11), and (AIV.12): the conclusions concern product powers. Appendix III's exact prefactor computation is conditional on an assumed smooth expansion. Neither is an unconditional survival-limit theorem.
- Fresh certified endpoints so far: m=2 {0,2}, geometric, b=3; m=3 {0,2}, geometric. Every independent interval lies inside the corresponding submitted twelve-decimal interval.

## Full endpoint checks and novelty attribution, approximately 02:36

- All eight submitted twelve-decimal endpoint intervals now independently confirmed, including both sparse laws. The sparse spike checkpoints also reproduce.
- The first newly certified FFT-only case, m=2 with {0,5}, gives 4.004902865598777 at n=10,000, versus submitted raw FFT 4.004908491291294 (difference 5.63e-6). This is consistent with the report's explicit lack of a rounding guarantee for F rows, but six displayed decimal places are not all accurate for this row.
- Found a more specific prior result relevant to Theorem A: Chen–Hu–Shi, arXiv:2306.12717, Remark 1.2, already uses the bound X_n >= the number of leaves initially at least n+1, to show necessity of an exponential-moment condition for their subcritical conclusion. Thus the one-large-leaf mechanism itself is established literature; the particular tuned sparse critical law and exponent obstruction are the possible new part.
- Package manifest: 50 present files all have correct recorded hashes; 17 entries are absent under claim_files (REPORT.md and 16 literature PDFs). CLAIM.md itself matches the manifest's former REPORT.md hash.
- Started independent single-threaded FFT reruns of both 100,000-generation diagnostics, alongside the one certified worker. Three numerical workers total, all at nice 15 and with library thread counts set to one. Governor is not in distress (CPU saturation warning only); memory remains comfortably below the requested ceiling.

## Draft verdict and broader source check, approximately 02:40

- Wrote REPORT.md with provisional disposition MINOR. The proof verification and literature assessment are complete; final numerical additions await the last runs.
- The independent exact geometric initialization check includes the total tilted mass of coefficients that round to zero. It verifies the chosen initial transport bound exactly; this avoids counting only visibly nonzero lattice coefficients without controlling the residual tail.
- ArXiv's complete title/abstract query returns sixteen Derrida–Retaux items. The additional recent items are Li–Zhang's scaling-limit paper (renewal rate tends to zero), Lotnikov–Kotova's phase criteria, and a coagulation/continuous-equation paper. Their statements do not prove the fixed deterministic-offspring critical survival constant.
- The independently certified m=3 {0,5} value at n=10,000 is 1.000506086873256, versus the submitted raw FFT 1.0005072613555224. This confirms that the six-decimal discrepancy affects both two-point F rows.

## All 10,000-generation checks complete, approximately 02:46

- Finished all sixteen independent certified cases. All forty-two main-table checkpoints have independent comparisons, all twelve sparse table values reproduce, and all eight submitted rational endpoint intervals contain the new rational enclosures.
- Across every saved checkpoint in these sixteen runs, the largest scaled interval width is 4.93e-19. The largest certified worker peak RSS was 83.24 MiB.
- The b=4 F rows also lose displayed digits: at m=2 the certified endpoint is 3.639732708119070, versus FFT 3.6397226150826034; at m=3 it is 0.922957994239232, versus FFT 0.922960499563346. REPORT.md now gives all eight corrected F endpoints and their differences.
- Added an exact illustration of the deleted-order issue: with m=2, K=3, critical nu=(16/17)delta_0+(1/17)delta_3 and dominated mu=(16/17)delta_0+(1/17)delta_2, the deleted updated survival probabilities are 32/289 and 33/289 respectively. This is an obstruction to a general monotonicity proof, not a claimed counterexample to the specific quantizer.
- The two independent 100,000-generation FFT runs remain active; all other numerical work has completed.

## Finished, approximately 02:50

- Both independent FFT runs reached 100,000 generations and exited successfully. All six displayed long-run checkpoints match the submitted binary64 outputs exactly, including the {0,2} endpoint 4.385326014725255 and b=3 endpoint 1.5000525117509445. These remain raw diagnostics, not certificates for the true law.
- Final resource metadata: maximum worker peak RSS 189.91 MiB; sum of the three largest individual peaks 458.27 MiB; maximum three simultaneous numerical workers, each single-threaded at nice 15. Numerical processes are finished.
- Final comparison artifacts record 42 independent main-table comparisons, 8 independently confirmed twelve-decimal certificates, 86 table/source checks, 46 independently reconstructed fits, 24 leaf-bound checks, and 6 exact binary64 long-checkpoint matches. Small exact-law checks and the deleted-order example are retained separately.
- Rechecked the source snapshot: submitted files and CLAIM.md remain unchanged. REPORT.md begins exactly MINOR, contains the required numbered fixes, proof audit, numerical results and literature/novelty assessment. No central mathematical error was found. No publication, repository operation or external write was performed; outputs are confined to this directory.

Task: “Your job is to break it if it is wrong. … Write REPORT.md. … Keep LOG.md as you go.” Received 13 November 2026, approximately 02:21 local shell time (+04).
