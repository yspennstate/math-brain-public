Open problem E0053. Source: A. S. Bandeira, "Ten lectures and forty-two open problems in the mathematics of data science"
(2015/2016 notes), Open Problem 8.5 / Conjecture 8.5, PDF p. 117: Let G be a uniformly random d-regular graph on n vertices.
Prove or disprove that for every d, as n grows, (1/n)(MaxBis(G) + MinBis(G)) = d/2 + o(1). The source notes it holds up to
o(sqrt(d)) terms by Dembo-Montanari-Sen (arXiv:1503.03923). It is attributed to Zdeborova-Boettcher.

Do this, in order, saving as you go:
1. Literature first. Read the source statement exactly (download it into sources/). Search for later work: Zdeborova-Boettcher
   2010 (J. Stat. Mech., "A conjecture on the maximum cut and bisection width in random regular graphs"), Dembo-Montanari-Sen,
   Sen 2018 (Optimization on sparse random hypergraphs), Jagannath-Sen, Gamarnik-Li, Lyons (factors of iid, cuts in regular
   trees), Bhattacharya et al., Coja-Oghlan et al., Diaz-Serna-Wormald bounds for d=3,4, numerical studies of max-cut and
   bisection width for cubic graphs (e.g. Boettcher-Percus extremal optimisation; Gao-?), any 2016-2026 paper that proves or
   refutes the conjecture for small d (d=3 in particular). If it is settled in print (proved, or refuted for some d), say so
   with exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Think about d=3 and d=4 specifically: known rigorous upper and lower bounds on MaxBis/n and MinBis/n (e.g. MinBis/n <= 1/6
   for cubic, MaxBis bounds by Diaz-Do-Serna-Wormald). Check whether known rigorous bounds already contradict d/2 for some d
   (e.g. if rigorous upper bound on MaxBis plus rigorous upper bound on MinBis is below d/2, or lower bounds sum above d/2).
   That would be a COUNTEREXAMPLE with a rigorous proof - check this very carefully, with exact constants from the papers.
3. Numerics. Estimate MaxBis/n and MinBis/n for d=3,4,5 at n up to as large as you can (exact for small n by ILP/branch and
   bound if available; heuristics such as extremal optimisation / simulated annealing with careful extrapolation in n for large
   n). Report whether the sum deviates from d/2 beyond error bars, with honest uncertainty.
4. Any rigorous partial result you can prove (e.g. one inequality direction for all d, or a reduction) - write it with proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, what was proved (with proofs), the numerics with method and error bars, and the literature found with exact
references. Keep LOG.md as you go. Code in code/, data in data/. Work only in this directory. At most 4 threads, under 4 GB,
nice 10. No publication anywhere, no pushes.
