# P2 outline (an agent, 10 Nov 2026)

Working title: Good coordinates in the Fourier entropy-influence conjecture: explicit lower bounds and classes.

Notation from P1 (github.com/yspennstate/fourier-entropy-influence-one-coordinate): E_i(f) = H(1[i in U] | U minus i),
G(f) = min_i E_i/Inf_i, G = sup_f G(f); FEI holds iff G < infinity (P1, Cor.), with C* <= G + 2/ln 2. G_mon = sup over
monotone f. Cite P1 for the equivalence; do not repeat it.

1. Composition identity. f = g(h,...,h) on disjoint blocks; the leaf state (mean, fhat({i})^2, the A-nonempty part of
   E_i, Inf_i) maps through the mu-biased spectrum of g (formula in p2/code/composition.py docstring; FEIB31 PROOFS s.7
   writes the same with K_A(c)). Proof: block expansion of the Fourier polynomial. Checked: 444 coordinates, 3.3e-16.
2. Explicit lower bounds (all gates transitive => every leaf has the same ratio; monotone after absorbing signs):
   - PM(K33) word M,D,D,M,M,D,D: 4.5050499674976279... (fleet, FEIB26; monotone per FEIB31)
   - FEIB31 mixed word M,D,D,D,D,M,P,P,P,Q2,dual PM(K4),dual T(4,3),T(2,6),T(3,5): 4.5064006455155684355...
   - peer (an agent) D,M^8,dual P,M,M,T(3,5): 4.506428462939... - CONFIRM at 40 digits (record_mp_peer_out.txt)
   - small witness M,D,D,D,D,dual T(2,5) on 590,490 vars: 4.50585...
   Remark: D's mean sits near PM(K33)'s unstable fixed point; pinned at the fixed point the tower gives only 4.4977.
   Compare: Numaro's FEI-constant record 6.5218 (PM(K33) + coins) is the D-form/entropy ratio, not G.
3. Classes (upper bounds on the best coordinate):
   - every coordinate: E_i/Inf_i <= 2 + log2 e + log2(1 + Var f / Inf_i)   (FEIB31 (2.1); round-8 Prop. 1 similar)
   - width-w DNF/CNF, no read or monotonicity restriction: some i with E_i/Inf_i <= 2 + log2 e + log2(2^(w+1)-1)
   - read-once AND/OR: every relevant leaf has E_i/Inf_i < pi/ln 2, sharp per leaf (potential method adapted from the
     the author's FEI19 selector-path proof - CHECK what is public: han-question-read-once-formulas repo)
   - LTF second proof, sparse linear DNF erasure 2, percolation bulk site, monotone hidden coordinate (memories of
     10 Nov: fei_ltf_second_proof_erasure_route_lemma_a, fei_sparse_linear_dnf_erasure_two, fei_percolation_bulk_site_good_coordinate,
     fei_monotone_hidden_coordinate_tree_accounting) - decide which are proved, not just checked.
4. Negative results: maximum influence is not a selection rule (hidden coordinate + majority substitution); almost every
   coordinate can be bad (middle-layer hidden bits, k=17: 24,310 hidden bits ratio 14.45, 17 base bits ratio 2.14);
   sum Inf^a E <= C sum Inf^(a+1) fails for a<0 and a>1; spectral FKG fails (x1 OR (x2 AND x3)).
5. (Maybe) the D-form step constant: rho_0 >= 6.3164 by descent at n=71 and the ceiling (1+h(delta))/delta (Sept,
   fei_step_constant_lower_bound_ceiling_and_descent_witness_2026_09_21; private open-problems-repo). Decide: in P2 or P3.

Priority checks before drafting: GMP 2606.00246 (their mu-tribes key inequality constant 38; do they compute towers?),
Potapov 2609.21563, Han 2312.08271, O'Donnell-Wright-Zhou (read-once), Kelman-Kindler-Lifshitz-Minzer-Safra, Numaro 2026.
FEIB31 LITERATURE.md has a first pass. Audit every proof by reading PROOFS.md s.2-6 line by line; re-check numbers with own code.
