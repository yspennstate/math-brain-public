# D0093 work log

Task received: 2026-11-13, approximately 12:28 Asia/Tbilisi.
Task: Open problem D0093, remove logarithms in the fast-phase cycle ARW toppling bound.

## 2026-11-13 12:31 +04 — working

- Read startup memory and recalled prior ARW work. Recall had no D0093 match.
- Read compute state: status ok, owner_away_open. All subsequent computation will use nice 10, one worker, thread caps; no subprocess agents.
- The present request confines all work and writes to this directory. Consequently no global checklist/mesh/memory writes are made; this log is the local task record.
- Found survey arXiv:1906.05037v2 (28 September 2020), and original cycle paper arXiv:1709.09163.
- Literature search discovered Johnson–Richey, 'The Odometer in Subcritical Activated Random Walk', arXiv:2510.05514; checking whether its result settles the requested bound before any new proof/computation.
- No publications, pushes, PDFs, paper images, or scans will be saved.

## 2026-11-13 12:36 +04 — literature/proof corrections

- Survey Theorem 6.1 and open problem are PDF p.30 / printed p.507. Initial data are iid Poisson(zeta), not Bernoulli.
- Proof of (6.3) is Section 6.2, PDF pp.32–35 / printed pp.509–512. Section 6.1 concerns the slow phase.
- Explicit fast-phase regime in its proof: zeta < lambda/(1+lambda), choose intermediate zeta'. There are two stages, no logarithmic number of rounds. A global union bound makes radius r ~ log n; diffusive concentration at sources costs r^2 per particle. Thus two powers arise from one diffusive scale squared.
- BGHR arXiv:1709.09163v2 (2018, published 2019), Theorem 1 p.2: n log^2 n for Bernoulli data and zeta < lambda/(1+lambda); Theorem 2 p.3: exponential lower bound for sufficiently small lambda. Survey extends initial data to Poisson explicitly.
- HJJ arXiv:2406.01731v2, Proposition 8.12, PDF pp.67–68: extends n log^2 n fast bound to all rho<rho_c, but does not remove logs.
- Johnson–Richey arXiv:2510.05514v3 (13 October 2026), Theorem 1.1 / Corollary 1.2, p.2: sharp stretched-exponential odometer tail and finite mean for Bernoulli initial data on Z. Not by itself a cycle theorem; their p.3 says light-tail generalization should hold but does not state/prove it as a theorem.
- Process priority independently read with os.getpriority: 10. Explicit nice commands warn because sandbox denies setpriority; the inherited required priority is already 10. No priority change is needed.

## 2026-11-13 12:43 +04 — proof attempt before computation

- Literature search has not found a printed O(n) toppling theorem for the conservative cycle. The fast-mixing papers concern a driven chain whose time unit is a particle addition followed by stabilization.
- Checked additional work: Forien (macroscopic flow, 2025); Forien (density conjecture, 2025); Hoffman–Hu–Richey–Rizzolo (stochastic sandpile, a different model); Cairns–Ganguly–Levine (one particle per site, sleep rate depending on system size); de Lima–Rolla–Terra (slow phase); 2026 stationary ARW work (driven system).
- Found a rigorous obstruction to the original two-stage method. For equally spaced sources distance L apart, Poisson splitting makes source counts independent Poisson(zeta L). A fixed or o(log n) spacing fails the required source-cap condition with probability tending to one. Meanwhile gathering all particles has mean zeta(1+lambda)n(L^2-1)/6 and cost at least c n L^2 with exponentially high probability. Thus the gathering cost really is quadratic in the logarithmic block scale.
- Attempts based on geometric site charging fail because every return can reactivate a sleeper; a sleep does not provide a permanent site retirement. Infinite-line odometer bounds do not immediately dominate cycle odometers: cuts remove returns around the cycle and yield the opposite monotonicity for killed systems.
- No new O(n) or O(n log n) upper bound is established. Preparing a precise method-obstruction proof, a conditional localization criterion, and reproducible simulations. These must not be reported as a solution of D0093.

## 2026-11-13 12:53 +04 — computation complete; audit

- Completed 5,320 Poisson-cycle simulations, n=1,000 to 100,000, seven parameter pairs. All stabilized before 10,000n instructions; no discarded or censored runs. Data/runs.csv contains every seed and count. Means of T/n are stable over the tested range; no asymptotic claim is inferred.
- Main simulation wall time: 25.2 seconds; one thread, nice 10, measured peak RSS 17,629,184 bytes. macOS/sandbox rejected setrlimit requests; actual footprint and errors are recorded in simulation_metadata.json.
- Validation: 360 cases replayed under three legal orders using identical retained stacks, exact odometer/final-state agreement. Three 100,000-trial one-particle geometric-law checks passed. Independent CSV accounting, Poisson mass and jump instruction diagnostics passed.
- Code/check_math.py independently solved 252 exact rational hitting-time systems; formula for mean gathering cost and elementary lower-bound constants passed.
- Added a rigorous deduction from Johnson–Richey: for survey-fast Poisson cycle data, liminf_n P(m_n(0)>=t) is at least c exp(-C sqrt(t)). Hence a size-uniform geometric marginal bound (even with an error vanishing in n) is impossible. This does not rule out a linear sum.
- Added a conditional localization lemma with a complete variance proof and an almost-sure linear law for the killed Bernoulli interval. Neither is represented as a conservative-cycle solution.
- Rechecked HJJ Proposition 8.7 p.64 and Proposition 8.12 pp.67–68. The Poisson extension of their all-subcritical n log^2 n bound is explicitly marked as a deduction from their point-source confinement result and the survey construction.
- Saved 19 paper texts with page separators, hashes, and pinned arXiv versions where present. All source downloads were converted in memory; no PDF, paper scan or page image was written.
- REPORT.md status is NO_PROGRESS for the requested improvement: no O(n) or O(n log n) cycle upper bound proved. The report includes precise obstructions and simulation evidence, not a purported resolution.

## 2026-11-13 12:56 +0400 — done

Completed the authorized investigation. Final status: NO_PROGRESS on the requested logarithm removal. REPORT.md, 19 paper texts, code, raw and summarized data, and two original SVG plots are saved. Final audit passed: source hashes, report links, exact arithmetic and simulation checks, no retained PDFs or raster images. Visually reviewed the simulation plot. No publication, push, subagent, global-memory edit, or unrelated work.
