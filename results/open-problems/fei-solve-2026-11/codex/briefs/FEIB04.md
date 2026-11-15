disk: small

Read ~/fei_solve_agent/NOTES.md first.

Task: the cancellation conjecture ("Gamma-conjecture"):
  Gamma(f) = sum_S fhat(S)^2 log2( E_z|c_S(z)| / |E_z c_S(z)| ) <= C I(f) for every Boolean f,
where c_S(z) is the S-coefficient of f restricted to the subcube with the coordinates outside S fixed to z (so
fhat(S) = E_z c_S(z)). FEI implies it (Gamma <= B/2 <= H/2). Together with the containment conjecture A <= C I it
is equivalent to FEI (Proposition 4). For |S| = 1 the terms are fhat(i)^2 log(I_i/|fhat(i)|) <= I_i/ (e ln 2).
1. Try to prove it. Things to test, each pushed to a proof or to the exact failing step with a witness:
   (a) c_S(z) as a martingale in z (expose the outside coordinates one at a time): the L1 norm E|c| grows from
       |fhat(S)| to abs1(S); write log(abs1/|fhat|) as a sum of increments and look for a charge against influences;
   (b) the terms of S are tied to terms of supersets: abs1(S) <= sum over minimal patterns ...; find an inequality of
       the form  sum_S mu(S) log(abs1(S)/|fhat(S)|) <= sum_U mu(U) w(U) with w(U) = O(|U|) by a Gibbs/coding
       argument (a sub-probability nu on sets with nu(S) >= mu(S)^{1/2} abs1(S)^{...} would do it; find the right one);
   (c) hypercontractivity applied to the function z -> c_S(z) (values in 2^{1-|S|} Z, bounded by 1);
   (d) monotone f, unate f, and f whose derivatives D_S f have constant sign (then Gamma = 0): characterise the class
       with Gamma = 0 and say which known FEI classes it contains.
2. Try to break it: exhaustive n <= 4 gives sup Gamma/I = 0.375 and balanced sup Gamma/(I-1) = 0.517. Search
   6 <= n <= 20 (hill-climb, majority-like, bent-like, random low-degree polynomial thresholds, compositions) for
   families where Gamma/I or balanced Gamma/(I-1) grows. Majority has Gamma of order sqrt(n) ~ I; get its constant.
   Does Gamma obey the composition law Gamma(f o g) = Gamma(f) + I(f) Gamma(g) for balanced g? Prove or refute.
3. Report suprema by n with witnesses.
Deliverables: PROOFS.md, scripts with outputs, RESULTS.md, REPORT.md with one verdict line per idea.
Memory: each process under 3 GiB, at most 2 threads, nice 10.
