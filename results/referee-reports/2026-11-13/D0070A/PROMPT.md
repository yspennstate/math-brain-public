Open problem D0070. Source: G. R. Grimmett and Z. Li, "Self-avoiding walks and connective constants" (survey, 2017,
arXiv:1704.05884), Question 2.3, Section 2.2, PDF p. 10, and Question 3.4: for Delta >= 3, what is the sharp lower bound
mu_min(Delta) = inf{mu(G) : G infinite, connected, transitive, simple, of degree Delta} for the connective constant? How does
mu_min(Delta) behave as Delta -> infinity? Question 3.4 asks whether mu_min(3) is the golden mean (1+sqrt5)/2. Read the source
for the exact class (transitive vs quasi-transitive, Cayley graphs), the known lower bound mu(G) >= sqrt(Delta-1) or similar,
and the families where the golden-mean conjecture is confirmed.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1704.05884 into sources/ (plain text only) and read Sections 2-3 exactly. Search for later
   work: Grimmett-Li "Cubic graphs and the golden mean" (Discrete Math. 2020), "Connective constants and height functions
   for Cayley graphs", "Bounds on connective constants of regular graphs" (Combinatorica 2015, mu >= sqrt(Delta-1)),
   Georgakopoulos-Wendland on two-ended graphs, Panagiotis, Lindorfer ("A general bridge theorem for self-avoiding walks",
   "connective constant of transitive graphs is at least ..."), Gilch-Muller on free products, Grimmett-Holroyd-Peres,
   Martineau, and 2017-2026 work on lower bounds for connective constants of transitive graphs. If it is answered in print,
   give the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the gap. State the best known lower bound for general transitive Delta-regular graphs and why the golden mean
   would be sharp for Delta = 3 (the ladder / the Cayley graph of Z x Z_2 with the right generators, or the hexagonal-type
   examples): give the extremal examples explicitly with their connective constants.
3. Prove what you can, with complete proofs: improve the general lower bound for Delta = 3 or for all Delta (for instance
   via an injection of self-avoiding walks built from a height function, a bridge decomposition, or a cycle-space argument),
   confirm the golden-mean bound for a new class of cubic transitive graphs (one-ended amenable, graphs with a graph height
   function, planar cubic transitive graphs), or determine the asymptotics of mu_min(Delta) (is mu_min(Delta) = Delta - O(1)?
   compare with explicit transitive graphs of small mu, e.g. products of cliques and lines).
4. Compute (evidence only). Enumerate self-avoiding walks on small cubic and quartic vertex-transitive graphs and their
   infinite covers (ladders, prisms, Cayley graphs of small groups extended by Z) to estimate connective constants, and look
   for any cubic transitive graph with mu below the golden mean.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
