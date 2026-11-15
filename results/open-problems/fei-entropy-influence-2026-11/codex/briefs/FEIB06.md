disk: small

Read ~/fei_solve_agent/NOTES.md first.

Task: a potential for the recursion of Lemma 3. For real g and coordinate i, a = E_i g, d = D_i g:
  B(g) = B(a) + B(d) + J_i(g),  J_i(g) = sum_{S not containing i} ahat(S)^2 log2(1 + up_d(S)/up_a(S)).
Unrolling over all coordinates in an order pi writes B(f) as a sum of J terms over the binary tree of (E, D) choices,
while I(f) is the sum of ||D_i g||^2 over the same tree. Paying each J by its own ||d||^2 is impossible (NOTES.md,
dead routes). Wanted: a potential Phi on real functions (degree-2 homogeneous or with a controlled normalisation) and
a rule for choosing i such that
   J_i(g) <= C ||D_i g||^2 + Phi(g) - Phi(E_i g) - Phi(D_i g)        (*)
for every g that arises as an iterated (E, D) image of a Boolean function, with Phi(f) <= C' I(f) at the root and
Phi >= 0 at the leaves. Then B <= (C + C') I and FEI follows by Theorem 1.
1. Census. For all Boolean f on n <= 4 variables (and a large sample on 5, 6) enumerate every node g of the (E, D)
   tree for every order, with features: ||g||^2, ||d||^2, J_i(g), level profile of g, entropy of the normalised
   spectrum of g, B(g), A(g), sum_S ghat(S)^2 log(1/up_g(S)), min and max of up ratios. Save as compact numpy files.
2. Linear programs. For feature families Phi = sum of c_k * feature_k (include H(g), A(g), B(g) themselves, the
   normalisation entropy ||g||^2 log(1/||g||^2), level-weighted versions) solve for the smallest C such that (*)
   holds at every node for the best coordinate (min over i) and for every coordinate (max over i). Report C by n and
   by family; a family is interesting only if C does not grow from n = 3 to 4 to 5 to 6.
3. Whatever the LP suggests, try to prove (*) for the simplest winning Phi, or find the node that kills it.
   Note the trivial solutions: Phi = -B telescopes to nothing, Phi = H reproduces the dead H induction; say so
   explicitly when the LP returns one of them and exclude it.
Deliverables: scripts with outputs, RESULTS.md (C by n and family, the killing nodes), PROOFS.md if anything is
proved, REPORT.md. Memory: each process under 3 GiB, at most 2 threads, nice 10; size the census before allocating.
