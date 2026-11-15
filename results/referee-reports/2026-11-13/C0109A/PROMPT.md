Open problem C0109. Source: T. Tao and V. Vu, "From the Littlewood-Offord problem to the circular law: universality of the
spectral distribution of random matrices" (Bull. AMS 46 (2009), arXiv:0810.2994), Section 6, p. 22: determine the optimal
rate n^{-delta} of convergence of the empirical spectral distribution of n^{-1/2} M_n (i.i.d. entries, mean 0, variance 1) to
the circular law under a (2+eps)-th moment assumption, and the exact dependence of delta on eps. Read the source for the exact
wording, the metric in which the rate is measured (Kolmogorov-type distance on test functions, Wasserstein, or discrepancy on
discs), and what rate was known then.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:0810.2994 into sources/ (plain text only) and read Section 6 exactly. Search for rates of
   convergence to the circular law: Gotze-Tikhomirov ("The circular law for random matrices", Ann. Probab. 2010, rate
   statements), Tao-Vu "Random matrices: universality of local spectral statistics of non-Hermitian matrices", Bourgade-Yau-
   Yin (local circular law, rates under finite moments), Alt-Erdos-Kruger (local inhomogeneous circular law), Jalowy
   ("Rate of convergence for products of random matrices", "rates of convergence to the circular law", 2021-2023, optimal
   n^{-1/2} type rates in Kolmogorov distance), Gotze-Jalowy ("Rate of convergence to the circular law via smoothing
   inequalities", Ann. Probab.?), Cipolloni-Erdos-Schroder (CLT for linear statistics, fluctuations of order 1/n), Tikhomirov
   on heavy-ish tails, and 2009-2026 work. Determine which (moment assumption, metric, rate) combinations are proved and
   whether the dependence of delta on eps under only 2+eps moments is known and optimal. If the question is answered in print,
   give the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the gap. With only 2+eps moments, the truncation level and the smallest singular value bound limit the rate.
   Derive the rate that truncation at n^{1/2 - c} plus the best known local laws gives, and a lower-bound construction showing
   that some rate loss in eps is unavoidable (heavy-tailed entries create outlier eigenvalues; estimate their effect on the
   empirical measure in the chosen metric).
3. Prove what you can, with complete proofs: an explicit rate n^{-delta(eps)} under 2+eps moments in a stated metric; a
   matching lower bound for some metric and entry law; or the exact delta(eps) in one metric.
4. Compute (evidence only). Simulate n up to a few thousand with entries having exactly 2+eps moments (symmetric Pareto-type
   tails) for several eps, measure the distance to the circular law in the chosen metric, and fit delta(eps).
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
