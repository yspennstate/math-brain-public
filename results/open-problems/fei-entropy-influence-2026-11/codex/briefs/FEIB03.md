disk: small

Read ~/fei_solve_agent/NOTES.md first.

Task: the containment conjecture ("A-conjecture"):  A(f) = sum_S fhat(S)^2 log2(1/up(S)) <= C I(f) for every Boolean f,
where up(S) = sum_{U contains S} fhat(U)^2 = E[(D_S f)^2]. In words: a spectral sample S is contained in an
independent spectral sample with probability at least 2^{-C|S|}, on log-average. FEI implies it (A <= H). It is
weaker than FEI and may be provable. Known for free: A <= H/2 + I - Var (Theorem 1 restated), and for |S| = 1 the
terms are fhat(i)^2 log(1/I_i) <= I_i (since fhat(i)^2 <= I_i^2).
1. Try to prove it. Ideas to test, in this order, each either pushed to a proof, or to the exact step that fails with
   the function that breaks it:
   (a) generalized-influence inequalities of KKL/Talagrand type for I_S = up(S) (the KKLMS 2020 paper proves
       level-d inequalities for exactly these quantities; reconstruct what you can and see what they give for A);
   (b) a recursion on coordinates: with a = E_i g, d = D_i g one has up_g(S) = up_a(S) + up_d(S), up_g(S+i) = up_d(S);
       find a potential that pays the normalisation entropy; note the plain version is the dead H induction;
   (c) positive association: if Pr[U contains S] >= prod_{i in S} I_i held one would get sum I_i log(1/I_i); find
       what replaces it (the spectral sample is not positively associated in general; measure how it fails);
   (d) a second-moment route through Pr[S subset U] = E_U ||E[f | x_U]||^2.
2. Try to break it. Search for families where A/I grows: exhaustive on n <= 4 (sup A/I = 1.9375, balanced sup
   A/(I-1) = 4), hill-climb and structured families on 6 <= n <= 20 (tribes, recursive majority, address, iterated
   compositions, the record family "perfect matching of K_{3,3} with coins", random DNF, bent-like). A balanced
   family with A/(I-1) growing in n would be a real finding; triple-check it with exact arithmetic before reporting.
3. Report sup A/I and balanced sup A/(I-1) by n with witnesses, and whether composition makes A/(I-1) a constant
   sequence (it should: A(f o g) = A(f) + I(f) A(g) for balanced g? prove or refute this law for A).
Deliverables: PROOFS.md, scripts with outputs, RESULTS.md, REPORT.md with one verdict line per idea (a)-(d).
Memory: each process under 3 GiB, at most 2 threads, nice 10.
