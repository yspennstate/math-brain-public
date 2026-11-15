Open problem D0028. Source: a 2025 paper on stationary measures of kinetically constrained models / facilitated spin models
(find it on arXiv: search 2025 papers with "kinetically constrained" and "stationary measures" or "invariant measures" and
"bootstrap percolation", e.g. by Hartarsky, Toninelli, Marêché, Shapira, Chleboun, Faggionato, Martinelli, Blondel, or their
students; confirm it by its Theorem 2.13 for the d-dimensional East model and its Conjecture 3), Conjecture 3, Section 2,
PDF p. 8: let mu be a stationary measure of a kinetically constrained model (KCM). Then there is a probability measure mu* on
the set E of bootstrap-percolation-stable configurations such that mu = integral over E of pi_beta d mu*(beta), where pi_beta
is the product measure pi conditioned on {BP(eta) = beta}. The source proves it for the d-dimensional East model and in d = 1,
or for translation-invariant mu in general. Read the source for the exact definitions (update families, BP map, conditioning
on a possibly null event, the class of KCMs and of stationary measures, finite versus infinite volume).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read Sections 1-3 exactly, including the proofs of
   the East and d = 1 / translation-invariant cases. Search for later or related work: Hartarsky-Toninelli "Kinetically
   constrained models" (book/survey), Shapira, Blondel-Cancrini-Martinelli-Roberto-Toninelli (FA-1f relaxation), Mountford
   (FA-1f stationary measures), Cancrini-Martinelli-Roberto-Toninelli, "ergodicity of KCMs", "invariant measures of the
   Fredrickson-Andersen model", and 2025-2026 papers citing the source. If Conjecture 3 is proved in print in general, give the
   exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Reduce. Explain why the East and d = 1 cases work (orientation, a renewal / last-empty-site argument, the role of
   translation invariance) and which step fails for a general update family in d >= 2 (for instance FA-2f on Z^2, or the
   North-East model). Identify the minimal missing lemma.
3. Prove what you can, with complete proofs: the conjecture for a new class (FA-1f on Z^d for every d, all supercritical
   update families, all KCMs on trees or on Z x {finite}, models whose BP-stable configurations have a finite description),
   or for stationary measures with an extra hypothesis (finite range of dependence, a spatial-mixing condition, measures
   absolutely continuous with respect to pi on finite boxes), or a counterexample to the conjecture as literally stated.
   Note: a related result (FA-1f on Z, q > 1/2: convergence to pi from any law with an infected site) is in
   claim notes we hold; use it only if you re-derive what you need.
4. Compute (evidence only). Exact finite-volume stationary measures of KCMs on small tori or boxes with various boundary
   conditions (solve the generator's kernel), and check the decomposition numerically.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
