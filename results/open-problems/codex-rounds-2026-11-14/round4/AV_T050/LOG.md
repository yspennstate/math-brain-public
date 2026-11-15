# T050 round 4 log

Task: “Verify: has open problem T050 been settled by the OpenAI math release?” — received 2026-11-15T04:15:56+04:00.

## 1. Orientation and earlier work
Read both earlier REPORT.md and LOG.md files, the round 3 PROOF.md and check_local_potential.py, and the startup memory index and compute state. The first folder has no PROOF.md or scripts. Reads used `OMP_NUM_THREADS=1 nice -n 15 python3`; inherited lower priority causes the familiar macOS nice warning. Compute state: warn/cpu_saturated, owner_away_open; only tiny reads and finite checks planned. The instruction to write only in this folder excludes global mesh, checklist and brain mutations. No git or subagents.

Initial web searches: exact strict-convexity title; `openai/math first-passage error`; `first passage percolation strict convexity 2026 exponential limit shape arxiv`. No new solution established by these search results. Current primary sources and the known later citation will be opened next.

## 2. Bounded update check and extension choice
Within the initial five-minute window, opened the current strict-convexity introduction, foundations and README through the GitHub read-only connector, lean/docs/212.md, repository history, and arXiv:2610.42124 abstract (Scott Armstrong and Ahmed Bou-Rabee). Searches for exact title plus error, November, refutation, and arXiv strict convexity found no new resolution or proof assessment. Lean scope still explicitly omits strict convexity; history has no relevant repair/withdrawal. Incorrect guessed raw introduction path returned 404; the correct connector path sections/introduction.tex opened. No SOLVED_ELSEWHERE finding.

Chosen extension: audit found:lem-common-gauge, specifically the same-baseline insertion in different completed worlds, with admissibility, equal means and support independence checked separately. This is the next step explicitly requested by the round 3 report. First independently recheck the round 3 abstract lemma and its constant; do not treat its finite tests as proof of FPP hypotheses. Current foundations saved as strict-foundations-current.tex.

## 3. Primary source and independent re-derivation
Current foundations are byte-identical to round 3: SHA256 2b4099ac2502613172cba97cd1cd8c842f7ffab33678fa9fee7fa1e013792ba4. Read foundations lines 1–150, 150–250, 460–870, 950–1100, plus improvement lines 1–245. Copied the prior VERIFY.md and supporting evidence into this folder, leaving prior folders untouched.

Independent re-derivation of round 3: write Pi_S as the product over i in S of (identity minus integration in i), followed by integration off S. Its norm is at most 2^|S|, its mean is zero, and it kills any function missing one S coordinate. The gauge subtraction has a centered residual of norm <=2 epsilon; its common and cutoff terms number at most 2N. A cutoff path takes <=4R boundary edges and 4H+10 eastward edges, plus one label switch, so B=4R+4H+11. Hence C_H=2+2NB2^m as reported. For H=2, 2*(73^2)*163=1737254 and m+q=106; the prior claim holds. A distinct small exact script will check these identities and the new world-coupling step.

Extension geometry: choose L=2R+4H+22 periods earlier along the baseline coordinate. For every contributing S, reach the nearest side of Q_R(k(S)) in <=L steps, traverse <=4R boundary steps and then 4H+10 eastward steps. With one attachment comparison this costs J=L+4R+4H+11 comparisons, all with supports disjoint from S. This yields C_common=N 2^m (L+J K), where K beta bounds each network comparison error. Independence, equal means, and interpolation will be proved explicitly in PROOF.md.

## 4. Conditional common-gauge proof and exact checks
Wrote PROOF.md, check_common_gauge.py and a provisional REPORT.md before running checks. The proof separates admissibility of private insertion, same-law random-anchor means, exterior-independent conditional projections, the disjoint-support signed detour, and interpolation. It assumes the uniform network comparisons rather than certifying them.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 check_common_gauge.py`. Exit 0. Earlier tensor decomposition, zero means and L1 bounds passed on all 8 biased atom functions; C_2 reproduced exactly. For H=2,3,5, exhaustive center/direction detour maxima were [264,228], [320,276], [432,372]; J was 265,321,433 respectively. Three coupled worlds passed all 24 conditional-expectation and 21 nonempty projection comparisons. Random-anchor mean was -1/135 in all worlds. Deliberate exterior dependence gave L1 discrepancy 40/81 (negative control); independent incoming blocks factorized exactly. Runtime 0.071 seconds, peak RSS 15.70 MiB, inherited nice 20. No check failed.

All three current primary introduction sources were reopened through the read-only connector. Their exact theorem environments match the preserved quotations: exponential planar strict convexity, Gamma differentiability only, planar no-bigeodesics, and unrelated univalent integral means. Opened the full arXiv HTML of Armstrong–Bou-Rabee 2610.42124v1: it still calls the planar exponential result an announcement and studies continuum fluctuations.

## 5. Attempted failure cases and source consistency
Reopened current PlanarFirstPassage.lean and GammaPassage.lean. Their contents and all three primary introductions match saved earlier sources after trailing-newline normalization; saved reopened-sources.json for review. Both selected Lean conclusions still omit strict convexity.

Re-derived every load-bearing computed value algebraically: L=20H+62; J=56H+153; A detour maximum=56H+152; B maximum=48H+132. Toy xor anchor has probability 7/15, giving mean (-1/15)(28/9)+(7/15)(3/7)=-1/135. The exterior-dependence negative control is 2(4/9)(5/9)=40/81. Reviewed failure cases: shared private arrays can destroy incoming independence; exterior-dependent baseline costs can destroy common projections; a non-periodic tube can destroy admissibility. The proof states the necessary restrictions and the displayed straight-tube construction supplies them as described.

Appended the exact common-gauge lemma and round 4 spot check to VERIFY.md, retained the exact original theorem quotations and recommended three-sentence status, and finalized REPORT.md with actual check outputs. Remaining uncertainty is the uniform network hypothesis and downstream estimates.

## 6. Final audit, initial failure and repair
Final document audit confirmed the theorem quotations but stopped on a missing inherited local evidence link: current-source-audit.json. This was a copy omission in the retained round 3 appendix, not a mathematical check failure. Reading the remaining local links and copying their existing round 3 evidence into this folder before rerunning the audit.
Copied: check_local_potential.py, current-source-audit.json. Earlier folders untouched.
Also preserved the full earlier proof as round3-finite-cell-proof.md and repaired its inherited VERIFY link, so the round 3 appendix still leads to its original detailed argument.

## 7. Final audit passed
Command: `OMP_NUM_THREADS=1 nice -n 15 python3` document/source audit. PASS: four original theorem environments and common-gauge lemma quoted exactly; all local links in VERIFY.md and both proof files exist; recommended replacement has at most three sentences; REPORT uses its required final verdict; reopened sources match saved files. The initial document audit failure was repaired by copying missing inherited evidence and preserving the earlier full proof separately.

Reviewed the proof against the source. Removed an unnecessary identical-marginal requirement on exterior auxiliary arrays: common projections need only independence, and random-anchor means use the separately established joint law of the actual environment and anchor. The mathematical check script has not changed since its successful run.

Completed VERIFY.md, PROOF.md, REPORT.md, check_common_gauge.py and source evidence. General T050 literature status remains PARTIAL-CLAIMED; PROVED refers only to the conditional common-gauge step. Task: “Verify: has open problem T050 been settled by the OpenAI math release?” — received 15 November 2026, 04:15 +04.
