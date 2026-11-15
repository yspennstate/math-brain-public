# D0023 work log

2026-11-13, started approximately 10:27 Asia/Tbilisi (shell clock).

Task: “Open problem D0023” — literature first, then a rigorous tractable result and numerical evidence if the original dynamic question is not resolved in print.

Constraints: all artifacts and writes confined to this directory; no PDFs or page images retained; one worker, numerical work at nice 10, one numerical thread, memory below 4 GB; no publication or git push.

Orientation: read startup memory and compute state; brain recall found no D0023 memory. Compute state warns of existing CPU saturation but reports owner away. No heavy computation started. The later explicit directory restriction prevents modifying the global checklist, mesh database, or brain. These are not relocated to a private imitation of the shared mesh. Read-only coordination inspection is used; this task writes only its isolated directory.

Literature discovery: original source is Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas 4(1), 1–15 (1999), arXiv:math/9906194. Located BMRS 2015, 2017, and 2020 papers. Full texts and exact theorem statements remain to be checked.

10:29: Initial source-download invocation stopped before downloading because macOS rejected os.nice(10). Startup memory already flags this platform issue: get current priority and only set it when below 10. Corrected before continuing.

10:32: Saved original source and BMRS 2015/2017/2020, BMRS local-equilibrium paper, 2021 survey, AFGL, GKS, Mailler–Mörters–Ueltschi, Godrèche–Luck, and Jain–Barma as text extracted in memory. Confirmed original Problem 2 on PDF p. 9 and its distinction from Problem 3. Read-only shared mesh query found no claim mentioning D0023 or this audit directory.

Literature finding: GKS (2004), Theorem 1, preprint PDF p. 6, gives two-sided annealed stretched-exponential tail bounds for tagged-particle correction on scale t^(kappa/(kappa+1)); it is real mesoscopic progress, but not a law for the condensate mass measure. BMRS local-equilibrium Theorem 2.3, preprint pp. 15–16, requires typical moving observation points; Theorem 2.4, p. 17, is time averaged without that restriction. Neither statement directly identifies the exceptional sites carrying mass.

Proof direction: finite totally asymmetric ring with g(n)=1, iid rates c+(1-c)U^(1/kappa), kappa>1, N/L -> rho>rho_c. Use exact representation of the canonical bulk as independent geometrics at fugacity equal to the sample minimum, conditioned on their sum being at most N. Control the rare near-tie between the two smallest rates explicitly; do not average 1/(rate-minimum) without truncation, whose expectation can diverge.

10:35: Literature-first assessment recorded in sources/SEARCH_NOTES.txt. No inspected theorem supplies the full joint space-time concentration picture. MMU's theorem assumes stationary weights with exponent beta>1, and therefore cannot simply be applied to constant g=1 (beta=0). Later coarsening and defect models have different limits. Proceeding to the explicitly authorized finite-ring proof and simulations. Found and corrected an indexed arXiv-identifier mismatch before using it as evidence.

Theorem A saved with a complete proof for every kappa>1, including the exact canonical representation, a polynomial bound on bad near-ties, slow-set size/tolerance, minimum-rate Weibull law, and the stationary empirical mass measure. The time limit is explicitly iterated, not a mixing estimate.

Numerical experiment completed: 36 independent rate realizations (kappa=1.5,2,3; L=128,384; six each), 11 snapshots each, exact Poisson uniformization from evenly spread supercritical mass. All raw occupancies and rates saved. Tiny-system validation uses 50,000 independent trajectories and a separately enumerated 15-state generator. Analysis completed successfully; macOS /usr/bin/time -l itself exits 1 because the sandbox denies sysctl kern.clockrate. Replaced that resource measurement with Python getrusage. Added a positive Poisson-series evaluation to cross-check scipy's matrix exponential after it emitted internal floating-point warnings; finite final probabilities were already within sampling error.

10:50: Completed REPORT.md with Theorem A and its full proof, including a finite-L quantitative error bound; the dynamic gap and initial-pile persistence bound; numerical methods, data and limitations; and exact theorem numbers and saved-version PDF pages for the literature. Follow-up checks included 2025 inhomogeneous geodesics/queues and 2026 semi-infinite exclusion, without conflating tagged second-class behavior or close-packed initial states with excess-mass evolution.

Verification: stationary balance residual 2.78e-17; conditioned-geometric formula discrepancy 5.56e-17; independent Poisson-series versus matrix-exponential discrepancy 1.39e-16. The 50,000 simulated tiny-system endpoints have TV discrepancy 0.005327 and maximum standardized error 1.755. Audited all 396 snapshots and rank-based masses. Across 36 trajectories: 298,460,791 proposals and 98,687,121 moves. At final time all 36 largest piles lie among the five slowest rates, but only 30/36 are at the single slowest rate. This is evidence, not a time-scale proof.

Resource record: one numerical thread, nice 10; analysis peak RSS 111,591,424 bytes. C++ state is O(L) and streamed, with no thread creation or large allocations. No numerical jobs remain running. Checked report status line, Python syntax, explicit proof exponents, all source files UTF-8 plain text with no NULs, and absence of PDFs or raster images anywhere in this directory. Shared/global brain and checklist were not modified under the directory-only instruction. Durable result and remaining gap are recorded here instead.

Task completed as PARTIAL: “Open problem D0023”, requested at approximately 10:27 Asia/Tbilisi, 2026-11-13. The original dynamic concentration question remains unresolved in this work; the finite-ring stationary theorem is proved and reproducible numerical evidence is saved. No publication or push.

Final follow-up audit: independently recomputed largest-pile rate ranks, slow-set membership, masses and baseline-subtracted estimates from every raw snapshot; all passed. Saved the 35-page Menshikov–Popov–Wade source as text only. Corrected the manifest name of the excluded random-DFA identifier mismatch so every manifest record points to its actual retained text file. Final source/plain-text and forbidden-image/PDF checks passed.
