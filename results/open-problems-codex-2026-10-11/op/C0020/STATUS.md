STATE: DONE
NEXT: Future work: bound B_n(c), the trajectory-weighted drift deficit in SECOND_ATTEMPT.md (11), using critical square geometry; no further work scheduled in this attempt.
VERDICT: PARTIAL

2026-10-12: Source fetched and model corrected: expected zero-error single-bit query cost for critical triangular-site square crossings; printed p.90/PDF p.92.
2026-10-12: Queried arXiv, OpenAlex (source resolved; citing-works endpoint rate-limited), Crossref, Semantic Scholar (source and 118 citation records retrieved; keyword search rate-limited), and GitHub. No exact solution identified. The closely relevant 2024 paper explicitly calls the exponent open. This bounded search is not a proof of current openness.
2026-10-12: Proved an integer-valued refinement of the influence-square bound and an exact conditional-score-variance reduction; the correction is bounded and does not improve the exponent.
2026-10-12: Proved the 2x2 triangular rhombus optimum 5/2 by matching lower bound and explicit tree. Exact Bellman optima include 3x3 = 555/128 and 4x3 = 10685/2048. These are rhombus special cases, not the source square asymptotic problem.
2026-10-12: All 197 monotone truth tables on <=4 bits passed exact inequality checks. Finite Bellman steps and integer gap accepted by Lean 4 with kernel checking, exit 0 and no warnings; no sorry. Largest computational run used about 130 MiB.
2026-10-12: Attempt closed with the original exponent gap [3/2,7/4] unchanged. Full proofs, literature limitations, and remaining gap saved.

2026-10-12: Reopened for one serious additional attempt requested by the user.
2026-10-12: Additional attempt proved restriction moment identities, found a 3x3 counterexample to greedy optimality, and refuted universal drift and influence-based upper-bound shortcuts. Full Bellman certificate checked.
2026-10-12: Additional attempt complete, VERDICT PARTIAL. Selected maximum-conditional-pivotal construction from two new approaches; proved its finite nonoptimality and refuted uniform drift and universal influence-based upper bounds. All 19683 Bellman states checked; Lean pivotal counts accepted, exit 0; guarded largest job 557 MiB and 62 seconds. Remaining B_n(c) estimate unproved; interval [3/2,7/4] unchanged.
