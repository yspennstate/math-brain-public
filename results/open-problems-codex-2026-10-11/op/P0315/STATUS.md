STATE: DONE
NEXT: Prove a uniform smoothing estimate for P_(r/2,r) applied to the cusp observable, or a sharper observable-specific cancellation, to obtain o(r^(-2)) and ultimately oscillatory amplitudes.
VERDICT: PARTIAL
2026-10-11: Fetched Dumaz-Malvy and verified the fixed-beta continuous pair-density target and density conventions.
2026-10-11: Queried arXiv, Crossref, OpenAlex, Semantic Scholar, and GitHub; OpenAlex and Semantic Scholar remained HTTP 429. No full solution verified; literature search coverage is incomplete.
2026-10-11: Checked Qu-Valko Theorem 3: it is a pointwise upper bound, not exact leading asymptotics. Found July 2026 beta=6 expansion and October 2026 tail-triviality paper; neither solves general beta.
2026-10-11: Proved density rescaling, beta=2 exact formula, beta=1 and beta=4 explicit remainder expansions, formal nonoscillatory coefficient recurrence, necessary formal harmonic exponents, and weighted Fourier tail bound.
2026-10-11: Identified a missing beta=1 sine descendant in Lewin (148) and insufficient literal truncation in (149); neither is a counterexample to the intended full family.
2026-10-11: Fifteen high-precision classical remainder checks passed. Finite coefficient cancellation passed Lean 4 with exit code 0; no sorry or native_decide.
2026-10-11: Attempt concluded with precise general-beta analytic gap in ATTEMPT.md. No complete proof or counterexample to P0315 claimed.

2026-10-11: Reopened at user request for a second serious attempt; comparing two new reductions.
2026-10-11: Second attempt compared finite even-beta normal forms with synchronous circle-diffusion contraction; pursued contraction after targeted read-only brain queries.
2026-10-11: Proved a new decay bound from exact observable plus finite-density Duhamel: kappa=2-4beta for beta<=1/3, or (1-beta)^2/(2beta) for 1/3<=beta<1; improves the recorded Qu-Valko bound for beta<1/2. No novelty priority asserted.
2026-10-11: Proved uniqueness in the normalized positive-definite probability-valued moment-hierarchy class for beta<1, and actual fixed-mode inverse-square asymptotics for beta<3-2sqrt(2).
2026-10-11: Exact second- and third-density residuals passed symbolic checks; 33800 angular generator checks and eight positivity grids passed. Generator inequality passed Lean 4 with exit 0.
2026-10-11: Second attempt finished. Full P0315 remains unproved: Holder-beta cusp prevents summing fixed-mode estimates, global contraction fails for beta>=1, and oscillatory amplitudes/remainders remain unidentified. Details and full proofs in SECOND_ATTEMPT.md.
