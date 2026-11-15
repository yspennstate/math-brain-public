account: acc2
disk: small

# FEIB20 - the nested witness over ALL orders on the tree DNF: a bounded order, or a log D lower bound

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Read ~/fei_solve_agent/FLOW.md sections 7, 12 (head, (b), (l)), 12(o) and 12(p) first; the code is
~/fei_solve_agent/code/tree_dnf.py (run `python3 tree_dnf.py selftest`; use
`export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH` for a python3 with numpy).

Definitions. f Boolean (+-1) on n bits, mu(S) = f^(S)^2, U ~ mu. For a coordinate i:
E_i = H(1[i in U] | U - i) = sum_T Phi(g^(T)^2, h^(T)^2), g = E_i f, h = D_i f, Phi(p,q) = (p+q) h2(p/(p+q)).
FEI is equivalent to: every Boolean f has a coordinate with E_i <= C Inf_i (FLOW 7).
Nested witness for an order pi of the other coordinates (pi reveals coordinates one at a time): K(U) = the LAST
revealed element of U - i (or "none"); L^pi_i = H(1[i in U] | K(U)) >= E_i. Resampling form (FLOW 12(l)): with R_j =
the last j coordinates of the order, W(R) = E h(x) h(x^R) = P[i in U, U misses R], V(R) = E g^2 - E g(x) g(x^R),
and L^pi_i = sum_j Phi(V(R_j) - V(R_{j-1}), W(R_{j-1}) - W(R_j)) + Phi(P[i not in U, U - i empty], P[U = {i}]).
The conjecture FWC said: sup_f min_{i,pi} L^pi_i / Inf_i < infinity.

What is known (FLOW 12(p), measured with tree_dnf.py). Tree model: root x; D blocks of L = w - 1 mates z; each
mate carries Q_z = OR of D - 1 disjoint ANDs of width L on fresh variables;
f = [x and OR_t AND_{z in t} z] or OR_z [z and Q_z]. In the balanced regime D^2 L 2^-L ~ 1.4:
E_root/Inf -> 2 (2.26, 2.13, 2.05, 2.02, 2.00, 1.99 for w = 10, 12, 14, 16, 20, 24) while the nested witness with
the mates revealed LAST grows like log2 D + 1.5 (6.4 ... 12.9). Conditioning on the last two revealed mates
instead of one gives about 3.0 in round-robin order.

Your job: settle the nested witness (window 1) on this family over all orders and all coordinates.
1. Extend the closed forms to orders that interleave leaves (the variables of the Q's) with mates: you need the
   block resampling moments when some leaves are resampled too. Everything is still a product over blocks and,
   inside a block, over mates; a mate's state is (z resampled or not, which of its D - 1 clauses have how many
   leaves resampled). Validate against brute-force truth tables on small cases (w = 3, D = 2 has 13 variables;
   w = 3, D = 3 has 31 - use w = 4, D = 2 with 22 variables as the second case), the way selftest does.
2. Evaluate L^pi_root / Inf for: leaves first then mates (done), mates first then leaves, clause by clause,
   block by block with each block's leaves next to its mates, and a random order; rows w = 10, 12, 14, 16 in the
   balanced regime. FLOW 12(o) predicts about (1 - c) log2(1/Inf) for mates-first; check it.
3. Do the same with i = a mate and i = a leaf (the function is not symmetric; the witness only needs ONE good
   coordinate). A leaf sits in one clause of one Q; its E_i/Inf_i and its best nested witness matter as much as
   the root's.
4. On small instances with exact truth tables (n <= 22), hill-climb over orders for every i and report
   min_{i, pi} L / Inf against min_i E_i / Inf_i; ~/fei_agent-style code exists on the other Mac only, so write
   your own short version (Walsh-Hadamard on 2^n, then group spectrum by last revealed element).
5. Then either (a) give an order family and a coordinate with L/Inf bounded as D grows, with the computation, or
   (b) prove a lower bound L^pi_i / Inf_i >= c log D for every i and every order on this family (or on a D-regular
   linear-hypergraph DNF), stating exactly what is proved and what is assumed. A proof sketch with the gap named is
   worth more than a claim.

Rules for this brief: 2 threads, nice 10, under 3 GiB a process; keep the folder under 200 MB. Report every number
with the command that produced it. Label anything not proved as heuristic. Write RESULTS.md as you go and finish
with REPORT.md (what is proved, what is measured, what is open).
