# Independent referee log

Task: “You are an independent referee… Break it if it is wrong.” Received 2026-11-13 07:36:31 +04 (Asia/Tbilisi), from PROMPT.md timestamp.

## Orientation, 2026-11-13

- Read the supplied instructions, startup memory index, compute state, and shared mesh protocol. This task explicitly confines work to this directory; shared mesh/checklist/brain writes are outside scope and unavailable under the sandbox. No substitute coordination database, subagents, publication, or pushes.
- Compute state: warn / owner_away_open, CPU saturated. Shell has nice 10. All simulation and numerical analysis will use one thread with library thread caps and small memory.
- Read claim_files/REPORT.md and LOG.md. Claim Theorem A uses a short second-stage patched law; the essential audit point is whether BCMRT's uniform-distance result has constants uniform over that family. Theorem B is explicitly a near-equilibrium CMST argument.
- Located the four requested primary papers through arXiv. Sources will be downloaded independently, converting PDF bytes through a pipe in memory; only plain text will be retained in sources/.

## Primary-source and proof checkpoint

- Independently downloaded all four requested arXiv PDFs into memory and piped bytes to pdftotext. Saved text only, plus SHA256 and page counts in sources/manifest.txt. BCMRT arXiv v1 has 21 pages; survey 29; Mountford–Valle 22; CMST 16.
- Read exact Conjectures 1–2: centered exponential gap tail; no independence/stationarity/infinite-infection assumption. Survey cites only threshold-q results and gives different-generator all-q results.
- Read BCMRT Theorem 2.1 and Sections 3–5, Mountford–Valle Theorem 1.1/Remark 1.2, and CMST Theorem 2.1 with proof. BCMRT is uniform over laws with a fixed exponential-distance moment bound. Its Section 5 uses union bounds, not independence of bad blocks.
- Re-derived claim drift algebra: lambda=(theta-1)(q/theta-p), b=q(theta-1)/theta, B=b/lambda=q/(q-p theta). Positive for 1<theta<q/p, hence q>1/2. The cone/short second-stage inequalities have sufficient slack, including integer floors.
- Noted a loose source-paper exit-event estimate (BCMRT Section 3.2, p. 8); a volume factor and endpoint term repair it and are only polynomial on the required boxes. Will give the repaired argument in the report so this does not remain a hidden dependency.
- Wrote independent C++ flip-rate Gillespie code without reading or reusing claim_files/code. First single-seed run: q=.55, 500,000 trajectories, 49,816,304 flips, 3.29 seconds, no boundary hits. q=.6 and .75 runs follow; full per-batch counts retained.
- Literature search found a September 2026 oriented-KCM preprint, arXiv:2609.30585, absent from the claim's search. Checking its actual scope and citations before assigning significance.

## Independent numerical checkpoint

- Preliminary 500,000-trajectory runs at q=.55,.6,.75 and separate 1,000,000-trajectory longer runs show an initial positive bias, an equilibrium crossing, then a negative bias decaying back toward zero. Therefore a single semilog fit across the whole trajectory would be inappropriate.
- Longer runs: q=.55 through t=96 (1,125,536,292 flips, 53.95 seconds); q=.6 through t=80 (971,635,469 flips, 46.91 seconds). No boundary hits. Interval is [-512,512], initially healthy except its single infection at 0, frozen healthy exterior.
- Independent validation: enumerate the 128-state seven-site chain with infected boundary, construct its generator directly, and compare exact matrix exponentials against 200,000 Gillespie trajectories at each of the three q values. Across 24 time/q comparisons the largest absolute standardized discrepancy is 2.4933. Row sums, detailed balance, and stationarity agree to floating-point precision. Exhaustive nine-site drift checks have maximum residual 1.20e-15. Active-list bookkeeping checked after every flip in a separate smoke run.
- Citation checks: OpenAlex confirms W4416620060 and returns one citing work, the 2026 ICM survey. Semantic Scholar returns zero citations (different coverage), not a comprehensive bibliography. ICM publisher direct access is HTTP 403; indexed publisher text states Conjecture 2.11 and a threshold-q restriction. Saved API responses as text. Chleboun 2609.30585 is about oriented update families, does not cite 2510.20461, and does not apply to FA-1f.
- To improve later-tail precision, a separate 5,000,000-trajectory confirmation run per q will use fixed windows chosen now from the exploratory runs: .55 at t=24,32,40,48,64; .6 at t=20,24,32,40,48; .75 at t=8,10,12,16,20. Fits and residuals will all be retained, including poor fits. These are finite-time evidence only.

## Confirmation results and referee decision

- All three five-million-path runs finished with zero boundary hits. Wall times .55/.6/.75: 206.151 / 99.966 / 42.930 seconds; flips 4,018,471,493 / 1,906,540,050 / 740,533,411. At most three single-thread simulation processes ran concurrently, all inheriting nice 10.
- Fixed-window log-OLS slopes: .0543821, .0716738, .135785; batch bootstrap intervals [.0482080,.0627554], [.0636712,.0825771], [.112408,.169219]. All data, seeds, signed summaries, and bootstrap diagnostics are retained.
- A separate correlated-error exact-exponential shape fit has approximate p values .373, .267, .000111. The .75 window still includes transient curvature and rejects an exact single exponential. The report explicitly preserves this negative result; no window was changed to improve it. This does not test or contradict an exponential upper bound.
- For the single-seed start, boundary influence is bounded by 2(qT)^512/512!, using the necessary ordered infection-coin sequence across successive sites. At the largest actual qT=52.8 this is less than 5.61e-285. This sharper start-specific bound also handles the exploratory t=96 run, where the crude generic FP bound would be uninformative.
- Saved REPORT.md with ACCEPT as its first line. Theorem A's drift, replacement-law moment bound, uniform BCMRT input, short second-stage propagation, integration over arbitrary initial laws, and single-seed case check. Theorem B is a valid CMST-type perturbative result; its Markov examples were already covered by those methods. No claimed all-q solution is accepted.
- Saved the independent simulation figure as data/referee_decay.svg, with resolved and unresolved points distinguished. Source texts remain text only. No publication or push.

## Final independent audit

- Re-derived all three fitted slopes using scalar sums from integer CSV counts, independently of the NumPy fitting code. They agree to <1e-12. Re-derived the boundary bound with a 60-digit Decimal product: 5.6021850109601064e-285. Rechecked the drift coefficient against BCMRT's differently written formula and checked both cone inequalities numerically at all three q values.
- Verified every saved paper text against its SHA256 in the manifest; sources/ contains .txt files only. Confirmed no retained PDF/PS/DjVu, plot SVG parses, REPORT.md starts ACCEPT, and claim REPORT/LOG hashes are unchanged.
- A separate environment-version probe omitted the plotting-cache environment variables: home-cache access was blocked, and Matplotlib briefly used its automatic temporary directory outside the task folder. Its exit cleanup removed that directory, which was checked. The actual analysis uses task-local cache paths. A read-only ps resource probe was denied by the sandbox; no result relies on it.
- On draining the finite-generator validation's stderr, observed dense BLAS/matrix-exponential floating-point warnings even though all returned numbers were finite. Replaced the exact expectation calculation with sparse Poisson uniformization (tail bound <1e-30), and stationarity multiplication with elementwise sums. Preserved the first dense-method validation JSON for comparison, and reran the affected checks. The agreement, rather than an assumption of harmless warnings, is required before finalizing.
- Final uniformization validation passed with empty stderr. Maximum difference from the original dense matrix-exponential calculation is 6.7724e-15; maximum Monte Carlo standardized discrepancy remains 2.4933. Recorded both methods in REPORT.md. All simulation/validation/analysis processes have completed.
- Done: ACCEPT the claimed partial result, with source-proof repairs and literature qualifications stated; no all-q solution or novelty certificate. REPORT.md, LOG.md, twenty plain-text source records, independent code, and numerical evidence are local. Original claim REPORT/LOG hashes are unchanged. No subagents, publication, pushes, or persistent shared-state mutations.

Task: “Break it if it is wrong.” Received 2026-11-13 07:36:31 +04 (Asia/Tbilisi).
