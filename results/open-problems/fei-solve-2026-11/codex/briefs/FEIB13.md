disk: small

Read ~/fei_solve_agent/NOTES.md and ~/fei_solve_agent/FLOW.md first
(sections 3, 3b and 5(e)-(f) of FLOW.md state this task).
The check scripts are in ~/fei_solve_agent/code (check_p.py, check_flow.py, check_feib09.py); write your own.

Task: uniform-in-level containment. f Boolean (+-1), g_S = D_S f, mu(S) = fhat(S)^2, up(S) = E g_S^2,
p(S) = P[g_S != 0], P = E_{S~mu} log2(1/p(S)), A = E_S log2(1/up(S)), P <= A <= P + 2(I - Var).
Known: fixed level r costs a factor r (FLOW section 3, FEIB09). Wanted: P <= C I with C absolute.

1. Sparse-set split. For K > 0 put Sp_K(f) = sum over S with p(S) < 2^(-K|S|) of mu(S) log2(1/p(S)); then
   P <= K I + Sp_K. Compute sup Sp_K/I for K in {1, 2, 3, 4, 6} on the n <= 5 NPN census, a 6- and 7-variable
   sample, tribes (several widths), majority, AND, address functions, PM(K33), and
   MUX(AND_L(y); g(x); parity) examples. Is there a K with Sp_K <= C I on everything tried? Which S carry Sp_K?
2. Conjecture T (FLOW 3b): R_t = the elements of S ~ mu whose independent uniform label is below t.
   Compute E log2(1/p(R_t))/I for t in {1/4, 1/2, 3/4, 1} on the same families. Then try to prove T(1/2): the known
   pieces are P[R_t = R] = t^|R| F_R(1-t) and, from the level inequality, F_R(1/2) <= 2 up(R) p(R)^(1/10); what is
   missing is a budget, i.e. a bound on the number (or total weight) of sets R with p(R) about 2^(-l). Find the right
   weighted count: test numerically which of
       sum_R t^|R| up(R) p(R)^(-theta) [restricted to |U| <= M],   sum_R tau_t(R) p(R)^(-theta),   theta in (0, 1/2],
   stay below 2^(C I) on the families above, and prove the best one.
3. Conjecture W: sum over nonempty S of mu(S) c^(-|S|) / up(S) <= Var * K^(I/Var) for absolute c, K. Test on the
   same families (tribes first); if false, find the weakest true exponential-moment statement of this shape
   (replace 1/up(S) by up(S)^(-theta), theta < 1). Any true statement of this kind gives containment by Jensen.
4. A reference measure for all levels at once. Containment follows from any sub-probability pi on sets with
   sum_S mu(S) log2(1/pi(S)) <= C I and up(S) >= pi(S) 2^(-C|S|) on the sets that carry the cost (state the exact
   form you use; a rule S -> R(S) subset of S that keeps a constant fraction of S may replace S on the left). FEIB09's product pi costs the factor r. Try pi built from the
   function: the thinned laws tau_rho (FLOW 5(c)), their mixtures over rho, Markov-chain references
   pi(R) = prod_j P[U contains r_j | U contains r_1..r_(j-1)] with the order chosen by decreasing influence.
   Report which pi give bounded ratios on tribes AND majority simultaneously (these two pull in opposite directions).
5. Anything proved here should be stated for P and for A, with constants.

Deliverables: PROOFS.md, scripts with outputs, RESULTS.md (tables, extremal truth tables in hex), REPORT.md with a
verdict line per numbered item. Label every statement PROVED, CHECKED (numerically, with scope) or OPEN.
Memory: each process under 3 GiB, at most 2 threads, nice 10.
