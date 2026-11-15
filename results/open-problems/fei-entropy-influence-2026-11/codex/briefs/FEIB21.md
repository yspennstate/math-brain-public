account: acc2
disk: small

# FEIB21 - prove the tree-DNF facts, then find what breaks a fixed window

Launched by an agent (laptop) for the author's 9 Nov 22:20 ask: solve the Fourier Entropy-Influence
conjecture. Read ~/fei_solve_agent/FLOW.md sections 7, 12 (head, (b), (i), (l)), 12(o) and 12(p) first; code
~/fei_solve_agent/code/tree_dnf.py and mc_chain.py (`export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH`).
Earlier Codex reports on the same line: ~/codex_fleet/20261108_pro/workers/FEIB18 and FEIB19 (REPORT.md, PROOFS.md).

Setting. f Boolean (+-1), mu(S) = f^(S)^2, U ~ mu, g = E_i f, h = D_i f, delta = Inf_i.
E_i = H(1[i in U] | U - i) = sum_T Phi(g^(T)^2, h^(T)^2); FEI <=> every f has a coordinate with E_i <= C delta.
Equivalent per coordinate (FLOW 12(p)): D(nu_h || mu_-i) >= log2(1/delta) - C, nu_h = h^^2/delta, mu_-i = g^^2 + h^^2.
Window witness: fix an order of the other coordinates; S_r(U) = the last r revealed elements of U - i;
L^r_i = H(1[i in U] | S_r(U)); L^1 >= L^2 >= ... >= E_i. L^1 is the "filtration witness" of FLOW 12.

Measured (tree_dnf.py; model in its docstring; balanced regime D^2 L 2^-L ~ 1.4, L = w - 1):
    w   D     E_root/Inf   L1/Inf   L2/Inf (round robin)   L3/Inf
    10  8     2.260        6.42     3.11                   2.64
    12  16    2.127        7.39     3.17                   2.44
    14  30    2.051        8.28     3.13                   2.29
    16  55    2.023        9.15     3.06                   2.19
    20  196   1.997        10.99    3.00                   2.12
    24  712   1.995        12.86    2.96                   2.08
(mates revealed last; leaves before them). The heuristic explanation is FLOW 12(o).

Tasks, in this order.
1. Prove, for the tree model in the balanced regime, with explicit error terms:
   (a) E_root/Inf_root -> 2 (identify the limit; is it exactly 2?), (b) L^1_root/Inf_root = log2 D + O(1) for the
   round-robin order with mates last, (c) L^2_root/Inf_root = O(1) for that order, and the limit if you can.
   The spectrum is a tensor product over blocks: with N_t = prod_z (1 - z Q_z), A_t = prod_z z, N = prod N_t,
   M = prod (1 - A_t) N_t (0/1 values), g = N + M - 1 and h = N - M up to sign. Check each formula numerically
   against tree_dnf.py before relying on it.
2. Generalise honestly: for which monotone DNFs does the same proof give E_i <= C Inf_i for some i? Aim at:
   width-w terms, every variable in at most D terms, any two terms sharing at most one variable (linear
   hypergraph), D 2^-w small. State the theorem you can actually prove and its constant. Check the brain and the
   literature first for what is known: read-k DNF bounds (our 23 Sep 2026 read-k DNF FEI bound, constant grows
   with k; Shalev; Arunachalam-Chakraborty-Koucky-Saurabh-de Wolf arXiv:1809.09819; Wan-Wright-Wu arXiv:1312.3003;
   Kelman-Kindler-Lifshitz-Minzer-Safra arXiv:1911.10579). Attribution in one neutral clause; never call a class new
   without that check.
3. Find what breaks a fixed window. For each fixed r, look for Boolean functions with min over i and over orders
   of L^r_i / Inf_i unbounded although FEI is not threatened: candidates are DNFs whose terms share many variables
   (D 2^-w not small, k_0 of FLOW 12(o) growing), the unbalanced tree row (w 9, D 24: L2/Inf 6.5), iterated trees
   of depth 3 and more, and compositions. Use exact truth tables up to n = 22 and the tensor-product formulas
   beyond. If a fixed r cannot work, say what the right statistic is (a window that grows with the local structure;
   the block witness H(1[i in U] | U cap B) for a neighbourhood B of i; something else) and test it on the worst
   cases you found and on PM(K33)-type towers from FEIB19.
4. One page at the end: the strongest statement about good coordinates you now believe is TRUE for all Boolean
   functions and could be proved, with the first lemma you would attack.

Rules for this brief: 2 threads, nice 10, under 3 GiB a process; folder under 200 MB. Proofs go in PROOFS.md with
every step written; mark each statement PROVED, CHECKED NUMERICALLY (with the command) or HEURISTIC. RESULTS.md as
you go; REPORT.md at the end.
