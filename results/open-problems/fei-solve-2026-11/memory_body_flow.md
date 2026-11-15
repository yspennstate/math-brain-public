FEI in L1 form: what exactly is open, and what did the first Codex round prove? (an agent, 9 Nov 2026, loop T-20261109-026.)

Answer: H = 2 A1 + 2 Gamma exactly, so FEI holds iff A1 <= C I and Gamma <= C I, and equivalently iff P <= C I and Gamma <= C I.
g_S = D_S f (the S-coefficient with the outside fixed), alpha(S) = E|g_S|, up(S) = E g_S^2, p(S) = P[g_S != 0], mu = fhat^2.
A1 = sum mu log(1/alpha), Gamma = sum mu log(alpha/|fhat|), P = sum mu log(1/p), A = sum mu log(1/up), B = H - A.
Proved, and checked on all 4-variable functions and 6-variable samples (code/check_p.py, check_flow.py):
- A1 <= A <= 2 A1; B <= A + 2 Gamma; 2P + 2 Gamma <= H <= 2P + 2 Gamma + 3(I - Var).
- A1 >= Var log(1/max Inf), so A1 <= C I contains KKL. P-conjecture in words: for a spectral sample S the restriction of f to S
  has full degree with probability 2^(-C|S|) on log-average; Gamma: its top coefficient keeps a sign bias 2^(-C|S|).
- Isoperimetric step 2 p(S) log(1/p(S)) <= sum_{j not in S} p(S+j). Level form B <= sum_d W_d log(E C(|U|,d)/W_d): right for
  majority, loses log I on tribes.
- Chain flow: m(R) = sum_{S contains R} mu(S)/C(|S|,|R|), sum_R m(R) = I + 1, A1 = sum_R m(R) x (mean last-step cost into R).
  Generalized Talagrand: m(R) <= up(R) min(1, r!/L^r), L = ln(||g_R||_2/||g_R||_1); r = 1 is Talagrand's inequality.
- Level-1 theorem: E_S log(1/min_{i in S} Inf_i) <= C I (hypercontractivity: P[S contains i, |S| <= k] <= 3^k Inf_i^(3/2)).
Where it stops: at level r >= 2 the budget sum_{|R|=r} up(R) = E C(|U|,r) is too large; the same count is what costs KKLMS
their log. Needed: a cross-subsidy rule from large sets U to their subsets that uses local data of f (FLOW.md section 3).

Codex round 1 on Mac mini 1 (FEIB01, 03, 04; reports in codex/workers/, my independent check code/check_workers.py):
- Composition with balanced inner gates on disjoint blocks: X(f o g) = X(f) + sum_j Inf_j(f) X(g_j) for X = A, B, Gamma, A1.
  So each constant has sup_all X/I = sup_balanced X/(I-1), and towers cannot raise a ratio above the best single gate.
- Majority: alpha(S) is the same for every nonempty S, Gamma = H/2 + log2(alpha), Gamma/I -> 1/ln 2 = 1.4427. So the Gamma
  constant is at least 1.4427 and majority's entropy is all cancellation (A1 = log(1/alpha) is about (1/2) log n).
- The 18-variable record gate (matching on K33 with nine coins, H/(I-1) 6.5218): A = 4.361829, I = 261/128,
  A/(I-1) = 4.197851. Largest balanced Gamma/(I-1) found through n = 20: 1.0279.
- Dead routes with witnesses: constant payment per coordinate in a restriction induction for A (a bent function in one slice,
  one flipped point in the other: Delta_i A / Inf_i grows like m); A <= C log(1/Pr[S inside U]) (mux-address family);
  charging each later reveal of Gamma to its own influence (exponential ratio); Gamma = 0 for unate functions (false).
- Theorem 1's factor 2 on I is sharp (iterated q = (x1x2 + x2x3 + x3x4 - x1x4)/2 has B = 0, A/I -> 2).
None of this bounds the FEI constant; both conjectures are open.

Where: brain-repo/06_math_research/fei_solve_2026_11_09/ (FLOW.md, STATE.md section 2c, code/, codex/workers/).

Related: [[fei_splits_into_containment_and_cancellation_n5_census_2026_11_09]] [[fei_solve_plan_up_ratio_form_h_le_2b_plus_2i_2026_11_09]]
[[fei_public_lower_bound_record_is_numaro_6_5218_not_hod_2026_09_22]]
