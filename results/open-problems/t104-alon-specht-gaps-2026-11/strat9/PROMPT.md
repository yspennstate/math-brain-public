You are working on one case of a graph inequality. Work in this folder only and write as you go: keep LOG.md current
after every step, and put the final write-up in RESULT.md. Label every statement PROVED (with an exact certificate and a
replay script), NUMERICAL or OPEN. Never present a numerical finding as a proof.

READ FIRST (read-only, do not modify): ~/agent_run/STRAT7/ - RESULT.md proves T >= 0 for every disconnected
six-vertex graph with D = 2 except one case: a connected five-vertex component carrying both top eigenvalues plus one
isolated vertex (5+1). It proves 5+1 for internal scale a <= 11/25 (scale_certificate.py) and gives the padding formulas:
X1 and S5 do not depend on the number N of isolated vertices, X2 = 2N B/(N - 2), X3 = (1 - lambda)[D(N - 1)(N - 4)lambda
- 2D(N - 2) + 2N h]/(N - 2)^2. terms.py there is the numerical reference (never a proof).
Also read ~/agent_run/STRAT6/RESULT.md: for N = 5 itself (no isolated vertex) the connected D = 2 stratum has the
radial reduction (R1) to the zero-weight face, moment inequalities (M1), 176 rational cells, and face boxes. The 5+1 case is
the same five-vertex graph with the N = 6 constants; reuse those tools with c = 2N/(N - 2) and beta = (1 - lambda)/(N - 2)
at N = 6.

THE QUANTITY: as in STRAT7/RESULT.md (W symmetric nonnegative, edge sum 1, L, lambda, D, Pi, G = lambda(I - J/N) - L,
X1, X2, X3, S5, T = X1 + X2 + X3 - 2 S5).

TASK
Prove T >= 0 for the 5+1 case at N = 6, beyond a <= 11/25. Suggested order:
1. Write T for 5+1 at N = 6 in the frame form of STRAT6 (u, w, r, a) using the padding formulas; check it numerically
   against terms.py on random frames.
2. Check whether the radial identity (R1) holds for the padded quantity (the projector is fixed along the ray), and if so
   reduce to the far end.
3. Prove as much as possible with moment cells and face boxes in exact rational arithmetic, each with a replay script.
4. State the remaining region exactly. Then, if the method allows, extend to N >= 7 with one isolated vertex added each time.
Keep memory under 4 GB and use at most 4 processes. No network and no language-model workers. Write only in this folder.
