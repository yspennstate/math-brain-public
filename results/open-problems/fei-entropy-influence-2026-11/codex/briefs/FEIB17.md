disk: small

Read ~/fei_solve_agent/FLOW.md first, all of it; sections 7, 9 and 10 state this task. Scripts:
the code folder beside it. Earlier proofs: ~/codex_fleet/20261108_pro/workers/FEIB10, FEIB12 (PROOFS.md in each).

You are a referee and then a prover.

Part 1 - referee FLOW sections 7, 9 and 10 line by line. For each displayed claim give a full proof or a
counterexample, and a numerical check (all 4-variable functions; samples at n = 6..8):
 (a) D_i = E_i + JS_i with 0 <= JS_i <= (2/ln 2) Inf_i, and whether 2/ln 2 is sharp;
 (b) the path formula H(f) = E_path sum_k D_{i_k}, I(f) = E_path sum_k Inf_{i_k} for any decision-tree order, and
     the two brackets  sup H^-/I <= C* <= sup H^-/I + 2/ln 2  and  C* <= R <= C* + 2/ln 2;
 (c) G <= H^- <= G + I/ln 2 with G = E_U sum_{i in U} log2(1 + mu(U - i)/mu(U));
 (d) the edge-law identity G = I [log2(n/I) - KL(P||Q)] of 9(d): check the definition of Q and the constant;
 (e) the pair form of 9(b), including the error term (log2 3 + 1/ln 2) delta;
 (f) the example of 9(c) (bent of majorities with one point replaced): compute E_i/Inf_i exactly by the product
     formula for m = 2, 4, 6 and suitable r, and confirm that i is the unique coordinate of largest influence;
 (g) the complex unimodular example of 9(e);
 (h) the block-witness bound of 10(d), with the exact two-cell formula.
 Report every error, however small, with the corrected statement.

Part 2 - prove something new in the general case. Target, in order of ambition:
 1. H^- <= C I log(I + 2) for Boolean f, proved in the edge or vertex form of section 10 (not by quoting KKLMS);
    or at least H^- <= C I^2. Input allowed: hypercontractivity, the level-k inequalities, KKL, Friedgut, Talagrand.
 2. Use what is special to real Boolean f. With f = f0 + x_i f1 on the other variables: f0 f1 = 0 and
    f0^2 + f1^2 = 1 pointwise, so the coefficient vectors a = f0hat, b = f1hat satisfy a*b = 0 and a*a + b*b = delta_0
    (convolution over symmetric difference), for every i at once. Find an inequality on
    sum_T b_T^2 log2(1 + a_T^2/b_T^2), summed over i, that uses these relations for all i together and fails for
    the complex example. Test every candidate numerically before proving.
 3. The vertex form: for g = f chi_T the ratios rho_i = (ghat(i)/ghat(0))^2 are level-one data of a Boolean
    function relative to its mean. Is sum_i rho_i log2(1 + 1/rho_i) <= C (1 + sum_i rho_i) + (something that sums
    to O(I) over T ~ mu)? Find the right correction term by an LP on the n <= 5 census, then try to prove it.
 4. If you believe FEI is false, describe the spectral structure a counterexample must have (which edges are steep,
    how many, at which levels) as sharply as the proved constraints allow.

Deliverables: REFEREE.md (Part 1, one verdict per letter), PROOFS.md (Part 2; PROVED / CHECKED with scope / OPEN),
scripts with outputs, REPORT.md with one verdict line per item, LEARNINGS.md. Write as you go.
Memory: each process under 3 GiB, at most 2 threads, nice 10.
