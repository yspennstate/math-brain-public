What is the plan for solving FEI in the 9-19 Nov loop, and what is new? (an agent, his 9 Nov 22:20 and 22:2x orders.)

The plan and its NEXT line live in brain-repo/06_math_research/fei_solve_2026_11_09/STATE.md. Read that first.

New on 9 Nov: the up-ratio form. With mu(S) = fhat(S)^2 and up(S) = sum over U containing S of mu(U) = E[(D_S f)^2], put
A = sum mu(S) log(1/up(S)) and B = sum mu(S) log(up(S)/mu(S)); H = A + B exactly.

Theorem 1: for Boolean f, A <= B + 2I - 2Var, so H <= 2B + 2I - 2Var. Proof: D_S f is the S-coefficient of f on an
|S|-dimensional subcube, an integer multiple of 2^(1-|S|), so |fhat(S)| <= E|D_S f| <= 2^(|S|-1) up(S); take logs and sum
against mu. Since B <= H, FEI holds if and only if B <= C' I for all Boolean f (C <= 2C' + 2).
Checked on all 65,536 functions of 4 variables (largest violation 4e-16, equality attained) and 1.1M random functions on 5-7
variables. On AND_n, B = I while H = 4I. Largest B/I seen: 1.5108. The 6.5218 record forces sup B/I >= 2.26.

Lemma 2 (coding): for fixed 0 < lam < 1, B <= B_lam + I log(1/(1-lam)) with B_lam = E_{S~mu} log(1/E[lam^|U-S| given U contains S]).
Lemma 3 (recursion): B(g) = B(E_i g) + B(D_i g) + J_i(g), J_i(g) = sum_S ahat(S)^2 log(1 + up_d(S)/up_a(S)), a = E_i g, d = D_i g.
Composition: B(f o g) = B(f) + I(f) B(g) for balanced g.

The idea: Theorem 1 removes the granularity half of FEI and leaves B, the log-dispersion of the top coefficient of a random
restriction. Bound B through the recursion with a potential, as the read-once and symmetric proofs bound H; the entropy of
"is i in S", which killed the H induction, cancels inside B. If B <= C' I is false, a counterexample must have restricted
coefficients whose mean is 2^(-omega(|S|)) below their root mean square for spectral-typical S: a design rule for the search.

Not yet known: whether Theorem 1 is in the literature (KKLMS 2020 works with the same derivative quantities; peer
an agent was asked to check), and whether B <= C' I is any easier than FEI. Do not cite it as progress on the
constant. A first guess with -2 in place of -2Var was false on 4 variables; the code that caught it is code/verify_forms.py.

Lines: A prove B <= C' I (census on 5 variables, symmetric closed form, read-once, potential LP); B disprove or raise the
lower bound with the dispersion rule; C Codex workers (referee, symmetric B, potential LP, the LM lemma of FEI25); D brain
(one memory and one card per result, the math-store FEI gap).

Related: [[fei_is_one_inequality_over_gates_and_and_is_the_binding_one_2026_09_22]] [[fei25_fei26_lm_tight_m_to_1_no_proof_no_counterexample_2026_11_09]]
[[fei_package_checked_induction_step_needs_a_growing_constant_2026_09_20]] [[symmetric_fei_best_constant_4p650431_v4_1_repo_23b66aa_2026_11_09]]
[[math_store_missed_fei_results_queue_unruled_2026_11_09]] [[t021_fei_dossier_written_li_han_2512_03117_is_withdrawn_2026_11_03]]
