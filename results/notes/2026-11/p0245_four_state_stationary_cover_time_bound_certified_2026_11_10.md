---
name: p0245_four_state_stationary_cover_time_bound_certified_2026_11_10
description: "[PROVISIONAL] P0245 (Aldous-Fill Open Problem 6.30, E_pi C >= (n-1)H_(n-1)) for n=4: Codex OPEN3 computer-assisted proof, certificate independently re-checked; n=5 numeric min 25/3 at K5"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T04:51:26+02:00
  status: provisional
  evidence: ""
---

OPEN3 (codex_local_1108/briefs/OPEN3, SOLUTION.md, 10 Nov 2026) proves every irreducible reversible 4-state chain has stationary cover time E_pi C >= 11/2, equality only for the simple walk on K4. Route: E_pi C - 11/2 = F/(2 W tau prod Delta_ij) with W the sum of degrees, tau the spanning-tree polynomial, Delta_ij the 2x2 Laplacian minors; F (degree 16, 13,368 terms, 2,421 negative) becomes coefficient-nonnegative after the ordered partial-sum substitution in each of the 30 orbit cones of edge orderings; an analytic argument adds holding.

Independent check by an agent (my own code, briefs/OPEN3/independent_check_agent): the identity holds in exact arithmetic at three random integer chains and K4; F is S4-invariant; all 30 cones nonnegative (python-flint compose, 3 s; sympy rings ~500 s a cone). The holding extension was NOT re-derived, only checked numerically (minimum 5.5 with holding). n=5 Nelder-Mead probe on worker machine 1: minimum exactly 25/3 at K5, none below.

**Why:** a standing rule to use Codex on open math problems; prior record had n=2 and an internal n=3.
**How to apply:** status computer-assisted n=4, external audit zero, priority unestablished; before any paper, re-derive the holding step by hand and search the literature for an n=4 result. Fast cone checks: python-flint fmpz_mpoly compose, not sympy expansion.
