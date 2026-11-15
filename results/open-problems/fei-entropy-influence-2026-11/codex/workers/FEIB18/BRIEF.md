# Worker FEIB18 (account acc2)

disk: small

Read ~/fei_solve_agent/FLOW.md first, all of it; section 11 states this task (section 7 is
what it rests on). Scripts: the code folder beside it (ltf_level.py, ltf_product.py, ltf_cross.py,
lemmaA_check.py, ol_check.py, hazard.py). Earlier proofs: ~/codex_fleet/20261108_pro/workers/FEIB10, FEIB12,
FEIB14, FEIB17 (PROOFS.md in each).

You are the referee of section 11: a claimed proof that H(f) <= C I(f) for every linear threshold function, by
restricting the coordinate of largest weight. Assume it is wrong somewhere and find where.

Part 1. Line by line. For each of 11(a), (b), (c), (e), (i), (j), (k) and the theorem at the end: restate the
claim in your own words, check every inequality and every case split, and give one of PROVED / GAP (say exactly
which step and what is missing) / FALSE (with a counterexample you computed). Points to press on:
  - (c) the two-sequence lemma: the dyadic grouping, the use of superadditivity, the constant, levels with
    beta_k = 0, and whether the hypothesis is needed at K = 0;
  - (e) the passage from level weights to noise stability: both displayed bounds, the choice of rho for K = 1 and
    K >= 2, the identity E f0^2 - Stab_rho(f0) = P[y not in S, z in S] + 2 Cross, the constant 6.33;
  - (i) Lemma A: the induction, every case of (-), closed against open intervals, ties, weights equal to a;
  - (j) Lemma B: the stopping time, the use of Levy's inequality, the 1/8, the covering count;
  - (k) Cross-Stay: independence of T and y, the conditioning on (T, A), the symmetry step, the
    Kolmogorov-Rogozin constant (give an explicit admissible K_0 with a reference or a proof), the Chernoff step,
    and the final supremum (compute an explicit M_cs and the explicit final C).
  - the setting: "no ties" and "delta = 0 implies constant"; thresholds with zero weights; n = 1, 2.

Part 2. Attack by computation. Exact enumeration on rational weight grids (n <= 16), integer weights with ties
removed by a small shift, weights with one or two heavy coordinates, geometric weights with ratio near 1 and
near 2, and thresholds from 0 to 4 standard deviations: the largest observed values of the Lemma A ratio, the
Lemma B ratio, Cross Stay / delta^2 over rho, M = max_K A_{>=K} B_{<=K} / delta^2, and L_1 / Inf_1. Report any
value above the proved bound at once and stop to recheck.

Part 3. If the proof stands: the shortest complete write-up of the theorem with all constants explicit, in the
form of a paper section (statement, lemmas, proofs), plain mathematical prose, no account of how it was found.
If it does not stand: the smallest repair, or the exact statement that is still open.

Deliverables: REFEREE.md (one verdict line per item of Part 1, then the details), PROOFS.md (Part 3; each
statement marked PROVED / CHECKED with scope / OPEN), scripts with their outputs, REPORT.md with one verdict line
per part, LEARNINGS.md. Write as you go. Memory: each process under 3 GiB, at most 2 threads, nice 10.

