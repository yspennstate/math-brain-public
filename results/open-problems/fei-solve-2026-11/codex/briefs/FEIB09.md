disk: small

Read ~/fei_solve_agent/NOTES.md and ~/fei_solve_agent/FLOW.md first.
The check scripts are in ~/fei_solve_agent/code (check_p.py, check_flow.py); write your own.

Task: the containment half, A1 <= C I, attacked level by level (FLOW.md sections 2 and 3).
Notation as in FLOW.md: g_R = D_R f, up(R) = E g_R^2, alpha(R) = E|g_R|, mu = fhat^2.
Define for r = 1, 2, 3, ... the truncated containment cost
    A_r(f) = E_{S~mu} log2( 1 / min{ up(R) : R subset of S, |R| <= r } ).
up is decreasing along inclusion, so A_r increases with r and A_r = A once r >= deg f. FLOW.md proves A_1 <= C I
(the level-1 theorem). The whole containment conjecture is "A_r <= C I with C independent of r".
1. Referee the proofs in FLOW.md section 2 (flow identity, generalized Talagrand, size statement, level-1 theorem)
   as a hostile reader; give the best explicit constant in the level-1 theorem and the function that needs it.
2. Compute sup A_r / I and balanced sup A_r/(I-1) for r = 1, 2, 3, 4 on all functions of at most 4 variables, on
   a large sample at 5..8 variables, and on tribes, majority, address, AND, parity times AND, bent functions, the
   18-variable matching gate with nine coins, and compositions. Does the supremum grow with r? Report the table and
   the extremal functions.
3. Prove A_2 <= C I, or find where it fails. The level-1 proof pays the small sets from the budget
   sum_i Inf_i = I; at level 2 the budget sum_{|R|=2} up(R) = E C(|U|,2) is too large (majority). Candidate repairs,
   to be decided by proof or counterexample: (a) charge a pair R = {i,j} only through its cheaper chain
   (up(i) -> up(ij)), using the conditional statement for g_i in place of f:
   sum_{S contains ij, |S| <= k+2} mu(S) <= 3^k ||D_j g_i||_{4/3}^2 and the budget sum_j ||D_j g_i||_2^2 =
   E[|U| - 1; U contains i]; (b) a pair pays only when it is the minimizing pair of S, and each S has at most
   C(|S|,2) pairs; (c) a fixed p-norm chain (p = 4/3) in place of L1 so that granularity never costs 2^r.
4. The cross-subsidy problem of FLOW.md section 3 as a linear program: on every function of at most 4 variables
   (and a sample at 5 and 6), unknowns w(U,S) >= 0 restricted to a parametrized family (functions of |U|, |S| and
   of quantized local data such as L(S) or up(S)/up(S - s)), constraints sum_{S in U} w(U,S) <= C|U| and
   mu(S) log(1/alpha(S)) <= C|S| mu(S) + sum_{U contains S} mu(U) w(U,S). Find the smallest C for which a universal
   rule in the family exists, and describe the rule; say which functions force C up.
5. If 3 succeeds, do r = 3 and look for the induction on r that keeps C fixed. If it fails, write the obstruction
   family and say what it implies for A itself.
Deliverables: PROOFS.md, scripts with outputs, RESULTS.md (the tables of 2 and 4), REPORT.md with a verdict line
per numbered item. Label every statement PROVED, CHECKED (numerically, with scope) or OPEN.
Memory: each process under 3 GiB, at most 2 threads, nice 10.
