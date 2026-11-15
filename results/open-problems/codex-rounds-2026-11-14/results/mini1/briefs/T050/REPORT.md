VERDICT: PARTIAL located a September 2026 preprint claiming planar exponential strict convexity; correctness not independently established

The literature check found OpenAI's *Strict convexity and differentiability of
the planar exponential first-passage limit shape* (September 24, 2026).
[The opened manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf)
states the relevant special case in Theorem 1.1. Reference, scope, and arXiv-ID
search outcome are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).

Following the requested literature-discovery stop branch, no new proof or
numerical computation was attempted. The general problem is not proved here.

The audit separated strict convexity from differentiability, exponential from
general Gamma laws, and dimension two from higher dimensions. The
[author's scope note](https://raw.githubusercontent.com/openai/math/main/lean/docs/212.md)
confirms that strict convexity is outside the selected Lean statements.
The full proof and the formalization's mathematical fidelity remain unchecked.

Commands, exact search queries, useful outputs, and failed fetches appear in
[LOG.md](LOG.md). No simulation command or numerical data exists. A requested
`nice -n 15` read printed `setpriority: Operation not permitted`; no heavy
programs were run. No git or external write was used.

Next worker: obtain and audit the preprint's strict-convexity argument in Part II,
especially Propositions 9.5 and 15.2 and the admissible path class they share.
Check for independent reviews or corrections before updating T050 to a proved
special case. Do not infer general Gamma strict convexity from differentiability.

Task: “push this problem forward by one checkable piece” — first recorded
2026-11-14 20:46:04 Asia/Tbilisi (16:46:04 UTC; receipt time not supplied).
