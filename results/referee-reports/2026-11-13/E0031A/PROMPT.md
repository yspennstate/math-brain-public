Open problem E0031. Source: S. Chatterjee, "A general method for lower bounds on fluctuations of random variables" (Ann. Probab.
47 (2019); arXiv:1706.04290; check the exact reference and version), list of open problems, item (3), PDF p. 27: a tight lower
bound on the fluctuations (variance) of the Euclidean minimal matching cost of n i.i.d. uniform points in [0,1]^d (state exactly
which matching - bipartite or not, which power of distance, which dimensions - and what "tight" means there, i.e. the order of
the known upper bound).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ as plain text and state item (3) exactly, with page numbers. Search 2017-2026
   work: Chatterjee's own lower-bound method and examples in that paper, Barthe-Bordenave, Goldman-Trevisan, Ambrosio-Stra-
   Trevisan (bipartite matching in d=2), Ledoux, Talagrand matching, Dereich-Scheutzow-Schottstedt, Steele (non-bipartite
   matching is a stabilising Euclidean functional), Penrose-Yukich, Kesten-Lee variance and CLT for Euclidean functionals,
   Cao, Gold, "minimal matching" "variance lower bound", "Euclidean matching" "central limit theorem". If a printed result gives the
   tight order (matching the known upper bound) in the stated setting, give the theorem and page and stop with
   RESOLVED_IN_LITERATURE (or PARTIAL if it covers only some d or some version).
2. Otherwise prove the tight lower bound in as much of the setting as you can (for example non-bipartite matching in d >= 3 via
   stabilisation and a positive-variance argument, or d = 2), with every step checked; state precisely what remains.
3. Compute (evidence only): exact minimum-weight matchings (write a Blossom or use networkx max_weight_matching for small n, or
   an assignment solver for the bipartite case) for n up to a few thousand, many samples, estimate Var and its trend in n.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
