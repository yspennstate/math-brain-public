disk: small

Read ~/fei_solve_agent/FLOW.md first (sections 7, 9, 10). Scripts: the code folder beside it
(check_erasure.py computes all quantities; hill_rho.py is a truth-table hill climb already running elsewhere for
n = 6..10, do not duplicate it). Earlier record constructions: ~/codex_fleet/20261108_pro/workers (FEI R72 and PM(K33)
folders; grep for PMK33) and FEIB11, FEIB13.

Setting. f Boolean on n bits, mu = fhat^2, U ~ mu, I = E|U|, H = H(mu).
  E_i = H(1[i in U] | U - i);  H^- = sum_i E_i;  D_i = H(f) - H(f_{i->1})/2 - H(f_{i->-1})/2 = E_i + JS_i.
  Three constants: C* = sup H/I (>= 6.5218), C^- = sup H^-/I, R = sup_f min_i D_i/Inf_i. Proved:
  C^- <= C* <= C^- + 2/ln 2 and C* <= R <= C* + 2/ln 2. FEI <=> any of them is finite.

Task: find functions making H^-/I and min_i D_i/Inf_i as large as possible, by exact formulas rather than truth tables,
so that n can be large. If either grows without bound along a family, FEI is false; say so loudly and check it three ways.

1. Composition law. For f = F(g_1, ..., g_m) on disjoint blocks (and for F(g, ..., g)), derive exact formulas for
   H^-, E_i and D_i from the spectra of F and g (the spectrum of a composition with balanced or unbalanced inner
   functions is a known product formula). Verify against truth tables for small cases to 1e-12.
2. Evaluate on: tribes of every width and number of tribes (n up to 10^6 by formula); iterated majority; recursive
   3-majority and recursive tribes of depth up to 6; AND-OR trees; address functions; bent functions and bent with
   k points replaced by fresh dictators; PM(K33) (the record function) and its self-compositions, lifts and
   compositions with tribes, majority, AND_k; the complete-quadratic and Maiorana-McFarland families; functions
   of the form F(x) XOR g(y) and F(x) AND g(y). For each family: the limit or the growth of H/I, H^-/I and
   min_i D_i/Inf_i.
3. Optimise inside the families: for F(g_1..g_m) with F from the n <= 4 census (all 222 NPN classes) and g_j from
   AND_k, OR_k, MAJ_k, XOR_k, tribes, find the best two-level and three-level compositions for each of the three
   ratios. Report the top 20 of each with exact parameters.
4. Biased inner functions are the lever in the record (PM(K33) with dummies): scan F(g) with g = AND_k (bias
   1 - 2^(1-k)) and g = threshold functions, all F on <= 5 variables (NPN census file in FEIB11/FEIB13).
5. For the best functions found: list E_i/Inf_i for each coordinate orbit, and say which statistic of U - i predicts
   i (parity, block, level), in the sense of FLOW 10(c)-(d).

Deliverables: FORMULAS.md with proofs, scripts with outputs, RESULTS.md (ranked tables with exact parameters and
truth tables in hex where n <= 10), REPORT.md with one verdict line per item and the current best value of each of
the three ratios, LEARNINGS.md. Label every statement PROVED, CHECKED (scope) or OPEN. Write as you go.
Memory: each process under 3 GiB, at most 2 threads, nice 10.
