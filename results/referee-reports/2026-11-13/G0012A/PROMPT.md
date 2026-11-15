Open problem G0012. Source: a 2026 paper by Dozier (and possibly coauthors) on a birthday-type problem for non-backtracking
walks (find it on arXiv by author and title words "non-backtracking", "birthday", "simple"; record the arXiv number),
Conjecture 1.5 (Alon-Peres), Section 1, PDF p. 2: for every eps > 0 there is C = C(eps) such that for every graph Gamma on n
vertices with all degrees at least 3, every k > C sqrt(n) and every directed edge delta, the probability that a length-k random
non-backtracking walk starting with delta is simple (visits no vertex twice) is less than eps. The source proves the regular
(fixed-degree) case. Read the source for the exact wording (multigraphs allowed?, simple in vertices or edges, uniform choice
among the non-backtracking continuations, the constant's dependence) and the proof for regular graphs.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read Sections 1-3 and the regular-case proof exactly.
   Search: Alon-Benjamini-Lubetzky-Sodin (non-backtracking walks mix faster), Alon-Peres origin of the conjecture (a talk, a
   problem list, or a paper on "random walks on graphs and the birthday problem"), Barnes-Feige (short random walks on graphs),
   Fitzner-van der Hofstad (non-backtracking walk on Z^d), Lubetzky-Sly cutoff, Angel-Friedman-Hoory (non-backtracking spectrum),
   Kempton, Glover-Kempton, Hermon, and 2026 citers of the source. If the conjecture is proved in print for all graphs with
   minimum degree 3, give the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the gap: write out exactly where regularity is used in the source's proof (the non-backtracking operator being
   doubly stochastic, the uniform stationary measure on directed edges, collision counting via the second moment of the number
   of self-intersections) and what breaks for irregular graphs (non-uniform stationary measure, the walk can be trapped on
   high-degree-poor parts; the role of degree 3 versus degree 2 paths).
3. Prove what you can, with complete proofs: the conjecture for bounded degree ratio (max degree / min degree <= D with C
   depending on D), for graphs with min degree 3 and max degree Delta with explicit C(eps, Delta), for the expected number of
   self-intersections, or a counterexample (an irregular family where simple walks of length >> sqrt(n) have probability
   bounded below; think of graphs built from long paths of degree-3 vertices arranged so that the non-backtracking walk is
   nearly deterministic, e.g. ladders, cubic graphs with long girth-like structure, or trees of cycles).
4. Compute (evidence only). Exact probabilities by dynamic programming / Monte Carlo on cubic graphs, irregular graphs with
   degrees 3 and large, and candidate counterexample families, for n up to 10^5, plotting P(simple) against k / sqrt(n).
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
