# Open problems E0094 and E0095: which generator or edge to add to speed up a random walk

Source: P. Diaconis, "The Markov chain Monte Carlo revolution" / "Some things we've learned (about MCMC)" (2013), Questions 3
and 4, PDF p. 9. Check the literature first (Diaconis-Saloff-Coste comparison, Hildebrand, Wilson on the "transpose and
cycle" walk, Helfgott-Seress-Zuk on random generators of S_n, Chung's and Friedman's work on adding matchings or edges,
Mosk-Aoyama on spectral-gap maximisation by edge addition); if a question is already settled in print, say where and stop.

E0094. G = S_n, n odd, S = {tau = (1,2), c = (1,2,...,n)} with inverses (lazy walk if needed). Order n^3 log n steps are
necessary and sufficient. QUESTION: is there sigma in S_n such that the walk on S + {sigma, sigma^{-1}} mixes appreciably
faster (by a power of n)? What is the best possible order over all sigma?

E0095. Connected d-regular graph on n vertices (n even). Which edge, or which perfect matching, should be added to best
speed up the nearest-neighbour walk (spectral gap or total-variation mixing time)?

TASK, in order:
1. E0094 lower bound: the best order any single added sigma can give (entropy / diameter / conductance argument; note a
   3-generator Cayley graph on S_n has diameter at least about n log n / log 5). State it as a theorem with proof.
2. E0094 upper bound: find an explicit sigma (a power of c, the perfect shuffle, a reversal, a product of disjoint
   transpositions, ...) and PROVE a mixing bound that beats n^3 log n by a power of n (comparison with a known fast walk
   is the natural route). Support it with exact or Monte Carlo total-variation curves for n = 5..11 (exact on S_n up to 9 or
   10 is feasible; keep memory under 4 GB).
3. E0095: settle the cycle C_n exactly (best single edge for the gap, with proof; best perfect matching up to constants),
   then any structural theorem for general d-regular graphs (e.g. the optimal edge joins vertices extremal for the Fiedler
   vector, or a counterexample to that), with exact computation on all small regular graphs that fit.
Keep peak memory under 4 GB; no worker pools larger than 4 threads.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.
