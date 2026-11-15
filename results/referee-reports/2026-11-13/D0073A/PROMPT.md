Open problem D0073. Source: G. R. Grimmett and Z. Li, "Self-avoiding walks and connective constants" (survey, 2017,
arXiv:1704.05884), Question 4.6, Section 4.2, PDF p. 17: let G be an infinite connected transitive simple graph, Gamma a
transitive group of automorphisms, and A a non-trivial (not necessarily normal) subgroup of Gamma acting freely on the vertex
set such that the quotient graph G_A is transitive. Is mu(G_A) < mu(G)? An affirmative answer is known under the extra
condition that some cycle length l occurs in G_A but not in G. For normal subgroups the strict inequality is a theorem of
Grimmett-Li ("Strict inequalities for connective constants of transitive graphs", SIAM J. Discrete Math. 28 (2014)) under
their conditions. Read the source for the exact hypotheses (quotient graph definition: is G_A simple, does it have loops or
multiple edges; which group must act transitively on G_A).

Do this, in order, saving as you go:
1. Literature first. Get arXiv:1704.05884 into sources/ (plain text only) and read Section 4 exactly, then the strict
   inequality paper (arXiv:1310.? search "Strict inequalities for connective constants of transitive graphs") and its proofs
   for normal and non-normal quotients. Search later work: Grimmett-Li "Locality of connective constants", "Connective
   constants and height functions for Cayley graphs", Lindorfer, Panagiotis, Martineau-Severo ("strict monotonicity of
   percolation thresholds under covering maps", Ann. Probab. 2019 - the percolation analogue of this question for non-normal
   quotients!), Grimmett-Li "Cubic graphs and the golden mean", and 2017-2026 work. If Question 4.6 is answered in print, give
   the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Reduce. Explain the normal-subgroup proof (lifting walks, inserting a pattern that closes in G_A but not in G, the
   Kesten-pattern / unfolding argument) and exactly where normality is used. Compare with Martineau-Severo's method for p_c
   under covering maps, which handles non-normal quotients via a different route; decide whether that route transfers to the
   connective constant.
3. Prove what you can, with complete proofs: the strict inequality for all non-normal free quotients; or for a new class
   (quotients with a quasi-transitive lift, Cayley graphs with A a subgroup of the group itself, amenable G, G with a graph
   height function); or a counterexample with mu(G_A) = mu(G).
4. Compute (evidence only). For small explicit examples (quotients of the square lattice, the hexagonal lattice, trees, and
   Cayley graphs of small groups by non-normal subgroups) enumerate self-avoiding walks on G and G_A and compare growth.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
