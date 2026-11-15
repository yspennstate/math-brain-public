Open problem G0010. Source: a 2026 paper by Christoph, Morawski and Wigderson on the critical probability of finite graphs
(find it on arXiv by authors and title words "percolation", "finite graphs", "spectral radius"; record the arXiv number),
Question 5.2, Section 5, PDF p. 19. Setting: Bernoulli bond percolation G_p on a finite graph G with maximum degree Delta(G)
and spectral radius lambda(G), with p <= (1 - eps)/lambda(G). The source's Theorem 1.4: a.a.s. the largest component has size
O(sqrt(|G| Delta(G)) log|G| / lambda(G)); optimal when lambda(G) >> sqrt|G| (e.g. K_{s,s^3}) but not in all regimes (for
lambda(G) = Delta(G) and G connected the truth is O(log|G|)). Question 5.2: for given Delta and lambda, what is the tight upper
bound for the typical size of the largest component of G_p when p <= (1 - eps)/lambda(G)? The source singles out the
near-regular case Delta(G) <= (1 + delta) lambda(G).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read Theorem 1.4, its proof and Section 5 exactly.
   Search for related and later work: Alon-Benjamini-Stacey (percolation on finite graphs and isoperimetry), Bollobas-Borgs-
   Chayes-Riordan (percolation on dense graph sequences, spectral threshold 1/lambda), Krivelevich-Sudakov, Frieze-Krivelevich-
   Martin (giant in expanders), Nachmias-Peres, Hutchcroft-Easo ("supercritical percolation on finite transitive graphs"),
   Diskin-Krivelevich (percolation in high-dimensional product graphs, "isoperimetric" and spectral bounds), Bhamidi-van der
   Hofstad, and 2025-2026 work citing the source. If Question 5.2 is answered in print, give the exact reference and theorem and
   stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the gap. Explain where the sqrt(|G| Delta) factor comes from in the proof (a path-counting / Perron-vector
   argument) and construct the extremal families: for each regime of (Delta, lambda, n), the best known lower-bound
   constructions (complete bipartite K_{s,t}, stars glued to expanders, disjoint unions, a dense core plus pendant trees).
3. Prove what you can, with complete proofs: a tight bound in the near-regular case Delta <= (1 + delta) lambda (for instance
   O_{eps,delta}(log n), or a bound of the form f(delta) log n, or a counterexample showing polynomial components are possible
   when Delta = (1 + delta) lambda); or matching upper and lower bounds in a new range of (Delta, lambda); or an improvement of
   the log factor. State exactly the regime covered.
4. Compute (evidence only). Simulate percolation at p = (1 - eps)/lambda on candidate extremal graphs (bipartite, star-plus-
   expander, random graphs with planted high-degree vertices) for n up to about 10^6 and fit the largest-component size.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
