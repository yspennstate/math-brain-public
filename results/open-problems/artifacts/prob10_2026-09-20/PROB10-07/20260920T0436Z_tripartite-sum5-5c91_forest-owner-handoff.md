# PROB10-07 non-mutating handoff to forest-owner history

This file does not edit or seize P14/HARD10-01/NM13 claims. It records the complementary PROB10-07 structural-family delta for readers of the parent forest-conjecture history.

Consumed owner/history pointers:

- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md` — P14 all-graphs metric 9 and 3-connected residual obstruction.
- `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md` — HARD10 forest handoff after two recovery cycles; all-graphs metric 9.
- `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md` — superseded Boolean-Komlos state preserved before PROB10-07 refocus.
- newest same-parent neighboring follow-up read this run: `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T04-18-30Z__triangle-matched-right-sign-theorem.md`; its `K_3 join (M_k disjoint_union I_r)` theorem is a different graph family/transfer algebra.

PROB10-07 new restricted theorem proved in this run:

For every `n>=1`, uniform forests have strict pairwise negative edge correlation on each of

- `K_{1,3,n}`;
- `K_{2,2,n}`;
- `K_{1,4,n}`;
- `K_{2,3,n}`.

Combined only with PROB10-07's immediately preceding `K_{1,2,n}` theorem (and trivial/known smaller layers), this gives a repository structural-family corollary for complete tripartite graphs whose two smallest part sizes have sum at most five. This is PARTIAL on Grimmett-Winkler: it does not move the complete-all-graphs order-nine metric and does not prove arbitrary complete tripartite graphs.

Mechanism: exact Bell-partition transfer on the fixed `m=a+b` terminals, `M_m=(m+1)I+N_m`, `N_m^m=0`, followed by exhaustive edge-pair orbit reduction. Across the four new families there are 44 orbits. Every normalized Rayleigh polynomial has nonnegative exact rational coefficients and is strictly positive on its physical domain. The standard-library checker also brute-force regresses `n=1,2` against direct enumeration of all forest subsets.

Artifacts:

- idea-before-code: `artifacts/prob10_2026-09-20/PROB10-07/20260920T0436Z_tripartite-sum5-5c91_idea.md`;
- checker: `artifacts/prob10_2026-09-20/PROB10-07/20260920T0436Z_tripartite-sum5-5c91_checker.py`;
- executed output: `artifacts/prob10_2026-09-20/PROB10-07/20260920T0436Z_tripartite-sum5-5c91.out`.

Universal source status remains OPEN/PARTIAL. Novelty/priority of the restricted complete-tripartite theorem remains UNVERIFIED after bounded repository/public searching; no priority claim is made.
