# C0034: an exact finite rank-two special case

Status: proof of a special case, awaiting w347's blind audit. No general solution or novelty claim.

Let E be finite and u,v be orthogonal unit vectors in C^E. The rank-one projection laws choose singleton {i} with probabilities a_i=|u_i|^2 and b_i=|v_i|^2. The rank-two law for span(u,v) chooses {i,j} with probability q_ij=|u_i v_j-u_j v_i|^2, for i<j.

There is a coupling of these two singleton laws with disjoint sets and union law q. To construct it, distribute each edge mass q_ij between its endpoints, giving vertex i total mass a_i. This is a finite flow network: source-to-edge capacities q_ij, edge-to-its-two-endpoints capacities 1, and endpoint-to-sink capacities a_i. A unit flow exists exactly when every subset A of vertices can absorb its internal edge mass: sum_{i<j in A} q_ij <= sum_{i in A} a_i. This is the capacitated Hall condition, or equivalently the max-flow min-cut condition. Total source and sink capacity are both one.

The required inequality is explicit. Put U_A=sum_A |u_i|^2, V_A=sum_A |v_i|^2 and c_A=sum_A u_i conjugate(v_i). Expanding the determinant gives sum_{i<j in A} q_ij=U_A V_A-|c_A|^2 <= U_A, since V_A<=1. Thus all cuts pass.

Given the unit flow, sample an edge {i,j} with law q and select its first endpoint according to the two flow portions. Call that singleton X_1; call the other endpoint X_2. The first marginal is a. Expanding and using global orthogonality gives sum_{j != i} q_ij=a_i+b_i. Consequently the second marginal is (a_i+b_i)-a_i=b_i. The union marginal is q by construction. Zero capacities cause no difficulty; an edge with q_ij=0 is never sampled.

The previous ledger C0034-A002 correctly says that its floating-point LP feasibility was not an exact certificate. This proof supplies a constructive exact certificate for the finite rank-two case. It does not settle arbitrary higher ranks, because one-vertex inclusion probabilities do not determine a larger subset's law.

A broader EXISTING-THEOREM reduction is available when either summand has rank one and the other has finite rank. Lyons's cached Theorem 2.7 says that projection laws are stochastically ordered by subspace inclusion; Strassen gives a coupling X_other subset X_H. The difference has size one. At every i its inclusion probability is P(i in X_H)-P(i in X_other), the diagonal of the rank-one complementary projection. These probabilities determine the law of a singleton. Thus the difference has the required rank-one law. This is a short consequence of the published domination theorem, not a new general solution. The flow proof above makes the both-rank-one construction explicit without relying on determinantal stochastic domination.

Measured checks: checks.py produced and independently replayed 64 rational certificates, checked 2,580 subset inequalities exactly, and found a rational naive-splitting counterexample with marginal total variation 0.1136890368. The exact vectors and fraction are saved in measurements/C0034_naive_counterexample.json.

The separate higher_rank_certificates.py goes beyond the singleton special case as EXACT EVIDENCE, not a theorem. It produced eight rational feasible couplings for rank-2 plus rank-2 projections in dimensions five and six. The float LP was used only to propose a support; a rational linear solve and independent Gram-determinant replay verified nonnegative masses and all three marginals with exactly zero residual. The eight certificates are in measurements/C0034_higher_rank_certificates.jsonl. Finite examples do not establish the general conjecture.

Checks run: exact orthogonality and normalization; all cut inequalities; nonnegative rational flows; all three marginals; zero-coordinate boundaries; a counterexample to the naive conditional splitting rule. The real rational cases are executable in checks.py; the proof itself also covers complex vectors. A blind proof audit must independently check the capacitated Hall direction and the second marginal. Higher-rank replay must use exact arithmetic.

Cached primary source: Russell Lyons, *Determinantal probability: basic properties and conjectures*, arXiv:1406.2707 (2014), Theorem 2.7 and Question 2.8. Local text: Downloads/Probability_1000_intake_claude_20260907/sources/lyons_determinantal_2014/text.txt:337-350. The general question is open in that cached source; no later disposition was verified.

Source target: ~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl:34, "Given H = H_1 (+) H_2 orthogonal in l^2(E), is there a coupling ... whose union has law P_H?" Prior attempt: attempts.jsonl:116, "Feasibility asserted to solver tolerance only; exact rational verification is the next step."
