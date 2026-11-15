disk: small

Read ~/fei_solve_agent/NOTES.md first.

Task: the coding route to B <= C I (Lemma 2 and its kernel generalisation). For any kernel r(U,S) >= 0 with
sum_{S subset U} r(U,S) = 1 for every U (a random way of shrinking a set), Gibbs' inequality gives
   B <= E_{S~mu} log2( 1 / E_{U~mu}[ r(U,S) | U contains S ] ).
The kernel may depend on f. The product kernel r = prod_{i in U-S} lam_i prod_{i in S} (1 - lam_i) gives
   B <= sum_i I_i log(1/(1-lam_i)) + E_S log 1/E[ prod_{i in U-S} lam_i | U contains S ].
1. Recover the state of the art through this route: prove B <= C (I + sum_i I_i log(1/I_i)) with an explicit choice
   of lam_i (or show the product kernel cannot do it and say what it does give). Then Theorem 1 gives
   H <= 2B + 2I: compare with the known bound of that shape (Han, arXiv 2312.08271; KKLMS 2020).
2. Adaptive kernels: r may shrink U along a decision process that looks at U (for example: keep the coordinates of U
   in an f-dependent order and stop at a stopping time; or keep U intersected with a random restriction's live set).
   For which kernels is the right side bounded by C I for tribes, majority, address, AND, the 5-variable extremals
   0x0000000e and 0x008eeeee (bit x set means f(x) = -1) and compositions? Compute the right side exactly for
   candidate kernels on all 4-variable functions and report the best universal kernel family you can find and its
   worst ratio to I.
3. The optimal kernel is r = indicator of S = U (right side = B). The useful kernels are those for which the right
   side can be bounded by an argument that does not already assume FEI: say for each kernel what such an argument
   would be, and push the most promising one as far as a theorem for a class not yet known (monotone functions,
   functions with all influences below I/n^(1/2), or DNF of width w).
Deliverables: PROOFS.md, scripts with outputs, RESULTS.md, REPORT.md with a verdict line per kernel family.
Memory: each process under 3 GiB, at most 2 threads, nice 10.
