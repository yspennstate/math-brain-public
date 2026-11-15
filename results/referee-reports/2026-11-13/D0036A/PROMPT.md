Open problem D0036. Source: R. C. Bradley, "Basic properties of strong mixing conditions. A survey and some open questions"
(Probability Surveys 2 (2005); arXiv:math/0511078), Question 8, Section 6.5, PDF p. 26: what condition on a spectral density
function is necessary and sufficient for a complex, centred, weakly stationary (CCWS) random sequence to satisfy r*(n) -> 0 as
n -> infinity? Theorem 6.5 of the source characterises the conjunction "r*(1) < 1 and r*(n) -> 0" as the existence of a
continuous positive spectral density; the question is what r*(n) -> 0 alone corresponds to. Here r*(n) is the maximal
correlation between the closed linear spans of {X_k : k in S} and {X_k : k in T} over all S, T with dist(S,T) >= n. Read the
source for the exact definitions and wording.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read Section 6.5 and Theorem 6.5 exactly. Search:
   Bradley's own papers on rho* and spectral density (1983 "Equivalent measures of dependence", 1992 "On the spectral density and
   asymptotic normality of weakly dependent random fields", later notes), Bradley's three-volume "Introduction to Strong Mixing
   Conditions" (2007; the chapters on linear dependence coefficients and spectral density), Helson-Sarason, Sarason
   ("An addendum to Past and future"), Ibragimov-Rozanov, Peller-Khrushchev, Kolmogorov-Rozanov, Miller, Simon "Szego's theorem
   and its probabilistic descendants" (arXiv:1108.0368), and 2005-2026 work. If the question is answered in print (for example a
   characterisation of the form f = |P|^2 g with P a trigonometric polynomial with zeros on the circle and g continuous
   positive), give the theorem and page and stop with RESOLVED_IN_LITERATURE.
2. Understand the gap: what r*(n) -> 0 with r*(1) = 1 allows (zeros of f, absence of a density, finite-dimensional degeneracy,
   e.g. X_k = Y_k - Y_{k-1}), and why Theorem 6.5's proof needs r*(1) < 1.
3. Prove what you can, with complete proofs: a necessary and sufficient condition, or both directions in a large class (f with
   finitely many zeros of finite order, f = |P|^2 g), and an explicit example showing which candidate conditions fail.
4. Compute (evidence only): for candidate spectral densities, compute r*(n) numerically (or its finite-window approximation via
   canonical correlations between spans on S and T inside a large window, with gaps n) and show the decay or its failure.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
