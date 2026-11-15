# Open problem F0096: Hamiltonicity of G_{n,cn;3} for c >= 3/2

G_{n,m;3} is uniform over graphs on [n] with m edges and minimum degree at least 3. L_c = lim Pr(G_{n,cn;3} is
Hamiltonian). Conjecture (Frieze, ICM 2014 slides pp. 166-170): L_c = 1 for every c >= 3/2. Known as stated there:
c = 3/2 (random cubic graph, Robinson-Wormald 1984/1994), c >= 128 (Bollobas-Cooper-Fenner-Frieze 2000), c >= 10
(Frieze 2012), and c >= 3 conditional on a numerical ODE solution.

Check the literature 2014-2026 FIRST: Anastos and Frieze, "Hamilton cycles in random graphs with minimum degree at least
3: an improved analysis" (Random Structures & Algorithms, about 2020; check the exact constant they reach, I believe
about 2.67), any later paper by Anastos, Frieze, Cooper or others, and arXiv searches on "minimum degree three"
"Hamilton cycle" "random graph" and "2-core / 3-core Hamiltonicity". State exactly what is proved in print and for which c.
If L_c = 1 is proved in print for every c >= 3/2, report that with the reference and stop.

Prior work here (unreviewed, 8 Sep 2026 and a partial Codex pass 11-12 Oct): G_{n,cn;3} is contiguous to (or can be
reduced to) the configuration model with degrees iid Poisson(lambda) conditioned on >= 3, with lambda fixed by the mean 2c;
at c = 3/2 the degrees are all 3 and the graph is a random cubic graph. The natural open window is between 3/2 and the
best constant in print.

TASK, in order:
1. Simulation first: for c in {1.5, 1.55, 1.6, 1.75, 2, 2.25, 2.5}, sample G_{n,cn;3} (or the truncated-Poisson
   configuration model, with a check that they agree) for n up to 10^5 and test Hamiltonicity with a good heuristic
   (e.g. a Posa rotation-extension solver, or Concorde/LKH if available locally, no downloads of binaries that need
   install privileges). Report the fraction Hamiltonian and any failure structure (for instance a vertex with three
   neighbours of degree 3 sharing a common structure, small obstructions).
2. The most promising route to an unconditional new range: the window c in [3/2, 3/2 + epsilon]. There the degree
   sequence is mostly 3s with a vanishing fraction of higher degrees as epsilon -> 0. Try small-subgraph conditioning
   (Robinson-Wormald, Janson) for the number of Hamilton cycles in the configuration model with such a degree sequence:
   compute the first and second moments, the cycle-count corrections, and check whether E[H^2]/E[H]^2 -> exp(sum
   lambda_k delta_k^2). Unbounded maximum degree (about log n / log log n) must be handled, e.g. by truncation plus a
   separate argument for the few high-degree vertices.
3. Alternatively improve the constant in print by a sharper analysis of the Anastos-Frieze algorithm, if the paper's
   bottleneck is identifiable.
4. Prove what you can; state precisely what remains. A result "L_c = 1 for all c in [3/2, 3/2 + epsilon_0] with an
   explicit epsilon_0" would be new progress if not in print.
Keep peak memory under 4 GB; no worker pools larger than 4 threads.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.
