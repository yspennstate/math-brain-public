# D0027 work log

Task: “Open problem D0027.” Launcher prompt timestamp: 2026-11-13 07:14:13 +04 (Asia/Tbilisi).

## 2026-11-13: orientation and literature first

- Read startup memory, consulted brain recall for FA-1f / distinguished zero (no relevant prior result), and read compute state: warn, owner away, CPU saturated. All numerical work will be single threaded at nice 10, below 4 GB.
- Shared mesh registration attempted before work; rejected by filesystem sandbox: `attempt to write a readonly database`. Shared brain/checklist mutations are outside the explicitly allowed directory; no private mesh pretending to coordinate shared state will be used. Work is confined to this isolated task directory. No subagents, pushes, publication, or trading services.
- Located original arXiv HTML and a primary author copy of Blondel–Cancrini–Martinelli–Roberto–Toninelli (BCMRT). Initial search also found Mountford–Valle (2019), which needs checking before interpreting its title as a resolution.
- Important correction to supplied paraphrase: source Conjecture 1 assumes at least one infection almost surely, not infinitely many. Exact source text and theorem statements to follow.

## Literature checkpoint

- Saved arXiv:2510.20461 (29 PDF pages) and BCMRT author preprint (21 pages) as text, with source URLs and SHA256 in sources/manifest.jsonl; PDF bytes passed directly to pdftotext and never written to disk.
- Read Section 1 of the survey and BCMRT Theorem 2.1, Proposition 3.1, Proposition 4.1 and Section 5 proof. BCMRT requires `sup_x E_nu(theta^{distance(x,infections)}) < infinity`, not independence. The drift threshold is q > 1/2.
- Read Mountford–Valle Theorem 1.1 and Remark 1.2 (arXiv:1609.01364, pp. 2–3). Remark 1.2 explicitly treats an exponential distance tail at a single center, but only for q sufficiently close to 1. Its title does not resolve all-q Conjecture 2.
- Candidate partial theorem: extend BCMRT's q>1/2 estimate to the survey's origin-only hypothesis by a two-stage argument (create a cone with uniformly bounded infection-distance moments, replace the configuration outside the cone by zeros, then apply uniform-law relaxation and finite speed). No novelty claim until audit.
- Source survey Section 3 is about the East-polluted model, Section 4 about delta-West, Section 5 about BABP; their all-q conclusions cannot be transferred to ordinary FA-1f merely by comparing generators.
- Numerical priority inspection gives inherited nice 15. `nice -n 10` cannot raise it to 10 in this sandbox; subsequent work keeps nice 15, which is lower priority than requested. Numerical libraries will be limited to one thread.

## Proof and evidence checkpoint

- Saved REPORT.md with first line PARTIAL, Theorem A (q>1/2, arbitrary centered-gap initial law), its distance-drift and finite-propagation proofs, and Theorem B (all q, sufficiently slow local likelihood-ratio growth), with a correlated Markov-law corollary.
- Theorem A uses BCMRT Theorem 2.1 as an explicit published input. It does not assert a new all-q result or silently import the East distinguished-zero property.
- Citation follow-up: OpenAlex W4416620060 returned one citing work, Fabio Martinelli's ICM 2026 survey (DOI 10.1137/25M180425X). Its Section 2.2.1, Conjecture 2.11, still formulates the nonstationary FA-1f problem as a conjecture and discusses only threshold-q results. Semantic Scholar returned HTTP 429; citation coverage is not exhaustive. A 2026 MPI talk on patch-positive systems concerns the East model with independent noise, not a stated solution of D0027.
- Mountford 1995 exact title/DOI checked through Crossref: Exponential convergence for attractive reversible subcritical nearest particle systems, DOI 10.1016/0304-4149(95)00048-c. Full-text attempt returned HTTP 429; no theorem number or FA-1f application inferred from its title.
- Corrected an ancillary source download: guessed arXiv math/0610109 was unrelated Jacobi-polynomial work. Replaced CMRT2008.txt with the verified author copy of Kinetically constrained spin models, PTRF 140 (2008), 459–504. The old manifest record is superseded by the later record of that filename. Theorem 6.3, journal p. 484/PDF p. 26, is the actual all-q spectral-gap input.
- Built a single-thread C++ exact continuous-time simulator using the legal-site rate-one proposal clocks. Smoke runs audited the active-site list after every update. Main runs: stationary shifted-geometric renewal and hidden-Markov initial laws, q=.25 and .65, 1,000 independent trajectories each, length 1024, middle 256 sites, t<=60. Two equilibrium controls use 500 trajectories each.
- Independent N=8 generator checks use 6,000 trajectories for each of renewal/q=.25, hidden-Markov/q=.65, and equilibrium/q=.25. All four observables agree with exact matrix-exponential expectations within 2.33 empirical standard errors over the sampled times. Exhaustive N=10 checks verify the distance-generator inequality in all 1,024 states for 18 parameter pairs, to roundoff. These finite checks are evidence, not proofs of infinite-volume relaxation.
- The first density fits show that renewal/q=.25 is already below the noise level at t>=8, while hidden-Markov/q=.25 first moves away from equilibrium and has not reached a convincing decay regime by t=60. Kept those outcomes. An exploratory longer hidden-Markov run (length 8192, 500 trajectories, t<=600) will check later behavior; it does not replace the first data.
- Fixed local plot-cache paths after Matplotlib's initial attempted home-cache access was blocked. Files outside this workspace were not deliberately modified. Replaced a diagonal matrix multiplication in the detailed-balance checker with elementwise row weighting after spurious BLAS floating-point warnings; the numerical outputs already passed, and the revised checker will be rerun.

## Final audit

- Longer hidden-Markov/q=.25 run completed all 500 trajectories. Exploratory 75–600 fit: c=.00356295, trajectory bootstrap interval [.00319553,.00397260], log R^2=.996378, free-beta fit 1.01. This is compatible finite-time evidence, not a proof or a restriction on other laws.
- Recorded the renewal/q=.25 original later-window non-fit and the hidden-Markov/q=.25 early poor fit, alongside exploratory alternatives. Main raw data and signed means remain saved.
- Independently reran the revised generator/drift checker without the diagonal BLAS multiplication; it passed. Largest matrix-exponential versus Monte Carlo standardized discrepancy: 2.329967. Exhaustive drift residual at most 1.6e-15.
- Saved exact references/theorem numbers and version-specific pages in REPORT.md. Kept unverified Mountford-1995 full text/theorem number and limited citation indexing explicitly identified. The only indexed 2026 citing survey still states the FA-1f convergence conjecture.
- Saved code/reproduce.py with all parameters and seeds, serial execution, nice >=10, and thread caps. Its syntax and individual underlying commands were checked; the entire runner was not executed again because the underlying checks had already passed.
- Reviewed both generated plots. Set consistent colors for the same laws across panels, preserving all numerical outputs.
- Artifact audit: REPORT.md starts PARTIAL; all source files decode as text; no retained PDF, PostScript, DjVu, paper images, or scans; own simulation figures only. Source hashes match the latest download records. All deliberately written task artifacts are within this directory. No subagents, publication, or pushes.
- Shared mesh/checklist/brain writes remained unavailable in the read-only sandbox. Durable results are in REPORT.md and this local log; no private coordination store was substituted for the shared mesh.

Task complete as a partial research result: “Open problem D0027.” Prompt file timestamp 2026-11-13 07:14:13 Asia/Tbilisi.
