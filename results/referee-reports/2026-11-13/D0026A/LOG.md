# D0026 work log

- Task received 2026-11-13 about 07:28 Asia/Tbilisi (launch files; first shell clock 07:29).
- Scope: D0026, literature first, independent of D0027; all deliverable writes in this directory; no subagents, publication, pushes, PDFs or page images. Simulation will use one thread at nice 10.
- Read startup memory and recalled the shared brain. Shared mesh/checklist mutations and durable brain writes fall outside this task's explicit directory-only scope and filesystem write permissions; keep the task record here. Do not contact sibling run.
- Initial governor: warn/cpu_saturated, owner_away_open. Keep compute small, one thread.
- Started primary source and resolution searches. Source retrieved directly into RAM and extracted into numbered plain-text pages; no PDF file created.

## Literature and first proof checkpoint (07:31–07:34)

- Read survey pp. 1–5 and Section 6 pp. 25–27. Conjecture 1 allows arbitrary nu; zero is infected; pi assigns q to zero (Bernoulli(1-q) on occupation variables). Conjecture 2 assumes an exponential tail for the origin-centred empty-of-infections interval, not a uniform gap assumption over all centres.
- Survey Theorem 6.2 proves linear Y(t) and diameter D(t) for finite infections at all q>0. It does not assert bilateral positive front speeds or local equilibration.
- Read BCMRT Theorem 2.1, Proposition 4.1 and Section 5 proof. The global uniform exponential moment of distance to a zero is used to control the probability that blocks in a growing observation box lack two zeros. No independence of the initial law is required.
- Read CMST Theorem 2.1 proof (near-equilibrium perturbative all-q result) and distinguished-zero setup; read Ertul Theorems 2.1–2.2 and Section 4. Their q restrictions must be retained.
- Bibliographic correction: 'Cutoff for the non reversible SSEP with reservoirs', arXiv:2211.14687, is by Hong-Quan Tran, not Ertul. Actual FA-1f front paper is Blondel–Deshayes–Toninelli, 'Front evolution...', EJP 24 (2019), paper 1.
- Candidate rigorous partial result: q>1/2, every deterministic configuration with at least one zero, hence arbitrary nu by bounded convergence. Burn in for (1-delta)t; the distance Lyapunov estimate is uniform on a box of radius 100 delta t around f. Fill exterior with zeros; the resulting time-dependent law has a uniform global exponential distance moment. Apply BCMRT Theorem 2.1 for remaining delta t and use finite-speed coupling. This avoids assuming monotonicity. Needs full constant audit.
- nice command attempted to increase inherited nice 10 to 20 and was denied; Python confirmed current priority already nice 10. Subsequent commands inherit nice 10.

## Proof checkpoint before computation

- Saved Theorem A with explicit theta, Lyapunov drift, time split, uniform moment bound for the auxiliary law, and clock-path coupling bound. The exterior fill is only at the start of the auxiliary evolution; no censoring/monotone comparison is used.
- Independently checked the cancellation: delta=lambda/[2(lambda+100 log theta)] makes 100 delta log(theta)-lambda(1-delta)=-lambda/2. Drift constant B=q/(q-p theta) agrees with BCMRT Proposition 4.1.
- Saved bilateral front bounds for finite infection sets at q>1/2 and all-q convergence for laws absolutely continuous with respect to pi. Neither establishes the missing low-q single seed case.
- Found a genuine 2026 citation: Fabio Martinelli, ICM 2026 short survey, DOI 10.1137/25M180425X, pp. 497–515, published online 13 July 2026. Exact-ID search finds this citation; its full text must be checked before completing literature audit. Search index alone is not a resolution certificate.

## Computation and final audit (07:36–07:43)

- Completed eight serial Gillespie experiments: q=0.1,0.3,0.6,0.85, two initial laws each, 2,000 independent paths per combination, interval [-24000,24000]. Main experiments executed 1,268,891,734 flips in total. All simulation processes confirmed nice 10; no parallel workers.
- Initial law (b): origin infected at time zero, independent extra infections with probability 0.04/(1+|x|/10). Its infinite-volume counterpart has infinitely many infections almost surely. Origin is not frozen after initialization.
- Saved CSV time series, seeds/commands/times, terminal residuals and standard errors, and an SVG chart. All 24 final local residuals are within 2.094 estimated SE of equilibrium. Single-seed low-q fronts have positive observed late slopes. These observations are not proofs.
- Simulator verified against all 31 nonempty states of a five-site generator with healthy boundaries. 120,000 paths, six observables, six observation times: maximum discrepancy 2.205 SE. Matrix exponential independently agrees with Poisson uniformization within 2.23e-16. Initial SciPy floating-point warnings were investigated; all outputs finite and the independent calculation agreed. No warnings suppressed until after that check.
- General clock-path bound gives log local boundary-influence probability <=-2365 for the main experiments. Sparse paths occasionally include/visit a boundary; that statistic does not imply influence at the origin. Global sparse extremes are not used as spreading evidence.
- Found and read a 2026 citing source: Fabio Martinelli, ICM survey, Conjecture 2.11, printed p. 502/PDF p. 6, still states the problem as open. Saved a primary text excerpt. Direct publisher download returned 403; web PDF text extraction succeeded. No resolving 2025–2026 theorem found by exact-ID/topic searches.
- Bibliography audit corrected Pillai–Smith Theorem 1 location to archived PDF p. 3. Source/preprint versus journal numbering is explicit. Mountford 1995 full theorem unavailable; exact title/DOI/page range verified through Crossref and no theorem number inferred.
- Resource probe: 5,423,104 bytes maximum resident memory, nice 10, one thread. `/usr/bin/time -l` cannot read sysctl under the sandbox, so peak memory was read inside the C++ process with getrusage. Main run memory arrays have the same fixed size and paths are processed sequentially.
- Final source scan found a NUL character inherited from a web search result, stripped it, then repeated the plain-text audit. No PDFs, paper images/scans, subagents, commits, pushes or publication.
- Final result: PARTIAL. Complete high-q deduction uses BCMRT Theorem 2.1 with every assumption checked; no novelty claimed. All-q singular initial laws, including the single seed at small q, remain unresolved. Report, code, data and sources saved here.
- Task: “Open problem D0026.” — 13 November 2026, 07:28 Asia/Tbilisi.
