# G0012 research log

2026-11-13 09:39 Asia/Tbilisi — Task received: Open problem G0012. Literature first; then gap, proofs, computations. No subagents, publication, or pushes. All research artifacts remain here.

Startup: memory index and compute governor read (status ok, owner_away_open); brain recall attempted. Mesh hello failed: readonly database. Shared checklist is readable but cannot be updated within directory-only sandbox. No external state will be mutated.

Located Dozier, arXiv:2608.26321v1 (26 August 2026). Source has Sections 1 and 2, no Section 3. Proof is by plans/excursion reversal, not second moments.

Literature checkpoint — Full Dozier source saved as HTML-derived mathematical text and as page-labelled PDF extraction (PDF bytes only in RAM). Read entire proof, Lemmas 2.1–2.3, PDF pp. 3–8; introduction pp. 1–3. No Section 3 exists. Bencs et al. 2608.09729v1 saved similarly: Theorems 1–3 and Question 4 show bounded-degree sqrt(n) log(n) upper bound and explicitly distinguish multigraph counterexamples. Searches cover all named authors plus exact arXiv/title/Alon–Peres queries. No all-simple-graph resolution located. Alon birthday draft search hit found, direct old URL 404; will try current author host.

Proof direction: weighted departures 1/(deg(v)-1), inverse pairing distorts weight by at most (Delta-1)/(m-1). Uniform conditional resampling of the replacement derangement should give unit integrated congestion per possible departure index. Need check repeated excursion vertices, endpoint returns, and first-collision indices before asserting theorem.

2026-11-13T09:48:49 — Candidate weighted plan proof saved in PROOF.md: p_k <= min(1,256 Q(1+Q)n/k^2), Q=maximum degree/(minimum degree-1). Explicit bounded-ratio and bounded-maximum-degree corollaries. Full conjecture remains open here. Simulation and exhaustive small-plan audit running, inherited nice verified 10, numerical libraries limited to one thread.

2026-11-13T09:50:46 — Exact proof audit passed: {'plans': 6168, 'reversal_checks': 35624, 'replacement_checks': 26750, 'packing_checks': 23200, 'congestion_checks': 8010}. Cases: K4, K5 minus one edge with both starting orientations, K3,3, cube; all k from 2 to n-1 and L from 1 to n+1. Checked plan/DP probabilities, reversals including involution, directed-edge disjointness, terminal injection, certificate persistence under every replacement, and congestion.

Monte Carlo finished: 27 graphs, 39 fixed directed starts, 4000 trials each = 156000 walks, maximum n=100000. Runtime 17.98 s before plotting; peak process RSS 254443520 bytes. Six small graphs checked by exact rational visited-set DP plus 20000 Monte Carlo trials each. PNG and SVG plots saved and visually inspected. No candidate showed long survival beyond sqrt(n); numerical evidence is not a proof.

Literature limitations: Alon birthday draft is indexed under his old author URL, but all four old/current author-host paths tried returned 404; indexed excerpt only, not a verified full source. Semantic Scholar citation query returned 429. OpenAlex successfully returned cited_by_count=0 (record updated 2026-11-07); exact-ID/title web searches found no later mathematical citer resolving the conjecture. This does not establish completeness.

2026-11-13T09:56:35 — REPORT.md completed with first line PARTIAL, full bounded-ratio proof, explicit maximum-degree corollary, expected first-collision bound, source/gap corrections, literature table, computations and limitations. Added complete excluded-multigraph counterexample proof with minimum degree 4. Verified no saved PDFs/scans, source files decode as text, 351 CSV rows and maximum n=100000. Source-text SHA256 manifest saved. No publication or push.
